#!/usr/bin/env python3
"""Production exact engine for P49 State A.

The engine has no project-local imports.  It uses rational linear forms in
logarithms of primes and residue-grouped geometric sums.  Decimal arithmetic
is intentionally absent.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterator, Sequence


Form = dict[int, Fraction]
SLUG = "49-transient-phase-allocation-tree-shifts"


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def reject(code: str) -> int:
    sys.stdout.buffer.write(canonical({"payload": {"code": code}, "schema": "stage0-error-v1", "status": "REJECT"}))
    return 2


def load_json(path: Path) -> Any:
    def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for key, value in pairs:
            if key in out:
                raise ValueError("duplicate JSON key")
            out[key] = value
        return out
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique)


def exact_int(value: Any) -> bool:
    return type(value) is int


def factors(value: int) -> dict[int, int]:
    if not exact_int(value) or value < 1:
        raise ValueError("positive integer required")
    answer: dict[int, int] = {}
    divisor = 2
    remainder = value
    while divisor * divisor <= remainder:
        while remainder % divisor == 0:
            answer[divisor] = answer.get(divisor, 0) + 1
            remainder //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remainder > 1:
        answer[remainder] = answer.get(remainder, 0) + 1
    return answer


def clean(form: Form) -> Form:
    return {prime: coeff for prime, coeff in form.items() if coeff}


def add(*forms: Form) -> Form:
    answer: Form = {}
    for form in forms:
        for prime, coeff in form.items():
            answer[prime] = answer.get(prime, Fraction(0)) + coeff
    return clean(answer)


def scale(form: Form, scalar: Fraction | int) -> Form:
    return clean({prime: Fraction(scalar) * coeff for prime, coeff in form.items()})


def log_integer(value: int) -> Form:
    return {prime: Fraction(exponent) for prime, exponent in factors(value).items()}


def compare(left: Form, right: Form) -> int:
    difference = add(left, scale(right, -1))
    if not difference:
        return 0
    common = 1
    for coeff in difference.values():
        common = math.lcm(common, coeff.denominator)
    numerator = 1
    denominator = 1
    for prime, coeff in difference.items():
        exponent = coeff.numerator * (common // coeff.denominator)
        if exponent > 0:
            numerator *= prime**exponent
        elif exponent < 0:
            denominator *= prime ** (-exponent)
    return (numerator > denominator) - (numerator < denominator)


def serialize(form: Form) -> list[dict[str, int]]:
    return [
        {"denominator": coeff.denominator, "numerator": coeff.numerator, "prime": prime}
        for prime, coeff in sorted(clean(form).items())
    ]


def serialize_exponents(form: dict[int, int]) -> list[dict[str, int]]:
    return [{"exponent": exponent, "prime": prime} for prime, exponent in sorted(form.items()) if exponent]


def validate(d: int, a: Sequence[int], m: Sequence[int] | None = None, total: int | None = None) -> None:
    if not exact_int(d) or d < 2 or not a or any(not exact_int(x) or x < 1 for x in a):
        raise ValueError("typed tree parameters")
    if m is not None:
        wanted = d if total is None else total
        if len(m) != len(a) or any(not exact_int(x) or x < 0 for x in m) or sum(m) != wanted:
            raise ValueError("typed composition")


def h_forms(d: int, a: Sequence[int]) -> list[Form]:
    validate(d, a)
    p = len(a)
    denominator = d**p - 1
    return [
        add(*(
            scale(log_integer(a[(j - t) % p]), Fraction((d - 1) * d ** (p - 1 - t), denominator))
            for t in range(p)
        ))
        for j in range(p)
    ]


def residue_forms(d: int, a: Sequence[int], m: Sequence[int], total: int) -> list[Form]:
    validate(d, a, m, total)
    h = h_forms(d, a)
    p = len(a)
    return [
        scale(add(*(scale(h[(s + j) % p], m[s]) for s in range(p))), Fraction(1, total))
        for j in range(p)
    ]


def shifted_products(a: Sequence[int], m: Sequence[int]) -> list[int]:
    p = len(a)
    return [math.prod(a[(s + k) % p] ** m[s] for s in range(p)) for k in range(p)]


def minimum(forms: Sequence[Form]) -> tuple[int, Form]:
    if not forms:
        raise ValueError("empty form list")
    index = 0
    for candidate in range(1, len(forms)):
        if compare(forms[candidate], forms[index]) < 0:
            index = candidate
    return index, forms[index]


def compositions(total: int, parts: int) -> Iterator[tuple[int, ...]]:
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def grouped_core_prefix(d: int, a: Sequence[int], root: int, depth: int) -> dict[int, int]:
    p = len(a)
    out: dict[int, int] = {}
    for residue in range(p):
        if residue > depth:
            continue
        count = (depth - residue) // p + 1
        coefficient = d**residue * (d ** (p * count) - 1) // (d**p - 1)
        for prime, exponent in factors(a[(root + residue) % p]).items():
            out[prime] = out.get(prime, 0) + coefficient * exponent
    return {prime: exponent for prime, exponent in out.items() if exponent}


def grouped_feeder_prefix(d: int, a: Sequence[int], m: Sequence[int], depth: int) -> dict[int, int]:
    validate(d, a, m, d)
    if depth < 1:
        return {}
    p = len(a)
    core_depth = depth - 1
    out: dict[int, int] = {}
    for s, multiplicity in enumerate(m):
        for residue in range(p):
            if residue > core_depth:
                continue
            count = (core_depth - residue) // p + 1
            coefficient = d**residue * (d ** (p * count) - 1) // (d**p - 1)
            for prime, exponent in factors(a[(s + residue) % p]).items():
                out[prime] = out.get(prime, 0) + multiplicity * coefficient * exponent
    return {prime: exponent for prime, exponent in out.items() if exponent}


def best_level(d: int, a: Sequence[int], level: int) -> tuple[tuple[int, ...], Form, list[Form]]:
    total = d**level
    best_m: tuple[int, ...] | None = None
    best_form: Form | None = None
    best_residues: list[Form] | None = None
    for m in compositions(total, len(a)):
        residues = residue_forms(d, a, m, total)
        _, dimension = minimum(residues)
        if best_form is None or compare(dimension, best_form) > 0:
            best_m, best_form, best_residues = m, dimension, residues
    assert best_m is not None and best_form is not None and best_residues is not None
    return best_m, best_form, best_residues


def evaluate_mutation(record: dict[str, Any]) -> str:
    kind = record["kind"]
    payload = record["payload"]
    if kind == "unconditional_divisibility_necessity":
        d, a, m = payload["d"], tuple(payload["a"]), tuple(payload["m"])
        residues = residue_forms(d, a, m, d)
        if all(form == residues[0] for form in residues[1:]) and d % len(a) != 0:
            return "REJECT_FALSE_DIVISIBILITY_NECESSITY"
    elif kind == "missing_complete_block_edge":
        sizes = tuple(payload["phase_sizes"])
        removed = tuple(tuple(vertex) for vertex in payload["removed_edge"])
        complete = {
            ((phase, source), ((phase + 1) % len(sizes), target))
            for phase, size in enumerate(sizes)
            for source in range(size)
            for target in range(sizes[(phase + 1) % len(sizes)])
        }
        incomplete = set(complete)
        incomplete.discard(removed)
        if removed in complete and incomplete != complete:
            return "REJECT_INCOMPLETE_CORE"
    elif kind == "core_to_feeder_return":
        adjacency = payload["adjacency"]
        reachable = {0}
        revisits = []
        for depth in range(1, payload["depth"] + 1):
            reachable = {target for source in reachable for target, edge in enumerate(adjacency[source]) if edge == 1}
            if 0 in reachable:
                revisits.append(depth)
        if revisits and revisits[-1] == payload["depth"]:
            return "REJECT_NONTRANSIENT"
    elif kind == "incomplete_feeder_row":
        p, d = payload["p"], payload["d"]
        allowed = set(payload["allowed_child_phases"])
        unrestricted = set(compositions(d, p))
        admitted = {m for m in unrestricted if all(m[phase] == 0 for phase in range(p) if phase not in allowed)}
        if admitted != unrestricted:
            return "REJECT_UNRESTRICTED_PHASE_ACCESS"
    elif kind == "invalid_d_phase_size_and_composition":
        rejected = 0
        for case in payload["invalid_cases"]:
            try:
                validate(case["d"], tuple(case["a"]), tuple(case["m"]), case["d"])
            except ValueError:
                rejected += 1
        if rejected == len(payload["invalid_cases"]):
            return "REJECT_TYPED_BOUNDARIES"
    elif kind == "four_state_max_scc_formula":
        d, a, m = payload["d"], tuple(payload["a"]), tuple(payload["m"])
        _, core = minimum(h_forms(d, a))
        _, feeder = minimum(residue_forms(d, a, m, d))
        if compare(feeder, core) > 0:
            return "REJECT_ARBITRARY_MAX_SCC"
    raise ValueError("mutation survived")


def evaluate_case(case: dict[str, Any]) -> dict[str, Any]:
    case_id = case["case_id"]
    kind = case["kind"]
    if kind == "four_state_strict_scc":
        d, a, m = case["d"], tuple(case["a"]), tuple(case["m"])
        validate(d, a, m, d)
        core = h_forms(d, a)
        feeder = residue_forms(d, a, m, d)
        core_index, core_dim = minimum(core)
        feeder_index, feeder_dim = minimum(feeder)
        prefixes = [
            {
                "component_root0": serialize_exponents(grouped_core_prefix(d, a, 0, depth)),
                "depth": depth,
                "feeder": serialize_exponents(grouped_feeder_prefix(d, a, m, depth)),
            }
            for depth in case["prefix_depths"]
        ]
        result = {
            "component_dimension": serialize(core_dim),
            "component_min_residue": core_index,
            "component_residues": [serialize(form) for form in core],
            "feeder_dimension": serialize(feeder_dim),
            "feeder_min_residue": feeder_index,
            "feeder_residues": [serialize(form) for form in feeder],
            "full_strictly_exceeds_component": compare(feeder_dim, core_dim) > 0,
            "prefix_exponents": prefixes,
        }
    elif kind == "nondivisible_saturation":
        d, a, m = case["d"], tuple(case["a"]), tuple(case["m"])
        residues = residue_forms(d, a, m, d)
        products = shifted_products(a, m)
        result = {
            "p_divides_d": d % len(a) == 0,
            "residue_forms": [serialize(form) for form in residues],
            "saturates": all(form == residues[0] for form in residues[1:]),
            "shifted_products": products,
        }
    elif kind == "p2_odd_optimizer":
        d, a = case["d"], tuple(case["a"])
        core_index, core_dim = minimum(h_forms(d, a))
        rows: list[dict[str, Any]] = []
        best_m: tuple[int, ...] | None = None
        best_dim: Form | None = None
        for k in range(d + 1):
            m = (k, d - k)
            _, dimension = minimum(residue_forms(d, a, m, d))
            rows.append({"dimension": serialize(dimension), "m": list(m)})
            if best_dim is None or compare(dimension, best_dim) > 0:
                best_m, best_dim = m, dimension
        assert best_m is not None and best_dim is not None
        mean = scale(add(*(log_integer(value) for value in a)), Fraction(1, 2))
        result = {
            "component_dimension": serialize(core_dim),
            "component_min_residue": core_index,
            "fixed_compositions": rows,
            "mean": serialize(mean),
            "optimum_composition": list(best_m),
            "optimum_dimension": serialize(best_dim),
            "optimum_saturates": best_dim == mean,
            "strictly_exceeds_component": compare(best_dim, core_dim) > 0,
        }
    elif kind == "level_optimizer":
        d, a, level, next_level = case["d"], tuple(case["a"]), case["level"], case["next_level"]
        if not exact_int(level) or not exact_int(next_level) or level < 1 or next_level != level + 1:
            raise ValueError("typed levels")
        m_l, dim_l, residues_l = best_level(d, a, level)
        m_next, dim_next, residues_next = best_level(d, a, next_level)
        embedded = tuple(d * value for value in m_l)
        _, embedded_dim = minimum(residue_forms(d, a, embedded, d**next_level))
        result = {
            "embedded_composition": list(embedded),
            "embedded_dimension": serialize(embedded_dim),
            "level": level,
            "level_dimension": serialize(dim_l),
            "level_optimizer": list(m_l),
            "level_residues": [serialize(form) for form in residues_l],
            "next_dimension": serialize(dim_next),
            "next_level": next_level,
            "next_optimizer": list(m_next),
            "next_residues": [serialize(form) for form in residues_next],
            "optimized_monotone": compare(dim_next, dim_l) >= 0,
        }
    else:
        raise ValueError("unknown case kind")
    return {"case_id": case_id, "kind": kind, "result": result}


def main() -> int:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--root")
    parser.add_argument("--state")
    parser.add_argument("--mutation")
    try:
        args = parser.parse_args()
    except SystemExit:
        return reject("REJECT_ARGUMENTS")
    if args.state != "A":
        return reject("REJECT_STATE")
    try:
        root = Path(args.root)
        if not root.is_absolute() or root.is_symlink() or not root.is_dir() or root.resolve(strict=True) != root:
            return reject("REJECT_ROOT")
        if args.mutation is not None:
            registry = load_json(root / "contracts" / "MUTATION_REGISTRY.json")
            matches = [record for record in registry["mutations"] if record["id"] == args.mutation]
            if len(matches) != 1:
                return reject("REJECT_MUTATION_ID")
            return reject(evaluate_mutation(matches[0]))
        spec = load_json(root / "contracts" / "STATE_A_CASES.json")
        if spec.get("project_slug") != SLUG or spec.get("state") != "A" or type(spec.get("cases")) is not list:
            return reject("REJECT_CASE_CONTRACT")
        cases = [evaluate_case(case) for case in spec["cases"]]
        envelope = {
            "payload": {
                "cases": cases,
                "evidence_class": "FINITE_EXACT_FALSIFICATION_ONLY",
                "project_slug": SLUG,
                "state": "A",
            },
            "schema": "p49-stage0-science-v1",
            "status": "PASS",
        }
        sys.stdout.buffer.write(canonical(envelope))
        return 0
    except (KeyError, OSError, TypeError, ValueError, AssertionError, json.JSONDecodeError):
        return reject("REJECT_CASE_CONTRACT")


if __name__ == "__main__":
    raise SystemExit(main())
