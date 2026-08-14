#!/usr/bin/env python3
"""Produce the exact HCS-C51 weight/clock bifurcation certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any


SCHEMA = "hcs-c51-certificate-v1"
CANDIDATE_ID = "HCS-C51"
PROJECT_SLUG = "henon_mu3_weight_clock_bifurcation"
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


def canonical_json(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def fraction_record(value: Fraction | int) -> dict[str, int]:
    value = Fraction(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


def read_fraction(value: Any) -> Fraction:
    if type(value) is not dict or set(value) != {"numerator", "denominator"}:
        raise AssertionError("noncanonical fraction shape")
    if type(value["numerator"]) is not int or type(value["denominator"]) is not int:
        raise AssertionError("fraction leaves must be exact integers")
    result = Fraction(value["numerator"], value["denominator"])
    if fraction_record(result) != value:
        raise AssertionError("fraction must be reduced with positive denominator")
    return result


def source_bundle(repository: Path) -> tuple[list[dict[str, str]], dict[str, dict[str, Any]]]:
    locks: list[dict[str, str]] = []
    certificates: dict[str, dict[str, Any]] = {}
    for source, (relative, expected_hash) in SOURCE_HASHES.items():
        path = repository / relative
        actual_hash = sha256_file(path)
        if actual_hash != expected_hash:
            raise AssertionError(f"source-lock mismatch for {source}: {actual_hash}")
        certificate = json.loads(path.read_text(encoding="utf-8"))
        if type(certificate) is not dict or type(certificate.get("payload_sha256")) is not str:
            raise AssertionError(f"malformed source certificate {source}")
        locks.append({
            "source": source,
            "path": relative,
            "sha256": actual_hash,
            "schema": certificate["schema"],
            "payload_sha256": certificate["payload_sha256"],
        })
        certificates[source] = certificate
    return locks, certificates


COMPONENT_SPECS = (
    # n, id, parity, motive, W, t, multiplicity, rank, trace expression, status
    (2, "n2_tate", "EVEN", "Q(0)", 0, 0, 7, 1, "7", "C50_EXACT_FACTOR"),
    (2, "n2_curve_H1", "ODD", "H^1(C)", 1, 0, 1, 8, "a_C,p", "C50_EXACT_FACTOR"),
    (3, "n3_tate", "EVEN", "Q(0)", 0, 0, 21, 1, "21", "C49_EXACT_TRACE_TERM"),
    (3, "n3_fermat_Jacobi_rank2", "EVEN", "H^4_prim(S_3)_{non-Tate/Jacobi}(2)", 4, 2, 1, 2, "(alpha_p-20p^2)/p^2=a_F,p/p", "C49_EXACT_TRACE_TERM"),
    (3, "n3_fano_H3", "ODD", "H^3(X_3)(1)", 3, 1, 1, 40, "b_X,p=beta_p/p", "C49_EXACT_TRACE_TERM"),
    (4, "n4_tate", "EVEN", "Q(0)", 0, 0, 1, 1, "1", "C50_EXACT_TRACE_TERM"),
    (4, "n4_cubic_H6", "EVEN", "H^6_prim(S_4)(3)", 6, 3, 1, 86, "alpha_p/p^3", "C50_EXACT_TRACE_TERM"),
    (4, "n4_fivefold_H5", "ODD", "H^5(X_4)(2)", 5, 2, 1, 168, "beta_p/p^2", "C50_EXACT_TRACE_TERM"),
)


def trace_components() -> list[dict[str, Any]]:
    result = []
    for n, component_id, parity, motive, raw_weight, division, multiplicity, rank, expression, status in COMPONENT_SPECS:
        normalized_weight = raw_weight - 2 * division
        expected_parity = "ODD" if normalized_weight % 2 else "EVEN"
        if expected_parity != parity or normalized_weight not in (0, 1):
            raise AssertionError(f"weight/parity mismatch for {component_id}")
        result.append({
            "moment_n": n,
            "component_id": component_id,
            "parity": parity,
            "motive_after_source_twist": motive,
            "raw_weight_W": raw_weight,
            "source_p_division_t": division,
            "normalized_weight_w": normalized_weight,
            "multiplicity_in_e_plus_o": multiplicity,
            "base_motive_rank": rank,
            "contribution_rank": multiplicity * rank,
            "trace_expression_in_e_plus_o": expression,
            "status": status,
        })
    return result


def exact_prime_controls(certificates: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    rows2 = {
        row["prime"]: row
        for row in certificates["C48"]["payload"]["exact_controls"]
    }
    rows3 = {
        row["prime"]: row
        for row in certificates["C49"]["payload"]["exact_geometry_controls"]
    }
    rows4 = certificates["C50"]["payload"]["exact_fourth_moment_controls"]
    result: list[dict[str, Any]] = []
    for source4 in rows4:
        p = source4["p"]
        source2, source3 = rows2[p], rows3[p]
        d = Fraction(p - 1, 2)

        curve_trace = source2["frobenius_trace_a_p"]
        even2, odd2 = Fraction(7), Fraction(curve_trace)
        C2 = -2 * (even2 + odd2)
        c2 = C2 / d
        if C2 != Fraction(source2["galois_traced_second_moment_C_p_2"]):
            raise AssertionError(f"n=2 trace decomposition failed at p={p}")
        if c2 != read_fraction(source2["normalized_second_moment_c_p_2"]):
            raise AssertionError(f"n=2 normalization failed at p={p}")

        alpha3, beta3 = source3["alpha_p"], source3["beta_p"]
        if (alpha3 - 20 * p * p) % p or beta3 % p:
            raise AssertionError(f"n=3 integral trace extraction failed at p={p}")
        fermat_trace = Fraction(alpha3 - 20 * p * p, p)
        fermat_weight4_trace = alpha3 - 20 * p * p
        fano_trace = Fraction(beta3, p)
        even3 = Fraction(21) + fermat_trace / p
        odd3 = fano_trace
        C3 = -2 * (even3 + odd3)
        c3 = C3 / d
        if C3 != read_fraction(source3["galois_traced_third_moment_C_p_3"]):
            raise AssertionError(f"n=3 trace decomposition failed at p={p}")
        if c3 != read_fraction(source3["normalized_third_moment_c_p_3"]):
            raise AssertionError(f"n=3 normalization failed at p={p}")

        alpha4, beta4 = source4["alpha_p"], source4["beta_p"]
        even4 = Fraction(1) + Fraction(alpha4, p**3)
        odd4 = Fraction(beta4, p**2)
        C4 = -2 * (even4 + odd4)
        c4 = C4 / d
        if C4 != read_fraction(source4["C_p_4"]):
            raise AssertionError(f"n=4 trace decomposition failed at p={p}")
        if c4 != read_fraction(source4["c_p_4"]):
            raise AssertionError(f"n=4 normalization failed at p={p}")

        result.append({
            "p": p,
            "rho": source4["rho"],
            "real_cyclotomic_degree_d_p": int(d),
            "moments": {
                "n2": {
                    "even_trace_e_p_n": fraction_record(even2),
                    "odd_trace_o_p_n": fraction_record(odd2),
                    "C_p_n": fraction_record(C2),
                    "c_p_n": fraction_record(c2),
                    "C_equals_minus_2_times_e_plus_o": True,
                    "source_certificate_match": True,
                },
                "n3": {
                    "fermat_Jacobi_raw_weight4_trace": fermat_weight4_trace,
                    "fermat_Jacobi_weight2_quotient_a_F_p": fraction_record(fermat_trace),
                    "fano_raw_trace_b_X_p": fraction_record(fano_trace),
                    "even_trace_e_p_n": fraction_record(even3),
                    "odd_trace_o_p_n": fraction_record(odd3),
                    "C_p_n": fraction_record(C3),
                    "c_p_n": fraction_record(c3),
                    "C_equals_minus_2_times_e_plus_o": True,
                    "source_certificate_match": True,
                },
                "n4": {
                    "cubic_raw_trace_alpha_p": alpha4,
                    "fivefold_raw_trace_beta_p": beta4,
                    "even_trace_e_p_n": fraction_record(even4),
                    "odd_trace_o_p_n": fraction_record(odd4),
                    "C_p_n": fraction_record(C4),
                    "c_p_n": fraction_record(c4),
                    "C_equals_minus_2_times_e_plus_o": True,
                    "source_certificate_match": True,
                },
            },
        })
    if len(result) != 11:
        raise AssertionError("expected eleven common split-prime controls")
    return result


def truncated_series_division(
    numerator: list[int], denominator: list[int], degree: int
) -> list[int]:
    if not denominator or denominator[0] != 1:
        raise AssertionError("series denominator must be monic at H=0")
    quotient = [0] * (degree + 1)
    for k in range(degree + 1):
        source = numerator[k] if k < len(numerator) else 0
        quotient[k] = source - sum(
            denominator[j] * quotient[k - j]
            for j in range(1, min(k, len(denominator) - 1) + 1)
        )
    return quotient


def rank_controls() -> list[dict[str, Any]]:
    controls = []
    for n in range(2, 21):
        numerator = [comb(2 * n, k) for k in range(2 * n + 1)]
        cubic_dimension = 2 * n - 2
        complete_dimension = 2 * n - 3
        cubic_coefficient = truncated_series_division(
            numerator, [1, 3], cubic_dimension
        )[cubic_dimension]
        complete_coefficient = truncated_series_division(
            numerator, [1, 5, 6], complete_dimension
        )[complete_dimension]
        cubic_euler = 3 * cubic_coefficient
        complete_euler = 6 * complete_coefficient
        cubic_rank = cubic_euler - (cubic_dimension + 1)
        complete_rank = (complete_dimension + 1) - complete_euler
        formula_cubic = (4**n + 2) // 3
        formula_complete = (2 * 4**n - 8) // 3
        total = 1 + cubic_rank + complete_rank
        if (
            cubic_rank != formula_cubic
            or complete_rank != formula_complete
            or total != 4**n - 1
        ):
            raise AssertionError(f"rank identity failed at n={n}")
        controls.append({
            "n": n,
            "ambient_projective_dimension": 2 * n - 1,
            "cubic_dimension": cubic_dimension,
            "cubic_top_chern_coefficient": cubic_coefficient,
            "cubic_Euler_characteristic": cubic_euler,
            "cubic_primitive_middle_rank": cubic_rank,
            "complete_intersection_dimension": complete_dimension,
            "complete_intersection_top_chern_coefficient": complete_coefficient,
            "complete_intersection_Euler_characteristic": complete_euler,
            "complete_intersection_middle_rank": complete_rank,
            "Tate_rank": 1,
            "total_normalized_trace_rank": total,
            "source_geometry_status": (
                "HENON_CHAR0_GEOMETRY_LOCKED"
                if n <= 4
                else "CONDITIONAL_SYMBOLIC_SMOOTH_CI_CONTROL"
            ),
        })
    return controls


def center_tower_controls(components: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    controls: list[dict[str, Any]] = []
    for component in components:
        n = component["moment_n"]
        weight = component["normalized_weight_w"]
        for j in range(1, 5):
            reflection_constant = Fraction(weight + 1 - 2 * j, n)
            center = reflection_constant / 2
            controls.append({
                "component_id": component["component_id"],
                "moment_n": n,
                "normalized_weight_w": weight,
                "tower_index_j": j,
                "normalized_L_variable": {"slope": n, "intercept": j},
                "mapped_s_reflection": {
                    "s_coefficient": -1,
                    "constant": fraction_record(reflection_constant),
                },
                "mapped_s_center": fraction_record(center),
            })

    def centers(j: int, parity: str | None = None) -> list[dict[str, int]]:
        selected = set()
        parity_by_id = {row["component_id"]: row["parity"] for row in components}
        for row in controls:
            if row["tower_index_j"] != j:
                continue
            if parity is not None and parity_by_id[row["component_id"]] != parity:
                continue
            selected.add(read_fraction(row["mapped_s_center"]))
        return [fraction_record(value) for value in sorted(selected)]

    odd_by_j = {f"j{j}": centers(j, "ODD") for j in range(1, 5)}
    summary = {
        "tower_expansion": "1/(p-1)=sum_(j>=1) p^(-j)",
        "normalized_variable": "u_(n,j)=n*s+j",
        "mapped_center_formula": "center_s=((w+1)/2-j)/n",
        "j1_full_center_set": centers(1),
        "j1_odd_center_set": odd_by_j["j1"],
        "odd_center_sets_by_tower_index": odd_by_j,
        "odd_weight_alignment_holds_exactly_at_j1": odd_by_j["j1"] == [fraction_record(0)],
        "odd_weight_alignment_holds_for_full_tower": False,
        "full_source_native_affine_center_exists": False,
        "minimal_exact_witness": {
            "source": "C50 exact n=2 factorization",
            "factor_1": "zeta_K(2s+1)^7",
            "factor_1_center": fraction_record(Fraction(-1, 4)),
            "factor_2": "L(H^1(C/K),2s+1)",
            "factor_2_center": fraction_record(0),
            "factorwise_common_center_exists": False,
            "residual_H2_functional_equation_certified": False,
            "nonfactorwise_miracle_ruled_out": False,
        },
    }
    return controls, summary


def tate_relabel_controls() -> list[dict[str, Any]]:
    controls = []
    for n in range(2, 5):
        for weight in (0, 1):
            for j in range(1, 5):
                original_center = Fraction(weight + 1 - 2 * j, 2 * n)
                integer_checks = []
                for twist in range(-3, 4):
                    twisted_weight = weight - 2 * twist
                    twisted_intercept = j - twist
                    center = Fraction(
                        twisted_weight + 1 - 2 * twisted_intercept, 2 * n
                    )
                    integer_checks.append({
                        "twist_k": twist,
                        "twisted_weight": twisted_weight,
                        "twisted_variable_intercept": twisted_intercept,
                        "center": fraction_record(center),
                        "center_invariant": center == original_center,
                    })
                half_twist = Fraction(-1, 2)
                half_weight = Fraction(weight) - 2 * half_twist
                half_intercept = Fraction(j) - half_twist
                half_center = Fraction(
                    half_weight + 1 - 2 * half_intercept, 2 * n
                )
                if not all(row["center_invariant"] for row in integer_checks):
                    raise AssertionError("integral Tate relabel changed center")
                if half_center != original_center:
                    raise AssertionError("consistent half relabel changed center")
                controls.append({
                    "moment_n": n,
                    "normalized_weight_w": weight,
                    "tower_index_j": j,
                    "original_center": fraction_record(original_center),
                    "integral_twists": integer_checks,
                    "formal_half_twist": {
                        "twist_k": fraction_record(half_twist),
                        "twisted_weight": fraction_record(half_weight),
                        "consistent_variable_intercept": fraction_record(half_intercept),
                        "consistent_center": fraction_record(half_center),
                        "consistent_center_invariant": True,
                        "fixed_clock_local_coefficient_multiplier": "p^(1/2)",
                        "fixed_clock_preserves_source_moment": False,
                    },
                })
    return controls


def coefficient_field_exponents() -> list[dict[str, Any]]:
    result = []
    for n in range(2, 5):
        exponent = Fraction(2, n)
        result.append({
            "moment_n": n,
            "rational_split_prime_leading_log_multiplier_per_trace": fraction_record(Fraction(4, n)),
            "degree_one_K_primes_above_split_p": 2,
            "candidate_K_L_exponent_per_trace": fraction_record(exponent),
            "exponent_integral": exponent.denominator == 1,
            "ordinary_single_valued_meromorphic_L_power_certified": n == 2,
        })
    return result


def ordinary_compatible_system_obstruction(
    components: list[dict[str, Any]], rank_rows: list[dict[str, Any]]
) -> dict[str, Any]:
    ranks: dict[int, tuple[int, int]] = {}
    for n in range(2, 5):
        even_rank = sum(
            row["contribution_rank"]
            for row in components
            if row["moment_n"] == n and row["parity"] == "EVEN"
        )
        odd_rank = sum(
            row["contribution_rank"]
            for row in components
            if row["moment_n"] == n and row["parity"] == "ODD"
        )
        if even_rank + odd_rank != rank_rows[n - 2]["total_normalized_trace_rank"]:
            raise AssertionError("component/general-rank partition mismatch")
        ranks[n] = (even_rank, odd_rank)
    rows = []
    for n, (even_rank, odd_rank) in ranks.items():
        exponent = Fraction(2, n)
        required_even = exponent * even_rank
        required_odd = exponent * odd_rank
        required_total = exponent * (even_rank + odd_rank)
        restricted_even = exponent * 2 * even_rank
        restricted_odd = exponent * 2 * odd_rank
        restricted_total = exponent * 2 * (even_rank + odd_rank)
        rows.append({
            "moment_n": n,
            "even_rank": even_rank,
            "odd_rank": odd_rank,
            "total_rank": even_rank + odd_rank,
            "required_K_multiplicity": fraction_record(exponent),
            "required_even_rank": fraction_record(required_even),
            "required_odd_rank": fraction_record(required_odd),
            "required_total_rank": fraction_record(required_total),
            "even_rank_integral": required_even.denominator == 1,
            "odd_rank_integral": required_odd.denominator == 1,
            "total_rank_integral": required_total.denominator == 1,
            "ordinary_sectorwise_compatible_system_obstructed": (
                required_even.denominator != 1 or required_odd.denominator != 1
            ),
            "Res_K_to_Q_required_even_rank": fraction_record(restricted_even),
            "Res_K_to_Q_required_odd_rank": fraction_record(restricted_odd),
            "Res_K_to_Q_required_total_rank": fraction_record(restricted_total),
            "Res_K_to_Q_rank_obstructed": (
                restricted_even.denominator != 1
                or restricted_odd.denominator != 1
            ),
        })
    return {
        "assumptions": "direct semisimple finite-rank systems over K preserving the same degree-one split-prime traces; no restriction-of-scalars or added Galois-conjugate counterpacket; Chebotarev trace rigidity and purity keep normalized weights 0 and 1 in separate sectors",
        "rank_principle": "an ordinary compatible-system direct-sum multiplicity and each pure-sector rank must be integral",
        "controls": rows,
        "n3_exact_witness": "even required rank=46/3 and odd required rank=80/3",
        "n4_exact_witness": "even required rank=87/2 and total required rank=255/2",
        "n3_direct_K_sectorwise_realization": "REFUTED_UNDER_STATED_CHEBOTAREV_PURITY_ASSUMPTIONS",
        "n3_after_Res_K_to_Q_rank_realization": "REFUTED_BY_92_OVER_3_AND_160_OVER_3",
        "n4_direct_K_sectorwise_square_root": "REFUTED_BY_EVEN_RANK_87_OVER_2",
        "n4_after_Res_K_to_Q_rank_realization": "NOT_EXCLUDED_BY_RANK_OR_HODGE_PARITY",
        "virtual_or_normalized_trace_realization_excluded": False,
    }


def denominator_cleared_odd_skeleton() -> dict[str, Any]:
    odd_ranks = {2: 8, 3: 40, 4: 168}
    fe_status = {
        2: "PROVED_IN_C50",
        3: "OPEN_EXPECTED_FROM_PURE_MOTIVE",
        4: "OPEN_EXPECTED_FROM_PURE_MOTIVE",
    }
    rows = []
    for n in range(2, 5):
        source_exponent = Fraction(2, n)
        cleared_exponent = 6 * source_exponent
        rows.append({
            "moment_n": n,
            "tower_index_j": 1,
            "normalized_weight_w": 1,
            "center_s": fraction_record(0),
            "source_K_exponent": fraction_record(source_exponent),
            "denominator_cleared_K_exponent": fraction_record(cleared_exponent),
            "odd_rank": odd_ranks[n],
            "cleared_ordinary_rank": int(cleared_exponent * odd_ranks[n]),
            "functional_equation_status": fe_status[n],
        })
    return {
        "clearing_power": 6,
        "reason": "lcm of denominators of 2/n for n=2,3,4",
        "integral_exponents_12_over_n": [6, 4, 3],
        "controls": rows,
        "common_center": fraction_record(0),
        "alignment_scope": "odd normalized-weight leading clock j=1 only",
        "n2_FE_theorem": True,
        "n3_n4_FE_open": True,
        "full_denominator_tower_FE_claimed": False,
    }


def hodge_gamma_ledger() -> dict[str, Any]:
    rows = [
        {
            "moment_n": 2,
            "sector": "EVEN",
            "rank": 7,
            "normalized_weight": 0,
            "normalized_Hodge_types": [{"p": 0, "q": 0, "multiplicity": 7}],
            "expected_Gamma_C_factor": "Gamma_C(u)^7",
            "functional_equation_status": "PROVED_IN_C50",
        },
        {
            "moment_n": 2,
            "sector": "ODD",
            "rank": 8,
            "normalized_weight": 1,
            "normalized_Hodge_types": [
                {"p": 0, "q": 1, "multiplicity": 4},
                {"p": 1, "q": 0, "multiplicity": 4},
            ],
            "expected_Gamma_C_factor": "Gamma_C(u)^8",
            "functional_equation_status": "PROVED_IN_C50",
        },
        {
            "moment_n": 3,
            "sector": "EVEN",
            "rank": 23,
            "normalized_weight": 0,
            "normalized_Hodge_types": [
                {"p": -1, "q": 1, "multiplicity": 1},
                {"p": 0, "q": 0, "multiplicity": 21},
                {"p": 1, "q": -1, "multiplicity": 1},
            ],
            "expected_Gamma_C_factor": "Gamma_C(u)^21*Gamma_C(u+1)^2",
            "functional_equation_status": "OPEN_EXPECTED_FROM_PURE_MOTIVE",
        },
        {
            "moment_n": 3,
            "sector": "ODD",
            "rank": 40,
            "normalized_weight": 1,
            "normalized_Hodge_types": [
                {"p": 0, "q": 1, "multiplicity": 20},
                {"p": 1, "q": 0, "multiplicity": 20},
            ],
            "expected_Gamma_C_factor": "Gamma_C(u)^40",
            "functional_equation_status": "OPEN_EXPECTED_FROM_PURE_MOTIVE",
        },
        {
            "moment_n": 4,
            "sector": "EVEN",
            "rank": 87,
            "normalized_weight": 0,
            "normalized_Hodge_types": [
                {"p": -1, "q": 1, "multiplicity": 8},
                {"p": 0, "q": 0, "multiplicity": 71},
                {"p": 1, "q": -1, "multiplicity": 8},
            ],
            "expected_Gamma_C_factor": "Gamma_C(u)^71*Gamma_C(u+1)^16",
            "functional_equation_status": "OPEN_EXPECTED_FROM_PURE_MOTIVE",
        },
        {
            "moment_n": 4,
            "sector": "ODD",
            "rank": 168,
            "normalized_weight": 1,
            "normalized_Hodge_types": [
                {"p": -1, "q": 2, "multiplicity": 1},
                {"p": 0, "q": 1, "multiplicity": 83},
                {"p": 1, "q": 0, "multiplicity": 83},
                {"p": 2, "q": -1, "multiplicity": 1},
            ],
            "expected_Gamma_C_factor": "Gamma_C(u)^166*Gamma_C(u+1)^2",
            "functional_equation_status": "OPEN_EXPECTED_FROM_PURE_MOTIVE",
        },
    ]
    for row in rows:
        if sum(item["multiplicity"] for item in row["normalized_Hodge_types"]) != row["rank"]:
            raise AssertionError("Hodge/Gamma rank mismatch")
        if any(item["p"] + item["q"] != row["normalized_weight"] for item in row["normalized_Hodge_types"]):
            raise AssertionError("Hodge/Gamma weight mismatch")
    return {
        "leading_variable": "u=u_(n,1)=n*s+1",
        "Gamma_convention": "expected Gamma_C bookkeeping from normalized Hodge types",
        "sector_controls": rows,
        "n2_status": "THEOREM_LEVEL_COMPLETIONS",
        "n3_n4_status": "EXPECTED_CONDITIONAL_GAMMA_FACTORS_FE_OPEN",
        "full_Henon_archimedean_completion_constructed": False,
    }


def n4_hodge_ledger() -> dict[str, Any]:
    chi_y = [1, 0, -82, 82, 0, -1]
    dimension = 5
    primitive_x = []
    for p, coefficient in enumerate(chi_y):
        ambient = (-1) ** p
        sign = (-1) ** (dimension - p)
        multiplicity = (coefficient - ambient) // sign
        if ambient + sign * multiplicity != coefficient or multiplicity < 0:
            raise AssertionError("chi_y reconstruction failure")
        if multiplicity:
            primitive_x.append({"p": p, "q": dimension - p, "multiplicity": multiplicity})
    primitive_x.sort(key=lambda row: (row["p"], row["q"]))
    twisted_x = [
        {"p": row["p"] - 2, "q": row["q"] - 2, "multiplicity": row["multiplicity"]}
        for row in primitive_x
    ]
    if sum(row["multiplicity"] for row in primitive_x) != 168:
        raise AssertionError("X_4 middle Hodge rank failure")

    primitive_s = []
    for q in range(7):
        jacobian_degree = 3 * (q + 1) - 8
        multiplicity = comb(8, jacobian_degree) if 0 <= jacobian_degree <= 8 else 0
        if multiplicity:
            primitive_s.append({
                "p": 6 - q,
                "q": q,
                "Jacobian_ring_degree": jacobian_degree,
                "multiplicity": multiplicity,
            })
    primitive_s.sort(key=lambda row: (row["p"], row["q"]))
    twisted_s = [
        {"p": row["p"] - 3, "q": row["q"] - 3, "multiplicity": row["multiplicity"]}
        for row in primitive_s
    ]
    if sum(row["multiplicity"] for row in primitive_s) != 86:
        raise AssertionError("S_4 primitive Hodge rank failure")
    if 1 + 86 + 168 != 4**4 - 1:
        raise AssertionError("n=4 total Hodge rank failure")
    return {
        "complete_intersection_X4": {
            "dimension": 5,
            "chi_y_convention": "chi_y=sum_pq (-1)^q*h^(p,q)*y^p",
            "chi_y_coefficients_low_to_high": chi_y,
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


def build_payload(repository: Path) -> dict[str, Any]:
    locks, certificates = source_bundle(repository)
    components = trace_components()
    rank_rows = rank_controls()
    tower_controls, tower_summary = center_tower_controls(components)
    return {
        "material_passport": {
            "candidate_id": CANDIDATE_ID,
            "project_slug": PROJECT_SLUG,
            "artifact_status": "RELEASE_CANDIDATE",
        },
        "source_lock": locks,
        "normalization_convention": {
            "norm_clock": "z_p=p^(-s)",
            "field_degree": "d_p=(p-1)/2 for split p",
            "normalized_moment": "c_p,n=C_p,n/d_p",
            "log_moment_term": "-c_p,n*p^(-n*s)/n",
            "trace_decomposition": "C_p,n=-2(e_p,n+o_p,n)",
            "denominator_tower": "1/(p-1)=sum_(j>=1)p^(-j)",
            "chronological_dynamics_preserved": True,
            "averaged_transition_matrix_used": False,
        },
        "trace_components": components,
        "exact_moment_theorem": {
            "n2": "C_p,2=-2*(7+a_C,p)",
            "n3": "C_p,3=-2*(21+(alpha_p-20p^2)/p^2+beta_p/p)=-2*(21+a_F,p/p+b_X,p)",
            "n4": "C_p,4=-2*(1+alpha_p/p^3+beta_p/p^2)",
            "uniform_form": "C_p,n=-2(e_p,n+o_p,n)",
            "normalized_weight_parity": "e has weight 0 and o has weight 1 componentwise",
        },
        "exact_prime_controls": exact_prime_controls(certificates),
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
        "center_bifurcation_theorem": tower_summary,
        "center_tower_controls_j1_to_j4": tower_controls,
        "tate_relabel_controls": tate_relabel_controls(),
        "coefficient_field_exponents": {
            "derivation": "-c_p,n/n=4(e_p,n+o_p,n)/(n(p-1)); two split K-primes give exponent 2/n per trace",
            "controls": coefficient_field_exponents(),
            "n2_component_powers": {"zeta_K": fraction_record(7), "H1_curve": fraction_record(1)},
            "n3_component_powers": {"Tate_total": fraction_record(14), "Fermat_Jacobi_rank2_trace": fraction_record(Fraction(2, 3)), "Fano_trace": fraction_record(Fraction(2, 3))},
            "n4_component_powers": {"Tate_total": fraction_record(Fraction(1, 2)), "cubic_trace": fraction_record(Fraction(1, 2)), "fivefold_trace": fraction_record(Fraction(1, 2))},
            "fractional_power_firewall": "n=3,4 powers are coefficient bookkeeping, not certified ordinary meromorphic L-products",
        },
        "ordinary_compatible_system_obstruction": ordinary_compatible_system_obstruction(components, rank_rows),
        "denominator_cleared_odd_skeleton": denominator_cleared_odd_skeleton(),
        "Hodge_Gamma_sector_ledger": hodge_gamma_ledger(),
        "n4_Hodge_ledger": n4_hodge_ledger(),
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    arguments = parser.parse_args()
    repository = Path(__file__).resolve().parents[3]
    payload = build_payload(repository)
    certificate = {
        "schema": SCHEMA,
        "payload": payload,
        "payload_sha256": hashlib.sha256(canonical_json(payload)).hexdigest(),
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"wrote {arguments.output}")
    print(f"payload_sha256={certificate['payload_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
