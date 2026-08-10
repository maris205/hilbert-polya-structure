#!/usr/bin/env python3
"""Independent exact replay for HCS-C28.

This checker does not import the producer.  It uses list arithmetic, a
Bareiss determinant, explicit minors, trial factorization, and an independent
Jacobi/Kronecker implementation for the decisive source and P073 sentinels.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
HENON_ROOT = PROJECT.parent
PRODUCER_PATH = PROJECT / "code" / "c28_producer.py"
C24_PATH = HENON_ROOT / "rauzy_metaplectic_obstruction" / "results" / "c24_certificate.json"
C25_PATH = HENON_ROOT / "agy_metaplectic_transfer_obstruction" / "results" / "c25_certificate.json"
C26_PATH = HENON_ROOT / "agy_holomorphic_slice_obstruction" / "results" / "c26_certificate.json"
C27_PATH = HENON_ROOT / "agy_finite_weil_determinant" / "results" / "c27_certificate.json"
CERTIFICATE = PROJECT / "results" / "c28_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c28_independent_check.json"

EXPECTED_SOURCE_HASHES = {
    "C24": "4b4fe5943262137eeeb3eda4de887725a0663402a1f39f8cc43e089bcc91e778",
    "C25": "a35cee22714abbb9dc9aadcc165720d1ff77aff3b7f29071f53a1b451760bd12",
    "C26": "1c0289b9b47e65e0603ea001be7cce263aea13d58c66e4609eac88edf8f7ce4a",
    "C27": "8676d17c5a0e4444dded88b5a76f5ea1fa974275528aa0a51400730759d8b029",
}

GAMMA_STAR = "t" * 64 + "tbttbtbb" * 8


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha256(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def eye(n: int) -> list[list[int]]:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def transpose(a: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*a)]


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matsub(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def det_bareiss(matrix: list[list[int]]) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    a = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for k in range(n - 1):
        pivot = next((i for i in range(k, n) if a[i][k] != 0), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * value - a[i][k] * a[k][j]
                if numerator % previous:
                    raise AssertionError("Bareiss exact division failed")
                a[i][j] = numerator // previous
        previous = value
    return sign * a[-1][-1]


def extract(a: list[list[int]], rows: tuple[int, ...], cols: tuple[int, ...]) -> list[list[int]]:
    return [[a[i][j] for j in cols] for i in rows]


def minors(a: list[list[int]], size: int) -> list[int]:
    return [
        det_bareiss(extract(a, rows, cols))
        for rows in itertools.combinations(range(len(a)), size)
        for cols in itertools.combinations(range(len(a[0])), size)
    ]


def rank_q(a: list[list[int]]) -> int:
    for size in range(min(len(a), len(a[0])), 0, -1):
        if any(value != 0 for value in minors(a, size)):
            return size
    return 0


def factor_trial(value: int) -> dict[int, int]:
    n = abs(value)
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            n //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def squarefree_from_factors(value: int, factors: dict[int, int]) -> int:
    result = -1 if value < 0 else 1
    for prime, exponent in factors.items():
        if exponent % 2:
            result *= prime
    return result


def jacobi(a: int, n: int) -> int:
    if n <= 0 or n % 2 == 0:
        raise ValueError("Jacobi denominator must be positive and odd")
    a %= n
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def kronecker_odd_numerator(a: int, n: int) -> int:
    if a <= 0 or a % 2 == 0 or n <= 0:
        raise ValueError("checker only needs positive odd numerator and positive denominator")
    twos = 0
    while n % 2 == 0:
        twos += 1
        n //= 2
    two_symbol = -1 if a % 8 in (3, 5) else 1
    return (two_symbol**twos) * jacobi(a, n)


def graph_replay(c26: dict[str, object]) -> list[list[int]]:
    edges = {
        (int(edge["source"]), str(edge["type"])): (
            int(edge["target"]),
            [[int(v) for v in row] for row in edge["chronological_matrix"]],
        )
        for edge in c26["graph"]["edges"]
    }
    state = 4
    product = eye(4)
    for token in GAMMA_STAR:
        state, edge_matrix = edges[(state, token)]
        product = matmul(edge_matrix, product)
    if state != 4:
        raise AssertionError("gamma_star did not close")
    return product


def p073_replay(c24: dict[str, object]) -> dict[str, object]:
    row = next(item for item in c24["eventually_positive_cycles"] if item["id"] == "C24-P073")
    g = [[int(v) for v in values] for values in row["base_trivialized_symplectic_matrix"]]
    form = [[int(v) for v in values] for values in c24["source_lock"]["J0"]]
    h = matsub(g, eye(4))
    two = minors(h, 2)
    three = minors(h, 3)
    c = [[1, 0], [0, 1], [0, 0], [0, 0]]
    quotient = matmul(matmul(transpose(c), matmul(transpose(h), form)), c)
    checks = {
        "det_g": det_bareiss(g) == 1,
        "symplectic": matmul(matmul(transpose(g), form), g) == form,
        "rank_h": rank_q(h) == 2,
        "gcd_2_minors": math.gcd(*two) == 1,
        "zero_3_minors": all(value == 0 for value in three),
        "quotient": quotient == [[1, 0], [8, -4]],
        "quotient_det": det_bareiss(quotient) == -4,
    }
    if not all(checks.values()):
        raise AssertionError(f"independent P073 replay failed: {checks}")
    return {
        "checks": checks,
        "g_minus_I_rank": rank_q(h),
        "two_minor_gcd": math.gcd(*two),
        "quotient_form": quotient,
        "symbolic_character_check": (
            "Legendre(-4,p)*Legendre(-1,p)*p=Legendre(4,p)*p=p for every odd p"
        ),
    }


def census(c24: dict[str, object]) -> dict[int, int]:
    counts: dict[int, int] = {}
    rank_two_ids = []
    for row in c24["eventually_positive_cycles"]:
        g = [[int(v) for v in values] for values in row["base_trivialized_symplectic_matrix"]]
        k = 4 - rank_q(matsub(g, eye(4)))
        counts[k] = counts.get(k, 0) + 1
        if k == 2:
            rank_two_ids.append(str(row["id"]))
    if counts != {0: 125, 1: 20, 2: 1} or rank_two_ids != ["C24-P073"]:
        raise AssertionError("independent C24 census failed")
    return counts


def phase_diagram_replay() -> list[dict[str, object]]:
    rows = []
    for z, q, expected in [
        (0, 1, False),
        (1, 3, False),
        (1, 4, True),
        (2, 1, False),
        (2, 2, True),
        (3, 1, False),
        (4, 1, True),
    ]:
        observed = q * z > 3
        if observed != expected:
            raise AssertionError("phase diagram control failed")
        rows.append({"Re_z": z, "q": q, "membership": observed})
    return rows


def decisive_certificate_checks(
    certificate: dict[str, object],
    observed_hashes: dict[str, str],
    gamma: list[list[int]],
    d_gamma: int,
    factors: dict[int, int],
    sqf: int,
    p073: dict[str, object],
    count: dict[int, int],
    phase: list[dict[str, object]],
) -> dict[str, bool]:
    """Check every release-level gate independently of the payload digest.

    The payload digest catches accidental byte-level mutations.  These checks
    intentionally remain as well, so changing a claim and recomputing its
    self-digest cannot make the independent replay pass.
    """

    expected_source_lock = {
        "files": {
            name: {
                "path": str(path.relative_to(HENON_ROOT.parent)),
                "sha256": observed_hashes[name],
            }
            for name, path in {
                "C24": C24_PATH,
                "C25": C25_PATH,
                "C26": C26_PATH,
                "C27": C27_PATH,
            }.items()
        },
        "chronology": "later Rauzy edges and later AGY returns multiply on the left",
        "prime_scope": "all odd primes in theorems; no new bounded prime scan",
        "fibre": "the full p^2-dimensional finite Weil representation from C27",
    }
    expected_decisions = {
        "raw_unweighted_prime_direct_sum": "FAIL_NOT_COMPACT",
        "raw_gamma_star_character_product": "FAIL_NONCONVERGENT",
        "normalized_trace_AGY_limit": "EXISTS_BUT_DETERMINANT_GERM_EQUALS_ONE",
        "prime_norm_direct_sum": "PASS_ORDINARY_FREDHOLM_IFF_RE_Z_GT_3",
        "full_Rauzy_dimension_normalized_marked_assembly": "FAIL_P073_HARMONIC_DIVERGENCE",
        "C26_induced_dimension_normalized_marked_assembly": "OPEN_ALL_WORD_FIXED_SPACE_GATE",
        "intrinsic_one_clock_Hilbert_Polya_gate": "FAIL_EXTERNAL_LOG_P_CLOCK",
        "route_B_authorized": False,
        "next_action": (
            "pivot to a two-sided based/path-groupoid trace or a genuine "
            "p-adic oscillator/automorphic architecture"
        ),
    }
    expected_scope_flags = {
        "prime_direct_sum_called_adelic_restricted_tensor_product": False,
        "small_prime_window_extended": False,
        "chronology_averaged": False,
        "branch_characters_multiplied": False,
        "Theta_of_g_power_replaced_by_Theta_power": False,
        "C24_P073_called_a_C26_branch": False,
        "Schatten_regularization_called_an_ordinary_determinant": False,
        "prime_weight_called_source_derived": False,
        "common_quadratic_conductor_claimed": False,
        "xi_divisor_or_RH_claimed": False,
        "Route_B_used": False,
    }

    gamma_record = certificate["gamma_star_raw_product_control"]
    normalized = certificate["normalized_character_limit_theorem"]
    monoid = normalized["AGY_positive_monoid"]
    schatten = certificate["sharp_schatten_theorem"]
    general_weight = schatten["general_weight"]
    prime_weight = schatten["prime_norm_weight"]
    regularized = schatten["regularized_determinants"]
    fredholm = certificate["prime_direct_sum_fredholm_theorem"]
    marked = certificate["marked_normalization_threshold"]
    p073_record = certificate["c24_p073_fixed_plane_obstruction"]
    p073_prime = p073_record["all_odd_prime_theorem"]
    scope = certificate["scope_firewall"]
    certificate_phase = [
        {
            "Re_z": row["Re_z"],
            "q": row["Schatten_q"],
            "membership": row["membership"],
        }
        for row in prime_weight["phase_diagram_controls"]
    ]
    expected_factorization = {str(prime): exponent for prime, exponent in factors.items()}
    expected_mobius = {"1": 1, **{str(n): 0 for n in range(2, 33)}}

    return {
        "schema": certificate["schema"] == "HCS-C28-PRIME-DIRECT-SUM-DETERMINANT-V1",
        "candidate_identity": certificate["candidate_id"] == "HCS-C28"
        and certificate["candidate_name"] == "AGY prime-direct-sum finite-Weil determinant",
        "source_lock": certificate["source_lock"] == expected_source_lock,
        "producer_hash": certificate["runtime"]["producer_sha256"] == sha256(PRODUCER_PATH),
        "gamma_matrix": gamma_record["matrix"] == gamma,
        "gamma_discriminant": gamma_record["det_I_minus_g"] == d_gamma,
        "gamma_factorization": gamma_record["factorization"] == expected_factorization,
        "gamma_squarefree": gamma_record["squarefree_kernel"] == sqf,
        "gamma_character_classes": gamma_record["first_negative_reduced_class"] == 2
        and gamma_record["negative_class_character"] == -1
        and gamma_record["first_positive_reduced_class"] == 3
        and gamma_record["positive_class_character"] == 1,
        "gamma_raw_product_gate": gamma_record["raw_character_product"]
        == "NO_NONZERO_UNORDERED_PRODUCT",
        "normalized_character_status": normalized["status"]
        == "PROVED_FROM_C27_THOMAS_FORMULA_AND_EVENTUAL_RANK_STABILITY",
        "normalized_character_limit": normalized["pointwise_limit"]
        == "Theta_p(h)/p^2 -> 1 if h=I and 0 otherwise",
        "regular_trace_identity_gate": monoid["nonempty_identity_words"] == 0
        and monoid["normalized_moments"]
        == "p^(-2) Tr(L_(s,p)^n) -> 0 for every n>=1"
        and monoid["determinant_germ"]
        == (
            "exp[p^(-2) Log_0 D_p(s,u)] -> 1 locally uniformly on "
            "K x {|u|<epsilon_K}"
        )
        and monoid["logarithm_branch"] == "Log_0 D_p(s,0)=0"
        and monoid["common_disc_quantifier"]
        == "for every compact K in the s-domain, epsilon_K>0 is independent of p",
        "schatten_status": schatten["status"] == "PROVED",
        "schatten_local_asymptotic": schatten["local_asymptotic"]
        == "norm_Sq(L_(s,p)) is comparable to p^(2/q), 1<=q<=infinity",
        "schatten_general_weight_gate": general_weight["Schatten_q_iff"]
        == "sum_p p^2*abs(c_p)^q < infinity"
        and general_weight["compact_iff"] == "c_p -> 0",
        "schatten_prime_weight_gate": prime_weight["Schatten_q_iff"] == "q*Re(z)>3"
        and prime_weight["ordinary_trace_class_iff"] == "Re(z)>3"
        and prime_weight["unweighted_direct_sum"] == "NOT_COMPACT",
        "schatten_phase_diagram": certificate_phase == phase,
        "regularized_determinant_gate": regularized
        == {
            "det_m_available": "Re(z)>3/m",
            "z_equals_2": "S_2 but not S_1; det_2 deletes the first trace",
            "z_equals_1": "first finite regularized determinant is det_4",
            "z_equals_0": "not compact; no finite-order regularized determinant",
        },
        "fredholm_status_and_domain": fredholm["status"] == "PROVED"
        and fredholm["domain"] == "Re(s)>-sigma_0 and Re(z)>3",
        "fredholm_product_gate": fredholm["local_product"]
        == "D_sum(s,z,u)=product_(p odd) D_p(s,u*p^(-z))"
        and fredholm["product_convergence"]
        == "locally normal and independent of prime enumeration"
        and fredholm["joint_holomorphy"] == "in (s,z,u) on the displayed domain",
        "fredholm_chronology_gate": fredholm["word_trace"]
        == (
            "Tr L_sum(s,z)^n=sum_p p^(-n*z) sum_(w in Gamma^n) "
            "Theta_p(g_w)*lambda_w^(-(s+1))/chi_w'(lambda_w)"
        )
        and fredholm["repetition_firewall"]
        == "w^r uses p^(-n*r*z)*Theta_p(g_w^r), never Theta_p(g_w)^r",
        "fredholm_terminology_gate": fredholm["terminology"]
        == "prime-graded Dirichlet-Fredholm determinant, not an adelic Weil representation",
        "marked_threshold_gate": marked["status"] == "PROVED"
        and marked["parameter_domain"] == "alpha in C"
        and marked["marked_absolute_prime_sum"]
        == "sum_p p^(-Re(alpha))*abs(Theta_p(g))"
        and marked["convergence_iff"] == "Re(alpha)>1+k_Q/2"
        and marked["dimension_normalization_safe_iff"] == "k_Q<=1"
        and marked["critical_fixed_plane"] == "k_Q=2 gives sum_p 1/p",
        "p073_exact_arithmetic": p073_record["fixed_dimension_over_Q"]
        == p073["g_minus_I_rank"]
        and p073_record["two_by_two_minor_gcd"] == p073["two_minor_gcd"]
        and p073_record["thomas_quotient_form"] == p073["quotient_form"]
        and p073_record["thomas_quotient_determinant"] == -4,
        "p073_all_prime_gate": p073_prime["kernel_dimension_mod_p"] == 2
        and p073_prime["exact_character"] == "p"
        and p073_prime["dimension_normalized_character"] == "1/p"
        and p073_prime["marked_prime_sum"] == "sum_(p odd) 1/p diverges"
        and p073_prime["consequence"]
        == "FULL_RAUZY_DIMENSION_NORMALIZED_MARKED_ASSEMBLY_FAILS",
        "fixed_space_census": certificate["c24_fixed_space_census"]["fixed_dimension_counts"]
        == {str(key): value for key, value in sorted(count.items())}
        and certificate["c24_fixed_space_census"]["unique_fixed_dimension_two_id"] == "C24-P073",
        "mobius_prime_series_gate": certificate["quadratic_prime_series"]["divisor_mobius_sums"]
        == expected_mobius
        and certificate["quadratic_prime_series"]["maximum_formal_prime_power_order_checked"] == 32
        and certificate["quadratic_prime_series"]["odd_prime_series_definition"]
        == "P_chi^odd(q)=sum_(p odd) chi(p)*p^(-q)"
        and certificate["quadratic_prime_series"]["identity"]
        == (
            "P_chi^odd(q)=sum_(k>=1) mu(k)/k Log_E L(k*q,chi^k)"
            "-chi(2)*2^(-q), Re(q)>1"
        )
        and certificate["quadratic_prime_series"]["euler_log_branch"]
        == (
            "Log_E is the Euler-product logarithm on Re(q)>1, "
            "normalized to 0 as Re(q)->+infinity"
        )
        and certificate["quadratic_prime_series"]["power_character_scope"]
        == "chi^k(n)=chi(n)^k pointwise and may be imprimitive",
        "decisions": certificate["decisions"] == expected_decisions,
        "scope_flags": scope["flags"] == expected_scope_flags,
        "scope_positive_claim": scope["positive_claim"]
        == (
            "a sharp prime-Schatten phase diagram and an ordinary prime-graded Fredholm determinant "
            "for Re(z)>3"
        ),
        "scope_negative_claim": scope["negative_claim"]
        == (
            "the unweighted direct sum is noncompact, the canonical normalized-trace AGY limit is trivial, "
            "and a full-Rauzy fixed-plane orbit defeats dimension-normalized marked assembly"
        ),
    }


def run(certificate_path: Path) -> dict[str, object]:
    paths = {"C24": C24_PATH, "C25": C25_PATH, "C26": C26_PATH, "C27": C27_PATH}
    observed_hashes = {name: sha256(path) for name, path in paths.items()}
    if observed_hashes != EXPECTED_SOURCE_HASHES:
        raise AssertionError(f"independent source lock failed: {observed_hashes}")
    c24 = json.loads(C24_PATH.read_text(encoding="utf-8"))
    c26 = json.loads(C26_PATH.read_text(encoding="utf-8"))
    c27 = json.loads(C27_PATH.read_text(encoding="utf-8"))
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))

    stored_payload_hash = certificate.get("certificate_payload_sha256")
    unsigned_payload = dict(certificate)
    unsigned_payload.pop("certificate_payload_sha256", None)
    observed_payload_hash = canonical_sha256(unsigned_payload)
    payload_hash_check = stored_payload_hash == observed_payload_hash
    if not payload_hash_check:
        raise AssertionError(
            "certificate payload digest failed: "
            f"stored={stored_payload_hash!r}, observed={observed_payload_hash}"
        )

    gamma = graph_replay(c26)
    released = [[int(v) for v in row] for row in c26["source_locked_branch"]["chronological_matrix_B"]]
    d_gamma = det_bareiss(matsub(eye(4), gamma))
    factors = factor_trial(d_gamma)
    sqf = squarefree_from_factors(d_gamma, factors)
    delta = sqf if sqf % 4 == 1 else 4 * sqf
    gamma_checks = {
        "matrix_replay": gamma == released,
        "det_I_minus": d_gamma == 460097253,
        "factorization": factors == {3: 4, 7: 1, 11: 1, 71: 1, 1039: 1},
        "squarefree": sqf == 5680213,
        "fundamental_discriminant": delta == 5680213,
        "negative_class": kronecker_odd_numerator(delta, 2) == -1,
        "positive_class": kronecker_odd_numerator(delta, 3) == 1,
        "c27_match": d_gamma
        == int(c27["published_orbit_discriminants"]["records"]["gamma_star"]["value"]),
    }
    if not all(gamma_checks.values()):
        raise AssertionError(f"independent gamma controls failed: {gamma_checks}")

    p073 = p073_replay(c24)
    count = census(c24)
    phase = phase_diagram_replay()

    certificate_checks = decisive_certificate_checks(
        certificate,
        observed_hashes,
        gamma,
        d_gamma,
        factors,
        sqf,
        p073,
        count,
        phase,
    )
    if not all(certificate_checks.values()):
        raise AssertionError(f"certificate replay failed: {certificate_checks}")

    return {
        "schema": "HCS-C28-INDEPENDENT-CHECK-V1",
        "status": "PASS",
        "source_hashes": observed_hashes,
        "gamma_star_checks": gamma_checks,
        "p073_replay": p073,
        "fixed_space_census": {str(key): value for key, value in sorted(count.items())},
        "schatten_phase_controls": phase,
        "payload_hash_check": payload_hash_check,
        "certificate_payload_sha256": observed_payload_hash,
        "certificate_checks": certificate_checks,
        "scope": {
            "bounded_prime_scan_used": False,
            "floating_point_decision_used": False,
            "producer_imported": False,
            "P073_called_C26_branch": False,
        },
        "runtime": {
            "python": platform.python_version(),
            "checker_sha256": sha256(Path(__file__)),
            "certificate_sha256": sha256(certificate_path),
        },
    }


def main() -> None:
    args = parse_args()
    report = run(args.certificate)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "status": report["status"]}, sort_keys=True))


if __name__ == "__main__":
    main()
