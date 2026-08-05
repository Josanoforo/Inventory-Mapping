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
  un `Handoff_sessionNN.md` liste bajo una sección "Uploads a project
  files" debe existir en la capa, salvo que esté en JUBILADOS. Supuesto de
  formato, no verificado contra un ejemplo real (ninguno estaba disponible
  para esta construcción): el encabezado de sección se busca por el texto
  literal "uploads a project files" (case-insensitive), y los nombres de
  archivo dentro de esa sección se leen como tokens entre backticks
  (`` `Nombre.md` ``) — la misma convención de cita que ya usa
  `ledger_path_check.py` y `indice_check.py` para nombrar documentos de esta
  capa. Si el formato real difiere, este extractor no los verá y hay que
  ajustarlo; no se inventó un formato distinto a falta de un ejemplo.

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
UPLOAD_HEADING_RE = re.compile(r"^(#{1,4})\s*.*uploads?\s+a\s+project\s*files.*$", re.M | re.I)
UPLOAD_TOKEN_RE = re.compile(r"`([^`]+\.\w+)`")


def extract_uploads_section(text):
    m = UPLOAD_HEADING_RE.search(text)
    if not m:
        return None
    level = len(m.group(1))
    rest = text[m.end():]
    end_m = re.search(rf"^#{{1,{level}}}\s", rest, re.M)
    return rest[:end_m.start()] if end_m else rest


def extract_upload_tokens(body):
    tokens = []
    for tok in UPLOAD_TOKEN_RE.findall(body):
        if re.search(r"\s", tok):
            continue
        tokens.append(tok)
    return sorted(set(tokens))


def check_pf_nuevo(root: Path):
    """PF-nuevo: archivos declarados bajo 'Uploads a project files' en cada
    Handoff_sessionNN.md contra la capa real. Returns (handoffs_con_seccion,
    total_declarado, fallas)."""
    handoffs_con_seccion = []
    total_declarado = 0
    fallas = []
    for f in sorted(root.glob(HANDOFF_GLOB)):
        text = f.read_text(errors="replace")
        body = extract_uploads_section(text)
        if body is None:
            continue
        handoffs_con_seccion.append(f.name)
        for tok in extract_upload_tokens(body):
            total_declarado += 1
            if tok in JUBILADOS:
                continue
            if not (root / tok).exists():
                fallas.append(
                    f"PF-nuevo (inventario declarado sin archivo real): {f.name} declara "
                    f"'{tok}' bajo 'Uploads a project files' y ese archivo no está en {root}"
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
