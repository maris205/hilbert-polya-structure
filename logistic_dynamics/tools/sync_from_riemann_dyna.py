#!/usr/bin/env python3
"""Synchronize source-locked HP-Dynamics stages into the shareable mirror.

The manifest is authoritative for the synchronization boundary.  This tool
never deletes files and never rewrites hand-maintained manuscripts.  It copies
versioned evidence byte-for-byte, generates deterministic provenance records,
and can run as a read-only drift checker with ``--check``.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable

import yaml


SCRIPT = Path(__file__).resolve()
STREAM_ROOT = SCRIPT.parents[1]
MIRROR_ROOT = SCRIPT.parents[2]
DEFAULT_SOURCE_ROOT = MIRROR_ROOT.parent / "find_dyna"
DEFAULT_MANIFEST = STREAM_ROOT / "sync_manifest.yaml"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def git_head(root: Path) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=root, text=True
    ).strip()


def load_manifest(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("stages"), list):
        raise ValueError("manifest must contain a stages list")
    return data


def as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list) and all(isinstance(item, str) for item in value):
        return value
    raise TypeError(f"expected a path string or list, got {value!r}")


def expanded_sources(source_root: Path, stage: dict[str, Any]) -> list[str]:
    ordered: list[str] = []
    for key in (
        "source_locks",
        "evaluations",
        "results",
        "obstructions",
        "experiments",
        "tests",
        "artifacts",
        "literature",
        "extra_files",
    ):
        for relative in as_list(stage.get(key)):
            source = source_root / relative
            if source.is_dir():
                ordered.extend(
                    str(path.relative_to(source_root))
                    for path in sorted(source.rglob("*"))
                    if path.is_file() and "__pycache__" not in path.parts
                )
            else:
                ordered.append(relative)
    # Close over repository-relative paths mentioned by copied generators,
    # tests, result notes, and evaluations.  This keeps a stage runnable after
    # export without editing historical path strings.  The independent legacy
    # repository is deliberately excluded and recorded as an external
    # dependency instead of being silently imported.
    path_pattern = re.compile(
        r"(?<![A-Za-z0-9_])((?:configs|evaluations|experiments|formal|artifacts|"
        r"docs/literature|docs/prior_work)/[A-Za-z0-9_./-]+)"
    )
    seen: set[str] = set()
    queue = list(ordered)
    deduplicated: list[str] = []
    while queue:
        relative = queue.pop(0).rstrip("`'\")>,;:.")
        if relative in seen:
            continue
        seen.add(relative)
        candidate = source_root / relative
        if not candidate.is_file():
            continue
        deduplicated.append(relative)
        if not stage.get("auto_dependencies", True):
            continue
        try:
            text = candidate.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for match in path_pattern.findall(text):
            referenced = match.rstrip("`'\")>,;:.")
            if "docs/related_programs/prime_dynamics_theory" in referenced:
                continue
            if referenced not in seen:
                queue.append(referenced)
    # Some repository-wide ledgers are required as exact test fixtures but
    # contain links to many unrelated stages. Copy these files without treating
    # their prose references as dependency edges.
    for relative in as_list(stage.get("no_follow_files")):
        source = source_root / relative
        if source.is_dir():
            passive_paths = [
                str(path.relative_to(source_root))
                for path in sorted(source.rglob("*"))
                if path.is_file() and "__pycache__" not in path.parts
            ]
        else:
            passive_paths = [relative]
        for passive in passive_paths:
            if passive not in seen:
                seen.add(passive)
                deduplicated.append(passive)
    return deduplicated


def latest_path(stage: dict[str, Any], key: str) -> str | None:
    paths = as_list(stage.get(key))
    return paths[-1] if paths else None


def tuple_from_evaluation(evaluation: dict[str, Any]) -> list[str] | None:
    explicit = evaluation.get("analytic_route_tuple")
    if isinstance(explicit, list):
        return [str(item) for item in explicit]
    values: list[str] = []
    for key in ("a1", "a2", "a3", "a4"):
        layer = evaluation.get(key)
        if not isinstance(layer, dict) or "verdict" not in layer:
            return None
        values.append(str(layer["verdict"]))
    return values


def target_tuple_from_evaluation(evaluation: dict[str, Any]) -> list[str] | None:
    explicit = evaluation.get("riemann_target_tuple")
    if isinstance(explicit, list):
        return [str(item) for item in explicit]
    return None


def route_summary(source_root: Path, stage: dict[str, Any]) -> dict[str, Any]:
    path = latest_path(stage, "evaluations")
    if path is None:
        return {
            "analytic_tuple": None,
            "target_tuple": None,
            "overall": "NOT_FORMALLY_EVALUATED",
            "verdict": stage.get("status", "ARCHIVED"),
            "route_b_allowed": False,
        }
    evaluation = yaml.safe_load((source_root / path).read_text(encoding="utf-8"))
    verdict = (
        evaluation.get("recommended_verdict")
        or evaluation.get("recommended_audit_verdict")
        or evaluation.get("scoped_audit_verdict")
        or stage.get("status")
    )
    return {
        "analytic_tuple": tuple_from_evaluation(evaluation),
        "target_tuple": target_tuple_from_evaluation(evaluation),
        "overall": evaluation.get("overall_verdict", "NOT_RECORDED"),
        "verdict": verdict,
        "route_b_allowed": bool(evaluation.get("route_b_invocation_allowed", False)),
    }


def format_tuple(value: list[str] | None) -> str:
    return "(" + ", ".join(value) + ")" if value else "not separately recorded"


def generated_readme(source_root: Path, stage: dict[str, Any]) -> str:
    route = route_summary(source_root, stage)
    candidate = stage.get("candidate_id") or "none (audit/archive)"
    formal = str(bool(stage.get("formal_candidate", False))).lower()
    paper_status = stage.get("paper_status", "not_opened")
    tests = as_list(stage.get("tests"))
    reproduction_mode = stage.get("reproduction_mode", "mirror_portable")
    if reproduction_mode == "source_bound":
        reproduction = (
            f"python3 logistic_dynamics/tools/test_all_projects.py "
            f"--project {Path(stage['project']).name}\n"
            f"cd logistic_dynamics/{stage['project']}\n"
            "sha256sum -c results/SOURCE_HASHES.sha256"
        )
        reproduction_location = "Run from the `hilbert-polya-structure` repository root."
        reproduction_note = (
            "This historical regression is source-bound because it verifies the "
            "original `riemann_dyna` Git commit or an artifact containing frozen "
            "absolute source paths. The wrapper runs the original test at the "
            "manifest-bound source commit; mirror bytes remain checked independently."
        )
    else:
        reproduction = "\n".join(
            f"PYTHONPATH=. python3 -m unittest -v {path}" for path in tests
        ) or "# No standalone executable regression was frozen for this archive stage."
        reproduction += "\nsha256sum -c results/SOURCE_HASHES.sha256"
        reproduction_location = "Run from this project directory."
        reproduction_note = "This regression is portable inside the mirrored project snapshot."
    source_locks = as_list(stage.get("source_locks"))
    evaluations = as_list(stage.get("evaluations"))
    source_lock_entry = source_locks[-1] if source_locks else "none"
    evaluation_entry = evaluations[-1] if evaluations else "none"
    dependencies = stage.get("dependencies") or []
    dependency_lines = (
        "\n".join(f"- `{item}`" for item in dependencies)
        if dependencies
        else "- None beyond files mirrored in this project."
    )
    return f"""# {stage['title']}

- Stage ID: `{stage['stage_id']}`
- Candidate ID: `{candidate}`
- Formal candidate: `{formal}`
- Archive status: `{stage.get('status', 'NOT_RECORDED')}`
- Paper status: `{paper_status}`

## Purpose

{stage['summary']}

This directory is a source-locked shareable snapshot of the corresponding
HP-Dynamics checkpoint.  It does not replace or rewrite the versioned evidence
in `riemann_dyna`; copied evidence is verified byte-for-byte by
`SOURCE_PROVENANCE.yaml` and `results/SOURCE_HASHES.sha256`.

## Route-A checkpoint

```text
analytic tuple:       {format_tuple(route['analytic_tuple'])}
Riemann-target tuple: {format_tuple(route['target_tuple'])}
overall:              {route['overall']}
recommended verdict: {route['verdict']}
Route B authorized:   {str(route['route_b_allowed']).lower()}
```

## Strongest failure / limitation

{stage['failure']}

## Claim boundary

Established only within the frozen object and data boundary described by
`source_lock.yaml` and `route_a_evaluation.yaml`.  No project in this stream
claims a completed-xi identity, a Hilbert--Pólya realization, the Riemann
Hypothesis, or permission to mix determinant conventions.

## Canonical records

- Main source lock: `{source_lock_entry}`
- Main Route-A evaluation: `{evaluation_entry}`
- `results/`: formal result notes copied from the main research repository.
- `obstructions/`: scoped obstruction notes, when applicable.
- `experiments/`, `tests/`, and `artifacts/`: repository-compatible
  reproduction snapshot.
- `SOURCE_PROVENANCE.yaml`: source commit, paths, and hashes.

## Dependencies

{dependency_lines}

## Reproduction

{reproduction_location}

{reproduction_note}

```bash
{reproduction}
```

## Next smallest task

{stage['next_task']}
"""


def generated_narrative(stage: dict[str, Any]) -> str:
    return f"""# Narrative report — {stage['title']}

## One-sentence contribution

{stage['summary']}

## Frozen evidence

The mathematical object, clock, normalization, determinant convention, data
firewall, cutoffs, and stopping conditions are inherited byte-for-byte from
`source_lock.yaml`.  The Route-A decision is inherited byte-for-byte from
`route_a_evaluation.yaml`; this mirror performs no new fitting or claim
promotion.

## Strongest limitation

{stage['failure']}

## Interpretation

This stage is retained because it supplies a reusable theorem, certified
result, strict obstruction, or meaningful negative result.  It must be read
with its signed/complex cancellation and determinant-ledger conventions
unchanged.

## Nonclaims

This report does not establish a prime-orbit correspondence, completed-xi
divisor equality, self-adjoint Hilbert--Pólya operator, RH proof, or Route-B
authorization unless the copied evaluation explicitly says otherwise.

## Reproduction and provenance

See `README.md`, `SOURCE_PROVENANCE.yaml`, and
`results/SOURCE_HASHES.sha256`.
"""


def generated_paper_plan(stage: dict[str, Any]) -> str:
    return f"""# Paper plan — {stage['title']}

Paper status: `{stage.get('paper_status', 'planned')}`.

## Working contribution

{stage['summary']}

## Claim-evidence boundary

| Item | Paper treatment |
|---|---|
| Frozen object | State exactly from `source_lock.yaml` |
| Main result | Prove or reproduce only the source-locked checkpoint |
| Strongest failure | {stage['failure']} |
| Route-A decision | Quote `route_a_evaluation.yaml` without promotion |
| Route B / RH | Explicit nonclaim |

## Proposed structure

1. Frozen dynamical object and data firewall.
2. Primitive-orbit or operator ledger.
3. Exact/certified result.
4. Reproduction protocol and source hashes.
5. Strongest obstruction and claim boundary.
6. Smallest legitimate reopening task.

## Reproducibility boundary

The manuscript may use only files named in `SOURCE_PROVENANCE.yaml`.  Any
later theorem edge requires a new source lock, evaluation version, and mirror
checkpoint.
"""


def metadata_payload(
    manifest: dict[str, Any], source_root: Path, stage: dict[str, Any], sources: list[str]
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "sync_id": manifest["sync_id"],
        "sync_timestamp": manifest["sync_timestamp"],
        "source_repository": manifest["source_repository"],
        "source_commit": manifest["source_commit"],
        "mirror_repository": manifest["mirror_repository"],
        "mirror_path": f"logistic_dynamics/{stage['project']}",
        "stage_id": stage["stage_id"],
        "candidate_id": stage.get("candidate_id"),
        "formal_candidate": bool(stage.get("formal_candidate", False)),
        "paper_status": stage.get("paper_status", "not_opened"),
        "reproduction_mode": stage.get("reproduction_mode", "mirror_portable"),
        "external_dependencies": stage.get("external_dependencies", []),
        "source_files": [
            {"path": relative, "sha256": sha256(source_root / relative)}
            for relative in sources
        ],
    }


def yaml_bytes(payload: dict[str, Any]) -> bytes:
    return yaml.safe_dump(
        payload, sort_keys=False, allow_unicode=True, width=100
    ).encode("utf-8")


def hashes_bytes(source_root: Path, sources: Iterable[str]) -> bytes:
    return "".join(
        f"{sha256(source_root / relative)}  {relative}\n" for relative in sources
    ).encode("utf-8")


def compare_or_write(path: Path, expected: bytes, check: bool, drift: list[str]) -> None:
    if check:
        if not path.exists() or path.read_bytes() != expected:
            drift.append(str(path.relative_to(STREAM_ROOT)))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_bytes() != expected:
        path.write_bytes(expected)


def sync_stage(
    manifest: dict[str, Any],
    source_root: Path,
    stage: dict[str, Any],
    check: bool,
    drift: list[str],
) -> None:
    project = STREAM_ROOT / stage["project"]
    sources = expanded_sources(source_root, stage)
    for relative in sources:
        source = source_root / relative
        if not source.is_file():
            raise FileNotFoundError(source)
        destination = project / relative
        if check:
            if not destination.exists() or destination.read_bytes() != source.read_bytes():
                drift.append(str(destination.relative_to(STREAM_ROOT)))
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            if not destination.exists() or destination.read_bytes() != source.read_bytes():
                shutil.copy2(source, destination)

    lock = latest_path(stage, "source_locks")
    if lock:
        compare_or_write(project / "source_lock.yaml", (source_root / lock).read_bytes(), check, drift)
    evaluation = latest_path(stage, "evaluations")
    if evaluation:
        compare_or_write(
            project / "route_a_evaluation.yaml",
            (source_root / evaluation).read_bytes(),
            check,
            drift,
        )

    for relative in as_list(stage.get("results")):
        compare_or_write(
            project / "results" / Path(relative).name,
            (source_root / relative).read_bytes(),
            check,
            drift,
        )
    for relative in as_list(stage.get("obstructions")):
        compare_or_write(
            project / "obstructions" / Path(relative).name,
            (source_root / relative).read_bytes(),
            check,
            drift,
        )

    metadata = metadata_payload(manifest, source_root, stage, sources)
    compare_or_write(project / "SOURCE_PROVENANCE.yaml", yaml_bytes(metadata), check, drift)
    compare_or_write(
        project / "results" / "SOURCE_HASHES.sha256",
        hashes_bytes(source_root, sources),
        check,
        drift,
    )

    if stage.get("documentation", "generated") == "generated":
        compare_or_write(
            project / "README.md",
            generated_readme(source_root, stage).encode("utf-8"),
            check,
            drift,
        )
        if stage.get("paper_status") in {"planned", "draft", "published"}:
            compare_or_write(
                project / "NARRATIVE_REPORT.md",
                generated_narrative(stage).encode("utf-8"),
                check,
                drift,
            )
            compare_or_write(
                project / "PAPER_PLAN.md",
                generated_paper_plan(stage).encode("utf-8"),
                check,
                drift,
            )


def generated_index(source_root: Path, manifest: dict[str, Any]) -> bytes:
    lines = [
        "# HP-Dynamics synchronized stage index\n",
        "This index is generated from `sync_manifest.yaml`. The source research "
        "repository is frozen at commit "
        f"`{manifest['source_commit']}`.\n",
        "| Group | Stage | Candidate | Status | Route-A | Paper |\n",
        "|---|---|---|---|---|---|\n",
    ]
    for stage in manifest["stages"]:
        route = route_summary(source_root, stage)
        candidate = stage.get("candidate_id") or "audit"
        lines.append(
            f"| {stage['group']} | "
            f"[`{stage['stage_id']}`]({stage['project']}/README.md) | "
            f"`{candidate}` | `{stage.get('status', 'NOT_RECORDED')}` | "
            f"`{route['overall']}` / `{route['verdict']}` | "
            f"`{stage.get('paper_status', 'not_opened')}` |\n"
        )
    lines.extend(
        [
            "\n## Synchronization boundary\n",
            "- All paths and hashes are recorded per project in "
            "`SOURCE_PROVENANCE.yaml`.\n",
            "- Audit-only and superseded checkpoints remain visible but are not "
            "promoted to papers.\n",
            "- Route B stays closed unless the copied Route-A evaluation explicitly "
            "authorizes it.\n",
        ]
    )
    return "".join(lines).encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--stage", action="append", default=[])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    source_root = args.source_root.resolve()
    manifest = load_manifest(args.manifest.resolve())
    actual_head = git_head(source_root)
    if actual_head != manifest["source_commit"]:
        print(
            f"source HEAD mismatch: manifest={manifest['source_commit']} actual={actual_head}",
            file=sys.stderr,
        )
        return 2

    selected = set(args.stage)
    known = {stage["stage_id"] for stage in manifest["stages"]}
    unknown = selected - known
    if unknown:
        print(f"unknown stages: {sorted(unknown)}", file=sys.stderr)
        return 2

    drift: list[str] = []
    for stage in manifest["stages"]:
        if selected and stage["stage_id"] not in selected:
            continue
        sync_stage(manifest, source_root, stage, args.check, drift)

    if not selected:
        compare_or_write(
            STREAM_ROOT / "STAGE_INDEX.md",
            generated_index(source_root, manifest),
            args.check,
            drift,
        )

    if drift:
        print("synchronization drift detected:")
        for path in sorted(set(drift)):
            print(f"  {path}")
        return 1
    print(
        f"{'checked' if args.check else 'synchronized'} "
        f"{len(selected) if selected else len(manifest['stages'])} stage(s) "
        f"at source commit {actual_head}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
