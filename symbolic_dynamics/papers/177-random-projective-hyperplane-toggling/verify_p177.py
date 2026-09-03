#!/usr/bin/env python3
"""Paper-local author-side exact falsifier for P177.

This verifier is deliberately organized around the frozen theorem contracts,
not around the earlier breadth-scout candidate ledger.  It imports no project
modules.  Every calculation uses integers or ``fractions.Fraction``.

Finite enumeration is counterexample pressure only.  It neither proves the
all-dimension statements nor supplies novelty or release authority.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import product


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def dot(a: int, x: int) -> int:
    return (a & x).bit_count() & 1


class ProjectiveToggleModel:
    """Literal F_2 projective-hyperplane toggle model in bit-mask form."""

    def __init__(self, d: int) -> None:
        self.d = d
        self.q = 1 << d
        self.N = self.q - 1
        self.m = self.N
        self.points = tuple(range(1, self.q))
        self.full = (1 << self.m) - 1
        self.code = tuple(self._evaluation_word(a) for a in range(self.q))
        self.hyperplanes = tuple(
            self.full ^ self.code[a] for a in range(1, self.q)
        )
        self.W = tuple(
            sorted({(epsilon * self.full) ^ self.code[a]
                    for epsilon in (0, 1) for a in range(self.q)})
        )

    def _evaluation_word(self, form: int) -> int:
        word = 0
        for position, x in enumerate(self.points):
            if dot(form, x):
                word |= 1 << position
        return word

    def sigma(self, subset_mask: int) -> int:
        answer = 0
        for position, x in enumerate(self.points):
            if (subset_mask >> position) & 1:
                answer ^= x
        return answer

    def canonical_coset(self, state: int) -> int:
        return min(state ^ word for word in self.W)

    def step(self, state: int, form: int) -> int:
        check(1 <= form < self.q, "step form is nonzero")
        return state ^ self.hyperplanes[form - 1]

    def coordinates(self, word: int) -> tuple[int, int]:
        for epsilon in (0, 1):
            candidate = word ^ (epsilon * self.full)
            for a, codeword in enumerate(self.code):
                if candidate == codeword:
                    return epsilon, a
        raise AssertionError("word is not in W")


def history_formula(model: ProjectiveToggleModel, t: int, total: int) -> int:
    sign = -1 if t & 1 else 1
    if total == 0:
        return (model.N**t + model.N * sign) // model.q
    return (model.N**t - sign) // model.q


def audit_geometry(d: int) -> None:
    model = ProjectiveToggleModel(d)
    check(len(set(model.code)) == model.q, f"simplex injective d={d}")
    check(model.code[0] == 0, f"zero codeword d={d}")
    check(model.full not in model.code, f"one outside code d={d}")
    check(len(model.W) == 2 * model.q, f"W cardinality d={d}")

    for a in range(model.q):
        for b in range(model.q):
            check(model.code[a] ^ model.code[b] == model.code[a ^ b],
                  f"code linearity d={d} a={a} b={b}")
    for form in range(1, model.q):
        h = model.hyperplanes[form - 1]
        check(h == model.full ^ model.code[form],
              f"hyperplane complement word d={d} form={form}")
        check(h.bit_count() == (1 << (d - 1)) - 1,
              f"projective hyperplane size d={d} form={form}")
        check(h.bit_count() & 1 == 1,
              f"odd generator weight d={d} form={form}")
    check(len(set(model.hyperplanes)) == model.N,
          f"distinct sampled masks d={d}")

    reached = {0}
    frontier = deque([0])
    while frontier:
        word = frontier.popleft()
        for h in model.hyperplanes:
            nxt = word ^ h
            if nxt not in reached:
                reached.add(nxt)
                frontier.append(nxt)
    check(reached == set(model.W), f"generators span W d={d}")


def audit_crown_component(d: int) -> None:
    model = ProjectiveToggleModel(d)
    coordinate_to_word = {
        (epsilon, a): (epsilon * model.full) ^ model.code[a]
        for epsilon in (0, 1) for a in range(model.q)
    }
    check(len(coordinate_to_word) == 2 * model.q,
          f"unique W coordinates d={d}")
    for coordinate, word in coordinate_to_word.items():
        check(model.coordinates(word) == coordinate,
              f"coordinate inverse d={d} coordinate={coordinate}")

    for epsilon in (0, 1):
        for a in range(model.q):
            word = coordinate_to_word[epsilon, a]
            actual = {
                model.coordinates(word ^ h)
                for h in model.hyperplanes
            }
            expected = {
                (epsilon ^ 1, b) for b in range(model.q) if b != a
            }
            check(actual == expected,
                  f"crown neighborhood d={d} vertex={(epsilon, a)}")
            check(len(actual) == model.N,
                  f"support degree d={d} vertex={(epsilon, a)}")

    # Connectedness and exact period-two witnesses are checked from support.
    seen = {0}
    frontier = deque([0])
    while frontier:
        word = frontier.popleft()
        for h in model.hyperplanes:
            nxt = word ^ h
            if nxt not in seen:
                seen.add(nxt)
                frontier.append(nxt)
    check(seen == set(model.W), f"component connected d={d}")
    for word in model.W:
        check(all(((word ^ h).bit_count() - word.bit_count()) & 1
                  for h in model.hyperplanes),
              f"each edge flips parity d={d} word={word}")
        h = model.hyperplanes[0]
        check((word ^ h) ^ h == word,
              f"two-step return d={d} word={word}")


def audit_full_carrier(d: int) -> None:
    model = ProjectiveToggleModel(d)
    total_states = 1 << model.m
    classes: dict[int, list[int]] = defaultdict(list)
    for state in range(total_states):
        classes[model.canonical_coset(state)].append(state)
    expected_classes = 1 << (model.m - d - 1)
    check(len(classes) == expected_classes, f"class count d={d}")
    check(sum(map(len, classes.values())) == total_states,
          f"class partition d={d}")
    for representative, states in classes.items():
        state_set = set(states)
        check(len(states) == 2 * model.q,
              f"class size d={d} rep={representative}")
        check(state_set == {representative ^ word for word in model.W},
              f"class is W coset d={d} rep={representative}")
        even = sum(state.bit_count() % 2 == 0 for state in states)
        check(even == model.q and len(states) - even == model.q,
              f"balanced bipartition d={d} rep={representative}")
        for state in states:
            neighbors = {state ^ h for h in model.hyperplanes}
            check(len(neighbors) == model.N,
                  f"degree d={d} state={state}")
            check(neighbors <= state_set,
                  f"closed class d={d} state={state}")
            check(all(state in {neighbor ^ h for h in model.hyperplanes}
                      for neighbor in neighbors),
                  f"symmetric support d={d} state={state}")


def audit_history_counts(d: int, max_t: int) -> None:
    model = ProjectiveToggleModel(d)
    counts = [0] * model.q
    counts[0] = 1
    for t in range(max_t + 1):
        check(sum(counts) == model.N**t, f"history mass d={d} t={t}")
        for total, actual in enumerate(counts):
            check(actual == history_formula(model, t, total),
                  f"history formula d={d} t={t} L={total}")
            increment = ((t & 1) * model.full) ^ model.code[total]
            check(increment in model.W,
                  f"endpoint increment d={d} t={t} L={total}")
            check(model.coordinates(increment) == (t & 1, total),
                  f"unique endpoint coordinate d={d} t={t} L={total}")
        grand_total = sum(counts)
        counts = [grand_total - counts[total] for total in range(model.q)]


def audit_literal_histories(d: int, max_t: int) -> None:
    model = ProjectiveToggleModel(d)
    selected_starts = [0, model.full, model.code[1]]
    if d <= 3:
        selected_starts = list(range(1 << model.m))
    for t in range(max_t + 1):
        by_total = Counter()
        by_increment = Counter()
        for forms in product(range(1, model.q), repeat=t):
            total = 0
            increment = 0
            for form in forms:
                total ^= form
                increment ^= model.hyperplanes[form - 1]
            by_total[total] += 1
            by_increment[increment] += 1
            expected_increment = ((t & 1) * model.full) ^ model.code[total]
            check(increment == expected_increment,
                  f"literal history endpoint d={d} t={t} forms={forms}")
        check(sum(by_total.values()) == model.N**t,
              f"literal history mass d={d} t={t}")
        for total in range(model.q):
            count = history_formula(model, t, total)
            increment = ((t & 1) * model.full) ^ model.code[total]
            check(by_total[total] == count,
                  f"literal total count d={d} t={t} L={total}")
            check(by_increment[increment] == count,
                  f"literal endpoint count d={d} t={t} L={total}")
            for start in selected_starts:
                endpoint = start ^ increment
                check((start ^ endpoint) == increment,
                      f"translated endpoint d={d} t={t} A={start} L={total}")


def audit_total_variation(d: int, max_t: int) -> None:
    model = ProjectiveToggleModel(d)
    phase_uniform = Fraction(1, model.q)
    for t in range(1, max_t + 1):
        probabilities = [
            Fraction(history_formula(model, t, total), model.N**t)
            for total in range(model.q)
        ]
        check(sum(probabilities) == 1, f"phase probability mass d={d} t={t}")
        check(all(probability >= 0 for probability in probabilities),
              f"phase probability positivity d={d} t={t}")
        tv = sum(abs(probability - phase_uniform)
                 for probability in probabilities) / 2
        expected = Fraction(1, model.q * model.N ** (t - 1))
        check(tv == expected, f"phase TV d={d} t={t}")
        # The ordinary stationary law on a component is uniform on 2q states.
        # Embed the time-t law in its occupied parity half and compute that TV.
        stationary = Fraction(1, 2 * model.q)
        ordinary_tv = (
            sum(abs(probability - stationary) for probability in probabilities)
            + model.q * stationary
        ) / 2
        expected_ordinary = (
            Fraction(1, 2) + Fraction(1, 2 * model.q)
            if t == 1 else Fraction(1, 2)
        )
        check(ordinary_tv == expected_ordinary,
              f"ordinary periodic TV d={d} t={t}")
        check(ordinary_tv >= Fraction(1, 2),
              f"no ordinary TV mixing d={d} t={t}")


def audit_fourier_spectrum(d: int) -> None:
    model = ProjectiveToggleModel(d)
    multiplicity = Counter()
    fibre = Counter()
    for subset in range(1 << model.m):
        sigma = model.sigma(subset)
        parity = subset.bit_count() & 1
        numerator = sum(
            -1 if (subset & h).bit_count() & 1 else 1
            for h in model.hyperplanes
        )
        if sigma == 0:
            expected = model.N * (-1 if parity else 1)
        else:
            expected = -(-1 if parity else 1)
        check(numerator == expected,
              f"Fourier eigenvalue d={d} S={subset}")
        eigenvalue = Fraction(numerator, model.N)
        multiplicity[eigenvalue] += 1
        fibre[parity, sigma] += 1

    K = 1 << (model.m - d - 1)
    expected_multiplicity = {
        Fraction(1): K,
        Fraction(-1): K,
        Fraction(1, model.N): model.N * K,
        Fraction(-1, model.N): model.N * K,
    }
    check(multiplicity == expected_multiplicity,
          f"global spectral multiplicities d={d}")
    check(sum(multiplicity.values()) == 1 << model.m,
          f"global spectral mass d={d}")
    for parity in (0, 1):
        for sigma in range(model.q):
            check(fibre[parity, sigma] == K,
                  f"rank fibre d={d} parity={parity} sigma={sigma}")


def audit_reconstruction(d: int) -> None:
    model = ProjectiveToggleModel(d)
    observed_degree = len(set(model.hyperplanes))
    reconstructed_q = observed_degree + 1
    check(reconstructed_q & (reconstructed_q - 1) == 0,
          f"degree plus one power of two d={d}")
    reconstructed_d = reconstructed_q.bit_length() - 1
    check(reconstructed_d == d, f"recover d d={d}")
    total_states = 1 << model.m
    reconstructed_K = total_states // (2 * reconstructed_q)
    check(reconstructed_K == 1 << (model.m - d - 1),
          f"recover class count d={d}")


def audit_history_support_boundaries(d: int) -> None:
    """Make the two zero-count phase coordinates explicit."""
    model = ProjectiveToggleModel(d)
    check(history_formula(model, 0, 1) == 0,
          f"zero-step nonzero L has no history d={d}")
    check(history_formula(model, 1, 0) == 0,
          f"one-step zero L has no history d={d}")
    check(all(history_formula(model, t, total) > 0
              for t in range(2, 17) for total in range(model.q)),
          f"all phase coordinates supported from time two d={d}")


def audit_excluded_boundary() -> None:
    model = ProjectiveToggleModel(1)
    check(model.N == 1 and model.m == 1, "d=1 carrier")
    check(model.hyperplanes == (0,), "d=1 sampled hyperplane empty")
    for state in range(2):
        check(model.step(state, 1) == state, f"d=1 identity state={state}")


def main() -> None:
    print("P177 PAPER-LOCAL EXACT CONTROL")
    print("lifecycle=HOLD_EXTERNAL owner=OWNER_AMBER")

    for d in range(2, 9):
        audit_geometry(d)
        audit_crown_component(d)
        audit_history_counts(d, max_t=16)
        audit_history_support_boundaries(d)
        audit_total_variation(d, max_t=16)
        audit_reconstruction(d)
        print(f"algebra d={d} q={1<<d} degree={(1<<d)-1} PASS")

    for d in range(2, 5):
        audit_full_carrier(d)
        audit_fourier_spectrum(d)
        audit_literal_histories(d, max_t=5)
        print(f"literal d={d} states={1<<((1<<d)-1)} spectrum+histories PASS")

    audit_excluded_boundary()
    print("theorem=communicating_cosets_and_crown_support PASS")
    print("theorem=every_time_every_target_kernel PASS")
    print("theorem=parity_phase_total_variation PASS")
    print("theorem=full_four_point_spectrum PASS")
    print("theorem=component_parameter_reconstruction PASS")
    print("boundary=d1_identity_excluded PASS")
    print("boundary=history_support_t0_t1_and_t_ge_2 PASS")
    print(f"exact_assertions={ASSERTIONS}")
    print("status=PASS")
    print("external_status=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
