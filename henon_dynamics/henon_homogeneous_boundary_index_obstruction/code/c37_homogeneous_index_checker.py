#!/usr/bin/env python3
"""Independent, fail-closed checker for HCS-C37."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


SCHEMA = "hcs-c37-certificate-v1"


class GateFailure(Exception):
    pass


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


def reject_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise GateFailure(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GateFailure(message)


def fraction_from_record(record: Any) -> Fraction:
    require(type(record) is dict, "fraction record must be dict")
    require(
        list(record.keys()) == ["denominator", "numerator"]
        or list(record.keys()) == ["numerator", "denominator"],
        "fraction keys changed",
    )
    require(type(record.get("numerator")) is int, "numerator type")
    require(type(record.get("denominator")) is int, "denominator type")
    require(record["denominator"] > 0, "denominator sign")
    return Fraction(record["numerator"], record["denominator"])


def audit(path: Path) -> dict[str, Any]:
    root = Path(__file__).resolve().parents[3]
    certificate = json.loads(
        path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_pairs
    )
    require(type(certificate) is dict, "certificate type")
    require(
        list(certificate.keys()) == ["payload", "payload_sha256"]
        or list(certificate.keys()) == ["payload_sha256", "payload"],
        "certificate keys",
    )
    payload = certificate["payload"]
    require(type(payload) is dict, "payload type")
    expected_digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
    require(
        type(certificate["payload_sha256"]) is str
        and certificate["payload_sha256"] == expected_digest,
        "payload hash mismatch",
    )

    gates: list[dict[str, str]] = []

    def gate(name: str, fn: Any) -> None:
        try:
            fn()
        except GateFailure as exc:
            gates.append({"gate": name, "status": "FAIL", "detail": str(exc)})
            raise
        except Exception as exc:  # unexpected checker errors are not semantic FAILs
            gates.append(
                {
                    "gate": name,
                    "status": "ERROR",
                    "detail": f"{type(exc).__name__}: {exc}",
                }
            )
            raise
        else:
            gates.append({"gate": name, "status": "PASS", "detail": "ok"})

    def g0() -> None:
        require(payload.get("schema") == SCHEMA, "schema")
        require(payload.get("candidate_id") == "HCS-C37", "candidate")
        require(
            set(payload.keys())
            == {
                "schema",
                "candidate_id",
                "material_passport",
                "source_lock",
                "conventions",
                "classical_gate",
                "equivariant_coboundary",
                "prime_loop_gate",
                "poisson_boundary_pair",
                "hardy_restricted_gate",
                "homogeneous_mellin_shadow",
                "route_a",
                "scope",
            },
            "payload key set",
        )
        require(
            strict_equal(
                payload["material_passport"],
                {
                    "ai_assistance_disclosed": True,
                    "artifact_kind": "theorem_and_exact_certificate",
                    "evidence_policy": "exact algebra plus an analytic VMO witness; no Riemann zero or prime table",
                },
            ),
            "passport",
        )

    def g1() -> None:
        expected_paths = {
            "source_henon_pdf": "henon_dynamics/docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf",
            "c35_theorem_package": "henon_dynamics/adelic_henon_theta_route/THEOREM_PACKAGE.md",
            "c36_theorem_package": "henon_dynamics/henon_mellin_parity_obstruction/THEOREM_PACKAGE.md",
            "route_a_evaluator": "henon_dynamics/skills/route-a-evaluator.md",
            "candidate_registry": "henon_dynamics/docs/candidate_registry.md",
            "obstruction_registry": "henon_dynamics/docs/obstruction_registry.md",
        }
        lock = payload["source_lock"]
        require(type(lock) is dict and set(lock) == set(expected_paths), "source keys")
        for key, relative in expected_paths.items():
            row = lock[key]
            require(
                strict_equal(set(row.keys()), {"path", "sha256"}),
                f"source row keys {key}",
            )
            require(type(row["path"]) is str and row["path"] == relative, key)
            require(
                type(row["sha256"]) is str
                and row["sha256"] == sha256_file(root / relative),
                f"source digest {key}",
            )

    def g2() -> None:
        classical = payload["classical_gate"]
        require(type(classical["determinant"]) is int, "det type")
        require(classical["determinant"] == 1, "area determinant")
        require(classical["area_preserving"] is True, "area bool")
        require(classical["generating_phase_homogeneous_degree"] == 3, "degree")
        require(
            strict_equal(classical["jacobian"], [[-12, -1], [1, 0]]),
            "Jacobian coefficient ledger",
        )
        require(
            payload["conventions"]["phase"] == "P0(x)=2*x^3",
            "phase convention",
        )

    def g3() -> None:
        record = payload["equivariant_coboundary"]
        # Coefficientwise replay with formal integer samples is sufficient here
        # because both sides are polynomials in a,b,q of degree at most three
        # in each variable and their expansions are also checked algebraically.
        for a in (-3, -1, 2, 5):
            for b in (-2, 1, 4):
                lhs = 2 * ((a * b) ** 3 - 1)
                rhs = 2 * (a**3 - 1) * b**3 + 2 * (b**3 - 1)
                require(lhs == rhs, "cocycle replay")
            for q in (-2, -1, 3):
                lhs = 2 * (a**3 - 1) * q**3 + 2 * (q**3 - 1)
                rhs = 2 * (q**3 - 1) * a**3 + 2 * (a**3 - 1)
                require(lhs == rhs, "descent replay")
        require(record["cocycle_identity"]["expanded_difference"] == "0", "cocycle field")
        require(record["q_star_descent_compatibility"]["expanded_difference"] == "0", "descent field")
        require(record["groupoid_H1_class"] == "ZERO", "H1")
        require(record["equivariant_line_bundle_class"] == "TRIVIAL", "bundle")
        require(record["simultaneous_gauge"] == "T(x,v)=(x,phi(x)^(-1)*v)", "gauge")

    def g4() -> None:
        prime = payload["prime_loop_gate"]
        for p in (2, 3, 5, 11):
            for r in (1, 2, 4, 7):
                telescoped = sum(
                    2 * (p**3 - 1) * p ** (3 * j) for j in range(r)
                )
                require(telescoped == 2 * (p ** (3 * r) - 1), "prime telescope")
        require(type(prime["closed_gauge_holonomy"]) is int, "holonomy type")
        require(prime["closed_gauge_holonomy"] == 1, "holonomy")
        require(prime["all_prime_repetitions"] == "TRIVIAL_HENON_HOLONOMY", "prime status")

    def g5() -> None:
        pair = payload["poisson_boundary_pair"]
        require(pair["functional_independence_germ"]["constant_row"] == [1, 1], "germ constant")
        require(pair["functional_independence_germ"]["x3_row"] == [0, "-i*tau*a^3"], "germ x3")
        require(type(pair["dim_K0_mod_W"]) is int and pair["dim_K0_mod_W"] == 1, "dim K0")
        require(type(pair["dim_Ka_mod_W"]) is int and pair["dim_Ka_mod_W"] == 1, "dim Ka")
        require(type(pair["essential_codimension"]) is int and pair["essential_codimension"] == 0, "index")
        require(pair["compression_index"] == "ind(P_Ka|K0)=0", "compression index")
        require("trace class" in pair["projection_difference"], "projection difference")
        require(pair["M_phi_preserves_K0"] is False, "preservation")
        require(pair["intrinsic_quotient_automorphism"] == "ABSENT", "quotient")
        require(pair["functorial_descended_anomaly"] == "ZERO_IF_DEFINED", "anomaly")

    def g6() -> None:
        hardy = payload["hardy_restricted_gate"]
        error_coeff = fraction_from_record(hardy["error_pi_coefficient_at_n2"])
        error_upper = fraction_from_record(hardy["error_upper"])
        threshold = fraction_from_record(hardy["error_upper_less_than"])
        mean_upper = fraction_from_record(hardy["mean_modulus_upper"])
        variance = fraction_from_record(hardy["l2_mean_oscillation_lower"])
        require(error_coeff == Fraction(289, 27648), "error coefficient")
        require(error_upper == Fraction(22, 7) * error_coeff, "pi upper")
        require(error_upper < threshold == Fraction(1, 30), "error threshold")
        require(mean_upper == Fraction(7, 10), "mean upper")
        require(variance == 1 - mean_upper**2 == Fraction(51, 100), "variance")
        require(hardy["interval_length_tends_to_zero"] is True, "interval bool")
        require(hardy["vmo_status"] == "NOT_VMO", "VMO")
        require(hardy["restricted_unitary_status"] == "NOT_IN_U_RES", "restricted")
        require(hardy["toeplitz_determinant_line_from_this_polarization"] == "UNAVAILABLE", "det line")
        require(hardy["log_scaling_companion"]["vmo_status"] == "NOT_VMO", "log VMO")

    def g7() -> None:
        shadow = payload["homogeneous_mellin_shadow"]
        require(shadow["open_strip_zero_or_pole"] is False, "strip")
        require(strict_equal(shadow["fully_kinematic_normalized_channels"], [1, 1]), "channels")
        require(type(shadow["normalized_relative_anomaly"]) is int, "relative type")
        require(shadow["normalized_relative_anomaly"] == 1, "relative anomaly")

    def g8() -> None:
        route = payload["route_a"]
        require(
            strict_equal(
                route["tuple"],
                [
                    "A1_WEAK",
                    "A2_FAIL",
                    "A3_PARTIAL_ANALYTIC_STRUCTURE",
                    "A4_NATURAL_QUANTIZATION",
                ],
            ),
            "Route tuple",
        )
        require(route["overall"] == "ROUTE_A_REJECTED_FOR_SCALAR_HOMOGENEOUS_ANOMALY", "overall")
        require(route["route_b_invocation_allowed"] is False, "Route B")
        require(route["decisions"]["next_big_door"] == "NONSCALAR_Z3_GRADED_KUMMER_TATE_EXTENSION", "next door")
        require(
            "RH or a Hilbert-Polya operator" in payload["scope"]["not_claimed"],
            "RH firewall",
        )

    def g9() -> None:
        """Freeze every non-source semantic field, including explanatory gates."""
        expected_conventions = {
            "phase": "P0(x)=2*x^3",
            "henon_map": "H0(q,p)=(-6*q^2-p,q)",
            "chirp": "phi(x)=psi(P0(x)); archimedean phi_R(x)=exp(4*pi*i*x^3)",
            "half_density_dilation": "D_a f(x)=|a|^(1/2) f(a*x)",
            "groupoid_chronology": "later action on the left",
            "poisson_boundary_map": "b0(f)=(f(0), integral(f))",
            "relative_index_convention": "essential codimension Tr(P_K0-P_Ka), equivalently ind(P_Ka restricted to K0)",
        }
        expected_classical = {
            "jacobian": [[-12, -1], [1, 0]],
            "jacobian_entry_scope": "top-left entry is -12*q",
            "determinant": 1,
            "area_preserving": True,
            "generating_phase_homogeneous_degree": 3,
        }
        expected_coboundary = {
            "increment": "d(a;x)=P0(a*x)-P0(x)=2*(a^3-1)*x^3",
            "cocycle_identity": {
                "lhs_x3_coefficient": "2*((a*b)^3-1)",
                "rhs_x3_coefficient": "2*(a^3-1)*b^3+2*(b^3-1)",
                "expanded_difference": "0",
            },
            "q_star_descent_compatibility": {
                "lhs_x3_coefficient": "2*(a^3-1)*q^3+2*(q^3-1)",
                "rhs_x3_coefficient": "2*(q^3-1)*a^3+2*(a^3-1)",
                "expanded_difference": "0",
            },
            "twisted_q_action": "q.(x,v)=(q*x,phi(q*x)*phi(x)^(-1)*v)",
            "scaling_lift": "a.(x,v)=(a*x,phi(a*x)*phi(x)^(-1)*v)",
            "simultaneous_gauge": "T(x,v)=(x,phi(x)^(-1)*v)",
            "gauge_transformed_q_action": "q.(x,w)=(q*x,w)",
            "gauge_transformed_scaling_lift": "a.(x,w)=(a*x,w)",
            "groupoid_H1_class": "ZERO",
            "equivariant_line_bundle_class": "TRIVIAL",
        }
        expected_prime = {
            "r_step_exponent_sum": "sum_(j=0)^(r-1) 2*(p^3-1)*p^(3*j)=2*(p^(3*r)-1)",
            "endpoint_gauge_exponent": "P0(x)-P0(p^r*x)=-2*(p^(3*r)-1)*x^3",
            "closed_gauge_holonomy": 1,
            "all_prime_repetitions": "TRIVIAL_HENON_HOLONOMY",
            "clock_preserved": "ell(C_p)=log(p), inherited from the scaling site",
        }
        expected_pair = {
            "V": "ker(ev_0)",
            "K0": "V intersect ker(Lambda_0)",
            "Ka": "V intersect ker(Lambda_(-P_a))",
            "W": "V intersect ker(Lambda_0) intersect ker(Lambda_(-P_a))",
            "functional_independence_germ": {
                "basis": ["1", "exp(-i*tau*a^3*x^3)"],
                "constant_row": [1, 1],
                "x3_row": [0, "-i*tau*a^3"],
                "determinant": "-i*tau*a^3 != 0 for tau!=0,a>0",
            },
            "dim_K0_mod_W": 1,
            "dim_Ka_mod_W": 1,
            "projection_difference": "P_K0-P_Ka=p_v-p_u is trace class of rank at most 2",
            "essential_codimension": 0,
            "compression_index": "ind(P_Ka|K0)=0",
            "M_phi_preserves_K0": False,
            "intrinsic_quotient_automorphism": "ABSENT",
            "functorial_descended_anomaly": "ZERO_IF_DEFINED",
        }
        expected_hardy = {
            "symbol": "phi_R(x)=exp(4*pi*i*x^3)",
            "interval": "I_n=[n,n+1/(12*n^2)]",
            "interval_length_tends_to_zero": True,
            "rescaled_phase_increment": "pi*y+pi*y^2/(12*n^3)+pi*y^3/(432*n^6)",
            "n_scope": "integer n>=2",
            "pi_bounds": "3<pi<22/7",
            "error_pi_coefficient_at_n2": {"numerator": 289, "denominator": 27648},
            "error_upper": {"numerator": 3179, "denominator": 96768},
            "error_upper_less_than": {"numerator": 1, "denominator": 30},
            "mean_modulus_upper": {"numerator": 7, "denominator": 10},
            "l2_mean_oscillation_lower": {"numerator": 51, "denominator": 100},
            "vmo_status": "NOT_VMO",
            "hardy_commutator_status": "NONCOMPACT_BY_UCHIYAMA_COMPACT_COMMUTATOR_THEOREM",
            "restricted_unitary_status": "NOT_IN_U_RES",
            "toeplitz_determinant_line_from_this_polarization": "UNAVAILABLE",
            "log_scaling_companion": {
                "symbol": "exp(4*pi*i*exp(3*t))",
                "interval": "J_T=[T,T+exp(-3*T)/12]",
                "rescaled_limit": "exp(i*pi*u) uniformly for u in [0,1]",
                "vmo_status": "NOT_VMO",
            },
        }
        expected_shadow = {
            "kappa_plus": "(1/3)*(4*pi)^(-z/3)*Gamma(z/3)*exp(i*pi*z/6)",
            "kappa_minus": "(1/3)*(4*pi)^(-z/3)*Gamma(z/3)*exp(-i*pi*z/6)",
            "even_channel": "(2/3)*(4*pi)^(-z/3)*Gamma(z/3)*cos(pi*z/6)",
            "odd_channel": "(2/3)*(4*pi)^(-z/3)*Gamma(z/3)*sin(pi*z/6)",
            "open_strip_zero_or_pole": False,
            "fully_kinematic_normalized_channels": [1, 1],
            "normalized_relative_anomaly": 1,
            "interpretation": "strip safety is exact but the scalar homogeneous increment is gauge transport, not a new determinant",
        }
        expected_route = {
            "tuple": [
                "A1_WEAK",
                "A2_FAIL",
                "A3_PARTIAL_ANALYTIC_STRUCTURE",
                "A4_NATURAL_QUANTIZATION",
            ],
            "overall": "ROUTE_A_REJECTED_FOR_SCALAR_HOMOGENEOUS_ANOMALY",
            "route_b_invocation_allowed": False,
            "decisions": {
                "functorial_poisson_boundary_anomaly": "REFUTED",
                "static_boundary_pair_nonzero_index": "REFUTED",
                "standard_hardy_restricted_index": "REFUTED_AS_UNAVAILABLE",
                "homogeneous_strip_divisor": "SAFE_BUT_TRIVIALIZED",
                "scalar_polynomial_chirp_route": "STOP_SCOPED",
                "next_big_door": "NONSCALAR_Z3_GRADED_KUMMER_TATE_EXTENSION",
            },
        }
        expected_scope = {
            "proved": [
                "exact equivariant trivialization of the scalar homogeneous chirp lift",
                "trivial holonomy for every scaling-site prime repetition in that lift",
                "zero pre-Poisson relative hyperplane index",
                "failure of the standard Hardy restricted-unitary gate",
            ],
            "not_claimed": [
                "RH or a Hilbert-Polya operator",
                "a no-go for nonscalar graded or projective cocycles",
                "a no-go for every nonfunctorial renormalized quotient",
                "a new proof of the Tate or Connes scaling determinant",
                "a Fredholm theorem for an unspecified polarization",
            ],
            "forbidden_repairs": [
                "declare a coboundary holonomy nontrivial by changing gauge along a closed orbit",
                "call a noncompact Hardy commutator a determinant-class anomaly",
                "import xi and count its divisor as evidence generated by H0",
            ],
        }
        for name, actual, expected in (
            ("conventions", payload["conventions"], expected_conventions),
            ("classical", payload["classical_gate"], expected_classical),
            ("coboundary", payload["equivariant_coboundary"], expected_coboundary),
            ("prime", payload["prime_loop_gate"], expected_prime),
            ("pair", payload["poisson_boundary_pair"], expected_pair),
            ("hardy", payload["hardy_restricted_gate"], expected_hardy),
            ("shadow", payload["homogeneous_mellin_shadow"], expected_shadow),
            ("route", payload["route_a"], expected_route),
            ("scope", payload["scope"], expected_scope),
        ):
            require(strict_equal(actual, expected), f"full semantic contract: {name}")

    for name, fn in (
        ("G0_SCHEMA", g0),
        ("G1_SOURCE_LOCK", g1),
        ("G2_HOMOGENEOUS_HENON", g2),
        ("G3_EQUIVARIANT_COBoundary", g3),
        ("G4_PRIME_HOLONOMY", g4),
        ("G5_BOUNDARY_PAIR_INDEX", g5),
        ("G6_HARDY_RESTRICTED_GATE", g6),
        ("G7_MELLIN_SHADOW", g7),
        ("G8_ROUTE_SCOPE", g8),
        ("G9_FULL_SEMANTIC_CONTRACT", g9),
    ):
        gate(name, fn)

    return {
        "schema": "hcs-c37-independent-check-v1",
        "certificate": str(path.name),
        "payload_sha256": expected_digest,
        "gates": gates,
        "passed": len(gates),
        "total": 10,
        "all_pass": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        report = audit(args.certificate)
    except GateFailure as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
    except Exception as exc:
        print(f"ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(2)
    text = json.dumps(report, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
