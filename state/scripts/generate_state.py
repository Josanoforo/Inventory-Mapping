#!/usr/bin/env python3
"""Generate state/STATE.md — a mechanical snapshot of repo state.

No interpretation. Every figure comes from git, state/pendientes_ledger.md,
or a manifest file found in the repo/branches. Anything not mechanically
extractable is reported as absent ("no disponible" / "no registrada en
repo" / "no disponibles en repo") — never estimated or inferred.

Run from the repository root:
    python3 state/scripts/generate_state.py
"""
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
STATE_SCRIPTS = REPO_ROOT / "state" / "scripts"
OUTPUT_PATH = REPO_ROOT / "state" / "STATE.md"

sys.path.insert(0, str(STATE_SCRIPTS))
import ledger_check  # noqa: E402


def run_git(args, cwd=REPO_ROOT):
    result = subprocess.run(
        ["git", *args], cwd=cwd, capture_output=True, text=True
    )
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def section_header_and_head():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    head_sha = run_git(["rev-parse", "HEAD"]) or "no disponible"
    lines = [
        "# STATE.md",
        "",
        f"Generado: {now} (UTC), sobre HEAD `{head_sha}`.",
        "",
        "Snapshot mecánico. Regenerado automáticamente por "
        "`.github/workflows/state-snapshot.yml` en cada push. Sin juicio, "
        "sin narrativa — solo lo que es extraíble determinísticamente de "
        "git, el ledger y los manifests del repo.",
        "",
    ]
    return lines


def section_main():
    lines = ["## main", ""]
    short_sha = run_git(["rev-parse", "--short", "origin/main"])
    if short_sha is None:
        short_sha = run_git(["rev-parse", "--short", "HEAD"]) or "no disponible"
    lines.append(f"- SHA: `{short_sha}`")

    ci_status = get_ci_status_locally()
    if ci_status is not None:
        lines.append(f"- Último run de CI: {ci_status}")
    lines.append("")
    return lines


def get_ci_status_locally():
    """Try to read the last CI run for main via the gh CLI, if present and
    authenticated. Returns None (omit, don't invent) if not consultable."""
    gh_check = subprocess.run(
        ["which", "gh"], capture_output=True, text=True
    )
    if gh_check.returncode != 0:
        return None
    result = subprocess.run(
        [
            "gh", "run", "list",
            "--branch", "main",
            "--limit", "1",
            "--json", "status,conclusion,workflowName,createdAt",
        ],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if result.returncode != 0 or not result.stdout.strip():
        return None
    try:
        runs = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None
    if not runs:
        return None
    run = runs[0]
    status = run.get("conclusion") or run.get("status") or "no disponible"
    workflow = run.get("workflowName", "?")
    created = run.get("createdAt", "?")
    return f"{workflow} — {status} ({created})"


def section_remote_branches(current_branch):
    lines = ["## Ramas remotas con commits en origin", ""]
    raw = run_git([
        "for-each-ref",
        "--sort=-committerdate",
        "--format=%(refname:short)|%(committerdate:iso-strict)|%(subject)",
        "refs/remotes/origin",
    ])
    if raw is None:
        lines.append("no disponible")
        lines.append("")
        return lines

    # git for-each-ref shortens the symbolic refs/remotes/origin/HEAD ref to
    # just "origin" (not "origin/HEAD") via refname:short — must exclude
    # that bare form too, or it slices into an empty branch name below.
    excluded = {"origin/HEAD", "origin/main", "origin"}
    if current_branch:
        excluded.add(f"origin/{current_branch}")

    rows = []
    for line in raw.splitlines():
        parts = line.split("|", 2)
        if len(parts) != 3:
            continue
        ref, date, subject = parts
        if ref in excluded or not ref.startswith("origin/"):
            continue
        rows.append((ref, date, subject))

    if not rows:
        lines.append("(ninguna otra rama con commits en origin)")
    else:
        for ref, date, subject in rows:
            name = ref[len("origin/"):]
            lines.append(f"- `{name}` — {date} — {subject}")
    lines.append("")
    return lines


def section_ledger():
    lines = ["## Ledger (`state/pendientes_ledger.md`)", ""]
    ledger_path = REPO_ROOT / "state" / "pendientes_ledger.md"
    if not ledger_path.is_file():
        lines.append("no disponible: state/pendientes_ledger.md no existe")
        lines.append("")
        return lines

    text = ledger_path.read_text(encoding="utf-8")
    ledger_lines = text.splitlines()
    try:
        tables = {
            label: ledger_check.get_table(ledger_lines, label)
            for label in ledger_check.TABLE_SECTION_HEADINGS
        }
    except SystemExit:
        lines.append("no disponible: el ledger no parsea con ledger_check")
        lines.append("")
        return lines

    counts = {label: len(rows) for label, rows in tables.items()}
    lines.append(f"- Grupo A (abiertas): {counts['A']}")
    lines.append(f"- Grupo B (abiertas): {counts['B']}")
    lines.append(f"- Grupo C (abiertas): {counts['C']}")
    lines.append(f"- Grupo D (abiertas): {counts['D']}")
    lines.append(f"- Total abiertas: {sum(counts.values())}")

    parked_match = re.search(
        r"\*\*Parqueadas \(fuera del conteo de abiertos\):\*\*\s*(\d+)", text
    )
    if parked_match:
        lines.append(f"- Parqueadas: {parked_match.group(1)}")
    else:
        lines.append("- Parqueadas: no disponible")
    lines.append("")
    return lines


DECISION_LOG_NAME_RE = re.compile(r"decision.?log", re.IGNORECASE)
DECISION_ID_RE = re.compile(r"^\|?\s*(D-\d+[a-z]?)\s*\|?\s*(.*)$")


def find_decision_log_files():
    candidates = []
    for path in REPO_ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file() and DECISION_LOG_NAME_RE.search(path.name):
            candidates.append(path)
    return candidates


def section_decisions():
    lines = ["## Últimas 5 decisiones registradas", ""]
    candidates = find_decision_log_files()
    if not candidates:
        lines.append("Decisiones: no disponibles en repo")
        lines.append("")
        return lines

    most_recent = max(candidates, key=lambda p: p.stat().st_mtime)
    text = most_recent.read_text(encoding="utf-8")

    entries = []
    for line in text.splitlines():
        m = re.match(r"^[|\-\s]*\*{0,2}(D-\d+[a-z]?)\*{0,2}\b[\s:|.\-–—]*(.*)$", line)
        if m:
            decision_id = m.group(1)
            title = m.group(2).strip(" |").strip()
            title = re.sub(r"\*+", "", title)
            entries.append((decision_id, title))

    if not entries:
        lines.append(f"Decisiones: no disponibles en repo (sin filas D-NNN en `{most_recent.relative_to(REPO_ROOT)}`)")
        lines.append("")
        return lines

    lines.append(f"Fuente: `{most_recent.relative_to(REPO_ROOT)}`")
    lines.append("")
    for decision_id, title in entries[-5:]:
        title_display = title if title else "(sin título extraíble)"
        lines.append(f"- {decision_id}: {title_display}")
    lines.append("")
    return lines


def find_reextraction_manifests():
    """Search every origin branch for working_reextraction/*/manifest.json.
    Never invents a branch that doesn't exist in origin."""
    branches_raw = run_git(["branch", "-r"])
    if branches_raw is None:
        return None
    branches = []
    for line in branches_raw.splitlines():
        name = line.strip()
        if not name or "->" in name:
            continue
        branches.append(name)

    found = []
    for branch in branches:
        listing = run_git(["ls-tree", "-r", "--name-only", branch])
        if listing is None:
            continue
        for path in listing.splitlines():
            if re.match(r"^working_reextraction/[^/]+/manifest\.json$", path):
                found.append((branch, path))
    return found


def describe_manifest_progress(manifest):
    status = manifest.get("status", "no disponible")

    batch = None
    if isinstance(manifest.get("batches_completed"), list) and manifest["batches_completed"]:
        batch = manifest["batches_completed"][-1]
    elif manifest.get("completed_at"):
        batch = manifest["completed_at"]
    elif isinstance(manifest.get("processed_skeletons"), list) and manifest["processed_skeletons"]:
        last = manifest["processed_skeletons"][-1]
        if isinstance(last, dict):
            batch = last.get("batch") or last.get("processed_at")

    if batch is None:
        batch = "no disponible"

    return status, batch


def section_long_processes():
    lines = ["## Procesos largos en curso (re-extracción)", ""]
    manifests = find_reextraction_manifests()
    if manifests is None:
        lines.append("no disponible")
        lines.append("")
        return lines
    if not manifests:
        lines.append("(ningún manifest de re-extracción encontrado en origin)")
        lines.append("")
        return lines

    for branch, path in manifests:
        content = run_git(["show", f"{branch}:{path}"])
        if content is None:
            lines.append(f"- `{branch}` (`{path}`): no disponible")
            continue
        try:
            manifest = json.loads(content)
        except json.JSONDecodeError:
            lines.append(f"- `{branch}` (`{path}`): no disponible (manifest no parsea)")
            continue
        status, batch = describe_manifest_progress(manifest)
        lines.append(f"- `{branch}` (`{path}`): status={status}, batch alcanzado={batch}")
    lines.append("")
    return lines


FROZEN_HEADING_RE = re.compile(r"(?i)superficie congelada|archivos congelados")


def section_frozen_surface():
    lines = ["## Superficie congelada", ""]
    state_dir = REPO_ROOT / "state"
    found_block = None
    found_file = None
    for path in sorted(state_dir.rglob("*.md")):
        if not path.is_file():
            continue
        if path == OUTPUT_PATH:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        m = FROZEN_HEADING_RE.search(text)
        if m:
            found_block = text[m.start():m.start() + 2000]
            found_file = path
            break

    if found_block is None:
        lines.append("Superficie congelada: no registrada en repo")
    else:
        lines.append(f"Fuente: `{found_file.relative_to(REPO_ROOT)}`")
        lines.append("")
        lines.append("```")
        lines.append(found_block.strip())
        lines.append("```")
    lines.append("")
    return lines


def main():
    current_branch = run_git(["rev-parse", "--abbrev-ref", "HEAD"])
    if current_branch == "HEAD":
        current_branch = None

    lines = []
    lines += section_header_and_head()
    lines += section_main()
    lines += section_remote_branches(current_branch)
    lines += section_ledger()
    lines += section_decisions()
    lines += section_long_processes()
    lines += section_frozen_surface()

    OUTPUT_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Escrito {OUTPUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
