#!/usr/bin/env python3
"""Independent fail-closed checker for the HCS-C51 certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
from typing import Any, Callable


SCHEMA = "hcs-c51-certificate-v1"
CHECK_SCHEMA = "hcs-c51-independent-check-v1"
FROZEN_PAYLOAD_SHA256 = "2fdfc4fb2559d4cc9b253d978b8074bf57c49888ce2ff4d29545b127e9af95c1"
SOURCE_HASHES = {
    "C47": (
        "henon_dynamics/henon_mu3_normalized_trace_operator_gate/results/c47_certificate.json",
        "2c30a488f675bb68af17b2567c81946188525d007188c91b058c964c0ed7c09e",
    ),
    "C48": (
        "henon_dynamics/henon_mu3_genus4_second_moment/results/c48_certificate.json",
        "92cd5c1079ebbaeaa27fc32e617852ae5d5989500ff3a816dd9fe306c32a32a8",
    ),
    "C49": (
        "henon_dynamics/henon_mu3_fano_threefold_third_moment/results/c49_certificate.json",
        "b3ec1bf12ea0f05469054fda37bd34ee4b6748030813c8c6407752035a3c25d2",
    ),
    "C50": (
        "henon_dynamics/henon_mu3_elliptic_resummation_fourth_moment/results/c50_certificate.json",
        "ef77b61758ccaf59e2e24e79dc535e2216d794843ff5f16ae0ca4ded12eb9dde",
    ),
}
COMPONENT_SPECS = (
    (2, "n2_tate", "EVEN", "Q(0)", 0, 0, 7, 1, "7", "C50_EXACT_FACTOR"),
    (2, "n2_curve_H1", "ODD", "H^1(C)", 1, 0, 1, 8, "a_C,p", "C50_EXACT_FACTOR"),
    (3, "n3_tate", "EVEN", "Q(0)", 0, 0, 21, 1, "21", "C49_EXACT_TRACE_TERM"),
    (3, "n3_fermat_Jacobi_rank2", "EVEN", "H^4_prim(S_3)_{non-Tate/Jacobi}(2)", 4, 2, 1, 2, "(alpha_p-20p^2)/p^2=a_F,p/p", "C49_EXACT_TRACE_TERM"),
    (3, "n3_fano_H3", "ODD", "H^3(X_3)(1)", 3, 1, 1, 40, "b_X,p=beta_p/p", "C49_EXACT_TRACE_TERM"),
    (4, "n4_tate", "EVEN", "Q(0)", 0, 0, 1, 1, "1", "C50_EXACT_TRACE_TERM"),
    (4, "n4_cubic_H6", "EVEN", "H^6_prim(S_4)(3)", 6, 3, 1, 86, "alpha_p/p^3", "C50_EXACT_TRACE_TERM"),
    (4, "n4_fivefold_H5", "ODD", "H^5(X_4)(2)", 5, 2, 1, 168, "beta_p/p^2", "C50_EXACT_TRACE_TERM"),
)


class GateFailure(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if type(condition) is not bool or not condition:
        raise GateFailure(message)


def canonical_json(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            value.update(block)
    return value.hexdigest()


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


def same_recursive_shape(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return set(left) == set(right) and all(
            same_recursive_shape(left[key], right[key]) for key in left
        )
    if isinstance(left, list):
        return len(left) == len(right) and all(
            same_recursive_shape(a, b) for a, b in zip(left, right)
        )
    return True


def record(value: Fraction | int) -> dict[str, int]:
    value = Fraction(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


def parse_record(value: Any) -> Fraction:
    require(type(value) is dict, "fraction is not dict")
    require(set(value) == {"numerator", "denominator"}, "fraction keys")
    require(type(value["numerator"]) is int, "fraction numerator type")
    require(type(value["denominator"]) is int, "fraction denominator type")
    require(value["denominator"] > 0, "fraction denominator sign")
    result = Fraction(value["numerator"], value["denominator"])
    require(strict_equal(value, record(result)), "fraction not reduced")
    return result


def expected_sources(repository: Path) -> tuple[list[dict[str, str]], dict[str, dict[str, Any]]]:
    locks, certificates = [], {}
    for source, (relative, expected_hash) in SOURCE_HASHES.items():
        path = repository / relative
        require(digest(path) == expected_hash, f"live source hash {source}")
        certificate = json.loads(path.read_text(encoding="utf-8"))
        locks.append({
            "source": source,
            "path": relative,
            "sha256": expected_hash,
            "schema": certificate["schema"],
            "payload_sha256": certificate["payload_sha256"],
        })
        certificates[source] = certificate
    return locks, certificates


def expected_components() -> list[dict[str, Any]]:
    result = []
    for n, cid, parity, motive, raw_weight, division, multiplicity, rank, expression, status in COMPONENT_SPECS:
        weight = raw_weight - 2 * division
        require(weight in (0, 1), f"normalized weight {cid}")
        require(parity == ("ODD" if weight == 1 else "EVEN"), f"parity {cid}")
        result.append({
            "moment_n": n,
            "component_id": cid,
            "parity": parity,
            "motive_after_source_twist": motive,
            "raw_weight_W": raw_weight,
            "source_p_division_t": division,
            "normalized_weight_w": weight,
            "multiplicity_in_e_plus_o": multiplicity,
            "base_motive_rank": rank,
            "contribution_rank": multiplicity * rank,
            "trace_expression_in_e_plus_o": expression,
            "status": status,
        })
    return result


def expected_prime_rows(certificates: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    c48 = {row["prime"]: row for row in certificates["C48"]["payload"]["exact_controls"]}
    c49 = {row["prime"]: row for row in certificates["C49"]["payload"]["exact_geometry_controls"]}
    output = []
    for four in certificates["C50"]["payload"]["exact_fourth_moment_controls"]:
        p = four["p"]
        two, three = c48[p], c49[p]
        degree = Fraction(p - 1, 2)

        curve = two["frobenius_trace_a_p"]
        e2, o2 = Fraction(7), Fraction(curve)
        C2 = -2 * e2 - 2 * o2
        c2 = C2 / degree
        require(C2 == two["galois_traced_second_moment_C_p_2"], f"n2 C p={p}")
        require(c2 == parse_record(two["normalized_second_moment_c_p_2"]), f"n2 c p={p}")

        alpha3, beta3 = three["alpha_p"], three["beta_p"]
        require((alpha3 - 20 * p**2) % p == 0, f"n3 alpha p={p}")
        require(beta3 % p == 0, f"n3 beta p={p}")
        a_fermat = Fraction(alpha3 - 20 * p**2, p)
        fermat_weight4_trace = alpha3 - 20 * p**2
        b_fano = Fraction(beta3, p)
        e3, o3 = Fraction(21) + a_fermat / p, b_fano
        C3 = -2 * e3 - 2 * o3
        c3 = C3 / degree
        require(C3 == parse_record(three["galois_traced_third_moment_C_p_3"]), f"n3 C p={p}")
        require(c3 == parse_record(three["normalized_third_moment_c_p_3"]), f"n3 c p={p}")

        alpha4, beta4 = four["alpha_p"], four["beta_p"]
        e4, o4 = Fraction(1) + Fraction(alpha4, p**3), Fraction(beta4, p**2)
        C4 = -2 * e4 - 2 * o4
        c4 = C4 / degree
        require(C4 == parse_record(four["C_p_4"]), f"n4 C p={p}")
        require(c4 == parse_record(four["c_p_4"]), f"n4 c p={p}")

        output.append({
            "p": p,
            "rho": four["rho"],
            "real_cyclotomic_degree_d_p": int(degree),
            "moments": {
                "n2": {
                    "even_trace_e_p_n": record(e2), "odd_trace_o_p_n": record(o2),
                    "C_p_n": record(C2), "c_p_n": record(c2),
                    "C_equals_minus_2_times_e_plus_o": True, "source_certificate_match": True,
                },
                "n3": {
                    "fermat_Jacobi_raw_weight4_trace": fermat_weight4_trace,
                    "fermat_Jacobi_weight2_quotient_a_F_p": record(a_fermat),
                    "fano_raw_trace_b_X_p": record(b_fano),
                    "even_trace_e_p_n": record(e3), "odd_trace_o_p_n": record(o3),
                    "C_p_n": record(C3), "c_p_n": record(c3),
                    "C_equals_minus_2_times_e_plus_o": True, "source_certificate_match": True,
                },
                "n4": {
                    "cubic_raw_trace_alpha_p": alpha4, "fivefold_raw_trace_beta_p": beta4,
                    "even_trace_e_p_n": record(e4), "odd_trace_o_p_n": record(o4),
                    "C_p_n": record(C4), "c_p_n": record(c4),
                    "C_equals_minus_2_times_e_plus_o": True, "source_certificate_match": True,
                },
            },
        })
    require(len(output) == 11, "common prime count")
    return output


def expected_rank_rows() -> list[dict[str, int]]:
    """Independent coefficient sums, not producer's truncated division."""
    output = []
    for n in range(2, 21):
        d_s, d_x = 2 * n - 2, 2 * n - 3
        cubic_coefficient = sum(
            comb(2 * n, d_s - k) * (-3) ** k for k in range(d_s + 1)
        )
        complete_coefficient = sum(
            comb(2 * n, d_x - k)
            * (-1) ** k
            * (3 ** (k + 1) - 2 ** (k + 1))
            for k in range(d_x + 1)
        )
        chi_s, chi_x = 3 * cubic_coefficient, 6 * complete_coefficient
        b_s, b_x = chi_s - (d_s + 1), (d_x + 1) - chi_x
        require(3 * b_s == 4**n + 2, f"cubic rank n={n}")
        require(3 * b_x == 2 * 4**n - 8, f"CI rank n={n}")
        require(1 + b_s + b_x == 4**n - 1, f"total rank n={n}")
        output.append({
            "n": n,
            "ambient_projective_dimension": 2 * n - 1,
            "cubic_dimension": d_s,
            "cubic_top_chern_coefficient": cubic_coefficient,
            "cubic_Euler_characteristic": chi_s,
            "cubic_primitive_middle_rank": b_s,
            "complete_intersection_dimension": d_x,
            "complete_intersection_top_chern_coefficient": complete_coefficient,
            "complete_intersection_Euler_characteristic": chi_x,
            "complete_intersection_middle_rank": b_x,
            "Tate_rank": 1,
            "total_normalized_trace_rank": 1 + b_s + b_x,
            "source_geometry_status": (
                "HENON_CHAR0_GEOMETRY_LOCKED"
                if n <= 4
                else "CONDITIONAL_SYMBOLIC_SMOOTH_CI_CONTROL"
            ),
        })
    return output


def expected_center_sections(components: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows = []
    for component in components:
        n, weight = component["moment_n"], component["normalized_weight_w"]
        for j in range(1, 5):
            reflection = Fraction(weight + 1 - 2 * j, n)
            rows.append({
                "component_id": component["component_id"],
                "moment_n": n,
                "normalized_weight_w": weight,
                "tower_index_j": j,
                "normalized_L_variable": {"slope": n, "intercept": j},
                "mapped_s_reflection": {"s_coefficient": -1, "constant": record(reflection)},
                "mapped_s_center": record(reflection / 2),
            })
    parity = {row["component_id"]: row["parity"] for row in components}

    def spectrum(j: int, selected_parity: str | None = None) -> list[dict[str, int]]:
        values = {
            parse_record(row["mapped_s_center"])
            for row in rows
            if row["tower_index_j"] == j
            and (selected_parity is None or parity[row["component_id"]] == selected_parity)
        }
        return [record(value) for value in sorted(values)]

    odd = {f"j{j}": spectrum(j, "ODD") for j in range(1, 5)}
    summary = {
        "tower_expansion": "1/(p-1)=sum_(j>=1) p^(-j)",
        "normalized_variable": "u_(n,j)=n*s+j",
        "mapped_center_formula": "center_s=((w+1)/2-j)/n",
        "j1_full_center_set": spectrum(1),
        "j1_odd_center_set": odd["j1"],
        "odd_center_sets_by_tower_index": odd,
        "odd_weight_alignment_holds_exactly_at_j1": strict_equal(odd["j1"], [record(0)]),
        "odd_weight_alignment_holds_for_full_tower": False,
        "full_source_native_affine_center_exists": False,
        "minimal_exact_witness": {
            "source": "C50 exact n=2 factorization",
            "factor_1": "zeta_K(2s+1)^7", "factor_1_center": record(Fraction(-1, 4)),
            "factor_2": "L(H^1(C/K),2s+1)", "factor_2_center": record(0),
            "factorwise_common_center_exists": False,
            "residual_H2_functional_equation_certified": False,
            "nonfactorwise_miracle_ruled_out": False,
        },
    }
    return rows, summary


def expected_tate_rows() -> list[dict[str, Any]]:
    result = []
    for n in range(2, 5):
        for weight in (0, 1):
            for j in range(1, 5):
                original = Fraction(weight + 1 - 2 * j, 2 * n)
                integer_rows = []
                for k in range(-3, 4):
                    new_weight, new_intercept = weight - 2 * k, j - k
                    new_center = Fraction(new_weight + 1 - 2 * new_intercept, 2 * n)
                    integer_rows.append({
                        "twist_k": k, "twisted_weight": new_weight,
                        "twisted_variable_intercept": new_intercept,
                        "center": record(new_center), "center_invariant": new_center == original,
                    })
                half = Fraction(-1, 2)
                half_weight, half_intercept = Fraction(weight) - 2 * half, Fraction(j) - half
                half_center = Fraction(half_weight + 1 - 2 * half_intercept, 2 * n)
                result.append({
                    "moment_n": n, "normalized_weight_w": weight, "tower_index_j": j,
                    "original_center": record(original), "integral_twists": integer_rows,
                    "formal_half_twist": {
                        "twist_k": record(half), "twisted_weight": record(half_weight),
                        "consistent_variable_intercept": record(half_intercept),
                        "consistent_center": record(half_center),
                        "consistent_center_invariant": half_center == original,
                        "fixed_clock_local_coefficient_multiplier": "p^(1/2)",
                        "fixed_clock_preserves_source_moment": False,
                    },
                })
    return result


def expected_exponents() -> dict[str, Any]:
    controls = []
    for n in range(2, 5):
        exponent = Fraction(2, n)
        controls.append({
            "moment_n": n,
            "rational_split_prime_leading_log_multiplier_per_trace": record(Fraction(4, n)),
            "degree_one_K_primes_above_split_p": 2,
            "candidate_K_L_exponent_per_trace": record(exponent),
            "exponent_integral": exponent.denominator == 1,
            "ordinary_single_valued_meromorphic_L_power_certified": n == 2,
        })
    return {
        "derivation": "-c_p,n/n=4(e_p,n+o_p,n)/(n(p-1)); two split K-primes give exponent 2/n per trace",
        "controls": controls,
        "n2_component_powers": {"zeta_K": record(7), "H1_curve": record(1)},
        "n3_component_powers": {"Tate_total": record(14), "Fermat_Jacobi_rank2_trace": record(Fraction(2, 3)), "Fano_trace": record(Fraction(2, 3))},
        "n4_component_powers": {"Tate_total": record(Fraction(1, 2)), "cubic_trace": record(Fraction(1, 2)), "fivefold_trace": record(Fraction(1, 2))},
        "fractional_power_firewall": "n=3,4 powers are coefficient bookkeeping, not certified ordinary meromorphic L-products",
    }


def expected_ordinary_obstruction(
    components: list[dict[str, Any]], rank_rows: list[dict[str, Any]]
) -> dict[str, Any]:
    rank_data = []
    for n in range(2, 5):
        even = sum(
            row["contribution_rank"]
            for row in components
            if row["moment_n"] == n and row["parity"] == "EVEN"
        )
        odd = sum(
            row["contribution_rank"]
            for row in components
            if row["moment_n"] == n and row["parity"] == "ODD"
        )
        require(even + odd == rank_rows[n - 2]["total_normalized_trace_rank"], f"component rank partition n={n}")
        rank_data.append((n, even, odd))
    controls = []
    for n, even_rank, odd_rank in rank_data:
        multiplier = Fraction(2, n)
        required_even = multiplier * even_rank
        required_odd = multiplier * odd_rank
        required_total = multiplier * (even_rank + odd_rank)
        restricted_even = multiplier * 2 * even_rank
        restricted_odd = multiplier * 2 * odd_rank
        restricted_total = multiplier * 2 * (even_rank + odd_rank)
        controls.append({
            "moment_n": n,
            "even_rank": even_rank,
            "odd_rank": odd_rank,
            "total_rank": even_rank + odd_rank,
            "required_K_multiplicity": record(multiplier),
            "required_even_rank": record(required_even),
            "required_odd_rank": record(required_odd),
            "required_total_rank": record(required_total),
            "even_rank_integral": required_even.denominator == 1,
            "odd_rank_integral": required_odd.denominator == 1,
            "total_rank_integral": required_total.denominator == 1,
            "ordinary_sectorwise_compatible_system_obstructed": (
                required_even.denominator != 1 or required_odd.denominator != 1
            ),
            "Res_K_to_Q_required_even_rank": record(restricted_even),
            "Res_K_to_Q_required_odd_rank": record(restricted_odd),
            "Res_K_to_Q_required_total_rank": record(restricted_total),
            "Res_K_to_Q_rank_obstructed": (
                restricted_even.denominator != 1
                or restricted_odd.denominator != 1
            ),
        })
    require(parse_record(controls[1]["required_even_rank"]) == Fraction(46, 3), "n3 even rank witness")
    require(parse_record(controls[1]["required_odd_rank"]) == Fraction(80, 3), "n3 odd rank witness")
    require(parse_record(controls[2]["required_total_rank"]) == Fraction(255, 2), "n4 total rank witness")
    require(parse_record(controls[1]["Res_K_to_Q_required_even_rank"]) == Fraction(92, 3), "n3 restricted even witness")
    require(controls[2]["Res_K_to_Q_rank_obstructed"] is False, "n4 restriction removes rank obstruction")
    return {
        "assumptions": "direct semisimple finite-rank systems over K preserving the same degree-one split-prime traces; no restriction-of-scalars or added Galois-conjugate counterpacket; Chebotarev trace rigidity and purity keep normalized weights 0 and 1 in separate sectors",
        "rank_principle": "an ordinary compatible-system direct-sum multiplicity and each pure-sector rank must be integral",
        "controls": controls,
        "n3_exact_witness": "even required rank=46/3 and odd required rank=80/3",
        "n4_exact_witness": "even required rank=87/2 and total required rank=255/2",
        "n3_direct_K_sectorwise_realization": "REFUTED_UNDER_STATED_CHEBOTAREV_PURITY_ASSUMPTIONS",
        "n3_after_Res_K_to_Q_rank_realization": "REFUTED_BY_92_OVER_3_AND_160_OVER_3",
        "n4_direct_K_sectorwise_square_root": "REFUTED_BY_EVEN_RANK_87_OVER_2",
        "n4_after_Res_K_to_Q_rank_realization": "NOT_EXCLUDED_BY_RANK_OR_HODGE_PARITY",
        "virtual_or_normalized_trace_realization_excluded": False,
    }


def expected_cleared_odd_skeleton() -> dict[str, Any]:
    ranks = {2: 8, 3: 40, 4: 168}
    statuses = {2: "PROVED_IN_C50", 3: "OPEN_EXPECTED_FROM_PURE_MOTIVE", 4: "OPEN_EXPECTED_FROM_PURE_MOTIVE"}
    controls = []
    for n in (2, 3, 4):
        source = Fraction(2, n)
        cleared = source * 6
        controls.append({
            "moment_n": n,
            "tower_index_j": 1,
            "normalized_weight_w": 1,
            "center_s": record(0),
            "source_K_exponent": record(source),
            "denominator_cleared_K_exponent": record(cleared),
            "odd_rank": ranks[n],
            "cleared_ordinary_rank": int(cleared * ranks[n]),
            "functional_equation_status": statuses[n],
        })
    require([parse_record(row["denominator_cleared_K_exponent"]) for row in controls] == [6, 4, 3], "cleared exponent list")
    return {
        "clearing_power": 6,
        "reason": "lcm of denominators of 2/n for n=2,3,4",
        "integral_exponents_12_over_n": [6, 4, 3],
        "controls": controls,
        "common_center": record(0),
        "alignment_scope": "odd normalized-weight leading clock j=1 only",
        "n2_FE_theorem": True,
        "n3_n4_FE_open": True,
        "full_denominator_tower_FE_claimed": False,
    }


def expected_hodge_gamma() -> dict[str, Any]:
    controls = [
        (2, "EVEN", 7, 0, [(0, 0, 7)], "Gamma_C(u)^7", "PROVED_IN_C50"),
        (2, "ODD", 8, 1, [(0, 1, 4), (1, 0, 4)], "Gamma_C(u)^8", "PROVED_IN_C50"),
        (3, "EVEN", 23, 0, [(-1, 1, 1), (0, 0, 21), (1, -1, 1)], "Gamma_C(u)^21*Gamma_C(u+1)^2", "OPEN_EXPECTED_FROM_PURE_MOTIVE"),
        (3, "ODD", 40, 1, [(0, 1, 20), (1, 0, 20)], "Gamma_C(u)^40", "OPEN_EXPECTED_FROM_PURE_MOTIVE"),
        (4, "EVEN", 87, 0, [(-1, 1, 8), (0, 0, 71), (1, -1, 8)], "Gamma_C(u)^71*Gamma_C(u+1)^16", "OPEN_EXPECTED_FROM_PURE_MOTIVE"),
        (4, "ODD", 168, 1, [(-1, 2, 1), (0, 1, 83), (1, 0, 83), (2, -1, 1)], "Gamma_C(u)^166*Gamma_C(u+1)^2", "OPEN_EXPECTED_FROM_PURE_MOTIVE"),
    ]
    rows = []
    for n, sector, rank, weight, hodge, gamma, status in controls:
        types = [{"p": p, "q": q, "multiplicity": multiplicity} for p, q, multiplicity in hodge]
        require(sum(item["multiplicity"] for item in types) == rank, f"Gamma rank n={n} {sector}")
        require(all(item["p"] + item["q"] == weight for item in types), f"Gamma weight n={n} {sector}")
        rows.append({
            "moment_n": n,
            "sector": sector,
            "rank": rank,
            "normalized_weight": weight,
            "normalized_Hodge_types": types,
            "expected_Gamma_C_factor": gamma,
            "functional_equation_status": status,
        })
    return {
        "leading_variable": "u=u_(n,1)=n*s+1",
        "Gamma_convention": "expected Gamma_C bookkeeping from normalized Hodge types",
        "sector_controls": rows,
        "n2_status": "THEOREM_LEVEL_COMPLETIONS",
        "n3_n4_status": "EXPECTED_CONDITIONAL_GAMMA_FACTORS_FE_OPEN",
        "full_Henon_archimedean_completion_constructed": False,
    }


def expected_hodge() -> dict[str, Any]:
    chi = hrr_chi_y_complete_intersection_23_P7()
    primitive_x = []
    for p in range(6):
        multiplicity = (chi[p] - (-1) ** p) * (-1) ** (5 - p)
        require(multiplicity >= 0, f"X Hodge p={p}")
        if multiplicity:
            primitive_x.append({"p": p, "q": 5 - p, "multiplicity": multiplicity})
    twisted_x = [{"p": row["p"] - 2, "q": row["q"] - 2, "multiplicity": row["multiplicity"]} for row in primitive_x]
    primitive_s = []
    for q in range(7):
        degree = 3 * q - 5
        multiplicity = comb(8, degree) if 0 <= degree <= 8 else 0
        if multiplicity:
            primitive_s.append({"p": 6 - q, "q": q, "Jacobian_ring_degree": degree, "multiplicity": multiplicity})
    primitive_s.sort(key=lambda row: (row["p"], row["q"]))
    twisted_s = [{"p": row["p"] - 3, "q": row["q"] - 3, "multiplicity": row["multiplicity"]} for row in primitive_s]
    require(sum(row["multiplicity"] for row in primitive_x) == 168, "X Hodge rank")
    require(sum(row["multiplicity"] for row in primitive_s) == 86, "S Hodge rank")
    return {
        "complete_intersection_X4": {
            "dimension": 5,
            "chi_y_convention": "chi_y=sum_pq (-1)^q*h^(p,q)*y^p",
            "chi_y_coefficients_low_to_high": chi,
            "primitive_middle_H5_before_twist": primitive_x,
            "primitive_middle_rank": 168,
            "after_Tate_twist_2": twisted_x,
            "normalized_weight": 1,
        },
        "cubic_S4": {
            "dimension": 6,
            "Jacobian_ring_Hilbert_series": "(1+z)^8",
            "primitive_middle_H6_before_twist": primitive_s,
            "primitive_middle_rank": 86,
            "after_Tate_twist_3": twisted_s,
            "normalized_weight": 0,
        },
        "Tate_Q0": {"Hodge_type": [0, 0], "rank": 1, "weight": 0},
        "total_rank": 255,
    }


def hrr_chi_y_complete_intersection_23_P7() -> list[int]:
    """Exact HRR coefficient expansion, independent of the frozen chi_y row.

    We evaluate the Hirzebruch class at y=0,...,5 with exact truncated
    power series and interpolate the degree-five chi_y polynomial.
    """
    order = 7

    def multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
        output = [Fraction(0)] * (order + 1)
        for i, a in enumerate(left):
            for j, b in enumerate(right):
                if i + j <= order:
                    output[i + j] += a * b
        return output

    def inverse(source: list[Fraction]) -> list[Fraction]:
        require(source[0] != 0, "HRR series inversion")
        output = [Fraction(0)] * (order + 1)
        output[0] = 1 / source[0]
        for k in range(1, order + 1):
            output[k] = -sum(
                source[j] * output[k - j] for j in range(1, k + 1)
            ) / source[0]
        return output

    def power(source: list[Fraction], exponent: int) -> list[Fraction]:
        output = [Fraction(1)] + [Fraction(0)] * order
        for _ in range(exponent):
            output = multiply(output, source)
        return output

    def exponential_minus(degree: int) -> list[Fraction]:
        return [Fraction((-degree) ** k, factorial(k)) for k in range(order + 1)]

    def genus_value(y_value: int) -> Fraction:
        y = Fraction(y_value)
        exp_one = exponential_minus(1)
        numerator = [
            (Fraction(1) if k == 0 else Fraction(0)) + y * exp_one[k]
            for k in range(order + 1)
        ]
        # (1-exp(-x))/x
        denominator = [Fraction((-1) ** k, factorial(k + 1)) for k in range(order + 1)]
        q_series = multiply(numerator, inverse(denominator))
        integrand = power(q_series, 8)
        for degree in (2, 3):
            exponential = exponential_minus(degree)
            top = [
                (Fraction(1) if k == 0 else Fraction(0)) - exponential[k]
                for k in range(order + 1)
            ]
            bottom = [
                (Fraction(1) if k == 0 else Fraction(0)) + y * exponential[k]
                for k in range(order + 1)
            ]
            integrand = multiply(integrand, multiply(top, inverse(bottom)))
        # Euler sequence: TP^7=O(1)^8-O, so divide by Q_y(0)=1+y.
        return integrand[7] / (1 + y)

    values = [genus_value(y) for y in range(6)]
    matrix = [
        [Fraction(i) ** degree for degree in range(6)] + [values[i]]
        for i in range(6)
    ]
    for column in range(6):
        pivot = next(row for row in range(column, 6) if matrix[row][column])
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        scale = matrix[column][column]
        matrix[column] = [value / scale for value in matrix[column]]
        for row in range(6):
            if row == column:
                continue
            scale = matrix[row][column]
            matrix[row] = [
                value - scale * pivot_value
                for value, pivot_value in zip(matrix[row], matrix[column])
            ]
    coefficients = [matrix[index][-1] for index in range(6)]
    require(all(value.denominator == 1 for value in coefficients), "HRR chi_y integrality")
    return [int(value) for value in coefficients]


def expected_payload(repository: Path) -> dict[str, Any]:
    locks, certificates = expected_sources(repository)
    components = expected_components()
    rank_rows = expected_rank_rows()
    center_rows, center_summary = expected_center_sections(components)
    return {
        "material_passport": {"candidate_id": "HCS-C51", "project_slug": "henon_mu3_weight_clock_bifurcation", "artifact_status": "RELEASE_CANDIDATE"},
        "source_lock": locks,
        "normalization_convention": {
            "norm_clock": "z_p=p^(-s)", "field_degree": "d_p=(p-1)/2 for split p",
            "normalized_moment": "c_p,n=C_p,n/d_p", "log_moment_term": "-c_p,n*p^(-n*s)/n",
            "trace_decomposition": "C_p,n=-2(e_p,n+o_p,n)",
            "denominator_tower": "1/(p-1)=sum_(j>=1)p^(-j)",
            "chronological_dynamics_preserved": True, "averaged_transition_matrix_used": False,
        },
        "trace_components": components,
        "exact_moment_theorem": {
            "n2": "C_p,2=-2*(7+a_C,p)",
            "n3": "C_p,3=-2*(21+(alpha_p-20p^2)/p^2+beta_p/p)=-2*(21+a_F,p/p+b_X,p)",
            "n4": "C_p,4=-2*(1+alpha_p/p^3+beta_p/p^2)",
            "uniform_form": "C_p,n=-2(e_p,n+o_p,n)",
            "normalized_weight_parity": "e has weight 0 and o has weight 1 componentwise",
        },
        "exact_prime_controls": expected_prime_rows(certificates),
        "rank_theorem": {
            "cubic_family": "S_n: smooth cubic hypersurface of dimension 2n-2 in P^(2n-1)",
            "complete_intersection_family": "X_n: smooth (2,3) complete intersection of dimension 2n-3 in P^(2n-1)",
            "cubic_Chern_series": "c(TS_n)=(1+H)^(2n)/(1+3H)",
            "complete_intersection_Chern_series": "c(TX_n)=(1+H)^(2n)/((1+2H)(1+3H))",
            "cubic_primitive_rank_formula": "b_prim(S_n)=(4^n+2)/3",
            "complete_intersection_middle_rank_formula": "b_mid(X_n)=(2*4^n-8)/3",
            "rank_with_Tate_Q0_formula": "1+b_prim(S_n)+b_mid(X_n)=4^n-1",
            "control_range": "2<=n<=20",
            "producer_algorithm": "truncated integral power-series division followed by Chern-Gauss-Bonnet and weak Lefschetz",
            "algebraic_formula_scope": "valid for smooth cubic S_n and smooth (2,3) complete intersection X_n",
            "actual_Henon_source_geometry_theorem_range": "n=2,3,4",
            "n5_to_n20_status": "SYMBOLIC_CHERN_FORMULA_CONDITIONAL_ON_SMOOTH_SOURCE_GEOMETRY",
        },
        "rank_controls_n2_to_n20": rank_rows,
        "center_bifurcation_theorem": center_summary,
        "center_tower_controls_j1_to_j4": center_rows,
        "tate_relabel_controls": expected_tate_rows(),
        "coefficient_field_exponents": expected_exponents(),
        "ordinary_compatible_system_obstruction": expected_ordinary_obstruction(components, rank_rows),
        "denominator_cleared_odd_skeleton": expected_cleared_odd_skeleton(),
        "Hodge_Gamma_sector_ledger": expected_hodge_gamma(),
        "n4_Hodge_ledger": expected_hodge(),
        "decisions": {
            "full_source_native_factorwise_affine_center": "REFUTED_BY_EXACT_N2_WITNESS",
            "odd_weight_j1_center_alignment": "PROVED_CENTER_S_ZERO",
            "odd_weight_full_denominator_tower_alignment": "REFUTED",
            "integral_Tate_relabel_can_repair_alignment": False,
            "consistent_half_weight_relabel_can_repair_alignment": False,
            "fixed_clock_half_weight_mutation_preserves_Henon_object": False,
            "n3_n4_fractional_L_powers_promoted_to_meromorphic_functions": False,
            "direct_K_ordinary_system_for_raw_n3_exponent": "REFUTED_UNDER_CHEBOTAREV_PURITY_SCOPE",
            "direct_K_ordinary_system_for_raw_n4_square_root": "REFUTED_UNDER_CHEBOTAREV_PURITY_SCOPE",
            "n4_Res_K_to_Q_realization": "NOT_EXCLUDED_BY_RANK_OR_HODGE_PARITY",
            "denominator_cleared_odd_j1_skeleton_integral": True,
        },
        "scope": {
            "no_go_scope": "source-native factorwise standard pure-motive functional-equation reflections",
            "n2_factor_functional_equations_theorem_level": True,
            "n3_n4_global_motivic_functional_equations_claimed": False,
            "residual_factor_functional_equation_claimed": False,
            "nonfactorwise_miracle_excluded": False,
            "full_Henon_functional_equation_claimed": False,
            "Riemann_hypothesis_claimed": False,
            "self_adjoint_Hilbert_Polya_operator_claimed": False,
            "half_Tate_object_adjoined": False,
            "rank_formula_for_smooth_models_claimed": True,
            "Henon_Xn_smoothness_claimed_for_n_greater_than_4": False,
            "ordinary_compatible_system_no_go_excludes_virtual_trace_categories": False,
        },
    }


def gate(name: str, check: Callable[[], Any]) -> dict[str, str]:
    try:
        check()
        return {"gate": name, "status": "PASS"}
    except Exception as error:
        return {"gate": name, "status": "FAIL", "diagnostic": type(error).__name__}


def audit_certificate(certificate: Any, repository: Path) -> tuple[list[dict[str, str]], bool]:
    expected = expected_payload(repository)
    payload = certificate.get("payload", {}) if type(certificate) is dict else {}
    gates = [
        gate("certificate_envelope", lambda: (
            require(type(certificate) is dict and set(certificate) == {"schema", "payload", "payload_sha256"}, "certificate keys"),
            require(certificate["schema"] == SCHEMA and type(certificate["schema"]) is str, "schema"),
            require(type(certificate["payload"]) is dict, "payload type"),
            require(type(certificate["payload_sha256"]) is str and len(certificate["payload_sha256"]) == 64, "digest type"),
            require(certificate["payload_sha256"] == hashlib.sha256(canonical_json(certificate["payload"])).hexdigest(), "self digest"),
        )),
        gate("frozen_full_payload", lambda: require(
            hashlib.sha256(canonical_json(payload)).hexdigest() == FROZEN_PAYLOAD_SHA256,
            "frozen payload digest",
        )),
        gate("recursive_exact_schema", lambda: require(same_recursive_shape(payload, expected), "recursive keys/types/list lengths")),
        gate("passport_and_sources", lambda: (
            require(strict_equal(payload["material_passport"], expected["material_passport"]), "passport"),
            require(strict_equal(payload["source_lock"], expected["source_lock"]), "sources"),
        )),
        gate("normalization_and_components", lambda: (
            require(strict_equal(payload["normalization_convention"], expected["normalization_convention"]), "normalization"),
            require(strict_equal(payload["trace_components"], expected["trace_components"]), "components"),
        )),
        gate("exact_moment_replay", lambda: (
            require(strict_equal(payload["exact_moment_theorem"], expected["exact_moment_theorem"]), "moment formulas"),
            require(strict_equal(payload["exact_prime_controls"], expected["exact_prime_controls"]), "eleven-prime replay"),
        )),
        gate("rank_Chern_generating", lambda: (
            require(strict_equal(payload["rank_theorem"], expected["rank_theorem"]), "rank theorem"),
            require(strict_equal(payload["rank_controls_n2_to_n20"], expected["rank_controls_n2_to_n20"]), "independent coefficient sums"),
        )),
        gate("center_tower", lambda: (
            require(strict_equal(payload["center_bifurcation_theorem"], expected["center_bifurcation_theorem"]), "center theorem"),
            require(strict_equal(payload["center_tower_controls_j1_to_j4"], expected["center_tower_controls_j1_to_j4"]), "center rows"),
        )),
        gate("Tate_and_half_weight", lambda: require(strict_equal(payload["tate_relabel_controls"], expected["tate_relabel_controls"]), "Tate controls")),
        gate("K_exponent_firewall", lambda: require(strict_equal(payload["coefficient_field_exponents"], expected["coefficient_field_exponents"]), "K exponent controls")),
        gate("ordinary_compatible_system", lambda: require(strict_equal(payload["ordinary_compatible_system_obstruction"], expected["ordinary_compatible_system_obstruction"]), "ordinary rank obstruction")),
        gate("cleared_odd_skeleton", lambda: require(strict_equal(payload["denominator_cleared_odd_skeleton"], expected["denominator_cleared_odd_skeleton"]), "cleared odd skeleton")),
        gate("Hodge_Gamma", lambda: require(strict_equal(payload["Hodge_Gamma_sector_ledger"], expected["Hodge_Gamma_sector_ledger"]), "Hodge/Gamma sectors")),
        gate("n4_Hodge", lambda: require(strict_equal(payload["n4_Hodge_ledger"], expected["n4_Hodge_ledger"]), "chi_y and Hodge reconstruction")),
        gate("decisions_and_scope", lambda: (
            require(strict_equal(payload["decisions"], expected["decisions"]), "decisions"),
            require(strict_equal(payload["scope"], expected["scope"]), "scope"),
        )),
    ]
    return gates, all(row["status"] == "PASS" for row in gates)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    arguments = parser.parse_args()
    repository = Path(__file__).resolve().parents[3]
    certificate = json.loads(arguments.certificate.read_text(encoding="utf-8"))
    gates, passed = audit_certificate(certificate, repository)
    report = {
        "schema": CHECK_SCHEMA,
        "certificate_sha256": digest(arguments.certificate),
        "gates": gates,
        "gate_summary": {"passed": sum(row["status"] == "PASS" for row in gates), "total": len(gates)},
        "overall": "PASS" if passed else "FAIL",
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{report['overall']} {report['gate_summary']['passed']}/{report['gate_summary']['total']}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
