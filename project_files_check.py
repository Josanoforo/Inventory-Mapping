#!/usr/bin/env python3
"""
project_files_check.py — verificador de la capa project files.

LIMITACIÓN DE CAPA, léela antes de cablear nada. CI clona el repo. La capa
project files no está en ese clon. Un job de CI que la busque encuentra un
directorio vacío y reporta verde — el modo de falla que el encabezado de
`ci.yml` prohíbe (R-K) y que D-286 ya negó explícitamente para
`resource_check` y `ledger_path_check`. Este check NO se cablea a CI. No es
preferencia: el insumo no está donde CI mira.

Es herramienta de sesión, patrón de `indice_check.py`: recibe por argumento
la ruta donde está montada la capa project files y corre ahí, contra el
estado real de esa capa. Mide project files declarados en el repo (handoffs,
`ledger_path_check.py`, el propio índice) contra project files que existen
de verdad en la ruta que se le pase.

Dos capas, un problema con una mitad cerrada y una abierta. Cerrada: por lo
de arriba, este check no puede ser gate de CI. Abierta, y es decisión del
operador, no de esta sesión:
  (A) Herramienta de sesión (esto). Funciona hoy, sin infraestructura nueva,
      y encaja con D-281 (el Centinela la invoca en su ronda). No hay gate:
      si nadie corre el botón, nadie mide.
  (B) Manifiesto en el repo: la capa project files declara su inventario en
      un archivo versionado y CI verifica el repo contra ese manifiesto. Gate
      real, pero el manifiesto lo mantiene quien ve las dos capas, así que
      desincronizarse es posible — sería una capa de proceso manual sobre el
      problema, no una solución. Queda escrita aquí como opción, sin
      implementar.

Invariantes:

  PF4 — el índice contra los logs por sesión. Absorbe `indice_check.py`
  (entregado en S41) como módulo: `check()` de ese archivo se llama
  directamente abajo, sin reimplementar J1-J4.
    J1 toda decisión con enunciado en un log por sesión tiene fila en el
       índice
    J2 toda fila del índice apunta a un archivo que existe
    J3 toda decisión citada tiene fila o está declarada como hueco de
       numeración
    J4 detector de copia trunca: si el índice dice que una decisión vive en
       un `Decision_Log_update_sessionNN.md`, esa copia debe contener su
       encabezado

  PF-nuevo — inventario declarado contra inventario real. Todo archivo que
  un `Handoff_sessionNN.md` liste bajo su sección de uploads debe existir en
  la capa, salvo que esté en JUBILADOS. Formato medido contra los 17
  handoffs reales de la capa (S41), no supuesto: la sección se encabeza
  como markdown (`#`-`####`) o como negrita dentro de lista numerada
  (`**3. Uploads del operador a project files (8):**`, `**5. Uploads de
  esta sesión a project files:**` — el patrón de S39/S40), y un handoff
  puede declarar más de una sección de uploads. Los nombres de archivo se
  leen como tokens entre backticks, con o sin extensión `.md` (los handoffs
  citan ambas formas); la existencia se resuelve probando el token tal cual
  y con `.md` añadido. Regla de cero: si la capa tiene handoffs pero
  ninguno produce una sección reconocida, eso es un extractor roto o un
  formato que volvió a cambiar, no una capa sin uploads — se reporta como
  falla en vez de aprobar en silencio sobre cero coincidencias.

  JUBILADOS — documentos retirados de la capa project files, cada uno con su
  razón escrita, declarados en la constante de abajo (mecanismo citado en
  D-280(b) como lo que cerró P-116). Un documento en JUBILADOS no cuenta
  como faltante en PF-nuevo. Alcance deliberado: JUBILADOS NO se consulta
  dentro de PF4 — extenderlo ahí significaría tocar la lógica absorbida de
  `indice_check.py`, que este encargo pide no reimplementar. Si algún día un
  `Decision_Log_update_sessionNN.md` necesita jubilarse, eso es una decisión
  para el operador, no algo que este script decida solo.

  PF1 — cerrado (marca retroactiva en `Handoff_session36`, según el handoff
  de S39). No se mide aquí.
  PF6 — sin efecto: D-279 rechazó volver el índice repo-autoritativo.
  PF2, PF3, PF5 — hueco de spec declarado. Su especificación no aparece en
  ningún archivo legible para esta construcción. Números reservados, no
  inventados; se reporta el hueco en cada corrida en vez de rellenarlo
  (rellenar sería la clase P-153: escribir la restricción sobre la
  superficie que uno imagina, agravado aquí porque el hueco ya está
  declarado).

Regla de construcción: solo lectura. Este check no escribe, no mueve, no
borra nada de la capa project files. Mide y reporta.

Uso:
    python3 project_files_check.py /ruta/a/project_files
    python3 project_files_check.py --help
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import indice_check

# JUBILADOS — documentos de la capa project files retirados a propósito,
# cada uno con su razón escrita. Un documento aquí no cuenta como faltante
# en PF-nuevo (ver alcance en el docstring de arriba). Vacío hoy: no se
# entregó ninguna baja concreta que registrar en la construcción de este
# check. Añadir una entrada es responsabilidad del operador, citando la
# decisión que jubiló el documento — sin razón escrita no es jubilación, es
# pérdida sin registrar.
JUBILADOS = {
    # "Nombre_del_documento.md": "razón — decisión que lo jubiló",
}

HANDOFF_GLOB = "Handoff_session*.md"
# Dos formas reales de encabezar la sección, medidas contra los 17 handoffs de
# la capa (S41). NO es un supuesto: (a) encabezado markdown, (b) negrita dentro
# de una lista numerada, que es la que usan S39 y S40:
#     **3. Uploads del operador a project files (8):**
#     **5. Uploads de esta sesión a project files:**
# Por eso el patrón admite material entre "Uploads" y "a project files" — la
# versión previa exigía la frase contigua bajo `#` y no encontraba ninguna.
UPLOAD_HEADING_RE = re.compile(
    r"^(?:(#{1,4})\s*|\*\*)\s*(?:\d+\.\s*)?[^\n`]{0,40}?uploads?\b[^\n`]{0,60}?\ba\s+project\s*files[^\n]*$",
    re.M | re.I,
)
# Fin de sección: el siguiente encabezado markdown o el siguiente ítem en
# negrita numerada.
SECTION_END_RE = re.compile(r"^(?:#{1,4}\s|\*\*\d+\.\s)", re.M)
# Los handoffs citan indistintamente con extensión y sin ella
# (`Handoff_session40` en S40, `Handoff_session39.md` en S39). Se aceptan las
# dos y la existencia se resuelve probando el token y el token + `.md`.
UPLOAD_TOKEN_RE = re.compile(r"`([A-Za-z0-9_.+-]+)`")


def extract_uploads_sections(text):
    """Todas las secciones de uploads del documento, no solo la primera: un
    handoff puede declarar uploads en más de un lugar (S39 lo hace)."""
    out = []
    for m in UPLOAD_HEADING_RE.finditer(text):
        rest = text[m.end():]
        end_m = SECTION_END_RE.search(rest)
        out.append(rest[:end_m.start()] if end_m else rest)
    return out


def extract_upload_tokens(body):
    tokens = []
    for tok in UPLOAD_TOKEN_RE.findall(body):
        if re.search(r"\s", tok) or "/" in tok:
            continue
        tokens.append(tok)
    return sorted(set(tokens))


def resolve_declared(root: Path, tok: str):
    """El token existe si está tal cual o con `.md` añadido."""
    return (root / tok).exists() or (root / f"{tok}.md").exists()


def check_pf_nuevo(root: Path):
    """PF-nuevo: archivos declarados bajo 'Uploads a project files' en cada
    Handoff_sessionNN.md contra la capa real. Returns (handoffs_con_seccion,
    total_declarado, fallas)."""
    handoffs_con_seccion = []
    total_declarado = 0
    fallas = []
    for f in sorted(root.glob(HANDOFF_GLOB)):
        text = f.read_text(errors="replace")
        bodies = extract_uploads_sections(text)
        if not bodies:
            continue
        handoffs_con_seccion.append(f.name)
        for tok in sorted({t for b in bodies for t in extract_upload_tokens(b)}):
            total_declarado += 1
            if tok in JUBILADOS or tok.replace(".md", "") in JUBILADOS:
                continue
            if not resolve_declared(root, tok):
                fallas.append(
                    f"PF-nuevo (inventario declarado sin archivo real): {f.name} declara "
                    f"'{tok}' bajo 'Uploads a project files' y ese archivo no está en {root}"
                )
    # Regla de cero (R-K). Un extractor que no encuentra NADA en toda la capa
    # está roto o la superficie cambió de formato; en los dos casos tiene que
    # gritar. Aprobar sobre cero es el falso verde que este check existe para
    # no producir. Medido en S41: 2 de 17 handoffs declaran uploads, así que
    # el umbral correcto es "al menos uno", no "todos".
    handoffs_totales = len(list(root.glob(HANDOFF_GLOB)))
    if handoffs_totales and not handoffs_con_seccion:
        fallas.append(
            f"PF-nuevo (extractor mudo): {handoffs_totales} handoffs en {root} y CERO con "
            f"sección de uploads reconocida. O el formato cambió, o el patrón está roto. "
            f"No se aprueba sobre cero"
        )
    return handoffs_con_seccion, total_declarado, fallas


def build_report(root: Path):
    filas, ausentes, definidas, pf4_fallas = indice_check.check(root)
    handoffs_con_seccion, total_declarado, pfnuevo_fallas = check_pf_nuevo(root)
    return {
        "filas": filas,
        "ausentes": ausentes,
        "definidas": definidas,
        "pf4_fallas": pf4_fallas,
        "handoffs_con_seccion": handoffs_con_seccion,
        "total_declarado": total_declarado,
        "pfnuevo_fallas": pfnuevo_fallas,
        "fallas": pf4_fallas + pfnuevo_fallas,
    }


def print_report(root: Path, report: dict):
    print("=" * 78)
    print("PROJECT FILES CHECK")
    print("=" * 78)
    print(f"Capa: {root}")
    print()

    print("-" * 78)
    print("PF4 — índice de decisiones contra logs por sesión (indice_check.py, J1-J4)")
    print("-" * 78)
    print(f"  {len(report['filas'])} filas · {len(report['definidas'])} decisiones con enunciado propio · "
          f"{len(report['ausentes'])} sin texto redactado")
    if report["ausentes"]:
        print("  Pendientes de recuperación: " + ", ".join(f"D-{n}" for n in sorted(report["ausentes"])))
    if report["pf4_fallas"]:
        for f in report["pf4_fallas"]:
            print(f"  FAIL: {f}")
    else:
        print("  OK: J1, J2, J3, J4 pasan.")
    print()

    print("-" * 78)
    print("PF-nuevo — inventario declarado (handoffs) contra inventario real")
    print("-" * 78)
    print(f"  Handoffs con sección 'Uploads a project files': {len(report['handoffs_con_seccion'])}")
    print(f"  Archivos declarados: {report['total_declarado']}")
    if report["pfnuevo_fallas"]:
        for f in report["pfnuevo_fallas"]:
            print(f"  FAIL: {f}")
    else:
        print("  OK: todo archivo declarado existe (o está en JUBILADOS).")
    print()

    print("-" * 78)
    print(f"JUBILADOS — documentos retirados con razón escrita ({len(JUBILADOS)})")
    print("-" * 78)
    if JUBILADOS:
        for name, reason in sorted(JUBILADOS.items()):
            print(f"  {name}: {reason}")
    else:
        print("  (vacío — ninguna baja registrada todavía)")
    print()

    print("-" * 78)
    print("PF1, PF2, PF3, PF5, PF6 — estado declarado, no medido por este script")
    print("-" * 78)
    print("  PF1: cerrado (marca retroactiva en Handoff_session36, según handoff de S39).")
    print("  PF2, PF3, PF5: hueco de spec declarado — no se recuperó su especificación en")
    print("    ningún archivo legible. Números reservados, no inventados.")
    print("  PF6: sin efecto (D-279 rechazó volver el índice repo-autoritativo).")
    print()

    fallas = report["fallas"]
    if fallas:
        print(f"{len(fallas)} violación(es) total (PF4 + PF-nuevo).")
    else:
        print("OK: PF4 y PF-nuevo pasan.")
    return fallas


def main():
    parser = argparse.ArgumentParser(
        prog="project_files_check.py",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "project_files_path",
        type=Path,
        help="Ruta donde está montada la capa project files (fuera del repo). "
             "Solo lectura: el check no escribe, no mueve, no borra nada ahí.",
    )
    args = parser.parse_args()

    root = args.project_files_path
    if not root.exists() or not root.is_dir():
        sys.exit(f"no encuentro un directorio en {root} — pásame la ruta donde está montada "
                  f"la capa project files")

    report = build_report(root)
    fallas = print_report(root, report)
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
