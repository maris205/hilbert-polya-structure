#!/usr/bin/env python3
"""Strict recursive type, schema, raw-token, and coverage auditor T."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

import jsonschema
import mpmath as mp

EXPECTED_CONTRACT_SHA256 = "6ff3776a29b1211762b929782b556d0cae71a60ec97b102863059fc5bf302fbe"
EXPECTED_SCHEMA_SHA256 = "7052ec51bae97ec81da89404cfd63ac14a6f2e498729ad738d85b036792cc243"
EXPECTED_REGISTRY_SHA256 = "e212120010437f95996d3ff502d38ea527a3bd971bb7baa4f318d26d19ba1540"

class DuplicateMember(Exception):
    pass


class SemanticRejectT(Exception):
    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


T_ATTACKS = [
    (("case", "h"), 1, "INVALID_H"), (("case", "h"), "3/2", "H_NOT_INTEGER"),
    (("case", "k"), 0, "INVALID_POWER_K"), (("case", "q"), "0", "INVALID_SCHATTEN_Q"),
    (("case", "basis_index"), "0", "INVALID_BASIS_INDEX"), (("case", "label_m"), "12", "BLOCK_LABEL_NOT_H_FREE"),
    (("object", "J_h"), "all_prime_divisors", "SATURATED_SET_WRONG"),
    (("object", "retraction"), "swapped_with_old_formula", "RETRACTION_SWAP"),
    (("case", "sigma"), "complex_s", "SIGMA_COMPLEX_TYPE_ERROR"),
    (("object", "basis_weight"), "m^(-s/2)_before_fiber_sum", "WEIGHT_OWNER_CHANGED"),
    (("record", "evidence_type"), "INFINITE_THEOREM_CERTIFICATE", "FINITE_AS_INFINITE"),
    (("record", "nonzero_cyclic_atoms"), "include_block_kernel_zeros", "ZERO_EIGENVALUE_RETYPE"),
    (("case", "determinant_order_r"), "3/2", "DETERMINANT_ORDER_NOT_INTEGER"),
    (("case", "determinant_order_r"), 0, "DETERMINANT_ORDER_NONPOSITIVE"),
    (("record", "evidence_type"), "ANALYTIC_HEARSAY", "UNKNOWN_EVIDENCE_TAG"),
    (("comparison", "bool_int"), "python_equality", "STRICT_SCALAR_TYPE_FAILURE"),
    (("controls", "free_UFD"), "positive_prime_evidence", "FREE_UFD_POSITIVE_PRIME_EVIDENCE"),
    (("scope", "all_h"), False, "H2_SINGLETON_PAPER_ADMISSION"),
    (("record", "singular_value_type"), "eigenvalue", "SINGULAR_VALUE_RETYPE_AS_EIGENVALUE"),
    (("record", "riesz_norm_type"), "probability", "RIESZ_NORM_RETYPE_AS_PROBABILITY"),
    (("record", "finite_eigenvalue_encoding"), "rational_complexExact", "FINITE_EIGENVALUE_RATIONAL_COMPLEX_RETYPE"),
    (("record", "finite_eigenvalue_branch"), "PRINCIPAL_COMPLEX_LOG", "DIRICHLET_POWER_BRANCH_CHANGED"),
    (("infinite_coverage", "B", "exact_count"), 14, "B_INF_CASE_MISSING"),
    (("infinite_coverage", "B", "exact_count"), 16, "B_INF_CASE_EXTRA"),
    (("infinite_coverage", "B", "order"), "reordered", "B_INF_CASE_REORDERED"),
    (("infinite_coverage", "B", "membership"), "includes_INF_UNDECLARED", "B_INF_UNDECLARED_CASE"),
    (("infinite_coverage", "B", "certificate_owner"), "A", "B_CERTIFICATE_OWNER_CHANGED"),
    (("infinite_coverage", "A", "exact_count"), 1, "A_INF_RECORD_ADDED"),
    (("infinite_coverage", "P", "exact_count"), 14, "P_INF_CASE_MISSING"),
    (("infinite_coverage", "P", "exact_count"), 16, "P_INF_CASE_EXTRA"),
    (("infinite_coverage", "P", "order"), "reordered", "P_INF_CASE_REORDERED"),
    (("infinite_coverage", "P", "audit_owner"), "B", "P_AUDIT_OWNER_CHANGED"),
    (("infinite_coverage", "ordered_set_sha256"), "0" * 64, "INF_COVERAGE_SET_HASH_CHANGED"),
    (("infinite_coverage", "P", "hash_closure"), "accept_mismatch", "P_CERTIFICATE_HASH_CLOSURE_BROKEN"),
    (("infinite_coverage", "P", "verdict_closure"), "overall_independent_of_per_case", "P_VERDICT_CLOSURE_BROKEN"),
    (("record", "finite_eigenvalue_base_encoding"), "JSON_number_6.0", "AST_BASE_6_DOT_0_NUMBER"),
    (("record", "finite_eigenvalue_base_encoding"), "JSON_number_6e0", "AST_BASE_6E0_NUMBER"),
    (("record", "finite_eigenvalue_base_encoding"), "JSON_boolean_true", "AST_BASE_BOOLEAN_NUMERIC"),
    (("record", "finite_eigenvalue_rational_encoding"), "JSON_number_1.0_component", "AST_RATIONAL_COMPONENT_1_DOT_0_NUMBER"),
    (("raw_parser", "duplicate_members"), "last_win", "DUPLICATE_JSON_MEMBER_LAST_WIN"),
    (("raw_parser", "reordered_unique_members"), "reject_noncanonical_input_order", "REORDERED_AST_KEYS_FALSE_REJECT"),
    (("raw_parser", "noncanonical_stored_jcs"), "accept", "NONCANONICAL_AST_STORAGE_ACCEPTED"),
    (("record", "finite_eigenvalue_storage"), "trust_stored_hash_without_recompute", "AST_JCS_HASH_NOT_RECOMPUTED"),
]


def semantic_input_code_t(contract: dict):
    baseline = contract.get("mutation_baseline")
    if type(baseline) is not dict:
        return "CONTRACT_BASELINE_SHAPE"
    for path, attacked, code in T_ATTACKS:
        node = baseline
        try:
            for part in path:
                node = node[part]
        except (KeyError, TypeError):
            return "CONTRACT_BASELINE_SHAPE"
        if type(node) is type(attacked) and node == attacked:
            return code
    return None


def no_duplicate_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateMember(key)
        result[key] = value
    return result


def strict_raw_loads(raw: str):
    return json.loads(raw, object_pairs_hook=no_duplicate_pairs,
                      parse_constant=lambda _: (_ for _ in ()).throw(ValueError("constant")))


def jcs(obj) -> str:
    # Every accepted AST is string/object only, so JSON key ordering is the RFC8785 result.
    def reject_numbers(node):
        if type(node) in (float, int, bool):
            raise ValueError("numeric AST token")
        if type(node) is dict:
            for value in node.values():
                reject_numbers(value)
        elif type(node) is list:
            for value in node:
                reject_numbers(value)
        elif type(node) is not str:
            raise ValueError("AST type")
    reject_numbers(obj)
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def canonical_integer_string(value: str, positive: bool) -> bool:
    if type(value) is not str:
        return False
    pattern = r"[1-9][0-9]*" if positive else r"-?(0|[1-9][0-9]*)"
    return re.fullmatch(pattern, value) is not None and value != "-0"


def validate_ast(ast: dict):
    if type(ast) is not dict or set(ast) != {"node_type", "base", "exponent", "log_branch"}:
        return "AST_OBJECT_SHAPE"
    if ast["node_type"] != "DIRICHLET_POWER" or ast["log_branch"] != "REAL_LOG_POSITIVE_BASE":
        return "AST_BRANCH_OR_TYPE"
    if not canonical_integer_string(ast["base"], True):
        return "AST_POSITIVE_INTEGER_STRING_REQUIRED"
    exp = ast["exponent"]
    if type(exp) is not dict or set(exp) != {"real", "imag"}:
        return "AST_OBJECT_SHAPE"
    for part in (exp["real"], exp["imag"]):
        if type(part) is not dict or set(part) != {"numerator", "denominator"}:
            return "AST_OBJECT_SHAPE"
        if not canonical_integer_string(part["numerator"], False):
            return "AST_CANONICAL_SIGNED_INTEGER_STRING_REQUIRED"
        if not canonical_integer_string(part["denominator"], True):
            return "AST_POSITIVE_INTEGER_STRING_REQUIRED"
        f = Fraction(int(part["numerator"]), int(part["denominator"]))
        if str(f.numerator) != part["numerator"] or str(f.denominator) != part["denominator"]:
            return "AST_REDUCED_RATIONAL_REQUIRED"
    return "NONE"


def serialization_grid(contract: dict):
    outcomes = []
    for case in contract["serialization_case_grid"]:
        cid, raw = case["case_id"], case["raw_json"]
        code = "NONE"
        try:
            parsed = strict_raw_loads(raw)
            if cid == "NEG-AST-NONCANONICAL-STORED-JCS":
                actual = jcs(parsed["ast"])
                actual_hash = hashlib.sha256(actual.encode()).hexdigest()
                if parsed["canonical_jcs_utf8"] != actual or parsed["canonical_jcs_sha256"] != actual_hash:
                    code = "NONCANONICAL_AST_STORAGE"
            else:
                code = validate_ast(parsed)
        except DuplicateMember:
            code = "DUPLICATE_JSON_MEMBER"
            parsed = None
        except (ValueError, TypeError, KeyError, json.JSONDecodeError):
            code = "AST_POSITIVE_INTEGER_STRING_REQUIRED"
            parsed = None
        if case["expected_outcome"].startswith("ACCEPT"):
            accepted = code == "NONE"
            if accepted:
                canonical = jcs(parsed)
                accepted = hashlib.sha256(canonical.encode()).hexdigest() == case["expected_jcs_sha256"]
            if not accepted:
                raise ValueError("serialization positive:" + cid)
        elif code != case["expected_code"]:
            raise ValueError("serialization negative:" + cid + ":" + code)
        outcomes.append((cid, code))
    return outcomes


def semantic_contract(root: Path):
    inputs = root / "inputs" / "preauthority"
    contract = json.loads((inputs / "EXPERIMENT_CONTRACT.json").read_text())
    semantic_code = semantic_input_code_t(contract)
    if semantic_code:
        raise SemanticRejectT(semantic_code)
    if hashlib.sha256((inputs / "EXPERIMENT_CONTRACT.json").read_bytes()).hexdigest() != EXPECTED_CONTRACT_SHA256:
        raise ValueError("frozen contract digest")
    if hashlib.sha256((inputs / "EXPERIMENT_CONTRACT_SCHEMA.json").read_bytes()).hexdigest() != EXPECTED_SCHEMA_SHA256:
        raise ValueError("frozen schema digest")
    if hashlib.sha256((inputs / "MUTATION_REGISTRY.json").read_bytes()).hexdigest() != EXPECTED_REGISTRY_SHA256:
        raise ValueError("frozen registry digest")
    schema = json.loads((inputs / "EXPERIMENT_CONTRACT_SCHEMA.json").read_text())
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(schema).validate(contract)
    ids = [x["case_id"] for x in contract["case_registry"]]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate case")
    inf = sorted(x["case_id"] for x in contract["case_registry"] if x["evidence_type"] == "INFINITE_THEOREM_CERTIFICATE")
    gate = contract["infinite_coverage_gate"]
    if inf != gate["ordered_case_ids"] or hashlib.sha256(("\n".join(inf) + "\n").encode()).hexdigest() != gate["ordered_set_sha256"]:
        raise ValueError("infinite coverage")
    expected_paths = [x["path"] for x in contract["output_artifacts"]]
    if expected_paths != sorted(expected_paths) or len(expected_paths) != 8 or len(set(expected_paths)) != 8:
        raise ValueError("output whitelist")
    serialization_grid(contract)
    return contract, schema


def evaluate_ast_240(envelope: dict, box: dict):
    if type(envelope) is not dict or set(envelope) != {"ast", "canonical_jcs_utf8", "canonical_jcs_sha256"}:
        raise ValueError("AST envelope fields")
    ast = envelope["ast"]
    if validate_ast(ast) != "NONE":
        raise ValueError("AST grammar")
    canonical = jcs(ast)
    if envelope["canonical_jcs_utf8"] != canonical or hashlib.sha256(canonical.encode()).hexdigest() != envelope["canonical_jcs_sha256"]:
        raise ValueError("AST JCS/hash")
    base = int(ast["base"])
    real = Fraction(int(ast["exponent"]["real"]["numerator"]), int(ast["exponent"]["real"]["denominator"]))
    imag = Fraction(int(ast["exponent"]["imag"]["numerator"]), int(ast["exponent"]["imag"]["denominator"]))
    with mp.workdps(245):
        exponent = mp.mpc(mp.mpf(real.numerator) / real.denominator, mp.mpf(imag.numerator) / imag.denominator)
        expanded = mp.exp(exponent * mp.log(base)) if base != 1 else mp.mpc(1, 0)
        for value, interval_box in ((mp.re(expanded), box["real"]), (mp.im(expanded), box["imag"])):
            low, high = mp.mpf(interval_box["lower"]), mp.mpf(interval_box["upper"])
            if not low <= value <= high:
                raise ValueError("AST interval containment")


def exact_finite_order(contract: dict):
    result = []
    for case in contract["case_registry"]:
        if case["evidence_type"] == "FINITE_COMPRESSION":
            result.extend((case["case_id"], cutoff, bits) for cutoff, bits in zip(case["cutoffs"], contract["precision_bits"]))
        elif case["evidence_type"] == "FINITE_OPTIMIZATION":
            result.extend((case["case_id"], sigma, x) for sigma, x in zip(case["samples_sigma"], case["x_cutoffs"]))
    return result


def finite_identity(record: dict):
    if record["evidence_type"] == "FINITE_COMPRESSION":
        return record["case_id"], record["cutoff"], record["precision_bits"]
    return record["case_id"], record["sigma"], record["x_cutoff"]


def strict_interval(node: dict, bits: int):
    expected_width = {128: "1e-30", 256: "1e-60", 512: "1e-120"}[bits]
    if (type(node) is not dict or set(node) != {"lower", "upper", "precision_bits", "width_target", "method_id"} or
            type(node["lower"]) is not str or type(node["upper"]) is not str or
            type(node["precision_bits"]) is not int or node["precision_bits"] != bits or
            node["width_target"] != expected_width or type(node["method_id"]) is not str or not node["method_id"]):
        raise ValueError("strict interval fields")
    low, high, width = Decimal(node["lower"]), Decimal(node["upper"]), Decimal(expected_width)
    if not low.is_finite() or not high.is_finite() or low > high or high - low > width:
        raise ValueError("interval order/width")


def strict_finite_record(record: dict):
    if record["evidence_type"] == "FINITE_OPTIMIZATION":
        if (type(record["h"]) is not int or type(record["x_cutoff"]) is not int or
                any(type(record[name]) is not str for name in ("case_id", "evidence_type", "sigma", "maximizer_label", "primorial_label")) or
                type(record["tie_labels"]) is not list or any(type(item) is not str for item in record["tie_labels"])):
            raise ValueError("optimization strict types")
        return
    bits = record["precision_bits"]
    if (type(record["cutoff"]) is not int or type(bits) is not int or bits not in (128, 256, 512) or
            type(record["map_values"]) is not list or type(record["fiber_membership"]) is not dict or
            set(record["fiber_membership"]) != {"SATURATED", "MODULO"} or type(record["block_rank"]) is not dict or
            set(record["block_rank"]) != {"SATURATED", "MODULO"}):
        raise ValueError("finite strict root types")
    for item in record["map_values"]:
        if type(item) is not dict or set(item) != {"n", "tau_h", "omega_h"} or any(type(value) is not str for value in item.values()):
            raise ValueError("map value fields")
    for owner in ("SATURATED", "MODULO"):
        if (type(record["fiber_membership"][owner]) is not list or
                any(type(item) is not str for item in record["fiber_membership"][owner]) or
                type(record["block_rank"][owner]) is not int):
            raise ValueError("fiber/rank types")
        if type(record["finite_power_residual"][owner]) is not dict or set(record["finite_power_residual"][owner]) != {"real", "imag"}:
            raise ValueError("residual fields")
        for root_name in ("finite_singular_value_interval", "finite_riesz_norm_interval"):
            strict_interval(record[root_name][owner], bits)
        if type(record["finite_commutator_singular_intervals"][owner]) is not list or len(record["finite_commutator_singular_intervals"][owner]) != 2:
            raise ValueError("commutator interval cardinality")
        for interval in record["finite_commutator_singular_intervals"][owner]:
            strict_interval(interval, bits)
        eigen_box = record["finite_nonzero_eigenvalue_interval"][owner]
        if type(eigen_box) is not dict or set(eigen_box) != {"real", "imag"}:
            raise ValueError("eigen interval fields")
        strict_interval(eigen_box["real"], bits)
        strict_interval(eigen_box["imag"], bits)


def validate_results(root: Path, results: Path):
    contract, schema = semantic_contract(root)
    defs = schema["$defs"]
    mapping = {"evaluator_a.json": "scienceProjection", "evaluator_b.json": "scienceProjection",
               "proof_auditor_p.json": "proofAudit", "comparator_x.json": "comparisonReport",
               "mutation_outcomes.json": "mutationBundle",
               "evaluation_report.json": "evaluationReport"}
    for filename, definition in mapping.items():
        raw = (results / filename).read_text(encoding="utf-8")
        data = strict_raw_loads(raw)
        if raw != json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n":
            raise ValueError("result canonical bytes:" + filename)
        wrapper = {"$schema": "https://json-schema.org/draft/2020-12/schema", "$ref": f"#/$defs/{definition}", "$defs": defs}
        jsonschema.Draft202012Validator(wrapper).validate(data)
    integrity_raw = (results / "integrity_audit.json").read_text(encoding="utf-8")
    integrity = strict_raw_loads(integrity_raw)
    if integrity_raw != json.dumps(integrity, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n":
        raise ValueError("integrity canonical bytes")
    validate_integrity_v2(root, results, integrity)
    a = json.loads((results / "evaluator_a.json").read_text())
    b = json.loads((results / "evaluator_b.json").read_text())
    p = json.loads((results / "proof_auditor_p.json").read_text())
    ids = contract["infinite_coverage_gate"]["ordered_case_ids"]
    expected_order = exact_finite_order(contract)
    if [finite_identity(x) for x in a["finite_records"]] != expected_order or [finite_identity(x) for x in b["finite_records"]] != expected_order:
        raise ValueError("finite exact order/coverage")
    finite_keys = {"case_id", "evidence_type", "cutoff", "precision_bits", "map_values", "fiber_membership",
                   "block_rank", "finite_nonzero_eigenvalue", "finite_nonzero_eigenvalue_interval",
                   "finite_singular_value_interval", "finite_power_residual", "finite_riesz_norm_interval",
                   "finite_commutator_singular_intervals"}
    optimization_keys = {"case_id", "evidence_type", "h", "sigma", "x_cutoff", "maximizer_label", "primorial_label", "tie_labels"}
    for projection in (a, b):
        if set(projection) != {"schema_version", "producer", "contract_sha256", "declared_infinite_case_set_sha256",
                              "finite_records", "infinite_case_ids", "infinite_records"}:
            raise ValueError("science projection keys")
        if projection["contract_sha256"] != hashlib.sha256((root / "inputs/preauthority/EXPERIMENT_CONTRACT.json").read_bytes()).hexdigest():
            raise ValueError("contract hash")
        for record in projection["finite_records"]:
            if record["evidence_type"] == "FINITE_COMPRESSION":
                if set(record) != finite_keys:
                    raise ValueError("finite record keys/missing eigen interval")
                strict_finite_record(record)
                for owner in ("SATURATED", "MODULO"):
                    evaluate_ast_240(record["finite_nonzero_eigenvalue"][owner],
                                     record["finite_nonzero_eigenvalue_interval"][owner])
            elif set(record) != optimization_keys:
                raise ValueError("optimization keys")
            else:
                strict_finite_record(record)
    if a["infinite_case_ids"] != [] or a["infinite_records"] != []:
        raise ValueError("A infinite leak")
    if b["infinite_case_ids"] != ids or [x["case_id"] for x in b["infinite_records"]] != ids:
        raise ValueError("B coverage")
    if p["audited_case_ids"] != ids or [x["case_id"] for x in p["per_case_audits"]] != ids:
        raise ValueError("P coverage")
    infinite_record_keys = {"case_id", "evidence_type", "certificate_owner", "theorem_field",
                            "strict_domain_expression", "endpoint_witness_type", "certificate_value",
                            "proof_dependency_hash", "analytic_derivation_hash", "certificate_payload_sha256"}
    audit_keys = {"case_id", "certificate_owner", "audit_owner", "certificate_payload_sha256",
                  "proof_dependency_hash", "analytic_derivation_hash", "verdict"}
    if any(type(item) is not dict or set(item) != infinite_record_keys for item in b["infinite_records"]):
        raise ValueError("B certificate fields")
    if any(type(item) is not dict or set(item) != audit_keys for item in p["per_case_audits"]):
        raise ValueError("P audit fields")
    for br, pa in zip(b["infinite_records"], p["per_case_audits"]):
        for key in ("case_id", "certificate_owner", "certificate_payload_sha256", "proof_dependency_hash", "analytic_derivation_hash"):
            if br[key] != pa[key]:
                raise ValueError("B/P closure")
        if pa["audit_owner"] != "P":
            raise ValueError("P owner")
        payload = strict_raw_loads(br["certificate_value"])
        if br["certificate_value"] != json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False):
            raise ValueError("B analytic payload JCS")
        stripped = {key: val for key, val in br.items() if key != "certificate_payload_sha256"}
        if br["certificate_payload_sha256"] != hashlib.sha256(
                json.dumps(stripped, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest():
            raise ValueError("B payload hash")
    if (p["verdict"] == "PASS") != all(x["verdict"] == "PASS" for x in p["per_case_audits"]):
        raise ValueError("P iff")
    if (p["verdict"] == "PASS") != (p["findings"] == []):
        raise ValueError("P findings iff")
    x = json.loads((results / "comparator_x.json").read_text())
    if (x["verdict"] == "PASS") != (x["exact_mismatch_count"] == 0 and x["interval_mismatch_count"] == 0):
        raise ValueError("X verdict iff")
    outcomes = json.loads((results / "mutation_outcomes.json").read_text())
    if len(outcomes["outcomes"]) != 168:
        raise ValueError("mutation exact 168")
    if outcomes["contract_sha256"] != hashlib.sha256((root / "inputs/preauthority/EXPERIMENT_CONTRACT.json").read_bytes()).hexdigest():
        raise ValueError("mutation contract digest")
    if outcomes["registry_sha256"] != hashlib.sha256((root / "inputs/preauthority/MUTATION_REGISTRY.json").read_bytes()).hexdigest():
        raise ValueError("mutation registry digest")
    if outcomes["registry_sha256"] != EXPECTED_REGISTRY_SHA256 or outcomes["contract_sha256"] != EXPECTED_CONTRACT_SHA256:
        raise ValueError("immutable bundle digests")
    pairs = []
    for item in outcomes["outcomes"]:
        if (type(item) is not dict or set(item) != {"mutation_id", "consumer_key", "outcome", "exit_code",
                                                    "rejection_code", "result_digest"} or
                item["outcome"] != "REJECT" or type(item["exit_code"]) is not int or item["exit_code"] != 2 or
                re.fullmatch(r"M[0-9]{3}", item["mutation_id"]) is None or
                re.fullmatch(r"[0-9a-f]{64}", item["result_digest"]) is None):
            raise ValueError("mutation exact outcome fields")
        pairs.append((item["mutation_id"], item["consumer_key"]))
    if len(set(pairs)) != 168 or {item[0] for item in pairs} != {f"M{i:03d}" for i in range(1, 76)}:
        raise ValueError("mutation exact pair coverage")
    report = json.loads((results / "evaluation_report.json").read_text())
    closure = (x["verdict"] == "PASS" and p["verdict"] == "PASS" and report["mutation_survivors"] == 0 and
               report["infinite_coverage"]["b_p_id_match"] is True and
               report["infinite_coverage"]["b_p_owner_hash_closure"] is True)
    if ((report["c1"] == "PASS") != closure or (report["c2"] == "PASS") != closure or
            (report["infinite_coverage"]["verdict"] == "PASS") != (p["verdict"] == "PASS") or
            (report["external_disposition"] == "GO_EVALUATED") != closure):
        raise ValueError("evaluation verdict iff")
    return True


def validate_integrity_v2(root: Path, results: Path, value: dict):
    keys = {"schema_version", "producer", "contract_sha256", "exact_output_paths", "state_a", "state_b",
            "provenance", "manifest_verified", "path_policy_verified", "late_failure_identity_verified",
            "second_run_zero_replacements", "pre_io_containment_verified", "recursive_namespace_verified", "verdict"}
    if type(value) is not dict or set(value) != keys or value["schema_version"] != "paper45.integrity-report.v2" or value["producer"] != "G":
        raise ValueError("integrity top schema")
    exact_paths = ["results/SHA256SUMS.txt", "results/comparator_x.json", "results/evaluation_report.json",
                   "results/evaluator_a.json", "results/evaluator_b.json", "results/integrity_audit.json",
                   "results/mutation_outcomes.json", "results/proof_auditor_p.json"]
    if value["exact_output_paths"] != exact_paths or value["contract_sha256"] != EXPECTED_CONTRACT_SHA256:
        raise ValueError("integrity identity")
    booleans = [value[name] for name in ("manifest_verified", "path_policy_verified", "late_failure_identity_verified",
                                         "second_run_zero_replacements", "pre_io_containment_verified",
                                         "recursive_namespace_verified")]
    if any(type(item) is not bool for item in booleans) or (value["verdict"] == "PASS") != all(booleans):
        raise ValueError("integrity boolean iff")
    a, b = value["state_a"], value["state_b"]
    if (type(a) is not dict or set(a) != {"phase", "target_status", "pending"} or a["phase"] != "PREINSTALL" or
            [item.get("path") for item in a["pending"]] != exact_paths or len(a["pending"]) != 8):
        raise ValueError("state A")
    ledger_keys = {"path", "file_type", "mode", "sha256", "size_bytes", "mtime_ns"}
    if any(type(item) is not dict or set(item) != ledger_keys or item["file_type"] != "PENDING" for item in a["pending"]):
        raise ValueError("state A fields")
    if (type(b) is not dict or set(b) != {"phase", "actual", "self_excluding", "resolved_count"} or
            b["phase"] != "STAGED_VALIDATED" or b["resolved_count"] != 8 or len(b["actual"]) != 6 or
            b["self_excluding"] != [{"path": "results/integrity_audit.json", "reason": "SELF_HASH_CYCLE"},
                                     {"path": "results/SHA256SUMS.txt", "reason": "MANIFEST_SELF_EXCLUDING"}]):
        raise ValueError("state B")
    for item in b["actual"]:
        if (type(item) is not dict or set(item) != ledger_keys or item["file_type"] != "regular" or item["mode"] != "0444" or
                type(item["size_bytes"]) is not int or type(item["mtime_ns"]) is not int or
                re.fullmatch(r"[0-9a-f]{64}", item["sha256"]) is None):
            raise ValueError("state B fields")
        name = Path(item["path"]).name
        if name in {"integrity_audit.json", "SHA256SUMS.txt"}:
            raise ValueError("state B self cycle")
        target = results / name
        info = target.stat()
        if (hashlib.sha256(target.read_bytes()).hexdigest() != item["sha256"] or info.st_size != item["size_bytes"] or
                f"{info.st_mode & 0o7777:04o}" != item["mode"] or info.st_mtime_ns != item["mtime_ns"]):
            raise ValueError("state B physical closure")
    provenance = value["provenance"]
    pkeys = {"frozen_input_manifest_sha256", "experiment_contract_sha256", "experiment_contract_schema_sha256",
             "mutation_registry_sha256", "integration_contract_sha256", "route_expectation_sha256",
             "source_manifest_seals", "evaluator_output_seals"}
    if type(provenance) is not dict or set(provenance) != pkeys:
        raise ValueError("provenance keys")
    if (provenance["frozen_input_manifest_sha256"] != "4053f398c8318d09a821907ce421cb34a2adbe88efa2ac4dbfdc059e54d1e849" or
            provenance["experiment_contract_sha256"] != EXPECTED_CONTRACT_SHA256 or
            provenance["experiment_contract_schema_sha256"] != EXPECTED_SCHEMA_SHA256 or
            provenance["mutation_registry_sha256"] != EXPECTED_REGISTRY_SHA256 or
            provenance["route_expectation_sha256"] != "d02ce9f054567aa6d0c8e099797920ea9d29bbcebc062c4874b11baaab6b9c01"):
        raise ValueError("provenance digests")
    if provenance["integration_contract_sha256"] != hashlib.sha256((root / "code/contracts/INTEGRATION_CONTRACT.json").read_bytes()).hexdigest():
        raise ValueError("integration contract digest")
    manifest_names = ("A_SOURCE.sha256", "B_SOURCE.sha256", "P_SOURCE.sha256", "AUDITOR_SOURCE.sha256")
    if (type(provenance["source_manifest_seals"]) is not dict or set(provenance["source_manifest_seals"]) != set(manifest_names) or
            any(provenance["source_manifest_seals"][name] != hashlib.sha256((root / "code/manifests" / name).read_bytes()).hexdigest()
                for name in manifest_names)):
        raise ValueError("source manifest provenance")
    if provenance["evaluator_output_seals"] != {
            "A": hashlib.sha256((results / "evaluator_a.json").read_bytes()).hexdigest(),
            "B": hashlib.sha256((results / "evaluator_b.json").read_bytes()).hexdigest()}:
        raise ValueError("evaluator seal provenance")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--validate-results", type=Path)
    ns = ap.parse_args()
    try:
        if ns.validate_results:
            validate_results(ns.root, ns.validate_results)
        else:
            semantic_contract(ns.root)
        print(json.dumps({"consumer": "T", "verdict": "PASS"}, sort_keys=True, separators=(",", ":")))
        return 0
    except SemanticRejectT as exc:
        print(json.dumps({"consumer_key": "T", "outcome": "REJECT", "exit_code": 2,
                          "rejection_code": exc.code,
                          "result_digest": hashlib.sha256(("T\n" + exc.code + "\n").encode()).hexdigest()},
                         sort_keys=True, separators=(",", ":")))
        return 2
    except Exception:
        print(json.dumps({"outcome": "HARNESS_ERROR", "exit_code": 3,
                          "error": {"code": "SCHEMA_ERROR", "stage": "T", "detail": "redacted"}},
                         sort_keys=True, separators=(",", ":")))
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
