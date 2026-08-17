#!/usr/bin/env python3
"""Independent no-import auditor for the Paper 43 Route JSON/YAML subset."""

from __future__ import annotations

import copy
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any


TOP_KEYS = {
    "a0", "a1", "a2", "a3", "a4", "adversarial_controls",
    "artifact_path_base", "authority_integration", "blocking_conditions",
    "branch_status", "candidate_id", "claim_boundary", "code_commit",
    "evaluation_date", "freeze_note", "next_smallest_test", "overall_verdict",
    "projection_firewall", "round2_clues", "route_b",
    "route_b_invocation_allowed", "route_tuple", "skill", "skill_version",
    "source_commit", "source_lock", "target_and_root_metrics", "terminal_codes",
    "typed_return_map",
}
ROOT = Path(__file__).resolve().parents[2]
DECLARED_GENERATED_ARTIFACTS = {
    "results/factor_periodic_rigidity_certificate.json",
    "results/operator_ownership_certificate.json",
    "results/periodic_ledger_certificate.json",
    "results/scientific_results.json",
    "results/source_resolver.json",
}
EXPECTED_NORMALIZED_ROUTE_SHA256 = "636b61c59c8e2b04dde5cbdae5b0a62f7c28ccf0e7f054f40ccc944c503112ee"
STATE_A_FREEZE_NOTE = (
    "State-A first-artifact Route card. Static implementation inputs were frozen "
    "before the declared canonical rerun; the theorem, selector, literature, "
    "witnesses, and earlier smoke diagnostics were already known. The run is "
    "retrospective and supplies no novelty, priority, ranking, or authorization credit."
)
NESTED = {
    "a0": {"arithmetic_controls", "artifacts", "evidence_status", "strongest_evidence",
           "strongest_failure", "verdict"},
    "a1": {"artifacts", "evidence_status", "metrics", "strongest_evidence",
           "strongest_failure", "verdict"},
    "a2": {"artifacts", "evidence_status", "metrics", "strongest_evidence",
           "strongest_failure", "verdict"},
    "a3": {"analytic_structure", "artifacts", "evidence_status", "strongest_evidence",
           "strongest_failure", "verdict", "weil_compression"},
    "a4": {"artifacts", "evidence_status", "metrics", "strongest_evidence",
           "strongest_failure", "verdict"},
    "adversarial_controls": {"controls_used", "proves_too_much_risk", "verdict"},
    "authority_integration": {"git_operations_by_integrator", "paper_manifest_present",
                              "state", "status"},
    "projection_firewall": {"declared_repairs_are_exhaustive", "decisive_witnesses",
                            "factor_type", "primitive_type", "required_fields",
                            "source_type", "target_comparator_type"},
    "route_b": {"invocation_allowed", "reason"},
    "source_lock": {"allowed_data", "arithmetic_origin", "artifact_paths",
                    "candidate_definition", "clock", "cocycle", "code_commit", "cutoff",
                    "determinant_convention", "dynamics", "family", "forbidden_data",
                    "function_space", "main_theorem_marker", "normalization", "object",
                    "orbit_cutoff", "parameter_provenance", "parameters", "phase_space",
                    "potential_function", "precision", "regularization_order",
                    "roof_function", "training_data"},
    "target_and_root_metrics": {"exact_period_quantifier", "exact_window_quantifier",
                                "factor_fiber_bound", "numerical_root_search_used",
                                "target_zero_data_used"},
    "terminal_codes": {"determinant_comparison", "factor_cycle_creation", "literature",
                       "rational_prime_identification"},
    "typed_return_map": {"factor_marker", "factor_primitive", "factor_repetition",
                         "rational_prime_marker", "rational_prime_same_type_identification_exists",
                         "source_marker", "source_primitive", "source_repetition"},
}


def serialized(value: Any) -> bytes:
    text = json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2,
                      separators=(",", ": "))
    return (text + "\n").encode("ascii")


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def pair_guard(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError("duplicate mapping key")
        output[key] = value
    return output


def decode(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=pair_guard)
    if type(value) is not dict or serialized(value) != raw:
        raise ValueError("route/science byte form is not canonical JSON-subset YAML")
    return value, raw


def relative_path(value: str) -> bool:
    if type(value) is not str or not value or "\\" in value:
        return False
    pure = PurePosixPath(value)
    return not pure.is_absolute() and all(part not in {".", ".."} for part in pure.parts)


def artifact_resolves(value: str) -> bool:
    if not relative_path(value) or value.startswith("writer_snapshot/"):
        return False
    if value in DECLARED_GENERATED_ARTIFACTS:
        return True
    path = ROOT / value
    return path.is_file() and not path.is_symlink()


def normalized_copy(route: dict[str, Any]) -> dict[str, Any]:
    value = copy.deepcopy(route)
    for owner, key in ((value, "source_commit"), (value, "code_commit"),
                       (value, "freeze_note"), (value["source_lock"], "code_commit")):
        owner[key] = "NORMALIZED_PROVENANCE"
    value["authority_integration"].clear()
    value["authority_integration"].update({
        "git_operations_by_integrator": 0,
        "paper_manifest_present": False,
        "state": "NORMALIZED",
        "status": "NORMALIZED_PROVENANCE",
    })
    return value


def audit(route: dict[str, Any], route_raw: bytes,
          science: dict[str, Any], science_raw: bytes) -> dict[str, Any]:
    verdicts = [route[f"a{index}"]["verdict"] for index in range(5)]
    evidence = [route[f"a{index}"]["evidence_status"] for index in range(5)]
    checks = {
        "artifact_base_rebased": route.get("artifact_path_base")
            == "papers/43-squarefree-factor-periodic-rigidity",
        "candidate_and_skill": (route.get("candidate_id"), route.get("skill"),
                                route.get("skill_version"))
            == ("SD-C45", "route-a-evaluator", "0.2.0"),
        "canonical_json_yaml_subset": serialized(route) == route_raw,
        "chronology_not_prospective": (
            science["integration_chronology"]["prospective"] is False
            and science["integration_chronology"]["results_unseen"] is False
            and science["integration_chronology"]["novelty_credit"] is False
        ),
        "determinant_orientation": (
            science["periodic_ledger"]["determinant_orientation"] == "D_AM=zeta_AM_inverse"
            and science["periodic_ledger"]["inverse_determinant"] == "1-z"
        ),
        "duplicate_boundary_external": (
            science["literature_boundary"]["conditional_code"] == "STOP_DUPLICATE"
            and science["literature_boundary"]["route_terminal"] is False
            and b"STOP_DUPLICATE" not in route_raw
        ),
        "evidence_vector": evidence
            == ["MODELING_CHOICE", "PROVED", "PROVED", "PROVED", "NOT_TESTABLE"],
        "exact_nested_key_sets": all(set(route.get(name, {})) == keys
                                     for name, keys in NESTED.items()),
        "exact_top_key_set": set(route) == TOP_KEYS,
        "factor_scope": (
            science["claim_scope"]["factor_class"]
            == "all_continuous_surjective_fully_Z_equivariant_compact_metrizable_factors_with_homeomorphism"
            and science["universal_aperiodic_factor_theorem_claimed"] is False
        ),
        "fixed_counts": all(row["fixed_count"] == 1
                            for row in science["periodic_ledger"]["fixed_count_rows"]),
        "marker_firewall": (
            route["typed_return_map"]["factor_marker"] == "z_power_time"
            and route["typed_return_map"]["rational_prime_marker"] == "independent_u"
            and route["typed_return_map"]["rational_prime_same_type_identification_exists"] is False
        ),
        "operator_scope": (
            science["operator_ledger"]["matrix"] == [[1]]
            and science["operator_ledger"]["full_state_operator"] is False
            and science["operator_ledger"]["rational_prime_owner"] is False
        ),
        "overall_rejected": route["overall_verdict"] == "ROUTE_A_REJECTED"
            == science["route"]["overall_verdict"],
        "repair_nonexhaustive": route["projection_firewall"]["declared_repairs_are_exhaustive"]
            is False,
        "route_b_locked": (
            route["route_b_invocation_allowed"] is False
            and route["route_b"]["invocation_allowed"] is False
            and route["route_b"]["reason"]
            == "same_object_primitive_ledger_and_completed_structure_fail"
        ),
        "route_tuple": verdicts == route["route_tuple"] == science["route"]["tuple"]
            == ["A0_FAIL", "A1_FAIL", "A2_ANALYTIC_DETERMINANT", "A3_FAIL", "A4_FAIL"],
        "science_hash_bound": route["a2"]["metrics"]["scientific_results_sha256"]
            == sha(science_raw),
        "target_data_absent": (
            route["target_and_root_metrics"]["target_zero_data_used"] is False
            and route["target_and_root_metrics"]["numerical_root_search_used"] is False
        ),
        "terminal_mapping": route["terminal_codes"] == science["terminal_codes"] == {
            "determinant_comparison": "STOP_TRIVIAL_ONE_MINUS_Z_DIVISOR",
            "factor_cycle_creation": "STOP_PROXIMAL_PERIODIC_RIGIDITY",
            "literature": "PROCEED_ONLY_AS_INTERNAL_EXACT_CLOSURE",
            "rational_prime_identification": "STOP_SINGLETON_PRIMITIVE_SUPPORT",
        },
        "typed_source_factor_comparator": (
            route["projection_firewall"]["source_type"] == "SquarefreeAdmissiblePoint"
            and route["projection_firewall"]["factor_type"] == "TopologicalFactorState"
            and route["projection_firewall"]["target_comparator_type"] == "RationalPrimeAtom"
        ),
    }
    artifacts = list(route["source_lock"]["artifact_paths"])
    for index in range(5):
        artifacts.extend(route[f"a{index}"]["artifacts"])
    checks["artifact_paths_portable"] = all(artifact_resolves(path) for path in artifacts)
    triple = [route["source_commit"], route["code_commit"], route["source_lock"]["code_commit"]]
    authority = route["authority_integration"]
    if authority["state"] == "A":
        provenance_ok = (
            triple == ["PENDING_FIRST_ARTIFACT_COMMIT"] * 3
            and authority["paper_manifest_present"] is False
            and authority["status"] == "STATE_A_FIRST_ARTIFACT_PENDING_TRIPLE"
            and authority["git_operations_by_integrator"] == 0
            and route["freeze_note"] == STATE_A_FREEZE_NOTE
        )
    elif authority["state"] == "B":
        provenance_ok = (
            len(set(triple)) == 1 and re.fullmatch(r"[0-9a-f]{40}", triple[0]) is not None
            and triple[0] != "0" * 40 and authority["paper_manifest_present"] is True
            and authority["status"] == "STATE_B_METADATA_ONLY_SEAL"
            and authority["git_operations_by_integrator"] == 0
            and route["freeze_note"] == (
                "State-B metadata-only seal. The source_commit, code_commit, and "
                "source_lock.code_commit fields all bind Stage-1 artifact commit "
                f"{triple[0]}; no science, code, experiment, result, report, writer, "
                "PDF, research, registry, or root-registration byte changed."
            )
        )
    else:
        provenance_ok = False
    checks["paired_provenance_state"] = provenance_ok
    checks["full_normalized_payload_exact"] = (
        sha(serialized(normalized_copy(route))) == EXPECTED_NORMALIZED_ROUTE_SHA256
    )
    if not all(checks.values()):
        raise ValueError("independent Route audit failures: "
                         + ",".join(sorted(key for key, value in checks.items() if not value)))
    return {
        "checks": checks,
        "checks_passed": len(checks),
        "checks_total": len(checks),
        "normalized_route_sha256": sha(serialized(normalized_copy(route))),
        "route_sha256": sha(route_raw),
        "schema": "paper43-independent-route-audit-v1",
        "science_sha256": sha(science_raw),
        "state": authority["state"],
        "status": "PASS",
    }


def main(args: list[str]) -> int:
    if not sys.flags.isolated or not sys.dont_write_bytecode:
        raise RuntimeError("audit_route_a.py requires python3 -I -B")
    if len(args) == 3 and args[0] == "--batch":
        batch_raw = Path(args[1]).read_bytes()
        batch = json.loads(batch_raw.decode("ascii"), object_pairs_hook=pair_guard)
        if serialized(batch) != batch_raw:
            raise ValueError("independent Route mutation batch is not canonical")
        science, science_raw = decode(Path(args[2]))
        if type(batch) is not list:
            raise ValueError("independent Route mutation batch must be a list")
        accepted: list[str] = []
        rejected: list[dict[str, str]] = []
        seen: set[str] = set()
        for row in batch:
            if type(row) is not dict or set(row) != {"id", "route"} \
                    or type(row["id"]) is not str or row["id"] in seen:
                raise ValueError("independent Route mutation row failure")
            seen.add(row["id"])
            route_raw = serialized(row["route"])
            try:
                audit(row["route"], route_raw, science, science_raw)
            except Exception as error:  # each mutation is expected to reject
                rejected.append({"id": row["id"], "reason": str(error)})
            else:
                accepted.append(row["id"])
        result = {
            "accepted_ids": accepted,
            "batch_sha256": sha(batch_raw),
            "consumer": "independent_route_auditor",
            "mutation_count": len(batch),
            "rejected": rejected,
            "rejected_count": len(rejected),
            "schema": "paper43-independent-route-mutation-batch-result-v1",
            "status": "PASS" if not accepted and len(rejected) == len(batch) else "FAIL",
        }
        sys.stdout.buffer.write(serialized(result))
        return 0 if result["status"] == "PASS" else 1
    if len(args) != 2:
        raise SystemExit("usage: audit_route_a.py [--batch BATCH.json] ROUTE.yaml SCIENCE.json")
    route, route_raw = decode(Path(args[0]))
    science, science_raw = decode(Path(args[1]))
    sys.stdout.buffer.write(serialized(audit(route, route_raw, science, science_raw)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
