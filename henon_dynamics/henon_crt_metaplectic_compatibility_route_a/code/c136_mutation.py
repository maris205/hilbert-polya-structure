#!/usr/bin/env python3
"""Repaired-hash semantic and stale-hash mutation suite for HCS-C136."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "c136_independent_checker", ROOT / "code" / "c136_crt_metaplectic_checker.py"
)
CHECKER = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(CHECKER)
BASE = json.loads((ROOT / "results" / "c136_crt_metaplectic_evidence.json").read_text())


def rehash(obj: dict) -> None:
    obj.pop("payload_sha256", None)
    obj["payload_sha256"] = hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def changed(path: list, value, repair: bool = True) -> dict:
    obj = copy.deepcopy(BASE)
    node = obj
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    if repair:
        rehash(obj)
    return obj


SEMANTIC_CASES = [
    (["schema"], "bad"),
    (["candidate_id"], "HCS-C999"),
    (["date_utc"], "2026-08-23"),
    (["scope"], "expanded"),
    (["classical_matrix", 0, 0], 2),
    (["source_dependency", "evidence_sha256"], "0" * 64),
    (["source_dependency", "used_content"], "external target"),
    (["family", "levels"], "prime levels only"),
    (["family", "characters"], "c=1 only"),
    (["family", "factorizations"], "unordered factor multiset"),
    (["family", "certified_pairs", 0], [3, 9]),
    (["phase_conventions", "omega_r"], "exp(-2*pi*i/r)"),
    (["phase_conventions", "half"], "floor(r/2)"),
    (["phase_conventions", "fourier"], "unscaled Fourier"),
    (["phase_conventions", "chirp"], "wrong chirp"),
    (["phase_conventions", "unitary"], "F*C"),
    (["phase_conventions", "weyl"], "Q_r^q*P_r^p"),
    (["phase_conventions", "conjugation"], "fitted conjugation"),
    (["phase_conventions", "antiunitary"], "Theta=K"),
    (["phase_conventions", "clock"], "two steps"),
    (["antiunitary_theorem", "hypotheses"], "all even and odd levels"),
    (["antiunitary_theorem", "definition"], "Theta_[r,c]=K_r"),
    (["antiunitary_theorem", "involution_identity"], "Theta^2=-I"),
    (["antiunitary_theorem", "unitary_reversal_identity"], "Theta U Theta^-1=U"),
    (["antiunitary_theorem", "weyl_swap_identity"], "Theta W(q,p) Theta^-1=W(-q,-p)"),
    (["antiunitary_theorem", "crt_identity"], "projective anti-tensor"),
    (["antiunitary_theorem", "crt_tensor_convention"], "undefined tensor convention"),
    (["two_factor_theorem", "hypotheses"], "all M,N"),
    (["two_factor_theorem", "canonical_identification"], "fitted identification"),
    (["two_factor_theorem", "local_characters"], "c_M=c_N=1"),
    (["two_factor_theorem", "fourier_identity"], "naive tensor"),
    (["two_factor_theorem", "chirp_identity"], "naive tensor"),
    (["two_factor_theorem", "weyl_identity"], "phase omitted"),
    (["two_factor_theorem", "unitary_identity"], "projective only"),
    (["two_factor_theorem", "antiunitary_identity"], "antiunitary compatibility omitted"),
    (["two_factor_theorem", "scalar_anomaly"], True),
    (["two_factor_theorem", "clock_preserved"], False),
    (["certified_pair_receipts", 0, "a_M_inverse_of_N"], 1),
    (["certified_pair_receipts", 0, "fourier_kernel_ledger", "sha256"], "0" * 64),
    (["certified_pair_receipts", 1, "weyl_basis_action_ledger", "cases"], 1),
    (["certified_pair_receipts", 0, "conjugation_basis_ledger", "sha256"], "1" * 64),
    (["certified_pair_receipts", 0, "antiunitary_crt_kernel_ledgers", 0, "character"], 3),
    (["certified_pair_receipts", 0, "antiunitary_crt_kernel_ledgers", 1, "ledger", "sha256"], "2" * 64),
    (["certified_pair_receipts", 2, "naive_standard_character_tensor_compatible"], True),
    (["certified_triple_receipts", 0, "characters", 0, "direct_twists", "3"], 0),
    (["certified_triple_receipts", 0, "characters", 0, "left_bracket_twists", "5"], 0),
    (["certified_triple_receipts", 0, "characters", 0, "right_bracket_twists", "7"], 0),
    (["certified_triple_receipts", 1, "characters", 1, "unitary_kernel_ledger", "sha256"], "f" * 64),
    (["four_factor_coherence_receipt", "characters", 0, "bracketings", "balanced", "11"], 0),
    (["antiunitary_level_receipts", 0, "r"], 7),
    (["antiunitary_level_receipts", 1, "unit_characters", 0, "character"], 2),
    (["antiunitary_level_receipts", 0, "unit_characters", 0, "theta_square_ledger", "sha256"], "3" * 64),
    (["antiunitary_level_receipts", 1, "unit_characters", 0, "unitary_reversal_kernel_ledger", "cases"], 1),
    (["antiunitary_level_receipts", 2, "unit_characters", 0, "weyl_swap_basis_action_ledger", "sha256"], "4" * 64),
    (["multi_factor_theorem", "ordered_leaves"], "unordered leaves"),
    (["multi_factor_theorem", "antiunitary_identity"], "anti-tensor omitted"),
    (["multi_factor_theorem", "coherence"], "independent of factor permutation"),
    (["multi_factor_theorem", "factor_permutation_coherence_claimed"], True),
    (["controls", "naive_standard_character", "naive_tensor_exponent_mod_15"], 1),
    (["controls", "naive_standard_character", "row_x0_forces_projective_scalar_one"], False),
    (["controls", "naive_standard_character", "naive_tensor_equal_even_projectively"], True),
    (["controls", "raw_residue_instead_of_inverse", "raw_residue_rule_valid"], True),
    (["controls", "noncoprime", "crt_identification_available"], True),
    (["controls", "even_modulus", "inverse_of_two_exists"], True),
    (["exact_certificate", "pair_weyl_basis_action_cases"], 658313),
    (["exact_certificate", "pair_conjugation_basis_cases"], 305),
    (["exact_certificate", "pair_antiunitary_crt_kernel_cases"], 27039),
    (["exact_certificate", "antiunitary_theta_square_cases"], 2403),
    (["exact_certificate", "antiunitary_unitary_reversal_cases"], 2403),
    (["exact_certificate", "antiunitary_weyl_swap_cases"], 31927),
    (["exact_certificate", "all_antiunitary_receipts_pass"], False),
    (["exact_certificate", "all_pair_receipts_pass"], False),
    (["progress", "closed_gate"], "standard factors compatible"),
    (["progress", "new_route_a_coordinate"], "A4_UNSUPPORTED"),
    (["progress", "over_prior_gate"], "Route-B ready"),
    (["route_a", "tuple"], ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_ROUTE_B_READY"]),
    (["route_a", "overall"], "ROUTE_A_SUCCESS_ROUTE_B_READY"),
    (["route_a", "route_b_invocation_allowed"], True),
    (["scope_flags", "claims_hilbert_polya"], True),
    (["scope_flags", "claims_factor_permutation_coherence"], True),
    (["nonclaims", 0], "standard c=1 factors are directly compatible"),
    (["nonclaims", 3], "factor permutations are coherent"),
    (["unexpected_top_level_key"], True),
]


repaired_caught = 0
for path, value in SEMANTIC_CASES:
    try:
        CHECKER.validate(changed(path, value, repair=True))
    except (AssertionError, KeyError, TypeError, ValueError):
        repaired_caught += 1
assert repaired_caught == len(SEMANTIC_CASES)

stale_caught = 0
try:
    CHECKER.validate(changed(["schema"], "stale-hash-schema", repair=False))
except (AssertionError, KeyError, TypeError, ValueError):
    stale_caught = 1
assert stale_caught == 1

print(
    "C136 mutation suite: PASS "
    f"({repaired_caught} repaired-hash semantic + {stale_caught} stale-hash rejected)"
)
