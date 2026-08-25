#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C163."""
from __future__ import annotations

import argparse
from decimal import Decimal, getcontext
from fractions import Fraction
from hashlib import sha256
import json
from math import comb
from pathlib import Path


K_MAX = 32
M_MAX = 24


def canonical_hash(data: dict) -> str:
    work = dict(data)
    work.pop("payload_sha256", None)
    return sha256(json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def poly_rows(limit: int) -> list[list[Fraction]]:
    rows = [[Fraction(2)], [Fraction(0), Fraction(1)]]
    for _ in range(2, limit + 1):
        shifted = [Fraction(0)] + rows[-1]
        size = max(len(shifted), len(rows[-2]))
        result = [Fraction(0) for _ in range(size)]
        for j, value in enumerate(shifted):
            result[j] += value
        for j, value in enumerate(rows[-2]):
            result[j] -= value
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        rows.append(result)
    return rows[: limit + 1]


def decimal_rows(polynomials: list[list[Fraction]]) -> list[dict]:
    getcontext().prec = 90
    c = (Decimal(3).sqrt() - Decimal(111).sqrt()) / Decimal(6)
    rows = []
    for m in range(1, M_MAX + 1):
        value = sum(
            Decimal(coefficient.numerator) / Decimal(coefficient.denominator) * c**power
            for power, coefficient in enumerate(polynomials[m])
        )
        q2 = (Decimal(2) + value) / Decimal(4)
        if q2 < 0 and abs(q2) < Decimal("1e-75"):
            q2 = Decimal(0)
        q = q2.sqrt()
        rows.append(
            {
                "m": m,
                "two_cos_m_delta_polynomial_ascending": [text(x) for x in polynomials[m]],
                "r_power_not_one": True,
                "q_m_squared_decimal": format(q2, ".60f"),
                "q_m_decimal": format(q, ".60f"),
                "fourier_magnitude_at_k_16_decimal": format(q**16, ".60f"),
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=Path(__file__).resolve().parents[1] / "results/c163_phase_evidence.json")
    parser.add_argument("--mutation-fast", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0

    def check(condition: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    def keys(mapping: object, expected: set[str], message: str) -> None:
        check(isinstance(mapping, dict) and set(mapping) == expected, message)

    top = {
        "schema", "candidate_id", "evaluation_date", "scope_literal", "source_commit", "source_lock",
        "phase_algebra", "all_k_phase_theorem", "general_binary_phase_dichotomy", "phase_k_ledgers",
        "fourier_decay_ledgers", "controls", "route_a", "claim_boundary", "integrity", "payload_sha256",
    }
    keys(data, top, "top closure")
    check(data["schema"] == "hcs-c163-open-walsh-phase-equidistribution-v1", "schema")
    check(data["candidate_id"] == "HCS-C163", "candidate")
    check(data["evaluation_date"] == "2026-08-25", "date")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["source_commit"] == "63f75cf476711de93e6096ef74ac16969e1127d0", "source commit")
    check(data["payload_sha256"] == canonical_hash(data), "payload hash")

    lock = data["source_lock"]
    keys(lock, {"object", "full_cycle", "clock", "phase_convention", "measure_convention", "joint_scaling", "cutoffs", "precision", "forbidden_data"}, "source lock closure")
    check(lock["object"] == "frozen C148/C153/C158 three-symbol open Walsh gate with A=F3^*diag(1,0,1)", "object")
    check(lock["full_cycle"] == "C_k=B_k^k=A^(tensor k)", "cycle")
    check(lock["clock"] == "one B_k application is one tick; one full cycle is exactly k ticks", "clock")
    check(lock["phase_convention"] == "phase(rho)=rho/|rho| for every nonzero eigenvalue rho of C_k", "phase convention")
    check(lock["measure_convention"] == "mu_k is the algebraic-multiplicity-weighted probability measure on surviving phases", "measure convention")
    check(lock["joint_scaling"] == "X_k=(1/k)log|rho| and Y_k=sqrt(k)*(X_k+log(3)/4)", "joint scaling")
    check(lock["cutoffs"] == {"phase_k_max": 32, "fourier_m_max": 24, "moved_hole_k_max": 32}, "cutoffs")
    check(lock["precision"] == "exact integers and rational polynomials in c=2cos(delta); 60-place decimals are sentinels only", "precision")
    check(lock["forbidden_data"] == "target zeros or divisors, primes, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya, Route B", "forbidden data")

    algebra = data["phase_algebra"]
    keys(algebra, {"one_site_polynomial", "tau", "q0", "phase_units", "phase_ratio", "two_cos_delta", "c_squared_q_sqrt37", "primitive_irreducible_integer_polynomial_coefficients_ascending", "primitive_irreducible_integer_polynomial", "monic_rational_minimal_polynomial", "irreducibility_receipt", "not_algebraic_integer", "integrality_obstruction", "phase_ratio_not_root_of_unity", "proof_receipt"}, "phase algebra closure")
    check(algebra["one_site_polynomial"] == "lambda*(lambda^2-tau*lambda+q0)", "one-site polynomial")
    check(algebra["tau"] == "sqrt(3)/6-i/2", "tau")
    check(algebra["q0"] == "-1/2-sqrt(3)*i/6", "q0")
    check(algebra["phase_units"] == "u_+/-=lambda_+/-/|lambda_+/-| with |lambda_+|>|lambda_-|>0", "phase units")
    check(algebra["phase_ratio"] == "r=u_+/u_-=exp(i*delta)", "phase ratio")
    check(algebra["two_cos_delta"] == "c=r+r^(-1)=2cos(delta)=(sqrt(3)-sqrt(111))/6", "phase cosine")
    check(algebra["c_squared_q_sqrt37"] == ["19/6", "-1/6"], "c square receipt")
    check(algebra["primitive_irreducible_integer_polynomial_coefficients_ascending"] == [27, 0, -19, 0, 3], "primitive integer coefficients")
    check(algebra["primitive_irreducible_integer_polynomial"] == "3*c^4-19*c^2+27", "primitive integer polynomial text")
    check(algebra["monic_rational_minimal_polynomial"] == "c^4-(19/3)*c^2+9", "monic rational minimal polynomial text")
    # Independent Q(sqrt(37)) arithmetic verifies c^2 and its quadratic equation.
    y = (Fraction(19, 6), Fraction(-1, 6))
    def add(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        return a[0] + b[0], a[1] + b[1]
    def scale(a: tuple[Fraction, Fraction], q: Fraction) -> tuple[Fraction, Fraction]:
        return q * a[0], q * a[1]
    def multiply(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        return a[0] * b[0] + 37 * a[1] * b[1], a[0] * b[1] + a[1] * b[0]
    quadratic_value = add(add(scale(multiply(y, y), Fraction(3)), scale(y, Fraction(-19))), (Fraction(27), Fraction(0)))
    check(quadratic_value == (0, 0), "c square quadratic equation")
    check(37 not in {n * n for n in range(7)}, "37 nonsquare")
    check(algebra["irreducibility_receipt"] == "c^2 has irreducible polynomial 3*y^2-19*y+27 with discriminant 37, while c is not in Q(sqrt(37)) because that would put sqrt(3) there", "irreducibility receipt")
    check(algebra["not_algebraic_integer"] is True, "nonintegrality")
    check(algebra["integrality_obstruction"] == "the monic rational minimal polynomial has nonintegral coefficient -19/3; equivalently its primitive integer associate has nonunit leading coefficient 3", "integrality obstruction")
    check(algebra["phase_ratio_not_root_of_unity"] is True, "nontorsion")
    check(algebra["proof_receipt"] == "if r were a root of unity then r+r^(-1)=c would be an algebraic integer, contradicting the nonintegral coefficient in its monic rational minimal polynomial", "root-unity proof")

    theorem = data["all_k_phase_theorem"]
    keys(theorem, {"phase_measure", "fourier_identity", "fourier_magnitude", "fixed_cutoff_bound", "weak_limit", "joint_limit", "sigma_squared", "mixed_transform", "asymptotic_independence", "proof_basis"}, "theorem closure")
    check(theorem["phase_measure"] == "mu_k=2^(-k)*sum_(j=0)^k binom(k,j)*delta_(u_-^k*r^j)", "phase measure")
    check(theorem["fourier_identity"] == "mu_hat_k(m)=u_-^(m*k)*((1+r^m)/2)^k for every integer m", "Fourier identity")
    check(theorem["fourier_magnitude"] == "|mu_hat_k(m)|=|cos(m*delta/2)|^k", "Fourier magnitude")
    check(theorem["fixed_cutoff_bound"] == "for p(z)=sum_|m|<=M a_m z^m, |mu_k(p)-Haar(p)|<=sum_(0<|m|<=M)|a_m|*q_m^k, q_m=|cos(m*delta/2)|<1", "cutoff bound")
    check(theorem["weak_limit"] == "mu_k converges weakly to normalized Haar measure on the unit circle", "Haar limit")
    check(theorem["joint_limit"] == "(Y_k,phase(rho)) converges jointly to Normal(0,sigma^2) tensor Haar", "joint limit")
    check(theorem["sigma_squared"] == "sigma^2=(log(|lambda_+|/|lambda_-|))^2/4", "variance")
    check(theorem["mixed_transform"] == "E[exp(i*t*Y_k)*phase(rho)^m]=u_-^(m*k)*exp(-i*t*d*sqrt(k)/2)*((1+r^m*exp(i*t*d/sqrt(k)))/2)^k, d=log(|lambda_+|/|lambda_-|)", "mixed transform")
    check(theorem["asymptotic_independence"] is True, "asymptotic independence")
    check(theorem["proof_basis"] == "binomial theorem, the non-root-of-unity obstruction, Fourier density on the circle, and the Bernoulli characteristic-function CLT", "proof basis")

    dichotomy = data["general_binary_phase_dichotomy"]
    keys(dichotomy, {"non_torsion_branch", "torsion_branch", "torsion_tv_bound", "frozen_branch"}, "dichotomy closure")
    check(dichotomy["non_torsion_branch"] == "if r is not a root of unity, the binomial phase measures converge weakly to Haar", "nontorsion branch")
    check(dichotomy["torsion_branch"] == "if r has exact order h, the measure converges in total variation to the uniform measure on the moving coset u_-^k<r>", "torsion branch")
    check(dichotomy["torsion_tv_bound"] == "TV<=((h-1)/2)*max_(1<=m<h)|cos(pi*m/h)|^k", "torsion bound")
    check(dichotomy["frozen_branch"] == "NON_TORSION_HAAR", "frozen branch")

    ledgers = data["phase_k_ledgers"]
    check(isinstance(ledgers, list) and len(ledgers) == K_MAX, "phase ledger length")
    for k, row in enumerate(ledgers, 1):
        keys(row, {"k", "ambient_dimension", "surviving_multiplicity", "zero_generalized_eigenspace_dimension", "distinct_phase_atoms", "multiplicities_by_j", "multiplicity_sum", "phase_atoms_distinct_reason"}, f"phase row closure {k}")
        expected = [comb(k, j) for j in range(k + 1)]
        check(row["k"] == k, f"phase k {k}")
        check(row["ambient_dimension"] == 3**k, f"ambient {k}")
        check(row["surviving_multiplicity"] == 2**k, f"survival {k}")
        check(row["zero_generalized_eigenspace_dimension"] == 3**k - 2**k, f"zero space {k}")
        check(row["distinct_phase_atoms"] == k + 1, f"distinct atoms {k}")
        check(row["multiplicities_by_j"] == expected, f"multiplicities {k}")
        check(row["multiplicity_sum"] == sum(expected) == 2**k, f"mass {k}")
        check(row["phase_atoms_distinct_reason"] == "r is not a root of unity", f"distinct reason {k}")

    polynomials = poly_rows(M_MAX)
    frozen_fourier = data["fourier_decay_ledgers"]
    check(isinstance(frozen_fourier, list) and len(frozen_fourier) == M_MAX, "Fourier ledger length")
    expected_fourier = decimal_rows(polynomials)
    for m, (row, expected) in enumerate(zip(frozen_fourier, expected_fourier), 1):
        keys(row, {"m", "two_cos_m_delta_polynomial_ascending", "r_power_not_one", "q_m_squared_decimal", "q_m_decimal", "fourier_magnitude_at_k_16_decimal"}, f"Fourier row closure {m}")
        check(row == expected, f"Fourier receipt {m}")
        check(Decimal(row["q_m_squared_decimal"]) >= 0, f"q2 nonnegative {m}")
        check(Decimal(row["q_m_decimal"]) < 1, f"q strict {m}")

    controls = data["controls"]
    keys(controls, {"projector_order", "moved_hole", "closed_parent"}, "controls closure")
    order = controls["projector_order"]
    keys(order, {"gate", "result"}, "order closure")
    check(order["gate"] == "A_right=diag(1,0,1)F3^*=F3*A*F3^*", "order gate")
    check(order["result"] == "unitary similarity preserves the phase ratio and the Haar and joint limits", "order result")
    moved = controls["moved_hole"]
    keys(moved, {"projector", "nonzero_eigenvalues", "phase_ratio", "phase_ratio_order", "limit", "tv_bound", "residue_ledgers"}, "moved closure")
    check(moved["projector"] == "diag(0,1,1)", "moved projector")
    check(moved["nonzero_eigenvalues"] == "-i and -1/sqrt(3)", "moved eigenvalues")
    check(moved["phase_ratio"] == "i" and moved["phase_ratio_order"] == 4, "moved ratio")
    check(moved["limit"] == "uniform measure on the moving four-point coset (-1)^k< i >", "moved limit")
    check(moved["tv_bound"] == "TV<=(3/2)*(sqrt(2)/2)^k", "moved bound")
    residues = moved["residue_ledgers"]
    check(isinstance(residues, list) and len(residues) == K_MAX, "residue ledger length")
    getcontext().prec = 80
    for k, row in enumerate(residues, 1):
        keys(row, {"k", "counts_by_j_mod_4", "count_sum", "tv_to_uniform_coset_numerator", "tv_to_uniform_coset_denominator"}, f"residue row closure {k}")
        counts = [sum(comb(k, j) for j in range(k + 1) if j % 4 == residue) for residue in range(4)]
        numerator = sum(abs(4 * count - 2**k) for count in counts)
        check(row["k"] == k and row["counts_by_j_mod_4"] == counts, f"residue counts {k}")
        check(row["count_sum"] == sum(counts) == 2**k, f"residue mass {k}")
        check(row["tv_to_uniform_coset_numerator"] == numerator, f"tv numerator {k}")
        check(row["tv_to_uniform_coset_denominator"] == 8 * 2**k, f"tv denominator {k}")
        exact_tv = Decimal(numerator) / Decimal(8 * 2**k)
        bound = Decimal(3) / Decimal(2) * (Decimal(2).sqrt() / Decimal(2))**k
        check(exact_tv <= bound, f"tv inequality {k}")
    closed = controls["closed_parent"]
    keys(closed, {"projector", "result"}, "closed closure")
    check(closed["projector"] == "I_3", "closed projector")
    check(closed["result"] == "the one-site gate is unitary with three surviving phases, so it lies outside the binary theorem rather than serving as a forged binary control", "closed result")

    check(data["route_a"] == {"tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_UNITARY_OR_SCATTERING_CANDIDATE"], "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False}, "Route A")
    boundary = {
        "source_side_phase_limit": True,
        "source_side_joint_modulus_phase_limit": True,
        "self_adjoint_limit": False,
        "antiunitary_limit": False,
        "target_divisor_matching": False,
        "target_functional_equation": False,
        "target_counting_law": False,
        "prime_like_correspondence": False,
        "arithmetic_local_data": False,
        "euler_factors": False,
        "root_numbers": False,
        "automorphy": False,
        "hilbert_polya_operator": False,
    }
    check(data["claim_boundary"] == boundary, "claim boundary")
    check(data["integrity"] == {"pivot_required": False, "hard_gate": "unconditional all-k phase theorem for the frozen gate", "hard_gate_status": "PASS", "finite_ledgers_are_proof": False, "external_reviewer_simulated": False}, "integrity")
    print(json.dumps({"status": "C163_CHECKER_PASS", "assertions": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
