#!/usr/bin/env python3
"""Process-separated hostile Review-A exact control for P188.

The author uses integer bit masks and a forward weak-chain enumeration.  This
reviewer uses frozensets throughout and evaluates the all-time formula by a
backwards interval-capacity transfer.  No author module is imported.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
INPUTS = {
    "papers/188-self-cardinality-truncation/main.tex":
        "f08712d1b1e43f707c1254ebf791724727e9387a5e0794dae3b5c40d4874ab39",
    "papers/188-self-cardinality-truncation/main_round0_original.pdf":
        "10b881a6200e075ed66514e8f4f8873c433383c8118c6037ad1ecd1d5bcb8bc3",
    "papers/188-self-cardinality-truncation/verify_p188.py":
        "94f4aa2b656fcbf291106b63b0b22bf2fe3ca4f5d7ac6f0dfb3dc6693be9741d",
    "papers/188-self-cardinality-truncation/CANONICAL.txt":
        "ff0457f32e495f2405f494af83f461ad6bca310d25f04923fdb413c856d245ef",
    "papers/188-self-cardinality-truncation/PROOF_PACKAGE.md":
        "6307ac2d3f7eb9b82dff1118898225c910d3647e98bd823fc6ae7fc73c785235",
    "papers/188-self-cardinality-truncation/SOURCE_VERIFICATION.md":
        "aa0ccf0a56fe33ddcd087d94f52177369da4bc19d920766c71fe67eddd20dc47",
}

ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def bind_inputs():
    for relative, expected in INPUTS.items():
        path = ROOT / relative
        check(path.is_file(), ("missing pinned input", relative))
        check(sha256(path.read_bytes()).hexdigest() == expected,
              ("pinned-input drift", relative))


@lru_cache(maxsize=None)
def subsets(n):
    states = (frozenset(),)
    for label in range(1, n + 1):
        states = states + tuple(state | {label} for state in states)
    return states


def update(state):
    cutoff = len(state)
    return frozenset(label for label in state if label <= cutoff)


def rank(state, cutoff):
    return sum(label <= cutoff for label in state)


def initial_run(state, n):
    length = 0
    while length < n and length + 1 in state:
        length += 1
    return length


def initial_segment(length):
    return frozenset(range(1, length + 1))


def orbit_tail(state):
    seen = set()
    time = 0
    while update(state) != state:
        check(state not in seen, ("nonfixed cycle", state))
        seen.add(state)
        state = update(state)
        time += 1
        check(time <= len(seen) + 1, ("orbit guard", state))
    return time, state


def iterate(state, time):
    for _ in range(time):
        state = update(state)
    return state


def target_maximum(target):
    return max(target, default=0)


@lru_cache(maxsize=None)
def backward_chain_formula(n, b, maximum, time):
    """Equation (10), evaluated from k_t=b backwards to k_0."""
    if time == 0:
        return 1
    lower = max(b, maximum)
    if time == 1:
        return sum(comb(n - k0, k0 - b)
                   for k0 in range(lower, n + 1)
                   if 0 <= k0 - b <= n - k0)

    total = 0
    for last in range(lower, n + 1):
        # Keys are the adjacent pair (k_j,k_{j+1}).
        layer = {(last, b): 1}
        for _j in range(time - 1, 0, -1):
            previous_layer = defaultdict(int)
            for (current, following), multiplicity in layer.items():
                choose = current - following
                for previous in range(current, n + 1):
                    capacity = previous - current
                    if 0 <= choose <= capacity:
                        previous_layer[(previous, current)] += (
                            multiplicity * comb(capacity, choose)
                        )
            layer = previous_layer
        for (k0, k1), multiplicity in layer.items():
            choose = k0 - k1
            if 0 <= choose <= n - k0:
                total += multiplicity * comb(n - k0, choose)
    return total


def fibonacci(index):
    previous, current = 0, 1
    for _ in range(index):
        previous, current = current, previous + current
    return previous


def pointwise_box(n):
    states = subsets(n)
    endpoint_counts = Counter()
    one_step_fibres = Counter(update(state) for state in states)
    deepest = []
    maximum_tail = -1

    for state in states:
        rho = initial_run(state, n)
        time, endpoint = orbit_tail(state)
        endpoint_counts[endpoint] += 1
        check(endpoint == initial_segment(rho),
              ("endpoint initial segment", n, state))
        check(time <= len(state) - rho, ("tail cardinality bound", n, state))

        cutoff = len(state)
        current = state
        for t in range(1, n + 3):
            expected = frozenset(label for label in state if label <= cutoff)
            current = update(current)
            check(current == expected, ("pointwise iterate", n, state, t))
            following = rank(state, cutoff)
            check(following <= cutoff, ("rank chain monotonicity", n, state, t))
            check(len(current) == following,
                  ("rank chain cardinality", n, state, t))
            cutoff = following
        check(current == initial_segment(rho),
              ("eventual endpoint after stress horizon", n, state))

        if time > maximum_tail:
            maximum_tail = time
            deepest = [state]
        elif time == maximum_tail:
            deepest.append(state)

    expected_height = max(0, n - 1)
    check(maximum_tail == expected_height, ("sharp height", n))
    if n >= 2:
        check(deepest == [frozenset(range(2, n + 1))],
              ("unique deepest state", n, deepest))
    else:
        check(set(deepest) == set(states), ("n=0/1 all fixed", n))

    image = set(one_step_fibres)
    for target in states:
        b = len(target)
        maximum = target_maximum(target)
        formula = backward_chain_formula(n, b, maximum, 1)
        check(formula == one_step_fibres[target],
              ("t=1 every-target formula", n, target))
        check((target in image) == (2 * maximum <= n + b),
              ("image criterion", n, target))
    check(sum(one_step_fibres.values()) == 2 ** n,
          ("one-step mass", n))
    check(len(image) == fibonacci(n + 2), ("Fibonacci image", n))
    check(one_step_fibres[frozenset()] == fibonacci(n + 1),
          ("empty-target Fibonacci fibre", n))
    for b in range(n + 1):
        actual_layer = sum(len(target) == b for target in image)
        check(actual_layer == comb((n + b) // 2, b),
              ("image layer", n, b))
    largest = max(one_step_fibres.values())
    check(largest == fibonacci(n + 1), ("maximum fibre size", n))
    maximizers = [target for target in states
                  if one_step_fibres[target] == largest]
    if n >= 2:
        check(maximizers == [frozenset()],
              ("empty target unique maximizer", n, maximizers))
    elif n == 1:
        check(set(maximizers) == set(states), ("n=1 tied fibres", n))
    else:
        check(maximizers == [frozenset()], ("n=0 singleton fibre", n))

    for r in range(n + 1):
        endpoint = initial_segment(r)
        expected = 1 if r == n else 2 ** (n - r - 1)
        check(endpoint_counts[endpoint] == expected,
              ("terminal basin", n, r))
    check(sum(endpoint_counts.values()) == 2 ** n,
          ("terminal mass", n))

    stable_time = max(1, n - 1)
    stabilized = Counter(iterate(state, stable_time) for state in states)
    check(set(stabilized) == {initial_segment(r) for r in range(n + 1)},
          ("stabilized image", n, stable_time))
    check(stabilized == endpoint_counts,
          ("stabilized fibres equal terminal basins", n, stable_time))
    return len(states), maximum_tail, len(image), largest, len(endpoint_counts)


def all_time_box(n):
    states = subsets(n)
    current = tuple(states)
    checks = 0
    for time in range(0, n + 3):
        actual = Counter(current)
        formula_mass = 0
        for target in states:
            if time == 0:
                formula = 1
            else:
                formula = backward_chain_formula(
                    n, len(target), target_maximum(target), time
                )
            check(formula == actual[target],
                  ("all-time every-target fibre", n, time, target))
            formula_mass += formula
            checks += 1
        check(formula_mass == 2 ** n, ("all-time mass", n, time))

        if time >= max(1, n - 1):
            for target in states:
                r = len(target)
                if target == initial_segment(r):
                    expected = 1 if r == n else 2 ** (n - r - 1)
                else:
                    expected = 0
                check(actual[target] == expected,
                      ("post-stabilization target fibre", n, time, target))
        current = tuple(update(state) for state in current)
    return len(states), checks


def boundary_attack():
    empty = frozenset()
    check(subsets(0) == (empty,), "n=0 carrier")
    check(update(empty) == empty, "n=0 fixed")
    check(backward_chain_formula(0, 0, 0, 1) == 1, "n=0 t=1 fibre")
    singleton_states = subsets(1)
    check(all(update(state) == state for state in singleton_states),
          "n=1 all fixed")
    check([backward_chain_formula(1, len(target), target_maximum(target), 1)
           for target in singleton_states] == [1, 1],
          "n=1 one-step fibres")


def main():
    bind_inputs()
    boundary_attack()

    pointwise_signatures = []
    pointwise_states = 0
    for n in range(0, 17):
        signature = pointwise_box(n)
        pointwise_signatures.append((n,) + signature)
        pointwise_states += signature[0]

    all_time_signatures = []
    all_time_states = 0
    all_time_target_checks = 0
    for n in range(0, 11):
        signature = all_time_box(n)
        all_time_signatures.append((n,) + signature)
        all_time_states += signature[0]
        all_time_target_checks += signature[1]

    print("P188_HOSTILE_REVIEW_A_EXACT_CONTROL")
    print("REPRESENTATION=frozensets_and_backward_interval_capacity_transfer")
    print(f"PINNED_INPUTS={len(INPUTS)}")
    print(f"POINTWISE_BOXES={len(pointwise_signatures)} "
          f"STATES={pointwise_states} LAST={pointwise_signatures[-1]}")
    print(f"ALL_TIME_BOXES={len(all_time_signatures)} "
          f"STATES={all_time_states} TARGET_TIME_CHECKS={all_time_target_checks} "
          f"LAST={all_time_signatures[-1]}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("CRITICAL_FINDINGS=0")
    print("MAJOR_FINDINGS=0")
    print("MINOR_FINDINGS=0")
    print("VERDICT=PROVABLE_AS_STATED")
    print("FINITE_CONTROL_IS_NOT_PROOF_OR_NOVELTY=true")
    print("STATUS=HOLD_EXTERNAL")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
