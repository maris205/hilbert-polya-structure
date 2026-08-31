#!/usr/bin/env python3
"""Exact breadth scout for stochastic and local-rewrite dynamics.

The 27 systems below are literal kernels, not renamed parameter choices.
Every probability is a fractions.Fraction.  There is no floating point,
sampling, third-party dependency, network access, or timestamp in the run.
"""

from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial


ASSERTIONS = 0
RESULTS = []


def check(condition, message="exact assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def record(code, family, scope, states, signal, decision, before):
    RESULTS.append(
        {
            "code": code,
            "family": family,
            "scope": scope,
            "states": states,
            "assertions": ASSERTIONS - before,
            "signal": signal,
            "decision": decision,
        }
    )


def all_words(alphabet, n):
    return product(alphabet, repeat=n)


def comps(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in comps(total - first, length - 1):
            yield (first,) + tail


def dag_analyzer(successors):
    """Return exact terminal set, path lengths, event histories, and mean."""

    @lru_cache(maxsize=None)
    def analyze(state):
        out = tuple(successors(state))
        if not out:
            return frozenset((state,)), frozenset((0,)), 1, Fraction(0)
        terminals = set()
        lengths = set()
        histories = 0
        mean = Fraction(1)
        for target in out:
            target_terminals, target_lengths, target_histories, target_mean = analyze(target)
            terminals.update(target_terminals)
            lengths.update(length + 1 for length in target_lengths)
            histories += target_histories
            mean += target_mean / len(out)
        return frozenset(terminals), frozenset(lengths), histories, mean

    return analyze


def terminal_distribution(successors):
    @lru_cache(maxsize=None)
    def distribution(state):
        out = tuple(successors(state))
        if not out:
            return ((state, Fraction(1)),)
        answer = defaultdict(Fraction)
        for target in out:
            for terminal, probability in distribution(target):
                answer[terminal] += probability / len(out)
        return tuple(sorted(answer.items()))

    return distribution


# ---------------------------------------------------------------------------
# R01: Fibonacci rewrite 100 -> 011


def fib_successors(word):
    return [word[:i] + (0, 1, 1) + word[i + 3 :]
            for i in range(len(word) - 2) if word[i : i + 3] == (1, 0, 0)]


def fib_weights(length):
    values = [1, 1]
    while len(values) < length:
        values.append(values[-1] + values[-2])
    return tuple(reversed(values[:length]))


def fibonacci(index):
    a, b = 0, 1
    for _ in range(index):
        a, b = b, a + b
    return a


def fib_value(word):
    return sum(bit * weight for bit, weight in zip(word, fib_weights(len(word))))


def fib_special_normal(length):
    if length == 1:
        return (1,)
    word = (1,) + (0,) * (length - 1)
    while True:
        out = fib_successors(word)
        if not out:
            return word
        word = out[0]


def run_r01():
    before = ASSERTIONS
    analyze = dag_analyzer(fib_successors)
    state_count = 0
    maximums = []
    fibre_ranges = []
    for n in range(1, 15):
        fibres = Counter()
        local_max = 0
        weights = fib_weights(n)
        for word in all_words((0, 1), n):
            state_count += 1
            terminals, lengths, _, mean = analyze(word)
            check(len(terminals) == 1, "R01 lost confluence")
            check(len(lengths) == 1, "R01 path length depends on scheduler")
            terminal = next(iter(terminals))
            depth = next(iter(lengths))
            check((1, 0, 0) not in tuple(terminal[i : i + 3]
                                         for i in range(n - 2)))
            check(sum(bit * weight for bit, weight in zip(word, weights))
                  == sum(bit * weight for bit, weight in zip(terminal, weights)))
            check(depth == sum(terminal) - sum(word))
            check(mean == depth)
            for target in fib_successors(word):
                check(fib_value(target) == fib_value(word))
                check(sum(target) == sum(word) + 1)
            fibres[terminal] += 1
            local_max = max(local_max, depth)
        predicted = 0 if n < 3 else (n - 1) // 2
        check(local_max == predicted)
        special = fib_special_normal(n)
        check(sum(special) - 1 == predicted)
        check(len(fibres) == fibonacci(n + 3) - 1,
              "R01 forbidden-word image count failed")
        if n <= 2:
            predicted_max_fibre = 1
        elif n % 2:
            predicted_max_fibre = fibonacci((n + 3) // 2)
        else:
            predicted_max_fibre = 2 * fibonacci(n // 2)
        check(max(fibres.values()) == predicted_max_fibre,
              "R01 extremal fibre signal failed")
        maximums.append(local_max)
        fibre_ranges.append((min(fibres.values()), max(fibres.values()), len(fibres)))
    record(
        "R01", "finite word rewrite",
        "all binary words of lengths 1..14", state_count,
        f"terminating confluent Fibonacci normalization; sharp depths {maximums[-8:]}; terminal fibre ranges end at {fibre_ranges[-1]}",
        "KILL_OWNER_FIBONACCI_REPRESENTATIONS", before,
    )


# ---------------------------------------------------------------------------
# R02: open-boundary k-mer convoy rewrite 1^k 0 -> 0 1^k


def kmer_successors(word, k):
    source = (1,) * k + (0,)
    target = (0,) + (1,) * k
    return [word[:i] + target + word[i + k + 1 :]
            for i in range(len(word) - k) if word[i : i + k + 1] == source]


def one_gaps(word):
    gaps = []
    run = 0
    for bit in word:
        if bit:
            run += 1
        else:
            gaps.append(run)
            run = 0
    gaps.append(run)
    return tuple(gaps)


def word_from_gaps(gaps):
    out = []
    for gap in gaps[:-1]:
        out.extend((1,) * gap)
        out.append(0)
    out.extend((1,) * gaps[-1])
    return tuple(out)


def kmer_direct(word, k):
    gaps = one_gaps(word)
    carry = 0
    depth = 0
    terminal_gaps = []
    for gap in gaps[:-1]:
        carry += gap // k
        depth += carry
        terminal_gaps.append(gap % k)
    terminal_gaps.append(gaps[-1] + k * carry)
    return word_from_gaps(tuple(terminal_gaps)), depth


def one_zero_inversions(word):
    ones = 0
    answer = 0
    for bit in word:
        if bit:
            ones += 1
        else:
            answer += ones
    return answer


@lru_cache(maxsize=None)
def gaussian_binomial_coefficients(n, k):
    """Coefficient tuple of the q-binomial [n choose k]_q."""
    if k < 0 or k > n:
        return ()
    if k == 0 or k == n:
        return (1,)
    left = gaussian_binomial_coefficients(n - 1, k)
    right = gaussian_binomial_coefficients(n - 1, k - 1)
    shift = n - k
    degree = max(len(left), len(right) + shift)
    answer = [0] * degree
    for exponent, coefficient in enumerate(left):
        answer[exponent] += coefficient
    for exponent, coefficient in enumerate(right):
        answer[exponent + shift] += coefficient
    return tuple(answer)


def run_r02():
    before = ASSERTIONS
    state_count = 0
    max_depths = {}
    largest_fibre = 0
    scopes = ((2, 16), (3, 13), (4, 13))
    for k, maximum_length in scopes:
        successors = lambda word, k=k: kmer_successors(word, k)
        analyze = dag_analyzer(successors)
        family_max = 0
        for n in range(1, maximum_length + 1):
            fibres = Counter()
            depth_fibres = defaultdict(Counter)
            local_max = 0
            for word in all_words((0, 1), n):
                state_count += 1
                direct_terminal, direct_depth = kmer_direct(word, k)
                terminals, lengths, _, mean = analyze(word)
                check(terminals == frozenset((direct_terminal,)),
                      "R02 normal form mismatch")
                check(lengths == frozenset((direct_depth,)),
                      "R02 odometer mismatch")
                check(mean == direct_depth)
                check((one_zero_inversions(word) - one_zero_inversions(direct_terminal))
                      == k * direct_depth)
                for target in successors(word):
                    check(one_zero_inversions(target)
                          == one_zero_inversions(word) - k)
                fibres[direct_terminal] += 1
                depth_fibres[direct_terminal][direct_depth] += 1
                local_max = max(local_max, direct_depth)
            for terminal, fibre_size in fibres.items():
                gaps = one_gaps(terminal)
                check(all(gap < k for gap in gaps[:-1]))
                zero_count = len(gaps) - 1
                budget = gaps[-1] // k
                predicted = comb(budget + zero_count, zero_count)
                check(fibre_size == predicted, "R02 all-fibre formula failed")
                coefficients = gaussian_binomial_coefficients(
                    budget + zero_count, zero_count
                )
                actual_coefficients = tuple(
                    depth_fibres[terminal].get(exponent, 0)
                    for exponent in range(len(coefficients))
                )
                check(actual_coefficients == coefficients,
                      "R02 q-binomial depth enumerator failed")
            largest_fibre = max(largest_fibre, max(fibres.values()))
            family_max = max(family_max, local_max)
        max_depths[k] = family_max
    record(
        "R02", "open-boundary k-mer rewrite / directed toppling",
        "all binary words: k=2 lengths 1..16; k=3,4 lengths 1..13",
        state_count,
        f"all-k gap normal form and odometer; every target fibre has a Gaussian-binomial depth polynomial; tested max depths {max_depths}, largest fibre {largest_fibre}",
        "PROMOTE_INTERNAL_OWNER_HOLD", before,
    )


# ---------------------------------------------------------------------------
# R03--R09: other word and cellular rewrites


def alt_contract_successors(word):
    return [word[:i] + (0,) + word[i + 3 :]
            for i in range(len(word) - 2) if word[i : i + 3] == (0, 1, 0)]


def run_r03():
    before = ASSERTIONS
    analyze = dag_analyzer(alt_contract_successors)
    states = 0
    max_depth = 0
    for n in range(0, 17):
        for word in all_words((0, 1), n):
            states += 1
            terminals, lengths, _, _ = analyze(word)
            check(len(terminals) == 1)
            check(len(lengths) == 1)
            depth = next(iter(lengths))
            check(len(word) - len(next(iter(terminals))) == 2 * depth)
            max_depth = max(max_depth, depth)
    record("R03", "shrinking word rewrite", "all binary words length 0..16",
           states, f"unique irreducible and fixed path length; maximum {max_depth}",
           "KILL_STANDARD_STRING_REDUCTION", before)


def run_contract_successors(word):
    return [word[:i] + (word[i],) + word[i + 2 :]
            for i in range(len(word) - 1) if word[i] == word[i + 1]]


def compress_runs(word):
    out = []
    for letter in word:
        if not out or out[-1] != letter:
            out.append(letter)
    return tuple(out)


def run_r04():
    before = ASSERTIONS
    analyze = dag_analyzer(run_contract_successors)
    states = 0
    for n in range(0, 10):
        for word in all_words((0, 1, 2), n):
            states += 1
            terminals, lengths, histories, mean = analyze(word)
            terminal = compress_runs(word)
            depth = len(word) - len(terminal)
            check(terminals == frozenset((terminal,)))
            check(lengths == frozenset((depth,)))
            check(histories >= 1 and mean == depth)
    record("R04", "idempotent word erosion", "all ternary words length 0..9",
           states, "run compression is the exact terminal map and the clock is n-runs",
           "KILL_FREE_IDEMPOTENT_NORMAL_FORM", before)


def unequal_cancel_successors(word):
    return [word[:i] + word[i + 2 :]
            for i in range(len(word) - 1) if word[i] != word[i + 1]]


def run_r05():
    before = ASSERTIONS
    analyze = dag_analyzer(unequal_cancel_successors)
    states = 0
    for n in range(0, 19):
        for word in all_words((0, 1), n):
            states += 1
            terminals, lengths, _, mean = analyze(word)
            zeros = word.count(0)
            ones = n - zeros
            if zeros >= ones:
                terminal = (0,) * (zeros - ones)
            else:
                terminal = (1,) * (ones - zeros)
            depth = min(zeros, ones)
            check(terminals == frozenset((terminal,)))
            check(lengths == frozenset((depth,)))
            check(mean == depth)
    record("R05", "annihilating word rewrite", "all binary words length 0..18",
           states, "unique signed-count normal form and deterministic cancellation clock",
           "KILL_FREE_GROUP_REDUCTION", before)


def cyclic_isolate_successors(word):
    n = len(word)
    out = []
    for i in range(n):
        if word[i - 1] == word[(i + 1) % n] != word[i]:
            target = list(word)
            target[i] = word[i - 1]
            out.append(tuple(target))
    return out


def walls(word):
    return sum(word[i] != word[(i + 1) % len(word)] for i in range(len(word)))


def run_r06():
    before = ASSERTIONS
    analyze = dag_analyzer(cyclic_isolate_successors)
    distribution = terminal_distribution(cyclic_isolate_successors)
    states = 0
    multi_sources = 0
    max_terminals = 0
    for n in range(3, 13):
        for word in all_words((0, 1), n):
            states += 1
            terminals, lengths, _, mean = analyze(word)
            law = dict(distribution(word))
            check(sum(law.values(), Fraction()) == 1)
            check(set(law) == set(terminals))
            check(all(not cyclic_isolate_successors(target) for target in terminals))
            for target in cyclic_isolate_successors(word):
                check(walls(target) == walls(word) - 2)
            check(mean >= min(lengths) and mean <= max(lengths))
            multi_sources += len(terminals) > 1
            max_terminals = max(max_terminals, len(terminals))
    record("R06", "cyclic spin erosion", "all cyclic binary words length 3..12",
           states, f"exact terminal laws; {multi_sources} nonconfluent sources and up to {max_terminals} terminals",
           "KILL_ZERO_TEMPERATURE_GLAUBER", before)


def ternary_reverse_successors(word):
    return [word[:i] + (2, 1, 0) + word[i + 3 :]
            for i in range(len(word) - 2) if word[i : i + 3] == (0, 1, 2)]


def inversions(word):
    return sum(word[i] > word[j] for i in range(len(word)) for j in range(i + 1, len(word)))


def run_r07():
    before = ASSERTIONS
    analyze = dag_analyzer(ternary_reverse_successors)
    states = 0
    max_depth = 0
    for n in range(0, 10):
        for word in all_words((0, 1, 2), n):
            states += 1
            terminals, lengths, _, mean = analyze(word)
            check(len(terminals) == 1 and len(lengths) == 1)
            depth = next(iter(lengths))
            check(inversions(next(iter(terminals))) - inversions(word) == 3 * depth)
            check(mean == depth)
            max_depth = max(max_depth, depth)
    record("R07", "ternary local reversal", "all ternary words length 0..9",
           states, f"orthogonal confluent rewrite with inversion clock; maximum {max_depth}",
           "KILL_ORTHOGONAL_REWRITE_TRIVIAL", before)


def thue_successors(word):
    return [word[:i] + (1, 0, 1) + word[i + 3 :]
            for i in range(len(word) - 2) if word[i : i + 3] == (0, 1, 0)]


def run_r08():
    before = ASSERTIONS
    analyze = dag_analyzer(thue_successors)
    states = 0
    multi = 0
    variable = 0
    maximum = 0
    for n in range(1, 13):
        for word in all_words((0, 1), n):
            states += 1
            terminals, lengths, _, _ = analyze(word)
            check(all(sum(target) > sum(word) for target in thue_successors(word)))
            multi += len(terminals) > 1
            variable += len(lengths) > 1
            maximum = max(maximum, len(terminals))
    check(multi > 0 and variable > 0)
    record("R08", "nonconfluent cellular rewrite", "all binary words length 1..12",
           states, f"{multi} multiple-normal-form and {variable} variable-clock sources; max terminals {maximum}",
           "KILL_NONCONFLUENT", before)


def cyclic_111_successors(word):
    n = len(word)
    out = []
    if n < 3:
        return out
    for i in range(n):
        indices = (i, (i + 1) % n, (i + 2) % n)
        if all(word[j] == 1 for j in indices):
            target = list(word)
            target[(i + 1) % n] = 0
            out.append(tuple(target))
    return out


def run_r09():
    before = ASSERTIONS
    analyze = dag_analyzer(cyclic_111_successors)
    states = 0
    max_terminals = 0
    for n in range(3, 13):
        for word in all_words((0, 1), n):
            states += 1
            terminals, lengths, _, mean = analyze(word)
            check(all(sum(target) == sum(word) - 1 for target in cyclic_111_successors(word)))
            check(all("111" not in "".join(map(str, target + target[:2])) for target in terminals))
            check(mean >= min(lengths) and mean <= max(lengths))
            max_terminals = max(max_terminals, len(terminals))
    record("R09", "cyclic hard-core erosion", "all cyclic binary words length 3..12",
           states, f"terminal independent-distance-two configurations; up to {max_terminals} outcomes",
           "KILL_RANDOM_SEQUENTIAL_ADSORPTION", before)


# ---------------------------------------------------------------------------
# P01--P06: permutation kernels


def local_max_successors(word):
    n = len(word)
    out = []
    for i, value in enumerate(word):
        left_ok = i == 0 or value > word[i - 1]
        right_ok = i == n - 1 or value > word[i + 1]
        if left_ok and right_ok and n > 1:
            out.append(word[:i] + word[i + 1 :])
    return out


def cartesian_subtree_sizes(word):
    sizes = {}

    def visit(segment):
        if not segment:
            return 0
        root_value = min(segment)
        root_index = segment.index(root_value)
        left_size = visit(segment[:root_index])
        right_size = visit(segment[root_index + 1 :])
        sizes[root_value] = 1 + left_size + right_size
        return sizes[root_value]

    visit(word)
    return sizes


def run_p01():
    before = ASSERTIONS
    analyze = dag_analyzer(local_max_successors)
    states = 0
    max_histories = 0
    probability_spread = (Fraction(1), Fraction(1))

    @lru_cache(maxsize=None)
    def history_law(word):
        out = local_max_successors(word)
        if not out:
            return (((), Fraction(1)),)
        law = defaultdict(Fraction)
        for target in out:
            deleted = next(value for value in word if value not in target)
            for order, probability in history_law(target):
                law[(deleted,) + order] += probability / len(out)
        return tuple(sorted(law.items()))

    for n in range(1, 9):
        for word in permutations(range(n)):
            states += 1
            terminals, lengths, histories, mean = analyze(word)
            check(terminals == frozenset(((min(word),),)))
            check(lengths == frozenset((n - 1,)) and mean == n - 1)
            subtree_sizes = cartesian_subtree_sizes(word)
            denominator = 1
            for value, size in subtree_sizes.items():
                if value != min(word):
                    denominator *= size
            predicted = factorial(n - 1) // denominator
            check(histories == predicted, "P01 Cartesian hook formula failed")
            law = dict(history_law(word))
            check(len(law) == histories)
            check(sum(law.values(), Fraction()) == 1)
            check(all(order[-1] != min(word) if order else True for order in law))
            if law:
                probability_spread = (
                    min(probability_spread[0], min(law.values())),
                    max(probability_spread[1], max(law.values())),
                )
            max_histories = max(max_histories, histories)
    record(
        "P01", "permutation erosion / Cartesian-tree pruning",
        "all permutations of sizes 1..8", states,
        f"exact conjugacy to uniform-active leaf pruning; schedule count is the tree hook formula; max histories {max_histories}",
        "KILL_CLASSICAL_AND_INTERNAL_CARTESIAN_TREE", before,
    )


def descent_swap_successors(word):
    out = []
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            target = list(word)
            target[i], target[i + 1] = target[i + 1], target[i]
            out.append(tuple(target))
    return out


def run_p02():
    before = ASSERTIONS
    analyze = dag_analyzer(descent_swap_successors)
    states = 0
    maximum_histories = 0
    for n in range(1, 10):
        for word in permutations(range(n)):
            states += 1
            terminals, lengths, histories, mean = analyze(word)
            inv = inversions(word)
            check(terminals == frozenset((tuple(range(n)),)))
            check(lengths == frozenset((inv,)) and mean == inv)
            maximum_histories = max(maximum_histories, histories)
    record("P02", "random-scheduler sorting", "all permutations size 1..9",
           states, f"inversion clock and reduced-word history recursion; max histories {maximum_histories}",
           "KILL_COXETER_ZERO_HECKE", before)


def descent_delete_successors(word):
    return [word[:i] + word[i + 1 :]
            for i in range(len(word) - 1) if word[i] > word[i + 1]]


def right_to_left_minima(word):
    answer = []
    current = None
    for value in reversed(word):
        if current is None or value < current:
            answer.append(value)
            current = value
    return tuple(reversed(answer))


def run_p03():
    before = ASSERTIONS
    analyze = dag_analyzer(descent_delete_successors)
    states = 0
    max_histories = 0
    for n in range(1, 9):
        for word in permutations(range(n)):
            states += 1
            terminal = right_to_left_minima(word)
            terminals, lengths, histories, mean = analyze(word)
            depth = n - len(terminal)
            check(terminals == frozenset((terminal,)))
            check(lengths == frozenset((depth,)) and mean == depth)
            max_histories = max(max_histories, histories)
    record("P03", "permutation descent deletion", "all permutations size 1..8",
           states, f"terminal is exactly the right-to-left minima subsequence; max histories {max_histories}",
           "KILL_MONOTONE_STACK_NORMAL_FORM", before)


def delete_smaller_successors(word):
    out = []
    for i in range(len(word) - 1):
        delete = i if word[i] < word[i + 1] else i + 1
        out.append(word[:delete] + word[delete + 1 :])
    return out


def run_p04():
    before = ASSERTIONS
    analyze = dag_analyzer(delete_smaller_successors)
    states = 0
    for n in range(1, 9):
        for word in permutations(range(n)):
            states += 1
            terminals, lengths, histories, mean = analyze(word)
            check(terminals == frozenset(((n - 1,),)))
            check(lengths == frozenset((n - 1,)) and mean == n - 1)
            check(histories >= factorial(n - 1))
    record("P04", "adjacent tournament erosion", "all permutations size 1..8",
           states, "global maximum is the unique survivor; all clocks equal n-1",
           "KILL_TOURNAMENT_TRIVIAL", before)


def record_delete_successors(word):
    maximum = -1
    records = set()
    for value in word:
        if value > maximum:
            records.add(value)
            maximum = value
    return [word[:i] + word[i + 1 :] for i, value in enumerate(word) if value not in records]


def left_records(word):
    answer = []
    maximum = -1
    for value in word:
        if value > maximum:
            answer.append(value)
            maximum = value
    return tuple(answer)


def run_p05():
    before = ASSERTIONS
    analyze = dag_analyzer(record_delete_successors)
    states = 0
    for n in range(1, 9):
        for word in permutations(range(n)):
            states += 1
            terminal = left_records(word)
            depth = n - len(terminal)
            terminals, lengths, histories, mean = analyze(word)
            check(terminals == frozenset((terminal,)))
            check(lengths == frozenset((depth,)) and mean == depth)
            check(histories == factorial(depth))
    record("P05", "record-filter erosion", "all permutations size 1..8",
           states, "left-record projection with a factorial schedule set",
           "KILL_IMMEDIATE_RECORD_THEORY", before)


def run_p06():
    before = ASSERTIONS
    states = 0
    for n in range(2, 8):
        perms = tuple(permutations(range(n)))
        perm_set = set(perms)
        pairs = tuple(combinations(range(n), 2))
        seen = {perms[0]}
        queue = deque((perms[0],))
        while queue:
            word = queue.popleft()
            for i, j in pairs:
                target = list(word)
                target[i], target[j] = target[j], target[i]
                target = tuple(target)
                check(target in perm_set)
                # Exact symmetry gives detailed balance for uniform measure.
                reverse = list(target)
                reverse[i], reverse[j] = reverse[j], reverse[i]
                check(tuple(reverse) == word)
                if target not in seen:
                    seen.add(target)
                    queue.append(target)
        check(len(seen) == factorial(n))
        states += len(perms)
    record("P06", "permutation Markov chain", "random transpositions on S_n, n=2..7",
           states, "irreducible symmetric graph, uniform stationary law, parity period two",
           "KILL_RANDOM_TRANSPOSITION_CLASSICAL", before)


# ---------------------------------------------------------------------------
# G01--G05: tree, DAG, greedy graph, and growth kernels


def prufer_edges(code):
    n = len(code) + 2
    degree = [1] * n
    for value in code:
        degree[value] += 1
    edges = []
    for value in code:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((min(leaf, value), max(leaf, value)))
        degree[leaf] -= 1
        degree[value] -= 1
    leaves = [i for i in range(n) if degree[i] == 1]
    edges.append((min(leaves), max(leaves)))
    return tuple(sorted(edges))


def rooted_tree_data(n, edges, root=0):
    adjacency = [[] for _ in range(n)]
    for a, b in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    parent = [-1] * n
    order = [root]
    for vertex in order:
        for neighbor in adjacency[vertex]:
            if neighbor != parent[vertex]:
                parent[neighbor] = vertex
                order.append(neighbor)
    subtree = [1] * n
    for vertex in reversed(order[1:]):
        subtree[parent[vertex]] += subtree[vertex]
    return parent, subtree


def run_g01():
    before = ASSERTIONS
    trees = 0
    dynamic_states = 0
    for n in range(2, 7):
        for code in product(range(n), repeat=n - 2):
            edges = prufer_edges(code)
            parent, subtree = rooted_tree_data(n, edges)

            @lru_cache(maxsize=None)
            def histories(mask):
                if mask == 1:
                    return 1
                children = [0] * n
                for vertex in range(1, n):
                    if mask >> vertex & 1:
                        children[parent[vertex]] += 1
                leaves = [vertex for vertex in range(1, n)
                          if mask >> vertex & 1 and children[vertex] == 0]
                check(bool(leaves))
                return sum(histories(mask & ~(1 << leaf)) for leaf in leaves)

            actual = histories((1 << n) - 1)
            denominator = 1
            for vertex in range(1, n):
                denominator *= subtree[vertex]
            check(actual == factorial(n - 1) // denominator)
            trees += 1
            dynamic_states += histories.cache_info().currsize
    record("G01", "rooted-tree leaf erosion", "all labelled trees n=2..6 rooted at 0",
           dynamic_states, f"tree hook-length schedule formula over {trees} rooted trees",
           "KILL_CLASSICAL_AND_P01_CONJUGATE", before)


def run_g02():
    before = ASSERTIONS
    dags = 0
    states = 0
    for n in range(1, 6):
        possible = tuple(combinations(range(n), 2))
        for edge_mask in range(1 << len(possible)):
            edges = tuple(edge for k, edge in enumerate(possible) if edge_mask >> k & 1)

            @lru_cache(maxsize=None)
            def top_orders(mask):
                if mask == 0:
                    return 1
                sources = []
                for vertex in range(n):
                    if not (mask >> vertex & 1):
                        continue
                    if all(not (mask >> a & 1 and b == vertex) for a, b in edges):
                        sources.append(vertex)
                check(bool(sources))
                return sum(top_orders(mask & ~(1 << source)) for source in sources)

            count = top_orders((1 << n) - 1)
            brute = 0
            for order in permutations(range(n)):
                position = {value: i for i, value in enumerate(order)}
                brute += all(position[a] < position[b] for a, b in edges)
            check(count == brute)
            dags += 1
            states += top_orders.cache_info().currsize
    record("G02", "DAG source erosion", "all naturally ordered DAGs n=1..5",
           states, f"random-source histories equal topological orders for {dags} DAGs",
           "KILL_LINEAR_EXTENSION_CLASSICAL", before)


def greedy_is_successors(mask, n):
    out = []
    for vertex in range(n):
        if mask >> vertex & 1:
            removed = 1 << vertex
            if vertex:
                removed |= 1 << (vertex - 1)
            if vertex + 1 < n:
                removed |= 1 << (vertex + 1)
            out.append((mask & ~removed, 1 << vertex))
    return out


def run_g03():
    before = ASSERTIONS
    total_states = 0
    means = []
    for n in range(1, 16):
        @lru_cache(maxsize=None)
        def law(mask):
            if mask == 0:
                return ((0, Fraction(1)),)
            answer = defaultdict(Fraction)
            out = greedy_is_successors(mask, n)
            for target, accepted in out:
                for chosen, probability in law(target):
                    answer[chosen | accepted] += probability / len(out)
            return tuple(sorted(answer.items()))

        distribution = dict(law((1 << n) - 1))
        check(sum(distribution.values(), Fraction()) == 1)
        for chosen in distribution:
            check(not (chosen & (chosen << 1)))
            check((chosen | (chosen << 1) | (chosen >> 1)) & ((1 << n) - 1)
                  == (1 << n) - 1)
        mean = sum(mask.bit_count() * probability for mask, probability in distribution.items())
        means.append(mean)
        total_states += law.cache_info().currsize
    record("G03", "random greedy independent set", "full paths P_n, n=1..15",
           total_states, f"complete exact maximal-independent-set laws; final mean {means[-1]}",
           "KILL_RANDOM_SEQUENTIAL_ADSORPTION", before)


def matching_successors(mask, n):
    out = []
    for edge in range(n):
        if mask >> edge & 1:
            removed = (1 << edge) | (1 << ((edge - 1) % n)) | (1 << ((edge + 1) % n))
            out.append((mask & ~removed, 1 << edge))
    return out


def run_g04():
    before = ASSERTIONS
    total_states = 0
    means = []
    for n in range(3, 15):
        @lru_cache(maxsize=None)
        def law(mask):
            if mask == 0:
                return ((0, Fraction(1)),)
            answer = defaultdict(Fraction)
            out = matching_successors(mask, n)
            for target, chosen_edge in out:
                for chosen, probability in law(target):
                    answer[chosen | chosen_edge] += probability / len(out)
            return tuple(sorted(answer.items()))

        distribution = dict(law((1 << n) - 1))
        check(sum(distribution.values(), Fraction()) == 1)
        for chosen in distribution:
            check(all(not ((chosen >> edge & 1) and (chosen >> ((edge + 1) % n) & 1))
                      for edge in range(n)))
        means.append(sum(mask.bit_count() * probability for mask, probability in distribution.items()))
        total_states += law.cache_info().currsize
    record("G04", "random greedy cycle matching", "full cycles C_n, n=3..14",
           total_states, f"complete exact greedy-matching laws; final mean {means[-1]}",
           "KILL_RANDOM_GREEDY_MATCHING", before)


def growth_successors(mask, n):
    events = []
    for i in range(n):
        j = (i + 1) % n
        left = mask >> i & 1
        right = mask >> j & 1
        if left != right:
            events.append(mask | (1 << i) | (1 << j))
    return events


def run_g05():
    before = ASSERTIONS
    analyze_cache = 0
    last_laws = []
    for n in range(3, 18):
        analyze = dag_analyzer(lambda mask, n=n: growth_successors(mask, n))

        @lru_cache(maxsize=None)
        def last_distribution(mask):
            out = growth_successors(mask, n)
            if not out:
                return ((-1, Fraction(1)),)
            answer = defaultdict(Fraction)
            for target in out:
                newly = target ^ mask
                if target == (1 << n) - 1:
                    answer[newly.bit_length() - 1] += Fraction(1, len(out))
                else:
                    for vertex, probability in last_distribution(target):
                        answer[vertex] += probability / len(out)
            return tuple(sorted(answer.items()))

        start = 1
        terminals, lengths, _, mean = analyze(start)
        check(terminals == frozenset(((1 << n) - 1,)))
        check(lengths == frozenset((n - 1,)) and mean == n - 1)
        law = dict(last_distribution(start))
        check(sum(law.values(), Fraction()) == 1)
        check(law[1] == law[n - 1])
        last_laws.append(tuple(law.items()))
        analyze_cache += analyze.cache_info().currsize + last_distribution.cache_info().currsize
    record("G05", "cycle boundary growth", "single-seed cycles C_n, n=3..17",
           analyze_cache, f"deterministic cover clock and exact symmetric last-site laws through n=17",
           "KILL_EDEN_RICHARDSON_SPECIALIZATION", before)


# ---------------------------------------------------------------------------
# Q01--Q04: piles and queues


def transport_successors(state):
    out = []
    for i in range(len(state) - 1):
        if state[i]:
            target = list(state)
            target[i] -= 1
            target[i + 1] += 1
            out.append(tuple(target))
    return out


def transport_potential(state):
    n = len(state)
    return sum((n - 1 - i) * value for i, value in enumerate(state))


def run_q01():
    before = ASSERTIONS
    analyze = dag_analyzer(transport_successors)
    states = 0
    max_depth = 0
    for n in range(2, 7):
        for total in range(0, 11):
            for state in comps(total, n):
                states += 1
                depth = transport_potential(state)
                terminals, lengths, _, mean = analyze(state)
                check(terminals == frozenset(((0,) * (n - 1) + (total,),)))
                check(lengths == frozenset((depth,)) and mean == depth)
                max_depth = max(max_depth, depth)
    record("Q01", "directed token queue", "compositions total <=10, lengths 2..6",
           states, f"weighted-distance clock independent of scheduler; maximum {max_depth}",
           "KILL_INDEPENDENT_TOKEN_TRANSPORT", before)


def carry3_successors(state):
    out = []
    for i in range(len(state) - 1):
        if state[i] >= 3:
            target = list(state)
            target[i] -= 3
            target[i + 1] += 1
            out.append(tuple(target))
    return out


def carry3_direct(state):
    target = list(state)
    firings = 0
    weighted = sum(value * 3 ** i for i, value in enumerate(state))
    for i in range(len(target) - 1):
        quotient, target[i] = divmod(target[i], 3)
        target[i + 1] += quotient
        firings += quotient
    return tuple(target), firings, weighted


def run_q02():
    before = ASSERTIONS
    analyze = dag_analyzer(carry3_successors)
    states = 0
    for length in range(2, 7):
        for state in product(range(7), repeat=length):
            states += 1
            direct, firings, weighted = carry3_direct(state)
            terminals, lengths, _, mean = analyze(state)
            check(terminals == frozenset((direct,)))
            check(lengths == frozenset((firings,)) and mean == firings)
            check(sum(value * 3 ** i for i, value in enumerate(direct)) == weighted)
            check(all(value < 3 for value in direct[:-1]))
    record("Q02", "ternary carrying network", "digits 0..6, lengths 2..6",
           states, "unique base-three stabilization and scheduler-independent odometer",
           "KILL_ABELIAN_CARRY", before)


def smooth_successors(state):
    out = []
    for i in range(len(state) - 1):
        if state[i] >= state[i + 1] + 2:
            target = list(state)
            target[i] -= 1
            target[i + 1] += 1
            out.append(tuple(target))
    return out


def run_q03():
    before = ASSERTIONS
    analyze = dag_analyzer(smooth_successors)
    states = 0
    max_depth = 0
    terminal_counts = Counter()
    for n in range(2, 7):
        for total in range(0, 16):
            for state in comps(total, n):
                states += 1
                terminals, lengths, _, mean = analyze(state)
                check(len(terminals) == 1 and len(lengths) == 1)
                terminal = next(iter(terminals))
                depth = next(iter(lengths))
                check(all(terminal[i] <= terminal[i + 1] + 1 for i in range(n - 1)))
                check(sum(terminal) == total and mean == depth)
                for target in smooth_successors(state):
                    check(sum((i + 1) * x for i, x in enumerate(target))
                          == sum((i + 1) * x for i, x in enumerate(state)) + 1)
                terminal_counts[terminal] += 1
                max_depth = max(max_depth, depth)
    record("Q03", "directed load smoothing", "all compositions total <=15, lengths 2..6",
           states, f"confluent stabilization and fixed odometer; max depth {max_depth}, {len(terminal_counts)} targets",
           "RESERVE_ABELLANESS_GATE", before)


def pair_erosion_successors(state):
    out = []
    for i in range(len(state) - 1):
        if state[i] and state[i + 1]:
            target = list(state)
            target[i] -= 1
            target[i + 1] -= 1
            out.append(tuple(target))
    return out


def run_q04():
    before = ASSERTIONS
    analyze = dag_analyzer(pair_erosion_successors)
    distribution = terminal_distribution(pair_erosion_successors)
    states = 0
    multi = 0
    max_terminals = 0
    for n in range(2, 8):
        for state in product(range(3), repeat=n):
            states += 1
            terminals, lengths, _, mean = analyze(state)
            law = dict(distribution(state))
            check(sum(law.values(), Fraction()) == 1)
            check(set(law) == set(terminals))
            check(all(all(not (target[i] and target[i + 1]) for i in range(n - 1))
                      for target in terminals))
            check(mean >= min(lengths) and mean <= max(lengths))
            multi += len(terminals) > 1
            max_terminals = max(max_terminals, len(terminals))
    record("Q04", "adjacent pile erosion", "heights 0..2, lengths 2..7",
           states, f"exact absorbing laws; {multi} nonconfluent sources, up to {max_terminals} terminals",
           "KILL_STOCHASTIC_MATCHING_EROSION", before)


# ---------------------------------------------------------------------------
# M01--M03: classical stochastic controls


def canonical_partition(blocks):
    return tuple(sorted((tuple(sorted(block)) for block in blocks), key=lambda b: b[0]))


def partition_merge_successors(partition):
    out = []
    for i, j in combinations(range(len(partition)), 2):
        blocks = [partition[k] for k in range(len(partition)) if k not in (i, j)]
        blocks.append(tuple(sorted(partition[i] + partition[j])))
        out.append(canonical_partition(blocks))
    return out


def run_m01():
    before = ASSERTIONS
    analyze = dag_analyzer(partition_merge_successors)
    states = 0
    for n in range(1, 9):
        start = tuple((i,) for i in range(n))
        terminals, lengths, histories, mean = analyze(start)
        expected_histories = 1
        for blocks in range(n, 1, -1):
            expected_histories *= comb(blocks, 2)
        check(terminals == frozenset(((tuple(range(n)),),)))
        check(lengths == frozenset((n - 1,)) and mean == n - 1)
        check(histories == expected_histories)
        states += analyze.cache_info().currsize
    record("M01", "set-partition coalescent", "singleton starts n=1..8",
           states, "Kingman pair-merge clock and exact merger-history product",
           "KILL_KINGMAN_COALESCENT", before)


def run_m02():
    before = ASSERTIONS
    states = 0
    for n in range(1, 41):
        stationary = [Fraction(comb(n, i), 2 ** n) for i in range(n + 1)]
        check(sum(stationary, Fraction()) == 1)
        for i in range(n + 1):
            states += 1
            if i < n:
                check(stationary[i] * Fraction(n - i, n)
                      == stationary[i + 1] * Fraction(i + 1, n))
        # The sign eigenfunction certifies period two for the non-lazy chain.
        check(sum(((-1) ** i) * stationary[i] for i in range(n + 1)) == 0)
    record("M02", "birth-death Markov chain", "Ehrenfest urn with n=1..40 balls",
           states, "exact binomial reversible law and period-two parity",
           "KILL_EHRENFEST_CLASSICAL", before)


def run_m03():
    before = ASSERTIONS
    states = 0
    for n in range(2, 41):
        probability = [Fraction(i, n) for i in range(n + 1)]
        expected = [Fraction(0) for _ in range(n + 1)]
        # Solve the tridiagonal Bellman equation through first differences.
        # For p_i=q_i=i(n-i)/n^2, d_{i+1}-d_i=-1/p_i and sum d_i=0.
        increments = [Fraction(n * n, i * (n - i)) for i in range(1, n)]
        d1 = sum(Fraction(n - j, n) * increments[j - 1] for j in range(1, n))
        differences = [d1]
        for increment in increments:
            differences.append(differences[-1] - increment)
        for i in range(1, n + 1):
            expected[i] = expected[i - 1] + differences[i - 1]
        check(expected[n] == 0)
        for i in range(1, n):
            states += 1
            p = Fraction(i * (n - i), n * n)
            hold = 1 - 2 * p
            check(probability[i] == p * probability[i + 1]
                  + p * probability[i - 1] + hold * probability[i])
            check(expected[i] == 1 + p * expected[i + 1]
                  + p * expected[i - 1] + hold * expected[i])
            check(expected[i] > 0)
    record("M03", "absorbing population chain", "neutral Moran counts n=2..40",
           states, "fixation probability i/n and exact Bellman absorption means",
           "KILL_MORAN_CLASSICAL", before)


def main():
    runners = (
        run_r01, run_r02, run_r03, run_r04, run_r05, run_r06, run_r07,
        run_r08, run_r09, run_p01, run_p02, run_p03, run_p04, run_p05,
        run_p06, run_g01, run_g02, run_g03, run_g04, run_g05, run_q01,
        run_q02, run_q03, run_q04, run_m01, run_m02, run_m03,
    )
    for runner in runners:
        runner()
    check(len(RESULTS) == 27, "literal system count changed")
    check(len({result["code"] for result in RESULTS}) == 27, "duplicate code")
    check(sum(result["assertions"] for result in RESULTS) == ASSERTIONS - 2,
          "assertion ledger mismatch")
    check(sum(result["states"] for result in RESULTS) > 1_000_000,
          "breadth floor lost")

    print("STOCHASTIC_LOCAL_REWRITE_SCOUT_V1")
    for result in RESULTS:
        print(
            "|".join(
                (
                    result["code"],
                    result["family"],
                    result["scope"],
                    f"states={result['states']}",
                    f"assertions={result['assertions']}",
                    result["decision"],
                    result["signal"],
                )
            )
        )
    print(f"SYSTEMS={len(RESULTS)}")
    print(f"ENUMERATED_OR_DP_STATES={sum(result['states'] for result in RESULTS)}")
    print(f"SYSTEM_ASSERTIONS={sum(result['assertions'] for result in RESULTS)}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("EXACT_ARITHMETIC=integers+fractions.Fraction")
    print("FLOATING_POINT=none")
    print("SAMPLING=none")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
