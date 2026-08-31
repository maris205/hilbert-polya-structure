#!/usr/bin/env python3
"""Exact breadth pilots for the P127--P131 root/cross-family lane.

The twenty-two maps below are fixed before their functional-graph summaries
are computed.  This program is a falsification and triage instrument only.
All arithmetic is exact and every carrier slice is exhausted.
"""

from __future__ import annotations

from collections import Counter
from itertools import permutations, product
from math import isqrt


ASSERTIONS = 0


def check(condition: bool, message: str = "") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message or f"assertion {ASSERTIONS} failed")


def analyse(states, update):
    states = tuple(states)
    state_set = set(states)
    check(len(states) == len(state_set))
    image = {}
    indegree = Counter()
    for state in states:
        target = update(state)
        check(target in state_set)
        image[state] = target
        indegree[target] += 1
    max_tail = 0
    periods = set()
    fixed = 0
    for state in states:
        fixed += image[state] == state
        seen = {}
        x = state
        while x not in seen:
            seen[x] = len(seen)
            x = image[x]
        tail = seen[x]
        period = len(seen) - tail
        check(period >= 1)
        y = x
        for _ in range(period):
            y = image[y]
        check(y == x)
        max_tail = max(max_tail, tail)
        periods.add(period)
    check(sum(indegree.values()) == len(states))
    return {
        "states": len(states),
        "image": len(indegree),
        "fixed": fixed,
        "max_tail": max_tail,
        "periods": tuple(sorted(periods)),
        "max_fibre": max(indegree.values(), default=0),
    }


def prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def pairs(n: int):
    return tuple((i, j) for i in range(n) for j in range(i + 1, n))


def degrees(mask: int, n: int):
    answer = [0] * n
    for bit, (i, j) in enumerate(pairs(n)):
        if mask >> bit & 1:
            answer[i] += 1
            answer[j] += 1
    return answer


def cut_mask(vertices, n: int):
    selected = set(vertices)
    answer = 0
    for bit, (i, j) in enumerate(pairs(n)):
        if (i in selected) ^ (j in selected):
            answer |= 1 << bit
    return answer


def graph_switch(mask: int, n: int, selector):
    deg = degrees(mask, n)
    selected = selector(mask, deg, n)
    return mask ^ cut_mask(selected, n)


def triangle_parities(mask: int, n: int):
    edge_index = {edge: bit for bit, edge in enumerate(pairs(n))}

    def has(i, j):
        if i > j:
            i, j = j, i
        return mask >> edge_index[i, j] & 1

    parity = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if has(i, j) and has(i, k) and has(j, k):
                    parity[i] ^= 1
                    parity[j] ^= 1
                    parity[k] ^= 1
    return parity


def tournament_scores(mask: int, n: int):
    score = [0] * n
    for bit, (i, j) in enumerate(pairs(n)):
        if mask >> bit & 1:
            score[i] += 1
        else:
            score[j] += 1
    return score


def tournament_switch(mask: int, n: int, selector):
    score = tournament_scores(mask, n)
    return mask ^ cut_mask(selector(mask, score, n), n)


def bipartite_odd_margin(mask: int, n: int):
    row = [0] * n
    col = [0] * n
    for i in range(n):
        for j in range(n):
            if mask >> (i * n + j) & 1:
                row[i] += 1
                col[j] += 1
    answer = mask
    for i in range(n):
        for j in range(n):
            if (row[i] & 1) ^ (col[j] & 1):
                answer ^= 1 << (i * n + j)
    return answer


def parity_gram_transpose(mask: int, n: int):
    rows = [sum(mask >> (i * n + j) & 1 for j in range(n)) & 1 for i in range(n)]
    answer = 0
    for i in range(n):
        for j in range(n):
            bit = ((mask >> (j * n + i)) & 1) ^ (rows[i] & rows[j])
            answer |= bit << (i * n + j)
    return answer


def runs(word):
    if not word:
        return []
    answer = []
    start = 0
    for i in range(1, len(word) + 1):
        if i == len(word) or word[i] != word[start]:
            answer.append(word[start:i])
            start = i
    return answer


def reverse_run_lengths(word):
    blocks = runs(word)
    if not blocks:
        return word
    lengths = [len(block) for block in blocks][::-1]
    bit = word[0]
    answer = []
    for length in lengths:
        answer.extend([bit] * length)
        bit ^= 1
    return tuple(answer)


def zero_blocks(word):
    answer = []
    current = []
    for letter in word:
        current.append(letter)
        if letter == 0:
            answer.append(tuple(current))
            current = []
    if current:
        answer.append(tuple(current))
    return answer


def rotate_zero_blocks(word):
    blocks = zero_blocks(word)
    if len(blocks) > 1:
        blocks = blocks[1:] + blocks[:1]
    return tuple(letter for block in blocks for letter in block)


def reverse_zero_blocks(word):
    return tuple(letter for block in zero_blocks(word)[::-1] for letter in block)


def rotate_nonzero_runs(word):
    answer = list(word)
    i = 0
    while i < len(word):
        if word[i] == 0:
            i += 1
            continue
        j = i
        while j < len(word) and word[j] != 0:
            j += 1
        if j - i > 1:
            answer[i:j] = answer[i + 1 : j] + answer[i : i + 1]
        i = j
    return tuple(answer)


def cfl_factors(word):
    """Chen--Fox--Lyndon factorization via Duval's algorithm."""
    n = len(word)
    answer = []
    i = 0
    while i < n:
        j = i + 1
        k = i
        while j < n and word[k] <= word[j]:
            if word[k] < word[j]:
                k = i
            else:
                k += 1
            j += 1
        length = j - k
        while i <= k:
            answer.append(word[i : i + length])
            i += length
    return answer


def reverse_cfl(word):
    return tuple(letter for factor in cfl_factors(word)[::-1] for letter in factor)


def dyck_words(n: int):
    for word in product((1, -1), repeat=2 * n):
        balance = 0
        valid = True
        for step in word:
            balance += step
            if balance < 0:
                valid = False
                break
        if valid and balance == 0:
            yield word


def motzkin_words(n: int):
    for word in product((1, 0, -1), repeat=n):
        balance = 0
        valid = True
        for step in word:
            balance += step
            if balance < 0:
                valid = False
                break
        if valid and balance == 0:
            yield word


def return_factors(path):
    answer = []
    current = []
    balance = 0
    for step in path:
        current.append(step)
        balance += step
        if balance == 0:
            answer.append(tuple(current))
            current = []
    check(not current)
    return answer


def reverse_factors(path):
    return tuple(step for factor in return_factors(path)[::-1] for step in factor)


def rotate_factors(path):
    factors = return_factors(path)
    if len(factors) > 1:
        factors = factors[1:] + factors[:1]
    return tuple(step for factor in factors for step in factor)


def compositions(n: int):
    if n == 0:
        yield ()
        return
    for first in range(1, n + 1):
        for rest in compositions(n - first):
            yield (first,) + rest


def cf_words(n: int):
    return tuple(word for word in compositions(n) if word and word[-1] >= 2)


def cf_canon(word):
    word = list(word)
    if len(word) > 1 and word[-1] == 1:
        word[-2] += 1
        word.pop()
    check(word and word[-1] >= 2)
    return tuple(word)


def cf_reverse(word):
    return cf_canon(word[::-1])


def cf_rotate(word):
    if len(word) <= 1:
        return word
    return cf_canon(word[1:] + word[:1])


def partitions(n: int, ceiling=None):
    if n == 0:
        yield ()
        return
    if ceiling is None:
        ceiling = n
    for first in range(min(n, ceiling), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def conjugate(partition):
    if not partition:
        return partition
    return tuple(sum(part >= j for part in partition) for j in range(1, partition[0] + 1))


def odd_distinct_conjugate(partition):
    return conjugate(partition) if len(set(partition)) & 1 else partition


def odd_multiplicity_conjugate(partition):
    multiplicities = Counter(partition)
    odd = sum(count & 1 for count in multiplicities.values())
    return conjugate(partition) if odd & 1 else partition


def pop_stack(permutation):
    answer = []
    i = 0
    while i < len(permutation):
        j = i + 1
        while j < len(permutation) and permutation[j - 1] > permutation[j]:
            j += 1
        answer.extend(reversed(permutation[i:j]))
        i = j
    return tuple(answer)


def isolated_flip(word):
    n = len(word)
    return tuple(
        word[i] ^ (word[(i - 1) % n] == word[(i + 1) % n]) for i in range(n)
    )


def format_summary(summary):
    return (
        f"states={summary['states']} image={summary['image']} "
        f"fixed={summary['fixed']} tail={summary['max_tail']} "
        f"periods={','.join(map(str, summary['periods']))} "
        f"max_fibre={summary['max_fibre']}"
    )


def run_family(identifier, sizes_and_states, update_builder):
    tested = 0
    last = None
    for size, states in sizes_and_states:
        states = tuple(states)
        last = analyse(states, update_builder(size))
        tested += len(states)
    print(f"{identifier} tested={tested} final[{format_summary(last)}]")


def main() -> None:
    # X01--X03: three intrinsically selected Seidel cut switches.
    graph_slices = [(n, range(1 << len(pairs(n)))) for n in range(2, 7)]
    run_family(
        "X01 graph odd-degree cut switch",
        graph_slices,
        lambda n: lambda mask: graph_switch(mask, n, lambda _m, d, _n: [i for i, x in enumerate(d) if x & 1]),
    )
    run_family(
        "X02 graph triangle-parity cut switch",
        graph_slices,
        lambda n: lambda mask: graph_switch(mask, n, lambda m, _d, nn: [i for i, x in enumerate(triangle_parities(m, nn)) if x]),
    )
    run_family(
        "X03 graph prime-degree cut switch",
        graph_slices,
        lambda n: lambda mask: graph_switch(mask, n, lambda _m, d, _n: [i for i, x in enumerate(d) if prime(x)]),
    )

    # Exact odd-degree switching laws, checked independently of summaries.
    for n, states in graph_slices:
        exponent = len(pairs(n)) - n + 1
        for mask in states:
            update = lambda x: graph_switch(x, n, lambda _m, d, _n: [i for i, z in enumerate(d) if z & 1])
            first = update(mask)
            if n & 1:
                check(update(first) == first)
                check(all(d % 2 == 0 for d in degrees(first, n)))
            else:
                check(update(first) == mask)
        if n & 1:
            eulerian = sum(all(d % 2 == 0 for d in degrees(mask, n)) for mask in states)
            check(eulerian == 1 << exponent)
            fibres = Counter(
                graph_switch(mask, n, lambda _m, d, _n: [i for i, z in enumerate(d) if z & 1])
                for mask in states
            )
            check(set(fibres.values()) == {1 << (n - 1)})
        else:
            fixed = sum(
                graph_switch(mask, n, lambda _m, d, _n: [i for i, z in enumerate(d) if z & 1]) == mask
                for mask in states
            )
            check(fixed == 1 << (exponent + 1))

    # X04--X05: score-selected tournament switches.
    tournament_slices = [(n, range(1 << len(pairs(n)))) for n in range(2, 7)]
    run_family(
        "X04 tournament odd-score cut reversal",
        tournament_slices,
        lambda n: lambda mask: tournament_switch(mask, n, lambda _m, d, _n: [i for i, x in enumerate(d) if x & 1]),
    )
    run_family(
        "X05 tournament maximum-score cut reversal",
        tournament_slices,
        lambda n: lambda mask: tournament_switch(mask, n, lambda _m, d, _n: [i for i, x in enumerate(d) if x == max(d)]),
    )
    for n, states in tournament_slices:
        update = lambda x: tournament_switch(x, n, lambda _m, d, _n: [i for i, z in enumerate(d) if z & 1])
        for mask in states:
            first = update(mask)
            if n % 4 in (0, 2):
                check(update(first) == mask)
            else:
                check(update(first) == first)
                target = 0 if n % 4 == 1 else 1
                check(all(d % 2 == target for d in tournament_scores(first, n)))

    # X06--X07: binary incidence-array maps.
    matrix_slices = [(n, range(1 << (n * n))) for n in range(1, 5)]
    run_family("X06 bipartite odd-margin cut switch", matrix_slices, lambda n: lambda mask: bipartite_odd_margin(mask, n))
    run_family("X07 parity-Gram transpose", matrix_slices, lambda n: lambda mask: parity_gram_transpose(mask, n))

    # X08--X12: word maps.
    binary_slices = lambda: [(n, product((0, 1), repeat=n)) for n in range(1, 13)]
    ternary_slices = lambda: [(n, product((0, 1, 2), repeat=n)) for n in range(1, 9)]
    run_family("X08 binary run-length reversal", binary_slices(), lambda _n: reverse_run_lengths)
    run_family("X09 binary zero-block rotation", binary_slices(), lambda _n: rotate_zero_blocks)
    run_family("X10 ternary nonzero-run rotation", ternary_slices(), lambda _n: rotate_nonzero_runs)
    run_family("X11 ternary zero-block reversal", ternary_slices(), lambda _n: reverse_zero_blocks)
    run_family("X12 binary CFL-factor reversal", binary_slices(), lambda _n: reverse_cfl)

    # X13--X16: path factor maps.
    run_family("X13 Dyck primitive-factor reversal", [(n, dyck_words(n)) for n in range(1, 9)], lambda _n: reverse_factors)
    run_family("X14 Dyck primitive-factor rotation", [(n, dyck_words(n)) for n in range(1, 9)], lambda _n: rotate_factors)
    run_family("X15 Motzkin return-factor reversal", [(n, motzkin_words(n)) for n in range(1, 11)], lambda _n: reverse_factors)
    run_family("X16 Motzkin return-factor rotation", [(n, motzkin_words(n)) for n in range(1, 11)], lambda _n: rotate_factors)

    # X17--X18: canonical regular-continued-fraction digit words.
    cf_slices = [(n, cf_words(n)) for n in range(2, 15)]
    run_family("X17 canonical-CF reversal-normalization", cf_slices, lambda _n: cf_reverse)
    run_family("X18 canonical-CF rotation-normalization", cf_slices, lambda _n: cf_rotate)
    for n, states in cf_slices:
        fibres = Counter(map(cf_reverse, states))
        expected_image = {word for word in states if word[0] >= 2}
        check(set(fibres) == expected_image)
        check(len(expected_image) == (1 if n == 2 else 1 << (n - 3)))
        check(set(fibres.values()) == ({1} if n == 2 else {2}))
        for word in states:
            check(cf_reverse(cf_reverse(cf_reverse(word))) == cf_reverse(word))

    # X19--X20: statistic-selected Ferrers conjugations.
    partition_slices = [(n, tuple(partitions(n))) for n in range(1, 26)]
    run_family("X19 odd-distinct-part conjugation", partition_slices, lambda _n: odd_distinct_conjugate)
    run_family("X20 odd-multiplicity conjugation", partition_slices, lambda _n: odd_multiplicity_conjugate)

    # X21--X22: one classical permutation sorter and one nonlinear cyclic CA.
    permutation_slices = [(n, permutations(range(1, n + 1))) for n in range(1, 9)]
    run_family("X21 pop-stack descent-run reversal", permutation_slices, lambda _n: pop_stack)
    cyclic_slices = [(n, product((0, 1), repeat=n)) for n in range(3, 15)]
    run_family("X22 cyclic isolated-bit flip", cyclic_slices, lambda _n: isolated_flip)

    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
