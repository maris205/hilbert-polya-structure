#!/usr/bin/env python3
"""Independent serialized-artifact evaluator for SD-C33.

This module imports neither wilson_core nor generate_results.
"""

from __future__ import annotations

import argparse
import csv
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import random
from typing import Callable, Iterable


SEED = 31033
ROUTE_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_PASS_ANALYTIC",
    "A2_FAIL",
    "A3_FAIL",
    "A4_FAIL",
]


class Audit:
    def __init__(self) -> None:
        self.rows: list[dict[str, object]] = []

    def check(self, name: str, condition: bool, detail: str = "") -> None:
        self.rows.append({"name": name, "pass": bool(condition), "detail": detail})

    def result(self) -> dict[str, object]:
        failures = [row for row in self.rows if not row["pass"]]
        return {
            "candidate_id": "SD-C33",
            "schema_version": "SD-C33-independent-evaluation-v1",
            "independent_of_candidate_core": True,
            "check_count": len(self.rows),
            "pass_count": len(self.rows) - len(failures),
            "failure_count": len(failures),
            "all_pass": not failures,
            "failures": failures,
            "checks": self.rows,
            "route_tuple": ROUTE_TUPLE,
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        }


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def residues(n: int) -> tuple[int, ...]:
    value = 1
    rows = [value]
    for factor in range(2, n):
        value = (value * factor) % n
        rows.append(value)
    return tuple(rows)


def factor_vector(n: int) -> tuple[tuple[int, int], ...]:
    rows: list[tuple[int, int]] = []
    remaining = n
    divisor = 2
    while divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
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
    return "*".join(f"x_{prime}" if exponent == 1 else f"x_{prime}^{exponent}" for prime, exponent in vector)


def exact_product(support: Iterable[int], z: Fraction, power: Callable[[int], int]) -> Fraction:
    value = Fraction(1, 1)
    for n in support:
        value *= 1 - (z ** power(n)) * Fraction(1, n * n)
    return value


def fraction_payload(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


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
    return {
        "closed": closed,
        "add_commutative": add_comm,
        "mul_commutative": mul_comm,
        "add_associative": add_assoc,
        "mul_associative": mul_assoc,
        "distributive": distributive,
        "additive_identities": additive_identities,
        "multiplicative_identities": multiplicative_identities,
        "passes_commutative_semiring_axioms": bool(
            closed and add_comm and mul_comm and add_assoc and mul_assoc
            and distributive and additive_identities and multiplicative_identities
        ),
    }


def modular_semiring(size: int, permutation: list[int]) -> tuple[list[list[int]], list[list[int]]]:
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


def expected_random_controls() -> list[dict[str, object]]:
    rng = random.Random(SEED)
    rows: list[dict[str, object]] = []
    for control_index in range(32):
        size = 4
        add = [[rng.randrange(size) for _ in range(size)] for _ in range(size)]
        mul = [[rng.randrange(size) for _ in range(size)] for _ in range(size)]
        rows.append({"control_index": control_index, "table_sha256": table_hash(add, mul), **check_semiring_tables(add, mul)})
    permutation = list(range(11))
    rng.shuffle(permutation)
    add, mul = modular_semiring(11, permutation)
    rows.append(
        {
            "control_index": "matched_random_relabel_Zmod11",
            "table_sha256": table_hash(add, mul),
            "finite_characteristic": 11,
            "permutation": permutation,
            **check_semiring_tables(add, mul),
        }
    )
    return rows


def fibonacci_set(cutoff: int) -> set[int]:
    values: set[int] = set()
    left, right = 1, 2
    while right <= cutoff:
        values.add(right)
        left, right = right, left + right
    return values


def wrapper_expected(primes: list[int]) -> list[dict[str, object]]:
    fibonacci = fibonacci_set(4096)

    def square(n: int) -> bool:
        root = math.isqrt(n)
        return n >= 2 and root * root == n

    def power_two(n: int) -> bool:
        return n >= 2 and n & (n - 1) == 0

    def seeded_hash(n: int) -> bool:
        return hashlib.sha256(f"{SEED}:{n}".encode("ascii")).digest()[0] < 48

    functions: dict[str, Callable[[int], bool]] = {
        "wilson_primes": lambda n: n in set(primes),
        "squares": square,
        "powers_of_two": power_two,
        "fibonacci": lambda n: n in fibonacci,
        "seeded_hash": seeded_hash,
    }
    rows: list[dict[str, object]] = []
    for name, predicate in functions.items():
        support = [n for n in range(2, 129) if predicate(n)]
        rows.append(
            {
                "support": name,
                "accepted_count_through_128": len(support),
                "accepted_sha256": hashlib.sha256(",".join(map(str, support)).encode("ascii")).hexdigest(),
                "transient_accept_loop_determinant": fraction_payload(exact_product(support, Fraction(1, 3), lambda n: 1)),
                "recurrent_cycle_formal_product": fraction_payload(exact_product(support, Fraction(1, 3), lambda n: n - 1)),
                "transient_prunes_to_diagonal": True,
                "recurrent_exact_clock_noncompact_when_support_has_unbounded_n": True,
            }
        )
    return rows


def evaluate(results: Path) -> dict[str, object]:
    audit = Audit()
    wilson = read_csv(results / "wilson_ledger.csv")
    audit.check("wilson:row_count", len(wilson) == 4095)
    primes: list[int] = []
    final_by_n: dict[int, int] = {}
    for expected_n, row in enumerate(wilson, start=2):
        n = int(row["n"])
        path = residues(n)
        prime = is_prime(n)
        accepts = path[-1] == n - 1
        if prime:
            primes.append(n)
        final_by_n[n] = path[-1]
        path_hash = hashlib.sha256(",".join(map(str, path)).encode("ascii")).hexdigest()
        audit.check(f"wilson:{n}:index", n == expected_n)
        audit.check(f"wilson:{n}:final", int(row["final_residue"]) == path[-1])
        audit.check(f"wilson:{n}:accept", bool(int(row["accepts"])) == accepts)
        audit.check(f"wilson:{n}:prime", bool(int(row["independent_prime_audit"])) == prime and accepts == prime)
        audit.check(f"wilson:{n}:cycle", int(row["cycle_length_if_accepted"]) == (n - 1 if prime else 0))
        audit.check(f"wilson:{n}:path_hash", row["residue_path_sha256"] == path_hash)
    audit.check("wilson:prime_count", len(primes) == 564)
    audit.check("wilson:largest_prime", primes[-1] == 4093)

    composites = read_csv(results / "composite_controls.csv")
    expected_composites = [
        {"n": str(n), "final_residue": str(final_by_n[n]), "target_residue": str(n - 1), "wilson_accepts": "0"}
        for n in range(2, 4097) if not is_prime(n)
    ]
    audit.check("controls:composite_count", len(composites) == 3531)
    audit.check("controls:composite_rows", composites == expected_composites)

    pseudoprimes = read_csv(results / "fermat_pseudoprime_controls.csv")
    expected_pseudoprimes = [
        {
            "n": str(n),
            "fermat_base2_residue": "1",
            "wilson_final_residue": str(final_by_n[n]),
            "wilson_accepts": "0",
        }
        for n in range(2, 4097)
        if not is_prime(n) and math.gcd(2, n) == 1 and pow(2, n - 1, n) == 1
    ]
    audit.check("controls:pseudoprime_count", len(pseudoprimes) == 13)
    audit.check("controls:pseudoprime_rows", pseudoprimes == expected_pseudoprimes)

    bare = read_csv(results / "bare_ufd_addition_failure.csv")
    audit.check("bare:row_count", len(bare) == 144)
    for row in bare:
        left, right = int(row["left"]), int(row["right"])
        audit.check(
            f"bare:{left}:{right}",
            row["X_left"] == monomial_text(left)
            and row["X_right"] == monomial_text(right)
            and row["required_target"] == monomial_text(left + right)
            and row["ordinary_polynomial_sum"] == f"({monomial_text(left)})+({monomial_text(right)})"
            and row["ordinary_sum_is_required_monic_monomial"] == "0",
        )

    matched = read_csv(results / "matched_semiring_clone.csv")
    audit.check("matched:row_count", len(matched) == 169)
    for row in matched:
        left, right = int(row["left"][2:]), int(row["right"][2:])
        audit.check(
            f"matched:{left}:{right}",
            row["transported_sum"] == f"y_{left + right}"
            and row["transported_product"] == f"y_{left * right}"
            and int(row["baseline_sum_index"]) == left + right
            and int(row["baseline_product_index"]) == left * right
            and row["matches"] == "1",
        )

    semirings = read_json(results / "semiring_controls.json")
    passing_names = [row["name"] for row in semirings if row["passes_source_lock"]]
    audit.check("semiring:row_count", len(semirings) == 7)
    audit.check("semiring:passing_names", passing_names == ["full_shift_positive_integer_semiring", "matched_transported_semiring_clone"])

    random_controls = read_json(results / "random_operation_controls.json")
    audit.check("random:exact_regeneration", random_controls == expected_random_controls())
    audit.check("random:32_fail", all(not row["passes_commutative_semiring_axioms"] for row in random_controls[:32]))
    audit.check("random:matched_pass", random_controls[-1]["passes_commutative_semiring_axioms"] is True)

    dilution = read_csv(results / "entropy_budget_dilution.csv")
    audit.check("dilution:row_count", len(dilution) == 564 * 3)
    for row in dilution:
        p, sigma = int(row["p"]), int(row["sigma"])
        length = p - 1
        expected_bound = format(math.exp(-sigma * math.log(p) / length), ".17g")
        audit.check(
            f"dilution:{p}:{sigma}",
            is_prime(p)
            and int(row["cycle_length"]) == length
            and row["total_roof"] == f"log({p})"
            and row["max_edge_weight_lower_bound"] == expected_bound
            and row["exact_expression"] == f"{p}^(-{sigma}/{length})",
        )

    traces = read_csv(results / "formal_trace_ledger.csv")
    audit.check("trace:row_count", len(traces) == 16)
    for power, row in enumerate(traces, start=1):
        contributions: list[str] = []
        value = Fraction(0, 1)
        for prime in primes:
            length = prime - 1
            if power % length == 0:
                exponent = 2 * power // length
                value += Fraction(length, prime**exponent)
                contributions.append(f"{length}/{prime}^{exponent}")
        audit.check(
            f"trace:{power}",
            int(row["power"]) == power
            and int(row["finite_contribution_count"]) == len(contributions)
            and row["formal_flat_trace_s2"] == f"{value.numerator}/{value.denominator}"
            and row["contributions"] == ";".join(contributions)
            and row["ordinary_operator_trace_owned"] == "0",
        )

    marker = read_json(results / "marker_change_certificate.json")
    marker_expected: list[dict[str, object]] = []
    support = [prime for prime in primes if prime <= 31]
    for z in (Fraction(1, 1), Fraction(1, 3)):
        raw = exact_product(support, z, lambda p: p - 1)
        induced = exact_product(support, z, lambda p: 1)
        marker_expected.append(
            {
                "cutoff": 31,
                "s": 2,
                "z": f"{z.numerator}/{z.denominator}",
                "raw_cycle_product": fraction_payload(raw),
                "induced_return_product": fraction_payload(induced),
                "equal": raw == induced,
            }
        )
    audit.check("marker:exact", marker == marker_expected)
    audit.check("marker:z1_equal", marker[0]["equal"] is True)
    audit.check("marker:z_third_differs", marker[1]["equal"] is False)

    wrappers = read_json(results / "universal_wrapper_controls.json")
    audit.check("wrappers:exact", wrappers == wrapper_expected(primes))
    audit.check("wrappers:five", len(wrappers) == 5)

    oracle = read_json(results / "source_oracle_certificate.json")
    audit.check("oracle:passes", oracle["passes"] is True)
    audit.check("oracle:no_forbidden", oracle["forbidden_seen"] == [] and oracle["external_file_or_network_calls"] == [])
    audit.check("oracle:literals", oracle["integer_literals"] == [0, 1, 2])
    audit.check(
        "oracle:source_hashes",
        oracle["candidate_source_sha256"] == {
            "source_remainder": "7ca41d286d1aa78d13a2ae254104730775e8e5afa0aa989bbbd4be7f4540de11",
            "wilson_accept": "d4ba8ef7863c196a03b5a7013e04a88978ac6e8e558ace612fe26f48ff2106c1",
            "wilson_residues": "50eeedb76c2996487828cd72bd37a9bc9e56b11cf94ea4be9e70c476ee9e0f61",
        },
    )

    summary = read_json(results / "summary.json")
    audit.check("summary:cutoff", summary["cutoff"] == 4096)
    audit.check("summary:counts", summary["accepted_count"] == 564 and summary["composite_control_count"] == 3531 and summary["base2_pseudoprime_control_count"] == 13)
    audit.check("summary:clones", summary["bare_ufd_addition_matches"] == 0 and summary["matched_clone_wilson_equal"] is True)
    audit.check("summary:route", summary["route_tuple"] == ROUTE_TUPLE and summary["overall"] == "ROUTE_A_REJECTED" and summary["route_b"] == "LOCKED")
    return audit.result()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", type=Path, required=True)
    args = parser.parse_args()
    payload = evaluate(args.results)
    (args.results / "evaluation.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if not payload["all_pass"]:
        raise SystemExit(json.dumps(payload["failures"], indent=2, sort_keys=True))
    print(json.dumps({key: payload[key] for key in ("check_count", "pass_count", "failure_count", "all_pass")}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
