#!/usr/bin/env python3
"""
indice_check.py — el índice de decisiones contra los logs por sesión.

Por qué existe. `Indice_Decisiones.md` declara "se regenera; no se edita a
mano" y no había con qué regenerarlo. En S41 el índice llevaba 23 entradas de
atraso (D-267 a D-289) mientras el System Registry de S40 lo declaraba al día.
El conteo a mano no sostiene esa invariante; este script sí.

LIMITACIÓN DE CAPA, léela antes de cablear nada. El registro autoritativo de
decisiones son los `Decision_Log_update_sessionNN.md`, que viven en project
files, FUERA del árbol del repo (D-233, D-266/R-I). Este script no puede correr
como gate de CI: su insumo no está en el repo que CI clona. Es herramienta de
sesión, se corre apuntándola al directorio donde están montados los project
files. Cablearla a CI la dejaría midiendo un directorio vacío y reportando
verde — el modo de falla que R-K prohíbe.

Uso:
    python3 indice_check.py /ruta/a/project_files
    python3 indice_check.py /ruta/a/project_files --json

Absorbida como módulo por `project_files_check.py` (E-S41-PF): la función
`check()` de abajo es la que ese script importa y llama directamente, sin
reimplementar los cuatro invariantes. `main()` sigue siendo el punto de
entrada para uso standalone y se limita a llamar `check()` y presentar el
resultado — el cuerpo de los invariantes no cambió.

Tres invariantes, independientes:
  J1  Toda decisión con encabezado propio en un log por sesión tiene fila en
      el índice.
  J2  Toda fila del índice apunta a un archivo que existe, salvo las marcadas
      ENUNCIADO AUSENTE.
  J4  DETECTOR DE COPIA TRUNCA. Si una fila apunta a un
      `Decision_Log_update_sessionNN.md`, ese archivo debe contener el
      encabezado de esa decisión. Es el invariante que faltaba: en S41 la
      copia de S39 en project files cortaba en D-278 mientras el archivo
      definitivo llegaba a D-285, y nada lo detectaba — el índice y los
      handoffs traían la glosa, así que la ausencia parecía pérdida.

  J3  Toda decisión citada en cualquier project file tiene fila en el
      índice, o está declarada en la tabla de huecos de numeración. El
      índice es el registro de existencia; el enunciado puede vivir en el
      consolidado (D-001 a D-205) o en el log por sesión (D-206 en
      adelante). No exijas enunciado en log por sesión para todo: eso mide
      una sola capa y reporta el recorte como hallazgo (clase P-153).

Exit 0 si J1-J3 pasan. Exit 1 con la lista de violaciones si no.
"""
import json
import re
import sys
from pathlib import Path

INDICE = "Indice_Decisiones.md"
MARCAS_SIN_TEXTO = ("ENUNCIADO AUSENTE", "ENUNCIADO NO ESCRITO")
DEF_RE = re.compile(r"^#{1,4}\s*D-(\d+)\s*[—–-]\s*(.+)$", re.M)
FILA_RE = re.compile(r"^\| D-(\d+) \| ([^|]*)\| ([^|]*)\| ([^|]*)\|", re.M)
CITA_RE = re.compile(r"\bD-(\d+)\b")


def scan(root: Path):
    idx_path = root / INDICE
    if not idx_path.exists():
        sys.exit(f"no encuentro {INDICE} en {root}")
    idx_text = idx_path.read_text(errors="replace")

    filas, ausentes = {}, set()
    for n, ses, titulo, fuente in FILA_RE.findall(idx_text):
        filas[int(n)] = (ses.strip(), titulo.strip(), fuente.strip())
        if any(m in titulo for m in MARCAS_SIN_TEXTO):
            ausentes.add(int(n))

    definidas, citadas = {}, set()
    for f in sorted(root.glob("*.md")):
        if f.name == INDICE:
            continue
        text = f.read_text(errors="replace")
        if f.name.startswith("Decision_Log_update_session"):
            for n, titulo in DEF_RE.findall(text):
                definidas.setdefault(int(n), (f.name, titulo.strip()))
        citadas.update(int(n) for n in CITA_RE.findall(text))

    huecos = set()
    for m in re.finditer(r"^\| D-(\d+)(?: a D-(\d+))? \|", idx_text, re.M):
        pass
    hsec = re.search(r"## Huecos de numeraci[óo]n(.+?)(?=\n## )", idx_text, re.S)
    if hsec:
        for a, b in re.findall(r"D-(\d+)(?:\s*a\s*D-(\d+))?", hsec.group(1)):
            huecos.update(range(int(a), int(b or a) + 1))

    return filas, ausentes, definidas, citadas, huecos


def check(root: Path):
    """J1-J4 against a project files root. Returns (filas, ausentes,
    definidas, fallas). Extracted out of main() so project_files_check.py
    can absorb this module by calling it directly, without reimplementing
    the invariant logic below — that logic is unchanged from the original
    delivery of this script."""
    filas, ausentes, definidas, citadas, huecos = scan(root)
    fallas = []

    for n, (archivo, _titulo) in sorted(definidas.items()):
        if n not in filas and n not in huecos:
            fallas.append(f"J1 (definida sin fila): D-{n} tiene enunciado en {archivo} y no está en el índice")

    for n, (_ses, _titulo, fuente) in sorted(filas.items()):
        if n in ausentes:
            continue
        nombre = fuente.strip("`").strip()
        if nombre.endswith(".md") and not (root / nombre).exists():
            fallas.append(f"J2 (fuente inexistente): D-{n} apunta a {nombre}, que no está en {root}")

    for n in sorted(citadas):
        if n not in filas and n not in huecos and n <= max(filas):
            fallas.append(
                f"J3 (citada sin fila): D-{n} se cita en algún project file y no tiene fila en el "
                f"índice ni está declarada como hueco de numeración"
            )

    for n, (_ses, _titulo, fuente) in sorted(filas.items()):
        if n in ausentes:
            continue
        nombre = fuente.strip("`").strip()
        if not nombre.startswith("Decision_Log_update_session"):
            continue
        f = root / nombre
        if not f.exists():
            continue
        if not re.search(rf"^#{{1,4}}\s*D-{n}\b", f.read_text(errors="replace"), re.M):
            fallas.append(
                f"J4 (copia trunca): el índice dice que D-{n} vive en {nombre}, y esa copia no "
                f"contiene su encabezado. O la fila apunta mal, o el archivo subido no es el definitivo"
            )

    return filas, ausentes, definidas, fallas


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = Path(args[0]) if args else Path(".")
    filas, ausentes, definidas, fallas = check(root)

    if "--json" in sys.argv:
        print(json.dumps({
            "filas": len(filas), "definidas": len(definidas),
            "ausentes": sorted(ausentes), "fallas": fallas,
        }, indent=2, ensure_ascii=False))
    else:
        print(f"Índice: {len(filas)} filas · {len(definidas)} decisiones con enunciado propio · "
              f"{len(ausentes)} sin texto redactado")
        if ausentes:
            print("  Pendientes de recuperación: " + ", ".join(f"D-{n}" for n in sorted(ausentes)))
        for f in fallas:
            print("FAIL: " + f)
        print("OK: J1-J3 pasan." if not fallas else f"\n{len(fallas)} violación(es).")

    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
