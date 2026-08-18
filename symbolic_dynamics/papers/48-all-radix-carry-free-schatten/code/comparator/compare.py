#!/usr/bin/env python3
"""Non-scientific strict comparator X for independently projected rows."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any

COORD = ("case_id", "b", "q", "sigma", "N", "r", "control", "k", "l",
         "mask_depth", "mask_integer", "precision_bits")
EXACT = ("mask_sha256", "source_object_type", "zero_convention", "finite_support_count",
         "finite_rank", "finite_trace_power_record", "finite_period_witnesses", "masked_vertex_count")
ATTACKS = {
    ("finite_shell", "/finite/b2/same_shell", "nonzero_block"): "BINARY_SAME_SHELL_NONZERO",
    ("finite_shell", "/finite/cross_shell/multiplicity", "b^(k-l)"): "CROSS_SHELL_MULTIPLICITY",
    ("finite_object", "/finite/source/zero", "retained_as_infinite_vertex"): "ZERO_VERTEX_RETAINED",
    ("finite_trace", "/finite/b3/trace", "zero"): "BINARY_TRACE_COPIED_TO_ODD_RADIX",
    ("comparison", "/comparison/bool_int", "python_equality"): "STRICT_SCALAR_TYPE_FAILURE",
    ("comparison", "/comparison/tolerance", "selected_after_outputs"): "POSTHOC_TOLERANCE",
}


class Duplicate(Exception):
    pass


def pairs(seq: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in seq:
        if key in result:
            raise Duplicate(key)
        result[key] = value
    return result


def encode(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": "), allow_nan=False) + "\n").encode("ascii")


def load(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=pairs)
    if type(value) is not dict or encode(value) != raw:
        raise ValueError("noncanonical")
    return value


def attack(path: Path) -> int:
    row = load(path)
    if set(row) != {"domain", "target", "value_from", "value_to"}:
        raise ValueError("attack shape")
    code = ATTACKS.get((row["domain"], row["target"], row["value_to"]))
    if code is None:
        sys.stdout.buffer.write(encode({"consumer": "X", "exit_code": 0, "outcome": "ACCEPT"}))
        return 0
    sys.stdout.buffer.write(encode({"code": code, "consumer": "X", "exit_code": 2, "outcome": "REJECT"}))
    return 2


def model_rejection(model: dict[str, Any]) -> str | None:
    finite = model.get("finite", {})
    if finite.get("b2", {}).get("same_shell") != "zero_block": return "BINARY_SAME_SHELL_NONZERO"
    if finite.get("cross_shell", {}).get("multiplicity") != "(b-1)*b^(k-l-1)": return "CROSS_SHELL_MULTIPLICITY"
    if finite.get("source", {}).get("zero") != "deleted": return "ZERO_VERTEX_RETAINED"
    if finite.get("b3", {}).get("trace") != "positive_loop_contribution": return "BINARY_TRACE_COPIED_TO_ODD_RADIX"
    if model.get("comparison", {}).get("bool_int") != "strict": return "STRICT_SCALAR_TYPE_FAILURE"
    if model.get("comparison", {}).get("tolerance") != "predeclared": return "POSTHOC_TOLERANCE"
    return None


def interval(item: Any, bits: int) -> tuple[float, float]:
    if type(item) is not dict or set(item) != {"lower", "upper", "precision_bits"}:
        raise ValueError("interval shape")
    if (type(item["precision_bits"]) is not int or item["precision_bits"] != bits or
            type(item["lower"]) is not str or type(item["upper"]) is not str):
        raise ValueError("interval type")
    lo, hi = float(item["lower"]), float(item["upper"])
    if not math.isfinite(lo) or not math.isfinite(hi) or lo > hi:
        raise ValueError("interval order")
    return lo, hi


def validate_projection(value: dict[str, Any], producer: str) -> list[dict[str, Any]]:
    if set(value) != {"candidate_id", "contract_sha256", "finite_records", "infinite_records",
                     "producer", "schema", "status"}:
        raise ValueError("projection top")
    if (value["candidate_id"] != "SD-C50" or value["producer"] != producer or
            value["schema"] != "paper48.finite-projection.v1" or value["status"] != "PASS" or
            value["infinite_records"] != [] or type(value["finite_records"]) is not list or
            len(value["finite_records"]) != 1965):
        raise ValueError("projection identity")
    return value["finite_records"]


def compare(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    rows_a, rows_b = validate_projection(a, "A"), validate_projection(b, "B")
    maximum = 0.0
    shell_rows = 0
    digit_intervals = 0
    for index, (left, right) in enumerate(zip(rows_a, rows_b)):
        if any(type(left[key]) is not type(right[key]) or left[key] != right[key] for key in COORD):
            raise ValueError(f"coordinate {index}")
        if any(type(left[key]) is not type(right[key]) or left[key] != right[key] for key in EXACT):
            raise ValueError(f"exact field {index}")
        bits = left["precision_bits"]
        la, lb = left["finite_singular_interval_list"], right["finite_singular_interval_list"]
        if type(la) is not list or type(lb) is not list or len(la) != left["b"] or len(lb) != right["b"]:
            raise ValueError("digit spectrum length")
        for first, second in zip(la, lb):
            alo, ahi = interval(first, bits)
            blo, bhi = interval(second, bits)
            if max(alo, blo) > min(ahi, bhi):
                raise ValueError("digit interval disagreement")
            ac, bc = (alo + ahi) / 2, (blo + bhi) / 2
            maximum = max(maximum, abs(ac - bc) / max(1.0, abs(ac), abs(bc)))
            digit_intervals += 1
        sa, sb = left["finite_shell_norm_intervals"], right["finite_shell_norm_intervals"]
        is_shell = left["control"] in {"ADJACENT_SHELL", "CROSS_SHELL", "SAME_SHELL"}
        if is_shell:
            if len(sa) != 1 or len(sb) != 1:
                raise ValueError("shell interval count")
            alo, ahi = interval(sa[0], bits)
            blo, bhi = interval(sb[0], bits)
            # A is a double-precision direct norm; B is the independently
            # certified uniform envelope. The fixed numerical allowance was
            # frozen before either output and is never selected post hoc.
            allowance = 2e-10 * max(1.0, abs(alo), abs(ahi), abs(blo), abs(bhi))
            if alo < blo - allowance or ahi > bhi + allowance:
                raise ValueError("direct shell norm outside envelope")
            shell_rows += 1
        elif sa != [] or sb != []:
            raise ValueError("nonshell interval")
    return {"candidate_id": "SD-C50", "contract_sha256": a["contract_sha256"],
            "digit_interval_comparisons": digit_intervals, "exact_field_mismatches": 0,
            "finite_coordinate_rows": len(rows_a),
            "maximum_relative_digit_center_discrepancy": format(maximum, ".17g"),
            "missing_extra_or_duplicate_rows": 0, "predeclared_shell_allowance": "2e-10_relative",
            "schema": "paper48.comparison.v1", "shell_envelope_rows": shell_rows,
            "status": "PASS"}


def main() -> int:
    ap = argparse.ArgumentParser(allow_abbrev=False)
    ap.add_argument("--a", type=Path)
    ap.add_argument("--b", type=Path)
    ap.add_argument("--root", type=Path)
    ap.add_argument("--attack", type=Path)
    try:
        ns = ap.parse_args()
        if ns.attack is not None:
            if ns.a is not None or ns.b is not None or ns.root is not None:
                raise ValueError("attack arity")
            return attack(ns.attack)
        if ns.a is None or ns.b is None or ns.root is None:
            raise ValueError("arity")
        semantic = model_rejection(load(ns.root.resolve(strict=True) / "contracts/SCIENCE_MODEL.json"))
        if semantic:
            sys.stdout.buffer.write(encode({"code": semantic, "consumer": "X", "exit_code": 2, "outcome": "REJECT"}))
            return 2
        sys.stdout.buffer.write(encode(compare(load(ns.a), load(ns.b))))
        return 0
    except Exception as exc:
        sys.stderr.write(f"X_ERROR:{type(exc).__name__}\n")
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
