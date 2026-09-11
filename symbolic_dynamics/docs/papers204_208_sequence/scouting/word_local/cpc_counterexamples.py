#!/usr/bin/env python3
"""Named cycle witnesses inside the original CPC boxes; direct new formula."""
from itertools import product
import json


def step(x):
    return tuple(sum((x[j]-x[i])%3 == 1 for j in ((i-1)%len(x),(i+1)%len(x)))
                 for i in range(len(x)))


for n, wanted in ((8,32),(9,30)):
    found = None
    for x in product(range(3),repeat=n):
        seen = {}; path = []; y = x
        while y not in seen:
            seen[y] = len(path); path.append(y); y = step(y)
        cycle = path[seen[y]:]
        if len(cycle) == wanted:
            assert len(set(cycle)) == wanted
            assert all(step(cycle[i]) == cycle[(i+1)%wanted] for i in range(wanted))
            found = {'n':n,'exact_period':wanted,'cycle':cycle}
            break
    assert found is not None
    print(json.dumps(found,sort_keys=True))
