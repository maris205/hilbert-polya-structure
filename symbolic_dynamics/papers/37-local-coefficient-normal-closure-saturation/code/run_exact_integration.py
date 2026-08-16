#!/usr/bin/env python3
"""Build the exact Paper 37 evidence and strict Route-A Stage-1 artifacts."""

from __future__ import annotations

import ast
import csv
from fractions import Fraction
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"
RESULTS = ROOT / "results"
EVALUATION_DIR = ROOT / "evaluations" / "route_a" / "SD-C39"
ROUTE_CARD = EVALUATION_DIR / "2026-08-15.yaml"
LEDGER = RESULTS / "SHA256SUMS.txt"
PAPER_MANIFEST = ROOT / "PAPER_MANIFEST.sha256"

EXPECTED_SCIENCE_SHA256 = (
    "b17967f294da018e2e045ae70ac7731f5612f4bd4693115ea33dbaebb7fc0d6e"
)
EXPECTED_SOURCE_CORE_SHA256 = (
    "f127037786d0ca3eea3125d9b94f924e4534cd33e7252e94e2c5ef373378b116"
)
EXPECTED_EVALUATOR_CORE_SHA256 = (
    "eae6fad20e45fce97d82113552ec7a8c13f33a398cda90b3948ad11af39c4b09"
)
EXPECTED_BRIDGE_HASHES = {
    "/tmp/paper37_exact_prototype/EXPERIMENT_PLAN.md": "9ec8ae5442c6b1c7541dc8b8e4796b041a4720ac0009a1dd46e8f17510531546",
    "/tmp/paper37_exact_prototype/PREREGISTRATION.md": "8906a3700f37496e032778306e9a001ba9759919b17b74323c4446fa5300c212",
    "/tmp/paper37_exact_prototype/independent_evaluator.py": "eae6fad20e45fce97d82113552ec7a8c13f33a398cda90b3948ad11af39c4b09",
    "/tmp/paper37_exact_prototype/run_exact.py": "d01df2a017b026a8704718fa516da762fe552498eb3e9bd9b9010cb51a66f8ef",
    "/tmp/paper37_exact_prototype/source_core.py": "f127037786d0ca3eea3125d9b94f924e4534cd33e7252e94e2c5ef373378b116",
    "/tmp/paper37_research_package.md": "e39a8c89975670926461c46c9c82df58e886647e49fb77244fc530d3a060f3aa",
    "/tmp/paper37_source_lock.md": "d725f03caffc6c5fab916314df25097b7383af7494287052496516deab0dcb4e",
}

EXPECTED_RESULT_PATHS = [
    "results/SHA256SUMS.txt",
    "results/affine_rows.csv",
    "results/analysis_summary.json",
    "results/canonical_counts.json",
    "results/exact_result_set.json",
    "results/fixed_one_relator_rows.csv",
    "results/idempotence_certificate.json",
    "results/integrity_audit.json",
    "results/integrity_contract.json",
    "results/manifest_metadata_stability.json",
    "results/metadata_stability.json",
    "results/paired_two_relator_rows.csv",
    "results/prototype_bridge.json",
    "results/random_one_relator_rows.csv",
    "results/reproducibility_certificate.json",
    "results/route_evaluation.json",
    "results/runs/A/route_evaluation.json",
    "results/runs/A/scientific_results.json",
    "results/runs/B/route_evaluation.json",
    "results/runs/B/scientific_results.json",
    "results/runs/C/route_evaluation.json",
    "results/runs/C/scientific_results.json",
    "results/scientific_results.json",
    "results/source_evaluator_boundary.json",
    "results/source_manifest.json",
    "results/test_results.json",
]


def canonical_bytes(payload: object) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=True) + "\n").encode("ascii")


def text_bytes(text: str) -> bytes:
    return (text.rstrip("\n") + "\n").encode("utf-8")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes())


def write_if_changed(path: Path, data: bytes) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_bytes() == data:
        return False
    path.write_bytes(data)
    return True


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def parse_canonical_json(data: bytes, label: str) -> Any:
    require(data.endswith(b"\n") and not data.endswith(b"\n\n"),
            f"{label} does not have exactly one EOF newline")
    payload = json.loads(data)
    require(canonical_bytes(payload) == data, f"{label} is not canonical JSON")
    return payload


def clean_environment(label: str) -> dict[str, str]:
    environment = os.environ.copy()
    environment.pop("PYTHONPATH", None)
    environment.pop("PYTHONHOME", None)
    environment["PYTHONHASHSEED"] = "0"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PAPER37_RUN_LABEL"] = label
    return environment


def run_python(script: Path, label: str, input_bytes: bytes | None = None,
               arguments: list[str] | None = None) -> bytes:
    command = [sys.executable, "-I", "-B", str(script)]
    if arguments:
        command.extend(arguments)
    completed = subprocess.run(
        command,
        cwd=str(script.parent),
        env=clean_environment(label),
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(completed.returncode == 0,
            f"{label} failed: {completed.stderr.decode('utf-8', errors='replace')}")
    require(not completed.stderr,
            f"{label} wrote stderr: {completed.stderr.decode('utf-8', errors='replace')}")
    return completed.stdout


def metadata_envelope(fixtures: dict[str, Any], state: str) -> object:
    if state == "absent":
        return fixtures
    if state == "null":
        metadata: object = None
    elif state == "empty":
        metadata = {}
    elif state == "populated":
        metadata = {
            "environment": "excluded",
            "run_label": "metadata-stability",
            "schema": "transport-metadata-v1",
        }
    else:
        raise ValueError(f"unknown metadata state: {state}")
    return {"fixtures": fixtures, "transport_metadata": metadata}


def route_envelope(science: dict[str, Any], metadata: object = ...) -> object:
    if metadata is ...:
        return science
    return {"scientific_results": science, "integration_metadata": metadata}


def run_evaluator(code_root: Path, packet: object, label: str) -> tuple[bytes, bytes]:
    evaluator_input = canonical_bytes(packet)
    science_bytes = run_python(
        code_root / "evaluator" / "evaluate_packet.py",
        f"{label}-evaluator",
        evaluator_input,
    )
    science = parse_canonical_json(science_bytes, f"{label} science")
    route_bytes = run_python(
        code_root / "evaluator" / "evaluate_route_a.py",
        f"{label}-route",
        science_bytes,
    )
    parse_canonical_json(route_bytes, f"{label} Route evaluation")
    return science_bytes, route_bytes


def run_pipeline(code_root: Path, label: str) -> tuple[bytes, bytes, bytes]:
    source_bytes = run_python(
        code_root / "source" / "emit_packet.py", f"{label}-source"
    )
    fixtures = parse_canonical_json(source_bytes, f"{label} source packet")
    require(isinstance(fixtures, dict), "source packet is not an object")
    science_bytes, route_bytes = run_evaluator(
        code_root, fixtures, label
    )
    return source_bytes, science_bytes, route_bytes


def verify_research_lock() -> dict[str, Any]:
    lock = json.loads((ROOT / "docs" / "RESEARCH_LOCK.json").read_text("utf-8"))
    for path_text, expected in lock["root_authority_files"].items():
        require(file_sha256(ROOT / path_text) == expected,
                f"root authority hash mismatch: {path_text}")
    require(lock["bridge_inputs"] == EXPECTED_BRIDGE_HASHES,
            "recorded bridge hash map differs from the frozen constants")
    for path_text, expected in lock["bridge_inputs"].items():
        path = Path(path_text)
        if path.is_file():
            require(file_sha256(path) == expected,
                    f"available bridge-input hash mismatch: {path_text}")
    for path_text, expected in lock["stable_plan_pointers"].items():
        require(file_sha256(ROOT / path_text) == expected,
                f"stable-plan hash mismatch: {path_text}")
    require(lock["expected_scientific_aggregate_sha256"]
            == EXPECTED_SCIENCE_SHA256, "research-lock science hash mismatch")
    require(file_sha256(ROOT / "SOURCE_LOCK.md")
            == EXPECTED_BRIDGE_HASHES["/tmp/paper37_source_lock.md"],
            "authority SOURCE_LOCK hash differs from the frozen constant")
    return lock


def imported_modules(path: Path) -> set[str]:
    tree = ast.parse(path.read_text("utf-8"), filename=str(path))
    modules: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.add(node.module.split(".")[0])
    return modules


def csv_bytes(fieldnames: list[str], rows: list[dict[str, object]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fieldnames,
                            lineterminator="\n", extrasaction="raise")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def fraction_record(numerator: int, denominator: int) -> dict[str, object]:
    value = Fraction(numerator, denominator)
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "exact": f"{value.numerator}/{value.denominator}",
        "decimal_6dp": f"{float(value):.6f}",
    }


def make_tables(science: dict[str, Any]) -> dict[str, bytes]:
    affine_rows = []
    for row in science["affine_results"]:
        witness = row["mixed"]["shortest_mixed_leak"]
        exponent = int(row["exponent"])
        affine_rows.append({
            "exponent": exponent,
            "parameter_class": row["parameter_class"],
            "direct_factor_cancels": str(
                row["direct"]["direct_factor_cancels"]
            ).lower(),
            "shortest_mixed_word": witness["word"],
            "mixed_word_length": witness["length"],
            "first_supertrace": witness["first_supertrace"],
            "closed_formula_value": -4 * exponent**4 * (exponent - 1),
            "formula_required": str(exponent >= 2).lower(),
        })

    fixed_rows = []
    for row in science["fixed_one_relator_results"]:
        witness = row["mixed"]["shortest_mixed_leak"]
        fixed_rows.append({
            "control_id": row["control_id"],
            "relator": row["direct"]["relator"],
            "direct_factor_cancels": str(
                row["direct"]["direct_factor_cancels"]
            ).lower(),
            "mixed_leak_exists": str(witness is not None).lower(),
            "shortest_mixed_word": "" if witness is None else witness["word"],
            "first_supertrace": "" if witness is None else witness["first_supertrace"],
        })

    random_rows = []
    for row in science["random_one_relator_results"]:
        mixed = row["mixed"]
        witness = None if mixed is None else mixed["shortest_mixed_leak"]
        random_rows.append({
            "control_id": row["control_id"],
            "relator": row["direct"]["relator"],
            "direct_factor_cancels": str(
                row["direct"]["direct_factor_cancels"]
            ).lower(),
            "mixed_evaluated": str(mixed is not None).lower(),
            "mixed_leak_exists": str(witness is not None).lower(),
            "shortest_mixed_word": "" if witness is None else witness["word"],
            "first_supertrace": "" if witness is None else witness["first_supertrace"],
        })

    paired_rows = []
    for row in science["random_presentations"]:
        paired_rows.append({
            "control_id": row["control_id"],
            "relator_1": row["relators"][0],
            "relator_2": row["relators"][1],
            "all_direct_factors_cancel": str(
                row["all_direct_factors_cancel"]
            ).lower(),
            "mixed_leak_after_direct_hit": str(
                row["mixed_leak_after_direct_hit"]
            ).lower(),
        })

    return {
        "results/affine_rows.csv": csv_bytes(
            ["exponent", "parameter_class", "direct_factor_cancels",
             "shortest_mixed_word", "mixed_word_length", "first_supertrace",
             "closed_formula_value", "formula_required"], affine_rows
        ),
        "results/fixed_one_relator_rows.csv": csv_bytes(
            ["control_id", "relator", "direct_factor_cancels",
             "mixed_leak_exists", "shortest_mixed_word", "first_supertrace"],
            fixed_rows,
        ),
        "results/random_one_relator_rows.csv": csv_bytes(
            ["control_id", "relator", "direct_factor_cancels",
             "mixed_evaluated", "mixed_leak_exists", "shortest_mixed_word",
             "first_supertrace"], random_rows
        ),
        "results/paired_two_relator_rows.csv": csv_bytes(
            ["control_id", "relator_1", "relator_2",
             "all_direct_factors_cancel", "mixed_leak_after_direct_hit"],
            paired_rows,
        ),
    }


def make_analysis(route: dict[str, Any]) -> dict[str, Any]:
    counts = route["canonical_counts"]
    affine_rate = fraction_record(counts["affine_direct_cancellations"],
                                  counts["affine_rows"])
    random_rate = fraction_record(counts["random_direct_cancellations"],
                                  counts["random_one_relator_rows"])
    direct_rate_delta = fraction_record(
        counts["affine_direct_cancellations"]
        * counts["random_one_relator_rows"]
        - counts["random_direct_cancellations"] * counts["affine_rows"],
        counts["affine_rows"] * counts["random_one_relator_rows"],
    )
    return {
        "schema": "paper37-analysis-summary-v1",
        "candidate": "SD-C39",
        "raw_tables": [
            "results/affine_rows.csv",
            "results/fixed_one_relator_rows.csv",
            "results/random_one_relator_rows.csv",
            "results/paired_two_relator_rows.csv",
        ],
        "rates": {
            "affine_direct_cancellation": affine_rate,
            "random_direct_cancellation": random_rate,
            "affine_minus_random_direct_rate": direct_rate_delta,
            "random_conditional_mixed_leak": fraction_record(
                counts["random_mixed_leaks_after_direct"],
                counts["random_direct_cancellations"],
            ),
            "paired_all_direct_match": fraction_record(
                counts["paired_all_direct_cancellations"],
                counts["paired_two_relator_rows"],
            ),
            "paired_conditional_mixed_leak": fraction_record(
                counts["paired_mixed_leaks_after_all_direct"],
                counts["paired_all_direct_cancellations"],
            ),
        },
        "findings": [
            {
                "observation": "All 8 affine direct factors cancel, while all 8 bounded affine rows leak on a primitive mixed word.",
                "interpretation": "Direct-cell spectral matching is exact but does not extend multiplicatively to mixed normal-closure products.",
                "implication": "The graded fixture cannot erase the complete relation ledger.",
                "next_step": "No further coefficient refit is allowed; retain the theorem-owned saturation stop.",
            },
            {
                "observation": "Only 9 of 48 random relators match directly, and all 9 conditional cases leak; 2 of 24 paired controls match both direct factors and both leak.",
                "interpretation": "Direct matching can occur accidentally in generic syntax without producing selective arithmetic recurrence.",
                "implication": "The observed survival pattern fails the generic firewall.",
                "next_step": "Close SD-C39 under strict Route A and keep Route B locked.",
            },
        ],
        "scientific_conclusion": "negative_confirmed",
        "route_conclusion": "ROUTE_A_REJECTED",
    }


def make_report(route: dict[str, Any], analysis: dict[str, Any],
                reproducibility: dict[str, Any], test_summary: dict[str, Any]) -> str:
    counts = route["canonical_counts"]
    rates = analysis["rates"]
    lines = [
        "# Paper 37 exact experiment report — SD-C39",
        "",
        "## Outcome",
        "",
        "The frozen prototype is reproduced exactly and the negative Route-A",
        "conclusion is confirmed: `STOP_LOCAL_COEFFICIENT_SATURATION` /",
        "`ROUTE_A_REJECTED`. The same-object analytic determinant exists, but",
        "direct graded relator cancellation leaks on mixed consequences; full",
        "normal-closure saturation is theorem-owned and erases every closed",
        "factor. Route B remains locked.",
        "",
        "## Canonical exact counts",
        "",
        "| Evidence | Exact result |",
        "|---|---:|",
        f"| evaluator assertions | {counts['exact_checks_passed']}/{counts['exact_checks_total']} |",
        f"| affine direct cancellations | {counts['affine_direct_cancellations']}/{counts['affine_rows']} |",
        f"| affine bounded mixed leaks | {counts['affine_mixed_leaks']}/{counts['affine_rows']} |",
        f"| random direct cancellations | {counts['random_direct_cancellations']}/{counts['random_one_relator_rows']} |",
        f"| random conditional mixed leaks | {counts['random_mixed_leaks_after_direct']}/{counts['random_direct_cancellations']} |",
        f"| paired all-direct matches | {counts['paired_all_direct_cancellations']}/{counts['paired_two_relator_rows']} |",
        f"| paired conditional mixed leaks | {counts['paired_mixed_leaks_after_all_direct']}/{counts['paired_all_direct_cancellations']} |",
        "",
        f"The affine direct-match rate is `{rates['affine_direct_cancellation']['exact']}`;",
        f"the random-control rate is `{rates['random_direct_cancellation']['exact']}`,",
        f"an exact difference of `{rates['affine_minus_random_direct_rate']['exact']}`.",
        "Every preregistered affine row with `r>=2` matches",
        "`-4*r^4*(r-1)` exactly.",
        "",
        "## Reproducibility and separation",
        "",
        f"- Fresh/cold runs: {reproducibility['byte_identical_run_count']}/3 byte-identical.",
        "- Run C executed from an isolated temporary code copy that was removed.",
        "- Source and evaluator use disjoint directories and a JSON-only",
        "  subprocess boundary; neither imports the other.",
        "- Metadata states absent/null/empty/populated and simulated future",
        "  manifest absence/presence leave scientific and Route bytes unchanged.",
        f"- Integration checks: {test_summary['passed']}/{test_summary['total']}.",
        f"- Scientific aggregate SHA-256: `{EXPECTED_SCIENCE_SHA256}`.",
        "",
        "## Evidence boundary",
        "",
        "The CSV files are the raw finite tables; `results/analysis_summary.json`",
        "contains exact rational rates and their baseline delta. These finite",
        "runs audit formulas, controls, separation, and reproducibility. They do",
        "not prove trace class, the arbitrary-rank nilpotence criterion, or the",
        "normal-closure saturation theorem.",
    ]
    return "\n".join(lines)


def managed_files() -> list[Path]:
    files: list[Path] = []
    for dirname in ("code", "results", "experiments", "docs"):
        base = ROOT / dirname
        if base.exists():
            files.extend(path for path in base.rglob("*") if path.is_file())
    if EVALUATION_DIR.exists():
        files.extend(path for path in EVALUATION_DIR.rglob("*") if path.is_file())
    if (ROOT / "EXPERIMENT_REPORT.md").is_file():
        files.append(ROOT / "EXPERIMENT_REPORT.md")
    return sorted(set(files), key=lambda path: path.relative_to(ROOT).as_posix())


def forbidden_cache_paths() -> list[str]:
    bad = []
    for base_name in ("code", "results", "experiments", "docs", "evaluations"):
        base = ROOT / base_name
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if (path.name in {"__pycache__", ".pytest_cache"}
                    or path.suffix in {".pyc", ".pyo"}):
                bad.append(path.relative_to(ROOT).as_posix())
    return sorted(bad)


def canonical_text_violations(paths: list[Path]) -> list[str]:
    bad = []
    for path in paths:
        data = path.read_bytes()
        rel = path.relative_to(ROOT).as_posix()
        try:
            data.decode("utf-8")
        except UnicodeDecodeError:
            bad.append(f"{rel}:not-utf8")
            continue
        if data.startswith(b"\xef\xbb\xbf"):
            bad.append(f"{rel}:bom")
        if b"\r" in data:
            bad.append(f"{rel}:cr")
        if not data.endswith(b"\n") or data.endswith(b"\n\n"):
            bad.append(f"{rel}:eof-newline")
    return bad


def make_ledger() -> bytes:
    exclusions = {
        LEDGER.resolve(),
        ROUTE_CARD.resolve(),
        PAPER_MANIFEST.resolve(),
    }
    entries = []
    for path in managed_files():
        if path.resolve() in exclusions:
            continue
        rel = path.relative_to(ROOT).as_posix()
        entries.append(f"{file_sha256(path)}  {rel}")
    require(entries == sorted(entries, key=lambda row: row.split("  ", 1)[1]),
            "ledger paths are not sorted")
    return text_bytes("\n".join(entries))


def main() -> int:
    RESULTS.mkdir(parents=True, exist_ok=True)
    EVALUATION_DIR.mkdir(parents=True, exist_ok=True)
    require(not PAPER_MANIFEST.exists(),
            "Stage-1 integration must not create PAPER_MANIFEST.sha256")
    research_lock = verify_research_lock()

    source_core = CODE / "source" / "source_core.py"
    evaluator_core = CODE / "evaluator" / "independent_evaluator.py"
    require(file_sha256(source_core) == EXPECTED_SOURCE_CORE_SHA256,
            "bridged source core differs from prototype")
    require(file_sha256(evaluator_core) == EXPECTED_EVALUATOR_CORE_SHA256,
            "bridged evaluator core differs from prototype")
    require("independent_evaluator" not in imported_modules(source_core),
            "source core imports evaluator code")
    require("source_core" not in imported_modules(evaluator_core),
            "evaluator core imports source code")

    source_a, science_a, route_a = run_pipeline(CODE, "A")
    require(sha256(science_a) == EXPECTED_SCIENCE_SHA256,
            "sanity run does not bridge the frozen scientific aggregate")
    source_b, science_b, route_b = run_pipeline(CODE, "B")

    with tempfile.TemporaryDirectory(prefix=".paper37-cold-c-", dir=RESULTS) as tmp:
        cold_root = Path(tmp) / "code"
        shutil.copytree(CODE / "source", cold_root / "source")
        shutil.copytree(CODE / "evaluator", cold_root / "evaluator")
        source_c, science_c, route_c = run_pipeline(cold_root, "C-cold")
    require(not any(path.name.startswith(".paper37-cold-c-")
                    for path in RESULTS.iterdir()), "cold-run directory was retained")

    require(source_a == source_b == source_c,
            "A/B/C source fixture packets differ")
    require(science_a == science_b == science_c,
            "A/B/C scientific outputs differ")
    require(route_a == route_b == route_c,
            "A/B/C Route evaluations differ")

    fixtures = parse_canonical_json(source_a, "canonical source packet")
    science = parse_canonical_json(science_a, "canonical science")
    route = parse_canonical_json(route_a, "canonical Route evaluation")

    metadata_rows = []
    for state in ("absent", "null", "empty", "populated"):
        packet = metadata_envelope(fixtures, state)
        state_science, _ = run_evaluator(CODE, packet, f"metadata-{state}")
        state_payload = parse_canonical_json(
            state_science, f"metadata-{state} science"
        )
        if state == "absent":
            route_packet = route_envelope(state_payload)
        elif state == "null":
            route_packet = route_envelope(state_payload, None)
        elif state == "empty":
            route_packet = route_envelope(state_payload, {})
        else:
            route_packet = route_envelope(
                state_payload, {"state": "populated", "value": "excluded"}
            )
        state_route = run_python(
            CODE / "evaluator" / "evaluate_route_a.py",
            f"metadata-{state}-route-stability",
            canonical_bytes(route_packet),
        )
        parse_canonical_json(state_route, f"metadata-{state} Route")
        metadata_rows.append({
            "state": state,
            "source_envelope_sha256": sha256(canonical_bytes(packet)),
            "scientific_sha256": sha256(state_science),
            "route_evaluation_sha256": sha256(state_route),
        })
        require(state_science == science_a,
                f"scientific bytes changed under {state} metadata")
        require(state_route == route_a,
                f"Route bytes changed under {state} metadata")

    manifest_rows = []
    manifest_metadata = {
        "absent": {"paper_manifest": {"state": "absent"}},
        "present": {
            "paper_manifest": {
                "state": "present",
                "sha256": "0" * 64,
                "path": "PAPER_MANIFEST.sha256",
            }
        },
    }
    for state, metadata in manifest_metadata.items():
        result = run_python(
            CODE / "evaluator" / "evaluate_route_a.py",
            f"manifest-{state}-route",
            canonical_bytes(route_envelope(science, metadata)),
        )
        parse_canonical_json(result, f"manifest-{state} Route")
        require(result == route_a,
                f"Route bytes changed with manifest metadata {state}")
        manifest_rows.append({
            "state": state,
            "route_evaluation_sha256": sha256(result),
            "scientific_aggregate_sha256": sha256(science_a),
        })

    counts = route["canonical_counts"]
    reproducibility = {
        "schema": "paper37-fresh-ab-cold-c-v1",
        "runs": [
            {"run": "A", "mode": "fresh", "source_packet_sha256": sha256(source_a),
             "scientific_sha256": sha256(science_a), "route_sha256": sha256(route_a)},
            {"run": "B", "mode": "fresh", "source_packet_sha256": sha256(source_b),
             "scientific_sha256": sha256(science_b), "route_sha256": sha256(route_b)},
            {"run": "C", "mode": "cold_isolated_copy", "source_packet_sha256": sha256(source_c),
             "scientific_sha256": sha256(science_c), "route_sha256": sha256(route_c)},
        ],
        "byte_identical_run_count": 3,
        "source_packets_byte_identical": True,
        "scientific_results_byte_identical": True,
        "route_evaluations_byte_identical": True,
        "cold_copy_removed": True,
        "python_version_metadata": sys.version.split()[0],
        "environment_metadata_excluded_from_scientific_payload": True,
    }
    metadata_certificate = {
        "schema": "paper37-four-state-metadata-stability-v1",
        "states": metadata_rows,
        "state_order": ["absent", "null", "empty", "populated"],
        "scientific_bytes_stable": True,
        "route_bytes_stable": True,
    }
    manifest_certificate = {
        "schema": "paper37-manifest-metadata-stability-v1",
        "actual_stage1_manifest_state": "absent",
        "simulated_states": manifest_rows,
        "scientific_bytes_stable": True,
        "route_bytes_stable": True,
        "excluded_from_immutable_ledger": True,
        "excluded_from_canonical_text_count": True,
    }
    boundary = {
        "schema": "paper37-source-evaluator-boundary-v1",
        "source_directory": "code/source",
        "evaluator_directory": "code/evaluator",
        "physical_directories_disjoint": True,
        "transport": "canonical_json_subprocess_stdin_stdout",
        "source_imports_evaluator": False,
        "evaluator_imports_source": False,
        "source_packet_sha256": sha256(source_a),
        "source_core_sha256": file_sha256(source_core),
        "evaluator_core_sha256": file_sha256(evaluator_core),
    }
    prototype_bridge = {
        "schema": "paper37-prototype-bridge-v1",
        "source_core_byte_preserved": True,
        "evaluator_core_byte_preserved": True,
        "source_core_sha256": file_sha256(source_core),
        "evaluator_core_sha256": file_sha256(evaluator_core),
        "prototype_scientific_sha256_expected": EXPECTED_SCIENCE_SHA256,
        "integrated_scientific_sha256_observed": sha256(science_a),
        "scientific_payload_byte_preserved": True,
        "research_package_sha256": research_lock["bridge_inputs"][
            "/tmp/paper37_research_package.md"
        ],
        "source_lock_sha256": research_lock["bridge_inputs"][
            "/tmp/paper37_source_lock.md"
        ],
        "external_bridge_observability": {
            path_text: {
                "available_at_freeze": Path(path_text).is_file(),
                "hash_matches_if_available": (
                    not Path(path_text).is_file()
                    or file_sha256(Path(path_text)) == expected
                ),
            }
            for path_text, expected in sorted(EXPECTED_BRIDGE_HASHES.items())
        },
        "external_bridge_availability_is_terminal_gate": False,
    }
    source_manifest = {
        "schema": "paper37-integrated-code-manifest-v1",
        "files": {
            path.relative_to(ROOT).as_posix(): {
                "bytes": len(path.read_bytes()),
                "sha256": file_sha256(path),
            }
            for path in sorted(CODE.rglob("*.py"))
        },
    }
    analysis = make_analysis(route)
    tables = make_tables(science)

    primary: dict[str, bytes] = {
        "results/scientific_results.json": science_a,
        "results/route_evaluation.json": route_a,
        "results/runs/A/scientific_results.json": science_a,
        "results/runs/A/route_evaluation.json": route_a,
        "results/runs/B/scientific_results.json": science_b,
        "results/runs/B/route_evaluation.json": route_b,
        "results/runs/C/scientific_results.json": science_c,
        "results/runs/C/route_evaluation.json": route_c,
        "results/reproducibility_certificate.json": canonical_bytes(reproducibility),
        "results/metadata_stability.json": canonical_bytes(metadata_certificate),
        "results/manifest_metadata_stability.json": canonical_bytes(manifest_certificate),
        "results/source_evaluator_boundary.json": canonical_bytes(boundary),
        "results/prototype_bridge.json": canonical_bytes(prototype_bridge),
        "results/source_manifest.json": canonical_bytes(source_manifest),
        "results/canonical_counts.json": canonical_bytes({
            "schema": "paper37-canonical-counts-v1",
            "candidate": "SD-C39",
            "counts": counts,
        }),
        "results/analysis_summary.json": canonical_bytes(analysis),
        "evaluations/route_a/SD-C39/independent_evaluation.json": route_a,
    }
    primary.update(tables)

    first_changed = []
    for rel, data in primary.items():
        if write_if_changed(ROOT / rel, data):
            first_changed.append(rel)
    second_changed = []
    for rel, data in primary.items():
        if write_if_changed(ROOT / rel, data):
            second_changed.append(rel)
    require(not second_changed, "second primary materialization was not idempotent")
    primary_aggregate = sha256(canonical_bytes({
        rel: sha256(data) for rel, data in sorted(primary.items())
    }))
    idempotence = {
        "schema": "paper37-idempotence-certificate-v1",
        "primary_artifact_count": len(primary),
        "first_materialization_completed": True,
        "second_materialization_changed_paths": second_changed,
        "second_materialization_byte_identical": True,
        "primary_artifact_hash_aggregate": primary_aggregate,
        "timestamps_excluded": True,
    }
    write_if_changed(RESULTS / "idempotence_certificate.json",
                     canonical_bytes(idempotence))

    test_rows = [
        ("research_lock_verified", True),
        ("source_core_bridge_hash", file_sha256(source_core) == EXPECTED_SOURCE_CORE_SHA256),
        ("evaluator_core_bridge_hash", file_sha256(evaluator_core) == EXPECTED_EVALUATOR_CORE_SHA256),
        ("source_does_not_import_evaluator", "independent_evaluator" not in imported_modules(source_core)),
        ("evaluator_does_not_import_source", "source_core" not in imported_modules(evaluator_core)),
        ("fresh_a_science_hash", sha256(science_a) == EXPECTED_SCIENCE_SHA256),
        ("fresh_b_science_hash", sha256(science_b) == EXPECTED_SCIENCE_SHA256),
        ("cold_c_science_hash", sha256(science_c) == EXPECTED_SCIENCE_SHA256),
        ("abc_science_byte_identity", science_a == science_b == science_c),
        ("abc_route_byte_identity", route_a == route_b == route_c),
        ("cold_copy_removed", reproducibility["cold_copy_removed"] is True),
        ("metadata_state_count_four", len(metadata_rows) == 4),
        ("metadata_science_stable", all(row["scientific_sha256"] == EXPECTED_SCIENCE_SHA256 for row in metadata_rows)),
        ("metadata_route_stable", len({row["route_evaluation_sha256"] for row in metadata_rows}) == 1),
        ("manifest_state_count_two", len(manifest_rows) == 2),
        ("manifest_route_stable", len({row["route_evaluation_sha256"] for row in manifest_rows}) == 1),
        ("exact_checks_131", counts["exact_checks_passed"] == counts["exact_checks_total"] == 131),
        ("affine_rows_8", counts["affine_rows"] == 8),
        ("affine_direct_8", counts["affine_direct_cancellations"] == 8),
        ("affine_leaks_8", counts["affine_mixed_leaks"] == 8),
        ("fixed_rows_6", counts["fixed_one_relator_rows"] == 6),
        ("random_rows_48", counts["random_one_relator_rows"] == 48),
        ("random_direct_9", counts["random_direct_cancellations"] == 9),
        ("random_conditional_leaks_9", counts["random_mixed_leaks_after_direct"] == 9),
        ("paired_rows_24", counts["paired_two_relator_rows"] == 24),
        ("paired_direct_2", counts["paired_all_direct_cancellations"] == 2),
        ("paired_conditional_leaks_2", counts["paired_mixed_leaks_after_all_direct"] == 2),
        ("route_rejected", route["overall"] == "ROUTE_A_REJECTED"),
        ("route_b_locked", route["route_b_invocation_allowed"] is False),
        ("primary_idempotence", not second_changed),
        ("stage1_manifest_absent", not PAPER_MANIFEST.exists()),
        ("no_cache_before_freeze", not forbidden_cache_paths()),
    ]
    failed = [name for name, passed in test_rows if not passed]
    require(not failed, f"integration checks failed: {failed!r}")
    test_summary = {
        "schema": "paper37-integration-tests-v1",
        "tests": [{"name": name, "passed": passed} for name, passed in test_rows],
        "passed": sum(int(passed) for _, passed in test_rows),
        "total": len(test_rows),
        "failed": failed,
    }
    write_if_changed(RESULTS / "test_results.json", canonical_bytes(test_summary))

    report = make_report(route, analysis, reproducibility, test_summary)
    write_if_changed(ROOT / "EXPERIMENT_REPORT.md",
                     text_bytes(report))

    integrity_contract = {
        "schema": "paper37-integrity-contract-v1",
        "managed_roots": ["EXPERIMENT_REPORT.md", "code", "results",
                          "experiments", "docs", "evaluations/route_a/SD-C39"],
        "immutable_ledger": "results/SHA256SUMS.txt",
        "ledger_exclusions": [
            "results/SHA256SUMS.txt",
            "evaluations/route_a/SD-C39/2026-08-15.yaml",
            "PAPER_MANIFEST.sha256",
        ],
        "paper_manifest_stage1": "ABSENT",
        "canonical_text_exclusions": ["PAPER_MANIFEST.sha256"],
        "text_encoding": "UTF-8",
        "line_ending": "LF",
        "eof_newline_count": 1,
        "cache_allowed": False,
        "expected_result_paths": EXPECTED_RESULT_PATHS,
    }
    write_if_changed(RESULTS / "integrity_contract.json",
                     canonical_bytes(integrity_contract))
    exact_result_set = {
        "schema": "paper37-exact-result-set-v1",
        "candidate": "SD-C39",
        "paths": EXPECTED_RESULT_PATHS,
        "path_count": len(EXPECTED_RESULT_PATHS),
        "closed_set": True,
    }
    write_if_changed(RESULTS / "exact_result_set.json",
                     canonical_bytes(exact_result_set))

    require(not forbidden_cache_paths(),
            f"cache residue before ledger: {forbidden_cache_paths()!r}")
    preledger_paths = [path for path in managed_files()
                       if path.resolve() != LEDGER.resolve()]
    violations = canonical_text_violations(preledger_paths)
    require(not violations, f"text hygiene violations: {violations!r}")

    audit_prepare_bytes = run_python(
        CODE / "audit_integrity.py",
        "integrity-audit-prepare",
        arguments=["--prepare"],
    )
    audit_prepare = parse_canonical_json(
        audit_prepare_bytes, "prepared full integrity audit"
    )
    require(audit_prepare["all_pass"] is True,
            "prepared full integrity audit did not pass")
    write_if_changed(RESULTS / "integrity_audit.json", audit_prepare_bytes)

    ledger_bytes = make_ledger()
    write_if_changed(LEDGER, ledger_bytes)

    audit_final_bytes = run_python(
        CODE / "audit_integrity.py", "integrity-audit-final"
    )
    audit_final = parse_canonical_json(
        audit_final_bytes, "final full integrity audit"
    )
    require(audit_final["all_pass"] is True,
            "final full integrity audit did not pass")
    require(audit_final_bytes == audit_prepare_bytes,
            "prepared/final integrity audit fixed point differs")
    audit_hidden_bytes = run_python(
        CODE / "audit_integrity.py",
        "integrity-audit-clean-clone-simulation",
        arguments=["--hide-external-provenance"],
    )
    audit_hidden = parse_canonical_json(
        audit_hidden_bytes, "clean-clone provenance-isolation audit"
    )
    require(audit_hidden["all_pass"] is True,
            "clean-clone provenance-isolation audit did not pass")
    require(audit_hidden_bytes == audit_final_bytes,
            "optional external provenance changed the integrity verdict")

    actual_results = sorted(
        path.relative_to(ROOT).as_posix()
        for path in RESULTS.rglob("*") if path.is_file()
    )
    require(actual_results == EXPECTED_RESULT_PATHS,
            f"exact result set mismatch: {actual_results!r}")
    final_paths = managed_files()
    violations = canonical_text_violations(final_paths)
    require(not violations, f"final text hygiene violations: {violations!r}")
    require(not forbidden_cache_paths(),
            f"final cache residue: {forbidden_cache_paths()!r}")

    print(f"evaluator_checks={counts['exact_checks_passed']}/{counts['exact_checks_total']}")
    print(f"integration_tests={test_summary['passed']}/{test_summary['total']}")
    print(f"integrity_audit={audit_final['passed']}/{audit_final['total']}")
    for group_name, group in sorted(audit_final["groups"].items()):
        print(f"integrity_{group_name}={group['passed']}/{group['total']}")
    print(f"scientific_aggregate_sha256={sha256(science_a)}")
    print(f"route_evaluation_sha256={sha256(route_a)}")
    print(f"route_card_sha256={file_sha256(ROUTE_CARD)}")
    print(f"experiment_report_sha256={file_sha256(ROOT / 'EXPERIMENT_REPORT.md')}")
    print(f"immutable_ledger_sha256={file_sha256(LEDGER)}")
    print(f"immutable_ledger_entries={len(ledger_bytes.decode('utf-8').splitlines())}")
    print(f"canonical_text_files={len(final_paths)}")
    print("fresh_a_b_c=PASS")
    print("metadata_four_state=PASS")
    print("manifest_absent_present_stability=PASS")
    print("clean_clone_external_provenance_absent=PASS")
    print("stage1_manifest=ABSENT")
    print("strict_route_a=ROUTE_A_REJECTED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
