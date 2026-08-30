#!/usr/bin/env python3
"""Canonical exact controls for regular Engel dynamics on U_n(F_q).

The program uses literal polynomial-basis finite fields and literal matrix
operations.  It exhausts the lanes listed in ``LANES``; verifies every
restricted image, one-step and iterated fibre, depth layer, filtration-type
indegree, centralizer coset, and triangular matrix equation; checks the
near-regular U_4 counterexample; and byte-checks the exact layer-table
artifact.  Only the Python standard library is used.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
from pathlib import Path


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message="exact assertion failed"):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


class FiniteField:
    """Small field F_p[z]/(modulus), with base-p integer encoding."""

    def __init__(self, p, modulus, label):
        self.p = p
        self.modulus = tuple(modulus)  # low coefficient first, monic
        self.degree = len(self.modulus) - 1
        self.q = p**self.degree
        self.label = label
        AUDIT.check(self.degree >= 1, f"{label}: positive extension degree")
        AUDIT.check(self.modulus[-1] == 1, f"{label}: monic modulus")
        self._add = tuple(
            tuple(self._add_raw(x, y) for y in range(self.q))
            for x in range(self.q)
        )
        self._mul = tuple(
            tuple(self._mul_raw(x, y) for y in range(self.q))
            for x in range(self.q)
        )
        self._neg = tuple(self._neg_raw(x) for x in range(self.q))

    def digits(self, value, length=None):
        if length is None:
            length = self.degree
        out = []
        for _ in range(length):
            out.append(value % self.p)
            value //= self.p
        return out

    def encode(self, digits):
        value = 0
        place = 1
        for digit in digits:
            value += (digit % self.p) * place
            place *= self.p
        return value

    def _add_raw(self, left, right):
        return self.encode(
            (x + y) % self.p
            for x, y in zip(self.digits(left), self.digits(right))
        )

    def _neg_raw(self, value):
        return self.encode((-x) % self.p for x in self.digits(value))

    def _mul_raw(self, left, right):
        x = self.digits(left)
        y = self.digits(right)
        raw = [0] * (2 * self.degree - 1)
        for i, xi in enumerate(x):
            for j, yj in enumerate(y):
                raw[i + j] = (raw[i + j] + xi * yj) % self.p
        for degree in range(len(raw) - 1, self.degree - 1, -1):
            coefficient = raw[degree] % self.p
            if coefficient:
                shift = degree - self.degree
                for j, modulus_coefficient in enumerate(self.modulus):
                    raw[shift + j] = (
                        raw[shift + j] - coefficient * modulus_coefficient
                    ) % self.p
        return self.encode(raw[: self.degree])

    def add(self, left, right):
        return self._add[left][right]

    def neg(self, value):
        return self._neg[value]

    def sub(self, left, right):
        return self.add(left, self.neg(right))

    def mul(self, left, right):
        return self._mul[left][right]

    def power(self, value, exponent):
        result = 1
        base = value
        while exponent:
            if exponent & 1:
                result = self.mul(result, base)
            base = self.mul(base, base)
            exponent //= 2
        return result

    def inverse(self, value):
        AUDIT.check(value != 0, f"{self.label}: inverse of zero requested")
        return self.power(value, self.q - 2)

    def audit_field(self):
        for x in range(self.q):
            AUDIT.check(self.add(x, 0) == x, f"{self.label}: additive identity")
            AUDIT.check(self.add(x, self.neg(x)) == 0, f"{self.label}: additive inverse")
            AUDIT.check(self.mul(x, 1) == x, f"{self.label}: multiplicative identity")
            AUDIT.check(self.power(x, self.q) == x, f"{self.label}: Frobenius law")
            if x:
                AUDIT.check(self.mul(x, self.inverse(x)) == 1, f"{self.label}: inverse")
        for x in range(self.q):
            for y in range(self.q):
                AUDIT.check(self.add(x, y) == self.add(y, x), f"{self.label}: add commutes")
                AUDIT.check(self.mul(x, y) == self.mul(y, x), f"{self.label}: mul commutes")
                for z in range(self.q):
                    AUDIT.check(
                        self.mul(x, self.add(y, z))
                        == self.add(self.mul(x, y), self.mul(x, z)),
                        f"{self.label}: distributivity",
                    )


FIELDS = (
    FiniteField(2, (0, 1), "F_2"),
    FiniteField(3, (0, 1), "F_3"),
    FiniteField(2, (1, 1, 1), "F_4"),
    FiniteField(5, (0, 1), "F_5"),
    FiniteField(2, (1, 1, 0, 1), "F_8"),
    FiniteField(3, (1, 0, 1), "F_9"),
)

LANES = {
    "F_2": 6,
    "F_3": 4,
    "F_4": 4,
    "F_5": 4,
    "F_8": 3,
    "F_9": 3,
}


def identity(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def matrix_add(left, right, field):
    n = len(left)
    return tuple(
        tuple(field.add(left[i][j], right[i][j]) for j in range(n))
        for i in range(n)
    )


def scalar_matrix_multiple(scalar, matrix, field):
    return tuple(
        tuple(field.mul(scalar, entry) for entry in row)
        for row in matrix
    )


def multiply(left, right, field):
    n = len(left)
    return tuple(
        tuple(
            sum_in_field(
                (field.mul(left[i][h], right[h][j]) for h in range(n)), field
            )
            for j in range(n)
        )
        for i in range(n)
    )


def sum_in_field(values, field):
    total = 0
    for value in values:
        total = field.add(total, value)
    return total


@lru_cache(maxsize=None)
def inverse(matrix, field):
    """Inverse of an upper unitriangular matrix by its nilpotent series."""
    n = len(matrix)
    unit = identity(n)
    nilpotent = tuple(
        tuple(field.sub(matrix[i][j], unit[i][j]) for j in range(n))
        for i in range(n)
    )
    answer = unit
    power = unit
    for exponent in range(1, n):
        power = multiply(power, nilpotent, field)
        coefficient = field.neg(1) if exponent % 2 else 1
        answer = matrix_add(answer, scalar_matrix_multiple(coefficient, power, field), field)
    AUDIT.check(multiply(matrix, answer, field) == unit, "matrix inverse: right identity")
    AUDIT.check(multiply(answer, matrix, field) == unit, "matrix inverse: left identity")
    return answer


def regular_unipotent(n):
    return tuple(
        tuple(int(i == j or j == i + 1) for j in range(n))
        for i in range(n)
    )


def regular_nilpotent(n):
    return tuple(
        tuple(int(j == i + 1) for j in range(n))
        for i in range(n)
    )


@lru_cache(maxsize=None)
def engel(matrix, regular, field):
    """Return [matrix,regular]=matrix^-1 regular^-1 matrix regular."""
    return multiply(
        multiply(
            multiply(inverse(matrix, field), inverse(regular, field), field),
            matrix,
            field,
        ),
        regular,
        field,
    )


def iterate(matrix, regular, field, times):
    for _ in range(times):
        matrix = engel(matrix, regular, field)
    return matrix


def gamma_elements(n, field, level):
    coordinates = [
        (i, j) for i in range(n) for j in range(i + level, n)
    ]
    for values in product(range(field.q), repeat=len(coordinates)):
        matrix = [list(row) for row in identity(n)]
        for (i, j), value in zip(coordinates, values):
            matrix[i][j] = value
        yield tuple(tuple(row) for row in matrix)


def in_gamma(matrix, level):
    n = len(matrix)
    return all(
        matrix[i][j] == 0
        for i in range(n)
        for j in range(i + 1, min(n, i + level))
    )


def filtration_level(matrix):
    n = len(matrix)
    active = [
        j - i
        for i in range(n)
        for j in range(i + 1, n)
        if matrix[i][j] != 0
    ]
    return min(active) if active else n


def literal_depth(matrix, regular, field):
    unit = identity(len(matrix))
    time = 0
    while matrix != unit:
        matrix = engel(matrix, regular, field)
        time += 1
        AUDIT.check(time < len(unit), "orbit exceeded sharp nilpotent bound")
    return time


def cumulative_exponent(n, level, time):
    return sum(n - j for j in range(level, level + time))


def predicted_layer(n, q, level, time):
    if time == 0:
        return 1
    return (
        q ** (n - level - time + 1) - 1
    ) * q ** cumulative_exponent(n, level, time - 1)


def expected_gamma_size(n, q, level):
    return q ** sum(n - j for j in range(level, n))


def is_regular_centralizer_form(matrix, level):
    """Test I+a_level N^level+...+a_(n-1)N^(n-1)."""
    n = len(matrix)
    for offset in range(1, n):
        diagonal = [matrix[i][i + offset] for i in range(n - offset)]
        if offset < level:
            if any(diagonal):
                return False
        elif any(value != diagonal[0] for value in diagonal):
            return False
    return True


def difference_map(vector, field):
    return tuple(field.sub(vector[i], vector[i + 1]) for i in range(len(vector) - 1))


def audit_difference_maps(field, maximum_length):
    for length in range(1, maximum_length + 1):
        counts = Counter(
            difference_map(vector, field)
            for vector in product(range(field.q), repeat=length)
        )
        AUDIT.check(len(counts) == field.q ** (length - 1), "difference map: onto")
        for fibre_size in counts.values():
            AUDIT.check(fibre_size == field.q, "difference map: one free constant")


def audit_regular_case(n, field, stats):
    q = field.q
    unit = identity(n)
    regular = regular_unipotent(n)
    phase = tuple(gamma_elements(n, field, 1))
    stats["phase_states"] += len(phase)
    AUDIT.check(len(phase) == q ** (n * (n - 1) // 2), "phase cardinality")

    # The n=1 boundary is a singleton fixed system.
    if n == 1:
        AUDIT.check(phase == (unit,), "U_1 is a singleton")
        AUDIT.check(engel(unit, regular, field) == unit, "U_1 update")
        AUDIT.check(literal_depth(unit, regular, field) == 0, "U_1 depth")
        return

    full_image = Counter(engel(x, regular, field) for x in phase)
    full_histogram = Counter()
    for x in phase:
        y = engel(x, regular, field)
        full_histogram[literal_depth(x, regular, field)] += 1
        AUDIT.check(in_gamma(y, 2), "full image lies in gamma_2")
        AUDIT.check(
            multiply(x, regular, field)
            == multiply(multiply(regular, x, field), y, field),
            "triangular equation XJ=JXY",
        )
    expected_full_histogram = Counter(
        {
            time: predicted_layer(n, q, 1, time)
            for time in range(0, n)
        }
    )
    AUDIT.check(full_histogram == expected_full_histogram, "full depth histogram")
    AUDIT.check(max(full_histogram) == n - 1, "sharp maximum depth")
    AUDIT.check(
        full_histogram[n - 1] == (q - 1) * q ** (n * (n - 1) // 2 - 1),
        "deepest shell",
    )
    for y in phase:
        expected = q ** (n - 1) if in_gamma(y, 2) else 0
        AUDIT.check(full_image[y] == expected, "full functional-graph indegree")

    for period in range(1, n + 2):
        for x in phase:
            AUDIT.check(
                (iterate(x, regular, field, period) == x) == (x == unit),
                "unique periodic point",
            )

    for level in range(1, n):
        domain = tuple(gamma_elements(n, field, level))
        target = tuple(gamma_elements(n, field, level + 1))
        target_set = set(target)
        buckets = defaultdict(list)
        for x in domain:
            y = engel(x, regular, field)
            buckets[y].append(x)
            AUDIT.check(in_gamma(y, level + 1), "restricted filtration increase")
        AUDIT.check(set(buckets) == target_set, "restricted surjectivity")
        AUDIT.check(
            len(domain) == expected_gamma_size(n, q, level),
            "restricted phase cardinality",
        )
        for y in target:
            AUDIT.check(len(buckets[y]) == q ** (n - level), "one-step fibre")
        stats["restricted_surjections"] += 1

        centralizer = []
        for x in domain:
            commutes = multiply(x, regular, field) == multiply(regular, x, field)
            prescribed = is_regular_centralizer_form(x, level)
            AUDIT.check(commutes == prescribed, "regular centralizer form")
            if commutes:
                centralizer.append(x)
        AUDIT.check(len(centralizer) == q ** (n - level), "centralizer cardinality")

        # Equality fibres are left centralizer cosets C_{gamma_k}(J) X.
        for y in target:
            representative = buckets[y][0]
            left_coset = {
                multiply(c, representative, field) for c in centralizer
            }
            AUDIT.check(left_coset == set(buckets[y]), "left-coset fibre orientation")

        depth_histogram = Counter(
            literal_depth(x, regular, field) for x in domain
        )
        expected_histogram = Counter(
            {
                time: predicted_layer(n, q, level, time)
                for time in range(0, n - level + 1)
            }
        )
        AUDIT.check(depth_histogram == expected_histogram, "restricted exact layers")

        for time in range(0, n - level + 1):
            image_counts = Counter(
                iterate(x, regular, field, time) for x in domain
            )
            iterated_target = tuple(gamma_elements(n, field, level + time))
            AUDIT.check(
                set(image_counts) == set(iterated_target),
                "iterated restricted image",
            )
            expected_fibre = q ** cumulative_exponent(n, level, time)
            for y in iterated_target:
                AUDIT.check(
                    image_counts[y] == expected_fibre,
                    "iterated restricted fibre",
                )
            cumulative = sum(
                count for depth, count in depth_histogram.items() if depth <= time
            )
            AUDIT.check(cumulative == expected_fibre, "depth CDF equals root fibre")
            stats["iterated_profiles"] += 1

    # Predecessors split by the exact source filtration stratum.
    for level in range(1, n):
        stratum = tuple(
            x for x in gamma_elements(n, field, level)
            if not in_gamma(x, level + 1)
        )
        counts = Counter(engel(x, regular, field) for x in stratum)
        for y in phase:
            if level == n - 1:
                expected = q - 1 if y == unit else 0
            else:
                expected = (
                    q ** (n - level) * int(in_gamma(y, level + 1))
                    - q ** (n - level - 1) * int(in_gamma(y, level + 2))
                )
            AUDIT.check(counts[y] == expected, "filtration-stratum indegree")


def nonregular_unipotent(n):
    AUDIT.check(n == 4, "the counterexample is four-dimensional")
    matrix = [list(row) for row in identity(n)]
    matrix[0][1] = 1
    matrix[2][3] = 1
    return tuple(tuple(row) for row in matrix)


def nonregular_centralizer_condition(matrix):
    return matrix[1][2] == 0 and matrix[1][3] == matrix[0][2]


def audit_nonregular_counterexample(field, stats):
    n = 4
    q = field.q
    phase = tuple(gamma_elements(n, field, 1))
    gamma_two = set(gamma_elements(n, field, 2))
    regular_missing_middle = nonregular_unipotent(n)
    centralizer = []
    images = Counter()
    for x in phase:
        commutes = (
            multiply(x, regular_missing_middle, field)
            == multiply(regular_missing_middle, x, field)
        )
        AUDIT.check(
            commutes == nonregular_centralizer_condition(x),
            "near-regular centralizer equations",
        )
        if commutes:
            centralizer.append(x)
        y = engel(x, regular_missing_middle, field)
        AUDIT.check(in_gamma(y, 2), "near-regular image still lies in gamma_2")
        images[y] += 1
    AUDIT.check(len(centralizer) == q**4, "near-regular centralizer has q^4 points")
    AUDIT.check(len(images) == q**2, "near-regular image has q^2 points")
    AUDIT.check(set(images) != gamma_two, "near-regular image is not gamma_2")
    for fibre_size in images.values():
        AUDIT.check(fibre_size == q**4, "near-regular fibres have q^4 points")
    stats["counterexample_states"] += len(phase)


def build_layer_table():
    rows = [
        "q\tn\tk\tt\trestricted_phase_size\tcumulative_depth_le_t\texact_depth_t"
    ]
    for q, n in ((2, 6), (3, 5), (4, 4)):
        for level in range(1, n):
            phase_size = expected_gamma_size(n, q, level)
            for time in range(0, n - level + 1):
                cumulative = q ** cumulative_exponent(n, level, time)
                exact = predicted_layer(n, q, level, time)
                rows.append(
                    f"{q}\t{n}\t{level}\t{time}\t{phase_size}\t{cumulative}\t{exact}"
                )
    return "\n".join(rows) + "\n"


def main():
    stats = Counter()
    for field in FIELDS:
        field.audit_field()
        audit_difference_maps(field, LANES[field.label])
        for n in range(1, LANES[field.label] + 1):
            audit_regular_case(n, field, stats)

    for label in ("F_2", "F_3", "F_4", "F_5"):
        field = next(candidate for candidate in FIELDS if candidate.label == label)
        audit_nonregular_counterexample(field, stats)

    table_path = Path(__file__).with_name("exact_layer_table.tsv")
    table_bytes = table_path.read_text(encoding="utf-8")
    expected_table = build_layer_table()
    AUDIT.check(table_bytes == expected_table, "exact layer-table artifact")
    table_rows = len(expected_table.rstrip("\n").splitlines()) - 1

    print("regular Engel exact control: PASS")
    print(f"assertions={AUDIT.assertions:,}")
    print("fields=F_2,F_3,F_4,F_5,F_8,F_9")
    print(f"exhaustive_phase_states={stats['phase_states']:,}")
    print(f"restricted_surjections={stats['restricted_surjections']}")
    print(f"iterated_fibre_profiles={stats['iterated_profiles']}")
    print(f"nonregular_counterexample_states={stats['counterexample_states']:,}")
    print(f"exact_layer_table_rows={table_rows}")
    print("claim_ceiling=fixed_J_equals_I_plus_regular_shift")


if __name__ == "__main__":
    main()
