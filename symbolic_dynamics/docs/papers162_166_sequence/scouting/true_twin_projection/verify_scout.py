#!/usr/bin/env python3
"""Independent exhaustive verifier for true-twin projection.

Graphs are edge bitmasks.  The literal side constructs closed neighborhoods
and their equality classes.  The formula side uses partition-lattice Mobius
inversion; a third route enumerates co-point-determining quotient graphs.
Only the Python standard library is used.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from math import factorial


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(maxsize=None)
def edges(n):
    return tuple((i, j) for i in range(n) for j in range(i + 1, n))


def closed_neighborhoods(mask, n):
    neighborhoods = [1 << i for i in range(n)]
    bit = 1
    for i, j in edges(n):
        if mask & bit:
            neighborhoods[i] |= 1 << j
            neighborhoods[j] |= 1 << i
        bit <<= 1
    return tuple(neighborhoods)


def open_neighborhoods(mask, n):
    """Separate adjacency-row implementation for the complement route."""
    neighborhoods = [0] * n
    for position, (i, j) in enumerate(edges(n)):
        if mask & (1 << position):
            neighborhoods[i] |= 1 << j
            neighborhoods[j] |= 1 << i
    return tuple(neighborhoods)


def twin_partition(mask, n):
    classes = {}
    for vertex, neighborhood in enumerate(closed_neighborhoods(mask, n)):
        classes.setdefault(neighborhood, []).append(vertex)
    return tuple(tuple(block) for block in sorted(classes.values(), key=lambda b: b[0]))


@lru_cache(maxsize=None)
def cluster_mask(partition, n):
    index = {edge: position for position, edge in enumerate(edges(n))}
    mask = 0
    for block in partition:
        for p, i in enumerate(block):
            for j in block[p + 1 :]:
                mask |= 1 << index[(min(i, j), max(i, j))]
    return mask


def cluster_graph(mask, n):
    """Literal component test: every connected component is complete."""
    neighborhoods = closed_neighborhoods(mask, n)
    unseen = (1 << n) - 1
    while unseen:
        first = (unseen & -unseen).bit_length() - 1
        component = 0
        frontier = 1 << first
        while frontier:
            component |= frontier
            expanded = 0
            scan = frontier
            while scan:
                bit = scan & -scan
                vertex = bit.bit_length() - 1
                expanded |= neighborhoods[vertex]
                scan ^= bit
            frontier = expanded & ~component
        for vertex in range(n):
            if component & (1 << vertex):
                if neighborhoods[vertex] != component:
                    return False
        unseen &= ~component
    return True


@lru_cache(maxsize=None)
def set_partitions(n):
    if n == 0:
        return ((),)
    answer = []
    for partition in set_partitions(n - 1):
        for position in range(len(partition)):
            blocks = list(partition)
            blocks[position] = blocks[position] + (n - 1,)
            answer.append(tuple(blocks))
        answer.append(partition + ((n - 1,),))
    return tuple(answer)


def mobius_from_bottom(partition):
    value = 1
    for block in partition:
        value *= (-1) ** (len(block) - 1) * factorial(len(block) - 1)
    return value


def poly_mul_binomial(polynomial, exponent):
    answer = Counter(polynomial)
    for degree, coefficient in polynomial.items():
        answer[degree + exponent] += coefficient
    return answer


@lru_cache(maxsize=None)
def mobius_fibre(sizes):
    """The proposed edge-weighted fibre polynomial."""
    k = len(sizes)
    answer = Counter()
    for gamma in set_partitions(k):
        mu = mobius_from_bottom(gamma)
        totals = [sum(sizes[i] for i in block) for block in gamma]
        internal = sum(s * (s - 1) // 2 for s in totals)
        term = Counter({internal: mu})
        for c in range(len(totals)):
            for d in range(c + 1, len(totals)):
                term = poly_mul_binomial(term, totals[c] * totals[d])
        answer.update(term)
    return +answer


def co_point_determining(mask, n):
    # H has distinct closed neighborhoods iff its complement has distinct
    # open neighborhoods.  This avoids reusing the literal tau routine.
    complement = ((1 << len(edges(n))) - 1) ^ mask
    neighborhoods = open_neighborhoods(complement, n)
    return len(set(neighborhoods)) == n


def quotient_fibre(sizes):
    """Third route: directly enumerate true-twin-free quotient graphs."""
    k = len(sizes)
    internal = sum(s * (s - 1) // 2 for s in sizes)
    answer = Counter()
    for mask in range(1 << len(edges(k))):
        if not co_point_determining(mask, k):
            continue
        exponent = internal
        for position, (i, j) in enumerate(edges(k)):
            if mask & (1 << position):
                exponent += sizes[i] * sizes[j]
        answer[exponent] += 1
    return +answer


def bell(n):
    return len(set_partitions(n))


def poly_text(polynomial):
    pieces = []
    for degree in sorted(polynomial):
        coefficient = polynomial[degree]
        if degree == 0:
            monomial = "1"
        elif degree == 1:
            monomial = "z"
        else:
            monomial = f"z^{degree}"
        pieces.append(monomial if coefficient == 1 else f"{coefficient}*{monomial}")
    return " + ".join(pieces) if pieces else "0"


def main():
    summaries = []
    q_values = []

    # Structural formula route, including the empty and singleton boundaries.
    for k in range(0, 8):
        unit_sizes = (1,) * k
        mobius = mobius_fibre(unit_sizes)
        quotient = quotient_fibre(unit_sizes)
        check(mobius == quotient, f"unit quotient polynomial k={k}")
        q_values.append(sum(quotient.values()))
        check(q_values[-1] == sum(mobius.values()), f"quotient total k={k}")

    # Full literal enumeration on every labelled graph through n=7.
    for n in range(0, 8):
        actual = defaultdict(Counter)
        fixed_count = 0
        graph_count = 1 << len(edges(n))
        for partition in set_partitions(n):
            target = cluster_mask(partition, n)
            check(twin_partition(target, n) == partition, f"idempotence n={n}, partition={partition}")
            check(cluster_graph(target, n), f"target is cluster graph n={n}, partition={partition}")
        for mask in range(graph_count):
            partition = twin_partition(mask, n)
            target = cluster_mask(partition, n)
            is_fixed = mask == target
            if is_fixed:
                fixed_count += 1
            actual[partition][mask.bit_count()] += 1

        check(len(actual) == bell(n), f"image/Bell n={n}")
        check(fixed_count == bell(n), f"fixed/Bell n={n}")
        check(sum(sum(poly.values()) for poly in actual.values()) == graph_count, f"mass n={n}")

        cache = {}
        for partition in set_partitions(n):
            sizes = tuple(sorted((len(block) for block in partition), reverse=True))
            if sizes not in cache:
                formula = mobius_fibre(sizes)
                quotient = quotient_fibre(sizes)
                check(formula == quotient, f"Mobius/quotient n={n}, sizes={sizes}")
                cache[sizes] = formula
            expected = cache[sizes]
            observed = +actual.get(partition, Counter())
            check(observed == expected, f"literal/formula n={n}, partition={partition}")
            check(all(c > 0 for c in expected.values()), f"positivity n={n}, partition={partition}")
            k = len(partition)
            check(sum(expected.values()) == q_values[k], f"size-independent total n={n}, partition={partition}")
            valuation = min(expected) if expected else None
            forced = sum(s * (s - 1) // 2 for s in sizes)
            check(valuation == forced, f"valuation n={n}, partition={partition}")
            check(expected[forced] == 1, f"unique minimum n={n}, partition={partition}")

        summaries.append((n, graph_count, len(actual), fixed_count))

    # Target-statistic recovery checkpoints.
    for n in range(1, 8):
        for partition in set_partitions(n):
            sizes = tuple(len(block) for block in partition)
            polynomial = mobius_fibre(tuple(sorted(sizes, reverse=True)))
            valuation = min(polynomial)
            sum_squares = n + 2 * valuation
            check(sum_squares == sum(s * s for s in sizes), f"square recovery n={n}, sizes={sizes}")

    # Strict increase makes Phi(1) recover k, except q_1=q_2; valuation resolves it.
    check(q_values[:4] == [1, 1, 1, 4], "small quotient counts")
    for k in range(2, 7):
        check(q_values[k + 1] > q_values[k], f"strict quotient growth k={k}")
    for n in range(2, 30):
        check(n * (n - 1) // 2 > (n - 1) * (n - 2) // 2, f"k=1/2 valuation split n={n}")

    example = mobius_fibre((2, 1, 1))
    check(example == Counter({1: 1, 4: 2, 5: 1}), "(2,1,1) example")

    print("TRUE-TWIN PROJECTION -- INDEPENDENT EXACT SCOUT")
    print("literal map             tau(G): clique graph of equal closed neighborhoods")
    print("exhaustive box          every labelled simple graph, 0 <= n <= 7")
    print("three-way fibre check   literal = Mobius formula = quotient enumeration PASS")
    print("idempotence/image/fixed PASS; image and fixed count Bell(n)")
    for n, states, images, fixed_count in summaries:
        print(f"n={n} states={states:8d} image={images:4d} fixed={fixed_count:4d}")
    print("co-point totals q_k     " + ",".join(str(value) for value in q_values))
    print("example sizes 2,1,1    " + poly_text(example))
    print(f"ASSERTIONS              {ASSERTIONS}")
    print("MATHEMATICAL STATUS     PASS")
    print("SELECTION DECISION      KILL")
    print("EXTERNAL STATUS         HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
