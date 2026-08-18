#!/usr/bin/env python3
"""Comparator X reads sealed finite-only views; INF data is not an input type."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from pathlib import Path

import mpmath as mp


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def get_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class SemanticReject(Exception):
    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


X_ATTACKS = [
    (("comparison", "bool_int"), "python_equality", "STRICT_SCALAR_TYPE_FAILURE"),
    (("comparison", "tolerance"), "selected_after_outputs", "POSTHOC_TOLERANCE"),
    (("record", "singular_value_type"), "eigenvalue", "SINGULAR_VALUE_RETYPE_AS_EIGENVALUE"),
    (("record", "riesz_norm_type"), "probability", "RIESZ_NORM_RETYPE_AS_PROBABILITY"),
    (("record", "finite_eigenvalue_encoding"), "rational_complexExact", "FINITE_EIGENVALUE_RATIONAL_COMPLEX_RETYPE"),
    (("record", "finite_eigenvalue_branch"), "PRINCIPAL_COMPLEX_LOG", "DIRICHLET_POWER_BRANCH_CHANGED"),
    (("raw_parser", "noncanonical_stored_jcs"), "accept", "NONCANONICAL_AST_STORAGE_ACCEPTED"),
    (("record", "finite_eigenvalue_storage"), "trust_stored_hash_without_recompute", "AST_JCS_HASH_NOT_RECOMPUTED"),
]


def semantic_input_code_x(contract: dict):
    baseline = contract.get("mutation_baseline")
    if type(baseline) is not dict:
        return "CONTRACT_BASELINE_SHAPE"
    for path, attacked, code in X_ATTACKS:
        node = baseline
        try:
            for part in path:
                node = node[part]
        except (KeyError, TypeError):
            return "CONTRACT_BASELINE_SHAPE"
        if type(node) is type(attacked) and node == attacked:
            return code
    return None


def record_key(record: dict):
    if record["evidence_type"] == "FINITE_COMPRESSION":
        return record["case_id"], record["cutoff"], record["precision_bits"]
    return record["case_id"], record["sigma"], record["x_cutoff"]


def exact_projection(record: dict) -> dict:
    if record["evidence_type"] == "FINITE_OPTIMIZATION":
        return record
    exact_keys = ["case_id", "evidence_type", "cutoff", "precision_bits", "map_values", "fiber_membership",
                  "block_rank", "finite_nonzero_eigenvalue", "finite_power_residual"]
    return {k: record[k] for k in exact_keys}


def walk_intervals(record: dict):
    if record["evidence_type"] != "FINITE_COMPRESSION":
        return []
    roots = ["finite_nonzero_eigenvalue_interval", "finite_singular_value_interval",
             "finite_riesz_norm_interval", "finite_commutator_singular_intervals"]
    found = []

    def visit(path: str, node):
        if type(node) is dict and set(node) == {"lower", "upper", "precision_bits", "width_target", "method_id"}:
            found.append((path, node))
        elif type(node) is dict:
            for key in sorted(node):
                visit(path + "/" + key, node[key])
        elif type(node) is list:
            for i, item in enumerate(node):
                visit(path + "/" + str(i), item)
        else:
            raise ValueError("non-interval numerical leaf")

    for root in roots:
        visit(root, record[root])
    return found


def valid_interval(node: dict) -> bool:
    try:
        lo, hi, target = Decimal(node["lower"]), Decimal(node["upper"]), Decimal(node["width_target"])
    except (InvalidOperation, KeyError):
        return False
    return lo <= hi and hi - lo <= target and type(node["precision_bits"]) is int and type(node["method_id"]) is str


def independently_evaluate_ast(envelope: dict, box: dict) -> bool:
    if type(envelope) is not dict or set(envelope) != {"ast", "canonical_jcs_utf8", "canonical_jcs_sha256"}:
        return False
    ast = envelope["ast"]
    if type(ast) is not dict or set(ast) != {"node_type", "base", "exponent", "log_branch"}:
        return False
    if (ast.get("node_type") != "DIRICHLET_POWER" or ast.get("log_branch") != "REAL_LOG_POSITIVE_BASE" or
            type(ast.get("base")) is not str or re.fullmatch(r"[1-9][0-9]*", ast["base"]) is None or
            type(ast.get("exponent")) is not dict or set(ast["exponent"]) != {"real", "imag"}):
        return False
    for part in (ast["exponent"]["real"], ast["exponent"]["imag"]):
        if (type(part) is not dict or set(part) != {"numerator", "denominator"} or
                type(part["numerator"]) is not str or type(part["denominator"]) is not str or
                re.fullmatch(r"(?:0|[1-9][0-9]*|-[1-9][0-9]*)", part["numerator"]) is None or
                re.fullmatch(r"[1-9][0-9]*", part["denominator"]) is None):
            return False
        reduced = Fraction(int(part["numerator"]), int(part["denominator"]))
        if (str(reduced.numerator), str(reduced.denominator)) != (part["numerator"], part["denominator"]):
            return False
    canonical = json.dumps(ast, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    if canonical != envelope["canonical_jcs_utf8"] or sha(canonical.encode()) != envelope["canonical_jcs_sha256"]:
        return False
    try:
        base = int(ast["base"])
        real = Fraction(int(ast["exponent"]["real"]["numerator"]), int(ast["exponent"]["real"]["denominator"]))
        imag = Fraction(int(ast["exponent"]["imag"]["numerator"]), int(ast["exponent"]["imag"]["denominator"]))
        with mp.workdps(250):
            exponent = mp.mpc(mp.mpf(real.numerator) / real.denominator, mp.mpf(imag.numerator) / imag.denominator)
            value = mp.exp(exponent * mp.log(base)) if base != 1 else mp.mpc(1, 0)
            for component, observed in ((mp.re(value), box["real"]), (mp.im(value), box["imag"])):
                if not valid_interval(observed):
                    return False
                lower = mp.mpf(observed["lower"])
                upper = mp.mpf(observed["upper"])
                if not lower <= component <= upper:
                    return False
        return True
    except (KeyError, TypeError, ValueError, ZeroDivisionError):
        return False


def overlap(left: dict, right: dict) -> bool:
    return max(Decimal(left["lower"]), Decimal(right["lower"])) <= min(Decimal(left["upper"]), Decimal(right["upper"]))


def validate_comparison_report(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    report = json.loads(raw, object_pairs_hook=lambda pairs: _unique_pairs_x(pairs),
                        parse_constant=lambda _x: (_ for _ in ()).throw(ValueError("constant")))
    exact = {"schema_version", "producer", "contract_sha256", "finite_case_ids",
             "exact_mismatch_count", "interval_mismatch_count", "verdict"}
    if type(report) is not dict or set(report) != exact:
        raise SemanticReject("COMPARATOR_REPORT_FIELD_SET")
    if (type(report["exact_mismatch_count"]) is not int or type(report["interval_mismatch_count"]) is not int or
            report["exact_mismatch_count"] < 0 or report["interval_mismatch_count"] < 0):
        raise SemanticReject("STRICT_SCALAR_TYPE_FAILURE")
    closure = report["exact_mismatch_count"] == 0 and report["interval_mismatch_count"] == 0
    if (report["verdict"] == "PASS") != closure:
        raise SemanticReject("COMPARATOR_VERDICT_IFF")
    canonical = json.dumps(report, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n"
    if raw != canonical:
        raise SemanticReject("COMPARATOR_REPORT_CANONICAL")
    return report


def _unique_pairs_x(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate")
        result[key] = value
    return result


def compare(a_path: Path, b_path: Path, inputs: Path) -> dict:
    a, b = get_json(a_path), get_json(b_path)
    if set(a) != {"producer", "contract_sha256", "finite_records"} or set(b) != set(a):
        raise ValueError("finite-only view schema")
    if a["producer"] != "A" or b["producer"] != "B" or a["contract_sha256"] != b["contract_sha256"]:
        raise ValueError("view identity")
    ar, br = a["finite_records"], b["finite_records"]
    if len(ar) != 21 or len(br) != 21:
        raise SemanticReject("FINITE_COVERAGE_EXACT_21")
    contract = get_json(inputs / "EXPERIMENT_CONTRACT.json")
    semantic_code = semantic_input_code_x(contract)
    if semantic_code:
        raise SemanticReject(semantic_code)
    expected_keys = []
    for case in contract["case_registry"]:
        if case["evidence_type"] == "FINITE_COMPRESSION":
            expected_keys.extend((case["case_id"], cutoff, bits) for cutoff, bits in zip(case["cutoffs"], contract["precision_bits"]))
        elif case["evidence_type"] == "FINITE_OPTIMIZATION":
            expected_keys.extend((case["case_id"], sigma, x) for sigma, x in zip(case["samples_sigma"], case["x_cutoffs"]))
    akeys, bkeys = [record_key(x) for x in ar], [record_key(x) for x in br]
    if akeys != expected_keys or bkeys != expected_keys or len(set(akeys)) != 21:
        raise SemanticReject("FINITE_RECORD_ORDER_COVERAGE")
    exact_mismatch = 0
    interval_mismatch = 0
    for left, right in zip(ar, br):
        if type(left) is not dict or type(right) is not dict or exact_projection(left) != exact_projection(right):
            exact_mismatch += 1
        if left["evidence_type"] == "FINITE_COMPRESSION":
            expected_record_keys = {"case_id", "evidence_type", "cutoff", "precision_bits", "map_values", "fiber_membership",
                                    "block_rank", "finite_nonzero_eigenvalue", "finite_nonzero_eigenvalue_interval",
                                    "finite_singular_value_interval", "finite_power_residual", "finite_riesz_norm_interval",
                                    "finite_commutator_singular_intervals"}
            if set(left) != expected_record_keys or set(right) != expected_record_keys:
                raise SemanticReject("FINITE_RECORD_FIELD_SET")
            for lane_record in (left, right):
                for owner in ("SATURATED", "MODULO"):
                    if not independently_evaluate_ast(lane_record["finite_nonzero_eigenvalue"][owner],
                                                      lane_record["finite_nonzero_eigenvalue_interval"][owner]):
                        raise SemanticReject("AST_INTERVAL_CONTAINMENT_250DPS")
        li, ri = walk_intervals(left), walk_intervals(right)
        if [p for p, _ in li] != [p for p, _ in ri]:
            interval_mismatch += 1
            continue
        for (_, lint), (_, rint) in zip(li, ri):
            if not valid_interval(lint) or not valid_interval(rint) or lint["precision_bits"] != rint["precision_bits"] or not overlap(lint, rint):
                interval_mismatch += 1
    case_ids = []
    for item in ar:
        if item["case_id"] not in case_ids:
            case_ids.append(item["case_id"])
    contract_sha = sha((inputs / "EXPERIMENT_CONTRACT.json").read_bytes())
    verdict = "PASS" if exact_mismatch == 0 and interval_mismatch == 0 else "HOLD"
    return {"schema_version": "paper45.comparison-report.v1", "producer": "X", "contract_sha256": contract_sha,
            "finite_case_ids": case_ids, "exact_mismatch_count": exact_mismatch,
            "interval_mismatch_count": interval_mismatch, "verdict": verdict}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--inputs", type=Path, required=True)
    ap.add_argument("--a-finite", type=Path)
    ap.add_argument("--b-finite", type=Path)
    ap.add_argument("--emit", type=Path)
    ap.add_argument("--validate-report", type=Path)
    ns = ap.parse_args()
    if not ns.validate_report and (not ns.a_finite or not ns.b_finite):
        return 3
    try:
        result = (validate_comparison_report(ns.validate_report) if ns.validate_report else
                  compare(ns.a_finite, ns.b_finite, ns.inputs))
        raw = json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n"
        if ns.emit:
            ns.emit.write_text(raw, encoding="utf-8")
        else:
            sys.stdout.write(raw)
        return 0
    except SemanticReject as exc:
        result = {"outcome": "REJECT", "exit_code": 2, "consumer_key": "X", "rejection_code": exc.code,
                  "result_digest": sha(("X\n" + exc.code + "\n").encode())}
        sys.stdout.write(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")
        return 2
    except Exception:
        sys.stderr.write(json.dumps({"outcome": "HARNESS_ERROR", "exit_code": 3,
                                     "error": {"code": "INTERNAL_EXCEPTION", "stage": "X", "detail": "redacted"}},
                                    sort_keys=True, separators=(",", ":")) + "\n")
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
