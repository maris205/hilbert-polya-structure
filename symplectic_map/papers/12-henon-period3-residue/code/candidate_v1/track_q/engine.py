"""Track Q: private quotient-algebra and pre-collapse exact arithmetic.

This module deliberately has no imports and no filesystem, environment,
serialization, subprocess, or network capability.  Its arithmetic and data
structures are private to Track Q.
"""


def _q_factorial(n):
    if type(n) is not int or n < 0:
        raise ValueError("Q factorial domain")
    value = 1
    cursor = 2
    while cursor <= n:
        value *= cursor
        cursor += 1
    return value


def _q_choose(n, k):
    if type(n) is not int or type(k) is not int:
        raise TypeError("Q choose requires exact integers")
    if n < 0 or k < 0 or k > n:
        return 0
    k = min(k, n - k)
    value = 1
    cursor = 1
    while cursor <= k:
        value = value * (n - k + cursor) // cursor
        cursor += 1
    return value


def _q_multinomial(total, parts):
    if type(total) is not int or type(parts) is not tuple:
        raise TypeError("Q multinomial types")
    if any(type(item) is not int or item < 0 for item in parts):
        return 0
    if sum(parts) != total:
        return 0
    remaining = total
    value = 1
    for item in parts:
        value *= _q_choose(remaining, item)
        remaining -= item
    return value


def _q_compositions(total, width):
    if type(total) is not int or type(width) is not int or total < 0 or width < 1:
        raise ValueError("Q composition domain")
    if width == 1:
        yield (total,)
        return
    head = 0
    while head <= total:
        for tail in _q_compositions(total - head, width - 1):
            yield (head,) + tail
        head += 1


def _q_poly_add(left, right):
    result = dict(left)
    for monomial, coefficient in right.items():
        updated = result.get(monomial, 0) + coefficient
        if updated:
            result[monomial] = updated
        elif monomial in result:
            del result[monomial]
    return result


def _q_poly_scale(poly, scalar):
    if scalar == 0:
        return {}
    return {monomial: scalar * coefficient for monomial, coefficient in poly.items()}


def _q_poly_multiply(left, right):
    result = {}
    for (l1, a1, b1, c1), coefficient_left in left.items():
        for (l2, a2, b2, c2), coefficient_right in right.items():
            monomial = (l1 + l2, a1 + a2, b1 + b2, c1 + c2)
            result[monomial] = result.get(monomial, 0) + coefficient_left * coefficient_right
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def _q_poly_power(poly, exponent):
    if type(exponent) is not int or exponent < 0:
        raise ValueError("Q polynomial exponent")
    result = {(0, 0, 0, 0): 1}
    base = dict(poly)
    power = exponent
    while power:
        if power & 1:
            result = _q_poly_multiply(result, base)
        power //= 2
        if power:
            base = _q_poly_multiply(base, base)
    return result


def _q_reduce_quartic_monomial(monomial, memo):
    if monomial in memo:
        return memo[monomial]
    l_power, e0, e1, e2 = monomial
    exponents = [e0, e1, e2]
    selected = None
    for index in (0, 1, 2):
        if exponents[index] >= 4:
            selected = index
            break
    if selected is None:
        result = {monomial: 1}
        memo[monomial] = result
        return result
    reduced = list(exponents)
    reduced[selected] -= 4
    branch_terms = []
    first = list(reduced)
    first[selected] += 2
    branch_terms.append((2, (l_power + 1, first[0], first[1], first[2])))
    branch_terms.append((-1, (l_power + 2, reduced[0], reduced[1], reduced[2])))
    previous = (selected - 1) % 3
    prior = list(reduced)
    prior[previous] += 1
    branch_terms.append((-1, (l_power, prior[0], prior[1], prior[2])))
    following = (selected + 1) % 3
    after = list(reduced)
    after[following] += 1
    branch_terms.append((1, (l_power, after[0], after[1], after[2])))
    result = {}
    for scalar, child in branch_terms:
        result = _q_poly_add(result, _q_poly_scale(_q_reduce_quartic_monomial(child, memo), scalar))
    memo[monomial] = result
    return result


def _q_reduce_quartic(poly):
    memo = {}
    result = {}
    for monomial, coefficient in poly.items():
        reduced = _q_reduce_quartic_monomial(monomial, memo)
        result = _q_poly_add(result, _q_poly_scale(reduced, coefficient))
    return result


def _q_quartic_trace_polynomial():
    generators = []
    for index in (0, 1, 2):
        high = [0, 0, 0]
        high[index] = 3
        low = [0, 0, 0]
        low[index] = 1
        generators.append({(0, high[0], high[1], high[2]): 1,
                           (1, low[0], low[1], low[2]): -1})
    product = _q_poly_multiply(_q_poly_multiply(generators[0], generators[1]), generators[2])
    trace_element = _q_poly_scale(product, 64)
    for generator in generators:
        trace_element = _q_poly_add(trace_element, _q_poly_scale(generator, 4))
    square = _q_poly_multiply(trace_element, trace_element)
    diagonal_trace = {}
    for e0 in range(4):
        for e1 in range(4):
            for e2 in range(4):
                basis_monomial = {(0, e0, e1, e2): 1}
                image = _q_reduce_quartic(_q_poly_multiply(square, basis_monomial))
                for (l_power, a0, a1, a2), coefficient in image.items():
                    if (a0, a1, a2) == (e0, e1, e2):
                        diagonal_trace[l_power] = diagonal_trace.get(l_power, 0) + coefficient
    return {power: coefficient for power, coefficient in diagonal_trace.items() if coefficient}


def _q_truncated_add(left, right, degree):
    result = list(left) + [0] * (degree + 1 - len(left))
    cursor = 0
    while cursor < len(right) and cursor <= degree:
        result[cursor] += right[cursor]
        cursor += 1
    return result[:degree + 1]


def _q_truncated_scale(poly, scalar, degree):
    result = [0] * (degree + 1)
    cursor = 0
    while cursor < len(poly) and cursor <= degree:
        result[cursor] = scalar * poly[cursor]
        cursor += 1
    return result


def _q_truncated_multiply(left, right, degree):
    result = [0] * (degree + 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            if i + j <= degree:
                result[i + j] += left_value * right_value
    return result


def _q_truncated_power(poly, exponent, degree):
    result = [1] + [0] * degree
    cursor = 0
    while cursor < exponent:
        result = _q_truncated_multiply(result, poly, degree)
        cursor += 1
    return result


def _q_local_fixed_series(root_multiplicity):
    if root_multiplicity not in (2, 4):
        raise ValueError("quartic fixed multiplicity")
    degree = 2 * root_multiplicity - 2
    delta = [0, 1] + [0] * (degree - 1)
    u = [0] * (degree + 1)
    v = [0] * (degree + 1)
    for _ in range(4):
        delta_plus_v = _q_truncated_add(delta, v, degree)
        u = _q_truncated_scale(
            _q_truncated_power(delta_plus_v, root_multiplicity, degree), -1, degree
        )
        delta_plus_u = _q_truncated_add(delta, u, degree)
        v = _q_truncated_power(delta_plus_u, root_multiplicity, degree)
    p_delta = _q_truncated_power(delta, root_multiplicity, degree)
    remaining = _q_truncated_add(_q_truncated_add(p_delta, v, degree),
                                 _q_truncated_scale(u, -1, degree), degree)
    nonzero = [index for index, coefficient in enumerate(remaining) if coefficient]
    return {
        "root_multiplicity": root_multiplicity,
        "truncation_degree": degree,
        "remaining_order": nonzero[0] if nonzero else None,
        "remaining_leading_coefficient": remaining[nonzero[0]] if nonzero else None,
        "u_terms": [{"exponent": index, "coefficient": coefficient}
                    for index, coefficient in enumerate(u) if coefficient],
        "v_terms": [{"exponent": index, "coefficient": coefficient}
                    for index, coefficient in enumerate(v) if coefficient],
    }


def _q_symbolic_add(left, right):
    result = dict(left)
    for key, coefficient in right.items():
        updated = result.get(key, 0) + coefficient
        if updated:
            result[key] = updated
        elif key in result:
            del result[key]
    return result


def _q_symbolic_multiply(left, right):
    result = {}
    for (s_left, t_left), c_left in left.items():
        for (s_right, t_right), c_right in right.items():
            key = (s_left + s_right, t_left + t_right)
            result[key] = result.get(key, 0) + c_left * c_right
    return {key: coefficient for key, coefficient in result.items() if coefficient}


def _q_bcd_add(left, right):
    result = dict(left)
    for key, coefficient in right.items():
        updated = result.get(key, 0) + coefficient
        if updated:
            result[key] = updated
        elif key in result:
            del result[key]
    return result


def _q_bcd_multiply(left, right):
    result = {}
    for left_power, left_coefficient in left.items():
        for right_power, right_coefficient in right.items():
            key = tuple(left_power[index] + right_power[index] for index in (0, 1, 2))
            result[key] = result.get(key, 0) + left_coefficient * right_coefficient
    return {key: coefficient for key, coefficient in result.items() if coefficient}


def _q_bcd_scale(poly, scalar):
    return {key: scalar * coefficient for key, coefficient in poly.items() if scalar * coefficient}


def _q_general_trace_elimination():
    zero = {}
    one = {(0, 0, 0): 1}
    b_symbol = {(1, 0, 0): 1}
    c_symbol = {(0, 1, 0): 1}
    d_symbol = {(0, 0, 1): 1}
    general_quartic = [d_symbol, c_symbol, b_symbol, zero, one]
    derivative = []
    degree = 1
    while degree < len(general_quartic):
        derivative.append(_q_bcd_scale(general_quartic[degree], degree))
        degree += 1
    square = [{} for _ in range(2 * len(derivative) - 1)]
    for left_degree, left in enumerate(derivative):
        for right_degree, right in enumerate(derivative):
            square[left_degree + right_degree] = _q_bcd_add(
                square[left_degree + right_degree], _q_bcd_multiply(left, right)
            )
    remainder = list(square)
    while len(remainder) > 4:
        top_degree = len(remainder) - 1
        top = remainder.pop()
        if not top:
            continue
        shift = top_degree - 4
        replacements = (
            (shift + 2, b_symbol),
            (shift + 1, c_symbol),
            (shift, d_symbol),
        )
        for target_degree, parameter in replacements:
            remainder[target_degree] = _q_bcd_add(
                remainder[target_degree],
                _q_bcd_scale(_q_bcd_multiply(top, parameter), -1),
            )
    expected = [
        {(0, 2, 0): 1},
        {(1, 1, 0): 4},
        {(2, 0, 0): 4, (0, 0, 1): -16},
        {(0, 1, 0): -8},
    ]
    if remainder != expected:
        raise ArithmeticError("Q general-quartic derivative-square remainder")
    return {
        "general_centered_coefficients": ["d", "c", "b", "0", "1"],
        "derivative_square_remainder": [
            [
                {
                    "b_exponent": powers[0],
                    "c_exponent": powers[1],
                    "d_exponent": powers[2],
                    "coefficient": coefficient,
                }
                for powers, coefficient in sorted(poly.items())
            ]
            for poly in remainder
        ],
        "first_eliminated_variable": "c",
        "first_pivot_coefficient": -8,
        "remaining_relation_terms": [
            {"b_exponent": 2, "d_exponent": 0, "coefficient": 4},
            {"b_exponent": 0, "d_exponent": 1, "coefficient": -16},
        ],
        "classification_condition": "p_divides_derivative_squared",
    }


def _q_centered_square_elimination():
    one = {(0, 0): 1}
    s_symbol = {(1, 0): 1}
    t_symbol = {(0, 1): 1}
    quadratic = [t_symbol, s_symbol, one]
    square = [{} for _ in range(5)]
    for left_degree, left in enumerate(quadratic):
        for right_degree, right in enumerate(quadratic):
            square[left_degree + right_degree] = _q_symbolic_add(
                square[left_degree + right_degree], _q_symbolic_multiply(left, right)
            )
    centered = []
    for coefficient in square:
        centered.append({t_power: value for (s_power, t_power), value in coefficient.items() if s_power == 0})
    b_squared = {}
    for left_power, left_value in centered[2].items():
        for right_power, right_value in centered[2].items():
            power = left_power + right_power
            b_squared[power] = b_squared.get(power, 0) + left_value * right_value
    relation = dict(b_squared)
    for power, value in centered[0].items():
        relation[power] = relation.get(power, 0) - 4 * value
    relation = {power: value for power, value in relation.items() if value}
    if square[3] != {(1, 0): 2} or centered[1] or relation:
        raise ArithmeticError("Q centered-square coefficient elimination failed")
    return {
        "quadratic_square_coefficients": [
            [
                {"s_exponent": s_power, "t_exponent": t_power, "coefficient": coefficient}
                for (s_power, t_power), coefficient in sorted(poly.items())
            ]
            for poly in square
        ],
        "centered_constraint_coefficient": 2,
        "centered_solution_s": 0,
        "centered_b_terms": [{"t_exponent": power, "coefficient": value}
                             for power, value in sorted(centered[2].items())],
        "centered_c_terms": [],
        "centered_d_terms": [{"t_exponent": power, "coefficient": value}
                             for power, value in sorted(centered[0].items())],
        "eliminated_relation_remainder": [],
        "parameter_change": "t=-L",
    }


def _q_bareiss_determinant(matrix):
    size = len(matrix)
    if size == 0 or any(type(row) is not list or len(row) != size for row in matrix):
        raise ValueError("Q determinant square matrix")
    work = [list(row) for row in matrix]
    sign = 1
    divisor = 1
    pivot_index = 0
    while pivot_index < size - 1:
        pivot_row = pivot_index
        while pivot_row < size and work[pivot_row][pivot_index] == 0:
            pivot_row += 1
        if pivot_row == size:
            return 0
        if pivot_row != pivot_index:
            work[pivot_index], work[pivot_row] = work[pivot_row], work[pivot_index]
            sign = -sign
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                )
                if numerator % divisor:
                    raise ArithmeticError("Q Bareiss exact division")
                work[row][column] = numerator // divisor
        for row in range(pivot_index + 1, size):
            work[row][pivot_index] = 0
        divisor = pivot
        pivot_index += 1
    return sign * work[-1][-1]


def _q_resultant(left_high_to_low, right_high_to_low):
    left_degree = len(left_high_to_low) - 1
    right_degree = len(right_high_to_low) - 1
    size = left_degree + right_degree
    matrix = [[0] * size for _ in range(size)]
    for row in range(right_degree):
        for offset, coefficient in enumerate(left_high_to_low):
            matrix[row][row + offset] = coefficient
    for local_row in range(left_degree):
        row = right_degree + local_row
        for offset, coefficient in enumerate(right_high_to_low):
            matrix[row][local_row + offset] = coefficient
    return _q_bareiss_determinant(matrix)


def _q_l_add(left, right):
    result = dict(left)
    for power, coefficient in right.items():
        updated = result.get(power, 0) + coefficient
        if updated:
            result[power] = updated
        elif power in result:
            del result[power]
    return result


def _q_l_multiply(left, right):
    result = {}
    for p_left, c_left in left.items():
        for p_right, c_right in right.items():
            power = p_left + p_right
            result[power] = result.get(power, 0) + c_left * c_right
    return {power: coefficient for power, coefficient in result.items() if coefficient}


def _q_fixed_reduce_monomial(l_power, x_power, memo):
    key = (l_power, x_power)
    if key in memo:
        return memo[key]
    if x_power < 4:
        result = {key: 1}
        memo[key] = result
        return result
    result = {}
    branches = (
        (2, l_power + 1, x_power - 2),
        (-1, l_power + 2, x_power - 4),
    )
    for scalar, child_l, child_x in branches:
        child = _q_fixed_reduce_monomial(child_l, child_x, memo)
        for child_key, coefficient in child.items():
            result[child_key] = result.get(child_key, 0) + scalar * coefficient
    result = {child_key: coefficient for child_key, coefficient in result.items() if coefficient}
    memo[key] = result
    return result


def _q_fixed_reduce(poly):
    result = {}
    memo = {}
    for (l_power, x_power), coefficient in poly.items():
        for key, reduced_coefficient in _q_fixed_reduce_monomial(l_power, x_power, memo).items():
            result[key] = result.get(key, 0) + coefficient * reduced_coefficient
    return {key: coefficient for key, coefficient in result.items() if coefficient}


def _q_fixed_product(left, right):
    raw = {}
    for (l_left, x_left), c_left in left.items():
        for (l_right, x_right), c_right in right.items():
            key = (l_left + l_right, x_left + x_right)
            raw[key] = raw.get(key, 0) + c_left * c_right
    return _q_fixed_reduce(raw)


def _q_matrix_product(left, right):
    size = len(left)
    result = [[{} for _ in range(size)] for _ in range(size)]
    for row in range(size):
        for column in range(size):
            value = {}
            for middle in range(size):
                value = _q_l_add(value, _q_l_multiply(left[row][middle], right[middle][column]))
            result[row][column] = value
    return result


def _q_permutations(values):
    if not values:
        yield ()
        return
    for index, value in enumerate(values):
        remainder = values[:index] + values[index + 1:]
        for tail in _q_permutations(remainder):
            yield (value,) + tail


def _q_tl_add(left, right):
    result = dict(left)
    for key, coefficient in right.items():
        updated = result.get(key, 0) + coefficient
        if updated:
            result[key] = updated
        elif key in result:
            del result[key]
    return result


def _q_tl_multiply(left, right):
    result = {}
    for (t_left, l_left), c_left in left.items():
        for (t_right, l_right), c_right in right.items():
            key = (t_left + t_right, l_left + l_right)
            result[key] = result.get(key, 0) + c_left * c_right
    return {key: coefficient for key, coefficient in result.items() if coefficient}


def _q_characteristic_polynomial(matrix):
    size = len(matrix)
    entries = [[{} for _ in range(size)] for _ in range(size)]
    for row in range(size):
        for column in range(size):
            entry = {(0, l_power): -coefficient for l_power, coefficient in matrix[row][column].items()}
            if row == column:
                entry = _q_tl_add(entry, {(1, 0): 1})
            entries[row][column] = entry
    determinant = {}
    for permutation in _q_permutations(tuple(range(size))):
        inversions = sum(
            1 for left in range(size) for right in range(left + 1, size)
            if permutation[left] > permutation[right]
        )
        term = {(0, 0): -1 if inversions % 2 else 1}
        for row in range(size):
            term = _q_tl_multiply(term, entries[row][permutation[row]])
        determinant = _q_tl_add(determinant, term)
    return determinant


def _q_low_period_and_fixed_moment():
    q_poly = {(0, 3): 4, (1, 1): -4}
    basis = tuple(range(4))
    matrix = [[{} for _ in basis] for _ in basis]
    for column, basis_power in enumerate(basis):
        image = _q_fixed_product(q_poly, {(0, basis_power): 1})
        for (l_power, x_power), coefficient in image.items():
            matrix[x_power][column] = _q_l_add(matrix[x_power][column], {l_power: coefficient})
    matrix_square = _q_matrix_product(matrix, matrix)
    square_nonzero_entries = sum(1 for row in matrix_square for entry in row if entry)
    characteristic = _q_characteristic_polynomial(matrix)
    q_square = _q_fixed_product(q_poly, q_poly)
    q_cube = _q_fixed_product(q_square, q_poly)
    fixed_trace = _q_symbolic_fixed_sum(q_cube, _q_fixed_scale(q_poly, 3))
    fixed_trace_square = _q_fixed_product(fixed_trace, fixed_trace)
    if square_nonzero_entries or characteristic != {(4, 0): 1} or q_square or fixed_trace_square:
        raise ArithmeticError("Q low-period fixed algebra computation failed")
    ambient_period_two_length = len(basis) * len(basis)
    return {
        "fixed_basis_count": len(basis),
        "multiplication_matrix": [
            [
                [{"L_exponent": power, "coefficient": value} for power, value in sorted(entry.items())]
                for entry in row
            ]
            for row in matrix
        ],
        "multiplication_matrix_square_nonzero_entry_count": square_nonzero_entries,
        "fixed_characteristic_terms": [
            {"T_exponent": t_power, "L_exponent": l_power, "coefficient": coefficient}
            for (t_power, l_power), coefficient in sorted(characteristic.items())
        ],
        "period_two_ambient_basis_count": ambient_period_two_length,
        "period_two_exact_basis_count": ambient_period_two_length - len(basis),
        "period_two_nilpotent_correction_square_nonzero_term_count": len(q_square) ** 2,
        "fixed_trace_square_remainder": [
            {"L_exponent": l_power, "x_exponent": x_power, "coefficient": coefficient}
            for (l_power, x_power), coefficient in sorted(fixed_trace_square.items())
        ],
    }


def _q_fixed_scale(poly, scalar):
    return {key: scalar * coefficient for key, coefficient in poly.items() if scalar * coefficient}


def _q_symbolic_fixed_sum(left, right):
    result = dict(left)
    for key, coefficient in right.items():
        result[key] = result.get(key, 0) + coefficient
        if result[key] == 0:
            del result[key]
    return result


def _q_conjugacy_witness():
    scale_order = 3
    parameter_weight = -2
    invariant_power = 1
    while (parameter_weight * invariant_power) % scale_order:
        invariant_power += 1
    centered_translation_coefficient = 4
    if invariant_power != 3 or centered_translation_coefficient == 0:
        raise ArithmeticError("Q conjugacy coefficient comparison")
    return {
        "centered_translation_coefficient": centered_translation_coefficient,
        "translation_solution": 0,
        "monic_scale_order": scale_order,
        "parameter_scale_weight": parameter_weight,
        "minimal_invariant_power": invariant_power,
        "explicit_sufficiency_exponent": 1,
    }


def quartic_quotient_witness():
    trace_polynomial = _q_quartic_trace_polynomial()
    fixed_series = [_q_local_fixed_series(2), _q_local_fixed_series(4)]
    if any(record["remaining_order"] != record["root_multiplicity"] or
           record["remaining_leading_coefficient"] != 3 for record in fixed_series):
        raise ArithmeticError("Q local multiplicity witness failed")
    general_elimination = _q_general_trace_elimination()
    fiber = _q_centered_square_elimination()
    negative_resultant = _q_resultant([1, 0, 0, -1, 0], [4, 0, 0, -1])
    square_resultant = _q_resultant([1, 0, -2, 0, 1], [4, 0, -4, 0])
    low_period = _q_low_period_and_fixed_moment()
    conjugacy = _q_conjugacy_witness()
    if negative_resultant == 0 or square_resultant != 0:
        raise ArithmeticError("Q resultant fiber control failed")
    return {
        "route": "STANDARD_MONOMIAL_MULTIPLICATION_TRACE",
        "standard_basis_bounds": [4, 4, 4],
        "standard_basis_count": 64,
        "monic_relations": [
            "x_i^4=2*L*x_i^2-L^2-x_(i-1)+x_(i+1)"
        ],
        "general_quartic_trace_elimination": general_elimination,
        "fiber_parameter_reconstruction": fiber,
        "subresultant_controls": {
            "simple_root_fixture_resultant": negative_resultant,
            "square_family_specialization_resultant": square_resultant,
        },
        "normalized_affine_comparison": conjugacy,
        "low_period_and_fixed_moment": low_period,
        "local_fixed_series": fixed_series,
        "trace_polynomial": [
            {"exponent": exponent, "coefficient": trace_polynomial[exponent]}
            for exponent in sorted(trace_polynomial)
        ]
    }


def _q_reduction_state(m, exponents, alpha, beta, memo):
    key = (exponents, alpha, beta)
    if key in memo:
        return memo[key]
    if (type(alpha) is not int or type(beta) is not int or alpha < 0 or beta < 0
            or any(type(item) is not int or item < 0 for item in exponents)):
        return 0
    nu = 2 * m - 1
    if sum(exponents) != 3 * nu + m * alpha + nu * beta:
        return 0
    selected = None
    for index in (0, 1, 2):
        if exponents[index] >= 2 * m:
            selected = index
            break
    if selected is None:
        value = int(exponents == (nu, nu, nu) and alpha == 0 and beta == 0)
        memo[key] = value
        return value
    first = list(exponents)
    first[selected] -= m
    second = list(exponents)
    second[selected] -= 2 * m
    previous = list(second)
    previous[(selected - 1) % 3] += 1
    following = list(second)
    following[(selected + 1) % 3] += 1
    value = (
        2 * _q_reduction_state(m, tuple(first), alpha - 1, beta, memo)
        - _q_reduction_state(m, tuple(second), alpha - 2, beta, memo)
        - _q_reduction_state(m, tuple(previous), alpha, beta - 1, memo)
        + _q_reduction_state(m, tuple(following), alpha, beta - 1, memo)
    )
    memo[key] = value
    return value


def _q_recurrence_component(m, j, memo):
    if j == m + 1:
        return 0
    if j < 0 or j > m:
        raise ValueError("Q component index")
    r = m - j
    nu = 2 * m - 1
    total = 0
    for s_values in _q_compositions(j, 3):
        n_values = tuple(r + 1 + item for item in s_values)
        s_weight = _q_multinomial(j, s_values)
        for ell0 in range(n_values[0] + 1):
            for ell1 in range(n_values[1] + 1):
                for ell2 in range(n_values[2] + 1):
                    ell_values = (ell0, ell1, ell2)
                    ell_total = ell0 + ell1 + ell2
                    requested_alpha = nu - ell_total
                    if requested_alpha < 0:
                        continue
                    exponents = tuple(
                        (2 * m - 1) * n_values[index] - m * ell_values[index]
                        for index in (0, 1, 2)
                    )
                    low_weight = (-1 if ell_total % 2 else 1)
                    for index in (0, 1, 2):
                        low_weight *= _q_choose(n_values[index], ell_values[index])
                    total += s_weight * low_weight * _q_reduction_state(
                        m, exponents, requested_alpha, 2 * r, memo
                    )
    return total


def _q_local_decorated_sum(m, n_source, transfer_in, count_negative, count_positive, factor_count):
    numerator = (2 * m - 1) * (factor_count - 1) + transfer_in
    if numerator % m:
        return 0
    target = numerator // m - 2 * n_source
    if target < 0:
        return 0
    total = 0
    ell = 0
    while ell <= factor_count:
        remaining = target - ell
        if remaining >= 0:
            count_square = 0
            while 2 * count_square <= remaining:
                count_linear = remaining - 2 * count_square
                word_total = count_linear + count_square + n_source
                denominator = (
                    _q_factorial(count_linear)
                    * _q_factorial(count_square)
                    * _q_factorial(count_negative)
                    * _q_factorial(count_positive)
                )
                sign_exponent = ell + count_square + count_negative
                sign = -1 if sign_exponent % 2 else 1
                term = (
                    sign
                    * (2 ** count_linear)
                    * _q_choose(factor_count, ell)
                    * _q_factorial(word_total)
                    // denominator
                )
                total += term
                count_square += 1
        ell += 1
    return total


def _q_decorated_tuple_component(m, j):
    if j == m + 1:
        return 0
    if j < 0 or j > m:
        raise ValueError("Q tuple component index")
    r = m - j
    total = 0
    j_zero_pattern_totals = {}
    for s_values in _q_compositions(j, 3):
        factor_counts = tuple(r + 1 + item for item in s_values)
        s_weight = _q_multinomial(j, s_values)
        for transfer_values in _q_compositions(2 * r, 6):
            negative = transfer_values[:3]
            positive = transfer_values[3:]
            source_counts = tuple(negative[index] + positive[index] for index in (0, 1, 2))
            incoming = tuple(
                negative[(index + 1) % 3] + positive[(index - 1) % 3]
                for index in (0, 1, 2)
            )
            if j == 0 and all(value % m == 0 for value in incoming):
                j_zero_pattern_totals.setdefault(incoming, 0)
            local_product = 1
            for index in (0, 1, 2):
                local_product *= _q_local_decorated_sum(
                    m,
                    source_counts[index],
                    incoming[index],
                    negative[index],
                    positive[index],
                    factor_counts[index],
                )
                if local_product == 0:
                    break
            total += s_weight * local_product
            if j == 0 and incoming in j_zero_pattern_totals:
                j_zero_pattern_totals[incoming] += s_weight * local_product
    return total, j_zero_pattern_totals


def _q_registered_coefficient_diagnostic(index):
    if type(index) is not int or index not in (8, 9):
        raise ValueError("Q isolated index allowlist")
    memo = {}
    components = []
    final_integer = 0
    j_zero_patterns = None
    j = 0
    while j <= index + 1:
        recurrence_value = _q_recurrence_component(index, j, memo)
        tuple_value, pattern_totals = _q_decorated_tuple_component(index, j)
        if recurrence_value != tuple_value:
            raise ArithmeticError("Q private routes disagree")
        components.append({
            "component_index": j,
            "recurrence_value": recurrence_value,
            "decorated_tuple_value": tuple_value,
        })
        if j == 0:
            j_zero_patterns = pattern_totals
        final_integer += (
            _q_choose(index + 1, j)
            * ((2 * index) ** (3 * index + 3 - 2 * j))
            * recurrence_value
        )
        j += 1
    expected_patterns = {
        tuple(index * value for value in composition)
        for composition in _q_compositions(2, 3)
    }
    if j_zero_patterns is None or set(j_zero_patterns) != expected_patterns:
        raise ArithmeticError("Q j=0 incoming pattern classification")
    exceptional = [
        pattern for pattern in sorted(j_zero_patterns)
        if sorted(pattern) == [0, 0, 2 * index]
    ]
    regular = [
        pattern for pattern in sorted(j_zero_patterns)
        if sorted(pattern) == [0, index, index]
    ]
    if len(exceptional) != 3 or len(regular) != 3 or any(
        j_zero_patterns[pattern] != 0 for pattern in exceptional
    ):
        raise ArithmeticError("Q j=0 exceptional pattern control")
    empty_range_records = [
        record for record in components
        if record["component_index"] > index // 2 and record["component_index"] <= index
    ]
    if not empty_range_records or any(record["recurrence_value"] != 0 for record in empty_range_records):
        raise ArithmeticError("Q empty guarded range control")
    return {
        "index": index,
        "final_integer": final_integer,
        "private_component_records": components,
        "reduction_state_cache_size": len(memo),
        "route_agreement": True,
        "empty_range_zero_component_count": len(empty_range_records),
        "j_zero_incoming_pattern_totals": [
            {"incoming": list(pattern), "contribution": j_zero_patterns[pattern]}
            for pattern in sorted(j_zero_patterns)
        ],
        "j_zero_regular_pattern_count": len(regular),
        "j_zero_exceptional_pattern_count": len(exceptional),
        "j_zero_exceptional_nonzero_count": sum(
            1 for pattern in exceptional if j_zero_patterns[pattern] != 0
        ),
        "route_contract": {
            "base_case_outcomes": [1, 0],
            "signed_branch_coefficients": [2, -1, -1, 1],
            "termination_total_degree_decreases": [index, 2 * index, 2 * index - 1, 2 * index - 1],
            "normal_form_choice_rule": "first_reducible_coordinate",
            "independent_private_route_count": 2,
            "decorated_tuple_parameter_count": 18,
        },
    }


def _q_public_quartic_record(trace_terms, witness):
    low_period = witness["low_period_and_fixed_moment"]
    invariant_power = witness["normalized_affine_comparison"]["minimal_invariant_power"]
    fixed_length = low_period["fixed_basis_count"]
    exact_period_two_length = low_period["period_two_exact_basis_count"]
    quotient_rank = 4 * 4 * 4
    if exact_period_two_length != 12:
        raise ArithmeticError("Q period-two length")
    return {
        "cyclewise_moment": {
            "variable": "L",
            "terms": [
                {"exponent": 0, "coefficient": trace_terms[0]["coefficient"] // 3},
                {"exponent": 3, "coefficient": trace_terms[1]["coefficient"] // 3},
            ],
        },
        "exact_period_three_length": quotient_rank - fixed_length,
        "fiber_normal_form": "(x^2-L)^2",
        "fixed_length": fixed_length,
        "fixed_moment": len(low_period["fixed_trace_square_remainder"]),
        "normalized_conjugacy_coordinate": "L^" + str(invariant_power),
        "period_one_characteristic_polynomial": "T^" + str(fixed_length),
        "period_two_characteristic_polynomial": "(T-2)^" + str(exact_period_two_length),
        "pointwise_moment": {"variable": "L", "terms": trace_terms},
        "quotient_rank": quotient_rank,
    }


def run_science(definitions):
    if type(definitions) is not dict:
        raise TypeError("Q definitions object")
    if definitions.get("candidate_id") != "henon_period3_residue_v1":
        raise ValueError("Q candidate identity")
    if definitions.get("registered_coefficient_indices") != [8, 9]:
        raise ValueError("Q registered tuple is immutable")
    quartic_witness = quartic_quotient_witness()
    trace_terms = quartic_witness["trace_polynomial"]
    diagnostics = []
    private_diagnostics = []
    for index in (8, 9):
        record = _q_registered_coefficient_diagnostic(index)
        diagnostics.append({"index": index, "final_integer": record["final_integer"]})
        private_diagnostics.append(record)
    return {
        "public_quartic": _q_public_quartic_record(trace_terms, quartic_witness),
        "public_coefficient_diagnostics": diagnostics,
        "private_witness": {
            "schema": "HENON_PERIOD3_TRACK_Q_PRIVATE_WITNESS_V1",
            "track": "Q",
            "quartic": quartic_witness,
            "coefficient_diagnostics": private_diagnostics,
            "registered_engine_index_evaluation_count": 2,
            "full_high_degree_quotient_count": 0,
            "historical_result_access_count": 0,
        },
    }
