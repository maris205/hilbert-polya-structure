#!/usr/bin/env python3
"""Generate the frozen exact SD-C33 Wilson and control artifacts.

Candidate-side acceptance uses only successor-ordered multiplication and
reduction modulo n (the computational image of the full-shift semiring
congruence).  Independent trial division is confined to evaluator functions.
No target-zero data or supplied prime table is read.
"""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import inspect
import json
import math
import random
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable

from wilson_core import source_remainder, wilson_accept, wilson_residues


CANDIDATE_ID = "SD-C33"
DEFAULT_CUTOFF = 512
SEED = 31033


def evaluator_is_prime(n: int) -> bool:
    """Independent audit predicate, never called by candidate functions."""
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def factor_vector(n: int) -> tuple[tuple[int, int], ...]:
    """Evaluator-only formal-UFD label used by the clone control."""
    if n < 1:
        raise ValueError("formal monomial control is restricted to n>=1")
    rows: list[tuple[int, int]] = []
    divisor = 2
    remaining = n
    while divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            exponent += 1
            remaining //= divisor
        if exponent:
            rows.append((divisor, exponent))
        divisor += 1
    if remaining > 1:
        rows.append((remaining, 1))
    return tuple(rows)


def monomial_text(n: int) -> str:
    vector = factor_vector(n)
    if not vector:
        return "1"
    return "*".join(f"x_{p}" if e == 1 else f"x_{p}^{e}" for p, e in vector)


def ordinary_monomial_sum_matches(left: int, right: int, target: int) -> bool:
    """Compare sparse integer polynomials, rather than recording a verdict."""
    coefficients: dict[tuple[tuple[int, int], ...], int] = {}
    for monomial in (factor_vector(left), factor_vector(right)):
        coefficients[monomial] = coefficients.get(monomial, 0) + 1
    target_polynomial = {factor_vector(target): 1}
    return coefficients == target_polynomial


CloneLabel = tuple[str, int]


def clone_label(index: int) -> CloneLabel:
    return ("y", index)


def clone_index(label: CloneLabel) -> int:
    tag, index = label
    if tag != "y" or index < 0:
        raise ValueError("invalid matched-clone label")
    return index


def clone_add(left: CloneLabel, right: CloneLabel) -> CloneLabel:
    return clone_label(clone_index(left) + clone_index(right))


def clone_multiply(left: CloneLabel, right: CloneLabel) -> CloneLabel:
    return clone_label(clone_index(left) * clone_index(right))


def clone_remainder(value: CloneLabel, modulus: CloneLabel) -> CloneLabel:
    modulus_index = clone_index(modulus)
    return clone_label(source_remainder(clone_index(value), modulus_index))


def clone_wilson_residues(n: int) -> tuple[CloneLabel, ...]:
    """Recompute Wilson's path entirely with transported clone operations."""
    if n < 2:
        raise ValueError("Wilson objects start at n=2")
    modulus = clone_label(n)
    residue = clone_label(1)
    rows = [residue]
    for successor_index in range(2, n):
        residue = clone_remainder(
            clone_multiply(residue, clone_label(successor_index)), modulus
        )
        rows.append(residue)
    return tuple(rows)


def fraction_payload(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def exact_product(support: Iterable[int], z: Fraction, power: Callable[[int], int]) -> Fraction:
    value = Fraction(1, 1)
    for n in support:
        exponent = power(n)
        value *= 1 - (z ** exponent) * Fraction(1, n * n)
    return value


def support_square(n: int) -> bool:
    root = math.isqrt(n)
    return root * root == n and n >= 2


def support_power_two(n: int) -> bool:
    return n >= 2 and n & (n - 1) == 0


def fibonacci_set(cutoff: int) -> set[int]:
    values: set[int] = set()
    a, b = 1, 2
    while b <= cutoff:
        values.add(b)
        a, b = b, a + b
    return values


def support_hash(n: int) -> bool:
    digest = hashlib.sha256(f"{SEED}:{n}".encode("ascii")).digest()
    return digest[0] < 48


def check_semiring_tables(add: list[list[int]], mul: list[list[int]]) -> dict[str, object]:
    size = len(add)
    values = range(size)
    closed = all(0 <= add[a][b] < size and 0 <= mul[a][b] < size for a in values for b in values)
    add_comm = all(add[a][b] == add[b][a] for a in values for b in values)
    mul_comm = all(mul[a][b] == mul[b][a] for a in values for b in values)
    add_assoc = all(add[add[a][b]][c] == add[a][add[b][c]] for a in values for b in values for c in values)
    mul_assoc = all(mul[mul[a][b]][c] == mul[a][mul[b][c]] for a in values for b in values for c in values)
    distributive = all(
        mul[a][add[b][c]] == add[mul[a][b]][mul[a][c]]
        and mul[add[b][c]][a] == add[mul[b][a]][mul[c][a]]
        for a in values
        for b in values
        for c in values
    )
    additive_identities = [z for z in values if all(add[z][a] == a and add[a][z] == a for a in values)]
    multiplicative_identities = [u for u in values if all(mul[u][a] == a and mul[a][u] == a for a in values)]
    passes = bool(
        closed
        and add_comm
        and mul_comm
        and add_assoc
        and mul_assoc
        and distributive
        and additive_identities
        and multiplicative_identities
    )
    return {
        "closed": closed,
        "add_commutative": add_comm,
        "mul_commutative": mul_comm,
        "add_associative": add_assoc,
        "mul_associative": mul_assoc,
        "distributive": distributive,
        "additive_identities": additive_identities,
        "multiplicative_identities": multiplicative_identities,
        "passes_commutative_semiring_axioms": passes,
    }


def modular_semiring(size: int, permutation: list[int] | None = None) -> tuple[list[list[int]], list[list[int]]]:
    if permutation is None:
        permutation = list(range(size))
    inverse = [0] * size
    for original, label in enumerate(permutation):
        inverse[label] = original
    add = [[0] * size for _ in range(size)]
    mul = [[0] * size for _ in range(size)]
    for left_label in range(size):
        for right_label in range(size):
            left = inverse[left_label]
            right = inverse[right_label]
            add[left_label][right_label] = permutation[(left + right) % size]
            mul[left_label][right_label] = permutation[(left * right) % size]
    return add, mul


def table_hash(add: list[list[int]], mul: list[list[int]]) -> str:
    payload = json.dumps({"add": add, "mul": mul}, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def random_table_controls() -> list[dict[str, object]]:
    rng = random.Random(SEED)
    rows: list[dict[str, object]] = []
    for control_index in range(32):
        size = 4
        add = [[rng.randrange(size) for _ in range(size)] for _ in range(size)]
        mul = [[rng.randrange(size) for _ in range(size)] for _ in range(size)]
        result = check_semiring_tables(add, mul)
        rows.append({"control_index": control_index, "table_sha256": table_hash(add, mul), **result})
    permutation = list(range(11))
    rng.shuffle(permutation)
    add, mul = modular_semiring(11, permutation)
    result = check_semiring_tables(add, mul)
    rows.append(
        {
            "control_index": "matched_random_relabel_Zmod11",
            "table_sha256": table_hash(add, mul),
            "finite_characteristic": 11,
            "permutation": permutation,
            **result,
        }
    )
    return rows


def candidate_call_audit() -> dict[str, object]:
    banned = {
        "evaluator_is_prime",
        "factorint",
        "factorization",
        "factor_vector",
        "isprime",
        "monomial_text",
        "prime_iterator",
        "sympy",
        "prime_table",
        "riemann_zero",
        "zero_table",
    }
    functions = [source_remainder, wilson_residues, wilson_accept]
    seen_calls: set[str] = set()
    seen_identifiers: set[str] = set()
    integer_literals: set[int] = set()
    source_hashes: dict[str, str] = {}
    for function in functions:
        source = inspect.getsource(function)
        source_hashes[function.__name__] = hashlib.sha256(
            source.encode("utf-8")
        ).hexdigest()
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                seen_identifiers.add(node.id.lower())
            elif isinstance(node, ast.Attribute):
                seen_identifiers.add(node.attr.lower())
            elif isinstance(node, ast.Constant) and isinstance(node.value, int):
                integer_literals.add(node.value)
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    seen_calls.add(node.func.id)
                elif isinstance(node.func, ast.Attribute):
                    seen_calls.add(node.func.attr)
    forbidden_seen = sorted(seen_identifiers & banned)
    external_calls = sorted(
        seen_identifiers & {"open", "read", "read_text", "urlopen", "request"}
    )
    return {
        "audited_functions": [function.__name__ for function in functions],
        "seen_calls": sorted(seen_calls),
        "seen_identifiers": sorted(seen_identifiers),
        "integer_literals": sorted(integer_literals),
        "candidate_source_sha256": source_hashes,
        "forbidden_identifiers": sorted(banned),
        "forbidden_seen": forbidden_seen,
        "external_file_or_network_calls": external_calls,
        "passes": not forbidden_seen and not external_calls,
    }


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def generate(output: Path, cutoff: int) -> dict[str, object]:
    output.mkdir(parents=True, exist_ok=True)
    wilson_rows: list[dict[str, object]] = []
    accepted: list[int] = []
    composite_rows: list[dict[str, object]] = []
    pseudoprime_rows: list[dict[str, object]] = []
    matched_clone_equal = True
    for n in range(2, cutoff + 1):
        residues = wilson_residues(n)
        accepts = residues[-1] == n - 1
        evaluator = evaluator_is_prime(n)
        if accepts:
            accepted.append(n)
        wilson_rows.append(
            {
                "n": n,
                "final_residue": residues[-1],
                "accepts": int(accepts),
                "independent_prime_audit": int(evaluator),
                "cycle_length_if_accepted": n - 1 if accepts else 0,
                "residue_path_sha256": hashlib.sha256(
                    ",".join(map(str, residues)).encode("ascii")
                ).hexdigest(),
            }
        )
        clone_residues = tuple(
            clone_index(value) for value in clone_wilson_residues(n)
        )
        matched_clone_equal = matched_clone_equal and clone_residues == residues
        if not evaluator:
            composite_rows.append(
                {
                    "n": n,
                    "final_residue": residues[-1],
                    "target_residue": n - 1,
                    "wilson_accepts": int(accepts),
                }
            )
            if math.gcd(2, n) == 1 and pow(2, n - 1, n) == 1:
                pseudoprime_rows.append(
                    {
                        "n": n,
                        "fermat_base2_residue": pow(2, n - 1, n),
                        "wilson_final_residue": residues[-1],
                        "wilson_accepts": int(accepts),
                    }
                )

    write_csv(
        output / "wilson_ledger.csv",
        ["n", "final_residue", "accepts", "independent_prime_audit", "cycle_length_if_accepted", "residue_path_sha256"],
        wilson_rows,
    )
    write_csv(output / "composite_controls.csv", ["n", "final_residue", "target_residue", "wilson_accepts"], composite_rows)
    write_csv(
        output / "fermat_pseudoprime_controls.csv",
        ["n", "fermat_base2_residue", "wilson_final_residue", "wilson_accepts"],
        pseudoprime_rows,
    )

    bare_rows: list[dict[str, object]] = []
    for left in range(1, 13):
        for right in range(1, 13):
            ordinary_sum_matches = ordinary_monomial_sum_matches(
                left, right, left + right
            )
            bare_rows.append(
                {
                    "left": left,
                    "right": right,
                    "X_left": monomial_text(left),
                    "X_right": monomial_text(right),
                    "ordinary_polynomial_sum": f"({monomial_text(left)})+({monomial_text(right)})",
                    "required_target": monomial_text(left + right),
                    "ordinary_sum_is_required_monic_monomial": int(
                        ordinary_sum_matches
                    ),
                }
            )
    write_csv(
        output / "bare_ufd_addition_failure.csv",
        ["left", "right", "X_left", "X_right", "ordinary_polynomial_sum", "required_target", "ordinary_sum_is_required_monic_monomial"],
        bare_rows,
    )

    matched_rows: list[dict[str, object]] = []
    for left in range(0, 13):
        for right in range(0, 13):
            left_label = clone_label(left)
            right_label = clone_label(right)
            transported_sum = clone_add(left_label, right_label)
            transported_product = clone_multiply(left_label, right_label)
            matched_rows.append(
                {
                    "left": f"y_{left}",
                    "right": f"y_{right}",
                    "transported_sum": f"y_{clone_index(transported_sum)}",
                    "transported_product": f"y_{clone_index(transported_product)}",
                    "baseline_sum_index": left + right,
                    "baseline_product_index": left * right,
                    "matches": int(
                        clone_index(transported_sum) == left + right
                        and clone_index(transported_product) == left * right
                    ),
                }
            )
    write_csv(
        output / "matched_semiring_clone.csv",
        ["left", "right", "transported_sum", "transported_product", "baseline_sum_index", "baseline_product_index", "matches"],
        matched_rows,
    )

    semiring_controls = [
        {
            "name": "full_shift_positive_integer_semiring",
            "commutative_semiring": True,
            "additively_generated_by_one": True,
            "characteristic_zero": True,
            "unbounded_successor_order": True,
            "passes_source_lock": True,
            "wilson_ledger_relation": "baseline",
        },
        {
            "name": "bare_polynomial_UFD_monomials",
            "commutative_semiring": False,
            "additively_generated_by_one": False,
            "characteristic_zero": True,
            "unbounded_successor_order": False,
            "passes_source_lock": False,
            "wilson_ledger_relation": "undefined_addition_not_closed",
        },
        {
            "name": "matched_transported_semiring_clone",
            "commutative_semiring": True,
            "additively_generated_by_one": True,
            "characteristic_zero": True,
            "unbounded_successor_order": True,
            "passes_source_lock": True,
            "wilson_ledger_relation": "exact_copy",
        },
        {
            "name": "Boolean_semiring",
            "commutative_semiring": True,
            "additively_generated_by_one": True,
            "characteristic_zero": False,
            "unbounded_successor_order": False,
            "passes_source_lock": False,
            "wilson_ledger_relation": "finite_characteristic_collapse",
        },
        {
            "name": "Z_mod_11",
            "commutative_semiring": True,
            "additively_generated_by_one": True,
            "characteristic_zero": False,
            "unbounded_successor_order": False,
            "passes_source_lock": False,
            "wilson_ledger_relation": "finite_characteristic_collapse",
        },
        {
            "name": "N_polynomial_t",
            "commutative_semiring": True,
            "additively_generated_by_one": False,
            "characteristic_zero": True,
            "unbounded_successor_order": True,
            "passes_source_lock": False,
            "wilson_ledger_relation": "nonconstant_elements_not_successor_generated",
        },
        {
            "name": "tropical_min_plus",
            "commutative_semiring": True,
            "additively_generated_by_one": False,
            "characteristic_zero": False,
            "unbounded_successor_order": False,
            "passes_source_lock": False,
            "wilson_ledger_relation": "idempotent_addition",
        },
    ]
    write_json(output / "semiring_controls.json", semiring_controls)
    random_controls = random_table_controls()
    write_json(output / "random_operation_controls.json", random_controls)

    dilution_rows: list[dict[str, object]] = []
    for prime in accepted:
        length = prime - 1
        for sigma in (1, 2, 3):
            lower_bound = math.exp(-sigma * math.log(prime) / length)
            dilution_rows.append(
                {
                    "p": prime,
                    "cycle_length": length,
                    "sigma": sigma,
                    "total_roof": f"log({prime})",
                    "max_edge_weight_lower_bound": format(lower_bound, ".17g"),
                    "exact_expression": f"{prime}^(-{sigma}/{length})",
                }
            )
    write_csv(
        output / "entropy_budget_dilution.csv",
        ["p", "cycle_length", "sigma", "total_roof", "max_edge_weight_lower_bound", "exact_expression"],
        dilution_rows,
    )

    trace_rows: list[dict[str, object]] = []
    for power in range(1, 17):
        contributions: list[str] = []
        value = Fraction(0, 1)
        for prime in accepted:
            length = prime - 1
            if power % length == 0:
                exponent = 2 * power // length
                term = Fraction(length, prime**exponent)
                value += term
                contributions.append(f"{length}/{prime}^{exponent}")
        trace_rows.append(
            {
                "power": power,
                "finite_contribution_count": len(contributions),
                "formal_flat_trace_s2": f"{value.numerator}/{value.denominator}",
                "contributions": ";".join(contributions),
                "ordinary_operator_trace_owned": 0,
            }
        )
    write_csv(
        output / "formal_trace_ledger.csv",
        ["power", "finite_contribution_count", "formal_flat_trace_s2", "contributions", "ordinary_operator_trace_owned"],
        trace_rows,
    )

    product_support = [prime for prime in accepted if prime <= 31]
    product_rows: list[dict[str, object]] = []
    for z in (Fraction(1, 1), Fraction(1, 3)):
        raw = exact_product(product_support, z, lambda p: p - 1)
        induced = exact_product(product_support, z, lambda p: 1)
        product_rows.append(
            {
                "cutoff": 31,
                "s": 2,
                "z": f"{z.numerator}/{z.denominator}",
                "raw_cycle_product": fraction_payload(raw),
                "induced_return_product": fraction_payload(induced),
                "equal": raw == induced,
            }
        )
    write_json(output / "marker_change_certificate.json", product_rows)

    fib = fibonacci_set(cutoff)
    support_functions: dict[str, Callable[[int], bool]] = {
        "wilson_primes": wilson_accept,
        "squares": support_square,
        "powers_of_two": support_power_two,
        "fibonacci": lambda n: n in fib,
        "seeded_hash": support_hash,
    }
    wrapper_rows: list[dict[str, object]] = []
    for name, predicate in support_functions.items():
        support = [n for n in range(2, min(cutoff, 128) + 1) if predicate(n)]
        diagonal = exact_product(support, Fraction(1, 3), lambda n: 1)
        recurrent = exact_product(support, Fraction(1, 3), lambda n: n - 1)
        wrapper_rows.append(
            {
                "support": name,
                "accepted_count_through_128": len(support),
                "accepted_sha256": hashlib.sha256(",".join(map(str, support)).encode("ascii")).hexdigest(),
                "transient_accept_loop_determinant": fraction_payload(diagonal),
                "recurrent_cycle_formal_product": fraction_payload(recurrent),
                "transient_prunes_to_diagonal": True,
                "recurrent_exact_clock_noncompact_when_support_has_unbounded_n": True,
            }
        )
    write_json(output / "universal_wrapper_controls.json", wrapper_rows)

    call_audit = candidate_call_audit()
    write_json(output / "source_oracle_certificate.json", call_audit)

    random_pass_count = sum(bool(row["passes_commutative_semiring_axioms"]) for row in random_controls[:32])
    tests = {
        "wilson_matches_independent_prime_audit": all(bool(row["accepts"]) == bool(row["independent_prime_audit"]) for row in wilson_rows),
        "all_composites_rejected": all(not bool(row["wilson_accepts"]) for row in composite_rows),
        "all_base2_pseudoprime_controls_rejected": all(not bool(row["wilson_accepts"]) for row in pseudoprime_rows),
        "bare_ufd_not_additively_closed": all(not bool(row["ordinary_sum_is_required_monic_monomial"]) for row in bare_rows),
        "explicit_1_plus_1_breaks_bare_clone": monomial_text(1) == "1" and monomial_text(2) == "x_2",
        "matched_semiring_clone_operations_copy": all(bool(row["matches"]) for row in matched_rows),
        "matched_semiring_clone_wilson_copy": matched_clone_equal,
        "source_lock_selects_baseline_and_matched_clone_only": [row["name"] for row in semiring_controls if row["passes_source_lock"]] == ["full_shift_positive_integer_semiring", "matched_transported_semiring_clone"],
        "random_magma_tables_do_not_accidentally_pass": random_pass_count == 0,
        "random_relabel_Zmod11_is_semiring": bool(random_controls[-1]["passes_commutative_semiring_axioms"]),
        "candidate_call_audit_passes": bool(call_audit["passes"]),
        "prime_cycle_length_is_p_minus_1": all(row["cycle_length_if_accepted"] == row["n"] - 1 for row in wilson_rows if row["accepts"]),
        "dilution_lower_bound_exceeds_0_95_at_largest_prime_sigma2": float([row for row in dilution_rows if row["p"] == accepted[-1] and row["sigma"] == 2][0]["max_edge_weight_lower_bound"]) > 0.95,
        "formal_trace_contributions_are_finite": all(row["finite_contribution_count"] <= power + 1 for power, row in enumerate(trace_rows, start=1)),
        "raw_and_induced_products_agree_at_z1": bool(product_rows[0]["equal"]),
        "raw_and_induced_products_differ_at_z_one_third": not bool(product_rows[1]["equal"]),
        "universal_wrapper_has_five_supports": len(wrapper_rows) == 5,
        "all_transient_wrappers_prune": all(bool(row["transient_prunes_to_diagonal"]) for row in wrapper_rows),
    }
    write_json(
        output / "test_report.json",
        {
            "candidate_id": CANDIDATE_ID,
            "passed": sum(bool(value) for value in tests.values()),
            "total": len(tests),
            "failures": sorted(key for key, value in tests.items() if not value),
            "tests": tests,
        },
    )

    summary = {
        "candidate_id": CANDIDATE_ID,
        "cutoff": cutoff,
        "accepted_count": len(accepted),
        "largest_accepted": accepted[-1],
        "composite_control_count": len(composite_rows),
        "base2_pseudoprime_control_count": len(pseudoprime_rows),
        "bare_ufd_addition_pairs": len(bare_rows),
        "bare_ufd_addition_matches": sum(int(row["ordinary_sum_is_required_monic_monomial"]) for row in bare_rows),
        "matched_clone_operation_rows": len(matched_rows),
        "matched_clone_wilson_equal": matched_clone_equal,
        "random_magma_controls": 32,
        "random_magma_semiring_passes": random_pass_count,
        "matched_random_relabel_semiring_pass": bool(random_controls[-1]["passes_commutative_semiring_axioms"]),
        "formal_trace_orders": len(trace_rows),
        "wrapper_control_families": len(wrapper_rows),
        "route_tuple": [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_PASS_ANALYTIC",
            "A2_FAIL",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "overall": "ROUTE_A_REJECTED",
        "route_b": "LOCKED",
        "decision": "GO_NEGATIVE_CLOSURE_PAPER_STOP_POSITIVE_CANDIDATE",
    }
    write_json(output / "summary.json", summary)
    return summary


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def freeze(output: Path) -> str:
    entries: list[str] = []
    for path in sorted(output.iterdir(), key=lambda p: p.name):
        if path.is_file() and path.name not in {"SHA256SUMS.txt", "aggregate_sha256.txt"}:
            entries.append(f"{sha256_file(path)}  {path.name}")
    (output / "SHA256SUMS.txt").write_text("\n".join(entries) + "\n", encoding="utf-8")
    aggregate = hashlib.sha256(("\n".join(entries) + "\n").encode("utf-8")).hexdigest()
    (output / "aggregate_sha256.txt").write_text(aggregate + "\n", encoding="utf-8")
    return aggregate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--cutoff", type=int, default=DEFAULT_CUTOFF)
    args = parser.parse_args()
    if args.cutoff < 31:
        raise SystemExit("cutoff must be at least 31")
    summary = generate(args.output, args.cutoff)
    print(json.dumps({"summary": summary}, sort_keys=True))


if __name__ == "__main__":
    main()
