#!/usr/bin/env python3
"""Test weaker prefix nonexpansion and scalar monotonicity on valid arrays."""
from collections import Counter
import json
from probe_complete_valid import rgfs, zscan


def main():
    rows = []
    for n in range(2, 12):
        valid = sorted(set(map(zscan, rgfs(n))))
        groups = {}
        for x in valid:
            gx = zscan(zscan(x))
            mask = tuple(a == 0 for a in x)
            for i in range(1, n):
                groups.setdefault((mask, x[:i], i), []).append((x[i], gx[i], x))
        nonexpansion_witness, monotone_witness = None, None
        nonexpansion_failures, monotone_failures = 0, 0
        maps = Counter()
        nontrivial_groups = 0
        for (mask, prefix, i), values in groups.items():
            scalar = {}
            for v, gv, x in values:
                if v in scalar and scalar[v][0] != gv:
                    nonexpansion_failures += 1
                    if nonexpansion_witness is None:
                        y = scalar[v][1]
                        nonexpansion_witness = {"i": i, "x": y, "y": x,
                                                "Gx": zscan(zscan(y)), "Gy": zscan(zscan(x))}
                else:
                    scalar[v] = gv, x
            pairs = sorted((v, gv[0]) for v, gv in scalar.items())
            if len(pairs) > 1:
                nontrivial_groups += 1
                maps[tuple(pairs)] += 1
                if any(a[1] > b[1] for a, b in zip(pairs, pairs[1:])):
                    monotone_failures += 1
                    if monotone_witness is None:
                        monotone_witness = {"mask": mask, "prefix": prefix, "i": i,
                                            "pairs": pairs}
        rows.append({"n": n, "valid_arrays": len(valid),
                     "nontrivial_scalar_groups": nontrivial_groups,
                     "prefix_nonexpansion_failures": nonexpansion_failures,
                     "nonexpansion_witness": nonexpansion_witness,
                     "scalar_monotonicity_failures": monotone_failures,
                     "monotone_witness": monotone_witness,
                     "scalar_maps": [{"pairs": pairs, "count": c} for pairs, c in sorted(maps.items())]})
    print(json.dumps({"scope": "full valid arrays, finite falsification only", "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
