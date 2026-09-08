"""One frozen AY8 exact falsification diagnostic; see DIAGNOSTIC_PROTOCOL.md."""

import itertools
import json
import resource
from collections import Counter

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024,) * 2)


def audit(k):
    bound = max(abs(k) + 1, 4)
    edges = {}
    vertices = 0
    for state in itertools.product(range(-bound, bound + 1), repeat=4):
        p, q, r, s = state
        denominator = 1 + p * s
        if denominator == 0 or 1 + r * q == 0:
            continue
        vertices += 1
        if k % denominator:
            continue
        h = k // denominator
        target = (r - h * p, s, p, q + h * s)
        if max(map(abs, target)) > bound:
            continue
        a, b, c, d = target
        if 1 + a * d == 0 or 1 + c * b == 0:
            continue
        edges[state] = target
    done = set()
    cycles = []
    for start in edges:
        if start in done:
            continue
        path = []
        index = {}
        state = start
        while state in edges and state not in done and state not in index:
            index[state] = len(path)
            path.append(state)
            state = edges[state]
        if state in index:
            cycles.append(path[index[state]:])
        done.update(path)
    nonzero = [cycle for cycle in cycles if any(any(v) for v in cycle)]
    return {
        "k": k,
        "bound": bound,
        "domain_vertices": vertices,
        "retained_edges": len(edges),
        "cycle_counts_by_least_period": dict(sorted(Counter(map(len, cycles)).items())),
        "one_nonzero_cycle": nonzero[0] if nonzero else None,
    }


if __name__ == "__main__":
    for parameter in (-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6):
        print(json.dumps(audit(parameter), sort_keys=True), flush=True)
