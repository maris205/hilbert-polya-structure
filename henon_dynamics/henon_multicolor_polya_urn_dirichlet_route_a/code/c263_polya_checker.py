#!/usr/bin/env python3
"""Independent exact checker for HCS-C263; imports no producer code."""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c263_polya_evidence.json"
SOURCE = "98782afe1e754c311ad0736f72ce09dcc7c85c77"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


def F(value):
    return Fraction(value)


def rising(x, n):
    ans = Fraction(1)
    for j in range(n):
        ans *= x + j
    return ans


def falling(x, n):
    ans = 1
    for j in range(n):
        ans *= x - j
    return ans


def ph(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return sha256(raw.encode()).hexdigest()


def closed(n, counts, masses, c):
    coeff = math.factorial(n)
    for x in counts:
        coeff //= math.factorial(x)
    total = sum(masses)
    if c == 0:
        ans = Fraction(coeff)
        for a, x in zip(masses, counts):
            ans *= Fraction(a, total) ** x
        return ans
    alpha = [Fraction(a, c) for a in masses]
    ans = Fraction(coeff)
    for a, x in zip(alpha, counts):
        ans *= rising(a, x)
    return ans / rising(sum(alpha), n)


def word_prob(word, masses, c):
    counts = [0] * len(masses)
    total = sum(masses)
    ans = Fraction(1)
    for t, color in enumerate(word):
        ans *= Fraction(masses[color] + c * counts[color], total + c * t)
        counts[color] += 1
    return ans


def check(path):
    d = json.loads(path.read_text())
    a = 0
    def ok(condition):
        nonlocal a
        assert condition
        a += 1
    ok(d["schema"] == "hcs-c263-multicolor-polya-dirichlet-v1")
    ok(d["candidate_id"] == "HCS-C263")
    ok(d["source_commit"] == SOURCE)
    ok(d["scope_literal"] == SCOPE)
    ok(d["evaluator"]["sha256"] == EVAL)
    ok(d["payload_sha256"] == ph(d))
    ok(d["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"])
    ok(d["route_a"]["overall"] == "ROUTE_A_REJECTED")
    ok(d["route_a"]["route_b_invocation_allowed"] is False)
    for value in d["scope_flags"].values():
        ok(value is False)
    cases = {row["case_id"]: row for row in d["regression"]["cases"]}
    ok(len(cases) == 12)
    for case in cases.values():
        ok(sum(case["initial_masses"]) > 0)
        ok(case["reinforcement"] >= 0)
        ok((case["normalization"] is None) == (case["reinforcement"] == 0))
        if case["reinforcement"] > 0:
            ok([F(x) for x in case["normalization"]] == [Fraction(x, case["reinforcement"]) for x in case["initial_masses"]])

    comp = {}
    for row in d["regression"]["composition_rows"]:
        case = cases[row["case_id"]]
        masses = tuple(case["initial_masses"])
        c = case["reinforcement"]
        counts = tuple(row["counts"])
        n = row["n"]
        expected = closed(n, counts, masses, c)
        ok(sum(counts) == n)
        ok(F(row["recursive_probability"]) == F(row["closed_probability"]))
        ok(F(row["closed_probability"]) == expected)
        ok(row["multiplicity"] == math.factorial(n) // math.prod(math.factorial(x) for x in counts))
        comp[(row["case_id"], n, counts)] = expected
    for case_id, case in cases.items():
        for n in range(case["max_n"] + 1):
            ok(sum(value for (cid, level, _), value in comp.items() if cid == case_id and level == n) == 1)

    words_by_counts = {}
    for row in d["regression"]["ordered_word_rows"]:
        case = cases[row["case_id"]]
        word = tuple(row["word"])
        counts = tuple(row["counts"])
        ok(len(word) == case["max_n"])
        ok(all(0 <= x < case["K"] for x in word))
        ok(counts == tuple(word.count(i) for i in range(case["K"])))
        expected = word_prob(word, tuple(case["initial_masses"]), case["reinforcement"])
        ok(F(row["probability"]) == expected)
        words_by_counts.setdefault((row["case_id"], counts), []).append(expected)
    for row in d["regression"]["exchangeability_rows"]:
        values = words_by_counts[(row["case_id"], tuple(row["counts"]))]
        ok(row["word_count"] == len(values))
        ok(row["distinct_probabilities"] == len(set(values)) == 1)
        ok(F(row["per_word_probability"]) == values[0])
        ok(F(row["aggregate_probability"]) == sum(values))
        case = cases[row["case_id"]]
        key = (row["case_id"], case["max_n"], tuple(row["counts"]))
        ok(sum(values) == comp[key])

    for row in d["regression"]["marginal_rows"]:
        case = cases[row["case_id"]]
        n, color, x = row["n"], row["color"], row["x"]
        observed = sum(value for (cid, level, counts), value in comp.items() if cid == row["case_id"] and level == n and counts[color] == x)
        ok(F(row["observed"]) == observed)
        ok(F(row["closed"]) == observed)
        ok(row["family"] == ("binomial" if case["reinforcement"] == 0 else "beta_binomial"))

    moments = {(row["case_id"], row["n"]): row for row in d["regression"]["moment_rows"]}
    for (case_id, n), row in moments.items():
        case = cases[case_id]
        masses = case["initial_masses"]
        total = sum(masses)
        for i in range(case["K"]):
            ok(F(row["mean"][i]) == Fraction(n * masses[i], total))
            for j in range(case["K"]):
                entries = [(counts, value) for (cid, level, counts), value in comp.items() if cid == case_id and level == n]
                mi = sum(Fraction(counts[i]) * p for counts, p in entries)
                mj = sum(Fraction(counts[j]) * p for counts, p in entries)
                cov = sum(Fraction(counts[i] * counts[j]) * p for counts, p in entries) - mi * mj
                ok(F(row["covariance"][i][j]) == cov)
                if case["reinforcement"] == 0:
                    pi, pj = Fraction(masses[i], total), Fraction(masses[j], total)
                    formula = n * pi * (1 - pi) if i == j else -n * pi * pj
                else:
                    alpha_i = Fraction(masses[i], case["reinforcement"])
                    alpha_j = Fraction(masses[j], case["reinforcement"])
                    big_a = Fraction(total, case["reinforcement"])
                    if i == j:
                        formula = Fraction(n) * alpha_i * (big_a - alpha_i) * (big_a + n) / (big_a**2 * (big_a + 1))
                    else:
                        formula = -Fraction(n) * alpha_i * alpha_j * (big_a + n) / (big_a**2 * (big_a + 1))
                ok(F(row["covariance"][i][j]) == formula)
        ok(all(sum(F(x) for x in covariance_row) == 0 for covariance_row in row["covariance"]))

    for row in d["regression"]["factorial_rows"]:
        case = cases[row["case_id"]]
        r = tuple(row["multiindex"])
        n = row["n"]
        entries = [(counts, value) for (cid, level, counts), value in comp.items() if cid == row["case_id"] and level == n]
        observed = sum(Fraction(math.prod(falling(counts[i], r[i]) for i in range(case["K"]))) * p for counts, p in entries)
        ok(F(row["observed"]) == observed)
        R = sum(r)
        formula = Fraction(falling(n, R))
        if case["reinforcement"] == 0:
            total = sum(case["initial_masses"])
            for mass, degree in zip(case["initial_masses"], r):
                formula *= Fraction(mass, total) ** degree
        else:
            alpha = [Fraction(mass, case["reinforcement"]) for mass in case["initial_masses"]]
            for parameter, degree in zip(alpha, r):
                formula *= rising(parameter, degree)
            formula /= rising(sum(alpha), R)
        ok(F(row["closed"]) == observed == formula)

    for row in d["regression"]["martingale_rows"]:
        case = cases[row["case_id"]]
        masses, c = case["initial_masses"], case["reinforcement"]
        counts, n, i = row["counts"], row["n"], row["color"]
        denom = sum(masses) + c * n
        current = Fraction(masses[i] + c * counts[i], denom)
        future = Fraction(0)
        for color in range(case["K"]):
            pred = Fraction(masses[color] + c * counts[color], denom)
            future += pred * Fraction(masses[i] + c * (counts[i] + int(i == color)), denom + c)
        ok(F(row["current"]) == current)
        ok(F(row["expected_next"]) == future == current)

    for row in d["regression"]["de_finetti_rows"]:
        case = cases[row["case_id"]]
        ok(case["reinforcement"] > 0)
        counts = tuple(row["counts"])
        alpha = [Fraction(x, case["reinforcement"]) for x in case["initial_masses"]]
        moment = Fraction(1)
        for parameter, degree in zip(alpha, counts):
            moment *= rising(parameter, degree)
        moment /= rising(sum(alpha), sum(counts))
        ok(F(row["ordered_word_probability"]) == moment)
        ok(F(row["dirichlet_monomial_moment"]) == moment)

    counts = d["regression"]["counts"]
    for key, value in counts.items():
        ok(value == len(d["regression"][key]))
    ok(any(case["reinforcement"] == 0 for case in cases.values()))
    ok(any(0 in case["initial_masses"] for case in cases.values()))
    ok(any(case["K"] == 1 for case in cases.values()))
    return a


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=DEFAULT)
    args = parser.parse_args()
    assertions = check(args.evidence)
    print(f"C263 independent checker: PASS ({assertions} assertions; producer_imported=false)")


if __name__ == "__main__":
    main()
