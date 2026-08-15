#!/usr/bin/env python3
import itertools
import json
from fractions import Fraction
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]

def palindrome(half):
    return half + half[:0:-1]

def u(word, center, radius):
    n = len(word)
    return int(all(word[(center-k) % n] == word[(center+k) % n] for k in range(1, radius+1)))

rows = []
for radius in range(1, 6):
    n = 2*radius + 11
    words = [palindrome(half) for half in itertools.product((0, 1), repeat=(n+1)//2)]
    mean = Fraction(sum(u(word, 1, radius) for word in words), len(words))
    if mean != Fraction(1, 2**radius):
        raise ArithmeticError
    rows.append({"radius": radius, "mean": str(mean), "v_anomaly": str(2*(1-mean))})
result = {"candidate_id": "HCS-P66-INDEPENDENT", "rows": rows, "check": True}
(PROJECT / "results/c66_independent_check.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({"check": True, "rows": 5}, sort_keys=True))
