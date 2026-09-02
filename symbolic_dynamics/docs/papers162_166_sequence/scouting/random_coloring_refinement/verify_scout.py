#!/usr/bin/env python3
"""Independent exhaustive verifier for random q-colour refinement (RCR).

No author or repository module is imported.  Set partitions are generated as
restricted-growth strings.  Literal colour histories are compared with the
signature theorem, every source/target transition, absorption CDF and mean,
block occupancy, zeta-basis eigenrelations, and target-sensitive weighted
all-source history polynomials.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(maxsize=None)
def partitions(n):
    if n == 0:
        return ((),)
    out = []

    def visit(prefix, maximum):
        if len(prefix) == n:
            out.append(tuple(prefix))
            return
        for value in range(maximum + 2):
            prefix.append(value)
            visit(prefix, max(maximum, value))
            prefix.pop()

    visit([0], 0)
    return tuple(out)


def canonical(values):
    names = {}
    out = []
    for value in values:
        if value not in names:
            names[value] = len(names)
        out.append(names[value])
    return tuple(out)


def meet(left, right):
    return canonical(tuple(zip(left, right)))


def kernel(values):
    return canonical(values)


def blocks(pi):
    out = [[] for _ in range(number_blocks(pi))]
    for i, label in enumerate(pi):
        out[label].append(i)
    return tuple(tuple(b) for b in out)


def block_sizes(pi):
    return tuple(len(b) for b in blocks(pi))


def number_blocks(pi):
    return 0 if not pi else max(pi) + 1


def pair_count(pi):
    return sum(size * (size - 1) // 2 for size in block_sizes(pi))


def refines(fine, coarse):
    assignment = {}
    for f, c in zip(fine, coarse):
        if f in assignment and assignment[f] != c:
            return False
        assignment[f] = c
    return True


def falling(q, k):
    answer = 1
    for j in range(k):
        answer *= q - j
    return answer


def stirling2(n, k):
    table = [[0] * (k + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            table[i][j] = table[i - 1][j - 1] + j * table[i - 1][j]
    return table[n][k]


def transition_count(source, target, Q):
    if not refines(target, source):
        return 0
    target_labels = defaultdict(set)
    for s, t in zip(source, target):
        target_labels[s].add(t)
    answer = 1
    for labels in target_labels.values():
        answer *= falling(Q, len(labels))
    return answer


def signature_partition(history, n):
    if not history:
        return (0,) * n
    signatures = tuple(tuple(colour[i] for colour in history)
                       for i in range(n))
    return kernel(signatures)


def apply_history(source, history):
    current = source
    for colour in history:
        current = meet(current, kernel(colour))
    return current


def histories(n, q, t):
    if t == 0:
        yield ()
        return
    for flat in product(range(q), repeat=n * t):
        yield tuple(tuple(flat[j * n:(j + 1) * n]) for j in range(t))


def literal_matrix(n, q, t):
    parts = partitions(n)
    counts = {source: Counter() for source in parts}
    for history in histories(n, q, t):
        sig = signature_partition(history, n)
        for source in parts:
            direct = meet(source, sig)
            iterative = apply_history(source, history)
            check(direct == iterative,
                  f"signature failure n={n} q={q} t={t} source={source}")
            counts[source][direct] += 1
    return counts


def occupancy_distribution(source, Q):
    result = Counter({0: 1})
    for size in block_sizes(source):
        one = Counter({k: falling(Q, k) * stirling2(size, k)
                       for k in range(1, min(size, Q) + 1)})
        updated = Counter()
        for a, value_a in result.items():
            for b, value_b in one.items():
                updated[a + b] += value_a * value_b
        result = updated
    return result


def poly_mul(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def falling_polynomial(size):
    out = [1]
    for j in range(size):
        out = poly_mul(out, [-j, 1])
    return out


def absorption_polynomial(source):
    out = [1]
    for size in block_sizes(source):
        out = poly_mul(out, falling_polynomial(size))
    return out


def absorption_count(source, Q):
    answer = 1
    for size in block_sizes(source):
        answer *= falling(Q, size)
    return answer


def expectation_closed(source, q):
    n = len(source)
    coefficients = absorption_polynomial(source)
    answer = Fraction(0)
    for j, coefficient in enumerate(coefficients[:-1]):
        answer -= Fraction(coefficient, 1) / (1 - Fraction(q ** j, q ** n))
    return answer


def one_step_formula_matrix(n, q):
    return {source: Counter({target: transition_count(source, target, q)
                             for target in partitions(n)
                             if transition_count(source, target, q)})
            for source in partitions(n)}


def expectation_recursive(n, q):
    matrix = one_step_formula_matrix(n, q)
    discrete = tuple(range(n))
    means = {discrete: Fraction(0)}
    ordered = sorted(partitions(n), key=number_blocks, reverse=True)
    denominator = q ** n
    for source in ordered:
        if source == discrete:
            continue
        stay = matrix[source][source]
        numerator = Fraction(1)
        for target, count in matrix[source].items():
            if target != source:
                check(number_blocks(target) > number_blocks(source),
                      f"non-refining transition n={n} q={q}")
                numerator += Fraction(count, denominator) * means[target]
        means[source] = numerator / (1 - Fraction(stay, denominator))
    return means, matrix


def source_from_grouping(target, grouping):
    return canonical(tuple(grouping[label] for label in target))


def weighted_history_formula(target, Q):
    """Counter for (new merged pairs, source blocks, source size profile)."""
    k = number_blocks(target)
    result = Counter()
    for grouping in partitions(k):
        source = source_from_grouping(target, grouping)
        group_sizes = Counter(grouping)
        history_count = 1
        for size in group_sizes.values():
            history_count *= falling(Q, size)
        key = (pair_count(source) - pair_count(target),
               number_blocks(source), tuple(sorted(block_sizes(source))))
        result[key] += history_count
    return +result


def weighted_history_actual(target, Q, matrix):
    result = Counter()
    for source in partitions(len(target)):
        count = matrix[source][target]
        if count:
            check(refines(target, source), "positive impossible transition")
            key = (pair_count(source) - pair_count(target),
                   number_blocks(source), tuple(sorted(block_sizes(source))))
            result[key] += count
    return +result


def exact_box(n, q, t):
    parts = partitions(n)
    Q = q ** t
    total_histories = Q ** n
    matrix = literal_matrix(n, q, t)
    discrete = tuple(range(n))
    nonzero = 0
    max_column = 0
    column_sums = Counter()
    for source in parts:
        check(sum(matrix[source].values()) == total_histories,
              f"row mass n={n} q={q} t={t} source={source}")
        for target in parts:
            expected = transition_count(source, target, Q)
            check(matrix[source][target] == expected,
                  f"transition n={n} q={q} t={t} {source}->{target}")
            nonzero += int(expected > 0)
            column_sums[target] += expected
        check(matrix[source][discrete] == absorption_count(source, Q),
              f"absorption CDF numerator n={n} q={q} t={t}")
        actual_blocks = Counter()
        for target, count in matrix[source].items():
            actual_blocks[number_blocks(target)] += count
        check(actual_blocks == occupancy_distribution(source, Q),
              f"occupancy law n={n} q={q} t={t} source={source}")
    for target in parts:
        actual = weighted_history_actual(target, Q, matrix)
        expected = weighted_history_formula(target, Q)
        check(actual == expected,
              f"weighted target history n={n} q={q} t={t} target={target}")
        max_column = max(max_column, column_sums[target])
    return (f"BOX n={n} q={q} t={t} partitions={len(parts)} Q={Q} "
            f"histories={total_histories} nonzero={nonzero} "
            f"maxColumn={max_column}")


def spectral_and_mean_controls():
    lines = []
    for n in range(1, 7):
        for q in (2, 3, 5):
            means, matrix = expectation_recursive(n, q)
            denominator = q ** n
            for source in partitions(n):
                check(means[source] == expectation_closed(source, q),
                      f"mean n={n} q={q} source={source}")
                coefficients = absorption_polynomial(source)
                check(sum(coefficients) == absorption_count(source, 1),
                      f"absorption polynomial n={n} q={q}")
            # Check every zeta-basis eigenrelation using literal one-step
            # transition counts reconstructed independently by colour kernels.
            literal = literal_matrix(n, q, 1)
            check(literal == matrix, f"one-step matrix n={n} q={q}")
            multiplicities = Counter(number_blocks(rho) for rho in partitions(n))
            for k in range(1, n + 1):
                check(multiplicities[k] == stirling2(n, k),
                      f"Stirling multiplicity n={n} q={q} k={k}")
            for rho in partitions(n):
                eigen_numerator = q ** number_blocks(rho)
                for source in partitions(n):
                    left = sum(count for target, count in literal[source].items()
                               if refines(rho, target))
                    right = eigen_numerator if refines(rho, source) else 0
                    check(left == right,
                          f"zeta eigenrelation n={n} q={q} rho={rho}")
            spectrum = ",".join(
                f"{q}^{k-n}:{stirling2(n,k)}" for k in range(1, n + 1))
            top = (0,) * n
            lines.append(f"SPECTRUM n={n} q={q} {spectrum} "
                         f"Etop={means[top]}")
    return lines


def target_sensitive_witnesses():
    lines = []
    for Q in (2, 4, 9):
        sigma31 = (0, 0, 0, 1)
        sigma22 = (0, 0, 1, 1)
        p31 = weighted_history_formula(sigma31, Q)
        p22 = weighted_history_formula(sigma22, Q)
        check(sum(p31.values()) == sum(p22.values()),
              f"unweighted column should depend only on k Q={Q}")
        check(p31 != p22, f"pair-weight target sensitivity Q={Q}")
        # Project to (new pair exponent, source-block count) for a compact line.
        def project(poly):
            out = Counter()
            for (pairs, count, _profile), coefficient in poly.items():
                out[(pairs, count)] += coefficient
            return ";".join(f"u^{p}v^{b}:{out[p,b]}" for p, b in sorted(out))
        lines.append(f"WITNESS Q={Q} sizes31={project(p31)} "
                     f"sizes22={project(p22)}")
    return lines


def boundary_controls():
    # q=1 never splits a non-discrete block, showing why q>=2 is required.
    source = (0, 0, 1)
    history = ((0, 0, 0),) * 4
    check(apply_history(source, history) == source, "q=1 boundary")
    # t=0 is identity for every source, including non-discrete sources.
    for n in range(1, 7):
        for source in partitions(n):
            check(apply_history(source, ()) == source, f"t=0 boundary n={n}")
            check(transition_count(source, source, 1) == 1,
                  f"t=0 identity count n={n}")
    return ["BOUNDARY q=1 nonsplitting (q>=2 essential)",
            "BOUNDARY t=0 identity on every partition"]


def main():
    print("RCR INDEPENDENT EXACT AUDIT")
    print("domain n>=1 q>=2; HOLD_EXTERNAL")
    boxes = [
        (1, 2, 0), (2, 2, 0), (2, 2, 1), (2, 2, 2),
        (3, 2, 1), (3, 2, 2), (3, 2, 3),
        (4, 2, 1), (4, 2, 2), (4, 2, 3),
        (5, 2, 1), (5, 2, 2),
        (3, 3, 1), (3, 3, 2), (3, 3, 3),
        (4, 3, 1), (4, 3, 2), (5, 3, 1),
    ]
    literal_pairs = 0
    for n, q, t in boxes:
        print(exact_box(n, q, t))
        literal_pairs += len(partitions(n)) * (q ** (n * t))
    for line in spectral_and_mean_controls():
        print(line)
    for line in target_sensitive_witnesses():
        print(line)
    for line in boundary_controls():
        print(line)
    print(f"boxes={len(boxes)} literal_source_histories={literal_pairs}")
    print(f"assertions={ASSERTIONS}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
