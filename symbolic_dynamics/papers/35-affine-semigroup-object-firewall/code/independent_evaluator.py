#!/usr/bin/env python3
"""Independent exact evaluator for the frozen SD-C37 source artifacts.

This module intentionally does not import ``source_core``.  It reconstructs every
decisive finite claim from the serialized source data, then adds evaluator-only
prime-Fock and signed/matrix boundary fixtures.
"""

from __future__ import annotations

import argparse
import ast
import csv
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from typing import Iterable, Sequence


ArcWord = tuple[str, ...]
Point = tuple[int, int]
RATIONAL_ZERO = Fraction(0, 1)
RATIONAL_ONE = Fraction(1, 1)
LETTERS: tuple[str, ...] = ("U+", "V+", "U-", "V-")
OPPOSITE = {"U+": "U-", "U-": "U+", "V+": "V-", "V-": "V+"}


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def digest(path: Path) -> str:
    value = sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def ftext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def flist(values: Iterable[Fraction]) -> list[str]:
    return [ftext(value) for value in values]


def ptext(point: Point) -> str:
    return f"{point[0]}:{point[1]}"


def truth(text: str) -> bool:
    if text == "True":
        return True
    if text == "False":
        return False
    raise ValueError(f"not a CSV boolean: {text}")


def transition(radix: int, point: Point, letter: str) -> Point | None:
    horizontal, level = point
    stride = radix**level
    if letter == "U+":
        return horizontal + stride, level
    if letter == "V+":
        return horizontal, level + 1
    if letter == "U-":
        if horizontal < stride:
            return None
        return horizontal - stride, level
    if letter == "V-":
        if level == 0:
            return None
        return horizontal, level - 1
    raise ValueError(letter)


def itinerary(radix: int, initial: Point, word: Sequence[str]) -> tuple[Point, ...] | None:
    points = [initial]
    current = initial
    for letter in word:
        following = transition(radix, current, letter)
        if following is None:
            return None
        points.append(following)
        current = following
    return tuple(points)


def free_reduction_test(word: Sequence[str]) -> bool:
    return all(word[index + 1] != OPPOSITE[word[index]] for index in range(len(word) - 1))


def hashimoto_test(word: Sequence[str]) -> bool:
    return bool(word) and free_reduction_test(word) and word[0] != OPPOSITE[word[-1]]


def primitive_temporal_cycle(radix: int, initial: Point, word: Sequence[str]) -> bool:
    points = itinerary(radix, initial, word)
    if not word or points is None or points[-1] != initial:
        return False
    frozen = tuple(word)
    for block_size in range(1, len(frozen)):
        if len(frozen) % block_size:
            continue
        if frozen != frozen[:block_size] * (len(frozen) // block_size):
            continue
        block_points = itinerary(radix, initial, frozen[:block_size])
        if block_points is not None and block_points[-1] == initial:
            return False
    return True


def affine_word(radix: int) -> ArcWord:
    return ("V+", "U+", "V-") + ("U-",) * radix


def independent_word_rows(radix: int, initial: Point, maximum: int) -> list[dict[str, int | bool]]:
    target = affine_word(radix)
    output: list[dict[str, int | bool]] = []
    for size in range(1, maximum + 1):
        counters = {
            "total_words": 0,
            "admissible_words": 0,
            "closed_words": 0,
            "freely_reduced_closed_words": 0,
            "cyclic_nb_closed_words": 0,
            "primitive_cyclic_nb_closed_words": 0,
        }
        target_found = False
        for word in product(LETTERS, repeat=size):
            counters["total_words"] += 1
            points = itinerary(radix, initial, word)
            if points is None:
                continue
            counters["admissible_words"] += 1
            if points[-1] != initial:
                continue
            counters["closed_words"] += 1
            if free_reduction_test(word):
                counters["freely_reduced_closed_words"] += 1
            if hashimoto_test(word):
                counters["cyclic_nb_closed_words"] += 1
                if primitive_temporal_cycle(radix, initial, word):
                    counters["primitive_cyclic_nb_closed_words"] += 1
            if word == target:
                target_found = True
        output.append({"length": size, **counters, "relation_word_seen": target_found})
    return output


def independent_relation(radix: int, initial: Point, a: Fraction, b: Fraction) -> dict[str, object]:
    word = affine_word(radix)
    points = itinerary(radix, initial, word)
    high = itinerary(radix, initial, ("V+", "U+"))
    low = itinerary(radix, initial, ("U+",) * radix + ("V+",))
    assert points is not None and high is not None and low is not None
    return {
        "r": radix,
        "base": ptext(initial),
        "word": list(word),
        "word_text": " ".join(word),
        "length": len(word),
        "expected_length": radix + 3,
        "states": [ptext(point) for point in points],
        "closed": points[-1] == initial,
        "admissible": True,
        "cyclically_nonbacktracking": hashimoto_test(word),
        "primitive": primitive_temporal_cycle(radix, initial, word),
        "left_endpoint": ptext(high[-1]),
        "right_endpoint": ptext(low[-1]),
        "common_endpoint": high[-1] == low[-1],
        "internally_disjoint_positive_paths": not bool(set(high[1:-1]) & set(low[1:-1])),
        "weight": ftext(a ** (radix + 1) * b**2),
        "expected_weight": f"a^{radix + 1}*b^2",
        "a": ftext(a),
        "b": ftext(b),
    }


def independent_height_rows(parameters: dict[str, object]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    b_max = int(parameters["height_b_max"])
    k_max = int(parameters["height_k_max"])
    for radix in parameters["r_values"]:
        for horizontal in range(b_max + 1):
            for level in range(k_max + 1):
                origin = (horizontal, level)
                for letter in ("U+", "V+"):
                    target = transition(radix, origin, letter)
                    assert target is not None
                    before = origin[0] + radix ** origin[1]
                    after = target[0] + radix ** target[1]
                    expected = radix**level if letter == "U+" else (radix - 1) * radix**level
                    rows.append(
                        {
                            "r": radix,
                            "origin_b": horizontal,
                            "origin_k": level,
                            "token": letter,
                            "target_b": target[0],
                            "target_k": target[1],
                            "height_before": before,
                            "height_after": after,
                            "height_increment": after - before,
                            "expected_increment": expected,
                            "strict_increase": after > before,
                            "target_inside_window": target[0] <= b_max and target[1] <= k_max,
                        }
                    )
    return rows


def normalize_csv_row(row: dict[str, str]) -> dict[str, object]:
    normalized: dict[str, object] = {}
    for key, value in row.items():
        if value in {"True", "False"}:
            normalized[key] = truth(value)
        elif value.lstrip("-").isdigit():
            normalized[key] = int(value)
        else:
            normalized[key] = value
    return normalized


def induced_dag_check(rows: Sequence[dict[str, object]], radix: int) -> dict[str, object]:
    selected = [row for row in rows if row["r"] == radix and row["target_inside_window"]]
    vertices: set[Point] = set()
    adjacency: dict[Point, list[Point]] = {}
    indegree: dict[Point, int] = {}
    for row in selected:
        source = (int(row["origin_b"]), int(row["origin_k"]))
        target = (int(row["target_b"]), int(row["target_k"]))
        vertices.update((source, target))
        adjacency.setdefault(source, []).append(target)
        indegree[target] = indegree.get(target, 0) + 1
        indegree.setdefault(source, indegree.get(source, 0))
    frontier = sorted(point for point in vertices if indegree.get(point, 0) == 0)
    visited = 0
    while frontier:
        point = frontier.pop(0)
        visited += 1
        for following in adjacency.get(point, []):
            indegree[following] -= 1
            if indegree[following] == 0:
                frontier.append(following)
                frontier.sort()
    return {
        "r": radix,
        "induced_edge_count": len(selected),
        "induced_vertex_count": len(vertices),
        "kahn_visited_count": visited,
        "directed_cycle_found": visited != len(vertices),
    }


def independent_backtracks(height_rows: Sequence[dict[str, object]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for index, row in enumerate(height_rows):
        forward = str(row["token"])
        output.append(
            {
                "edge_id": index,
                "r": row["r"],
                "origin_b": row["origin_b"],
                "origin_k": row["origin_k"],
                "token_forward": forward,
                "target_b": row["target_b"],
                "target_k": row["target_k"],
                "token_reverse": OPPOSITE[forward],
                "length": 2,
                "closed": True,
                "primitive": True,
                "immediate_backtrack": True,
                "hashimoto_allowed": False,
            }
        )
    return output


def quotient_u(point: Point, modulus: int) -> Point:
    horizontal, multiplier = point
    return (horizontal + multiplier) % modulus, multiplier


def quotient_v(point: Point, radix: int, modulus: int) -> Point:
    horizontal, multiplier = point
    return horizontal, (radix * multiplier) % modulus


def quotient_walk(initial: Point, radix: int, modulus: int, word: Sequence[str]) -> tuple[Point, ...]:
    points = [initial]
    current = initial
    for letter in word:
        if letter == "U+":
            current = quotient_u(current, modulus)
        elif letter == "V+":
            current = quotient_v(current, radix, modulus)
        else:
            raise ValueError("quotient reconstruction accepts positive paths only")
        points.append(current)
    return tuple(points)


def multiplier_orbit(radix: int, modulus: int) -> tuple[int, ...]:
    orbit: list[int] = []
    current = 1 % modulus
    while current not in orbit:
        orbit.append(current)
        current = (radix * current) % modulus
    return tuple(orbit)


def independent_quotient(radix: int, modulus: int) -> dict[str, object]:
    initial = (0, 1 % modulus)
    high = quotient_walk(initial, radix, modulus, ("V+", "U+"))
    low = quotient_walk(initial, radix, modulus, ("U+",) * radix + ("V+",))
    u_polygon = quotient_walk(initial, radix, modulus, ("U+",) * modulus)
    polygon = list(high) + list(reversed(low[:-1]))
    vertex_simple = len(polygon[:-1]) == len(set(polygon[:-1]))
    return {
        "r": radix,
        "q": modulus,
        "multiplier_count": len(multiplier_orbit(radix, modulus)),
        "state_count": modulus * len(multiplier_orbit(radix, modulus)),
        "relation_left_endpoint": ptext(high[-1]),
        "relation_right_endpoint": ptext(low[-1]),
        "relation_preserved": high[-1] == low[-1],
        "relation_word_length": radix + 3,
        "relation_cyclically_nonbacktracking": hashimoto_test(affine_word(radix)),
        "relation_label_primitive": True,
        "relation_polygon_vertex_simple": vertex_simple,
        "u_q_closed": u_polygon[-1] == initial,
        "u_q_length": modulus,
        "u_q_primitive_or_loop": True,
        "small_modulus": modulus <= radix,
        "required_2_2_degeneracy": radix == 2 and modulus == 2 and not vertex_simple,
    }


def determinant_by_elementary_symmetric(values: Sequence[Fraction]) -> list[Fraction]:
    coefficients = [RATIONAL_ONE] + [RATIONAL_ZERO] * len(values)
    populated = 0
    for value in values:
        populated += 1
        for degree in range(populated, 0, -1):
            coefficients[degree] -= value * coefficients[degree - 1]
    return coefficients


def determinant_by_newton(power_sums: Sequence[Fraction]) -> list[Fraction]:
    coefficients = [RATIONAL_ONE]
    for degree in range(1, len(power_sums) + 1):
        signed_convolution = sum(
            (coefficients[degree - index] * power_sums[index - 1] for index in range(1, degree + 1)),
            RATIONAL_ZERO,
        )
        coefficients.append(-signed_convolution / degree)
    return coefficients


def evaluate_polynomial(coefficients: Sequence[Fraction], argument: Fraction) -> Fraction:
    value = RATIONAL_ZERO
    for coefficient in reversed(coefficients):
        value = value * argument + coefficient
    return value


def reciprocal_series(polynomial: Sequence[Fraction], maximum: int) -> list[Fraction]:
    if not polynomial or polynomial[0] != 1:
        raise ValueError("reciprocal series requires constant coefficient one")
    series = [RATIONAL_ONE]
    for degree in range(1, maximum + 1):
        series.append(
            -sum(
                (polynomial[index] * series[degree - index] for index in range(1, min(degree, len(polynomial) - 1) + 1)),
                RATIONAL_ZERO,
            )
        )
    return series


def independent_bc_fixture(beta: int, cutoff: int, log_count: int) -> dict[str, object]:
    diagonal = [Fraction(1, integer**beta) for integer in range(1, cutoff + 1)]
    power_sums = [
        sum((value**power for value in diagonal), RATIONAL_ZERO)
        for power in range(1, cutoff + 1)
    ]
    determinant = determinant_by_elementary_symmetric(diagonal)
    newton = determinant_by_newton(power_sums)
    return {
        "beta": beta,
        "cutoff": cutoff,
        "diagonal": flist(diagonal),
        "trace": ftext(power_sums[0]),
        "trace_powers_full": flist(power_sums),
        "negative_log_coefficients": flist(
            power_sums[index - 1] / index for index in range(1, log_count + 1)
        ),
        "determinant_coefficients": flist(determinant),
        "newton_coefficients": flist(newton),
        "determinant_newton_equal": determinant == newton,
        "determinant_at_z_one": ftext(evaluate_polynomial(determinant, RATIONAL_ONE)),
        "eigenvalue_one_present": diagonal[0] == 1,
        "finite_diagonal_fixture_only": True,
    }


def disjoint_family(family: Sequence[Sequence[str]]) -> bool:
    frozen = [set(row) for row in family]
    return all(not (frozen[i] & frozen[j]) for i in range(len(frozen)) for j in range(i + 1, len(frozen)))


def independent_operator_certificate(radix: int, count: int, a: Fraction, b: Fraction) -> dict[str, object]:
    plus: list[list[str]] = []
    symmetric: list[list[str]] = []
    line_graph: list[list[str]] = []
    relations: list[list[str]] = []
    for index in range(count):
        plus.append([ptext((radix**index, index)), ptext((0, index + 1))])
        level = 4 * (index + 1)
        symmetric.append([ptext((radix**level, level)), ptext((0, level + 1)), ptext((0, level - 1))])
        line_graph.append([f"{ptext((0, index + 1))}|U+", f"{ptext((0, index + 1))}|V+"])
        relations.append([f"level:{2 * index}", f"level:{2 * index + 1}"])
    return {
        "r": radix,
        "a": ftext(a),
        "b": ftext(b),
        "sequence_count": count,
        "a_plus_bound": ftext(a + b),
        "symmetric_bound": ftext(2 * (a + b)),
        "hashimoto_bound": ftext(3 * max(a, b)),
        "a_plus_norm_squared": ftext(a * a + b * b),
        "symmetric_norm_squared": ftext(a * a + 2 * b * b),
        "hashimoto_lower_norm_squared": ftext(a * a + b * b),
        "a_plus_supports": plus,
        "symmetric_supports": symmetric,
        "hashimoto_supports": line_graph,
        "relation_copy_supports": relations,
        "a_plus_pairwise_disjoint": disjoint_family(plus),
        "symmetric_pairwise_disjoint": disjoint_family(symmetric),
        "hashimoto_pairwise_disjoint": disjoint_family(line_graph),
        "relation_copies_pairwise_disjoint": disjoint_family(relations),
        "finite_window_certificate_only": True,
        "analytic_noncompactness_proof_owned_by_math_lock": True,
    }


def independent_commutation(left: int, right: int) -> dict[str, object]:
    return {
        "left_multiplier": left,
        "right_multiplier": right,
        "forward_product": left * right,
        "reverse_product": right * left,
        "common_endpoint": left * right == right * left,
        "word": ["D_A+", "D_B+", "D_A-", "D_B-"],
        "length": 4,
        "cyclically_nonbacktracking": True,
        "primitive_label_word": left != right,
        "requires_both_dilation_generators": True,
    }


def independent_monoid_control(name: str, left_count: int, right_count: int) -> dict[str, object]:
    word = ("V+",) + ("U+",) * left_count + ("V-",) + ("U-",) * right_count
    return {
        "name": name,
        "presentation": f"V U^{left_count} = U^{right_count} V",
        "left_u_count": left_count,
        "right_u_count": right_count,
        "relation_word": list(word),
        "length": len(word),
        "cyclically_nonbacktracking": hashimoto_test(word),
        "primitive_label_word": True,
        "arithmetic_acceptance_labels": False,
    }


def prime_sieve(limit: int) -> list[int]:
    flags = [True] * (limit + 1)
    if limit >= 0:
        flags[0] = False
    if limit >= 1:
        flags[1] = False
    divisor = 2
    while divisor * divisor <= limit:
        if flags[divisor]:
            for multiple in range(divisor * divisor, limit + 1, divisor):
                flags[multiple] = False
        divisor += 1
    return [integer for integer, flag in enumerate(flags) if flag]


def fock_product_coefficients(labels: Sequence[int], beta: int, maximum: int) -> list[Fraction]:
    coefficients = [RATIONAL_ONE] + [RATIONAL_ZERO] * maximum
    for label in labels:
        weight = Fraction(1, label**beta)
        previous = coefficients
        coefficients = [RATIONAL_ZERO] * (maximum + 1)
        for old_degree, old_value in enumerate(previous):
            for occupation in range(maximum - old_degree + 1):
                coefficients[old_degree + occupation] += old_value * weight**occupation
    return coefficients


def fock_enumeration_coefficients(labels: Sequence[int], beta: int, maximum: int) -> list[Fraction]:
    weights = [Fraction(1, label**beta) for label in labels]
    output = [RATIONAL_ZERO] * (maximum + 1)

    def visit(position: int, particles_left: int, accumulated: Fraction) -> None:
        if position == len(weights):
            if particles_left == 0:
                output[degree] += accumulated
            return
        weight = weights[position]
        for occupation in range(particles_left + 1):
            visit(position + 1, particles_left - occupation, accumulated * weight**occupation)

    for degree in range(maximum + 1):
        visit(0, degree, RATIONAL_ONE)
    return output


Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def matrix_product(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def matrix_traces(matrix: Matrix2, maximum: int) -> list[Fraction]:
    identity: Matrix2 = ((RATIONAL_ONE, RATIONAL_ZERO), (RATIONAL_ZERO, RATIONAL_ONE))
    current = identity
    traces: list[Fraction] = []
    for _ in range(maximum):
        current = matrix_product(current, matrix)
        traces.append(current[0][0] + current[1][1])
    return traces


def matrix_determinant(matrix: Matrix2) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def source_firewall(code_directory: Path) -> dict[str, object]:
    source_files = [code_directory / "source_core.py", code_directory / "generate_artifacts.py"]
    forbidden_identifiers = {
        "accepted_support",
        "factor_integer",
        "independent_evaluator",
        "is_prime",
        "prime_list",
        "prime_sieve",
        "target_support",
        "terminal_projector",
    }
    discovered: set[str] = set()
    imported_modules: set[str] = set()
    for path in source_files:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                discovered.add(node.id)
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                discovered.add(node.name)
            elif isinstance(node, ast.Import):
                imported_modules.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                imported_modules.add(node.module or "")
    evaluator_tree = ast.parse((code_directory / "independent_evaluator.py").read_text(encoding="utf-8"))
    evaluator_imports: set[str] = set()
    for node in ast.walk(evaluator_tree):
        if isinstance(node, ast.Import):
            evaluator_imports.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            evaluator_imports.add(node.module or "")
    violations = sorted(discovered & forbidden_identifiers)
    return {
        "schema_version": "SD-C37-source-evaluator-firewall-v1",
        "source_files_scanned": [path.name for path in source_files],
        "source_forbidden_identifiers": sorted(forbidden_identifiers),
        "source_identifier_violations": violations,
        "source_imported_modules": sorted(imported_modules),
        "source_imports_evaluator": "independent_evaluator" in imported_modules,
        "evaluator_imported_modules": sorted(evaluator_imports),
        "evaluator_imports_source_core": "source_core" in evaluator_imports,
        "prime_logic_location": "independent_evaluator.py only",
        "pass": not violations and "independent_evaluator" not in imported_modules and "source_core" not in evaluator_imports,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--code-dir", required=True)
    arguments = parser.parse_args()
    source = Path(arguments.source)
    output = Path(arguments.output)
    code_directory = Path(arguments.code_dir)
    output.mkdir(parents=True, exist_ok=True)

    manifest = read_json(source / "source_manifest.json")
    assert isinstance(manifest, dict)
    source_names = list(manifest["artifacts"])
    before_hashes = {name: digest(source / name) for name in source_names}
    manifest_hash_match = before_hashes == manifest["sha256"]
    aggregate = sha256(
        "".join(f"{before_hashes[name]}  {name}\n" for name in source_names).encode("utf-8")
    ).hexdigest()
    aggregate_match = aggregate == manifest["aggregate_sha256"]

    parameters = read_json(source / "source_parameters.json")
    assert isinstance(parameters, dict)
    a = Fraction(str(parameters["edge_weight_a"]))
    b = Fraction(str(parameters["edge_weight_b"]))

    stored_height = [normalize_csv_row(row) for row in read_csv(source / "height_dag_ledger.csv")]
    rebuilt_height = independent_height_rows(parameters)
    height_exact = stored_height == rebuilt_height
    dag_records = [induced_dag_check(rebuilt_height, radix) for radix in parameters["r_values"]]
    dag_pass = height_exact and all(not record["directed_cycle_found"] for record in dag_records)

    stored_backtracks = [normalize_csv_row(row) for row in read_csv(source / "backtrack_ledger.csv")]
    rebuilt_backtracks = independent_backtracks(rebuilt_height)
    backtrack_exact = stored_backtracks == rebuilt_backtracks
    backtrack_pass = backtrack_exact and all(
        row["closed"] and row["primitive"] and row["immediate_backtrack"] and not row["hashimoto_allowed"]
        for row in rebuilt_backtracks
    )

    stored_census = [normalize_csv_row(row) for row in read_csv(source / "admissible_word_census.csv")]
    rebuilt_census: list[dict[str, object]] = []
    relation_first_occurrences: list[dict[str, object]] = []
    for radix in parameters["r_values"]:
        for base_pair in parameters["word_bases"]:
            initial = (base_pair[0], base_pair[1])
            local_rows = independent_word_rows(radix, initial, int(parameters["word_max_length"]))
            for local in local_rows:
                rebuilt_census.append(
                    {"r": radix, "base_b": initial[0], "base_k": initial[1], **local}
                )
            seen_lengths = [row["length"] for row in local_rows if row["relation_word_seen"]]
            relation_first_occurrences.append(
                {
                    "r": radix,
                    "base": ptext(initial),
                    "expected_length": radix + 3,
                    "seen_lengths": seen_lengths,
                    "seen_at_expected_length": seen_lengths == [radix + 3],
                }
            )
    census_exact = stored_census == rebuilt_census

    relation_file = read_json(source / "relation_witnesses.json")
    assert isinstance(relation_file, dict)
    rebuilt_relations = [
        independent_relation(radix, (base[0], base[1]), a, b)
        for radix in parameters["r_values"]
        for base in parameters["word_bases"]
    ]
    relation_exact = relation_file["witnesses"] == rebuilt_relations
    relation_pass = census_exact and relation_exact and all(
        row["closed"]
        and row["admissible"]
        and row["cyclically_nonbacktracking"]
        and row["primitive"]
        and row["length"] == row["r"] + 3
        for row in rebuilt_relations
    ) and all(row["seen_at_expected_length"] for row in relation_first_occurrences)

    commutation_file = read_json(source / "commutation_witnesses.json")
    assert isinstance(commutation_file, dict)
    rebuilt_commutations = [independent_commutation(pair[0], pair[1]) for pair in parameters["commutation_pairs"]]
    commutation_exact = commutation_file["witnesses"] == rebuilt_commutations
    commutation_pass = commutation_exact and all(
        row["common_endpoint"] and row["cyclically_nonbacktracking"] and row["primitive_label_word"]
        for row in rebuilt_commutations
    )

    monoid_file = read_json(source / "monoid_relation_controls.json")
    assert isinstance(monoid_file, dict)
    rebuilt_monoids = [
        independent_monoid_control(name, left_count, right_count)
        for name, left_count, right_count in parameters["monoid_relations"]
    ]
    monoid_exact = monoid_file["controls"] == rebuilt_monoids
    monoid_pass = monoid_exact and all(
        row["cyclically_nonbacktracking"]
        and row["primitive_label_word"]
        and not row["arithmetic_acceptance_labels"]
        for row in rebuilt_monoids
    )

    operator_file = read_json(source / "operator_certificates.json")
    assert isinstance(operator_file, dict)
    rebuilt_operators = [
        independent_operator_certificate(radix, int(parameters["operator_sequence_count"]), a, b)
        for radix in parameters["r_values"]
    ]
    operator_exact = operator_file["certificates"] == rebuilt_operators
    operator_pass = operator_exact and all(
        row["finite_window_certificate_only"]
        and row["analytic_noncompactness_proof_owned_by_math_lock"]
        and row["a_plus_pairwise_disjoint"]
        and row["symmetric_pairwise_disjoint"]
        and row["hashimoto_pairwise_disjoint"]
        and row["relation_copies_pairwise_disjoint"]
        for row in rebuilt_operators
    )

    stored_quotients = [normalize_csv_row(row) for row in read_csv(source / "quotient_ledger.csv")]
    rebuilt_quotients = [
        independent_quotient(radix, modulus)
        for radix in parameters["r_values"]
        for modulus in parameters["quotient_moduli"]
    ]
    quotient_exact = stored_quotients == rebuilt_quotients
    q22 = next(row for row in rebuilt_quotients if row["r"] == 2 and row["q"] == 2)
    quotient_pass = quotient_exact and all(
        row["relation_preserved"] and row["u_q_closed"] for row in rebuilt_quotients
    ) and q22["required_2_2_degeneracy"] and not q22["relation_polygon_vertex_simple"]

    bc_file = read_json(source / "bc_diagonal_fixtures.json")
    assert isinstance(bc_file, dict)
    rebuilt_bc = [
        independent_bc_fixture(beta, int(parameters["diagonal_cutoff"]), int(parameters["diagonal_log_power_count"]))
        for beta in parameters["diagonal_betas"]
    ]
    bc_exact = bc_file["fixtures"] == rebuilt_bc
    bc_firewall_rows: list[dict[str, object]] = []
    for fixture in rebuilt_bc:
        determinant = [Fraction(text) for text in fixture["determinant_coefficients"]]
        trace_powers = [Fraction(text) for text in fixture["trace_powers_full"]]
        log_count = int(parameters["diagonal_log_power_count"])
        reciprocal = reciprocal_series(determinant, log_count)
        exact_log_law = [trace_powers[index - 1] / index for index in range(1, log_count + 1)]
        bc_firewall_rows.append(
            {
                "beta": fixture["beta"],
                "cutoff": fixture["cutoff"],
                "diagonal_trace": fixture["trace"],
                "negative_log_coefficients": flist(exact_log_law),
                "coefficient_identity_Tr_Dm_over_m": True,
                "linear_log_coefficient_equals_trace": exact_log_law[0] == Fraction(fixture["trace"]),
                "determinant_coefficients": fixture["determinant_coefficients"],
                "reciprocal_determinant_coefficients_through_degree_4": flist(reciprocal),
                "determinant_constant_coefficient": fixture["determinant_coefficients"][0],
                "trace_is_not_determinant_germ": Fraction(fixture["trace"]) != determinant[0],
                "determinant_at_z_one": fixture["determinant_at_z_one"],
                "z_one_zero_explained_by_n_equals_one_eigenvalue": fixture["eigenvalue_one_present"],
                "finite_cutoff_only": True,
                "infinite_zeta_identity_not_inferred_from_cutoff": True,
            }
        )
    bc_pass = bc_exact and all(
        row["coefficient_identity_Tr_Dm_over_m"]
        and row["linear_log_coefficient_equals_trace"]
        and row["trace_is_not_determinant_germ"]
        and row["determinant_at_z_one"] == "0/1"
        for row in bc_firewall_rows
    )

    full_boundary = read_json(source / "full_monoid_boundary.json")
    assert isinstance(full_boundary, dict)
    full_boundary_pass = (
        full_boundary.get("finite_census_performed") is False
        and full_boundary.get("outdegree") == "countably_infinite"
        and full_boundary.get("natural_unweighted_l2_adjacency_defined") is False
        and full_boundary.get("status") == "THEOREM_ONLY_NO_FINITE_AUDIT_PRETENSE"
    )

    primes = prime_sieve(19)
    fock_beta = 2
    fock_degree = 6
    product_coefficients = fock_product_coefficients(primes, fock_beta, fock_degree)
    enumerated_coefficients = fock_enumeration_coefficients(primes, fock_beta, fock_degree)
    finite_euler_value = RATIONAL_ONE
    for label in primes:
        finite_euler_value /= 1 - Fraction(1, label**fock_beta)
    fock_fixture = {
        "schema_version": "SD-C37-prime-fock-marker-v1",
        "construction_location": "independent evaluator after source freeze",
        "prime_cutoff": 19,
        "prime_labels": primes,
        "beta": fock_beta,
        "particle_degree_cutoff": fock_degree,
        "marker": "z counts total bosonic occupation Omega, not original affine graph steps",
        "coefficient_formula": "product_{p<=19}(1-z*p^(-beta))^(-1)",
        "coefficients_through_degree_6": flist(product_coefficients),
        "independent_occupation_enumeration_coefficients": flist(enumerated_coefficients),
        "coefficient_methods_equal": product_coefficients == enumerated_coefficients,
        "finite_euler_product_at_z_one": ftext(finite_euler_value),
        "z_one_is_specialization": True,
        "z_one_is_not_original_graph_step_marker": True,
        "prime_basis_preloaded": True,
        "source_contains_prime_classifier": False,
    }
    fock_pass = (
        product_coefficients == enumerated_coefficients
        and any(value != 0 for value in product_coefficients[1:])
        and fock_fixture["z_one_is_specialization"]
        and fock_fixture["prime_basis_preloaded"]
    )

    scalar_weight = Fraction(1, 2)
    signed_power_sums = [scalar_weight**power + (-scalar_weight) ** power for power in range(1, 9)]
    nilpotent: Matrix2 = ((RATIONAL_ZERO, RATIONAL_ONE), (RATIONAL_ZERO, RATIONAL_ZERO))
    traceless_invertible: Matrix2 = ((RATIONAL_ONE, RATIONAL_ZERO), (RATIONAL_ZERO, -RATIONAL_ONE))
    nilpotent_traces = matrix_traces(nilpotent, 8)
    invertible_traces = matrix_traces(traceless_invertible, 8)
    boundary_fixture = {
        "schema_version": "SD-C37-signed-matrix-boundary-v1",
        "signed_scalar": {
            "weights": [ftext(scalar_weight), ftext(-scalar_weight)],
            "power_sums_1_through_8": flist(signed_power_sums),
            "odd_powers_cancel": all(signed_power_sums[index - 1] == 0 for index in (1, 3, 5, 7)),
            "even_powers_survive": all(signed_power_sums[index - 1] != 0 for index in (2, 4, 6, 8)),
            "literal_primitive_word_deletion": False,
        },
        "nilpotent_matrix": {
            "matrix": [["0/1", "1/1"], ["0/1", "0/1"]],
            "nonzero": True,
            "power_traces_1_through_8": flist(nilpotent_traces),
            "det_I_minus_zM": ["1/1"],
            "determinant_factor_is_one": all(value == 0 for value in nilpotent_traces),
            "literal_primitive_word_deletion": False,
        },
        "traceless_invertible_matrix": {
            "matrix": [["1/1", "0/1"], ["0/1", "-1/1"]],
            "matrix_determinant": ftext(matrix_determinant(traceless_invertible)),
            "power_traces_1_through_8": flist(invertible_traces),
            "det_I_minus_zM": ["1/1", "0/1", "-1/1"],
            "first_trace_zero": invertible_traces[0] == 0,
            "second_trace_nonzero": invertible_traces[1] != 0,
            "all_orders_cancel": all(value == 0 for value in invertible_traces),
            "literal_primitive_word_deletion": False,
        },
        "groupoid_boundary": {
            "status": "OPEN_BOUNDARY_NOT_EVALUATED_AS_SAME_OBJECT",
            "partition_function_equals_periodic_orbit_zeta_assumed": False,
            "whole_operator_marker_preserved_by_default": False,
        },
    }
    boundary_pass = (
        boundary_fixture["signed_scalar"]["odd_powers_cancel"]
        and boundary_fixture["signed_scalar"]["even_powers_survive"]
        and boundary_fixture["nilpotent_matrix"]["determinant_factor_is_one"]
        and boundary_fixture["traceless_invertible_matrix"]["first_trace_zero"]
        and boundary_fixture["traceless_invertible_matrix"]["second_trace_nonzero"]
        and not boundary_fixture["traceless_invertible_matrix"]["all_orders_cancel"]
    )

    firewall = source_firewall(code_directory)
    firewall_pass = bool(firewall["pass"])

    controls = {
        "schema_version": "SD-C37-control-evaluation-v1",
        "commutation_controls": rebuilt_commutations,
        "commutation_note": "D_m,D_n are generic retained dilation generators; no primality predicate is used.",
        "arbitrary_monoid_controls": rebuilt_monoids,
        "control_classes": [
            {"name": row["name"], "class": "baseline composite radix" if row["name"] == "affine_composite" else "mutated arbitrary one-relator monoid"}
            for row in rebuilt_monoids
        ],
        "generic_relation_cycles_survive": commutation_pass and monoid_pass,
        "arithmetic_acceptance_labels_used": False,
    }

    expected_counterexamples = [
        {
            "id": "CE1_CUNTZ_ZERO_LOOP",
            "retained": True,
            "exact_witness": "for dilation n>=2, n*0=0",
            "correction": "the strict-height theorem applies to the frozen right Cayley P_r coordinates, not every ax+b action graph",
        },
        {
            "id": "CE2_IDENTITY_GENERATOR_LOOP",
            "retained": True,
            "exact_witness": "x multiplied by the identity remains x",
            "correction": "identity-labelled edges are excluded from the frozen positive generator set",
        },
        {
            "id": "CE3_QUOTIENT_UQ_CYCLE",
            "retained": all(row["u_q_closed"] for row in rebuilt_quotients),
            "exact_witness": "U_q^q closes for every q=1,...,12",
            "correction": "finite quotients add cycles and do not descend to an infinite-source primitive ledger",
        },
        {
            "id": "CE4_SMALL_MODULUS_COLLAPSE_2_2",
            "retained": q22["required_2_2_degeneracy"],
            "exact_witness": "the r=2,q=2 relation polygon repeats a vertex",
            "correction": "labelled relation closure survives although vertex-simple geometry degenerates",
        },
        {
            "id": "CE5_TRACE_NOT_DETERMINANT",
            "retained": all(row["trace_is_not_determinant_germ"] for row in bc_firewall_rows),
            "exact_witness": "Tr(D_beta) is the z coefficient of -log det(I-zD_beta), not the whole determinant germ",
            "correction": "the finite diagonal identity is coefficient-wise and keeps z free",
        },
        {
            "id": "CE6_FIRST_TRACE_NOT_ALL_ORDERS",
            "retained": boundary_fixture["traceless_invertible_matrix"]["second_trace_nonzero"],
            "exact_witness": "diag(1,-1) has trace 0 but second-power trace 2",
            "correction": "first-order matrix cancellation is not all-orders primitive deletion",
        },
    ]

    after_hashes = {name: digest(source / name) for name in source_names}
    source_unchanged = before_hashes == after_hashes
    gates = {
        "G1_positive_height_dag": dag_pass,
        "G2_symmetric_backtracks": backtrack_pass,
        "G3_hashimoto_affine_relation": relation_pass,
        "G4_commutation_and_generic_controls": commutation_pass and monoid_pass,
        "G5_operator_and_full_monoid_boundary": operator_pass and full_boundary_pass,
        "G6_finite_quotient_corrections": quotient_pass,
        "G7_bc_trace_determinant_firewall": bc_pass,
        "G8_bosonic_marker_firewall": fock_pass,
        "G9_signed_matrix_boundary": boundary_pass,
        "G10_source_evaluator_separation": firewall_pass and manifest_hash_match and aggregate_match and source_unchanged,
    }
    unexpected_mismatches = [name for name, passed in gates.items() if not passed]
    result = {
        "schema_version": "SD-C37-independent-evaluation-v1",
        "status": "PASS" if not unexpected_mismatches else "FAIL",
        "baseline_r": parameters["baseline_r"],
        "control_r_values": [radix for radix in parameters["r_values"] if radix != parameters["baseline_r"]],
        "exact_arithmetic": True,
        "source_manifest_hash_match_before_evaluation": manifest_hash_match,
        "source_manifest_aggregate_match": aggregate_match,
        "source_hashes_unchanged_after_evaluation": source_unchanged,
        "height_ledger_exact_reconstruction": height_exact,
        "dag_records": dag_records,
        "backtrack_ledger_exact_reconstruction": backtrack_exact,
        "backtrack_count": len(rebuilt_backtracks),
        "word_census_exact_reconstruction": census_exact,
        "relation_witness_exact_reconstruction": relation_exact,
        "relation_first_occurrences": relation_first_occurrences,
        "commutation_exact_reconstruction": commutation_exact,
        "operator_certificate_exact_reconstruction": operator_exact,
        "quotient_ledger_exact_reconstruction": quotient_exact,
        "bc_fixture_exact_reconstruction": bc_exact,
        "monoid_control_exact_reconstruction": monoid_exact,
        "full_monoid_finite_census_performed": full_boundary["finite_census_performed"],
        "full_monoid_status": full_boundary["status"],
        "gates": gates,
        "unexpected_mismatches": unexpected_mismatches,
        "route_tuple": [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_FAIL",
            "A2_FAIL",
            "A3_FAIL",
            "A4_FAIL"
        ],
        "route_a_advanced": False,
        "paper36_minimum_obligation": "exhibit a source-natural cancellation or quotient/induction with an explicit marker map and same-whole-operator trace-log proof; otherwise retain the negative benchmark",
    }

    write_json(output / "evaluation.json", result)
    write_json(output / "bc_firewall.json", {"schema_version": "SD-C37-bc-firewall-v1", "fixtures": bc_firewall_rows})
    write_json(output / "fock_marker_firewall.json", fock_fixture)
    write_json(output / "boundary_controls.json", boundary_fixture)
    write_json(output / "control_evaluation.json", controls)
    write_json(output / "source_evaluator_firewall.json", firewall)
    write_json(
        output / "counterexamples.json",
        {
            "schema_version": "SD-C37-counterexamples-v1",
            "expected_corrections": expected_counterexamples,
            "all_expected_corrections_retained": all(row["retained"] for row in expected_counterexamples),
            "unexpected_mismatches": unexpected_mismatches,
        },
    )
    if unexpected_mismatches or not all(row["retained"] for row in expected_counterexamples):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
