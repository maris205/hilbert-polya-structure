#!/usr/bin/env python3
"""Neutral exact affine-semigroup and diagonal-operator machinery."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from typing import Iterable, Iterator, Sequence


State = tuple[int, int]
Token = str
Polynomial = list[Fraction]

TOKENS: tuple[Token, ...] = ("U+", "V+", "U-", "V-")
INVERSE: dict[Token, Token] = {
    "U+": "U-",
    "U-": "U+",
    "V+": "V-",
    "V-": "V+",
}


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def fraction_list(values: Iterable[Fraction]) -> list[str]:
    return [fraction_text(value) for value in values]


def state_text(state: State) -> str:
    return f"{state[0]}:{state[1]}"


def edge_text(left: State, token: Token, right: State) -> str:
    return f"{state_text(left)}|{token}|{state_text(right)}"


def height(r: int, state: State) -> int:
    """Authority height h_r(b,k)=b+r^k from the frozen source lock."""
    return state[0] + r ** state[1]


def step(r: int, state: State, token: Token) -> State | None:
    b, k = state
    scale = r**k
    if token == "U+":
        return b + scale, k
    if token == "V+":
        return b, k + 1
    if token == "U-":
        return (b - scale, k) if b >= scale else None
    if token == "V-":
        return (b, k - 1) if k >= 1 else None
    raise ValueError(f"unknown token: {token}")


def path_states(r: int, base: State, word: Sequence[Token]) -> tuple[State, ...] | None:
    states = [base]
    current = base
    for token in word:
        current = step(r, current, token)
        if current is None:
            return None
        states.append(current)
    return tuple(states)


def edge_itinerary(r: int, base: State, word: Sequence[Token]) -> tuple[str, ...] | None:
    states = path_states(r, base, word)
    if states is None:
        return None
    return tuple(edge_text(states[index], token, states[index + 1]) for index, token in enumerate(word))


def freely_reduced(word: Sequence[Token]) -> bool:
    return all(word[index + 1] != INVERSE[word[index]] for index in range(len(word) - 1))


def cyclically_nonbacktracking(word: Sequence[Token]) -> bool:
    return bool(word) and freely_reduced(word) and word[0] != INVERSE[word[-1]]


def proper_divisors(value: int) -> Iterator[int]:
    for item in range(1, value):
        if value % item == 0:
            yield item


def primitive_closed_word(r: int, base: State, word: Sequence[Token]) -> bool:
    states = path_states(r, base, word)
    if states is None or states[-1] != base or not word:
        return False
    items = tuple(word)
    for period in proper_divisors(len(items)):
        if items == items[:period] * (len(items) // period):
            prefix_states = path_states(r, base, items[:period])
            if prefix_states is not None and prefix_states[-1] == base:
                return False
    return True


def relation_word(r: int) -> tuple[Token, ...]:
    return ("V+", "U+", "V-") + ("U-",) * r


def relation_witness(r: int, base: State, a: Fraction, b: Fraction) -> dict[str, object]:
    word = relation_word(r)
    states = path_states(r, base, word)
    if states is None:
        raise AssertionError("affine relation must be admissible")
    left_path = path_states(r, base, ("V+", "U+"))
    right_path = path_states(r, base, ("U+",) * r + ("V+",))
    if left_path is None or right_path is None:
        raise AssertionError
    internal_left = set(left_path[1:-1])
    internal_right = set(right_path[1:-1])
    weight = a ** (r + 1) * b**2
    return {
        "r": r,
        "base": state_text(base),
        "word": list(word),
        "word_text": " ".join(word),
        "length": len(word),
        "expected_length": r + 3,
        "states": [state_text(state) for state in states],
        "closed": states[-1] == base,
        "admissible": True,
        "cyclically_nonbacktracking": cyclically_nonbacktracking(word),
        "primitive": primitive_closed_word(r, base, word),
        "left_endpoint": state_text(left_path[-1]),
        "right_endpoint": state_text(right_path[-1]),
        "common_endpoint": left_path[-1] == right_path[-1],
        "internally_disjoint_positive_paths": not bool(internal_left & internal_right),
        "weight": fraction_text(weight),
        "expected_weight": f"a^{r + 1}*b^2",
        "a": fraction_text(a),
        "b": fraction_text(b),
    }


def word_census(r: int, base: State, max_length: int) -> list[dict[str, object]]:
    target = relation_word(r)
    rows: list[dict[str, object]] = []
    for length in range(1, max_length + 1):
        counts = {
            "total_words": 0,
            "admissible_words": 0,
            "closed_words": 0,
            "freely_reduced_closed_words": 0,
            "cyclic_nb_closed_words": 0,
            "primitive_cyclic_nb_closed_words": 0,
        }
        target_seen = False
        for word in product(TOKENS, repeat=length):
            counts["total_words"] += 1
            states = path_states(r, base, word)
            if states is None:
                continue
            counts["admissible_words"] += 1
            if states[-1] != base:
                continue
            counts["closed_words"] += 1
            if freely_reduced(word):
                counts["freely_reduced_closed_words"] += 1
            if cyclically_nonbacktracking(word):
                counts["cyclic_nb_closed_words"] += 1
                if primitive_closed_word(r, base, word):
                    counts["primitive_cyclic_nb_closed_words"] += 1
            if word == target:
                target_seen = True
        rows.append(
            {
                "r": r,
                "base_b": base[0],
                "base_k": base[1],
                "length": length,
                **counts,
                "relation_word_seen": target_seen,
            }
        )
    return rows


def positive_edges(r: int, b_max: int, k_max: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for b in range(b_max + 1):
        for k in range(k_max + 1):
            origin = (b, k)
            for token in ("U+", "V+"):
                target = step(r, origin, token)
                if target is None:
                    raise AssertionError
                expected = r**k if token == "U+" else (r - 1) * r**k
                rows.append(
                    {
                        "r": r,
                        "origin_b": b,
                        "origin_k": k,
                        "token": token,
                        "target_b": target[0],
                        "target_k": target[1],
                        "height_before": height(r, origin),
                        "height_after": height(r, target),
                        "height_increment": height(r, target) - height(r, origin),
                        "expected_increment": expected,
                        "strict_increase": height(r, target) > height(r, origin),
                        "target_inside_window": target[0] <= b_max and target[1] <= k_max,
                    }
                )
    return rows


def backtrack_rows(edges: Sequence[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for index, edge in enumerate(edges):
        token = str(edge["token"])
        rows.append(
            {
                "edge_id": index,
                "r": edge["r"],
                "origin_b": edge["origin_b"],
                "origin_k": edge["origin_k"],
                "token_forward": token,
                "target_b": edge["target_b"],
                "target_k": edge["target_k"],
                "token_reverse": INVERSE[token],
                "length": 2,
                "closed": True,
                "primitive": True,
                "immediate_backtrack": True,
                "hashimoto_allowed": False,
            }
        )
    return rows


def quotient_multipliers(r: int, q: int) -> tuple[int, ...]:
    if q < 1:
        raise ValueError
    seen: list[int] = []
    value = 1 % q
    while value not in seen:
        seen.append(value)
        value = (value * r) % q
    return tuple(seen)


def quotient_u(state: State, q: int) -> State:
    b, a = state
    return (b + a) % q, a


def quotient_v(state: State, r: int, q: int) -> State:
    b, a = state
    return b, (r * a) % q


def quotient_path(start: State, r: int, q: int, tokens: Sequence[Token]) -> tuple[State, ...]:
    states = [start]
    current = start
    for token in tokens:
        if token == "U+":
            current = quotient_u(current, q)
        elif token == "V+":
            current = quotient_v(current, r, q)
        else:
            raise ValueError("positive quotient paths only")
        states.append(current)
    return tuple(states)


def quotient_record(r: int, q: int) -> dict[str, object]:
    start = (0, 1 % q)
    left = quotient_path(start, r, q, ("V+", "U+"))
    right = quotient_path(start, r, q, ("U+",) * r + ("V+",))
    u_cycle = quotient_path(start, r, q, ("U+",) * q)
    polygon_vertices = list(left) + list(reversed(right[:-1]))
    if polygon_vertices[-1] != start:
        raise AssertionError
    before_close = polygon_vertices[:-1]
    vertex_simple = len(before_close) == len(set(before_close))
    word = relation_word(r)
    return {
        "r": r,
        "q": q,
        "multiplier_count": len(quotient_multipliers(r, q)),
        "state_count": q * len(quotient_multipliers(r, q)),
        "relation_left_endpoint": state_text(left[-1]),
        "relation_right_endpoint": state_text(right[-1]),
        "relation_preserved": left[-1] == right[-1],
        "relation_word_length": len(word),
        "relation_cyclically_nonbacktracking": cyclically_nonbacktracking(word),
        "relation_label_primitive": True,
        "relation_polygon_vertex_simple": vertex_simple,
        "u_q_closed": u_cycle[-1] == start,
        "u_q_length": q,
        "u_q_primitive_or_loop": True,
        "small_modulus": q <= r,
        "required_2_2_degeneracy": r == 2 and q == 2 and not vertex_simple,
    }


def polynomial_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    output = [Fraction(0, 1)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] += a * b
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def diagonal_values(beta: int, cutoff: int) -> list[Fraction]:
    return [Fraction(1, n**beta) for n in range(1, cutoff + 1)]


def trace_powers(values: Sequence[Fraction], maximum: int) -> list[Fraction]:
    return [sum((value**power for value in values), Fraction(0, 1)) for power in range(1, maximum + 1)]


def determinant_product(values: Sequence[Fraction]) -> Polynomial:
    result = [Fraction(1, 1)]
    for value in values:
        result = polynomial_multiply(result, [Fraction(1, 1), -value])
    return result


def determinant_newton(power_sums: Sequence[Fraction]) -> Polynomial:
    coefficients = [Fraction(1, 1)]
    for degree in range(1, len(power_sums) + 1):
        total = sum(
            (coefficients[degree - index] * power_sums[index - 1] for index in range(1, degree + 1)),
            Fraction(0, 1),
        )
        coefficients.append(-total / degree)
    return coefficients


def polynomial_evaluate(poly: Sequence[Fraction], value: Fraction) -> Fraction:
    output = Fraction(0, 1)
    for coefficient in reversed(poly):
        output = output * value + coefficient
    return output


def bc_fixture(beta: int, cutoff: int, log_power_count: int) -> dict[str, object]:
    values = diagonal_values(beta, cutoff)
    powers = trace_powers(values, cutoff)
    determinant = determinant_product(values)
    newton = determinant_newton(powers)
    return {
        "beta": beta,
        "cutoff": cutoff,
        "diagonal": fraction_list(values),
        "trace": fraction_text(powers[0]),
        "trace_powers_full": fraction_list(powers),
        "negative_log_coefficients": fraction_list(
            powers[index - 1] / index for index in range(1, log_power_count + 1)
        ),
        "determinant_coefficients": fraction_list(determinant),
        "newton_coefficients": fraction_list(newton),
        "determinant_newton_equal": determinant == newton,
        "determinant_at_z_one": fraction_text(polynomial_evaluate(determinant, Fraction(1, 1))),
        "eigenvalue_one_present": values[0] == 1,
        "finite_diagonal_fixture_only": True,
    }


def pairwise_disjoint(items: Sequence[Sequence[str]]) -> bool:
    sets = [set(item) for item in items]
    return all(not (sets[i] & sets[j]) for i in range(len(sets)) for j in range(i + 1, len(sets)))


def operator_certificates(r: int, count: int, a: Fraction, b: Fraction) -> dict[str, object]:
    plus_supports: list[list[str]] = []
    symmetric_supports: list[list[str]] = []
    hashimoto_supports: list[list[str]] = []
    relation_supports: list[list[str]] = []
    for j in range(count):
        plus_supports.append([state_text((r**j, j)), state_text((0, j + 1))])
        level = 4 * (j + 1)
        symmetric_supports.append(
            [state_text((r**level, level)), state_text((0, level + 1)), state_text((0, level - 1))]
        )
        hashimoto_supports.append(
            [f"{state_text((0, j + 1))}|U+", f"{state_text((0, j + 1))}|V+"]
        )
        relation_supports.append([f"level:{2*j}", f"level:{2*j+1}"])
    return {
        "r": r,
        "a": fraction_text(a),
        "b": fraction_text(b),
        "sequence_count": count,
        "a_plus_bound": fraction_text(a + b),
        "symmetric_bound": fraction_text(2 * (a + b)),
        "hashimoto_bound": fraction_text(3 * max(a, b)),
        "a_plus_norm_squared": fraction_text(a * a + b * b),
        "symmetric_norm_squared": fraction_text(a * a + 2 * b * b),
        "hashimoto_lower_norm_squared": fraction_text(a * a + b * b),
        "a_plus_supports": plus_supports,
        "symmetric_supports": symmetric_supports,
        "hashimoto_supports": hashimoto_supports,
        "relation_copy_supports": relation_supports,
        "a_plus_pairwise_disjoint": pairwise_disjoint(plus_supports),
        "symmetric_pairwise_disjoint": pairwise_disjoint(symmetric_supports),
        "hashimoto_pairwise_disjoint": pairwise_disjoint(hashimoto_supports),
        "relation_copies_pairwise_disjoint": pairwise_disjoint(relation_supports),
        "finite_window_certificate_only": True,
        "analytic_noncompactness_proof_owned_by_math_lock": True,
    }


def commutation_record(left: int, right: int) -> dict[str, object]:
    word = ("D_A+", "D_B+", "D_A-", "D_B-")
    return {
        "left_multiplier": left,
        "right_multiplier": right,
        "forward_product": left * right,
        "reverse_product": right * left,
        "common_endpoint": left * right == right * left,
        "word": list(word),
        "length": 4,
        "cyclically_nonbacktracking": True,
        "primitive_label_word": left != right,
        "requires_both_dilation_generators": True,
    }


def monoid_relation_record(name: str, left_u_count: int, right_u_count: int) -> dict[str, object]:
    word = ("V+",) + ("U+",) * left_u_count + ("V-",) + ("U-",) * right_u_count
    return {
        "name": name,
        "presentation": f"V U^{left_u_count} = U^{right_u_count} V",
        "left_u_count": left_u_count,
        "right_u_count": right_u_count,
        "relation_word": list(word),
        "length": len(word),
        "cyclically_nonbacktracking": cyclically_nonbacktracking(word),
        "primitive_label_word": True,
        "arithmetic_acceptance_labels": False,
    }


def full_monoid_boundary() -> dict[str, object]:
    return {
        "object": "N_0 semidirect N^times right Cayley graph",
        "generator_rule": "U together with D_n for every n>=2",
        "outdegree": "countably_infinite",
        "unweighted_basis_image_squared_norm": "infinity",
        "natural_unweighted_l2_adjacency_defined": False,
        "finite_census_performed": False,
        "status": "THEOREM_ONLY_NO_FINITE_AUDIT_PRETENSE",
    }
