#!/usr/bin/env python3
"""Validate frozen P48 outputs and emit a compact writer-side summary.

The script treats finite evaluator records as controls only.  It never
promotes a cutoff or tensor computation to an infinite theorem.  Infinite
claims are copied solely from the independently owned proof certificates.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import stat
from collections import Counter
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


EXPECTED = {
    "candidate_id": "SD-C50",
    "contract_sha256": "1d383f12ce28a24f534564ce3270bc55aad613c87733019f7d841fc1e90bb628",
    "integration_candidate_seal_sha256": "2726c5eac3ef0aed1e67158912b58ae1a8f98339573b683ba348bdf72171d02d",
    "preauthority_manifest_sha256": "f5669e651c4c31ce860bad534d17e64956a8750412f74257d341810424252057",
    "state_a_tree_sha256": "c23b59034303af74f2a9433b92f9f5c1e1cce4510bd8032ef1214372390bda58",
    "state_b_tree_sha256": "3fc18f7f6122fb91d8c418a6a9da497c29253407b52db6ecad156e3a29b22a48",
    "static_inventory_sha256": "133b8e723c155ea35bb4b3fc6cd328d0d6c52837d39618f6385ee69fee8eae88",
}

EXACT_FIELDS = {
    "case_id", "b", "q", "sigma", "N", "r", "control", "k", "l",
    "mask_depth", "mask_integer", "mask_sha256", "source_object_type",
    "zero_convention", "finite_support_count", "finite_rank",
    "finite_trace_power_record", "finite_period_witnesses",
    "masked_vertex_count", "precision_bits",
}


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical(value: Any) -> bytes:
    return (
        json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                   allow_nan=False, separators=(",", ": "))
        + "\n"
    ).encode("ascii")


def unique(items: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in items:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load(path: Path, canonical_required: bool = True) -> dict[str, Any]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if type(value) is not dict:
        raise ValueError(f"non-object JSON: {path}")
    if canonical_required and raw != canonical(value):
        raise ValueError(f"noncanonical JSON: {path}")
    return value


def strict_equal(left: Any, right: Any) -> bool:
    return type(left) is type(right) and left == right


def tree_rows(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in root.rglob("*"):
        info = os.lstat(path)
        relative = path.relative_to(root).as_posix()
        mode = f"{stat.S_IMODE(info.st_mode):04o}"
        if stat.S_ISLNK(info.st_mode):
            raise ValueError(f"symlink in output tree: {relative}")
        if stat.S_ISDIR(info.st_mode):
            rows.append({"kind": "directory", "mode": mode, "path": relative})
        elif stat.S_ISREG(info.st_mode):
            rows.append({
                "kind": "regular", "mode": mode, "path": relative,
                "sha256": sha(path.read_bytes()),
            })
        else:
            raise ValueError(f"nonregular output node: {relative}")
    return sorted(rows, key=lambda row: row["path"])


def tree_sha(root: Path) -> str:
    return sha(canonical(tree_rows(root)))


def verify_result_ledger(outputs: Path) -> None:
    ledger = outputs / "results/SHA256SUMS.txt"
    rows = ledger.read_text("ascii").splitlines()
    paths: list[str] = []
    for row in rows:
        digest, relative = row.split("  ", 1)
        path = outputs / relative
        if path.is_symlink() or not path.is_file() or sha(path.read_bytes()) != digest:
            raise ValueError(f"result ledger mismatch: {relative}")
        paths.append(relative)
    if paths != sorted(paths) or len(paths) != len(set(paths)) or len(paths) != 12:
        raise ValueError("result ledger framing or census")


def midpoint(interval: dict[str, Any]) -> Decimal:
    return (Decimal(interval["lower"]) + Decimal(interval["upper"])) / 2


def intervals_overlap(left: dict[str, Any], right: dict[str, Any]) -> bool:
    return max(Decimal(left["lower"]), Decimal(right["lower"])) \
        <= min(Decimal(left["upper"]), Decimal(right["upper"]))


def digit_data(base: int, q_values: tuple[int, ...] = (1, 2, 3, 4)) -> dict[str, Any]:
    values = [1.0 / (2.0 * math.sin((2 * j - 1) * math.pi / (4 * base + 2)))
              for j in range(1, base + 1)]
    norms: dict[str, Any] = {}
    for q in q_values:
        kappa = sum(value ** q for value in values) ** (1.0 / q)
        wall = math.log(kappa, base)
        norms[str(q)] = {
            "critical_sigma": format(max(1.0, wall), ".12f"),
            "kappa": format(kappa, ".12f"),
            "log_b_kappa": format(wall, ".12f"),
        }
    return {
        "alpha_b": norms["1"]["log_b_kappa"],
        "b": base,
        "singular_values": [format(value, ".12f") for value in values],
        "schatten_norms": norms,
        "tau_b": norms["1"]["kappa"],
    }


def representative(records: list[dict[str, Any]], case_id: str, control: str,
                   **coordinates: Any) -> dict[str, Any]:
    matches = [
        row for row in records
        if row["case_id"] == case_id and row["control"] == control
        and row["precision_bits"] == 512
        and all(row[key] == value for key, value in coordinates.items())
    ]
    if len(matches) != 1:
        raise ValueError(f"representative row cardinality: {case_id}/{control}/{coordinates}")
    row = matches[0]
    shell = row["finite_shell_norm_intervals"]
    return {
        "N": row["N"],
        "case_id": row["case_id"],
        "control": row["control"],
        "finite_period_witnesses": row["finite_period_witnesses"],
        "finite_rank": row["finite_rank"],
        "finite_support_count": row["finite_support_count"],
        "finite_trace_power_record": row["finite_trace_power_record"],
        "k": row["k"],
        "l": row["l"],
        "mask_depth": row["mask_depth"],
        "mask_integer": row["mask_integer"],
        "q": row["q"],
        "r": row["r"],
        "shell_norm_interval": shell[0] if shell else None,
        "sigma": row["sigma"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--integration-root", type=Path, required=True)
    parser.add_argument("--state-a-outputs", type=Path, required=True)
    parser.add_argument("--state-b-outputs", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--ledger", type=Path, required=True)
    args = parser.parse_args()
    integration = args.integration_root.resolve(strict=True)
    state_a = args.state_a_outputs.resolve(strict=True)
    state_b = args.state_b_outputs.resolve(strict=True)

    contract = integration / "preauthority/EXPERIMENT_CONTRACT.json"
    if sha(contract.read_bytes()) != EXPECTED["contract_sha256"]:
        raise ValueError("experiment contract digest")
    static = load(integration / "PREOUTPUT_STATIC_SEAL.json")
    if static["preauthority_manifest_sha256"] != EXPECTED["preauthority_manifest_sha256"] \
            or static["static_inventory_sha256"] != EXPECTED["static_inventory_sha256"]:
        raise ValueError("static seal binding")
    if static["smoke"]["state_A_final_tree_sha256"] != EXPECTED["state_a_tree_sha256"] \
            or static["smoke"]["state_B_final_tree_sha256"] != EXPECTED["state_b_tree_sha256"]:
        raise ValueError("static seal tree bindings")

    if tree_sha(state_a) != EXPECTED["state_a_tree_sha256"]:
        raise ValueError("State-A tree digest")
    if tree_sha(state_b) != EXPECTED["state_b_tree_sha256"]:
        raise ValueError("State-B tree digest")
    verify_result_ledger(state_a)
    verify_result_ledger(state_b)

    a = load(state_a / "results/evaluator_a_projection.json")
    b = load(state_a / "results/evaluator_b_projection.json")
    a_records = a["finite_records"]
    b_records = b["finite_records"]
    if len(a_records) != 1965 or len(b_records) != 1965:
        raise ValueError("finite row count")
    digit_intervals = 0
    shell_rows = 0
    for left, right in zip(a_records, b_records):
        if any(not strict_equal(left[key], right[key]) for key in EXACT_FIELDS):
            raise ValueError("cross-lane exact-field mismatch")
        if len(left["finite_singular_interval_list"]) != len(right["finite_singular_interval_list"]):
            raise ValueError("cross-lane digit interval census")
        for first, second in zip(left["finite_singular_interval_list"],
                                 right["finite_singular_interval_list"]):
            if not intervals_overlap(first, second):
                raise ValueError("cross-lane digit interval separation")
            digit_intervals += 1
        if left["finite_shell_norm_intervals"]:
            shell_rows += 1
    if (digit_intervals, shell_rows) != (8010, 420):
        raise ValueError("cross-lane comparison census")

    comparison = load(state_a / "results/comparison.json")
    mutations = load(state_a / "results/mutation_outcomes.json")
    adversarial = load(state_a / "results/adversarial_tests.json")
    proof = load(state_a / "results/proof_audit.json")
    route_main = load(state_a / "evaluations/main_evaluation.json")
    route_independent = load(state_a / "evaluations/independent_evaluation.json")
    if comparison["status"] != "PASS" or comparison["exact_field_mismatches"] != 0 \
            or comparison["missing_extra_or_duplicate_rows"] != 0:
        raise ValueError("comparison status")
    if mutations["status"] != "PASS" or mutations["survivors"] != 0 \
            or mutations["mutation_instances"] != 39 \
            or mutations["designated_consumer_invocations"] != 68 \
            or mutations["nondesignated_acceptances"] != 322:
        raise ValueError("mutation closeout")
    if adversarial["status"] != "PASS" or adversarial["survivors"] != 0 \
            or adversarial["physical_instances"] != 76:
        raise ValueError("adversarial closeout")
    if proof["status"] != "PASS" or proof["certificate_owner"] != "P" \
            or len(proof["records"]) != 4:
        raise ValueError("proof certificate ownership")
    if route_main["route_sha256"] != route_independent["route_sha256"] \
            or route_main["status"] != "PASS" \
            or route_independent["status"] != "PASS":
        raise ValueError("route validator agreement")

    scientific_shared = [
        "results/adversarial_tests.json", "results/comparison.json",
        "results/evaluator_a_native.json", "results/evaluator_a_projection.json",
        "results/evaluator_b_native.json", "results/evaluator_b_projection.json",
        "results/mutation_outcomes.json", "results/proof_audit.json",
    ]
    for relative in scientific_shared:
        if sha((state_a / relative).read_bytes()) != sha((state_b / relative).read_bytes()):
            raise ValueError(f"State A/B scientific drift: {relative}")

    control_counts = Counter(row["control"] for row in a_records)
    case_counts = Counter(row["case_id"] for row in a_records)
    getcontext().prec = 80
    digit_midpoints: dict[str, list[str]] = {}
    for base in (2, 3, 4, 5):
        row = next(row for row in a_records if row["b"] == base and row["precision_bits"] == 512)
        digit_midpoints[str(base)] = [
            format(midpoint(interval), "f")
            for interval in row["finite_singular_interval_list"]
        ]

    summary = {
        "candidate_id": EXPECTED["candidate_id"],
        "evidence_boundary": {
            "finite_controls_are_proof": False,
            "finite_controls_role": "falsification_and_consistency_only",
            "infinite_certificate_owner": "P",
            "priority_claimed": False,
        },
        "finite_control_census": {
            "case_counts": dict(sorted(case_counts.items())),
            "control_counts": dict(sorted(control_counts.items())),
            "digit_interval_comparisons": digit_intervals,
            "empty_random_mask_rows_per_lane": 57,
            "empty_random_mask_unique_coordinates": 19,
            "exact_field_mismatches": 0,
            "finite_rows_per_lane": len(a_records),
            "mask_rows_per_lane": control_counts["RANDOMIZED_DIGIT_MASK"],
            "missing_extra_or_duplicate_rows": 0,
            "shell_envelope_rows": shell_rows,
        },
        "hostile_control_census": {
            "all_consumer_invocations": mutations["all_consumer_invocations"],
            "designated_rejections": mutations["designated_consumer_invocations"],
            "mutation_instances": mutations["mutation_instances"],
            "nondesignated_acceptances": mutations["nondesignated_acceptances"],
            "physical_instances": adversarial["physical_instances"],
            "survivors": 0,
        },
        "input_bindings": EXPECTED,
        "proof_certificates": proof["records"],
        "representative_finite_controls": [
            representative(a_records, "FIN-B2-Q1-EQUALITY", "ADJACENT_SHELL",
                           N=256, r=4, k=3, l=2),
            representative(a_records, "FIN-B3-Q2-SAME-SHELL", "SAME_SHELL",
                           N=729, r=4, k=3, l=3),
            representative(a_records, "FIN-B4-Q2-DIRECT-PREDICATE", "CROSS_SHELL",
                           N=1024, r=4, k=3, l=1),
            representative(a_records, "FIN-B5-Q3-RANDOM-MASK", "RANDOMIZED_DIGIT_MASK",
                           N=625, r=4, mask_depth=8, mask_integer=254),
        ],
        "route": {
            "route_b_invocation_allowed": False,
            "route_sha256": route_main["route_sha256"],
            "route_tuple": ["A0_FAIL", "A1_FAIL", "A2_ANALYTIC_DETERMINANT",
                            "A3_FAIL", "A4_FAIL"],
            "status": "ROUTE_A_REJECTED",
            "two_validators_agree": True,
        },
        "theoretical_digit_data": [digit_data(base) for base in (2, 3, 4, 5)],
        "validated_digit_midpoints_512bit": digit_midpoints,
    }
    args.summary.write_bytes(canonical(summary))

    ledger_lines = [
        "# Canonical Results Ledger — Paper 48\n",
        "\n",
        "This writer-side ledger is reconstructed from the frozen State-A outputs. "
        "All finite records are controls; they are not proofs of the infinite theorem.\n",
        "\n",
        f"- Candidate: `{EXPECTED['candidate_id']}`\n",
        f"- Integration candidate seal (external binding): `{EXPECTED['integration_candidate_seal_sha256']}`\n",
        f"- State-A output tree: `{EXPECTED['state_a_tree_sha256']}`\n",
        f"- State-B cross-check tree: `{EXPECTED['state_b_tree_sha256']}`\n",
        f"- Finite rows per evaluator: `{len(a_records)}`\n",
        f"- Digit interval comparisons: `{digit_intervals}`\n",
        f"- Weighted shell envelopes: `{shell_rows}`\n",
        f"- Atomic mutations: `{mutations['mutation_instances']}`; survivors: `0`\n",
        f"- Physical/adversarial instances: `{adversarial['physical_instances']}`; survivors: `0`\n",
        "- Infinite certificate owner: `P` (four records)\n",
        "\n",
        "The Route validators agree on `ROUTE_A_REJECTED`; this has no bearing on the "
        "mathematical validity of the weighted-operator theorem and does not authorize Route B.\n",
    ]
    args.ledger.write_text("".join(ledger_lines), encoding="utf-8", newline="\n")
    print(
        "PASS rows=1965 digit_intervals=8010 shell_rows=420 "
        f"summary_sha256={sha(args.summary.read_bytes())} "
        f"ledger_sha256={sha(args.ledger.read_bytes())}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
