#!/usr/bin/env python3
"""Independent exact control for P196 hostile Review B.

States are packed radix-q integers, not tuple words.  Inverse counts are
computed as traces of products of symbol-labelled binary relation matrices,
not by enumerating weak chains.  Characteristic polynomials are computed by
the Faddeev--LeVerrier algorithm, not by row operations, a determinant lemma,
or a Leibniz expansion.  The script imports no author or Review-A code.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from math import comb, gcd


ASSERTIONS = 0
TRANSITIONS = 0
TARGET_CHECKS = 0
HIGHER_TIME_TARGET_CHECKS = 0
FIXED_ITERATE_CHECKS = 0
GAP_MATRIX_CHECKS = 0
CHARPOLY_CHECKS = 0


def check(condition: bool, label: object) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def radix_powers(q: int, m: int) -> list[int]:
    powers = [1]
    for _ in range(m):
        powers.append(powers[-1] * q)
    return powers


def digit(code: int, position: int, q: int, powers: list[int]) -> int:
    return (code // powers[position]) % q


def literal_step(code: int, q: int, m: int, powers: list[int]) -> int:
    """Apply the synchronous rule directly to the packed state."""
    top = q - 1
    result = 0
    for i in range(m):
        antecedent = digit(code, i, q, powers)
        consequent = digit(code, (i + 1) % m, q, powers)
        value = top if antecedent <= consequent else consequent
        result += value * powers[i]
    return result


def left_rotate(code: int, q: int, m: int, amount: int,
                powers: list[int]) -> int:
    amount %= m
    result = 0
    for i in range(m):
        result += digit(code, (i + amount) % m, q, powers) * powers[i]
    return result


def is_core(code: int, q: int, m: int, powers: list[int]) -> bool:
    top = q - 1
    for i in range(m):
        current = digit(code, i, q, powers)
        following = digit(code, (i + 1) % m, q, powers)
        if following < top and current <= following:
            return False
    return True


def identity(size: int) -> list[list[int]]:
    return [[int(i == j) for j in range(size)] for i in range(size)]


def matrix_multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    rows = len(left)
    middle = len(right)
    columns = len(right[0])
    return [[sum(left[i][h] * right[h][j] for h in range(middle))
             for j in range(columns)] for i in range(rows)]


def matrix_power(matrix: list[list[int]], exponent: int) -> list[list[int]]:
    result = identity(len(matrix))
    base = matrix
    while exponent:
        if exponent & 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        exponent //= 2
    return result


def matrix_trace(matrix: list[list[int]]) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))


def implication_relation(symbol: int, q: int) -> list[list[int]]:
    """Rows are antecedents and columns are consequents."""
    top = q - 1
    if symbol == top:
        return [[int(a <= b) for b in range(q)] for a in range(q)]
    return [[int(b == symbol and a > b) for b in range(q)] for a in range(q)]


def csp_fibre(code: int, q: int, m: int, powers: list[int]) -> int:
    """Trace of the cyclic product of output-labelled relation matrices.

    Multiplication is specialized: the top relation is the weak-order matrix,
    while a nontop relation has one possibly nonzero column.  This remains a
    relation-product calculation and never generates a source word.
    """
    top = q - 1
    product_matrix = identity(q)
    for i in range(m):
        symbol = digit(code, i, q, powers)
        next_product = [[0] * q for _ in range(q)]
        if symbol == top:
            # Right multiplication by U[a,b]=1{a<=b}: row prefix sums.
            for row in range(q):
                running = 0
                for column in range(q):
                    running += product_matrix[row][column]
                    next_product[row][column] = running
        else:
            # Right multiplication by u_symbol e_symbol^T.
            for row in range(q):
                next_product[row][symbol] = sum(
                    product_matrix[row][middle]
                    for middle in range(symbol + 1, q)
                )
        product_matrix = next_product
    return matrix_trace(product_matrix)


def gap_closed(top: int, a: int, b: int, distance: int) -> int:
    total = comb(top - a + distance - 1, distance - 1)
    excluded = comb(b - a + distance - 1, distance - 1) if b >= a else 0
    return total - excluded


def formula_fibre(code: int, q: int, m: int, powers: list[int]) -> int:
    if not is_core(code, q, m, powers):
        return 0
    top = q - 1
    sites = [i for i in range(m) if digit(code, i, q, powers) < top]
    if not sites:
        return q
    result = 1
    for index, site in enumerate(sites):
        next_site = sites[(index + 1) % len(sites)]
        distance = (next_site - site) % m
        if distance == 0:
            distance = m
        a = digit(code, site, q, powers)
        b = digit(code, next_site, q, powers)
        result *= gap_closed(top, a, b, distance)
    return result


def core_adjacency(q: int) -> list[list[int]]:
    top = q - 1
    return [[int(b == top or a > b) for b in range(q)] for a in range(q)]


def trace_power(q: int, exponent: int) -> int:
    return matrix_trace(matrix_power(core_adjacency(q), exponent))


def characteristic_faddeev(matrix: list[list[int]]) -> list[int]:
    """Return monic characteristic coefficients, highest degree first."""
    size = len(matrix)
    auxiliary = identity(size)
    coefficients = [1]
    for order in range(1, size + 1):
        product_matrix = matrix_multiply(matrix, auxiliary)
        numerator = -matrix_trace(product_matrix)
        if numerator % order:
            raise ArithmeticError(("nonintegral Faddeev coefficient", order, numerator))
        coefficient = numerator // order
        coefficients.append(coefficient)
        auxiliary = product_matrix
        for i in range(size):
            auxiliary[i][i] += coefficient
    return coefficients


def expected_characteristic(q: int) -> list[int]:
    # lambda^q-(lambda+1)^(q-1), highest degree first.
    return [1] + [-comb(q - 1, degree) for degree in range(q - 1, -1, -1)]


def divisors(number: int) -> list[int]:
    return [d for d in range(1, number + 1) if number % d == 0]


def mobius(number: int) -> int:
    remaining = number
    prime_count = 0
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            remaining //= factor
            prime_count += 1
            if remaining % factor == 0:
                return 0
            while remaining % factor == 0:
                remaining //= factor
        factor += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def least_rotation_period(code: int, q: int, m: int,
                          powers: list[int]) -> int:
    for period in divisors(m):
        if left_rotate(code, q, m, period, powers) == code:
            return period
    raise AssertionError(("period", q, m, code))


def verify_relation_factors(digest) -> None:
    """Check the binomial factor as a relation-matrix coefficient."""
    global GAP_MATRIX_CHECKS
    for q in range(2, 11):
        top = q - 1
        upper = implication_relation(top, q)
        for distance in range(1, 13):
            bridge = matrix_power(upper, distance - 1)
            for a in range(top):
                for b in range(top):
                    relation_count = sum(bridge[a][terminal]
                                         for terminal in range(b + 1, q))
                    closed = gap_closed(top, a, b, distance)
                    check(relation_count == closed,
                          ("relation-gap", q, a, b, distance,
                           relation_count, closed))
                    if distance == 1:
                        check(closed == int(a > b),
                              ("adjacent-gap", q, a, b, closed))
                    GAP_MATRIX_CHECKS += 1
                    digest.update(
                        f"G|{q}|{distance}|{a}|{b}|{relation_count}\n".encode()
                    )


def verify_characteristics(digest) -> None:
    """Use Faddeev--LeVerrier plus the induced trace recurrence."""
    global CHARPOLY_CHECKS
    for q in range(2, 13):
        matrix = core_adjacency(q)
        observed = characteristic_faddeev(matrix)
        expected = expected_characteristic(q)
        check(observed == expected, ("characteristic", q, observed, expected))

        traces = []
        power = identity(q)
        for exponent in range(4 * q + 1):
            traces.append(matrix_trace(power))
            power = matrix_multiply(power, matrix)
        for exponent in range(q, 4 * q + 1):
            recurrence = sum(
                comb(q - 1, h) * traces[exponent - q + h]
                for h in range(q)
            )
            check(traces[exponent] == recurrence,
                  ("trace-recurrence", q, exponent,
                   traces[exponent], recurrence))
        CHARPOLY_CHECKS += 1
        digest.update(f"C|{q}|{tuple(observed)}|{tuple(traces)}\n".encode())


def verify_box(q: int, m: int, digest) -> tuple[int, int, int, int, tuple[int, ...]]:
    global TRANSITIONS, TARGET_CHECKS, HIGHER_TIME_TARGET_CHECKS
    global FIXED_ITERATE_CHECKS

    powers = radix_powers(q, m)
    state_count = powers[m]
    transitions = [0] * state_count
    incoming = [0] * state_count
    core_flags = [False] * state_count

    for code in range(state_count):
        target = literal_step(code, q, m, powers)
        transitions[code] = target
        incoming[target] += 1
        TRANSITIONS += 1
        target_core = is_core(target, q, m, powers)
        source_core = is_core(code, q, m, powers)
        core_flags[code] = source_core
        check(target_core, ("image-subset", q, m, code, target))
        if source_core:
            check(target == left_rotate(code, q, m, 1, powers),
                  ("core-action", q, m, code, target))
        else:
            check(target != code, ("outside-not-fixed", q, m, code))

    core_size = sum(core_flags)
    check(core_size == trace_power(q, m), ("core-trace", q, m, core_size))

    maximum_fibre = 0
    for target in range(state_count):
        csp_count = csp_fibre(target, q, m, powers)
        formula_count = formula_fibre(target, q, m, powers)
        actual_count = incoming[target]
        check(actual_count == csp_count,
              ("literal-vs-CSP", q, m, target, actual_count, csp_count))
        check(csp_count == formula_count,
              ("CSP-vs-product", q, m, target, csp_count, formula_count))
        check((actual_count > 0) == core_flags[target],
              ("image-iff", q, m, target, actual_count, core_flags[target]))
        maximum_fibre = max(maximum_fibre, actual_count)
        TARGET_CHECKS += 1
        digest.update(
            f"F|{q}|{m}|{target}|{actual_count}|{csp_count}|{formula_count}\n".encode()
        )

    top_code = state_count - 1
    fixed_states = [code for code in range(state_count)
                    if transitions[code] == code]
    check(fixed_states == [top_code], ("unique-fixed", q, m, fixed_states))
    check(incoming[top_code] == q, ("all-top-fibre", q, m, incoming[top_code]))
    check(sum(incoming) == state_count, ("mass", q, m, sum(incoming)))
    if m == 1:
        check(core_size == 1, ("m1-core", q, core_size))
        check(all(target == top_code for target in transitions),
              ("m1-collapse", q))

    direct_periods = Counter(
        least_rotation_period(code, q, m, powers)
        for code in range(state_count) if core_flags[code]
    )
    for period in divisors(m):
        primitive = sum(mobius(period // e) * trace_power(q, e)
                        for e in divisors(period))
        check(direct_periods[period] == primitive,
              ("least-period", q, m, period,
               direct_periods[period], primitive))
        check(primitive % period == 0,
              ("cycle-integrality", q, m, period, primitive))

    selected_times = {1, 2, m, m + 1, 2 * m}
    iterate_images = list(range(state_count))
    for steps in range(1, 2 * m + 1):
        iterate_images = [transitions[value] for value in iterate_images]
        actual_fixed = sum(iterate_images[code] == code
                           for code in range(state_count))
        expected_fixed = trace_power(q, gcd(m, steps))
        check(actual_fixed == expected_fixed,
              ("iterate-fixed", q, m, steps,
               actual_fixed, expected_fixed))
        FIXED_ITERATE_CHECKS += 1

        if steps in selected_times:
            iterate_incoming = [0] * state_count
            for target in iterate_images:
                iterate_incoming[target] += 1
            for target in range(state_count):
                rotated = left_rotate(target, q, m, 1 - steps, powers)
                predicted = csp_fibre(rotated, q, m, powers)
                check(iterate_incoming[target] == predicted,
                      ("higher-fibre", q, m, steps, target,
                       iterate_incoming[target], predicted))
                HIGHER_TIME_TARGET_CHECKS += 1

    period_support = tuple(sorted(direct_periods))
    digest.update(
        f"B|{q}|{m}|{state_count}|{core_size}|{maximum_fibre}|{period_support}\n".encode()
    )
    return state_count, core_size, len(fixed_states), maximum_fibre, period_support


def main() -> None:
    digest = sha256()
    verify_relation_factors(digest)
    verify_characteristics(digest)

    boxes = sorted(
        [(q, m) for q in range(2, 8) for m in range(1, 6)]
        + [(2, 9), (3, 8)]
    )
    summaries = []
    total_states = 0
    total_core = 0
    for q, m in boxes:
        summary = verify_box(q, m, digest)
        summaries.append((q, m, summary))
        total_states += summary[0]
        total_core += summary[1]

    last_q, last_m, last = summaries[-1]
    print("P196_HOSTILE_REVIEW_B_EXACT_CONTROL")
    print("REPRESENTATION=packed_radix_relation_matrix_CSP_faddeev_leverrier")
    print("AUTHOR_OR_REVIEW_A_CODE_IMPORTED=false")
    print("BOXES=q2..7_m1..5_plus_q2m9_q3m8")
    print(f"BOX_COUNT={len(boxes)}")
    print(f"STATES={total_states}")
    print(f"CORE_STATES={total_core}")
    print(f"TRANSITIONS={TRANSITIONS}")
    print(f"TARGET_CHECKS={TARGET_CHECKS}")
    print(f"HIGHER_TIME_TARGET_CHECKS={HIGHER_TIME_TARGET_CHECKS}")
    print(f"FIXED_ITERATE_CHECKS={FIXED_ITERATE_CHECKS}")
    print(f"GAP_MATRIX_CHECKS={GAP_MATRIX_CHECKS}")
    print(f"CHARPOLY_CHECKS={CHARPOLY_CHECKS}")
    print(
        f"LAST_BOX=q{last_q}_m{last_m}_states{last[0]}_core{last[1]}_"
        f"fixed{last[2]}_maxfibre{last[3]}_periods"
        f"{','.join(map(str, last[4]))}"
    )
    print(f"ASSERTIONS={ASSERTIONS}")
    print(f"CONTROL_DIGEST={digest.hexdigest()}")
    print("CRITICAL_FINDINGS=0")
    print("MAJOR_FINDINGS=0")
    print("MINOR_FINDINGS=0")
    print("VERDICT=PROVABLE_AS_STATED")
    print("DECISION=ACCEPTED_NO_CHANGE")
    print("OWNER_GATE=OWNER_AMBER")
    print("EXTERNAL_STATE=HOLD_EXTERNAL")
    print("FINITE_CONTROL_IS_NOT_PROOF_OR_NOVELTY=true")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
