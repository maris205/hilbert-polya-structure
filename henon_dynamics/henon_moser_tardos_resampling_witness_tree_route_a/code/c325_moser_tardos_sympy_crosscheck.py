#!/usr/bin/env python3
"""Disjoint SymPy checks for HCS-C325."""
import json
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c325_moser_tardos_evidence.json"


def main():
    if sys.flags.optimize:
        raise RuntimeError("C325 SymPy lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    checks = 0
    for instance in data["instance_rows"]:
        live = [row for row in instance["transition_rows"] if row["chosen_event"] is not None]
        locate = {row["state"]: index for index, row in enumerate(live)}
        matrix = sp.eye(len(live))
        for i, row in enumerate(live):
            for target in row["targets"]:
                if target["state"] in locate:
                    matrix[i, locate[target["state"]]] -= sp.Rational(target["probability"])
        for receipt in instance["expected_resamplings_by_event"]:
            rhs = sp.Matrix([int(row["chosen_event"] == receipt["label"]) for row in live])
            solution = matrix.inv() * rhs
            value = sum(solution, sp.S.Zero) / (2 ** instance["variable_count"])
            if sp.simplify(value - sp.Rational(receipt["value"])) != 0:
                raise AssertionError("absorbing expectation")
            checks += 1
        for event in instance["event_rows"]:
            p, rhs = sp.Rational(event["probability"]), sp.Rational(event["lll_rhs"])
            x, bound = sp.Rational(event["witness_x"]), sp.Rational(event["expectation_bound"])
            if p > rhs or sp.simplify(bound - x / (1 - x)) != 0:
                raise AssertionError("LLL/branching identity")
            if sp.Rational(event["witness_tree_weight_by_size_1_to_6"][0]) != p:
                raise AssertionError("one-node witness tree")
            checks += 2
    print(f"C325 SymPy cross-check: PASS ({checks} identities)")


if __name__ == "__main__":
    main()
