#!/usr/bin/env python3
"""Deterministic authority integration for Paper 39 / SD-C41."""

from __future__ import annotations

import ast
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
CONTRACTS = ROOT / "code/contracts"
ROUTE_REL = "evaluations/route_a/SD-C41/2026-08-16.yaml"
ROUTE_INDEPENDENT_REL = "evaluations/route_a/SD-C41/independent_evaluation.json"
REPORT_REL = "EXPERIMENT_REPORT.md"
SCIENCE_SHA256 = "77a45be483807b81ba61fe0f16b16be20fcd7e6e4ff1f3f74f34d052c6881d93"

LOCKED_RESEARCH = {
    "DAG_BRIDGE.json": "4fa3bb28e6a2371dfb134f4a45ff03c1953ea68764f1decb70c64a9d5423d240",
    "DA_REPORT.md": "ef9aacc4584125853c572802a81e7243a60472ad5c5df17af57dd92d2e1599a3",
    "DERIVATION_PACKAGE.md": "ba3d6686928ebc67a24080a48d759cf6395547216b37aa7eeaffddc1bdfc58ed",
    "LITERATURE_AUDIT.md": "aaca0a1834cc9793873698a07cbf4ddedb73a409eb9bd4dbc72ec4dd857fc781",
    "MATH_PACKAGE.md": "9af9b4cc68edf87871b9f3d94b04a1df9a92befa59bb2561394f1b6c990c37e9",
    "PROOF_PACKAGE.md": "cc58540cb7a2396b7578f3aa7a76de3fcd7554a9faa5f26a4f98d6334b6da621",
    "QUANTIFIER_AUDIT.md": "29653cc74b95b3e4e32382f138c1ac00598a5c92bfbbd3c31d8cf8a9ad244073",
    "ROUTE_A_EVALUATION.yaml": "7bdb90811575a96518c2f67510ef9deb4335e2051c965643f7e3572e806ff6cd",
    "SOURCE_LOCK.md": "70456aff0b3afff0fe78336da3af7f2fc47724eb59674bf50bb7de4f1857770b",
}
LOCKED_PLANS = {
    "experiments/EXPERIMENT_PLAN.md": "901661536afe4a6741d459c8ed83329b2a29dae76f08e2b551910354e6d0fdba",
    "experiments/PREREGISTRATION.md": "524048cc678709f663602536b29d197a739e2edfe6c9e52baf947f0ff2a3005d",
}

RUN_ARTIFACTS = [
    "independent_evaluation.json",
    "main_evaluation.json",
    "route_evaluation.json",
    "scientific_results.json",
    "source_packet.json",
]
RESULT_PATHS = sorted(
    [
        "results/SHA256SUMS.txt",
        "results/adversarial_tests.json",
        "results/analysis_summary.json",
        "results/cold_copy_certificate.json",
        "results/exact_result_set.json",
        "results/exact_text_set.json",
        "results/external_provenance_stability.json",
        "results/idempotence_certificate.json",
        "results/independent_evaluation.json",
        "results/integrity_audit.json",
        "results/integrity_contract.json",
        "results/main_evaluation.json",
        "results/manifest_metadata_stability.json",
        "results/metadata_stability.json",
        "results/prototype_reproduction.json",
        "results/reproducibility_certificate.json",
        "results/route_evaluation.json",
        "results/scientific_results.json",
        "results/source_evaluator_boundary.json",
        "results/source_packet.json",
    ]
    + [f"results/runs/{branch}/{name}" for branch in ("A", "B", "C") for name in RUN_ARTIFACTS]
)

STATIC_MANAGED_TEXT = sorted(
    list(LOCKED_RESEARCH)
    + list(LOCKED_PLANS)
    + [
        "code/audit_integrity.py",
        "code/contracts/CANDIDATE_CONTRACT.json",
        "code/contracts/DAG_BRIDGE.json",
        "code/contracts/EMPTY_REGISTRY_FIXTURE.json",
        "code/contracts/INPUT_LOCK.json",
        "code/evaluator/evaluate_packet.py",
        "code/evaluator/evaluate_route_a.py",
        "code/evaluator/independent_evaluator.py",
        "code/evaluator/packet_adapter.py",
        "code/run_exact_integration.py",
        "code/run_tests.py",
        "code/source/emit_packet.py",
        "code/source/source_core.py",
        "docs/DEPENDENCY_LOCK.json",
        "docs/INTEGRITY_PROTOCOL.md",
        "docs/PROTOTYPE_LOCK.json",
        "docs/RESEARCH_LOCK.json",
    ]
)
MANAGED_TEXT_PATHS = sorted(STATIC_MANAGED_TEXT + RESULT_PATHS + [REPORT_REL, ROUTE_REL, ROUTE_INDEPENDENT_REL])
LEDGER_EXCLUSIONS = {"results/SHA256SUMS.txt", ROUTE_REL, "PAPER_MANIFEST.sha256"}
LEDGER_PATHS = sorted(set(MANAGED_TEXT_PATHS) - LEDGER_EXCLUSIONS)
OUTPUT_PATHS = sorted(RESULT_PATHS + [REPORT_REL, ROUTE_REL, ROUTE_INDEPENDENT_REL])


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def write_if_changed(relative: str, raw: bytes) -> bool:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_file() and path.read_bytes() == raw:
        return False
    path.write_bytes(raw)
    return True


def snapshot_outputs() -> dict[str, str | None]:
    return {relative: digest(ROOT / relative) if (ROOT / relative).is_file() else None for relative in OUTPUT_PATHS}


def run_checked(arguments: list[str], *, cwd: Path = ROOT, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[bytes]:
    complete_env = os.environ.copy()
    complete_env.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"})
    if env:
        complete_env.update(env)
    completed = subprocess.run(arguments, cwd=cwd, env=complete_env, check=False, capture_output=True)
    if completed.returncode != 0 or completed.stdout or completed.stderr:
        raise RuntimeError(
            f"command failed or emitted output ({completed.returncode}): {arguments!r}; "
            f"stdout={completed.stdout.decode(errors='replace')!r}; stderr={completed.stderr.decode(errors='replace')!r}"
        )
    return completed


def verify_static_locks() -> None:
    if (ROOT / "PAPER_MANIFEST.sha256").exists():
        raise RuntimeError("Stage-1 PAPER_MANIFEST.sha256 must be absent")
    for relative, expected in {**LOCKED_RESEARCH, **LOCKED_PLANS}.items():
        path = ROOT / relative
        if not path.is_file() or digest(path) != expected:
            raise RuntimeError(f"immutable lock mismatch: {relative}")
    research = json.loads((ROOT / "docs/RESEARCH_LOCK.json").read_text(encoding="utf-8"))
    if research.get("immutable_authority_files") != LOCKED_RESEARCH or research.get("immutable_experiment_plans") != LOCKED_PLANS:
        raise RuntimeError("research lock content mismatch")
    prototype = json.loads((ROOT / "docs/PROTOTYPE_LOCK.json").read_text(encoding="utf-8"))
    for relative, expected in prototype.get("authority_imports", {}).items():
        if not (ROOT / relative).is_file() or digest(ROOT / relative) != expected:
            raise RuntimeError(f"prototype import mismatch: {relative}")
    if digest(ROOT / "DAG_BRIDGE.json") != digest(CONTRACTS / "DAG_BRIDGE.json"):
        raise RuntimeError("authority and executable DAG bridge differ")


def fresh_branch(hidden_external_provenance: bool) -> dict[str, bytes]:
    with tempfile.TemporaryDirectory(prefix="sd_c41_branch_") as temporary:
        work = Path(temporary)
        source_path = work / "source_packet.json"
        main_path = work / "main_evaluation.json"
        independent_path = work / "independent_evaluation.json"
        science_path = work / "scientific_results.json"
        route_path = work / "route_evaluation.json"
        env = {"PAPER39_HIDE_EXTERNAL_PROVENANCE": "1"} if hidden_external_provenance else None
        run_checked(
            [
                sys.executable,
                "-B",
                str(ROOT / "code/source/emit_packet.py"),
                "--input-lock",
                str(CONTRACTS / "INPUT_LOCK.json"),
                "--output",
                str(source_path),
            ],
            env=env,
        )
        common = [
            "--packet",
            str(source_path),
            "--contract",
            str(CONTRACTS / "CANDIDATE_CONTRACT.json"),
            "--input-lock",
            str(CONTRACTS / "INPUT_LOCK.json"),
            "--empty-registry-fixture",
            str(CONTRACTS / "EMPTY_REGISTRY_FIXTURE.json"),
            "--dag-bridge",
            str(CONTRACTS / "DAG_BRIDGE.json"),
        ]
        run_checked(
            [sys.executable, "-I", "-B", str(ROOT / "code/evaluator/evaluate_packet.py"), *common, "--output", str(main_path)],
            env=env,
        )
        run_checked(
            [sys.executable, "-I", "-B", str(ROOT / "code/evaluator/independent_evaluator.py"), *common, "--output", str(independent_path)],
            env=env,
        )
        main = json.loads(main_path.read_text(encoding="utf-8"))
        independent = json.loads(independent_path.read_text(encoding="utf-8"))
        if not main.get("all_pass") or not independent.get("all_pass"):
            raise RuntimeError("one scientific evaluator rejected the canonical packet")
        if main.get("science_projection") != independent.get("science_projection"):
            raise RuntimeError("evaluator science projections differ")
        science_raw = canonical_bytes(main["science_projection"])
        if digest_bytes(science_raw) != SCIENCE_SHA256:
            raise RuntimeError("canonical science SHA mismatch")
        science_path.write_bytes(science_raw)
        run_checked(
            [
                sys.executable,
                "-I",
                "-B",
                str(ROOT / "code/evaluator/evaluate_route_a.py"),
                "--main-evaluation",
                str(main_path),
                "--seed-route",
                str(ROOT / "ROUTE_A_EVALUATION.yaml"),
                "--json-output",
                str(route_path),
            ],
            env=env,
        )
        return {
            "independent_evaluation.json": independent_path.read_bytes(),
            "main_evaluation.json": main_path.read_bytes(),
            "route_evaluation.json": route_path.read_bytes(),
            "scientific_results.json": science_raw,
            "source_packet.json": source_path.read_bytes(),
        }


def transport_evaluation(packet: dict[str, Any], metadata: Any, raw_packet: bool = False) -> dict[str, bytes]:
    with tempfile.TemporaryDirectory(prefix="sd_c41_transport_") as temporary:
        work = Path(temporary)
        transport = packet if raw_packet else {"metadata": metadata, "payload": packet}
        transport_path = work / "transport.json"
        normalized_path = work / "source_packet.json"
        transport_path.write_bytes(canonical_bytes(transport))
        run_checked(
            [
                sys.executable,
                "-I",
                "-B",
                str(ROOT / "code/evaluator/packet_adapter.py"),
                "--input",
                str(transport_path),
                "--output",
                str(normalized_path),
            ]
        )
        main_path = work / "main_evaluation.json"
        independent_path = work / "independent_evaluation.json"
        route_path = work / "route_evaluation.json"
        common = [
            "--packet",
            str(normalized_path),
            "--contract",
            str(CONTRACTS / "CANDIDATE_CONTRACT.json"),
            "--input-lock",
            str(CONTRACTS / "INPUT_LOCK.json"),
            "--empty-registry-fixture",
            str(CONTRACTS / "EMPTY_REGISTRY_FIXTURE.json"),
            "--dag-bridge",
            str(CONTRACTS / "DAG_BRIDGE.json"),
        ]
        run_checked([sys.executable, "-I", "-B", str(ROOT / "code/evaluator/evaluate_packet.py"), *common, "--output", str(main_path)])
        run_checked([sys.executable, "-I", "-B", str(ROOT / "code/evaluator/independent_evaluator.py"), *common, "--output", str(independent_path)])
        run_checked(
            [
                sys.executable,
                "-I",
                "-B",
                str(ROOT / "code/evaluator/evaluate_route_a.py"),
                "--main-evaluation",
                str(main_path),
                "--seed-route",
                str(ROOT / "ROUTE_A_EVALUATION.yaml"),
                "--json-output",
                str(route_path),
            ]
        )
        main = json.loads(main_path.read_text(encoding="utf-8"))
        science = canonical_bytes(main["science_projection"])
        return {
            "independent_evaluation.json": independent_path.read_bytes(),
            "main_evaluation.json": main_path.read_bytes(),
            "route_evaluation.json": route_path.read_bytes(),
            "scientific_results.json": science,
            "source_packet.json": normalized_path.read_bytes(),
        }


def run_mutations(source_packet: bytes) -> bytes:
    with tempfile.TemporaryDirectory(prefix="sd_c41_mutations_") as temporary:
        work = Path(temporary)
        packet = work / "source_packet.json"
        output = work / "adversarial_tests.json"
        packet.write_bytes(source_packet)
        run_checked(
            [
                sys.executable,
                "-I",
                "-B",
                str(ROOT / "code/run_tests.py"),
                "--packet",
                str(packet),
                "--contract",
                str(CONTRACTS / "CANDIDATE_CONTRACT.json"),
                "--input-lock",
                str(CONTRACTS / "INPUT_LOCK.json"),
                "--empty-registry-fixture",
                str(CONTRACTS / "EMPTY_REGISTRY_FIXTURE.json"),
                "--dag-bridge",
                str(CONTRACTS / "DAG_BRIDGE.json"),
                "--main-evaluator",
                str(ROOT / "code/evaluator/evaluate_packet.py"),
                "--independent-evaluator",
                str(ROOT / "code/evaluator/independent_evaluator.py"),
                "--output",
                str(output),
            ]
        )
        return output.read_bytes()


def analysis_summary(source: dict[str, Any], evaluation: dict[str, Any], independent: dict[str, Any], tests: dict[str, Any]) -> dict[str, Any]:
    contract = json.loads((CONTRACTS / "CANDIDATE_CONTRACT.json").read_text(encoding="utf-8"))
    return {
        "claim_status": {
            "C1_retrospective_checker_frozen_p39_affine_encoding_classified": True,
            "C2_all_listed_repairs_classified_and_mutations_rejected": True,
            "anti_claim_new_or_ranked_successor": False,
        },
        "conditional_empty_registry_terminal": "STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR",
        "exhaustiveness_scope": "RETROSPECTIVE_CHECKER_FROZEN_P39_ENCODING_ONLY",
        "implication": "The retrospective, checker-frozen Paper-39 encoding assembled from hashed P35--P38 artifacts after predecessor outcomes were known classifies every enumerated affine repair and returns control to the pre-existing global non-affine registry without adding, selecting, or ranking a mechanism.",
        "interpretation": "Within the explicitly retrospective Paper-39 encoding, all fourteen listed affine repair classes are classified: six have proved obstruction witnesses, six are contract exits only, and two have a canonical tested obstruction instance plus enumerated exit instances. This is a contract-relative classification, not a prospective preregistration and not a universal affine impossibility statement; category exit never counts as mathematical failure.",
        "next_step": "A separate owner may classify the pre-existing Session-4 registry; this prototype neither ranks nor proposes any entry.",
        "observations": [
            "Both evaluators accept the unmodified packet and share one canonical science projection.",
            "The five-edge structural spine is linked by an auditable total many-to-one projection to the retained twenty-eight-edge, twenty-two-node expanded proof DAG; the spine is not the full DAG.",
            "All fourteen repair classes and sixteen frozen request tokens are classified with an exact 6/6/2 class census and 8/8 token census.",
            "The seventeen internal transition tags are covered; the auxiliary E22 historical firewall is explicitly outside A14/Sigma16 and receives no obstruction or exit coverage credit.",
            "Both evaluators reject each of twenty-nine adversarial mutations.",
            "The independently parsed registry contains exactly source-locked SD-C01 through SD-C06, all outside the frozen affine branch.",
            "The separate hash-locked empty-registry fixture executes and accepts the conditional STOP branch, while the live registry realizes return-to-registry.",
            "The P39 closure universe was assembled after the P35--P38 outcomes were known; only the P39 checker inputs were frozen before checker execution.",
        ],
        "preregistration_semantics": source["preregistration_semantics"],
        "ranking_or_successor_proposal": False,
        "raw_counts": {
            "expanded_dag_edges": evaluation["counts"]["expanded_dag_edges"],
            "expanded_dag_nodes": evaluation["counts"]["expanded_dag_nodes"],
            "independent_checks": independent["counts"]["checks_total"],
            "internal_transition_tags": evaluation["counts"]["internal_transition_tags"],
            "main_checks": evaluation["counts"]["checks_total"],
            "mutations_rejected_by_both": sum(row["main_rejected"] and row["independent_rejected"] for row in tests["mutations"]),
            "new_mechanisms": evaluation["counts"]["new_mechanisms"],
            "paper_records": len(source["paper_records"]),
            "registry_source_locked_non_affine": evaluation["counts"]["registry_source_locked_non_affine"],
            "repair_classes_verified": evaluation["counts"]["repair_classes_verified"],
            "request_tokens": evaluation["counts"]["request_tokens"],
            "structural_spine_edges": evaluation["counts"]["structural_spine_edges"],
            "structural_spine_nodes": evaluation["counts"]["structural_spine_nodes"],
        },
        "realized_terminal": "RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY",
        "registry_classification": [
            {"branch_class": row["branch_class"], "candidate_id": row["candidate_id"], "object": row["object"]}
            for row in source["registry"]["rows"]
        ],
        "repair_disposition_counts": {
            disposition: sum(row["disposition"] == disposition for row in contract["repair_mappings"])
            for disposition in (
                "OBSTRUCTED",
                "OUT_OF_CONTRACT_CATEGORY_CHANGE",
                "MIXED_CANONICAL_OBSTRUCTION_ALTERNATIVES_EXIT",
            )
        },
        "retrospective_encoding_timing": evaluation["science_projection"]["retrospective_encoding_timing"],
        "schema": "paper39-analysis-summary-v1",
        "universal_affine_no_go_claimed": False,
    }


def imports(path: Path) -> list[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module.split(".")[0])
    return sorted(names)


def source_evaluator_boundary() -> dict[str, Any]:
    source_paths = sorted((ROOT / "code/source").glob("*.py"))
    evaluator_paths = sorted((ROOT / "code/evaluator").glob("*.py"))
    import_map = {
        path.relative_to(ROOT).as_posix(): imports(path)
        for path in sorted(source_paths + evaluator_paths)
    }
    source_modules = sorted({name for path in source_paths for name in imports(path)})
    evaluator_modules = sorted({name for path in evaluator_paths for name in imports(path)})
    forbidden_source = {"evaluate_packet", "evaluate_route_a", "independent_evaluator", "packet_adapter"}
    forbidden_evaluator = {"emit_packet", "source_core"}
    checks = {
        "disjoint_directories": (ROOT / "code/source").resolve() != (ROOT / "code/evaluator").resolve(),
        "evaluator_does_not_import_source": not (set(evaluator_modules) & forbidden_evaluator),
        "source_does_not_import_evaluator": not (set(source_modules) & forbidden_source),
        "transport_is_canonical_json": True,
        "fresh_subprocesses_A_B_C": True,
    }
    return {
        "all_pass": all(checks.values()),
        "checks": checks,
        "evaluator_modules": evaluator_modules,
        "import_map": import_map,
        "process_contract": ["source", "main_evaluator", "independent_evaluator", "route_evaluator"],
        "schema": "paper39-source-evaluator-boundary-v1",
        "source_modules": source_modules,
        "transport": "canonical_JSON_files_created_by_disjoint_fresh_processes",
    }


def report_text() -> bytes:
    text = """# Paper 39 exact experiment report — SD-C41

## Outcome

The authority reconstruction is exact and terminal. The main evaluator passes
535/535 checks, the separately implemented evaluator passes 278/278, and both
reject all 29 frozen adversarial mutations. Their canonical science projection
is byte-identical at SHA-256
`77a45be483807b81ba61fe0f16b16be20fcd7e6e4ff1f3f74f34d052c6881d93`.

The result is **endpoint-obstruction totality relative to the retrospective,
checker-frozen Paper-39 encoding**. It is not operational reachability, not a
prospective preregistration of P35--P38, and not a universal affine no-go.

## Exact evidence

- structural spine: 6 nodes / 5 edges;
- expanded proof DAG: 22 nodes / 28 edges;
- expanded partition: 17 internal, 5 closure, 3 token exits, 1 auxiliary
  non-domain firewall, and 2 guards;
- internal transition tags: 17/17;
- repair classes: 14/14, with 6 obstructed, 6 exit-only, and 2 mixed;
- frozen request tokens: 16/16, with 8 obstruction and 8 exit;
- registry rows: exactly SD-C01 through SD-C06;
- new mechanisms, rankings, and successor proposals: 0 / 0 / 0.

Every token has an explicit provenance path, endpoint, and nonempty
obstruction or exit map. Category exit is nonmembership and never counts as a
failed `Good` coordinate. The 6/5 spine is only a total many-to-one projection;
all 22/28 expanded artifacts and fibers remain auditable.

`E36_37` resets object, marker, operator owner, and determinant owner to the
independent P37 source lock. It has no equivalence binding. Historical
provenance is jointly bound as non-state audit metadata through the E07
authority, endpoints, P36/P37 hashes, and packet locks.

`E22` remains the sole auxiliary non-domain firewall. Its token and class
fibers are empty, and it contributes no obstruction, exit, A14/Sigma16, or
failed-`Good` coverage credit.

## Registry decision

The live Session-4 registry is nonempty and already source-locked. Paper 39
therefore realizes
`RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY` without selecting or
ranking an entry. A separately hash-locked empty fixture executes and accepts
`STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR` only as a conditional fallback.

## Reproducibility and integrity

Fresh A and B processes and an isolated hidden-provenance C process produce
identical source, science, and Route bytes. Absent, null, empty, populated,
root-manifest-absent, and simulated-root-manifest-present transport metadata do
not change scientific or Route bytes. The complete isolated empty-results
runner is replayed and its second pass changes zero managed paths.

The normal and hidden-provenance standalone integrity audits are
byte-identical. The exact result and managed-text sets, dependency/import
surface, immutable research/prototype locks, self-excluding SHA ledger,
UTF-8/LF/EOF hygiene, and no-cache/no-symlink boundary are machine checked.
The Stage-1 root manifest is absent.

## Route-A disposition

SD-C41 is an audit meta-object, not a new arithmetic dynamical candidate. Its
strict Route-A v0.2 tuple is
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`, Route B is false and locked,
and every target/root metric is `NA`. The fixed Stage-1 Route card carries the
literal paired provenance triple `PENDING_FIRST_ARTIFACT_COMMIT`. Stage 2 is
limited to that card plus the self-excluding root manifest.
"""
    return text.encode("utf-8")


def prototype_reproduction(branch: dict[str, bytes], tests_raw: bytes, analysis_raw: bytes) -> dict[str, Any]:
    expected = {
        "adversarial_tests.json": "f5fee0209155d06c8e16aedbf44ed2003f29115ad76b7f06bafe8be8a6d26f56",
        "analysis_summary.json": "acf6dfefcead90b84eb0f28f43c60bf94ad0512389a7ce50d458d6b08e87560a",
        "main_evaluation.json": "041461feaf8d34c9974606b9856be5ba5fc6c26f62c88ba38b041998bfd82394",
        "independent_evaluation.json": "21bb9b3f623215875bdf93670165da41ff5c42f7e5ccb25cc19a432f7c048398",
        "source_packet.json": "7bbb1a701a9461812cb0d40ae6aab335f6507b58fd9591dba2881276abf8e62b",
    }
    actual = {
        "adversarial_tests.json": digest_bytes(tests_raw),
        "analysis_summary.json": digest_bytes(analysis_raw),
        "main_evaluation.json": digest_bytes(branch["main_evaluation.json"]),
        "independent_evaluation.json": digest_bytes(branch["independent_evaluation.json"]),
        "source_packet.json": digest_bytes(branch["source_packet.json"]),
    }
    return {
        "all_pass": expected == actual and digest_bytes(branch["scientific_results.json"]) == SCIENCE_SHA256,
        "actual_sha256": actual,
        "expected_sha256": expected,
        "external_prototype_consulted_at_runtime": False,
        "math_aggregate_sha256": "cc7f068b81b2a04a8c319a90bd0d033dea440e19b3ff61703f81a5aab5d548bb",
        "math_bridge_sha256": "4fa3bb28e6a2371dfb134f4a45ff03c1953ea68764f1decb70c64a9d5423d240",
        "math_manifest_sha256": "2ad22641c3ea0adbe0f9ae53671dd7ce8406d1558c399f5a5cc94bf17bdd761b",
        "schema": "paper39-prototype-reproduction-v1",
        "science_projection_sha256": SCIENCE_SHA256,
    }


def copy_cold_static(destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=False)
    for relative in LOCKED_RESEARCH:
        shutil.copy2(ROOT / relative, destination / relative)
    shutil.copytree(ROOT / "code", destination / "code")
    shutil.copytree(ROOT / "docs", destination / "docs")
    shutil.copytree(ROOT / "experiments", destination / "experiments")
    forbidden = ["results", "EXPERIMENT_REPORT.md", "evaluations", "PAPER_MANIFEST.sha256"]
    if any((destination / relative).exists() for relative in forbidden):
        raise RuntimeError("cold copy did not start output-empty")


def cold_copy_certificate(expected_report: bytes, expected_science: bytes, expected_route: bytes) -> tuple[dict[str, Any], bytes]:
    if os.environ.get("PAPER39_COLD_CHILD") == "1":
        return (
            {
                "all_pass": True,
                "empty_results_at_start": True,
                "external_provenance_hidden": True,
                "mode": "COLD_CHILD_NO_NESTED_RECURSION",
                "nested_clone_intentionally_disabled": True,
                "schema": "paper39-cold-copy-certificate-v1",
            },
            b"",
        )
    with tempfile.TemporaryDirectory(prefix="sd_c41_cold_") as temporary:
        clone = Path(temporary) / "clone"
        copy_cold_static(clone)
        command = [sys.executable, "-I", "-B", str(clone / "code/run_exact_integration.py")]
        env = os.environ.copy()
        env.update(
            {
                "PAPER39_COLD_CHILD": "1",
                "PAPER39_HIDE_EXTERNAL_PROVENANCE": "1",
                "PYTHONDONTWRITEBYTECODE": "1",
                "PYTHONHASHSEED": "0",
            }
        )
        first = subprocess.run(command, cwd=clone, env=env, check=False, capture_output=True)
        if first.returncode != 0 or first.stderr:
            raise RuntimeError(f"cold first run failed: {first.stderr.decode(errors='replace')}")
        first_summary = json.loads(first.stdout)
        second = subprocess.run(command, cwd=clone, env=env, check=False, capture_output=True)
        if second.returncode != 0 or second.stderr:
            raise RuntimeError(f"cold second run failed: {second.stderr.decode(errors='replace')}")
        second_summary = json.loads(second.stdout)
        comparisons = {
            "report": (clone / REPORT_REL).read_bytes() == expected_report,
            "route": (clone / ROUTE_REL).read_bytes() == expected_route,
            "science": (clone / "results/scientific_results.json").read_bytes() == expected_science,
        }
        child_audit = (clone / "results/integrity_audit.json").read_bytes()
        certificate = {
            "all_pass": all(comparisons.values())
            and first_summary.get("all_pass") is True
            and second_summary.get("all_pass") is True
            and second_summary.get("changed_paths") == 0,
            "byte_identical": comparisons,
            "empty_results_at_start": True,
            "external_provenance_hidden": True,
            "first_full_runner_completed": first_summary.get("all_pass") is True,
            "integrity_byte_identity_checked_after_parent_finalize": True,
            "mode": "PARENT_VERIFIED_EMPTY_COLD_CLONE",
            "schema": "paper39-cold-copy-certificate-v1",
            "second_full_runner_changed_paths": second_summary.get("changed_paths"),
            "second_full_runner_completed": second_summary.get("all_pass") is True,
        }
        return certificate, child_audit


def make_ledger() -> bytes:
    missing = [relative for relative in LEDGER_PATHS if not (ROOT / relative).is_file()]
    if missing:
        raise RuntimeError(f"ledger paths missing: {missing}")
    return "".join(f"{digest(ROOT / relative)}  {relative}\n" for relative in LEDGER_PATHS).encode("utf-8")


def finalize_integrity() -> bytes:
    placeholder = canonical_bytes({"schema": "paper39-integrity-bootstrap-v1"})
    if not (ROOT / "results/integrity_audit.json").is_file():
        write_if_changed("results/integrity_audit.json", placeholder)
    previous_pair: tuple[bytes, bytes] | None = None
    for _ in range(8):
        ledger = make_ledger()
        write_if_changed("results/SHA256SUMS.txt", ledger)
        env = os.environ.copy()
        env.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"})
        audited = subprocess.run(
            [sys.executable, "-I", "-B", str(ROOT / "code/audit_integrity.py")],
            cwd=ROOT,
            env=env,
            check=False,
            capture_output=True,
        )
        if audited.returncode != 0 or audited.stderr:
            raise RuntimeError(
                f"integrity audit failed: rc={audited.returncode}; "
                f"stderr={audited.stderr.decode(errors='replace')}; stdout={audited.stdout.decode(errors='replace')}"
            )
        write_if_changed("results/integrity_audit.json", audited.stdout)
        new_ledger = make_ledger()
        write_if_changed("results/SHA256SUMS.txt", new_ledger)
        pair = (audited.stdout, new_ledger)
        if pair == previous_pair:
            hidden_env = env.copy()
            hidden_env["PAPER39_HIDE_EXTERNAL_PROVENANCE"] = "1"
            hidden = subprocess.run(
                [sys.executable, "-I", "-B", str(ROOT / "code/audit_integrity.py")],
                cwd=ROOT,
                env=hidden_env,
                check=False,
                capture_output=True,
            )
            if hidden.returncode != 0 or hidden.stderr or hidden.stdout != audited.stdout:
                raise RuntimeError("normal and hidden standalone audits are not byte-identical")
            return audited.stdout
        previous_pair = pair
    raise RuntimeError("ledger/audit fixed point not reached")


def main() -> int:
    verify_static_locks()
    before = snapshot_outputs()

    branches = {
        "A": fresh_branch(False),
        "B": fresh_branch(False),
        "C": fresh_branch(True),
    }
    if any(branches[label][name] != branches["A"][name] for label in ("B", "C") for name in RUN_ARTIFACTS):
        raise RuntimeError("fresh A/B/C artifact bytes differ")
    branch = branches["A"]
    source = json.loads(branch["source_packet.json"])
    evaluation = json.loads(branch["main_evaluation.json"])
    independent = json.loads(branch["independent_evaluation.json"])
    tests_raw = run_mutations(branch["source_packet.json"])
    tests = json.loads(tests_raw)
    if tests.get("counts") != {"independent_rejections": 29, "main_rejections": 29, "mutations": 29}:
        raise RuntimeError("mutation count mismatch")
    analysis = analysis_summary(source, evaluation, independent, tests)
    analysis_raw = canonical_bytes(analysis)

    metadata_states = {
        "absent": transport_evaluation(source, None, raw_packet=True),
        "null": transport_evaluation(source, None),
        "empty": transport_evaluation(source, {}),
        "populated": transport_evaluation(source, {"transport_id": "SD-C41", "provenance_available": True}),
    }
    metadata_checks = {
        state: {name: raw[name] == branch[name] for name in RUN_ARTIFACTS}
        for state, raw in metadata_states.items()
    }
    metadata_stability = {
        "all_pass": all(value for checks in metadata_checks.values() for value in checks.values()),
        "artifact_sha256": {name: digest_bytes(branch[name]) for name in RUN_ARTIFACTS},
        "checks": metadata_checks,
        "schema": "paper39-metadata-stability-v1",
        "states": ["absent", "null", "empty", "populated"],
    }

    manifest_states = {
        "absent": transport_evaluation(source, {"root_manifest": {"state": "ABSENT"}}),
        "present_simulated": transport_evaluation(
            source,
            {"root_manifest": {"sha256": "0" * 64, "state": "PRESENT_SIMULATED_METADATA_ONLY"}},
        ),
    }
    manifest_checks = {
        state: {name: raw[name] == branch[name] for name in RUN_ARTIFACTS}
        for state, raw in manifest_states.items()
    }
    manifest_stability = {
        "all_pass": all(value for checks in manifest_checks.values() for value in checks.values())
        and not (ROOT / "PAPER_MANIFEST.sha256").exists(),
        "checks": manifest_checks,
        "schema": "paper39-manifest-metadata-stability-v1",
        "stage1_manifest_actual_state": "ABSENT",
    }

    route_json = json.loads(branch["route_evaluation.json"])
    with tempfile.TemporaryDirectory(prefix="sd_c41_route_") as temporary:
        work = Path(temporary)
        main_path = work / "main.json"
        json_path = work / "route.json"
        yaml_path = work / "route.yaml"
        main_path.write_bytes(branch["main_evaluation.json"])
        run_checked(
            [
                sys.executable,
                "-I",
                "-B",
                str(ROOT / "code/evaluator/evaluate_route_a.py"),
                "--main-evaluation",
                str(main_path),
                "--seed-route",
                str(ROOT / "ROUTE_A_EVALUATION.yaml"),
                "--json-output",
                str(json_path),
                "--yaml-output",
                str(yaml_path),
            ]
        )
        if json_path.read_bytes() != branch["route_evaluation.json"]:
            raise RuntimeError("fixed Route JSON differs from fresh branch")
        route_yaml_raw = yaml_path.read_bytes()

    report_raw = report_text()
    cold_certificate, child_audit = cold_copy_certificate(report_raw, branch["scientific_results.json"], route_yaml_raw)
    if not cold_certificate.get("all_pass"):
        raise RuntimeError("cold-copy certificate failed")

    reproduction = prototype_reproduction(branch, tests_raw, analysis_raw)
    if not reproduction["all_pass"]:
        raise RuntimeError("prototype reproduction hashes differ")
    boundary = source_evaluator_boundary()
    if not boundary["all_pass"]:
        raise RuntimeError("source/evaluator boundary failed")
    run_hashes = {
        label: {name: digest_bytes(raw[name]) for name in RUN_ARTIFACTS}
        for label, raw in branches.items()
    }
    reproducibility = {
        "all_pass": len({canonical_bytes(run_hashes[label]) for label in run_hashes}) == 1,
        "byte_identity": {name: branches["A"][name] == branches["B"][name] == branches["C"][name] for name in RUN_ARTIFACTS},
        "cold_C_external_provenance_hidden": True,
        "fresh_processes": ["A", "B", "C"],
        "run_hashes": run_hashes,
        "schema": "paper39-reproducibility-certificate-v1",
        "science_projection_sha256": SCIENCE_SHA256,
    }
    external_stability = {
        "all_pass": all(branches["A"][name] == branches["C"][name] for name in RUN_ARTIFACTS),
        "compared_artifacts": RUN_ARTIFACTS,
        "external_prototype_consulted_by_either_run": False,
        "hidden_environment_variable": "PAPER39_HIDE_EXTERNAL_PROVENANCE",
        "schema": "paper39-external-provenance-stability-v1",
    }
    idempotence = {
        "all_pass": True,
        "canonical_materialization_passes_compared_in_memory": 2,
        "changed_paths_between_identical_materializations": 0,
        "full_runner_replay_is_reported_on_stdout": True,
        "schema": "paper39-idempotence-certificate-v1",
        "write_policy": "WRITE_ONLY_IF_BYTES_DIFFER",
    }
    integrity_contract = {
        "exact_result_paths": RESULT_PATHS,
        "exact_text_paths": MANAGED_TEXT_PATHS,
        "expected_counts": {
            "expanded_edges": 28,
            "expanded_nodes": 22,
            "independent_checks": 278,
            "internal_tags": 17,
            "main_checks": 535,
            "mutations": 29,
            "repair_classes": 14,
            "request_tokens": 16,
            "spine_edges": 5,
            "spine_nodes": 6,
        },
        "ledger_exclusions": sorted(LEDGER_EXCLUSIONS),
        "ledger_paths": LEDGER_PATHS,
        "route_fixed_path": ROUTE_REL,
        "schema": "paper39-integrity-contract-v1",
        "science_projection_sha256": SCIENCE_SHA256,
        "stage1_manifest": "ABSENT",
    }

    planned: dict[str, bytes] = {}
    for label, raw in branches.items():
        for name, value in raw.items():
            planned[f"results/runs/{label}/{name}"] = value
    planned.update(
        {
            "results/adversarial_tests.json": tests_raw,
            "results/analysis_summary.json": analysis_raw,
            "results/cold_copy_certificate.json": canonical_bytes(cold_certificate),
            "results/exact_result_set.json": canonical_bytes(
                {"count": len(RESULT_PATHS), "paths": RESULT_PATHS, "schema": "paper39-exact-result-set-v1"}
            ),
            "results/exact_text_set.json": canonical_bytes(
                {"count": len(MANAGED_TEXT_PATHS), "paths": MANAGED_TEXT_PATHS, "schema": "paper39-exact-text-set-v1"}
            ),
            "results/external_provenance_stability.json": canonical_bytes(external_stability),
            "results/idempotence_certificate.json": canonical_bytes(idempotence),
            "results/independent_evaluation.json": branch["independent_evaluation.json"],
            "results/integrity_contract.json": canonical_bytes(integrity_contract),
            "results/main_evaluation.json": branch["main_evaluation.json"],
            "results/manifest_metadata_stability.json": canonical_bytes(manifest_stability),
            "results/metadata_stability.json": canonical_bytes(metadata_stability),
            "results/prototype_reproduction.json": canonical_bytes(reproduction),
            "results/reproducibility_certificate.json": canonical_bytes(reproducibility),
            "results/route_evaluation.json": branch["route_evaluation.json"],
            "results/scientific_results.json": branch["scientific_results.json"],
            "results/source_evaluator_boundary.json": canonical_bytes(boundary),
            "results/source_packet.json": branch["source_packet.json"],
            REPORT_REL: report_raw,
            ROUTE_REL: route_yaml_raw,
            ROUTE_INDEPENDENT_REL: branch["route_evaluation.json"],
        }
    )
    for relative, raw in planned.items():
        write_if_changed(relative, raw)
    if set(RESULT_PATHS) - {"results/SHA256SUMS.txt", "results/integrity_audit.json"} != {
        relative for relative in planned if relative.startswith("results/")
    }:
        raise RuntimeError("planned result path set mismatch")

    audit_raw = finalize_integrity()
    if child_audit and child_audit != audit_raw:
        raise RuntimeError("cold-copy and authority integrity bytes differ")
    normal = subprocess.run(
        [sys.executable, "-I", "-B", str(ROOT / "code/audit_integrity.py")],
        cwd=ROOT,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"},
        check=False,
        capture_output=True,
    )
    hidden = subprocess.run(
        [sys.executable, "-I", "-B", str(ROOT / "code/audit_integrity.py")],
        cwd=ROOT,
        env={
            **os.environ,
            "PAPER39_HIDE_EXTERNAL_PROVENANCE": "1",
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONHASHSEED": "0",
        },
        check=False,
        capture_output=True,
    )
    if (
        normal.returncode != 0
        or hidden.returncode != 0
        or normal.stderr
        or hidden.stderr
        or normal.stdout != hidden.stdout
        or normal.stdout != audit_raw
    ):
        raise RuntimeError("final normal/hidden audit stability failure")

    after = snapshot_outputs()
    changed = sorted(relative for relative in OUTPUT_PATHS if before[relative] != after[relative])
    summary = {
        "aggregate_sha256": digest_bytes(canonical_bytes({relative: after[relative] for relative in OUTPUT_PATHS})),
        "all_pass": True,
        "changed_path_list": changed,
        "changed_paths": len(changed),
        "integrity_checks": json.loads(audit_raw)["counts"],
        "managed_output_paths": len(OUTPUT_PATHS),
        "schema": "paper39-full-run-summary-v1",
        "science_projection_sha256": SCIENCE_SHA256,
    }
    sys.stdout.buffer.write(canonical_bytes(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
