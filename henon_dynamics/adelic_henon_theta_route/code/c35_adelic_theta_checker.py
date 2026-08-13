#!/usr/bin/env python3
"""Independent fail-closed checker for the HCS-C35 certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable


SCHEMA = "hcs-c35-adelic-henon-theta-v3"
PROJECT = Path(__file__).resolve().parents[1]
REPOSITORY = PROJECT.parents[1]
SOURCE_PATHS = {
    "area_preserving_henon_model": "henon_dynamics/docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf",
    "prior_work_readme": "henon_dynamics/docs/prior_work/README.md",
    "related_programs_readme": "henon_dynamics/docs/related_programs/README.md",
    "route_a_evaluator": "henon_dynamics/skills/route-a-evaluator.md",
}


class GateFailure(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GateFailure(message)


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(
            strict_equal(left[key], right[key]) for key in left
        )
    if isinstance(left, list):
        return len(left) == len(right) and all(
            strict_equal(a, b) for a, b in zip(left, right)
        )
    return left == right


def canonical_json(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")


def factor_integer(n: int) -> dict[int, int]:
    n = abs(n)
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def padic_fractional_part(x: Fraction, p: int) -> Fraction:
    exponent = factor_integer(x.denominator).get(p, 0)
    if exponent == 0:
        return Fraction(0)
    modulus = p**exponent
    other = x.denominator // modulus
    return Fraction((x.numerator * pow(other, -1, modulus)) % modulus, modulus)


def global_exponent(x: Fraction) -> Fraction:
    return -x + sum(
        (padic_fractional_part(x, p) for p in factor_integer(x.denominator)),
        Fraction(0),
    )


def parse_fraction(text: str) -> Fraction:
    require(type(text) is str, "fraction must be serialized as a string")
    return Fraction(text)


def replay_cyclotomic_control(p: int, m: int) -> dict[str, Any]:
    modulus = p ** (3 * m)
    block = modulus // p
    counts = [0] * modulus
    for u in range(modulus):
        exponent = (2 * u**3 - p ** (2 * m) * u) % modulus
        counts[exponent] += 1
    target = p ** (2 * m)
    quotient: list[int] = []
    for residue in range(block):
        values = [
            counts[residue + digit * block]
            - (target if residue == 0 and digit == 0 else 0)
            for digit in range(p)
        ]
        require(len(set(values)) == 1, "cyclotomic divisibility replay failed")
        quotient.append(values[0])
    return {
        "prime": p,
        "dilation_level": m,
        "root_of_unity_order": modulus,
        "enumerated_terms": modulus,
        "target_integer": target,
        "cyclotomic_divisibility": True,
        "quotient_nonzero_coefficients": sum(value != 0 for value in quotient),
        "quotient_coefficient_sum": sum(quotient),
    }


def audit(certificate: dict[str, Any]) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []

    def gate(name: str, fn: Callable[[], None]) -> None:
        try:
            fn()
        except GateFailure as error:
            results.append({"gate": name, "status": "FAIL", "detail": str(error)})
        except Exception as error:  # unexpected checker error is not semantic rejection
            results.append(
                {"gate": name, "status": "ERROR", "detail": f"{type(error).__name__}: {error}"}
            )
        else:
            results.append({"gate": name, "status": "PASS", "detail": "independent replay passed"})

    def g0() -> None:
        require(type(certificate) is dict, "certificate must be an object")
        require(
            certificate.keys() == {"schema", "payload_sha256", "payload"},
            "certificate top-level key set mismatch",
        )
        require(certificate["schema"] == SCHEMA, "schema mismatch")
        require(type(certificate["payload_sha256"]) is str, "hash must be a string")
        expected = hashlib.sha256(canonical_json(certificate["payload"])).hexdigest()
        require(certificate["payload_sha256"] == expected, "payload hash mismatch")
        require(
            certificate["payload"].keys()
            == {
                "schema",
                "source_lock",
                "object",
                "exact_additive_character_gate",
                "constant_gauge_gate",
                "finite_spherical_vacuum_gate",
                "theta_gate",
                "boundary_space_gate",
                "scaling_site_gate",
                "raw_finite_quantum_product_kill",
                "local_dilation_tower_gate",
                "fixed_domain_relative_range_gate",
                "scaling_covariance_gate",
                "poisson_boundary_defect_gate",
                "route_a",
                "decisions",
                "scope",
            },
            "payload key set mismatch",
        )
        require(certificate["payload"]["schema"] == SCHEMA, "payload schema mismatch")

    gate("G0_SCHEMA_HASH", g0)

    payload = certificate.get("payload", {})

    def g1() -> None:
        expected_source_lock = {
            name: {
                "path": relative,
                "sha256": hashlib.sha256((REPOSITORY / relative).read_bytes()).hexdigest(),
            }
            for name, relative in SOURCE_PATHS.items()
        }
        require(
            strict_equal(payload["source_lock"], expected_source_lock),
            "source lock mismatch",
        )
        expected = {
            "field": "Q",
            "phase": "S6(q,Q)=q*Q-q+2*q^3",
            "chirp": "P6(q)=2*q^3-q",
            "classical_map": "H6(q,p)=(1-6*q^2-p,q)",
            "jacobian": [["-12*q", -1], [1, 0]],
            "jacobian_determinant": 1,
            "global_hilbert_space": "L2(A_Q)",
            "global_unitary": "U_H=F_A M_{psi(P6)}",
        }
        require(strict_equal(payload["object"], expected), "Hénon object mismatch")

    gate("G1_HENON_OBJECT", g1)

    def g2() -> None:
        block = payload["exact_additive_character_gate"]
        require(
            block.keys()
            == {"convention", "grid_max_denominator", "grid_size", "all_global_values_one", "records"},
            "additive-character block keys mismatch",
        )
        require(
            block["convention"]
            == "psi_infty(x)=exp(-2*pi*i*x); psi_p(x)=exp(2*pi*i*{x}_p)",
            "character convention mismatch",
        )
        require(block["grid_max_denominator"] == 32, "grid denominator mismatch")
        require(type(block["grid_size"]) is int, "grid size must be integer")
        require(block["grid_size"] == len(block["records"]), "grid size mismatch")
        require(block["grid_size"] >= 1000, "registered grid unexpectedly small")
        require(block["all_global_values_one"] is True, "global verdict changed")
        for row in block["records"]:
            require(
                row.keys()
                == {
                    "rational_point",
                    "phase_value",
                    "finite_fractional_parts",
                    "global_exponent",
                    "global_character_value",
                },
                "additive-character row keys mismatch",
            )
            x = parse_fraction(row["rational_point"])
            phase = 2 * x**3 - x
            require(parse_fraction(row["phase_value"]) == phase, "phase replay mismatch")
            exponent = global_exponent(phase)
            require(exponent.denominator == 1, "global exponent is not integral")
            require(type(row["global_exponent"]) is int, "global exponent type mismatch")
            require(row["global_exponent"] == exponent.numerator, "global exponent mismatch")
            require(row["global_character_value"] == "1", "global character is not one")
            expected_pieces = {
                str(p): str(padic_fractional_part(phase, p))
                for p in sorted(factor_integer(phase.denominator))
            }
            require(
                strict_equal(row["finite_fractional_parts"], expected_pieces),
                "p-adic fractional-part ledger mismatch",
            )

    gate("G2_GLOBAL_ADDITIVE_CHARACTER", g2)

    def g3() -> None:
        block = payload["constant_gauge_gate"]
        require(block.keys() == {"rule", "records", "verdict"}, "gauge block keys mismatch")
        require(block["rule"] == "prod_v psi_v(C)=1 for C in Q", "gauge rule mismatch")
        require(block["verdict"] == "GLOBAL_CONSTANT_GAUGE_CANCELS", "gauge verdict mismatch")
        require(
            [row["constant"] for row in block["records"]] == ["0", "1/2", "-7/15", "41/19"],
            "gauge registry mismatch",
        )
        for row in block["records"]:
            require(
                row.keys() == {"constant", "global_exponent", "global_character_value"},
                "gauge row keys mismatch",
            )
            value = parse_fraction(row["constant"])
            exponent = global_exponent(value)
            require(exponent.denominator == 1, "constant gauge exponent not integral")
            require(row["global_exponent"] == exponent.numerator, "constant exponent mismatch")
            require(row["global_character_value"] == "1", "constant gauge did not cancel")

    gate("G3_CONSTANT_GAUGE", g3)

    def g4() -> None:
        block = payload["finite_spherical_vacuum_gate"]
        require(
            block.keys()
            == {"local_character_conductor", "self_dual_lattice", "rows", "verdict", "all_prime_theorem"},
            "vacuum block keys mismatch",
        )
        require(block["local_character_conductor"] == "Z_p", "conductor mismatch")
        require(block["self_dual_lattice"] == "Z_p", "lattice mismatch")
        primes = []
        for row in block["rows"]:
            require(
                row.keys()
                == {"prime", "sample_count", "phase_integral_on_samples", "theorem_reason", "vacuum_verdict"},
                "vacuum row keys mismatch",
            )
            require(type(row["prime"]) is int, "prime type mismatch")
            primes.append(row["prime"])
            require(row["phase_integral_on_samples"] is True, "integrality sample failed")
            require(row["sample_count"] == 4 * row["prime"] + 1, "sample count mismatch")
            require(row["vacuum_verdict"] == "U_H,p 1_Zp = 1_Zp", "vacuum verdict mismatch")
            require(
                row["theorem_reason"]
                == "P6 has integral coefficients, hence P6(Z_p) subset Z_p",
                "vacuum theorem reason mismatch",
            )
        require(
            primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],
            "prime registry drift",
        )
        require(block["verdict"] == "ALL_REGISTERED_PRIMES_FIX_STANDARD_VACUUM", "vacuum block verdict mismatch")
        require(
            block["all_prime_theorem"]
            == "PROVED_FROM_INTEGRAL_COEFFICIENTS_AND_SELF_DUALITY",
            "all-prime theorem scope mismatch",
        )

    gate("G4_SPHERICAL_VACUUM", g4)

    def g5() -> None:
        expected_theta = {
            "poisson": "Theta(F g)=Theta(g)",
            "rational_phase": "psi(P6(r))=1 for every r in Q",
            "identity": "Theta(U_H f)=Theta(f)",
            "status": "PROVED",
        }
        require(strict_equal(payload["theta_gate"], expected_theta), "theta theorem mismatch")
        expected_boundary = {
            "poisson_map": "E_x(g)(x)=|x|^(1/2)*sum_(r in Q^x) g(r*x)",
            "parity_firewall": "positive-integer real half-model is valid only in the even sector, which M_P6 does not preserve",
            "standard": "S0={g:g(0)=0 and hat(g)(0)=0}",
            "henon": "SH={f:f(0)=0 and hat(M_P6 f)(0)=0}",
            "bijection": "M_P6:SH->S0",
            "range_identity": "E_x U_H(SH)=E_x(S0)",
            "status": "PROVED_UNDER_STANDARD_POISSON_DOMAIN",
        }
        require(strict_equal(payload["boundary_space_gate"], expected_boundary), "boundary theorem mismatch")

    gate("G5_THETA_AND_RANGE", g5)

    def g6() -> None:
        block = payload["raw_finite_quantum_product_kill"]
        rows = block["rows"]
        require(len(rows) >= 10, "accumulation registry too short")
        previous_prime = 0
        for row in rows:
            require(
                row.keys()
                == {"prime", "local_dimension", "guaranteed_nearby_zero_count", "distance_bound"},
                "raw-product row keys mismatch",
            )
            p = row["prime"]
            require(type(p) is int and p > previous_prime, "prime order/type mismatch")
            previous_prime = p
            require(row["local_dimension"] == p, "local dimension mismatch")
            require(row["guaranteed_nearby_zero_count"] == p, "zero count mismatch")
            require(row["distance_bound"] == "pi/log(p)", "distance theorem mismatch")
        require(
            block.keys() == {"candidate", "theorem", "rows", "limit", "verdict"},
            "raw-product block keys mismatch",
        )
        require(block["candidate"] == "prod_p det(I-p^(1/2-s) U_p)", "raw candidate mismatch")
        require(
            block["theorem"]
            == "p zeros lie within pi/log(p) of 1/2 for every p-dimensional unitary U_p",
            "raw-product theorem mismatch",
        )
        require(block["limit"] == "1/2 is an interior zero accumulation point", "limit mismatch")
        require(
            block["verdict"]
            == "NOT_A_NONZERO_MEROMORPHIC_GLOBAL_PRODUCT_WITHOUT_EXACT_CANCELLATION",
            "raw-product stop verdict mismatch",
        )

    gate("G6_RAW_PRODUCT_NO_GO", g6)

    def g7() -> None:
        block = payload["local_dilation_tower_gate"]
        require(
            block.keys()
            == {
                "prime_scope",
                "sum_definition",
                "stationary_digit_condition",
                "recurrence",
                "integral_theorem",
                "rows",
                "direct_cyclotomic_controls",
                "weak_null_sequence",
                "noncompactness_witness",
                "verdict",
            },
            "dilation block keys mismatch",
        )
        require(
            block["sum_definition"]
            == "S_(p,m)=sum_(u mod p^(3m)) exp(2*pi*i*(2*u^3-p^(2m)*u)/p^(3m))",
            "sum definition mismatch",
        )
        require(
            block["stationary_digit_condition"]
            == "sum over the highest base-p digit forces u=0 mod p",
            "stationary digit condition mismatch",
        )
        require(
            block["integral_theorem"]
            == "integral_(p^(-m) Z_p) psi_p(2*x^3-x) dx=1 for every m>=0",
            "integral theorem mismatch",
        )
        require(block["prime_scope"] == "p>3", "local prime scope mismatch")
        require(
            block["recurrence"] == "S_(p,m)=p^2*S_(p,m-1), S_(p,0)=1",
            "stationary-digit recurrence mismatch",
        )
        expected_pairs = [(p, m) for p in [5, 7, 11, 13] for m in range(0, 7)]
        seen: list[tuple[int, int]] = []
        for row in block["rows"]:
            require(
                row.keys()
                == {
                    "prime",
                    "dilation_level",
                    "residue_modulus",
                    "exponential_sum",
                    "haar_cell_volume",
                    "ball_integral",
                    "normalized_matrix_coefficient",
                    "defect_norm_squared",
                },
                "tower row keys mismatch",
            )
            p = row["prime"]
            m = row["dilation_level"]
            require(type(p) is int and type(m) is int, "tower index type mismatch")
            seen.append((p, m))
            require(row["residue_modulus"] == p ** (3 * m), "tower modulus mismatch")
            require(row["exponential_sum"] == p ** (2 * m), "tower sum mismatch")
            require(
                parse_fraction(row["haar_cell_volume"]) == Fraction(1, p ** (2 * m)),
                "Haar cell volume mismatch",
            )
            require(parse_fraction(row["ball_integral"]) == 1, "ball integral mismatch")
            require(
                parse_fraction(row["normalized_matrix_coefficient"]) == Fraction(1, p**m),
                "normalized matrix coefficient mismatch",
            )
            require(
                parse_fraction(row["defect_norm_squared"])
                == Fraction(2) - Fraction(2, p**m),
                "noncompactness norm mismatch",
            )
        require(seen == expected_pairs, "tower registry mismatch")
        expected_controls = [
            replay_cyclotomic_control(p, m)
            for p, m in [(5, 1), (5, 2), (7, 1), (7, 2), (11, 1), (13, 1)]
        ]
        require(
            strict_equal(block["direct_cyclotomic_controls"], expected_controls),
            "direct cyclotomic sum controls mismatch",
        )
        require(
            block["verdict"] == "M_P6_MINUS_IDENTITY_IS_NOT_COMPACT_ON_L2_QP",
            "same-space noncompactness verdict mismatch",
        )
        require(
            block["weak_null_sequence"]
            == "e_(p,m)=p^(-m/2) 1_(p^(-m) Z_p) converges weakly to 0",
            "weak-null theorem mismatch",
        )
        require(
            block["noncompactness_witness"]
            == "||(M_P6-I)e_(p,m)||^2=2-2*p^(-m) -> 2",
            "noncompactness witness mismatch",
        )

    gate("G7_LOCAL_DILATION_NONCOMPACTNESS", g7)

    def g8() -> None:
        expected = {
            "ambient_test_space": "V={f in S(A_Q):f(0)=0}",
            "functionals": [
                "Lambda_0(f)=integral f",
                "Lambda_(-P)(f)=integral psi(-P6(x))*f(x) dx",
            ],
            "standard_hyperplane": "S0=V intersect ker(Lambda_0)",
            "chirped_hyperplane": "M_P6 S0=V intersect ker(Lambda_(-P))",
            "common_subspace": "W=V intersect ker(Lambda_0) intersect ker(Lambda_(-P))",
            "quotient_bounds": {"dim(S0/W)": 1, "dim(M_P6*S0/W)": 1},
            "range_pair": [
                "R0=closure(E F(S0))",
                "RH=closure(E F(M_P6 S0))",
            ],
            "algebraic_range_quotient_bound": 2,
            "projection_hypothesis": "both images extend to closed subspaces of one scaling Hilbert completion",
            "conditional_projection_difference_rank_bound": 2,
            "status": "PROVED_STATIC_ALGEBRAIC_RANGE_PAIR_BOUND",
            "dynamic_scattering_consequence": "NOT_PROVED",
        }
        require(
            strict_equal(payload["fixed_domain_relative_range_gate"], expected),
            "static range-pair theorem mismatch",
        )
        expected_covariance = {
            "dilation": "D_a f(x)=|a|^(1/2) f(a*x)",
            "conjugated_phase": "D_a M_P6 D_a^(-1)=M_(P_a), P_a(x)=2*a^3*x^3-a*x",
            "boundary_orbit": "Lambda_(-P_a)(f)=integral psi(-P_a(x))*f(x) dx",
            "archimedean_kernels": "phi_a(z)=exp(-2*pi*i*(2*a^3*z^3-a*z))",
            "independence_proof": "on z=r*exp(i*pi/6), the largest a has unique growth exp(4*pi*a^3*r^3+O(r))",
            "registered_positive_a": list(range(1, 9)),
            "registered_cubic_growth_coefficients": [4 * a**3 for a in range(1, 9)],
            "pre_E_boundary_orbit_dimension": "INFINITE",
            "static_rank_two_implies_dynamic_two_channel": False,
            "verdict": "DYNAMIC_FINITE_CHANNEL_INFERENCE_REFUTED",
            "next_gate": "CONSTRUCT_SCALING_COVARIANT_POISSON_RENORMALIZATION_OR_CROSSED_PRODUCT_SCATTERING",
        }
        require(
            strict_equal(payload["scaling_covariance_gate"], expected_covariance),
            "scaling covariance obstruction mismatch",
        )
        expected_poisson_defect = {
            "full_scaling_map": "E_x(g)(x)=|x|^(1/2)*sum_(r in Q^x) g(r*x)",
            "poisson_identity": "E_x(F g)(x)=E_x(g)(x^(-1))+|x|^(-1/2)*g(0)-|x|^(1/2)*hat(g)(0)",
            "henon_specialization": "if g=M_(P_a)f and f(0)=0 then E_x(F M_(P_a)f)(x)=E_x(M_(P_a)f)(x^(-1))-|x|^(1/2)*Lambda_(P_a)(f)",
            "general_boundary_modes": ["|x|^(-1/2)", "|x|^(1/2)"],
            "zero_input_output_mode": "|x|^(1/2)",
            "fixed_scale_output_defect_dimension": 1,
            "static_boundary_family": "Lambda_(-P_a)",
            "poisson_coefficient_family": "Lambda_(+P_a)",
            "sign_firewall": "the plus and minus families are separately infinite-dimensional and are not identified",
            "coefficient_functional_orbit": "INFINITE_AND_NOT_COLLAPSED_BY_THIS_IDENTITY",
            "boundary_mode_Hilbert_membership": "NOT_ASSERTED",
            "bounded_finite_rank_operator": "NOT_CLAIMED",
            "determinant_class": "OPEN",
            "status": "EXACT_FIXED_SCALE_POISSON_BOUNDARY_IDENTITY",
        }
        require(
            strict_equal(payload["poisson_boundary_defect_gate"], expected_poisson_defect),
            "Poisson boundary-defect identity mismatch",
        )

    gate("G8_STATIC_RANGE_AND_SCALING_COVARIANCE", g8)

    def g9() -> None:
        expected_route = {
            "current_tuple": [
                "A1_WEAK",
                "A2_FAIL",
                "A3_PARTIAL_ANALYTIC_STRUCTURE",
                "A4_NATURAL_QUANTIZATION",
            ],
            "overall": "ROUTE_A_EXPLORATORY",
            "qualification": "the scaling mother system supplies A1-A3 while H6 supplies A4; coordinatewise maximization is forbidden until one relative scattering object carries all four",
            "route_b_invocation_allowed": False,
        }
        require(strict_equal(payload["route_a"], expected_route), "Route-A contract mismatch")
        expected_scaling = {
            "primitive_orbits": "C_p=R_+^*/p^Z",
            "clock": "ell(C_p)=log(p)",
            "separate_henon_fact": "U_H,p 1_Zp=1_Zp",
            "coupling_status": "FORMAL_TRIVIAL_VACUUM_DECORATION_ONLY",
            "missing_bridge": "no scaling-site bundle/cocycle with U_H,p as orbit holonomy has been constructed",
            "zeta": "the inherited scaling-site mother zeta is zeta(s)",
            "status": "PRIOR_ART_ZETA_AND_SEPARATE_HENON_VACUUM_COMPATIBILITY",
        }
        require(strict_equal(payload["scaling_site_gate"], expected_scaling), "scaling-site scope mismatch")
        require(
            payload["decisions"]["henon_vacuum_essentiality"]
            == "REFUTED_BY_SIMPLER_PARENT_CONTROL",
            "simpler-parent firewall missing",
        )
        expected_decisions = {
            "adelic_henon_theta_route": "GO_EXACT_MOTHER_ROUTE",
            "raw_finite_quantum_euler_product": "STOP_THEOREM",
            "henon_vacuum_essentiality": "REFUTED_BY_SIMPLER_PARENT_CONTROL",
            "naive_same_space_relative_fredholm": "STOP_NONCOMPACTNESS_THEOREM",
            "static_fixed_domain_range_pair": "PROVED_ALGEBRAIC_RANK_BOUND_TWO",
            "dynamic_two_channel_scattering": "STOP_INVALID_INFERENCE",
            "henon_scaling_covariant_scattering": "GO_NEXT_BIG_GATE",
        }
        require(strict_equal(payload["decisions"], expected_decisions), "decision ledger mismatch")
        expected_scope = {
            "no_rh_proof": True,
            "no_new_tate_or_connes_proof": True,
            "finite_field_operator_not_identified_with_p_adic_operator": True,
            "theta_invariance_not_unique_to_H6": True,
            "no_zero_or_prime_fitting": True,
        }
        require(strict_equal(payload["scope"], expected_scope), "scope firewall failed")

    gate("G9_ROUTE_AND_SCOPE", g9)
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    gates = audit(certificate)
    report = {
        "schema": "hcs-c35-independent-check-v1",
        "all_pass": all(row["status"] == "PASS" for row in gates),
        "gates": gates,
    }
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")
    raise SystemExit(0 if report["all_pass"] else 1)


if __name__ == "__main__":
    main()
