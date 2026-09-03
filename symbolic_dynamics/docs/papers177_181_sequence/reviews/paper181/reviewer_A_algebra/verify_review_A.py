#!/usr/bin/env python3
"""Independent hostile verifier for P181.

Permutations are states numbered by their factoradic ranks.  The graph is
analysed as two flat integer arrays: a forward map and a target-sorted edge
list.  Cycle vertices are found by indegree peeling and all tail distances by
reverse breadth-first propagation.  No author/scout module or tuple-keyed
incoming/orbit implementation is imported.

Finite boxes are counterexample pressure, not an all-n proof or an ownership
search.
"""

from __future__ import annotations

from collections import Counter, deque
from math import factorial


ASSERTIONS = 0


def require(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def unrank_permutation(n: int, code: int) -> tuple[int, ...]:
    require(0 <= code < factorial(n), f"factoradic code range n={n}")
    available = list(range(1, n + 1))
    word: list[int] = []
    residual = code
    for remaining in range(n, 0, -1):
        block = factorial(remaining - 1)
        digit, residual = divmod(residual, block)
        word.append(available.pop(digit))
    require(residual == 0 and not available, f"factoradic exhaustion n={n}")
    return tuple(word)


def rank_permutation(word: tuple[int, ...]) -> int:
    n = len(word)
    available = list(range(1, n + 1))
    code = 0
    for position, value in enumerate(word):
        require(value in available, f"permutation alphabet n={n}")
        digit = available.index(value)
        code += digit * factorial(n - position - 1)
        available.pop(digit)
    require(not available, f"permutation consumed n={n}")
    return code


def descent_index(word: tuple[int, ...]) -> int | None:
    """Zero-based index of the left entry in the first descent."""
    for index in range(len(word) - 1):
        if word[index] > word[index + 1]:
            return index
    return None


def fdr_word(word: tuple[int, ...]) -> tuple[int, ...]:
    index = descent_index(word)
    if index is None:
        return word
    length = index + 2
    return tuple(reversed(word[:length])) + word[length:]


def first_sort_word(word: tuple[int, ...]) -> tuple[int, ...]:
    """Project Euler 523 update: move the first-descent follower to front."""
    index = descent_index(word)
    if index is None:
        return word
    follower = word[index + 1]
    return (follower,) + word[: index + 1] + word[index + 2 :]


def starts_ascent(word: tuple[int, ...]) -> bool:
    return len(word) >= 2 and word[0] < word[1]


def peak_at_two(word: tuple[int, ...]) -> bool:
    return len(word) >= 3 and word[0] < word[1] > word[2]


def run_from_position_two(word: tuple[int, ...]) -> int:
    require(len(word) >= 2, "decreasing-run domain")
    run = 1
    while run + 1 < len(word) and word[run] > word[run + 1]:
        run += 1
    return run


def reverse_prefix(word: tuple[int, ...], length: int) -> tuple[int, ...]:
    require(1 <= length <= len(word), "legal prefix length")
    return tuple(reversed(word[:length])) + word[length:]


def expected_predecessor_codes(word: tuple[int, ...]) -> tuple[int, ...]:
    n = len(word)
    if n == 1:
        return (0,)
    if not starts_ascent(word):
        return ()
    run = run_from_position_two(word)
    sources = {
        rank_permutation(reverse_prefix(word, length))
        for length in range(2, run + 2)
    }
    if word == tuple(range(1, n + 1)):
        sources.add(0)
    return tuple(sorted(sources))


def flat_reverse_graph(
    transition: list[int],
) -> tuple[list[int], list[int], list[int]]:
    """Return indegrees, cumulative offsets, and target-sorted sources."""
    size = len(transition)
    indegree = [0] * size
    for target in transition:
        indegree[target] += 1
    offsets = [0] * (size + 1)
    for target in range(size):
        offsets[target + 1] = offsets[target] + indegree[target]
    cursor = offsets[:-1].copy()
    sources = [0] * size
    for source, target in enumerate(transition):
        sources[cursor[target]] = source
        cursor[target] += 1
    for target in range(size):
        lo, hi = offsets[target], offsets[target + 1]
        sources[lo:hi] = sorted(sources[lo:hi])
    return indegree, offsets, sources


def peel_and_measure_depths(
    transition: list[int], offsets: list[int], sources: list[int]
) -> tuple[set[int], list[int]]:
    """Find cycle states by Kahn peeling, then reverse-BFS all tail depths."""
    size = len(transition)
    residual_indegree = [0] * size
    for target in transition:
        residual_indegree[target] += 1
    queue = deque(i for i, degree in enumerate(residual_indegree) if degree == 0)
    while queue:
        source = queue.popleft()
        target = transition[source]
        residual_indegree[target] -= 1
        if residual_indegree[target] == 0:
            queue.append(target)

    recurrent = {i for i, degree in enumerate(residual_indegree) if degree > 0}
    depth = [-1] * size
    queue = deque(sorted(recurrent))
    for state in recurrent:
        depth[state] = 0
    while queue:
        target = queue.popleft()
        for cursor in range(offsets[target], offsets[target + 1]):
            source = sources[cursor]
            if depth[source] < 0:
                depth[source] = depth[target] + 1
                queue.append(source)
    require(all(value >= 0 for value in depth), "reverse BFS covers graph")
    return recurrent, depth


def theoretical_run_histogram(n: int) -> Counter[int]:
    """Count exact decreasing-run lengths among ascent-starting targets."""
    at_least = {
        k: factorial(n) * k // factorial(k + 1) for k in range(1, n)
    }
    result: Counter[int] = Counter()
    for k in range(1, n):
        result[k] = at_least[k] - at_least.get(k + 1, 0)
    return +result


def theoretical_fibre_histogram(n: int) -> Counter[int]:
    if n == 1:
        return Counter({1: 1})
    result: Counter[int] = Counter({0: factorial(n) // 2})
    runs = theoretical_run_histogram(n)
    result.update(runs)
    # The identity has run one but gains its fixed predecessor.
    result[1] -= 1
    result[2] += 1
    return +result


def expected_maximizers(words: list[tuple[int, ...]], n: int) -> set[int]:
    if n == 1:
        return {0}
    if n == 2:
        return {0}
    result = {
        code
        for code, word in enumerate(words)
        if word[1] == n
        and all(word[position] > word[position + 1]
                for position in range(1, n - 1))
    }
    if n == 3:
        result.add(0)
    return result


def audit_size(n: int) -> tuple[int, int, Counter[int], int, int, Counter[int]]:
    size = factorial(n)
    words = [unrank_permutation(n, code) for code in range(size)]
    for code, word in enumerate(words):
        require(rank_permutation(word) == code, f"rank/unrank n={n} code={code}")

    transition = [rank_permutation(fdr_word(word)) for word in words]
    indegree, offsets, reverse_sources = flat_reverse_graph(transition)
    recurrent, depths = peel_and_measure_depths(transition, offsets, reverse_sources)
    identity = tuple(range(1, n + 1))

    for source, word in enumerate(words):
        target_word = words[transition[source]]
        index = descent_index(word)
        if index is None:
            require(word == identity and transition[source] == source,
                    f"unique descent-free fixed point n={n}")
        else:
            expected_word = tuple(reversed(word[: index + 2])) + word[index + 2 :]
            require(target_word == expected_word,
                    f"literal plus-one prefix n={n} source={source}")
            require(n < 2 or starts_ascent(target_word),
                    f"nonfixed output ascent n={n} source={source}")

        first_sort = first_sort_word(word)
        if index is None or index == 0:
            require(first_sort == target_word,
                    f"First Sort equality boundary n={n} source={source}")
        else:
            require(first_sort != target_word,
                    f"First Sort strict separation n={n} source={source}")

    actual_image = {code for code, degree in enumerate(indegree) if degree > 0}
    expected_image = (
        {0} if n == 1 else
        {code for code, word in enumerate(words) if starts_ascent(word)}
    )
    require(actual_image == expected_image, f"exact image n={n}")
    if n >= 2:
        require(len(actual_image) == size // 2, f"half image n={n}")

    for target, word in enumerate(words):
        actual = tuple(reverse_sources[offsets[target] : offsets[target + 1]])
        predicted = expected_predecessor_codes(word)
        require(actual == predicted, f"complete target fibre n={n} target={target}")
        require(indegree[target] == len(predicted),
                f"target fibre cardinality n={n} target={target}")
        for source in predicted:
            require(transition[source] == target,
                    f"predicted source returns n={n} target={target}")

    if n == 1:
        expected_recurrent = {0}
        expected_depths = Counter({0: 1})
    elif n == 2:
        expected_recurrent = {0}
        expected_depths = Counter({0: 1, 1: 1})
    else:
        expected_recurrent = {0} | {
            code for code, word in enumerate(words) if peak_at_two(word)
        }
        expected_depths = Counter({
            0: size // 3 + 1,
            1: size // 2,
            2: size // 6 - 1,
        })
        expected_depths = +expected_depths

    require(recurrent == expected_recurrent, f"exact recurrent core n={n}")
    actual_depths = Counter(depths)
    require(actual_depths == expected_depths, f"tail census n={n}")
    require(max(depths) <= (0 if n == 1 else 1 if n == 2 else 2),
            f"sharp depth ceiling n={n}")

    cycle_pairs: set[tuple[int, int]] = set()
    for state in recurrent:
        partner = transition[state]
        require(partner in recurrent, f"cycle invariance n={n} state={state}")
        require(transition[partner] == state,
                f"period divides two n={n} state={state}")
        if state == 0:
            require(partner == state, f"identity fixed n={n}")
        else:
            require(n >= 3 and peak_at_two(words[state]) and partner != state,
                    f"nontrivial recurrent peak n={n} state={state}")
            cycle_pairs.add(tuple(sorted((state, partner))))
    expected_pair_count = 0 if n < 3 else size // 6
    require(len(cycle_pairs) == expected_pair_count, f"two-cycle count n={n}")

    if n >= 3:
        for source, depth in enumerate(depths):
            if depth == 2:
                middle = transition[source]
                require(source not in actual_image and middle in actual_image,
                        f"depth-two crosses half-image n={n} source={source}")
                require(middle not in recurrent and transition[middle] in recurrent,
                        f"depth-two lands via noncore image n={n} source={source}")
            elif depth == 1:
                require(transition[source] in recurrent,
                        f"depth-one enters core n={n} source={source}")

    if n >= 2:
        actual_runs = Counter(
            run_from_position_two(word)
            for word in words if starts_ascent(word)
        )
        require(actual_runs == theoretical_run_histogram(n),
                f"decreasing-run histogram n={n}")

    actual_fibres = Counter(indegree)
    expected_fibres = theoretical_fibre_histogram(n)
    require(actual_fibres == expected_fibres, f"fibre histogram n={n}")
    maximum = max(indegree)
    maximizers = {code for code, degree in enumerate(indegree) if degree == maximum}
    predicted_maximizers = expected_maximizers(words, n)
    expected_maximum = 1 if n == 1 else 2 if n in (2, 3) else n - 1
    require(maximum == expected_maximum, f"maximum fibre n={n}")
    require(maximizers == predicted_maximizers, f"all maximizers n={n}")
    if n >= 4:
        require(len(maximizers) == n - 1, f"maximizer count n={n}")

    if n == 1:
        require(transition == [0] and indegree == [1], "S1 boundary atlas")
    if n == 2:
        require(transition == [0, 0] and indegree == [2, 0], "S2 boundary atlas")
    if n == 3:
        require(transition == [0, 3, 0, 1, 1, 3], "S3 boundary atlas")

    return (
        size,
        len(actual_image),
        actual_depths,
        maximum,
        len(maximizers),
        actual_fibres,
    )


def compact_counter(counter: Counter[int]) -> str:
    return ",".join(f"{key}:{counter[key]}" for key in sorted(counter))


def main() -> None:
    print("P181 REVIEW-A FACTORADIC EDGE AUDIT")
    print("representation=factoradic_codes graph=indegree_peeling_plus_reverse_BFS")
    for n in range(1, 10):
        size, image, tails, maximum, maximizers, fibres = audit_size(n)
        print(
            f"n={n} states={size} image={image} tails={compact_counter(tails)} "
            f"max_fibre={maximum} maximizers={maximizers} "
            f"fibre_hist={compact_counter(fibres)} PASS"
        )
    print("literal=reverse_through_first_descent_follower PASS")
    print("image=exact_half_for_n_ge_2 PASS")
    print("recurrent=identity_plus_peak_two_cycles PASS")
    print("depth=zero_one_two_census PASS")
    print("inverse=decreasing_run_full_sets_and_histogram PASS")
    print("maximizers=all_targets_with_n1_n2_n3_boundaries PASS")
    print("negative_control=Project_Euler_First_Sort_separated PASS")
    print("boundary=n1_singleton_atlas PASS")
    print(f"assertions={ASSERTIONS}")
    print("result=PASS")
    print("external_status=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
