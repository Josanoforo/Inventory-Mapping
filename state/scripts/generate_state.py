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
MAP_OUTPUT_PATH = REPO_ROOT / "state" / "MAP.md"

# Directories whose tracked content is corpus/state, not structural surface:
# working/ (6864 tracked files — pipeline intermediate state: skeleton
# batches, packets, records, cards, scans, manifests) and input/ (73 tracked
# files — raw deep_search shards, the pipeline's source corpus per
# CLAUDE.md). Both are bulk data an operator would never enumerate by name;
# everything else (phases, schemas, skills, agents, state scripts, output
# reports, root config) is surface someone might ask "does X exist?" about.
DATA_DIRS = ("working", "input")

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


def get_tracked_files():
    raw = run_git(["ls-files"])
    if raw is None:
        return []
    return [line for line in raw.splitlines() if line]


def is_data_path(path):
    return any(path == d or path.startswith(f"{d}/") for d in DATA_DIRS)


def build_name_index(surface_files):
    index = {}
    for path in surface_files:
        name = path.rsplit("/", 1)[-1]
        index.setdefault(name, []).append(path)
    for paths in index.values():
        paths.sort()
    return index


def extract_ci_jobs(workflow_path):
    """Extract job names from a workflow YAML by line-scanning under the
    top-level `jobs:` key. No YAML parser is assumed to be installed in the
    CI runner (the state-snapshot workflow does not pip-install one), so
    this reads the stdlib-only structural convention GitHub Actions
    requires: job names are 2-space-indented keys directly under `jobs:`."""
    text = workflow_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    jobs_idx = None
    for i, line in enumerate(lines):
        if re.match(r"^jobs:\s*$", line):
            jobs_idx = i
            break
    if jobs_idx is None:
        return []

    job_names = []
    for line in lines[jobs_idx + 1:]:
        if line.strip() == "":
            continue
        m = re.match(r"^  ([A-Za-z0-9_.-]+):\s*(#.*)?$", line)
        if m:
            job_names.append(m.group(1))
            continue
        if re.match(r"^\S", line):
            break
    return job_names


def section_name_index(surface_files):
    lines = ["## Índice inverso por nombre", ""]
    index = build_name_index(surface_files)
    for name in sorted(index.keys()):
        paths = index[name]
        if len(paths) == 1:
            lines.append(f"- `{name}` — `{paths[0]}`")
        else:
            lines.append(f"- `{name}`:")
            for path in paths:
                lines.append(f"  - `{path}`")
    lines.append("")
    return lines, index


def section_surface_by_area(surface_files):
    lines = ["## Superficie por área", ""]
    groups = {}
    for path in surface_files:
        dir_parts = path.split("/")[:-1]
        if not dir_parts:
            key = "(raíz)"
        else:
            key = "/".join(dir_parts[:2])
        groups.setdefault(key, 0)
        groups[key] += 1
    for key in sorted(groups.keys()):
        lines.append(f"- `{key}`: {groups[key]}")
    lines.append("")
    return lines


def section_ci():
    lines = ["## CI", ""]
    workflows_dir = REPO_ROOT / ".github" / "workflows"
    if not workflows_dir.is_dir():
        lines.append("no disponible: .github/workflows/ no existe")
        lines.append("")
        return lines
    workflow_files = sorted(
        p for p in workflows_dir.iterdir() if p.suffix in (".yml", ".yaml")
    )
    if not workflow_files:
        lines.append("(ningún workflow en .github/workflows/)")
        lines.append("")
        return lines
    for wf in workflow_files:
        rel = wf.relative_to(REPO_ROOT)
        jobs = extract_ci_jobs(wf)
        if jobs:
            lines.append(f"- `{rel}`: {', '.join(jobs)}")
        else:
            lines.append(f"- `{rel}`: no disponible (sin jobs detectados)")
    lines.append(
        "- extracción por línea sobre claves de 2 espacios bajo `jobs:` "
        "(sin parser YAML en el runner de CI)"
    )
    lines.append("")
    return lines


def section_data_volume(all_files):
    lines = ["## Volumen de datos", ""]
    for data_dir in DATA_DIRS:
        prefix = f"{data_dir}/"
        count = sum(1 for p in all_files if p == data_dir or p.startswith(prefix))
        lines.append(f"- `{data_dir}/`: {count} archivos rastreados")
    lines.append("")
    return lines


def build_map(all_files, head_sha, now):
    surface_files = [p for p in all_files if not is_data_path(p)]

    header = [
        "# MAP.md",
        "",
        f"Generado en {now} (UTC) sobre HEAD `{head_sha}`.",
        "",
        "Snapshot mecánico, sin juicio. Regenerado automáticamente por "
        "`.github/workflows/state-snapshot.yml` en cada push, a partir "
        "únicamente de `git ls-files`.",
        "",
        "Si el HEAD de arriba no es el vigente, este archivo es "
        "procedencia, no evidencia: dice qué había, no qué hay.",
        "",
    ]

    index_lines, index = section_name_index(surface_files)
    area_lines = section_surface_by_area(surface_files)
    ci_lines = section_ci()
    volume_lines = section_data_volume(all_files)

    lines = header + index_lines + area_lines + ci_lines + volume_lines

    indexed_count = sum(len(paths) for paths in index.values())
    if indexed_count != len(surface_files):
        print(
            "COBERTURA INCOMPLETA: índice inverso cubre "
            f"{indexed_count} rutas, superficie tiene {len(surface_files)} "
            "archivos.",
            file=sys.stderr,
        )
        sys.exit(1)

    return "\n".join(lines).rstrip() + "\n"


def main():
    current_branch = run_git(["rev-parse", "--abbrev-ref", "HEAD"])
    if current_branch == "HEAD":
        current_branch = None

    lines = []
    lines += section_header_and_head()
    lines += section_main()
    lines += section_remote_branches(current_branch)
    lines += section_ledger()
    lines += section_long_processes()

    OUTPUT_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Escrito {OUTPUT_PATH.relative_to(REPO_ROOT)}")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    head_sha = run_git(["rev-parse", "HEAD"]) or "no disponible"
    all_files = get_tracked_files()
    map_content = build_map(all_files, head_sha, now)
    MAP_OUTPUT_PATH.write_text(map_content, encoding="utf-8")
    print(f"Escrito {MAP_OUTPUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
