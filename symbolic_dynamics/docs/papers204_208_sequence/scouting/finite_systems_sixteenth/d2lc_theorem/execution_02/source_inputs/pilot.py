"""D2LC author theorem pressure, same six original graph boxes only."""
import collections
import hashlib
import itertools
import json
import pathlib
import sys

assert sys.flags.optimize == 0
CHECKS = 0


def check(condition):
    global CHECKS
    CHECKS += 1
    assert condition


def histogram(values):
    return [[key, count] for key, count in sorted(collections.Counter(values).items())]


def vertices(mask, n):
    return [v for v in range(n) if mask & (1 << v)]


def main():
    relative = ('docs/papers204_208_sequence/scouting/finite_systems_sixteenth/'
                'CANONICAL.json')
    original_path = pathlib.Path(__file__).parent.parent / 'historical_inputs' / relative
    original = json.loads(original_path.read_text())
    old_rows = {row['parameters'][0]: row for row in original['rows'] if row['map'] == 'D2LC'}
    rows = []
    for n in range(1, 7):
        checks_before = CHECKS
        edges = list(itertools.combinations(range(n), 2))
        edge_bit = {edge: 1 << i for i, edge in enumerate(edges)}
        order = 1 << len(edges)

        def graph(x):
            adjacent = [0] * n
            for i, (a, b) in enumerate(edges):
                if x & (1 << i):
                    adjacent[a] |= 1 << b
                    adjacent[b] |= 1 << a
            degree = [mask.bit_count() for mask in adjacent]
            active = [v for v in range(n) if degree[v] == 2]
            return adjacent, degree, active

        def toggle(x, adjacent, pivot):
            a, b = vertices(adjacent[pivot], n)
            return x ^ edge_bit[a, b]

        data = [graph(x) for x in range(order)]
        images = [toggle(x, data[x][0], data[x][2][0]) if data[x][2] else x
                  for x in range(order)]
        arrow_sha = hashlib.sha256(json.dumps(images, separators=(',', ':')).encode()).hexdigest()
        check(arrow_sha == old_rows[n]['integer_arrow_sha256'])
        predecessors = [[] for _ in range(order)]
        for x, y in enumerate(images):
            predecessors[y].append(x)
        depths, periods, supports = [], [], []
        for x in range(order):
            adjacent, degree, active = data[x]
            path, seen, at = [], {}, x
            while at not in seen:
                seen[at] = len(path)
                path.append(at)
                at = images[at]
            depth, period = seen[at], len(path) - seen[at]
            depths.append(depth)
            periods.append(period)
            if not active:
                predicted = 0
                support = set()
                recurrent = True
            else:
                p = active[0]
                a, b = vertices(adjacent[p], n)
                support = {p, a, b}
                epsilon = -1 if adjacent[a] & (1 << b) else 1
                newly_lower = [v for v in (a, b) if v < p and degree[v] == 2 - epsilon]
                recurrent = not newly_lower
                predicted = 0 if recurrent else 1
                if newly_lower and epsilon == -1:
                    q = min(newly_lower)
                    r = b if q == a else a
                    extras = vertices(adjacent[q] & ~((1 << p) | (1 << r)), n)
                    check(len(extras) == 1)
                    s = extras[0]
                    support.add(s)
                    predicted = 2 if s < q and degree[s] == 1 else 1
            check(depth == predicted)
            check((depth == 0) == recurrent)
            check(period == (2 if active else 1))
            check(len(support) <= 4)
            supports.append(len(support))
            support_mask = sum(1 << v for v in support)
            local_edge_mask = sum(1 << i for i, (a, b) in enumerate(edges)
                                  if a in support and b in support)
            residual = {v: min(3, (adjacent[v] & ~support_mask).bit_count())
                        for v in support}
            for at in path:
                current_adj, current_degree, current_active = data[at]
                check((x ^ at) & ~local_edge_mask == 0)
                check(all(current_adj[v] == adjacent[v] for v in range(n) if v not in support))
                local_active = sorted(v for v in support
                                      if residual[v] + (current_adj[v] & support_mask).bit_count() == 2)
                check((local_active[0] if local_active else None)
                      == (current_active[0] if current_active else None))
                local_image = (toggle(at, current_adj, local_active[0]) if local_active else at)
                check(local_image == images[at])
        equality_targets = []
        for y in range(order):
            adjacent, degree, active = data[y]
            if not active:
                candidates = []
                proposed = [y]
                triangle_equality = False
            else:
                u = active[0]
                neighbours = vertices(adjacent[u], n)
                candidates = [v for v in [u] + neighbours if degree[v] == 2]
                check(len(candidates) <= 3)
                proposed = []
                for v in candidates:
                    c, d = vertices(adjacent[v], n)
                    epsilon = -1 if adjacent[c] & (1 << d) else 1
                    acceptable = all(degree[h] + (epsilon if h in (c, d) else 0) != 2
                                     for h in range(v))
                    if acceptable:
                        proposed.append(toggle(y, adjacent, v))
                triangle = {u, *neighbours}
                triangle_equality = (all(degree[v] == 2 for v in triangle)
                                     and bool(adjacent[neighbours[0]] & (1 << neighbours[1]))
                                     and all(v > max(triangle) for v in active if v not in triangle))
            check(len(proposed) == len(set(proposed)))
            check(sorted(proposed) == predecessors[y])
            check(len(predecessors[y]) <= 3)
            if n >= 3:
                check((len(predecessors[y]) == 3) == triangle_equality)
                if triangle_equality:
                    equality_targets.append(y)
            else:
                check(predecessors[y] == [y])
        check(max(depths) == (0 if n <= 2 else 1 if n == 3 else 2))
        check(max(map(len, predecessors)) == (1 if n <= 2 else 3))
        check(histogram(depths) == old_rows[n]['depth_histogram'])
        check(len(equality_targets) == (old_rows[n]['max_fibre_target_count'] if n >= 3 else 0))
        rows.append({'n': n, 'states': order, 'max_tail': max(depths), 'max_period': max(periods),
                     'max_fibre': max(map(len, predecessors)),
                     'three_parent_equality_target_masks': equality_targets,
                     'depth_histogram': histogram(depths), 'support_size_histogram': histogram(supports),
                     'integer_arrow_sha256': arrow_sha, 'assertions': CHECKS - checks_before})
    print(json.dumps({'role': 'AUTHOR_THEOREM_CHECK_NOT_INDEPENDENT_REVIEW',
                      'literal_maps_executed': 1, 'complete_boxes': len(rows),
                      'new_literal_maps': 0, 'new_boxes': 0,
                      'state_map_pairs': sum(row['states'] for row in rows),
                      'assertions': CHECKS, 'rows': rows}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
