#!/usr/bin/env python3
"""Falsification of a different route: same-mask lexicographic antitonicity."""
from random import Random
import json
from probe_complete_valid import rgfs, zscan


def main():
    rows = []
    for n in range(2, 12):
        groups = {}
        for x in set(map(zscan, rgfs(n))):
            groups.setdefault(tuple(a == 0 for a in x), []).append(x)
        failures, witness, pairs = 0, None, 0
        for group in groups.values():
            ordered = sorted(group)
            for x, y in zip(ordered, ordered[1:]):
                pairs += 1
                fx, fy = zscan(x), zscan(y)
                if fx < fy:
                    failures += 1
                    if witness is None:
                        witness = {"x": x, "y": y, "Fx": fx, "Fy": fy}
        rows.append({"n": n, "adjacent_same_mask_pairs": pairs,
                     "antitone_failures": failures, "witness": witness})
    rng = Random(204208)
    stress = []
    for n in (16, 32, 64, 128):
        anti, nonexp, comparisons, witness = 0, 0, 0, None
        for _ in range(4000):
            source = (0,)+tuple(rng.randrange(3) for _ in range(n-1))
            i = rng.randrange(1, n)
            if source[i] == 0:
                continue
            mutated = source[:i]+(3-source[i],)+source[i+1:]
            x, y = sorted((zscan(source), zscan(mutated)))
            if x == y:
                continue
            comparisons += 1
            fx, fy = zscan(x), zscan(y)
            d = next(i for i in range(n) if x[i] != y[i])
            gx, gy = zscan(fx), zscan(fy)
            if fx < fy:
                anti += 1
                if witness is None:
                    witness = {"source": source, "mutated": mutated,
                               "x": x, "y": y, "Fx": fx, "Fy": fy}
            nonexp += gx[:d] != gy[:d]
        stress.append({"n": n, "trials": 4000, "nonidentical_same_mask_pairs": comparisons,
                       "lex_antitone_failures": anti, "two_step_prefix_nonexpansion_failures": nonexp,
                       "first_antitone_witness": witness})
    print(json.dumps({"complete_valid_checks": rows,
                      "random_mutated_realizer_checks": stress,
                      "seed": 204208}, indent=2))


if __name__ == "__main__":
    main()
