#!/usr/bin/env python3
"""Independent signed-edge and composition-power MCT control. No file I/O."""
from itertools import combinations
from collections import Counter

ASSERTIONS = 0


def check(ok, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not ok:
        raise AssertionError(message)


def setup(n):
    edges = tuple(combinations(range(n), 2))
    edge_index = {e: i for i, e in enumerate(edges)}
    triples = tuple(combinations(range(n), 3))
    supports = tuple(tuple(edge_index[e] for e in combinations(t, 2))
                     for t in triples)
    masks = tuple(sum(1 << e for e in supp) for supp in supports)
    return edges, edge_index, triples, supports, masks


def edge(i, j):
    return (i, j) if i < j else (j, i)


def signs(rank, size):
    return tuple(1 if rank & (1 << j) else -1 for j in range(size))


def mono(s, supp):
    a, b, c = (s[i] for i in supp)
    return (1 + a*b + a*c + b*c) // 4


def least(s, supports):
    return next((i for i, supp in enumerate(supports)
                 if abs(sum(s[e] for e in supp)) == 3), -1)


def revised_indicator(s, supp, reversal):
    a, b, c = (s[e] * (-1 if e in reversal else 1) for e in supp)
    return (1 + a*b + a*c + b*c) // 4


def inverse_indices(s, supports):
    eligible = set()
    for q, supp in enumerate(supports):
        if not mono(s, supp):
            continue
        # Every summand is0 or1, so zero sum excludes all earlier priorities.
        energy = sum(revised_indicator(s, p, supp) for p in supports[:q])
        if energy == 0:
            eligible.add(q)
    return eligible


def star_certificate(s, n, ab, edge_index, triples, supports):
    a, b = ab
    outside = tuple(v for v in range(n) if v not in ab)
    c = s[edge_index[ab]]
    if any(s[edge_index[edge(a, v)]] != c or
           s[edge_index[edge(b, v)]] != c for v in outside):
        return False
    faces = {tuple(sorted((a, b, v))) for v in outside}
    last = max(faces)
    for x, y in combinations(outside, 2):
        if s[edge_index[x, y]] == c:
            for z in outside:
                if z not in (x, y) and not (
                        tuple(sorted((a, b, z))) < tuple(sorted((a, x, y)))):
                    return False
    for tri, supp in zip(triples, supports):
        if not (a in tri or b in tri) and mono(s, supp) and tri <= last:
            return False
    return True


def top_certificate(s, n, vertices, edge_index, triples, supports):
    internal = tuple(combinations(vertices, 2))
    c = s[edge_index[internal[0]]]
    if any(s[edge_index[e]] != c for e in internal):
        return False
    faces = tuple(combinations(vertices, 3))
    last = max(faces)
    vertex_set = set(vertices)
    for tri, supp in zip(triples, supports):
        if len(vertex_set.intersection(tri)) <= 1 and mono(s, supp) and tri <= last:
            return False
    for u in range(n):
        if u in vertex_set:
            continue
        for x, y in internal:
            d = s[edge_index[edge(u, x)]]
            if d != s[edge_index[edge(u, y)]]:
                continue
            forbidden = tuple(q for q in faces
                              if ((x in q and y in q) == (d == -c)))
            if tuple(sorted((u, x, y))) <= max(forbidden):
                return False
    return True


def powers_and_depths(mapping):
    size = len(mapping)
    powers = [mapping]
    exponent = 1
    while exponent < 2*size:
        last = powers[-1]
        powers.append(tuple(last[last[x]] for x in range(size)))
        exponent *= 2
    projection = powers[-1]
    check(all(projection[projection[x]] == projection[x] for x in range(size)),
          "whole-map even power is idempotent")
    core = tuple(projection[x] == x for x in range(size))
    check(all(core[x] == (mapping[mapping[x]] == x) for x in range(size)),
          "discovered core equals fixed F squared")
    depths = []
    for x in range(size):
        if core[x]:
            depths.append(0)
            continue
        position, elapsed = x, 0
        for j in range(len(powers)-1, -1, -1):
            new = powers[j][position]
            if not core[new]:
                position = new
                elapsed += 1 << j
        check(elapsed < size and core[mapping[position]], "exact first entry")
        depths.append(elapsed+1)
    return core, tuple(depths)


def full_box(n):
    edges, edge_index, triples, supports, masks = setup(n)
    size = 1 << len(edges)
    vectors = tuple(signs(x, len(edges)) for x in range(size))
    selectors = tuple(least(s, supports) for s in vectors)
    mapping = tuple(x if q < 0 else x ^ masks[q]
                    for x, q in enumerate(selectors))
    incoming = [set() for _ in range(size)]
    for x, y in enumerate(mapping):
        incoming[y].add(x)
    core, depths = powers_and_depths(mapping)
    for x, s in enumerate(vectors):
        q, y = selectors[x], mapping[x]
        check(all(mono(s, supp) == (abs(sum(s[e] for e in supp)) == 3)
                  for supp in supports), "quadratic indicator literal equality")
        if q >= 0:
            check(selectors[y] >= 0 and selectors[y] <= q, "priority descent")
            check(core[x] == (selectors[y] == q), "local recurrent iff")
            check(depths[x] == 0 if core[x] else depths[x] == depths[y]+1,
                  "first-entry clock recurrence")
            for v in range(n):
                incident = [i for i, e in enumerate(edges) if v in e]
                check(sum(s[i] == 1 for i in incident) % 2 ==
                      sum(vectors[y][i] == 1 for i in incident) % 2,
                      "old degree-parity invariant")
        else:
            check(core[x] and depths[x] == 0, "holding is recurrent")
        used = set(triples[q]) if q >= 0 else set()
        position = x
        for _ in range(depths[x]):
            nxt = mapping[position]
            old_tri, new_tri = set(triples[selectors[position]]), set(triples[selectors[nxt]])
            check(len(new_tri-old_tri) == 1 and len(new_tri-used) == 1,
                  "strict transition introduces unused vertex")
            used.update(new_tri)
            position = nxt
        check(core[position], "trace terminates at first recurrent state")
        eligible = inverse_indices(s, supports)
        decoded = {x ^ masks[q] for q in eligible}
        if selectors[x] < 0:
            decoded.add(x)
        check(decoded == incoming[x], "correlation decoder entire source set")
        for p, q in combinations(sorted(eligible), 2):
            check(len(set(triples[p]).intersection(triples[q])) == 2,
                  "owned Johnson clique cap prerequisite")
        if n >= 4:
            stars = []
            tops = []
            for ab in edges:
                faces = {i for i, t in enumerate(triples) if set(ab) <= set(t)}
                certificate = star_certificate(s, n, ab, edge_index, triples, supports)
                check(certificate == (faces <= eligible), "all-star target certificate")
                stars.append(certificate)
            for vertices in combinations(range(n), 4):
                faces = {i for i, t in enumerate(triples) if set(t) <= set(vertices)}
                certificate = top_certificate(s, n, vertices, edge_index, triples, supports)
                check(certificate == (faces <= eligible), "all-top target certificate")
                tops.append(certificate)
            equality = (any(tops) if n < 6 else any(stars) or any(tops)
                        if n == 6 else any(stars))
            check((len(incoming[x]) == max(4, n-2)) == equality,
                  "complete maximum-target classification")
        else:
            check(len(incoming[x]) == 1, "small-size every fibre singleton")
    check(max(depths) == max(0, n-3), "all-size height at this full box")
    maximum = 1 if n <= 3 else max(4, n-2)
    check(max(map(len, incoming)) == maximum, "sharp maximum fibre at full box")
    fixed = sum(mapping[x] == x for x in range(size))
    check(fixed == (1, 1, 2, 6, 18, 12, 0)[n], "owned Ramsey small fixed census")
    print("n=%d states=%d image=%d fixed=%d core=%d depth=%s max_fibre=%d maximizers=%d" %
          (n, size, sum(bool(v) for v in incoming), fixed, sum(core),
           tuple(sorted(Counter(depths).items())), maximum,
           sum(len(v) == maximum for v in incoming)))


def temporal_witness(n):
    edges, edge_index, triples, supports, _ = setup(n)
    v = tuple(range(n-1, 0, -1))
    spoke = tuple(0 if i <= 1 else (i-1) % 2 for i in range(n-1))
    bits = {}
    for i, vertex in enumerate(v):
        bits[0, vertex] = spoke[i]
    for i, j in combinations(range(n-1), 2):
        colour = (i % 2 if j == i+1 else
                  1-spoke[i] if spoke[i] == spoke[j] else spoke[i])
        bits[edge(v[i], v[j])] = colour
    s = tuple(2*bits[e]-1 for e in edges)
    for t in range(n-2):
        q = least(s, supports)
        check(q >= 0 and triples[q] == tuple(sorted((0, v[t], v[t+1]))),
              "uniform witness exact ordered selector")
        check(s[supports[q][0]] == 2*(t % 2)-1, "witness alternating colours")
        after = tuple(-value if i in supports[q] else value for i, value in enumerate(s))
        if t == n-3:
            check(least(after, supports) == q, "sharp endpoint already recurrent")
        else:
            check(least(after, supports) < q, "witness strict step")
        s = after


def inverse_witness(n, colour, family):
    edges, edge_index, triples, supports, _ = setup(n)
    if family == "star":
        bits = {e: colour if 0 in e or 1 in e else 1-colour for e in edges}
        expected_faces = {i for i, t in enumerate(triples) if 0 in t and 1 in t}
    else:
        bits = {e: 1-colour if e[0] == 0 and e[1] >= 4 else colour for e in edges}
        expected_faces = {i for i, t in enumerate(triples) if max(t) <= 3}
    s = tuple(2*bits[e]-1 for e in edges)
    eligible = inverse_indices(s, supports)
    check(expected_faces <= eligible, "literal extremal family realized")
    check(len(eligible) <= max(4, n-2), "owned static cap on realized target")
    if (family == "star" and n >= 6) or (family == "top" and n <= 6):
        check(len(eligible) == max(4, n-2), "correct crossover sharp witness")


def main():
    print("MCT signed correlations and whole-map powers; independent finite control")
    for n in range(7):
        full_box(n)
    for n in range(3, 81):
        temporal_witness(n)
    for n in range(4, 25):
        for colour in (0, 1):
            for family in ("star", "top"):
                inverse_witness(n, colour, family)
    print("full_boxes=n0..6; temporal_witness=n3..80; inverse_witness=n4..24")
    print("status=PASS")
    print("assertions=%d" % ASSERTIONS)
    print("finite_failed_assertions=0; NOT_A_REVIEW_VERDICT; HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
