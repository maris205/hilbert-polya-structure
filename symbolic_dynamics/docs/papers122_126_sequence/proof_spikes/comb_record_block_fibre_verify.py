#!/usr/bin/env python3
"""Independent verifier for record-block reversal and its fibre DP."""

from collections import Counter
from itertools import permutations


ASSERTIONS = 0


def check(statement, context):
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(context)


def blocks(word):
    if not word:
        return ()
    starts = []
    maximum = -1
    for i, value in enumerate(word):
        if value > maximum:
            starts.append(i)
            maximum = value
    starts.append(len(word))
    return tuple(word[starts[i] : starts[i + 1]] for i in range(len(starts) - 1))


def step(word):
    result = []
    for block in blocks(word):
        result.extend(reversed(block) if len(block) % 2 == 0 else block)
    return tuple(result)


def fibre_dp(word):
    n = len(word)
    if not n:
        return 1
    prefix_max = []
    current = -1
    for value in word:
        current = max(current, value)
        prefix_max.append(current)
    dp = [0] * (n + 1)
    dp[0] = 1
    for j in range(1, n + 1):
        for i in range(j):
            length = j - i
            admissible = (
                length % 2 == 1 and word[i] == prefix_max[j - 1]
            ) or (
                length % 2 == 0 and word[j - 1] == prefix_max[j - 1]
            )
            if admissible:
                dp[j] += dp[i]
    return dp[n]


def reconstructed_preimages(word):
    n = len(word)
    if not n:
        return {()}
    prefix_max = []
    current = -1
    for value in word:
        current = max(current, value)
        prefix_max.append(current)
    answer = set()

    def visit(start, pieces):
        if start == n:
            candidate = tuple(value for piece in pieces for value in piece)
            answer.add(candidate)
            return
        for end in range(start + 1, n + 1):
            length = end - start
            segment = word[start:end]
            if length % 2:
                admissible = word[start] == prefix_max[end - 1]
                preimage_piece = segment
            else:
                admissible = word[end - 1] == prefix_max[end - 1]
                preimage_piece = tuple(reversed(segment))
            if admissible:
                visit(end, pieces + (preimage_piece,))

    visit(0, ())
    return answer


def predicted_fixed(n):
    if n == 0:
        return 1
    def odd_double_factorial(value):
        result = 1
        for term in range(1, value + 1, 2):
            result *= term
        return result
    if n % 2 == 0:
        return odd_double_factorial(n - 1) ** 2
    return odd_double_factorial(n) * odd_double_factorial(n - 2)


def main():
    rows = []
    for n in range(10):
        universe = tuple(permutations(range(n)))
        literal = Counter(step(word) for word in universe)
        fixed = 0
        image = 0
        maximum_fibre = 0
        for word in universe:
            reconstructed = reconstructed_preimages(word)
            check(all(step(candidate) == word for candidate in reconstructed), (n, word, "reconstruction"))
            check(len(reconstructed) == fibre_dp(word), (n, word, "cut DP"))
            check(len(reconstructed) == literal[word], (n, word, "literal fibre"))
            check((fibre_dp(word) > 0) == (word in literal), (n, word, "image"))
            fixed += step(word) == word
            image += literal[word] > 0
            maximum_fibre = max(maximum_fibre, literal[word])
        check(fixed == predicted_fixed(n), (n, "fixed", fixed))
        check(sum(literal.values()) == len(universe), (n, "mass"))
        rows.append((n, len(universe), fixed, image, maximum_fibre))
    print("record-block reversal fibre verifier: PASS")
    print(f"assertions={ASSERTIONS}")
    print("n states fixed image maximum_fibre")
    for row in rows:
        print(*row)


if __name__ == "__main__":
    main()
