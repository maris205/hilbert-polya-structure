"""Exact bounded semigroup/SCC diagnostic; no spectral extrapolation.

Run from this directory. Standard output is the entire result; no files
are written by this program. Matrix products are chronological (left
multiplication). SCC periods are graph invariants, not proved residues
of the full switching zeta.
"""

from collections import Counter, deque
from math import gcd
import json
import time


def successors(state, modulus):
    a, b, c, d, last = state
    if last != 0:
        yield ((3*a+c) % modulus, (3*b+d) % modulus,
               (a+3*c) % modulus, (b+3*d) % modulus, 0)
    yield ((3*a+2*c) % modulus, (3*b+2*d) % modulus,
           (2*a+4*c) % modulus, (2*b+4*d) % modulus, 1)


def graph(k, cap):
    modulus = 2**k
    states = [(1, 0, 0, 1, 2)]
    indices = {states[0]: 0}
    edges = []
    cursor = 0
    while cursor < len(states):
        row = []
        for nxt in successors(states[cursor], modulus):
            target = indices.get(nxt)
            if target is None:
                if len(states) == cap:
                    return None, None, {"k": k, "status": "STATE_CAP",
                                        "states": cap, "expanded": cursor}
                target = len(states)
                states.append(nxt)
                indices[nxt] = target
            row.append(target)
        edges.append(row)
        cursor += 1
    return states, edges, None


def components(edges):
    count = len(edges)
    reverse = [[] for _ in edges]
    for source, targets in enumerate(edges):
        for target in targets:
            reverse[target].append(source)
    seen = bytearray(count)
    order = []
    for root in range(count):
        if seen[root]:
            continue
        seen[root] = 1
        stack = [(root, 0)]
        while stack:
            node, cursor = stack[-1]
            if cursor == len(edges[node]):
                order.append(node)
                stack.pop()
                continue
            stack[-1] = (node, cursor+1)
            nxt = edges[node][cursor]
            if not seen[nxt]:
                seen[nxt] = 1
                stack.append((nxt, 0))
    labels = [-1] * count
    groups = []
    for root in reversed(order):
        if labels[root] >= 0:
            continue
        label = len(groups)
        labels[root] = label
        stack = [root]
        group = []
        while stack:
            node = stack.pop()
            group.append(node)
            for nxt in reverse[node]:
                if labels[nxt] < 0:
                    labels[nxt] = label
                    stack.append(nxt)
        groups.append(group)
    return groups, labels


def analyze(k, states, edges):
    groups, labels = components(edges)
    records = []
    for label, group in enumerate(groups):
        if any(labels[target] != label for node in group for target in edges[node]):
            continue
        depths = {group[0]: 0}
        queue = deque([group[0]])
        period = 0
        while queue:
            node = queue.popleft()
            for nxt in edges[node]:
                if nxt not in depths:
                    depths[nxt] = depths[node]+1
                    queue.append(nxt)
                period = gcd(period, abs(depths[node]+1-depths[nxt]))
        assert len(depths) == len(group) and period > 0
        accepted = [node for node in group
                    if (states[node][0]+states[node][3]-1) % (2**k) == 0]
        records.append({"size": len(group), "period": period,
                        "trace_one_states": len(accepted),
                        "accepted_depth_residues": dict(sorted(Counter(
                            depths[node] % period for node in accepted).items()))})
    return {"k": k, "status": "COMPLETE_FINITE_GRAPH", "states": len(states),
            "edges": sum(map(len, edges)), "scc_count": len(groups),
            "closed_scc_count": len(records),
            "closed_period_counts": dict(sorted(Counter(
                record["period"] for record in records).items())),
            "closed_components": records}


def main():
    for k in range(1, 7):
        start = time.monotonic()
        states, edges, failure = graph(k, 250_000)
        result = failure or analyze(k, states, edges)
        result["elapsed_seconds"] = round(time.monotonic()-start, 4)
        print(json.dumps(result, sort_keys=True), flush=True)
        if failure:
            break


if __name__ == "__main__":
    main()
