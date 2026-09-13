"""Track Q: exact cyclic-quotient and reduction certificates.

This module is a scientific root.  It imports only the standard exact
``Fraction`` type and no project module.  It never opens a path, creates a
process, uses a network capability, or writes an artifact.
"""

from fractions import Fraction


def _q_exact_value(left, right):
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(
            _q_exact_value(left[key], right[key]) for key in left
        )
    if type(left) in (list, tuple):
        return len(left) == len(right) and all(
            _q_exact_value(left[index], right[index]) for index in range(len(left))
        )
    return left == right


def _q_rat(value):
    if type(value) is Fraction:
        return value
    if type(value) is int:
        return Fraction(value, 1)
    if type(value) is dict and set(value) == {"denominator", "numerator"}:
        numerator = value["numerator"]
        denominator = value["denominator"]
        if type(numerator) is not int or type(denominator) is not int:
            raise TypeError("Q rational wire integers required")
        if denominator <= 0:
            raise ValueError("Q rational denominator must be positive")
        return Fraction(numerator, denominator)
    raise TypeError("Q exact rational input required")


def _q_rat_wire(value):
    exact = _q_rat(value)
    return {"denominator": exact.denominator, "numerator": exact.numerator}


def _q_fraction_divide(left, right):
    numerator = _q_rat(left)
    denominator = _q_rat(right)
    if not denominator:
        raise ZeroDivisionError("Q exact rational division by zero")
    return Fraction(
        numerator.numerator * denominator.denominator,
        numerator.denominator * denominator.numerator,
    )


def _q_exact_nonnegative_power(base, exponent):
    if type(base) not in (int, Fraction):
        raise TypeError("Q exact scalar base required")
    if type(exponent) is not int or exponent < 0:
        raise TypeError("Q exact scalar exponent must be a nonnegative integer")
    answer = 1 if type(base) is int else Fraction(1, 1)
    factor = base
    remaining = exponent
    while remaining:
        if remaining & 1:
            answer = answer * factor
        remaining //= 2
        if remaining:
            factor = factor * factor
    return answer


def _q_degree_one_boundary(rank):
    if type(rank) is not int or rank < 1:
        raise TypeError("Q positive integral rank required")
    return rank == 1


def _q_route_monodromy_evidence(rank, characteristic_polynomial):
    if type(rank) is not int or rank < 1:
        raise TypeError("Q positive integral rank required")
    if type(characteristic_polynomial) not in (list, tuple):
        raise TypeError("Q characteristic polynomial sequence required")
    if len(characteristic_polynomial) != rank + 1:
        raise ValueError("Q characteristic degree/rank mismatch")
    if any(type(coefficient) is not dict for coefficient in characteristic_polynomial):
        raise TypeError("Q characteristic coefficients must be sparse polynomials")
    return len(characteristic_polynomial) - 1 > 1


def _q_poly_clean(polynomial):
    if type(polynomial) is not dict:
        raise TypeError("Q sparse polynomial must be a dictionary")
    cleaned = {}
    for monomial, coefficient in polynomial.items():
        if type(monomial) is not tuple or len(monomial) != 4:
            raise TypeError("Q monomial must have four exponents")
        if any(type(exponent) is not int or exponent < 0 for exponent in monomial):
            raise TypeError("Q monomial exponents must be nonnegative integers")
        exact = _q_rat(coefficient)
        if exact:
            cleaned[monomial] = cleaned.get(monomial, Fraction(0, 1)) + exact
    return {monomial: coefficient for monomial, coefficient in cleaned.items() if coefficient}


def _q_poly_add(left, right):
    answer = dict(_q_poly_clean(left))
    for monomial, coefficient in _q_poly_clean(right).items():
        answer[monomial] = answer.get(monomial, Fraction(0, 1)) + coefficient
    return _q_poly_clean(answer)


def _q_poly_scale(coefficient, polynomial):
    exact = _q_rat(coefficient)
    return _q_poly_clean(
        {monomial: exact * value for monomial, value in _q_poly_clean(polynomial).items()}
    )


def _q_poly_sub(left, right):
    return _q_poly_add(left, _q_poly_scale(-1, right))


def _q_poly_mul(left, right):
    answer = {}
    for left_monomial, left_coefficient in _q_poly_clean(left).items():
        for right_monomial, right_coefficient in _q_poly_clean(right).items():
            monomial = tuple(
                left_monomial[index] + right_monomial[index] for index in (0, 1, 2, 3)
            )
            answer[monomial] = answer.get(monomial, Fraction(0, 1)) + (
                left_coefficient * right_coefficient
            )
    return _q_poly_clean(answer)


def _q_poly_pow(polynomial, exponent):
    if type(exponent) is not int or exponent < 0:
        raise TypeError("Q exponent must be a nonnegative integer")
    answer = {(0, 0, 0, 0): Fraction(1, 1)}
    factor = _q_poly_clean(polynomial)
    power = exponent
    while power:
        if power & 1:
            answer = _q_poly_mul(answer, factor)
        power //= 2
        if power:
            factor = _q_poly_mul(factor, factor)
    return answer


def _q_monomial_order(item):
    return sum(item), item


def _q_poly_lead_all(polynomial):
    cleaned = _q_poly_clean(polynomial)
    if not cleaned:
        return None, Fraction(0, 1)
    monomial = max(cleaned, key=_q_monomial_order)
    return monomial, cleaned[monomial]


def _q_poly_exact_div(dividend, divisor):
    """Single-divisor exact sparse division; every endpoint returns a pair."""
    work = _q_poly_clean(dividend)
    denominator = _q_poly_clean(divisor)
    if not denominator:
        raise ZeroDivisionError("Q sparse polynomial division by zero")
    denominator_monomial, denominator_coefficient = _q_poly_lead_all(denominator)
    quotient = {}
    remainder = {}
    while work:
        work_monomial, work_coefficient = _q_poly_lead_all(work)
        if all(work_monomial[index] >= denominator_monomial[index] for index in (0, 1, 2, 3)):
            shift = tuple(
                work_monomial[index] - denominator_monomial[index]
                for index in (0, 1, 2, 3)
            )
            term = {shift: _q_fraction_divide(work_coefficient, denominator_coefficient)}
            quotient = _q_poly_add(quotient, term)
            work = _q_poly_sub(work, _q_poly_mul(term, denominator))
        else:
            term = {work_monomial: work_coefficient}
            remainder = _q_poly_add(remainder, term)
            work = _q_poly_sub(work, term)
    return _q_poly_clean(quotient), _q_poly_clean(remainder)


def _q_dense_trim(coefficients):
    if type(coefficients) not in (list, tuple):
        raise TypeError("Q dense coefficients must be a sequence")
    cleaned = [_q_rat(value) for value in coefficients]
    while cleaned and cleaned[-1] == 0:
        cleaned.pop()
    return tuple(cleaned)


def _q_dense_add(left, right):
    left_clean = _q_dense_trim(left)
    right_clean = _q_dense_trim(right)
    length = max(len(left_clean), len(right_clean))
    return _q_dense_trim(
        [
            (left_clean[index] if index < len(left_clean) else Fraction(0, 1))
            + (right_clean[index] if index < len(right_clean) else Fraction(0, 1))
            for index in range(length)
        ]
    )


def _q_dense_mul(left, right):
    left_clean = _q_dense_trim(left)
    right_clean = _q_dense_trim(right)
    if not left_clean or not right_clean:
        return ()
    answer = [Fraction(0, 1)] * (len(left_clean) + len(right_clean) - 1)
    for left_index, left_value in enumerate(left_clean):
        for right_index, right_value in enumerate(right_clean):
            answer[left_index + right_index] += left_value * right_value
    return _q_dense_trim(answer)


def _q_dense_compose(outer, inner):
    answer = ()
    for coefficient in reversed(_q_dense_trim(outer)):
        answer = _q_dense_add(_q_dense_mul(answer, inner), (coefficient,))
    return _q_dense_trim(answer)


def _q_dense_divmod(dividend, divisor):
    numerator = list(_q_dense_trim(dividend))
    denominator = _q_dense_trim(divisor)
    if not denominator:
        raise ZeroDivisionError("Q polynomial division by zero")
    if not numerator or len(numerator) < len(denominator):
        return (), tuple(numerator)
    quotient = [Fraction(0, 1)] * (len(numerator) - len(denominator) + 1)
    while numerator and len(numerator) >= len(denominator):
        shift = len(numerator) - len(denominator)
        coefficient = _q_fraction_divide(numerator[-1], denominator[-1])
        quotient[shift] += coefficient
        for index, denominator_value in enumerate(denominator):
            numerator[index + shift] -= coefficient * denominator_value
        numerator = list(_q_dense_trim(numerator))
    return _q_dense_trim(quotient), _q_dense_trim(numerator)


def _q_dense_eval(coefficients, point):
    exact_point = _q_rat(point)
    answer = Fraction(0, 1)
    for coefficient in reversed(_q_dense_trim(coefficients)):
        answer = answer * exact_point + coefficient
    return answer


def _q_cycle_groups(polynomial):
    groups = {}
    for (a_exponent, c_exponent, z0_exponent, z1_exponent), coefficient in (
        _q_poly_clean(polynomial).items()
    ):
        cycle_monomial = (z0_exponent, z1_exponent)
        base_monomial = (a_exponent, c_exponent)
        group = groups.setdefault(cycle_monomial, {})
        group[base_monomial] = group.get(base_monomial, Fraction(0, 1)) + coefficient
    return {
        cycle: {base: value for base, value in coefficients.items() if value}
        for cycle, coefficients in groups.items()
        if any(coefficients.values())
    }


def _q_cycle_lead(polynomial):
    groups = _q_cycle_groups(polynomial)
    if not groups:
        return None, {}
    monomial = max(groups, key=_q_cycle_monomial_order)
    return monomial, groups[monomial]


def _q_cycle_monomial_order(item):
    return sum(item), item[0], item[1]


def _q_standard_exponents_from_leads(leads):
    if type(leads) not in (list, tuple) or len(leads) != 2:
        raise TypeError("Q two leading monomials required")
    if (
        type(leads[0]) is not tuple
        or type(leads[1]) is not tuple
        or leads[0][1] != 0
        or leads[1][0] != 0
        or leads[0][0] < 1
        or leads[1][1] < 1
    ):
        raise ValueError("Q pure-power leading monomials required")
    return tuple(
        (z0_exponent, z1_exponent)
        for z0_exponent in range(leads[0][0])
        for z1_exponent in range(leads[1][1])
    )


def _q_sum_from_exact_cycle_linear(linear_quotient):
    groups = _q_cycle_groups(linear_quotient)
    if set(groups) != {(0, 0), (0, 1), (1, 0)}:
        raise ArithmeticError("Q exact-cycle linear support")
    if groups[(1, 0)] != {(0, 0): Fraction(1, 1)}:
        raise ArithmeticError("Q z0 coefficient in exact-cycle quotient")
    if groups[(0, 1)] != {(0, 0): Fraction(1, 1)}:
        raise ArithmeticError("Q z1 coefficient in exact-cycle quotient")
    base_part = {
        (a_exponent, c_exponent, 0, 0): coefficient
        for (a_exponent, c_exponent), coefficient in groups[(0, 0)].items()
    }
    return _q_poly_scale(-1, base_part)


def _q_standard_reduce_boundary(polynomial, g0, g1):
    """Reduce by the two monic boundary relations; always return a pair."""
    work = _q_poly_clean(polynomial)
    normal = {}
    steps = []
    basis = (g0, g1)
    leads = ((2, 0), (0, 2))
    while work:
        cycle_monomial, base_coefficient = _q_cycle_lead(work)
        chosen = None
        for index, lead in enumerate(leads):
            if all(cycle_monomial[position] >= lead[position] for position in (0, 1)):
                chosen = index
                break
        if chosen is None:
            selected_terms = {
                monomial: coefficient
                for monomial, coefficient in work.items()
                if monomial[2:] == cycle_monomial
            }
            normal = _q_poly_add(normal, selected_terms)
            work = _q_poly_sub(work, selected_terms)
            continue
        shift_cycle = tuple(
            cycle_monomial[position] - leads[chosen][position] for position in (0, 1)
        )
        multiplier = {
            (a_exponent, c_exponent, shift_cycle[0], shift_cycle[1]): coefficient
            for (a_exponent, c_exponent), coefficient in base_coefficient.items()
        }
        work = _q_poly_sub(work, _q_poly_mul(multiplier, basis[chosen]))
        steps.append((chosen, shift_cycle, len(base_coefficient)))
    return _q_poly_clean(normal), tuple(steps)


def _q_swap_cycles(polynomial):
    return _q_poly_clean(
        {
            (a_exponent, c_exponent, z1_exponent, z0_exponent): coefficient
            for (
                a_exponent,
                c_exponent,
                z0_exponent,
                z1_exponent,
            ), coefficient in _q_poly_clean(polynomial).items()
        }
    )


def _q_reynolds_boundary(polynomial):
    return _q_poly_scale(Fraction(1, 2), _q_poly_add(polynomial, _q_swap_cycles(polynomial)))


def _q_matmul2(left, right):
    if (
        type(left) not in (list, tuple)
        or type(right) not in (list, tuple)
        or len(left) != 2
        or len(right) != 2
        or any(type(row) not in (list, tuple) or len(row) != 2 for row in left)
        or any(type(row) not in (list, tuple) or len(row) != 2 for row in right)
    ):
        raise TypeError("Q matrices must be two by two")
    return tuple(
        tuple(
            _q_poly_add(
                _q_poly_mul(left[row][0], right[0][column]),
                _q_poly_mul(left[row][1], right[1][column]),
            )
            for column in (0, 1)
        )
        for row in (0, 1)
    )


def _q_trace2(matrix):
    if type(matrix) not in (tuple, list) or len(matrix) != 2:
        raise TypeError("Q trace requires a two by two matrix")
    return _q_poly_add(matrix[0][0], matrix[1][1])


def _q_scope_rejections(assertions, observable):
    if observable not in ("tau", "rho") or type(assertions) is not list:
        raise TypeError("Q scope guard input")
    required = {
        (observable + "_is_base", "r_greater_than_one"),
        (observable + "_is_not_base", "r_equals_one"),
    }
    if len(assertions) != 2:
        raise ValueError("Q scope guard requires two distinct attacks")
    observed = set()
    for assertion in assertions:
        if type(assertion) is not dict or set(assertion) != {"predicate", "scope"}:
            raise ValueError("Q assertion shape")
        observed.add((assertion["predicate"], assertion["scope"]))
    if len(observed) != len(assertions) or observed != required:
        raise ValueError("Q malformed-scope fixture drift")
    return tuple(
        {"assertion": predicate + "@" + scope, "disposition": "REJECTED_SCOPE_ERROR"}
        for predicate, scope in sorted(observed)
    )


def _q_direction_rejection(control):
    required = {
        "left_group": "global",
        "relation": "contained_in",
        "right_group": "special",
        "use": "lower_bound",
    }
    if not _q_exact_value(control, required):
        raise ValueError("Q direction fixture drift")
    return {"disposition": "REJECTED_DIRECTION", "proposed": "global_to_special"}


def _q_trace_rejections(control):
    if not _q_exact_value(control, {
        "replacements": ["field_trace", "jacobian_determinant"],
        "target": "pointwise_derivative_return_trace",
    }):
        raise ValueError("Q trace-category fixture drift")
    return tuple(
        {"disposition": "REJECTED_CATEGORY_SUBSTITUTION", "replacement": item}
        for item in control["replacements"]
    )


def _q_semigroup_member(target, generators):
    if type(target) is not int or target < 0:
        raise TypeError("Q semigroup target")
    if (
        type(generators) not in (list, tuple)
        or not generators
        or any(type(item) is not int or item <= 0 for item in generators)
    ):
        raise TypeError("Q positive semigroup generators")
    reachable = {0}
    for value in range(1, target + 1):
        if any(value >= generator and (value - generator) in reachable for generator in generators):
            reachable.add(value)
    return target in reachable


def _q_substitute_cycle_product_once(polynomial, product):
    answer = {}
    for monomial, coefficient in _q_poly_clean(polynomial).items():
        a_exponent, c_exponent, z0_exponent, z1_exponent = monomial
        base_term = {(a_exponent, c_exponent, 0, 0): coefficient}
        if (z0_exponent, z1_exponent) == (0, 0):
            answer = _q_poly_add(answer, base_term)
        elif (z0_exponent, z1_exponent) == (1, 1):
            answer = _q_poly_add(answer, _q_poly_mul(base_term, product))
        else:
            raise ArithmeticError("Q unsupported cycle-product substitution")
    return _q_poly_clean(answer)


def _q_wire_poly(polynomial):
    return [
        {
            "coefficient": _q_rat_wire(coefficient),
            "exponents_acz0z1": list(monomial),
        }
        for monomial, coefficient in sorted(_q_poly_clean(polynomial).items())
    ]


def _q_validate_inputs(definitions, fixture):
    if type(definitions) is not dict or definitions.get("schema") != "P13_DEFINITIONS_AND_TYPES_V1":
        raise ValueError("Q definitions schema")
    if set(fixture) != {"boundary", "candidate_id", "controls", "schema", "track"}:
        raise ValueError("Q fixture keys")
    if fixture["schema"] != "P13_Q_PRIVATE_INPUT_V1" or fixture["track"] != "Q":
        raise ValueError("Q fixture identity")
    if fixture["candidate_id"] != definitions.get("candidate_id"):
        raise ValueError("Q candidate identity")
    if set(fixture["controls"]) != {"N1", "N2", "N3", "N5", "N6", "N7", "N8"}:
        raise ValueError("Q control inventory")
    boundary = fixture["boundary"]
    if set(boundary) != {
        "coordinate_names",
        "degree",
        "parameter_names",
        "period",
        "route",
    }:
        raise ValueError("Q boundary keys")
    if boundary["degree"] != 2 or boundary["period"] != 2:
        raise ValueError("Q only accepts the frozen boundary")
    if not _q_exact_value(boundary, {
        "coordinate_names": ["z0", "z1"],
        "degree": 2,
        "parameter_names": ["a", "c"],
        "period": 2,
        "route": "cyclic_quotient_reduction",
    }):
        raise ValueError("Q boundary convention drift")
    controls = fixture["controls"]
    if controls["N1"].keys() != {"coordinate", "family_degree", "parameter"}:
        raise ValueError("Q N1 keys")
    _q_rat(controls["N1"]["coordinate"])
    _q_rat(controls["N1"]["parameter"])
    if controls["N1"]["family_degree"] != boundary["degree"]:
        raise ValueError("Q N1 degree drift")
    if set(controls["N2"]) != {
        "base_parameter",
        "generator",
        "relation",
        "specialize_parameter_to",
    }:
        raise ValueError("Q N2 keys")
    if controls["N2"]["base_parameter"] != "a" or controls["N2"]["generator"] != "t":
        raise ValueError("Q N2 names")
    if set(controls["N2"]["relation"]) != {"constant", "linear", "quadratic"}:
        raise ValueError("Q N2 relation keys")
    if set(controls["N2"]["relation"]["constant"]) != {"coefficient", "parameter_power"}:
        raise ValueError("Q N2 constant keys")
    if any(
        type(value) is not int
        for value in (
            controls["N2"]["relation"]["constant"]["coefficient"],
            controls["N2"]["relation"]["constant"]["parameter_power"],
            controls["N2"]["relation"]["linear"],
            controls["N2"]["relation"]["quadratic"],
            controls["N2"]["specialize_parameter_to"],
        )
    ):
        raise TypeError("Q N2 exact integer coefficients")
    if not _q_exact_value(controls["N2"], {
        "base_parameter": "a",
        "generator": "t",
        "relation": {
            "constant": {"coefficient": -1, "parameter_power": 1},
            "linear": 0,
            "quadratic": 1,
        },
        "specialize_parameter_to": 0,
    }):
        raise ValueError("Q N2 fixed fixture drift")
    if set(controls["N3"]) != {
        "ambient_generator",
        "fraction_denominator_exponent",
        "fraction_numerator_exponent",
        "normalizer_exponent",
        "subring_generator_exponents",
    }:
        raise ValueError("Q N3 keys")
    if controls["N3"]["ambient_generator"] != "t":
        raise ValueError("Q N3 ambient name")
    if any(
        type(value) is not int or value <= 0
        for value in (
            controls["N3"]["fraction_denominator_exponent"],
            controls["N3"]["fraction_numerator_exponent"],
            controls["N3"]["normalizer_exponent"],
            *controls["N3"]["subring_generator_exponents"],
        )
    ):
        raise TypeError("Q N3 positive exponents")
    if not _q_exact_value(controls["N3"], {
        "ambient_generator": "t",
        "fraction_denominator_exponent": 2,
        "fraction_numerator_exponent": 3,
        "normalizer_exponent": 1,
        "subring_generator_exponents": [2, 3],
    }):
        raise ValueError("Q N3 fixed fixture drift")
    for identifier, observable in (("N5", "tau"), ("N6", "rho")):
        if set(controls[identifier]) != {"assertions"}:
            raise ValueError("Q scope-control keys")
        _q_scope_rejections(controls[identifier]["assertions"], observable)
    _q_direction_rejection(controls["N7"])
    _q_trace_rejections(controls["N8"])


def _q_validate_certificate(certificate):
    required = {"candidate_id", "certificate_kind", "controls", "route", "schema", "track"}
    if type(certificate) is not dict or set(certificate) != required:
        raise ValueError("Q certificate keys")
    if certificate["schema"] != "P13_Q_EXACT_CERTIFICATE_V1" or certificate["track"] != "Q":
        raise ValueError("Q certificate identity")
    if set(certificate["controls"]) != {"N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"}:
        raise ValueError("Q certificate control inventory")
    forbidden = ("PROVED", "SOURCE" + "_LOCK_PASS")
    stack = [certificate]
    while stack:
        value = stack.pop()
        if type(value) is dict:
            stack.extend(value.keys())
            stack.extend(value.values())
        elif type(value) in (list, tuple):
            stack.extend(value)
        elif type(value) is str and any(token in value for token in forbidden):
            raise ValueError("Q forbidden authority language")
    return certificate


def run_science(definitions, fixture):
    """Compute the bounded Track-Q certificate; called only after launch gates."""
    _q_validate_inputs(definitions, fixture)
    zero = {}
    one = {(0, 0, 0, 0): Fraction(1, 1)}
    a = {(1, 0, 0, 0): Fraction(1, 1)}
    c = {(0, 1, 0, 0): Fraction(1, 1)}
    z0 = {(0, 0, 1, 0): Fraction(1, 1)}
    z1 = {(0, 0, 0, 1): Fraction(1, 1)}
    b = _q_poly_sub(a, one)

    n1 = fixture["controls"]["N1"]
    point = _q_rat(n1["coordinate"])
    parameter = _q_rat(n1["parameter"])
    degree = n1["family_degree"]
    scalar_map = tuple(
        [parameter] + [Fraction(0, 1)] * (degree - 1) + [Fraction(1, 1)]
    )
    second_iterate_minus_identity = _q_dense_add(
        _q_dense_compose(scalar_map, scalar_map),
        (Fraction(0, 1), Fraction(-1, 1)),
    )
    first_iterate_minus_identity = _q_dense_add(
        scalar_map,
        (Fraction(0, 1), Fraction(-1, 1)),
    )
    dynatomic, dynatomic_remainder = _q_dense_divmod(
        second_iterate_minus_identity, first_iterate_minus_identity
    )
    if dynatomic_remainder:
        raise ArithmeticError("Q N1 dynatomic division was not exact")
    first_value = _q_dense_eval(scalar_map, point)
    dynatomic_value = _q_dense_eval(dynatomic, point)
    multiplier = degree * _q_exact_nonnegative_power(point, degree - 1)
    if first_value != point or dynatomic_value != 0 or multiplier != -1:
        raise ArithmeticError("Q N1 fixed formal-lower-period record")

    n2 = fixture["controls"]["N2"]
    n2_relation = n2["relation"]
    n2_constant = _q_poly_scale(
        n2_relation["constant"]["coefficient"],
        _q_poly_pow(a, n2_relation["constant"]["parameter_power"]),
    )
    n2_linear = _q_poly_scale(n2_relation["linear"], one)
    n2_quadratic = _q_poly_scale(n2_relation["quadratic"], one)
    n2_discriminant = _q_poly_sub(
        _q_poly_pow(n2_linear, 2),
        _q_poly_scale(4, _q_poly_mul(n2_quadratic, n2_constant)),
    )
    if not n2_discriminant or n2_relation["quadratic"] == 0:
        raise ArithmeticError("Q N2 generic separability witness")
    specialization = n2["specialize_parameter_to"]
    specialized_constant = (
        n2_relation["constant"]["coefficient"]
        * _q_exact_nonnegative_power(
            specialization, n2_relation["constant"]["parameter_power"]
        )
    )
    special_relation = _q_dense_trim(
        (specialized_constant, n2_relation["linear"], n2_relation["quadratic"])
    )
    special_degree = len(special_relation) - 1
    t_square_quotient, t_square_remainder = _q_dense_divmod((0, 0, 1), special_relation)
    t_quotient, t_remainder = _q_dense_divmod((0, 1), special_relation)
    if t_square_remainder or not t_square_quotient or not t_remainder or t_quotient:
        raise ArithmeticError("Q N2 special nilpotent computation")
    special_basis_exponents = tuple(range(special_degree))

    n3 = fixture["controls"]["N3"]
    n3_generators = tuple(n3["subring_generator_exponents"])
    normalizer_exponent = n3["normalizer_exponent"]
    numerator_exponent = n3["fraction_numerator_exponent"]
    denominator_exponent = n3["fraction_denominator_exponent"]
    semigroup_contains_normalizer = _q_semigroup_member(normalizer_exponent, n3_generators)
    if semigroup_contains_normalizer:
        raise ArithmeticError("Q N3 strict inclusion witness")
    if numerator_exponent not in n3_generators or denominator_exponent not in n3_generators:
        raise ArithmeticError("Q N3 fraction witnesses are not subring generators")
    if numerator_exponent - denominator_exponent != normalizer_exponent:
        raise ArithmeticError("Q N3 fraction-field identity")
    module_exponents = tuple(range(min(n3_generators)))
    if normalizer_exponent not in module_exponents:
        raise ArithmeticError("Q N3 finite-module witness")

    g0 = _q_poly_add(_q_poly_add(_q_poly_pow(z0, 2), _q_poly_mul(b, z1)), c)
    g1 = _q_poly_add(_q_poly_add(_q_poly_pow(z1, 2), _q_poly_mul(b, z0)), c)
    g0_lead = _q_cycle_lead(g0)
    g1_lead = _q_cycle_lead(g1)
    if g0_lead != ((2, 0), {(0, 0): Fraction(1, 1)}):
        raise ArithmeticError("Q first monic leading term")
    if g1_lead != ((0, 2), {(0, 0): Fraction(1, 1)}):
        raise ArithmeticError("Q second monic leading term")
    difference = _q_poly_sub(g0, g1)
    difference_factor = _q_poly_mul(_q_poly_sub(z0, z1), _q_poly_sub(_q_poly_add(z0, z1), b))
    if difference != difference_factor:
        raise ArithmeticError("Q cyclic difference factorization")
    exact_cycle_linear, exact_cycle_remainder = _q_poly_exact_div(
        difference, _q_poly_sub(z0, z1)
    )
    if exact_cycle_remainder:
        raise ArithmeticError("Q exact-cycle quotient remainder")
    cycle_sum = _q_sum_from_exact_cycle_linear(exact_cycle_linear)
    product_numerator = _q_poly_add(
        _q_poly_add(_q_poly_pow(cycle_sum, 2), _q_poly_mul(b, cycle_sum)),
        _q_poly_scale(2, c),
    )
    cycle_product = _q_poly_scale(Fraction(1, 2), product_numerator)
    symmetric_equation = _q_poly_add(
        _q_poly_add(_q_poly_sub(_q_poly_pow(cycle_sum, 2), _q_poly_scale(2, cycle_product)), _q_poly_mul(b, cycle_sum)),
        _q_poly_scale(2, c),
    )
    if symmetric_equation:
        raise ArithmeticError("Q symmetric quotient relation")
    matrix0 = ((_q_poly_scale(2, z0), a), (one, zero))
    matrix1 = ((_q_poly_scale(2, z1), a), (one, zero))
    return_matrix = _q_matmul2(matrix1, matrix0)
    derivative_trace = _q_trace2(return_matrix)
    trace_after_quotient = _q_substitute_cycle_product_once(
        derivative_trace, cycle_product
    )
    if derivative_trace != _q_poly_add(_q_poly_scale(4, _q_poly_mul(z0, z1)), _q_poly_scale(2, a)):
        raise ArithmeticError("Q direct trace identity")
    nu = _q_exact_nonnegative_power(fixture["boundary"]["degree"], 2) - fixture["boundary"]["degree"]
    rank = nu // fixture["boundary"]["period"]
    if (nu, rank) != (2, 1):
        raise ArithmeticError("Q boundary degree")
    reynolds_z0 = _q_reynolds_boundary(z0)
    if _q_reynolds_boundary(reynolds_z0) != reynolds_z0:
        raise ArithmeticError("Q Reynolds idempotence")
    if _q_reynolds_boundary(_q_swap_cycles(z0)) != reynolds_z0:
        raise ArithmeticError("Q Reynolds shift invariance")
    reduction_probe, reduction_steps = _q_standard_reduce_boundary(
        _q_poly_add(_q_poly_pow(z0, 2), _q_poly_pow(z1, 2)), g0, g1
    )
    expected_reduction_probe = _q_poly_sub(
        _q_poly_scale(-2, c), _q_poly_mul(b, _q_poly_add(z0, z1))
    )
    if not reduction_steps or reduction_probe != expected_reduction_probe:
        raise ArithmeticError("Q quotient reducer was hollow")
    standard_exponents = _q_standard_exponents_from_leads(
        (g0_lead[0], g1_lead[0])
    )
    characteristic_tau = [_q_poly_scale(-1, cycle_sum), one]
    characteristic_rho = [_q_poly_scale(-1, trace_after_quotient), one]
    degree_one_boundary = _q_degree_one_boundary(rank)
    nontrivial_monodromy_evidence = _q_route_monodromy_evidence(
        rank, characteristic_tau
    )

    certificate = {
        "candidate_id": fixture["candidate_id"],
        "certificate_kind": "BOUNDED_EXACT_CONSISTENCY_RECORD",
        "controls": {
            "N1": {
                "dynatomic_at_point": _q_rat_wire(dynatomic_value),
                "first_iterate_at_point": _q_rat_wire(first_value),
                "multiplier": _q_rat_wire(multiplier),
                "unsafe_inference": "REJECTED_FORMAL_TO_ACTUAL",
            },
            "N2": {
                "generic_discriminant": _q_wire_poly(n2_discriminant),
                "generic_separable": bool(n2_discriminant),
                "special_basis_exponents": list(special_basis_exponents),
                "special_generator_nonzero": bool(t_remainder),
                "special_nilpotent_square": [_q_rat_wire(value) for value in t_square_remainder],
                "unsafe_inference": "REJECTED_GENERIC_TO_ALL_FIBERS",
            },
            "N3": {
                "finite_module_generator_exponents": list(module_exponents),
                "fraction_exponent_identity": [
                    numerator_exponent,
                    denominator_exponent,
                    normalizer_exponent,
                ],
                "normalizer_exponent_in_subring_semigroup": semigroup_contains_normalizer,
                "unsafe_inference": "REJECTED_BIRATIONAL_TO_NORMAL_EQUALITY",
            },
            "N4": {
                "characteristic_polynomial_rho": [_q_wire_poly(value) for value in characteristic_rho],
                "characteristic_polynomial_tau": [_q_wire_poly(value) for value in characteristic_tau],
                "cycle_product": _q_wire_poly(cycle_product),
                "cycle_sum": _q_wire_poly(cycle_sum),
                "derivative_trace": _q_wire_poly(trace_after_quotient),
                "degree_one_boundary": degree_one_boundary,
                "nontrivial_monodromy_evidence": nontrivial_monodromy_evidence,
                "nu": nu,
                "rank": rank,
                "reduction_probe": _q_wire_poly(reduction_probe),
                "reduction_step_count": len(reduction_steps),
                "reynolds_z0": _q_wire_poly(reynolds_z0),
                "standard_cycle_exponents": [list(item) for item in standard_exponents],
            },
            "N5": list(_q_scope_rejections(fixture["controls"]["N5"]["assertions"], "tau")),
            "N6": list(_q_scope_rejections(fixture["controls"]["N6"]["assertions"], "rho")),
            "N7": _q_direction_rejection(fixture["controls"]["N7"]),
            "N8": list(_q_trace_rejections(fixture["controls"]["N8"])),
        },
        "route": "CYCLIC_QUOTIENT_REDUCTION",
        "schema": "P13_Q_EXACT_CERTIFICATE_V1",
        "track": "Q",
    }
    return _q_validate_certificate(certificate)
