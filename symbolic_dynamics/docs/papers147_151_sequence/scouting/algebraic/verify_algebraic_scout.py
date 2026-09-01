#!/usr/bin/env python3
"""Exact breadth falsifier for the P147--P151 algebraic/arithmetic scout.

The ten handles below are ten genuinely different literal finite self-maps.
Sweeping parameters of one literal update still counts as one system.  Every
check uses exact integer or finite-field-coordinate arithmetic from Python's
standard library.  Enumeration is counterexample pressure and theorem triage;
it is not a proof and it says nothing by itself about novelty.
"""

from collections import Counter
from itertools import permutations, product
from math import comb, gcd, isqrt, lcm


ASSERTIONS = 0
RESULTS = []


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def compact(value):
    if isinstance(value, dict):
        return "/".join(f"{key}:{value[key]}" for key in sorted(value))
    if isinstance(value, (tuple, list)):
        return "/".join(compact(item) for item in value)
    return str(value).replace(" ", "_")


def record(handle, carrier, scope, start, signal, decision, reason, **metrics):
    RESULTS.append(
        {
            "id": handle,
            "carrier": carrier,
            "scope": scope,
            "assertions": ASSERTIONS - start,
            "signal": signal,
            "decision": decision,
            "reason": reason,
            "metrics": metrics,
        }
    )


def orbit_data(states, step):
    states = tuple(states)
    state_set = set(states)
    nxt = {}
    for state in states:
        image = step(state)
        check(image in state_set, "literal map left its declared carrier")
        nxt[state] = image
    tails = Counter()
    periods = Counter()
    recurrent = set()
    point_data = {}
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
        check(period >= 1, "functional graph orbit missed recurrence")
        check(nxt[order[-1]] == current, "functional graph did not close")
        tails[tail] += 1
        periods[period] += 1
        recurrent.update(order[tail:])
        point_data[state] = (tail, period)
    fibres = Counter(nxt.values())
    return {
        "nxt": nxt,
        "point_data": point_data,
        "fibres": fibres,
        "states": len(states),
        "fixed": sum(nxt[state] == state for state in states),
        "recurrent": len(recurrent),
        "max_tail": max(tails, default=0),
        "max_period": max(periods, default=0),
        "tails": dict(tails),
        "periods": dict(periods),
        "image": len(fibres),
        "max_fibre": max(fibres.values(), default=0),
    }


def factor_integer(value):
    factors = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor += 1 if divisor == 2 else 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def primes_up_to(bound):
    output = []
    for candidate in range(2, bound + 1):
        if all(candidate % prime for prime in output if prime * prime <= candidate):
            output.append(candidate)
    return output


def v_p_capped(value, prime, cap):
    if value == 0:
        return cap
    exponent = 0
    while exponent < cap and value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def multiplicative_order(value, modulus):
    check(gcd(value, modulus) == 1, "multiplicative order needs a unit")
    current = 1
    for exponent in range(1, modulus + 1):
        current = current * value % modulus
        if current == 1:
            return exponent
    raise AssertionError("multiplicative order search exceeded group size")


def ceil_log_base(value, base):
    check(value >= 1 and base >= 2, "invalid discrete logarithm ceiling")
    exponent = 0
    power = 1
    while power < value:
        power *= base
        exponent += 1
    return exponent


# ---------------------------------------------------------------------------
# QAR: a quadratic absorber on the maximal ideal of Z/p^e Z


def qar_predicted_depth(state, prime, exponent):
    if state == 0:
        return 0
    valuation = v_p_capped(state, prime, exponent)
    if valuation >= 2:
        return exponent - valuation
    unit = state // prime
    branch = v_p_capped(unit + 1, prime, exponent - 1)
    return max(1, exponent - 1 - branch)


def qar_root_count(delta, prime, exponent):
    """Number of s mod p^exponent with s^2=delta."""
    modulus = prime ** exponent
    delta %= modulus
    if delta == 0:
        return prime ** (exponent // 2)
    valuation = v_p_capped(delta, prime, exponent)
    if valuation >= exponent or valuation % 2:
        return 0
    half = valuation // 2
    unit = delta // (prime ** valuation)
    if pow(unit % prime, (prime - 1) // 2, prime) != 1:
        return 0
    return 2 * prime ** half


def qar_expected_profile(prime, exponent):
    if exponent == 2:
        return {0: 1, 1: prime - 1}
    coefficients = Counter({0: 1, 1: 2 * prime - 1})
    for depth in range(2, exponent - 1):
        coefficients[depth] = 2 * (prime - 1) * prime ** (depth - 1)
    coefficients[exponent - 1] = (prime - 2) * prime ** (exponent - 2)
    return dict(sorted(coefficients.items()))


def run_qar():
    start = ASSERTIONS
    boxes = (
        tuple((3, exponent) for exponent in range(2, 9))
        + tuple((5, exponent) for exponent in range(2, 7))
        + tuple((7, exponent) for exponent in range(2, 6))
        + tuple((11, exponent) for exponent in range(2, 5))
    )
    total_states = 0
    profiles = []
    for prime, exponent in boxes:
        modulus = prime ** exponent
        states = tuple(range(0, modulus, prime))

        def step(state):
            return state * (state + prime) % modulus

        data = orbit_data(states, step)
        expected_profile = qar_expected_profile(prime, exponent)
        check(data["tails"] == expected_profile,
              "QAR temporal polynomial failed")
        check(data["recurrent"] == 1 and data["fixed"] == 1,
              "QAR acquired a nonzero recurrent state")
        check(data["max_period"] == 1, "QAR acquired a nontrivial cycle")
        expected_max = 1 if exponent == 2 else exponent - 1
        check(data["max_tail"] == expected_max, "QAR sharp clock failed")
        for state in states:
            tail, period = data["point_data"][state]
            check(tail == qar_predicted_depth(state, prime, exponent),
                  "QAR pointwise absorption time failed")
            check(period == 1, "QAR did not end at a fixed absorber")
        if exponent == 2:
            check(data["image"] == 1 and data["max_fibre"] == prime,
                  "QAR e=2 collapse failed")
        else:
            reduced_exponent = exponent - 2
            reduced_modulus = prime ** reduced_exponent
            expected_image = 1 + sum(
                (prime - 1) * prime ** (reduced_exponent - 2 * half - 1) // 2
                for half in range((reduced_exponent - 1) // 2 + 1)
            )
            check(data["image"] == expected_image, "QAR image-size formula failed")
            root_hist = Counter((root * root) % reduced_modulus
                                for root in range(reduced_modulus))
            for target in states:
                expected_fibre = 0
                if target % (prime * prime) == 0:
                    reduced_target = (target // (prime * prime)) % reduced_modulus
                    delta = (1 + 4 * reduced_target) % reduced_modulus
                    predicted_roots = qar_root_count(
                        delta, prime, reduced_exponent
                    )
                    check(root_hist.get(delta, 0) == predicted_roots,
                          "QAR square-root multiplicity formula failed")
                    expected_fibre = prime * predicted_roots
                check(data["fibres"].get(target, 0) == expected_fibre,
                      "QAR all-target fibre atlas failed")
        total_states += len(states)
        if (prime, exponent) in ((3, 6), (5, 6), (7, 5), (11, 4)):
            profiles.append(
                f"p{prime}e{exponent}:D{compact(data['tails'])}:"
                f"I{data['image']}:M{data['max_fibre']}"
            )
    record(
        "QAR", "maximal_ideal_pZ_mod_p^e",
        "odd p: (3,2..8),(5,2..6),(7,2..5),(11,2..4); x->x(x+p)",
        start,
        "single absorber; exact branched valuation clock and depth polynomial; discriminant square-root fibre atlas",
        "SELECT_INTERNAL_OWNER_PENDING",
        "literal map has a coherent theorem package, but affine quadratic/p-adic owner subtraction remains mandatory",
        boxes=len(boxes), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# TMD: multiplication by the absolute trace on F_{p^n}


def order_in_prime_field(value, prime):
    if value % prime == 0:
        return 0
    return multiplicative_order(value % prime, prime)


def run_tmd():
    start = ASSERTIONS
    boxes = (
        tuple((3, degree) for degree in range(2, 6))
        + tuple((5, degree) for degree in range(2, 5))
        + tuple((7, degree) for degree in range(2, 5))
        + tuple((11, degree) for degree in range(2, 4))
    )
    total_states = 0
    profiles = []
    for prime, degree in boxes:
        states = tuple(product(range(prime), repeat=degree))

        def trace(state):
            return sum(state) % prime

        def scale(scalar, state):
            return tuple(scalar * coordinate % prime for coordinate in state)

        def step(state):
            return scale(trace(state), state)

        data = orbit_data(states, step)
        group_order = prime - 1
        two_part = 0
        odd_part = group_order
        while odd_part % 2 == 0:
            odd_part //= 2
            two_part += 1
        expected_tails = Counter({0: 1, 1: prime ** (degree - 1) - 1})
        expected_tails[0] += prime ** (degree - 1) * odd_part
        for valuation in range(1, two_part + 1):
            expected_tails[valuation] += (
                prime ** (degree - 1) * (2 ** (valuation - 1)) * odd_part
            )
        check(data["tails"] == dict(expected_tails),
              "TMD temporal polynomial failed")
        check(data["recurrent"] == 1 + prime ** (degree - 1) * odd_part,
              "TMD recurrent census failed")
        check(data["fixed"] == 1 + prime ** (degree - 1),
              "TMD fixed-point census failed")
        for state in states:
            scalar = trace(state)
            current = state
            for iterate in range(7):
                predicted = (state if iterate == 0 else
                             scale(pow(scalar, 2 ** iterate - 1, prime), state))
                check(current == predicted, "TMD closed iterate formula failed")
                current = step(current)
            tail, period = data["point_data"][state]
            if scalar == 0:
                check(tail == (0 if all(x == 0 for x in state) else 1),
                      "TMD trace-zero tail failed")
                check(period == 1, "TMD trace-zero orbit missed zero")
            else:
                scalar_order = order_in_prime_field(scalar, prime)
                valuation = 0
                odd_order = scalar_order
                while odd_order % 2 == 0:
                    valuation += 1
                    odd_order //= 2
                expected_period = 1 if odd_order == 1 else multiplicative_order(2, odd_order)
                check(tail == valuation and period == expected_period,
                      "TMD pointwise order decomposition failed")
        for target in states:
            target_trace = trace(target)
            is_zero = all(value == 0 for value in target)
            if is_zero:
                expected_fibre = prime ** (degree - 1)
            elif target_trace and pow(target_trace, (prime - 1) // 2, prime) == 1:
                expected_fibre = 2
            else:
                expected_fibre = 0
            check(data["fibres"].get(target, 0) == expected_fibre,
                  "TMD all-target fibre atlas failed")
        total_states += len(states)
        if (prime, degree) in ((3, 5), (5, 4), (7, 4), (11, 3)):
            profiles.append(
                f"p{prime}n{degree}:D{compact(data['tails'])}:"
                f"R{data['recurrent']}:P{data['max_period']}:I{data['image']}"
            )
    record(
        "TMD", "finite_field_F_p^n_in_trace_normal_coordinates",
        "odd p: degrees through 5; x->x Tr(x)",
        start,
        "closed iterates; exact 2-primary tail/odd-order cycle law; complete temporal and fibre formulae",
        "SELECT_INTERNAL_OWNER_PENDING",
        "strong literal signal; x*h(Tr(x)) permutation-polynomial literature creates medium-high owner risk",
        boxes=len(boxes), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# ASH: the Artin--Schreier difference x^p-x


def run_ash():
    start = ASSERTIONS
    boxes = (
        tuple((2, degree) for degree in range(2, 11))
        + tuple((3, degree) for degree in range(2, 8))
        + tuple((5, degree) for degree in range(2, 6))
    )
    total_states = 0
    profiles = []
    for prime, degree in boxes:
        states = tuple(product(range(prime), repeat=degree))

        def step(state):
            shifted = state[-1:] + state[:-1]
            return tuple((shifted[index] - state[index]) % prime
                         for index in range(degree))

        data = orbit_data(states, step)
        check(data["image"] == prime ** (degree - 1),
              "ASH image hyperplane size failed")
        for target in states:
            expected_fibre = prime if sum(target) % prime == 0 else 0
            check(data["fibres"].get(target, 0) == expected_fibre,
                  "ASH Artin-Schreier fibre formula failed")
        kernel = [state for state in states if data["nxt"][state] == (0,) * degree]
        check(len(kernel) == prime, "ASH constant-field kernel failed")
        check(all(len(set(state)) == 1 for state in kernel),
              "ASH kernel was not the constant coordinate line")
        total_states += len(states)
        if (prime, degree) in ((2, 10), (3, 7), (5, 5)):
            profiles.append(
                f"p{prime}n{degree}:T{data['max_tail']}:P{data['max_period']}:"
                f"R{data['recurrent']}:D{compact(data['tails'])}"
            )
    record(
        "ASH", "finite_field_normal_basis_coordinates",
        "p=2,n<=10; p=3,n<=7; p=5,n<=5; x->x^p-x",
        start,
        "exact trace-zero image and constant-field fibres, but graph is a generic linear operator",
        "KILL_OWNER_LINEAR",
        "Artin-Schreier linear algebra and finite linear dynamical systems already own the mechanism",
        boxes=len(boxes), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# TFS: truncated Frobenius shear f -> f+f^p


def run_tfs():
    start = ASSERTIONS
    boxes = (
        tuple((2, degree) for degree in range(2, 12))
        + tuple((3, degree) for degree in range(2, 8))
        + tuple((5, degree) for degree in range(2, 6))
    )
    total_states = 0
    profiles = []
    for prime, truncation in boxes:
        states = tuple(product(range(prime), repeat=truncation - 1))

        def step(state):
            output = list(state)
            for exponent in range(1, truncation):
                target = exponent * prime
                if target < truncation:
                    output[target - 1] = (output[target - 1] + state[exponent - 1]) % prime
            return tuple(output)

        data = orbit_data(states, step)
        nilpotency_height = ceil_log_base(truncation, prime)
        predicted_order = prime ** ceil_log_base(nilpotency_height, prime)
        kernel_dimension = truncation - 1 - (truncation - 1) // prime
        check(data["max_tail"] == 0, "TFS invertible shear acquired a tail")
        check(data["recurrent"] == len(states), "TFS missed a recurrent state")
        check(data["max_period"] == predicted_order,
              "TFS p-power order formula failed")
        check(data["fixed"] == prime ** kernel_dimension,
              "TFS Frobenius-kernel fixed census failed")
        current = {state: state for state in states}
        for _ in range(predicted_order):
            current = {state: step(image) for state, image in current.items()}
        check(all(current[state] == state for state in states),
              "TFS predicted global order did not annihilate the shear")
        total_states += len(states)
        if (prime, truncation) in ((2, 11), (3, 7), (5, 5)):
            profiles.append(
                f"p{prime}N{truncation}:O{predicted_order}:"
                f"F{data['fixed']}:C{compact(data['periods'])}"
            )
    record(
        "TFS", "nilpotent_ideal_xF_p[x]/(x^N)",
        "p=2,N<=11; p=3,N<=7; p=5,N<=5; f->f+f^p",
        start,
        "exact p-power permutation order and fixed-space dimension",
        "KILL_INTERNAL_OWNER",
        "a unipotent linear Frobenius shear, close to the occupied bounded-Cartier/truncated-polynomial lane",
        boxes=len(boxes), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# SPP: state-dependent power on the symmetric group


def permutation_cycles(permutation):
    visited = [False] * len(permutation)
    cycles = []
    for start in range(len(permutation)):
        if visited[start]:
            continue
        cycle = []
        current = start
        while not visited[current]:
            visited[current] = True
            cycle.append(current)
            current = permutation[current]
        cycles.append(tuple(cycle))
    return cycles


def permutation_power(permutation, exponent):
    output = [None] * len(permutation)
    for cycle in permutation_cycles(permutation):
        length = len(cycle)
        for index, value in enumerate(cycle):
            output[value] = cycle[(index + exponent) % length]
    return tuple(output)


def run_spp():
    start = ASSERTIONS
    total_states = 0
    profiles = []
    for degree in range(2, 9):
        states = tuple(permutations(range(degree)))

        def step(state):
            cycle_count = len(permutation_cycles(state))
            return permutation_power(state, cycle_count)

        data = orbit_data(states, step)
        for state in states:
            cycles = permutation_cycles(state)
            cycle_count = len(cycles)
            image_count = len(permutation_cycles(data["nxt"][state]))
            check(image_count >= cycle_count,
                  "SPP cycle count decreased under powering")
            stable_now = all(gcd(cycle_count, len(cycle)) == 1 for cycle in cycles)
            check((data["point_data"][state][0] == 0) == stable_now,
                  "SPP recurrence criterion failed")
        total_states += len(states)
        profiles.append(
            f"n{degree}:T{data['max_tail']}:P{data['max_period']}:"
            f"R{data['recurrent']}:I{data['image']}"
        )
    record(
        "SPP", "symmetric_group_S_n",
        "2<=n<=8; sigma->sigma^(number of cycles of sigma)",
        start,
        "monotone cycle-count Lyapunov function and exact recurrent criterion, but no tractable global fibre/clock atlas",
        "KILL_HARD_EXCLUSION",
        "state-dependent group powering becomes partition-arithmetic casework without a paper-scale all-n spine",
        boxes=7, states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# CMD: iteration of the Carmichael exponent


def carmichael_lambda(value):
    if value == 1:
        return 1
    components = []
    for prime, exponent in factor_integer(value).items():
        if prime == 2 and exponent >= 3:
            component = 2 ** (exponent - 2)
        else:
            component = (prime - 1) * prime ** (exponent - 1)
        components.append(component)
    answer = 1
    for component in components:
        answer = lcm(answer, component)
    return answer


def run_cmd():
    start = ASSERTIONS
    bound = 20000
    states = tuple(range(1, bound + 1))
    data = orbit_data(states, carmichael_lambda)
    check(data["recurrent"] == 1 and data["fixed"] == 1,
          "CMD acquired a nontrivial recurrent endpoint")
    check(data["max_period"] == 1, "CMD acquired a nontrivial cycle")
    for state in states:
        image = data["nxt"][state]
        check(image == 1 if state == 1 else image < state,
              "CMD strict Carmichael descent failed")
    profiles = []
    for cutoff in (100, 1000, 10000, 20000):
        histogram = Counter(data["point_data"][state][0]
                            for state in range(1, cutoff + 1))
        profiles.append(
            f"B{cutoff}:T{max(histogram)}:D{compact(dict(histogram))}"
        )
    record(
        "CMD", "initial_interval_of_positive_integers",
        "1<=n<=20000; n->Carmichael lambda(n)",
        start,
        "strict arithmetic descent with visible iterated-exponent profiles",
        "KILL_DIRECT_OWNER",
        "the iterated Carmichael function is itself a mature named subject, so the literal system is owner-hit",
        boxes=1, states=len(states), profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# QCW: the quadratic-character nearest-neighbour walk


def legendre(value, prime):
    value %= prime
    if value == 0:
        return 0
    symbol = pow(value, (prime - 1) // 2, prime)
    return 1 if symbol == 1 else -1


def run_qcw():
    start = ASSERTIONS
    primes = tuple(prime for prime in primes_up_to(997) if prime % 2)
    total_states = 0
    profiles = []
    record_primes = {7, 31, 127, 251, 499, 997}
    for prime in primes:
        states = tuple(range(prime))

        def step(state):
            return 0 if state == 0 else (state + legendre(state, prime)) % prime

        data = orbit_data(states, step)
        sign_minus_one = legendre(-1, prime)
        boundary_pairs = sum(
            legendre(state, prime) == 1
            and legendre(state + 1, prime) == -1
            for state in range(1, prime - 1)
        )
        check(boundary_pairs == (prime - sign_minus_one) // 4,
              "QCW residue/nonresidue boundary count failed")
        check(data["recurrent"] == 1 + 2 * boundary_pairs,
              "QCW recurrent census failed")
        check(data["fixed"] == 1 and data["max_period"] <= 2,
              "QCW recurrent structure exceeded fixed/2-cycles")
        check(data["max_fibre"] <= 2, "QCW local walk acquired a large fibre")
        for state in states:
            if state:
                check((data["nxt"][state] - state) % prime in (1, prime - 1),
                      "QCW step was not nearest-neighbour")
        total_states += prime
        if prime in record_primes:
            profiles.append(
                f"p{prime}:T{data['max_tail']}:R{data['recurrent']}:"
                f"D{compact(data['tails'])}"
            )
    record(
        "QCW", "prime_field_F_p",
        "all odd primes p<=997; 0->0, x!=0 -> x+Legendre(x)",
        start,
        "exact fixed/2-cycle boundary census; transient clock equals irregular Legendre-run geometry",
        "KILL_THEOREM_THIN",
        "a sharp all-p maximum tail would require control of longest quadratic-residue runs, so early signal does not close",
        boxes=len(primes), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# MFR: a multiplicative Fibonacci map with absorbing coordinate boundary


def matrix_multiply(left, right):
    return (
        (left[0][0] * right[0][0] + left[0][1] * right[1][0],
         left[0][0] * right[0][1] + left[0][1] * right[1][1]),
        (left[1][0] * right[0][0] + left[1][1] * right[1][0],
         left[1][0] * right[0][1] + left[1][1] * right[1][1]),
    )


def matrix_power(matrix, exponent):
    answer = ((1, 0), (0, 1))
    while exponent:
        if exponent & 1:
            answer = matrix_multiply(answer, matrix)
        matrix = matrix_multiply(matrix, matrix)
        exponent //= 2
    return answer


def run_mfr():
    start = ASSERTIONS
    primes = tuple(prime for prime in primes_up_to(43))
    total_states = 0
    profiles = []
    fibonacci_matrix = ((0, 1), (1, 1))
    for prime in primes:
        states = tuple(product(range(prime), repeat=2))

        def step(state):
            x, y = state
            return (y, x * y % prime)

        data = orbit_data(states, step)
        expected_tails = {0: (prime - 1) ** 2 + 1,
                          1: prime - 1,
                          2: prime - 1}
        expected_tails = {key: value for key, value in expected_tails.items() if value}
        check(data["tails"] == expected_tails, "MFR boundary depth polynomial failed")
        check(data["recurrent"] == (prime - 1) ** 2 + 1,
              "MFR recurrent torus census failed")
        check(data["fixed"] == 2, "MFR fixed-point census failed")
        check(data["image"] == prime * (prime - 1) + 1,
              "MFR image census failed")
        for target in states:
            x, y = target
            expected_fibre = prime if target == (0, 0) else (1 if x else 0)
            check(data["fibres"].get(target, 0) == expected_fibre,
                  "MFR every-target fibre formula failed")
        modulus = prime - 1
        for iterate in range(1, 13):
            power = matrix_power(fibonacci_matrix, iterate)
            difference = (
                (power[0][0] - 1, power[0][1]),
                (power[1][0], power[1][1] - 1),
            )
            invariant_one = gcd(*(abs(value) for row in difference for value in row))
            determinant = abs(
                difference[0][0] * difference[1][1]
                - difference[0][1] * difference[1][0]
            )
            check(invariant_one > 0 and determinant > 0,
                  "MFR Smith invariants degenerated")
            invariant_two = determinant // invariant_one
            predicted_fixed = 1 + gcd(modulus, invariant_one) * gcd(modulus, invariant_two)
            actual_fixed = 0
            for state in states:
                current = state
                for _ in range(iterate):
                    current = data["nxt"][current]
                actual_fixed += current == state
            check(actual_fixed == predicted_fixed,
                  "MFR Smith-normal fixed-iterate census failed")
        total_states += len(states)
        if prime in (2, 5, 11, 23, 43):
            profiles.append(
                f"p{prime}:T{data['max_tail']}:P{data['max_period']}:"
                f"R{data['recurrent']}:I{data['image']}"
            )
    record(
        "MFR", "affine_plane_F_p^2",
        "all primes p<=43; (x,y)->(y,xy)",
        start,
        "depth-two absorbing boundary, complete fibres, torus conjugacy to the Fibonacci matrix, Smith fixed-iterate formula",
        "RESERVE_OWNER_COMPRESSED",
        "most long dynamics is the standard finite Fibonacci toral automorphism; only the boundary extension is new-looking",
        boxes=len(primes), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# LBG: gcd descent driven by the central binomial coefficient


def run_lbg():
    start = ASSERTIONS
    bound = 2500
    states = tuple(range(1, bound + 1))

    def step(state):
        return gcd(state, comb(2 * state, state))

    data = orbit_data(states, step)
    check(data["max_period"] == 1, "LBG divisibility descent acquired a cycle")
    for state in states:
        image = data["nxt"][state]
        check(state % image == 0 and image <= state,
              "LBG output was not a divisor descent")
        check((data["point_data"][state][0] == 0) == (image == state),
              "LBG recurrent/fixed criterion failed")
    profiles = []
    for cutoff in (50, 500, 2500):
        histogram = Counter(data["point_data"][state][0]
                            for state in range(1, cutoff + 1))
        profiles.append(
            f"B{cutoff}:T{max(histogram)}:F{histogram[0]}:D{compact(dict(histogram))}"
        )
    record(
        "LBG", "initial_interval_of_positive_integers",
        "1<=n<=2500; n->gcd(n,binomial(2n,n))",
        start,
        "short exact divisor descent, but irregular fixed endpoints and no stable parameter-level clock emerged",
        "KILL_NO_SPINE",
        "central-binomial divisibility is deep owner territory while the dynamical wrapper adds no closed all-bound theorem",
        boxes=1, states=len(states), profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# GND: finite quadratic-field norm followed by base-field squaring


def least_nonsquare(prime):
    for candidate in range(2, prime):
        if legendre(candidate, prime) == -1:
            return candidate
    raise AssertionError("odd prime had no nonsquare")


def run_gnd():
    start = ASSERTIONS
    primes = tuple(prime for prime in primes_up_to(43) if prime % 2)
    total_states = 0
    profiles = []
    for prime in primes:
        nonsquare = least_nonsquare(prime)
        states = tuple(product(range(prime), repeat=2))

        def norm(state):
            x, y = state
            return (x * x - nonsquare * y * y) % prime

        def step(state):
            return (norm(state), 0)

        data = orbit_data(states, step)
        for target in states:
            if target == (0, 0):
                expected_fibre = 1
            elif target[1] == 0 and target[0] != 0:
                expected_fibre = prime + 1
            else:
                expected_fibre = 0
            check(data["fibres"].get(target, 0) == expected_fibre,
                  "GND finite-field norm fibre formula failed")
        for state in states:
            initial_norm = norm(state)
            current = state
            for iterate in range(1, 6):
                current = data["nxt"][current]
                predicted = (pow(initial_norm, 2 ** (iterate - 1), prime), 0)
                check(current == predicted, "GND norm/square iterate formula failed")
        check(data["image"] == prime, "GND base-axis image failed")
        check(data["max_fibre"] == prime + 1,
              "GND nonzero norm fibre size failed")
        total_states += len(states)
        if prime in (3, 7, 19, 43):
            profiles.append(
                f"p{prime}:T{data['max_tail']}:P{data['max_period']}:"
                f"R{data['recurrent']}:D{compact(data['tails'])}"
            )
    record(
        "GND", "quadratic_finite_field_F_p^2",
        "all odd primes p<=43; (x,y)->(x^2-dy^2,0), d a nonsquare",
        start,
        "complete norm fibres and closed iterates, but the graph is exactly a norm collapse followed by scalar squaring",
        "KILL_DIRECT_OWNER",
        "standard finite-field norm plus the fully owned square map leaves no independent theorem mechanism",
        boxes=len(primes), states=total_states, profiles=";".join(profiles),
    )


def main():
    run_qar()
    run_tmd()
    run_ash()
    run_tfs()
    run_spp()
    run_cmd()
    run_qcw()
    run_mfr()
    run_lbg()
    run_gnd()
    check(len(RESULTS) == 10, "scout did not contain ten literal systems")
    check(len({row["id"] for row in RESULTS}) == 10,
          "scout handles were not distinct")
    print("PASS algebraic scout")
    for row in RESULTS:
        fields = [
            row["id"],
            f"carrier={compact(row['carrier'])}",
            f"scope={compact(row['scope'])}",
            f"assertions={row['assertions']}",
            f"signal={compact(row['signal'])}",
            f"decision={row['decision']}",
            f"reason={compact(row['reason'])}",
        ]
        fields.extend(f"{key}={compact(value)}"
                      for key, value in row["metrics"].items())
        print("|".join(fields))
    counts = Counter(row["decision"].split("_")[0] for row in RESULTS)
    print(
        "TOTAL|systems=10|assertions={}|selected={}|reserves={}|kills={}|"
        "status=HOLD_EXTERNAL".format(
            ASSERTIONS,
            counts.get("SELECT", 0),
            counts.get("RESERVE", 0),
            counts.get("KILL", 0),
        )
    )


if __name__ == "__main__":
    main()
