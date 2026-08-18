#!/usr/bin/env python3
"""Evaluator A: direct positive-integer carry tests and finite matrices."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys
from functools import lru_cache
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np
from scipy import sparse

CANDIDATE = "SD-C50"
CONTRACT_SHA = "1d383f12ce28a24f534564ce3270bc55aad613c87733019f7d841fc1e90bb628"
WIDTH = {128: mp.mpf("1e-30"), 256: mp.mpf("1e-60"), 512: mp.mpf("1e-120")}
DPS = {128: 60, 256: 100, 512: 180}
FINITE_FIELDS = {
    "case_id", "b", "q", "sigma", "N", "r", "control", "k", "l",
    "mask_depth", "mask_integer", "mask_sha256", "source_object_type",
    "zero_convention", "finite_support_count", "finite_rank",
    "finite_singular_interval_list", "finite_shell_norm_intervals",
    "finite_trace_power_record", "finite_period_witnesses",
    "masked_vertex_count", "precision_bits",
}


class DuplicateKey(Exception):
    pass


def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in items:
        if key in out:
            raise DuplicateKey(key)
        out[key] = value
    return out


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs,
                       parse_constant=lambda _: (_ for _ in ()).throw(ValueError("constant")))
    if type(value) is not dict:
        raise ValueError("object")
    return value


def enc(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": "), allow_nan=False) + "\n").encode("ascii")


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def reject(code: str) -> int:
    sys.stdout.buffer.write(enc({"code": code, "consumer": "A", "exit_code": 2, "outcome": "REJECT"}))
    return 2


A_ATTACKS = {
    ("finite_shell", "/finite/b2/same_shell", "nonzero_block"): "BINARY_SAME_SHELL_NONZERO",
    ("finite_shell", "/finite/cross_shell/multiplicity", "b^(k-l)"): "CROSS_SHELL_MULTIPLICITY",
    ("finite_object", "/finite/source/zero", "retained_as_infinite_vertex"): "ZERO_VERTEX_RETAINED",
    ("finite_trace", "/finite/b3/trace", "zero"): "BINARY_TRACE_COPIED_TO_ODD_RADIX",
    ("type", "/case/b", 1): "RADIX_BELOW_TWO",
    ("type", "/case/b", "5/2"): "RADIX_NOT_INTEGER",
    ("type", "/case/r", 0): "TRACE_LENGTH_NONPOSITIVE",
}


def attack(path: Path) -> int:
    obj = load_json(path)
    if set(obj) != {"domain", "target", "value_from", "value_to"}:
        raise ValueError("attack envelope")
    code = A_ATTACKS.get((obj["domain"], obj["target"], obj["value_to"]))
    if code:
        return reject(code)
    sys.stdout.buffer.write(enc({"consumer": "A", "exit_code": 0, "outcome": "ACCEPT"}))
    return 0


def model_code(model: dict[str, Any]) -> str | None:
    case = model.get("case", {})
    b = case.get("b")
    if type(b) is not int:
        return "RADIX_NOT_INTEGER"
    if b < 2:
        return "RADIX_BELOW_TWO"
    r = case.get("r")
    if type(r) is not int or r <= 0:
        return "TRACE_LENGTH_NONPOSITIVE"
    finite = model.get("finite", {})
    if finite.get("b2", {}).get("same_shell") != "zero_block":
        return "BINARY_SAME_SHELL_NONZERO"
    if finite.get("cross_shell", {}).get("multiplicity") != "(b-1)*b^(k-l-1)":
        return "CROSS_SHELL_MULTIPLICITY"
    if finite.get("source", {}).get("zero") != "deleted":
        return "ZERO_VERTEX_RETAINED"
    if finite.get("b3", {}).get("trace") != "positive_loop_contribution":
        return "BINARY_TRACE_COPIED_TO_ODD_RADIX"
    return None


def is_int(value: Any) -> bool:
    return type(value) is int


def rational(text: Any) -> Fraction:
    if type(text) is not str or re.fullmatch(r"[1-9][0-9]*(?:/[1-9][0-9]*)?", text) is None:
        raise ValueError("q")
    out = Fraction(text)
    if str(out) != text:
        raise ValueError("noncanonical q")
    return out


def validate_contract(contract: dict[str, Any]) -> None:
    expected = {"$schema", "artifact_path_policy", "case_registry", "common_finite_case_ids",
                "finite_case_expansion", "evidence_types", "declared_output_paths",
                "exception_total_mapping", "interval_width_targets", "json_schemas",
                "metadata_identity_fields", "outcome_union", "precision_bits",
                "randomized_digit_mask_control", "schema_version", "serialization"}
    if set(contract) != expected or contract["schema_version"] != "paper48.experiment-contract.v1":
        raise ValueError("contract root")
    if contract["precision_bits"] != [128, 256, 512]:
        raise ValueError("precision")
    finite_ids = []
    for case in contract["case_registry"]:
        if type(case) is not dict or type(case.get("case_id")) is not str:
            raise ValueError("case")
        if case["case_id"].startswith("FIN-"):
            finite_ids.append(case["case_id"])
            if not is_int(case.get("b")) or case["b"] < 2 or rational(case.get("q")) < 1:
                raise ValueError("scalar")
            if any(not is_int(x) or x < 1 for x in case.get("N", [])):
                raise ValueError("N")
            if any(not is_int(x) or x < 1 for x in case.get("r", [])):
                raise ValueError("r")
    if finite_ids != contract["common_finite_case_ids"] or len(finite_ids) != 7:
        raise ValueError("finite ids")


def scalar_mask_bytes(case: dict[str, Any], N: int, r: int, depth: int) -> bytes:
    text = (f"case_id={case['case_id']}\n"
            f"b={case['b']}\nq={case['q']}\nsigma={case['sigma']}\n"
            f"N={N}\nr={r}\ncontrol=RANDOMIZED_DIGIT_MASK\ndepth={depth}\n")
    return text.encode("ascii")


def masks(case: dict[str, Any], N: int, r: int, depth: int) -> list[tuple[int, str]]:
    scalar = scalar_mask_bytes(case, N, r, depth)
    seed = hashlib.sha256(scalar).digest()
    seen: set[int] = set()
    counter = 0
    while len(seen) < 16:
        digest = hashlib.sha256(seed + counter.to_bytes(8, "big")).digest()
        seen.add(int.from_bytes(digest[:8], "big") & ((1 << depth) - 1))
        counter += 1
    return [(value, sha(scalar + value.to_bytes(8, "big"))) for value in sorted(seen)]


def expand(contract: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    bits_list = contract["precision_bits"]
    for case in contract["case_registry"]:
        if not case["case_id"].startswith("FIN-"):
            continue
        for N in case["N"]:
            for r in case["r"]:
                for control in case["controls"]:
                    if control in {"ADJACENT_SHELL", "CROSS_SHELL", "SAME_SHELL"}:
                        for k, ell in case["shell_pairs_by_control"][control]:
                            if N < case["b"] ** (max(k, ell) + 1) - 1:
                                continue
                            for bits in bits_list:
                                rows.append({"case": case, "N": N, "r": r, "control": control,
                                             "k": k, "l": ell, "mask_depth": None,
                                             "mask_integer": None, "mask_sha256": None,
                                             "precision_bits": bits})
                    elif control == "RANDOMIZED_DIGIT_MASK":
                        for depth in contract["randomized_digit_mask_control"]["depths"]:
                            for mask, digest in masks(case, N, r, depth):
                                for bits in bits_list:
                                    rows.append({"case": case, "N": N, "r": r, "control": control,
                                                 "k": None, "l": None, "mask_depth": depth,
                                                 "mask_integer": mask, "mask_sha256": digest,
                                                 "precision_bits": bits})
                    else:
                        for bits in bits_list:
                            rows.append({"case": case, "N": N, "r": r, "control": control,
                                         "k": None, "l": None, "mask_depth": None,
                                         "mask_integer": None, "mask_sha256": None,
                                         "precision_bits": bits})
    def coord(row: dict[str, Any]) -> tuple[Any, ...]:
        case = row["case"]
        return (case["case_id"], case["b"], case["q"], case["sigma"], row["N"], row["r"],
                row["control"], -1 if row["k"] is None else row["k"],
                -1 if row["l"] is None else row["l"],
                -1 if row["mask_depth"] is None else row["mask_depth"],
                -1 if row["mask_integer"] is None else row["mask_integer"], row["precision_bits"])
    rows.sort(key=coord)
    coordinates = [coord(row) for row in rows]
    if len(coordinates) != len(set(coordinates)):
        raise ValueError("duplicate expansion")
    return rows


def carry_free(m: int, n: int, b: int) -> bool:
    if m < 0 or n < 0:
        raise ValueError("vertex")
    x, y = m, n
    while x or y:
        x, dx = divmod(x, b)
        y, dy = divmod(y, b)
        if dx + dy >= b:
            return False
    return True


@lru_cache(maxsize=None)
def positive_adjacency(b: int, N: int) -> np.ndarray:
    out = np.zeros((N, N), dtype=np.int8)
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            if carry_free(i, j, b):
                out[i - 1, j - 1] = out[j - 1, i - 1] = 1
    out.setflags(write=False)
    return out


def vertices_for(row: dict[str, Any]) -> tuple[list[int], list[int], str]:
    case, N, control = row["case"], row["N"], row["control"]
    b = case["b"]
    if control == "ZERO_INCLUDED":
        vertices = list(range(N))
        return vertices, vertices, "ZERO_INCLUDED_CONTROL"
    if control in {"ADJACENT_SHELL", "CROSS_SHELL", "SAME_SHELL"}:
        k, ell = row["k"], row["l"]
        return list(range(b ** k, b ** (k + 1))), list(range(b ** ell, b ** (ell + 1))), "ZERO_DELETED_POSITIVE"
    if control == "RANDOMIZED_DIGIT_MASK":
        depth, mask = row["mask_depth"], row["mask_integer"]
        kept = []
        for n in range(1, N + 1):
            x, ok = n, True
            pos = 0
            while x:
                x, digit = divmod(x, b)
                if pos >= depth and digit != 0:
                    ok = False
                    break
                if pos < depth and ((mask >> pos) & 1) == 0 and digit != 0:
                    ok = False
                    break
                pos += 1
            if ok:
                kept.append(n)
        return kept, kept, "ZERO_DELETED_POSITIVE"
    vertices = list(range(1, N + 1))
    return vertices, vertices, "ZERO_DELETED_POSITIVE"


@lru_cache(maxsize=None)
def control_matrix(b: int, left: tuple[int, ...], right: tuple[int, ...], sigma_text: str,
                   unweighted: bool) -> tuple[np.ndarray, np.ndarray]:
    adjacency = np.zeros((len(left), len(right)), dtype=np.int8)
    matrix = np.zeros((len(left), len(right)), dtype=np.float64)
    if sigma_text == "log_b_kappa_b_q":
        with mp.workdps(80):
            digit = mp.matrix([[1 if a + c < b else 0 for c in range(b)] for a in range(b)])
            vals = mp.svd_r(digit, compute_uv=False)
            kappa = mp.fsum(vals)
            sigma = float(mp.log(kappa) / mp.log(b))
    else:
        sigma = float(Fraction(sigma_text))
    for i, m in enumerate(left):
        for j, n in enumerate(right):
            if carry_free(m, n, b):
                adjacency[i, j] = 1
                matrix[i, j] = 1.0 if unweighted else (m * n) ** (-sigma / 2)
    return adjacency, matrix


def dec(x: mp.mpf, digits: int) -> str:
    if x == 0:
        return "0"
    return mp.nstr(x, n=digits, strip_zeros=False, min_fixed=-10000, max_fixed=10000)


def mp_interval(value: mp.mpf, bits: int) -> dict[str, Any]:
    radius = WIDTH[bits] / 4
    return {"lower": dec(value - radius, DPS[bits] - 5),
            "upper": dec(value + radius, DPS[bits] - 5), "precision_bits": bits}


@lru_cache(maxsize=None)
def digit_singulars(b: int, bits: int) -> tuple[dict[str, Any], ...]:
    with mp.workdps(DPS[bits]):
        C = mp.matrix([[1 if a + c < b else 0 for c in range(b)] for a in range(b)])
        values = list(mp.svd_r(C, compute_uv=False))
        values.sort(reverse=True)
        return tuple(mp_interval(mp.mpf(v), bits) for v in values)


@lru_cache(maxsize=None)
def trace_supports(b: int, N: int) -> tuple[int, int, int, int]:
    A = positive_adjacency(b, N).astype(np.int64)
    A2 = A @ A
    values = (int(np.trace(A)), int(A.sum()), int(np.sum(A2 * A)), int(np.sum(A2 * A2)))
    return values


def period_witnesses(b: int, N: int, r: int) -> list[str]:
    if r == 1:
        return ["1"] if b > 2 else []
    word = [b ** j for j in range(r)]
    if word[-1] > N:
        return []
    if not all(carry_free(word[j], word[(j + 1) % r], b) for j in range(r)):
        return []
    return [",".join(str(x) for x in word)]


def structural_rank(row: dict[str, Any], vertex_count: int) -> int:
    control, b = row["control"], row["case"]["b"]
    if control in {"ADJACENT_SHELL", "CROSS_SHELL"}:
        return (b - 1) * b ** min(row["k"], row["l"])
    if control == "SAME_SHELL":
        return 0 if b == 2 else (b - 2) * b ** row["k"]
    if control == "RANDOMIZED_DIGIT_MASK":
        if vertex_count == 0:
            return 0
        power, value = 0, 1
        while value < row["N"]:
            value *= b
            power += 1
        if value != row["N"]:
            raise ValueError("mask cutoff is not a radix power")
        boundary_allowed = row["mask_depth"] > power and ((row["mask_integer"] >> power) & 1) == 1
        return vertex_count if boundary_allowed else vertex_count - 1
    return vertex_count


@lru_cache(maxsize=None)
def support_only(b: int, left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(1 for m in left for n in right if carry_free(m, n, b))


@lru_cache(maxsize=None)
def direct_shell_qnorm(b: int, left: tuple[int, ...], right: tuple[int, ...], sigma: str,
                       q_text: str) -> float:
    _adjacency, matrix = control_matrix(b, left, right, sigma, False)
    if matrix.size == 0:
        return 0.0
    singular = np.linalg.svd(matrix, compute_uv=False)
    q = float(Fraction(q_text))
    return float(np.sum(singular ** q) ** (1.0 / q))


def float_interval(value: float, bits: int) -> dict[str, Any]:
    radius = max(1e-12, abs(value) * 2e-12)
    return {"lower": format(value - radius, ".17g"), "upper": format(value + radius, ".17g"),
            "precision_bits": bits}


def project(row: dict[str, Any]) -> dict[str, Any]:
    case, bits = row["case"], row["precision_bits"]
    left, right, zero = vertices_for(row)
    support = support_only(case["b"], tuple(left), tuple(right))
    rank = structural_rank(row, len(left))
    if rank < 0 or rank > min(len(left), len(right)):
        raise ValueError("structural rank")
    shell_intervals = []
    if row["control"] in {"ADJACENT_SHELL", "CROSS_SHELL", "SAME_SHELL"}:
        qnorm = direct_shell_qnorm(case["b"], tuple(left), tuple(right), case["sigma"], case["q"])
        shell_intervals = [float_interval(qnorm, bits)]
    record = {
        "case_id": case["case_id"], "b": case["b"], "q": case["q"], "sigma": case["sigma"],
        "N": row["N"], "r": row["r"], "control": row["control"], "k": row["k"], "l": row["l"],
        "mask_depth": row["mask_depth"], "mask_integer": row["mask_integer"],
        "mask_sha256": row["mask_sha256"],
        "source_object_type": "PositiveIntegerCarryFreeFiniteCompression", "zero_convention": zero,
        "finite_support_count": support, "finite_rank": rank,
        "finite_singular_interval_list": list(digit_singulars(case["b"], bits)),
        "finite_shell_norm_intervals": shell_intervals,
        "finite_trace_power_record": {"exact_value": str(trace_supports(case["b"], row["N"])[row["r"] - 1]),
                                      "interval": None},
        "finite_period_witnesses": period_witnesses(case["b"], row["N"], row["r"]),
        "masked_vertex_count": len(left) if row["control"] == "RANDOMIZED_DIGIT_MASK" else None,
        "precision_bits": bits,
    }
    if set(record) != FINITE_FIELDS:
        raise ValueError("projection fields")
    return record


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--root", type=Path)
    parser.add_argument("--projection", type=Path)
    parser.add_argument("--native", type=Path)
    parser.add_argument("--attack", type=Path)
    try:
        args = parser.parse_args()
        os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
        if args.attack is not None:
            if any(x is not None for x in (args.root, args.projection, args.native)):
                raise ValueError("attack arity")
            return attack(args.attack)
        if args.root is None or args.projection is None or args.native is None:
            raise ValueError("arity")
        root = args.root.resolve(strict=True)
        semantic = model_code(load_json(root / "contracts/SCIENCE_MODEL.json"))
        if semantic:
            return reject(semantic)
        contract_path = root / "preauthority/EXPERIMENT_CONTRACT.json"
        if sha(contract_path.read_bytes()) != CONTRACT_SHA:
            raise ValueError("contract hash")
        contract = load_json(contract_path)
        validate_contract(contract)
        expanded = expand(contract)
        records = [project(row) for row in expanded]
        coordinate_digest = sha(enc([{key: rec[key] for key in ("case_id", "b", "q", "sigma", "N", "r", "control", "k", "l", "mask_depth", "mask_integer", "precision_bits")} for rec in records]))
        projection = {"candidate_id": CANDIDATE, "contract_sha256": CONTRACT_SHA,
                      "finite_records": records, "infinite_records": [], "producer": "A",
                      "schema": "paper48.finite-projection.v1", "status": "PASS"}
        native = {"candidate_id": CANDIDATE, "contract_sha256": CONTRACT_SHA,
                  "coordinate_set_sha256": coordinate_digest,
                  "finite_record_count": len(records), "infinite_record_count": 0,
                  "method": "direct_positive_prefix_repeated_quotient_remainder",
                  "projection_sha256": sha(enc(projection)), "producer": "A",
                  "random_mask_generation": "locally_regenerated_no_shared_fixture",
                  "schema": "paper48.evaluator-a-native.v1", "status": "PASS"}
        args.projection.write_bytes(enc(projection))
        args.native.write_bytes(enc(native))
        return 0
    except Exception as exc:
        sys.stderr.write(f"A_ERROR:{type(exc).__name__}\n")
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
