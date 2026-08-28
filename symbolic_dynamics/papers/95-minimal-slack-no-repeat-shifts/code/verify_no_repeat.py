#!/usr/bin/env python3
"""Exact controls for the minimal-slack no-repeat shifts N_q."""

from collections import deque
from fractions import Fraction
from itertools import permutations, product


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def states(q):
    return list(permutations(range(q), q - 1))


def successors(state, q):
    missing = next(a for a in range(q) if a not in state)
    return (state[1:] + (state[0],), state[1:] + (missing,))


def complete(state, q):
    missing = next(a for a in range(q) if a not in state)
    return state + (missing,)


def rotate_positions(permutation, length):
    return permutation[1:length] + permutation[:1] + permutation[length:]


def compose(left, right):
    """Return left after right for permutations stored by their images."""
    return tuple(left[right[i]] for i in range(len(left)))


def inverse(permutation):
    answer = [0] * len(permutation)
    for i, value in enumerate(permutation):
        answer[value] = i
    return tuple(answer)


def predecessors(state, q):
    out = []
    for a in range(q):
        candidate = (a,) + state[:-1]
        if len(set(candidate)) != q - 1:
            continue
        if state in successors(candidate, q):
            out.append(candidate)
    return tuple(out)


def reachable(start, q, reverse=False):
    seen = {start}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        neighbors = predecessors(state, q) if reverse else successors(state, q)
        for nxt in neighbors:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def sparse_trace_counts(q, max_period):
    vertex_list = states(q)
    index = {state: i for i, state in enumerate(vertex_list)}
    edges = [[index[x] for x in successors(state, q)] for state in vertex_list]
    traces = []
    for period in range(1, max_period + 1):
        total = 0
        for start in range(len(vertex_list)):
            counts = {start: 1}
            for _ in range(period):
                updated = {}
                for vertex, multiplicity in counts.items():
                    for nxt in edges[vertex]:
                        updated[nxt] = updated.get(nxt, 0) + multiplicity
                counts = updated
            total += counts.get(start, 0)
        traces.append(total)
    return traces


def legal_cyclic_word(word, q):
    n = len(word)
    return all(word[i] != word[(i + gap) % n]
               for i in range(n) for gap in range(1, q - 1))


def literal_fixed_counts(q, max_period):
    return [sum(legal_cyclic_word(word, q)
                for word in product(range(q), repeat=n))
            for n in range(1, max_period + 1)]


def desert_formula(q, n):
    if n <= q - 2:
        return 0
    if n in (q - 1, q):
        factorial = 1
        for value in range(2, q + 1):
            factorial *= value
        return factorial
    if q + 1 <= n <= 2 * q - 3:
        return 0
    return None


def first_return_distribution_from_states(q, initial_states, cutoff):
    # Under the Parry measure the two outgoing edges are independent fair
    # choices.  Condition the uniform state distribution on x_0=0 and kill
    # a history when the first coordinate of the shifted state returns to 0.
    active = {state: Fraction(1, len(initial_states)) for state in initial_states}
    law = [Fraction(0) for _ in range(cutoff + 1)]
    for time in range(1, cutoff + 1):
        updated = {}
        for state, probability in active.items():
            for nxt in successors(state, q):
                mass = probability / 2
                if nxt[0] == 0:
                    law[time] += mass
                else:
                    updated[nxt] = updated.get(nxt, Fraction(0)) + mass
        active = updated
    return law


def first_return_distribution(q, cutoff):
    initial_states = [state for state in states(q) if state[0] == 0]
    return first_return_distribution_from_states(q, initial_states, cutoff)


def two_gap_joint_distribution(q, cutoff):
    initial_states = [state for state in states(q) if state[0] == 0]
    active = {(state, None): Fraction(1, len(initial_states))
              for state in initial_states}
    joint = {}
    for time in range(1, cutoff + 1):
        updated = {}
        for (state, first_gap), probability in active.items():
            for nxt in successors(state, q):
                mass = probability / 2
                if nxt[0] != 0:
                    key = (nxt, first_gap)
                    updated[key] = updated.get(key, Fraction(0)) + mass
                elif first_gap is None:
                    key = (nxt, time)
                    updated[key] = updated.get(key, Fraction(0)) + mass
                else:
                    second_gap = time - first_gap
                    key = (first_gap, second_gap)
                    joint[key] = joint.get(key, Fraction(0)) + mass
        active = updated
    return joint


def renewal_return_probabilities(q, cutoff):
    first = [Fraction(0) for _ in range(cutoff + 1)]
    for n in range(q - 1, cutoff + 1):
        first[n] = Fraction(1, 2 ** (n - q + 2))
    returns = [Fraction(0) for _ in range(cutoff + 1)]
    returns[0] = Fraction(1)
    for n in range(1, cutoff + 1):
        returns[n] = sum(first[k] * returns[n - k]
                         for k in range(1, n + 1))
    return first, returns


def direct_return_probabilities(q, cutoff):
    initial_states = [state for state in states(q) if state[0] == 0]
    distribution = {state: Fraction(1, len(initial_states))
                    for state in initial_states}
    returns = [Fraction(1)]
    for _ in range(cutoff):
        updated = {}
        for state, probability in distribution.items():
            for nxt in successors(state, q):
                updated[nxt] = updated.get(nxt, Fraction(0)) + probability / 2
        distribution = updated
        returns.append(sum(probability for state, probability in distribution.items()
                           if state[0] == 0))
    return returns


def check_q(q):
    vertex_list = states(q)
    vertex_set = set(vertex_list)
    check(len(vertex_list) == factorial(q), (q, "state count"))
    for state in vertex_list:
        nxt = successors(state, q)
        check(len(nxt) == 2 and len(set(nxt)) == 2, (q, state, "outdegree"))
        check(all(x in vertex_set for x in nxt), (q, state, "closure"))
        pred = predecessors(state, q)
        check(len(pred) == 2 and len(set(pred)) == 2, (q, state, "indegree"))
        permutation = complete(state, q)
        expected = (
            rotate_positions(permutation, q - 1)[:-1],
            rotate_positions(permutation, q)[:-1],
        )
        check(nxt == expected, (q, state, nxt, expected, "Cayley orientation"))

    identity = tuple(range(q))
    alpha = rotate_positions(identity, q - 1)
    beta = rotate_positions(identity, q)
    transposition = list(identity)
    transposition[-2], transposition[-1] = transposition[-1], transposition[-2]
    check(compose(inverse(alpha), beta) == tuple(transposition),
          (q, "alpha inverse beta"))
    alpha_power = identity
    for _ in range(q - 2):
        alpha_power = compose(alpha_power, alpha)
    beta_power = identity
    for _ in range(q - 1):
        beta_power = compose(beta_power, beta)
    check(alpha_power == inverse(alpha), (q, "positive alpha inverse"))
    check(beta_power == inverse(beta), (q, "positive beta inverse"))
    start = vertex_list[0]
    check(len(reachable(start, q)) == len(vertex_list), (q, "forward connectivity"))
    check(len(reachable(start, q, reverse=True)) == len(vertex_list),
          (q, "reverse connectivity"))

    max_period = 2 * q - 3
    traces = sparse_trace_counts(q, max_period)
    for n, value in enumerate(traces, start=1):
        expected = desert_formula(q, n)
        check(expected is None or value == expected, (q, n, value, expected))

    cutoff = 4 * q + 8
    first_literal = first_return_distribution(q, cutoff)
    first, renewal = renewal_return_probabilities(q, cutoff)
    check(first_literal == first, (q, "first return law"))
    for state in vertex_list:
        if state[0] == 0:
            state_law = first_return_distribution_from_states(q, [state], cutoff)
            check(state_law == first, (q, state, "state-independent first return"))
    direct = direct_return_probabilities(q, cutoff)
    check(direct == renewal, (q, "renewal law"))
    joint = two_gap_joint_distribution(q, cutoff)
    for gap_one in range(1, cutoff):
        for gap_two in range(1, cutoff - gap_one + 1):
            probability = joint.get((gap_one, gap_two), Fraction(0))
            check(probability == first[gap_one] * first[gap_two],
                  (q, gap_one, gap_two, probability,
                   "full-grid two-gap factorization"))
    return traces, renewal


def factorial(n):
    answer = 1
    for value in range(2, n + 1):
        answer *= value
    return answer


def main():
    summaries = {}
    for q in range(3, 7):
        traces, renewal = check_q(q)
        summaries[q] = (traces, renewal[:min(len(renewal), 11)])

    # A genuinely separate literal cyclic-word route at the feasible cutoff.
    literal_cases = 0
    for q in range(3, 6):
        cutoff = min(2 * q - 3, 7)
        literal = literal_fixed_counts(q, cutoff)
        sparse = sparse_trace_counts(q, cutoff)
        check(literal == sparse, (q, literal, sparse))
        literal_cases += sum(q ** n for n in range(1, cutoff + 1))

    print("minimal-slack no-repeat exact control: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"literal_cyclic_words={literal_cases}")
    for q, (traces, renewal) in summaries.items():
        print(f"q={q} F_1..F_{len(traces)}={traces}")
        print(f"q={q} u_0..u_{len(renewal)-1}="
              + ",".join(str(value) for value in renewal))


if __name__ == "__main__":
    main()
