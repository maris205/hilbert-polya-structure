#!/usr/bin/env python3
"""Independent hostile-Review-B verifier for P173.

This program intentionally imports no paper, scout, or Review-A module.  Its
literal states are incidence bitsets of normalized projective points.  This is
different from both vector-set and RREF/annihilator representations.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product


ASSERTIONS = 0


def require(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= q ** (n - i) - 1
        denominator *= q ** (k - i) - 1
    require(numerator % denominator == 0,
            "Gaussian coefficient lost integrality")
    return numerator // denominator


def injection_count(domain_dimension, codomain_dimension, q):
    if domain_dimension < 0 or codomain_dimension < domain_dimension:
        return 0
    answer = 1
    for i in range(domain_dimension):
        answer *= q ** codomain_dimension - q ** i
    return answer


def target_count(n, q, a, b):
    return injection_count(a - b, n - a, q)


def quotient_matrix(n, q):
    matrix = [[Fraction(0) for _ in range(n + 1)] for _ in range(n + 1)]
    for a in range(n + 1):
        denominator = q ** (a * (n - a))
        for b in range(a + 1):
            matrix[a][b] = Fraction(
                gaussian(a, b, q) * target_count(n, q, a, b), denominator
            )
    return matrix


def identity(size):
    return [[Fraction(int(i == j)) for j in range(size)] for i in range(size)]


def matrix_multiply(left, right):
    rows = len(left)
    middle = len(right)
    cols = len(right[0])
    out = [[Fraction(0) for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for k in range(middle):
            if left[i][k] == 0:
                continue
            coefficient = left[i][k]
            for j in range(cols):
                if right[k][j] != 0:
                    out[i][j] += coefficient * right[k][j]
    return out


def matrix_power(matrix, exponent):
    result = identity(len(matrix))
    base = matrix
    while exponent:
        if exponent & 1:
            result = matrix_multiply(result, base)
        exponent >>= 1
        if exponent:
            base = matrix_multiply(base, base)
    return result


def rational_rank(matrix):
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows)
                      if work[r][col] != 0), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][col]
        work[pivot_row] = [entry / pivot_value for entry in work[pivot_row]]
        for r in range(rows):
            if r == pivot_row or work[r][col] == 0:
                continue
            factor = work[r][col]
            work[r] = [work[r][c] - factor * work[pivot_row][c]
                       for c in range(cols)]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def shifted(matrix, eigenvalue):
    return [
        [entry - (eigenvalue if i == j else 0)
         for j, entry in enumerate(row)]
        for i, row in enumerate(matrix)
    ]


def row_action(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(len(vector)))
            for i in range(len(matrix))]


def normalize_projective(vector, q):
    first = next((entry for entry in vector if entry % q), None)
    if first is None:
        return None
    inverse = pow(first, -1, q)
    return tuple((entry * inverse) % q for entry in vector)


def projective_points(q, n):
    representatives = {
        normalize_projective(vector, q)
        for vector in product(range(q), repeat=n)
        if any(vector)
    }
    return sorted(representatives)


def span_mask(generators, q, point_index, n):
    mask = 0
    for coefficients in product(range(q), repeat=len(generators)):
        vector = tuple(
            sum(coefficients[i] * generators[i][coordinate]
                for i in range(len(generators))) % q
            for coordinate in range(n)
        )
        normalized = normalize_projective(vector, q)
        if normalized is not None:
            mask |= 1 << point_index[normalized]
    return mask


def enumerate_projective_subspaces(q, n):
    points = projective_points(q, n)
    point_index = {point: i for i, point in enumerate(points)}
    masks = set()
    for number_of_generators in range(n + 1):
        for chosen in combinations(points, number_of_generators):
            masks.add(span_mask(chosen, q, point_index, n))

    def dimension(mask):
        vector_count = 1 + (q - 1) * mask.bit_count()
        d = 0
        while q ** d < vector_count:
            d += 1
        require(q ** d == vector_count, "projective incidence is not a subspace")
        return d

    dimensions = {mask: dimension(mask) for mask in masks}
    ordered = sorted(masks, key=lambda mask: (dimensions[mask], mask))
    require(len(ordered) == sum(gaussian(n, d, q) for d in range(n + 1)),
            "subspace census mismatch")
    for d in range(n + 1):
        require(sum(dimensions[mask] == d for mask in ordered) == gaussian(n, d, q),
                "dimension layer census mismatch")
    return points, ordered, dimensions


def matrix_projective_action(entries, points, q, n, point_index):
    image = []
    for point in points:
        vector = tuple(
            sum(entries[row * n + column] * point[column]
                for column in range(n)) % q
            for row in range(n)
        )
        normalized = normalize_projective(vector, q)
        image.append(-1 if normalized is None else point_index[normalized])
    return image


def literal_box(q, n, epochs):
    points, states, dimensions = enumerate_projective_subspaces(q, n)
    state_index = {mask: i for i, mask in enumerate(states)}
    point_index = {point: i for i, point in enumerate(points)}
    transition_counts = [Counter() for _ in states]
    number_of_maps = q ** (n * n)

    for entries in product(range(q), repeat=n * n):
        action = matrix_projective_action(entries, points, q, n, point_index)
        for source_index, source in enumerate(states):
            target = 0
            remaining = source
            while remaining:
                bit = remaining & -remaining
                point = bit.bit_length() - 1
                image = action[point]
                if image < 0 or ((source >> image) & 1):
                    target |= bit
                remaining ^= bit
            require(target in state_index,
                    "literal update failed projective subspace closure")
            require((target & ~source) == 0,
                    "literal update violated nestedness")
            transition_counts[source_index][state_index[target]] += 1

    qmatrix = quotient_matrix(n, q)
    digest = sha256()
    for source_index, source in enumerate(states):
        a = dimensions[source]
        require(sum(transition_counts[source_index].values()) == number_of_maps,
                "ambient maps do not fill transition row")
        dimension_totals = Counter()
        for target_index, target in enumerate(states):
            b = dimensions[target]
            actual = transition_counts[source_index][target_index]
            if target & ~source:
                expected = 0
            else:
                expected = (q ** (n * n - a * (n - a))
                            * target_count(n, q, a, b))
            require(actual == expected, "every-target ambient fibre mismatch")
            dimension_totals[b] += actual
            digest.update(f"{source}:{target}:{actual};".encode("ascii"))
        for b in range(n + 1):
            require(Fraction(dimension_totals[b], number_of_maps) == qmatrix[a][b],
                    "literal dimension quotient mismatch")
        expected_diagonal = q ** (n * n - a * (n - a))
        require(transition_counts[source_index][source_index] == expected_diagonal,
                "literal self-loop mismatch")

    quotient_power = identity(n + 1)
    all_time_assertions = 0
    for source_index, source in enumerate(states):
        a = dimensions[source]
        distribution = {source_index: Fraction(1)}
        quotient_power = identity(n + 1)
        for epoch in range(epochs + 1):
            for target_index, target in enumerate(states):
                b = dimensions[target]
                if target & ~source:
                    expected = Fraction(0)
                else:
                    expected = quotient_power[a][b] / gaussian(a, b, q)
                require(distribution.get(target_index, Fraction(0)) == expected,
                        "all-time labelled target formula mismatch")
                all_time_assertions += 1
            if epoch == epochs:
                break
            next_distribution = defaultdict(Fraction)
            for current, probability in distribution.items():
                for target, multiplicity in transition_counts[current].items():
                    next_distribution[target] += (
                        probability * Fraction(multiplicity, number_of_maps)
                    )
            distribution = dict(next_distribution)
            quotient_power = matrix_multiply(quotient_power, qmatrix)

    return {
        "q": q,
        "n": n,
        "points": len(points),
        "states": len(states),
        "maps": number_of_maps,
        "updates": number_of_maps * len(states),
        "epochs": epochs,
        "all_time": all_time_assertions,
        "digest": digest.hexdigest(),
    }


def formula_box(q, n):
    qmatrix = quotient_matrix(n, q)
    size = n + 1
    for a in range(size):
        require(sum(qmatrix[a]) == 1, "quotient row is not stochastic")
        require(qmatrix[a][a] == Fraction(1, q ** (a * (n - a))),
                "quotient diagonal mismatch")
        for b in range(size):
            require((qmatrix[a][b] == 0) if b > a else True,
                    "quotient matrix is not lower triangular")
        require(target_count(n, q, a, a) == 1,
                "empty injection product mismatch")
        for b in range(a + 1):
            if a - b > n - a:
                require(qmatrix[a][b] == 0,
                        "impossible rank transition is nonzero")

    full_state_count = sum(gaussian(n, a, q) for a in range(size))
    spectral_multiplicity = Counter()
    for a in range(size):
        spectral_multiplicity[qmatrix[a][a]] += gaussian(n, a, q)
    require(sum(spectral_multiplicity.values()) == full_state_count,
            "full algebraic spectrum does not exhaust labelled states")

    diagonal_groups = defaultdict(list)
    for a in range(size):
        diagonal_groups[qmatrix[a][a]].append(a)
    expected_groups = []
    if n == 0:
        expected_groups.append([0])
    else:
        expected_groups.append([0, n])
        for b in range(1, (n + 1) // 2):
            if b < n - b:
                expected_groups.append([b, n - b])
        if n % 2 == 0:
            expected_groups.append([n // 2])
    require(sorted(sorted(group) for group in diagonal_groups.values()) ==
            sorted(expected_groups), "unexpected diagonal collision")

    direct_pairs = 0
    indirect_pairs = 0
    for eigenvalue, dimensions in diagonal_groups.items():
        base = shifted(qmatrix, eigenvalue)
        nullities = []
        current = identity(size)
        for exponent in range(1, 4):
            current = matrix_multiply(current, base)
            nullities.append(size - rational_rank(current))
        if n == 0:
            require(dimensions == [0] and nullities == [1, 1, 1],
                    "n=0 must have one semisimple endpoint block")
        elif dimensions == [0, n]:
            require(nullities == [2, 2, 2],
                    "endpoint eigenvalue is not two J1 blocks")
            ones = [Fraction(1) for _ in range(size)]
            top_indicator = [Fraction(0) for _ in range(size)]
            top_indicator[n] = 1
            require(row_action(qmatrix, ones) == ones,
                    "constant right endpoint eigenvector failed")
            require(row_action(qmatrix, top_indicator) == top_indicator,
                    "top-state right endpoint eigenvector failed")
            require(ones != top_indicator,
                    "endpoint eigenvectors unexpectedly coincide")
        elif len(dimensions) == 2:
            b, a = dimensions
            require(a == n - b and 1 <= b < n / 2,
                    "noncomplementary repeated eigenvalue")
            require(nullities == [1, 2, 2],
                    "complementary eigenvalue is not one J2 block")
            if qmatrix[a][b] != 0:
                direct_pairs += 1
            else:
                indirect_pairs += 1

            partial = [Fraction(0) for _ in range(size)]
            partial[b] = 1
            for k in range(b + 1, a):
                numerator = sum(qmatrix[k][j] * partial[j] for j in range(k))
                denominator = eigenvalue - qmatrix[k][k]
                require(denominator > 0, "intermediate Jordan denominator not positive")
                require(numerator > 0, "adjacent path failed to force positivity")
                partial[k] = numerator / denominator
                require(partial[k] > 0, "Jordan recursion coordinate not positive")
            obstruction = sum(qmatrix[a][j] * partial[j] for j in range(a))
            require(obstruction > 0, "resonant compatibility obstruction vanished")
            require(qmatrix[a][a - 1] * partial[a - 1] > 0,
                    "adjacent terminal contribution vanished")
        else:
            require(n % 2 == 0 and dimensions == [n // 2],
                    "unexpected simple diagonal group")
            require(nullities == [1, 1, 1],
                    "middle eigenvalue is not one J1 block")

    if n == 0:
        jordan_dimension = 1
    else:
        jordan_dimension = 2 + 2 * ((n - 1) // 2) + (1 if n % 2 == 0 else 0)
    require(jordan_dimension == size, "Jordan inventory does not exhaust quotient")

    means = [Fraction(0) for _ in range(size)]
    for a in range(1, n):
        require(qmatrix[a][a] < 1, "proper state has unit self-loop")
        require(qmatrix[a][a - 1] > 0, "proper state has no adjacent loss")
        means[a] = ((1 + sum(qmatrix[a][b] * means[b] for b in range(a)))
                    / (1 - qmatrix[a][a]))
        require(means[a] > 0, "absorption mean is not positive")
        require(means[a] == 1 + sum(qmatrix[a][b] * means[b]
                                    for b in range(a + 1)),
                "absorption first-step equation failed")

    powers = identity(size)
    previous_cdf = [powers[a][0] for a in range(size)]
    for _ in range(8):
        powers = matrix_multiply(powers, qmatrix)
        current_cdf = [powers[a][0] for a in range(size)]
        for a in range(1, n):
            require(current_cdf[a] >= previous_cdf[a],
                    "absorption CDF decreased")
            require(0 <= current_cdf[a] <= 1,
                    "absorption CDF left probability interval")
        previous_cdf = current_cdf

    if n == 0:
        require(qmatrix == [[Fraction(1)]], "n=0 boundary is not one fixed state")
    if n == 1:
        require(qmatrix == identity(2), "n=1 boundary is not two fixed states")
    if n == 2:
        require(qmatrix[1][0] == Fraction(q - 1, q), "n=2 loss entry mismatch")
        require(qmatrix[1][1] == Fraction(1, q), "n=2 hold entry mismatch")
        require(means[1] == Fraction(q, q - 1), "n=2 mean mismatch")

    return direct_pairs, indirect_pairs, full_state_count


def main():
    print("P173 HOSTILE REVIEW B — INDEPENDENT EXACT AUDIT")
    print("representation=normalized-projective-point incidence bitsets")
    print("literal_strategy=all ambient matrices acting on projective points")
    print("formula_strategy=exact rational quotient powers and nullity growth")

    literal_specs = [(2, n, 6) for n in range(5)] + [(3, n, 5) for n in range(4)]
    literal_results = []
    for q, n, epochs in literal_specs:
        result = literal_box(q, n, epochs)
        literal_results.append(result)
        print(
            "LITERAL "
            f"q={q} n={n} points={result['points']} states={result['states']} "
            f"maps={result['maps']} updates={result['updates']} "
            f"epochs=0..{epochs} alltime_checks={result['all_time']} "
            f"fibre_sha256={result['digest']}"
        )

    q_values = (2, 3, 4, 5, 7, 8, 9, 11)
    boxes = 0
    direct_pairs = 0
    indirect_pairs = 0
    largest_full_lattice = 0
    for q in q_values:
        for n in range(15):
            direct, indirect, full_count = formula_box(q, n)
            boxes += 1
            direct_pairs += direct
            indirect_pairs += indirect
            largest_full_lattice = max(largest_full_lattice, full_count)

    print(f"FORMULA q={','.join(map(str, q_values))} n=0..14 boxes={boxes}")
    print(f"JORDAN complementary_pairs_direct={direct_pairs} "
          f"complementary_pairs_indirect={indirect_pairs}")
    print("ENDPOINT_SENTINEL n=0:J1(1)x1 n>=1:J1(1)x2")
    print(f"MAX_LABELLED_SPECTRAL_CENSUS={largest_full_lattice}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("RESULT=PASS_INTENDED_FORMULAS; MANUSCRIPT_BOUNDARY_AND_SOURCE_GATES_EXTERNAL")


if __name__ == "__main__":
    main()
