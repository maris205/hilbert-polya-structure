#!/usr/bin/env python3
"""Evaluator B: independent digit automata and shell/Kronecker factors."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np

CID = "SD-C50"
CONTRACT_DIGEST = "1d383f12ce28a24f534564ce3270bc55aad613c87733019f7d841fc1e90bb628"
PRECISION_DPS = {128: 60, 256: 100, 512: 180}
TARGET_WIDTH = {128: "1e-30", 256: "1e-60", 512: "1e-120"}


class DuplicateMemberB(Exception):
    pass


def pair_object(sequence: list[tuple[str, Any]]) -> dict[str, Any]:
    answer: dict[str, Any] = {}
    for name, item in sequence:
        if name in answer:
            raise DuplicateMemberB(name)
        answer[name] = item
    return answer


def read_object(path: Path) -> dict[str, Any]:
    obj = json.loads(path.read_bytes().decode("utf-8"), object_pairs_hook=pair_object,
                     parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if obj.__class__ is not dict:
        raise ValueError("top object")
    return obj


def canonical(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2,
                       separators=(",", ": "), allow_nan=False) + "\n").encode("ascii")


def h256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


ATTACKS_B = {
    ("finite_shell", "/finite/b2/same_shell", "nonzero_block"): "BINARY_SAME_SHELL_NONZERO",
    ("finite_shell", "/finite/cross_shell/multiplicity", "b^(k-l)"): "CROSS_SHELL_MULTIPLICITY",
    ("finite_digit_matrix_and_endpoint", "/claims/tau_b", "tau_b=b"): "TAU_EQUALS_B_FALSE",
    ("finite_object", "/finite/source/zero", "retained_as_infinite_vertex"): "ZERO_VERTEX_RETAINED",
    ("finite_trace", "/finite/b3/trace", "zero"): "BINARY_TRACE_COPIED_TO_ODD_RADIX",
    ("type", "/case/b", 1): "RADIX_BELOW_TWO",
    ("type", "/case/b", "5/2"): "RADIX_NOT_INTEGER",
    ("type", "/case/r", 0): "TRACE_LENGTH_NONPOSITIVE",
}


def attack_mode(path: Path) -> int:
    row = read_object(path)
    if set(row) != {"domain", "target", "value_from", "value_to"}:
        raise ValueError("attack")
    code = ATTACKS_B.get((row["domain"], row["target"], row["value_to"]))
    if code is None:
        sys.stdout.buffer.write(canonical({"consumer": "B", "exit_code": 0, "outcome": "ACCEPT"}))
        return 0
    sys.stdout.buffer.write(canonical({"code": code, "consumer": "B", "exit_code": 2, "outcome": "REJECT"}))
    return 2


def model_rejection(model: dict[str, Any]) -> str | None:
    case = model.get("case", {})
    radix = case.get("b")
    if type(radix) is not int:
        return "RADIX_NOT_INTEGER"
    if radix < 2:
        return "RADIX_BELOW_TWO"
    length = case.get("r")
    if type(length) is not int or length <= 0:
        return "TRACE_LENGTH_NONPOSITIVE"
    finite = model.get("finite", {})
    if finite.get("b2", {}).get("same_shell") != "zero_block":
        return "BINARY_SAME_SHELL_NONZERO"
    if finite.get("cross_shell", {}).get("multiplicity") != "(b-1)*b^(k-l-1)":
        return "CROSS_SHELL_MULTIPLICITY"
    if model.get("claims", {}).get("tau_b") != "tau_b>b":
        return "TAU_EQUALS_B_FALSE"
    if finite.get("source", {}).get("zero") != "deleted":
        return "ZERO_VERTEX_RETAINED"
    if finite.get("b3", {}).get("trace") != "positive_loop_contribution":
        return "BINARY_TRACE_COPIED_TO_ODD_RADIX"
    return None


def qvalue(raw: Any) -> Fraction:
    if raw.__class__ is not str or re.fullmatch(r"[1-9][0-9]*(?:/[1-9][0-9]*)?", raw) is None:
        raise ValueError("q text")
    result = Fraction(raw)
    if str(result) != raw or result < 1:
        raise ValueError("q domain")
    return result


def preflight(contract: dict[str, Any]) -> None:
    if contract.get("schema_version") != "paper48.experiment-contract.v1":
        raise ValueError("schema")
    if contract.get("precision_bits") != [128, 256, 512]:
        raise ValueError("precision")
    finite = [item for item in contract.get("case_registry", []) if item.get("case_id", "").startswith("FIN-")]
    if len(finite) != 7 or [x["case_id"] for x in finite] != contract.get("common_finite_case_ids"):
        raise ValueError("coverage")
    for item in finite:
        if item.get("b").__class__ is not int or item["b"] < 2:
            raise ValueError("radix")
        qvalue(item.get("q"))
        if any(x.__class__ is not int or x < 1 for x in item.get("r", [])):
            raise ValueError("trace length")
        if any(x.__class__ is not int or x < 1 for x in item.get("N", [])):
            raise ValueError("prefix")


def mask_prefix(case: dict[str, Any], cutoff: int, power: int, depth: int) -> bytes:
    return ("case_id=" + case["case_id"] + "\n" +
            "b=" + str(case["b"]) + "\nq=" + case["q"] + "\nsigma=" + case["sigma"] + "\n" +
            "N=" + str(cutoff) + "\nr=" + str(power) + "\ncontrol=RANDOMIZED_DIGIT_MASK\n" +
            "depth=" + str(depth) + "\n").encode("ascii")


def mask_set(case: dict[str, Any], cutoff: int, power: int, depth: int) -> list[tuple[int, str]]:
    prefix = mask_prefix(case, cutoff, power, depth)
    seed = hashlib.sha256(prefix).digest()
    result: set[int] = set()
    counter = 0
    while len(result) != 16:
        block = hashlib.sha256(seed + int(counter).to_bytes(8, byteorder="big", signed=False)).digest()
        result.add(int.from_bytes(block[0:8], byteorder="big", signed=False) % (2 ** depth))
        counter += 1
    return [(m, h256(prefix + m.to_bytes(8, "big"))) for m in sorted(result)]


def independent_expansion(contract: dict[str, Any]) -> list[dict[str, Any]]:
    answer: list[dict[str, Any]] = []
    for spec in contract["case_registry"]:
        if not spec["case_id"].startswith("FIN-"):
            continue
        for cutoff in spec["N"]:
            for power in spec["r"]:
                for control in spec["controls"]:
                    shells = spec["shell_pairs_by_control"].get(control)
                    if shells is not None:
                        for first, second in shells:
                            if cutoff + 1 < spec["b"] ** (max(first, second) + 1):
                                continue
                            for precision in contract["precision_bits"]:
                                answer.append({"spec": spec, "N": cutoff, "r": power, "control": control,
                                               "k": first, "l": second, "mask_depth": None,
                                               "mask_integer": None, "mask_sha256": None,
                                               "precision_bits": precision})
                    elif control == "RANDOMIZED_DIGIT_MASK":
                        for depth in contract["randomized_digit_mask_control"]["depths"]:
                            for mask, digest in mask_set(spec, cutoff, power, depth):
                                for precision in contract["precision_bits"]:
                                    answer.append({"spec": spec, "N": cutoff, "r": power, "control": control,
                                                   "k": None, "l": None, "mask_depth": depth,
                                                   "mask_integer": mask, "mask_sha256": digest,
                                                   "precision_bits": precision})
                    else:
                        for precision in contract["precision_bits"]:
                            answer.append({"spec": spec, "N": cutoff, "r": power, "control": control,
                                           "k": None, "l": None, "mask_depth": None,
                                           "mask_integer": None, "mask_sha256": None,
                                           "precision_bits": precision})
    order = lambda x: (x["spec"]["case_id"], x["spec"]["b"], x["spec"]["q"], x["spec"]["sigma"],
                       x["N"], x["r"], x["control"], -1 if x["k"] is None else x["k"],
                       -1 if x["l"] is None else x["l"], -1 if x["mask_depth"] is None else x["mask_depth"],
                       -1 if x["mask_integer"] is None else x["mask_integer"], x["precision_bits"])
    answer.sort(key=order)
    keys = [order(item) for item in answer]
    if len(keys) != len(set(keys)):
        raise ValueError("duplicate")
    return answer


@lru_cache(maxsize=None)
def digits(n: int, b: int) -> tuple[int, ...]:
    if n == 0:
        return (0,)
    out: list[int] = []
    while n:
        out.append(n % b)
        n //= b
    return tuple(out)


def automaton_accepts(first: int, second: int, b: int) -> bool:
    x, y = digits(first, b), digits(second, b)
    length = max(len(x), len(y))
    return all((x[j] if j < len(x) else 0) + (y[j] if j < len(y) else 0) < b for j in range(length))


def selected_vertices(item: dict[str, Any]) -> tuple[list[int], list[int], str]:
    spec, control, N = item["spec"], item["control"], item["N"]
    b = spec["b"]
    if control == "ZERO_INCLUDED":
        sequence = list(range(0, N))
        return sequence, sequence, "ZERO_INCLUDED_CONTROL"
    if control in ("ADJACENT_SHELL", "CROSS_SHELL", "SAME_SHELL"):
        left = list(range(b ** item["k"], b ** (item["k"] + 1)))
        right = list(range(b ** item["l"], b ** (item["l"] + 1)))
        return left, right, "ZERO_DELETED_POSITIVE"
    if control == "RANDOMIZED_DIGIT_MASK":
        depth, mask = item["mask_depth"], item["mask_integer"]
        chosen = []
        for vertex in range(1, N + 1):
            ds = digits(vertex, b)
            legal = True
            for position, digit in enumerate(ds):
                if position >= depth and digit:
                    legal = False
                    break
                if position < depth and ((mask // (2 ** position)) % 2 == 0) and digit:
                    legal = False
                    break
            if legal:
                chosen.append(vertex)
        return chosen, chosen, "ZERO_DELETED_POSITIVE"
    sequence = list(range(1, N + 1))
    return sequence, sequence, "ZERO_DELETED_POSITIVE"


@lru_cache(maxsize=None)
def transition_table(b: int, left: tuple[int, ...], right: tuple[int, ...]) -> np.ndarray:
    table = np.fromiter((1 if automaton_accepts(i, j, b) else 0 for i in left for j in right),
                        dtype=np.int8, count=len(left) * len(right)).reshape((len(left), len(right)))
    table.setflags(write=False)
    return table


@lru_cache(maxsize=None)
def finite_support(b: int, left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return int(transition_table(b, left, right).sum())


def factor_rank(item: dict[str, Any], count: int) -> int:
    control, b = item["control"], item["spec"]["b"]
    if control in ("ADJACENT_SHELL", "CROSS_SHELL"):
        return (b - 1) * b ** min(item["k"], item["l"])
    if control == "SAME_SHELL":
        return (b - 2) * b ** item["k"] if b > 2 else 0
    if control == "RANDOMIZED_DIGIT_MASK":
        if count == 0:
            return 0
        boundary = 0
        radix_power = 1
        while radix_power != item["N"]:
            if radix_power > item["N"]:
                raise ValueError("non-power cutoff")
            radix_power *= b
            boundary += 1
        top_digit_is_present = (item["mask_depth"] > boundary and
                                (item["mask_integer"] // (2 ** boundary)) % 2 == 1)
        return count if top_digit_is_present else count - 1
    return count


def decimal(value: mp.mpf, digits_count: int) -> str:
    if value == 0:
        return "0"
    return mp.nstr(value, n=digits_count, strip_zeros=False, min_fixed=-10000, max_fixed=10000)


def small_interval(value: mp.mpf, bits: int) -> dict[str, Any]:
    epsilon = mp.mpf(TARGET_WIDTH[bits]) / 4
    return {"lower": decimal(value - epsilon, PRECISION_DPS[bits] - 5),
            "upper": decimal(value + epsilon, PRECISION_DPS[bits] - 5), "precision_bits": bits}


@lru_cache(maxsize=None)
def analytic_digit_spectrum(b: int, bits: int) -> tuple[dict[str, Any], ...]:
    with mp.workdps(PRECISION_DPS[bits]):
        values = [1 / (2 * mp.sin((2 * j - 1) * mp.pi / (4 * b + 2))) for j in range(1, b + 1)]
        return tuple(small_interval(value, bits) for value in values)


def kappa(d: int, q: Fraction) -> mp.mpf:
    if d == 0:
        return mp.mpf(0)
    values = [1 / (2 * mp.sin((2 * j - 1) * mp.pi / (4 * d + 2))) for j in range(1, d + 1)]
    exponent = mp.mpf(q.numerator) / q.denominator
    return mp.power(mp.fsum(mp.power(value, exponent) for value in values), 1 / exponent)


def sigma_numeric(spec: dict[str, Any]) -> mp.mpf:
    if spec["sigma"] == "log_b_kappa_b_q":
        return mp.log(kappa(spec["b"], qvalue(spec["q"]))) / mp.log(spec["b"])
    f = Fraction(spec["sigma"])
    return mp.mpf(f.numerator) / f.denominator


def shell_envelope(item: dict[str, Any]) -> list[dict[str, Any]]:
    if item["control"] not in ("ADJACENT_SHELL", "CROSS_SHELL", "SAME_SHELL"):
        return []
    spec, bits, first, second = item["spec"], item["precision_bits"], item["k"], item["l"]
    b, q = spec["b"], qvalue(spec["q"])
    with mp.workdps(PRECISION_DPS[bits]):
        if first == second:
            bare = kappa(b - 2, q) * mp.power(kappa(b, q), first)
        else:
            hi, lo = max(first, second), min(first, second)
            multiplicity = mp.mpf((b - 1) * b ** (hi - lo - 1))
            bare = mp.sqrt(multiplicity) * kappa(b - 1, q) * mp.power(kappa(b, q), lo)
        sigma = sigma_numeric(spec)
        upper = mp.power(b, -(first + second) * sigma / 2) * bare
        lower = mp.power(b, -sigma) * upper
        epsilon = mp.mpf(TARGET_WIDTH[bits]) / 4
        return [{"lower": decimal(max(mp.mpf(0), lower - epsilon), PRECISION_DPS[bits] - 5),
                 "upper": decimal(upper + epsilon, PRECISION_DPS[bits] - 5), "precision_bits": bits}]


@lru_cache(maxsize=None)
def closed_walk_counts(b: int, N: int) -> tuple[int, int, int, int]:
    sequence = tuple(range(1, N + 1))
    table = transition_table(b, sequence, sequence).astype(np.int64)
    square = table.dot(table)
    return (int(np.trace(table)), int(table.sum()), int(np.sum(square * table)), int(np.sum(square * square)))


def explicit_periods(b: int, N: int, r: int) -> list[str]:
    if r == 1:
        return ["1"] if b > 2 else []
    chosen = [b ** index for index in range(0, r)]
    if chosen[-1] > N:
        return []
    if any(not automaton_accepts(chosen[i], chosen[(i + 1) % r], b) for i in range(r)):
        return []
    return [",".join(map(str, chosen))]


def make_record(item: dict[str, Any]) -> dict[str, Any]:
    spec, bits = item["spec"], item["precision_bits"]
    left, right, zero = selected_vertices(item)
    support = finite_support(spec["b"], tuple(left), tuple(right))
    rank = factor_rank(item, len(left))
    if rank < 0 or rank > min(len(left), len(right)):
        raise ValueError("rank factor")
    record = {
        "N": item["N"], "b": spec["b"], "case_id": spec["case_id"], "control": item["control"],
        "finite_period_witnesses": explicit_periods(spec["b"], item["N"], item["r"]),
        "finite_rank": rank, "finite_shell_norm_intervals": shell_envelope(item),
        "finite_singular_interval_list": list(analytic_digit_spectrum(spec["b"], bits)),
        "finite_support_count": support,
        "finite_trace_power_record": {"exact_value": str(closed_walk_counts(spec["b"], item["N"])[item["r"] - 1]),
                                      "interval": None},
        "k": item["k"], "l": item["l"], "mask_depth": item["mask_depth"],
        "mask_integer": item["mask_integer"], "mask_sha256": item["mask_sha256"],
        "masked_vertex_count": len(left) if item["control"] == "RANDOMIZED_DIGIT_MASK" else None,
        "precision_bits": bits, "q": spec["q"], "r": item["r"], "sigma": spec["sigma"],
        "source_object_type": "PositiveIntegerCarryFreeFiniteCompression", "zero_convention": zero,
    }
    return record


def main() -> int:
    ap = argparse.ArgumentParser(allow_abbrev=False)
    ap.add_argument("--root", type=Path)
    ap.add_argument("--projection", type=Path)
    ap.add_argument("--native", type=Path)
    ap.add_argument("--attack", type=Path)
    try:
        ns = ap.parse_args()
        os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
        if ns.attack is not None:
            if any(value is not None for value in (ns.root, ns.projection, ns.native)):
                raise ValueError("attack arity")
            return attack_mode(ns.attack)
        if ns.root is None or ns.projection is None or ns.native is None:
            raise ValueError("arity")
        root = ns.root.resolve(strict=True)
        semantic = model_rejection(read_object(root / "contracts/SCIENCE_MODEL.json"))
        if semantic:
            sys.stdout.buffer.write(canonical({"code": semantic, "consumer": "B", "exit_code": 2, "outcome": "REJECT"}))
            return 2
        contract_path = root / "preauthority/EXPERIMENT_CONTRACT.json"
        if h256(contract_path.read_bytes()) != CONTRACT_DIGEST:
            raise ValueError("frozen contract")
        contract = read_object(contract_path)
        preflight(contract)
        expanded = independent_expansion(contract)
        records = [make_record(item) for item in expanded]
        coords = [{name: record[name] for name in ("case_id", "b", "q", "sigma", "N", "r", "control", "k", "l", "mask_depth", "mask_integer", "precision_bits")} for record in records]
        projection = {"candidate_id": CID, "contract_sha256": CONTRACT_DIGEST,
                      "finite_records": records, "infinite_records": [], "producer": "B",
                      "schema": "paper48.finite-projection.v1", "status": "PASS"}
        native = {"candidate_id": CID, "contract_sha256": CONTRACT_DIGEST,
                  "coordinate_set_sha256": h256(canonical(coords)), "finite_record_count": len(records),
                  "infinite_record_count": 0,
                  "method": "digit_automaton_and_independent_shell_kronecker_factorization",
                  "projection_sha256": h256(canonical(projection)), "producer": "B",
                  "random_mask_generation": "independent_counter_protocol_no_shared_expansion",
                  "schema": "paper48.evaluator-b-native.v1", "status": "PASS"}
        ns.projection.write_bytes(canonical(projection))
        ns.native.write_bytes(canonical(native))
        return 0
    except Exception as exc:
        sys.stderr.write(f"B_ERROR:{type(exc).__name__}\n")
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
