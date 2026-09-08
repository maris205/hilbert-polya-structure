"""Single predeclared tiny LAR scout, n<=6, complete canonical stdout."""
import itertools
import sys


def trees(n):
    if n == 1:
        yield ()
        return
    for code in itertools.product(range(1, n + 1), repeat=max(0, n - 2)):
        degree = [0] + [1] * n
        for x in code:
            degree[x] += 1
        edges = []
        for x in code:
            leaf = next(v for v in range(1, n + 1) if degree[v] == 1)
            edges.append(tuple(sorted((leaf, x))))
            degree[leaf] -= 1
            degree[x] -= 1
        last = [v for v in range(1, n + 1) if degree[v] == 1]
        edges.append(tuple(last))
        yield tuple(sorted(edges))


def adjacency(vertices, edges):
    out = {v: [] for v in vertices}
    for a, b in edges:
        out[a].append(b)
        out[b].append(a)
    return out


def distances(adj, v):
    out = {v: 0}
    queue = [v]
    for x in queue:
        for y in adj[x]:
            if y not in out:
                out[y] = out[x] + 1
                queue.append(y)
    return out


def farthest(adj, v):
    dd = distances(adj, v)
    return min(dd, key=lambda x: (-dd[x], x))


def leaf(adj):
    return min(v for v in adj if len(adj[v]) == 1)


def relay(n, edges):
    if n <= 2:
        return edges
    adj = adjacency(range(1, n + 1), edges)
    v = leaf(adj)
    a = farthest(adj, v)
    return tuple(sorted([e for e in edges if v not in e]
                        + [tuple(sorted((v, a)))]))


def skeleton(n, edges, v):
    return adjacency([x for x in range(1, n + 1) if x != v],
                     [e for e in edges if v not in e])


def canonical_pair(adj):
    eccentric = {v: max(distances(adj, v).values()) for v in adj}
    diameter = max(eccentric.values())
    p = min(v for v in adj if eccentric[v] == diameter)
    return p, farthest(adj, p)


def recurrence_prediction(n, edges):
    if n <= 2:
        return True
    adj = adjacency(range(1, n + 1), edges)
    v = leaf(adj)
    s = skeleton(n, edges, v)
    p, q = canonical_pair(s)
    return (adj[v][0] in (p, q)
            and all(v < x for x in s if len(s[x]) == 1))


def inverse_prediction(n, edges):
    if n <= 2:
        return 1, ()
    adj = adjacency(range(1, n + 1), edges)
    leaves = sorted(v for v in adj if len(adj[v]) == 1)
    m = leaves[0]
    base = 0
    a = adj[m][0]
    if len(adj[a]) == 2 and a > m:
        s = skeleton(n, edges, m)
        base = sum(farthest(s, u) == a for u in s)
    v = leaves[1]
    b = adj[v][0]
    extra = 0
    if len(adj[b]) == 2 and b > v:
        s = skeleton(n, edges, v)
        extra = int(farthest(s, m) == b)
    return base + extra, (base, extra)


def main():
    checks = 0
    for n in range(1, 7):
        states = sorted(trees(n))
        assert len(states) == len(set(states)) == (1 if n <= 2 else n ** (n - 2))
        index = {state: i for i, state in enumerate(states)}
        targets = [index[relay(n, state)] for state in states]
        indegree = [0] * len(states)
        for target in targets:
            indegree[target] += 1
        tails, periods = [], []
        for i, state in enumerate(states):
            seen, orbit = {}, []
            x = i
            while x not in seen:
                seen[x] = len(orbit)
                orbit.append(x)
                x = targets[x]
            tau, period = seen[x], len(orbit) - seen[x]
            tails.append(tau)
            periods.append(period)
            rec = recurrence_prediction(n, state)
            fib, parts = inverse_prediction(n, state)
            print(('state', n, i, state, targets[i], tau, period,
                   indegree[i], rec, fib, parts), flush=True)
            assert rec == (tau == 0), ('recurrence', n, i)
            assert fib == indegree[i], ('inverse', n, i, fib, indegree[i])
            if n >= 3:
                assert period == 2, ('period', n, i)
                adj = adjacency(range(1, n + 1), state)
                nxt = adjacency(range(1, n + 1), states[targets[i]])
                assert leaf(nxt) <= leaf(adj), ('label', n, i)
                p, q = canonical_pair(adj)
                assert set(farthest(adj, v) for v in adj) == {p, q}, ('pair', n, i)
                checks += 3
            checks += 2
        print(('summary', n, len(states), sum(d > 0 for d in indegree),
               sum(t == 0 for t in tails), max(tails), sorted(set(periods)),
               max(indegree), tuple(i for i, d in enumerate(indegree) if d == max(indegree))),
              flush=True)
        assert max(tails) == (0 if n <= 2 else n - 2), ('tail_max', n)
        assert max(indegree) <= (1 if n <= 2 else n - 1), ('fibre_bound', n)
        checks += 3
    print(('PASS', 'author_tiny_pressure_only', checks), flush=True)
    print(('runtime', sys.version, sys.executable,
           tuple(sorted((k, getattr(v, '__file__', None)) for k, v in sys.modules.items()))),
          file=sys.stderr, flush=True)


if __name__ == '__main__':
    main()
