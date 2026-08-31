#!/usr/bin/env python3
"""Exact algebraic/arithmetic breadth scout for the P132--P136 round.

The 27 handles in this file are literal finite self-maps.  Enumeration is a
falsification and triage device, not a proof, novelty certificate, or priority
claim.  Only Python's standard library and exact arithmetic are used.
"""

from collections import Counter
from functools import lru_cache
from itertools import combinations, product
from math import comb, gcd


ASSERTIONS = 0
RESULTS = []


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def record(system_id, family, scope, start, signal, decision, reason, **metrics):
    RESULTS.append({
        "id": system_id,
        "family": family,
        "scope": scope,
        "assertions": ASSERTIONS - start,
        "signal": signal,
        "decision": decision,
        "reason": reason,
        "metrics": metrics,
    })


def orbit_stats(states, step):
    states = tuple(states)
    state_set = set(states)
    nxt = {}
    for state in states:
        image = step(state)
        check(image in state_set, "map left its declared carrier")
        nxt[state] = image
    fixed = 0
    max_tail = 0
    max_period = 0
    period_hist = Counter()
    cycle_nodes = set()
    tails = Counter()
    for state in states:
        seen = {}
        order = []
        current = state
        while current not in seen:
            seen[current] = len(order)
            order.append(current)
            current = nxt[current]
        tail = seen[current]
        period = len(order) - tail
        check(period >= 1, "eventual cycle missing")
        check(nxt[order[-1]] == current, "orbit closure mismatch")
        cycle_nodes.update(order[tail:])
        tails[tail] += 1
        period_hist[period] += 1
        fixed += state == nxt[state]
        max_tail = max(max_tail, tail)
        max_period = max(max_period, period)
    return {
        "states": len(states),
        "fixed": fixed,
        "recurrent": len(cycle_nodes),
        "max_tail": max_tail,
        "max_period": max_period,
        "periods": "/".join(f"{k}:{period_hist[k]}" for k in sorted(period_hist)),
        "tails": "/".join(f"{k}:{tails[k]}" for k in sorted(tails)),
    }


def metric_text(value):
    if isinstance(value, dict):
        return "/".join(f"{k}:{value[k]}" for k in sorted(value))
    return str(value).replace(" ", "_")


# ---------------------------------------------------------------------------
# A01--A05: arithmetic functions on squarefree divisor lattices


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


def relation_image(mask, primes, factor_value):
    answer = 0
    for q_index, q in enumerate(primes):
        if mask >> q_index & 1:
            value = factor_value(q)
            for p_index, p in enumerate(primes):
                if value % p == 0:
                    answer |= 1 << p_index
    return answer


def euler_phi_squarefree(mask, primes):
    answer = 1
    for index, prime in enumerate(primes):
        if mask >> index & 1:
            answer *= prime - 1
    return answer


def sigma_squarefree(mask, primes):
    answer = 1
    for index, prime in enumerate(primes):
        if mask >> index & 1:
            answer *= prime + 1
    return answer


def jordan_two_squarefree(mask, primes):
    answer = 1
    for index, prime in enumerate(primes):
        if mask >> index & 1:
            answer *= prime * prime - 1
    return answer


def minus_heights(primes):
    """Longest q -> p path, where p divides q-1."""
    heights = []
    for index, prime in enumerate(primes):
        children = [heights[j] for j in range(index) if (prime - 1) % primes[j] == 0]
        heights.append(0 if not children else 1 + max(children))
    return heights


def relation_parents(mask, primes, factor_value):
    """Vertices q with an edge q -> p for at least one selected p."""
    answer = 0
    for p_index, p in enumerate(primes):
        if mask >> p_index & 1:
            for q_index, q in enumerate(primes):
                if q_index != p_index and factor_value(q) % p == 0:
                    answer |= 1 << q_index
    return answer


ARITH_PRIME_SETS = (
    (2, 3, 7, 43, 173),
    (2, 3, 5, 11, 23, 47),
    (2, 3, 5, 7, 13, 29, 43),
)


def run_a01():
    start = ASSERTIONS
    total_states = 0
    max_depth = 0
    profiles = []
    for primes in ARITH_PRIME_SETS:
        modulus = mask_product((1 << len(primes)) - 1, primes)
        heights = minus_heights(primes)

        def step(mask):
            d = mask_product(mask, primes)
            literal = divisor_mask(gcd(modulus, euler_phi_squarefree(mask, primes)), primes)
            predicted = relation_image(mask, primes, lambda q: q - 1)
            check(literal == predicted, "totient image lost its Pratt relation")
            check(d == mask_product(mask, primes), "divisor encoding changed")
            return literal

        depths = Counter()
        for mask in range(1 << len(primes)):
            current = mask
            depth = 0
            while current:
                current = step(current)
                depth += 1
                check(depth <= len(primes), "Pratt image exceeded DAG height")
            expected = 0 if mask == 0 else 1 + max(
                heights[i] for i in range(len(primes)) if mask >> i & 1
            )
            check(depth == expected, "totient depth is not the longest Pratt path")
            depths[depth] += 1
        total_states += 1 << len(primes)
        max_depth = max(max_depth, max(depths))
        profiles.append(f"m{len(primes)}:h{max(depths)}:L{metric_text(dict(depths))}")
    record(
        "A01", "squarefree_divisor_arithmetic",
        "d|n squarefree; d->gcd(n,phi(d)); three prime sets through 7 vertices",
        start,
        "every iterate is the length-t Pratt-relation image; depth is one plus longest selected prime chain",
        "FAMILY_CONTROL", "same Pratt-DAG carrier as A02 but a simpler nilpotent relational image",
        states=total_states, max_depth=max_depth, profiles=";".join(profiles),
    )


def run_a02():
    start = ASSERTIONS
    total_states = 0
    profiles = []
    max_tail = 0
    for primes in ARITH_PRIME_SETS:
        full = (1 << len(primes)) - 1
        modulus = mask_product(full, primes)

        def step(mask):
            d = mask_product(mask, primes)
            literal_value = gcd(modulus, (modulus // d) * euler_phi_squarefree(mask, primes))
            literal = divisor_mask(literal_value, primes)
            predicted = (full ^ mask) | relation_image(mask, primes, lambda q: q - 1)
            check(literal == predicted, "totient-complement Boolean rule failed")
            return literal

        stats = orbit_stats(range(1 << len(primes)), step)
        incoming = [False] * len(primes)
        for q_index, q in enumerate(primes):
            for p_index, p in enumerate(primes):
                if p_index != q_index and (q - 1) % p == 0:
                    incoming[p_index] = True
        sources = sum(not value for value in incoming)
        check(stats["fixed"] == 0, "a source coordinate forbids fixed points")
        check(stats["max_period"] == 2, "totient-complement acquired a non-2 cycle")
        check(stats["recurrent"] == 2 ** sources,
              "recurrent states are not parametrized by source phases")
        check(stats["max_tail"] <= 1 + max(minus_heights(primes)),
              "triangular transient exceeded Pratt height")
        fibres = Counter(
            (full ^ mask) | relation_image(mask, primes, lambda q: q - 1)
            for mask in range(1 << len(primes))
        )
        for target in range(1 << len(primes)):
            zero_set = full ^ target
            inclusion_exclusion = 0
            chosen = target
            while True:
                forced_one = zero_set | chosen
                forced_zero = relation_parents(
                    forced_one, primes, lambda q: q - 1
                )
                if forced_one & forced_zero == 0:
                    free = len(primes) - (forced_one | forced_zero).bit_count()
                    term = 1 << free
                    inclusion_exclusion += -term if chosen.bit_count() % 2 else term
                if chosen == 0:
                    break
                chosen = (chosen - 1) & target
            check(inclusion_exclusion == fibres[target],
                  "target-wise totient-complement fibre formula failed")
        total_states += stats["states"]
        max_tail = max(max_tail, stats["max_tail"])
        profiles.append(
            f"m{len(primes)}:src{sources}:rec{stats['recurrent']}:"
            f"tail{stats['max_tail']}:period{stats['max_period']}:"
            f"img{len(fibres)}:maxfib{max(fibres.values())}"
        )
    record(
        "A02", "squarefree_divisor_arithmetic",
        "d|n squarefree; d->gcd(n,(n/d)phi(d)); three prime sets through 7 vertices",
        start,
        "Pratt-DAG triangular Boolean network; no fixed points, only 2-cycles, source-phase recurrent census, Pratt-height transient bound, every-target inclusion-exclusion fibre",
        "LEAD", "literal-map owner not located; Pratt trees and generic signed Boolean networks are mandatory zero-credit boundaries",
        states=total_states, max_tail=max_tail, profiles=";".join(profiles),
    )


def run_a03():
    start = ASSERTIONS
    total_states = 0
    max_tail = 0
    profiles = []
    for primes in ARITH_PRIME_SETS:
        full = (1 << len(primes)) - 1
        modulus = mask_product(full, primes)

        def step(mask):
            complement = full ^ mask
            literal = divisor_mask(
                gcd(modulus, euler_phi_squarefree(complement, primes)), primes
            )
            predicted = relation_image(complement, primes, lambda q: q - 1)
            check(literal == predicted, "complement-totient relation failed")
            return literal

        stats = orbit_stats(range(1 << len(primes)), step)
        check(stats["fixed"] == 1 and stats["max_period"] == 1,
              "acyclic complement-totient network lost its unique fixed point")
        check(stats["max_tail"] <= len(primes), "triangular convergence bound failed")
        total_states += stats["states"]
        max_tail = max(max_tail, stats["max_tail"])
        profiles.append(f"m{len(primes)}:tail{stats['max_tail']}:fixed{stats['fixed']}")
    record(
        "A03", "squarefree_divisor_arithmetic",
        "d|n squarefree; d->gcd(n,phi(n/d)); three prime sets through 7 vertices",
        start,
        "a feed-forward complement network converges to a unique recursively defined divisor",
        "RESERVE_SIBLING", "same Pratt-DAG arithmetic family as A02 and a weaker recurrent package",
        states=total_states, max_tail=max_tail, profiles=";".join(profiles),
    )


def run_a04():
    start = ASSERTIONS
    profiles = []
    total_states = 0
    for primes in ARITH_PRIME_SETS:
        modulus = mask_product((1 << len(primes)) - 1, primes)

        def step(mask):
            literal = divisor_mask(gcd(modulus, sigma_squarefree(mask, primes)), primes)
            predicted = relation_image(mask, primes, lambda q: q + 1)
            check(literal == predicted, "sigma support graph failed")
            return literal

        stats = orbit_stats(range(1 << len(primes)), step)
        total_states += stats["states"]
        profiles.append(
            f"m{len(primes)}:tail{stats['max_tail']}:period{stats['max_period']}:rec{stats['recurrent']}"
        )
    record(
        "A04", "squarefree_divisor_arithmetic",
        "d|n squarefree; d->gcd(n,sigma(d)); three prime sets",
        start,
        "q+1 divisibility creates Boolean-relation cycles absent from the Pratt q-1 DAG",
        "KILL_OWNER", "literal arithmetic is exactly a disjunctive Boolean relation image after prime support",
        states=total_states, profiles=";".join(profiles),
    )


def run_a05():
    start = ASSERTIONS
    profiles = []
    total_states = 0
    for primes in ARITH_PRIME_SETS:
        modulus = mask_product((1 << len(primes)) - 1, primes)

        def step(mask):
            literal = divisor_mask(gcd(modulus, jordan_two_squarefree(mask, primes)), primes)
            predicted = relation_image(mask, primes, lambda q: q * q - 1)
            check(literal == predicted, "Jordan-totient support graph failed")
            return literal

        stats = orbit_stats(range(1 << len(primes)), step)
        total_states += stats["states"]
        profiles.append(
            f"m{len(primes)}:tail{stats['max_tail']}:period{stats['max_period']}:rec{stats['recurrent']}"
        )
    record(
        "A05", "squarefree_divisor_arithmetic",
        "d|n squarefree; d->gcd(n,J_2(d)); three prime sets",
        start,
        "q^2-1 support relation produces a denser recurrent Boolean image",
        "KILL_SIBLING", "same relation-image engine as A04 with only a changed edge predicate",
        states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# M01--M05: finite abelian groups and Nakayama-module functors


def bounded_partitions(max_part, max_length):
    answer = [()]
    for length in range(1, max_length + 1):
        answer.extend(combinations(range(1, max_part + 1), length))
    # combinations are strict; module types allow repeated parts.
    answer = [()]
    for length in range(1, max_length + 1):
        for values in product(range(1, max_part + 1), repeat=length):
            if all(values[i] >= values[i + 1] for i in range(length - 1)):
                answer.append(values)
    return tuple(answer)


def exterior_square_type(parts):
    factors = []
    for i in range(len(parts)):
        for j in range(i + 1, len(parts)):
            factors.append(min(parts[i], parts[j]))
    return tuple(sorted(factors, reverse=True))


def run_m01():
    start = ASSERTIONS
    total_states = 0
    profiles = []
    for exponent in range(1, 13):
        states = bounded_partitions(exponent, 3)
        fibres = Counter(exterior_square_type(state) for state in states)
        fixed = [state for state in states if exterior_square_type(state) == state]
        check(len(states) == comb(exponent + 3, 3), "bounded type count failed")
        check(len(fixed) == exponent + 1, "exterior-square fixed types failed")
        check(set(fixed) == {()} | {(c, c, c) for c in range(1, exponent + 1)},
              "unexpected exterior-square fixed type")
        for state in states:
            first = exterior_square_type(state)
            second = exterior_square_type(first)
            check(exterior_square_type(second) == second, "Lambda^2 did not stabilize by time two")
            if not first:
                expected_fibre = exponent + 1
            elif len(first) == 1:
                expected_fibre = exponent - first[0] + 1
            elif len(first) == 3 and first[1] == first[2]:
                expected_fibre = exponent - first[0] + 1
            else:
                expected_fibre = 0
            check(fibres[first] == expected_fibre, "one-step exterior-square fibre formula failed")
        terminal = Counter(exterior_square_type(exterior_square_type(state)) for state in states)
        check(terminal[()] == 1 + exponent + comb(exponent + 1, 2),
              "terminal trivial fibre failed")
        for c in range(1, exponent + 1):
            check(terminal[(c, c, c)] == comb(exponent - c + 2, 2),
                  "terminal homocyclic fibre failed")
        total_states += len(states)
        profiles.append(
            f"e{exponent}:states{len(states)}:fixed{len(fixed)}:image{len(fibres)}:maxfib{max(fibres.values())}"
        )
    record(
        "M01", "module_functors",
        "isomorphism types of abelian p-groups with exponent<=p^e and generator rank<=3; G->Lambda^2 G; e<=12",
        start,
        "closed rank-three accident gives depth<=2, complete image, every one-step/terminal fibre, and p-blind type dynamics",
        "RESERVE_OWNER_HEAVY", "the classical invariant-factor formula owns the reduction; fixed/image/fibre dynamics may be only immediate corollaries",
        states=total_states, max_depth=2, profiles=";".join(profiles),
    )


ZERO_MODULE = (-1, 0)


def nakayama_states(vertices, loewy):
    return (ZERO_MODULE,) + tuple(
        (vertex, length) for vertex in range(vertices) for length in range(1, loewy + 1)
    )


def syzygy_step(state, vertices, loewy):
    if state == ZERO_MODULE:
        return state
    vertex, length = state
    if length == loewy:
        return ZERO_MODULE
    return ((vertex + length) % vertices, loewy - length)


def run_m02():
    start = ASSERTIONS
    total_states = 0
    profiles = []
    for vertices in range(2, 11):
        for loewy in range(2, 10):
            states = nakayama_states(vertices, loewy)
            step = lambda state, v=vertices, e=loewy: syzygy_step(state, v, e)
            stats = orbit_stats(states, step)
            check(stats["max_tail"] == 1, "projectives should be the only transient states")
            check(stats["recurrent"] == 1 + vertices * (loewy - 1),
                  "nonprojective recurrent census failed")
            for state in states:
                if state == ZERO_MODULE or state[1] == loewy:
                    continue
                vertex, length = state
                twice = step(step(state))
                check(twice == ((vertex + loewy) % vertices, length),
                      "Omega^2 is not the Nakayama rotation")
                if 2 * length == loewy:
                    expected = vertices // gcd(vertices, loewy // 2)
                else:
                    expected = 2 * vertices // gcd(vertices, loewy)
                current = step(state)
                period = 1
                while current != state:
                    current = step(current)
                    period += 1
                check(period == expected, "syzygy period formula failed")
            total_states += len(states)
            if (vertices, loewy) in ((2, 2), (3, 4), (5, 6), (7, 9), (10, 8)):
                profiles.append(
                    f"n{vertices}e{loewy}:rec{stats['recurrent']}:"
                    f"tail{stats['max_tail']}:period{stats['max_period']}"
                )
    record(
        "M02", "module_functors",
        "indecomposables plus zero over the oriented n-cycle path algebra kQ_n/J^e; syzygy Omega; 2<=n<=10,2<=e<=9",
        start,
        "Omega^2 is rotation by e; all projectives are one-step leaves and every nonprojective period is explicit",
        "LEAD_OWNER_HEAVY", "Marks' periodicity lemma owns the exact period cases; leaves, fibres, and zeta are immediate finite-map packaging",
        states=total_states, profiles=";".join(profiles),
    )


def run_m03():
    start = ASSERTIONS
    states_total = 0
    max_depth = 0
    for vertices in range(2, 10):
        for loewy in range(2, 11):
            states = nakayama_states(vertices, loewy)

            def step(state):
                if state == ZERO_MODULE:
                    return state
                vertex, length = state
                return ZERO_MODULE if length == 1 else ((vertex + 1) % vertices, length - 1)

            for state in states:
                current = state
                depth = 0
                while current != ZERO_MODULE:
                    current = step(current)
                    depth += 1
                expected = 0 if state == ZERO_MODULE else state[1]
                check(depth == expected, "radical Loewy clock failed")
                max_depth = max(max_depth, depth)
            states_total += len(states)
    record(
        "M03", "module_functors",
        "indecomposable cyclic-Nakayama modules plus zero; M->rad M; n<=9,e<=10",
        start, "absorption time is exactly composition length",
        "KILL_OWNER", "literal radical filtration is the classical Loewy series",
        states=states_total, max_depth=max_depth,
    )


def run_m04():
    start = ASSERTIONS
    states_total = 0
    max_depth = 0
    for vertices in range(2, 10):
        for loewy in range(2, 11):
            states = nakayama_states(vertices, loewy)

            def step(state):
                if state == ZERO_MODULE:
                    return state
                vertex, length = state
                return ZERO_MODULE if length == 1 else (vertex, length - 1)

            for state in states:
                current = state
                depth = 0
                while current != ZERO_MODULE:
                    current = step(current)
                    depth += 1
                check(depth == (0 if state == ZERO_MODULE else state[1]),
                      "socle-quotient clock failed")
                max_depth = max(max_depth, depth)
            states_total += len(states)
    record(
        "M04", "module_functors",
        "indecomposable cyclic-Nakayama modules plus zero; M->M/soc M; n<=9,e<=10",
        start, "absorption time is exactly composition length with stationary top label",
        "KILL_SIBLING", "dual Loewy erosion is no stronger than M03",
        states=states_total, max_depth=max_depth,
    )


def run_m05():
    start = ASSERTIONS
    states_total = 0
    profiles = []
    for vertices in range(2, 13):
        for loewy in range(2, 9):
            states = tuple((i, length) for i in range(vertices) for length in range(1, loewy))
            step = lambda state, n=vertices: ((state[0] - 1) % n, state[1])
            stats = orbit_stats(states, step)
            check(stats["max_tail"] == 0 and stats["max_period"] == vertices,
                  "Auslander-Reiten translation period failed")
            check(stats["recurrent"] == len(states), "translation ceased to be bijective")
            states_total += len(states)
            if loewy == 5 and vertices in (2, 5, 11):
                profiles.append(f"n{vertices}:cycles{len(states)//vertices}:period{vertices}")
    record(
        "M05", "module_functors",
        "nonprojective indecomposables over self-injective Nakayama algebras; Auslander-Reiten translate",
        start, "each length stratum is one vertex-rotation cycle",
        "KILL_OWNER", "Auslander-Reiten translation is literally the standard quiver rotation",
        states=states_total, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# P01--P05: polynomial and binary-form transforms


def poly_trim(values, prime):
    answer = [value % prime for value in values]
    while answer and answer[-1] == 0:
        answer.pop()
    return tuple(answer)


def poly_monic(values, prime):
    values = poly_trim(values, prime)
    if not values:
        return ()
    inverse = pow(values[-1], -1, prime)
    return tuple(value * inverse % prime for value in values)


def poly_derivative(values, prime):
    return poly_trim((index * values[index] for index in range(1, len(values))), prime)


def poly_remainder(dividend, divisor, prime):
    dividend = list(poly_trim(dividend, prime))
    divisor = poly_trim(divisor, prime)
    check(bool(divisor), "division by zero polynomial")
    inverse = pow(divisor[-1], -1, prime)
    while dividend and len(dividend) >= len(divisor):
        coefficient = dividend[-1] * inverse % prime
        shift = len(dividend) - len(divisor)
        for index, value in enumerate(divisor):
            dividend[index + shift] = (dividend[index + shift] - coefficient * value) % prime
        while dividend and dividend[-1] == 0:
            dividend.pop()
    return tuple(dividend)


def poly_mul(left, right, prime):
    if not left or not right:
        return ()
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % prime
    return poly_trim(answer, prime)


def monic_polynomials(prime, degree_bound):
    states = [()]
    for degree in range(degree_bound + 1):
        states.extend(tuple(coefficients) + (1,)
                      for coefficients in product(range(prime), repeat=degree))
    return tuple(states)


def derivative_remainder_step(state, prime):
    derivative = poly_derivative(state, prime)
    if not derivative:
        return state
    return poly_monic(poly_remainder(state, derivative, prime), prime)


def run_p01():
    start = ASSERTIONS
    profiles = []
    total_states = 0
    max_tail = 0
    for prime, bound in ((2, 8), (3, 7), (5, 6), (7, 5)):
        states = monic_polynomials(prime, bound)
        step = lambda state, p=prime: derivative_remainder_step(state, p)
        stats = orbit_stats(states, step)
        for state in states:
            image = step(state)
            if image != state:
                check(len(image) < len(state), "derivative remainder did not lower degree")
            else:
                check(not poly_derivative(state, prime), "unexpected fixed polynomial")
        total_states += len(states)
        max_tail = max(max_tail, stats["max_tail"])
        profiles.append(
            f"p{prime}D{bound}:states{len(states)}:fixed{stats['fixed']}:tail{stats['max_tail']}"
        )
    record(
        "P01", "polynomial_transforms",
        "monic F_p[x] of bounded degree plus zero; f->monic(f mod f'); four boxes through 7,5",
        start,
        "strict Euclidean degree descent with characteristic-p derivative-zero terminal strata and nontrivial depth layers",
        "RESERVE_PROOF_BURDEN", "near the derivative Euclidean/subresultant literature and internally adjacent to P131; no all-degree fibre theorem yet",
        states=total_states, max_tail=max_tail, profiles=";".join(profiles),
    )


def graeffe_step(state, prime):
    if not state:
        return state
    degree = len(state) - 1
    even = tuple(state[2 * index] for index in range((degree // 2) + 1))
    odd = tuple(state[2 * index + 1] for index in range((degree + 1) // 2))
    even_square = poly_mul(even, even, prime)
    odd_square = (0,) + poly_mul(odd, odd, prime) if odd else ()
    length = max(len(even_square), len(odd_square))
    answer = [0] * length
    sign = -1 if degree % 2 else 1
    for index in range(length):
        value = (even_square[index] if index < len(even_square) else 0)
        value -= odd_square[index] if index < len(odd_square) else 0
        answer[index] = sign * value % prime
    answer = poly_trim(answer, prime)
    check(len(answer) == len(state) and answer[-1] == 1, "Graeffe transform lost degree/monicity")
    return answer


def run_p02():
    start = ASSERTIONS
    profiles = []
    total_states = 0
    for prime, max_degree in ((2, 7), (3, 5), (5, 4), (7, 3)):
        for degree in range(1, max_degree + 1):
            states = tuple(tuple(coefficients) + (1,)
                           for coefficients in product(range(prime), repeat=degree))
            stats = orbit_stats(states, lambda state, p=prime: graeffe_step(state, p))
            if prime == 2:
                check(stats["fixed"] == len(states), "binary Graeffe should be coefficient Frobenius")
            total_states += len(states)
            if degree == max_degree:
                profiles.append(
                    f"p{prime}n{degree}:tail{stats['max_tail']}:period{stats['max_period']}:rec{stats['recurrent']}"
                )
    record(
        "P02", "polynomial_transforms",
        "fixed-degree monic polynomials; classical Graeffe root-squaring transform",
        start,
        "finite-field tails and cycles are the symmetric-power shadow of root squaring; characteristic two freezes over F_2",
        "KILL_OWNER", "Graeffe iteration and root-squaring are direct classical owners; generic power dynamics remains zero credit",
        states=total_states, profiles=";".join(profiles),
    )


def poly_shift(state, constant, prime):
    if not state:
        return state
    answer = [0] * len(state)
    for degree, coefficient in enumerate(state):
        for power in range(degree + 1):
            answer[power] = (
                answer[power]
                + coefficient * comb(degree, power) * pow(constant, degree - power, prime)
            ) % prime
    return poly_trim(answer, prime)


def run_p03():
    start = ASSERTIONS
    total_states = 0
    image_total = 0
    profiles = []
    for prime, degree in ((2, 3), (3, 4), (5, 3), (5, 4), (7, 5)):
        check(degree % prime != 0, "centering requires invertible degree")
        states = tuple(tuple(coefficients) + (1,)
                       for coefficients in product(range(prime), repeat=degree))

        def step(state):
            coefficient = state[-2]
            shift = (-coefficient * pow(degree, -1, prime)) % prime
            image = poly_shift(state, shift, prime)
            check(image[-2] == 0, "depressed polynomial still has subleading term")
            return image

        stats = orbit_stats(states, step)
        check(stats["max_tail"] == 1 and stats["max_period"] == 1,
              "centering is not an idempotent retraction")
        check(stats["fixed"] == prime ** (degree - 1), "depressed-polynomial count failed")
        total_states += len(states)
        image_total += stats["fixed"]
        profiles.append(f"p{prime}n{degree}:states{len(states)}:image{stats['fixed']}")
    record(
        "P03", "polynomial_transforms",
        "monic degree-n polynomials in characteristic not dividing n; translate by the unique centering shift",
        start, "uniform p-to-1 idempotent retraction onto depressed polynomials",
        "KILL_THIN", "Tschirnhaus centering is classical and the dynamics stops after one step",
        states=total_states, images=image_total, profiles=";".join(profiles),
    )


def trunc_mul(left, right, prime, degree):
    answer = [0] * (degree + 1)
    for i, a in enumerate(left[:degree + 1]):
        for j, b in enumerate(right[:degree + 1 - i]):
            answer[i + j] = (answer[i + j] + a * b) % prime
    return tuple(answer)


def trunc_compose(outer, inner, prime, degree):
    answer = [0] * (degree + 1)
    power = [0] * (degree + 1)
    power[0] = 1
    for exponent, coefficient in enumerate(outer):
        if coefficient:
            for index in range(degree + 1):
                answer[index] = (answer[index] + coefficient * power[index]) % prime
        power = trunc_mul(power, inner, prime, degree)
    return tuple(answer)


def run_p04():
    start = ASSERTIONS
    total_states = 0
    profiles = []
    for prime, degree in ((2, 7), (3, 5), (5, 4)):
        states = tuple((0, 1) + tuple(coefficients)
                       for coefficients in product(range(prime), repeat=degree - 1))
        identity = (0, 1) + (0,) * (degree - 1)
        inverse = {}
        for state in states:
            candidates = [other for other in states
                          if trunc_compose(state, other, prime, degree) == identity]
            check(len(candidates) == 1, "formal inverse is not unique")
            other = candidates[0]
            check(trunc_compose(other, state, prime, degree) == identity,
                  "one-sided formal inverse failed")
            inverse[state] = other
        stats = orbit_stats(states, inverse.__getitem__)
        check(stats["max_tail"] == 0 and stats["max_period"] <= 2,
              "reversion should be an involution")
        total_states += len(states)
        profiles.append(
            f"p{prime}D{degree}:states{len(states)}:fixed{stats['fixed']}:two{len(states)-stats['fixed']}"
        )
    record(
        "P04", "polynomial_transforms",
        "truncated tangent-to-identity formal series; compositional reversion",
        start, "exact fixed/self-inverse census inside finite Nottingham quotients",
        "KILL_OWNER", "formal reversion is an involution by definition; fixed-series enumeration is the only residual",
        states=total_states, profiles=";".join(profiles),
    )


def projective_normalize(vector, prime):
    for value in vector:
        if value % prime:
            inverse = pow(value, -1, prime)
            return tuple(entry * inverse % prime for entry in vector)
    raise ValueError("zero vector has no projective normalization")


def binary_form_action(form, prime):
    """Substitute (X,Y)->(X+Y,X) in a binary form."""
    degree = len(form) - 1
    answer = [0] * (degree + 1)
    for x_power, coefficient in enumerate(form):
        y_power = degree - x_power
        # (X+Y)^x_power X^y_power
        for chosen_x in range(x_power + 1):
            new_x = chosen_x + y_power
            answer[new_x] = (
                answer[new_x] + coefficient * comb(x_power, chosen_x)
            ) % prime
    return projective_normalize(answer, prime)


def run_p05():
    start = ASSERTIONS
    total_states = 0
    profiles = []
    for prime, degree in ((2, 5), (3, 4), (5, 3), (7, 2)):
        states_set = set()
        for vector in product(range(prime), repeat=degree + 1):
            if any(vector):
                states_set.add(projective_normalize(vector, prime))
        states = tuple(sorted(states_set))
        stats = orbit_stats(states, lambda state, p=prime: binary_form_action(state, p))
        check(stats["max_tail"] == 0, "GL2 substitution is not projectively bijective")
        check(len(states) == (prime ** (degree + 1) - 1) // (prime - 1),
              "projective binary-form count failed")
        total_states += len(states)
        profiles.append(
            f"p{prime}n{degree}:states{len(states)}:fixed{stats['fixed']}:period{stats['max_period']}"
        )
    record(
        "P05", "polynomial_transforms",
        "projective binary forms; substitute (X,Y)->(X+Y,X)",
        start, "cycle lengths reflect the projective order of one Fibonacci matrix across symmetric powers",
        "KILL_OWNER", "literal map is a standard PGL_2 action on binary forms",
        states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# L01--L05: bilinear, matrix, and code transforms


def span_mask(vectors):
    basis = []
    for value in vectors:
        x = value
        for pivot in basis:
            x = min(x, x ^ pivot)
        if x:
            basis.append(x)
            basis.sort(reverse=True)
    values = {0}
    for pivot in basis:
        values |= {value ^ pivot for value in tuple(values)}
    return sum(1 << value for value in values)


@lru_cache(maxsize=None)
def binary_subspaces(dimension):
    if dimension == 0:
        return (1,)
    vectors = tuple(range(1, 1 << dimension))
    spaces = set()
    for selector in range(1 << len(vectors)):
        spaces.add(span_mask(vectors[index] for index in range(len(vectors))
                             if selector >> index & 1))
    return tuple(sorted(spaces))


def space_elements(space, dimension):
    return tuple(vector for vector in range(1 << dimension) if space >> vector & 1)


def binary_orthogonal(space, dimension):
    elements = space_elements(space, dimension)
    return span_mask(
        vector for vector in range(1 << dimension)
        if all((vector & other).bit_count() % 2 == 0 for other in elements)
    )


def mat_mul(left, right, size, prime):
    return tuple(
        sum(left[i * size + k] * right[k * size + j] for k in range(size)) % prime
        for i in range(size) for j in range(size)
    )


def mat_transpose(matrix, size):
    return tuple(matrix[j * size + i] for i in range(size) for j in range(size))


def mat_add(left, right, prime):
    return tuple((a + b) % prime for a, b in zip(left, right))


def mat_sub(left, right, prime):
    return tuple((a - b) % prime for a, b in zip(left, right))


def mat_identity(size):
    return tuple(1 if i == j else 0 for i in range(size) for j in range(size))


def mat_inverse(matrix, size, prime):
    rows = [list(matrix[i * size:(i + 1) * size])
            + [1 if i == j else 0 for j in range(size)] for i in range(size)]
    for column in range(size):
        pivot = next((row for row in range(column, size) if rows[row][column] % prime), None)
        if pivot is None:
            return None
        rows[column], rows[pivot] = rows[pivot], rows[column]
        inverse = pow(rows[column][column] % prime, -1, prime)
        rows[column] = [value * inverse % prime for value in rows[column]]
        for row in range(size):
            if row != column and rows[row][column] % prime:
                factor = rows[row][column] % prime
                rows[row] = [
                    (rows[row][j] - factor * rows[column][j]) % prime
                    for j in range(2 * size)
                ]
    return tuple(rows[i][size + j] for i in range(size) for j in range(size))


def all_gl(size, prime):
    return tuple(matrix for matrix in product(range(prime), repeat=size * size)
                 if mat_inverse(matrix, size, prime) is not None)


def binary_mat_vec(matrix, vector, size):
    answer = 0
    for i in range(size):
        bit = 0
        for j in range(size):
            bit ^= matrix[i * size + j] & ((vector >> j) & 1)
        answer |= bit << i
    return answer


def binary_space_image(matrix, space, size):
    return span_mask(binary_mat_vec(matrix, vector, size)
                     for vector in space_elements(space, size))


def run_l01():
    start = ASSERTIONS
    profiles = []
    total_states = 0
    matrices = {
        3: (1, 1, 0,
            0, 1, 1,
            0, 0, 1),
        4: (1, 1, 0, 0,
            0, 1, 1, 0,
            0, 0, 1, 1,
            0, 0, 0, 1),
    }
    for dimension, matrix in matrices.items():
        spaces = binary_subspaces(dimension)
        inverse = mat_inverse(matrix, dimension, 2)
        check(inverse is not None, "twisting matrix is singular")
        inverse_transpose = mat_transpose(inverse, dimension)
        cosquare = mat_mul(matrix, inverse_transpose, dimension, 2)

        def step(space):
            return binary_space_image(matrix, binary_orthogonal(space, dimension), dimension)

        stats = orbit_stats(spaces, step)
        for space in spaces:
            check(step(step(space)) == binary_space_image(cosquare, space, dimension),
                  "twisted duality square is not the asymmetry action")
        check(stats["max_tail"] == 0, "twisted duality is not bijective")
        total_states += len(spaces)
        profiles.append(
            f"d{dimension}:states{len(spaces)}:fixed{stats['fixed']}:period{stats['max_period']}"
        )
    record(
        "L01", "linear_bilinear",
        "binary subspace lattices in dimensions 3,4; U->A(U^perp) for fixed unipotent A",
        start,
        "the square is the cosquare/asymmetry action A A^{-T}, turning twisted duality into an explicit permutation census",
        "RESERVE_OWNER_HEAVY", "bilinear-form asymmetry and twisted polarities own the reduction; family-wide fixed counts are absent",
        states=total_states, profiles=";".join(profiles),
    )


def run_l02():
    start = ASSERTIONS
    profiles = []
    total_states = 0
    for size, prime in ((2, 2), (2, 3), (2, 5), (3, 2)):
        states = all_gl(size, prime)

        def step(matrix):
            inverse = mat_inverse(matrix, size, prime)
            return mat_mul(mat_transpose(inverse, size), matrix, size, prime)

        stats = orbit_stats(states, step)
        for matrix in states:
            image = step(matrix)
            check(mat_inverse(image, size, prime) is not None, "cosquare became singular")
        total_states += len(states)
        profiles.append(
            f"n{size}p{prime}:states{len(states)}:tail{stats['max_tail']}:period{stats['max_period']}"
        )
    record(
        "L02", "linear_bilinear",
        "GL_2(F_2,F_3,F_5) and GL_3(F_2); A->A^{-T}A",
        start, "cosquare iteration has mixed finite tails/periods beyond immediate bilinear-form classification",
        "KILL_NO_SPINE", "cosquares/asymmetry operators are mature and the pilot exposes no monotone or uniform theorem",
        states=total_states, profiles=";".join(profiles),
    )


def run_l03():
    start = ASSERTIONS
    profiles = []
    total_states = 0
    for prime in (3, 5, 7):
        size = 2
        identity = mat_identity(size)
        states = tuple(
            matrix for matrix in all_gl(size, prime)
            if mat_inverse(mat_add(identity, matrix, prime), size, prime) is not None
            and mat_inverse(mat_sub(identity, matrix, prime), size, prime) is not None
        )

        def step(matrix):
            numerator = mat_sub(identity, matrix, prime)
            denominator_inverse = mat_inverse(mat_add(identity, matrix, prime), size, prime)
            check(denominator_inverse is not None, "Cayley denominator vanished")
            return mat_mul(numerator, denominator_inverse, size, prime)

        stats = orbit_stats(states, step)
        check(stats["max_tail"] == 0 and stats["max_period"] <= 2,
              "matrix Cayley transform is not involutory")
        total_states += len(states)
        profiles.append(f"p{prime}:states{len(states)}:fixed{stats['fixed']}")
    record(
        "L03", "linear_bilinear",
        "2x2 matrices over odd prime fields with A and I+/-A invertible; matrix Cayley transform",
        start, "closed-domain rational involution with an exact fixed census",
        "KILL_OWNER_THIN", "Cayley transform involutivity is classical and creates no transient",
        states=total_states, profiles=";".join(profiles),
    )


def run_l04():
    start = ASSERTIONS
    states = tuple((dimension, space)
                   for dimension in range(5)
                   for space in binary_subspaces(dimension))

    def step(state):
        dimension, space = state
        if dimension == 0:
            return state
        dual = binary_orthogonal(space, dimension)
        mask = (1 << (dimension - 1)) - 1
        punctured = span_mask(vector & mask for vector in space_elements(dual, dimension))
        return (dimension - 1, punctured)

    stats = orbit_stats(states, step)
    for state in states:
        current = state
        depth = 0
        while current[0]:
            current = step(current)
            depth += 1
        check(depth == state[0], "punctured-dual ambient clock failed")
    record(
        "L04", "linear_bilinear",
        "disjoint union of binary linear codes of lengths 0..4; dual then puncture last coordinate",
        start, "ambient length is the exact absorption clock independently of code dimension",
        "KILL_MECHANICAL", "ordinary duality/puncturing translated into a shrinking carrier",
        **stats,
    )


def cyclic_rotate_vector(vector, dimension):
    return ((vector << 1) & ((1 << dimension) - 1)) | (vector >> (dimension - 1))


def cyclic_space_image(space, dimension, times=1):
    def rotate(vector):
        for _ in range(times % dimension):
            vector = cyclic_rotate_vector(vector, dimension)
        return vector
    return span_mask(rotate(vector) for vector in space_elements(space, dimension))


def run_l05():
    start = ASSERTIONS
    profiles = []
    total_states = 0
    for dimension in (3, 4):
        spaces = binary_subspaces(dimension)

        def step(space):
            return space & cyclic_space_image(space, dimension)

        stats = orbit_stats(spaces, step)
        check(stats["max_period"] == 1, "cyclic core should be absorbing")
        for space in spaces:
            current = space
            intersection = space
            for time in range(1, dimension):
                current = step(current)
                intersection &= cyclic_space_image(space, dimension, time)
                check(current == intersection, "cyclic-core window identity failed")
            check(step(current) == current, "cyclic invariant core did not stabilize")
        total_states += len(spaces)
        profiles.append(
            f"d{dimension}:states{len(spaces)}:image{stats['fixed']}:tail{stats['max_tail']}"
        )
    record(
        "L05", "linear_bilinear",
        "subspaces of F_2^d, d=3,4; U->U intersect rho(U) for coordinate rotation rho",
        start,
        "T^t(U)=intersection_{j=0}^t rho^j(U), ending at the largest cyclic-code core inside U",
        "KILL_CLOSURE", "generic invariant-core intersection and cyclic-code background own the mechanism",
        states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# G01--G05: group-like, cluster, and polynomial-automorphism controls


def run_g01():
    start = ASSERTIONS
    profiles = []
    total_states = 0
    for prime in (3, 5, 7, 11):
        states = tuple(product(range(prime), repeat=3))

        def invariant(state):
            x, y, z = state
            return (x * x + y * y + z * z - x * y * z) % prime

        def step(state):
            x, y, z = state
            image = (y, z, (y * z - x) % prime)
            check(invariant(image) == invariant(state), "Fricke invariant changed")
            check(((image[0] * image[1] - image[2]) % prime, image[0], image[1]) == state,
                  "trace-map inverse failed")
            return image

        stats = orbit_stats(states, step)
        check(stats["max_tail"] == 0, "Fricke trace map is not bijective")
        total_states += len(states)
        profiles.append(f"p{prime}:period{stats['max_period']}:fixed{stats['fixed']}")
    record(
        "G01", "group_cluster_controls",
        "F_p^3; Fricke trace map (x,y,z)->(y,z,yz-x)",
        start, "preserved Markoff-Fricke cubic with field-dependent long permutation cycles",
        "KILL_DIRECT_OWNER", "Markoff/Fricke trace-map dynamics is a mature direct owner",
        states=total_states, profiles=";".join(profiles),
    )


def run_g02():
    start = ASSERTIONS
    profiles = []
    total_states = 0
    for prime in (3, 5, 7, 11):
        states = tuple(product(range(prime), repeat=3))

        def step(state):
            x, y, z = state
            return (x, y, (x * y - z) % prime)

        stats = orbit_stats(states, step)
        check(stats["max_tail"] == 0 and stats["max_period"] <= 2,
              "Vieta move is not involutory")
        total_states += len(states)
        profiles.append(f"p{prime}:fixed{stats['fixed']}:two{len(states)-stats['fixed']}")
    record(
        "G02", "group_cluster_controls",
        "F_p^3; one Vieta move (x,y,z)->(x,y,xy-z)",
        start, "exact involution and fixed-plane census",
        "KILL_DIRECT_OWNER", "one Markoff Vieta involution is definition-level background",
        states=total_states, profiles=";".join(profiles),
    )


def run_g03():
    start = ASSERTIONS
    profiles = []
    total_states = 0
    for modulus in range(3, 11):
        states = tuple(product(range(modulus), repeat=3))

        def rack(left, right):
            return right, (2 * right - left) % modulus

        def step(state):
            x, y, z = state
            x, y = rack(x, y)
            y, z = rack(y, z)
            return x, y, z

        stats = orbit_stats(states, step)
        check(stats["max_tail"] == 0, "Alexander-quandle braid sweep is not bijective")
        check(stats["max_period"] == 6, "braid sweep lost its period-six ceiling")
        check(stats["fixed"] == modulus, "fixed triples are not exactly the diagonal")
        total_states += len(states)
        profiles.append(f"m{modulus}:period{stats['max_period']}:fixed{stats['fixed']}")
    record(
        "G03", "group_cluster_controls",
        "(Z/mZ)^3; two adjacent Alexander-quandle braid generators per sweep",
        start, "uniform period-six ceiling and exactly m diagonal fixed triples, with no transient",
        "KILL_OWNER", "Alexander quandles and Burau/linear braid actions own the complete mechanism",
        states=total_states, profiles=";".join(profiles),
    )


def mobius_order_three(value, prime):
    infinity = prime
    if value == infinity:
        return 0
    denominator = (1 - value) % prime
    if denominator == 0:
        return infinity
    return pow(denominator, -1, prime)


def run_g04():
    start = ASSERTIONS
    profiles = []
    total_states = 0
    for prime in (2, 3, 5, 7, 11, 13, 17, 19):
        states = tuple(range(prime + 1))
        step = lambda value, p=prime: mobius_order_three(value, p)
        stats = orbit_stats(states, step)
        for value in states:
            check(step(step(step(value))) == value, "Mobius order-three identity failed")
        total_states += len(states)
        profiles.append(f"p{prime}:fixed{stats['fixed']}:period{stats['max_period']}")
    record(
        "G04", "group_cluster_controls",
        "projective lines P^1(F_p); x->1/(1-x)",
        start, "fixed-point anomaly is controlled by the discriminant -3, all other points lie in 3-cycles",
        "KILL_OWNER", "literal map is a single order-three PGL_2 element",
        states=total_states, profiles=";".join(profiles),
    )


def run_g05():
    start = ASSERTIONS
    profiles = []
    total_states = 0
    for prime in (3, 5, 7, 11):
        states = tuple(product(range(prime), repeat=2))

        def step(state):
            x, y = state
            return y, (y * y + 1 - x) % prime

        stats = orbit_stats(states, step)
        for state in states:
            image = step(state)
            check(((image[0] * image[0] + 1 - image[1]) % prime, image[0]) == state,
                  "Henon inverse failed")
        check(stats["max_tail"] == 0, "Henon map is not bijective")
        total_states += len(states)
        profiles.append(f"p{prime}:fixed{stats['fixed']}:period{stats['max_period']}")
    record(
        "G05", "group_cluster_controls",
        "F_p^2; area-preserving Henon map (x,y)->(y,y^2+1-x)",
        start, "mixed long cycles despite a polynomial inverse of the same degree",
        "KILL_OWNER_NO_SPINE", "finite-field Henon dynamics is heavily owned and the pilot has no uniform census",
        states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# R01--R02: local/residue-ring controls completing the literal 27


def valuation_two(value, exponent):
    if value % (1 << exponent) == 0:
        return exponent
    answer = 0
    while value % 2 == 0:
        answer += 1
        value //= 2
    return answer


def run_r01():
    start = ASSERTIONS
    total_states = 0
    profiles = []
    for exponent in range(2, 14):
        modulus = 1 << exponent
        states = tuple(range(modulus))

        def step(value):
            return value * value * (3 - 2 * value) % modulus

        layers = Counter()
        for value in states:
            target = value & 1
            defect = (value - target) % modulus
            initial_v = valuation_two(defect, exponent)
            current = value
            depth = 0
            while current != target:
                old_defect = (current - target) % modulus
                image = step(current)
                new_defect = (image - target) % modulus
                check(valuation_two(new_defect, exponent)
                      == min(exponent, 2 * valuation_two(old_defect, exponent)),
                      "smoothstep defect valuation did not double")
                current = image
                depth += 1
                check(depth <= exponent, "smoothstep did not converge")
            expected = 0
            power = initial_v
            while power < exponent:
                power *= 2
                expected += 1
            check(depth == expected, "smoothstep exact clock failed")
            layers[depth] += 1
        check(sum(layers.values()) == modulus, "smoothstep layer count failed")
        total_states += modulus
        profiles.append(f"e{exponent}:tail{max(layers)}:layers{metric_text(dict(layers))}")
    record(
        "R01", "local_ring_controls",
        "Z/2^e Z; x->x^2(3-2x); 2<=e<=13",
        start,
        "parity selects 0/1 and the 2-adic defect valuation doubles exactly, giving every depth layer",
        "KILL_INTERNAL", "Newton/Hensel error squaring was already rejected in earlier project scouting near P100",
        states=total_states, profiles=";".join(profiles),
    )


def run_r02():
    start = ASSERTIONS
    profiles = []
    total_states = 0
    for prime, exponent in ((2, 5), (2, 7), (3, 4), (5, 3), (7, 2)):
        modulus = prime ** exponent
        states = tuple(range(modulus))
        step = lambda value, m=modulus: (value * value + value + 1) % m
        stats = orbit_stats(states, step)
        total_states += len(states)
        profiles.append(
            f"p{prime}e{exponent}:tail{stats['max_tail']}:period{stats['max_period']}:fixed{stats['fixed']}"
        )
    record(
        "R02", "local_ring_controls",
        "Z/p^e Z; x->x^2+x+1 in five prime-power boxes",
        start, "ramified lifts change tails and periods discontinuously across p and e",
        "KILL_GENERIC", "generic quadratic polynomial dynamics has no clean invariant or fibre theorem in this pilot",
        states=total_states, profiles=";".join(profiles),
    )


def main():
    runners = (
        run_a01, run_a02, run_a03, run_a04, run_a05,
        run_m01, run_m02, run_m03, run_m04, run_m05,
        run_p01, run_p02, run_p03, run_p04, run_p05,
        run_l01, run_l02, run_l03, run_l04, run_l05,
        run_g01, run_g02, run_g03, run_g04, run_g05,
        run_r01, run_r02,
    )
    for runner in runners:
        runner()
    check(len(RESULTS) == 27, "literal-system count changed")
    check(len({result['id'] for result in RESULTS}) == 27, "duplicate handle")
    print("algebraic arithmetic breadth scout: PASS")
    print(f"systems={len(RESULTS)} leads={sum('LEAD' in r['decision'] for r in RESULTS)}")
    for result in RESULTS:
        metrics = ",".join(f"{key}={metric_text(value)}"
                           for key, value in result["metrics"].items())
        print(
            f"{result['id']} family={result['family']} scope={result['scope']} "
            f"assertions={result['assertions']} metrics={metrics} "
            f"signal={result['signal']} decision={result['decision']} reason={result['reason']}"
        )
    print(f"TOTAL_ASSERTIONS={ASSERTIONS}")
    print("scope_sentinel=finite exact enumeration is falsification evidence, not proof")
    print("novelty_sentinel=bounded owner non-hit is not novelty or priority")


if __name__ == "__main__":
    main()
