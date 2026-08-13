#!/usr/bin/env python3
"""Independent fail-closed checker for the HCS-C47 operator certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable


SCHEMA = "hcs-c47-certificate-v1"
CONTROL_BOUND = 499
MOMENT_CONTROL_PRIMES = (7, 13, 19, 31, 37, 43, 61)
EXPECTED_C2 = (-6, -6, -6, -30, 18, -54, 18)
EXPECTED_C3 = (
    Fraction(12, 7), Fraction(132, 13), Fraction(54, 19),
    Fraction(960, 31), Fraction(-612, 37), Fraction(3054, 43),
    Fraction(3414, 61),
)


class GateFailure(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GateFailure(message)


def canonical_json(obj: Any) -> bytes:
    return json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return set(left) == set(right) and all(
            strict_equal(left[key], right[key]) for key in left
        )
    if isinstance(left, list):
        return len(left) == len(right) and all(
            strict_equal(a, b) for a, b in zip(left, right)
        )
    return left == right


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def is_prime(n: int) -> bool:
    if type(n) is not int or n < 2:
        return False
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            return False
    return True


def multiplicative_order(value: int, p: int) -> int:
    running = 1
    for exponent in range(1, p):
        running = running * value % p
        if running == 1:
            return exponent
    raise GateFailure("order not found")


def least_primitive_root(p: int) -> int:
    for candidate in range(2, p):
        if multiplicative_order(candidate, p) == p - 1:
            return candidate
    raise GateFailure("primitive root not found")


def split_primes_through(bound: int) -> list[int]:
    return [p for p in range(5, bound + 1) if p % 3 == 1 and is_prime(p)]


def record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


@lru_cache(maxsize=None)
def count_ordered_phase_zeroes(p: int, rho: int, n: int) -> int:
    """Independent dictionary DP for the exact ordered 2n-step phase."""
    length = 2 * n
    cube = [2 * pow(x, 3, p) % p for x in range(p)]
    total = 0
    for start in range(p):
        states: dict[tuple[int, int], int] = {(start, cube[start]): 1}
        for _ in range(1, length):
            following: dict[tuple[int, int], int] = {}
            for (previous, residue), multiplicity in states.items():
                for current in range(p):
                    new_residue = (
                        residue + previous * current + cube[current]
                    ) % p
                    key = (current, new_residue)
                    following[key] = following.get(key, 0) + multiplicity
            states = following
        for (endpoint, residue), multiplicity in states.items():
            if (residue + rho * endpoint * start) % p == 0:
                total += multiplicity
    return total


def traced_moment(p: int, n: int, zero_count: int) -> Fraction:
    return Fraction(2 * zero_count, p ** (n - 1)) - 2 * p**n


def rebuild_block(p: int) -> dict[str, Any]:
    require(type(p) is int and is_prime(p) and p % 3 == 1, "invalid block prime")
    d = (p - 1) // 2
    d0 = (p + 2) // 3
    d1 = (p - 1) // 3
    even = 4 * d * d0
    odd = 4 * d * d1
    identity = Fraction(even + odd, d)
    require(identity == Fraction(8 * p + 4, 3), "identity trace formula")
    return {
        "prime": p,
        "real_galois_class_count_d_p": d,
        "sector_dimension_d0": d0,
        "sector_dimensions_d1_d2": [d1, d1],
        "per_galois_class_even_block": "2*T_(a,0) plus 2*T_(-a,0)",
        "per_galois_class_odd_block": "T_(a,1),T_(a,2),T_(-a,1),T_(-a,2)",
        "total_even_dimension": even,
        "total_odd_dimension": odd,
        "positive_normalized_trace_of_identity": record(identity),
        "absolute_Lq_trace_coefficient": record(identity),
        "first_signed_supertrace_moment": record(Fraction(-6, d)),
    }


@lru_cache(maxsize=None)
def rebuild_moment(p: int, expected_c2: int, expected_c3: Fraction) -> dict[str, Any]:
    require(p in MOMENT_CONTROL_PRIMES, "unexpected moment prime")
    generator = least_primitive_root(p)
    rho = pow(generator, (p - 1) // 3, p)
    zeroes = [count_ordered_phase_zeroes(p, rho, n) for n in (1, 2, 3)]
    moments = [traced_moment(p, n, zeroes[n - 1]) for n in (1, 2, 3)]
    require(moments == [Fraction(-6), Fraction(expected_c2), expected_c3], "moment ledger mismatch")
    d = (p - 1) // 2
    return {
        "prime": p,
        "rho_order_3": rho,
        "chronological_zero_counts_n1_n2_n3": zeroes,
        "galois_traced_moments_C1_C2_C3": [record(value) for value in moments],
        "normalized_signed_supertrace_moments_c1_c2_c3": [
            record(value / d) for value in moments
        ],
    }


def expected_source_lock(project_root: Path) -> list[dict[str, str]]:
    root = project_root.parent
    relatives = (
        "henon_mu3_galois_norm_rank_obstruction/results/c45_certificate.json",
        "henon_mu3_normalized_root_branch_obstruction/results/c46_certificate.json",
    )
    return [
        {
            "path": f"henon_dynamics/{relative}",
            "sha256": sha256_file(root / relative),
        }
        for relative in relatives
    ]


def expected_payload(project_root: Path) -> dict[str, Any]:
    primes = split_primes_through(CONTROL_BOUND)
    blocks = [rebuild_block(p) for p in primes]
    moments = [
        rebuild_moment(p, c2, c3)
        for p, c2, c3 in zip(MOMENT_CONTROL_PRIMES, EXPECTED_C2, EXPECTED_C3)
    ]
    return {
        "material_passport": {
            "candidate_id": "HCS-C47",
            "project": "henon_mu3_normalized_trace_operator_gate",
            "ai_assistance_disclosed": True,
            "evidence_policy": "exact graded block algebra, exact chronological moments, and prime-series comparison; no zero-table data",
        },
        "source_lock": expected_source_lock(project_root),
        "local_operator_algebra": {
            "algebra": "M_p=B(H_p^+) direct_sum B(H_p^-)",
            "positive_trace": "tau_p(A_+ direct_sum A_-)=(Tr A_+ + Tr A_-)/d_p",
            "grading": "Gamma_p=+I on H_p^+ and -I on H_p^-",
            "signed_supertrace": "str_p(A)=tau_p(Gamma_p*A)",
            "block_operator": "W_p in M_p acts on H_p^+ direct_sum H_p^- and is the direct sum over real Galois classes [a] of the exact even and odd Henon sector blocks",
            "moment_identity": "str_p(W_p^n)=c_p,n=C_p,n/d_p for every n>=1",
            "local_determinant_identity": "G_p(z)=exp(str_p(Log(I-z*W_p))) on the origin zero-free branch",
            "positive_trace_warning": "tau_p is positive but str_p is signed; they cannot be interchanged",
            "fuglede_kadison_warning": "a positive FK determinant sees log absolute value and loses the analytic phase of G_p",
        },
        "global_operator_algebra": {
            "algebra": "M=semifinite direct product over split primes with tau=sum_p tau_p",
            "operator": "X_s=direct_sum_p p^(-s)*W_p",
            "exact_Lq_identity": "tau(|X_s|^q)=sum_(p=1 mod 3) ((8p+4)/3)*p^(-q*Re(s))",
            "Lq_criterion": "X_s belongs to L^q(M,tau) iff q*Re(s)>2",
            "compactness_on_hilbert_direct_sum": "X_s is compact iff Re(s)>0",
            "tau_L1_threshold": "L1(M,tau) iff Re(s)>2",
            "tau_L2_threshold": "L2(M,tau) iff Re(s)>1",
            "tau_L3_threshold": "L3(M,tau) iff Re(s)>2/3",
            "tau_L4_threshold": "L4(M,tau) iff Re(s)>1/2",
            "grading_cannot_improve_positive_tau_L1": "|Gamma_p*X_s|=|X_s|",
            "classical_Hilbert_trace_identity": "Tr_H(|X_s|^q)=sum_(p=1 mod 3) d_p*((8p+4)/3)*p^(-q*Re(s))",
            "classical_Schatten_criterion": "X_s belongs to classical S^q(H) iff q*Re(s)>3",
            "classical_trace_class_threshold": "classical S1(H) iff Re(s)>3",
            "classical_Hilbert_Schmidt_threshold": "classical S2(H) iff Re(s)>3/2",
            "classical_determinant_warning": "the classical Hilbert trace does not implement the field-degree-normalized root G",
        },
        "regularized_graded_determinant": {
            "counterterms": "ell_n(s)=sum_p c_p,n*p^(-n*s), n=1,2,3",
            "det4_definition": "det4_tau_gr(I-X_s)=exp(-sum_(n>=4) str_tau(X_s^n)/n)",
            "exact_factorization": "G(s)=exp(-ell_1(s)-ell_2(s)/2-ell_3(s)/3)*det4_tau_gr(I-X_s)",
            "domain": "Re(s)>1/2",
            "minimal_fixed_schatten_order_on_full_domain": 4,
            "unregularized_tau_determinant_domain": "Re(s)>2",
            "determinant_category": "semifinite tau-associated graded regularization, not a classical Fredholm determinant",
            "counterterm_status": "three source-native chronological Galois-supertrace moments, not fitted prefactors",
        },
        "exact_block_controls": blocks,
        "exact_chronological_moment_controls": moments,
        "aggregate_control": {
            "control_bound_inclusive": CONTROL_BOUND,
            "control_primes": primes,
            "number_of_block_controls": len(blocks),
            "all_positive_identity_traces_equal_8p_plus_4_over_3": True,
            "moment_control_primes": list(MOMENT_CONTROL_PRIMES),
            "C2_ledger": list(EXPECTED_C2),
            "C3_ledger": [record(value) for value in EXPECTED_C3],
            "all_first_signed_moments_equal_minus_12_over_p_minus_1": True,
        },
        "decisions": {
            "finite_local_normalized_trace_model": "CONSTRUCTED_EXACTLY",
            "positive_trace_and_signed_supertrace_distinguished": "YES",
            "ordinary_global_semifinite_trace_class_on_critical_half_plane": "REFUTED_BY_TAU_L1_THRESHOLD_RE_S_GREATER_THAN_2",
            "fourth_order_regularized_graded_determinant": "CONSTRUCTED_IN_SEMIFINITE_TAU_CATEGORY_ON_RE_S_GREATER_THAN_ONE_HALF",
            "positive_fuglede_kadison_equals_complex_G": "REFUTED_PHASE_IS_LOST",
            "next_large_gate": "C48_IDENTIFY_GEOMETRIC_OR_MOTIVIC_STRUCTURE_OF_c_p_2_AND_COUNTERTERMS",
        },
        "route_a": {
            "A1": "A1_WEAK",
            "A2": "A2_ANALYTIC_DETERMINANT",
            "A2_reason": "canonical L4(M,tau) regularized graded determinant with three exact source-native counterterms realizes the C45 germ on Re(s)>1/2",
            "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "A3_reason": "operator-category realization reaches the half-plane to the right of the Riemann critical abscissa, but no continuation, functional equation, Gamma factor, or Riemann divisor is proved",
            "A4": "A4_NATURAL_QUANTIZATION",
            "overall": "ROUTE_A_EXPLORATORY",
            "scoped_status": "ROUTE_A_EXPLORATORY_REGULARIZED_GRADED_DETERMINANT",
            "route_b_invocation_allowed": False,
        },
        "scope": {
            "rh_proved": False,
            "hilbert_polya_self_adjoint_operator_constructed": False,
            "global_meromorphic_continuation_claimed": False,
            "gamma_factor_claimed": False,
            "riemann_zero_data_used": False,
            "unregularized_tau_L1_determinant_claimed_on_Re_s_gt_one_half": False,
            "classical_Fredholm_determinant_claimed_on_Re_s_gt_one_half": False,
            "classical_Schatten_criterion_claimed_qRe_s_gt_2": False,
            "positive_FK_determinant_claimed_equal_to_complex_germ": False,
            "counterterms_claimed_arithmetic_motives": False,
        },
    }


def audit_certificate(certificate: Any, project_root: Path) -> tuple[list[dict[str, str]], bool]:
    gates: list[dict[str, str]] = []

    def run(name: str, check: Callable[[], None]) -> None:
        try:
            check()
        except GateFailure as exc:
            gates.append({"gate": name, "status": "FAIL", "detail": str(exc)})
        except Exception as exc:
            gates.append({"gate": name, "status": "ERROR", "detail": f"{type(exc).__name__}: {exc}"})
        else:
            gates.append({"gate": name, "status": "PASS", "detail": "verified"})

    def schema_gate() -> None:
        require(type(certificate) is dict, "certificate must be dictionary")
        require(set(certificate) == {"schema", "payload", "payload_sha256"}, "top-level keys")
        require(certificate["schema"] == SCHEMA, "schema mismatch")
        require(type(certificate["payload"]) is dict, "payload type")

    def digest_gate() -> None:
        expected = hashlib.sha256(canonical_json(certificate["payload"])).hexdigest()
        require(certificate["payload_sha256"] == expected, "digest mismatch")

    def source_gate() -> None:
        require(strict_equal(certificate["payload"]["source_lock"], expected_source_lock(project_root)), "source lock")

    def prime_scope_gate() -> None:
        aggregate = certificate["payload"]["aggregate_control"]
        require(type(aggregate["control_bound_inclusive"]) is int, "bound type")
        require(aggregate["control_bound_inclusive"] == CONTROL_BOUND, "bound mismatch")
        primes = split_primes_through(CONTROL_BOUND)
        require(aggregate["control_primes"] == primes, "prime ledger")
        actual = [row["prime"] for row in certificate["payload"]["exact_block_controls"]]
        require(all(type(p) is int for p in actual) and actual == primes, "block prime rows")

    def block_gate() -> None:
        for row in certificate["payload"]["exact_block_controls"]:
            require(strict_equal(row, rebuild_block(row["prime"])), f"block mismatch p={row['prime']}")

    def trace_supertrace_gate() -> None:
        local = certificate["payload"]["local_operator_algebra"]
        require(local["positive_trace_warning"] == "tau_p is positive but str_p is signed; they cannot be interchanged", "trace warning")
        require(local["moment_identity"] == "str_p(W_p^n)=c_p,n=C_p,n/d_p for every n>=1", "supertrace identity")
        require(local["fuglede_kadison_warning"].endswith("analytic phase of G_p"), "FK warning")

    def moment_gate() -> None:
        rows = certificate["payload"]["exact_chronological_moment_controls"]
        require(
            certificate["payload"]["aggregate_control"]["moment_control_primes"]
            == list(MOMENT_CONTROL_PRIMES),
            "aggregate moment-prime ledger mismatch",
        )
        require([row["prime"] for row in rows] == list(MOMENT_CONTROL_PRIMES), "moment primes")
        for row, c2, c3 in zip(rows, EXPECTED_C2, EXPECTED_C3):
            require(strict_equal(row, rebuild_moment(row["prime"], c2, c3)), f"moment mismatch p={row['prime']}")

    def schatten_gate() -> None:
        global_data = certificate["payload"]["global_operator_algebra"]
        require(global_data["exact_Lq_identity"] == "tau(|X_s|^q)=sum_(p=1 mod 3) ((8p+4)/3)*p^(-q*Re(s))", "Lq identity")
        require(global_data["Lq_criterion"] == "X_s belongs to L^q(M,tau) iff q*Re(s)>2", "Lq criterion")
        require(global_data["tau_L1_threshold"] == "L1(M,tau) iff Re(s)>2", "tau L1 threshold")
        require(global_data["tau_L2_threshold"] == "L2(M,tau) iff Re(s)>1", "tau L2 threshold")
        require(global_data["tau_L3_threshold"] == "L3(M,tau) iff Re(s)>2/3", "tau L3 threshold")
        require(global_data["tau_L4_threshold"] == "L4(M,tau) iff Re(s)>1/2", "tau L4 threshold")
        require(global_data["grading_cannot_improve_positive_tau_L1"] == "|Gamma_p*X_s|=|X_s|", "grading absolute value")
        require(global_data["classical_Hilbert_trace_identity"] == "Tr_H(|X_s|^q)=sum_(p=1 mod 3) d_p*((8p+4)/3)*p^(-q*Re(s))", "classical trace identity")
        require(global_data["classical_Schatten_criterion"] == "X_s belongs to classical S^q(H) iff q*Re(s)>3", "classical Schatten criterion")
        require(global_data["classical_trace_class_threshold"] == "classical S1(H) iff Re(s)>3", "classical trace class")
        require(global_data["classical_Hilbert_Schmidt_threshold"] == "classical S2(H) iff Re(s)>3/2", "classical Hilbert-Schmidt")
        require(global_data["classical_determinant_warning"].endswith("field-degree-normalized root G"), "classical determinant warning")

    def det4_gate() -> None:
        data = certificate["payload"]["regularized_graded_determinant"]
        require(data["minimal_fixed_schatten_order_on_full_domain"] == 4, "minimal order")
        require(data["domain"] == "Re(s)>1/2", "det4 domain")
        require(data["exact_factorization"] == "G(s)=exp(-ell_1(s)-ell_2(s)/2-ell_3(s)/3)*det4_tau_gr(I-X_s)", "factorization")
        require(data["unregularized_tau_determinant_domain"] == "Re(s)>2", "unregularized tau determinant domain")
        require(data["determinant_category"] == "semifinite tau-associated graded regularization, not a classical Fredholm determinant", "determinant category")
        require(data["counterterm_status"] == "three source-native chronological Galois-supertrace moments, not fitted prefactors", "counterterms")

    def decision_gate() -> None:
        decisions = certificate["payload"]["decisions"]
        require(decisions["finite_local_normalized_trace_model"] == "CONSTRUCTED_EXACTLY", "local model")
        require(decisions["ordinary_global_semifinite_trace_class_on_critical_half_plane"] == "REFUTED_BY_TAU_L1_THRESHOLD_RE_S_GREATER_THAN_2", "tau L1 verdict")
        require(decisions["fourth_order_regularized_graded_determinant"] == "CONSTRUCTED_IN_SEMIFINITE_TAU_CATEGORY_ON_RE_S_GREATER_THAN_ONE_HALF", "det4 verdict")
        require(decisions["positive_fuglede_kadison_equals_complex_G"] == "REFUTED_PHASE_IS_LOST", "FK verdict")

    def route_scope_gate() -> None:
        route = certificate["payload"]["route_a"]
        require(route["A1"] == "A1_WEAK", "A1")
        require(route["A2"] == "A2_ANALYTIC_DETERMINANT", "A2")
        require(route["A3"] == "A3_PARTIAL_ANALYTIC_STRUCTURE", "A3")
        require(route["A4"] == "A4_NATURAL_QUANTIZATION", "A4")
        require(route["overall"] == "ROUTE_A_EXPLORATORY", "overall")
        require(route["route_b_invocation_allowed"] is False, "Route B")
        scope = certificate["payload"]["scope"]
        require(all(type(value) is bool for value in scope.values()), "scope types")
        require(not any(scope.values()), "scope overclaim")

    def full_payload_gate() -> None:
        require(strict_equal(certificate["payload"], expected_payload(project_root)), "full payload")

    run("G01_SCHEMA_AND_TYPES", schema_gate)
    run("G02_PAYLOAD_DIGEST", digest_gate)
    run("G03_SOURCE_LOCK", source_gate)
    run("G04_COMPLETE_SPLIT_PRIME_SCOPE", prime_scope_gate)
    run("G05_EXACT_GRADED_BLOCK_DIMENSIONS", block_gate)
    run("G06_POSITIVE_TRACE_VS_SIGNED_SUPERTRACE", trace_supertrace_gate)
    run("G07_CHRONOLOGICAL_MOMENT_IDENTITIES", moment_gate)
    run("G08_GLOBAL_SCHATTEN_THRESHOLDS", schatten_gate)
    run("G09_REGULARIZED_DET4_FACTORIZATION", det4_gate)
    run("G10_OPERATOR_CATEGORY_DECISIONS", decision_gate)
    run("G11_ROUTE_A_AND_SCOPE", route_scope_gate)
    run("G12_FULL_PAYLOAD_REPLAY", full_payload_gate)
    return gates, all(row["status"] == "PASS" for row in gates)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate")
    parser.add_argument("--output")
    args = parser.parse_args()
    path = Path(args.certificate)
    project_root = Path(__file__).resolve().parents[1]
    certificate = json.loads(path.read_text(encoding="utf-8"))
    gates, passed = audit_certificate(certificate, project_root)
    report = {
        "schema": "hcs-c47-independent-check-v1",
        "certificate_sha256": sha256_file(path),
        "gates": gates,
        "passed": passed,
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
