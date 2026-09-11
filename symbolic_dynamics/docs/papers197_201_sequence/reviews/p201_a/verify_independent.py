#!/usr/bin/env python3
"""P201 Review A: Floyd literal, reverse-distance graph, pointed-component DP.

Written for this review without reading/copying/importing author or Stage-1
verifier code. Exact incoming sets use labelled block reconstruction at
n<=5; every labelled target count, including zero, is checked through n=7.
"""
from array import array
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial, prod

CHECKS = 0


def check(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(label)


def feedback(f):
    """Floyd's two-speed chase, independently at each labelled start."""
    out = []
    for start in range(len(f)):
        slow, fast = f[start], f[f[start]]
        while slow != fast:
            slow, fast = f[slow], f[f[fast]]
        length, at = 1, f[slow]
        while at != slow:
            length, at = length + 1, f[at]
        out.append(length - 1)
    return tuple(out)


def reachability_feedback(f):
    """Independent small-box Boolean transitive-closure dictionary."""
    n = len(f)
    reach = [(1 << i) | (1 << f[i]) for i in range(n)]
    for k in range(n):
        for i in range(n):
            if reach[i] & (1 << k):
                reach[i] |= reach[k]
    cyclic = [j for j in range(n) if reach[f[j]] & (1 << j)]
    lengths = {}
    for j in cyclic:
        lengths[j] = sum(bool(reach[j] & (1 << k)) and
                         bool(reach[k] & (1 << j)) for k in cyclic)
    return tuple(max(lengths[j] for j in cyclic if reach[i] & (1 << j)) - 1
                 for i in range(n))


def old_cycle_length_modulo(f):
    """Reimplement historical OCL using n-step landing, not its old code."""
    n, out = len(f), []
    for start in range(n):
        oncycle = start
        for _ in range(n):
            oncycle = f[oncycle]
        length, at = 1, f[oncycle]
        while at != oncycle:
            at, length = f[at], length + 1
        out.append(length % n)
    return tuple(out)


def conjugate_labels(f):
    n = len(f)
    return tuple((f[(i - 1) % n] + 1) % n for i in range(n))


def number(f, n):
    out = 0
    for x in f:
        out = out * n + x
    return out


def digits(index, n):
    out = [0] * n
    for j in range(n - 1, -1, -1):
        index, out[j] = divmod(index, n)
    return tuple(out)


def height(f):
    seen, t = set(), 0
    while any(f):
        check(f not in seen, "no nonzero operator cycle")
        seen.add(f)
        f, t = feedback(f), t + 1
    return t


def threshold_height(n):
    if n == 1:
        return 0
    size, h = 2, 2
    while size * (size + 1) // 2 <= n:
        size, h = size * (size + 1) // 2, h + 1
    return h


def connected(m, d):
    if m < d:
        return 0
    # Choose cyclic labels, cyclic order, then a prescribed-root forest.
    rooted = 1 if m == d else d * m ** (m - d - 1)
    return comb(m, d) * factorial(d - 1) * rooted


@lru_cache(None)
def block_count(m, d):
    """Decompose at the component containing the smallest block label."""
    if m == 0:
        return 1
    return sum(comb(m - 1, k - 1) * connected(k, d) * block_count(m - k, d)
               for k in range(1, m + 1))


def image_count(n):
    def rec(j, remaining, denominators):
        if j == n:
            return factorial(n) // denominators if remaining == 0 else 0
        return sum(rec(j + 1, remaining - k, denominators * factorial(k))
                   for k in [0] + list(range(j + 1, remaining + 1)))
    return rec(0, n, 1)


def permutation_cycles(f):
    if len(set(f)) != len(f):
        return None
    left, sizes = set(range(len(f))), []
    while left:
        start = min(left)
        at, size = start, 0
        while at in left:
            left.remove(at)
            at, size = f[at], size + 1
        check(at == start, "permutation components close at start")
        sizes.append(size)
    return sorted(sizes)


def critical_test(f, n):
    if n == 2:
        return f == (1, 0)
    k = {3: 2, 6: 3}[n]
    sizes = permutation_cycles(f)
    if sizes != list(range(1, k + 1)):
        return False
    core = feedback(f)[:k]
    return len(set(core)) == k and height(core) == threshold_height(k)


@lru_cache(None)
def local_blocks(m, d):
    return tuple(f for f in product(range(m), repeat=m)
                 if reachability_feedback(f) == (d - 1,) * m)


def reconstructed_sources(g):
    n = len(g)
    blocks = [tuple(i for i, value in enumerate(g) if value == j) for j in range(n)]
    choices = []
    occupied = []
    for j, labels in enumerate(blocks):
        if not labels:
            continue
        if len(labels) < j + 1:
            return set()
        choices.append(local_blocks(len(labels), j + 1))
        occupied.append(labels)
    answer = set()
    for maps in product(*choices):
        f = [-1] * n
        for labels, small in zip(occupied, maps):
            for i, target in enumerate(small):
                f[labels[i]] = labels[target]
        answer.add(number(f, n))
    return answer


def audit_box(n):
    size = n ** n
    forward = array("i")
    head = array("i", [-1]) * size
    link = array("i")
    indegree = array("i", [0]) * size
    full_incoming = [set() for _ in range(size)] if n <= 5 else None
    for index, f in enumerate(product(range(n), repeat=n)):
        g = feedback(f)
        shifted = conjugate_labels(f)
        check(old_cycle_length_modulo(shifted) == conjugate_labels(g),
              "CRITICAL exact historical OCL conjugacy OCL H = H P")
        check(len(set(shifted)) == len(set(f)), "conjugacy preserves source rank")
        if n <= 5:
            check(g == reachability_feedback(f), "Floyd vs Boolean closure")
        target = number(g, n)
        forward.append(target)
        link.append(head[target])
        head[target] = index
        indegree[target] += 1
        if full_incoming is not None:
            full_incoming[target].add(index)
        lengths = {j + 1 for j in g}
        check(len(set(f)) >= sum(lengths), "distinct cycles fit in source rank")
        check(sum(lengths) >= len(lengths) * (len(lengths) + 1) // 2,
              "distinct-length triangular cost")
        check(all(g[i] == g[f[i]] for i in range(n)), "output levels invariant under source")

    # Reverse breadth-first distances to zero: no proposed clock is used.
    depth = array("i", [-1]) * size
    depth[0] = 0
    queue = deque([0])
    while queue:
        target = queue.popleft()
        source = head[target]
        while source != -1:
            if depth[source] == -1:
                depth[source] = depth[target] + 1
                queue.append(source)
            source = link[source]
    check(all(t >= 0 for t in depth), "zero reverse basin equals whole operator graph")
    check(forward[0] == 0, "zero is fixed")
    rank_max, depths = {}, Counter(depth)
    maximizers, deepest = [], 0
    maximum = (n + 1) ** (n - 1)
    for index, g in enumerate(product(range(n), repeat=n)):
        hist = Counter(g)
        predicted = prod(block_count(hist[j], j + 1) for j in range(n))
        check(indegree[index] == predicted, "every target pointed-component DP count")
        check(bool(indegree[index]) == all(k >= j + 1 for j, k in hist.items()),
              "every target image iff, including unsupported")
        check((forward[index] == index) == (index == 0), "unique fixed map")
        check(depth[index] == (0 if index == 0 else depth[forward[index]] + 1),
              "graph height recursion")
        rank = len(hist)
        rank_max[rank] = max(rank_max.get(rank, -1), depth[index])
        if rank >= 2:
            check(depth[index] <= threshold_height(rank), "pointwise all-rank ceiling")
        else:
            check(depth[index] <= 1, "constant rank-one boundary")
        check(indegree[index] <= maximum, "global fibre upper bound")
        if indegree[index] == maximum:
            maximizers.append(index)
        if full_incoming is not None:
            check(reconstructed_sources(g) == full_incoming[index], "complete reconstructed source SET")
        if n in (2, 3, 6):
            critical = critical_test(g, n)
            check(critical == (depth[index] == threshold_height(n)), "critical full iff")
            deepest += critical
    for rank in range(1, n + 1):
        expected = (0 if n == 1 else 1) if rank == 1 else threshold_height(rank)
        check(rank_max[rank] == expected, "every rank attains its ceiling")
    check(maximizers == [0], "unique maximum target")
    check(sum(indegree) == size, "fibre mass")
    check(sum(t > 0 for t in indegree) == image_count(n), "multinomial first-image census")
    if n in (2, 3, 6):
        check(deepest == {2: 1, 3: 1, 6: 6}[n], "complete critical factorial census")
    print(f"n={n} states={size} image={sum(t>0 for t in indegree)} "
          f"heights={sorted(depths.items())} rank_max={sorted(rank_max.items())} "
          f"max_fibre={maximum} max_targets={len(maximizers)} critical_deepest={deepest}")
    print(f"OCL_exact_conjugacy_n={n} all_states={size} sigma=i+1_mod_n PASS_COLLISION")


def decode_forest(m, roots, sequence):
    waiting = set(range(m))
    f = list(range(m))
    for at, parent in enumerate(sequence):
        leaf = min(waiting - set(roots) - set(sequence[at:]))
        check(parent in waiting and parent != leaf, "forest code points to remaining vertex")
        f[leaf] = parent
        waiting.remove(leaf)
    check(waiting == set(roots), "forest decoder ends exactly on prescribed roots")
    return tuple(f)


def encode_forest(f, roots):
    waiting, out = set(range(len(f))), []
    while waiting - set(roots):
        parents = {f[i] for i in waiting if i not in roots}
        leaf = min(waiting - set(roots) - parents)
        out.append(f[leaf])
        waiting.remove(leaf)
    return tuple(out)


def audit_forests():
    decoded = 0
    for m in range(1, 6):
        total = set()
        for s in range(1, m + 1):
            for roots in combinations(range(m), s):
                codes = [()] if s == m else (
                    prefix + (last,) for prefix in product(range(m), repeat=m-s-1)
                    for last in roots)
                seen = set()
                for seq in codes:
                    f = decode_forest(m, roots, seq)
                    check(encode_forest(f, roots) == seq, "prescribed-root code round trip")
                    check(reachability_feedback(f) == (0,) * m, "decoded forest has only loops")
                    check(tuple(i for i in range(m) if f[i] == i) == roots, "exact root set")
                    seen.add(f)
                    decoded += 1
                check(len(seen) == (1 if s == m else s * m ** (m-s-1)),
                      "all distinct prescribed-root codes")
                total.update(seen)
        check(len(total) == (m + 1) ** (m - 1), "all-root forest union Cayley count")
        check(total == set(local_blocks(m, 1)), "root-code bijection covers full zero fibre")
    print(f"prescribed_root_forest_codes={decoded} exhaustive_m=1..5 roundtrip_and_surjectivity=PASS")


def audit_extensions():
    tested = 0
    for n in range(1, 6):
        for k in range(1, n + 1):
            for g in product(range(k), repeat=n):
                core = g[:k]
                hg, hu = height(g), height(core)
                check(hg == hu if hu > 0 else hg == int(any(g)), "core height zero boundary")
                left, right = g, core
                for t in range(max(hg, hu) + 2):
                    check(left[:k] == right, "restriction commutes at every tested epoch")
                    if t:
                        check(any(left) == any(right), "zero equivalence at positive epoch")
                    left, right = feedback(left), feedback(right)
                tested += 1
    print(f"core_extensions={tested} exhaustive_n=1..5 all_k positive_epoch_and_zero_boundary=PASS")


def lift(permutation):
    k = len(permutation)
    n = k * (k + 1) // 2
    inverse = [permutation.index(j) for j in range(k)]
    out, fresh = [-1] * n, k
    for j in range(k):
        block = [inverse[j]] + list(range(fresh, fresh + j))
        fresh += j
        for a, b in zip(block, block[1:] + block[:1]):
            out[a] = b
    check(fresh == n and sorted(out) == list(range(n)), "lift is a full permutation")
    check(feedback(tuple(out))[:k] == permutation, "lift prescribes entire old core")
    return tuple(out)


def audit_witnesses():
    critical = [(1, 0)]
    for _ in range(5):
        critical.append(lift(critical[-1]))
    for h, f in enumerate(critical, 2):
        check(height(f) == h, "large critical witness exact height")
        check(height(f + (0,) * 3) == h, "large leaf extension")
        print(f"critical_witness_n={len(f)} height={h} rank={len(set(f))} leaf_extension=PASS")
    for rank in range(2, 33):
        h = threshold_height(rank)
        base = critical[h - 2]
        f = base + tuple(range(len(base), rank))
        for extra in (0, 4):
            g = f + (0,) * extra
            check(len(set(g)) == rank and height(g) == h, "all-rank padded witnesses")
    print("all_rank_witnesses=62 ranks=2..32 carrier_extra=0,4 PASS")


def main():
    print("P201_REVIEW_A_FLOYD_REVERSE_BFS_COMPONENT_DP")
    print("author_or_gate_code_read_or_imported=none; full_source_sets_n<=5; every_target_counts_n<=7")
    for n in range(1, 8):
        audit_box(n)
    audit_forests()
    audit_extensions()
    audit_witnesses()
    print(f"assertions={CHECKS}")
    print("PASS_MATHEMATICS_AND_EXACT_OCL_COLLISION; P201_ADMISSION_CRITICAL_NOT_REVIEW_PASS")


if __name__ == "__main__":
    main()
