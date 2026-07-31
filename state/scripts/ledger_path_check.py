#!/usr/bin/env python3
"""
P-154. Read-only. Extracts every path-like backtick-quoted token cited in
state/pendientes_ledger.md and checks whether it exists in the current
working tree (== main at the commit this is run against). Not wired to CI —
I7 (referential-integrity gate) is not authorized; this is a manual check.

A token counts as "path-like" if it contains a '/' or ends in a known file
extension (.py, .md, .json, .yaml, .yml, .xlsx). Bare identifiers (field
names, commit SHAs, branch-name-only tokens without a path separator that
match no extension) are not paths and are excluded. This is a heuristic,
not a parser -- false positives/negatives are possible and are not silently
resolved; ambiguous tokens are listed separately for a human to judge.

Usage:
    python3 state/scripts/ledger_path_check.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "state" / "pendientes_ledger.md"

PATH_EXTENSIONS = (".py", ".md", ".json", ".yaml", ".yml", ".xlsx")

TOKEN_RE = re.compile(r"`([^`]+)`")

# Tokens that are backtick-quoted but are clearly not filesystem paths
# (short field/enum/status identifiers, commit SHAs, flags, CI run ids).
NON_PATH_HINTS = re.compile(
    r"^(--|CC$|DSC$|OP$|Estado$)"
)


GIT_REF_RE = re.compile(r"^(claude|legacy|preserve)/")
LINE_SUFFIX_RE = re.compile(r":[\d,\-]+$")


def is_path_like(token):
    if "/" in token:
        return True
    if any(token.endswith(ext) for ext in PATH_EXTENSIONS):
        return True
    return False


def looks_like_sha_or_run_id(token):
    t = token.rstrip("/")
    if re.fullmatch(r"[0-9a-f]{6,40}", t):
        return True
    if re.fullmatch(r"\d{6,}", t):
        return True
    return False


def strip_line_suffix(token):
    return LINE_SUFFIX_RE.sub("", token)


def exists_anywhere(root, relpath):
    """True if relpath exists literally, as a basename anywhere in the tree, or
    as a path-suffix anywhere in the tree (the ledger sometimes cites a path
    fragment, e.g. `p1-extract-records/SKILL.md` for the real
    `.claude/skills/p1-extract-records/SKILL.md`)."""
    p = root / relpath
    if p.exists():
        return True, str(relpath)
    basename = relpath.rstrip("/").split("/")[-1]
    hits = [h for h in root.rglob(basename) if ".git" not in h.parts]
    if "/" not in relpath:
        if hits:
            return True, str(hits[0].relative_to(root))
        return False, None
    suffix_hits = [h for h in hits if str(h.relative_to(root)).replace("\\", "/").endswith(relpath.rstrip("/"))]
    if suffix_hits:
        return True, str(suffix_hits[0].relative_to(root))
    return False, None


def main():
    text = LEDGER.read_text()
    tokens = sorted(set(TOKEN_RE.findall(text)))

    candidates = []
    git_refs = []
    globs = []
    for tok in tokens:
        tok_clean = tok.rstrip(",.;:")
        if NON_PATH_HINTS.match(tok_clean):
            continue
        if looks_like_sha_or_run_id(tok_clean):
            continue
        if "*" in tok_clean or "<" in tok_clean:
            if is_path_like(tok_clean):
                globs.append(tok_clean)
            continue
        if GIT_REF_RE.match(tok_clean):
            git_refs.append(tok_clean)
            continue
        if is_path_like(tok_clean):
            candidates.append(strip_line_suffix(tok_clean))

    missing = []
    present = []
    for tok in sorted(set(candidates)):
        ok, resolved = exists_anywhere(ROOT, tok)
        if ok:
            present.append((tok, resolved))
        else:
            missing.append(tok)

    print(f"Rutas candidatas (archivo/directorio) extraídas del ledger: {len(set(candidates))}")
    print(f"Existen en el árbol actual (main@HEAD): {len(present)}")
    print(f"NO existen en el árbol actual: {len(missing)}")
    print()
    print("=== NO EXISTEN COMO ARCHIVO/DIRECTORIO ===")
    for tok in missing:
        print(f"  {tok}")

    print()
    print(f"=== PATRONES GLOB CITADOS (no verificables como ruta única, {len(globs)}) ===")
    for tok in globs:
        print(f"  {tok}")

    print()
    print(f"=== REFS DE GIT CITADAS COMO `claude/*`/`legacy/*`/`preserve/*` ({len(git_refs)}, no son rutas de archivo — se listan aparte) ===")
    for tok in sorted(set(git_refs)):
        print(f"  {tok}")


if __name__ == "__main__":
    sys.exit(main())
