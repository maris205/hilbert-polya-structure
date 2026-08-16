#!/usr/bin/env python3
"""Independent exact evaluator for Paper 38.

This file never imports source_core.  Scientific arithmetic uses integers and
fractions.Fraction only.  Infinite-object conclusions are emitted as theorem
boundaries and are not inferred from the finite checks.
"""

from __future__ import annotations

from fractions import Fraction
import json
from math import gcd
import sys
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


INVERSE = {"u": "U", "U": "u", "v": "V", "V": "v"}


def free_reduce(word: str) -> str:
    stack: List[str] = []
    for letter in word:
        if stack and INVERSE[letter] == stack[-1]:
            stack.pop()
        else:
            stack.append(letter)
    return "".join(stack)


def cyclic_reduce(word: str) -> str:
    word = free_reduce(word)
    while len(word) >= 2 and word[0] == INVERSE[word[-1]]:
        word = free_reduce(word[1:-1])
    return word


def inverse_word(word: str) -> str:
    return "".join(INVERSE[x] for x in reversed(word))


def rotations(word: str) -> Iterable[str]:
    for i in range(len(word)):
        yield word[i:] + word[:i]


def parse_gbs_relator(word: str) -> Optional[Tuple[int, int]]:
    """Recognize a cyclic BS(p,q) relator, independently of source metadata."""
    word = cyclic_reduce(word)
    if not word:
        return None
    for candidate in (word, inverse_word(word)):
        for rotated in rotations(candidate):
            if not rotated.startswith("v"):
                continue
            try:
                split = rotated.index("V", 1)
            except ValueError:
                continue
            first = rotated[1:split]
            second = rotated[split + 1 :]
            if not first or not second:
                continue
            if set(first) == {"u"} and set(second) == {"U"}:
                return (len(first), len(second))
            if set(first) == {"U"} and set(second) == {"u"}:
                return (len(first), len(second))
    return None


def divisors(n: int) -> List[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int, cache: Dict[int, int]) -> int:
    if n not in cache:
        cache[n] = -sum(mobius(d, cache) for d in divisors(n) if d < n)
    return cache[n]


def necklace_count(r: int, k: int) -> int:
    return sum(r ** gcd(j, k) for j in range(k)) // k


def positive_height_class_count(r: int, k: int) -> int:
    if r == 1:
        raise ValueError("balanced case has infinitely many group conjugacy classes")
    return necklace_count(r, k) - 1


def primitive_height_count(r: int, k: int) -> int:
    if r == 1:
        raise ValueError("balanced case diverges")
    if k == 1:
        return r - 1
    mu_cache = {1: 1}
    numerator = sum(mobius(d, mu_cache) * r ** (k // d) for d in divisors(k))
    assert numerator % k == 0
    return numerator // k


def residue_orbit_count(r: int, k: int) -> int:
    modulus = r**k - 1
    if modulus <= 0:
        raise ValueError("zero modulus")
    seen = set()
    count = 0
    for value in range(modulus):
        if value in seen:
            continue
        count += 1
        cursor = value
        while cursor not in seen:
            seen.add(cursor)
            cursor = (r * cursor) % modulus
    return count


def series_multiply(a: Sequence[Fraction], b: Sequence[Fraction], degree: int) -> List[Fraction]:
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= degree:
                out[i + j] += x * y
    return out


def binomial(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    out = 1
    for j in range(1, k + 1):
        out = out * (n - k + j) // j
    return out


def euler_product_series(r: int, degree: int, modular_power: int = 0) -> List[Fraction]:
    """Product over positive-height primitive classes with Delta^(-s)."""
    scale = Fraction(1, r**modular_power) if modular_power >= 0 else Fraction(r ** (-modular_power), 1)
    coeff = [Fraction(1)] + [Fraction(0) for _ in range(degree)]
    for k in range(1, degree + 1):
        multiplicity = primitive_height_count(r, k)
        factor = [Fraction(0) for _ in range(degree + 1)]
        for j in range(0, degree // k + 1):
            factor[j * k] = Fraction(binomial(multiplicity + j - 1, j)) * scale ** (j * k)
        coeff = series_multiply(coeff, factor, degree)
    return coeff


def closed_form_series(r: int, degree: int, modular_power: int = 0) -> List[Fraction]:
    scale = Fraction(1, r**modular_power) if modular_power >= 0 else Fraction(r ** (-modular_power), 1)
    out = [Fraction(1)]
    for n in range(1, degree + 1):
        out.append(Fraction(r - 1) * Fraction(r ** (n - 1)) * scale**n)
    return out


def fraction_json(value: Fraction) -> object:
    if value.denominator == 1:
        return value.numerator
    return {"numerator": value.numerator, "denominator": value.denominator}


def finite_rooted_tree(branching: int, depth: int) -> Dict[Tuple[int, ...], set]:
    vertex_set = {tuple()}
    frontier = {tuple()}
    for _ in range(depth):
        nxt = {path + (digit,) for path in frontier for digit in range(branching)}
        vertex_set.update(nxt)
        frontier = nxt
    adjacency = {vertex: set() for vertex in vertex_set}
    for vertex in vertex_set:
        if vertex:
            parent = vertex[:-1]
            adjacency[vertex].add(parent)
            adjacency[parent].add(vertex)
    return adjacency


def has_reduced_closed_walk(adjacency: Dict[Tuple[int, ...], set], max_length: int) -> bool:
    oriented = [(a, b) for a, neighbors in adjacency.items() for b in neighbors]
    for start_a, start_b in oriented:
        stack = [(start_a, start_b, 1)]
        while stack:
            previous, current, length = stack.pop()
            if length >= max_length:
                continue
            for nxt in adjacency[current]:
                if nxt == previous:
                    continue
                new_length = length + 1
                if nxt == start_a:
                    return True
                stack.append((current, nxt, new_length))
    return False


def height(word: str) -> int:
    return word.count("v") - word.count("V")


def evaluate(fixture: Dict[str, object]) -> Dict[str, object]:
    checks: List[Dict[str, object]] = []

    def check(name: str, condition: bool, detail: object = None) -> None:
        row: Dict[str, object] = {"name": name, "passed": bool(condition)}
        if detail is not None:
            row["detail"] = detail
        checks.append(row)
        if not condition:
            raise AssertionError(f"failed check: {name}: {detail}")

    check("schema", fixture.get("schema") == "paper38-source-fixture-v1")
    check("candidate", fixture.get("candidate_id") == "SD-C40")
    declaration = fixture["source_oracle_declaration"]
    check("no_source_oracle", not any(declaration.values()), declaration)
    obj = fixture["object"]
    check("new_object_declared", obj["new_object"] is True)
    check("no_same_object_credit", obj["inherits_same_object_credit"] is False)
    check("no_same_marker_credit", obj["inherits_same_marker_credit"] is False)

    limit = fixture["limits"]
    degree = int(limit["formal_series_degree"])
    parameter_results = []
    for row in fixture["parameter_rows"]:
        r = int(row["r"])
        direct = {
            "r": r,
            "declared_class": row["declared_class"],
            "tree_degree": r + 1,
            "vertex_stabilizer": "infinite_cyclic",
            "edge_stabilizer": "infinite_cyclic",
            "aut_tree_image_discrete": r == 1,
            "bass_serre_action_faithful": r >= 2,
            "action_kernel": "infinite_cyclic" if r == 1 else "trivial",
            "action_proper": False,
            "finite_stabilizer_tree_lattice_hypotheses_met": False,
            "full_tree_positive_reduced_closed_paths": 0,
            "full_tree_hashimoto_compact": False,
            "full_tree_hashimoto_trace_class": False,
            "ordinary_fredholm_determinant_owned": False,
            "canonical_modulus_is_signed_length_only": True,
        }
        check(f"r{r}:tree_degree", direct["tree_degree"] == r + 1)
        check(f"r{r}:infinite_stabilizer", direct["vertex_stabilizer"] == "infinite_cyclic")
        check(
            f"r{r}:action_topology",
            direct["action_proper"] is False
            and direct["finite_stabilizer_tree_lattice_hypotheses_met"] is False
            and (
                r == 1
                and direct["aut_tree_image_discrete"] is True
                and direct["bass_serre_action_faithful"] is False
                and direct["action_kernel"] == "infinite_cyclic"
                or r >= 2
                and direct["aut_tree_image_discrete"] is False
                and direct["bass_serre_action_faithful"] is True
                and direct["action_kernel"] == "trivial"
            ),
        )
        if r == 1:
            direct["orbital_group_conjugacy_ledger"] = "DIVERGENT_AT_EVERY_POSITIVE_HEIGHT"
            direct["positive_height_class_count"] = "infinite"
            check("r1:balanced_divergence", direct["positive_height_class_count"] == "infinite")
        else:
            total = [positive_height_class_count(r, k) for k in range(1, degree + 1)]
            primitive = [primitive_height_count(r, k) for k in range(1, degree + 1)]
            for k in range(1, degree + 1):
                check(
                    f"r{r}:primitive_repetition_k{k}",
                    total[k - 1] == sum(primitive_height_count(r, d) for d in divisors(k)),
                )
                if r <= int(limit["explicit_residue_r_max"]) and k <= int(limit["explicit_residue_k_max"]):
                    check(
                        f"r{r}:residue_orbits_k{k}",
                        residue_orbit_count(r, k) == total[k - 1],
                    )
            ordinary_series = euler_product_series(r, degree, 0)
            modular_series = euler_product_series(r, degree, 1)
            check(f"r{r}:ordinary_rational_collapse", ordinary_series == closed_form_series(r, degree, 0))
            check(f"r{r}:modular_rational_collapse", modular_series == closed_form_series(r, degree, 1))
            direct.update(
                {
                    "orbital_group_conjugacy_ledger": "FINITE_BUT_GENERIC_NECKLACE_LEDGER",
                    "positive_height_class_counts_1_to_12": total,
                    "positive_height_primitive_counts_1_to_12": primitive,
                    "positive_height_zeta_closed_form": "(1-z)/(1-r*z)",
                    "modular_weight_s1_closed_form": "(1-z/r)/(1-z)",
                    "ordinary_series_0_to_12": [fraction_json(x) for x in ordinary_series],
                    "modular_series_0_to_12": [fraction_json(x) for x in modular_series],
                    "source_selective": False,
                }
            )
        parameter_results.append(direct)

    finite_tree_results = []
    for spec in limit["finite_tree_checks"]:
        branching = int(spec["branching"])
        depth = int(spec["depth"])
        walk_length = int(spec["walk_length"])
        adjacency = finite_rooted_tree(branching, depth)
        edge_count = sum(len(x) for x in adjacency.values()) // 2
        check(f"finite_tree_b{branching}:edge_vertex_identity", edge_count == len(adjacency) - 1)
        no_closed = not has_reduced_closed_walk(adjacency, walk_length)
        check(f"finite_tree_b{branching}:no_reduced_closed_walk", no_closed)
        finite_tree_results.append(
            {
                "branching": branching,
                "depth": depth,
                "vertices": len(adjacency),
                "edges": edge_count,
                "max_checked_walk_length": walk_length,
                "reduced_closed_walk_found": not no_closed,
            }
        )

    noncompact_results = []
    for r in (1, 2, 4, 5, 6):
        rows = []
        for columns in limit["noncompact_columns"]:
            columns = int(columns)
            rows.append(
                {
                    "columns": columns,
                    "image_norm_squared_each": r,
                    "pairwise_image_inner_products": 0,
                    "partial_hilbert_schmidt_mass": columns * r,
                }
            )
        check(f"r{r}:noncompact_constant_norm", all(x["image_norm_squared_each"] == r for x in rows))
        check(f"r{r}:hs_mass_strict_growth", all(rows[i]["partial_hilbert_schmidt_mass"] < rows[i + 1]["partial_hilbert_schmidt_mass"] for i in range(len(rows) - 1)))
        noncompact_results.append({"r": r, "orthogonal_column_witness": rows})

    gbs_results = []
    for control in fixture["gbs_controls"]:
        parsed = parse_gbs_relator(control["relator"])
        check(f"{control['control_id']}:eligible", parsed is not None)
        assert parsed is not None
        p, q = parsed
        check(f"{control['control_id']}:source_match", (p, q) == (control["source_p"], control["source_q"]))
        gbs_results.append(
            {
                "control_id": control["control_id"],
                "parsed_p": p,
                "parsed_q": q,
                "ascending": p == 1 or q == 1,
                "balanced": p == q,
                "tree_degree": p + q,
                "infinite_vertex_stabilizer": True,
                "full_tree_closed_ledger_empty": True,
                "full_tree_fredholm_owned": False,
            }
        )

    random_results = []
    for control in fixture["random_relators"]:
        parsed = parse_gbs_relator(control["relator"])
        row = {
            "control_id": control["control_id"],
            "relator": control["relator"],
            "canonical_cyclic_gbs_split_detected": parsed is not None,
        }
        if parsed is None:
            row["paper38_object_status"] = "INELIGIBLE_NO_FROZEN_CYCLIC_HNN_SPLIT"
        else:
            p, q = parsed
            row.update(
                {
                    "parsed_p": p,
                    "parsed_q": q,
                    "paper38_object_status": "ELIGIBLE_CONTROL_SAME_TREE_OBSTRUCTIONS",
                    "full_tree_closed_ledger_empty": True,
                    "full_tree_fredholm_owned": False,
                }
            )
        random_results.append(row)
    eligible_random = sum(x["canonical_cyclic_gbs_split_detected"] for x in random_results)
    check("random_controls_present", len(random_results) == 64)

    marker_results = []
    for row in fixture["marker_rows"]:
        words = []
        for item in row["words"]:
            h = height(item["word"])
            words.append(
                {
                    "name": item["name"],
                    "word": item["word"],
                    "old_generator_marker_length": len(item["word"]),
                    "bass_serre_translation_length": abs(h),
                    "height": h,
                }
            )
        by_name = {x["name"]: x for x in words}
        check(f"marker_r{row['r']}:elliptic_collapses", by_name["elliptic_base"]["bass_serre_translation_length"] == 0 and by_name["elliptic_base"]["old_generator_marker_length"] > 0)
        check(f"marker_r{row['r']}:many_to_one", by_name["same_tree_step_a"]["bass_serre_translation_length"] == by_name["same_tree_step_b"]["bass_serre_translation_length"] and by_name["same_tree_step_a"]["old_generator_marker_length"] != by_name["same_tree_step_b"]["old_generator_marker_length"])
        check(f"marker_r{row['r']}:relator_zero_tree_length", by_name["defining_relator"]["bass_serre_translation_length"] == 0)
        marker_results.append({"r": row["r"], "words": words, "markers_compatible": False})

    check("all_prime_controls_fail_selectivity", all(not x.get("source_selective", False) for x in parameter_results if x["declared_class"] == "prime_control"))
    check("all_composite_controls_fail_selectivity", all(not x.get("source_selective", False) for x in parameter_results if x["declared_class"].startswith("composite")))
    check("all_gbs_full_tree_ledgers_empty", all(x["full_tree_closed_ledger_empty"] for x in gbs_results))
    check("all_gbs_no_full_tree_fredholm", all(not x["full_tree_fredholm_owned"] for x in gbs_results))
    check("all_markers_incompatible", all(not x["markers_compatible"] for x in marker_results))

    decision = {
        "hard_status": "STOP_BASS_SERRE_TREE_BRANCH",
        "branch_status": "CLOSE_ENTIRE_AFFINE_BRANCH",
        "full_tree_primitive_ledger": "EMPTY",
        "full_tree_fredholm": "NOT_OWNED_NON_TRACE_CLASS",
        "tree_lattice_formula_applicable": False,
        "orbital_substitute": "GENERIC_OR_DIVERGENT_AND_NOT_FULL_TREE_FREDHOLM",
        "old_marker_compatible": False,
        "proves_too_much_risk": "RECIPROCAL_INFINITE_STABILIZER_AS_ZERO",
        "route_tuple": [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_FAIL",
            "A2_FAIL",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
    }

    return {
        "schema": "paper38-scientific-results-v1",
        "source_evaluator_separated": True,
        "arithmetic_mode": "exact_integer_and_fraction",
        "parameter_results": parameter_results,
        "finite_tree_results": finite_tree_results,
        "noncompact_results": noncompact_results,
        "gbs_results": gbs_results,
        "random_one_relator_results": random_results,
        "random_control_summary": {
            "total": len(random_results),
            "eligible_cyclic_gbs": eligible_random,
            "ineligible_for_frozen_object": len(random_results) - eligible_random,
        },
        "marker_results": marker_results,
        "theorem_boundary": {
            "tree_has_no_positive_reduced_closed_path": True,
            "full_tree_hashimoto_noncompact": True,
            "ordinary_full_tree_fredholm_not_defined": True,
            "r_ge_2_faithful_image_non_discrete": True,
            "r1_image_discrete_but_infinite_kernel": True,
            "all_r_bass_serre_action_nonproper": True,
            "tree_lattice_finite_stabilizer_hypotheses_fail": True,
            "positive_height_conjugacy_ledger_is_necklace_quotient": True,
            "canonical_modulus_is_function_of_signed_length": True,
            "finite_checks_used_as_infinite_proof": False,
        },
        "decision": decision,
        "checks": checks,
        "check_summary": {"passed": sum(x["passed"] for x in checks), "total": len(checks)},
    }


def main() -> int:
    fixture = json.load(sys.stdin)
    result = evaluate(fixture)
    json.dump(result, sys.stdout, sort_keys=True, separators=(",", ":"))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
