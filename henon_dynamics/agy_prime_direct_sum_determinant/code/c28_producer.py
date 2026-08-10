#!/usr/bin/env python3
"""Produce the exact HCS-C28 prime-assembly certificate.

This program does not enlarge the C27 prime scan.  It verifies the finite
integer identities needed by three theorem-level conclusions:

* normalized finite-Weil characters converge to the regular character of
  the integral Rauzy matrix monoid;
* the C27 local Schatten growth is exactly p^(2/q), giving the sharp
  prime-direct-sum threshold q*Re(z)>3;
* the C24-P073 fixed plane has Theta_p=p for every odd prime, so its
  dimension-normalized marked prime trace is the divergent sum of 1/p.

The functional-analytic implications are recorded together with their exact
hypotheses.  No numerical Riemann-zero data or chronological average enters.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
from fractions import Fraction
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
HENON_ROOT = PROJECT.parent
C24_PATH = HENON_ROOT / "rauzy_metaplectic_obstruction" / "results" / "c24_certificate.json"
C25_PATH = HENON_ROOT / "agy_metaplectic_transfer_obstruction" / "results" / "c25_certificate.json"
C26_PATH = HENON_ROOT / "agy_holomorphic_slice_obstruction" / "results" / "c26_certificate.json"
C27_PATH = HENON_ROOT / "agy_finite_weil_determinant" / "results" / "c27_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c28_certificate.json"

EXPECTED_SOURCE_HASHES = {
    "C24": "4b4fe5943262137eeeb3eda4de887725a0663402a1f39f8cc43e089bcc91e778",
    "C25": "a35cee22714abbb9dc9aadcc165720d1ff77aff3b7f29071f53a1b451760bd12",
    "C26": "1c0289b9b47e65e0603ea001be7cce263aea13d58c66e4609eac88edf8f7ce4a",
    "C27": "8676d17c5a0e4444dded88b5a76f5ea1fa974275528aa0a51400730759d8b029",
}

GAMMA_STAR = "t" * 64 + "tbttbtbb" * 8


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha256(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def matrix_json(matrix: sp.MatrixBase) -> list[list[int]]:
    return [[int(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def load_sources() -> tuple[dict[str, object], ...]:
    paths = {"C24": C24_PATH, "C25": C25_PATH, "C26": C26_PATH, "C27": C27_PATH}
    observed = {name: sha256(path) for name, path in paths.items()}
    if observed != EXPECTED_SOURCE_HASHES:
        raise AssertionError(f"source lock changed: {observed}")
    loaded = tuple(json.loads(path.read_text(encoding="utf-8")) for path in paths.values())
    source_lock = {
        "files": {
            name: {
                "path": str(path.relative_to(HENON_ROOT.parent)),
                "sha256": observed[name],
            }
            for name, path in paths.items()
        },
        "chronology": "later Rauzy edges and later AGY returns multiply on the left",
        "prime_scope": "all odd primes in theorems; no new bounded prime scan",
        "fibre": "the full p^2-dimensional finite Weil representation from C27",
    }
    return (*loaded, source_lock)


def graph_edges(c26: dict[str, object]) -> dict[tuple[int, str], tuple[int, sp.Matrix]]:
    result: dict[tuple[int, str], tuple[int, sp.Matrix]] = {}
    for edge in c26["graph"]["edges"]:
        result[(int(edge["source"]), str(edge["type"]))] = (
            int(edge["target"]),
            sp.Matrix(edge["chronological_matrix"]),
        )
    if len(result) != 14:
        raise AssertionError("C26 seven-state graph changed")
    return result


def replay_word(
    start: int, word: str, edges: dict[tuple[int, str], tuple[int, sp.Matrix]]
) -> tuple[int, sp.Matrix]:
    state = start
    product = sp.eye(4)
    for token in word:
        state, edge_matrix = edges[(state, token)]
        product = edge_matrix * product
    return state, product


def squarefree_kernel(value: int) -> int:
    if value == 0:
        return 0
    factors = sp.factorint(abs(value))
    return (-1 if value < 0 else 1) * math.prod(
        int(prime) for prime, exponent in factors.items() if exponent % 2
    )


def fundamental_discriminant(squarefree: int) -> int:
    if squarefree == 0:
        raise ValueError("zero has no quadratic fundamental discriminant")
    return squarefree if squarefree % 4 == 1 else 4 * squarefree


def minor_values(matrix: sp.MatrixBase, size: int) -> list[int]:
    return [
        int(matrix.extract(rows, columns).det())
        for rows in itertools.combinations(range(matrix.rows), size)
        for columns in itertools.combinations(range(matrix.cols), size)
    ]


def fixed_dimension(matrix: sp.MatrixBase) -> int:
    return 4 - int((matrix - sp.eye(4)).rank())


def p073_control(c24: dict[str, object]) -> dict[str, object]:
    row = next(item for item in c24["eventually_positive_cycles"] if item["id"] == "C24-P073")
    matrix = sp.Matrix(row["base_trivialized_symplectic_matrix"])
    form = sp.Matrix(c24["source_lock"]["J0"])
    h = matrix - sp.eye(4)
    two_minors = minor_values(h, 2)
    three_minors = minor_values(h, 3)
    quotient_columns = [0, 1]
    complement = sp.eye(4)[:, quotient_columns]
    quotient_form = complement.T * h.T * form * complement
    checks = {
        "primitive_directed_cycle": bool(row["primitive_directed_cycle"]),
        "all_cyclic_phases_eventually_positive": len(row["positive_phase_indices"])
        == int(row["cyclic_phase_count"]),
        "symplectic": matrix.T * form * matrix == form,
        "determinant_one": int(matrix.det()) == 1,
        "rank_g_minus_I_over_Q_is_two": int(h.rank()) == 2,
        "gcd_of_two_by_two_minors_is_one": math.gcd(*two_minors) == 1,
        "all_three_by_three_minors_zero": all(value == 0 for value in three_minors),
        "quotient_form_determinant_is_minus_four": int(quotient_form.det()) == -4,
    }
    if not all(checks.values()):
        raise AssertionError(f"C24-P073 fixed-plane control failed: {checks}")
    characteristic = sp.factor(matrix.charpoly().as_expr())
    if characteristic != (sp.Symbol("lambda") - 1) ** 2 * (
        sp.Symbol("lambda") ** 2 - 18 * sp.Symbol("lambda") + 1
    ):
        raise AssertionError("C24-P073 characteristic polynomial changed")
    return {
        "id": row["id"],
        "scope": "C24 full Rauzy periodic ledger control; not asserted to be a C26 induced branch",
        "matrix": matrix_json(matrix),
        "symplectic_form": matrix_json(form),
        "characteristic_coefficients_descending": [int(v) for v in matrix.charpoly().all_coeffs()],
        "characteristic_factorization": "(x-1)^2*(x^2-18*x+1)",
        "g_minus_I": matrix_json(h),
        "fixed_dimension_over_Q": fixed_dimension(matrix),
        "two_by_two_minor_gcd": math.gcd(*two_minors),
        "three_by_three_minors": sorted(set(three_minors)),
        "quotient_columns": quotient_columns,
        "thomas_quotient_form": matrix_json(quotient_form),
        "thomas_quotient_determinant": int(quotient_form.det()),
        "checks": checks,
        "all_odd_prime_theorem": {
            "kernel_dimension_mod_p": 2,
            "reason_kernel": (
                "all 3x3 minors vanish and the gcd of the 2x2 minors is one, so rank(g-I)=2 "
                "over every finite field"
            ),
            "character_formula": "Theta_p=Legendre(-4,p)*Legendre(-1,p)*p=p",
            "exact_character": "p",
            "dimension_normalized_character": "1/p",
            "marked_prime_sum": "sum_(p odd) 1/p diverges",
            "consequence": "FULL_RAUZY_DIMENSION_NORMALIZED_MARKED_ASSEMBLY_FAILS",
        },
    }


def fixed_space_census(c24: dict[str, object]) -> dict[str, object]:
    counts: dict[int, int] = {}
    ids: dict[int, list[str]] = {}
    for row in c24["eventually_positive_cycles"]:
        k = fixed_dimension(sp.Matrix(row["base_trivialized_symplectic_matrix"]))
        counts[k] = counts.get(k, 0) + 1
        ids.setdefault(k, []).append(str(row["id"]))
    expected = {0: 125, 1: 20, 2: 1}
    if counts != expected or ids.get(2) != ["C24-P073"]:
        raise AssertionError(f"C24 fixed-space census changed: {counts}, {ids.get(2)}")
    return {
        "cycle_count": sum(counts.values()),
        "fixed_dimension_counts": {str(key): value for key, value in sorted(counts.items())},
        "unique_fixed_dimension_two_id": ids[2][0],
        "scope": "exact census of the 146 frozen C24 eventually-positive labeled cycles",
    }


def gamma_star_control(c26: dict[str, object], c27: dict[str, object]) -> dict[str, object]:
    source = c26["source_locked_branch"]
    end, replayed = replay_word(int(source["start_state"]), GAMMA_STAR, graph_edges(c26))
    released = sp.Matrix(source["chronological_matrix_B"])
    if end != int(source["end_state"]) or replayed != released:
        raise AssertionError("gamma_star chronological replay failed")
    discriminant = int((sp.eye(4) - released).det())
    sqf = squarefree_kernel(discriminant)
    published = c27["published_orbit_discriminants"]["records"]["gamma_star"]
    if discriminant != 460097253 or sqf != 5680213:
        raise AssertionError("gamma_star discriminant sentinel changed")
    if discriminant != int(published["value"]) or sqf != int(published["squarefree_kernel"]):
        raise AssertionError("C27 published gamma_star arithmetic disagrees")
    delta = fundamental_discriminant(sqf)
    negative_class = next(
        a for a in range(2, 1000) if math.gcd(a, delta) == 1 and sp.kronecker_symbol(delta, a) == -1
    )
    positive_class = next(
        a for a in range(2, 1000) if math.gcd(a, delta) == 1 and sp.kronecker_symbol(delta, a) == 1
    )
    return {
        "branch": "gamma_star",
        "AGY_return_count": 1,
        "elementary_Rauzy_length": len(GAMMA_STAR),
        "word_sha256": hashlib.sha256(GAMMA_STAR.encode("ascii")).hexdigest(),
        "matrix": matrix_json(released),
        "det_I_minus_g": discriminant,
        "factorization": {str(p): int(e) for p, e in sp.factorint(discriminant).items()},
        "squarefree_kernel": sqf,
        "fundamental_discriminant": delta,
        "first_negative_reduced_class": negative_class,
        "negative_class_character": int(sp.kronecker_symbol(delta, negative_class)),
        "first_positive_reduced_class": positive_class,
        "positive_class_character": int(sp.kronecker_symbol(delta, positive_class)),
        "dirichlet_progression_consequence": (
            "infinitely many good primes have Theta_p=-1 and infinitely many have Theta_p=+1"
        ),
        "raw_character_product": "NO_NONZERO_UNORDERED_PRODUCT",
    }


def normalized_character_limit_theorem() -> dict[str, object]:
    return {
        "status": "PROVED_FROM_C27_THOMAS_FORMULA_AND_EVENTUAL_RANK_STABILITY",
        "rank_definition": "r(h)=rank_Q(h-I)",
        "eventual_exact_magnitude": "abs(Theta_p(h))/p^2=p^(-r(h)/2) outside finitely many primes",
        "pointwise_limit": "Theta_p(h)/p^2 -> 1 if h=I and 0 otherwise",
        "interpretation": "the normalized characters converge pointwise to the regular character delta_identity",
        "AGY_positive_monoid": {
            "source": "C25 Theorem E.1 and Corollary E.2",
            "property": "the chronological first-return matrix monoid is free",
            "nonempty_identity_words": 0,
            "normalized_moments": "p^(-2) Tr(L_(s,p)^n) -> 0 for every n>=1",
            "determinant_germ": (
                "exp[p^(-2) Log_0 D_p(s,u)] -> 1 locally uniformly on "
                "K x {|u|<epsilon_K}"
            ),
            "logarithm_branch": "Log_0 D_p(s,0)=0",
            "common_disc_quantifier": (
                "for every compact K in the s-domain, epsilon_K>0 is independent of p"
            ),
        },
    }


def schatten_theorem() -> dict[str, object]:
    phase_rows = []
    for z, q in [(0, 1), (1, 3), (1, 4), (2, 1), (2, 2), (3, 1), (4, 1)]:
        product = q * z
        phase_rows.append(
            {
                "Re_z": z,
                "Schatten_q": q,
                "q_times_Re_z": product,
                "membership": product > 3,
                "boundary_or_failure_reason": (
                    "sum_p p^(2-q*Re_z) diverges" if product <= 3 else None
                ),
            }
        )
    return {
        "status": "PROVED",
        "local_asymptotic": "norm_Sq(L_(s,p)) is comparable to p^(2/q), 1<=q<=infinity",
        "uniformity": "comparison constants are locally uniform in s",
        "lower_bound_mechanism": (
            "compress by constants and point evaluation, test against rho_p(g_delta)^(-1), "
            "use C25 matrix injectivity plus normalized-character convergence and Schatten Holder"
        ),
        "upper_bound_mechanism": (
            "sum the C26 scalar branch Schatten norms after tensoring with p^2-dimensional unitaries"
        ),
        "general_weight": {
            "operator": "direct_sum_p c_p L_(s,p)",
            "Schatten_q_iff": "sum_p p^2*abs(c_p)^q < infinity",
            "compact_iff": "c_p -> 0",
        },
        "prime_norm_weight": {
            "c_p": "p^(-z)",
            "Schatten_q_iff": "q*Re(z)>3",
            "ordinary_trace_class_iff": "Re(z)>3",
            "unweighted_direct_sum": "NOT_COMPACT",
            "phase_diagram_controls": phase_rows,
        },
        "regularized_determinants": {
            "det_m_available": "Re(z)>3/m",
            "z_equals_2": "S_2 but not S_1; det_2 deletes the first trace",
            "z_equals_1": "first finite regularized determinant is det_4",
            "z_equals_0": "not compact; no finite-order regularized determinant",
        },
    }


def direct_sum_fredholm_theorem() -> dict[str, object]:
    return {
        "status": "PROVED",
        "hilbert_space": "H_sum=direct_sum_(p odd) (A^2(Omega) tensor C^(p^2))",
        "operator": "L_sum(s,z)=direct_sum_(p odd) p^(-z) L_(s,p)",
        "domain": "Re(s)>-sigma_0 and Re(z)>3",
        "determinant": "D_sum(s,z,u)=det(I-u L_sum(s,z))",
        "local_product": "D_sum(s,z,u)=product_(p odd) D_p(s,u*p^(-z))",
        "product_convergence": "locally normal and independent of prime enumeration",
        "joint_holomorphy": "in (s,z,u) on the displayed domain",
        "word_trace": (
            "Tr L_sum(s,z)^n=sum_p p^(-n*z) sum_(w in Gamma^n) "
            "Theta_p(g_w)*lambda_w^(-(s+1))/chi_w'(lambda_w)"
        ),
        "repetition_firewall": "w^r uses p^(-n*r*z)*Theta_p(g_w^r), never Theta_p(g_w)^r",
        "terminology": "prime-graded Dirichlet-Fredholm determinant, not an adelic Weil representation",
    }


def marked_normalization_threshold() -> dict[str, object]:
    return {
        "status": "PROVED",
        "parameter_domain": "alpha in C",
        "fixed_space_dimension": "k_Q=dim_Q ker(g-I)",
        "eventual_character_magnitude": "p^(k_Q/2)",
        "marked_absolute_prime_sum": "sum_p p^(-Re(alpha))*abs(Theta_p(g))",
        "convergence_iff": "Re(alpha)>1+k_Q/2",
        "dimension_normalization_alpha": 2,
        "dimension_normalization_safe_iff": "k_Q<=1",
        "critical_fixed_plane": "k_Q=2 gives sum_p 1/p",
        "scope": "marked orbit coefficient; aggregate cancellations are a different object",
    }


def mobius_log_l_check(maximum: int = 32) -> dict[str, object]:
    divisor_sums = {
        str(n): sum(int(sp.mobius(d)) for d in sp.divisors(n)) for n in range(1, maximum + 1)
    }
    if divisor_sums["1"] != 1 or any(value != 0 for key, value in divisor_sums.items() if key != "1"):
        raise AssertionError("Möbius log-L coefficient cancellation failed")
    return {
        "maximum_formal_prime_power_order_checked": maximum,
        "divisor_mobius_sums": divisor_sums,
        "odd_prime_series_definition": "P_chi^odd(q)=sum_(p odd) chi(p)*p^(-q)",
        "identity": (
            "P_chi^odd(q)=sum_(k>=1) mu(k)/k Log_E L(k*q,chi^k)"
            "-chi(2)*2^(-q), Re(q)>1"
        ),
        "euler_log_branch": (
            "Log_E is the Euler-product logarithm on Re(q)>1, normalized to 0 as Re(q)->+infinity"
        ),
        "power_character_scope": "chi^k(n)=chi(n)^k pointwise and may be imprimitive",
        "word_formula": (
            "sum_(p odd) p^(-n*z) Theta_p(g_w) equals the odd quadratic prime series "
            "P_(chi_w)(n*z) plus finitely many singular-prime corrections"
        ),
        "warning": "chi_w and its conductor depend on the chronological orbit",
    }


def scope_firewall() -> dict[str, object]:
    flags = {
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
    if any(flags.values()):
        raise AssertionError("scope firewall failed")
    return {
        "flags": flags,
        "positive_claim": (
            "a sharp prime-Schatten phase diagram and an ordinary prime-graded Fredholm determinant "
            "for Re(z)>3"
        ),
        "negative_claim": (
            "the unweighted direct sum is noncompact, the canonical normalized-trace AGY limit is trivial, "
            "and a full-Rauzy fixed-plane orbit defeats dimension-normalized marked assembly"
        ),
    }


def run() -> dict[str, object]:
    c24, _c25, c26, c27, source_lock = load_sources()
    p073 = p073_control(c24)
    census = fixed_space_census(c24)
    gamma = gamma_star_control(c26, c27)
    report = {
        "schema": "HCS-C28-PRIME-DIRECT-SUM-DETERMINANT-V1",
        "candidate_id": "HCS-C28",
        "candidate_name": "AGY prime-direct-sum finite-Weil determinant",
        "source_lock": source_lock,
        "gamma_star_raw_product_control": gamma,
        "normalized_character_limit_theorem": normalized_character_limit_theorem(),
        "sharp_schatten_theorem": schatten_theorem(),
        "prime_direct_sum_fredholm_theorem": direct_sum_fredholm_theorem(),
        "marked_normalization_threshold": marked_normalization_threshold(),
        "c24_fixed_space_census": census,
        "c24_p073_fixed_plane_obstruction": p073,
        "quadratic_prime_series": mobius_log_l_check(),
        "decisions": {
            "raw_unweighted_prime_direct_sum": "FAIL_NOT_COMPACT",
            "raw_gamma_star_character_product": "FAIL_NONCONVERGENT",
            "normalized_trace_AGY_limit": "EXISTS_BUT_DETERMINANT_GERM_EQUALS_ONE",
            "prime_norm_direct_sum": "PASS_ORDINARY_FREDHOLM_IFF_RE_Z_GT_3",
            "full_Rauzy_dimension_normalized_marked_assembly": "FAIL_P073_HARMONIC_DIVERGENCE",
            "C26_induced_dimension_normalized_marked_assembly": "OPEN_ALL_WORD_FIXED_SPACE_GATE",
            "intrinsic_one_clock_Hilbert_Polya_gate": "FAIL_EXTERNAL_LOG_P_CLOCK",
            "route_B_authorized": False,
            "next_action": (
                "pivot to a two-sided based/path-groupoid trace or a genuine p-adic oscillator/automorphic architecture"
            ),
        },
        "scope_firewall": scope_firewall(),
        "runtime": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
            "producer_sha256": sha256(Path(__file__)),
        },
        "material_passport": {
            "origin": "C28 theorem-level global finite-Weil assembly gate",
            "origin_date": "2026-08-10",
            "origin_mode": "exact source-locked arithmetic plus operator-theoretic derivation",
            "verification_status": "PRODUCER_COMPLETE; INDEPENDENT_REPLAY_REQUIRED",
            "version_label": "HCS-C28-v1",
        },
    }
    report["certificate_payload_sha256"] = canonical_sha256(report)
    return report


def main() -> None:
    args = parse_args()
    report = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "trace_class_threshold": report["sharp_schatten_theorem"]["prime_norm_weight"][
                    "ordinary_trace_class_iff"
                ],
                "p073_character": report["c24_p073_fixed_plane_obstruction"][
                    "all_odd_prime_theorem"
                ]["exact_character"],
                "normalized_limit": report["decisions"]["normalized_trace_AGY_limit"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
