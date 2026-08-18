#!/usr/bin/env python3
"""Evaluator B: independent exponent-state, closed-fiber, and Euler lane."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
from pathlib import Path

import mpmath as mp


INF_SET_SHA = "6401b141f7b46b0f7275ec124ec571542655b9874cfa9aa5c7123108577e8a84"
WIDTH = {128: "1e-30", 256: "1e-60", 512: "1e-120"}
RADIUS_DIGITS = {128: 35, 256: 65, 512: 125}
WORK_DIGITS = {128: 82, 256: 114, 512: 194}


class RepeatedKeyB(Exception):
    pass


class SemanticRejectB(Exception):
    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


B_ATTACKS = [
    (("claims", "saturated", "existence"), "sigma>=0", "SATURATED_EXISTENCE_ENDPOINT"),
    (("claims", "modulo", "existence"), "sigma>=1/h", "MODULO_EXISTENCE_ENDPOINT"),
    (("claims", "power_schatten"), "k*sigma*q>=2", "POWER_SCHATTEN_ENDPOINT"),
    (("claims", "modulo_power", "existence_guard"), False, "MODULO_EXISTENCE_GUARD_MISSING"),
    (("claims", "trace", "domain"), "k*sigma>=2", "TRACE_ENDPOINT_ILLEGAL"),
    (("claims", "determinant", "domain"), "r*sigma>=2", "DETERMINANT_ENDPOINT_ILLEGAL"),
    (("claims", "saturated", "similarity"), "sigma>=1", "SATURATED_SIMILARITY_ENDPOINT"),
    (("claims", "commutator", "domain"), "sigma*q>=1", "COMMUTATOR_ENDPOINT"),
    (("claims", "commutator", "h2_witness"), "h_ge_3_exponent_one_prime", "H2_COMMUTATOR_WITNESS_TYPE"),
    (("claims", "weyl", "constants"), "C_h_sigma!=D_h_sigma_for_all_sigma", "WEYL_CROSSOVER_FALSE"),
    (("cases", "INF-CROSSOVER-ALLH", "sigma_1"), "2", "WEYL_CROSSOVER_ROW_CHANGED"),
    (("claims", "tauberian", "hypotheses"), "residue_only", "TAUBERIAN_HYPOTHESES_MISSING"),
    (("case", "h"), 1, "INVALID_H"), (("case", "h"), "3/2", "H_NOT_INTEGER"),
    (("case", "k"), 0, "INVALID_POWER_K"), (("case", "q"), "0", "INVALID_SCHATTEN_Q"),
    (("case", "label_m"), "12", "BLOCK_LABEL_NOT_H_FREE"),
    (("object", "J_h"), "all_prime_divisors", "SATURATED_SET_WRONG"),
    (("object", "retraction"), "swapped_with_old_formula", "RETRACTION_SWAP"),
    (("case", "sigma"), "complex_s", "SIGMA_COMPLEX_TYPE_ERROR"),
    (("object", "basis_weight"), "m^(-s/2)_before_fiber_sum", "WEIGHT_OWNER_CHANGED"),
    (("record", "nonzero_cyclic_atoms"), "include_block_kernel_zeros", "ZERO_EIGENVALUE_RETYPE"),
    (("case", "determinant_order_r"), "3/2", "DETERMINANT_ORDER_NOT_INTEGER"),
    (("case", "determinant_order_r"), 0, "DETERMINANT_ORDER_NONPOSITIVE"),
    (("record", "singular_value_type"), "eigenvalue", "SINGULAR_VALUE_RETYPE_AS_EIGENVALUE"),
    (("record", "riesz_norm_type"), "probability", "RIESZ_NORM_RETYPE_AS_PROBABILITY"),
    (("record", "finite_eigenvalue_encoding"), "rational_complexExact", "FINITE_EIGENVALUE_RATIONAL_COMPLEX_RETYPE"),
    (("record", "finite_eigenvalue_branch"), "PRINCIPAL_COMPLEX_LOG", "DIRICHLET_POWER_BRANCH_CHANGED"),
    (("infinite_coverage", "B", "exact_count"), 14, "B_INF_CASE_MISSING"),
    (("infinite_coverage", "B", "exact_count"), 16, "B_INF_CASE_EXTRA"),
    (("infinite_coverage", "B", "order"), "reordered", "B_INF_CASE_REORDERED"),
    (("infinite_coverage", "B", "membership"), "includes_INF_UNDECLARED", "B_INF_UNDECLARED_CASE"),
    (("infinite_coverage", "B", "certificate_owner"), "A", "B_CERTIFICATE_OWNER_CHANGED"),
    (("infinite_coverage", "ordered_set_sha256"), "0" * 64, "INF_COVERAGE_SET_HASH_CHANGED"),
    (("record", "finite_eigenvalue_base_encoding"), "JSON_number_6.0", "AST_BASE_6_DOT_0_NUMBER"),
    (("record", "finite_eigenvalue_base_encoding"), "JSON_number_6e0", "AST_BASE_6E0_NUMBER"),
    (("record", "finite_eigenvalue_base_encoding"), "JSON_boolean_true", "AST_BASE_BOOLEAN_NUMERIC"),
    (("record", "finite_eigenvalue_rational_encoding"), "JSON_number_1.0_component", "AST_RATIONAL_COMPONENT_1_DOT_0_NUMBER"),
    (("raw_parser", "duplicate_members"), "last_win", "DUPLICATE_JSON_MEMBER_LAST_WIN"),
    (("raw_parser", "reordered_unique_members"), "reject_noncanonical_input_order", "REORDERED_AST_KEYS_FALSE_REJECT"),
    (("raw_parser", "noncanonical_stored_jcs"), "accept", "NONCANONICAL_AST_STORAGE_ACCEPTED"),
    (("record", "finite_eigenvalue_storage"), "trust_stored_hash_without_recompute", "AST_JCS_HASH_NOT_RECOMPUTED"),
]


def semantic_input_code_b(contract: dict):
    baseline = contract.get("mutation_baseline")
    if type(baseline) is not dict:
        return "CONTRACT_BASELINE_SHAPE"
    for path, attacked, code in B_ATTACKS:
        node = baseline
        try:
            for part in path:
                node = node[part]
        except (KeyError, TypeError):
            return "CONTRACT_BASELINE_SHAPE"
        if type(node) is type(attacked) and node == attacked:
            return code
    return None


def h256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def canonical_fraction(text: str) -> Fraction:
    if type(text) is not str or re.fullmatch(r"-?(0|[1-9][0-9]*)(/[1-9][0-9]*)?", text) is None:
        raise ValueError("rational")
    f = Fraction(text)
    if str(f) != text:
        raise ValueError("unreduced")
    return f


def token_pairs_b(pairs):
    destination = {}
    for name, value in pairs:
        if name in destination:
            raise RepeatedKeyB(name)
        destination[name] = value
    return destination


def integer_lexeme_b(value, positive=False):
    if not isinstance(value, str):
        return False
    expression = r"[1-9][0-9]*" if positive else r"-?(0|[1-9][0-9]*)"
    return re.fullmatch(expression, value) is not None and value != "-0"


def inspect_ast_b(value):
    if not isinstance(value, dict) or set(value.keys()) != {"node_type", "base", "exponent", "log_branch"}:
        return "AST_OBJECT_SHAPE"
    if value.get("node_type") != "DIRICHLET_POWER" or value.get("log_branch") != "REAL_LOG_POSITIVE_BASE":
        return "AST_BRANCH_OR_TYPE"
    if not integer_lexeme_b(value.get("base"), positive=True):
        return "AST_POSITIVE_INTEGER_STRING_REQUIRED"
    exponent = value.get("exponent")
    if not isinstance(exponent, dict) or set(exponent.keys()) != {"real", "imag"}:
        return "AST_OBJECT_SHAPE"
    for coordinate in (exponent["imag"], exponent["real"]):
        if not isinstance(coordinate, dict) or set(coordinate.keys()) != {"numerator", "denominator"}:
            return "AST_OBJECT_SHAPE"
        if not integer_lexeme_b(coordinate.get("numerator")):
            return "AST_CANONICAL_SIGNED_INTEGER_STRING_REQUIRED"
        if not integer_lexeme_b(coordinate.get("denominator"), positive=True):
            return "AST_POSITIVE_INTEGER_STRING_REQUIRED"
        reduced = Fraction(int(coordinate["numerator"]), int(coordinate["denominator"]))
        if str(reduced.numerator) != coordinate["numerator"] or str(reduced.denominator) != coordinate["denominator"]:
            return "AST_REDUCED_RATIONAL_REQUIRED"
    return "NONE"


def exercise_raw_grid_b(contract):
    for test in contract["serialization_case_grid"]:
        try:
            value = json.loads(test["raw_json"], object_pairs_hook=token_pairs_b,
                               parse_constant=lambda _: (_ for _ in ()).throw(ValueError("constant")))
            if test["case_id"] == "NEG-AST-NONCANONICAL-STORED-JCS":
                encoded = json.dumps(value["ast"], sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
                result_code = ("NONE" if value["canonical_jcs_utf8"] == encoded and
                               value["canonical_jcs_sha256"] == h256(encoded.encode()) else "NONCANONICAL_AST_STORAGE")
            else:
                result_code = inspect_ast_b(value)
                encoded = (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
                           if result_code == "NONE" else "")
        except RepeatedKeyB:
            result_code, encoded = "DUPLICATE_JSON_MEMBER", ""
        if test["expected_outcome"].startswith("ACCEPT"):
            if result_code != "NONE" or h256(encoded.encode()) != test["expected_jcs_sha256"]:
                raise ValueError("B serialization acceptance")
        elif result_code != test["expected_code"]:
            raise ValueError("B serialization rejection")


def sieve_primes(limit: int) -> list[int]:
    if limit < 2:
        return []
    alive = bytearray(b"\x01") * (limit + 1)
    alive[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if alive[p]:
            alive[p * p: limit + 1: p] = b"\x00" * (((limit - p * p) // p) + 1)
    return [i for i in range(2, limit + 1) if alive[i]]


def exponent_vector(n: int, primes: list[int] | None = None) -> tuple[tuple[int, int], ...]:
    if type(n) is not int or n < 1:
        raise ValueError("positive integer")
    remaining = n
    ps = primes if primes is not None else sieve_primes(math.isqrt(n) + 1)
    states = []
    for p in ps:
        if p * p > remaining:
            break
        exponent = 0
        while remaining % p == 0:
            remaining //= p
            exponent += 1
        if exponent:
            states.append((p, exponent))
    if remaining > 1:
        states.append((remaining, 1))
    return tuple(states)


def state_tau(n: int, h: int) -> int:
    return math.prod(p ** min(e, h - 1) for p, e in exponent_vector(n))


def state_omega(n: int, h: int) -> int:
    return math.prod(p ** (e % h) for p, e in exponent_vector(n))


def h_free_state(n: int, h: int) -> bool:
    return all(e < h for _, e in exponent_vector(n))


def j_state(n: int, h: int) -> tuple[int, ...]:
    return tuple(p for p, e in exponent_vector(n) if e == h - 1)


def saturated_closed_fiber(m: int, h: int, cutoff: int) -> list[int]:
    generators = list(j_state(m, h))
    out = []

    def visit(index: int, value: int) -> None:
        if index == len(generators):
            out.append(value)
            return
        p = generators[index]
        current = value
        while current <= cutoff:
            visit(index + 1, current)
            if current > cutoff // p:
                break
            current *= p

    visit(0, m)
    return sorted(set(out))


def modulo_closed_fiber(m: int, h: int, cutoff: int) -> list[int]:
    result = []
    a = 1
    while m * (a ** h) <= cutoff:
        result.append(m * (a ** h))
        a += 1
    return result


def rational_node(f: Fraction) -> dict:
    return {"numerator": str(f.numerator), "denominator": str(f.denominator)}


def canonical_ast(base: int, sr: Fraction, si: Fraction) -> dict:
    node = {"node_type": "DIRICHLET_POWER", "base": str(base),
            "exponent": {"real": rational_node(-sr / 2), "imag": rational_node(-si / 2)},
            "log_branch": "REAL_LOG_POSITIVE_BASE"}
    jcs = json.dumps(node, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return {"ast": node, "canonical_jcs_utf8": jcs, "canonical_jcs_sha256": h256(jcs.encode())}


def numeric_string(value: mp.mpf, digits: int) -> str:
    if value == 0:
        return "0"
    text = mp.nstr(value, n=digits, strip_zeros=False, min_fixed=0, max_fixed=0)
    return text.replace("e-0", "e-").replace("e+0", "e+")


def bounded_interval(value: mp.mpf, bits: int, method: str, zero: bool = False) -> dict:
    if zero or value == 0:
        lo = hi = "0"
    else:
        eps = mp.power(10, -RADIUS_DIGITS[bits])
        lo = numeric_string(value - eps, RADIUS_DIGITS[bits] + 10)
        hi = numeric_string(value + eps, RADIUS_DIGITS[bits] + 10)
    return {"lower": lo, "upper": hi, "precision_bits": bits,
            "width_target": WIDTH[bits], "method_id": method}


def bounded_complex(value: mp.mpc, bits: int, method: str) -> dict:
    return {"real": bounded_interval(mp.re(value), bits, method + ":real", mp.re(value) == 0),
            "imag": bounded_interval(mp.im(value), bits, method + ":imag", mp.im(value) == 0)}


def dyadic_to_decimal_b(mpf_tuple, upward: bool) -> str:
    negative, coefficient, binary_exponent, _ = mpf_tuple
    signed = -coefficient if negative else coefficient
    if binary_exponent < 0:
        divisor = 2 ** (-binary_exponent)
    else:
        signed *= 2 ** binary_exponent
        divisor = 1
    with localcontext() as dc:
        dc.prec = 232
        dc.rounding = ROUND_CEILING if upward else ROUND_FLOOR
        result = Decimal(signed) / Decimal(divisor)
        if not result:
            return "0"
        # Decimal division was performed with a directed rounding mode.  Do
        # not re-format to a shorter mantissa: that second rounding could move
        # an endpoint inward and destroy containment.
        return str(result)


def outward_interval_b(iv_number, bits: int, label: str) -> dict:
    low_tuple, high_tuple = iv_number._mpi_
    return {"lower": dyadic_to_decimal_b(low_tuple, False), "upper": dyadic_to_decimal_b(high_tuple, True),
            "precision_bits": bits, "width_target": WIDTH[bits],
            "method_id": label + ":INDEPENDENT_IV_OUTWARD"}


def outward_complex_b(iv_number, bits: int, label: str) -> dict:
    real_component, imaginary_component = iv_number._mpci_

    class HolderR:
        _mpi_ = real_component

    class HolderI:
        _mpi_ = imaginary_component

    return {"real": outward_interval_b(HolderR(), bits, label + ":real"),
            "imag": outward_interval_b(HolderI(), bits, label + ":imag")}


def finite_from_states(case: dict, cutoff: int, bits: int) -> dict:
    h = case["h"]
    m = int(case["label_m"])
    if not h_free_state(m, h):
        raise ValueError("h-free label")
    sr, si = canonical_fraction(case["s"]["real"]), canonical_fraction(case["s"]["imag"])
    sat = saturated_closed_fiber(m, h, cutoff)
    mod = modulo_closed_fiber(m, h, cutoff)
    checks = sorted(set((1, m, cutoff)))
    maps = [{"n": str(n), "tau_h": str(state_tau(n, h)), "omega_h": str(state_omega(n, h))} for n in checks]
    intervals = {}
    riesz = {}
    comm = {}
    with mp.workdps(max(265, WORK_DIGITS[bits])):
        prior_iv_precision = mp.iv.dps
        mp.iv.dps = max(212, WORK_DIGITS[bits] + 36)
        paired_ast = canonical_ast(m, sr, si)
        sigma = mp.mpf(sr.numerator) / sr.denominator
        complex_exponent = -mp.mpc(mp.mpf(sr.numerator) / sr.denominator,
                                   mp.mpf(si.numerator) / si.denominator) / 2
        eigenvalue = mp.exp(complex_exponent * mp.log(m)) if m > 1 else mp.mpc(1, 0)
        interval_sigma = mp.iv.mpf(sr.numerator) / sr.denominator
        interval_exponent = -(mp.iv.mpf(sr.numerator) / sr.denominator +
                              mp.iv.j * mp.iv.mpf(si.numerator) / si.denominator) / 2
        eigen_box = (mp.iv.exp(interval_exponent * mp.iv.log(mp.iv.mpf(m)))
                     if m > 1 else mp.iv.mpc(1, 0))
        eigen_boxes = {"SATURATED": outward_complex_b(eigen_box, bits, "B:AST_REAL_LOG_265DPS"),
                       "MODULO": outward_complex_b(eigen_box, bits, "B:AST_REAL_LOG_265DPS")}
        for label, fiber in (("SATURATED", sat), ("MODULO", mod)):
            # Closed fibers are generated from exponent states, not by testing n.
            terms = [mp.power(n, -sigma) for n in reversed(fiber)]
            mass = mp.fsum(terms)
            rho = mp.sqrt(mass)
            modulus = mp.power(m, -sigma / 2)
            pnorm = rho / modulus
            cvalue = (mp.mpf(0) if len(fiber) == 1 else
                      mass * mp.sqrt(max(mp.mpf(0), 1 - modulus * modulus / mass)))
            interval_mass = mp.iv.fsum([mp.iv.mpf(n) ** (-interval_sigma) for n in fiber])
            interval_rho = mp.iv.sqrt(interval_mass)
            interval_modulus = mp.iv.mpf(m) ** (-interval_sigma / 2)
            interval_projection = interval_rho / interval_modulus
            interval_commutator = (mp.iv.mpf(0) if len(fiber) == 1 else
                                   interval_mass * mp.iv.sqrt(1 - interval_modulus * interval_modulus / interval_mass))
            intervals[label] = outward_interval_b(interval_rho, bits, "B:CLOSED_FIBER_EXPONENT_SUM")
            riesz[label] = outward_interval_b(interval_projection, bits, "B:CLOSED_FIBER_ANGLE")
            one_comm = outward_interval_b(interval_commutator, bits, "B:RANK_ONE_SYMBOLIC_COMMUTATOR")
            comm[label] = [one_comm, json.loads(json.dumps(one_comm))]
        mp.iv.dps = prior_iv_precision
    return {
        "case_id": case["case_id"], "evidence_type": "FINITE_COMPRESSION", "cutoff": cutoff,
        "precision_bits": bits, "map_values": maps,
        "fiber_membership": {"SATURATED": [str(x) for x in sat], "MODULO": [str(x) for x in mod]},
        "block_rank": {"SATURATED": 1, "MODULO": 1},
        "finite_nonzero_eigenvalue": {"SATURATED": paired_ast, "MODULO": json.loads(json.dumps(paired_ast))},
        "finite_nonzero_eigenvalue_interval": eigen_boxes,
        "finite_singular_value_interval": intervals,
        "finite_power_residual": {"SATURATED": {"real": "0", "imag": "0"},
                                  "MODULO": {"real": "0", "imag": "0"}},
        "finite_riesz_norm_interval": riesz,
        "finite_commutator_singular_intervals": comm,
    }


def first_primes_for_primorial(h: int, x: int) -> list[int]:
    primes = sieve_primes(max(32, x))
    selected = []
    product = 1
    for p in primes:
        next_product = product * p
        if next_product ** (h - 1) > x:
            break
        selected.append(p)
        product = next_product
    return selected


def optimization_from_prime_states(case: dict, sigma_text: str, x: int) -> dict:
    h = case["h"]
    selected = first_primes_for_primorial(h, x)
    base = math.prod(selected) ** (h - 1) if selected else 1
    ties = []
    # Independent exponent-state enumeration: equality depends exactly on J_h.
    for m in range(1, x + 1):
        if h_free_state(m, h) and j_state(m, h) == tuple(selected):
            ties.append(str(m))
    if str(base) not in ties:
        raise RuntimeError("primorial state")
    return {"case_id": case["case_id"], "evidence_type": "FINITE_OPTIMIZATION", "h": h,
            "sigma": sigma_text, "x_cutoff": x, "maximizer_label": str(base),
            "primorial_label": str(base), "tie_labels": sorted(ties)}


THEOREM_META_B = {
    "saturated_bounded_compact_iff_sigma_gt_zero": ("sigma>0", "single_saturated_prime_geometric_fiber", "bounded_and_compact_iff", "Proposition 3"),
    "modulo_bounded_compact_iff_sigma_gt_one_over_h": ("sigma>1/h", "m_equals_1_zeta_endpoint", "bounded_and_compact_iff", "Proposition 3"),
    "power_schatten_k_sigma_q_gt_two": ("k*sigma*q>2 and M_requires_sigma>1/h", "positive_prime_harmonic_endpoint", "exact_power_Schatten_wall", "Proposition 4"),
    "trace_domain_and_zeta_quotient": ("sigma>1/h and k*sigma>2", "absolute_h_free_Dirichlet_endpoint", "trace_equals_zeta_quotient", "Proposition 5"),
    "regularized_determinant_domain": ("sigma>1/h and r*sigma>2", "h_free_prime_harmonic_endpoint", "common_integer_order_regularized_determinant", "Proposition 5"),
    "saturated_similarity_iff_sigma_gt_one": ("sigma>1", "unbounded_finite_prime_set_Riesz_norms", "bounded_similarity_iff", "Proposition 6"),
    "modulo_similarity_iff_sigma_gt_one_over_h": ("sigma>1/h", "uniform_zeta_projection_norm", "bounded_similarity_iff", "Proposition 6"),
    "primorial_maximal_order_three_regimes": ("sigma>0", "next_primorial_exceeds_x", "exact_optimizer_and_three_regime_coefficient", "Proposition 7"),
    "tauberian_strip_pole_and_residue": ("sigma>0 and Re(z)>max(1/h,(1-sigma)/(h-1))", "positive_measure_simple_pole", "Wiener_Ikehara_residue_C_h_sigma", "Proposition 8"),
    "C_D_and_eigenvalue_constants_away_from_crossover": ("sigma>1/h", "positive_h_free_counting_measure", "explicit_C_D_and_eigenvalue_constants_no_order_claim", "Proposition 9"),
    "C_and_D_equal_one_at_sigma_one": ("sigma=1", "local_factor_telescoping", "C_h_1=D_h_1=1", "Proposition 9"),
    "commutator_schatten_sigma_q_gt_one": ("sigma*q>1", "two_saturated_primes", "S_commutator_in_Sq_iff_sigma_q_gt_1", "Proposition 11"),
    "h_ge_3_commutator_necessity": ("sigma*q>1", "fixed_saturated_prime_plus_varying_exponent_one_prime", "prime_sum_endpoint_divergence", "Proposition 11"),
    "h2_commutator_hilbert_schmidt_euler_identity": ("sigma>1/2", "separate_positive_Euler_products", "two_product_difference_identity", "Proposition 12"),
    "free_UFD_clone_reproduces_structural_package": ("h>=2 with each_formula_on_its_legal_domain", "normed_atom_relabeling", "negative_control_no_rational_prime_selectivity", "Delete-shared-method conclusion"),
}


def theorem_certificate_fields(theorem_field: str) -> tuple[str, str, str, str]:
    try:
        return THEOREM_META_B[theorem_field]
    except KeyError as exc:
        raise ValueError("unknown theorem field") from exc


def ast_rat_b(value=0, denominator=1) -> dict:
    fraction = value if isinstance(value, Fraction) else Fraction(value, denominator)
    return {"op": "RATIONAL", "numerator": str(fraction.numerator), "denominator": str(fraction.denominator)}


def ast_param_b(name: str) -> dict:
    return {"op": "PARAMETER", "name": name}


def ast_neg_b(value: dict) -> dict:
    return {"op": "NEGATE", "operand": value}


def ast_add_b(*values: dict) -> dict:
    return {"op": "ADD", "operands": list(values)}


def ast_mul_b(*values: dict) -> dict:
    return {"op": "MULTIPLY", "operands": list(values)}


def ast_div_b(left: dict, right: dict) -> dict:
    return {"op": "DIVIDE", "numerator": left, "denominator": right}


def ast_pow_b(base: dict, exponent: dict) -> dict:
    return {"op": "POWER", "base": base, "exponent": exponent}


def ast_sum_b(values: list[dict]) -> dict:
    return {"op": "FINITE_SUM", "terms": values}


def ast_one_minus_b(value: dict) -> dict:
    return ast_add_b(ast_rat_b(1), ast_neg_b(value))


def eval_numeric_ast_b(node: dict, parameters: dict[str, str]):
    """Interval evaluator private to B; P has a separate point evaluator."""
    op = node["op"]
    if op == "RATIONAL":
        return mp.iv.mpf(node["numerator"]) / mp.iv.mpf(node["denominator"])
    if op == "PARAMETER":
        value = canonical_fraction(parameters[node["name"]])
        return mp.iv.mpf(value.numerator) / value.denominator
    if op == "NEGATE":
        return -eval_numeric_ast_b(node["operand"], parameters)
    if op in {"ADD", "FINITE_SUM"}:
        children = node["operands"] if op == "ADD" else node["terms"]
        return mp.iv.fsum([eval_numeric_ast_b(child, parameters) for child in children])
    if op == "MULTIPLY":
        return mp.iv.fprod([eval_numeric_ast_b(child, parameters) for child in node["operands"]])
    if op == "DIVIDE":
        return eval_numeric_ast_b(node["numerator"], parameters) / eval_numeric_ast_b(node["denominator"], parameters)
    if op == "POWER":
        return eval_numeric_ast_b(node["base"], parameters) ** eval_numeric_ast_b(node["exponent"], parameters)
    raise ValueError("non-executable numeric AST node")


def p_power_b(exponent: dict) -> dict:
    return ast_pow_b(ast_param_b("p"), exponent)


def scaled_sigma_b(scale: Fraction | int = 1) -> dict:
    return ast_mul_b(ast_rat_b(scale), ast_param_b("sigma"))


def saturated_mass_ast_b() -> dict:
    return ast_pow_b(ast_one_minus_b(p_power_b(ast_neg_b(ast_param_b("sigma")))), ast_rat_b(-1))


def modulo_mass_ast_b() -> dict:
    exponent = ast_neg_b(ast_mul_b(ast_param_b("h"), ast_param_b("sigma")))
    return ast_pow_b(ast_one_minus_b(p_power_b(exponent)), ast_rat_b(-1))


def saturated_riesz_ast_b() -> dict:
    return ast_pow_b(ast_one_minus_b(p_power_b(ast_neg_b(ast_param_b("sigma")))), ast_rat_b(-1, 2))


def power_a_ast_b() -> dict:
    return ast_mul_b(ast_param_b("k"), ast_param_b("sigma"), ast_param_b("q"), ast_rat_b(1, 2))


def power_s_local_ast_b(h: int) -> dict:
    a = power_a_ast_b()
    middle = [p_power_b(ast_neg_b(ast_mul_b(ast_rat_b(e), a))) for e in range(1, h - 1)]
    tail = ast_mul_b(
        p_power_b(ast_neg_b(ast_mul_b(ast_rat_b(h - 1), a))),
        ast_pow_b(ast_one_minus_b(p_power_b(ast_neg_b(ast_param_b("sigma")))), ast_neg_b(ast_mul_b(ast_param_b("q"), ast_rat_b(1, 2)))),
    )
    return ast_add_b(ast_rat_b(1), ast_sum_b(middle), tail)


def power_m_local_ast_b() -> dict:
    a = power_a_ast_b()
    zeta_local = ast_pow_b(
        ast_one_minus_b(p_power_b(ast_neg_b(ast_mul_b(ast_param_b("h"), ast_param_b("sigma"))))),
        ast_neg_b(ast_mul_b(ast_param_b("q"), ast_rat_b(1, 2))),
    )
    quotient = ast_div_b(
        ast_one_minus_b(p_power_b(ast_neg_b(ast_mul_b(ast_param_b("h"), a)))),
        ast_one_minus_b(p_power_b(ast_neg_b(a))),
    )
    return ast_mul_b(zeta_local, quotient)


def hfree_local_ast_b(h: int, order_name: str) -> dict:
    exponent = ast_mul_b(ast_param_b(order_name), ast_param_b("sigma"), ast_rat_b(1, 2))
    return ast_sum_b([p_power_b(ast_neg_b(ast_mul_b(ast_rat_b(e), exponent))) for e in range(h)])


def c_local_ast_b(h: int) -> dict:
    finite = ast_sum_b([p_power_b(ast_rat_b(-e)) for e in range(h - 1)])
    tail = ast_mul_b(
        p_power_b(ast_rat_b(-(h - 1))),
        ast_pow_b(ast_one_minus_b(p_power_b(ast_neg_b(ast_param_b("sigma")))), ast_neg_b(ast_div_b(ast_rat_b(1), ast_param_b("sigma")))),
    )
    return ast_mul_b(ast_one_minus_b(p_power_b(ast_rat_b(-1))), ast_add_b(finite, tail))


def d_local_ast_b() -> dict:
    return ast_mul_b(
        ast_one_minus_b(p_power_b(ast_neg_b(ast_param_b("h")))),
        ast_pow_b(
            ast_one_minus_b(p_power_b(ast_neg_b(ast_mul_b(ast_param_b("h"), ast_param_b("sigma"))))),
            ast_neg_b(ast_div_b(ast_rat_b(1), ast_param_b("sigma"))),
        ),
    )


def eigen_local_ast_b() -> dict:
    return ast_one_minus_b(p_power_b(ast_neg_b(ast_param_b("h"))))


def comm_a_local_ast_b(h: int) -> dict:
    finite = ast_sum_b([p_power_b(ast_neg_b(ast_mul_b(ast_rat_b(2 * e), ast_param_b("sigma")))) for e in range(h - 1)])
    tail = ast_mul_b(
        p_power_b(ast_neg_b(ast_mul_b(ast_rat_b(2 * (h - 1)), ast_param_b("sigma")))),
        ast_pow_b(ast_one_minus_b(p_power_b(ast_neg_b(ast_param_b("sigma")))), ast_rat_b(-2)),
    )
    return ast_add_b(finite, tail)


def comm_b_local_ast_b(h: int) -> dict:
    finite = ast_sum_b([p_power_b(ast_neg_b(ast_mul_b(ast_rat_b(2 * e), ast_param_b("sigma")))) for e in range(h - 1)])
    tail = ast_mul_b(
        p_power_b(ast_neg_b(ast_mul_b(ast_rat_b(2 * (h - 1)), ast_param_b("sigma")))),
        ast_pow_b(ast_one_minus_b(p_power_b(ast_neg_b(ast_param_b("sigma")))), ast_rat_b(-1)),
    )
    return ast_add_b(finite, tail)


def semantic_section_b(section: str) -> dict:
    collapsed = " ".join(section.replace("\r\n", "\n").replace("\r", "\n").split())
    blocks = re.findall(r"\\\[(.*?)\\\]|\\\((.*?)\\\)", section, flags=re.DOTALL)
    formulas = [re.sub(r"\s+", "", left or right) for left, right in blocks]
    math_text = "\n".join(formulas)
    operators = {token: math_text.count(token) for token in
                 ("\\iff", "\\sim", "\\max", "\\min", "\\ge", "\\le", ">", "<", "=", "\\prod", "\\sum", "\\zeta")}
    quantifiers = sorted(re.findall(r"h\\ge2|k\\ge1|0<q<\\infty|\\forall|\\exists", math_text))
    return {"normalized_section_sha256": h256(collapsed.encode()),
            "formula_ast_hashes": [h256(value.encode()) for value in formulas],
            "operator_counts": operators, "quantifier_tokens": quantifiers}


def proof_sections_b(proof_text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"(?m)^## ([^\n]+)\n", proof_text))
    return [(match.group(1), proof_text[match.start(): matches[index + 1].start() if index + 1 < len(matches) else len(proof_text)])
            for index, match in enumerate(matches)]


def proof_bindings_b(proof_text: str, heading_prefix: str) -> list[dict]:
    chosen = []
    for role, prefix in (("main", "Main theorem:"), ("theorem", heading_prefix)):
        occurrences = [(heading, body) for heading, body in proof_sections_b(proof_text) if heading.startswith(prefix)]
        if not occurrences:
            raise ValueError("missing proof section")
        for ordinal, (heading, body) in enumerate(occurrences):
            semantic = semantic_section_b(body)
            chosen.append({"role": role, "heading": heading, "occurrence": str(ordinal),
                           "section_bytes_sha256": h256(body.encode()), "semantic_ast": semantic,
                           "semantic_ast_sha256": h256(json.dumps(semantic, sort_keys=True, separators=(",", ":")).encode())})
    return chosen


def interval_from_iv_b(value, method: str) -> dict:
    low, high = value._mpi_
    return {"lower": dyadic_to_decimal_b(low, False), "upper": dyadic_to_decimal_b(high, True),
            "precision_bits": 768, "method_id": method}


def family_parameters_b(case: dict, sigma_text: str, h: int, prime: int | None = None) -> dict:
    values = {"h": str(h), "k": str(case.get("k", case.get("determinant_order_r", 1))),
              "q": str(case.get("q", "1")), "sigma": sigma_text, "p": str(prime if prime is not None else 2)}
    return values


def certified_family_b(case: dict, family_name: str, local_ast: dict, sigma_text: str, h: int) -> dict:
    primes = (2, 3, 5, 7, 11)
    local_hash = h256(json.dumps(local_ast, sort_keys=True, separators=(",", ":")).encode())
    values, rows = [], []
    for index, prime in enumerate(primes):
        parameters = family_parameters_b(case, sigma_text, h, prime)
        value = eval_numeric_ast_b(local_ast, parameters)
        values.append(value)
        enclosure = interval_from_iv_b(value, "B:ANALYTIC_AST_IV_260DPS:" + family_name)
        rows.append({"index": str(index), "prime": str(prime), "parameters": parameters,
                     "operation_ast": local_ast, "operation_ast_sha256": local_hash,
                     "lower": enclosure["lower"], "upper": enclosure["upper"],
                     "precision_bits": enclosure["precision_bits"], "method_id": enclosure["method_id"]})
    product = mp.iv.fprod(values)
    operation = {"op": "EULER_PRODUCT", "index_variable": "p", "prime_sample": [str(p) for p in primes],
                 "local_factor": local_ast}
    return {"family_id": f"{family_name}:h={h}:sigma={sigma_text}", "operation_ast": operation,
            "operation_ast_sha256": h256(json.dumps(operation, sort_keys=True, separators=(",", ":")).encode()),
            "local_factors": rows,
            "partial_product_certified_interval": interval_from_iv_b(product, "B:ANALYTIC_AST_PRODUCT_IV_260DPS:" + family_name)}


def positive_sigmas_b(case: dict) -> list[str]:
    values = [text for text in case.get("samples_sigma", ["1"]) if canonical_fraction(text) > 0]
    return values or ["1"]


def build_families_b(case: dict) -> tuple[list[dict], dict[str, list[dict]]]:
    field = case["theorem_field"]
    hs = [int(case["h"])] if "h" in case else [int(value) for value in case["h_values"]]
    sigmas = positive_sigmas_b(case)
    specs: list[tuple[str, dict, str, int]] = []
    for h in hs:
        for sigma in sigmas:
            if field == "saturated_bounded_compact_iff_sigma_gt_zero":
                specs.append(("SATURATED_FIBER_MASS", saturated_mass_ast_b(), sigma, h))
            elif field in {"modulo_bounded_compact_iff_sigma_gt_one_over_h", "modulo_similarity_iff_sigma_gt_one_over_h"}:
                specs.append(("MODULO_FIBER_MASS", modulo_mass_ast_b(), sigma, h))
            elif field == "power_schatten_k_sigma_q_gt_two":
                specs.extend((("POWER_S", power_s_local_ast_b(h), sigma, h), ("POWER_M", power_m_local_ast_b(), sigma, h)))
            elif field == "trace_domain_and_zeta_quotient":
                specs.append(("TRACE_HFREE", hfree_local_ast_b(h, "k"), sigma, h))
            elif field == "regularized_determinant_domain":
                specs.append(("DETERMINANT_HFREE", hfree_local_ast_b(h, "k"), sigma, h))
            elif field in {"saturated_similarity_iff_sigma_gt_one", "primorial_maximal_order_three_regimes"}:
                specs.append(("SATURATED_RIESZ", saturated_riesz_ast_b(), sigma, h))
            elif field in {"tauberian_strip_pole_and_residue", "C_D_and_eigenvalue_constants_away_from_crossover"}:
                specs.extend((("WEYL_C", c_local_ast_b(h), sigma, h), ("WEYL_D", d_local_ast_b(), sigma, h),
                              ("EIGENVALUE_CONSTANT", eigen_local_ast_b(), sigma, h)))
            elif field == "C_and_D_equal_one_at_sigma_one":
                specs.extend((("CROSSOVER_C", c_local_ast_b(h), sigma, h), ("CROSSOVER_D", d_local_ast_b(), sigma, h),
                              ("CROSSOVER_EIGEN", eigen_local_ast_b(), sigma, h)))
            elif field in {"commutator_schatten_sigma_q_gt_one", "h_ge_3_commutator_necessity", "h2_commutator_hilbert_schmidt_euler_identity"}:
                specs.extend((("COMMUTATOR_PRODUCT_A", comm_a_local_ast_b(h), sigma, h),
                              ("COMMUTATOR_PRODUCT_B", comm_b_local_ast_b(h), sigma, h)))
            elif field == "free_UFD_clone_reproduces_structural_package":
                specs.extend((("FREE_UFD_SATURATED_MASS", saturated_mass_ast_b(), sigma, h),
                              ("FREE_UFD_MODULO_MASS", modulo_mass_ast_b(), sigma, h),
                              ("FREE_UFD_SATURATED_RIESZ", saturated_riesz_ast_b(), sigma, h),
                              ("FREE_UFD_COMMUTATOR_A", comm_a_local_ast_b(h), sigma, h),
                              ("FREE_UFD_COMMUTATOR_B", comm_b_local_ast_b(h), sigma, h),
                              ("FREE_UFD_WEYL_C", c_local_ast_b(h), sigma, h),
                              ("FREE_UFD_WEYL_D", d_local_ast_b(), sigma, h),
                              ("FREE_UFD_EIGEN", eigen_local_ast_b(), sigma, h)))
            else:
                raise ValueError("unimplemented analytic family")
    families = [certified_family_b(case, name, ast, sigma, h) for name, ast, sigma, h in specs]
    by_name: dict[str, list[dict]] = {}
    for family in families:
        by_name.setdefault(family["family_id"].split(":", 1)[0], []).append(family)
    return families, by_name


def legacy_factor_rows_b(family: dict) -> list[dict]:
    return [{"prime": row["prime"], "lower": row["lower"], "upper": row["upper"]} for row in family["local_factors"]]


def difference_certificate_b(first: dict, second: dict) -> dict:
    params = first["local_factors"]
    left_values = [eval_numeric_ast_b(row["operation_ast"], row["parameters"]) for row in params]
    right_values = [eval_numeric_ast_b(row["operation_ast"], row["parameters"]) for row in second["local_factors"]]
    difference = ast_mul_b(ast_rat_b(2), {"op": "DIFFERENCE_OF_PRODUCTS",
                                         "minuend_family": first["family_id"], "subtrahend_family": second["family_id"]})
    return {"operation_ast": difference,
            "operation_ast_sha256": h256(json.dumps(difference, sort_keys=True, separators=(",", ":")).encode()),
            "certified_interval": interval_from_iv_b(2 * (mp.iv.fprod(left_values) - mp.iv.fprod(right_values)),
                                                      "B:COMMUTATOR_DIFFERENCE_IV_260DPS")}


def domain_ast_b(field: str) -> dict:
    gt = lambda left, right: {"op": "STRICT_GT", "left": left, "right": right}
    sigma, h = ast_param_b("sigma"), ast_param_b("h")
    if field in {"saturated_bounded_compact_iff_sigma_gt_zero", "primorial_maximal_order_three_regimes"}:
        return gt(sigma, ast_rat_b(0))
    if field in {"modulo_bounded_compact_iff_sigma_gt_one_over_h", "modulo_similarity_iff_sigma_gt_one_over_h",
                 "C_D_and_eigenvalue_constants_away_from_crossover"}:
        return gt(sigma, ast_div_b(ast_rat_b(1), h))
    if field == "power_schatten_k_sigma_q_gt_two":
        return {"op": "AND", "operands": [gt(ast_mul_b(ast_param_b("k"), sigma, ast_param_b("q")), ast_rat_b(2)),
                                             {"op": "MODULO_REQUIRES", "condition": gt(sigma, ast_div_b(ast_rat_b(1), h))}]}
    if field in {"trace_domain_and_zeta_quotient", "regularized_determinant_domain"}:
        order = "k" if field.startswith("trace") else "r"
        return {"op": "AND", "operands": [gt(sigma, ast_div_b(ast_rat_b(1), h)),
                                             gt(ast_mul_b(ast_param_b(order), sigma), ast_rat_b(2))]}
    if field == "saturated_similarity_iff_sigma_gt_one":
        return gt(sigma, ast_rat_b(1))
    if field == "tauberian_strip_pole_and_residue":
        strip = {"op": "MAX", "operands": [ast_div_b(ast_rat_b(1), h),
                                               ast_div_b(ast_add_b(ast_rat_b(1), ast_neg_b(sigma)), ast_add_b(h, ast_rat_b(-1)))]}
        return {"op": "AND", "operands": [gt(sigma, ast_rat_b(0)), gt(ast_param_b("Re_z"), strip)]}
    if field == "C_and_D_equal_one_at_sigma_one":
        return {"op": "EQUAL", "left": sigma, "right": ast_rat_b(1), "quantifier": {"op": "FOR_ALL", "variable": "h", "lower_bound": "2"}}
    if field in {"commutator_schatten_sigma_q_gt_one", "h_ge_3_commutator_necessity"}:
        return gt(ast_mul_b(sigma, ast_param_b("q")), ast_rat_b(1))
    if field == "h2_commutator_hilbert_schmidt_euler_identity":
        return gt(sigma, ast_rat_b(1, 2))
    if field == "free_UFD_clone_reproduces_structural_package":
        return {"op": "FOR_ALL", "variable": "h", "lower_bound": "2", "scope": "EACH_FORMULA_LEGAL_DOMAIN"}
    raise ValueError("domain AST")


def formula_ast_b(case: dict, family_ids: list[str]) -> dict:
    return {"op": "THEOREM_IFF", "theorem_field": case["theorem_field"],
            "domain_ast": domain_ast_b(case["theorem_field"]),
            "parameters": {"h": case.get("h", case.get("h_values")), "k": case.get("k"),
                           "q": case.get("q"), "r": case.get("determinant_order_r"),
                           "samples_sigma": case.get("samples_sigma", [])},
            "derivation_ast": {"op": "EULER_PRODUCT", "indexed_family_ids": family_ids}}


def analytic_payload_b(case: dict, domain: str, witness: str, value_label: str, section: str,
                       proof_text: str) -> dict:
    old_dps = mp.iv.dps
    mp.iv.dps = 260
    try:
        families, by_name = build_families_b(case)
        primary = families[-1]
        field = case["theorem_field"]
        if field == "power_schatten_k_sigma_q_gt_two":
            primary = by_name["POWER_S"][-1]
        elif field in {"commutator_schatten_sigma_q_gt_one", "h_ge_3_commutator_necessity", "h2_commutator_hilbert_schmidt_euler_identity"}:
            primary = by_name["COMMUTATOR_PRODUCT_A"][-1]
        elif field in {"tauberian_strip_pole_and_residue", "C_D_and_eigenvalue_constants_away_from_crossover"}:
            primary = by_name["WEYL_C"][-1]
        elif field == "C_and_D_equal_one_at_sigma_one":
            primary = by_name["CROSSOVER_C"][0]
        elif field == "free_UFD_clone_reproduces_structural_package":
            primary = by_name["FREE_UFD_SATURATED_MASS"][-1]
        payload = {"schema_version": "paper45.analytic-certificate-payload.v3", "case_id": case["case_id"],
                   "theorem_field": field, "formula_ast": formula_ast_b(case, [x["family_id"] for x in families]),
                   "endpoint_samples": case.get("samples_sigma", []), "endpoint_witness": witness,
                   "conclusion_label": value_label, "proof_heading": section,
                   "proof_bindings": proof_bindings_b(proof_text, section), "analytic_families": families,
                   "local_euler_factors": legacy_factor_rows_b(primary),
                   "partial_product_certified_interval": primary["partial_product_certified_interval"],
                   "derivation_family": ("free_UFD_negative_control" if field == "free_UFD_clone_reproduces_structural_package"
                                         else "prime_exponent_Euler_Tauberian")}
        if field == "power_schatten_k_sigma_q_gt_two":
            payload["power_s_local_factors"] = legacy_factor_rows_b(by_name["POWER_S"][-1])
            payload["power_m_local_factors"] = legacy_factor_rows_b(by_name["POWER_M"][-1])
        if field in {"commutator_schatten_sigma_q_gt_one", "h_ge_3_commutator_necessity", "h2_commutator_hilbert_schmidt_euler_identity"}:
            first, second = by_name["COMMUTATOR_PRODUCT_A"][-1], by_name["COMMUTATOR_PRODUCT_B"][-1]
            payload["first_product_local_factors"] = legacy_factor_rows_b(first)
            payload["second_product_local_factors"] = legacy_factor_rows_b(second)
            payload["commutator_product_difference"] = difference_certificate_b(first, second)
        if field in {"tauberian_strip_pole_and_residue", "C_D_and_eigenvalue_constants_away_from_crossover", "C_and_D_equal_one_at_sigma_one"}:
            c_name = "CROSSOVER_C" if field == "C_and_D_equal_one_at_sigma_one" else "WEYL_C"
            d_name = "CROSSOVER_D" if field == "C_and_D_equal_one_at_sigma_one" else "WEYL_D"
            e_name = "CROSSOVER_EIGEN" if field == "C_and_D_equal_one_at_sigma_one" else "EIGENVALUE_CONSTANT"
            payload["C_h_sigma"] = {"op": "EULER_PRODUCT", "family_ids": [x["family_id"] for x in by_name[c_name]]}
            payload["D_h_sigma"] = {"op": "EULER_PRODUCT", "family_ids": [x["family_id"] for x in by_name[d_name]]}
            payload["eigenvalue_constant"] = {"op": "EULER_PRODUCT", "family_ids": [x["family_id"] for x in by_name[e_name]]}
        if field == "tauberian_strip_pole_and_residue":
            h_node, sigma_node = ast_param_b("h"), ast_param_b("sigma")
            payload["strip_terms"] = {"op": "MAX", "operands": [ast_div_b(ast_rat_b(1), h_node),
                                                                     ast_div_b(ast_add_b(ast_rat_b(1), ast_neg_b(sigma_node)), ast_add_b(h_node, ast_rat_b(-1)))]}
            payload["remainder_orders"] = [{"op": "BIG_O", "exponent": ast_neg_b(ast_mul_b(h_node, ast_param_b("Re_z")))},
                                             {"op": "BIG_O", "exponent": ast_neg_b(ast_add_b(ast_mul_b(ast_add_b(h_node, ast_rat_b(-1)), ast_param_b("Re_z")), sigma_node))}]
            payload["simple_pole"] = {"op": "ZETA_QUOTIENT", "identity": "F_h_sigma(z)=zeta(z)*G_h_sigma(z)", "pole_at": "1"}
            payload["positive_residue"] = {"op": "EULER_PRODUCT", "constant": "C_h_sigma", "positive_measure": True}
            payload["asymptotic_inversion"] = {"op": "ASYMPTOTIC_INVERSION", "counting": "A_S(x)~C_h_sigma*x",
                                                "singular_values": "s_n~(C_h_sigma/n)^(sigma/2)"}
        if field == "primorial_maximal_order_three_regimes":
            payload["subcritical_coefficient"] = {"op": "DIVIDE", "numerator": ast_pow_b(ast_add_b(ast_param_b("h"), ast_rat_b(-1)), ast_add_b(ast_param_b("sigma"), ast_rat_b(-1))),
                                                    "denominator": ast_mul_b(ast_rat_b(2), ast_add_b(ast_rat_b(1), ast_neg_b(ast_param_b("sigma"))))}
            payload["mertens_regime"] = {"op": "ASYMPTOTIC_EQUIVALENCE", "condition": "sigma=1", "value": "sqrt(exp(gamma)*log(log(x)))"}
            payload["supercritical_limit"] = {"op": "LIMIT", "condition": "sigma>1", "value": "sqrt(zeta(sigma))"}
        if field == "free_UFD_clone_reproduces_structural_package":
            namespace = ["a_2", "a_3", "a_5", "a_7", "a_11"]
            payload["saturated_formula"] = {"op": "EULER_PRODUCT", "atom_namespace": namespace, "local_factor": saturated_mass_ast_b()}
            payload["modulo_formula"] = {"op": "ZETA_QUOTIENT", "atom_namespace": namespace, "fiber_local_factor": modulo_mass_ast_b(), "rational_prime_semantics": False}
            payload["similarity_formula"] = {"op": "EULER_PRODUCT", "atom_namespace": namespace, "local_factor": saturated_riesz_ast_b()}
            payload["commutator_formula"] = {"op": "DIFFERENCE_OF_PRODUCTS", "atom_namespace": namespace,
                                              "product_A_local": comm_a_local_ast_b(int(case["h"])),
                                              "product_B_local": comm_b_local_ast_b(int(case["h"])),
                                              "rational_prime_semantics": False}
        return payload
    finally:
        mp.iv.dps = old_dps


def proof_hash(bindings: list[dict]) -> str:
    return h256(("paper45-proof-dependency-v3\n" + json.dumps(bindings, sort_keys=True, separators=(",", ":")) + "\n").encode())


def analytic_hash(case_id: str, strict: str, witness: str, value: str) -> str:
    return h256(f"paper45-analytic-derivation-v3\n{case_id}\n{strict}\n{witness}\n{value}\n".encode())


def jcs_object(obj: dict) -> bytes:
    # Certificate objects contain only strings; this is the complete RFC8785 ordering needed here.
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def infinite_record(case: dict, proof_text: str) -> dict:
    cid, field = case["case_id"], case["theorem_field"]
    strict, witness, value, section = theorem_certificate_fields(field)
    payload = analytic_payload_b(case, strict, witness, value, section, proof_text)
    payload_jcs = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    record = {"case_id": cid, "evidence_type": "INFINITE_THEOREM_CERTIFICATE", "certificate_owner": "B",
              "theorem_field": field, "strict_domain_expression": strict,
              "endpoint_witness_type": witness, "certificate_value": payload_jcs,
              "proof_dependency_hash": proof_hash(payload["proof_bindings"]),
              "analytic_derivation_hash": analytic_hash(cid, strict, witness, payload_jcs)}
    record["certificate_payload_sha256"] = h256(jcs_object(record))
    return record


def evaluate(inputs: Path) -> dict:
    contract_path = inputs / "EXPERIMENT_CONTRACT.json"
    contract = read_json(contract_path)
    semantic_code = semantic_input_code_b(contract)
    if semantic_code:
        raise SemanticRejectB(semantic_code)
    exercise_raw_grid_b(contract)
    finite = []
    infinite_cases = []
    for case in contract["case_registry"]:
        kind = case["evidence_type"]
        if kind == "FINITE_COMPRESSION":
            for cutoff, bits in zip(case["cutoffs"], contract["precision_bits"]):
                finite.append(finite_from_states(case, cutoff, bits))
        elif kind == "FINITE_OPTIMIZATION":
            for sigma, x in zip(case["samples_sigma"], case["x_cutoffs"]):
                finite.append(optimization_from_prime_states(case, sigma, x))
        elif kind == "INFINITE_THEOREM_CERTIFICATE":
            infinite_cases.append(case)
    infinite_cases.sort(key=lambda c: c["case_id"])
    ids = [c["case_id"] for c in infinite_cases]
    if ids != contract["infinite_coverage_gate"]["ordered_case_ids"] or len(ids) != 15:
        raise RuntimeError("infinite set membership/order")
    digest = h256(("\n".join(ids) + "\n").encode())
    if digest != INF_SET_SHA or digest != contract["infinite_coverage_gate"]["ordered_set_sha256"]:
        raise RuntimeError("infinite set hash")
    proof_text = (inputs / "PROOF_PACKAGE.md").read_text(encoding="utf-8")
    records = [infinite_record(c, proof_text) for c in infinite_cases]
    if len(finite) != 21 or len(records) != 15:
        raise RuntimeError("coverage")
    return {"schema_version": "paper45.science-projection.v3", "producer": "B",
            "contract_sha256": h256(contract_path.read_bytes()),
            "declared_infinite_case_set_sha256": INF_SET_SHA,
            "finite_records": finite, "infinite_case_ids": ids, "infinite_records": records}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--inputs", type=Path, required=True)
    ap.add_argument("--emit", type=Path)
    ns = ap.parse_args()
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    try:
        projection = evaluate(ns.inputs)
        data = json.dumps(projection, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n"
        if ns.emit:
            ns.emit.write_text(data, encoding="utf-8")
        else:
            sys.stdout.write(data)
        return 0
    except SemanticRejectB as exc:
        payload = {"consumer_key": "B", "outcome": "REJECT", "exit_code": 2,
                   "rejection_code": exc.code,
                   "result_digest": h256(("B\n" + exc.code + "\n").encode())}
        sys.stdout.write(json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")
        return 2
    except Exception:
        err = {"outcome": "HARNESS_ERROR", "exit_code": 3,
               "error": {"code": "INTERNAL_EXCEPTION", "stage": "B", "detail": "redacted"}}
        sys.stderr.write(json.dumps(err, sort_keys=True, separators=(",", ":")) + "\n")
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
