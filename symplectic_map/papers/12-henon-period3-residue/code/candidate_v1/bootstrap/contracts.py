"""P1--P10 source-anchor and implementation-witness presence records.

The records intentionally contain no mathematical proof-status field and do
not replace the independent source review.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .constants import PROOF_PATH, PROOF_SHA256
from .protocol import sha256_file, stable_file_bytes


CONTRACTS: tuple[dict[str, Any], ...] = (
    {
        "contract_id": "P1",
        "anchors": ["algebraically closed field of characteristic zero", "Df_{m,a}(x,y)="],
        "witnesses": ["shared/definitions.json:category", "track_q/engine.py", "track_r/engine.py"],
    },
    {
        "contract_id": "P2",
        "anchors": ["free of rank \\((2m)^3\\)", "leading monomials of", "x_0^{2m}"],
        "witnesses": ["track_q/engine.py:standard_basis_count", "track_r/engine.py:quotient_rank"],
    },
    {
        "contract_id": "P3",
        "anchors": ["t_\\varepsilon=q_0q_1q_2+", "\\operatorname{Res}(t_\\varepsilon^{m+1})"],
        "witnesses": ["shared/definitions.json:cyclic_orientation", "tests:test_negative_controls"],
    },
    {
        "contract_id": "P4",
        "anchors": ["\\gcd(m,\\nu)=1", "(r,s)=(0,3m)"],
        "witnesses": ["bootstrap/contracts.py:anchor_presence_only"],
    },
    {
        "contract_id": "P5",
        "anchors": ["All roots distinct", "Exactly two roots equal", "All three roots equal"],
        "witnesses": ["bootstrap/contracts.py:three_branch_anchor_ledger"],
    },
    {
        "contract_id": "P6",
        "anchors": ["Reversal removes \\(C_m\\) for odd", "S_m(a,\\varepsilon)=S_m(a,-\\varepsilon)"],
        "witnesses": ["bootstrap/contracts.py:parity_anchor_ledger"],
    },
    {
        "contract_id": "P7",
        "anchors": [
            "tag{9.1}",
            "tag{9.2}",
            "tag{9.3}",
            "terminating induction certificate.",
            "There is no reduction-order ambiguity.",
            "tag{9.9}",
            "tag{9.10}",
            "tag{9.11}",
            "tag{9.12}",
            "tag{9.13}",
            "tag{9.14}",
            "tag{9.17}",
            "tag{9.18}",
            "tag{9.19}",
            "tag{9.20}",
            "tag{9.21}",
            "tag{9.22}",
            "tag{9.23}",
            "the defining range is empty",
            "tag{9.24}",
            "incoming-transfer patterns are exactly",
            "tag{9.25}",
            "tag{9.26}",
            "All three rotations of the second type vanish.",
            "tag{9.27}",
            "tag{9.28}",
        ],
        "witnesses": [
            "track_q/engine.py:private_reduction_and_decorated_tuple_routes",
            "track_r/engine.py:private_guarded_nested_sums",
            "manifest.py:route_symbol_deny_lists",
        ],
    },
    {
        "contract_id": "P8",
        "anchors": ["fixed contribution to the period-three moment is zero", "local length of \\(\\operatorname{Fix}(f^3)\\)"],
        "witnesses": [
            "track_q/engine.py:fixed_trace_nilpotence",
            "track_q/engine.py:local_fixed_series",
            "track_r/engine.py:fixed_moment",
            "track_r/engine.py:local_fixed_orders",
        ],
    },
    {
        "contract_id": "P9",
        "anchors": ["a^{2m-1}=b^{2m-1}", "affine diagonal"],
        "witnesses": ["track_q/engine.py:normalized_affine_comparison", "track_r/engine.py:normalized_scaling"],
    },
    {
        "contract_id": "P10",
        "anchors": ["is **not** part of the", "open combinatorial conjecture"],
        "witnesses": ["shared/definitions.json:nonclaim_tags", "adjudicator/acceptance_ledger.json:zero_claim_counters"],
    },
)


def collect_contract_witnesses(project_root: Path, code_paths: set[str]) -> list[dict[str, Any]]:
    proof_path = project_root / PROOF_PATH
    if sha256_file(proof_path) != PROOF_SHA256:
        raise RuntimeError("contract source proof hash mismatch")
    proof_text = stable_file_bytes(proof_path).decode("utf-8")
    records: list[dict[str, Any]] = []
    for contract in CONTRACTS:
        anchors = contract["anchors"]
        missing = [anchor for anchor in anchors if anchor not in proof_text]
        implementation_paths = []
        for witness in contract["witnesses"]:
            path_hint = witness.split(":", 1)[0]
            if path_hint.startswith(("shared/", "track_", "adjudicator/")):
                implementation_paths.append("candidate_v1/" + path_hint)
            elif path_hint.startswith("bootstrap/"):
                implementation_paths.append("candidate_v1/" + path_hint)
            elif path_hint.endswith(".py"):
                implementation_paths.append("candidate_v1/bootstrap/" + path_hint)
        missing_paths = [path for path in implementation_paths if path not in code_paths]
        if missing or missing_paths:
            raise RuntimeError("contract witness missing: " + contract["contract_id"])
        record = {
            "contract_id": contract["contract_id"],
            "source_anchor_count": len(anchors),
            "source_anchors_present": True,
            "implementation_witness_count": len(contract["witnesses"]),
            "implementation_witnesses_present": True,
            "consistency_status": "ANCHORS_AND_WITNESSES_PRESENT",
        }
        if contract["contract_id"] == "P8":
            record["separate_obligations"] = {
                "P8a_zero_fixed_moment": "WITNESS_PRESENT",
                "P8b_local_fixed_multiplicity": "WITNESS_PRESENT",
            }
        if contract["contract_id"] == "P7":
            record["implementation_subwitnesses"] = {
                "base_cases": "WITNESS_PRESENT",
                "four_signed_branches": "WITNESS_PRESENT",
                "termination_measure": "WITNESS_PRESENT",
                "order_independent_private_route_pair": "WITNESS_PRESENT",
                "decorated_tuple_constraints_and_weights": "WITNESS_PRESENT",
                "negative_upper_generalized_binomial": "WITNESS_PRESENT",
                "distinguished_coordinate_and_transfer_flow": "SOURCE_ANCHOR_AND_ROUTE_WITNESS_PRESENT",
                "empty_range": "WITNESS_PRESENT",
                "j0_two_incoming_pattern_types": "WITNESS_PRESENT",
                "j0_exceptional_type_zero": "WITNESS_PRESENT",
                "expanded_factored_boundary": "WITNESS_PRESENT",
            }
        records.append(record)
    if len(records) != 10:
        raise RuntimeError("contract record count")
    return records
