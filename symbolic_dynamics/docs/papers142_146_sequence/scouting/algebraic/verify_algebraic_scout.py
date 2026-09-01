#!/usr/bin/env python3
"""Exact algebraic/arithmetic breadth scout for the P142--P146 intake.

The ten handles below are ten literal finite self-maps on ten different
carriers.  Parameter sweeps of one literal map count once.  Enumeration is
counterexample pressure and theorem triage, never proof or novelty evidence.
Only Python's standard library and exact integer/finite-field arithmetic are
used.
"""

from collections import Counter
from itertools import combinations, permutations
from math import gcd, isqrt


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
    }


def ceil_log_two(value):
    """Least k with 2**k >= value, for positive integer value."""
    check(value >= 1, "ceil_log_two expects a positive integer")
    return (value - 1).bit_length()


# ---------------------------------------------------------------------------
# VGT: prime-power divisors under a valuation-gcd tent map


def v_p(value, prime):
    exponent = 0
    while value % prime == 0 and value:
        value //= prime
        exponent += 1
    return exponent


def vgt_predicted_depth(exponent, state):
    lower = (exponent + 2) // 3
    upper = 2 * exponent // 3
    if state == 0 or lower <= state <= upper:
        return 0
    if state < lower:
        depth = 0
        current = state
        while current < lower:
            current *= 2
            depth += 1
        return depth
    reflected = exponent - state
    if reflected == 0:
        return 1
    depth = 1
    while reflected < lower:
        reflected *= 2
        depth += 1
    return depth


def run_vgt():
    start = ASSERTIONS
    primes = (3, 5, 7, 11)
    total_states = 0
    profiles = []
    for prime in primes:
        for exponent in range(2, 129):
            modulus = prime ** exponent
            states = tuple(range(exponent + 1))

            def step(state):
                divisor = prime ** state
                literal = gcd(modulus, divisor * divisor + modulus // divisor)
                output_exponent = v_p(literal, prime)
                predicted = min(2 * state, exponent - state)
                check(literal == prime ** output_exponent,
                      "gcd output is not a pure prime power")
                check(output_exponent == predicted,
                      "valuation tent rule failed")
                return output_exponent

            data = orbit_data(states, step)
            lower = (exponent + 2) // 3
            upper = 2 * exponent // 3
            recurrent_count = upper - lower + 2
            fixed_count = 1 + (exponent % 2 == 0)
            check(data["recurrent"] == recurrent_count,
                  "recurrent interval census failed")
            check(data["fixed"] == fixed_count,
                  "fixed divisor census failed")
            check(data["max_period"] <= 2,
                  "valuation tent acquired a long cycle")
            for iterate in range(1, 9):
                fixed_iterate = 0
                for state in states:
                    current = state
                    for _ in range(iterate):
                        current = data["nxt"][current]
                    fixed_iterate += current == state
                predicted_fixed_iterate = (fixed_count if iterate % 2
                                             else recurrent_count)
                check(fixed_iterate == predicted_fixed_iterate,
                      "fixed-iterate parity formula failed")
            expected_fibres = Counter()
            for target in states:
                preimages = set()
                if target <= upper:
                    preimages.add(exponent - target)
                    if target % 2 == 0:
                        preimages.add(target // 2)
                expected_fibres[target] = len(preimages)
                check(data["fibres"].get(target, 0) == len(preimages),
                      "all-target one-step fibre formula failed")
            check(sum(value > 0 for value in expected_fibres.values()) == upper + 1,
                  "image interval census failed")
            depth_hist = Counter()
            for state in states:
                predicted_depth = vgt_predicted_depth(exponent, state)
                tail, period = data["point_data"][state]
                check(tail == predicted_depth,
                      "pointwise valuation-tent depth failed")
                if tail == 0:
                    check(state == 0 or lower <= state <= upper,
                          "recurrent state lies outside the claimed interval")
                    check(period == (1 if state == 0 or 2 * state == exponent else 2),
                          "recurrent complement pairing failed")
                depth_hist[tail] += 1
            m = ceil_log_two(lower)
            coefficients = Counter({0: recurrent_count, 1: 1})
            for depth in range(1, m + 1):
                count = ((lower + (1 << (depth - 1)) - 1) // (1 << (depth - 1))
                         - (lower + (1 << depth) - 1) // (1 << depth))
                coefficients[depth] += count
                coefficients[depth + 1] += count
            check(dict(sorted(coefficients.items())) == dict(sorted(depth_hist.items())),
                  "temporal generating polynomial coefficients failed")
            expected_max = 1 + m
            check(data["max_tail"] == expected_max,
                  "sharp valuation-tent clock failed")
            if exponent >= 4:
                deepest = [state for state in states
                           if data["point_data"][state][0] == expected_max]
                check(deepest == [exponent - 1],
                      "unique deepest divisor witness failed")
            else:
                check(data["point_data"][exponent][0] == 1,
                      "small-exponent boundary witness failed")
            total_states += len(states)
            if prime == 3 and exponent in (4, 8, 16, 32, 64, 128):
                profiles.append(
                    f"e{exponent}:R{recurrent_count}:I{upper + 1}:"
                    f"T{expected_max}:D{compact(dict(sorted(depth_hist.items())))}"
                )
    for state in range(1, 17):
        exponent = 3 * state
        modulus = 1 << exponent
        divisor = 1 << state
        exceptional = v_p(gcd(modulus, divisor * divisor + modulus // divisor), 2)
        check(exceptional == 2 * state + 1,
              "characteristic-two equal-valuation boundary was not detected")
    record(
        "VGT", "odd_prime_power_divisors",
        "p in {3,5,7,11}; 2<=e<=128; d|p^e; d->gcd(p^e,d^2+p^e/d)",
        start,
        "complete fixed/two-cycle interval, exact temporal polynomial, image interval, every-target fibres, unique deepest divisor",
        "FINALIST_INTERNAL_CONTRACT",
        "literal-owner status unresolved; piecewise valuation map is portfolio-distinct but needs owner subtraction",
        boxes=len(primes) * 127, states=total_states,
        max_tail_at_e128=1 + ceil_log_two((128 + 2) // 3),
        sharp_witness_at_e128=127, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# DNT: normalizer towers on every subgroup of a dihedral 2-group


def dihedral_mul(left, right, order):
    a, b = left
    c, d = right
    return ((a + (c if b == 0 else -c)) % order, (b + d) % 2)


def dihedral_inv(element, order):
    a, b = element
    return ((-a) % order, 0) if b == 0 else (a, 1)


def dihedral_conjugate(g, h, order):
    return dihedral_mul(dihedral_mul(g, h, order), dihedral_inv(g, order), order)


def dihedral_subgroups(power):
    order = 1 << power
    entries = []
    for k in range(power + 1):
        step = 1 << k
        rotations = frozenset((value, 0) for value in range(0, order, step))
        entries.append((('R', k, 0), rotations))
    for k in range(power + 1):
        step = 1 << k
        for shift in range(step):
            rotations = {(value, 0) for value in range(0, order, step)}
            reflections = {((shift + value) % order, 1)
                           for value in range(0, order, step)}
            entries.append((('H', k, shift), frozenset(rotations | reflections)))
    return entries


def run_dnt():
    start = ASSERTIONS
    total_states = 0
    profiles = []
    for power in range(1, 9):
        order = 1 << power
        group = tuple((a, b) for b in (0, 1) for a in range(order))
        entries = dihedral_subgroups(power)
        key_to_group = dict(entries)
        group_to_key = {value: key for key, value in entries}
        check(len(key_to_group) == len(group_to_key) == 2 * order + power,
              "dihedral subgroup classification has duplicates or omissions")
        full_key = ('H', 0, 0)
        literal_next = {}
        for key, subgroup in entries:
            normalizer = set()
            for element in group:
                if all(dihedral_conjugate(element, h, order) in subgroup
                       for h in subgroup):
                    normalizer.add(element)
            normalizer = frozenset(normalizer)
            check(normalizer in group_to_key,
                  "normalizer is missing from the classified subgroup carrier")
            literal_next[key] = group_to_key[normalizer]
            kind, k, shift = key
            if kind == 'R' or k == 0:
                predicted = full_key
            else:
                predicted = ('H', k - 1, shift % (1 << (k - 1)))
            check(literal_next[key] == predicted,
                  "dihedral normalizer-halving formula failed")
            check(subgroup <= normalizer, "normalizer tower is not inflationary")

        data = orbit_data(key_to_group, literal_next.__getitem__)
        check(data["fixed"] == data["recurrent"] == 1,
              "dihedral normalizer tower should have unique recurrent group")
        check(data["max_tail"] == power,
              "sharp dihedral normalizer clock failed")
        check(data["max_period"] == 1,
              "normalizer tower acquired a nontrivial cycle")
        expected_depths = Counter({0: 1, 1: power + 1})
        for k in range(1, power + 1):
            expected_depths[k] += 1 << k
        observed_depths = Counter(tail for tail, _ in data["point_data"].values())
        check(observed_depths == expected_depths,
              "dihedral normalizer temporal polynomial failed")
        deepest = [key for key, value in data["point_data"].items()
                   if value[0] == power]
        if power >= 2:
            check(len(deepest) == order and all(key[0] == 'H' and key[1] == power
                                               for key in deepest),
                  "reflection subgroups are not exactly the sharp witnesses")
        else:
            check(all(data["point_data"][('H', power, shift)][0] == power
                      for shift in range(order)),
                  "small dihedral reflection witnesses failed")
        for target in key_to_group:
            kind, k, _ = target
            if target == full_key:
                expected = power + 4
            elif kind == 'H' and 1 <= k <= power - 1:
                expected = 2
            else:
                expected = 0
            check(data["fibres"].get(target, 0) == expected,
                  "dihedral every-target normalizer fibre failed")
        check(sum(value > 0 for value in data["fibres"].values()) == order - 1,
              "dihedral normalizer image census failed")
        total_states += len(entries)
        profiles.append(
            f"m{power}:S{len(entries)}:I{order - 1}:T{power}:"
            f"FG{power + 4}:D{compact(dict(sorted(expected_depths.items())))}"
        )
    record(
        "DNT", "subgroups_of_dihedral_2_groups",
        "all subgroups of D_(2^(m+1)), 1<=m<=8; H->N_G(H)",
        start,
        "unique fixed full group, sharp m-step tower, exact temporal polynomial, image and every-target fibres",
        "RESERVE_OWNER_COMPRESSED",
        "normalizer towers and the dihedral subgroup classifier are classical inputs; retain only as a replacement reserve",
        boxes=8, states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# PCR: standard quadratic Cremona transformation on a finite projective plane


def projective_plane_points(prime):
    points = [(1, y, z) for y in range(prime) for z in range(prime)]
    points += [(0, 1, z) for z in range(prime)]
    points += [(0, 0, 1)]
    return tuple(points)


def projective_normalize(vector, prime):
    for value in vector:
        if value % prime:
            inverse = pow(value, -1, prime)
            return tuple((entry * inverse) % prime for entry in vector)
    return None


def run_pcr():
    start = ASSERTIONS
    primes = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)
    total_states = 0
    profiles = []
    for prime in primes:
        points = projective_plane_points(prime)
        states = points + (None,)

        def step(point):
            if point is None:
                return None
            x, y, z = point
            return projective_normalize((y * z, z * x, x * y), prime)

        data = orbit_data(states, step)
        recurrent = (prime - 1) ** 2 + 1
        check(data["recurrent"] == recurrent,
              "Cremona recurrent torus-plus-sink census failed")
        check(data["fixed"] == 5,
              "odd-field Cremona fixed-point census failed")
        expected_max_period = 1 if prime == 3 else 2
        check(data["max_tail"] == 2 and data["max_period"] == expected_max_period,
              "Cremona tail/period silhouette failed")
        expected_depths = {0: recurrent, 1: 3, 2: 3 * (prime - 1)}
        observed_depths = Counter(tail for tail, _ in data["point_data"].values())
        check(dict(observed_depths) == expected_depths,
              "Cremona temporal polynomial failed")
        for target in states:
            if target is None:
                expected = 4
            else:
                zeros = sum(value == 0 for value in target)
                if zeros == 0:
                    expected = 1
                elif zeros == 2:
                    expected = prime - 1
                else:
                    expected = 0
            check(data["fibres"].get(target, 0) == expected,
                  "Cremona all-target fibre formula failed")
        check(sum(value > 0 for value in data["fibres"].values())
              == (prime - 1) ** 2 + 4,
              "Cremona image census failed")
        total_states += len(states)
        profiles.append(
            f"p{prime}:S{len(states)}:R{recurrent}:"
            f"C2{(recurrent - 5) // 2}:MF{max(4, prime - 1)}"
        )
    record(
        "PCR", "finite_projective_planes_with_sink",
        "P^2(F_p) plus sink for 13 odd primes through 43; [x:y:z]->[yz:zx:xy]",
        start,
        "complete torus involution, boundary depth-two law, exact fixed/cycle/image/fibre census",
        "KILL_INTERNAL_AND_CLASSICAL",
        "projective diagonal-adjugation is both classical Cremona inversion and too close to P103 double-adjugate dynamics",
        boxes=len(primes), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# FAI: Frobenius-image chains inside truncated bivariate algebras


def frobenius_basis_image(basis, prime, x_bound, y_bound):
    return frozenset(
        (prime * i, prime * j)
        for i, j in basis
        if prime * i < x_bound and prime * j < y_bound
    )


def ceil_log_base(value, base):
    check(value >= 1 and base >= 2, "invalid exact logarithm input")
    power = 1
    exponent = 0
    while power < value:
        power *= base
        exponent += 1
    return exponent


def run_fai():
    start = ASSERTIONS
    boxes = []
    for prime in (2, 3, 5):
        for x_bound, y_bound in ((2, 3), (3, 5), (4, 7), (6, 10), (9, 12), (12, 12)):
            boxes.append((prime, x_bound, y_bound))
    total_states = 0
    profiles = []
    for prime, x_bound, y_bound in boxes:
        initial = frozenset((i, j) for i in range(x_bound) for j in range(y_bound))
        orbit = []
        current = initial
        while current not in orbit:
            orbit.append(current)
            current = frobenius_basis_image(current, prime, x_bound, y_bound)
        check(current == frozenset({(0, 0)}),
              "Frobenius image chain did not terminate at the constants")
        data = orbit_data(
            orbit,
            lambda basis: frobenius_basis_image(basis, prime, x_bound, y_bound),
        )
        depth = ceil_log_base(max(x_bound, y_bound), prime)
        check(len(orbit) == depth + 1,
              "Frobenius image chain length failed")
        check(data["fixed"] == data["recurrent"] == 1,
              "Frobenius constants are not the unique fixed image")
        check(data["max_tail"] == depth and data["max_period"] == 1,
              "Frobenius image clock failed")
        check(Counter(tail for tail, _ in data["point_data"].values())
              == Counter({value: 1 for value in range(depth + 1)}),
              "Frobenius temporal chain polynomial failed")
        total_states += len(orbit)
        profiles.append(f"p{prime}r{x_bound}s{y_bound}:T{depth}")
    record(
        "FAI", "embedded_subalgebras_of_truncated_polynomial_algebras",
        "Frobenius-image orbit of F_p[x,y]/(x^r,y^s) in 18 boxes",
        start,
        "sharp ceil(log_p max(r,s)) image-filtration clock",
        "KILL_OWNER_THIN",
        "generic Frobenius image filtration; a one-chain clock has no independent inverse theorem",
        boxes=len(boxes), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# BCH: dual-containing hull-sum retraction on binary linear codes


def span_binary(rows):
    values = {0}
    for row in rows:
        values |= {value ^ row for value in tuple(values)}
    return frozenset(values)


def all_binary_subspaces(dimension):
    spaces = set()
    columns = tuple(range(dimension))
    for rank in range(dimension + 1):
        for pivots in combinations(columns, rank):
            free_positions = []
            pivot_set = set(pivots)
            for row, pivot in enumerate(pivots):
                for column in columns:
                    if column not in pivot_set and column > pivot:
                        free_positions.append((row, column))
            for mask in range(1 << len(free_positions)):
                rows = [1 << pivot for pivot in pivots]
                for bit, (row, column) in enumerate(free_positions):
                    if mask >> bit & 1:
                        rows[row] |= 1 << column
                spaces.add(span_binary(rows))
    return tuple(sorted(spaces, key=lambda space: (len(space), tuple(sorted(space)))))


def gaussian_binomial_two(n, k):
    numerator = 1
    denominator = 1
    for index in range(k):
        numerator *= (1 << (n - index)) - 1
        denominator *= (1 << (k - index)) - 1
    return numerator // denominator


def binary_perp(code, dimension):
    return frozenset(
        value for value in range(1 << dimension)
        if all(((value & word).bit_count() & 1) == 0 for word in code)
    )


def run_bch():
    start = ASSERTIONS
    total_states = 0
    profiles = []
    for dimension in range(1, 6):
        spaces = all_binary_subspaces(dimension)
        expected_count = sum(gaussian_binomial_two(dimension, rank)
                             for rank in range(dimension + 1))
        check(len(spaces) == expected_count,
              "binary RREF subspace enumeration failed")
        carrier = set(spaces)

        def step(code):
            dual = binary_perp(code, dimension)
            image = frozenset(left ^ right for left in code for right in dual)
            check(len(code) * len(dual) >= len(image),
                  "code sum cardinality sanity check failed")
            return image

        data = orbit_data(spaces, step)
        for code in spaces:
            image = data["nxt"][code]
            check(code <= image, "hull-sum map is not extensive")
            check(data["nxt"][image] == image,
                  "hull-sum map is not idempotent")
            check(image in carrier, "hull-sum image is not a binary code")
        check(data["max_tail"] <= 1 and data["max_period"] == 1,
              "hull-sum retraction acquired temporal depth")
        total_states += len(spaces)
        profiles.append(
            f"n{dimension}:S{len(spaces)}:I{len(data['fibres'])}:"
            f"F{data['fixed']}:MF{max(data['fibres'].values())}"
        )
    record(
        "BCH", "binary_linear_codes",
        "all subspaces of F_2^n for 1<=n<=5; C->C+C^perp",
        start,
        "dual-containing idempotent image and exact bounded fibre profiles",
        "KILL_STATIC_RETRACTION",
        "orthogonal hull identity makes the update a one-step retraction, barred by the historical firewall",
        boxes=5, states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# QCI: conjugation on primitive reduced positive binary quadratic forms


def primitive_reduced_forms(discriminant):
    bound = isqrt(abs(discriminant) // 3) + 2
    forms = []
    for a in range(1, bound + 1):
        for b in range(-a, a + 1):
            numerator = b * b - discriminant
            if numerator % (4 * a):
                continue
            c = numerator // (4 * a)
            if a <= c and gcd(gcd(a, abs(b)), c) == 1:
                forms.append((a, b, c))
    return tuple(sorted(set(forms)))


def run_qci():
    start = ASSERTIONS
    discriminants = tuple(
        value for value in range(-3, -201, -1)
        if value % 4 in (0, 1)
    )
    total_states = 0
    total_fixed = 0
    profiles = []
    used = 0
    for discriminant in discriminants:
        forms = primitive_reduced_forms(discriminant)
        if not forms:
            continue
        used += 1
        carrier = set(forms)

        def step(form):
            a, b, c = form
            return (a, -b, c)

        data = orbit_data(forms, step)
        check(data["max_tail"] == 0 and data["max_period"] <= 2,
              "quadratic-form conjugation is not an involution")
        fixed = sum(b == 0 for _, b, _ in forms)
        check(data["fixed"] == fixed,
              "quadratic-form ambiguous representative census failed")
        for form in forms:
            check(step(step(form)) == form and step(form) in carrier,
                  "reduced-form conjugation left the carrier")
            a, b, c = form
            check(b * b - 4 * a * c == discriminant,
                  "quadratic form discriminant changed")
        total_states += len(forms)
        total_fixed += fixed
        if discriminant in (-3, -4, -15, -20, -84, -120, -195):
            profiles.append(
                f"D{discriminant}:S{len(forms)}:F{fixed}:C2{(len(forms)-fixed)//2}"
            )
    record(
        "QCI", "primitive_reduced_binary_quadratic_forms",
        "all nonempty primitive reduced-form boxes for -200<=D<=-3; (a,b,c)->(a,-b,c)",
        start,
        "complete fixed/two-cycle census on the symmetric reduced-form carrier",
        "KILL_DIRECT_INVOLUTION",
        "class inversion/conjugation is the defining classical symmetry and supplies no transient theorem",
        boxes=used, states=total_states, fixed=total_fixed,
        profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# LPS: right-parastrophe dynamics on labelled Latin squares


def latin_squares(order):
    row_permutations = tuple(permutations(range(order)))
    squares = []

    def extend(rows, column_masks):
        if len(rows) == order:
            squares.append(tuple(rows))
            return
        for row in row_permutations:
            if all((column_masks[column] >> value) & 1 == 0
                   for column, value in enumerate(row)):
                new_masks = list(column_masks)
                for column, value in enumerate(row):
                    new_masks[column] |= 1 << value
                extend(rows + [row], tuple(new_masks))

    extend([], (0,) * order)
    return tuple(squares)


def right_parastrophe(square):
    order = len(square)
    output = [[0] * order for _ in range(order)]
    for left in range(order):
        for right in range(order):
            product_value = square[left][right]
            output[left][product_value] = right
    return tuple(tuple(row) for row in output)


def run_lps():
    start = ASSERTIONS
    total_states = 0
    profiles = []
    expected_totals = {2: 2, 3: 12, 4: 576}
    for order in (2, 3, 4):
        squares = latin_squares(order)
        check(len(squares) == expected_totals[order],
              "labelled Latin-square enumeration failed")
        carrier = set(squares)
        data = orbit_data(squares, right_parastrophe)
        check(data["max_tail"] == 0 and data["max_period"] <= 2,
              "right parastrophe is not an involution")
        for square in squares:
            image = right_parastrophe(square)
            check(image in carrier, "parastrophe is not Latin")
            check(right_parastrophe(image) == square,
                  "right parastrophe failed to invert itself")
        total_states += len(squares)
        profiles.append(
            f"n{order}:S{len(squares)}:F{data['fixed']}:"
            f"C2{(len(squares)-data['fixed'])//2}"
        )
    record(
        "LPS", "labelled_latin_squares",
        "all labelled Latin squares of orders 2,3,4; swap right input with output",
        start,
        "exact fixed/two-cycle census in the bounded boxes",
        "KILL_DIRECT_PARASTROPHE",
        "quasigroup parastrophy is a coordinate permutation and the involution is definition-level",
        boxes=3, states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# RCC: reciprocal-complement dynamics on primitive cyclotomic divisors


def cyclotomic_cosets(units, multiplier, modulus):
    unseen = set(units)
    cosets = []
    while unseen:
        start = min(unseen)
        orbit = []
        current = start
        while current not in orbit:
            orbit.append(current)
            current = current * multiplier % modulus
        coset = frozenset(orbit)
        check(coset <= set(units), "multiplier left the primitive residue carrier")
        unseen -= coset
        cosets.append(coset)
    return tuple(sorted(cosets, key=lambda coset: min(coset)))


def run_rcc():
    start = ASSERTIONS
    raw_boxes = (
        (2, 5), (2, 7), (2, 9), (2, 15), (2, 21), (2, 31),
        (3, 5), (3, 7), (3, 8), (3, 10), (5, 7), (5, 12), (7, 15),
    )
    total_states = 0
    profiles = []
    for field_size, modulus in raw_boxes:
        check(gcd(field_size, modulus) == 1,
              "cyclotomic box has bad characteristic")
        units = tuple(value for value in range(1, modulus) if gcd(value, modulus) == 1)
        cosets = cyclotomic_cosets(units, field_size, modulus)
        check(len(cosets) <= 16, "cyclotomic test box is too large for exhaustive masks")
        index = {residue: coset_index
                 for coset_index, coset in enumerate(cosets)
                 for residue in coset}
        negation = []
        for coset in cosets:
            targets = {index[(-residue) % modulus] for residue in coset}
            check(len(targets) == 1,
                  "reciprocal does not descend to a cyclotomic-factor permutation")
            negation.append(next(iter(targets)))
        check(all(negation[negation[i]] == i for i in range(len(cosets))),
              "reciprocal factor permutation is not involutive")
        full = (1 << len(cosets)) - 1

        def reciprocal_mask(mask):
            output = 0
            for source, target in enumerate(negation):
                if mask >> source & 1:
                    output |= 1 << target
            return output

        def step(mask):
            return full ^ reciprocal_mask(mask)

        data = orbit_data(range(full + 1), step)
        fixed_cosets = sum(target == source for source, target in enumerate(negation))
        fixed_subsets = 0 if fixed_cosets else 1 << (len(cosets) // 2)
        check(data["fixed"] == fixed_subsets,
              "reciprocal-complement fixed-divisor census failed")
        check(data["max_tail"] == 0 and data["max_period"] <= 2,
              "reciprocal-complement map is not an involution")
        for mask in range(full + 1):
            check(step(step(mask)) == mask,
                  "reciprocal complement failed to square to identity")
        total_states += full + 1
        profiles.append(
            f"q{field_size}N{modulus}:C{len(cosets)}:SC{fixed_cosets}:"
            f"F{fixed_subsets}"
        )
    record(
        "RCC", "squarefree_divisors_of_finite_field_cyclotomic_polynomials",
        "divisors of Phi_N over F_q in 13 coprime boxes; f->Phi_N/f^* on factor supports",
        start,
        "fixed-point dichotomy from self-reciprocal factors and complete two-cycle census",
        "KILL_DIRECT_DUALITY",
        "reciprocal plus complement is an explicit Boolean involution, not a temporal advance",
        boxes=len(raw_boxes), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# CHE: the Chebyshev quadratic on prime fields


def primes_through(limit):
    primes = []
    for value in range(2, limit + 1):
        if all(value % prime for prime in primes if prime * prime <= value):
            primes.append(value)
    return tuple(primes)


def run_che():
    start = ASSERTIONS
    primes = tuple(prime for prime in primes_through(199) if prime % 2)
    total_states = 0
    profiles = []
    for prime in primes:
        def step(value):
            return (value * value - 2) % prime

        data = orbit_data(range(prime), step)
        for unit in range(1, prime):
            inverse = pow(unit, -1, prime)
            trace = (unit + inverse) % prime
            target = (unit * unit + pow(unit * unit, -1, prime)) % prime
            check(step(trace) == target,
                  "Chebyshev multiplicative trace semiconjugacy failed")
        total_states += prime
        if prime in (3, 5, 7, 11, 17, 31, 61, 127, 199):
            profiles.append(
                f"p{prime}:F{data['fixed']}:R{data['recurrent']}:"
                f"T{data['max_tail']}:P{data['max_period']}"
            )
    record(
        "CHE", "prime_finite_fields",
        "F_p for every odd prime p<=199; x->x^2-2",
        start,
        "exact bounded functional graphs and multiplicative-trace semiconjugacy controls",
        "KILL_DIRECT_OWNER",
        "Chebyshev finite-field dynamics and the powering semiconjugacy are mature direct-owner territory",
        boxes=len(primes), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# NSB: adjoin the Frobenius number of a numerical semigroup


def is_numerical_semigroup_mask(mask, bound):
    nongaps = [value for value in range(1, bound + 1)
               if not (mask >> (value - 1) & 1)]
    for left in nongaps:
        for right in nongaps:
            if left + right <= bound and mask >> (left + right - 1) & 1:
                return False
    return True


def largest_gap(mask):
    return mask.bit_length()


def run_nsb():
    start = ASSERTIONS
    total_states = 0
    profiles = []
    for bound in (8, 10, 12, 14, 16):
        states = tuple(mask for mask in range(1 << bound)
                       if is_numerical_semigroup_mask(mask, bound))
        carrier = set(states)

        def step(mask):
            if mask == 0:
                return 0
            return mask & ~(1 << (mask.bit_length() - 1))

        data = orbit_data(states, step)
        check(data["fixed"] == data["recurrent"] == 1,
              "Frobenius adjunction should terminate only at N")
        check(data["max_period"] == 1 and data["max_tail"] == bound,
              "numerical-semigroup genus clock failed")
        for mask in states:
            tail, _ = data["point_data"][mask]
            check(tail == mask.bit_count(),
                  "Frobenius-adjunction depth is not genus")
            target = step(mask)
            check(target in carrier, "adjoining Frobenius broke semigroup closure")
        deepest = [mask for mask in states
                   if data["point_data"][mask][0] == bound]
        check(deepest == [(1 << bound) - 1],
              "ordinary semigroup is not the unique deepest witness")
        for target in states:
            frobenius = largest_gap(target)
            predicted_sources = []
            if target == 0:
                predicted_sources.append(0)
            for gap in range(frobenius + 1, bound + 1):
                source = target | (1 << (gap - 1))
                if source in carrier:
                    predicted_sources.append(source)
                    check(step(source) == target,
                          "effective-generator inverse failed")
            check(data["fibres"].get(target, 0) == len(predicted_sources),
                  "numerical-semigroup every-target fibre failed")
        genus_hist = Counter(mask.bit_count() for mask in states)
        check(genus_hist[bound] == 1,
              "maximal genus coefficient failed")
        total_states += len(states)
        profiles.append(
            f"B{bound}:S{len(states)}:I{len(data['fibres'])}:"
            f"MF{max(data['fibres'].values())}:G{compact(dict(sorted(genus_hist.items())))}"
        )
    record(
        "NSB", "bounded_numerical_semigroups",
        "all numerical semigroups with gaps in [1,B], B=8,10,12,14,16; adjoin Frobenius number",
        start,
        "pointwise genus clock, unique sharp ordinary semigroup, exact effective-generator inverse fibres",
        "KILL_DIRECT_OWNER",
        "this is the standard numerical-semigroup tree orientation; the attractive theorem is definition-level owner material",
        boxes=5, states=total_states, profiles=";".join(profiles),
    )


def main():
    run_vgt()
    run_dnt()
    run_pcr()
    run_fai()
    run_bch()
    run_qci()
    run_lps()
    run_rcc()
    run_che()
    run_nsb()

    per_system_assertions = sum(result["assertions"] for result in RESULTS)
    global_start = ASSERTIONS
    check(len(RESULTS) == 10, "literal-system breadth count changed")
    check(len({result["id"] for result in RESULTS}) == len(RESULTS),
          "duplicate scout handle")
    global_assertions = ASSERTIONS - global_start

    print("P142-P146 ALGEBRAIC/ARITHMETIC SCOUT CANONICAL v1")
    print("external_status=HOLD_EXTERNAL")
    print("arithmetic=EXACT_INTEGER_AND_FINITE_FIELD")
    print("counting=one_boolean_equality_or_membership_check_per_assertion")
    for result in RESULTS:
        metrics = " ".join(
            f"{key}={compact(value)}" for key, value in result["metrics"].items()
        )
        print(
            f"SYSTEM id={result['id']} carrier={result['carrier']} "
            f"assertions={result['assertions']} scope={compact(result['scope'])} "
            f"signal={compact(result['signal'])} decision={result['decision']} "
            f"reason={compact(result['reason'])} {metrics}"
        )
    print(f"literal_systems={len(RESULTS)}")
    print(f"per_system_assertions={per_system_assertions}")
    print(f"global_assertions={global_assertions}")
    print(f"assertions={ASSERTIONS}")
    print("enumeration_is_proof=false")
    print("bounded_owner_nonhit_is_novelty=false")
    print("PASS")


if __name__ == "__main__":
    main()
