#!/usr/bin/env python3
"""Self-contained CRC3 author checks, no pilot/old/reviewer imports."""
from collections import Counter, deque
from itertools import product
import json


checks = Counter()


def require(tag, condition):
    checks[tag] += 1
    if not condition:
        raise AssertionError(tag)


def step(w):
    n = len(w)
    ans = []
    for start in range(n):
        high = 0
        count = 0
        for shift in range(n):
            value = w[(start + shift) % n]
            if value > high:
                high = value
                count += 1
        ans.append(count)
    return tuple(ans)


def first_image(w):
    return min(w) == 1 and all(w[i] - w[(i + 1) % len(w)] <= 1
                               for i in range(len(w)))


def core(w):
    return min(w) == 1 and all(abs(w[i] - w[(i + 1) % len(w)]) <= 1
                               for i in range(len(w)))


def blocks(w):
    roots = [i for i, value in enumerate(w) if value == 1]
    ans = []
    for start, end in zip(roots, roots[1:] + [roots[0] + len(w)]):
        ans.append(tuple(w[i % len(w)] for i in range(start + 1, end)))
    return ans


def fibre(w):
    if not first_image(w):
        return 0
    count = 1
    for u in blocks(w):
        if 3 not in u:
            count *= len(u) + 1
        else:
            last_three = max(i for i, value in enumerate(u) if value == 3)
            count *= len(u) - last_three - 1
    return count + int(3 not in w) + int(all(v == 1 for v in w))


def decode(w):
    """Materialize inverse from the proof's maximum/run choices (small n only)."""
    if not first_image(w):
        return set()
    n = len(w)
    roots = [i for i, value in enumerate(w) if value == 1]
    intervals = [[i % n for i in range(start + 1, end)]
                 for start, end in zip(roots, roots[1:] + [roots[0] + n])]
    choices = []
    for positions in intervals:
        u = tuple(w[i] for i in positions)
        if 3 not in u:
            choices.append([tuple([2] * a + [1] * (len(u) - a))
                            for a in range(len(u) + 1)])
        else:
            cut = max(i for i, value in enumerate(u) if value == 3) + 1
            prefix = tuple(1 if value == 3 else 2 for value in u[:cut])
            t = len(u) - cut
            choices.append([prefix + tuple([2] * a + [1] * (t - a))
                            for a in range(1, t + 1)])
    answer = set()
    for parts in product(*choices):
        source = [3] * n
        for positions, part in zip(intervals, parts):
            for i, v in zip(positions, part):
                source[i] = v
        answer.add(tuple(source))
    if 3 not in w:
        answer.add(tuple(3 - v for v in w))
    if all(v == 1 for v in w):
        answer.add((1,) * n)
    return answer


def product_optimum(n):
    if n == 1:
        return 1
    a, r = divmod(n, 3)
    return 3 ** a if r == 0 else (4 * 3 ** (a - 1) if r == 1 else 2 * 3 ** a)


def equality_target(w):
    n = len(w)
    if n == 1:
        return w == (1,)
    if n == 2:
        return w in ((1, 1), (1, 2), (2, 1))
    if min(w) != 1 or 3 in w:
        return False
    sizes = Counter(len(u) + 1 for u in blocks(w))
    if any(s not in (2, 3, 4) for s in sizes):
        return False
    twos, fours = sizes[2], sizes[4]
    if n % 3 == 0:
        return twos == fours == 0
    if n % 3 == 1:
        return (twos, fours) in ((2, 0), (0, 1))
    return (twos, fours) == (1, 0)


def graph_data(arrows):
    n = len(arrows)
    indegrees = [0] * n
    for j in arrows:
        indegrees[j] += 1
    queue = deque(i for i, degree in enumerate(indegrees) if not degree)
    removed = []
    while queue:
        i = queue.popleft()
        removed.append(i)
        j = arrows[i]
        indegrees[j] -= 1
        if not indegrees[j]:
            queue.append(j)
    depth = [0] * n
    for i in reversed(removed):
        depth[i] = depth[arrows[i]] + 1
    cycles = Counter()
    seen = set()
    for i, degree in enumerate(indegrees):
        if degree and i not in seen:
            j, length = i, 0
            while j not in seen:
                seen.add(j)
                length += 1
                j = arrows[j]
            cycles[length] += 1
    return depth, cycles


def main():
    rows = []
    lucas = [2, 3]
    pell = [2, 2]
    for n in range(2, 11):
        lucas.append(3 * lucas[-1] - lucas[-2])
        pell.append(2 * pell[-1] + pell[-2])
    for n in range(1, 11):
        words = list(product((1, 2, 3), repeat=n))
        indexes = {w: i for i, w in enumerate(words)}
        images = [step(w) for w in words]
        arrows = [indexes[w] for w in images]
        counts = Counter(images)
        depth, cycles = graph_data(arrows)
        actual_sources = {}
        if n <= 7:
            for w, image in zip(words, images):
                actual_sources.setdefault(image, set()).add(w)
        expected_max = 3 if n <= 2 else 1 + product_optimum(n)
        for i, w in enumerate(words):
            r1 = images[i]
            r2 = images[arrows[i]]
            r4 = images[arrows[arrows[arrows[i]]]]
            require("first_image_forward", first_image(r1))
            require("first_image_iff", (w in counts) == first_image(w))
            if first_image(w):
                require("first_image_constructed_source", step(tuple(4-v for v in w)) == w)
            require("second_image", core(r2))
            require("power_identity", r4 == r2)
            require("graph_core_iff", (depth[i] == 0) == core(w))
            if core(w):
                require("core_reflection", r1 == tuple(max(w)+1-v for v in w))
            require("target_fibre", counts[w] == fibre(w))
            require("maximum_equality_iff", (counts[w] == expected_max) == equality_target(w))
            if n <= 7:
                require("complete_inverse_source_sets", decode(w) == actual_sources.get(w, set()))
        require("first_image_population", len([k for k,v in counts.items() if v]) == lucas[n] - 2**n)
        recurrent = sum(d == 0 for d in depth)
        require("core_population", recurrent == pell[n] + 1 - 2**n)
        require("period_census", cycles[1] == 1 and set(cycles) <= {1, 2}
                and cycles[2] == (recurrent - 1)//2)
        require("sharp_height", max(depth) == (1 if n <= 2 else 2))
        require("sharp_fibre", max(counts.values()) == expected_max)
        require("fibre_mass", sum(fibre(w) for w in words) == 3**n)
        rows.append(dict(n=n, states=len(words), image=lucas[n]-2**n,
                         recurrent=recurrent, cycles=dict(sorted(cycles.items())),
                         depths=dict(sorted(Counter(depth).items())),
                         max_fibre=max(counts.values()),
                         maximizing_targets=sum(v==expected_max for v in counts.values())))
    # Independently optimize over all ordered compositions; this is finite
    # pressure on the exchange proof, not its justification for arbitrary n.
    opt = [1]
    for n in range(1, 41):
        opt.append(max(s * opt[n-s] for s in range(1, n+1)))
        require("integer_product_formula", opt[n] == product_optimum(n))
    print(json.dumps(dict(audit="CRC3_author_v1", reports=rows,
                          checks=dict(sorted(checks.items())),
                          total_checks=sum(checks.values())), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
