#!/usr/bin/env python3
"""Check structural invariants of state/pendientes_ledger.md.

Seven invariants (I1-I7), each independent — every violation found is
reported before exiting, not just the first:

  I1  Per-section row count. Real rows counted in tables A/B/C/D must
      match the corresponding row in the "Conteo" table.
  I2  Total. "Total abiertos" must equal the sum of the four real
      per-section counts.
  I3  Closing-note figures. The three figures in "Nota sobre la forma
      de la cola" must match the real row count of the section each
      one names (verificados-esperando-decision -> B, esperan-que-
      alguien-mire-el-repo -> A, "los N del grupo B" -> B). The note
      deliberately excludes group C, so B+A+D != Total by design —
      that is not checked here.
  I4  No row in an open table (A/B/C/D) may have an Estado starting
      with "cerrado"/"cerrada" — closed items belong in the closed
      lists/notes, not the open tables.
  I5  No ID may appear as a row in more than one table, or as a row
      and in a closed list at the same time.
  I6  No table row may have an empty ID (first cell).
  I7  Vencimiento a tres sesiones (D-256 cl. 4). Dos mitades:
      I7a (GATEA) Debe existir la línea "**Sesión vigente:** S<NN>" en
          el encabezado, y toda fila abierta (A/B/C/D) debe llevar en su
          columna Estado exactamente un token "·mov:S<NN>" parseable.
          Campo ausente, duplicado o no parseable = fallo.
      I7b (REPORTA) Toda fila abierta con (sesión vigente − sesión de
          movimiento) >= 3 se lista bajo el encabezado
          "I7b — VENCIDAS". Nunca falla el gate.
      D-256: "El conteo de sesiones sin movimiento no se lleva a mano.
      ledger_check.py ya corre como gate de CI; el vencimiento va ahí
      como invariante, con un campo de última sesión con movimiento por
      fila. El gate dice qué venció; el operador decide qué pasa con lo
      vencido."

Exit 0 only if all gating invariants pass (I1-I6 e I7a). Exit 1
otherwise, printing every invariant that failed and the values
involved. I7b nunca altera el código de salida.
"""
import re
import sys
from pathlib import Path

LEDGER_PATH = Path(__file__).resolve().parent.parent / "pendientes_ledger.md"

TABLE_SECTION_HEADINGS = {
    "A": "## A.",
    "B": "## B.",
    "C": "## C.",
    "D": "## D.",
}

ID_RE = re.compile(r"\b([PU]-\d+[a-z]?)\b")
SEP_CELL_RE = re.compile(r"^:?-+:?$")
CERRADO_RE = re.compile(r"(?i)^cerrad[oa]")
BOLD_COLON_HEADING_RE = re.compile(r"\*\*([^*]+:)\*\*")
SESION_VIGENTE_RE = re.compile(r"^\*\*Sesión vigente:\*\*\s*S(\d+)\s*$", re.MULTILINE)
MOV_TOKEN_RE = re.compile(r"·mov:S(\d+)\b")
MOV_LOOSE_RE = re.compile(r"·\s*mov\s*:\s*\S*")
VENCIMIENTO_SESIONES = 3


def abort(message):
    print(f"ERROR: {message}")
    sys.exit(1)


def load_ledger():
    if not LEDGER_PATH.is_file():
        abort(f"ledger no encontrado en {LEDGER_PATH}")
    return LEDGER_PATH.read_text(encoding="utf-8")


def section_lines(all_lines, heading_prefix):
    start = next((i for i, l in enumerate(all_lines) if l.startswith(heading_prefix)), None)
    if start is None:
        abort(f"sección '{heading_prefix}' no encontrada en el ledger")
    end = len(all_lines)
    for i in range(start + 1, len(all_lines)):
        if all_lines[i].startswith("## "):
            end = i
            break
    return all_lines[start:end]


def parse_table(lines, context):
    """Parse the first markdown table in `lines`. Returns data rows (cell lists),
    header and separator rows excluded."""
    rows = []
    header_seen = False
    sep_seen = False
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            if header_seen:
                break
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if not header_seen:
            header_seen = True
            continue
        if not sep_seen:
            if cells and all(SEP_CELL_RE.match(c) for c in cells):
                sep_seen = True
                continue
            abort(f"tabla en {context} no tiene fila separadora '|---|...' tras el header")
        rows.append(cells)
    if not header_seen:
        abort(f"no se encontró ninguna tabla en {context}")
    return rows


def get_table(all_lines, label):
    heading = TABLE_SECTION_HEADINGS[label]
    return parse_table(section_lines(all_lines, heading), heading)


def get_conteo(all_lines):
    rows = parse_table(section_lines(all_lines, "## Conteo"), "## Conteo")
    counts = {}
    for cells in rows:
        if len(cells) < 2:
            continue
        grupo = cells[0].replace("*", "").strip()
        filas_raw = cells[1].replace("*", "").strip()
        m = re.search(r"\d+", filas_raw)
        if not m:
            continue
        value = int(m.group())
        for label in ("A", "B", "C", "D"):
            if grupo.startswith(label):
                counts[label] = value
                break
        else:
            if grupo.startswith("Total"):
                counts["Total"] = value
    missing = [k for k in ("A", "B", "C", "D", "Total") if k not in counts]
    if missing:
        abort(f"tabla Conteo no declara valor para: {', '.join(missing)}")
    return counts


def get_closed_ids(text):
    """IDs listed under any '**Cerrad...:**' or '**Parquead...:**' heading
    (bullet list or inline comma list), across the whole document. Same
    matching for both: a parked row is reversible (returns to its table
    when its desparqueo condition is met) where a closed row is not, but
    structurally both remove a row from the open-table count the same
    way, so they share this collector. Parenthetical asides (citation
    pointers like '(ver citas ... P-121)') are stripped first so a mere
    cross-reference doesn't get mistaken for closed-list membership. Each
    segment ends at whichever comes first: the next bold-colon heading of
    ANY kind (e.g. '**Huecos...:**', so an unrelated trailing list never
    leaks in), the next '---' divider, or the next '## ' section heading —
    a closed list is always terminated by one of these three in practice,
    but never by the same one twice in a row."""
    headings = list(BOLD_COLON_HEADING_RE.finditer(text))
    closed = {}
    for i, m in enumerate(headings):
        label = m.group(1)
        if not re.match(r"(?i)^(cerrad[oa]s?|parquead[oa]s?)\b", label):
            continue
        start = m.end()
        end = len(text)
        if i + 1 < len(headings):
            end = min(end, headings[i + 1].start())
        hr = text.find("\n---", start)
        if hr != -1:
            end = min(end, hr)
        nxt_section = text.find("\n## ", start)
        if nxt_section != -1:
            end = min(end, nxt_section)
        segment = text[start:end]
        segment_no_parens = re.sub(r"\([^)]*\)", "", segment)
        for pid in ID_RE.findall(segment_no_parens):
            closed.setdefault(pid, []).append(label)
    return closed


def get_sesion_vigente(text):
    """Sesión vigente declarada en el encabezado. Fuente única del reloj de
    D-256: el número de sesión no es derivable del repo, se actualiza a mano
    en cada pasada. Devuelve None si la línea no existe o no es parseable —
    eso es fallo de I7a, no un abort."""
    m = SESION_VIGENTE_RE.search(text)
    return int(m.group(1)) if m else None


def get_nota_figures(text):
    heading = "## Nota sobre la forma de la cola"
    idx = text.find(heading)
    if idx == -1:
        abort(f"sección '{heading}' no encontrada")
    nota = text[idx:]
    figures = {}

    m = re.search(r"(\d+)\s+de\s+\d+\s+ya están verificados y esperan", nota)
    if not m:
        abort("no se encontró en la nota la cifra de 'verificados y esperan (decisión)'")
    figures["verificados_esperando_decision"] = int(m.group(1))

    m = re.search(r"(\d+)\s+esperan que alguien mire el repo", nota)
    if not m:
        abort("no se encontró en la nota la cifra de 'esperan que alguien mire el repo'")
    figures["esperan_mirar_repo"] = int(m.group(1))

    m = re.search(r"[Dd]e los (\d+) del grupo B", nota)
    if not m:
        abort("no se encontró en la nota la cifra 'de los N del grupo B'")
    figures["grupo_b_cifra"] = int(m.group(1))

    return figures


def main():
    text = load_ledger()
    lines = text.splitlines()

    tables = {label: get_table(lines, label) for label in TABLE_SECTION_HEADINGS}
    real_counts = {label: len(rows) for label, rows in tables.items()}
    conteo = get_conteo(lines)
    closed_ids = get_closed_ids(text)
    nota = get_nota_figures(text)

    failures = []

    # I1 — per-section row count vs Conteo table
    for label in ("A", "B", "C", "D"):
        if real_counts[label] != conteo[label]:
            failures.append(
                f"I1 (conteo sección {label}): filas reales={real_counts[label]} "
                f"vs Conteo declarado={conteo[label]}"
            )

    # I2 — Total abiertos vs suma de las cuatro secciones contadas
    sum_real = sum(real_counts[l] for l in ("A", "B", "C", "D"))
    if conteo["Total"] != sum_real:
        failures.append(
            f"I2 (total abiertos): declarado={conteo['Total']} vs suma real de A+B+C+D={sum_real} "
            f"(A={real_counts['A']}, B={real_counts['B']}, C={real_counts['C']}, D={real_counts['D']})"
        )

    # I3 — cifras de la nota de cierre vs conteo de su propia sección
    if nota["verificados_esperando_decision"] != real_counts["B"]:
        failures.append(
            "I3 (nota, verificados-esperando-decisión): "
            f"nota={nota['verificados_esperando_decision']} vs filas reales de B={real_counts['B']}"
        )
    if nota["esperan_mirar_repo"] != real_counts["A"]:
        failures.append(
            "I3 (nota, esperan-que-alguien-mire-el-repo): "
            f"nota={nota['esperan_mirar_repo']} vs filas reales de A={real_counts['A']}"
        )
    if nota["grupo_b_cifra"] != real_counts["B"]:
        failures.append(
            "I3 (nota, 'los N del grupo B'): "
            f"nota={nota['grupo_b_cifra']} vs filas reales de B={real_counts['B']}"
        )

    # I4 — filas cerradas en tabla abierta
    for label, rows in tables.items():
        for cells in rows:
            row_id = cells[0] if cells else ""
            estado = cells[-1] if cells else ""
            if CERRADO_RE.match(estado.strip()):
                failures.append(
                    f"I4 (fila cerrada en tabla abierta {label}): ID={row_id!r} Estado={estado!r}"
                )

    # I5 — IDs duplicados: fila en >1 tabla, o fila + lista de cerrados
    row_locations = {}
    for label, rows in tables.items():
        for cells in rows:
            row_id = cells[0].strip() if cells else ""
            if not row_id:
                continue
            row_locations.setdefault(row_id, []).append(f"tabla {label}")
    for row_id, locations in row_locations.items():
        all_locations = list(locations)
        if row_id in closed_ids:
            all_locations += [f"lista de cerrados ({h})" for h in closed_ids[row_id]]
        if len(all_locations) > 1:
            failures.append(f"I5 (ID duplicado): {row_id} aparece en: {', '.join(all_locations)}")

    # I6 — fila de tabla sin ID
    for label, rows in tables.items():
        for idx, cells in enumerate(rows, start=1):
            if not cells or not cells[0].strip():
                failures.append(f"I6 (fila sin ID): tabla {label}, fila #{idx}, celdas={cells!r}")

    # I7 — vencimiento a tres sesiones (D-256 cl. 4)
    sesion_vigente = get_sesion_vigente(text)
    if sesion_vigente is None:
        failures.append(
            "I7a (sesión vigente): no se encontró la línea "
            "'**Sesión vigente:** S<NN>' en el encabezado del ledger"
        )

    vencidas = []
    for label, rows in tables.items():
        for cells in rows:
            row_id = cells[0].strip() if cells else ""
            estado = cells[-1] if cells else ""
            strict = MOV_TOKEN_RE.findall(estado)
            loose = MOV_LOOSE_RE.findall(estado)
            if len(strict) == 1 and len(loose) == 1:
                if sesion_vigente is not None:
                    transcurridas = sesion_vigente - int(strict[0])
                    if transcurridas >= VENCIMIENTO_SESIONES:
                        vencidas.append((row_id, label, int(strict[0]), transcurridas))
                continue
            if not loose:
                motivo = "campo ausente"
            elif len(loose) > 1:
                motivo = f"campo duplicado ({len(loose)} tokens)"
            else:
                motivo = f"campo no parseable ({loose[0]!r})"
            failures.append(
                f"I7a (movimiento en tabla {label}): ID={row_id!r} {motivo}; "
                f"Estado={estado!r}"
            )

    # I7b — REPORTA, nunca gatea. El gate dice qué venció; el operador decide.
    if vencidas:
        print("I7b — VENCIDAS (D-256 cl. 4, decisión del operador):")
        for row_id, label, mov, transcurridas in sorted(vencidas, key=lambda v: -v[3]):
            print(
                f"  {row_id} (tabla {label}): último movimiento S{mov}, "
                f"{transcurridas} sesiones transcurridas"
            )
        print()

    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        print(f"\n{len(failures)} invariante(s) violada(s).")
        sys.exit(1)

    print("OK: I1-I6 e I7a pasan.")
    print(
        f"Conteo real — A={real_counts['A']} B={real_counts['B']} "
        f"C={real_counts['C']} D={real_counts['D']} Total={sum_real}"
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
