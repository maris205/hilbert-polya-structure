#!/usr/bin/env python3
"""Hostile repaired-hash semantic mutations for the C178 checker."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "code/c178_harmonic_strobe_checker.py"
EVIDENCE = ROOT / "results/c178_harmonic_strobe_evidence.json"


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def set_path(data: object, path: tuple[object, ...], value: object) -> None:
    cursor = data
    for key in path[:-1]:
        cursor = cursor[key]  # type: ignore[index]
    cursor[path[-1]] = value  # type: ignore[index]


MUTATIONS: list[tuple[str, tuple[object, ...], object]] = [
    ("schema", ("schema",), "mutated"),
    ("candidate", ("candidate_id",), "HCS-C000"),
    ("date", ("evaluation_date",), "2026-08-25"),
    ("source", ("source_commit",), "0" * 40),
    ("evaluator", ("evaluator", "version"), "0.1.0"),
    ("evaluator_hash", ("evaluator", "sha256"), "0" * 64),
    ("scope", ("scope_literal",), "BROKEN_SCOPE"),
    ("phase_space", ("source_lock", "phase_space"), "X=S^1"),
    ("hamiltonian", ("source_lock", "hamiltonian"), "H=0"),
    ("flow", ("source_lock", "flow"), "identity"),
    ("angle", ("source_lock", "angle_coordinate"), "wrong orientation"),
    ("parameter_domain", ("source_lock", "parameter_domain"), "theta modulo 2*pi for every lift"),
    ("strobe", ("source_lock", "strobe"), "T=R_(2*theta)"),
    ("clock", ("source_lock", "clock"), "heat time"),
    ("measure", ("source_lock", "gaussian_measure"), "Lebesgue"),
    ("Koopman_convention", ("source_lock", "koopman_convention"), "inverse"),
    ("quantum_H", ("source_lock", "quantum_hamiltonian"), "number operator only"),
    ("quantum_Q", ("source_lock", "quantum_propagator"), "heat semigroup"),
    ("quantum_cover", ("source_lock", "quantum_cover"), "Q_(theta+2*pi)=Q_theta"),
    ("determinant", ("source_lock", "determinant_convention"), "regularized"),
    ("training", ("source_lock", "training_data"), "target fitted"),
    ("iterate", ("classical_theorem", "iterate"), "T^n=R_theta"),
    ("fixed_dichotomy", ("classical_theorem", "fixed_set_dichotomy"), "always origin"),
    ("irrational_zeta", ("classical_theorem", "irrational_case"), "zeta=1"),
    ("rational_case", ("classical_theorem", "rational_case"), "finite count"),
    ("period", ("classical_theorem", "period_structure"), "isolated cycles"),
    ("zero_edge", ("classical_theorem", "zero_angle_edge"), "origin only"),
    ("reversor", ("classical_theorem", "reversor"), "S*T*S=T"),
    ("Gaussian_basis", ("gaussian_koopman_theorem", "basis"), "wrong normalization"),
    ("Gaussian_action", ("gaussian_koopman_theorem", "basis_action"), "negative phase"),
    ("Gaussian_irrational", ("gaussian_koopman_theorem", "irrational_spectrum"), "finite spectrum"),
    ("Gaussian_rational", ("gaussian_koopman_theorem", "rational_spectrum"), "simple spectrum"),
    ("Gaussian_compact", ("gaussian_koopman_theorem", "noncompact"), False),
    ("Gaussian_schatten", ("gaussian_koopman_theorem", "finite_schatten_class"), True),
    ("Gaussian_fredholm", ("gaussian_koopman_theorem", "ordinary_fredholm_determinant_available"), True),
    ("Gaussian_antiunitary", ("gaussian_koopman_theorem", "antiunitary_reversal"), "none"),
    ("quantum_clock", ("quantum_theorem", "same_clock"), "different clock"),
    ("quantum_domain", ("quantum_theorem", "parameter_domain"), "theta modulo 2*pi"),
    ("Hermite_energy", ("quantum_theorem", "hermite_basis"), "Hh_j=j h_j"),
    ("Hermite_phase", ("quantum_theorem", "hermite_spectrum"), "positive phase"),
    ("quantum_rational_spectrum", ("quantum_theorem", "rational_spectrum"), "unrotated b-th roots independent of representative"),
    ("quantum_periodicity", ("quantum_theorem", "metaplectic_periodicity"), "Q_(theta+2*pi)=Q_theta"),
    ("Egorov_q", ("quantum_theorem", "egorov_q"), "q fixed"),
    ("Egorov_p", ("quantum_theorem", "egorov_p"), "p fixed"),
    ("quantum_reversal", ("quantum_theorem", "conjugation_reversal"), "KQK=Q"),
    ("quantum_compact", ("quantum_theorem", "noncompact"), False),
    ("quantum_trace", ("quantum_theorem", "trace_class"), True),
    ("quantum_fredholm", ("quantum_theorem", "ordinary_fredholm_determinant_available"), True),
    ("heat_clock", ("quantum_theorem", "heat_wick_boundary"), "same clock"),
    ("fixed_row", ("finite_regression_sentinels", "rational_fixed_rows", 0, "fixed_set"), "origin"),
    ("irrational_row", ("finite_regression_sentinels", "irrational_fixed_rows", 0, "n_alpha_is_integer"), True),
    ("Laguerre_row", ("finite_regression_sentinels", "laguerre_rows", 0, "normalized_product"), "2"),
    ("Koopman_row", ("finite_regression_sentinels", "koopman_phase_rows", 20, "root_exponent"), 999),
    ("quantum_row", ("finite_regression_sentinels", "quantum_phase_rows", 20, "energy_twice"), 0),
    ("quantum_row_2pi_sign", ("finite_regression_sentinels", "quantum_phase_rows", 20, "two_pi_phase_ratio_exponent"), 0),
    ("route_tuple", ("route_a", "tuple"), []),
    ("route_overall", ("route_a", "overall"), "ROUTE_A_SUCCESS_ROUTE_B_READY"),
    ("route_b", ("route_a", "route_b_invocation_allowed"), True),
    ("zero_table", ("scope_flags", "used_target_zero_table"), True),
    ("heat_flag", ("scope_flags", "used_heat_or_wick_as_same_clock"), True),
    ("global_phase_flag", ("scope_flags", "silently_quotiented_quantum_global_phase"), True),
    ("finite_proof", ("integrity", "finite_ledgers_are_proof"), True),
    ("external_review", ("integrity", "external_reviewer_simulated"), True),
    ("model_rejection", ("integrity", "model_rejected_as_primary_route_a_candidate"), False),
]


def checker_rejects(data: dict, path: Path) -> bool:
    path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    completed = subprocess.run(
        [sys.executable, str(CHECKER), "--input", str(path)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return completed.returncode != 0


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    repaired = 0
    with tempfile.TemporaryDirectory(prefix="c178-mutation-") as directory:
        path = Path(directory) / "mutated.json"
        for label, field_path, value in MUTATIONS:
            mutated = deepcopy(original)
            set_path(mutated, field_path, value)
            mutated["payload_sha256"] = canonical_hash(mutated)
            if not checker_rejects(mutated, path):
                raise AssertionError(f"checker accepted repaired-hash mutation: {label}")
            repaired += 1

        stale = deepcopy(original)
        stale["classical_theorem"]["iterate"] = "T_theta^n=R_((n+1)*theta)"
        stale_rejected = checker_rejects(stale, path)
        if not stale_rejected:
            raise AssertionError("checker accepted stale-hash mutation")

    print(
        json.dumps(
            {
                "status": "C178_MUTATION_PASS",
                "repaired_hash_mutation_rejections": repaired,
                "stale_hash_mutation_rejections": int(stale_rejected),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
