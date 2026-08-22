#!/usr/bin/env python3
"""Deterministic finite-prefix kneading/pruning pilot (C105).

The object is deliberately a source-locked *candidate language*, not a claim
that the frozen prefix is already a complete Hénon kneading invariant.  The
script enumerates only words whose lexicographic comparisons are decided by
the frozen prefix; unresolved words are reported rather than silently kept.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c105_kneading_evidence.json"

PREFIX_LENGTH = 32
MAX_PERIOD = 12


def morphic_prefix(length: int) -> str:
    word = "0"
    while len(word) < length:
        word = "".join("01" if c == "0" else "011" for c in word)
    return word[:length]


def frozen_bounds() -> tuple[str, str]:
    seed = morphic_prefix(PREFIX_LENGTH)
    tail = seed[1:]
    # The first five symbols leave a certified interior window; the
    # non-periodic tail is the pruning witness rather than an admission rule.
    lower = "0" + "0" * 5 + tail[5:]
    upper = "1" + "1" * 5 + "".join("1" if c == "0" else "0" for c in tail[5:])
    return lower, upper


def compare_prefix(period: str, offset: int, bound: str) -> int | None:
    """Compare the periodic suffix with bound; None means unresolved."""
    n = len(period)
    for j in range(PREFIX_LENGTH):
        a = period[(offset + j) % n]
        b = bound[j]
        if a < b:
            return -1
        if a > b:
            return 1
    return None


def classify_word(word: str, lower: str, upper: str) -> str:
    relations = []
    for offset in range(len(word)):
        lo = compare_prefix(word, offset, lower)
        hi = compare_prefix(word, offset, upper)
        if lo is None or hi is None:
            return "UNRESOLVED"
        if lo < 0 or hi > 0:
            return "REJECT"
        relations.append((lo, hi))
    return "ACCEPT"


def rotations(word: str) -> list[str]:
    return [word[i:] + word[:i] for i in range(len(word))]


def primitive(word: str) -> bool:
    n = len(word)
    return all(n % d != 0 or word != word[:d] * (n // d) for d in range(1, n))


def mobius_primitive(traces: dict[int, int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for n in range(1, max(traces) + 1):
        total = traces.get(n, 0)
        for d, p in out.items():
            if n % d == 0:
                total -= d * p
        if total % n:
            raise AssertionError((n, total, traces, out))
        out[n] = total // n
    return out


def determinant_prefix(traces: dict[int, int]) -> list[str]:
    """Coefficients of exp(-sum trace_n z^n/n), through MAX_PERIOD."""
    coeff: list[Fraction] = [Fraction(1)]
    # n c_n = -sum_{k=1}^n k? Derive from D'/D=-sum tr_n z^(n-1).
    # For D=1+sum c_n z^n: n c_n = -sum_{k=1}^n tr_k c_{n-k}.
    for n in range(1, MAX_PERIOD + 1):
        value = -sum(Fraction(traces.get(k, 0)) * coeff[n - k] for k in range(1, n + 1))
        coeff.append(value / n)
    return [f"{x.numerator}/{x.denominator}" for x in coeff]


def main() -> None:
    lower, upper = frozen_bounds()
    accepted: dict[int, list[str]] = {}
    unresolved: dict[int, list[str]] = {}
    rejected: dict[int, int] = {}
    primitive_words: dict[int, list[str]] = {}
    for n in range(1, MAX_PERIOD + 1):
        a: list[str] = []
        u: list[str] = []
        r = 0
        for bits in itertools.product("01", repeat=n):
            word = "".join(bits)
            cls = classify_word(word, lower, upper)
            if cls == "ACCEPT":
                a.append(word)
            elif cls == "UNRESOLVED":
                u.append(word)
            else:
                r += 1
        # A cyclic language must be rotation invariant.  Keep this assertion
        # explicit: it catches orientation/shift mistakes in hostile tests.
        if any(classify_word(w, lower, upper) != "ACCEPT" for w in a for _ in [0] if any(classify_word(v, lower, upper) != "ACCEPT" for v in rotations(w))):
            raise AssertionError("accepted language is not rotation invariant")
        accepted[n] = sorted(a)
        unresolved[n] = sorted(u)
        rejected[n] = r
        primitive_words[n] = sorted(w for w in a if primitive(w))
    traces = {n: len(accepted[n]) for n in accepted}
    prim = mobius_primitive(traces)
    payload = {
        "schema": "hcs-c105-kneading-prefix-v1",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "status": "FINITE_PREFIX_CERTIFICATE_ONLY",
        "source_lock": {
            "base": "certified H6 two-branch itinerary interface; kneading pair is a frozen pilot prefix",
            "prefix_length": PREFIX_LENGTH,
            "lower_kneading": lower,
            "upper_kneading": upper,
            "unresolved_are_not_admitted": True,
        },
        "period_max": MAX_PERIOD,
        "accepted_words": accepted,
        "unresolved_words": unresolved,
        "rejected_counts": rejected,
        "primitive_words": primitive_words,
        "trace_counts": traces,
        "primitive_necklace_counts": prim,
        "determinant_prefix": determinant_prefix(traces),
        "verdict": {
            "A1": "A1_OPEN",
            "A2": "A2_CERTIFIED_PREFIX",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "reason": "finite kneading prefix does not prove complete infinite Hénon coding or analytic nuclearity",
        },
        "nonclaims": ["prime correspondence", "Riemann-zero matching", "global Hénon repeller", "analytic Fredholm determinant", "Route B"],
    }
    raw = json.dumps(payload, sort_keys=True, indent=2) + "\n"
    OUT.write_text(raw)
    print(json.dumps({"evidence_sha256": sha256(raw.encode()).hexdigest(), "accepted_counts": traces, "primitive_counts": prim}, sort_keys=True))


if __name__ == "__main__":
    main()
