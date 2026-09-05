#!/usr/bin/env python3
"""All restricted-growth realizers yield the complete valid-Z image."""
from itertools import product
import json
from probe_prefix import zstep


def zscan(word):
    return (0,) + tuple(next((j for j, (a, b) in enumerate(zip(word, word[i:])) if a != b),
                            len(word)-i) for i in range(1, len(word)))


def rgfs(n):
    def rec(word, maximum):
        if len(word) == n:
            yield word
        else:
            for a in range(maximum+2):
                yield from rec(word+(a,), max(maximum, a))
    yield from rec((0,), 0)


def main():
    independent_literal_checks = 0
    for n in range(1, 8):
        for word in product(range(3), repeat=n):
            assert zscan(word) == zstep(word)
            independent_literal_checks += 1
    rows = []
    for n in range(2, 12):
        valid, source_count = set(), 0
        for word in rgfs(n):
            valid.add(zscan(word))
            source_count += 1
        reference, witness, failures, comparisons = {}, None, 0, 0
        cores = {}
        max_tail, max_witness = 0, None
        for x in sorted(valid):
            mask = tuple(a == 0 for a in x)
            gx = zscan(zscan(x))
            for i in range(1, n):
                key = mask, x[:i], i
                if key in reference:
                    comparisons += 1
                    if reference[key][0] != gx[i]:
                        failures += 1
                        if witness is None:
                            witness = {"x": reference[key][1], "y": x, "i": i,
                                       "Gx": zscan(zscan(reference[key][1])), "Gy": gx}
                else:
                    reference[key] = gx[i], x
            path, where, y = [], {}, x
            while y not in where:
                where[y] = len(path)
                path.append(y)
                y = zscan(y)
            h, period = where[y], len(path)-where[y]
            assert period == 2
            endpoint = path[h + h % 2]
            cores.setdefault(mask, set()).add(endpoint)
            if h > max_tail:
                max_tail, max_witness = h, x
        rows.append({"n": n, "complete_rgf_sources": source_count,
                     "complete_valid_arrays": len(valid),
                     "comparable_prefix_groups": comparisons,
                     "two_step_prefix_failures": failures, "first_witness": witness,
                     "max_valid_tail": max_tail, "max_valid_witness": max_witness,
                     "zero_masks": len(cores),
                     "max_phase_endpoints_per_mask": max(map(len, cores.values()))})
    print(json.dumps({"independent_literal_checks": independent_literal_checks,
                      "scope": "all equality patterns via restricted growth words; complete valid-Z arrays",
                      "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
