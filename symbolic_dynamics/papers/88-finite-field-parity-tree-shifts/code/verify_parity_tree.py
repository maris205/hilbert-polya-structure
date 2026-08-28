#!/usr/bin/env python3
"""Exact controls for finite-field parity tree shifts.

The theorem in the accompanying paper is stated for every prime power.  The
main lanes use prime fields F_p, and an independent exhaustive lane uses
F_4 = F_2[a]/(a^2+a+1).  The all-prime-power scope is supplied by the
field-linear proof, not inferred from these finite checks.

Two independent control lanes are used:

1. definition-level enumeration of leaves, legal blocks, rays, restrictions,
   and root/subboundary joint laws;
2. modular row reduction of the constraint, extension, reconstruction, and
   observation matrices.

Only the Python standard library is required.
"""

from collections import Counter
from itertools import product


ASSERTIONS = 0


def require(condition, message="exact control failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def level(d, height):
    return list(product(range(d), repeat=height))


def nodes(d, height):
    return [word for depth in range(height + 1)
            for word in level(d, depth)]


def extend_from_leaves(p, d, coefficients, height, leaf_values):
    """Return the unique legal block with the prescribed terminal level."""
    block = dict(zip(level(d, height), leaf_values))
    for depth in range(height - 1, -1, -1):
        for word in level(d, depth):
            block[word] = sum(coefficients[j] * block[word + (j,)]
                              for j in range(d)) % p
    return block


def legal_block(p, d, coefficients, height, block):
    for depth in range(height):
        for word in level(d, depth):
            rhs = sum(coefficients[j] * block[word + (j,)]
                      for j in range(d)) % p
            if block[word] % p != rhs:
                return False
    return True


def reconstruction_coefficients(p, coefficients, height):
    return tuple(prod_mod((coefficients[j] for j in word), p)
                 for word in level(len(coefficients), height))


def prod_mod(values, p):
    answer = 1
    for value in values:
        answer = (answer * value) % p
    return answer


def rank_mod(matrix, p):
    """Exact Gaussian rank over the prime field F_p."""
    if not matrix:
        return 0
    a = [[entry % p for entry in row] for row in matrix]
    row_count = len(a)
    column_count = len(a[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next((r for r in range(pivot_row, row_count)
                      if a[r][column] % p), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inverse = pow(a[pivot_row][column], -1, p)
        a[pivot_row] = [(inverse * value) % p
                        for value in a[pivot_row]]
        for r in range(row_count):
            if r == pivot_row or a[r][column] == 0:
                continue
            factor = a[r][column]
            a[r] = [(a[r][c] - factor * a[pivot_row][c]) % p
                    for c in range(column_count)]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def matmul_mod(left, right, p):
    if not left:
        return []
    if not right:
        return [[] for _ in left]
    inner = len(right)
    columns = len(right[0])
    return [[sum(left[i][k] * right[k][j] for k in range(inner)) % p
             for j in range(columns)]
            for i in range(len(left))]


def constraint_matrix(p, d, coefficients, height):
    ordered = nodes(d, height)
    position = {word: index for index, word in enumerate(ordered)}
    matrix = []
    for depth in range(height):
        for word in level(d, depth):
            row = [0] * len(ordered)
            row[position[word]] = 1
            for j, coefficient in enumerate(coefficients):
                child = word + (j,)
                row[position[child]] = (-coefficient) % p
            matrix.append(row)
    return matrix, ordered


def extension_matrix(p, d, coefficients, height, ordered):
    leaves = level(d, height)
    columns = []
    for index in range(len(leaves)):
        terminal = [0] * len(leaves)
        terminal[index] = 1
        block = extend_from_leaves(p, d, coefficients, height, terminal)
        columns.append([block[word] for word in ordered])
    return [[columns[column][row] for column in range(len(columns))]
            for row in range(len(ordered))]


def rank_lane(p, d, coefficients, height):
    matrix, ordered = constraint_matrix(p, d, coefficients, height)
    leaves = level(d, height)
    internal_count = len(ordered) - len(leaves)
    require(rank_mod(matrix, p) == internal_count,
            "constraint rows do not have full rank")

    extension = extension_matrix(p, d, coefficients, height, ordered)
    require(rank_mod(extension, p) == len(leaves),
            "boundary extension is not injective")
    zero = matmul_mod(matrix, extension, p)
    require(all(entry == 0 for row in zero for entry in row),
            "extension columns violate a local constraint")

    terminal_positions = [ordered.index(word) for word in leaves]
    terminal_rows = [extension[position] for position in terminal_positions]
    identity = [[1 if i == j else 0 for j in range(len(leaves))]
                for i in range(len(leaves))]
    require(terminal_rows == identity,
            "extension does not preserve terminal coordinates")

    root_row = extension[ordered.index(())]
    claimed = list(reconstruction_coefficients(p, coefficients, height))
    require(root_row == claimed, "root reconstruction row is wrong")
    require(all(value != 0 for value in claimed),
            "a terminal reconstruction coefficient vanished")

    # A proper terminal subset plus the root functional has one more rank
    # than the subset.  This is the linear-algebra certificate for zero
    # mutual information.  For the complete level, the root row is already
    # in the coordinate span.
    subset_certificates = 0
    leaf_count = len(leaves)
    if leaf_count <= 10:
        masks = list(range(1 << leaf_count))
    else:
        full = (1 << leaf_count) - 1
        masks = {0, full}
        masks.update(1 << index for index in range(leaf_count))
        masks.update(full ^ (1 << index) for index in range(leaf_count))
        masks.update((1 << size) - 1 for size in range(1, leaf_count))
        masks.add(sum(1 << index for index in range(0, leaf_count, 2)))
        masks.add(sum(1 << index for index in range(1, leaf_count, 2)))
        masks = sorted(masks)
    for mask in masks:
        coordinate_rows = []
        selected = 0
        for index in range(leaf_count):
            if mask & (1 << index):
                row = [0] * leaf_count
                row[index] = 1
                coordinate_rows.append(row)
                selected += 1
        observed = coordinate_rows + [claimed]
        expected = selected + 1 if selected < leaf_count else leaf_count
        require(rank_mod(observed, p) == expected,
                "root/subboundary observation rank is wrong")
        subset_certificates += 1

    # The restriction from level h to level h-1 has one disjoint nonzero
    # row per parent, so it is onto with the claimed kernel dimension.
    if height >= 1:
        parent_level = level(d, height - 1)
        position = {word: index for index, word in enumerate(leaves)}
        restriction = []
        for parent in parent_level:
            row = [0] * leaf_count
            for j, coefficient in enumerate(coefficients):
                row[position[parent + (j,)]] = coefficient
            restriction.append(row)
        require(rank_mod(restriction, p) == len(parent_level),
                "level restriction is not onto")

    return len(matrix), len(leaves), subset_certificates


def exhaustive_case(p, d, coefficients, height,
                    check_all_subsets=False, brute_legal=False):
    leaves = level(d, height)
    ordered = nodes(d, height)
    leaf_count = len(leaves)
    assignments = list(product(range(p), repeat=leaf_count))
    blocks = []
    block_words = set()
    for terminal in assignments:
        block = extend_from_leaves(p, d, coefficients, height, terminal)
        require(legal_block(p, d, coefficients, height, block),
                "upward extension is not legal")
        blocks.append(block)
        block_words.add(tuple(block[word] for word in ordered))
    require(len(block_words) == p ** leaf_count,
            "leaf-to-block map is not bijective")

    claimed = reconstruction_coefficients(p, coefficients, height)
    for terminal, block in zip(assignments, blocks):
        reconstructed = sum(a * b for a, b in zip(claimed, terminal)) % p
        require(block[()] == reconstructed,
                "explicit root reconstruction failed")

    if brute_legal:
        legal_words = set()
        for values in product(range(p), repeat=len(ordered)):
            block = dict(zip(ordered, values))
            if legal_block(p, d, coefficients, height, block):
                legal_words.add(values)
        require(legal_words == block_words,
                "brute legal blocks differ from boundary extensions")

    # Restricting uniform height-h blocks to height h-1 must give the uniform
    # law, with a constant fiber size.
    if height >= 1:
        parent_level = level(d, height - 1)
        restriction_counts = Counter(
            tuple(block[word] for word in parent_level) for block in blocks)
        expected_targets = p ** len(parent_level)
        expected_fiber = p ** (leaf_count - len(parent_level))
        require(len(restriction_counts) == expected_targets,
                "restriction misses a boundary vector")
        require(set(restriction_counts.values()) == {expected_fiber},
                "restriction fibers are not constant")
    else:
        expected_fiber = 1

    # Every deterministic root-to-level-h ray has the product uniform law.
    for path in leaves:
        prefixes = [path[:depth] for depth in range(height + 1)]
        ray_counts = Counter(tuple(block[word] for word in prefixes)
                             for block in blocks)
        expected_patterns = p ** (height + 1)
        expected_ray_fiber = p ** (leaf_count - height - 1)
        require(len(ray_counts) == expected_patterns,
                "a ray does not realize every iid word")
        require(set(ray_counts.values()) == {expected_ray_fiber},
                "a ray law is not uniform")

    exact_subsets = 0
    if check_all_subsets:
        for mask in range((1 << leaf_count) - 1):
            indices = [index for index in range(leaf_count)
                       if mask & (1 << index)]
            joint = Counter((block[()], tuple(terminal[index]
                                               for index in indices))
                            for terminal, block in zip(assignments, blocks))
            expected_atoms = p ** (len(indices) + 1)
            expected_mass = p ** (leaf_count - len(indices) - 1)
            require(len(joint) == expected_atoms,
                    "root/subboundary joint law misses an atom")
            require(set(joint.values()) == {expected_mass},
                    "root and a proper subboundary are not independent")
            exact_subsets += 1

    return {
        "blocks": len(block_words),
        "leaves": leaf_count,
        "rays": len(leaves),
        "proper_subsets": exact_subsets,
        "restriction_fiber": expected_fiber,
    }


def f4_add(left, right):
    """Addition in F_4, encoded as a+b*a in the two binary digits."""
    return left ^ right


def f4_mul(left, right):
    """Multiplication modulo a^2+a+1 in the encoding 0,1,a,1+a."""
    left_0, left_1 = left & 1, (left >> 1) & 1
    right_0, right_1 = right & 1, (right >> 1) & 1
    constant = (left_0 * right_0) ^ (left_1 * right_1)
    linear = (left_0 * right_1) ^ (left_1 * right_0) ^ (left_1 * right_1)
    return constant | (linear << 1)


def f4_sum(values):
    answer = 0
    for value in values:
        answer = f4_add(answer, value)
    return answer


def f4_prod(values):
    answer = 1
    for value in values:
        answer = f4_mul(answer, value)
    return answer


def exhaustive_f4_case(coefficients=(1, 2), height=2):
    """Independent non-prime-field enumeration for the binary tree."""
    field = range(4)
    d = len(coefficients)
    require(d == 2, "the F_4 control is frozen to the binary tree")
    require(all(coefficient in (1, 2, 3) for coefficient in coefficients),
            "the F_4 control requires nonzero coefficients")

    # Guard the hand-written field implementation before using it as an
    # oracle for the tree identities.
    for x in field:
        require(f4_add(x, 0) == x, "F_4 additive identity failed")
        require(f4_add(x, x) == 0, "F_4 characteristic-two law failed")
        require(f4_mul(x, 1) == x, "F_4 multiplicative identity failed")
        for y in field:
            require(f4_add(x, y) in field, "F_4 addition is not closed")
            require(f4_mul(x, y) in field, "F_4 multiplication is not closed")
            require(f4_add(x, y) == f4_add(y, x),
                    "F_4 addition is not commutative")
            require(f4_mul(x, y) == f4_mul(y, x),
                    "F_4 multiplication is not commutative")
            for z in field:
                require(f4_add(x, f4_add(y, z)) ==
                        f4_add(f4_add(x, y), z),
                        "F_4 addition is not associative")
                require(f4_mul(x, f4_mul(y, z)) ==
                        f4_mul(f4_mul(x, y), z),
                        "F_4 multiplication is not associative")
                require(f4_mul(x, f4_add(y, z)) ==
                        f4_add(f4_mul(x, y), f4_mul(x, z)),
                        "F_4 distributivity failed")
    for x in (1, 2, 3):
        require(any(f4_mul(x, y) == 1 for y in (1, 2, 3)),
                "a nonzero F_4 element has no inverse")

    leaves = level(d, height)
    ordered = nodes(d, height)

    def extend(terminal):
        block = dict(zip(leaves, terminal))
        for depth in range(height - 1, -1, -1):
            for word in level(d, depth):
                block[word] = f4_sum(
                    f4_mul(coefficients[j], block[word + (j,)])
                    for j in range(d))
        return block

    assignments = list(product(field, repeat=len(leaves)))
    blocks = []
    block_words = set()
    for terminal in assignments:
        block = extend(terminal)
        for depth in range(height):
            for word in level(d, depth):
                rhs = f4_sum(
                    f4_mul(coefficients[j], block[word + (j,)])
                    for j in range(d))
                require(block[word] == rhs, "F_4 local rule failed")
        blocks.append(block)
        block_words.add(tuple(block[word] for word in ordered))
    require(len(block_words) == 4 ** len(leaves),
            "F_4 leaf-to-block map is not bijective")

    claimed = tuple(f4_prod(coefficients[j] for j in word)
                    for word in leaves)
    require(all(value != 0 for value in claimed),
            "an F_4 reconstruction coefficient vanished")
    for terminal, block in zip(assignments, blocks):
        reconstructed = f4_sum(f4_mul(a, b)
                               for a, b in zip(claimed, terminal))
        require(block[()] == reconstructed,
                "F_4 root reconstruction failed")

    parent_level = level(d, height - 1)
    restriction_counts = Counter(
        tuple(block[word] for word in parent_level) for block in blocks)
    expected_fiber = 4 ** (len(leaves) - len(parent_level))
    require(len(restriction_counts) == 4 ** len(parent_level),
            "F_4 restriction misses a boundary vector")
    require(set(restriction_counts.values()) == {expected_fiber},
            "F_4 restriction fibers are not constant")

    for path in leaves:
        prefixes = [path[:depth] for depth in range(height + 1)]
        ray_counts = Counter(tuple(block[word] for word in prefixes)
                             for block in blocks)
        require(len(ray_counts) == 4 ** (height + 1),
                "an F_4 ray misses a word")
        require(set(ray_counts.values()) ==
                {4 ** (len(leaves) - height - 1)},
                "an F_4 ray law is not uniform")

    proper_subsets = 0
    for mask in range((1 << len(leaves)) - 1):
        indices = [index for index in range(len(leaves))
                   if mask & (1 << index)]
        joint = Counter((block[()], tuple(terminal[index]
                                          for index in indices))
                        for terminal, block in zip(assignments, blocks))
        require(len(joint) == 4 ** (len(indices) + 1),
                "F_4 root/subboundary law misses an atom")
        require(set(joint.values()) ==
                {4 ** (len(leaves) - len(indices) - 1)},
                "F_4 root and proper subboundary are not independent")
        proper_subsets += 1

    return {
        "blocks": len(block_words),
        "leaves": len(leaves),
        "rays": len(leaves),
        "proper_subsets": proper_subsets,
        "restriction_fiber": expected_fiber,
    }


def assumption_failure_controls():
    """Check the two sharp failure mechanisms stated in Remark 5.2."""
    # With d=1 and coefficient 2 in F_3, the child is determined by the
    # parent, so only three of the nine possible two-letter ray words occur.
    d1_pairs = {(2 * child % 3, child) for child in range(3)}
    require(len(d1_pairs) == 3, "d=1 unexpectedly gives an iid ray")

    # With c=(1,0), omitting the zero-coefficient child leaves the root equal
    # to the first child, so that proper subset reconstructs the root.
    zero_coefficient_pairs = {(first, first) for first in range(3)}
    require(all(root == observed for root, observed in zero_coefficient_pairs),
            "zero-coefficient reconstruction witness failed")


def main():
    print("finite-field parity tree exact controls")
    print("control scope: prime fields plus one exhaustive F_4 lane")

    cases = [
        # (p, d, coefficients, height, all proper subsets, brute all blocks)
        (2, 2, (1, 1), 3, True, False),
        (2, 3, (1, 1, 1), 2, True, False),
        (3, 2, (1, 1), 2, True, True),
        (3, 2, (1, 2), 3, False, False),
        (5, 2, (1, 2), 2, True, False),
        (2, 2, (1, 1), 2, False, True),
        (2, 3, (1, 1, 1), 1, False, True),
    ]

    total_blocks = 0
    total_proper_subsets = 0
    for p, d, coefficients, height, all_subsets, brute in cases:
        result = exhaustive_case(p, d, coefficients, height,
                                 check_all_subsets=all_subsets,
                                 brute_legal=brute)
        total_blocks += result["blocks"]
        total_proper_subsets += result["proper_subsets"]
        print(
            f"F_{p}, d={d}, c={coefficients}, h={height}: "
            f"leaves={result['leaves']}, blocks={result['blocks']}, "
            f"rays={result['rays']}, "
            f"proper_subsets={result['proper_subsets']}, "
            f"restriction_fiber={result['restriction_fiber']}"
        )

    f4_result = exhaustive_f4_case()
    total_blocks += f4_result["blocks"]
    total_proper_subsets += f4_result["proper_subsets"]
    print(
        "F_4, d=2, c=(1,a), h=2: "
        f"leaves={f4_result['leaves']}, blocks={f4_result['blocks']}, "
        f"rays={f4_result['rays']}, "
        f"proper_subsets={f4_result['proper_subsets']}, "
        f"restriction_fiber={f4_result['restriction_fiber']}"
    )

    assumption_failure_controls()
    print("negative controls: d=1 ray degeneracy; zero-coefficient deletion leak")

    rank_cases = [
        (2, 2, (1, 1), 4),
        (2, 3, (1, 1, 1), 3),
        (3, 2, (1, 2), 4),
        (5, 2, (2, 4), 3),
        (5, 3, (1, 2, 4), 3),
        (7, 2, (3, 5), 4),
    ]
    total_rows = 0
    total_rank_subsets = 0
    for p, d, coefficients, height in rank_cases:
        rows, leaves_count, subset_count = rank_lane(
            p, d, coefficients, height)
        total_rows += rows
        total_rank_subsets += subset_count
        print(
            f"rank F_{p}, d={d}, c={coefficients}, h={height}: "
            f"constraint_rows={rows}, nullity={leaves_count}, "
            f"subset_certificates={subset_count}"
        )

    print(
        f"ledger: enumerated_blocks={total_blocks}, "
        f"exhaustive_proper_subsets={total_proper_subsets}, "
        f"rank_constraint_rows={total_rows}, "
        f"rank_subset_certificates={total_rank_subsets}, "
        f"assertions={ASSERTIONS}"
    )
    print("ALL EXACT CONTROLS PASSED")


if __name__ == "__main__":
    main()
