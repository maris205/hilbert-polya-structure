#!/usr/bin/env python3
"""Deterministic exact breadth scout for poset/language replacement systems.

The 25 pilots deliberately use small complete carriers.  They are
counterexample pressure and signature collection, not proofs or ownership
certificates.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, permutations, product
from math import gcd


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def functional_signature(states, update):
    states = tuple(states)
    state_set = set(states)
    successor = {}
    for state in states:
        target = update(state)
        check(target in state_set, f"functional carrier not closed: {state}->{target}")
        successor[state] = target
    check(len(successor) == len(states), "duplicate state representation")

    depth = {}
    period = {}
    cycles = set()
    for start in states:
        if start in depth:
            continue
        path = []
        position = {}
        current = start
        while current not in position and current not in depth:
            position[current] = len(path)
            path.append(current)
            current = successor[current]
        if current in position:
            begin = position[current]
            cycle = path[begin:]
            labels = tuple(repr(x) for x in cycle)
            rotations = [labels[i:] + labels[:i] for i in range(len(labels))]
            cycles.add(min(rotations))
            for node in cycle:
                depth[node] = 0
                period[node] = len(cycle)
            for node in reversed(path[:begin]):
                depth[node] = depth[successor[node]] + 1
                period[node] = period[successor[node]]
        else:
            for node in reversed(path):
                depth[node] = depth[successor[node]] + 1
                period[node] = period[successor[node]]

    image = len(set(successor.values()))
    fixed = sum(successor[state] == state for state in states)
    max_tail = max(depth.values(), default=0)
    cycle_histogram = Counter(len(cycle) for cycle in cycles)
    check(sum(length * number for length, number in cycle_histogram.items()) ==
          sum(value == 0 for value in depth.values()), "cycle accounting")
    return (len(states), image, fixed, max_tail,
            tuple(sorted(cycle_histogram.items())))


def iterate(state, update, steps):
    for _ in range(steps):
        state = update(state)
    return state


def point_tail_period(state, update):
    path = []
    position = {}
    while state not in position:
        position[state] = len(path)
        path.append(state)
        state = update(state)
    return position[state], len(path) - position[state]


def support_signature(states, transition_support):
    states = tuple(states)
    state_set = set(states)
    arcs = 0
    absorbing = 0
    degrees = []
    for state in states:
        targets = tuple(transition_support(state))
        check(targets, f"empty Markov support at {state}")
        check(all(target in state_set for target in targets), "Markov carrier not closed")
        unique = set(targets)
        arcs += len(unique)
        degrees.append(len(unique))
        absorbing += unique == {state}
    return (len(states), arcs, absorbing, min(degrees), max(degrees))


def bit_count(mask):
    return mask.bit_count()


def ideals(predecessors):
    n = len(predecessors)
    return tuple(mask for mask in range(1 << n)
                 if all(not (mask & (1 << point)) or
                        predecessors[point] & ~mask == 0
                        for point in range(n)))


def transitive_predecessors(n, covers):
    pred = [0] * n
    for lower, upper in covers:
        pred[upper] |= 1 << lower
    changed = True
    while changed:
        changed = False
        for point in range(n):
            old = pred[point]
            for lower in range(n):
                if old & (1 << lower):
                    pred[point] |= pred[lower]
            changed |= pred[point] != old
    return tuple(pred)


def toggle_ideal(mask, point, predecessor, phase):
    candidate = mask ^ (1 << point)
    return candidate if candidate in phase else mask


def maximal_count(mask, phase, n):
    return sum((mask & (1 << point)) and
               (mask ^ (1 << point)) in phase for point in range(n))


def rowmotion(mask, predecessor, phase):
    n = len(predecessor)
    minimal_complement = [point for point in range(n)
                          if not mask & (1 << point) and
                          predecessor[point] & ~mask == 0]
    answer = 0
    for point in minimal_complement:
        answer |= predecessor[point] | (1 << point)
    check(answer in phase, "rowmotion output is not an ideal")
    return answer


def poset_rows(rows):
    # P01: random legal single toggle on a chain.
    height = 5
    chain_states = tuple(range(height + 1))

    def chain_toggle_support(k):
        targets = {k}
        if k:
            targets.add(k - 1)
        if k < height:
            targets.add(k + 1)
        return targets

    sig = support_signature(chain_states, chain_toggle_support)
    # The label-choice kernel is symmetric, hence its integer numerator has
    # every row and every column sum equal to height.
    numerator = {}
    for k in chain_states:
        counts = Counter()
        for label in range(height):
            if label == k and k < height:
                counts[k + 1] += 1
            elif label == k - 1 and k:
                counts[k - 1] += 1
            else:
                counts[k] += 1
        numerator[k] = counts
        check(sum(counts.values()) == height, "chain kernel row")
    for target in chain_states:
        check(sum(numerator[source][target] for source in chain_states) == height,
              "chain kernel column")
    rows.append(("P01/CHT", sig))

    # P02: random feasible growth in the six-element fence.
    fence_pred = transitive_predecessors(
        6, ((0, 1), (2, 1), (2, 3), (4, 3), (4, 5)))
    fence = ideals(fence_pred)

    def available(mask):
        return tuple(point for point in range(6)
                     if not mask & (1 << point) and
                     fence_pred[point] & ~mask == 0)

    def fence_growth(mask):
        choices = available(mask)
        return (mask,) if not choices else tuple(mask | (1 << p) for p in choices)

    sig = support_signature(fence, fence_growth)
    histories = {0: 1}
    for size in range(6):
        for mask in sorted((m for m in fence if bit_count(m) == size)):
            for point in available(mask):
                target = mask | (1 << point)
                histories[target] = histories.get(target, 0) + histories.get(mask, 0)
    full = (1 << 6) - 1
    check(all(bit_count(target) == bit_count(mask) + 1
              for mask in fence if mask != full for target in fence_growth(mask)),
          "fence growth clock")
    rows.append(("P02/RFG", sig, histories[full]))

    # P03: Panyushev/rowmotion complement on the same fence.
    rows.append(("P03/PNC", functional_signature(
        fence, lambda mask: rowmotion(mask, fence_pred, set(fence)))))

    # P04: a state-dependent single toggle on a 2x3 rectangle.
    grid_points = [(i, j) for i in range(2) for j in range(3)]
    grid_index = {point: index for index, point in enumerate(grid_points)}
    covers = []
    for i, j in grid_points:
        if i + 1 < 2:
            covers.append((grid_index[(i, j)], grid_index[(i + 1, j)]))
        if j + 1 < 3:
            covers.append((grid_index[(i, j)], grid_index[(i, j + 1)]))
    grid_pred = transitive_predecessors(6, tuple(covers))
    grid = ideals(grid_pred)
    grid_set = set(grid)

    def adaptive_toggle(mask):
        point = (bit_count(mask) + maximal_count(mask, grid_set, 6)) % 6
        return toggle_ideal(mask, point, grid_pred, grid_set)

    rows.append(("P04/ATG", functional_signature(grid, adaptive_toggle)))

    # P05: largest complete rank-prefix extractor on a 3x3 product poset.
    points = [(i, j) for i in range(3) for j in range(3)]
    index = {point: k for k, point in enumerate(points)}
    covers = []
    for i, j in points:
        if i + 1 < 3:
            covers.append((index[(i, j)], index[(i + 1, j)]))
        if j + 1 < 3:
            covers.append((index[(i, j)], index[(i, j + 1)]))
    pred = transitive_predecessors(9, tuple(covers))
    phase = ideals(pred)
    rank_masks = []
    for rank in range(5):
        rank_masks.append(sum(1 << index[point] for point in points
                              if sum(point) == rank))

    def rank_prefix(mask):
        answer = 0
        for rank_mask in rank_masks:
            if mask & rank_mask == rank_mask:
                answer |= rank_mask
            else:
                break
        return answer

    sig = functional_signature(phase, rank_prefix)
    check(sig[3] <= 1, "rank-prefix extractor should retract")
    rows.append(("P05/RPE", sig))


@lru_cache(None)
def prefix_antichains(prefix, remaining):
    if remaining == 0:
        return (frozenset(), frozenset((prefix,)))
    out = {frozenset((prefix,))}
    left = prefix_antichains(prefix + "0", remaining - 1)
    right = prefix_antichains(prefix + "1", remaining - 1)
    for a in left:
        for b in right:
            out.add(a | b)
    return tuple(sorted(out, key=lambda code: (len(code), tuple(sorted(code)))))


def powerset(items):
    items = tuple(items)
    return tuple(frozenset(items[index] for index in range(len(items))
                           if mask & (1 << index))
                 for mask in range(1 << len(items)))


def transition_parity_feedback(word):
    """Shift left and append the parity of the internal 01 factors."""
    parity = sum(word[index] == 0 and word[index + 1] == 1
                 for index in range(len(word) - 1)) % 2
    return word[1:] + (parity,)


def fibonacci(index):
    left, right = 0, 1
    for _ in range(index):
        left, right = right, left + right
    return left


def cyclic_independent(word):
    return all(not (word[index] and word[(index + 1) % len(word)])
               for index in range(len(word)))


def recurrent_nfs(word):
    return cyclic_independent(word) and sum(word) % 2 == 0


def all_cyclic_independent_count(length):
    if length == 1:
        return 1
    return fibonacci(length - 1) + fibonacci(length + 1)


def even_cyclic_independent_count(length):
    if length == 1:
        return 1
    signed = (2, 1, -1, -2, -1, 1)[length % 6]
    return (all_cyclic_independent_count(length) + signed) // 2


def divisors(number):
    return tuple(value for value in range(1, number + 1)
                 if number % value == 0)


def mobius(number):
    prime_count = 0
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            number //= divisor
            prime_count += 1
            if number % divisor == 0:
                return 0
            while number % divisor == 0:
                number //= divisor
        divisor += 1
    if number > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def nfs_focused_controls():
    """Pressure-test the strongest pilot without turning evidence into proof.

    The finite identities below motivated the hand derivation in SCOUT.md.
    The all-n 2n clock and Fibonacci image chain remain explicitly outside
    the proved scout contract.
    """
    digest = []
    for length in range(1, 15):
        states = tuple(product((0, 1), repeat=length))
        signature = functional_signature(states, transition_parity_feedback)
        recurrent = tuple(word for word in states if recurrent_nfs(word))
        recurrent_set = set(recurrent)

        expected_tail = 1 if length == 1 else 3 if length == 2 else 2 * length
        check(signature[3] == expected_tail, f"NFS tail n={length}")
        check(len(recurrent) == even_cyclic_independent_count(length),
              f"NFS recurrent count n={length}")

        for word in states:
            tail, _ = point_tail_period(word, transition_parity_feedback)
            check((tail == 0) == (word in recurrent_set),
                  f"NFS recurrent classification n={length}, word={word}")
        for word in recurrent:
            check(transition_parity_feedback(word) == word[1:] + word[:1],
                  f"NFS recurrent rotation n={length}, word={word}")

        # The complete rotation-period census follows from the recurrent
        # classification.  If a period-d block is repeated n/d times, its
        # total weight is automatically even exactly when n/d is even.
        predicted_cycles = {}
        for period in divisors(length):
            primitive = 0
            for subperiod in divisors(period):
                repeated = length // subperiod
                fixed = (all_cyclic_independent_count(subperiod)
                         if repeated % 2 == 0
                         else even_cyclic_independent_count(subperiod))
                primitive += mobius(period // subperiod) * fixed
            check(primitive >= 0 and primitive % period == 0,
                  f"NFS primitive orbit divisibility n={length}, d={period}")
            if primitive:
                predicted_cycles[period] = primitive // period
        check(tuple(sorted(predicted_cycles.items())) == signature[4],
              f"NFS cycle census n={length}")

        for power in range(1, 2 * length + 1):
            fixed_direct = sum(iterate(word, transition_parity_feedback, power) == word
                               for word in states)
            block = gcd(length, power)
            repeated = length // block
            fixed_formula = (all_cyclic_independent_count(block)
                             if repeated % 2 == 0
                             else even_cyclic_independent_count(block))
            check(fixed_direct == fixed_formula,
                  f"NFS fixed iterate n={length}, k={power}")

        # Exact every-target one-step fibres.  Only the first target bit can
        # make the forgotten source bit visible to the feedback function.
        fibres = Counter()
        incoming = Counter(transition_parity_feedback(word) for word in states)
        for target in states:
            if length == 1:
                expected = 2 if target == (0,) else 0
            else:
                inner = sum(target[index] == 0 and target[index + 1] == 1
                            for index in range(length - 2)) % 2
                if target[0] == 1:
                    expected = 1
                else:
                    expected = 2 if target[-1] == inner else 0
            check(incoming[target] == expected,
                  f"NFS every-target fibre n={length}, target={target}")
            fibres[incoming[target]] += 1
        if length >= 2:
            check(fibres == Counter({0: 1 << (length - 2),
                                     1: 1 << (length - 1),
                                     2: 1 << (length - 2)}),
                  f"NFS fibre histogram n={length}")

        # Two striking finite patterns are retained as conjectural pressure,
        # not as all-parameter assertions: a Fibonacci image chain up to
        # n-1 and stabilization exactly at 2n for n>=3.
        image = set(states)
        for time in range(2 * length + 1):
            if time <= length - 1:
                expected_image = fibonacci(time + 3) * (1 << (length - time - 1))
                check(len(image) == expected_image,
                      f"NFS Fibonacci image pilot n={length}, t={time}")
            if time == 2 * length:
                check(image == recurrent_set,
                      f"NFS terminal image pilot n={length}")
            if length >= 3 and time == 2 * length - 1:
                check(image != recurrent_set,
                      f"NFS sharp terminal time pilot n={length}")
            image = {transition_parity_feedback(word) for word in image}

        digest.append((length, signature[1], signature[3], len(recurrent),
                       signature[4]))
    return tuple(digest)


def language_rows(rows):
    # L01: simultaneous sibling contraction of a bounded binary prefix code.
    height = 3
    codes = prefix_antichains("", height)
    code_set = set(codes)

    def contract(code):
        parents = {word[:-1] for word in code if word and
                   word[:-1] + ("1" if word[-1] == "0" else "0") in code}
        removed = {parent + bit for parent in parents for bit in "01"}
        return frozenset((set(code) - removed) | parents)

    sig = functional_signature(codes, contract)
    check(len(codes) == 677, "prefix-code carrier recurrence")
    check(sig[3] == height, "prefix-code sharp depth")
    root_basin = sum(1 for code in codes
                     if next(iterate_until_fixed(code, contract)) == frozenset(("",)))
    # Direct recursion q_0=1, q_h=1+q_(h-1)^2 for root-producing codes.
    q = 1
    for _ in range(height):
        q = 1 + q * q
    check(root_basin == q, "prefix-code root basin")
    rows.append(("L01/PSC", sig, root_basin))

    # L02: fixed-length languages under tagged left-symbol deletion.
    layered = []
    for length in range(4):
        words = tuple(product((0, 1), repeat=length))
        layered.extend((length, language) for language in powerset(words))
    layered = tuple(layered)

    def suffix_quotient(state):
        length, language = state
        if length == 0:
            return state
        return (length - 1, frozenset(word[1:] for word in language))

    rows.append(("L02/LSQ", functional_signature(layered, suffix_quotient)))

    # L03: collapse every maximal equal-letter run of a finite word.
    words = tuple(word for length in range(6)
                  for word in product(range(3), repeat=length))

    def run_normalize(word):
        answer = []
        for letter in word:
            if not answer or answer[-1] != letter:
                answer.append(letter)
        return tuple(answer)

    rows.append(("L03/RNC", functional_signature(words, run_normalize)))

    # L04: shift and append the least absent alphabet letter (or zero).
    words3 = tuple(product(range(3), repeat=5))

    def mex_feedback(word):
        absent = [letter for letter in range(3) if letter not in word]
        new = absent[0] if absent else 0
        return word[1:] + (new,)

    rows.append(("L04/MFS", functional_signature(words3, mex_feedback)))

    # L05: a nonlinear binary feedback shift using 01-factor parity.
    words2 = tuple(product((0, 1), repeat=7))

    rows.append(("L05/NFS", functional_signature(
        words2, transition_parity_feedback)))

    # L06: mixed finite languages under existential left quotient, retaining
    # epsilon as an absorbing accepted word.
    universe = tuple(word for length in range(3)
                     for word in product((0, 1), repeat=length))
    languages = powerset(universe)

    def union_left_quotient(language):
        answer = {()} if () in language else set()
        for word in language:
            if word:
                answer.add(word[1:])
        return frozenset(answer)

    rows.append(("L06/ULQ", functional_signature(languages, union_left_quotient)))


def iterate_until_fixed(state, update):
    seen = set()
    while state not in seen:
        seen.add(state)
        target = update(state)
        if target == state:
            yield state
            return
        state = target
    raise AssertionError("expected an absorbing functional graph")


def graph_components(mask, edges, n):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            parent[y] = x

    for index, (left, right) in enumerate(edges):
        if mask & (1 << index):
            union(left, right)
    return tuple(find(i) for i in range(n))


def is_tree(mask, edges, n):
    return bit_count(mask) == n - 1 and len(set(graph_components(mask, edges, n))) == 1


def matroid_rows(rows):
    # M01: Bernoulli--Laplace exchange on bases of U(6,3).
    bases = tuple(sum(1 << point for point in subset)
                  for subset in combinations(range(6), 3))

    def basis_exchange(mask):
        inside = [i for i in range(6) if mask & (1 << i)]
        outside = [i for i in range(6) if not mask & (1 << i)]
        return tuple(mask ^ (1 << i) ^ (1 << j) for i in inside for j in outside)

    sig = support_signature(bases, basis_exchange)
    check(sig[-2:] == (9, 9), "uniform basis exchange degree")
    rows.append(("M01/BLX", sig))

    # M02: replace a graph by the lexicographic Kruskal forest of its own
    # connected-component closure.
    edges = tuple(combinations(range(4), 2))
    graphs = tuple(range(1 << len(edges)))

    def kruskal_forest(mask):
        parent = list(range(4))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        answer = 0
        for index, (left, right) in enumerate(edges):
            if mask & (1 << index) and find(left) != find(right):
                parent[find(right)] = find(left)
                answer |= 1 << index
        return answer

    rows.append(("M02/KFN", functional_signature(graphs, kruskal_forest)))

    # M03: zero propagation in covectors of the Boolean oriented matroid.
    covectors = tuple(product((-1, 0, 1), repeat=6))

    def zero_propagate(vector):
        return tuple(value if value else vector[(i + 1) % len(vector)]
                     for i, value in enumerate(vector))

    sig = functional_signature(covectors, zero_propagate)
    check(sig[3] == 5, "zero-run sharp clock")
    rows.append(("M03/OZP", sig))

    # M04: random rooted-connected-set growth on a six-cycle antimatroid.
    n = 6
    feasible = []
    for mask in range(1 << n):
        if mask == 0:
            feasible.append(mask)
            continue
        if not mask & 1:
            continue
        vertices = [i for i in range(n) if mask & (1 << i)]
        reached = {0}
        changed = True
        while changed:
            changed = False
            for vertex in vertices:
                if vertex not in reached and any(
                    ((vertex - other) % n in (1, n - 1)) for other in reached
                ):
                    reached.add(vertex)
                    changed = True
        if len(reached) == len(vertices):
            feasible.append(mask)
    feasible = tuple(feasible)
    feasible_set = set(feasible)

    def connected_growth(mask):
        choices = tuple(mask | (1 << point) for point in range(n)
                        if not mask & (1 << point) and
                        mask | (1 << point) in feasible_set)
        if mask == 0:
            choices = (1,)
        return choices or (mask,)

    rows.append(("M04/RCG", support_signature(feasible, connected_growth)))

    # M05: lex-improving fundamental-cycle exchange on spanning trees of K4.
    trees = tuple(mask for mask in graphs if is_tree(mask, edges, 4))
    tree_set = set(trees)

    def greedy_exchange(mask):
        for incoming in range(len(edges)):
            if mask & (1 << incoming):
                continue
            candidates = []
            for outgoing in range(len(edges)):
                if mask & (1 << outgoing) and outgoing > incoming:
                    target = mask ^ (1 << outgoing) ^ (1 << incoming)
                    if target in tree_set:
                        candidates.append(outgoing)
            if candidates:
                return mask ^ (1 << max(candidates)) ^ (1 << incoming)
        return mask

    rows.append(("M05/GBD", functional_signature(trees, greedy_exchange)))


def compositions(total, parts):
    if parts == 1:
        return ((total,),)
    answer = []
    for first in range(total + 1):
        for suffix in compositions(total - first, parts - 1):
            answer.append((first,) + suffix)
    return tuple(answer)


def bounded_compositions(maximum, parts):
    return tuple(comp for total in range(maximum + 1)
                 for comp in compositions(total, parts))


def chip_rows(rows):
    # C01: deterministic parallel unit zero-range transport on a cycle.
    phase = compositions(5, 4)

    def zero_range(config):
        active = tuple(value > 0 for value in config)
        return tuple(config[i] - active[i] + active[(i - 1) % 4]
                     for i in range(4))

    rows.append(("C01/ZRC", functional_signature(phase, zero_range)))

    # C02: deterministic leftmost max-to-min balancing.
    phase = compositions(6, 4)

    def balance(config):
        high, low = max(config), min(config)
        if high - low <= 1:
            return config
        source = config.index(high)
        target = config.index(low)
        answer = list(config)
        answer[source] -= 1
        answer[target] += 1
        return tuple(answer)

    def potential(config):
        return sum(value * value for value in config)

    for config in phase:
        target = balance(config)
        check(target == config or potential(target) < potential(config),
              "balancing potential")
    rows.append(("C02/LBB", functional_signature(phase, balance)))

    # C03: smallest-index legal toppling on a three-vertex path with sinks
    # just outside both endpoints.
    phase = bounded_compositions(6, 3)

    def sink_fire(config):
        unstable = [i for i, value in enumerate(config) if value >= 2]
        if not unstable:
            return config
        point = unstable[0]
        answer = list(config)
        answer[point] -= 2
        if point:
            answer[point - 1] += 1
        if point + 1 < 3:
            answer[point + 1] += 1
        return tuple(answer)

    rows.append(("C03/SFS", functional_signature(phase, sink_fire)))

    # C04: one-chip rotor router on a four-cycle with binary rotors.
    rotor_states = tuple((position, rotors) for position in range(4)
                         for rotors in product((0, 1), repeat=4))

    def rotor_step(state):
        position, rotors = state
        new_rotors = list(rotors)
        new_rotors[position] ^= 1
        direction = 1 if new_rotors[position] else -1
        return ((position + direction) % 4, tuple(new_rotors))

    rows.append(("C04/RTR", functional_signature(rotor_states, rotor_step)))

    # C05: random clockwise unit zero-range transfer.
    phase = compositions(4, 3)

    def random_transfer(config):
        targets = []
        for source in range(3):
            if config[source] == 0:
                targets.append(config)
            else:
                answer = list(config)
                answer[source] -= 1
                answer[(source + 1) % 3] += 1
                targets.append(tuple(answer))
        return targets

    rows.append(("C05/ZRW", support_signature(phase, random_transfer)))

    # C06: parallel candy-sharing, retain floor half and send ceil half right.
    phase = compositions(5, 4)

    def candy(config):
        return tuple(config[i] // 2 + (config[(i - 1) % 4] + 1) // 2
                     for i in range(4))

    rows.append(("C06/CSH", functional_signature(phase, candy)))


def integer_partitions(total, maximum=None):
    if total == 0:
        return ((),)
    if maximum is None or maximum > total:
        maximum = total
    answer = []
    for first in range(maximum, 0, -1):
        for suffix in integer_partitions(total - first, first):
            answer.append((first,) + suffix)
    return tuple(answer)


def tableau_rows(rows):
    # Y01: sort rows and then columns of a 2x3 distinct filling.
    fillings = tuple(permutations(range(1, 7)))

    def row_column_sort(filling):
        matrix = [sorted(filling[:3]), sorted(filling[3:])]
        for column in range(3):
            values = sorted((matrix[0][column], matrix[1][column]))
            matrix[0][column], matrix[1][column] = values
        answer = tuple(matrix[0] + matrix[1])
        check(answer[0] < answer[1] < answer[2] and
              answer[3] < answer[4] < answer[5], "row order lost")
        check(all(answer[j] < answer[3 + j] for j in range(3)), "column order lost")
        return answer

    rows.append(("Y01/RCS", functional_signature(fillings, row_column_sort)))

    # Y02: Bulgarian solitaire on integer partitions of eight.
    partitions8 = integer_partitions(8)

    def bulgarian(partition):
        next_parts = [len(partition)] + [part - 1 for part in partition if part > 1]
        return tuple(sorted(next_parts, reverse=True))

    rows.append(("Y02/BGS", functional_signature(partitions8, bulgarian)))

    # Y03: 180-degree rectangle complement on diagrams in a 3x4 box.
    diagrams = tuple((a, b, c) for a in range(5) for b in range(a + 1)
                     for c in range(b + 1))

    def rectangle_complement(diagram):
        return tuple(4 - diagram[2 - i] for i in range(3))

    sig = functional_signature(diagrams, rectangle_complement)
    check(all(rectangle_complement(rectangle_complement(d)) == d for d in diagrams),
          "rectangle complement not involutive")
    rows.append(("Y03/RCI", sig))


def main():
    rows = []
    poset_rows(rows)
    language_rows(rows)
    matroid_rows(rows)
    chip_rows(rows)
    tableau_rows(rows)
    check(len(rows) == 25, "candidate count")
    nfs_digest = nfs_focused_controls()
    payload = "\n".join(repr(row) for row in rows)
    print("REPLACEMENT_POSETS_LANGUAGES_SCOUT_V1")
    print("systems=25")
    for row in rows:
        print(repr(row))
    print(f"row_sha256={sha256(payload.encode()).hexdigest()}")
    print(f"nfs_focused_n=1..14")
    print(f"nfs_focused_sha256={sha256(repr(nfs_digest).encode()).hexdigest()}")
    print(f"nfs_n14={nfs_digest[-1]!r}")
    print(f"assertions={ASSERTIONS}")
    print("status=EMPTY_POOL_AFTER_OWNER_AND_INTERNAL_COLLISION_GATES")
    print("HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
