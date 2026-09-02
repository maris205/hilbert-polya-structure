#!/usr/bin/env python3
"""Independent exhaustive checks for P166 replacement discovery round 2.

No project module is imported.  The four literal maps are implemented from
their definitions on independently generated small carriers.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from math import comb


ASSERTIONS = 0


def claim(value: bool, note: str = "") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not value:
        raise AssertionError(note)


def digest(rows) -> str:
    return sha256("\n".join(map(str, rows)).encode()).hexdigest()


def ceil_log2(n: int) -> int:
    if n <= 1:
        return 0
    return (n - 1).bit_length()


# ---------------------------------------------------------------------------
# PSE: strict-square erosion of a labelled poset.


def posets(n: int):
    pairs = list(combinations(range(n), 2))
    for choices in product((-1, 0, 1), repeat=len(pairs)):
        rel = set()
        for (a, b), choice in zip(pairs, choices):
            if choice == 1:
                rel.add((a, b))
            elif choice == -1:
                rel.add((b, a))
        ok = True
        for a, b in tuple(rel):
            for c, d in tuple(rel):
                if b == c and a != d and (a, d) not in rel:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            yield frozenset(rel)


def relation_product(left, right):
    return frozenset((a, d) for a, b in left for c, d in right if b == c)


def pse_step(rel):
    return relation_product(rel, rel)


def relation_power(rel, exponent: int):
    if exponent == 1:
        return rel
    answer = frozenset((a, a) for a in set(sum(([x, y] for x, y in rel), [])))
    # The verifier only calls powers 2^t, so repeated squaring avoids relying
    # on the diagonal identity when the relation has isolated vertices.
    answer = rel
    for _ in range(exponent.bit_length() - 1):
        answer = relation_product(answer, answer)
    return answer


def poset_height(n: int, rel) -> int:
    if n == 0:
        return 0
    dp = [1] * n
    # A topological order is recovered without using the enumeration labels.
    remaining = set(range(n))
    order = []
    while remaining:
        mins = sorted(x for x in remaining if not any((y, x) in rel for y in remaining))
        claim(bool(mins), "strict poset must have a minimum")
        order.extend(mins)
        remaining.difference_update(mins)
    for x in order:
        for y in range(n):
            if (x, y) in rel:
                dp[y] = max(dp[y], dp[x] + 1)
    return max(dp)


def verify_pse():
    summary = []
    transition_rows = []
    expected_counts = [1, 1, 3, 19, 219, 4231]
    for n in range(6):
        states = list(posets(n))
        claim(len(states) == expected_counts[n], "labelled-poset census")
        fibres = Counter()
        depths = Counter()
        for rel in states:
            image = pse_step(rel)
            fibres[image] += 1
            claim(all(a != b and (b, a) not in image for a, b in image))
            claim(all((a, d) in image for a, b in image for c, d in image if b == c))
            h = poset_height(n, rel)
            wanted = ceil_log2(h)
            cur = rel
            for t in range(wanted + 1):
                if t:
                    cur = pse_step(cur)
                claim(cur == (rel if t == 0 else relation_power(rel, 1 << t)))
            claim((not cur) == (t == wanted))
            probe = rel
            depth = 0
            while probe:
                probe = pse_step(probe)
                depth += 1
                claim(depth <= ceil_log2(max(1, n)) + 1)
            claim(depth == wanted)
            depths[depth] += 1
            transition_rows.append((n, tuple(sorted(rel)), tuple(sorted(image)), depth))
        max_depth = max(depths, default=0)
        claim(max_depth == ceil_log2(max(1, n)))
        claim(sum(fibres.values()) == len(states))
        summary.append((n, len(states), len(fibres), max(fibres.values()), tuple(sorted(depths.items()))))
    return summary, digest(transition_rows)


# ---------------------------------------------------------------------------
# PFR: reverse, in parallel, every arc incident with a current source of an
# acyclic orientation.  The underlying simple graph is allowed to vary, but
# is invariant along each orbit.


def source_layers(n: int, arcs):
    remaining = set(range(n))
    layers = []
    while remaining:
        layer = {x for x in remaining if not any((y, x) in arcs for y in remaining)}
        if not layer:
            return None
        layers.append(frozenset(layer))
        remaining.difference_update(layer)
    return tuple(layers)


def acyclic_orientations(n: int):
    pairs = list(combinations(range(n), 2))
    for choices in product((-1, 0, 1), repeat=len(pairs)):
        arcs = set()
        for (a, b), choice in zip(pairs, choices):
            if choice == 1:
                arcs.add((a, b))
            elif choice == -1:
                arcs.add((b, a))
        arcs = frozenset(arcs)
        if source_layers(n, arcs) is not None:
            yield arcs


def pfr_step(n: int, arcs):
    sources = {x for x in range(n) if not any(b == x for a, b in arcs)}
    return frozenset((b, a) if a in sources else (a, b) for a, b in arcs)


def pfr_fibre_formula(n: int, target) -> int:
    indeg = [0] * n
    outdeg = [0] * n
    undirected = [set() for _ in range(n)]
    for a, b in target:
        outdeg[a] += 1
        indeg[b] += 1
        undirected[a].add(b)
        undirected[b].add(a)
    active_sources = [x for x in range(n) if indeg[x] == 0 and outdeg[x] > 0]
    active_sinks = [x for x in range(n) if outdeg[x] == 0 and indeg[x] > 0]
    answer = 0
    for chosen_mask in range(1 << len(active_sinks)):
        chosen = {active_sinks[i] for i in range(len(active_sinks)) if chosen_mask >> i & 1}
        if all(undirected[x] & chosen for x in active_sources):
            answer += 1
    # Same number via inclusion--exclusion over uncovered active sources.
    ie = 0
    for bad_mask in range(1 << len(active_sources)):
        forbidden = set()
        sign = 1
        for i, x in enumerate(active_sources):
            if bad_mask >> i & 1:
                sign *= -1
                forbidden.update(undirected[x] & set(active_sinks))
        ie += sign * (1 << (len(active_sinks) - len(forbidden)))
    claim(answer == ie)
    return answer


def functional_shape(n: int, state):
    seen = {}
    probe = state
    while probe not in seen:
        seen[probe] = len(seen)
        probe = pfr_step(n, probe)
    return seen[probe], len(seen) - seen[probe]


def verify_pfr():
    summary = []
    transition_rows = []
    expected_counts = [1, 1, 3, 25, 543, 29281]
    for n in range(6):
        states = list(acyclic_orientations(n))
        claim(len(states) == expected_counts[n], "acyclic partial-orientation census")
        state_set = set(states)
        fibres = Counter()
        shapes = Counter()
        for state in states:
            target = pfr_step(n, state)
            claim(target in state_set)
            claim(frozenset(frozenset(e) for e in target) == frozenset(frozenset(e) for e in state))
            fibres[target] += 1
            shape = functional_shape(n, state)
            claim(shape[0] <= max(0, n - 2))
            shapes[shape] += 1
            transition_rows.append((n, tuple(sorted(state)), tuple(sorted(target)), shape))
        for target in states:
            claim(fibres[target] == pfr_fibre_formula(n, target))
        claim(sum(fibres.values()) == len(states))
        summary.append(
            (n, len(states), len(fibres), max(fibres.values()), max(t for t, p in shapes),
             max(p for t, p in shapes), tuple(sorted(shapes.items())))
        )
    return summary, digest(transition_rows)


# ---------------------------------------------------------------------------
# USC: the complex whose faces are unions of two old faces.


@lru_cache(None)
def complexes(n: int):
    if n == 0:
        return (frozenset(), frozenset({0}))  # void and {empty face}
    old = complexes(n - 1)
    bit = 1 << (n - 1)
    values = set()
    for lower in old:
        for link in old:
            if link.issubset(lower):
                values.add(frozenset(set(lower) | {f | bit for f in link}))
    return tuple(sorted(values, key=lambda K: (len(K), tuple(sorted(K)))))


def union_square(K):
    return frozenset(a | b for a in K for b in K)


def support(K) -> int:
    ans = 0
    for f in K:
        ans |= f
    return ans


def simplex(S: int):
    return frozenset(x for x in range(S + 1) if x & ~S == 0)


def cover_number(K) -> int:
    S = support(K)
    if S == 0:
        return 0
    reachable = {0}
    for k in range(1, S.bit_count() + 1):
        reachable = {a | b for a in reachable for b in K}
        if S in reachable:
            return k
    raise AssertionError("singletons must cover the support")


def union_k(K, k: int):
    answer = frozenset({0}) if K else frozenset()
    for _ in range(k):
        answer = frozenset(a | b for a in answer for b in K)
    return answer


def is_complex(n: int, K) -> bool:
    return all(all((f ^ (1 << e)) in K for e in range(n) if f >> e & 1) for f in K)


def verify_usc():
    summary = []
    transition_rows = []
    expected_counts = [2, 3, 6, 20, 168, 7581]
    full_support = []
    for n in range(6):
        states = complexes(n)
        claim(len(states) == expected_counts[n], "Dedekind/complex census")
        depths = Counter()
        fibres = Counter()
        stable_dest = Counter()
        full = 0
        for K in states:
            claim(is_complex(n, K))
            image = union_square(K)
            claim(is_complex(n, image))
            fibres[image] += 1
            c = cover_number(K)
            wanted = 0 if support(K) == 0 else ceil_log2(c)
            probe = K
            for t in range(wanted + 1):
                claim(probe == union_k(K, 1 << t))
                if t < wanted:
                    probe = union_square(probe)
            terminal = K if support(K) == 0 else simplex(support(K))
            claim(probe == terminal)
            claim(union_square(terminal) == terminal)
            depths[wanted] += 1
            stable_dest[terminal] += 1
            if support(K) == (1 << n) - 1:
                full += 1
            transition_rows.append((n, tuple(sorted(K)), tuple(sorted(image)), c, wanted))
        claim(max(depths, default=0) == ceil_log2(max(1, n)))
        claim(sum(fibres.values()) == len(states))
        if n == 0:
            expected_full = 2
        else:
            expected_full = sum((-1) ** j * comb(n, j) * expected_counts[n - j] for j in range(n + 1))
        claim(full == expected_full)
        full_support.append(full)
        # At stable time, every nonempty-support simplex has the corresponding
        # full-support count; void and {empty face} each have one source.
        claim(stable_dest[frozenset()] == 1)
        claim(stable_dest[frozenset({0})] == 1)
        for S in range(1, 1 << n):
            claim(stable_dest[simplex(S)] == full_support[S.bit_count()])
        claim(sum(stable_dest.values()) == len(states))
        summary.append((n, len(states), len(fibres), max(fibres.values()), tuple(sorted(depths.items())), full))
    return summary, full_support, digest(transition_rows)


# ---------------------------------------------------------------------------
# ASD: simplify (least-label representatives), then dualize.


def valid_bases(ground: int, bases) -> bool:
    if not bases:
        return False
    sizes = {b.bit_count() for b in bases}
    if len(sizes) != 1 or any(b & ~ground for b in bases):
        return False
    els = [e for e in range(ground.bit_length()) if ground >> e & 1]
    B = set(bases)
    for p in B:
        for q in B:
            left = [e for e in els if p >> e & 1 and not q >> e & 1]
            right = [e for e in els if q >> e & 1 and not p >> e & 1]
            for e in left:
                if not any(((p ^ (1 << e)) | (1 << f)) in B for f in right):
                    return False
    return True


@lru_cache(None)
def matroids_on_ground(ground: int):
    els = [e for e in range(ground.bit_length()) if ground >> e & 1]
    answer = []
    for rank in range(len(els) + 1):
        candidates = [sum(1 << e for e in C) for C in combinations(els, rank)]
        for chosen in range(1, 1 << len(candidates)):
            bases = frozenset(candidates[i] for i in range(len(candidates)) if chosen >> i & 1)
            if valid_bases(ground, bases):
                answer.append((ground, bases))
    return tuple(answer)


def dual(M):
    ground, bases = M
    return ground, frozenset(ground ^ b for b in bases)


def simplify(M):
    ground, bases = M
    els = [e for e in range(ground.bit_length()) if ground >> e & 1]
    nonloops = [e for e in els if any(b >> e & 1 for b in bases)]
    classes = []
    for e in nonloops:
        for C in classes:
            f = C[0]
            if not any((b >> e & 1) and (b >> f & 1) for b in bases):
                C.append(e)
                break
        else:
            classes.append([e])
    representative = {e: min(C) for C in classes for e in C}
    new_ground = sum(1 << min(C) for C in classes)
    new_bases = frozenset(
        sum(1 << representative[e] for e in els if b >> e & 1 and e in representative)
        for b in bases
    )
    return new_ground, new_bases


def asd_step(M):
    return dual(simplify(M))


def is_simple(M):
    return simplify(M) == M


def is_core(M):
    return is_simple(M) and is_simple(dual(M))


def matroid_code(M):
    return M[0], tuple(sorted(M[1]))


def asd_fibre_formula(n: int, target) -> int:
    ground, _ = target
    if not is_simple(dual(target)):
        return 0
    answer = 1
    S = [s for s in range(n) if ground >> s & 1]
    for e in range(n):
        if not (ground >> e & 1):
            answer *= 2 + sum(s < e for s in S)
    return answer


def verify_asd():
    summary = []
    transition_rows = []
    expected_counts = [1, 3, 10, 38, 171, 967]
    for n in range(6):
        states = []
        for ground in range(1 << n):
            states.extend(matroids_on_ground(ground))
        claim(len(states) == expected_counts[n], "small labelled-matroid census over all subgrounds")
        state_set = set(states)
        fibres = Counter()
        depths = Counter()
        images = set()
        for M in states:
            target = asd_step(M)
            claim(target in state_set)
            claim(is_simple(dual(target)), "every image is cosimple")
            fibres[target] += 1
            images.add(target)
            probe = M
            depth = 0
            while not is_core(probe):
                old_size = probe[0].bit_count()
                probe = asd_step(probe)
                depth += 1
                claim(depth <= n + 1)
                if depth >= 2:
                    claim(probe[0].bit_count() < old_size)
            claim(asd_step(asd_step(probe)) == probe)
            depths[depth] += 1
            transition_rows.append((n, matroid_code(M), matroid_code(target), depth))
        expected_image = {M for M in states if is_simple(dual(M))}
        claim(images == expected_image)
        for M in states:
            claim(fibres[M] == asd_fibre_formula(n, M))
        claim(sum(fibres.values()) == len(states))
        summary.append((n, len(states), len(images), max(fibres.values()), max(depths), tuple(sorted(depths.items()))))
    return summary, digest(transition_rows)


# ---------------------------------------------------------------------------
# CGP: remove all extreme points from a closed set in a convex geometry.


def closure_of(family, A: int, full: int) -> int:
    containing = [C for C in family if A & ~C == 0]
    answer = full
    for C in containing:
        answer &= C
    return answer


def convex_geometries(n: int):
    full = (1 << n) - 1
    middle = [A for A in range(1 << n) if A not in (0, full)]
    for choice in range(1 << len(middle)):
        family = {0, full}
        family.update(middle[i] for i in range(len(middle)) if choice >> i & 1)
        if any((A & B) not in family for A in family for B in family):
            continue
        ok = True
        for A in family:
            outside = [x for x in range(n) if not (A >> x & 1)]
            for x, y in combinations(outside, 2):
                cy = closure_of(family, A | (1 << y), full)
                cx = closure_of(family, A | (1 << x), full)
                if (cy >> x & 1) and (cx >> y & 1):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            yield frozenset(family)


def extremes(family, C: int):
    return frozenset(x for x in range(C.bit_length()) if C >> x & 1 and (C ^ (1 << x)) in family)


def cgp_step(family, C: int) -> int:
    answer = C
    for x in extremes(family, C):
        answer ^= 1 << x
    return answer


def verify_cgp():
    summary = []
    transition_rows = []
    expected_geometries = [1, 1, 3, 22, 485]
    for n in range(5):
        geometries = list(convex_geometries(n))
        claim(len(geometries) == expected_geometries[n], "labelled convex-geometry census")
        total_states = 0
        global_max = 0
        fibre_shapes = Counter()
        for family in geometries:
            fibres = Counter()
            for C in family:
                total_states += 1
                image = cgp_step(family, C)
                claim(image in family, "simultaneous extreme deletion stays closed")
                claim(C == 0 or image != C, "nonempty closed sets lose an extreme")
                fibres[image] += 1
                probe = C
                depth = 0
                while probe:
                    probe = cgp_step(family, probe)
                    depth += 1
                    claim(depth <= n)
                global_max = max(global_max, depth)
                transition_rows.append((n, tuple(sorted(family)), C, image, depth))
            claim(sum(fibres.values()) == len(family))
            fibre_shapes[tuple(sorted(fibres.values()))] += 1
        claim(global_max == n)
        summary.append((n, len(geometries), total_states, global_max, len(fibre_shapes)))
    return summary, digest(transition_rows)


def main():
    pse, pse_hash = verify_pse()
    pfr, pfr_hash = verify_pfr()
    usc, full_support, usc_hash = verify_usc()
    asd, asd_hash = verify_asd()
    cgp, cgp_hash = verify_cgp()
    print("P166 REPLACEMENT DISCOVERY ROUND 2 — INDEPENDENT EXACT VERIFIER")
    print("status=KILL_ALL; lifecycle=HOLD_EXTERNAL")
    print("PSE rows: n,states,image,max_fibre,depth_hist")
    for row in pse:
        print("PSE", row)
    print("PSE transition_sha256=" + pse_hash)
    print("PFR rows: n,states,image,max_fibre,max_tail,max_period,(tail,period)_hist")
    for row in pfr:
        print("PFR", row)
    print("PFR transition_sha256=" + pfr_hash)
    print("USC rows: n,states,image,max_fibre,depth_hist,full_support_sources")
    for row in usc:
        print("USC", row)
    print("USC full_support=" + repr(tuple(full_support)))
    print("USC transition_sha256=" + usc_hash)
    print("ASD rows: n,states,image,max_fibre,max_depth,depth_hist")
    for row in asd:
        print("ASD", row)
    print("ASD transition_sha256=" + asd_hash)
    print("CGP rows: n,geometries,total_closed_states,max_depth,fibre_spectra")
    for row in cgp:
        print("CGP", row)
    print("CGP transition_sha256=" + cgp_hash)
    print("assertions=" + str(ASSERTIONS))


if __name__ == "__main__":
    main()
