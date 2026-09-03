#!/usr/bin/env python3
"""Independent exact hostile verifier for multiplicity-profile descent.

This file intentionally does not import ``verify_mpd.py``.  It uses decreasing
partition notation (the scout uses increasing notation internally), rebuilds
the literal map and canonical lift, and checks the theorem interfaces by
separate exhaustive routes.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path


class Ledger:
    def __init__(self) -> None:
        self.assertions = 0

    def require(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)

    def same(self, left, right, label: str) -> None:
        self.assertions += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")


Q = Ledger()


def partitions(n: int, ceiling: int | None = None):
    """Generate partitions of n as weakly decreasing positive tuples."""
    if n == 0:
        yield ()
        return
    if ceiling is None or ceiling > n:
        ceiling = n
    for first in range(ceiling, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def D(lam: tuple[int, ...]) -> tuple[int, ...]:
    """Literal update: sorted positive multiplicities of distinct parts."""
    return tuple(sorted(Counter(lam).values(), reverse=True))


def L(mu: tuple[int, ...]) -> tuple[int, ...]:
    """Canonical lift in decreasing partition notation."""
    out: list[int] = []
    for index in range(len(mu), 0, -1):
        out.extend([index] * mu[index - 1])
    return tuple(out)


def conjugate(lam: tuple[int, ...]) -> tuple[int, ...]:
    if not lam:
        return ()
    return tuple(sum(part >= column for part in lam)
                 for column in range(1, lam[0] + 1))


def contained(inner: tuple[int, ...], outer: tuple[int, ...]) -> bool:
    """Ferrers containment, with both diagrams northwest justified."""
    return len(inner) <= len(outer) and all(
        part <= outer[index] for index, part in enumerate(inner)
    )


def orbit(lam: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    path = [lam]
    seen = {lam}
    while path[-1] != (1,):
        nxt = D(path[-1])
        Q.require(sum(nxt) <= sum(path[-1]), "total cannot increase")
        Q.require(nxt not in seen, "no nontrivial cycle")
        path.append(nxt)
        seen.add(nxt)
    return tuple(path)


def depth(lam: tuple[int, ...]) -> int:
    return len(orbit(lam)) - 1


def distinct_permutations(values: tuple[int, ...]):
    counts = Counter(values)
    keys = tuple(sorted(counts, reverse=True))
    word: list[int] = []

    def visit():
        if len(word) == len(values):
            yield tuple(word)
            return
        for value in keys:
            if counts[value] == 0:
                continue
            counts[value] -= 1
            word.append(value)
            yield from visit()
            word.pop()
            counts[value] += 1

    yield from visit()


def multiply_positive_geometric(poly: list[int], step: int) -> list[int]:
    cap = len(poly) - 1
    answer = [0] * (cap + 1)
    for degree, coefficient in enumerate(poly):
        if coefficient == 0:
            continue
        for multiple in range(step, cap - degree + 1, step):
            answer[degree + multiple] += coefficient
    return answer


def fibre_series(mu: tuple[int, ...], cap: int) -> list[int]:
    """Suffix-sum product, summed over distinct multiplicity orders."""
    answer = [0] * (cap + 1)
    for alpha in distinct_permutations(mu):
        suffix: list[int] = []
        running = 0
        for entry in reversed(alpha):
            running += entry
            suffix.append(running)
        poly = [0] * (cap + 1)
        poly[0] = 1
        for step in reversed(suffix):
            poly = multiply_positive_geometric(poly, step)
        answer = [left + right for left, right in zip(answer, poly)]
    return answer


def naive_labelled_permutation_series(mu: tuple[int, ...], cap: int) -> list[int]:
    """Deliberately wrong r!-term sum, used only as an overcount sentinel."""
    answer = [0] * (cap + 1)
    for alpha in itertools.permutations(mu):
        running = 0
        suffix = []
        for entry in reversed(alpha):
            running += entry
            suffix.append(running)
        poly = [0] * (cap + 1)
        poly[0] = 1
        for step in reversed(suffix):
            poly = multiply_positive_geometric(poly, step)
        answer = [left + right for left, right in zip(answer, poly)]
    return answer


def monomial_principal_series(mu: tuple[int, ...], cap: int) -> list[int]:
    """Direct m_mu(q,q^2,...) enumeration, independent of gap products."""
    answer = [0] * (cap + 1)
    rank = len(mu)
    for positions in itertools.combinations(range(1, cap + 1), rank):
        for alpha in distinct_permutations(mu):
            degree = sum(position * exponent
                         for position, exponent in zip(positions, alpha))
            if degree <= cap:
                answer[degree] += 1
    return answer


def least_weight(mu: tuple[int, ...]) -> int:
    return sum(index * entry for index, entry in enumerate(mu, 1))


def main() -> None:
    # Canonical Levine orbit, rebuilt without consulting the scout verifier.
    canonical: dict[int, tuple[int, ...]] = {}
    state = (2,)
    for d in range(1, 11):
        canonical[d] = state
        Q.same(depth(state), d, "canonical exact depth")
        Q.same(D(L(state)), state, "D after L")
        if d < 10:
            state = L(state)
    thresholds = [sum(canonical[d]) for d in range(1, 11)]
    Q.same(thresholds,
           [2, 2, 3, 4, 7, 14, 42, 213, 2837, 175450],
           "canonical threshold prefix")

    # The two equal thresholds are a real boundary, not a strict chain.
    Q.require(not contained(canonical[1], canonical[2]),
              "Lambda_1 not contained in Lambda_2")
    Q.require(not contained(canonical[2], canonical[1]),
              "Lambda_2 not contained in Lambda_1")
    for d in range(2, 9):
        Q.require(contained(canonical[d], canonical[d + 1]),
                  "strict canonical containment from depth two")
        Q.require(canonical[d] != canonical[d + 1],
                  "canonical containment is strict")
        Q.require(sum(canonical[d]) < sum(canonical[d + 1]),
                  "thresholds strictly rise after depth two")

    exact_min: dict[int, tuple[int, list[tuple[int, ...]]]] = {}
    exact_weight_height: dict[int, int] = {}
    cap_height: dict[int, int] = {}
    depth_buckets: dict[int, list[tuple[int, ...]]] = defaultdict(list)
    state_count = 0
    fixed = []
    running_height = 0

    for size in range(1, 43):
        weight_height = 0
        for lam in partitions(size):
            state_count += 1
            profile = D(lam)
            Q.same(sum(profile), len(lam), "profile total equals source length")
            Q.same(D(L(profile)), profile, "canonical lift is a right inverse")
            Q.require(contained(L(profile), lam), "one-step Ferrers containment")

            # Tail sums are the conjugate of the lift, a second construction.
            tails = tuple(sum(profile[index:])
                          for index in range(len(profile)))
            Q.same(conjugate(L(profile)), tails,
                   "lift conjugate equals profile tail sums")

            path = orbit(lam)
            d = len(path) - 1
            depth_buckets[d].append(lam)
            weight_height = max(weight_height, d)
            running_height = max(running_height, d)
            if D(lam) == lam:
                fixed.append(lam)

            if d > 0:
                penultimate = path[-2]
                Q.same(len(penultimate), 1,
                       "last nonterminal state has one part")
                Q.require(penultimate[0] >= 2,
                          "last nonterminal singleton is at least two")
                Q.require(contained(canonical[d], lam),
                          "exact-depth state contains canonical state")

                # L^j D^j(lambda) is contained in lambda for every j.
                image = lam
                for iterate in range(1, d + 1):
                    image = D(image)
                    restored = image
                    for _ in range(iterate):
                        restored = L(restored)
                    Q.require(contained(restored, lam),
                              "iterated canonical containment")

            previous = exact_min.get(d)
            if previous is None or size < previous[0]:
                exact_min[d] = (size, [lam])
            elif size == previous[0]:
                previous[1].append(lam)

        exact_weight_height[size] = weight_height
        cap_height[size] = running_height
        predicted = max([0] + [d for d in range(1, 11)
                               if thresholds[d - 1] <= size])
        Q.same(running_height, predicted, "sharp capped height")

    Q.same(state_count, 313064, "partition census through weight 42")
    Q.same(fixed, [(1,)], "unique fixed state in exhaustive carrier")
    Q.same(exact_min[0], (1, [(1,)]), "depth-zero boundary")
    for d in range(1, 8):
        Q.same(exact_min[d], (thresholds[d - 1], [canonical[d]]),
               "unique exact-depth minimizer")

    # At-least-depth minima must be computed separately from exact minima.
    at_least: dict[int, tuple[int, list[tuple[int, ...]]]] = {}
    for lower_depth in range(1, 8):
        eligible = [lam for d, bucket in depth_buckets.items()
                    if d >= lower_depth for lam in bucket]
        minimum = min(map(sum, eligible))
        minimizers = sorted(lam for lam in eligible if sum(lam) == minimum)
        at_least[lower_depth] = (minimum, minimizers)
    Q.same(at_least[1], (2, [(1, 1), (2,)]),
           "d=1 has exactly two at-least-depth minimizers")
    for d in range(2, 8):
        Q.same(at_least[d], (thresholds[d - 1], [canonical[d]]),
               "unique at-least-depth minimizer for d at least two")

    # N=1 is explicit: a_d only exists for d>=1, so the outer {0} is needed.
    Q.same(tuple(partitions(1)), ((1,),), "N=1 carrier")
    Q.same(depth((1,)), 0, "N=1 height")
    Q.same(cap_height[1], 0, "N=1 sharp cap")
    Q.same(D((1,)), (1,), "N=1 fixed update")

    # Ferrers monotonicity of L, using a larger independent comparison pool.
    comparison_states = [lam for size in range(1, 14)
                         for lam in partitions(size)]
    comparable_pairs = 0
    for inner in comparison_states:
        for outer in comparison_states:
            if contained(inner, outer):
                comparable_pairs += 1
                Q.require(contained(L(inner), L(outer)),
                          "L preserves Ferrers containment")

    # Complete actual fibres through source weight 30.
    fibre_cap = 30
    actual: dict[tuple[int, ...], Counter[int]] = defaultdict(Counter)
    actual_sources: dict[tuple[tuple[int, ...], int], list[tuple[int, ...]]] = \
        defaultdict(list)
    sources_checked = 0
    least_sources: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for size in range(1, fibre_cap + 1):
        for source in partitions(size):
            sources_checked += 1
            target = D(source)
            actual[target][size] += 1
            actual_sources[(target, size)].append(source)

    targets_checked = 0
    repeated_targets_checked = 0
    for target_weight in range(1, 16):
        for target in partitions(target_weight):
            targets_checked += 1
            if len(set(target)) < len(target):
                repeated_targets_checked += 1
            series = fibre_series(target, fibre_cap)
            Q.same(series,
                   [actual[target][degree]
                    for degree in range(fibre_cap + 1)],
                   "every-target fibre series")
            minimum = least_weight(target)
            support = [degree for degree, coefficient in enumerate(series)
                       if coefficient]
            if minimum <= fibre_cap:
                Q.same(min(support), minimum, "least source size")
                Q.same(series[minimum], 1, "unique least-source coefficient")
                least_sources[target] = actual_sources[(target, minimum)]
                Q.same(least_sources[target], [L(target)],
                       "canonical lift is unique least source")
            else:
                Q.same(support, [], "no source below canonical weight")
            for cap in range(1, fibre_cap + 1):
                represented = any(series[:cap + 1])
                Q.same(represented, minimum <= cap,
                       "bounded image iff canonical weight fits")

    # Repeated parts: r! labelled permutations provably overcount.
    repeated = (2, 2)
    correct = fibre_series(repeated, fibre_cap)
    naive = naive_labelled_permutation_series(repeated, fibre_cap)
    Q.require(any(correct), "repeated-part target has sources")
    Q.same(naive, [2 * coefficient for coefficient in correct],
           "ordinary permutations double-count target (2,2)")

    # Direct symmetric-function specialization on a separate finite window.
    symmetric_targets = 0
    symmetric_cap = 16
    for weight in range(1, 9):
        for target in partitions(weight):
            symmetric_targets += 1
            Q.same(fibre_series(target, symmetric_cap),
                   monomial_principal_series(target, symmetric_cap),
                   "m_mu(q,q^2,...) agrees with the gap product")

    # The N=1 target fibre is also explicit, not inferred from large N.
    Q.same(fibre_series((1,), 1), [0, 1], "N=1 fibre")
    Q.same(least_weight((1,)), 1, "N=1 canonical source weight")

    payload = {
        "assertions": Q.assertions,
        "at_least_minima_1_to_7": {
            str(d): [at_least[d][0], [list(lam) for lam in at_least[d][1]]]
            for d in range(1, 8)
        },
        "canonical_states_1_to_8": {
            str(d): list(canonical[d]) for d in range(1, 9)
        },
        "cap_height_1_to_42": cap_height,
        "comparable_pairs_checked": comparable_pairs,
        "decision": "KILL_DIRECT_FREQUENCY_DEPTH_OWNER",
        "exact_weight_height_1_to_42": exact_weight_height,
        "external_status": "HOLD_EXTERNAL",
        "fibre_cap": fibre_cap,
        "latest_lift_owner": "arXiv:2602.10992v2",
        "literal_map": "decreasing sort of positive distinct-part multiplicities",
        "math_verdict": "PASS_AFTER_N1_HEIGHT_SYNTAX_REPAIR",
        "owner_records": [
            "OEIS A225485",
            "OEIS A225486",
            "OEIS A325258",
            "OEIS A325280",
            "OEIS A325282",
        ],
        "repeated_targets_checked": repeated_targets_checked,
        "sources_checked_for_fibres": sources_checked,
        "states_checked_for_clock": state_count,
        "symmetric_targets_checked": symmetric_targets,
        "targets_checked_for_fibres": targets_checked,
        "thresholds_1_to_10": thresholds,
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    canonical_json = json.dumps(payload, indent=2, sort_keys=True)
    payload["payload_sha256"] = hashlib.sha256(
        canonical_json.encode("utf-8")
    ).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
