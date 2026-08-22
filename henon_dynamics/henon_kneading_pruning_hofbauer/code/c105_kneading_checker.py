#!/usr/bin/env python3
"""Independent reconstruction of the C105 finite-prefix ledger."""
from __future__ import annotations

from fractions import Fraction
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c105_kneading_evidence.json"


def morph(length: int) -> str:
    s = "0"
    while len(s) < length:
        s = "".join("01" if x == "0" else "011" for x in s)
    return s[:length]


def bounds() -> tuple[str, str]:
    s = morph(32)
    tail = s[1:]
    return "0" + "0" * 5 + tail[5:], "1" + "1" * 5 + "".join("1" if x == "0" else "0" for x in tail[5:])


def cmp(period: str, shift: int, bound: str) -> int | None:
    for j, b in enumerate(bound):
        a = period[(shift + j) % len(period)]
        if a != b:
            return -1 if a < b else 1
    return None


def accepted(w: str, lo: str, hi: str) -> bool:
    for j in range(len(w)):
        a, b = cmp(w, j, lo), cmp(w, j, hi)
        if a is None or b is None or a < 0 or b > 0:
            return False
    return True


def primitive(w: str) -> bool:
    return all(len(w) % d or w != w[:d] * (len(w) // d) for d in range(1, len(w)))


def main() -> None:
    doc = json.loads(EVIDENCE.read_text())
    lo, hi = bounds()
    traces = {}
    for n in range(1, int(doc["period_max"]) + 1):
        words = ["".join(bits) for bits in itertools.product("01", repeat=n) if accepted("".join(bits), lo, hi)]
        expected = doc["accepted_words"][str(n)]
        assert words == expected, (n, len(words), len(expected))
        assert all(accepted(w[i:] + w[:i], lo, hi) for w in words for i in range(n))
        assert sorted(w for w in words if primitive(w)) == doc["primitive_words"][str(n)]
        traces[n] = len(words)
    assert traces == {int(k): v for k, v in doc["trace_counts"].items()}
    for n in traces:
        lhs = traces[n]
        rhs = sum(d * doc["primitive_necklace_counts"][str(d)] for d in range(1, n + 1) if n % d == 0)
        assert lhs == rhs, (n, lhs, rhs)
    c = [Fraction(1)]
    for n in range(1, max(traces) + 1):
        c.append(-sum(Fraction(traces[k]) * c[n - k] for k in range(1, n + 1)) / n)
    assert [f"{x.numerator}/{x.denominator}" for x in c] == doc["determinant_prefix"]
    assert doc["verdict"]["A1"] == "A1_OPEN"
    assert doc["verdict"]["A2"] == "A2_CERTIFIED_PREFIX"
    print("C105_CHECK_PASS")


if __name__ == "__main__":
    main()
