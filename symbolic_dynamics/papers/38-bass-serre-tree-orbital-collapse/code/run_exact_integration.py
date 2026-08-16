#!/usr/bin/env python3
"""Build the exact Paper 38 evidence and strict Route-A Stage-1 artifacts."""

from __future__ import annotations

import ast
import csv
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
EVALUATION_DIR = ROOT / "evaluations" / "route_a" / "SD-C40"
ROUTE_CARD = EVALUATION_DIR / "2026-08-15.yaml"
LEDGER = RESULTS / "SHA256SUMS.txt"
PAPER_MANIFEST = ROOT / "PAPER_MANIFEST.sha256"

EXPECTED_SCIENCE_SHA256 = (
    "a9ffa66d826bcaf8eef0b00991aafa46cdbeaca7014430c68aacf070446adf24"
)
PROTOTYPE_SEED_SCIENCE_SHA256 = (
    "3485a1d925924459ce92ff3aeddb31302277589d61bd9d961ecb823b1e5bb089"
)
UNAFFECTED_PROJECTION_SHA256 = (
    "47ad757f78b3b634003082bd8504ce36ad8a3915afbf7ae96aa0616f07693198"
)
EXPECTED_SOURCE_CORE_SHA256 = (
    "e023f2c399ddc5b7981a0b7b78cb33934f6ee03e5e6e2d6f34934864c07c3c1d"
)
EXPECTED_EVALUATOR_CORE_SHA256 = (
    "0934d99fa05329d8146467e903b57f36e23588ce977354f3e948777c8ec5da13"
)
EXPECTED_PLAN_POINTERS = {
    "experiments/EXPERIMENT_PLAN.md":
        "fb4a332d3e72f14694c5294761619fd703bb236e0b401ab0d76701fc8b2f2e2b",
    "experiments/PREREGISTRATION.md":
        "18ada0cb02ab2af8473d37643f845aaffdde51d447d54e5cacc6a88b93c65423",
}
EXPECTED_RESEARCH_AUTHORITY = {
    "DERIVATION_PACKAGE.md":
        "18c07306c64297338d6b85b4f830ce0ccd15317ec0ee22f0e57823064171307a",
    "LITERATURE_AUDIT.md":
        "dd3b0e2e0258a6423f7a43266ca19d9597e1b3353e8491f7d51a81ab70b302d7",
    "PREREGISTRATION.md":
        "606541a6852e9953882ba07bcaaa12efe06ab7f2a5c25346486a48c19fdbed2f",
    "PROOF_PACKAGE.md":
        "fdb49515d5baafc2baa00e5e3d510d940c6af813f8a32ce56e3116171f7b6d73",
    "SOURCE_LOCK.md":
        "febaeb0b1db1a0713bbb68cf99110d7ecf2df8b39caf3ee9f311598f45fa6a7a",
}
EXPECTED_CORRECTED_PROTOTYPE_LOCK_SHA256 = (
    "7a25ecee27974aa1f593f4793c7f44b8a940ad1b13f824f0a5f3c11669290c5b"
)
EXPECTED_PROTOTYPE_PROVENANCE = {
    "/tmp/paper38_exact_prototype/EXPERIMENT_PLAN.md":
        "2d1cbc15aba2f144a99df61b929da32c0a30378b1f730999d3b753538baadb9c",
    "/tmp/paper38_exact_prototype/PREREGISTRATION.md":
        "e5d010d1acdfee84325601a253eda4e0596b29509cf06b56f3af82fc61003cca",
    "/tmp/paper38_exact_prototype/independent_evaluator.py":
        "ec2bdfed0fa7e26b98b7d0d70b4d286d7b855b2065996432308a8eca59fbf3b7",
    "/tmp/paper38_exact_prototype/run_exact.py":
        "06d23fbf5f2c7fa87aa609cb1f1908f8587c5142794847b17641fce2796aa508",
    "/tmp/paper38_exact_prototype/source_core.py":
        "e023f2c399ddc5b7981a0b7b78cb33934f6ee03e5e6e2d6f34934864c07c3c1d",
}
EXPECTED_RESEARCH_PROVENANCE = {
    "/tmp/paper38_research_package.md":
        "208e839b8379d0e30a2f3647fe7a52f543ead2c9d1dcf57d1c0271dbe525f0c3",
    "/tmp/paper38_route_v0_2.yaml":
        "34529b3fdd42d07311ff1995c81b04cb3ca8559b61fcecc3c841dd3583505983",
    "/tmp/paper38_source_lock.md":
        "34acddf6573a11adbd80adafa97e58cb1ac30be7a75a2c555443cbc7ee8762e0",
}
EXPECTED_RESULT_PATHS = [
    "results/SHA256SUMS.txt",
    "results/analysis_summary.json",
    "results/canonical_counts.json",
    "results/exact_result_set.json",
    "results/finite_tree_rows.csv",
    "results/gbs_rows.csv",
    "results/idempotence_certificate.json",
    "results/integrity_audit.json",
    "results/integrity_contract.json",
    "results/manifest_metadata_stability.json",
    "results/marker_rows.csv",
    "results/metadata_stability.json",
    "results/noncompact_rows.csv",
    "results/orbital_parameter_rows.csv",
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
    return (
        json.dumps(payload, sort_keys=True, separators=(",", ":"),
                   ensure_ascii=True) + "\n"
    ).encode("ascii")


def unaffected_science_projection(payload: dict[str, Any]) -> dict[str, Any]:
    """Remove only the corrected action-topology normalization fields."""
    projected = json.loads(json.dumps(payload))
    action_fields = {
        "action_discrete_in_Aut_tree",
        "aut_tree_image_discrete",
        "bass_serre_action_faithful",
        "action_kernel",
        "action_proper",
        "finite_stabilizer_tree_lattice_hypotheses_met",
    }
    theorem_fields = {
        "infinite_stabilizer_implies_action_not_discrete",
        "tree_lattice_zeta_hypotheses_fail",
        "r_ge_2_faithful_image_non_discrete",
        "r1_image_discrete_but_infinite_kernel",
        "all_r_bass_serre_action_nonproper",
        "tree_lattice_finite_stabilizer_hypotheses_fail",
    }
    for row in projected["parameter_results"]:
        for key in action_fields:
            row.pop(key, None)
    projected["theorem_boundary"] = {
        key: value for key, value in projected["theorem_boundary"].items()
        if key not in theorem_fields
    }
    projected["checks"] = [
        row for row in projected["checks"]
        if not (
            row["name"].startswith("r")
            and (
                row["name"].endswith(":not_discrete")
                or row["name"].endswith(":action_topology")
            )
        )
    ]
    return projected


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
    environment["PAPER38_RUN_LABEL"] = label
    return environment


def run_python(
    script: Path,
    label: str,
    input_bytes: bytes | None = None,
    arguments: list[str] | None = None,
) -> bytes:
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
    require(
        completed.returncode == 0,
        f"{label} failed: {completed.stderr.decode('utf-8', errors='replace')}",
    )
    require(
        not completed.stderr,
        f"{label} wrote stderr: {completed.stderr.decode('utf-8', errors='replace')}",
    )
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


def run_evaluator(
    code_root: Path, packet: object, label: str
) -> tuple[bytes, bytes]:
    science_bytes = run_python(
        code_root / "evaluator" / "evaluate_packet.py",
        f"{label}-evaluator",
        canonical_bytes(packet),
    )
    science = parse_canonical_json(science_bytes, f"{label} science")
    route_bytes = run_python(
        code_root / "evaluator" / "evaluate_route_a.py",
        f"{label}-route",
        canonical_bytes(science),
    )
    parse_canonical_json(route_bytes, f"{label} Route evaluation")
    return science_bytes, route_bytes


def run_pipeline(code_root: Path, label: str) -> tuple[bytes, bytes, bytes]:
    source_bytes = run_python(
        code_root / "source" / "emit_packet.py", f"{label}-source"
    )
    fixtures = parse_canonical_json(source_bytes, f"{label} source packet")
    require(isinstance(fixtures, dict), "source packet is not a JSON object")
    science_bytes, route_bytes = run_evaluator(code_root, fixtures, label)
    return source_bytes, science_bytes, route_bytes


def verify_research_lock() -> dict[str, Any]:
    lock = json.loads((ROOT / "docs" / "RESEARCH_LOCK.json").read_text("utf-8"))
    require(lock["schema"] == "paper38-research-lock-v2",
            "research lock schema is not v2")
    require(lock["locked_research_authority"] == EXPECTED_RESEARCH_AUTHORITY,
            "stable five-file research authority map differs")
    require(lock["stable_plan_pointers"] == EXPECTED_PLAN_POINTERS,
            "stable experiment-plan map differs")
    require(lock["prototype_provenance"] == EXPECTED_PROTOTYPE_PROVENANCE,
            "prototype provenance map differs")
    require(lock["research_provenance"] == EXPECTED_RESEARCH_PROVENANCE,
            "research provenance map differs")
    require(lock["provenance_policy"]["locked_research_file_count"] == 5,
            "research lock does not declare exactly five stable files")
    require(lock["corrected_prototype_witness"] == {
        "path": "docs/CORRECTED_PROTOTYPE_LOCK.json",
        "sha256": EXPECTED_CORRECTED_PROTOTYPE_LOCK_SHA256,
    }, "corrected prototype witness pointer differs")
    require(file_sha256(ROOT / "docs" / "CORRECTED_PROTOTYPE_LOCK.json")
            == EXPECTED_CORRECTED_PROTOTYPE_LOCK_SHA256,
            "corrected prototype witness hash mismatch")
    require(
        lock["normalization_v2"]["authority_science_sha256"]
        == EXPECTED_SCIENCE_SHA256
        and lock["normalization_v2"]["authority_evaluator_sha256"]
        == EXPECTED_EVALUATOR_CORE_SHA256
        and lock["normalization_v2"]["legacy_science_sha256"]
        == PROTOTYPE_SEED_SCIENCE_SHA256
        and lock["normalization_v2"]["unaffected_projection_sha256"]
        == UNAFFECTED_PROJECTION_SHA256
        and lock["normalization_v2"]["route_tuple_changed"] is False,
        "v2 normalization provenance differs",
    )
    for path_text, expected in EXPECTED_RESEARCH_AUTHORITY.items():
        require(file_sha256(ROOT / path_text) == expected,
                f"stable research hash mismatch: {path_text}")
    for path_text, expected in EXPECTED_PLAN_POINTERS.items():
        require(file_sha256(ROOT / path_text) == expected,
                f"stable plan hash mismatch: {path_text}")
    external = {**EXPECTED_PROTOTYPE_PROVENANCE, **EXPECTED_RESEARCH_PROVENANCE}
    for path_text, expected in external.items():
        path = Path(path_text)
        if external_provenance_visible() and path.is_file():
            require(file_sha256(path) == expected,
                    f"available external provenance mismatch: {path_text}")
    require(lock["expected_scientific_aggregate_sha256"]
            == EXPECTED_SCIENCE_SHA256, "science lock mismatch")
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


def external_provenance_visible() -> bool:
    """Allow an exact clean-clone run to hide optional /tmp provenance."""
    return os.environ.get("PAPER38_HIDE_EXTERNAL_PROVENANCE", "0") != "1"


def csv_bytes(fieldnames: list[str], rows: list[dict[str, object]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(
        stream,
        fieldnames=fieldnames,
        lineterminator="\n",
        extrasaction="raise",
    )
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def bool_text(value: object) -> str:
    return str(bool(value)).lower()


def make_tables(science: dict[str, Any]) -> dict[str, bytes]:
    parameter_rows = []
    for row in science["parameter_results"]:
        parameter_rows.append({
            "r": row["r"],
            "declared_class": row["declared_class"],
            "tree_degree": row["tree_degree"],
            "aut_tree_image_discrete": bool_text(row["aut_tree_image_discrete"]),
            "bass_serre_action_faithful": bool_text(row["bass_serre_action_faithful"]),
            "action_kernel": row["action_kernel"],
            "action_proper": bool_text(row["action_proper"]),
            "finite_stabilizer_hypotheses_met": bool_text(
                row["finite_stabilizer_tree_lattice_hypotheses_met"]
            ),
            "full_tree_closed_paths": row["full_tree_positive_reduced_closed_paths"],
            "hashimoto_compact": bool_text(row["full_tree_hashimoto_compact"]),
            "hashimoto_trace_class": bool_text(row["full_tree_hashimoto_trace_class"]),
            "ordinary_fredholm_owned": bool_text(row["ordinary_fredholm_determinant_owned"]),
            "orbital_ledger": row["orbital_group_conjugacy_ledger"],
            "source_selective": bool_text(row.get("source_selective", False)),
        })

    finite_rows = [{
        "branching": row["branching"],
        "depth": row["depth"],
        "vertices": row["vertices"],
        "edges": row["edges"],
        "max_checked_walk_length": row["max_checked_walk_length"],
        "reduced_closed_walk_found": bool_text(row["reduced_closed_walk_found"]),
    } for row in science["finite_tree_results"]]

    noncompact_rows = []
    for group in science["noncompact_results"]:
        for row in group["orthogonal_column_witness"]:
            noncompact_rows.append({
                "r": group["r"],
                "columns": row["columns"],
                "image_norm_squared_each": row["image_norm_squared_each"],
                "pairwise_image_inner_products": row["pairwise_image_inner_products"],
                "partial_hilbert_schmidt_mass": row["partial_hilbert_schmidt_mass"],
            })

    gbs_rows = [{
        "control_id": row["control_id"],
        "parsed_p": row["parsed_p"],
        "parsed_q": row["parsed_q"],
        "ascending": bool_text(row["ascending"]),
        "balanced": bool_text(row["balanced"]),
        "tree_degree": row["tree_degree"],
        "infinite_vertex_stabilizer": bool_text(row["infinite_vertex_stabilizer"]),
        "full_tree_closed_ledger_empty": bool_text(row["full_tree_closed_ledger_empty"]),
        "full_tree_fredholm_owned": bool_text(row["full_tree_fredholm_owned"]),
    } for row in science["gbs_results"]]

    random_rows = []
    for row in science["random_one_relator_results"]:
        random_rows.append({
            "control_id": row["control_id"],
            "relator": row["relator"],
            "canonical_cyclic_gbs_split_detected": bool_text(
                row["canonical_cyclic_gbs_split_detected"]
            ),
            "paper38_object_status": row["paper38_object_status"],
            "parsed_p": row.get("parsed_p", ""),
            "parsed_q": row.get("parsed_q", ""),
        })

    marker_rows = []
    for group in science["marker_results"]:
        for row in group["words"]:
            marker_rows.append({
                "r": group["r"],
                "name": row["name"],
                "word": row["word"],
                "old_generator_marker_length": row["old_generator_marker_length"],
                "bass_serre_translation_length": row["bass_serre_translation_length"],
                "height": row["height"],
                "markers_compatible": bool_text(group["markers_compatible"]),
            })

    return {
        "results/orbital_parameter_rows.csv": csv_bytes(
            ["r", "declared_class", "tree_degree", "aut_tree_image_discrete",
             "bass_serre_action_faithful", "action_kernel", "action_proper",
             "finite_stabilizer_hypotheses_met", "full_tree_closed_paths",
             "hashimoto_compact", "hashimoto_trace_class",
             "ordinary_fredholm_owned", "orbital_ledger", "source_selective"],
            parameter_rows,
        ),
        "results/finite_tree_rows.csv": csv_bytes(
            ["branching", "depth", "vertices", "edges",
             "max_checked_walk_length", "reduced_closed_walk_found"],
            finite_rows,
        ),
        "results/noncompact_rows.csv": csv_bytes(
            ["r", "columns", "image_norm_squared_each",
             "pairwise_image_inner_products", "partial_hilbert_schmidt_mass"],
            noncompact_rows,
        ),
        "results/gbs_rows.csv": csv_bytes(
            ["control_id", "parsed_p", "parsed_q", "ascending", "balanced",
             "tree_degree", "infinite_vertex_stabilizer",
             "full_tree_closed_ledger_empty", "full_tree_fredholm_owned"],
            gbs_rows,
        ),
        "results/random_one_relator_rows.csv": csv_bytes(
            ["control_id", "relator", "canonical_cyclic_gbs_split_detected",
             "paper38_object_status", "parsed_p", "parsed_q"],
            random_rows,
        ),
        "results/marker_rows.csv": csv_bytes(
            ["r", "name", "word", "old_generator_marker_length",
             "bass_serre_translation_length", "height", "markers_compatible"],
            marker_rows,
        ),
    }


def exact_fraction(numerator: int, denominator: int) -> dict[str, object]:
    divisor = __import__("math").gcd(numerator, denominator)
    reduced_numerator = numerator // divisor
    reduced_denominator = denominator // divisor
    return {
        "numerator": numerator,
        "denominator": denominator,
        "exact": f"{numerator}/{denominator}",
        "reduced": f"{reduced_numerator}/{reduced_denominator}",
    }


def make_analysis(
    route: dict[str, Any], science: dict[str, Any]
) -> dict[str, Any]:
    counts = route["canonical_counts"]
    return {
        "schema": "paper38-analysis-summary-v1",
        "candidate": "SD-C40",
        "material_passport": {
            "origin_skills": ["experiment-bridge", "analyze-results",
                              "ars-experiment-agent"],
            "verification_status": "VERIFIED",
            "verification_basis": "fresh_A_B_and_isolated_cold_C_exact_byte_identity",
            "version_label": "SD-C40-stage1-results-v1",
        },
        "analysis_regime": {
            "deterministic_exact_enumeration": True,
            "sampling_used": False,
            "p_values_applicable": False,
            "confidence_intervals_applicable": False,
            "error_bars_applicable": False,
            "finite_checks_promoted_to_infinite_proof": False,
        },
        "raw_tables": [
            "results/orbital_parameter_rows.csv",
            "results/finite_tree_rows.csv",
            "results/noncompact_rows.csv",
            "results/gbs_rows.csv",
            "results/random_one_relator_rows.csv",
            "results/marker_rows.csv",
        ],
        "exact_rates": {
            "generic_necklace_among_r_ge_2": exact_fraction(
                counts["generic_necklace_rows"], 10
            ),
            "source_selective_among_parameter_rows": exact_fraction(
                counts["source_selective_rows"], counts["parameter_rows"]
            ),
            "gbs_empty_full_tree_ledgers": exact_fraction(
                counts["gbs_empty_ledgers"], counts["gbs_rows"]
            ),
            "gbs_owned_full_tree_fredholm": exact_fraction(
                counts["gbs_fredholm_owned"], counts["gbs_rows"]
            ),
            "compatible_marker_rows": exact_fraction(
                counts["marker_compatible_rows"], counts["marker_rows"]
            ),
            "random_controls_eligible_for_frozen_split": exact_fraction(
                counts["random_eligible_cyclic_gbs"],
                counts["random_one_relator_rows"],
            ),
        },
        "findings": [
            {
                "observation": "The literal full-tree primitive ledger is empty and every preregistered GBS control has the same empty-ledger obstruction.",
                "interpretation": "Finite tree certificates agree with the independently proved tree no-cycle theorem.",
                "implication": "Gate A1 fails on the frozen object.",
                "next_step": "Retain theorem ownership; do not substitute a quotient or orbital ledger.",
            },
            {
                "observation": "Orthogonal-column norms stay nonzero while partial Hilbert-Schmidt mass grows for all five tested r rows.",
                "interpretation": "The finite witness sequence audits the noncompactness construction.",
                "implication": "The ordinary full-tree Fredholm determinant is not owned.",
                "next_step": "Do not introduce damping, a basepoint, or another determinant category.",
            },
            {
                "observation": "All ten r>=2 orbital rows collapse to the generic necklace product, while r=1 is divergent and every marker row is incompatible.",
                "interpretation": "The separately typed substitute carries index dynamics, not source-selective recurrence.",
                "implication": "Gates A3 and A4 fail and the affine branch closes.",
                "next_step": "Paper 39 may only synthesize the frozen obstruction DAG.",
            },
        ],
        "scientific_conclusion": "negative_confirmed",
        "hard_status": "STOP_BASS_SERRE_TREE_BRANCH",
        "branch_status": "CLOSE_ENTIRE_AFFINE_BRANCH",
        "route_conclusion": "ROUTE_A_REJECTED",
    }


def make_report(
    route: dict[str, Any],
    analysis: dict[str, Any],
    reproducibility: dict[str, Any],
    test_summary: dict[str, Any],
) -> str:
    counts = route["canonical_counts"]
    rates = analysis["exact_rates"]
    lines = [
        "# Paper 38 exact experiment report — SD-C40",
        "",
        "## Outcome",
        "",
        "The exact integration confirms `STOP_BASS_SERRE_TREE_BRANCH` /",
        "`CLOSE_ENTIRE_AFFINE_BRANCH` and strict `ROUTE_A_REJECTED`. The full",
        "presentation-canonical Bass--Serre tree has an empty reduced closed-",
        "path ledger; its full-tree Hashimoto operator is noncompact and not",
        "trace class; and the standard discrete tree-lattice determinant",
        "hypotheses fail. At `r=1` the automorphism-group image is discrete but",
        "the action has infinite kernel and is nonproper; for `r>=2` the",
        "faithful image is nondiscrete. The separately typed conjugacy ledger",
        "is generic for `r>=2`, divergent at `r=1`, and marker-incompatible.",
        "",
        "## Canonical exact counts",
        "",
        "| Evidence | Exact result |",
        "|---|---:|",
        f"| evaluator assertions | {counts['exact_checks_passed']}/{counts['exact_checks_total']} |",
        f"| parameter rows | {counts['parameter_rows']} |",
        f"| generic necklace rows among `r>=2` | {rates['generic_necklace_among_r_ge_2']['exact']} |",
        f"| deliberate GBS empty ledgers | {rates['gbs_empty_full_tree_ledgers']['exact']} |",
        f"| deliberate GBS owned full-tree Fredholm | {rates['gbs_owned_full_tree_fredholm']['exact']} |",
        f"| random one-relator controls | {counts['random_one_relator_rows']} |",
        f"| random controls eligible for the frozen split | {rates['random_controls_eligible_for_frozen_split']['exact']} |",
        f"| compatible marker rows | {rates['compatible_marker_rows']['exact']} |",
        "",
        "The random controls are eligibility controls: ineligible rows are not",
        "counted as failures of a mechanism they do not possess.",
        "",
        "## Reproducibility and separation",
        "",
        f"- Fresh/cold runs: {reproducibility['byte_identical_run_count']}/3 byte-identical.",
        "- Run C executed from an isolated temporary code copy that was removed.",
        "- Source and evaluator occupy disjoint directories and communicate",
        "  only by canonical JSON through subprocess standard streams.",
        "- Absent/null/empty/populated transport metadata and simulated future",
        "  root-manifest absence/presence leave scientific and Route bytes",
        "  unchanged.",
        f"- Integration checks: {test_summary['passed']}/{test_summary['total']}.",
        f"- Scientific aggregate SHA-256: `{EXPECTED_SCIENCE_SHA256}`.",
        "",
        "## Analysis boundary",
        "",
        "All reported counts are deterministic exact enumerations, so p-values,",
        "confidence intervals, and error bars are not applicable. Finite tree,",
        "orbit, and orthogonal-column rows audit formulas and implementation;",
        "they do not replace the independent infinite-object proofs in",
        "`PROOF_PACKAGE.md` and `DERIVATION_PACKAGE.md`. No quotient, arbitrary",
        "representation, damping, Route-B repair, or post-result mechanism search",
        "was performed.",
        "",
        "## Material passport",
        "",
        "Verification status: `VERIFIED` by exact fresh A/B and isolated cold-C",
        "byte identity plus independent full integrity audit.",
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
                    or path.suffix in {".pyc", ".pyo"}
                    or path.name.startswith(".paper38-cold-c-")):
                bad.append(path.relative_to(ROOT).as_posix())
    return sorted(bad)


def canonical_text_violations(paths: list[Path]) -> list[str]:
    bad = []
    for path in paths:
        data = path.read_bytes()
        rel = path.relative_to(ROOT).as_posix()
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            bad.append(f"{rel}:not-utf8")
            continue
        if data.startswith(b"\xef\xbb\xbf"):
            bad.append(f"{rel}:bom")
        if b"\r" in data:
            bad.append(f"{rel}:cr")
        if not data.endswith(b"\n") or data.endswith(b"\n\n"):
            bad.append(f"{rel}:eof-newline")
        if any(line.endswith((" ", "\t")) for line in text.splitlines()):
            bad.append(f"{rel}:trailing-whitespace")
    return bad


def make_ledger() -> bytes:
    exclusions = {LEDGER.resolve(), ROUTE_CARD.resolve(), PAPER_MANIFEST.resolve()}
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
    require(ROUTE_CARD.is_file(), "fixed strict Route card is missing")

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

    with tempfile.TemporaryDirectory(prefix=".paper38-cold-c-", dir=RESULTS) as tmp:
        cold_root = Path(tmp) / "code"
        shutil.copytree(CODE / "source", cold_root / "source")
        shutil.copytree(CODE / "evaluator", cold_root / "evaluator")
        source_c, science_c, route_c = run_pipeline(cold_root, "C-cold")
    require(not any(path.name.startswith(".paper38-cold-c-")
                    for path in RESULTS.iterdir()), "cold-run directory retained")

    require(source_a == source_b == source_c,
            "A/B/C source packets differ")
    require(science_a == science_b == science_c,
            "A/B/C scientific outputs differ")
    require(route_a == route_b == route_c,
            "A/B/C Route evaluations differ")

    fixtures = parse_canonical_json(source_a, "canonical source packet")
    science = parse_canonical_json(science_a, "canonical science")
    route = parse_canonical_json(route_a, "canonical Route evaluation")
    unaffected_projection_sha = sha256(
        canonical_bytes(unaffected_science_projection(science))
    )
    require(
        unaffected_projection_sha == UNAFFECTED_PROJECTION_SHA256,
        "science changed outside the predeclared r=1 topology normalization",
    )

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
        require(state_science == science_a,
                f"scientific bytes changed under {state} metadata")
        require(state_route == route_a,
                f"Route bytes changed under {state} metadata")
        metadata_rows.append({
            "state": state,
            "source_envelope_sha256": sha256(canonical_bytes(packet)),
            "scientific_sha256": sha256(state_science),
            "route_evaluation_sha256": sha256(state_route),
        })

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
        "schema": "paper38-fresh-ab-cold-c-v1",
        "runs": [
            {"run": "A", "mode": "fresh",
             "source_packet_sha256": sha256(source_a),
             "scientific_sha256": sha256(science_a),
             "route_sha256": sha256(route_a)},
            {"run": "B", "mode": "fresh",
             "source_packet_sha256": sha256(source_b),
             "scientific_sha256": sha256(science_b),
             "route_sha256": sha256(route_b)},
            {"run": "C", "mode": "cold_isolated_copy",
             "source_packet_sha256": sha256(source_c),
             "scientific_sha256": sha256(science_c),
             "route_sha256": sha256(route_c)},
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
        "schema": "paper38-four-state-metadata-stability-v1",
        "states": metadata_rows,
        "state_order": ["absent", "null", "empty", "populated"],
        "scientific_bytes_stable": True,
        "route_bytes_stable": True,
    }
    manifest_certificate = {
        "schema": "paper38-manifest-metadata-stability-v1",
        "actual_stage1_manifest_state": "absent",
        "simulated_states": manifest_rows,
        "scientific_bytes_stable": True,
        "route_bytes_stable": True,
        "excluded_from_immutable_ledger": True,
        "excluded_from_canonical_text_count": True,
    }
    boundary = {
        "schema": "paper38-source-evaluator-boundary-v1",
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
    external = {**EXPECTED_PROTOTYPE_PROVENANCE, **EXPECTED_RESEARCH_PROVENANCE}
    provenance_visible = external_provenance_visible()
    prototype_bridge = {
        "schema": "paper38-corrected-prototype-bridge-v2",
        "prototype_seed_version": "v1_known_r1_image_discreteness_defect",
        "authority_evaluator_version": "v2_corrected_action_topology",
        "source_core_byte_preserved": True,
        "evaluator_core_byte_preserved": False,
        "source_core_sha256": file_sha256(source_core),
        "evaluator_core_sha256": file_sha256(evaluator_core),
        "prototype_seed_evaluator_sha256": EXPECTED_PROTOTYPE_PROVENANCE[
            "/tmp/paper38_exact_prototype/independent_evaluator.py"
        ],
        "prototype_seed_scientific_sha256": PROTOTYPE_SEED_SCIENCE_SHA256,
        "authority_scientific_sha256": sha256(science_a),
        "scientific_payload_byte_preserved": False,
        "normalization_correction": {
            "scope": "Bass-Serre action topology only",
            "r1": "Aut(line) image discrete; infinite kernel; action nonproper",
            "r_ge_2": "faithful Aut(tree) image nondiscrete; action nonproper",
            "all_r": "finite-stabilizer tree-lattice hypotheses fail",
            "route_tuple_changed": False,
            "evaluator_check_count_changed": False,
        },
        "unaffected_projection_sha256": unaffected_projection_sha,
        "unaffected_projection_expected_sha256": UNAFFECTED_PROJECTION_SHA256,
        "unaffected_components_match_seed": True,
        "research_package_sha256": EXPECTED_RESEARCH_PROVENANCE[
            "/tmp/paper38_research_package.md"
        ],
        "source_lock_sha256": EXPECTED_RESEARCH_PROVENANCE[
            "/tmp/paper38_source_lock.md"
        ],
        "route_draft_sha256": EXPECTED_RESEARCH_PROVENANCE[
            "/tmp/paper38_route_v0_2.yaml"
        ],
        "external_bridge_observability": {
            path_text: {
                "available_at_freeze": (
                    provenance_visible and Path(path_text).is_file()
                ),
                "hash_matches_if_available": (
                    not provenance_visible
                    or not Path(path_text).is_file()
                    or file_sha256(Path(path_text)) == expected
                ),
            }
            for path_text, expected in sorted(external.items())
        },
        "external_bridge_availability_is_terminal_gate": False,
        "clean_clone_runtime_dependency_on_tmp": False,
    }
    source_manifest = {
        "schema": "paper38-integrated-code-manifest-v1",
        "files": {
            path.relative_to(ROOT).as_posix(): {
                "bytes": len(path.read_bytes()),
                "sha256": file_sha256(path),
            }
            for path in sorted(CODE.rglob("*.py"))
        },
    }
    analysis = make_analysis(route, science)
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
            "schema": "paper38-canonical-counts-v1",
            "candidate": "SD-C40",
            "counts": counts,
        }),
        "results/analysis_summary.json": canonical_bytes(analysis),
        "evaluations/route_a/SD-C40/independent_evaluation.json": route_a,
    }
    primary.update(tables)

    for rel, data in primary.items():
        write_if_changed(ROOT / rel, data)
    second_changed = []
    for rel, data in primary.items():
        if write_if_changed(ROOT / rel, data):
            second_changed.append(rel)
    require(not second_changed, "second primary materialization was not idempotent")
    primary_aggregate = sha256(canonical_bytes({
        rel: sha256(data) for rel, data in sorted(primary.items())
    }))
    idempotence = {
        "schema": "paper38-idempotence-certificate-v1",
        "primary_artifact_count": len(primary),
        "first_materialization_completed": True,
        "second_materialization_changed_paths": second_changed,
        "second_materialization_byte_identical": True,
        "primary_artifact_hash_aggregate": primary_aggregate,
        "timestamps_excluded": True,
    }
    write_if_changed(
        RESULTS / "idempotence_certificate.json", canonical_bytes(idempotence)
    )

    test_rows = [
        ("research_lock_verified", True),
        ("research_lock_exact_five", len(research_lock["locked_research_authority"]) == 5),
        ("stable_plan_exact_two", research_lock["stable_plan_pointers"] == EXPECTED_PLAN_POINTERS),
        ("source_core_bridge_hash", file_sha256(source_core) == EXPECTED_SOURCE_CORE_SHA256),
        ("evaluator_core_bridge_hash", file_sha256(evaluator_core) == EXPECTED_EVALUATOR_CORE_SHA256),
        ("source_does_not_import_evaluator", "independent_evaluator" not in imported_modules(source_core)),
        ("evaluator_does_not_import_source", "source_core" not in imported_modules(evaluator_core)),
        ("fresh_a_science_hash", sha256(science_a) == EXPECTED_SCIENCE_SHA256),
        ("fresh_b_science_hash", sha256(science_b) == EXPECTED_SCIENCE_SHA256),
        ("cold_c_science_hash", sha256(science_c) == EXPECTED_SCIENCE_SHA256),
        ("abc_source_byte_identity", source_a == source_b == source_c),
        ("abc_science_byte_identity", science_a == science_b == science_c),
        ("abc_route_byte_identity", route_a == route_b == route_c),
        ("cold_copy_removed", reproducibility["cold_copy_removed"] is True),
        ("metadata_state_count_four", len(metadata_rows) == 4),
        ("metadata_science_stable", all(row["scientific_sha256"] == EXPECTED_SCIENCE_SHA256 for row in metadata_rows)),
        ("metadata_route_stable", len({row["route_evaluation_sha256"] for row in metadata_rows}) == 1),
        ("manifest_state_count_two", len(manifest_rows) == 2),
        ("manifest_route_stable", len({row["route_evaluation_sha256"] for row in manifest_rows}) == 1),
        ("exact_checks_277", counts["exact_checks_passed"] == counts["exact_checks_total"] == 277),
        ("unaffected_seed_projection_exact", unaffected_projection_sha == UNAFFECTED_PROJECTION_SHA256),
        ("r1_image_discrete_infinite_kernel_nonproper", next(row for row in science["parameter_results"] if row["r"] == 1)["aut_tree_image_discrete"] is True and next(row for row in science["parameter_results"] if row["r"] == 1)["action_kernel"] == "infinite_cyclic" and next(row for row in science["parameter_results"] if row["r"] == 1)["action_proper"] is False),
        ("r_ge_2_faithful_image_nondiscrete_nonproper", all(row["bass_serre_action_faithful"] is True and row["aut_tree_image_discrete"] is False and row["action_proper"] is False for row in science["parameter_results"] if row["r"] >= 2)),
        ("parameter_rows_11", counts["parameter_rows"] == 11),
        ("prime_rows_4", counts["prime_rows"] == 4),
        ("composite_rows_6", counts["composite_rows"] == 6),
        ("finite_tree_rows_3", counts["finite_tree_rows"] == 3),
        ("noncompact_rows_5", counts["noncompact_rows"] == 5),
        ("gbs_rows_18", counts["gbs_rows"] == 18),
        ("gbs_empty_18", counts["gbs_empty_ledgers"] == 18),
        ("gbs_fredholm_owned_0", counts["gbs_fredholm_owned"] == 0),
        ("random_rows_64", counts["random_one_relator_rows"] == 64),
        ("random_eligible_0", counts["random_eligible_cyclic_gbs"] == 0),
        ("marker_rows_5", counts["marker_rows"] == 5),
        ("marker_compatible_0", counts["marker_compatible_rows"] == 0),
        ("generic_necklace_rows_10", counts["generic_necklace_rows"] == 10),
        ("source_selective_rows_0", counts["source_selective_rows"] == 0),
        ("hard_stop_exact", route["hard_status"] == "STOP_BASS_SERRE_TREE_BRANCH"),
        ("branch_closed", route["branch_status"] == "CLOSE_ENTIRE_AFFINE_BRANCH"),
        ("route_rejected", route["overall"] == "ROUTE_A_REJECTED"),
        ("route_b_locked", route["route_b_invocation_allowed"] is False),
        ("primary_idempotence", not second_changed),
        ("stage1_manifest_absent", not PAPER_MANIFEST.exists()),
        ("no_cache_before_freeze", not forbidden_cache_paths()),
    ]
    failed = [name for name, passed in test_rows if not passed]
    require(not failed, f"integration checks failed: {failed!r}")
    test_summary = {
        "schema": "paper38-integration-tests-v1",
        "tests": [{"name": name, "passed": passed} for name, passed in test_rows],
        "passed": sum(int(passed) for _, passed in test_rows),
        "total": len(test_rows),
        "failed": failed,
    }
    write_if_changed(RESULTS / "test_results.json", canonical_bytes(test_summary))

    write_if_changed(
        ROOT / "EXPERIMENT_REPORT.md",
        text_bytes(make_report(route, analysis, reproducibility, test_summary)),
    )

    integrity_contract = {
        "schema": "paper38-integrity-contract-v1",
        "managed_roots": ["EXPERIMENT_REPORT.md", "code", "results",
                          "experiments", "docs", "evaluations/route_a/SD-C40"],
        "writer_owned_paths_outside_managed_roots": True,
        "immutable_ledger": "results/SHA256SUMS.txt",
        "ledger_exclusions": [
            "results/SHA256SUMS.txt",
            "evaluations/route_a/SD-C40/2026-08-15.yaml",
            "PAPER_MANIFEST.sha256",
        ],
        "paper_manifest_stage1": "ABSENT",
        "canonical_text_exclusions": ["PAPER_MANIFEST.sha256"],
        "text_encoding": "UTF-8",
        "line_ending": "LF",
        "trailing_whitespace_allowed": False,
        "eof_newline_count": 1,
        "cache_allowed": False,
        "expected_result_paths": EXPECTED_RESULT_PATHS,
    }
    write_if_changed(
        RESULTS / "integrity_contract.json", canonical_bytes(integrity_contract)
    )
    exact_result_set = {
        "schema": "paper38-exact-result-set-v1",
        "candidate": "SD-C40",
        "paths": EXPECTED_RESULT_PATHS,
        "path_count": len(EXPECTED_RESULT_PATHS),
        "closed_set": True,
    }
    write_if_changed(
        RESULTS / "exact_result_set.json", canonical_bytes(exact_result_set)
    )

    require(not forbidden_cache_paths(),
            f"cache residue before ledger: {forbidden_cache_paths()!r}")
    preledger_paths = [
        path for path in managed_files() if path.resolve() != LEDGER.resolve()
    ]
    violations = canonical_text_violations(preledger_paths)
    require(not violations, f"text hygiene violations: {violations!r}")

    hidden_argument = (
        ["--hide-external-provenance"]
        if not external_provenance_visible() else []
    )
    audit_prepare_bytes = run_python(
        CODE / "audit_integrity.py",
        "integrity-audit-prepare",
        arguments=["--prepare", *hidden_argument],
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
        CODE / "audit_integrity.py", "integrity-audit-final",
        arguments=hidden_argument,
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
            "optional external provenance changed integrity verdict")

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
    require(not PAPER_MANIFEST.exists(), "Stage-1 manifest appeared")

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
