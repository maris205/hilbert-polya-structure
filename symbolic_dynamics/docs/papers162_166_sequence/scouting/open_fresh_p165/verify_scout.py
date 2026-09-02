#!/usr/bin/env python3
"""Independent exact checks for the open-fresh P165 scout.

No repository code, randomness, floating point, third-party package, network,
or clock is used.  The two admitted literal systems are:

PDI: a labelled poset is reordered by strict inclusion of strict principal
     downsets;
SDS: a q-ary linear code is shortened on the union of the supports of all
     nonzero words of weight strictly below twice its minimum distance.
"""

from collections import Counter, deque
from itertools import product
from math import factorial


ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


# ---------------------------------------------------------------------------
# PDI: principal-downset inclusion completion on all labelled posets.


def labelled_posets(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for choices in product(range(3), repeat=len(pairs)):
        relation = set()
        for (i, j), choice in zip(pairs, choices):
            if choice == 1:
                relation.add((i, j))
            elif choice == 2:
                relation.add((j, i))
        transitive = True
        for i, j in relation:
            for k in range(n):
                if (j, k) in relation and (i, k) not in relation:
                    transitive = False
                    break
            if not transitive:
                break
        if transitive:
            yield frozenset(relation)


def pdi_step(relation, n):
    strict_down = [set() for _ in range(n)]
    for i, j in relation:
        strict_down[j].add(i)
    return frozenset(
        (i, j)
        for i in range(n)
        for j in range(n)
        if i != j and strict_down[i] < strict_down[j]
    )


def is_weak_order_poset(relation, n):
    # For a strict partial order, weak-order layers are exactly the
    # equivalence classes of incomparability.  Test transitivity of that
    # reflexive incomparability relation directly.
    def tied(i, j):
        return i == j or ((i, j) not in relation and (j, i) not in relation)

    return all(
        not (tied(i, j) and tied(j, k)) or tied(i, k)
        for i in range(n)
        for j in range(n)
        for k in range(n)
    )


def pdi_audit():
    expected_states = [1, 3, 19, 219, 4231]
    expected_images = [1, 3, 13, 75, 601]
    expected_fixed = [1, 3, 13, 75, 541]
    expected_max_depth = [0, 0, 1, 1, 2]
    rows = []
    for n in range(1, 6):
        states = tuple(labelled_posets(n))
        state_set = set(states)
        check(len(states) == expected_states[n - 1], ("PDI states", n))
        image = Counter()
        depth_hist = Counter()
        fixed = 0
        for relation in states:
            nxt = pdi_step(relation, n)
            check(nxt in state_set, ("PDI closed", n, relation))
            check(relation <= nxt, ("PDI inflationary", n, relation))
            check(
                (nxt == relation) == is_weak_order_poset(relation, n),
                ("PDI fixed iff weak order", n, relation),
            )
            image[nxt] += 1
            fixed += nxt == relation
            seen = set()
            current = relation
            depth = 0
            while pdi_step(current, n) != current:
                check(current not in seen, ("PDI no nontrivial cycle", n))
                seen.add(current)
                current = pdi_step(current, n)
                depth += 1
                check(depth <= n * (n - 1) // 2, ("PDI finite bound", n))
            depth_hist[depth] += 1
        check(len(image) == expected_images[n - 1], ("PDI image", n))
        check(fixed == expected_fixed[n - 1], ("PDI fixed", n))
        check(max(depth_hist) == expected_max_depth[n - 1], ("PDI depth", n))
        rows.append(
            f"n={n}: states={len(states)}, image={len(image)}, fixed={fixed}, "
            f"max_depth={max(depth_hist)}, depth_hist={dict(sorted(depth_hist.items()))}"
        )
    return rows


# ---------------------------------------------------------------------------
# SDS over F_2, with every subspace generated independently by breadth first
# adjoining of vectors.


def binary_subspaces(n):
    zero = frozenset((0,))
    seen = {zero}
    queue = deque((zero,))
    while queue:
        space = queue.popleft()
        for vector in range(1, 1 << n):
            if vector not in space:
                extension = frozenset(set(space) | {x ^ vector for x in space})
                if extension not in seen:
                    seen.add(extension)
                    queue.append(extension)
    return seen


def binary_distance(code):
    return min((x.bit_count() for x in code if x), default=10**9)


def binary_support(code):
    ans = 0
    for word in code:
        ans |= word
    return ans


def binary_step(code):
    if len(code) == 1:
        return code
    distance = binary_distance(code)
    purge = 0
    for word in code:
        if word and word.bit_count() < 2 * distance:
            purge |= word
    return frozenset(word for word in code if word & purge == 0)


def iterate(step, state, time):
    for _ in range(time):
        state = step(state)
    return state


def rotate_binary(word, n):
    if n == 0:
        return word
    return ((word << 1) & ((1 << n) - 1)) | (word >> (n - 1))


def falling(value, length):
    ans = 1
    for offset in range(length):
        ans *= value - offset
    return ans


def minimal_binary_preimage_count(zero_coordinates, time):
    activated = (1 << time) - 1
    if zero_coordinates < activated:
        return 0
    denominator = 1
    for i in range(time):
        denominator *= factorial(1 << i)
    return falling(zero_coordinates, activated) // denominator


def binary_sds_audit():
    expected_states = [1, 2, 5, 16, 67, 374, 2825, 29212]
    rows = []
    for n in range(0, 8):
        spaces = binary_subspaces(n)
        check(len(spaces) == expected_states[n], ("F2 subspaces", n))
        depths = Counter()
        images_by_time = []
        max_time = 4
        current_image = set(spaces)
        for time in range(max_time + 1):
            images_by_time.append(current_image)
            current_image = {binary_step(code) for code in current_image}

        for code in spaces:
            nxt = binary_step(code)
            check(nxt in spaces, ("SDS F2 closed", n, code))
            check(nxt <= code, ("SDS F2 descending", n, code))
            if len(code) == 1:
                check(nxt == code, ("SDS F2 zero fixed", n))
            else:
                check(nxt != code, ("SDS F2 strict", n, code))
                if len(nxt) > 1:
                    check(
                        binary_distance(nxt) >= 2 * binary_distance(code),
                        ("SDS F2 distance doubles", n, code),
                    )
            rotated = frozenset(rotate_binary(word, n) for word in code)
            check(
                binary_step(rotated)
                == frozenset(rotate_binary(word, n) for word in nxt),
                ("SDS F2 coordinate covariance", n, code),
            )
            depth = 0
            current = code
            while len(current) > 1:
                current = binary_step(current)
                depth += 1
                check(depth <= (n + 1).bit_length(), ("SDS F2 termination", n))
            check(depth <= (n + 1).bit_length() - 1, ("SDS F2 sharp bound", n, code))
            depths[depth] += 1

        sharp = (n + 1).bit_length() - 1
        check(max(depths) == sharp, ("SDS F2 sharp height", n))

        for time, observed in enumerate(images_by_time):
            threshold = 1 << time
            required_zeros = threshold - 1
            predicted = {
                target
                for target in spaces
                if len(target) == 1
                or (
                    binary_distance(target) >= threshold
                    and n - binary_support(target).bit_count() >= required_zeros
                )
            }
            check(observed == predicted, ("SDS F2 exact image", n, time))

            # Count the simultaneous extremizers in each nonzero target fibre:
            # dimension increment=time and exactly 2^time-1 newly active sites.
            observed_extreme = Counter()
            for source in spaces:
                target = iterate(binary_step, source, time)
                if (
                    len(target) > 1
                    and len(source).bit_length() - len(target).bit_length() == time
                    and (
                        binary_support(source) & ~binary_support(target)
                    ).bit_count()
                    == required_zeros
                ):
                    observed_extreme[target] += 1
            for target in spaces:
                if len(target) == 1:
                    continue
                zero_coordinates = n - binary_support(target).bit_count()
                wanted = (
                    minimal_binary_preimage_count(zero_coordinates, time)
                    if binary_distance(target) >= threshold
                    else 0
                )
                check(
                    observed_extreme[target] == wanted,
                    ("SDS F2 extremal fibre", n, time, target),
                )

        rows.append(
            f"n={n}: states={len(spaces)}, max_depth={max(depths)}, "
            f"depth_hist={dict(sorted(depths.items()))}, "
            f"image_sizes_t0..4={[len(x) for x in images_by_time]}"
        )
    return rows


# ---------------------------------------------------------------------------
# A second implementation over F_3.  Tuples and explicit scalar spans avoid
# sharing the binary representation or update code above.


def q_vectors(q, n):
    return tuple(product(range(q), repeat=n))


def add_scaled(left, scalar, right, q):
    return tuple((x + scalar * y) % q for x, y in zip(left, right))


def qary_subspaces(q, n):
    zero_vector = (0,) * n
    zero = frozenset((zero_vector,))
    vectors = q_vectors(q, n)
    seen = {zero}
    queue = deque((zero,))
    while queue:
        space = queue.popleft()
        for vector in vectors:
            if vector not in space:
                extension = frozenset(
                    add_scaled(word, scalar, vector, q)
                    for word in space
                    for scalar in range(q)
                )
                if extension not in seen:
                    seen.add(extension)
                    queue.append(extension)
    return seen


def qary_weight(word):
    return sum(symbol != 0 for symbol in word)


def qary_distance(code):
    return min((qary_weight(word) for word in code if any(word)), default=10**9)


def qary_support(code):
    n = len(next(iter(code)))
    return frozenset(i for i in range(n) if any(word[i] for word in code))


def qary_step(code):
    if len(code) == 1:
        return code
    distance = qary_distance(code)
    purge = frozenset(
        i
        for word in code
        if any(word) and qary_weight(word) < 2 * distance
        for i, symbol in enumerate(word)
        if symbol
    )
    return frozenset(
        word for word in code if all(word[i] == 0 for i in purge)
    )


def qary_dimension(code, q):
    size = len(code)
    dimension = 0
    while size > 1:
        check(size % q == 0, ("q-ary dimension", q, len(code)))
        size //= q
        dimension += 1
    return dimension


def minimal_qary_preimage_count(zero_coordinates, time, q):
    binary_part = minimal_binary_preimage_count(zero_coordinates, time)
    activated = (1 << time) - 1
    return binary_part * (q - 1) ** (activated - time)


def ternary_sds_audit():
    expected_states = [1, 2, 6, 28, 212]
    rows = []
    q = 3
    for n in range(0, 5):
        spaces = qary_subspaces(q, n)
        check(len(spaces) == expected_states[n], ("F3 subspaces", n))
        depths = Counter()
        for code in spaces:
            nxt = qary_step(code)
            check(nxt in spaces, ("SDS F3 closed", n, code))
            check(nxt <= code, ("SDS F3 descending", n, code))
            if len(code) > 1:
                check(nxt != code, ("SDS F3 strict", n, code))
                if len(nxt) > 1:
                    check(
                        qary_distance(nxt) >= 2 * qary_distance(code),
                        ("SDS F3 distance doubles", n, code),
                    )
            current = code
            depth = 0
            while len(current) > 1:
                current = qary_step(current)
                depth += 1
            depths[depth] += 1
        check(
            max(depths) == (n + 1).bit_length() - 1,
            ("SDS F3 sharp height", n),
        )

        for time in range(0, 4):
            observed_image = {iterate(qary_step, source, time) for source in spaces}
            threshold = 1 << time
            required_zeros = threshold - 1
            predicted_image = {
                target
                for target in spaces
                if len(target) == 1
                or (
                    qary_distance(target) >= threshold
                    and n - len(qary_support(target)) >= required_zeros
                )
            }
            check(
                observed_image == predicted_image,
                ("SDS F3 exact image", n, time),
            )
            observed_extreme = Counter()
            for source in spaces:
                target = iterate(qary_step, source, time)
                if (
                    len(target) > 1
                    and qary_dimension(source, q) - qary_dimension(target, q) == time
                    and len(qary_support(source) - qary_support(target))
                    == required_zeros
                ):
                    observed_extreme[target] += 1
            for target in spaces:
                if len(target) == 1:
                    continue
                zero_coordinates = n - len(qary_support(target))
                wanted = (
                    minimal_qary_preimage_count(zero_coordinates, time, q)
                    if qary_distance(target) >= threshold
                    else 0
                )
                check(
                    observed_extreme[target] == wanted,
                    ("SDS F3 extremal fibre", n, time, target),
                )
        rows.append(
            f"n={n}: states={len(spaces)}, max_depth={max(depths)}, "
            f"depth_hist={dict(sorted(depths.items()))}"
        )
    return rows


def main():
    print("OPEN_FRESH_P165_EXACT_SCOUT")
    print("PDI_LABELLED_POSETS")
    for row in pdi_audit():
        print(row)
    print("SDS_BINARY_LINEAR_CODES")
    for row in binary_sds_audit():
        print(row)
    print("SDS_TERNARY_LINEAR_CODES")
    for row in ternary_sds_audit():
        print(row)
    print(f"ASSERTIONS {ASSERTIONS}")
    print("RESULT PASS")


if __name__ == "__main__":
    main()
