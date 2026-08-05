#!/usr/bin/env python3
"""Reads resources.yaml + `git ls-files` and reports on resource registry health.

resources.yaml is the authority: every tracked resource (data artifact,
script, module, schema, skill, etc.) should have a row declaring its
`clase`, `fase`, `productor` and `consumidores`. Per D-286, this script
gates exclusively on section 2 (REGISTRADO PERO MUERTO): exit 1 if that
section has >=1 entry, exit 0 otherwise. Sections 1, 3 and 4 are still
printed in full but never affect the exit code — their threshold for
failure is an open decision (1 = .gitkeep files and other placeholder
artifacts that legitimately have no resources.yaml row yet; 3 = pending
P-209; 4 = production that lives outside this repo). It reports four
sections:

  1. EN ARBOL SIN REGISTRO — tracked files no path/glob in resources.yaml
     covers. Grouped by root directory with a count; full list at the end.
     This is the backfill list, not an error.
  2. REGISTRADO PERO MUERTO — entries with clase `permanente` whose path
     matches nothing in the tree. Classes derivado/por-corrida/reporte are
     excluded: their absence between runs is normal. fuera_del_arbol is
     never checked here (it is not expected to exist in the tree).
  3. ESCRITOR SIN LECTOR — productor non-empty and consumidores == [].
  4. SIN PRODUCTOR — consumidores non-empty and productor == [], for
     entries with clase in {derivado, por-corrida}.

Path matching (fnmatch semantics, not shell/gitignore glob):
  - a path ending in '/' covers everything under it, by prefix
  - a path containing '*', '?' or '[' is matched with fnmatch.fnmatch
    ('*' crosses directory separators — it has no path awareness)
  - anything else must match a tracked file exactly

Determinism: two consecutive runs against the same tree produce identical
output (all groupings are sorted; no wall-clock, randomness, or unordered
set/dict iteration reaches the report).
"""
import fnmatch
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
RESOURCES_PATH = ROOT / "resources.yaml"

PERMANENT_EXEMPT_CLASSES = {"derivado", "por-corrida", "reporte"}
NO_PRODUCER_CLASSES = {"derivado", "por-corrida"}


def load_resources():
    with RESOURCES_PATH.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("resources", []), data.get("fuera_del_arbol", [])


def tracked_files():
    out = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    return sorted(line for line in out.splitlines() if line)


def path_matches(pattern, filepath):
    if pattern.endswith("/"):
        return filepath.startswith(pattern)
    if any(c in pattern for c in "*?["):
        return fnmatch.fnmatch(filepath, pattern)
    return filepath == pattern


def any_tracked_matches(pattern, files):
    return any(path_matches(pattern, f) for f in files)


def root_dir(filepath):
    if "/" in filepath:
        return filepath.split("/", 1)[0]
    return filepath


def section_unregistered(resources, files):
    patterns = [r["path"] for r in resources]
    unregistered = [f for f in files if not any(path_matches(p, f) for p in patterns)]
    unregistered.sort()

    by_root = defaultdict(int)
    for f in unregistered:
        by_root[root_dir(f)] += 1

    lines = []
    lines.append("1. EN ARBOL SIN REGISTRO")
    lines.append(f"   Total: {len(unregistered)}")
    lines.append("   Desglose por directorio raiz:")
    for root in sorted(by_root):
        lines.append(f"     {root}: {by_root[root]}")
    lines.append("   Lista completa:")
    for f in unregistered:
        lines.append(f"     {f}")
    return lines, unregistered


def section_dead(resources, files):
    dead = []
    for r in resources:
        if r.get("clase") != "permanente":
            continue
        if r.get("clase") in PERMANENT_EXEMPT_CLASSES:
            continue
        if not any_tracked_matches(r["path"], files):
            dead.append(r["path"])
    dead.sort()

    lines = ["", "2. REGISTRADO PERO MUERTO", f"   Total: {len(dead)}"]
    for p in dead:
        lines.append(f"     {p}")
    return lines, dead


def section_writer_no_reader(resources):
    found = sorted(
        r["path"] for r in resources
        if r.get("productor") and not r.get("consumidores")
    )
    lines = ["", "3. ESCRITOR SIN LECTOR", f"   Total: {len(found)}"]
    for p in found:
        lines.append(f"     {p}")
    return lines, found


def section_no_producer(resources):
    found = sorted(
        r["path"] for r in resources
        if r.get("consumidores") and not r.get("productor")
        and r.get("clase") in NO_PRODUCER_CLASSES
    )
    lines = ["", "4. SIN PRODUCTOR", f"   Total: {len(found)}"]
    for p in found:
        lines.append(f"     {p}")
    return lines, found


def main():
    resources, _fuera_del_arbol = load_resources()
    files = tracked_files()

    print("=" * 78)
    print("RESOURCE CHECK -- resources.yaml vs git ls-files")
    print("=" * 78)
    print(f"Filas registradas: {len(resources)}")
    print(f"Archivos rastreados: {len(files)}")
    print()

    l1, _ = section_unregistered(resources, files)
    l2, dead = section_dead(resources, files)
    l3, _ = section_writer_no_reader(resources)
    l4, _ = section_no_producer(resources)

    for block in (l1, l2, l3, l4):
        for line in block:
            print(line)

    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
