#!/usr/bin/env python3
"""Exact paper-local audit for totient--complement divisor dynamics.

The program is self-contained and uses only Python integers.  Finite
enumeration is a falsification control, not a proof or novelty claim.
"""

from collections import Counter
from math import gcd


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message="assertion failed"):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


CASES = (
    ("singleton", (2,)),
    ("chain5", (2, 3, 7, 43, 173)),
    ("mixed6", (2, 3, 5, 11, 23, 47)),
    ("disconnected7", (2, 3, 5, 7, 13, 29, 43)),
)


def mask_product(mask, primes):
    answer = 1
    for index, prime in enumerate(primes):
        if mask >> index & 1:
            answer *= prime
    return answer


def divisor_mask(value, primes):
    mask = 0
    for index, prime in enumerate(primes):
        if value % prime == 0:
            mask |= 1 << index
    return mask


def phi_squarefree(mask, primes):
    answer = 1
    for index, prime in enumerate(primes):
        if mask >> index & 1:
            answer *= prime - 1
    return answer


def parent_masks(primes):
    """parents[p] are q with q -> p, i.e. p divides q-1."""
    parents = []
    for p_index, p in enumerate(primes):
        mask = 0
        for q_index, q in enumerate(primes):
            if p_index != q_index and (q - 1) % p == 0:
                mask |= 1 << q_index
        parents.append(mask)
    return tuple(parents)


def support_step(mask, parents, vertex_count):
    full = (1 << vertex_count) - 1
    relation_image = 0
    for p_index, p_parents in enumerate(parents):
        if mask & p_parents:
            relation_image |= 1 << p_index
    return (full ^ mask) | relation_image


def literal_step(mask, primes):
    full = (1 << len(primes)) - 1
    modulus = mask_product(full, primes)
    divisor = mask_product(mask, primes)
    value = gcd(modulus, (modulus // divisor) * phi_squarefree(mask, primes))
    return divisor_mask(value, primes)


def y_step(mask, parents):
    answer = 0
    for index, p_parents in enumerate(parents):
        parent_product = (mask & p_parents) == p_parents
        if not (mask >> index & 1) and parent_product:
            answer |= 1 << index
    return answer


def vertex_depths(parents, vertex_count):
    depths = [None] * vertex_count
    # Every parent q is a larger prime, hence has a larger index.
    for index in range(vertex_count - 1, -1, -1):
        parent_indices = [
            q for q in range(vertex_count) if parents[index] >> q & 1
        ]
        depths[index] = (
            0 if not parent_indices else 1 + max(depths[q] for q in parent_indices)
        )
    return tuple(depths)


def orbit_data(states, step):
    next_state = {state: step(state) for state in states}
    recurrent = set()
    fixed = 0
    max_tail = 0
    periods = set()
    tails = {}
    for start in states:
        seen = {}
        state = start
        while state not in seen:
            AUDIT.check(state in next_state, "orbit left carrier")
            seen[state] = len(seen)
            state = next_state[state]
        tail = seen[state]
        period = len(seen) - tail
        AUDIT.check(period >= 1, "missing recurrent component")
        max_tail = max(max_tail, tail)
        periods.add(period)
        tails[start] = tail
        point = state
        for _ in range(period):
            recurrent.add(point)
            point = next_state[point]
        AUDIT.check(point == state, "cycle did not close")
        fixed += next_state[start] == start
    return next_state, recurrent, fixed, max_tail, tuple(sorted(periods)), tails


def phase_decoder(eta, source_indices, parents, vertex_count):
    y0 = 0
    y1 = 0
    for phase_index, vertex in enumerate(source_indices):
        value = eta >> phase_index & 1
        y0 |= value << vertex
        y1 |= (1 - value) << vertex

    for vertex in range(vertex_count - 1, -1, -1):
        if vertex in source_indices:
            continue
        p_parents = parents[vertex]
        a0 = (y0 & p_parents) == p_parents
        a1 = (y1 & p_parents) == p_parents
        AUDIT.check(not (a0 and a1), "parent phases overlap")
        y0 |= int(a1) << vertex
        y1 |= int(a0) << vertex
    return y0, y1


def parent_union(selected, parents, vertex_count):
    answer = 0
    for vertex in range(vertex_count):
        if selected >> vertex & 1:
            answer |= parents[vertex]
    return answer


def fibre_formula(target, parents, vertex_count):
    full = (1 << vertex_count) - 1
    zero_set = full ^ target
    total = 0
    chosen = target
    while True:
        forced_one = zero_set | chosen
        forced_zero = parent_union(forced_one, parents, vertex_count)
        if forced_one & forced_zero == 0:
            free = vertex_count - (forced_one | forced_zero).bit_count()
            term = 1 << free
            total += -term if chosen.bit_count() & 1 else term
        if chosen == 0:
            break
        chosen = (chosen - 1) & target
    return total


def verify_case(name, primes):
    start_assertions = AUDIT.assertions
    vertex_count = len(primes)
    full = (1 << vertex_count) - 1
    states = tuple(range(1 << vertex_count))
    parents = parent_masks(primes)
    depths = vertex_depths(parents, vertex_count)
    sources = tuple(index for index, mask in enumerate(parents) if mask == 0)
    height = max(depths)

    for mask in states:
        literal = literal_step(mask, primes)
        predicted = support_step(mask, parents, vertex_count)
        AUDIT.check(literal == predicted, (name, mask, literal, predicted))
        y = full ^ mask
        AUDIT.check(full ^ predicted == y_step(y, parents), "complement conjugacy")

    next_state, recurrent, fixed, max_tail, periods, tails = orbit_data(
        states, lambda mask: support_step(mask, parents, vertex_count)
    )
    AUDIT.check(fixed == 0, "a source coordinate must toggle")
    AUDIT.check(periods == (2,), (name, periods))
    AUDIT.check(len(recurrent) == 1 << len(sources), "wrong recurrent census")
    AUDIT.check(max_tail <= height + 1, "h+1 bound failed")
    for state, tail in tails.items():
        AUDIT.check(tail <= height + 1, (name, state, tail, height))

    decoded = set()
    for eta in range(1 << len(sources)):
        y0, y1 = phase_decoder(eta, sources, parents, vertex_count)
        AUDIT.check(y_step(y0, parents) == y1, "decoder phase 0 failed")
        AUDIT.check(y_step(y1, parents) == y0, "decoder phase 1 failed")
        AUDIT.check(y0 != y1, "source toggling forbids a fixed state")
        decoded.add(y0)
    recurrent_y = {full ^ state for state in recurrent}
    AUDIT.check(decoded == recurrent_y, (name, decoded, recurrent_y))
    AUDIT.check(len(decoded) == 1 << len(sources), "decoder is not injective")

    for y in states:
        first = y_step(y, parents)
        second = y_step(first, parents)
        for vertex, p_parents in enumerate(parents):
            AUDIT.check(not ((y >> vertex & 1) and (first >> vertex & 1)),
                        "consecutive coordinate ones")
            if p_parents:
                a_next = (first & p_parents) == p_parents
                AUDIT.check((second >> vertex & 1) == a_next,
                            "two-step erasure identity")

    fibres = Counter(next_state.values())
    for target in states:
        predicted_fibre = fibre_formula(target, parents, vertex_count)
        AUDIT.check(predicted_fibre == fibres[target],
                    (name, target, predicted_fibre, fibres[target]))
        AUDIT.check(predicted_fibre >= 0, "negative fibre")
    AUDIT.check(sum(fibres.values()) == len(states), "fibres do not partition")

    assertions = AUDIT.assertions - start_assertions
    return (
        f"case={name}|primes={','.join(map(str, primes))}"
        f"|vertices={vertex_count}|sources={len(sources)}|height={height}"
        f"|states={len(states)}|recurrent={len(recurrent)}"
        f"|cycles={len(recurrent)//2}|max_tail={max_tail}"
        f"|image={len(fibres)}|max_fibre={max(fibres.values())}"
        f"|assertions={assertions}"
    )


def main():
    lines = [verify_case(name, primes) for name, primes in CASES]
    print("TOTIENT_COMPLEMENT_PRATT_V1")
    for line in lines:
        print(line)
    print(f"TOTAL_STATES={sum(1 << len(primes) for _name, primes in CASES)}")
    print(f"TOTAL_TARGETS={sum(1 << len(primes) for _name, primes in CASES)}")
    print(f"TOTAL_ASSERTIONS={AUDIT.assertions}")
    print("EXACT_ARITHMETIC=python_integers")
    print("FLOATING_POINT=none")
    print("SAMPLING=none")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()

