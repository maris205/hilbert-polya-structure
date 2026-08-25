#!/usr/bin/env python3
"""Repaired-hash semantic and stale-hash attacks for HCS-C168."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c168_rank_three_evidence.json"
CHECKER = ROOT / "code/c168_rank_three_checker.py"


def digest(data: dict) -> str:
    work = dict(data)
    work.pop("payload_sha256", None)
    encoded = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(encoded).hexdigest()


def put(data: object, path: tuple[object, ...], value: object) -> None:
    target = data
    for key in path[:-1]:
        target = target[key]  # type: ignore[index]
    target[path[-1]] = value  # type: ignore[index]


def main() -> None:
    source = json.loads(EVIDENCE.read_text())
    mutations = [
        ("schema", ("schema",), "forged"),
        ("candidate", ("candidate_id",), "HCS-X"),
        ("date", ("evaluation_date",), "2025-01-01"),
        ("scope", ("scope_literal",), "expanded"),
        ("commit", ("source_commit",), "0" * 40),
        ("top_extra", ("forged",), True),
        ("object", ("source_lock", "object"), "fitted gate"),
        ("cycle", ("source_lock", "full_cycle"), "B_k"),
        ("clock", ("source_lock", "clock"), "one tick"),
        ("weight", ("source_lock", "spectral_weight"), "distinct labels"),
        ("phase_convention", ("source_lock", "phase_convention"), "principal argument"),
        ("scaling", ("source_lock", "joint_scaling"), "uncentered"),
        ("k_cutoff", ("source_lock", "cutoffs", "spectral_k_max"), 23),
        ("m_cutoff", ("source_lock", "cutoffs", "fourier_m_max"), 23),
        ("control_cutoff", ("source_lock", "cutoffs", "hole_zero_k_max"), 23),
        ("precision", ("source_lock", "precision"), "floating point"),
        ("forbidden", ("source_lock", "forbidden_data"), "none"),
        ("lock_extra", ("source_lock", "forged"), True),
        ("polynomial", ("one_site_spectrum", "characteristic_polynomial"), "x^4"),
        ("rank", ("one_site_spectrum", "rank"), 4),
        ("diagonalizable", ("one_site_spectrum", "diagonalizable"), False),
        ("eigenvalue", ("one_site_spectrum", "eigenvalues", 2), "1"),
        ("modulus", ("one_site_spectrum", "nonzero_moduli", 1), "1"),
        ("phase", ("one_site_spectrum", "normalized_phases", 1), "1"),
        ("phase_sum", ("one_site_spectrum", "phase_sum"), "0"),
        ("phase_product", ("one_site_spectrum", "phase_product"), "1"),
        ("ratio", ("one_site_spectrum", "phase_ratio"), "1"),
        ("ratio_trace", ("one_site_spectrum", "ratio_trace"), "-1"),
        ("nontorsion", ("one_site_spectrum", "ratio_not_root_of_unity"), False),
        ("nontorsion_proof", ("one_site_spectrum", "nontorsion_proof"), "numerical"),
        ("spectrum_extra", ("one_site_spectrum", "forged"), True),
        ("secular_product", ("all_k_secular_theorem", "multinomial_product"), "1"),
        ("degree", ("all_k_secular_theorem", "nonzero_degree"), "4^k"),
        ("zero_space", ("all_k_secular_theorem", "zero_generalized_eigenspace_dimension"), "4^k"),
        ("basis", ("all_k_secular_theorem", "diagonalization_basis"), "Jordan guess"),
        ("collisions", ("all_k_secular_theorem", "phase_labels_may_collide"), False),
        ("distinct", ("all_k_secular_theorem", "distinct_phase_count_not_claimed"), False),
        ("secular_proof", ("all_k_secular_theorem", "proof_basis"), "finite ledger"),
        ("secular_extra", ("all_k_secular_theorem", "forged"), True),
        ("measure", ("phase_limit_theorem", "phase_measure"), "delta_1"),
        ("fourier_identity", ("phase_limit_theorem", "fourier_identity"), "0"),
        ("fixed_contraction", ("phase_limit_theorem", "fixed_mode_contraction"), "uniform"),
        ("contraction_proof", ("phase_limit_theorem", "contraction_proof"), "plot"),
        ("weak_limit", ("phase_limit_theorem", "weak_limit"), "point mass"),
        ("uniform_gap", ("phase_limit_theorem", "all_m_uniform_gap_claimed"), True),
        ("finite_tv", ("phase_limit_theorem", "finite_k_tv_to_continuous_haar"), "0"),
        ("atomic_warning", ("phase_limit_theorem", "atomicity_warning"), "none"),
        ("phase_extra", ("phase_limit_theorem", "forged"), True),
        ("log_law", ("log_modulus_joint_theorem", "one_site_log_modulus_law"), "deterministic"),
        ("mean", ("log_modulus_joint_theorem", "mean"), "0"),
        ("variance", ("log_modulus_joint_theorem", "variance"), "0"),
        ("normalization", ("log_modulus_joint_theorem", "normalization"), "uncentered"),
        ("mixed_transform", ("log_modulus_joint_theorem", "mixed_transform"), "0"),
        ("joint_limit", ("log_modulus_joint_theorem", "joint_limit"), "correlated"),
        ("independence", ("log_modulus_joint_theorem", "asymptotic_independence"), False),
        ("joint_proof", ("log_modulus_joint_theorem", "proof_basis"), "marginals only"),
        ("joint_extra", ("log_modulus_joint_theorem", "forged"), True),
        ("control_gate", ("hole_zero_control", "gate"), "closed"),
        ("control_polynomial", ("hole_zero_control", "characteristic_polynomial"), "x^4"),
        ("control_spectrum", ("hole_zero_control", "nonzero_spectrum", 1), "1"),
        ("control_steps", ("hole_zero_control", "phase_steps_as_i_exponents", 1), 1),
        ("control_group", ("hole_zero_control", "torsion_group"), "circle"),
        ("control_fourier", ("hole_zero_control", "nontrivial_fourier_modulus"), "1"),
        ("control_bound", ("hole_zero_control", "tv_bound"), "TV<=1"),
        ("control_limit", ("hole_zero_control", "limit"), "Haar circle"),
        ("control_extra", ("hole_zero_control", "forged"), True),
        ("reflection", ("antiunitary_control", "digit_reflection"), "identity"),
        ("antiunitary", ("antiunitary_control", "antiunitary"), "K"),
        ("intertwining", ("antiunitary_control", "intertwining"), "fixed hole"),
        ("meaning", ("antiunitary_control", "meaning"), "self-adjoint limit"),
        ("selfadjoint", ("antiunitary_control", "fixed_hole_self_adjoint_limit"), True),
        ("anti_limit", ("antiunitary_control", "antiunitary_limiting_operator_claimed"), True),
        ("anti_extra", ("antiunitary_control", "forged"), True),
        ("spectral_k", ("spectral_ledgers", 4, "k"), 99),
        ("spectral_ambient", ("spectral_ledgers", 5, "ambient_dimension"), 1),
        ("spectral_degree", ("spectral_ledgers", 6, "nonzero_secular_degree"), 1),
        ("spectral_zero", ("spectral_ledgers", 7, "zero_generalized_eigenspace_dimension"), 0),
        ("spectral_labels", ("spectral_ledgers", 8, "multinomial_label_count"), 1),
        ("spectral_damped", ("spectral_ledgers", 9, "damped_count_multiplicities_by_j", 2), 999),
        ("spectral_mass", ("spectral_ledgers", 10, "nonzero_multiplicity_sum"), 1),
        ("spectral_distinct", ("spectral_ledgers", 11, "distinct_phase_count_claimed"), True),
        ("spectral_extra", ("spectral_ledgers", 12, "forged"), True),
        ("spectral_delete", ("spectral_ledgers",), deepcopy(source["spectral_ledgers"][:-1])),
        ("fourier_m", ("fourier_ledgers", 3, "m"), 99),
        ("fourier_pair", ("fourier_ledgers", 4, "phase_sum_coefficients_a_b", 0), "999"),
        ("fourier_basis", ("fourier_ledgers", 5, "phase_sum_basis"), "decimal"),
        ("fourier_modulus", ("fourier_ledgers", 6, "one_step_fourier_modulus_squared"), "1"),
        ("fourier_strict", ("fourier_ledgers", 7, "strict_contraction_from_nontorsion"), False),
        ("fourier_decimal", ("fourier_ledgers", 8, "fourier_magnitude_at_k_12_decimal"), "1"),
        ("fourier_extra", ("fourier_ledgers", 9, "forged"), True),
        ("fourier_delete", ("fourier_ledgers",), deepcopy(source["fourier_ledgers"][:-1])),
        ("hole_k", ("hole_zero_ledgers", 3, "k"), 99),
        ("hole_counts", ("hole_zero_ledgers", 4, "counts_by_i_exponent_mod_4", 0), 999),
        ("hole_mass", ("hole_zero_ledgers", 5, "count_sum"), 1),
        ("hole_num", ("hole_zero_ledgers", 6, "tv_to_uniform_numerator"), 999),
        ("hole_den", ("hole_zero_ledgers", 7, "tv_to_uniform_denominator"), 1),
        ("hole_bound", ("hole_zero_ledgers", 8, "fourier_bound_numerator_same_denominator"), 13),
        ("hole_extra", ("hole_zero_ledgers", 9, "forged"), True),
        ("hole_delete", ("hole_zero_ledgers",), deepcopy(source["hole_zero_ledgers"][:-1])),
        ("route_tuple", ("route_a", "tuple", 0), "A1_PASS"),
        ("route_overall", ("route_a", "overall"), "ROUTE_A_ADVANCE"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("phase_claim", ("claim_boundary", "source_side_phase_haar_limit"), False),
        ("selfadjoint_claim", ("claim_boundary", "self_adjoint_limit"), True),
        ("target_claim", ("claim_boundary", "target_divisor_matching"), True),
        ("euler_claim", ("claim_boundary", "euler_factors"), True),
        ("root_claim", ("claim_boundary", "root_numbers"), True),
        ("hp_claim", ("claim_boundary", "hilbert_polya_operator"), True),
        ("hard_gate", ("integrity", "hard_gate_status"), "FAIL"),
        ("pivot", ("integrity", "pivot_required"), True),
        ("finite_proof", ("integrity", "finite_ledgers_are_proof"), True),
        ("external_review", ("integrity", "external_reviewer_simulated"), True),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c168-mutations-") as temporary:
        for name, path, value in mutations:
            candidate = deepcopy(source)
            put(candidate, path, value)
            candidate["payload_sha256"] = digest(candidate)
            output = Path(temporary) / f"{name}.json"
            output.write_text(json.dumps(candidate, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            result = subprocess.run(
                [sys.executable, str(CHECKER), str(output), "--mutation-fast"],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                raise AssertionError(f"checker accepted repaired mutation {name}")
            rejected.append(name)
        stale = deepcopy(source)
        stale["payload_sha256"] = "0" * 64
        output = Path(temporary) / "stale.json"
        output.write_text(json.dumps(stale, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        result = subprocess.run(
            [sys.executable, str(CHECKER), str(output), "--mutation-fast"],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            raise AssertionError("checker accepted stale hash")
    print(
        json.dumps(
            {
                "status": "C168_MUTATION_PASS",
                "repaired_hash_rejected": len(rejected),
                "stale_hash_rejected": 1,
                "total": len(rejected) + 1,
                "names": rejected,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
