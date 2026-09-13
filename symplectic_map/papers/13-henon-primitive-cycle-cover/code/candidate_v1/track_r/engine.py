"""Track R: independent elimination, Fitting, and exterior certificates.

This scientific root has its own sparse arithmetic and never imports Track Q
or a project helper.  Its only import is the standard exact ``Fraction``
type.  Filesystem and capability confinement are owned by the Track-R runner.
"""

from fractions import Fraction


def _r_exact_value(left, right):
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(
            _r_exact_value(left[key], right[key]) for key in left
        )
    if type(left) in (list, tuple):
        return len(left) == len(right) and all(
            _r_exact_value(left[index], right[index]) for index in range(len(left))
        )
    return left == right


def _r_fraction(value):
    if type(value) is Fraction:
        return value
    if type(value) is int:
        return Fraction(value, 1)
    if type(value) in (list, tuple) and len(value) == 2:
        if type(value[0]) is not int or type(value[1]) is not int or value[1] <= 0:
            raise TypeError("R rational pair")
        return Fraction(value[0], value[1])
    raise TypeError("R exact rational required")


def _r_fraction_wire(value):
    exact = _r_fraction(value)
    return [exact.numerator, exact.denominator]


def _r_fraction_divide(left, right):
    numerator = _r_fraction(left)
    denominator = _r_fraction(right)
    if not denominator:
        raise ZeroDivisionError("R exact rational division by zero")
    return Fraction(
        numerator.numerator * denominator.denominator,
        numerator.denominator * denominator.numerator,
    )


def _r_exact_nonnegative_power(base, exponent):
    if type(base) not in (int, Fraction):
        raise TypeError("R exact scalar base required")
    if type(exponent) is not int or exponent < 0:
        raise TypeError("R exact scalar exponent must be a nonnegative integer")
    result = 1 if type(base) is int else Fraction(1, 1)
    factor = base
    remaining = exponent
    while remaining:
        if remaining % 2:
            result = result * factor
        remaining //= 2
        if remaining:
            factor = factor * factor
    return result


def _r_degree_one_boundary(rank):
    if type(rank) is not int or rank < 1:
        raise TypeError("R positive integral rank required")
    return rank == 1


def _r_exterior_monodromy_evidence(rank, difference_product):
    if type(rank) is not int or rank < 1:
        raise TypeError("R positive integral rank required")
    normalized = _r_normalize(difference_product)
    unit = {(0, 0, 0, 0): Fraction(1, 1)}
    return not _r_exact_value(normalized, unit)


def _r_normalize(polynomial):
    if type(polynomial) is not dict:
        raise TypeError("R polynomial dictionary required")
    output = {}
    for monomial, coefficient in polynomial.items():
        if type(monomial) is not tuple or len(monomial) != 4:
            raise TypeError("R monomial must be (a,c,x,y)")
        if any(type(exponent) is not int or exponent < 0 for exponent in monomial):
            raise TypeError("R exponent")
        exact = _r_fraction(coefficient)
        if exact:
            output[monomial] = output.get(monomial, Fraction(0, 1)) + exact
    return {monomial: coefficient for monomial, coefficient in output.items() if coefficient}


def _r_plus(left, right):
    result = dict(_r_normalize(left))
    for monomial, coefficient in _r_normalize(right).items():
        result[monomial] = result.get(monomial, Fraction(0, 1)) + coefficient
    return _r_normalize(result)


def _r_times_scalar(coefficient, polynomial):
    exact = _r_fraction(coefficient)
    return _r_normalize(
        {monomial: exact * value for monomial, value in _r_normalize(polynomial).items()}
    )


def _r_minus(left, right):
    return _r_plus(left, _r_times_scalar(-1, right))


def _r_times(left, right):
    result = {}
    for left_monomial, left_value in _r_normalize(left).items():
        for right_monomial, right_value in _r_normalize(right).items():
            monomial = tuple(
                left_monomial[index] + right_monomial[index]
                for index in (0, 1, 2, 3)
            )
            result[monomial] = result.get(monomial, Fraction(0, 1)) + left_value * right_value
    return _r_normalize(result)


def _r_power(polynomial, exponent):
    if type(exponent) is not int or exponent < 0:
        raise TypeError("R nonnegative exponent")
    result = {(0, 0, 0, 0): Fraction(1, 1)}
    factor = _r_normalize(polynomial)
    remaining = exponent
    while remaining:
        if remaining % 2:
            result = _r_times(result, factor)
        remaining //= 2
        if remaining:
            factor = _r_times(factor, factor)
    return result


def _r_monomial_order(item):
    return sum(item), item


def _r_leading(polynomial):
    normalized = _r_normalize(polynomial)
    if not normalized:
        return None, Fraction(0, 1)
    monomial = max(normalized, key=_r_monomial_order)
    return monomial, normalized[monomial]


def _r_exact_division(dividend, divisor):
    numerator = _r_normalize(dividend)
    denominator = _r_normalize(divisor)
    if not denominator:
        raise ZeroDivisionError("R exact division by zero")
    denominator_monomial, denominator_coefficient = _r_leading(denominator)
    quotient = {}
    remainder = {}
    while numerator:
        numerator_monomial, numerator_coefficient = _r_leading(numerator)
        if all(
            numerator_monomial[index] >= denominator_monomial[index]
            for index in (0, 1, 2, 3)
        ):
            shift = tuple(
                numerator_monomial[index] - denominator_monomial[index]
                for index in (0, 1, 2, 3)
            )
            term = {shift: _r_fraction_divide(numerator_coefficient, denominator_coefficient)}
            quotient = _r_plus(quotient, term)
            numerator = _r_minus(numerator, _r_times(term, denominator))
        else:
            term = {numerator_monomial: numerator_coefficient}
            remainder = _r_plus(remainder, term)
            numerator = _r_minus(numerator, term)
    return _r_normalize(quotient), _r_normalize(remainder)


def _r_bareiss(matrix):
    """Fraction-free determinant; every matrix size returns (det,pivots)."""
    if type(matrix) not in (list, tuple):
        raise TypeError("R matrix sequence required")
    size = len(matrix)
    one = {(0, 0, 0, 0): Fraction(1, 1)}
    if size == 0:
        return one, ()
    if any(type(row) not in (list, tuple) or len(row) != size for row in matrix):
        raise TypeError("R square matrix required")
    work = [[_r_normalize(entry) for entry in row] for row in matrix]
    if size == 1:
        return work[0][0], (work[0][0],)
    sign = 1
    previous = one
    pivots = []
    for pivot_index in range(size - 1):
        if not work[pivot_index][pivot_index]:
            replacement = None
            for row_index in range(pivot_index + 1, size):
                if work[row_index][pivot_index]:
                    replacement = row_index
                    break
            if replacement is None:
                return {}, tuple(pivots + [{}])
            work[pivot_index], work[replacement] = work[replacement], work[pivot_index]
            sign *= -1
        pivot = work[pivot_index][pivot_index]
        pivots.append(pivot)
        for row_index in range(pivot_index + 1, size):
            for column_index in range(pivot_index + 1, size):
                numerator = _r_minus(
                    _r_times(work[row_index][column_index], pivot),
                    _r_times(work[row_index][pivot_index], work[pivot_index][column_index]),
                )
                if pivot_index:
                    quotient, remainder = _r_exact_division(numerator, previous)
                    if remainder:
                        raise ArithmeticError("R nonexact Bareiss division")
                    work[row_index][column_index] = quotient
                else:
                    work[row_index][column_index] = numerator
            work[row_index][pivot_index] = {}
        previous = pivot
    determinant = _r_times_scalar(sign, work[size - 1][size - 1])
    pivots.append(work[size - 1][size - 1])
    return determinant, tuple(pivots)


def _r_sylvester_linear_quadratic(linear_low, quadratic_low):
    if (
        type(linear_low) not in (list, tuple)
        or type(quadratic_low) not in (list, tuple)
        or len(linear_low) != 2
        or len(quadratic_low) != 3
    ):
        raise TypeError("R linear/quadratic coefficient lists")
    zero = {}
    matrix = (
        (linear_low[1], linear_low[0], zero),
        (zero, linear_low[1], linear_low[0]),
        (quadratic_low[2], quadratic_low[1], quadratic_low[0]),
    )
    determinant, pivots = _r_bareiss(matrix)
    return determinant, tuple(pivots)


def _r_dense_strip(coefficients):
    if type(coefficients) not in (list, tuple):
        raise TypeError("R dense sequence")
    output = [_r_fraction(value) for value in coefficients]
    while output and output[-1] == 0:
        output.pop()
    return tuple(output)


def _r_dense_sum(left, right):
    first = _r_dense_strip(left)
    second = _r_dense_strip(right)
    width = max(len(first), len(second))
    return _r_dense_strip(
        tuple(
            (first[index] if index < len(first) else Fraction(0, 1))
            + (second[index] if index < len(second) else Fraction(0, 1))
            for index in range(width)
        )
    )


def _r_dense_product(left, right):
    first = _r_dense_strip(left)
    second = _r_dense_strip(right)
    if not first or not second:
        return ()
    output = [Fraction(0, 1)] * (len(first) + len(second) - 1)
    for first_index, first_value in enumerate(first):
        for second_index, second_value in enumerate(second):
            output[first_index + second_index] += first_value * second_value
    return _r_dense_strip(output)


def _r_dense_composition(outer, inner):
    output = ()
    for coefficient in reversed(_r_dense_strip(outer)):
        output = _r_dense_sum(_r_dense_product(output, inner), (coefficient,))
    return _r_dense_strip(output)


def _r_dense_quotient(dividend, divisor):
    numerator = list(_r_dense_strip(dividend))
    denominator = _r_dense_strip(divisor)
    if not denominator:
        raise ZeroDivisionError("R dense division by zero")
    if len(numerator) < len(denominator):
        return (), tuple(numerator)
    quotient = [Fraction(0, 1)] * (len(numerator) - len(denominator) + 1)
    while numerator and len(numerator) >= len(denominator):
        offset = len(numerator) - len(denominator)
        leading = _r_fraction_divide(numerator[-1], denominator[-1])
        quotient[offset] += leading
        for index, value in enumerate(denominator):
            numerator[index + offset] -= leading * value
        numerator = list(_r_dense_strip(numerator))
    return _r_dense_strip(quotient), _r_dense_strip(numerator)


def _r_dense_value(coefficients, point):
    exact_point = _r_fraction(point)
    output = Fraction(0, 1)
    for coefficient in reversed(_r_dense_strip(coefficients)):
        output = output * exact_point + coefficient
    return output


def _r_matrix_product2(left, right):
    if (
        type(left) not in (list, tuple)
        or type(right) not in (list, tuple)
        or len(left) != 2
        or len(right) != 2
        or any(type(row) not in (list, tuple) or len(row) != 2 for row in left)
        or any(type(row) not in (list, tuple) or len(row) != 2 for row in right)
    ):
        raise TypeError("R two by two matrices required")
    return tuple(
        tuple(
            _r_plus(
                _r_times(left[row][0], right[0][column]),
                _r_times(left[row][1], right[1][column]),
            )
            for column in (0, 1)
        )
        for row in (0, 1)
    )


def _r_matrix_trace2(matrix):
    if type(matrix) not in (list, tuple) or len(matrix) != 2:
        raise TypeError("R trace matrix")
    return _r_plus(matrix[0][0], matrix[1][1])


def _r_substitute_xy(polynomial, product):
    output = {}
    for (a_power, c_power, x_power, y_power), coefficient in _r_normalize(polynomial).items():
        base = {(a_power, c_power, 0, 0): coefficient}
        if (x_power, y_power) == (0, 0):
            output = _r_plus(output, base)
        elif (x_power, y_power) == (1, 1):
            output = _r_plus(output, _r_times(base, product))
        else:
            raise ArithmeticError("R unsupported xy substitution")
    return _r_normalize(output)


def _r_coefficients_in_x(polynomial):
    coefficients = {}
    for (a_power, c_power, x_power, y_power), coefficient in _r_normalize(polynomial).items():
        if y_power:
            raise ArithmeticError("R eliminated polynomial still contains y")
        base = coefficients.setdefault(x_power, {})
        base[(a_power, c_power, 0, 0)] = base.get(
            (a_power, c_power, 0, 0), Fraction(0, 1)
        ) + coefficient
    if not coefficients:
        return ()
    return tuple(_r_normalize(coefficients.get(index, {})) for index in range(max(coefficients) + 1))


def _r_semigroup_membership(target, generators):
    if type(target) is not int or target < 0:
        raise TypeError("R semigroup target")
    if (
        type(generators) not in (list, tuple)
        or not generators
        or any(type(generator) is not int or generator <= 0 for generator in generators)
    ):
        raise TypeError("R semigroup generators")
    frontier = {0}
    while frontier:
        value = min(frontier)
        frontier.remove(value)
        if value == target:
            return True
        for generator in generators:
            next_value = value + generator
            if next_value <= target and next_value not in frontier:
                frontier.add(next_value)
    return False


def _r_fitting_nilpotent_matrix(relation_low):
    relation = _r_dense_strip(relation_low)
    if len(relation) != 3 or relation[-1] != 1:
        raise ValueError("R monic quadratic relation")
    constant = relation[0]
    linear = relation[1]
    matrix = ((Fraction(0, 1), -constant), (Fraction(1, 1), -linear))
    square = tuple(
        tuple(
            sum(matrix[row][inner] * matrix[inner][column] for inner in (0, 1))
            for column in (0, 1)
        )
        for row in (0, 1)
    )
    return matrix, square


def _r_vandermonde(values):
    if type(values) not in (list, tuple):
        raise TypeError("R Vandermonde values")
    output = {(0, 0, 0, 0): Fraction(1, 1)}
    for left_index in range(len(values)):
        for right_index in range(left_index + 1, len(values)):
            output = _r_times(output, _r_minus(values[right_index], values[left_index]))
    return output


def _r_wire(polynomial):
    return [
        {
            "coefficient": _r_fraction_wire(coefficient),
            "exponents_acxy": list(monomial),
        }
        for monomial, coefficient in sorted(_r_normalize(polynomial).items())
    ]


def _r_scope_guard(record):
    if type(record) is not dict or set(record) != {"id", "malformed"}:
        raise ValueError("R scope-control shape")
    expected = {
        "N5": ["r>1 => tau in K", "r=1 => tau not in K"],
        "N6": ["r>1 => rho in K", "r=1 => rho not in K"],
    }
    if record["id"] not in expected or not _r_exact_value(record["malformed"], expected[record["id"]]):
        raise ValueError("R scope-control drift")
    if len(set(record["malformed"])) != 2:
        raise ValueError("R duplicated scope attack")
    return tuple(
        {"disposition": "REJECTED_SCOPE_ERROR", "statement": statement}
        for statement in record["malformed"]
    )


def _r_validate_inputs(definitions, fixture):
    if type(definitions) is not dict or definitions.get("schema") != "P13_DEFINITIONS_AND_TYPES_V1":
        raise ValueError("R definitions schema")
    if set(fixture) != {"candidate", "counter_inputs", "elimination_input", "schema", "track_identity"}:
        raise ValueError("R fixture keys")
    if fixture["schema"] != "P13_R_PRIVATE_INPUT_V1" or fixture["track_identity"] != "R":
        raise ValueError("R fixture identity")
    if fixture["candidate"] != definitions.get("candidate_id"):
        raise ValueError("R candidate identity")
    elimination = fixture["elimination_input"]
    if not _r_exact_value(elimination, {
        "cycle_length": 2,
        "degree": 2,
        "jacobian_layout": [["2*z", "a"], [1, 0]],
        "route": "sylvester_fitting_exterior",
        "variables": {"base": ["a", "c"], "cycle": ["x", "y"]},
    }):
        raise ValueError("R elimination boundary drift")
    controls = fixture["counter_inputs"]
    if type(controls) is not list or len(controls) != 7:
        raise ValueError("R control count")
    if not _r_exact_value([record.get("id") for record in controls], ["N1", "N2", "N3", "N5", "N6", "N7", "N8"]):
        raise ValueError("R control order or identity")
    n1 = controls[0]
    if not _r_exact_value(n1, {
        "id": "N1",
        "map_coefficients_high_to_low": [1, 0, "t_parameter"],
        "point": [-1, 2],
        "t_parameter": [-3, 4],
    }):
        raise ValueError("R N1 fixture drift")
    n2 = controls[1]
    if not _r_exact_value(n2, {
        "id": "N2",
        "relation_coefficients_low_to_high": [
            {"a_power": 1, "integer_coefficient": -1},
            {"a_power": 0, "integer_coefficient": 0},
            {"a_power": 0, "integer_coefficient": 1},
        ],
        "specialize": {"a": 0},
    }):
        raise ValueError("R N2 fixture drift")
    n3 = controls[2]
    if not _r_exact_value(n3, {
        "ambient": "Q[t]",
        "id": "N3",
        "normalizer_power": 1,
        "presentation": {
            "relation_left": {"u_power": 0, "v_power": 2},
            "relation_right": {"u_power": 3, "v_power": 0},
            "u_as_t_power": 2,
            "v_as_t_power": 3,
        },
    }):
        raise ValueError("R N3 fixture drift")
    _r_scope_guard(controls[3])
    _r_scope_guard(controls[4])
    if not _r_exact_value(controls[5], {
        "id": "N7",
        "proposed_restriction_arrow": "G_global -> subgroup_of -> G_special",
    }):
        raise ValueError("R N7 fixture drift")
    if not _r_exact_value(controls[6], {
        "id": "N8",
        "proposed_observable_kinds": ["field_extension_trace", "return_determinant"],
    }):
        raise ValueError("R N8 fixture drift")


def _r_validate_certificate(certificate):
    if type(certificate) is not dict or set(certificate) != {
        "candidate",
        "certificate_class",
        "records",
        "route",
        "schema",
        "track",
    }:
        raise ValueError("R certificate keys")
    if certificate["schema"] != "P13_R_EXACT_CERTIFICATE_V1" or certificate["track"] != "R":
        raise ValueError("R certificate identity")
    if set(certificate["records"]) != {"N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"}:
        raise ValueError("R record inventory")
    forbidden = ("PROVED", "SOURCE" + "_LOCK_PASS")
    pending = [certificate]
    while pending:
        item = pending.pop()
        if type(item) is dict:
            pending.extend(item.keys())
            pending.extend(item.values())
        elif type(item) in (list, tuple):
            pending.extend(item)
        elif type(item) is str and any(token in item for token in forbidden):
            raise ValueError("R forbidden authority language")
    return certificate


def run_science(definitions, fixture):
    """Compute Track R's bounded certificate after external launch gates."""
    _r_validate_inputs(definitions, fixture)
    one = {(0, 0, 0, 0): Fraction(1, 1)}
    zero = {}
    a = {(1, 0, 0, 0): Fraction(1, 1)}
    c = {(0, 1, 0, 0): Fraction(1, 1)}
    x = {(0, 0, 1, 0): Fraction(1, 1)}
    y = {(0, 0, 0, 1): Fraction(1, 1)}
    b = _r_minus(a, one)

    n1 = fixture["counter_inputs"][0]
    map_high = n1["map_coefficients_high_to_low"]
    parameter = _r_fraction(n1["t_parameter"])
    point = _r_fraction(n1["point"])
    map_low = tuple(
        parameter if value == "t_parameter" else _r_fraction(value)
        for value in reversed(map_high)
    )
    iterate_twice_minus_z = _r_dense_sum(
        _r_dense_composition(map_low, map_low), (0, -1)
    )
    iterate_once_minus_z = _r_dense_sum(map_low, (0, -1))
    phi2, phi2_remainder = _r_dense_quotient(iterate_twice_minus_z, iterate_once_minus_z)
    if phi2_remainder:
        raise ArithmeticError("R N1 dynatomic exact division")
    fixed_value = _r_dense_value(map_low, point)
    phi_value = _r_dense_value(phi2, point)
    map_degree = len(map_low) - 1
    multiplier = map_degree * _r_exact_nonnegative_power(point, map_degree - 1)
    if fixed_value != point or phi_value != 0 or multiplier != -1:
        raise ArithmeticError("R N1 formal lower-period record")

    n2 = fixture["counter_inputs"][1]
    n2_coefficients = []
    for coefficient in n2["relation_coefficients_low_to_high"]:
        n2_coefficients.append(
            _r_times_scalar(
                coefficient["integer_coefficient"],
                _r_power(a, coefficient["a_power"]),
            )
        )
    discriminant = _r_minus(
        _r_power(n2_coefficients[1], 2),
        _r_times_scalar(4, _r_times(n2_coefficients[2], n2_coefficients[0])),
    )
    if not discriminant:
        raise ArithmeticError("R N2 discriminant")
    specialized_relation = tuple(
        coefficient["integer_coefficient"]
        * _r_exact_nonnegative_power(n2["specialize"]["a"], coefficient["a_power"])
        for coefficient in n2["relation_coefficients_low_to_high"]
    )
    fitting_matrix, fitting_square = _r_fitting_nilpotent_matrix(specialized_relation)
    if fitting_matrix == ((0, 0), (0, 0)) or fitting_square != ((0, 0), (0, 0)):
        raise ArithmeticError("R N2 Fitting nilpotent witness")

    n3 = fixture["counter_inputs"][2]
    presentation = n3["presentation"]
    left_t_power = (
        presentation["relation_left"]["u_power"] * presentation["u_as_t_power"]
        + presentation["relation_left"]["v_power"] * presentation["v_as_t_power"]
    )
    right_t_power = (
        presentation["relation_right"]["u_power"] * presentation["u_as_t_power"]
        + presentation["relation_right"]["v_power"] * presentation["v_as_t_power"]
    )
    generators = (presentation["u_as_t_power"], presentation["v_as_t_power"])
    normalizer_power = n3["normalizer_power"]
    if left_t_power != right_t_power:
        raise ArithmeticError("R N3 presentation relation")
    normalizer_in_semigroup = _r_semigroup_membership(normalizer_power, generators)
    if normalizer_in_semigroup:
        raise ArithmeticError("R N3 strict normalization")
    fraction_power = presentation["v_as_t_power"] - presentation["u_as_t_power"]
    if fraction_power != normalizer_power:
        raise ArithmeticError("R N3 fraction-field witness")
    finite_module_exponents = tuple(range(min(generators)))

    elimination = fixture["elimination_input"]
    coefficient_a = _r_plus(_r_power(x, 2), c)
    coefficient_d = _r_plus(_r_times(b, x), c)
    resultant, sylvester_pivots = _r_sylvester_linear_quadratic(
        (coefficient_a, b), (coefficient_d, zero, one)
    )
    fixed_factor = _r_plus(_r_plus(_r_power(x, 2), _r_times(b, x)), c)
    primitive_factor, factor_remainder = _r_exact_division(resultant, fixed_factor)
    if factor_remainder:
        raise ArithmeticError("R fixed-factor elimination division")
    primitive_coefficients = _r_coefficients_in_x(primitive_factor)
    if len(primitive_coefficients) != 3 or primitive_coefficients[2] != one:
        raise ArithmeticError("R primitive quadratic shape")
    cycle_sum = _r_times_scalar(-1, primitive_coefficients[1])
    cycle_product = primitive_coefficients[0]
    matrix_x = ((_r_times_scalar(2, x), a), (one, zero))
    matrix_y = ((_r_times_scalar(2, y), a), (one, zero))
    return_matrix = _r_matrix_product2(matrix_y, matrix_x)
    pointwise_trace = _r_matrix_trace2(return_matrix)
    trace_on_cycle = _r_substitute_xy(pointwise_trace, cycle_product)
    nu = _r_exact_nonnegative_power(
        elimination["degree"], elimination["cycle_length"]
    ) - elimination["degree"]
    if nu % elimination["cycle_length"]:
        raise ArithmeticError("R boundary rank divisibility")
    rank = nu // elimination["cycle_length"]
    fitting_tau_det, fitting_tau_pivots = _r_bareiss(((cycle_sum,),))
    fitting_rho_det, fitting_rho_pivots = _r_bareiss(((trace_on_cycle,),))
    if fitting_tau_det != cycle_sum or fitting_rho_det != trace_on_cycle:
        raise ArithmeticError("R rank-one Fitting determinant")
    difference_product = _r_vandermonde((cycle_sum,))
    degree_one_boundary = _r_degree_one_boundary(rank)
    nontrivial_monodromy_evidence = _r_exterior_monodromy_evidence(
        rank, difference_product
    )

    certificate = {
        "candidate": fixture["candidate"],
        "certificate_class": "BOUNDED_EXACT_CONSISTENCY_RECORD",
        "records": {
            "N1": {
                "formal_dynatomic_value": _r_fraction_wire(phi_value),
                "map_value": _r_fraction_wire(fixed_value),
                "point_multiplier": _r_fraction_wire(multiplier),
                "unsafe_step": "REJECTED_FORMAL_TO_ACTUAL",
            },
            "N2": {
                "fitting_matrix": [[_r_fraction_wire(value) for value in row] for row in fitting_matrix],
                "fitting_square": [[_r_fraction_wire(value) for value in row] for row in fitting_square],
                "generic_discriminant": _r_wire(discriminant),
                "unsafe_step": "REJECTED_GENERIC_TO_ALL_FIBERS",
            },
            "N3": {
                "finite_module_exponents": list(finite_module_exponents),
                "fraction_exponent_identity": [
                    presentation["v_as_t_power"],
                    presentation["u_as_t_power"],
                    fraction_power,
                ],
                "fraction_power": fraction_power,
                "normalizer_in_semigroup": normalizer_in_semigroup,
                "presentation_t_power": left_t_power,
                "unsafe_step": "REJECTED_BIRATIONAL_TO_NORMAL_EQUALITY",
            },
            "N4": {
                "characteristic_rho": [_r_wire(_r_times_scalar(-1, trace_on_cycle)), _r_wire(one)],
                "characteristic_tau": [_r_wire(_r_times_scalar(-1, cycle_sum)), _r_wire(one)],
                "cycle_product": _r_wire(cycle_product),
                "cycle_sum": _r_wire(cycle_sum),
                "degree_one_boundary": degree_one_boundary,
                "difference_product": _r_wire(difference_product),
                "fitting_rho_pivot_count": len(fitting_rho_pivots),
                "fitting_tau_pivot_count": len(fitting_tau_pivots),
                "nontrivial_monodromy_evidence": nontrivial_monodromy_evidence,
                "nu": nu,
                "primitive_factor": _r_wire(primitive_factor),
                "rank": rank,
                "return_trace": _r_wire(trace_on_cycle),
                "sylvester_pivot_count": len(sylvester_pivots),
            },
            "N5": list(_r_scope_guard(fixture["counter_inputs"][3])),
            "N6": list(_r_scope_guard(fixture["counter_inputs"][4])),
            "N7": {
                "disposition": "REJECTED_DIRECTION",
                "proposed": fixture["counter_inputs"][5]["proposed_restriction_arrow"],
            },
            "N8": [
                {"disposition": "REJECTED_CATEGORY_SUBSTITUTION", "kind": kind}
                for kind in fixture["counter_inputs"][6]["proposed_observable_kinds"]
            ],
        },
        "route": "SYLVESTER_FITTING_EXTERIOR",
        "schema": "P13_R_EXACT_CERTIFICATE_V1",
        "track": "R",
    }
    return _r_validate_certificate(certificate)
