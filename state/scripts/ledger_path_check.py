#!/usr/bin/env python3
"""
P-154. Read-only extraction, gated exit. Extracts every path-like
backtick-quoted token cited in state/pendientes_ledger.md and checks
whether it exists in the current working tree (== main at the commit this
is run against). Wired to CI per D-271, with the fail path built in D-286:
this is an increment gate, not a full-ledger gate. `main()` returns 1 only
if a token now missing from the tree is NOT already recorded in
state/scripts/ledger_path_baseline.txt (a new dead reference the sweep
hasn't accounted for yet); it returns 0 if every missing token is a subset
of the baseline. The baseline itself is the pre-existing debt inherited
from before this gate existed — see that file's header for how it shrinks.

A token counts as "path-like" if it contains a '/' or ends in a known file
extension (.py, .md, .json, .yaml, .yml, .xlsx). Bare identifiers (field
names, commit SHAs, branch-name-only tokens without a path separator that
match no extension) are not paths and are excluded. This is a heuristic,
not a parser -- false positives/negatives are possible and are not silently
resolved; ambiguous tokens are listed separately for a human to judge.

Five mechanical exclusions narrow path-like tokens before they are checked
against the filesystem (D-286):

  (a) A token containing whitespace is not a single path -- it is a quoted
      shell command or code fragment (e.g. `grep -rc "..." .claude/skills/`,
      or a multi-line backtick span the extractor's regex ropes together
      via an embedded newline). These go to their own section instead of
      being treated as a bogus missing path.
  (b) A token that is only a bare extension (`.py`, `.xlsx`, ...) with no
      filename has nothing to check for existence -- it is discarded, with
      a count kept so the drop is visible rather than silent.
  (c) `GIT_REF_RE` also matches `origin/...` and `upstream/...` remote
      refs, alongside the existing `claude/`, `legacy/`, `preserve/`
      branch-name refs -- these are not filesystem paths either.
  (d) A token with a placeholder in braces (`{n}`, `{...}`) is a template,
      not a literal path -- it is treated like the existing `*`/`<...>`
      glob tokens and listed in the glob section instead of being checked
      for literal existence.
  (e) A token starting with `Blueprint_`, `DSC_`, `Decision_Log_`,
      `Handoff_`, `System_Registry_`, `Indice_`, or `Decision_Router_`
      names a project-files-layer document. This repo's tree cannot verify
      those -- project_files_check.py does, against the project-files
      store, not `git ls-files`. They get their own section noting that.

Usage:
    python3 state/scripts/ledger_path_check.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "state" / "pendientes_ledger.md"
BASELINE_PATH = ROOT / "state" / "scripts" / "ledger_path_baseline.txt"

PATH_EXTENSIONS = (".py", ".md", ".json", ".yaml", ".yml", ".xlsx")

TOKEN_RE = re.compile(r"`([^`]+)`")

# Tokens that are backtick-quoted but are clearly not filesystem paths
# (short field/enum/status identifiers, commit SHAs, flags, CI run ids).
NON_PATH_HINTS = re.compile(
    r"^(--|CC$|DSC$|OP$|Estado$)"
)

# (c) origin/... and upstream/... are remote refs, not filesystem paths,
# same as the claude/legacy/preserve branch-name refs already excluded here.
GIT_REF_RE = re.compile(r"^(claude|legacy|preserve|origin|upstream)/")
LINE_SUFFIX_RE = re.compile(r":[\d,\-]+$")

# (a) any whitespace inside a token means it's a command or code fragment,
# not a single path.
WHITESPACE_RE = re.compile(r"\s")

# (d) a brace placeholder ({n}, {...}) marks a template path, not a literal
# one -- route it to the glob section like the existing */< tokens.
PLACEHOLDER_RE = re.compile(r"\{[^}]*\}")

# (e) project-files-layer documents: not in this repo's tree, verified by
# project_files_check.py against the project-files store instead.
PROJECT_FILE_PREFIXES = (
    "Blueprint_",
    "DSC_",
    "Decision_Log_",
    "Handoff_",
    "System_Registry_",
    "Indice_",
    "Decision_Router_",
)


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


def load_baseline():
    if not BASELINE_PATH.exists():
        return set()
    lines = BASELINE_PATH.read_text().splitlines()
    return {line for line in lines if line and not line.lstrip().startswith("#")}


def extract(text):
    tokens = sorted(set(TOKEN_RE.findall(text)))

    non_path_tokens = []
    bare_extension_count = 0
    candidates = []
    git_refs = []
    globs = []
    project_files = []

    for tok in tokens:
        tok_clean = tok.rstrip(",.;:")

        if WHITESPACE_RE.search(tok_clean):
            non_path_tokens.append(tok_clean)
            continue
        if NON_PATH_HINTS.match(tok_clean):
            continue
        if looks_like_sha_or_run_id(tok_clean):
            continue
        if tok_clean in PATH_EXTENSIONS:
            bare_extension_count += 1
            continue
        if "*" in tok_clean or "<" in tok_clean or PLACEHOLDER_RE.search(tok_clean):
            if is_path_like(tok_clean):
                globs.append(tok_clean)
            continue
        if GIT_REF_RE.match(tok_clean):
            git_refs.append(tok_clean)
            continue
        if tok_clean.startswith(PROJECT_FILE_PREFIXES):
            project_files.append(tok_clean)
            continue
        if is_path_like(tok_clean):
            candidates.append(strip_line_suffix(tok_clean))

    return {
        "non_path_tokens": non_path_tokens,
        "bare_extension_count": bare_extension_count,
        "candidates": candidates,
        "git_refs": git_refs,
        "globs": globs,
        "project_files": project_files,
    }


def main():
    text = LEDGER.read_text()
    extracted = extract(text)
    candidates = extracted["candidates"]

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
    print(f"=== PATRONES GLOB CITADOS (no verificables como ruta única, {len(extracted['globs'])}) ===")
    for tok in extracted["globs"]:
        print(f"  {tok}")

    print()
    print(f"=== REFS DE GIT CITADAS COMO `claude/*`/`legacy/*`/`preserve/*`/`origin/*`/`upstream/*` ({len(extracted['git_refs'])}, no son rutas de archivo — se listan aparte) ===")
    for tok in sorted(set(extracted["git_refs"])):
        print(f"  {tok}")

    print()
    print(f"=== TOKENS NO-RUTA (comandos o fragmentos de código citados, {len(extracted['non_path_tokens'])}) ===")
    for tok in extracted["non_path_tokens"]:
        print(f"  {tok}")

    print()
    print(f"=== CAPA PROJECT FILES (no verificable desde el repo — la cubre project_files_check.py, {len(extracted['project_files'])}) ===")
    for tok in sorted(set(extracted["project_files"])):
        print(f"  {tok}")

    print()
    print(f"Extensiones sueltas descartadas (sin nombre de archivo): {extracted['bare_extension_count']}")

    baseline = load_baseline()
    missing_set = set(missing)
    new_missing = sorted(missing_set - baseline)
    resolved = sorted(baseline - missing_set)

    print()
    print(f"=== GATE POR INCREMENTO (baseline: {len(baseline)} tokens) ===")
    if resolved:
        for tok in resolved:
            print(f"  RESUELTO — retirar del baseline: {tok}")
    if new_missing:
        print(f"  Tokens faltantes NUEVOS (fuera del baseline, {len(new_missing)}):")
        for tok in new_missing:
            print(f"    {tok}")
        return 1

    print("  Sin tokens faltantes nuevos fuera del baseline.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
