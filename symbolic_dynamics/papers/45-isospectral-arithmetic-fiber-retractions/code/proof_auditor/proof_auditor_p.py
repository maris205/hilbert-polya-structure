#!/usr/bin/env python3
"""Proof/audit lane P.

P never imports B and never uses B's implementation helpers.  It rebuilds the
fifteen theorem obligations from the frozen contract and proof corpus, then
evaluates every recorded local Euler factor and its partial product at 320
decimal digits before accepting B's outward intervals.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp


SET_HASH = "6401b141f7b46b0f7275ec124ec571542655b9874cfa9aa5c7123108577e8a84"
FROZEN_PROOF_SHA256 = "964d7bd6ccc37cd95dff28b2b82a3903e25eb337afcde11310f299a75e40acd8"
PRIME_SAMPLE = (2, 3, 5, 7, 11)
RECORD_FIELDS = {
    "case_id", "evidence_type", "certificate_owner", "theorem_field",
    "strict_domain_expression", "endpoint_witness_type", "certificate_value",
    "proof_dependency_hash", "analytic_derivation_hash", "certificate_payload_sha256",
}
PAYLOAD_BASE_FIELDS = {
    "schema_version", "case_id", "theorem_field", "formula_ast", "endpoint_samples",
    "endpoint_witness", "conclusion_label", "proof_heading", "local_euler_factors",
    "partial_product_certified_interval", "derivation_family", "proof_bindings", "analytic_families",
}


class SemanticRejectP(Exception):
    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


P_ATTACKS = [
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
    (("record", "evidence_type"), "INFINITE_THEOREM_CERTIFICATE", "FINITE_AS_INFINITE"),
    (("record", "evidence_type"), "ANALYTIC_HEARSAY", "UNKNOWN_EVIDENCE_TAG"),
    (("case", "determinant_order_r"), "3/2", "DETERMINANT_ORDER_NOT_INTEGER"),
    (("case", "determinant_order_r"), 0, "DETERMINANT_ORDER_NONPOSITIVE"),
    (("infinite_coverage", "B", "exact_count"), 14, "B_INF_CASE_MISSING"),
    (("infinite_coverage", "B", "exact_count"), 16, "B_INF_CASE_EXTRA"),
    (("infinite_coverage", "B", "order"), "reordered", "B_INF_CASE_REORDERED"),
    (("infinite_coverage", "B", "membership"), "includes_INF_UNDECLARED", "B_INF_UNDECLARED_CASE"),
    (("infinite_coverage", "B", "certificate_owner"), "A", "B_CERTIFICATE_OWNER_CHANGED"),
    (("infinite_coverage", "P", "exact_count"), 14, "P_INF_CASE_MISSING"),
    (("infinite_coverage", "P", "exact_count"), 16, "P_INF_CASE_EXTRA"),
    (("infinite_coverage", "P", "order"), "reordered", "P_INF_CASE_REORDERED"),
    (("infinite_coverage", "P", "audit_owner"), "B", "P_AUDIT_OWNER_CHANGED"),
    (("infinite_coverage", "ordered_set_sha256"), "0" * 64, "INF_COVERAGE_SET_HASH_CHANGED"),
    (("infinite_coverage", "P", "hash_closure"), "accept_mismatch", "P_CERTIFICATE_HASH_CLOSURE_BROKEN"),
    (("infinite_coverage", "P", "verdict_closure"), "overall_independent_of_per_case", "P_VERDICT_CLOSURE_BROKEN"),
]


def semantic_input_code_p(contract: dict):
    baseline = contract.get("mutation_baseline")
    if type(baseline) is not dict:
        return "CONTRACT_BASELINE_SHAPE"
    for path, attacked, code in P_ATTACKS:
        node = baseline
        try:
            for part in path:
                node = node[part]
        except (KeyError, TypeError):
            return "CONTRACT_BASELINE_SHAPE"
        if type(node) is type(attacked) and node == attacked:
            return code
    return None


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def strict_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate member")
        result[key] = value
    return result


def strict_parse_bytes(path: Path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=strict_pairs,
                      parse_constant=lambda _x: (_ for _ in ()).throw(ValueError("constant")))


def strict_parse_text(text: str):
    return json.loads(text, object_pairs_hook=strict_pairs,
                      parse_constant=lambda _x: (_ for _ in ()).throw(ValueError("constant")))


def canonical(value) -> str:
    # The payload contains no binary floating-point values.  UTF-16 key order
    # and Unicode code-point order coincide for its ASCII keys, hence this is
    # the RFC 8785 representation for this deliberately restricted domain.
    def visit(node):
        if type(node) is float:
            raise ValueError("non-JCS payload token")
        if type(node) is dict:
            for key, child in node.items():
                if type(key) is not str:
                    raise ValueError("non-string key")
                visit(child)
        elif type(node) is list:
            for child in node:
                visit(child)
        elif node is not None and type(node) not in (str, int, bool):
            raise ValueError("unsupported payload token")
    visit(value)
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def rational(text: str) -> Fraction:
    if type(text) is not str or re.fullmatch(r"-?(0|[1-9][0-9]*)(/[1-9][0-9]*)?", text) is None:
        raise ValueError("rational syntax")
    value = Fraction(text)
    if str(value) != text:
        raise ValueError("noncanonical rational")
    return value


def dependency_hash(bindings: list[dict]) -> str:
    return digest(("paper45-proof-dependency-v3\n" + canonical(bindings) + "\n").encode())


def derivation_hash(cid: str, domain: str, witness: str, payload_jcs: str) -> str:
    return digest(f"paper45-analytic-derivation-v3\n{cid}\n{domain}\n{witness}\n{payload_jcs}\n".encode())


def record_payload_hash(record: dict) -> str:
    stripped = {key: value for key, value in record.items() if key != "certificate_payload_sha256"}
    return digest(canonical(stripped).encode("utf-8"))


def decimal_interval_contains(container: dict, value, require_precision: int = 230) -> bool:
    if type(container) is not dict or set(container) not in ({"lower", "upper"},
                                                              {"lower", "upper", "precision_bits", "method_id"}):
        return False
    if "precision_bits" in container and (type(container["precision_bits"]) is not int or
                                           container["precision_bits"] < require_precision):
        return False
    if type(container["lower"]) is not str or type(container["upper"]) is not str:
        return False
    low, high = mp.mpf(container["lower"]), mp.mpf(container["upper"])
    return mp.isfinite(low) and mp.isfinite(high) and low <= value <= high and low <= high


def qnode_p(value=0, denominator=1) -> dict:
    item = value if isinstance(value, Fraction) else Fraction(value, denominator)
    return {"op": "RATIONAL", "numerator": str(item.numerator), "denominator": str(item.denominator)}


def variable_p(label: str) -> dict:
    return {"op": "PARAMETER", "name": label}


def negative_p(item: dict) -> dict:
    return {"op": "NEGATE", "operand": item}


def plus_p(*items: dict) -> dict:
    return {"op": "ADD", "operands": list(items)}


def times_p(*items: dict) -> dict:
    return {"op": "MULTIPLY", "operands": list(items)}


def ratio_p(top: dict, bottom: dict) -> dict:
    return {"op": "DIVIDE", "numerator": top, "denominator": bottom}


def exponentiate_p(base: dict, power: dict) -> dict:
    return {"op": "POWER", "base": base, "exponent": power}


def sum_p(items: list[dict]) -> dict:
    return {"op": "FINITE_SUM", "terms": items}


def complement_p(item: dict) -> dict:
    return plus_p(qnode_p(1), negative_p(item))


def prime_to_p(power: dict) -> dict:
    return exponentiate_p(variable_p("p"), power)


def evaluate_expression_p(tree: dict, bindings: dict[str, str]):
    """P's point arithmetic is deliberately separate from B's interval lane."""
    operation = tree["op"]
    if operation == "RATIONAL":
        return mp.mpf(tree["numerator"]) / mp.mpf(tree["denominator"])
    if operation == "PARAMETER":
        value = rational(bindings[tree["name"]])
        return mp.mpf(value.numerator) / value.denominator
    if operation == "NEGATE":
        return -evaluate_expression_p(tree["operand"], bindings)
    if operation == "ADD":
        return sum((evaluate_expression_p(child, bindings) for child in tree["operands"]), mp.mpf(0))
    if operation == "FINITE_SUM":
        return sum((evaluate_expression_p(child, bindings) for child in tree["terms"]), mp.mpf(0))
    if operation == "MULTIPLY":
        answer = mp.mpf(1)
        for child in reversed(tree["operands"]):
            answer *= evaluate_expression_p(child, bindings)
        return answer
    if operation == "DIVIDE":
        return evaluate_expression_p(tree["numerator"], bindings) / evaluate_expression_p(tree["denominator"], bindings)
    if operation == "POWER":
        return mp.power(evaluate_expression_p(tree["base"], bindings), evaluate_expression_p(tree["exponent"], bindings))
    raise ValueError("P encountered a nonnumeric operation")


def saturated_mass_p() -> dict:
    return exponentiate_p(complement_p(prime_to_p(negative_p(variable_p("sigma")))), qnode_p(-1))


def modulo_mass_p() -> dict:
    return exponentiate_p(complement_p(prime_to_p(negative_p(times_p(variable_p("h"), variable_p("sigma"))))), qnode_p(-1))


def saturated_projection_p() -> dict:
    return exponentiate_p(complement_p(prime_to_p(negative_p(variable_p("sigma")))), qnode_p(-1, 2))


def power_scale_p() -> dict:
    return times_p(variable_p("k"), variable_p("sigma"), variable_p("q"), qnode_p(1, 2))


def saturated_power_p(h: int) -> dict:
    scale = power_scale_p()
    interior = [prime_to_p(negative_p(times_p(qnode_p(e), scale))) for e in range(1, h - 1)]
    tail = times_p(prime_to_p(negative_p(times_p(qnode_p(h - 1), scale))),
                   exponentiate_p(complement_p(prime_to_p(negative_p(variable_p("sigma")))),
                                  negative_p(times_p(variable_p("q"), qnode_p(1, 2)))))
    return plus_p(qnode_p(1), sum_p(interior), tail)


def modulo_power_p() -> dict:
    scale = power_scale_p()
    fiber = exponentiate_p(complement_p(prime_to_p(negative_p(times_p(variable_p("h"), variable_p("sigma"))))),
                           negative_p(times_p(variable_p("q"), qnode_p(1, 2))))
    hfree = ratio_p(complement_p(prime_to_p(negative_p(times_p(variable_p("h"), scale)))),
                    complement_p(prime_to_p(negative_p(scale))))
    return times_p(fiber, hfree)


def hfree_sum_p(h: int) -> dict:
    base = times_p(variable_p("k"), variable_p("sigma"), qnode_p(1, 2))
    return sum_p([prime_to_p(negative_p(times_p(qnode_p(e), base))) for e in range(h)])


def saturated_weyl_p(h: int) -> dict:
    beginning = sum_p([prime_to_p(qnode_p(-e)) for e in range(h - 1)])
    ending = times_p(prime_to_p(qnode_p(-(h - 1))),
                     exponentiate_p(complement_p(prime_to_p(negative_p(variable_p("sigma")))),
                                    negative_p(ratio_p(qnode_p(1), variable_p("sigma")))))
    return times_p(complement_p(prime_to_p(qnode_p(-1))), plus_p(beginning, ending))


def modulo_weyl_p() -> dict:
    return times_p(complement_p(prime_to_p(negative_p(variable_p("h")))),
                   exponentiate_p(complement_p(prime_to_p(negative_p(times_p(variable_p("h"), variable_p("sigma"))))),
                                  negative_p(ratio_p(qnode_p(1), variable_p("sigma")))))


def eigen_density_p() -> dict:
    return complement_p(prime_to_p(negative_p(variable_p("h"))))


def commutator_first_p(h: int) -> dict:
    prefix = sum_p([prime_to_p(negative_p(times_p(qnode_p(2 * e), variable_p("sigma")))) for e in range(h - 1)])
    suffix = times_p(prime_to_p(negative_p(times_p(qnode_p(2 * (h - 1)), variable_p("sigma")))),
                     exponentiate_p(complement_p(prime_to_p(negative_p(variable_p("sigma")))), qnode_p(-2)))
    return plus_p(prefix, suffix)


def commutator_second_p(h: int) -> dict:
    prefix = sum_p([prime_to_p(negative_p(times_p(qnode_p(2 * e), variable_p("sigma")))) for e in range(h - 1)])
    suffix = times_p(prime_to_p(negative_p(times_p(qnode_p(2 * (h - 1)), variable_p("sigma")))),
                     exponentiate_p(complement_p(prime_to_p(negative_p(variable_p("sigma")))), qnode_p(-1)))
    return plus_p(prefix, suffix)


def positive_samples_p(case: dict) -> list[str]:
    answer = [item for item in case.get("samples_sigma", ["1"]) if rational(item) > 0]
    return answer if answer else ["1"]


def expected_families_p(case: dict) -> list[tuple[str, dict, str, int]]:
    field = case["theorem_field"]
    hs = [int(case["h"])] if "h" in case else [int(item) for item in case["h_values"]]
    rows = []
    for h in hs:
        for sigma in positive_samples_p(case):
            if field.startswith("saturated_bounded_"):
                rows.append(("SATURATED_FIBER_MASS", saturated_mass_p(), sigma, h))
            elif field.startswith("modulo_bounded_") or field.startswith("modulo_similarity_"):
                rows.append(("MODULO_FIBER_MASS", modulo_mass_p(), sigma, h))
            elif field.startswith("power_schatten_"):
                rows.extend((("POWER_S", saturated_power_p(h), sigma, h), ("POWER_M", modulo_power_p(), sigma, h)))
            elif field.startswith("trace_domain_"):
                rows.append(("TRACE_HFREE", hfree_sum_p(h), sigma, h))
            elif field.startswith("regularized_determinant_"):
                rows.append(("DETERMINANT_HFREE", hfree_sum_p(h), sigma, h))
            elif field.startswith("saturated_similarity_") or field.startswith("primorial_maximal_"):
                rows.append(("SATURATED_RIESZ", saturated_projection_p(), sigma, h))
            elif field.startswith("tauberian_strip_") or field.startswith("C_D_and_eigenvalue_"):
                rows.extend((("WEYL_C", saturated_weyl_p(h), sigma, h), ("WEYL_D", modulo_weyl_p(), sigma, h),
                             ("EIGENVALUE_CONSTANT", eigen_density_p(), sigma, h)))
            elif field.startswith("C_and_D_equal_"):
                rows.extend((("CROSSOVER_C", saturated_weyl_p(h), sigma, h), ("CROSSOVER_D", modulo_weyl_p(), sigma, h),
                             ("CROSSOVER_EIGEN", eigen_density_p(), sigma, h)))
            elif field.startswith("commutator_") or field.startswith("h_ge_3_commutator_") or field.startswith("h2_commutator_"):
                rows.extend((("COMMUTATOR_PRODUCT_A", commutator_first_p(h), sigma, h),
                             ("COMMUTATOR_PRODUCT_B", commutator_second_p(h), sigma, h)))
            elif field.startswith("free_UFD_clone_"):
                rows.extend((("FREE_UFD_SATURATED_MASS", saturated_mass_p(), sigma, h),
                             ("FREE_UFD_MODULO_MASS", modulo_mass_p(), sigma, h),
                             ("FREE_UFD_SATURATED_RIESZ", saturated_projection_p(), sigma, h),
                             ("FREE_UFD_COMMUTATOR_A", commutator_first_p(h), sigma, h),
                             ("FREE_UFD_COMMUTATOR_B", commutator_second_p(h), sigma, h),
                             ("FREE_UFD_WEYL_C", saturated_weyl_p(h), sigma, h),
                             ("FREE_UFD_WEYL_D", modulo_weyl_p(), sigma, h),
                             ("FREE_UFD_EIGEN", eigen_density_p(), sigma, h)))
            else:
                raise ValueError("unknown proof family")
    return rows


def domain_tree_p(field: str) -> dict:
    strict = lambda left, right: {"op": "STRICT_GT", "left": left, "right": right}
    sigma, h = variable_p("sigma"), variable_p("h")
    if field.startswith("saturated_bounded_") or field.startswith("primorial_maximal_"):
        return strict(sigma, qnode_p(0))
    if field.startswith("modulo_bounded_") or field.startswith("modulo_similarity_") or field.startswith("C_D_and_eigenvalue_"):
        return strict(sigma, ratio_p(qnode_p(1), h))
    if field.startswith("power_schatten_"):
        return {"op": "AND", "operands": [strict(times_p(variable_p("k"), sigma, variable_p("q")), qnode_p(2)),
                                             {"op": "MODULO_REQUIRES", "condition": strict(sigma, ratio_p(qnode_p(1), h))}]}
    if field.startswith("trace_domain_") or field.startswith("regularized_determinant_"):
        symbol = "k" if field.startswith("trace") else "r"
        return {"op": "AND", "operands": [strict(sigma, ratio_p(qnode_p(1), h)),
                                             strict(times_p(variable_p(symbol), sigma), qnode_p(2))]}
    if field.startswith("saturated_similarity_"):
        return strict(sigma, qnode_p(1))
    if field.startswith("tauberian_strip_"):
        frontier = {"op": "MAX", "operands": [ratio_p(qnode_p(1), h),
                                                  ratio_p(plus_p(qnode_p(1), negative_p(sigma)), plus_p(h, qnode_p(-1)))]}
        return {"op": "AND", "operands": [strict(sigma, qnode_p(0)), strict(variable_p("Re_z"), frontier)]}
    if field.startswith("C_and_D_equal_"):
        return {"op": "EQUAL", "left": sigma, "right": qnode_p(1), "quantifier": {"op": "FOR_ALL", "variable": "h", "lower_bound": "2"}}
    if field.startswith("commutator_schatten_") or field.startswith("h_ge_3_commutator_"):
        return strict(times_p(sigma, variable_p("q")), qnode_p(1))
    if field.startswith("h2_commutator_"):
        return strict(sigma, qnode_p(1, 2))
    if field.startswith("free_UFD_clone_"):
        return {"op": "FOR_ALL", "variable": "h", "lower_bound": "2", "scope": "EACH_FORMULA_LEGAL_DOMAIN"}
    raise ValueError("unknown domain family")


def heading_prefix_p(field: str) -> str:
    if field.startswith(("saturated_bounded_", "modulo_bounded_")):
        number = "3"
    elif field.startswith("power_schatten_"):
        number = "4"
    elif field.startswith(("trace_domain_", "regularized_determinant_")):
        number = "5"
    elif field.startswith(("saturated_similarity_", "modulo_similarity_")):
        number = "6"
    elif field.startswith("primorial_maximal_"):
        number = "7"
    elif field.startswith("tauberian_strip_"):
        number = "8"
    elif field.startswith(("C_D_and_eigenvalue_", "C_and_D_equal_")):
        number = "9"
    elif field.startswith(("commutator_schatten_", "h_ge_3_commutator_")):
        number = "11"
    elif field.startswith("h2_commutator_"):
        number = "12"
    elif field.startswith("free_UFD_clone_"):
        return "Delete-shared-method conclusion"
    else:
        raise ValueError("proof heading family")
    return "Proposition " + number


def semantic_digest_p(body: str) -> dict:
    normalized = " ".join(body.replace("\r\n", "\n").replace("\r", "\n").split())
    captures = re.findall(r"\\\[(.*?)\\\]|\\\((.*?)\\\)", body, re.DOTALL)
    expressions = [re.sub(r"\s+", "", pair[0] if pair[0] else pair[1]) for pair in captures]
    joined = "\n".join(expressions)
    vocabulary = ("\\iff", "\\sim", "\\max", "\\min", "\\ge", "\\le", ">", "<", "=", "\\prod", "\\sum", "\\zeta")
    return {"normalized_section_sha256": digest(normalized.encode()),
            "formula_ast_hashes": [digest(expression.encode()) for expression in expressions],
            "operator_counts": {operator: joined.count(operator) for operator in vocabulary},
            "quantifier_tokens": sorted(re.findall(r"h\\ge2|k\\ge1|0<q<\\infty|\\forall|\\exists", joined))}


def proof_index_p(text: str) -> list[dict]:
    headers = list(re.finditer(r"(?m)^## ([^\n]+)\n", text))
    answer = []
    for position, header in enumerate(headers):
        stop = headers[position + 1].start() if position + 1 < len(headers) else len(text)
        answer.append({"heading": header.group(1), "body": text[header.start():stop]})
    return answer


def proof_bindings_p(text: str, theorem_prefix: str) -> list[dict]:
    result = []
    index = proof_index_p(text)
    for role, prefix in (("main", "Main theorem:"), ("theorem", theorem_prefix)):
        hits = [entry for entry in index if entry["heading"].startswith(prefix)]
        if not hits:
            raise ValueError("required proof section absent")
        for ordinal, entry in enumerate(hits):
            semantic = semantic_digest_p(entry["body"])
            result.append({"role": role, "heading": entry["heading"], "occurrence": str(ordinal),
                           "section_bytes_sha256": digest(entry["body"].encode()), "semantic_ast": semantic,
                           "semantic_ast_sha256": digest(canonical(semantic).encode())})
    return result


def math_normal_form_p(text: str) -> str:
    """Normalize only mathematical spelling; never normalize inequality direction."""
    value = re.sub(r"\s+", "", text.replace("\\left", "").replace("\\right", ""))
    return value.replace("\\ge", ">=").replace("\\le", "<=")


def relation_node_p(left: str, direction: str, right: str) -> dict:
    if direction not in {"GT", "GE", "LT", "LE", "EQ"}:
        raise ValueError("relation direction")
    return {"node_type": "RELATION", "left": left, "direction": direction, "right": right,
            "strict": direction in {"GT", "LT"}}


def find_relation_p(text: str, left: str, right: str, anchor: str | None = None) -> dict:
    region = text
    if anchor is not None:
        start = region.find(anchor)
        if start < 0:
            raise ValueError("semantic anchor absent:" + anchor)
        region = region[start: start + 600]
    compact = math_normal_form_p(region)
    normalized_left, normalized_right = math_normal_form_p(left), math_normal_form_p(right)
    spellings = ((">=", "GE"), ("<=", "LE"), (">", "GT"), ("<", "LT"), ("=", "EQ"))
    hits = []
    for spelling, direction in spellings:
        position = compact.find(normalized_left + spelling + normalized_right)
        if position >= 0:
            hits.append((position, direction))
    if hits:
        return relation_node_p(left, min(hits)[1], right)
    raise ValueError("proof relation absent:" + left + ":" + right)


def typed_claim_p(kind: str, operator: str, form: str, domain: dict, witness: str, conclusion: str,
                  evidence: list[str]) -> dict:
    return {"node_type": "THEOREM_CLAIM", "claim_kind": kind,
            "operator_form": {"operator": operator, "form": form}, "domain": domain,
            "witness": {"node_type": "WITNESS", "kind": witness, "evidence": evidence},
            "conclusion": {"node_type": "CONCLUSION", "kind": conclusion}}


def parse_main_semantics_p(body: str) -> dict:
    h_domain = find_relation_p(body, r"h", r"2", "Let \\(h")
    if h_domain["direction"] not in {"GE", "GT", "EQ"}:
        raise ValueError("main quantifier domain")
    compact = math_normal_form_p(body)
    if not all(token in compact for token in (r"S_{h,s}e_n=n^{-s/2}e_{\tau_h(n)}",
                                                r"M_{h,s}e_n=n^{-s/2}e_{\omega_h(n)}")):
        raise ValueError("main operator definitions")
    return {"node_type": "PROOF_SECTION", "section_kind": "MAIN_ALL_H",
            "quantifiers": [{"node_type": "FOR_ALL", "variable": "h", "domain": h_domain},
                            {"node_type": "FOR_ALL", "variable": "s", "domain": "COMPLEX"}],
            "operator_definitions": [{"operator": "S", "map": "tau_h", "weight": "n^(-s/2)"},
                                     {"operator": "M", "map": "omega_h", "weight": "n^(-s/2)"}]}


def parse_proposition_3_p(body: str) -> list[dict]:
    sat_domain = find_relation_p(body, r"\sigma", "0", r"Suppose \(\sigma")
    modulo_domain = find_relation_p(body, r"\sigma", r"1/h", "is finite exactly when")
    compact = math_normal_form_p(body)
    if not all(token in compact for token in (r"m=p^{h-1}", r"\sum_{r>=0}p^{-(h-1+r)\sigma}=\infty",
                                                r"\rho_M(m)=\zeta(h\sigma)^{1/2}m^{-\sigma/2}")):
        raise ValueError("Proposition 3 witness formulas")
    return [
        typed_claim_p("EXISTENCE_COMPACTNESS", "S", "BOUNDED_COMPACT_IFF", sat_domain,
                      "SATURATED_SINGLE_PRIME_GEOMETRIC_FIBER", "BOUNDED_COMPACT_IFF",
                      ["m=p^(h-1)", "geometric_fiber_mass_diverges_at_endpoint"]),
        typed_claim_p("EXISTENCE_COMPACTNESS", "M", "BOUNDED_COMPACT_IFF", modulo_domain,
                      "MODULO_UNIT_ZETA_ENDPOINT", "BOUNDED_COMPACT_IFF",
                      ["m=1", "zeta(h*sigma)_finite_exactly"]),
    ]


def parse_proposition_4_p(body: str) -> list[dict]:
    power_wall = find_relation_p(body, r"k\sigma q", "2", r"S^k\in\mathcal S_q\iff")
    modulo_guard = find_relation_p(body, r"\sigma", r"1/h", r"M^k\in\mathcal S_q")
    power_wall["left"] = "k*sigma*q"
    compact = math_normal_form_p(body)
    required = (r"1+\sum_{e=1}^{h-2}p^{-ek\sigmaq/2}", r"\zeta(h\sigma)^{q/2}",
                r"\zeta(k\sigmaq/2)", "primeharmonicsumdiverges")
    if not all(token in compact for token in required):
        raise ValueError("Proposition 4 operator/factor forms")
    domain = {"node_type": "AND", "operands": [power_wall,
               {"node_type": "SCOPED_REQUIREMENT", "scope": "M", "relation": modulo_guard}]}
    return [typed_claim_p("POWER_SCHATTEN", "S_AND_M", "POWER_IN_SCHATTEN_q_IFF", domain,
                          "POSITIVE_PRIME_HARMONIC_ENDPOINT", "EXACT_POWER_SCHATTEN_WALL",
                          ["saturated_Euler_factor", "modulo_zeta_quotient", "endpoint_divergence"])]


def parse_proposition_5_p(body: str) -> list[dict]:
    trace_wall = find_relation_p(body, r"k\sigma", "2", "On the common bounded domain")
    modulo_domain = relation_node_p(r"\sigma", "GT", r"1/h")
    det_wall = find_relation_p(body, r"r\sigma", "2", r"For an integer \(r")
    det_modulo = find_relation_p(body, r"\sigma", r"1/h", r"For an integer \(r")
    compact = math_normal_form_p(body)
    trace_wall["left"] = "k*sigma"
    det_wall["left"] = "r*sigma"
    if not all(token in compact for token in (r"\operatorname{Tr}(T^k)",
                                                r"\frac{\zeta(ks/2)}{\zeta(hks/2)}",
                                                r"\det_r(I-zT)", "regularizedFredholmproduct")):
        raise ValueError("Proposition 5 trace/determinant forms")
    return [
        typed_claim_p("TRACE", "S_AND_M", "ORDINARY_TRACE_ZETA_QUOTIENT",
                      {"node_type": "AND", "operands": [modulo_domain, trace_wall]},
                      "ABSOLUTE_H_FREE_DIRICHLET_ENDPOINT", "TRACE_EQUALS_ZETA_QUOTIENT",
                      ["absolute_convergence", "h_free_Euler_product"]),
        typed_claim_p("REGULARIZED_DETERMINANT", "S_AND_M", "COMMON_INTEGER_ORDER_DETERMINANT",
                      {"node_type": "AND", "operands": [det_modulo, det_wall]},
                      "H_FREE_PRIME_HARMONIC_ENDPOINT", "COMMON_INTEGER_ORDER_REGULARIZED_DETERMINANT",
                      ["integer_r>=1", "S_r_membership", "same_algebraic_eigenvalues"]),
    ]


def parse_proposition_6_p(body: str) -> list[dict]:
    sat = find_relation_p(body, r"\sigma", "1", r"S\sim_{\mathrm{bd}}")
    modulo = find_relation_p(body, r"\sigma", r"1/h", r"M\sim_{\mathrm{bd}}")
    compact = math_normal_form_p(body)
    if not all(token in compact for token in (r"\sup_m\|\Pi_{T,m}\|", r"\sqrt{\zeta(h\sigma)}",
                                                "everyfiniteprimesetcanoccur")):
        raise ValueError("Proposition 6 Riesz witness forms")
    return [
        typed_claim_p("SIMILARITY", "S", "BOUNDED_SIMILARITY_TO_NORMAL_IFF", sat,
                      "UNBOUNDED_FINITE_PRIME_SET_RIESZ_NORMS", "BOUNDED_SIMILARITY_IFF",
                      ["all_finite_J_h_sets", "Euler_product_finite_exactly"]),
        typed_claim_p("SIMILARITY", "M", "BOUNDED_SIMILARITY_TO_NORMAL_IFF", modulo,
                      "UNIFORM_ZETA_PROJECTION_NORM", "BOUNDED_SIMILARITY_IFF",
                      ["projection_norm=sqrt(zeta(h*sigma))", "uniform_blocks"]),
    ]


def parse_proposition_7_p(body: str) -> list[dict]:
    compact = math_normal_form_p(body)
    subcritical = find_relation_p(body, "0", r"\sigma", r"If \(0<\sigma<1")
    upper = find_relation_p(body, r"\sigma", "1", r"If \(0<\sigma<1")
    supercritical = find_relation_p(body, r"\sigma", "1", r"If \(\sigma>1")
    if not all(token in compact for token in (r"P_{k+1}^{h-1}>x", r"(h-1)^{\sigma-1}(\logx)^{1-\sigma}",
                                                r"\sqrt{e^\gamma\log\logx}", r"\sqrt{\zeta(\sigma)}")):
        raise ValueError("Proposition 7 optimizer/regimes")
    domain = {"node_type": "REGIME_UNION", "equivalent_domain": relation_node_p(r"\sigma", "GT", "0"),
              "regimes": [{"kind": "SUBCRITICAL", "relations": [subcritical, upper]},
                          {"kind": "CRITICAL", "relation": relation_node_p(r"\sigma", "EQ", "1")},
                          {"kind": "SUPERCRITICAL", "relation": supercritical}]}
    return [typed_claim_p("PRIMORIAL_MAXIMAL_ORDER", "S", "PROJECTION_MAXIMUM", domain,
                          "NEXT_PRIMORIAL_EXCEEDS_X", "EXACT_OPTIMIZER_THREE_REGIME_COEFFICIENT",
                          ["largest_k", "P_(k+1)^(h-1)>x", "three_sigma_regimes"])]


def parse_proposition_8_p(body: str) -> list[dict]:
    sigma = find_relation_p(body, r"\sigma", "0", r"For \(\sigma>0")
    rez = find_relation_p(body, r"\Re z", r"\theta_{h,\sigma}", r"\Re z>\theta")
    compact = math_normal_form_p(body)
    if not all(token in compact for token in (r"\theta_{h,\sigma}=\max(\frac1h,\frac{1-\sigma}{h-1})",
                                                r"F_{h,\sigma}(z)=\zeta(z)G_{h,\sigma}(z)",
                                                "positivelocallyfinitecountingmeasure", "Wiener--Ikehara",
                                                r"s_n(S_{h,s})\sim")):
        raise ValueError("Proposition 8 Tauberian forms")
    rez["left"] = "Re(z)"
    rez["right"] = "max(1/h,(1-sigma)/(h-1))"
    return [typed_claim_p("TAUBERIAN_WEYL", "S", "POSITIVE_DIRICHLET_SERIES_INVERSION",
                          {"node_type": "AND", "operands": [sigma, rez]},
                          "POSITIVE_MEASURE_SIMPLE_POLE", "WIENER_IKEHARA_RESIDUE_C_H_SIGMA",
                          ["F=zeta*G", "positive_measure", "simple_pole_at_one", "asymptotic_inversion"])]


def parse_proposition_9_p(body: str, main: dict) -> list[dict]:
    compact = math_normal_form_p(body)
    crossover = find_relation_p(body, r"\sigma", "1", r"At \(\sigma=1")
    all_h = main["quantifiers"][0]
    if not all(token in compact for token in (r"D_{h,\sigma}=\frac{\zeta(h\sigma)^{1/\sigma}}{\zeta(h)}",
                                                r"1/\zeta(h)", "Everylocalfactorof",
                                                r"C_{h,1}=D_{h,1}=1")):
        raise ValueError("Proposition 9 Weyl/crossover forms")
    legal = relation_node_p(r"\sigma", "GT", r"1/h")
    return [
        typed_claim_p("WEYL_CONSTANTS", "S_M_EIGEN", "C_D_EIGEN_ASYMPTOTICS", legal,
                      "POSITIVE_H_FREE_COUNTING_MEASURE", "EXPLICIT_C_D_EIGEN_CONSTANTS_NO_ORDER_CLAIM",
                      ["h_free_counting", "D_zeta_ratio", "eigen_constant=1/zeta(h)"]),
        typed_claim_p("WEYL_CROSSOVER", "S_AND_M", "ALL_H_CONSTANT_EQUALITY",
                      {"node_type": "QUANTIFIED", "quantifier": all_h, "relation": crossover},
                      "LOCAL_FACTOR_TELESCOPING", "C_H_1_D_H_1_EQUAL_ONE",
                      ["C_local_bracket_geometric_series", "D_zeta_cancellation"]),
    ]


def parse_proposition_11_p(body: str) -> list[dict]:
    wall = find_relation_p(body, r"\sigma q", "1", r"[S^*,S]\in\mathcal S_q\iff")
    wall["left"] = "sigma*q"
    compact = math_normal_form_p(body)
    if not all(token in compact for token in (r"m_r=p_0^{h-1}r", r"m_r=p_0r", "exponentoneissaturated",
                                                "primesumdivergesatandbelow")):
        raise ValueError("Proposition 11 commutator witnesses")
    return [
        typed_claim_p("COMMUTATOR_SCHATTEN_H2", "SELF_COMMUTATOR_S", "COMMUTATOR_IN_SCHATTEN_q_IFF", wall,
                      "TWO_SATURATED_PRIMES", "S_COMMUTATOR_IN_SQ_IFF_SIGMA_Q_GT_ONE",
                      ["h=2", "m_r=p_0*r", "both_exponent_one_primes_saturated"]),
        typed_claim_p("COMMUTATOR_SCHATTEN_HGE3", "SELF_COMMUTATOR_S", "COMMUTATOR_NECESSITY", wall,
                      "FIXED_SATURATED_PRIME_VARYING_EXPONENT_ONE_PRIME", "PRIME_SUM_ENDPOINT_DIVERGENCE",
                      ["h>=3", "m_r=p_0^(h-1)*r", "r_nonsaturated"]),
    ]


def parse_proposition_12_p(body: str) -> list[dict]:
    domain = find_relation_p(body, r"\sigma", r"1/2", r"For \(\sigma>1/2")
    compact = math_normal_form_p(body)
    if not all(token in compact for token in (r"\prod_p[1+(p^\sigma-1)^{-2}]-\prod_p",
                                                "twopositivesumsbelowconvergeseparately",
                                                r"\|[S^*,S]\|_2^2")):
        raise ValueError("Proposition 12 two-product form")
    return [typed_claim_p("COMMUTATOR_H2_EULER", "SELF_COMMUTATOR_S", "HILBERT_SCHMIDT_EULER_DIFFERENCE",
                          domain, "SEPARATE_POSITIVE_EULER_PRODUCTS", "TWO_PRODUCT_DIFFERENCE_IDENTITY",
                          ["product_A", "minus_product_B", "separate_convergence"])]


def parse_delete_shared_p(body: str, main: dict) -> list[dict]:
    collapsed = " ".join(body.split())
    if not all(token in collapsed for token in ("free-UFD methods", "exact all-", "remain")):
        raise ValueError("free-UFD negative-control conclusion")
    quantified = {"node_type": "QUANTIFIED_LEGAL_DOMAINS", "quantifier": main["quantifiers"][0],
                  "scope": "EACH_FORMULA"}
    return [typed_claim_p("FREE_UFD_NEGATIVE_CONTROL", "S_AND_M", "STRUCTURAL_PACKAGE_CLONE",
                          quantified, "NORMED_ATOM_RELABELING", "NEGATIVE_CONTROL_NO_RATIONAL_PRIME_SELECTIVITY",
                          ["free_UFD_methods_deleted", "all_h_structure_remains", "atom_relabeling_only"])]


def typed_proof_semantics_p(proof_text: str, heading: str) -> dict:
    sections = proof_index_p(proof_text)
    main_hits = [item for item in sections if item["heading"].startswith("Main theorem:")]
    theorem_hits = [item for item in sections if item["heading"].startswith(heading)]
    if len(main_hits) != 1 or len(theorem_hits) != 1:
        raise ValueError("typed parser section cardinality")
    main = parse_main_semantics_p(main_hits[0]["body"])
    body = theorem_hits[0]["body"]
    if heading == "Proposition 3":
        claims = parse_proposition_3_p(body)
    elif heading == "Proposition 4":
        claims = parse_proposition_4_p(body)
    elif heading == "Proposition 5":
        claims = parse_proposition_5_p(body)
    elif heading == "Proposition 6":
        claims = parse_proposition_6_p(body)
    elif heading == "Proposition 7":
        claims = parse_proposition_7_p(body)
    elif heading == "Proposition 8":
        claims = parse_proposition_8_p(body)
    elif heading == "Proposition 9":
        claims = parse_proposition_9_p(body, main)
    elif heading == "Proposition 11":
        claims = parse_proposition_11_p(body)
    elif heading == "Proposition 12":
        claims = parse_proposition_12_p(body)
    elif heading == "Delete-shared-method conclusion":
        claims = parse_delete_shared_p(body, main)
    else:
        raise ValueError("typed parser unsupported heading")
    return {"node_type": "PROOF_SEMANTICS", "main": main,
            "section": {"node_type": "PROOF_SECTION", "heading": heading, "claims": claims}}


def choose_semantic_claim_p(field: str, semantics: dict) -> dict:
    claims = semantics["section"]["claims"]
    if field.startswith("saturated_bounded_"):
        wanted, operator = "EXISTENCE_COMPACTNESS", "S"
    elif field.startswith("modulo_bounded_"):
        wanted, operator = "EXISTENCE_COMPACTNESS", "M"
    elif field.startswith("power_schatten_"):
        wanted, operator = "POWER_SCHATTEN", "S_AND_M"
    elif field.startswith("trace_domain_"):
        wanted, operator = "TRACE", "S_AND_M"
    elif field.startswith("regularized_determinant_"):
        wanted, operator = "REGULARIZED_DETERMINANT", "S_AND_M"
    elif field.startswith("saturated_similarity_"):
        wanted, operator = "SIMILARITY", "S"
    elif field.startswith("modulo_similarity_"):
        wanted, operator = "SIMILARITY", "M"
    elif field.startswith("primorial_maximal_"):
        wanted, operator = "PRIMORIAL_MAXIMAL_ORDER", "S"
    elif field.startswith("tauberian_strip_"):
        wanted, operator = "TAUBERIAN_WEYL", "S"
    elif field.startswith("C_D_and_eigenvalue_"):
        wanted, operator = "WEYL_CONSTANTS", "S_M_EIGEN"
    elif field.startswith("C_and_D_equal_"):
        wanted, operator = "WEYL_CROSSOVER", "S_AND_M"
    elif field.startswith("commutator_schatten_"):
        wanted, operator = "COMMUTATOR_SCHATTEN_H2", "SELF_COMMUTATOR_S"
    elif field.startswith("h_ge_3_commutator_"):
        wanted, operator = "COMMUTATOR_SCHATTEN_HGE3", "SELF_COMMUTATOR_S"
    elif field.startswith("h2_commutator_"):
        wanted, operator = "COMMUTATOR_H2_EULER", "SELF_COMMUTATOR_S"
    elif field.startswith("free_UFD_clone_"):
        wanted, operator = "FREE_UFD_NEGATIVE_CONTROL", "S_AND_M"
    else:
        raise ValueError("semantic claim selector")
    matches = [claim for claim in claims if claim["claim_kind"] == wanted and
               claim["operator_form"]["operator"] == operator]
    if len(matches) != 1:
        raise ValueError("semantic claim exact selection")
    return matches[0]


def render_relation_p(node: dict) -> str:
    symbols = {"GT": ">", "GE": ">=", "LT": "<", "LE": "<=", "EQ": "="}
    return node["left"].replace("\\", "") + symbols[node["direction"]] + node["right"].replace("\\", "")


def render_domain_p(node: dict) -> str:
    kind = node["node_type"]
    if kind == "RELATION":
        return render_relation_p(node)
    if kind == "AND":
        rendered = []
        for operand in node["operands"]:
            if operand["node_type"] == "SCOPED_REQUIREMENT":
                rendered.append(operand["scope"] + "_requires_" + render_relation_p(operand["relation"]))
            else:
                rendered.append(render_domain_p(operand))
        return " and ".join(rendered)
    if kind == "REGIME_UNION":
        return render_relation_p(node["equivalent_domain"])
    if kind == "QUANTIFIED":
        return render_relation_p(node["relation"])
    if kind == "QUANTIFIED_LEGAL_DOMAINS":
        h_relation = node["quantifier"]["domain"]
        return render_relation_p(h_relation) + " with each_formula_on_its_legal_domain"
    raise ValueError("domain renderer")


def render_witness_p(node: dict) -> str:
    kind = node["kind"]
    words = kind.lower().split("_")
    if kind == "SATURATED_SINGLE_PRIME_GEOMETRIC_FIBER":
        words[0:2] = reversed(words[0:2])
    elif kind == "MODULO_UNIT_ZETA_ENDPOINT":
        words = ["m", "equals", "1", "zeta", "endpoint"]
    elif kind == "FIXED_SATURATED_PRIME_VARYING_EXPONENT_ONE_PRIME":
        words.insert(3, "plus")
    elif kind not in {"POSITIVE_PRIME_HARMONIC_ENDPOINT", "ABSOLUTE_H_FREE_DIRICHLET_ENDPOINT",
                      "H_FREE_PRIME_HARMONIC_ENDPOINT", "UNBOUNDED_FINITE_PRIME_SET_RIESZ_NORMS",
                      "UNIFORM_ZETA_PROJECTION_NORM", "NEXT_PRIMORIAL_EXCEEDS_X",
                      "POSITIVE_MEASURE_SIMPLE_POLE", "POSITIVE_H_FREE_COUNTING_MEASURE",
                      "LOCAL_FACTOR_TELESCOPING", "TWO_SATURATED_PRIMES",
                      "SEPARATE_POSITIVE_EULER_PRODUCTS", "NORMED_ATOM_RELABELING"}:
        raise ValueError("witness renderer")
    words = [("Dirichlet" if word == "dirichlet" else "Riesz" if word == "riesz" else
              "Euler" if word == "euler" else word) for word in words]
    return "_".join(words)


def render_conclusion_p(node: dict) -> str:
    kind = node["kind"]
    words = kind.lower().split("_")
    if kind == "BOUNDED_COMPACT_IFF":
        words.insert(1, "and")
    elif kind == "EXACT_OPTIMIZER_THREE_REGIME_COEFFICIENT":
        words.insert(2, "and")
    elif kind == "EXPLICIT_C_D_EIGEN_CONSTANTS_NO_ORDER_CLAIM":
        words[1:4] = ["C", "D", "and", "eigenvalue"]
    elif kind == "C_H_1_D_H_1_EQUAL_ONE":
        return "C_h_1=D_h_1=1"
    elif kind == "S_COMMUTATOR_IN_SQ_IFF_SIGMA_Q_GT_ONE":
        words[0], words[3] = "S", "Sq"
        words[-1] = "1"
    elif kind not in {"EXACT_POWER_SCHATTEN_WALL", "TRACE_EQUALS_ZETA_QUOTIENT",
                      "COMMON_INTEGER_ORDER_REGULARIZED_DETERMINANT", "BOUNDED_SIMILARITY_IFF",
                      "WIENER_IKEHARA_RESIDUE_C_H_SIGMA", "PRIME_SUM_ENDPOINT_DIVERGENCE",
                      "TWO_PRODUCT_DIFFERENCE_IDENTITY", "NEGATIVE_CONTROL_NO_RATIONAL_PRIME_SELECTIVITY"}:
        raise ValueError("conclusion renderer")
    words = [("Schatten" if word == "schatten" else "Wiener" if word == "wiener" else
              "Ikehara" if word == "ikehara" else "C" if word == "c" else word) for word in words]
    return "_".join(words)


def derive_certificate_metadata_p(field: str, semantics: dict) -> tuple[str, str, str]:
    claim = choose_semantic_claim_p(field, semantics)
    return render_domain_p(claim["domain"]), render_witness_p(claim["witness"]), render_conclusion_p(claim["conclusion"])


def family_parameters_p(case: dict, sigma: str, h: int, prime: int) -> dict:
    return {"h": str(h), "k": str(case.get("k", case.get("determinant_order_r", 1))),
            "q": str(case.get("q", "1")), "sigma": sigma, "p": str(prime)}


def expected_formula_p(case: dict, identifiers: list[str]) -> dict:
    return {"op": "THEOREM_IFF", "theorem_field": case["theorem_field"],
            "domain_ast": domain_tree_p(case["theorem_field"]),
            "parameters": {"h": case.get("h", case.get("h_values")), "k": case.get("k"),
                           "q": case.get("q"), "r": case.get("determinant_order_r"),
                           "samples_sigma": case.get("samples_sigma", [])},
            "derivation_ast": {"op": "EULER_PRODUCT", "indexed_family_ids": identifiers}}


def expected_payload_keys_p(field: str) -> set[str]:
    result = set(PAYLOAD_BASE_FIELDS)
    if field.startswith("power_schatten_"):
        result |= {"power_s_local_factors", "power_m_local_factors"}
    if field.startswith("commutator_") or field.startswith("h_ge_3_commutator_") or field.startswith("h2_commutator_"):
        result |= {"first_product_local_factors", "second_product_local_factors", "commutator_product_difference"}
    if field.startswith(("tauberian_strip_", "C_D_and_eigenvalue_", "C_and_D_equal_")):
        result |= {"C_h_sigma", "D_h_sigma", "eigenvalue_constant"}
    if field.startswith("tauberian_strip_"):
        result |= {"strip_terms", "remainder_orders", "simple_pole", "positive_residue", "asymptotic_inversion"}
    if field.startswith("primorial_maximal_"):
        result |= {"subcritical_coefficient", "mertens_regime", "supercritical_limit"}
    if field.startswith("free_UFD_clone_"):
        result |= {"saturated_formula", "modulo_formula", "similarity_formula", "commutator_formula"}
    return result


def stripped_factor_rows_p(family: dict) -> list[dict]:
    return [{"prime": entry["prime"], "lower": entry["lower"], "upper": entry["upper"]} for entry in family["local_factors"]]


def audit_certificate(record: dict, case: dict, proof_text: str, proof_frozen: bool) -> tuple[bool, list[str]]:
    problems = []
    field, cid = case["theorem_field"], case["case_id"]
    try:
        if not proof_frozen:
            problems.append("ValueError:frozen proof bytes changed")
        if type(record) is not dict or set(record) != RECORD_FIELDS:
            raise ValueError("record exact keys")
        if (record["case_id"], record["evidence_type"], record["certificate_owner"], record["theorem_field"]) != (
                cid, "INFINITE_THEOREM_CERTIFICATE", "B", field):
            raise ValueError("record identity")
        if (type(record["strict_domain_expression"]) is not str or not record["strict_domain_expression"] or
                type(record["endpoint_witness_type"]) is not str or not record["endpoint_witness_type"]):
            raise ValueError("domain/witness scalar")
        payload = strict_parse_text(record["certificate_value"])
        if canonical(payload) != record["certificate_value"]:
            raise ValueError("payload RFC8785/JCS")
        if type(payload) is not dict or set(payload) != expected_payload_keys_p(field):
            raise ValueError("payload recursive exact keys")
        if (payload["schema_version"], payload["case_id"], payload["theorem_field"]) != (
                "paper45.analytic-certificate-payload.v3", cid, field):
            raise ValueError("payload identity")
        if payload["endpoint_samples"] != case.get("samples_sigma", []):
            raise ValueError("endpoint provenance")
        heading = heading_prefix_p(field)
        typed_semantics = typed_proof_semantics_p(proof_text, heading)
        expected_domain, expected_witness, expected_conclusion = derive_certificate_metadata_p(field, typed_semantics)
        if (record["strict_domain_expression"] != expected_domain or
                record["endpoint_witness_type"] != expected_witness or
                payload["endpoint_witness"] != expected_witness or
                payload["conclusion_label"] != expected_conclusion or payload["proof_heading"] != heading):
            raise ValueError("typed proof-derived domain/witness/conclusion")
        expected_bindings = proof_bindings_p(proof_text, heading)
        if payload["proof_bindings"] != expected_bindings:
            raise ValueError("proof section byte/semantic AST binding")
        expected_specs = expected_families_p(case)
        expected_ids = [f"{name}:h={h}:sigma={sigma}" for name, _tree, sigma, h in expected_specs]
        if payload["formula_ast"] != expected_formula_p(case, expected_ids):
            raise ValueError("independently rebuilt theorem AST")
        families = payload["analytic_families"]
        if type(families) is not list or len(families) != len(expected_specs):
            raise ValueError("analytic family exact coverage")
        products: dict[str, mp.mpf] = {}
        by_kind: dict[str, list[dict]] = {}
        with mp.workdps(320):
            for family, (kind, expected_local, sigma_text, h) in zip(families, expected_specs):
                family_id = f"{kind}:h={h}:sigma={sigma_text}"
                if type(family) is not dict or set(family) != {
                        "family_id", "operation_ast", "operation_ast_sha256", "local_factors",
                        "partial_product_certified_interval"}:
                    raise ValueError("family exact keys")
                expected_operation = {"op": "EULER_PRODUCT", "index_variable": "p",
                                      "prime_sample": [str(prime) for prime in PRIME_SAMPLE],
                                      "local_factor": expected_local}
                if family["family_id"] != family_id or family["operation_ast"] != expected_operation:
                    raise ValueError("indexed family AST identity")
                if family["operation_ast_sha256"] != digest(canonical(expected_operation).encode()):
                    raise ValueError("family AST hash")
                rows = family["local_factors"]
                if type(rows) is not list or len(rows) != len(PRIME_SAMPLE):
                    raise ValueError("indexed factor coverage")
                values = []
                local_hash = digest(canonical(expected_local).encode())
                for index, (prime, row) in enumerate(zip(PRIME_SAMPLE, rows)):
                    expected_parameters = family_parameters_p(case, sigma_text, h, prime)
                    if type(row) is not dict or set(row) != {
                            "index", "prime", "parameters", "operation_ast", "operation_ast_sha256",
                            "lower", "upper", "precision_bits", "method_id"}:
                        raise ValueError("factor recursive exact keys")
                    if (row["index"] != str(index) or row["prime"] != str(prime) or
                            row["parameters"] != expected_parameters or row["operation_ast"] != expected_local or
                            row["operation_ast_sha256"] != local_hash or row["precision_bits"] != 768 or
                            row["method_id"] != "B:ANALYTIC_AST_IV_260DPS:" + kind):
                        raise ValueError("factor provenance/AST")
                    point = evaluate_expression_p(expected_local, expected_parameters)
                    point_box = {name: row[name] for name in ("lower", "upper", "precision_bits", "method_id")}
                    if not decimal_interval_contains(point_box, point, 230):
                        raise ValueError("250dps local containment")
                    values.append(point)
                product = mp.mpf(1)
                for point in reversed(values):
                    product *= point
                partial = family["partial_product_certified_interval"]
                if (type(partial) is not dict or set(partial) != {"lower", "upper", "precision_bits", "method_id"} or
                        partial["precision_bits"] != 768 or
                        partial["method_id"] != "B:ANALYTIC_AST_PRODUCT_IV_260DPS:" + kind or
                        not decimal_interval_contains(partial, product, 230)):
                    raise ValueError("250dps partial-product containment")
                products[family_id] = product
                by_kind.setdefault(kind, []).append(family)

            primary = families[-1]
            if field.startswith("power_schatten_"):
                primary = by_kind["POWER_S"][-1]
            elif field.startswith("commutator_") or field.startswith("h_ge_3_commutator_") or field.startswith("h2_commutator_"):
                primary = by_kind["COMMUTATOR_PRODUCT_A"][-1]
            elif field.startswith("tauberian_strip_") or field.startswith("C_D_and_eigenvalue_"):
                primary = by_kind["WEYL_C"][-1]
            elif field.startswith("C_and_D_equal_"):
                primary = by_kind["CROSSOVER_C"][0]
            elif field.startswith("free_UFD_clone_"):
                primary = by_kind["FREE_UFD_SATURATED_MASS"][-1]
            if (payload["local_euler_factors"] != stripped_factor_rows_p(primary) or
                    payload["partial_product_certified_interval"] != primary["partial_product_certified_interval"]):
                raise ValueError("primary family compatibility closure")

            if field.startswith("power_schatten_"):
                if (payload["power_s_local_factors"] != stripped_factor_rows_p(by_kind["POWER_S"][-1]) or
                        payload["power_m_local_factors"] != stripped_factor_rows_p(by_kind["POWER_M"][-1])):
                    raise ValueError("power S/M exact family closure")
            commutator = (field.startswith("commutator_") or field.startswith("h_ge_3_commutator_") or
                          field.startswith("h2_commutator_"))
            if commutator:
                first, second = by_kind["COMMUTATOR_PRODUCT_A"][-1], by_kind["COMMUTATOR_PRODUCT_B"][-1]
                if (payload["first_product_local_factors"] != stripped_factor_rows_p(first) or
                        payload["second_product_local_factors"] != stripped_factor_rows_p(second)):
                    raise ValueError("commutator A/B factor closure")
                expected_difference_ast = times_p(qnode_p(2), {"op": "DIFFERENCE_OF_PRODUCTS",
                                                               "minuend_family": first["family_id"],
                                                               "subtrahend_family": second["family_id"]})
                difference = payload["commutator_product_difference"]
                if (type(difference) is not dict or set(difference) != {"operation_ast", "operation_ast_sha256", "certified_interval"} or
                        difference["operation_ast"] != expected_difference_ast or
                        difference["operation_ast_sha256"] != digest(canonical(expected_difference_ast).encode()) or
                        not decimal_interval_contains(difference["certified_interval"],
                                                      2 * (products[first["family_id"]] - products[second["family_id"]]), 230)):
                    raise ValueError("commutator difference containment")

        family = "free_UFD_negative_control" if field.startswith("free_UFD_clone_") else "prime_exponent_Euler_Tauberian"
        if payload["derivation_family"] != family:
            raise ValueError("derivation family")

        if field.startswith(("tauberian_strip_", "C_D_and_eigenvalue_", "C_and_D_equal_")):
            c_kind = "CROSSOVER_C" if field.startswith("C_and_D_equal_") else "WEYL_C"
            d_kind = "CROSSOVER_D" if field.startswith("C_and_D_equal_") else "WEYL_D"
            e_kind = "CROSSOVER_EIGEN" if field.startswith("C_and_D_equal_") else "EIGENVALUE_CONSTANT"
            for key, operation, kind in (("C_h_sigma", "EULER_PRODUCT", c_kind),
                                         ("D_h_sigma", "EULER_PRODUCT", d_kind),
                                         ("eigenvalue_constant", "EULER_PRODUCT", e_kind)):
                expected = {"op": operation, "family_ids": [item["family_id"] for item in by_kind[kind]]}
                if payload[key] != expected:
                    raise ValueError("Weyl C/D/eigen closure")
        if field.startswith("tauberian_strip_"):
            h_node, sigma_node = variable_p("h"), variable_p("sigma")
            strip = {"op": "MAX", "operands": [ratio_p(qnode_p(1), h_node),
                                                   ratio_p(plus_p(qnode_p(1), negative_p(sigma_node)), plus_p(h_node, qnode_p(-1)))]}
            remainder = [{"op": "BIG_O", "exponent": negative_p(times_p(h_node, variable_p("Re_z")))},
                         {"op": "BIG_O", "exponent": negative_p(plus_p(times_p(plus_p(h_node, qnode_p(-1)), variable_p("Re_z")), sigma_node))}]
            expected_tauberian = {
                "strip_terms": strip,
                "remainder_orders": remainder,
                "simple_pole": {"op": "ZETA_QUOTIENT", "identity": "F_h_sigma(z)=zeta(z)*G_h_sigma(z)", "pole_at": "1"},
                "positive_residue": {"op": "EULER_PRODUCT", "constant": "C_h_sigma", "positive_measure": True},
                "asymptotic_inversion": {"op": "ASYMPTOTIC_INVERSION", "counting": "A_S(x)~C_h_sigma*x",
                                           "singular_values": "s_n~(C_h_sigma/n)^(sigma/2)"},
            }
            if any(payload[key] != value for key, value in expected_tauberian.items()):
                raise ValueError("Tauberian executable AST")
        if field.startswith("primorial_maximal_"):
            expected_primorial = {
                "subcritical_coefficient": {"op": "DIVIDE",
                    "numerator": exponentiate_p(plus_p(variable_p("h"), qnode_p(-1)), plus_p(variable_p("sigma"), qnode_p(-1))),
                    "denominator": times_p(qnode_p(2), plus_p(qnode_p(1), negative_p(variable_p("sigma"))))},
                "mertens_regime": {"op": "ASYMPTOTIC_EQUIVALENCE", "condition": "sigma=1", "value": "sqrt(exp(gamma)*log(log(x)))"},
                "supercritical_limit": {"op": "LIMIT", "condition": "sigma>1", "value": "sqrt(zeta(sigma))"},
            }
            if any(payload[key] != value for key, value in expected_primorial.items()):
                raise ValueError("primorial three-regime AST")
        if field.startswith("free_UFD_clone_"):
            h = int(case["h"])
            atoms = ["a_2", "a_3", "a_5", "a_7", "a_11"]
            expected_free = {
                "saturated_formula": {"op": "EULER_PRODUCT", "atom_namespace": atoms, "local_factor": saturated_mass_p()},
                "modulo_formula": {"op": "ZETA_QUOTIENT", "atom_namespace": atoms, "fiber_local_factor": modulo_mass_p(), "rational_prime_semantics": False},
                "similarity_formula": {"op": "EULER_PRODUCT", "atom_namespace": atoms, "local_factor": saturated_projection_p()},
                "commutator_formula": {"op": "DIFFERENCE_OF_PRODUCTS", "atom_namespace": atoms,
                                         "product_A_local": commutator_first_p(h), "product_B_local": commutator_second_p(h),
                                         "rational_prime_semantics": False},
            }
            if any(payload[key] != value for key, value in expected_free.items()):
                raise ValueError("free-UFD full negative-control clone")
        if record["proof_dependency_hash"] != dependency_hash(expected_bindings):
            raise ValueError("proof binding hash")
        if record["analytic_derivation_hash"] != derivation_hash(
                cid, record["strict_domain_expression"], record["endpoint_witness_type"], record["certificate_value"]):
            raise ValueError("analytic hash")
        if record["certificate_payload_sha256"] != record_payload_hash(record):
            raise ValueError("certificate hash")
    except Exception as exc:
        problems.append(type(exc).__name__ + ":" + str(exc))
    return not problems, problems


def audit(inputs: Path, b_path: Path) -> dict:
    contract_path = inputs / "EXPERIMENT_CONTRACT.json"
    contract = strict_parse_bytes(contract_path)
    semantic_code = semantic_input_code_p(contract)
    if semantic_code:
        raise SemanticRejectP(semantic_code)
    b = strict_parse_bytes(b_path)
    proof_path = inputs / "PROOF_PACKAGE.md"
    proof_bytes = proof_path.read_bytes()
    proof_text = proof_bytes.decode("utf-8")
    proof_frozen = digest(proof_bytes) == FROZEN_PROOF_SHA256
    source_text = (inputs / "SOURCE_LOCK.md").read_text(encoding="utf-8")
    if not all(token in proof_text for token in ("Wiener--Ikehara", "free-UFD", "Proposition 12")):
        raise RuntimeError("frozen proof dependency corpus")
    if "Abanin" not in source_text:
        raise RuntimeError("frozen source dependency corpus")
    ids = contract["infinite_coverage_gate"]["ordered_case_ids"]
    if (type(ids) is not list or len(ids) != 15 or len(set(ids)) != 15 or
            digest(("\n".join(ids) + "\n").encode()) != SET_HASH):
        raise RuntimeError("exact theorem set")
    cases = {case["case_id"]: case for case in contract["case_registry"]
             if case["evidence_type"] == "INFINITE_THEOREM_CERTIFICATE"}
    records = b.get("infinite_records")
    if (type(records) is not list or [item.get("case_id") for item in records] != ids or
            b.get("infinite_case_ids") != ids or b.get("producer") != "B"):
        raise RuntimeError("B exact theorem order")
    audits, findings = [], []
    for cid, record in zip(ids, records):
        passed, reasons = audit_certificate(record, cases[cid], proof_text, proof_frozen)
        verdict = "PASS" if passed else "HOLD"
        if reasons:
            findings.append("certificate closure failure:" + cid)
        audits.append({"case_id": cid, "certificate_owner": record.get("certificate_owner", "B"),
                       "audit_owner": "P", "certificate_payload_sha256": record["certificate_payload_sha256"],
                       "proof_dependency_hash": record["proof_dependency_hash"],
                       "analytic_derivation_hash": record["analytic_derivation_hash"], "verdict": verdict})
    overall = "PASS" if len(audits) == 15 and all(item["verdict"] == "PASS" for item in audits) else "HOLD"
    if (overall == "PASS") != (len(audits) == 15 and all(item["verdict"] == "PASS" for item in audits)):
        raise RuntimeError("verdict iff")
    return {"schema_version": "paper45.proof-audit.v2", "producer": "P",
            "contract_sha256": digest(contract_path.read_bytes()),
            "declared_infinite_case_set_sha256": SET_HASH, "audited_case_ids": ids,
            "per_case_audits": audits, "findings": findings, "verdict": overall}


def validate_audit_document(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    value = strict_parse_text(raw)
    top = {"schema_version", "producer", "contract_sha256", "declared_infinite_case_set_sha256",
           "audited_case_ids", "per_case_audits", "findings", "verdict"}
    if type(value) is not dict or set(value) != top or len(value.get("per_case_audits", [])) != 15:
        raise SemanticRejectP("P_AUDIT_FIELD_SET")
    per_case_pass = all(item.get("verdict") == "PASS" for item in value["per_case_audits"])
    if (value["verdict"] == "PASS") != per_case_pass or (value["verdict"] == "PASS") != (value["findings"] == []):
        raise SemanticRejectP("P_VERDICT_CLOSURE_BROKEN")
    if raw != json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n":
        raise SemanticRejectP("P_AUDIT_CANONICAL")
    return {"consumer": "P", "verdict": "PASS"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--b", type=Path)
    parser.add_argument("--emit", type=Path)
    parser.add_argument("--validate-audit", type=Path)
    ns = parser.parse_args()
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    try:
        if ns.validate_audit:
            result = validate_audit_document(ns.validate_audit)
        elif ns.b:
            result = audit(ns.inputs, ns.b)
        else:
            raise ValueError("B input required")
        encoded = json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n"
        if ns.emit:
            ns.emit.write_text(encoded, encoding="utf-8")
        else:
            sys.stdout.write(encoded)
        return 0
    except SemanticRejectP as exc:
        payload = {"consumer_key": "P", "outcome": "REJECT", "exit_code": 2,
                   "rejection_code": exc.code,
                   "result_digest": digest(("P\n" + exc.code + "\n").encode())}
        sys.stdout.write(json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")
        return 2
    except Exception:
        sys.stderr.write(json.dumps({"outcome": "HARNESS_ERROR", "exit_code": 3,
                                     "error": {"code": "INTERNAL_EXCEPTION", "stage": "P", "detail": "redacted"}},
                                    sort_keys=True, separators=(",", ":")) + "\n")
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
