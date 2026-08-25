#!/usr/bin/env python3
"""Repaired-hash and stale-hash hostile tests for HCS-C163."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c163_phase_evidence.json"
CHECKER = ROOT / "code/c163_phase_checker.py"


def digest(data: dict) -> str:
    work = dict(data)
    work.pop("payload_sha256", None)
    return sha256(json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


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
        ("source_object", ("source_lock", "object"), "another gate"),
        ("cycle", ("source_lock", "full_cycle"), "B_k"),
        ("clock", ("source_lock", "clock"), "one cycle"),
        ("phase_convention", ("source_lock", "phase_convention"), "arg principal"),
        ("measure_convention", ("source_lock", "measure_convention"), "distinct phases"),
        ("joint_scaling", ("source_lock", "joint_scaling"), "unscaled"),
        ("phase_cutoff", ("source_lock", "cutoffs", "phase_k_max"), 31),
        ("fourier_cutoff", ("source_lock", "cutoffs", "fourier_m_max"), 23),
        ("precision", ("source_lock", "precision"), "float"),
        ("forbidden", ("source_lock", "forbidden_data"), "none"),
        ("source_extra", ("source_lock", "forged"), True),
        ("one_site", ("phase_algebra", "one_site_polynomial"), "lambda^3"),
        ("tau", ("phase_algebra", "tau"), "0"),
        ("q0", ("phase_algebra", "q0"), "0"),
        ("units", ("phase_algebra", "phase_units"), "undefined"),
        ("ratio", ("phase_algebra", "phase_ratio"), "1"),
        ("cosine", ("phase_algebra", "two_cos_delta"), "0"),
        ("c_square", ("phase_algebra", "c_squared_q_sqrt37", 0), "0"),
        ("primitive_integer_coefficient", ("phase_algebra", "primitive_irreducible_integer_polynomial_coefficients_ascending", 4), 1),
        ("primitive_integer_text", ("phase_algebra", "primitive_irreducible_integer_polynomial"), "c^2-1"),
        ("monic_rational_minimum", ("phase_algebra", "monic_rational_minimal_polynomial"), "c^4-19*c^2+27"),
        ("irreducibility", ("phase_algebra", "irreducibility_receipt"), "assumed"),
        ("integrality", ("phase_algebra", "not_algebraic_integer"), False),
        ("integrality_obstruction", ("phase_algebra", "integrality_obstruction"), "numerical angle only"),
        ("nontorsion", ("phase_algebra", "phase_ratio_not_root_of_unity"), False),
        ("root_proof", ("phase_algebra", "proof_receipt"), "numerical"),
        ("phase_algebra_extra", ("phase_algebra", "forged"), True),
        ("measure", ("all_k_phase_theorem", "phase_measure"), "delta_1"),
        ("fourier_identity", ("all_k_phase_theorem", "fourier_identity"), "0"),
        ("fourier_magnitude", ("all_k_phase_theorem", "fourier_magnitude"), "1"),
        ("cutoff_bound", ("all_k_phase_theorem", "fixed_cutoff_bound"), "none"),
        ("weak_limit", ("all_k_phase_theorem", "weak_limit"), "delta_1"),
        ("joint_limit", ("all_k_phase_theorem", "joint_limit"), "correlated"),
        ("sigma", ("all_k_phase_theorem", "sigma_squared"), "0"),
        ("mixed", ("all_k_phase_theorem", "mixed_transform"), "0"),
        ("independence", ("all_k_phase_theorem", "asymptotic_independence"), False),
        ("proof_basis", ("all_k_phase_theorem", "proof_basis"), "finite plot"),
        ("theorem_extra", ("all_k_phase_theorem", "forged"), True),
        ("dichotomy_non", ("general_binary_phase_dichotomy", "non_torsion_branch"), "delta"),
        ("dichotomy_tor", ("general_binary_phase_dichotomy", "torsion_branch"), "Haar"),
        ("dichotomy_bound", ("general_binary_phase_dichotomy", "torsion_tv_bound"), "TV<=1"),
        ("dichotomy_frozen", ("general_binary_phase_dichotomy", "frozen_branch"), "TORSION"),
        ("phase_k", ("phase_k_ledgers", 10, "k"), 99),
        ("ambient", ("phase_k_ledgers", 11, "ambient_dimension"), 1),
        ("survival", ("phase_k_ledgers", 12, "surviving_multiplicity"), 1),
        ("zero_space", ("phase_k_ledgers", 13, "zero_generalized_eigenspace_dimension"), 0),
        ("distinct", ("phase_k_ledgers", 14, "distinct_phase_atoms"), 1),
        ("multiplicity", ("phase_k_ledgers", 15, "multiplicities_by_j", 2), 999),
        ("mass", ("phase_k_ledgers", 16, "multiplicity_sum"), 1),
        ("distinct_reason", ("phase_k_ledgers", 17, "phase_atoms_distinct_reason"), "finite check"),
        ("phase_row_extra", ("phase_k_ledgers", 18, "forged"), True),
        ("phase_rows_delete", ("phase_k_ledgers",), deepcopy(source["phase_k_ledgers"][:-1])),
        ("fourier_m", ("fourier_decay_ledgers", 3, "m"), 99),
        ("fourier_poly", ("fourier_decay_ledgers", 4, "two_cos_m_delta_polynomial_ascending", 0), "999"),
        ("fourier_nonresonance", ("fourier_decay_ledgers", 5, "r_power_not_one"), False),
        ("q2", ("fourier_decay_ledgers", 6, "q_m_squared_decimal"), "0"),
        ("q", ("fourier_decay_ledgers", 7, "q_m_decimal"), "1"),
        ("decay", ("fourier_decay_ledgers", 8, "fourier_magnitude_at_k_16_decimal"), "1"),
        ("fourier_row_extra", ("fourier_decay_ledgers", 9, "forged"), True),
        ("fourier_rows_delete", ("fourier_decay_ledgers",), deepcopy(source["fourier_decay_ledgers"][:-1])),
        ("controls_extra", ("controls", "forged"), True),
        ("order_gate", ("controls", "projector_order", "gate"), "different"),
        ("order_result", ("controls", "projector_order", "result"), "changes"),
        ("moved_projector", ("controls", "moved_hole", "projector"), "diag(1,1,0)"),
        ("moved_spectrum", ("controls", "moved_hole", "nonzero_eigenvalues"), "unknown"),
        ("moved_ratio", ("controls", "moved_hole", "phase_ratio"), "1"),
        ("moved_order", ("controls", "moved_hole", "phase_ratio_order"), 1),
        ("moved_limit", ("controls", "moved_hole", "limit"), "Haar"),
        ("moved_bound", ("controls", "moved_hole", "tv_bound"), "none"),
        ("residue_count", ("controls", "moved_hole", "residue_ledgers", 9, "counts_by_j_mod_4", 0), 999),
        ("residue_mass", ("controls", "moved_hole", "residue_ledgers", 10, "count_sum"), 1),
        ("residue_num", ("controls", "moved_hole", "residue_ledgers", 11, "tv_to_uniform_coset_numerator"), 0),
        ("residue_den", ("controls", "moved_hole", "residue_ledgers", 12, "tv_to_uniform_coset_denominator"), 1),
        ("residue_extra", ("controls", "moved_hole", "residue_ledgers", 13, "forged"), True),
        ("closed_projector", ("controls", "closed_parent", "projector"), "0"),
        ("closed_result", ("controls", "closed_parent", "result"), "binary"),
        ("route_tuple", ("route_a", "tuple", 0), "A1_PASS"),
        ("overall", ("route_a", "overall"), "ROUTE_A_ADVANCE"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("phase_claim", ("claim_boundary", "source_side_phase_limit"), False),
        ("selfadjoint", ("claim_boundary", "self_adjoint_limit"), True),
        ("target", ("claim_boundary", "target_divisor_matching"), True),
        ("euler", ("claim_boundary", "euler_factors"), True),
        ("root_number", ("claim_boundary", "root_numbers"), True),
        ("hilbert_polya", ("claim_boundary", "hilbert_polya_operator"), True),
        ("pivot", ("integrity", "pivot_required"), True),
        ("hard_gate", ("integrity", "hard_gate_status"), "FAIL"),
        ("finite_proof", ("integrity", "finite_ledgers_are_proof"), True),
        ("external_review", ("integrity", "external_reviewer_simulated"), True),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c163-mutations-") as temporary:
        for name, path, value in mutations:
            candidate = deepcopy(source)
            put(candidate, path, value)
            candidate["payload_sha256"] = digest(candidate)
            output = Path(temporary) / f"{name}.json"
            output.write_text(json.dumps(candidate, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            result = subprocess.run([sys.executable, str(CHECKER), str(output), "--mutation-fast"], capture_output=True, text=True)
            if result.returncode == 0:
                raise AssertionError(f"checker accepted repaired mutation {name}")
            rejected.append(name)
        stale = deepcopy(source)
        stale["payload_sha256"] = "0" * 64
        output = Path(temporary) / "stale.json"
        output.write_text(json.dumps(stale, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        if subprocess.run([sys.executable, str(CHECKER), str(output), "--mutation-fast"], capture_output=True, text=True).returncode == 0:
            raise AssertionError("checker accepted stale hash")
    print(json.dumps({"status": "C163_MUTATION_PASS", "repaired_hash_rejected": len(rejected), "stale_hash_rejected": 1, "total": len(rejected) + 1, "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
