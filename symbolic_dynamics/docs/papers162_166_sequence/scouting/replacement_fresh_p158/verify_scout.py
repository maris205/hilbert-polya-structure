#!/usr/bin/env python3
"""Exact scout for ternary modular run consolidation.

The carrier X_N is the disjoint union of all words over Z/3Z of lengths at
most N.  One update replaces each maximal constant run r^ell by the single
letter ell*r modulo 3.  This script is deterministic and dependency-free.
"""

from collections import Counter, defaultdict
from itertools import product


Q = 3
EXHAUSTIVE_LENGTH = 9
FIBRE_CAP = 8
WITNESS_CAP = 1000
assertions = 0


def check(condition, message):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(message)


def words_of_length(n):
    return product(range(Q), repeat=n)


def literal_update(word):
    """Collapse maximal constant runs, adding inside Z/3Z."""
    if not word:
        return ()
    out = []
    left = 0
    while left < len(word):
        right = left + 1
        while right < len(word) and word[right] == word[left]:
            right += 1
        out.append(((right - left) * word[left]) % Q)
        left = right
    return tuple(out)


def reference_update(word):
    """Independent group-by-change implementation of the same literal rule."""
    if not word:
        return ()
    out = []
    letter = word[0]
    length = 1
    for value in word[1:]:
        if value == letter:
            length += 1
        else:
            out.append((length * letter) % Q)
            letter = value
            length = 1
    out.append((length * letter) % Q)
    return tuple(out)


def is_fixed(word):
    return all(a != b for a, b in zip(word, word[1:]))


def orbit_depth(word):
    depth = 0
    seen = set()
    while True:
        nxt = literal_update(word)
        if nxt == word:
            return depth, word
        check(word not in seen, ("cycle", word))
        seen.add(word)
        word = nxt
        depth += 1


def sharp_witness(n):
    """The prefix of 11(21)^infinity having length n."""
    if n == 0:
        return ()
    stream = (1, 1) + (2, 1) * ((n + 1) // 2)
    return stream[:n]


def alternate_witness(n):
    """The companion prefix 22(12)^infinity."""
    if n == 0:
        return ()
    stream = (2, 2) + (1, 2) * ((n + 1) // 2)
    return stream[:n]


def path_fibre_polynomial(target, cap):
    """Return source-length coefficients from the weighted path formula."""
    if not target:
        return Counter({0: 1})
    # (last run letter, accumulated source length) -> multiplicity.
    dp = {(None, 0): 1}
    for y in target:
        nxt = defaultdict(int)
        for (last, total), multiplicity in dp.items():
            for run_letter in range(Q):
                if run_letter == last:
                    continue
                for run_length in range(1, cap - total + 1):
                    if (run_length * run_letter) % Q == y:
                        nxt[(run_letter, total + run_length)] += multiplicity
        dp = nxt
    answer = Counter()
    for (_, total), multiplicity in dp.items():
        answer[total] += multiplicity
    return answer


def min_lift_cost(target, cap):
    polynomial = path_fibre_polynomial(target, cap)
    return min(polynomial) if polynomial else None


def temporal_checks():
    rows = []
    for n in range(EXHAUSTIVE_LENGTH + 1):
        states = 0
        fixed = 0
        image = set()
        max_depth = 0
        depth_histogram = Counter()
        for word in words_of_length(n):
            states += 1
            image_value = literal_update(word)
            check(image_value == reference_update(word), ("implementations", word))
            check((image_value == word) == is_fixed(word), ("fixed", word))
            check(len(image_value) <= len(word), ("length", word))
            if image_value != word:
                check(len(image_value) < len(word), ("strict length", word))
            depth, terminal = orbit_depth(word)
            check(is_fixed(terminal), ("terminal", word, terminal))
            check(depth <= max(0, n - 1), ("clock upper", word, depth))
            image.add(image_value)
            fixed += image_value == word
            max_depth = max(max_depth, depth)
            depth_histogram[depth] += 1
        expected_fixed = 1 if n == 0 else Q * (Q - 1) ** (n - 1)
        check(states == Q**n, ("state count", n))
        check(fixed == expected_fixed, ("fixed count", n, fixed))
        check(max_depth == max(0, n - 1), ("sharp exhaustive", n, max_depth))
        rows.append((n, states, len(image), fixed, max_depth,
                     tuple(sorted(depth_histogram.items()))))

    # These two identities give an induction proof, not merely an observed
    # long orbit: A_n -> B_(n-1) -> A_(n-2) -> ... -> one letter.
    for n in range(WITNESS_CAP + 1):
        witness_a = sharp_witness(n)
        witness_b = alternate_witness(n)
        check(len(witness_a) == n, ("witness A length", n))
        check(len(witness_b) == n, ("witness B length", n))
        if n >= 2:
            check(literal_update(witness_a) == alternate_witness(n - 1),
                  ("witness A recurrence", n))
            check(literal_update(witness_b) == sharp_witness(n - 1),
                  ("witness B recurrence", n))
        else:
            check(literal_update(witness_a) == witness_a,
                  ("witness A base", n))
            check(literal_update(witness_b) == witness_b,
                  ("witness B base", n))
    return rows


def fibre_checks():
    brute = defaultdict(Counter)
    for source_length in range(FIBRE_CAP + 1):
        for source in words_of_length(source_length):
            brute[literal_update(source)][source_length] += 1

    target_count = 0
    support_count = 0
    max_fibre = 0
    max_fibre_target = None
    for target_length in range(FIBRE_CAP + 1):
        for target in words_of_length(target_length):
            target_count += 1
            formula = path_fibre_polynomial(target, FIBRE_CAP)
            actual = brute.get(target, Counter())
            for source_length in range(FIBRE_CAP + 1):
                check(formula[source_length] == actual[source_length],
                      ("fibre coefficient", target, source_length,
                       formula[source_length], actual[source_length]))
            formula_min = min(formula) if formula else None
            actual_min = min(actual) if actual else None
            check(formula_min == actual_min, ("minimum lift", target))
            check((formula_min is not None) == (target in brute),
                  ("support", target))
            support_count += target in brute
            total = sum(actual.values())
            if total > max_fibre:
                max_fibre = total
                max_fibre_target = target

    for source_length in range(FIBRE_CAP + 1):
        total = sum(counts[source_length] for counts in brute.values())
        check(total == Q**source_length, ("fibre mass", source_length, total))

    # Hand-computable boundary cases, including zero runs and repeated targets.
    examples = {
        (): {0: 1},
        (0,): {1: 1, 2: 1, 3: 3, 4: 1, 5: 1, 6: 3, 7: 1, 8: 1},
        (1,): {1: 1, 2: 1, 4: 1, 5: 1, 7: 1, 8: 1},
        (2,): {1: 1, 2: 1, 4: 1, 5: 1, 7: 1, 8: 1},
    }
    for target, expected in examples.items():
        actual = dict(path_fibre_polynomial(target, FIBRE_CAP))
        check(actual == expected, ("example", target, actual, expected))
    return target_count, support_count, max_fibre, max_fibre_target


def main():
    rows = temporal_checks()
    target_count, support_count, max_fibre, max_target = fibre_checks()
    print("Ternary modular run-consolidation exact scout")
    print("external_status=HOLD_EXTERNAL")
    print("carrier=X_N=disjoint_union_{0<=k<=N}(Z/3Z)^k")
    print("update=maximal run r^ell -> (ell*r mod 3), simultaneously")
    print(f"temporal_exhaustive=all exact lengths 0..{EXHAUSTIVE_LENGTH}")
    for n, states, image, fixed, depth, histogram in rows:
        print(f"n={n}|states={states}|image={image}|fixed={fixed}|max_depth={depth}|depth_hist={histogram}")
    print(f"sharp_witnesses=all n 0..{WITNESS_CAP}|depth=max(0,n-1)")
    print(f"fibre_cap={FIBRE_CAP}|targets={target_count}|supported={support_count}|max_fibre={max_fibre}|max_target={max_target}")
    print("fibre_formula=three-state adjacent-distinct run-letter path polynomial PASS")
    print("verdict=KILL_INTERNAL_P147_SAME_RUN_CONSOLIDATION_ENGINE")
    print(f"assertions={assertions}")


if __name__ == "__main__":
    main()
