#!/usr/bin/env python3
"""Deterministic exact certificate for a contracted rotation.

The map is f_{lambda,delta}(x) = {lambda*x + delta}, with 0 < lambda < 1.
All itinerary and parameter-interval calculations use Fraction. Decimal
numbers occur only in the direct iteration probes and never decide
admissibility.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import itertools
import json
import os
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "489506cf92bfed721f94f22dd0444a60427f90a5"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
EVALUATION_DATE = "2026-08-30"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c240_contracted_rotation_evidence.json"
LAMBDAS = (F(1, 2), F(2, 3), F(3, 4))
NMAX = 12
ITERATIONS = 360
SERIALIZED_DIGITS = 64
mp.mp.dps = 90


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
    n = len(word)
    return word == min(word[i:] + word[:i] for i in range(n))


def words_upto(nmax: int = NMAX) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for n in range(1, nmax + 1):
        for word in itertools.product((0, 1), repeat=n):
            if is_primitive(word) and canonical_word(word):
                out.append(word)
    return out


def affine_data(lam: F, word: tuple[int, ...]) -> tuple[tuple[F, F], tuple[tuple[F, F], ...]]:
    """Return x_0 affine and all x_j affines as (delta slope, constant)."""
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


def _interval_update(lo: F, lo_closed: bool, hi: F, hi_closed: bool,
                     bound: F, lower: bool, closed: bool) -> tuple[F, bool, F, bool]:
    if lower:
        if bound > lo:
            lo, lo_closed = bound, closed
        elif bound == lo:
            lo_closed = lo_closed and closed
    else:
        if bound < hi:
            hi, hi_closed = bound, closed
        elif bound == hi:
            hi_closed = hi_closed and closed
    return lo, lo_closed, hi, hi_closed


def _constraint(lo: F, lo_closed: bool, hi: F, hi_closed: bool,
                A: F, B: F, C: F, relation: str) -> tuple[F, bool, F, bool, bool]:
    """Apply A*delta+B >= C (ge) or < C (lt)."""
    if A == 0:
        ok = B >= C if relation == "ge" else B < C
        return lo, lo_closed, hi, hi_closed, ok
    bound = (C - B) / A
    if relation == "ge":
        lower, closed = A > 0, True
    else:
        lower, closed = A < 0, False
    lo, lo_closed, hi, hi_closed = _interval_update(lo, lo_closed, hi, hi_closed, bound, lower, closed)
    return lo, lo_closed, hi, hi_closed, True


def interval_for_word(lam: F, word: tuple[int, ...]) -> dict:
    """Exact half-open delta interval and endpoint equality audit."""
    (a0, b0), states = affine_data(lam, word)
    constraints: list[dict] = []
    lo, lo_closed, hi, hi_closed = F(0), True, F(1), False
    constant_ok = True

    def add(A: F, B: F, C: F, relation: str, label: str) -> None:
        nonlocal lo, lo_closed, hi, hi_closed, constant_ok
        constraints.append({"A": A, "B": B, "C": C, "relation": relation, "label": label})
        lo, lo_closed, hi, hi_closed, ok = _constraint(lo, lo_closed, hi, hi_closed, A, B, C, relation)
        constant_ok = constant_ok and ok

    # Include the parameter-domain constraints in the endpoint audit as well
    # as in the initial interval.  This makes delta=1 visibly inadmissible.
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

    nonempty = constant_ok and (lo < hi or (lo == hi and lo_closed and hi_closed))

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
        "delta_interval": {"lo": ftext(lo), "lo_closed": lo_closed, "hi": ftext(hi), "hi_closed": hi_closed, "nonempty": nonempty},
        "boundary_audit": {"lo": endpoint(lo), "hi": endpoint(hi)},
    }


def word_row(lam: F, word: tuple[int, ...]) -> dict:
    info = interval_for_word(lam, word)
    n = len(word)
    rot = F(sum(word), n)
    return {
        "lambda": ftext(lam), "length": n, "word": "".join(map(str, word)),
        "word_id": f"n{n}_" + "".join(map(str, word)), "primitive": True, "canonical": True,
        "carry_sum": sum(word), "rotation_number": ftext(rot), "derivative": ftext(lam**n),
        **info,
    }


def exact_states(lam: F, delta: F, word: tuple[int, ...]) -> tuple[F, ...]:
    (_, _), states = affine_data(lam, word)
    return tuple(a * delta + b for a, b in states)


def boundary_ids(rows: list[dict], delta: F) -> list[str]:
    ids: list[str] = []
    for row in rows:
        iv = row["delta_interval"]
        if delta == F(iv["lo"]) or delta == F(iv["hi"]):
            ids.append(row["word_id"])
    return ids


def iterate_probe(lam: F, delta: F, word_rows_for_lambda: list[dict], label: str) -> dict:
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
    return {
        "lambda": ftext(lam), "delta": ftext(delta), "probe_label": label,
        "iterations": ITERATIONS, "suffix_period": period,
        "suffix_word": "".join(map(str, raw)), "canonical_suffix_word": "".join(map(str, canonical)),
        "suffix_rotation_number": ftext(F(sum(raw), len(raw))), "fixed_point": fixed,
        "iteration_state": dec(x), "iteration_residual": dec(residual),
        "converged": bool(period is not None and residual < mp.mpf("1e-25")),
        "suffix_admissible_under_half_open": admissible,
        "exact_boundary_word_ids": boundary_ids(word_rows_for_lambda, delta),
    }


def build() -> dict:
    all_words = words_upto()
    word_rows: list[dict] = []
    by_lambda: dict[str, list[dict]] = {}
    for lam in LAMBDAS:
        rows = [word_row(lam, w) for w in all_words]
        by_lambda[ftext(lam)] = rows
        word_rows.extend(rows)

    plateau_rows: list[dict] = []
    for lam in LAMBDAS:
        rows = [r for r in by_lambda[ftext(lam)] if r["delta_interval"]["nonempty"]]
        groups: dict[str, list[dict]] = {}
        for row in rows:
            groups.setdefault(row["rotation_number"], []).append(row)
        for rotation, group in sorted(groups.items(), key=lambda kv: (F(kv[0]), kv[0])):
            intervals = [
                {"word_id": r["word_id"], "lo": r["delta_interval"]["lo"], "hi": r["delta_interval"]["hi"],
                 "lo_closed": r["delta_interval"]["lo_closed"], "hi_closed": r["delta_interval"]["hi_closed"]}
                for r in sorted(group, key=lambda r: (F(r["delta_interval"]["lo"]), r["length"], r["word"]))
            ]
            plateau_rows.append({
                "lambda": ftext(lam), "rotation_number": rotation,
                "word_ids": [r["word_id"] for r in group], "component_intervals": intervals,
                "component_count": len(intervals), "maximal_plateau_claimed": False,
                "interpretation": "union of exact word-certified half-open components; maximality not inferred",
            })

    direct_rows: list[dict] = []
    base = [F(i, 8) for i in range(8)]
    for lam in LAMBDAS:
        rows = by_lambda[ftext(lam)]
        probes = {d: "base_grid" for d in base}
        for row in rows:
            if row["delta_interval"]["nonempty"]:
                for side in ("lo", "hi"):
                    d = F(row["delta_interval"][side])
                    probes.setdefault(d, "word_boundary")
        for delta, label in sorted(probes.items()):
            direct_rows.append(iterate_probe(lam, delta, rows, label))

    admissible_count = sum(1 for r in word_rows if r["delta_interval"]["nonempty"])
    data = {
        "schema": "hcs-c240-contracted-rotation-v1", "candidate_id": "HCS-C240",
        "evaluation_date": EVALUATION_DATE, "fixed_epoch": FIXED_EPOCH, "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "A Fraction-exact itinerary and mode-locking atlas for the one-discontinuity contracted rotation, with half-open boundary certificates and an independent direct-iteration replay.",
        "frozen_object": {
            "map": "f_{lambda,delta}(x) = {lambda*x + delta} on [0,1)",
            "phase_space": "half-open unit interval [0,1), identified with a circle only for rotation-number statements",
            "parameters": "lambda in {1/2,2/3,3/4}; delta in [0,1), with exact rational interval endpoints",
            "branch_rule": "carry k=0 when 0<=lambda*x+delta<1 and k=1 when 1<=lambda*x+delta<2",
            "clock": "discrete iteration count; no arithmetic-prime clock",
            "normalization": "slope lambda and carry rotation number sum(k_j)/n",
            "primitive_convention": "binary words primitive under repetition and lexicographically minimal under cyclic rotation",
            "determinant_convention": "source-local finite branch/itinerary factors only; no target determinant",
            "orbit_cutoff": f"all primitive canonical binary words of lengths 1..{NMAX}; {len(all_words)} words per lambda",
            "forbidden_data": "target primes/zeros, local arithmetic, Euler factors, root numbers, automorphy, target divisors, Hilbert-Polya operators",
        },
        "theorem": {
            "affine_composition": "For word w=(k_0,...,k_{n-1}), x_n=lambda^n*x_0+delta*(1-lambda^n)/(1-lambda)-sum_j k_j lambda^(n-1-j).",
            "unique_word_fixed_point": "Every word has one affine fixed point x_w(delta)=delta/(1-lambda)-K_w/(1-lambda^n); its admissibility is exactly the conjunction of the recorded half-open linear inequalities.",
            "interval_completeness": "The Fraction interval solver intersects [0,1) with x_j in [0,1) and k_j<=lambda*x_j+delta<k_j+1 for every step, so each retained component is exact at the declared cutoff.",
            "primitive_repetition": "Nonprimitive words are repetitions of a shorter cyclic word; only primitive lexicographic representatives are emitted, while repetition is recoverable from the affine formula.",
            "uniqueness_scope": "Each fixed itinerary has exactly one fixed point because 0<lambda^n<1. We do not promote a global one-cycle theorem: the general interval piecewise-contraction literature gives only a finite-orbit bound under its stated hypotheses, and the exact word census is the authority at this cutoff.",
            "mode_locking_scope": "Each nonempty word interval is a certified rotation-number component. Grouped rows report unions of word-certified components and explicitly do not claim maximal plateaux.",
            "boundary_scope": "Lower carry inequalities are closed and upper inequalities are open; every interval endpoint has an exact active-constraint and half-open-admissibility audit.",
            "direct_replay_scope": "High-precision direct iteration independently recovers a suffix itinerary and its affine fixed point at base and boundary probes; it is a control, not a proof beyond the finite cutoff.",
        },
        "regression": {
            "lambda_values": [ftext(x) for x in LAMBDAS], "word_rows": word_rows,
            "plateau_rows": plateau_rows, "direct_iteration_rows": direct_rows,
            "word_count_per_lambda": len(all_words), "total_word_rows": len(word_rows),
            "admissible_word_rows": admissible_count, "plateau_row_count": len(plateau_rows),
            "direct_iteration_row_count": len(direct_rows), "max_word_length": NMAX,
            "working_decimal_digits": 90, "serialized_decimal_digits": SERIALIZED_DIGITS,
        },
        "exact_identities": [
            {"name": "branch_composition", "formula": "x_n=lambda^n*x_0+delta*sum_{r=0}^{n-1}lambda^r-sum_{j=0}^{n-1}k_j lambda^(n-1-j)"},
            {"name": "fixed_point", "formula": "x_w=delta/(1-lambda)-K_w/(1-lambda^n)"},
            {"name": "branch_half_open", "formula": "k_j<=lambda*x_j+delta<k_j+1"},
            {"name": "derivative", "formula": "(f^n)'=lambda^n on an admissible word"},
            {"name": "rotation", "formula": "rho_w=(sum_j k_j)/n"},
            {"name": "primitive_test", "formula": "w is primitive iff it is not a repetition of a shorter block"},
            {"name": "canonical_cycle", "formula": "canonical word=min over cyclic rotations"},
            {"name": "parameter_domain", "formula": "0<lambda<1 and 0<=delta<1"},
            {"name": "endpoint_rule", "formula": "lower bounds closed, upper bounds open"},
            {"name": "source_local_factor", "formula": "one admissible n-cycle contributes a factor 1-z^n lambda^n (source-local only)"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
            "strongest_positive": "exact finite-cutoff primitive itinerary, affine fixed points, half-open delta intervals and boundary certificates",
            "strongest_failure": "parameters are source-defined rationals with no intrinsic prime carrier or target determinant; source-local factors are not target matches",
        },
        "scope_flags": {
            "uses_target_zero_table": False, "uses_prime_table": False, "claims_arithmetic_local_data": False,
            "claims_euler_factors": False, "claims_root_numbers": False, "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False, "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "citations": [
            {"key": "LaurentNogueira2018", "claim": "contracted rotations, rotation number, one-discontinuity piecewise contraction and algebraic-parameter mode locking", "source": "https://www.aimsciences.org/article/doi/10.3934/jmd.2018007", "doi": "10.3934/jmd.2018007"},
            {"key": "NogueiraPires2015", "claim": "injective piecewise contractions of an interval and the at-most-n periodic-orbit bound (n=2 branches gives an upper bound of 2)", "source": "https://doi.org/10.1017/etds.2014.16", "doi": "10.1017/etds.2014.16"},
            {"key": "BugeaudConze1999", "claim": "contracting linear transformations modulo one and Hecke-Mahler/Farey structure", "source": "https://doi.org/10.4064/aa-88-3-201-218", "doi": "10.4064/aa-88-3-201-218"},
        ],
        "nonclaims": [
            "The finite word atlas is complete only for primitive canonical words up to the declared length cutoff and frozen lambda grid.",
            "Grouped intervals are unions of exact word-certified components; no maximal plateau or global rotation-number classification is inferred.",
            "No global one-periodic-orbit theorem is claimed; the cited general two-branch piecewise-contraction theorem gives only an at-most-two bound under its hypotheses.",
            "Source-local branch factors and rotation numbers are not arithmetic Euler factors, target zeros, or a target determinant.",
            "No arithmetic origin, automorphy, target functional equation, Hilbert-Polya operator, or Route-B input is claimed.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    tmp = args.output.with_name(args.output.name + ".tmp")
    tmp.write_text(raw)
    os.replace(tmp, args.output)
    print(json.dumps({"status": "C240_PRODUCER_PASS", "payload_sha256": data["payload_sha256"], "evidence_sha256": sha256(raw.encode()).hexdigest(), "word_rows": data["regression"]["total_word_rows"], "admissible_word_rows": data["regression"]["admissible_word_rows"], "plateau_rows": data["regression"]["plateau_row_count"], "direct_rows": data["regression"]["direct_iteration_row_count"]}, sort_keys=True))


if __name__ == "__main__":
    main()
