"""Track R: private residue, root-partition, and collapsed exact arithmetic.

This module deliberately has no imports and no filesystem, environment,
serialization, subprocess, or network capability.  Its arithmetic and data
structures are private to Track R.
"""


def _r_product(values):
    result = 1
    for value in values:
        result *= value
    return result


def _r_binomial(nonnegative_top, lower):
    if type(nonnegative_top) is not int or type(lower) is not int:
        raise TypeError("R binomial exact integer domain")
    if nonnegative_top < 0 or lower < 0 or lower > nonnegative_top:
        return 0
    lower = min(lower, nonnegative_top - lower)
    numerator = 1
    denominator = 1
    cursor = 1
    while cursor <= lower:
        numerator *= nonnegative_top - lower + cursor
        denominator *= cursor
        cursor += 1
    return numerator // denominator


def generalized_binomial(upper, lower):
    if type(upper) is not int or type(lower) is not int:
        raise TypeError("R generalized binomial excludes booleans and non-integers")
    if lower < 0:
        return 0
    if lower == 0:
        return 1
    numerator = 1
    denominator = 1
    cursor = 0
    while cursor < lower:
        numerator *= upper - cursor
        denominator *= cursor + 1
        cursor += 1
    return numerator // denominator


def _r_multinomial(total, parts):
    if type(total) is not int or type(parts) is not tuple:
        raise TypeError("R multinomial types")
    if any(type(item) is not int or item < 0 for item in parts) or sum(parts) != total:
        return 0
    result = 1
    remaining = total
    for item in parts:
        result *= _r_binomial(remaining, item)
        remaining -= item
    return result


def _r_compositions(total, width):
    if type(total) is not int or type(width) is not int or total < 0 or width < 1:
        raise ValueError("R composition domain")
    if width == 1:
        yield (total,)
        return
    first = 0
    while first <= total:
        for remainder in _r_compositions(total - first, width - 1):
            yield (first,) + remainder
        first += 1


def _r_sparse_sum(left, right):
    result = dict(left)
    for powers, coefficient in right.items():
        updated = result.get(powers, 0) + coefficient
        if updated:
            result[powers] = updated
        elif powers in result:
            del result[powers]
    return result


def _r_sparse_product(left, right):
    result = {}
    for p_left, c_left in left.items():
        for p_right, c_right in right.items():
            powers = tuple(p_left[index] + p_right[index] for index in (0, 1, 2))
            result[powers] = result.get(powers, 0) + c_left * c_right
    return {powers: coefficient for powers, coefficient in result.items() if coefficient}


def _r_sparse_power(poly, exponent):
    if type(exponent) is not int or exponent < 0:
        raise ValueError("R sparse exponent")
    result = {(0, 0, 0): 1}
    cursor = 0
    while cursor < exponent:
        result = _r_sparse_product(result, poly)
        cursor += 1
    return result


def _r_rho(power_g, denominator_level, added_power):
    exponent = power_g - 2 * denominator_level - 2
    leading_power = added_power + power_g + 2 * exponent
    numerator = leading_power + 1
    if numerator % 2:
        return 0
    selection = numerator // 2
    if selection < 0:
        return 0
    return ((-1) ** selection) * generalized_binomial(exponent, selection)


def _r_coupling_polynomial(levels):
    forms = (
        {(0, 0, 1): 1, (0, 1, 0): -1},
        {(1, 0, 0): 1, (0, 0, 1): -1},
        {(0, 1, 0): 1, (1, 0, 0): -1},
    )
    result = {(0, 0, 0): 1}
    for index in (0, 1, 2):
        result = _r_sparse_product(result, _r_sparse_power(forms[index], levels[index]))
    return result


def _r_tensor_component(component_index):
    if type(component_index) is not int or component_index < 0 or component_index > 3:
        raise ValueError("R quartic tensor component")
    internal_epsilon_degree = 4 - 2 * component_index
    if internal_epsilon_degree < 0:
        return 0
    total = 0
    for selections in _r_compositions(component_index, 3):
        g_powers = tuple(3 - component_index + selections[index] for index in (0, 1, 2))
        selection_weight = _r_multinomial(component_index, selections)
        for denominator_levels in _r_compositions(internal_epsilon_degree, 3):
            coupling = _r_coupling_polynomial(denominator_levels)
            tensor_value = 0
            for added_powers, coefficient in coupling.items():
                factors = [
                    _r_rho(g_powers[index], denominator_levels[index], added_powers[index])
                    for index in (0, 1, 2)
                ]
                tensor_value += coefficient * _r_product(factors)
            sign = -1 if internal_epsilon_degree % 2 else 1
            total += selection_weight * sign * tensor_value
    return total


def _r_top_coefficient(exponents, memo):
    if exponents in memo:
        return memo[exponents]
    if any(type(value) is not int or value < 0 for value in exponents):
        return 0
    selected = None
    for index in (0, 1, 2):
        if exponents[index] >= 4:
            selected = index
            break
    if selected is None:
        value = int(exponents == (3, 3, 3))
        memo[exponents] = value
        return value
    base = list(exponents)
    base[selected] -= 4
    previous = list(base)
    previous[(selected - 1) % 3] += 1
    following = list(base)
    following[(selected + 1) % 3] += 1
    value = -_r_top_coefficient(tuple(previous), memo) + _r_top_coefficient(tuple(following), memo)
    memo[exponents] = value
    return value


def _r_quartic_constant():
    trace_terms = {
        (3, 3, 3): 64,
        (3, 0, 0): 4,
        (0, 3, 0): 4,
        (0, 0, 3): 4,
    }
    cube = _r_sparse_power(trace_terms, 3)
    memo = {}
    total = 0
    term_ledger = []
    for exponents in sorted(cube):
        residue = _r_top_coefficient(exponents, memo)
        contribution = cube[exponents] * residue
        if contribution:
            term_ledger.append({
                "exponents": list(exponents),
                "source_coefficient": cube[exponents],
                "top_coefficient": residue,
                "contribution": contribution,
            })
        total += contribution
    return total, term_ledger


def _r_root_partition_witness():
    allowed = []
    for first in range(4, 1, -1):
        remainder = 4 - first
        if remainder == 0:
            allowed.append([first])
        elif remainder >= 2 and first >= remainder:
            allowed.append([first, remainder])
    factor_minus = {(0, 1): 1, (1, 0): -1}
    factor_plus = {(0, 1): 1, (1, 0): 1}
    centered_two_plus_two = _r_alpha_product(
        _r_alpha_power(factor_minus, 2), _r_alpha_power(factor_plus, 2)
    )
    fourth_power = _r_alpha_power(factor_minus, 4)
    centered_fourth_cubic_coefficient = fourth_power.get((1, 3), 0)
    negative_fixture = [0, -1, 0, 0, 1]
    negative_derivative = [
        degree * negative_fixture[degree] for degree in range(1, len(negative_fixture))
    ]
    zero_is_root = negative_fixture[0] == 0
    derivative_at_zero = negative_derivative[0]
    expected_two_plus_two = {(0, 4): 1, (2, 2): -2, (4, 0): 1}
    if (allowed != [[4], [2, 2]] or centered_two_plus_two != expected_two_plus_two
            or centered_fourth_cubic_coefficient != -4 or not zero_is_root
            or derivative_at_zero == 0):
        raise ArithmeticError("R root-partition fiber derivation failed")
    return {
        "partitions_with_every_part_at_least_two": allowed,
        "partition_4_centering_coefficient": centered_fourth_cubic_coefficient,
        "partition_4_centered_root_coefficient": 0,
        "partition_2_plus_2_expansion": [
            {"alpha_exponent": alpha_power, "x_exponent": x_power, "coefficient": coefficient}
            for (alpha_power, x_power), coefficient in sorted(centered_two_plus_two.items())
        ],
        "parameter_alpha_exponent": 2,
        "simple_root_fixture": {
            "zero_is_root": zero_is_root,
            "derivative_at_zero": derivative_at_zero,
            "rejected": derivative_at_zero != 0,
        },
    }


def _r_alpha_product(left, right):
    result = {}
    for (alpha_left, x_left), coefficient_left in left.items():
        for (alpha_right, x_right), coefficient_right in right.items():
            key = (alpha_left + alpha_right, x_left + x_right)
            result[key] = result.get(key, 0) + coefficient_left * coefficient_right
    return {key: coefficient for key, coefficient in result.items() if coefficient}


def _r_alpha_power(poly, exponent):
    result = {(0, 0): 1}
    counter = 0
    while counter < exponent:
        result = _r_alpha_product(result, poly)
        counter += 1
    return result


def _r_series_sum(left, right):
    result = dict(left)
    for exponent, coefficient in right.items():
        updated = result.get(exponent, 0) + coefficient
        if updated:
            result[exponent] = updated
        elif exponent in result:
            del result[exponent]
    return result


def _r_series_product(left, right, maximum_degree):
    result = {}
    for exponent_left, coefficient_left in left.items():
        for exponent_right, coefficient_right in right.items():
            exponent = exponent_left + exponent_right
            if exponent <= maximum_degree:
                result[exponent] = result.get(exponent, 0) + coefficient_left * coefficient_right
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def _r_series_power(poly, exponent, maximum_degree):
    result = {0: 1}
    counter = 0
    while counter < exponent:
        result = _r_series_product(result, poly, maximum_degree)
        counter += 1
    return result


def _r_local_elimination(root_multiplicity):
    maximum_degree = 2 * root_multiplicity - 2
    delta = {1: 1}
    u = {}
    v = {}
    for _ in range(4):
        delta_plus_v = _r_series_sum(delta, v)
        u = {
            exponent: -coefficient
            for exponent, coefficient in _r_series_power(
                delta_plus_v, root_multiplicity, maximum_degree
            ).items()
        }
        delta_plus_u = _r_series_sum(delta, u)
        v = _r_series_power(delta_plus_u, root_multiplicity, maximum_degree)
    remaining = _r_series_sum(
        _r_series_sum(_r_series_power(delta, root_multiplicity, maximum_degree), v),
        {exponent: -coefficient for exponent, coefficient in u.items()},
    )
    ordered = sorted(remaining)
    return {
        "root_multiplicity": root_multiplicity,
        "truncation_degree": maximum_degree,
        "transverse_jacobian_determinant": 1,
        "u_terms": [{"exponent": exponent, "coefficient": u[exponent]} for exponent in sorted(u)],
        "v_terms": [{"exponent": exponent, "coefficient": v[exponent]} for exponent in sorted(v)],
        "remaining_order": ordered[0] if ordered else None,
        "remaining_leading_coefficient": remaining[ordered[0]] if ordered else None,
    }


def _r_local_order_witness():
    records = []
    for root_multiplicity in (2, 4):
        records.append(_r_local_elimination(root_multiplicity))
    return records


def _r_factor_polynomial_product(left, right):
    result = {}
    for (l_left, x_left), coefficient_left in left.items():
        for (l_right, x_right), coefficient_right in right.items():
            key = (l_left + l_right, x_left + x_right)
            result[key] = result.get(key, 0) + coefficient_left * coefficient_right
    return {key: coefficient for key, coefficient in result.items() if coefficient}


def _r_factor_polynomial_sum(left, right):
    result = dict(left)
    for key, coefficient in right.items():
        updated = result.get(key, 0) + coefficient
        if updated:
            result[key] = updated
        elif key in result:
            del result[key]
    return result


def _r_fixed_moment_witness():
    factor = {(0, 2): 1, (1, 0): -1}
    p_poly = _r_factor_polynomial_product(factor, factor)
    q_poly = {(0, 3): 4, (1, 1): -4}
    q_square = _r_factor_polynomial_product(q_poly, q_poly)
    expected_multiple = {
        (l_power, x_power + 2): 16 * coefficient
        for (l_power, x_power), coefficient in p_poly.items()
    }
    q_square_difference = _r_factor_polynomial_sum(
        q_square, {key: -coefficient for key, coefficient in expected_multiple.items()}
    )
    q_cube = _r_factor_polynomial_product(q_square, q_poly)
    trace_poly = _r_factor_polynomial_sum(
        q_cube, {key: 3 * coefficient for key, coefficient in q_poly.items()}
    )
    trace_square = _r_factor_polynomial_product(trace_poly, trace_poly)
    q_fourth = _r_factor_polynomial_product(q_square, q_square)
    inner = _r_factor_polynomial_sum(
        _r_factor_polynomial_sum(
            q_fourth, {key: 6 * coefficient for key, coefficient in q_square.items()}
        ),
        {(0, 0): 9},
    )
    quotient_factor = _r_factor_polynomial_product({(0, 2): 16}, inner)
    p_times_factor = _r_factor_polynomial_product(p_poly, quotient_factor)
    trace_square_difference = _r_factor_polynomial_sum(
        trace_square, {key: -coefficient for key, coefficient in p_times_factor.items()}
    )
    if q_square_difference or trace_square_difference:
        raise ArithmeticError("R fixed moment factorization failed")
    return {
        "q_square_quotient_factor": [{"L_exponent": 0, "x_exponent": 2, "coefficient": 16}],
        "q_square_factorization_remainder": [],
        "trace_square_factorization_remainder": [],
        "fixed_moment": 0,
    }


def _r_evaluate_alpha_relation(poly, sign):
    evaluated = {}
    for (l_power, x_power), coefficient in poly.items():
        alpha_power = 2 * l_power + x_power
        updated = evaluated.get(alpha_power, 0) + coefficient * (sign ** x_power)
        if updated:
            evaluated[alpha_power] = updated
        elif alpha_power in evaluated:
            del evaluated[alpha_power]
    return evaluated


def _r_evaluate_origin(poly):
    return poly.get((0, 0), 0)


def _r_low_period_partition_case(partition, q_poly):
    multiplicities = list(partition)
    if multiplicities == [2, 2]:
        support_parameters = (-1, 1)
        support_remainders = [
            _r_evaluate_alpha_relation(q_poly, sign) for sign in support_parameters
        ]
        relation = "x=sign*alpha,L=alpha^2"
    elif multiplicities == [4]:
        support_parameters = (0,)
        origin_value = _r_evaluate_origin(q_poly)
        support_remainders = [{}] if origin_value == 0 else [{0: origin_value}]
        relation = "x=0,L=0"
    else:
        raise ValueError("R unsupported quartic root partition")
    if any(remainder for remainder in support_remainders):
        raise ArithmeticError("R symbolic support factor failed")
    fixed_formal_values = []
    for multiplicity, remainder in zip(multiplicities, support_remainders):
        support_value = sum(remainder.values())
        fixed_formal_values.extend([support_value] * multiplicity)
    period_two_ambient_values = [
        2 + left * right for left in fixed_formal_values for right in fixed_formal_values
    ]
    fixed_length = sum(multiplicities)
    period_two_ambient_length = len(period_two_ambient_values)
    exact_period_two_length = period_two_ambient_length - fixed_length
    if (fixed_formal_values != [0] * fixed_length
            or period_two_ambient_length != fixed_length * fixed_length
            or any(value != 2 for value in period_two_ambient_values)):
        raise ArithmeticError("R low-period root-support calculation")
    return {
        "root_partition": multiplicities,
        "symbolic_root_relation": relation,
        "support_parameter_labels": list(support_parameters),
        "support_q_remainders": [
            [
                {"alpha_exponent": exponent, "coefficient": coefficient}
                for exponent, coefficient in sorted(remainder.items())
            ]
            for remainder in support_remainders
        ],
        "fixed_formal_values": fixed_formal_values,
        "fixed_length": fixed_length,
        "period_two_support_values": period_two_ambient_values,
        "period_two_ambient_length": period_two_ambient_length,
        "period_two_exact_length": exact_period_two_length,
    }


def _r_low_period_witness():
    h_poly = {(0, 2): 1, (1, 0): -1}
    p_poly = _r_factor_polynomial_product(h_poly, h_poly)
    q_from_factor = _r_factor_polynomial_product({(0, 1): 4}, h_poly)
    expected_p = {(0, 4): 1, (1, 2): -2, (2, 0): 1}
    expected_q = {(0, 3): 4, (1, 1): -4}
    p_difference = _r_factor_polynomial_sum(
        p_poly, {key: -coefficient for key, coefficient in expected_p.items()}
    )
    q_difference = _r_factor_polynomial_sum(
        q_from_factor, {key: -coefficient for key, coefficient in expected_q.items()}
    )
    if p_difference or q_difference:
        raise ArithmeticError("R symbolic quartic factor identities failed")
    cases = [
        _r_low_period_partition_case([2, 2], q_from_factor),
        _r_low_period_partition_case([4], q_from_factor),
    ]
    common_counts = {
        (case["fixed_length"], case["period_two_ambient_length"],
         case["period_two_exact_length"])
        for case in cases
    }
    if common_counts != {(4, 16, 12)}:
        raise ArithmeticError("R quartic partitions disagree on low-period lengths")
    fixed_length, ambient_length, exact_length = next(iter(common_counts))
    return {
        "factor_h_terms": [
            {"L_exponent": l_power, "x_exponent": x_power, "coefficient": coefficient}
            for (l_power, x_power), coefficient in sorted(h_poly.items())
        ],
        "p_minus_h_square_remainder": [],
        "q_minus_4x_h_remainder": [],
        "partition_cases": cases,
        "fixed_formal_zero_count": fixed_length,
        "fixed_length": fixed_length,
        "period_two_support_trace": cases[0]["period_two_support_values"][0],
        "period_two_ambient_length": ambient_length,
        "period_two_exact_length": exact_length,
    }


def _r_conjugacy_witness():
    group_order = 3
    parameter_weight = -2
    invariant_power = 1
    while (parameter_weight * invariant_power) % group_order:
        invariant_power += 1
    sufficiency_exponent = 0
    while (parameter_weight * sufficiency_exponent) % group_order != 1:
        sufficiency_exponent += 1
    if invariant_power != 3 or sufficiency_exponent != 1:
        raise ArithmeticError("R scaling-conjugator arithmetic")
    return {
        "root_of_unity_group_order": group_order,
        "parameter_weight": parameter_weight,
        "minimal_invariant_power": invariant_power,
        "explicit_conjugator_exponent": sufficiency_exponent,
    }


def quartic_residue_witness():
    tensor_components = [_r_tensor_component(index) for index in (0, 1, 2)]
    slope = 0
    for index, component in enumerate(tensor_components):
        slope += _r_binomial(3, index) * (4 ** (9 - 2 * index)) * component
    constant, constant_terms = _r_quartic_constant()
    local_orders = _r_local_order_witness()
    if any(record["remaining_order"] != record["root_multiplicity"] or
           record["remaining_leading_coefficient"] != 3 for record in local_orders):
        raise ArithmeticError("R local order witness failed")
    root_fiber = _r_root_partition_witness()
    low_period = _r_low_period_witness()
    fixed_moment = _r_fixed_moment_witness()
    conjugacy = _r_conjugacy_witness()
    return {
        "route": "NORMALIZED_GLOBAL_RESIDUE_AND_ROOT_PARTITIONS",
        "root_partition_fiber": root_fiber,
        "normalized_scaling": conjugacy,
        "low_period": low_period,
        "tensor_laurent_components": [
            {"component_index": index, "coefficient": tensor_components[index]}
            for index in (0, 1, 2)
        ],
        "direct_slope": slope,
        "constant_top_coefficient": constant,
        "constant_term_ledger": constant_terms,
        "fixed_moment": fixed_moment,
        "local_fixed_orders": local_orders,
    }


def H_value(r, k):
    if type(r) is not int or type(k) is not int or r < 0 or k < 0:
        raise ValueError("R H domain")
    total = 0
    u = 0
    while u <= k:
        v = k - u
        if 2 * u <= r and 2 * v <= r:
            total += _r_binomial(k, u) * _r_binomial(r, 2 * u) * _r_binomial(r, 2 * v)
        u += 1
    return total


def A_value(index, r):
    if type(index) is not int or type(r) is not int or index < 2 or r < 0:
        raise ValueError("R A domain")
    lower = (index + 1) // 2
    upper = min(index - 1, r)
    total = 0
    k = lower
    while k <= upper:
        sign = -1 if (r + k) % 2 else 1
        total += (
            sign
            * _r_binomial(index - 1, 2 * (index - k) - 1)
            * H_value(r, k)
        )
        k += 1
    return total


def _r_registered_collapsed_diagnostic(index):
    if type(index) is not int or index not in (8, 9):
        raise ValueError("R isolated index allowlist")
    q = index // 2
    expanded = 0
    factored_integer = 0
    records = []
    j = 0
    while j <= q:
        a_value = A_value(index, index - j)
        common = _r_binomial(index + 1, j)
        expanded_term = 3 * common * ((2 * index) ** (3 * index + 3 - 2 * j)) * a_value
        factored_term = common * ((2 * index) ** (2 * (q - j))) * a_value
        expanded += expanded_term
        factored_integer += factored_term
        records.append({
            "summation_index": j,
            "A_value": a_value,
            "expanded_term": expanded_term,
            "factored_term": factored_term,
        })
        j += 1
    reconstructed = 3 * ((2 * index) ** (3 * index + 3 - 2 * q)) * factored_integer
    if reconstructed != expanded:
        raise ArithmeticError("R expanded and factored forms disagree")
    empty_r = (index + 1) // 2 - 1
    empty_range_value = A_value(index, empty_r)
    if empty_range_value != 0 or not records or records[0]["summation_index"] != 0:
        raise ArithmeticError("R guarded-range boundary control")
    return {
        "index": index,
        "final_integer": expanded,
        "E_value": factored_integer,
        "guarded_records": records,
        "expanded_factored_agreement": True,
        "empty_range_probe_r": empty_r,
        "empty_range_probe_value": empty_range_value,
        "generalized_binomial_boundary": {
            "negative_upper_at_zero": generalized_binomial(-3, 0),
            "negative_upper_at_one": generalized_binomial(-3, 1),
            "negative_lower": generalized_binomial(5, -1),
            "ordinary_out_of_range": generalized_binomial(5, 6),
        },
        "route_contract": {
            "guarded_outer_lower": 0,
            "guarded_outer_upper": q,
            "inner_lower": (index + 1) // 2,
            "j_zero_term_present": records[0]["summation_index"] == 0,
            "expanded_factored_private_route_count": 2,
        },
    }


def _r_public_quartic_record(constant, slope, witness):
    low_period = witness["low_period"]
    fixed_length = low_period["fixed_length"]
    exact_period_two_length = low_period["period_two_exact_length"]
    quotient_rank = low_period["fixed_length"] ** 3
    invariant_power = witness["normalized_scaling"]["minimal_invariant_power"]
    pointwise = [
        {"exponent": 0, "coefficient": constant},
        {"exponent": 3, "coefficient": slope},
    ]
    return {
        "cyclewise_moment": {
            "variable": "L",
            "terms": [
                {"exponent": 0, "coefficient": constant // 3},
                {"exponent": 3, "coefficient": slope // 3},
            ],
        },
        "exact_period_three_length": quotient_rank - fixed_length,
        "fiber_normal_form": "(x^2-L)^2",
        "fixed_length": fixed_length,
        "fixed_moment": witness["fixed_moment"]["fixed_moment"],
        "normalized_conjugacy_coordinate": "L^" + str(invariant_power),
        "period_one_characteristic_polynomial": "T^" + str(low_period["fixed_formal_zero_count"]),
        "period_two_characteristic_polynomial": "(T-2)^" + str(exact_period_two_length),
        "pointwise_moment": {"variable": "L", "terms": pointwise},
        "quotient_rank": quotient_rank,
    }


def run_science(definitions):
    if type(definitions) is not dict:
        raise TypeError("R definitions object")
    if definitions.get("candidate_id") != "henon_period3_residue_v1":
        raise ValueError("R candidate identity")
    if definitions.get("registered_coefficient_indices") != [8, 9]:
        raise ValueError("R registered tuple is immutable")
    quartic = quartic_residue_witness()
    diagnostics = []
    private_diagnostics = []
    for index in (8, 9):
        record = _r_registered_collapsed_diagnostic(index)
        diagnostics.append({"index": index, "final_integer": record["final_integer"]})
        private_diagnostics.append(record)
    return {
        "public_quartic": _r_public_quartic_record(
            quartic["constant_top_coefficient"], quartic["direct_slope"], quartic
        ),
        "public_coefficient_diagnostics": diagnostics,
        "private_witness": {
            "schema": "HENON_PERIOD3_TRACK_R_PRIVATE_WITNESS_V1",
            "track": "R",
            "quartic": quartic,
            "coefficient_diagnostics": private_diagnostics,
            "registered_engine_index_evaluation_count": 2,
            "full_high_degree_residue_count": 0,
            "historical_result_access_count": 0,
        },
    }
