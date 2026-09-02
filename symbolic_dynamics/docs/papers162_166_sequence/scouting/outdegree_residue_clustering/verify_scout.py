#!/usr/bin/env python3
"""Independent exact controls for DRC3.

The implementation uses row subsets for literal digraph exhaustion and
restricted-growth strings for the induced set-partition dynamics.  It does
not import any other scout or paper verifier.
"""

from collections import Counter, defaultdict
from itertools import permutations, product
from math import comb, factorial


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def canonical(labels):
    rename = {}
    answer = []
    for value in labels:
        if value not in rename:
            rename[value] = len(rename)
        answer.append(rename[value])
    return tuple(answer)


def blocks(partition):
    out = [[] for _ in range(max(partition, default=-1) + 1)]
    for vertex, block in enumerate(partition):
        out[block].append(vertex)
    return tuple(tuple(block) for block in out)


def partition_map(partition):
    bb = blocks(partition)
    size_at = [0] * len(partition)
    for block in bb:
        for vertex in block:
            size_at[vertex] = len(block)
    return canonical(size % 3 for size in size_at)


def partition_depth(partition):
    seen = set()
    depth = 0
    while True:
        nxt = partition_map(partition)
        if nxt == partition:
            return depth
        check(partition not in seen, "partition cycle")
        seen.add(partition)
        partition = nxt
        depth += 1
        check(depth <= 3, "partition depth overflow")


def rgs_partitions(n, max_blocks=3):
    if n == 0:
        yield ()
        return
    word = [0] * n

    def visit(pos, largest):
        if pos == n:
            yield tuple(word)
            return
        for value in range(min(largest + 1, max_blocks - 1) + 1):
            word[pos] = value
            yield from visit(pos + 1, max(largest, value))

    yield from visit(1, 0)


def integer_partitions_at_most_three(n):
    yield (n,)
    for a in range(n - 1, 0, -1):
        for b in range(min(a, n - a), 0, -1):
            c = n - a - b
            if c == 0:
                yield (a, b)
            elif 1 <= c <= b:
                yield (a, b, c)


def target_multiplicity(shape):
    n = sum(shape)
    answer = factorial(n)
    multiplicities = Counter(shape)
    for size in shape:
        answer //= factorial(size)
    for count in multiplicities.values():
        answer //= factorial(count)
    return answer


def c_vector(n):
    return tuple(
        sum(comb(n - 1, degree) for degree in range(residue, n, 3))
        for residue in range(3)
    )


def c_vector_filter(n):
    power = 1 << (n - 1)
    corrections = (
        (2, -1, -1),
        (1, 1, -2),
        (-1, 2, -1),
        (-2, 1, 1),
        (-1, -1, 2),
        (1, -2, 1),
    )[(n - 1) % 6]
    return tuple((power + correction) // 3 for correction in corrections)


def common_exceptional(n):
    values = c_vector(n)
    counts = Counter(values)
    common = next(value for value, count in counts.items() if count == 2)
    exceptional = next(value for value, count in counts.items() if count == 1)
    exceptional_residue = values.index(exceptional)
    return common, exceptional, exceptional_residue


def fibre_formula_shape(shape, n):
    values = c_vector(n)
    total = 0
    for assignment in permutations(range(3), len(shape)):
        term = 1
        for size, residue in zip(shape, assignment):
            term *= values[residue] ** size
        total += term
    return total


def fibre_two_value_shape(shape, n):
    common, exceptional, _ = common_exceptional(n)
    if len(shape) == 1:
        return 2 * common**n + exceptional**n
    if len(shape) == 2:
        p, q = shape
        return 2 * (
            common**n
            + exceptional**p * common**q
            + exceptional**q * common**p
        )
    return 2 * sum(
        exceptional**size * common ** (n - size) for size in shape
    )


def shape_is_fixed(shape):
    residues = [size % 3 for size in shape]
    return len(residues) == len(set(residues))


def shape_is_deep(shape):
    residues = [size % 3 for size in shape]
    return len(shape) == 3 and set(residues) == {1, 2}


def multinomial_count(vector):
    answer = factorial(sum(vector))
    for value in vector:
        answer //= factorial(value)
    return answer


def vector_weight(n, vector):
    answer = multinomial_count(vector)
    for count, choices in zip(vector, c_vector(n)):
        answer *= choices**count
    return answer


def first_image_is_fixed(vector):
    residues = [count % 3 for count in vector if count]
    return len(residues) == len(set(residues))


def first_image_is_deep(vector):
    return all(vector) and {count % 3 for count in vector} == {1, 2}


def fixed_count_coordinate_formula(n):
    # In a fixed graph the residue-r class is a clique of size 1+r mod 3.
    total = 0
    for a0 in range(n + 1):
        for a1 in range(n - a0 + 1):
            vector = (a0, a1, n - a0 - a1)
            if all(
                count == 0 or count % 3 == (residue + 1) % 3
                for residue, count in enumerate(vector)
            ):
                total += multinomial_count(vector)
    return total


def stirling_two(n):
    return (2**n - 2) // 2


def stirling_three(n):
    return (3**n - 3 * 2**n + 3) // 6


def depth_census(n):
    total = 1 << (n * (n - 1))
    first_fixed_mass = 0
    deepest = 0
    for a0 in range(n + 1):
        for a1 in range(n - a0 + 1):
            vector = (a0, a1, n - a0 - a1)
            weight = vector_weight(n, vector)
            if first_image_is_fixed(vector):
                first_fixed_mass += weight
            elif first_image_is_deep(vector):
                deepest += weight
    fixed = fixed_count_coordinate_formula(n)
    return (
        fixed,
        first_fixed_mass - fixed,
        total - first_fixed_mass - deepest,
        deepest,
    )


def shape_sums(n):
    image = fixed = first_fixed_mass = deepest = mass = 0
    spectrum = defaultdict(int)
    image2_extra = 0
    for shape in integer_partitions_at_most_three(n):
        multiplicity = target_multiplicity(shape)
        fibre = fibre_formula_shape(shape, n)
        image += multiplicity
        mass += multiplicity * fibre
        spectrum[fibre] += multiplicity
        if shape_is_fixed(shape):
            fixed += multiplicity
            first_fixed_mass += multiplicity * fibre
        elif shape_is_deep(shape):
            deepest += multiplicity * fibre
        if (
            len(shape) == 2
            and shape[0] % 3 == shape[1] % 3
            and shape[0] % 3 in (1, 2)
        ):
            image2_extra += multiplicity
    return image, fixed, first_fixed_mass, deepest, image2_extra, mass, spectrum


def rows_to_partition(rows):
    return canonical(row.bit_count() % 3 for row in rows)


def target_rows(rows, n):
    residues = [row.bit_count() % 3 for row in rows]
    answer = []
    for tail in range(n):
        row = 0
        bit = 0
        for head in range(n):
            if head == tail:
                continue
            if residues[tail] == residues[head]:
                row |= 1 << bit
            bit += 1
        answer.append(row)
    return tuple(answer)


def literal_exhaustion(n):
    row_range = range(1 << (n - 1))
    fibres = Counter()
    depths = Counter()
    fixed = 0
    cache = {}
    for residue_word in product(range(3), repeat=n):
        part = canonical(residue_word)
        representative_rows = tuple(
            next(row for row in row_range if row.bit_count() % 3 == residue)
            for residue in residue_word
        )
        image_rows = target_rows(representative_rows, n)
        check(rows_to_partition(image_rows) == partition_map(part))
        check(partition_depth(part) <= 2)
        cache[residue_word] = (part, image_rows, partition_depth(part))

    for rows in product(row_range, repeat=n):
        residue_word = tuple(row.bit_count() % 3 for row in rows)
        part, image_rows, part_depth = cache[residue_word]
        direct_image = target_rows(rows, n)
        check(direct_image == image_rows, "row realization changed target")
        check(rows_to_partition(rows) == part)
        fibres[part] += 1
        if rows == direct_image:
            fixed += 1
            depths[0] += 1
            check(partition_map(part) == part)
        else:
            depths[1 + part_depth] += 1

    expected_targets = set(rgs_partitions(n, 3))
    check(set(fibres) == expected_targets)
    for part in expected_targets:
        shape = tuple(sorted((len(block) for block in blocks(part)), reverse=True))
        check(fibres[part] == fibre_formula_shape(shape, n), "literal fibre")
    check(fixed == fixed_count_coordinate_formula(n))
    check(tuple(depths[index] for index in range(4)) == depth_census(n))
    check(sum(fibres.values()) == 1 << (n * (n - 1)))
    return len(fibres), fixed, tuple(depths[index] for index in range(4))


def partition_image_controls(n):
    states = set(rgs_partitions(n, 3))
    image2 = {partition_map(part) for part in states}
    image3 = {partition_map(part) for part in image2}
    fixed = {part for part in states if partition_map(part) == part}
    for part in states:
        shape = tuple(len(block) for block in blocks(part))
        check(partition_depth(part) == (2 if shape_is_deep(shape) else 0 if shape_is_fixed(shape) else 1))
    check(image3 == fixed)
    shape_data = shape_sums(n)
    check(len(states) == shape_data[0])
    check(len(fixed) == shape_data[1])
    check(len(image2) == shape_data[1] + shape_data[4])
    return len(states), len(image2), len(image3)


def main():
    print("DRC3 independent exact verifier")
    print("carrier: all loopless labelled digraphs on [n], n>=4")

    for n in range(4, 19):
        values = c_vector(n)
        check(values == c_vector_filter(n), "roots-of-unity filter")
        check(sum(values) == 1 << (n - 1))
        check(all(value > 0 for value in values))
        check(sorted(Counter(values).values()) == [1, 2])
        for shape in integer_partitions_at_most_three(n):
            check(fibre_formula_shape(shape, n) == fibre_two_value_shape(shape, n))

        image, fixed, first_fixed, deepest, image2_extra, mass, _ = shape_sums(n)
        census = depth_census(n)
        check(image == 1 + stirling_two(n) + stirling_three(n))
        check(fixed == fixed_count_coordinate_formula(n))
        check(mass == 1 << (n * (n - 1)))
        check(first_fixed == census[0] + census[1])
        check(deepest == census[3])
        check(sum(census) == mass)
        check((deepest == 0) == (n % 3 == 0))
        check(image2_extra == 0 if n % 3 == 0 else image2_extra > 0)

    print("literal exhaustion")
    for n in (4, 5):
        image, fixed, census = literal_exhaustion(n)
        print(f"n={n} states={1 << (n*(n-1))} image={image} fixed={fixed} depth={census}")

    print("partition image tower")
    for n in range(4, 11):
        image1, image2, image3 = partition_image_controls(n)
        print(f"n={n} I1={image1} I2={image2} I3={image3}")

    print("all-parameter formula table")
    for n in range(4, 16):
        values = c_vector(n)
        _, exceptional, exceptional_residue = common_exceptional(n)
        image1, fixed, _, _, image2_extra, _, spectrum = shape_sums(n)
        census = depth_census(n)
        print(
            f"n={n} c={values} exceptional=(r{exceptional_residue},{exceptional}) "
            f"images=({image1},{fixed+image2_extra},{fixed}) "
            f"depth={census} fibre_values={len(spectrum)}"
        )

    print("selected fibre spectra (value:target-multiplicity)")
    for n in range(4, 9):
        spectrum = shape_sums(n)[-1]
        cells = ",".join(f"{value}:{spectrum[value]}" for value in sorted(spectrum))
        print(f"n={n} {cells}")

    # Explicit sharp witnesses expressed as residue-class cardinalities.
    for n in range(4, 19):
        if n % 3 == 1:
            witness = (1, 1, n - 2)
            check(first_image_is_deep(witness))
        elif n % 3 == 2:
            witness = (2, 2, n - 4)
            check(first_image_is_deep(witness))
        else:
            witness = (1, 1, n - 2)
            check(not first_image_is_fixed(witness))
            check(not first_image_is_deep(witness))
        check(all(count >= 0 for count in witness) and sum(witness) == n)

    print(f"assertions={ASSERTIONS}")
    print("PASS")


if __name__ == "__main__":
    main()
