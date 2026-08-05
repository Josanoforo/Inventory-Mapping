#!/usr/bin/env python3
"""
claude_md_refs_check.py

D-282(a) / P-156. Every path, script, or file cited between backticks in
CLAUDE.md must exist in the tree, with declared exceptions. Attacks the real
failure mode -- a dead reference left behind by a rename -- without trying
to validate prose.

A backtick token counts as path-like if it ends in a known extension (.py,
.md, .yaml, .yml, .json, .txt, .jsonl) or ends in '/'. Tokens inside fenced
(```) code blocks are not path citations and are excluded before extraction.
Tokens containing '*' are glob patterns, not a single path to check for
literal existence, and are reported separately instead of gated.

EXCEPTIONS below are the only escape hatch, each with its reason inline --
not a separate file that can drift out of sync with this one.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CLAUDE_MD = ROOT / "CLAUDE.md"

PATH_EXTENSIONS = (".py", ".md", ".yaml", ".yml", ".json", ".txt", ".jsonl")

FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
TOKEN_RE = re.compile(r"`([^`\n]+)`")

# token -> reason. Every entry here is a considered exception, not a
# workaround; see CLAUDE.md's own citation for context.
EXCEPTIONS = {
    "Blueprint_DSC.md": (
        "Vive en project files, no en el repo, por diseño (R-I, D-266). "
        "No existe en el árbol y no debe existir."
    ),
    "STATE.md": (
        "Cita en prosa dentro de una frase ilustrativa (sección 'Branch "
        "state verification'), no una referencia de ruta. El archivo real "
        "es state/STATE.md."
    ),
}


def is_path_like(token):
    return token.endswith(PATH_EXTENSIONS) or token.endswith("/")


def extract(text):
    stripped = FENCE_RE.sub("", text)
    tokens = sorted(set(TOKEN_RE.findall(stripped)))

    candidates = []
    globs = []
    for tok in tokens:
        if not is_path_like(tok):
            continue
        if "*" in tok:
            globs.append(tok)
            continue
        candidates.append(tok)
    return candidates, globs


def exists(token):
    return (ROOT / token).exists()


def main():
    text = CLAUDE_MD.read_text(encoding="utf-8")
    candidates, globs = extract(text)

    excepted = [tok for tok in candidates if tok in EXCEPTIONS]
    checked = [tok for tok in candidates if tok not in EXCEPTIONS]

    missing = [tok for tok in checked if not exists(tok)]
    present = [tok for tok in checked if exists(tok)]

    print("=" * 78)
    print("CLAUDE_MD REFS CHECK — every backtick path citation in CLAUDE.md")
    print("=" * 78)
    print(f"Path-like tokens cited: {len(candidates)}")
    print(f"  Checked against tree: {len(checked)} ({len(present)} exist, "
          f"{len(missing)} missing)")
    print(f"  Declared exceptions:  {len(excepted)}")
    print(f"  Glob patterns (not gated, listed only): {len(globs)}")
    print()

    print("-" * 78)
    print("MISSING FROM TREE (fails the check)")
    print("-" * 78)
    if missing:
        for tok in missing:
            print(f"  {tok}")
    else:
        print("(none)")
    print()

    print("-" * 78)
    print("DECLARED EXCEPTIONS")
    print("-" * 78)
    if excepted:
        for tok in excepted:
            print(f"  {tok}")
            print(f"    reason: {EXCEPTIONS[tok]}")
    else:
        print("(none)")
    print()

    print("-" * 78)
    print("GLOB PATTERNS CITED (not verifiable as a single path)")
    print("-" * 78)
    if globs:
        for tok in globs:
            print(f"  {tok}")
    else:
        print("(none)")
    print()

    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
