#!/usr/bin/env python3
"""Strict schema/semantic validator for canonical JSON-subset Route YAML."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "code/contracts/ROUTE_A_V0_2_SCHEMA.json"
EXPECTED_NORMALIZED_ROUTE_SHA256 = "636b61c59c8e2b04dde5cbdae5b0a62f7c28ccf0e7f054f40ccc944c503112ee"
STATE_A_FREEZE_NOTE = (
    "State-A first-artifact Route card. Static implementation inputs were frozen "
    "before the declared canonical rerun; the theorem, selector, literature, "
    "witnesses, and earlier smoke diagnostics were already known. The run is "
    "retrospective and supplies no novelty, priority, ranking, or authorization credit."
)
DECLARED_GENERATED_ARTIFACTS = {
    "results/factor_periodic_rigidity_certificate.json",
    "results/operator_ownership_certificate.json",
    "results/periodic_ledger_certificate.json",
    "results/scientific_results.json",
    "results/source_resolver.json",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def reject_duplicate(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate key: {key}")
        result[key] = value
    return result


def load(path: Path) -> tuple[Any, bytes]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=reject_duplicate)
    if canonical(value) != raw:
        raise ValueError(f"noncanonical JSON-subset YAML: {path.name}")
    return value, raw


def safe(relative: str) -> bool:
    if type(relative) is not str or not relative or "\\" in relative:
        return False
    path = PurePosixPath(relative)
    return not path.is_absolute() and ".." not in path.parts and "." not in path.parts


def declared_artifact_resolves(relative: str) -> bool:
    if not safe(relative) or relative.startswith("writer_snapshot/"):
        return False
    if relative in DECLARED_GENERATED_ARTIFACTS:
        return True
    path = ROOT / relative
    return path.is_file() and not path.is_symlink()


def normalize(route: dict[str, Any]) -> dict[str, Any]:
    clone = json.loads(json.dumps(route))
    clone["source_commit"] = "NORMALIZED_PROVENANCE"
    clone["code_commit"] = "NORMALIZED_PROVENANCE"
    clone["freeze_note"] = "NORMALIZED_PROVENANCE"
    clone["source_lock"]["code_commit"] = "NORMALIZED_PROVENANCE"
    clone["authority_integration"] = {
        "git_operations_by_integrator": 0,
        "paper_manifest_present": False,
        "state": "NORMALIZED",
        "status": "NORMALIZED_PROVENANCE",
    }
    return clone


def validate(route: dict[str, Any], route_raw: bytes,
             science: dict[str, Any], science_raw: bytes,
             schema: dict[str, Any]) -> dict[str, Any]:
    checks: dict[str, bool] = {}
    checks["json_subset_yaml_canonical"] = canonical(route) == route_raw
    checks["top_level_exact"] = set(route) == set(schema["required_top_level_keys"])
    checks["nested_exact"] = all(
        type(route.get(name)) is dict and set(route[name]) == set(keys)
        for name, keys in schema["required_nested_keys"].items()
    )
    checks["candidate_skill_date"] = (
        route["candidate_id"] == "SD-C45"
        and route["skill"] == "route-a-evaluator"
        and route["skill_version"] == "0.2.0"
        and route["evaluation_date"] == "2026-08-17"
    )
    checks["artifact_base"] = route["artifact_path_base"] == schema["artifact_path_base"]
    checks["tuple"] = route["route_tuple"] == science["route"]["tuple"] == [
        "A0_FAIL", "A1_FAIL", "A2_ANALYTIC_DETERMINANT", "A3_FAIL", "A4_FAIL"
    ]
    expected_evidence = ["MODELING_CHOICE", "PROVED", "PROVED", "PROVED", "NOT_TESTABLE"]
    checks["rung_evidence"] = all(
        route[f"a{index}"]["verdict"] == route["route_tuple"][index]
        and route[f"a{index}"]["evidence_status"] == expected_evidence[index]
        for index in range(5)
    )
    checks["overall"] = route["overall_verdict"] == science["route"]["overall_verdict"] \
        == "ROUTE_A_REJECTED"
    checks["route_b"] = (
        route["route_b_invocation_allowed"] is False
        and route["route_b"]["invocation_allowed"] is False
        and route["route_b"]["reason"] == "same_object_primitive_ledger_and_completed_structure_fail"
    )
    checks["terminal_mapping"] = route["terminal_codes"] == science["terminal_codes"] == {
        "determinant_comparison": "STOP_TRIVIAL_ONE_MINUS_Z_DIVISOR",
        "factor_cycle_creation": "STOP_PROXIMAL_PERIODIC_RIGIDITY",
        "literature": "PROCEED_ONLY_AS_INTERNAL_EXACT_CLOSURE",
        "rational_prime_identification": "STOP_SINGLETON_PRIMITIVE_SUPPORT",
    }
    checks["duplicate_token_absent"] = "STOP_DUPLICATE" not in route_raw.decode("ascii")
    checks["science_hash_binding"] = (
        route["a2"]["metrics"]["scientific_results_sha256"] == digest(science_raw)
    )
    checks["source_types"] = (
        route["projection_firewall"]["source_type"] == "SquarefreeAdmissiblePoint"
        and route["projection_firewall"]["factor_type"] == "TopologicalFactorState"
        and route["projection_firewall"]["target_comparator_type"] == "RationalPrimeAtom"
    )
    checks["marker_repetition"] = (
        route["typed_return_map"]["factor_marker"] == "z_power_time"
        and route["typed_return_map"]["rational_prime_marker"] == "independent_u"
        and route["typed_return_map"]["rational_prime_same_type_identification_exists"] is False
    )
    checks["repair_scope"] = route["projection_firewall"]["declared_repairs_are_exhaustive"] is False
    checks["target_data_absent"] = (
        route["target_and_root_metrics"]["target_zero_data_used"] is False
        and route["target_and_root_metrics"]["numerical_root_search_used"] is False
    )
    artifact_paths: list[str] = []
    artifact_paths.extend(route["source_lock"]["artifact_paths"])
    for index in range(5):
        artifact_paths.extend(route[f"a{index}"]["artifacts"])
    checks["artifact_paths_safe"] = (
        all(declared_artifact_resolves(path) for path in artifact_paths)
    )
    checks["branch_status"] = route["branch_status"] \
        == "CLOSE_SD_C02_TOPOLOGICAL_FACTOR_CYCLE_REPAIR"
    checks["adversarial_stop"] = route["adversarial_controls"]["verdict"] \
        == "STOP_SCOPED_EXACT_SQUAREFREE_FACTOR_PERIODIC_RIGIDITY"

    pending = "PENDING_FIRST_ARTIFACT_COMMIT"
    commit_values = [route["source_commit"], route["code_commit"],
                     route["source_lock"]["code_commit"]]
    state = route["authority_integration"]["state"]
    if state == "A":
        state_ok = (
            commit_values == [pending, pending, pending]
            and route["authority_integration"]["paper_manifest_present"] is False
            and route["authority_integration"]["status"] == "STATE_A_FIRST_ARTIFACT_PENDING_TRIPLE"
            and route["authority_integration"]["git_operations_by_integrator"] == 0
            and route["freeze_note"] == STATE_A_FREEZE_NOTE
        )
    elif state == "B":
        state_ok = (
            len(set(commit_values)) == 1
            and re.fullmatch(r"[0-9a-f]{40}", commit_values[0]) is not None
            and commit_values[0] != "0" * 40
            and route["authority_integration"]["paper_manifest_present"] is True
            and route["authority_integration"]["status"] == "STATE_B_METADATA_ONLY_SEAL"
            and route["authority_integration"]["git_operations_by_integrator"] == 0
            and route["freeze_note"] == (
                "State-B metadata-only seal. The source_commit, code_commit, and "
                "source_lock.code_commit fields all bind Stage-1 artifact commit "
                f"{commit_values[0]}; no science, code, experiment, result, report, "
                "writer, PDF, research, registry, or root-registration byte changed."
            )
        )
    else:
        state_ok = False
    checks["provenance_state"] = state_ok
    checks["science_claim_scope"] = (
        science["universal_aperiodic_factor_theorem_claimed"] is False
        and science["literature_boundary"]["conditional_code"] == "STOP_DUPLICATE"
        and science["literature_boundary"]["route_terminal"] is False
    )
    checks["chronology"] = (
        science["integration_chronology"]["prospective"] is False
        and science["integration_chronology"]["outcome_independent"] is False
        and science["integration_chronology"]["novelty_credit"] is False
    )
    checks["full_normalized_payload_exact"] = (
        digest(canonical(normalize(route))) == EXPECTED_NORMALIZED_ROUTE_SHA256
    )
    if not all(checks.values()):
        failed = sorted(key for key, value in checks.items() if not value)
        raise ValueError(f"strict Route checks failed: {failed}")
    return {
        "checks": checks,
        "checks_passed": len(checks),
        "checks_total": len(checks),
        "normalized_route_sha256": digest(canonical(normalize(route))),
        "route_sha256": digest(route_raw),
        "schema": "paper43-route-strict-validation-v1",
        "science_sha256": digest(science_raw),
        "state": state,
        "status": "PASS",
    }


def main(argv: list[str]) -> int:
    if not sys.flags.isolated or not sys.dont_write_bytecode:
        raise RuntimeError("validate_route_a.py requires python3 -I -B")
    if len(argv) == 3 and argv[0] == "--batch":
        batch, batch_raw = load(Path(argv[1]))
        science, science_raw = load(Path(argv[2]))
        schema, _ = load(SCHEMA_PATH)
        if type(batch) is not list:
            raise ValueError("Route mutation batch must be a list")
        accepted: list[str] = []
        rejected: list[dict[str, str]] = []
        seen: set[str] = set()
        for row in batch:
            if type(row) is not dict or set(row) != {"id", "route"} \
                    or type(row["id"]) is not str or row["id"] in seen:
                raise ValueError("Route mutation batch row failure")
            seen.add(row["id"])
            route_raw = canonical(row["route"])
            try:
                validate(row["route"], route_raw, science, science_raw, schema)
            except Exception as error:  # each mutation is expected to reject
                rejected.append({"id": row["id"], "reason": str(error)})
            else:
                accepted.append(row["id"])
        result = {
            "accepted_ids": accepted,
            "batch_sha256": digest(batch_raw),
            "consumer": "strict_route_validator",
            "mutation_count": len(batch),
            "rejected": rejected,
            "rejected_count": len(rejected),
            "schema": "paper43-route-mutation-batch-result-v1",
            "status": "PASS" if not accepted and len(rejected) == len(batch) else "FAIL",
        }
        sys.stdout.buffer.write(canonical(result))
        return 0 if result["status"] == "PASS" else 1
    if len(argv) != 2:
        raise SystemExit("usage: validate_route_a.py [--batch BATCH.json] ROUTE.yaml SCIENCE.json")
    route, route_raw = load(Path(argv[0]))
    science, science_raw = load(Path(argv[1]))
    schema, _ = load(SCHEMA_PATH)
    sys.stdout.buffer.write(canonical(validate(route, route_raw, science, science_raw, schema)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
