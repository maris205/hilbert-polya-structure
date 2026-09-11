#!/usr/bin/env python3
"""Original small full-box cyclic-predator count scout; profiler reuse only."""
from itertools import product
import json
from pilot import profile


def update(x):
    n = len(x)
    return tuple(int(x[i-1] == (x[i]+1)%3) +
                 int(x[(i+1)%n] == (x[i]+1)%3) for i in range(n))


for n in range(3,10):
    states = list(product(range(3),repeat=n))
    result = profile(states,update)
    result.update({'candidate':'CPC','n':n})
    print(json.dumps(result,sort_keys=True),flush=True)
