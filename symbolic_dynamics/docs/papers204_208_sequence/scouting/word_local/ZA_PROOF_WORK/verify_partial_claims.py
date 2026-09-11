#!/usr/bin/env python3
"""Check only the proved mask/image/fibre statements, not convergence."""
from collections import Counter
from itertools import product
from math import factorial
import json
from probe_complete_valid import zscan, rgfs
from nonexpansion_counterexample import right_recode


def main():
    rows = []
    for n in range(1, 9):
        carrier = tuple((0,)+w for w in product(*(range(n-i+1) for i in range(1, n))))
        fibres = Counter()
        sector_sizes = Counter()
        for x in carrier:
            y = zscan(x)
            assert all((x[i] == 0) != (y[i] == 0) for i in range(1, n))
            fibres[y] += 1
            sector_sizes[tuple(a == 0 for a in x[1:])] += 1
        for mask, count in sector_sizes.items():
            expected = 1
            for i, zero in enumerate(mask, 1):
                if not zero:
                    expected *= n-i
            assert count == expected
        maximal = sorted(x for x, c in fibres.items() if c == max(fibres.values()))
        expected_maximal = [(0,)*n] if n == 1 else [(0,)*n, (0,)*(n-1)+(1,)]
        assert maximal == expected_maximal
        assert max(fibres.values()) == factorial(n-1)
        for word in rgfs(n):
            renamed = right_recode(word)
            assert renamed[0] == 0
            assert all(0 <= renamed[i] <= n-i for i in range(1, n))
            assert zscan(word) == zscan(renamed)
        rows.append({"n": n, "ambient_states": len(carrier), "image": len(fibres),
                     "zero_mask_sectors": len(sector_sizes),
                     "max_fibre": max(fibres.values()), "maximal_targets": maximal})
    print(json.dumps({"scope": "proved partial claims only; no recurrence theorem asserted", "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
