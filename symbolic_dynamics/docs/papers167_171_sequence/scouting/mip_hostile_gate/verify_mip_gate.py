#!/usr/bin/env python3
"""Independent hostile verifier for minimum inverse-position feedback.

This file is deliberately self-contained and standard-library only.  It does
not import the earlier MIP scout, its canonical output, or any paper code.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)

    def equal(self, left, right, label: str) -> None:
        self.assertions += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")


A = Audit()


def mip(word: tuple[int, ...]) -> tuple[int, ...]:
    """Literal map: first position of each present symbol, else itself."""
    n = len(word)
    first: list[int | None] = [None] * n
    for position, symbol in enumerate(word):
        if first[symbol] is None:
            first[symbol] = position
    return tuple(i if first[i] is None else int(first[i]) for i in range(n))


def iterate(word: tuple[int, ...], steps: int) -> tuple[int, ...]:
    for _ in range(steps):
        word = mip(word)
    return word


def tail_period(word: tuple[int, ...]) -> tuple[int, int]:
    seen: dict[tuple[int, ...], int] = {}
    time = 0
    while word not in seen:
        seen[word] = time
        word = mip(word)
        time += 1
    return seen[word], time - seen[word]


def off_diagonal_injective(g: tuple[int, ...]) -> bool:
    values = [g[i] for i in range(len(g)) if g[i] != i]
    return len(values) == len(set(values))


def fibre_formula(g: tuple[int, ...]) -> int:
    """Compute the proposed every-target formula directly."""
    n = len(g)
    U = tuple(i for i in range(n) if g[i] != i)
    forced_values = tuple(g[i] for i in U)
    if len(forced_values) != len(set(forced_values)):
        return 0
    forced_positions = set(forced_values)
    F = tuple(i for i in range(n) if g[i] == i and i not in forced_positions)
    total = 0
    for mask in range(1 << len(F)):
        present = list(U)
        present.extend(F[j] for j in range(len(F)) if mask & (1 << j))
        first = {i: g[i] for i in present}
        occupied_first = set(first.values())
        term = 1
        for position in range(n):
            if position in occupied_first:
                continue
            choices = sum(first[i] < position for i in present)
            term *= choices
            if term == 0:
                break
        total += term
    return total


def path_map(order: tuple[int, ...]) -> tuple[int, ...]:
    g = list(range(len(order)))
    for j in range(1, len(order)):
        g[order[j]] = order[j - 1]
    return tuple(g)


def predicted_path_update(order: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    if len(order) == 1:
        return (order,)
    if order[0] > order[1]:
        return (tuple(reversed(order)),)
    return ((order[0],), tuple(reversed(order[1:])))


def components(g: tuple[int, ...]) -> tuple[tuple[str, tuple[int, ...]], ...]:
    """Canonical components for an off-diagonal-injective map."""
    n = len(g)
    A.check(off_diagonal_injective(g), "component parser precondition")
    child: dict[int, int] = {}
    for source, target in enumerate(g):
        if source != target:
            A.check(target not in child, "unique off-diagonal child")
            child[target] = source

    visited: set[int] = set()
    out: list[tuple[str, tuple[int, ...]]] = []
    for root in range(n):
        if g[root] != root:
            continue
        order = [root]
        visited.add(root)
        while order[-1] in child:
            nxt = child[order[-1]]
            A.check(nxt not in visited, "path cannot self-intersect")
            visited.add(nxt)
            order.append(nxt)
        out.append(("path", tuple(order)))

    for start in range(n):
        if start in visited:
            continue
        cycle = []
        cursor = start
        while cursor not in cycle:
            A.check(cursor not in visited, "cycles are disjoint")
            cycle.append(cursor)
            cursor = g[cursor]
        A.equal(cursor, start, "unvisited component closes at its start")
        minimum_index = cycle.index(min(cycle))
        cycle = cycle[minimum_index:] + cycle[:minimum_index]
        visited.update(cycle)
        out.append(("cycle", tuple(cycle)))
    A.equal(len(visited), n, "component cover")
    return tuple(sorted(out))


def partition_signature(word: tuple[int, ...]) -> tuple[int, ...]:
    """Restricted-growth signature of the word's kernel partition."""
    label_to_block: dict[int, int] = {}
    signature = []
    for symbol in word:
        if symbol not in label_to_block:
            label_to_block[symbol] = len(label_to_block)
        signature.append(label_to_block[symbol])
    return tuple(signature)


def connected_count(s: int) -> int:
    if s == 1:
        return 1
    if s == 2:
        return 1
    if s == 3:
        return 4
    return math.factorial(s - 1) + math.factorial(s) // 4


def recurrent_formula(limit: int) -> list[int]:
    values = [1]
    for n in range(1, limit + 1):
        value = 0
        for s in range(1, n + 1):
            value += math.comb(n - 1, s - 1) * connected_count(s) * values[n - s]
        values.append(value)
    return values


def involutions(limit: int) -> list[int]:
    values = [1]
    if limit >= 1:
        values.append(1)
    for n in range(2, limit + 1):
        values.append(values[n - 1] + (n - 1) * values[n - 2])
    return values


def bells(limit: int) -> list[int]:
    values = [1]
    for n in range(limit):
        values.append(sum(math.comb(n, k) * values[k] for k in range(n + 1)))
    return values


def egf_exp(coefficients: list[Fraction], limit: int) -> list[Fraction]:
    """Ordinary coefficients of exp(C(x)), from F'=C'F."""
    out = [Fraction(0) for _ in range(limit + 1)]
    out[0] = Fraction(1)
    for n in range(1, limit + 1):
        out[n] = sum(Fraction(k) * coefficients[k] * out[n - k]
                     for k in range(1, n + 1)) / n
    return out


def recurrent_egf_closed(limit: int) -> list[int]:
    # C(x)=-log(1-x)+x^3/3+x^4/(4(1-x)); expand independently.
    c = [Fraction(0) for _ in range(limit + 1)]
    for k in range(1, limit + 1):
        c[k] += Fraction(1, k)
    if limit >= 3:
        c[3] += Fraction(1, 3)
    for k in range(4, limit + 1):
        c[k] += Fraction(1, 4)
    ordinary = egf_exp(c, limit)
    return [int(ordinary[n] * math.factorial(n)) for n in range(limit + 1)]


def identity_source_from_partition(signature: tuple[int, ...]) -> tuple[int, ...]:
    minima: dict[int, int] = {}
    for position, block in enumerate(signature):
        minima.setdefault(block, position)
    return tuple(minima[block] for block in signature)


def all_rgs(n: int):
    if n == 0:
        yield ()
        return
    prefix = [0]

    def rec(position: int, maximum: int):
        if position == n:
            yield tuple(prefix)
            return
        for value in range(maximum + 2):
            prefix.append(value)
            yield from rec(position + 1, max(maximum, value))
            prefix.pop()

    yield from rec(1, 0)


def boundary_graph(n: int) -> dict[str, dict[str, object]]:
    graph: dict[str, dict[str, object]] = {}
    for word in itertools.product(range(n), repeat=n):
        tail, period = tail_period(word)
        graph["".join(map(str, word))] = {
            "image": "".join(map(str, mip(word))),
            "tail": tail,
            "period": period,
            "fibre": fibre_formula(word),
        }
    return graph


def main() -> None:
    limit_formula = 14
    expected_r = recurrent_formula(limit_formula)
    expected_r_egf = recurrent_egf_closed(limit_formula)
    expected_i = involutions(limit_formula)
    expected_b = bells(limit_formula)
    A.equal(expected_r, expected_r_egf, "component recurrence equals closed EGF")
    A.equal(expected_r[:8], [1, 1, 2, 8, 38, 220, 1540, 12460],
            "advertised recurrent prefix")
    A.equal(expected_i[1:8], [1, 2, 4, 10, 26, 76, 232],
            "advertised involution prefix")
    A.equal(expected_b[1:8], [1, 2, 5, 15, 52, 203, 877],
            "advertised Bell prefix")

    # Connected-component census and the sharp path clock are checked without
    # using the full-state enumeration below.
    component_table = {}
    path_clock_table = {}
    for s in range(1, 10):
        recurrent_paths = 0
        maximum_tail = -1
        maximizers = []
        for order in itertools.permutations(range(s)):
            g = path_map(order)
            actual = mip(g)
            predicted_components = predicted_path_update(order)
            predicted_map = list(range(s))
            for path in predicted_components:
                for j in range(1, len(path)):
                    predicted_map[path[j]] = path[j - 1]
            A.equal(actual, tuple(predicted_map), f"local path action s={s}")
            tail, period = tail_period(g)
            A.check(period in (1, 2), f"path terminal period s={s}")
            recurrent = (s == 1 or
                         (s >= 3 and order[0] > order[1]
                          and order[-1] > order[-2]))
            A.equal(tail == 0, recurrent, f"path recurrence criterion s={s}")
            if recurrent:
                recurrent_paths += 1
            if tail > maximum_tail:
                maximum_tail = tail
                maximizers = [order]
            elif tail == maximum_tail:
                maximizers.append(order)
        expected_paths = 1 if s == 1 else (2 if s == 3 else
                         (math.factorial(s) // 4 if s >= 4 else 0))
        A.equal(recurrent_paths, expected_paths, f"recurrent paths s={s}")
        A.equal(maximum_tail, 0 if s == 1 else 2 * s - 2,
                f"sharp path height s={s}")
        expected_maximizer = [tuple(reversed(range(s)))] if s >= 2 else [(0,)]
        A.equal(maximizers, expected_maximizer, f"unique decreasing maximizer s={s}")
        cycles = 0
        if s >= 2:
            # Fix label 0 as the first entry to quotient cyclic rotations.
            for tail_order in itertools.permutations(range(1, s)):
                order = (0,) + tail_order
                cycle_map = [0] * s
                inverse_map = [0] * s
                for j, vertex in enumerate(order):
                    cycle_map[vertex] = order[(j + 1) % s]
                    inverse_map[vertex] = order[(j - 1) % s]
                A.equal(mip(tuple(cycle_map)), tuple(inverse_map),
                        f"cycle orientation reversal s={s}")
                A.equal(tail_period(tuple(cycle_map)),
                        (0, 1 if s == 2 else 2),
                        f"cycle dynamical period s={s}")
                cycles += 1
            A.equal(cycles, math.factorial(s - 1), f"cycle census s={s}")
        A.equal(1 if s == 1 else cycles + recurrent_paths,
                connected_count(s),
                f"connected census s={s}")
        component_table[str(s)] = {
            "cycles": cycles,
            "recurrent_paths": 0 if s == 1 else recurrent_paths,
            "connected_total": connected_count(s),
        }
        path_clock_table[str(s)] = {
            "maximum": maximum_tail,
            "maximizers": [list(x) for x in maximizers],
        }

    full_table = {}
    false_positive_image_tests = {}
    for n in range(1, 8):
        fibre_counts: Counter[tuple[int, ...]] = Counter()
        recurrent_count = 0
        fixed_count = 0
        full_maximum = -1
        full_maximizers = 0
        periodic_orbits = Counter()
        kernel_target_seen: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()

        for word in itertools.product(range(n), repeat=n):
            target = mip(word)
            fibre_counts[target] += 1
            A.check(off_diagonal_injective(target), f"first-image injection n={n}")
            # The selected least representatives give a semigroup inner inverse.
            A.equal(tuple(word[target[word[j]]] for j in range(n)), word,
                    f"f M(f) f = f, n={n}")
            krr = tuple(target[word[j]] for j in range(n))
            A.equal(tuple(krr[krr[j]] for j in range(n)), krr,
                    f"kernel representative retraction, n={n}")
            A.equal(tuple(word[j] == word[k] for j in range(n) for k in range(n)),
                    tuple(krr[j] == krr[k] for j in range(n) for k in range(n)),
                    f"KRR kernel equality, n={n}")

            tail, period = tail_period(word)
            A.check(period in (1, 2), f"global period bound n={n}")
            if tail == 0:
                recurrent_count += 1
                periodic_orbits[period] += Fraction(1, period)
            if mip(word) == word:
                fixed_count += 1
            if tail > full_maximum:
                full_maximum = tail
                full_maximizers = 1
            elif tail == full_maximum:
                full_maximizers += 1
            for k in range(1, 7):
                predicted_fixed = (tail == 0 and period == 1) if k % 2 else (tail == 0)
                A.equal(iterate(word, k) == word, predicted_fixed,
                        f"positive iterate fixed count pointwise n={n}, k={k}")

            if n <= 6:
                signature = partition_signature(word)
                key = (target, signature)
                A.check(key not in kernel_target_seen,
                        f"target forces labels for kernel partition n={n}")
                kernel_target_seen.add(key)

        image_maximum = max(tail_period(g)[0] for g in fibre_counts)
        A.equal(recurrent_count, expected_r[n], f"recurrent total n={n}")
        A.equal(fixed_count, expected_i[n], f"fixed total n={n}")
        A.equal(periodic_orbits[1], expected_i[n], f"one-cycle census n={n}")
        A.equal(periodic_orbits[2], (expected_r[n] - expected_i[n]) // 2,
                f"two-cycle census n={n}")
        A.equal(full_maximum, 0 if n == 1 else 2 * n - 2,
                f"global sharp height n={n}")
        A.equal(image_maximum, 0 if n == 1 else 2 * n - 3,
                f"image sharp height n={n}")
        if n >= 2:
            witness = tuple(range(1, n)) + (1,)
            A.equal(tail_period(witness)[0], 2 * n - 2,
                    f"displayed global witness n={n}")
            increasing_path = path_map(tuple(range(n)))
            A.equal(mip(witness), increasing_path,
                    f"displayed witness first image n={n}")
            A.equal(tail_period(increasing_path)[0], 2 * n - 3,
                    f"displayed image witness n={n}")
            decreasing_path = path_map(tuple(reversed(range(n))))
            A.equal(fibre_formula(decreasing_path), 0,
                    f"decreasing full path excluded from image n={n}")

        formula_maximum = 0
        supported_by_formula = 0
        offdiag_candidates = 0
        offdiag_but_unsupported = 0
        for g in itertools.product(range(n), repeat=n):
            exact = fibre_counts.get(g, 0)
            formula = fibre_formula(g)
            A.equal(formula, exact, f"every-target fibre formula n={n}")
            formula_maximum = max(formula_maximum, formula)
            supported_by_formula += formula > 0
            if off_diagonal_injective(g):
                offdiag_candidates += 1
                offdiag_but_unsupported += formula == 0
        A.equal(supported_by_formula, len(fibre_counts), f"exact image test n={n}")
        A.equal(formula_maximum, expected_b[n], f"Bell maximum n={n}")
        identity = tuple(range(n))
        A.equal(fibre_formula(identity), expected_b[n], f"identity Bell fibre n={n}")

        # Every set partition produces a distinct identity preimage by labelling
        # each block with its minimum.
        identity_sources = set()
        for signature in all_rgs(n):
            source = identity_source_from_partition(signature)
            A.equal(mip(source), identity, f"partition-to-identity source n={n}")
            identity_sources.add(source)
        A.equal(len(identity_sources), expected_b[n], f"Bell injection n={n}")

        # Parse every image component and independently test local dynamics.
        for g in fibre_counts:
            parsed = components(g)
            reconstructed = list(range(n))
            for kind, order in parsed:
                if kind == "path":
                    for j in range(1, len(order)):
                        reconstructed[order[j]] = order[j - 1]
                else:
                    for j, vertex in enumerate(order):
                        reconstructed[vertex] = order[(j + 1) % len(order)]
            A.equal(tuple(reconstructed), g, f"component reconstruction n={n}")
        full_table[str(n)] = {
            "states": n ** n,
            "image_size": len(fibre_counts),
            "recurrent": recurrent_count,
            "fixed": fixed_count,
            "one_cycles": int(periodic_orbits[1]),
            "two_cycles": int(periodic_orbits[2]),
            "full_height": full_maximum,
            "full_height_sources": full_maximizers,
            "image_height": image_maximum,
            "maximum_fibre": formula_maximum,
        }
        false_positive_image_tests[str(n)] = {
            "off_diagonal_injective_targets": offdiag_candidates,
            "unsupported_among_them": offdiag_but_unsupported,
        }

    # Explicit collision/adversarial targets, including fixed coordinates
    # occupied by forced off-diagonal first occurrences.
    adversaries = {
        "repeated_offdiag_n3": (1, 0, 1),
        "no_zero_value_n3": (1, 2, 2),
        "forced_fixed_absent_supported_n3": (0, 0, 2),
        "forced_fixed_absent_unsupported_n2": (1, 1),
    }
    adversary_results = {}
    for name, g in adversaries.items():
        brute = sum(mip(word) == g
                    for word in itertools.product(range(len(g)), repeat=len(g)))
        formula = fibre_formula(g)
        A.equal(formula, brute, f"adversary {name}")
        adversary_results[name] = {"target": list(g), "fibre": formula}

    result = {
        "decision": "GREEN_OWNER_THIN",
        "external_status": "HOLD_EXTERNAL",
        "literal_map": "M(f)(i)=min{j:f(j)=i}, with default i when absent",
        "assertions": A.assertions,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "formula_prefixes": {
            "recurrent_R_0_to_14": expected_r,
            "fixed_I_0_to_14": expected_i,
            "Bell_B_0_to_14": expected_b,
        },
        "connected_components_s_1_to_9": component_table,
        "path_clock_s_1_to_9": path_clock_table,
        "full_exhaustion_n_1_to_7": full_table,
        "necessary_not_sufficient_image_test": false_positive_image_tests,
        "adversarial_targets": adversary_results,
        "boundaries": {str(n): boundary_graph(n) for n in range(1, 4)},
    }
    print(json.dumps(result, indent=2, sort_keys=True, separators=(",", ": ")))


if __name__ == "__main__":
    main()
