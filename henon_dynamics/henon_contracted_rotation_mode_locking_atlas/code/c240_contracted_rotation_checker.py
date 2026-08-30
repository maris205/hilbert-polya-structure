#!/usr/bin/env python3
"""Producer-independent checker for the C240 contracted-rotation receipt."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import itertools
import json
from pathlib import Path
import re

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c240_contracted_rotation_evidence.json"
SOURCE_COMMIT = "489506cf92bfed721f94f22dd0444a60427f90a5"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
EVALUATION_DATE = "2026-08-30"
LAMBDAS = (F(1, 2), F(2, 3), F(3, 4))
NMAX = 12
ITERATIONS = 360
SERIALIZED_DIGITS = 64
mp.mp.dps = 90

TOP_KEYS = {"schema", "candidate_id", "evaluation_date", "fixed_epoch", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
SCOPE_KEYS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}
NUM_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+|[eE][+-]?[0-9]+)$")


def ftext(q: F | int) -> str:
    q = q if isinstance(q, F) else F(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def mpq(q: F | int) -> mp.mpf:
    q = q if isinstance(q, F) else F(q)
    return mp.mpf(q.numerator) / q.denominator


def dec(x: mp.mpf | F | int) -> str:
    y = mpq(x) if isinstance(x, (F, int)) else mp.mpf(x)
    if abs(y) < mp.mpf("1e-82"):
        y = mp.mpf("0")
    return mp.nstr(y, SERIALIZED_DIGITS, strip_zeros=False, min_fixed=-70, max_fixed=70)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def is_primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def canonical_word(word: tuple[int, ...]) -> bool:
    return word == min(word[i:] + word[:i] for i in range(len(word)))


def words_upto() -> list[tuple[int, ...]]:
    return [word for n in range(1, NMAX + 1) for word in itertools.product((0, 1), repeat=n) if is_primitive(word) and canonical_word(word)]


def affine_data(lam: F, word: tuple[int, ...]) -> tuple[tuple[F, F], tuple[tuple[F, F], ...]]:
    n = len(word)
    den = 1 - lam**n
    geom = sum(lam**j for j in range(n))
    carry = sum(F(word[j]) * lam ** (n - 1 - j) for j in range(n))
    a0, b0 = geom / den, -carry / den
    states: list[tuple[F, F]] = []
    a, b = a0, b0
    for bit in word:
        states.append((a, b))
        a, b = lam * a + 1, lam * b - F(bit)
    return (a0, b0), tuple(states)


def _update(lo: F, lc: bool, hi: F, hc: bool, bound: F, lower: bool, closed: bool) -> tuple[F, bool, F, bool]:
    if lower:
        if bound > lo:
            lo, lc = bound, closed
        elif bound == lo:
            lc = lc and closed
    else:
        if bound < hi:
            hi, hc = bound, closed
        elif bound == hi:
            hc = hc and closed
    return lo, lc, hi, hc


def _constraint(lo: F, lc: bool, hi: F, hc: bool, A: F, B: F, C: F, relation: str) -> tuple[F, bool, F, bool, bool]:
    if A == 0:
        return lo, lc, hi, hc, (B >= C if relation == "ge" else B < C)
    bound = (C - B) / A
    if relation == "ge":
        lower, closed = A > 0, True
    else:
        lower, closed = A < 0, False
    lo, lc, hi, hc = _update(lo, lc, hi, hc, bound, lower, closed)
    return lo, lc, hi, hc, True


def interval_for_word(lam: F, word: tuple[int, ...]) -> dict:
    (a0, b0), states = affine_data(lam, word)
    constraints: list[dict] = []
    lo, lc, hi, hc = F(0), True, F(1), False
    constant_ok = True

    def add(A: F, B: F, C: F, relation: str, label: str) -> None:
        nonlocal lo, lc, hi, hc, constant_ok
        constraints.append({"A": A, "B": B, "C": C, "relation": relation, "label": label})
        lo, lc, hi, hc, ok = _constraint(lo, lc, hi, hc, A, B, C, relation)
        constant_ok = constant_ok and ok

    # Keep the half-open parameter domain in the same constraint list used
    # for endpoint auditing; in particular delta=1 must fail explicitly.
    add(F(1), F(0), F(0), "ge", "delta>=0")
    add(F(1), F(0), F(1), "lt", "delta<1")

    a, b = a0, b0
    for j, bit in enumerate(word):
        add(a, b, F(0), "ge", f"x{j}>=0")
        add(a, b, F(1), "lt", f"x{j}<1")
        ay, by = lam * a + 1, lam * b
        add(ay, by, F(bit), "ge", f"carry{j}>={bit}")
        add(ay, by, F(bit + 1), "lt", f"carry{j}<{bit + 1}")
        a, b = ay, by - F(bit)

    nonempty = constant_ok and (lo < hi or (lo == hi and lc and hc))

    def endpoint(value: F) -> dict:
        active: list[str] = []
        valid = True
        for c in constraints:
            lhs = c["A"] * value + c["B"]
            if lhs == c["C"]:
                active.append(c["label"])
            valid = valid and (lhs >= c["C"] if c["relation"] == "ge" else lhs < c["C"])
        return {"value": ftext(value), "active_constraints": active, "half_open_admissible": bool(valid)}

    return {
        "fixed_point_affine": {"delta_slope": ftext(a0), "constant": ftext(b0)},
        "state_affines": [{"step": j, "delta_slope": ftext(a), "constant": ftext(b)} for j, (a, b) in enumerate(states)],
        "delta_interval": {"lo": ftext(lo), "lo_closed": lc, "hi": ftext(hi), "hi_closed": hc, "nonempty": nonempty},
        "boundary_audit": {"lo": endpoint(lo), "hi": endpoint(hi)},
    }


def expected_word_row(lam: F, word: tuple[int, ...]) -> dict:
    n = len(word)
    return {"lambda": ftext(lam), "length": n, "word": "".join(map(str, word)), "word_id": f"n{n}_" + "".join(map(str, word)), "primitive": True, "canonical": True, "carry_sum": sum(word), "rotation_number": ftext(F(sum(word), n)), "derivative": ftext(lam**n), **interval_for_word(lam, word)}


def exact_states(lam: F, delta: F, word: tuple[int, ...]) -> tuple[F, ...]:
    (_, _), states = affine_data(lam, word)
    return tuple(a * delta + b for a, b in states)


def boundary_ids(rows: list[dict], delta: F) -> list[str]:
    return [r["word_id"] for r in rows if delta == F(r["delta_interval"]["lo"]) or delta == F(r["delta_interval"]["hi"])]


def iterate_probe(lam: F, delta: F, rows: list[dict], label: str) -> dict:
    lm, dm = mpq(lam), mpq(delta)
    x = dm
    carries: list[int] = []
    for _ in range(ITERATIONS):
        y = lm * x + dm
        bit = 1 if y >= 1 else 0
        carries.append(bit)
        x = y - bit
    period = None
    for n in range(1, NMAX + 1):
        if carries[-2 * n:-n] == carries[-n:]:
            period = n
            break
    raw = tuple(carries[-period:]) if period else tuple(carries[-NMAX:])
    canonical = min(raw[i:] + raw[:i] for i in range(len(raw)))
    fixed = None
    residual = mp.mpf("0")
    admissible = False
    if period:
        (a0, b0), _ = affine_data(lam, raw)
        fixed_q = a0 * delta + b0
        fixed = ftext(fixed_q)
        residual = abs(x - mpq(fixed_q))
        states = exact_states(lam, delta, raw)
        admissible = all(F(bit) <= lam * state + delta < F(bit + 1) for state, bit in zip(states, raw))
    return {"lambda": ftext(lam), "delta": ftext(delta), "probe_label": label, "iterations": ITERATIONS, "suffix_period": period, "suffix_word": "".join(map(str, raw)), "canonical_suffix_word": "".join(map(str, canonical)), "suffix_rotation_number": ftext(F(sum(raw), len(raw))), "fixed_point": fixed, "iteration_state": dec(x), "iteration_residual": dec(residual), "converged": bool(period is not None and residual < mp.mpf("1e-25")), "suffix_admissible_under_half_open": admissible, "exact_boundary_word_ids": boundary_ids(rows, delta)}


def expected_plateaux(lam: F, rows: list[dict]) -> list[dict]:
    groups: dict[str, list[dict]] = {}
    for row in rows:
        if row["delta_interval"]["nonempty"]:
            groups.setdefault(row["rotation_number"], []).append(row)
    out: list[dict] = []
    for rotation, group in sorted(groups.items(), key=lambda kv: (F(kv[0]), kv[0])):
        intervals = [{"word_id": r["word_id"], "lo": r["delta_interval"]["lo"], "hi": r["delta_interval"]["hi"], "lo_closed": r["delta_interval"]["lo_closed"], "hi_closed": r["delta_interval"]["hi_closed"]} for r in sorted(group, key=lambda r: (F(r["delta_interval"]["lo"]), r["length"], r["word"]))]
        out.append({"lambda": ftext(lam), "rotation_number": rotation, "word_ids": [r["word_id"] for r in group], "component_intervals": intervals, "component_count": len(intervals), "maximal_plateau_claimed": False, "interpretation": "union of exact word-certified half-open components; maximality not inferred"})
    return out


def expected_direct_rows(lam: F, rows: list[dict]) -> list[dict]:
    probes = {F(i, 8): "base_grid" for i in range(8)}
    for row in rows:
        if row["delta_interval"]["nonempty"]:
            for side in ("lo", "hi"):
                probes.setdefault(F(row["delta_interval"][side]), "word_boundary")
    return [iterate_probe(lam, d, rows, label) for d, label in sorted(probes.items())]


_EXPECTED_CACHE: tuple[list[dict], list[dict], list[dict], list[tuple[int, ...]]] | None = None


def expected_bundle() -> tuple[list[dict], list[dict], list[dict], list[tuple[int, ...]]]:
    """Build the independent baseline once per checker process.

    Mutation tests call ``validate`` repeatedly; caching this immutable
    deterministic baseline keeps the adversarial suite quick without reading
    or importing the producer.
    """
    global _EXPECTED_CACHE
    if _EXPECTED_CACHE is not None:
        return _EXPECTED_CACHE
    all_words = words_upto()
    expected_rows: list[dict] = []
    for lam in LAMBDAS:
        expected_rows.extend(expected_word_row(lam, w) for w in all_words)
    expected_plateau: list[dict] = []
    expected_direct: list[dict] = []
    for lam in LAMBDAS:
        lrows = [r for r in expected_rows if r["lambda"] == ftext(lam)]
        expected_plateau.extend(expected_plateaux(lam, lrows))
        expected_direct.extend(expected_direct_rows(lam, lrows))
    _EXPECTED_CACHE = (expected_rows, expected_plateau, expected_direct, all_words)
    return _EXPECTED_CACHE


def quick_preflight(data: dict) -> None:
    assert set(data) == TOP_KEYS
    assert data["schema"] == "hcs-c240-contracted-rotation-v1" and data["candidate_id"] == "HCS-C240"
    assert data["evaluation_date"] == EVALUATION_DATE and data["fixed_epoch"] == FIXED_EPOCH and data["source_commit"] == SOURCE_COMMIT and data["scope_literal"] == SCOPE
    assert data["payload_sha256"] == payload_hash(data)
    assert data["route_a"]["tuple"] == ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert data["route_a"]["overall"] == "ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False
    print("C240 quick hostile preflight: PASS")


def validate(data: dict) -> int:
    checks = 0

    def check(ok: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not ok:
            raise AssertionError(label)

    def exact(a, b, label: str) -> None:
        check(type(a) is type(b), label + " type")
        check(a == b, label)

    check(set(data) == TOP_KEYS, "top closure")
    exact(data["schema"], "hcs-c240-contracted-rotation-v1", "schema")
    exact(data["candidate_id"], "HCS-C240", "candidate")
    exact(data["evaluation_date"], EVALUATION_DATE, "date")
    exact(data["fixed_epoch"], FIXED_EPOCH, "fixed epoch")
    exact(data["source_commit"], SOURCE_COMMIT, "source")
    exact(data["scope_literal"], SCOPE, "scope")
    exact(data["evaluator"], {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False, "route verdict")
    check(set(data["scope_flags"]) == SCOPE_KEYS and all(v is False for v in data["scope_flags"].values()), "scope firewall")
    check("Each fixed itinerary has exactly one fixed point" in data["theorem"]["uniqueness_scope"], "local uniqueness scope")
    check("do not claim maximal" in data["theorem"]["mode_locking_scope"], "plateau scope")
    check(data["regression"]["working_decimal_digits"] == 90 and data["regression"]["serialized_decimal_digits"] == SERIALIZED_DIGITS, "precision")

    expected_rows, expected_plateau, expected_direct, all_words = expected_bundle()
    rows = data["regression"]["word_rows"]
    check(len(rows) == len(expected_rows), "word row count")
    check(data["regression"]["word_count_per_lambda"] == len(all_words), "word count per lambda")
    check(data["regression"]["total_word_rows"] == len(expected_rows), "total word rows")
    row_keys = {"lambda", "length", "word", "word_id", "primitive", "canonical", "carry_sum", "rotation_number", "derivative", "fixed_point_affine", "state_affines", "delta_interval", "boundary_audit"}
    for i, (got, exp) in enumerate(zip(rows, expected_rows)):
        check(set(got) == row_keys, f"word {i} keys")
        exact(got, exp, f"word {i}")
    admissible = sum(1 for r in rows if r["delta_interval"]["nonempty"])
    check(data["regression"]["admissible_word_rows"] == admissible == 138, "admissible count")
    check(data["regression"]["max_word_length"] == NMAX, "cutoff")

    exact(data["regression"]["plateau_rows"], expected_plateau, "plateau rows")
    exact(data["regression"]["plateau_row_count"], len(expected_plateau), "plateau count")

    exact(data["regression"]["direct_iteration_rows"], expected_direct, "direct iteration rows")
    exact(data["regression"]["direct_iteration_row_count"], len(expected_direct), "direct count")
    check(sum(r["converged"] for r in expected_direct) >= 80, "direct convergence controls")
    check(any(r["probe_label"] == "word_boundary" and r["exact_boundary_word_ids"] for r in expected_direct), "boundary probes")

    check(len(data["exact_identities"]) == 10, "identity count")
    check(len(data["citations"]) == 3 and all(set(c) == {"key", "claim", "source", "doi"} for c in data["citations"]), "citation closure")
    check(len(data["nonclaims"]) == 5 and all(isinstance(x, str) for x in data["nonclaims"]), "nonclaim closure")
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    if args.quick:
        quick_preflight(data)
    else:
        print(f"C240 independent checker: PASS ({validate(data)} assertions; Fraction itinerary intervals and direct iteration)")


if __name__ == "__main__":
    main()
