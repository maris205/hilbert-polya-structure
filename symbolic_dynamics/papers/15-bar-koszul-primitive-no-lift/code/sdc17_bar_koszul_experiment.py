"""Exact SD-C17 bar-to-Koszul primitive-necklace audit.

The implementation uses only finite symbolic subset alphabets, cyclic words,
integer/Fraction arithmetic, and fixed-seed structural controls.  It never
loads or compares Riemann-zero data.
"""

from __future__ import annotations

import csv
import hashlib
import itertools
import json
import math
import random
from fractions import Fraction
from pathlib import Path
from typing import Sequence


SQUAREFREE_ENUM_CUTOFFS = tuple(range(2, 8))
STIRLING_CUTOFF = 12
REPETITION_CUTOFF = 8
RANDOM_ATOM_CUTOFFS = tuple(range(2, 9))
RANDOM_SEEDS = tuple(range(15100, 15116))
ZERO_DATA_USED = False


Edge = tuple[int, ...]
Word = tuple[Edge, ...]
Multidegree = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


def nonempty_subsets(atom_count: int) -> tuple[Edge, ...]:
    return tuple(
        subset
        for size in range(1, atom_count + 1)
        for subset in itertools.combinations(range(atom_count), size)
    )


def edge_sign(edge: Edge) -> int:
    return (-1) ** (len(edge) + 1)


def word_sign(word: Word) -> int:
    return math.prod(edge_sign(edge) for edge in word)


def word_multidegree(word: Word, atom_count: int) -> Multidegree:
    degree = [0] * atom_count
    for edge in word:
        for atom in edge:
            degree[atom] += 1
    return tuple(degree)


def rotations(word: Word) -> tuple[Word, ...]:
    return tuple(word[index:] + word[:index] for index in range(len(word)))


def canonical_necklace(word: Word) -> Word:
    return min(rotations(word))


def least_period(word: Word) -> int:
    length = len(word)
    for period in range(1, length + 1):
        if length % period == 0 and word == word[:period] * (length // period):
            return period
    raise AssertionError("unreachable")


def is_primitive(word: Word) -> bool:
    return least_period(word) == len(word)


def word_label(word: Word, atom_names: Sequence[str] | None = None) -> str:
    if atom_names is None:
        atom_names = tuple(chr(ord("a") + index) for index in range(26))
    return "".join(
        "[" + "".join(atom_names[atom] for atom in edge) + "]" for edge in word
    )


def necklaces_at_multidegree(target: Multidegree) -> tuple[Word, ...]:
    atom_count = len(target)
    alphabet = tuple(
        edge
        for edge in nonempty_subsets(atom_count)
        if all(int(atom in edge) <= target[atom] for atom in range(atom_count))
    )
    necklaces: set[Word] = set()
    for length in range(1, sum(target) + 1):
        for word in itertools.product(alphabet, repeat=length):
            if word_multidegree(word, atom_count) == target:
                necklaces.add(canonical_necklace(tuple(word)))
    return tuple(sorted(necklaces))


def primitive_necklaces_at_multidegree(target: Multidegree) -> tuple[Word, ...]:
    return tuple(word for word in necklaces_at_multidegree(target) if is_primitive(word))


def primitive_power_ledger_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    atom_names = ("p", "q")
    for target_name, target in (("pq", (1, 1)), ("p2q2", (2, 2))):
        for word in primitive_necklaces_at_multidegree(target):
            rows.append(
                {
                    "target": target_name,
                    "layer": "primitive_at_target",
                    "base_word": word_label(word, atom_names),
                    "base_multidegree": str(target),
                    "base_length": len(word),
                    "least_period": least_period(word),
                    "base_sign": word_sign(word),
                    "repetition": 1,
                    "powered_sign": word_sign(word),
                    "log_contribution": str(Fraction(word_sign(word), 1)),
                }
            )
    for word in primitive_necklaces_at_multidegree((1, 1)):
        rows.append(
            {
                "target": "p2q2",
                "layer": "r2_from_pq_primitive",
                "base_word": word_label(word, atom_names),
                "base_multidegree": str((1, 1)),
                "base_length": len(word),
                "least_period": least_period(word),
                "base_sign": word_sign(word),
                "repetition": 2,
                "powered_sign": word_sign(word) ** 2,
                "log_contribution": str(Fraction(word_sign(word) ** 2, 2)),
            }
        )
    return rows


def p2q2_certificate(rows: Sequence[dict[str, object]]) -> dict[str, object]:
    pq_primitive = [
        row
        for row in rows
        if row["target"] == "pq" and row["layer"] == "primitive_at_target"
    ]
    target_primitive = [
        row
        for row in rows
        if row["target"] == "p2q2" and row["layer"] == "primitive_at_target"
    ]
    repeats = [
        row
        for row in rows
        if row["target"] == "p2q2" and row["layer"] == "r2_from_pq_primitive"
    ]
    primitive_sum = sum(Fraction(str(row["log_contribution"])) for row in target_primitive)
    repetition_sum = sum(Fraction(str(row["log_contribution"])) for row in repeats)
    return {
        "pq_primitives": [
            {"word": row["base_word"], "sign": row["base_sign"]}
            for row in pq_primitive
        ],
        "pq_positive_count": sum(int(row["base_sign"]) > 0 for row in pq_primitive),
        "pq_negative_count": sum(int(row["base_sign"]) < 0 for row in pq_primitive),
        "pq_primitive_pairing_possible": len(pq_primitive) == 2
        and {int(row["base_sign"]) for row in pq_primitive} == {-1, 1},
        "p2q2_primitives": [
            {"word": row["base_word"], "sign": row["base_sign"]}
            for row in target_primitive
        ],
        "p2q2_positive_primitive_count": sum(
            int(row["base_sign"]) > 0 for row in target_primitive
        ),
        "p2q2_negative_primitive_count": sum(
            int(row["base_sign"]) < 0 for row in target_primitive
        ),
        "primitive_level_bijection_possible": sum(
            int(row["base_sign"]) > 0 for row in target_primitive
        )
        == sum(int(row["base_sign"]) < 0 for row in target_primitive),
        "p2q2_primitive_sum": str(primitive_sum),
        "pq_r2_repetition_sum": str(repetition_sum),
        "complete_log_coefficient": str(primitive_sum + repetition_sum),
        "cross_layer_cancellation_required": primitive_sum != 0
        and primitive_sum + repetition_sum == 0,
    }


def set_partitions(items: tuple[int, ...]) -> tuple[tuple[Edge, ...], ...]:
    """All unordered set partitions in canonical block order."""

    if not items:
        return ((),)
    first, rest = items[0], items[1:]
    results: set[tuple[Edge, ...]] = set()
    for partition in set_partitions(rest):
        results.add(tuple(sorted(((first,),) + partition)))
        for index in range(len(partition)):
            blocks = list(partition)
            blocks[index] = tuple(sorted((first,) + blocks[index]))
            results.add(tuple(sorted(blocks)))
    return tuple(sorted(results))


def canonical_block_cycle(blocks: tuple[Edge, ...]) -> tuple[Edge, ...]:
    return min(blocks[index:] + blocks[:index] for index in range(len(blocks)))


def cyclic_partition_orbits(atom_count: int) -> tuple[tuple[Edge, ...], ...]:
    orbits: set[tuple[Edge, ...]] = set()
    for partition in set_partitions(tuple(range(atom_count))):
        anchor = min(partition)
        others = tuple(block for block in partition if block != anchor)
        for ordering in itertools.permutations(others):
            orbits.add(canonical_block_cycle((anchor,) + ordering))
    return tuple(sorted(orbits))


def cyclic_partition_sign(block_cycle: tuple[Edge, ...], atom_count: int) -> int:
    return (-1) ** (atom_count + len(block_cycle))


def apply_atom_permutation(
    block_cycle: tuple[Edge, ...], permutation: tuple[int, ...]
) -> tuple[Edge, ...]:
    image = tuple(
        tuple(sorted(permutation[atom] for atom in block)) for block in block_cycle
    )
    return canonical_block_cycle(image)


def block_cycle_label(block_cycle: tuple[Edge, ...]) -> str:
    names = ("p", "q", "r", "s", "t", "u", "v", "w")
    return "".join("[" + "".join(names[a] for a in block) + "]" for block in block_cycle)


def action_orbit_decomposition(
    objects: Sequence[tuple[Edge, ...]],
    permutations: Sequence[tuple[int, ...]],
) -> tuple[tuple[tuple[Edge, ...], ...], ...]:
    """Return the exact atom-permutation orbits inside a finite object set."""

    object_set = set(objects)
    remaining = set(objects)
    decomposition = []
    while remaining:
        representative = min(remaining)
        orbit = {
            apply_atom_permutation(representative, permutation)
            for permutation in permutations
        }
        if not orbit <= object_set:
            raise AssertionError("the supplied object set is not action invariant")
        decomposition.append(tuple(sorted(orbit)))
        remaining -= orbit
    return tuple(sorted(decomposition, key=lambda orbit: (len(orbit), orbit)))


def s3_character_certificate() -> dict[str, object]:
    orbits = cyclic_partition_orbits(3)
    positive = tuple(orbit for orbit in orbits if cyclic_partition_sign(orbit, 3) > 0)
    negative = tuple(orbit for orbit in orbits if cyclic_partition_sign(orbit, 3) < 0)
    representatives = {
        "identity": (0, 1, 2),
        "transposition": (1, 0, 2),
        "three_cycle": (1, 2, 0),
    }
    fixed = {}
    virtual_character = []
    for name, permutation in representatives.items():
        positive_fixed = sum(
            apply_atom_permutation(orbit, permutation) == orbit for orbit in positive
        )
        negative_fixed = sum(
            apply_atom_permutation(orbit, permutation) == orbit for orbit in negative
        )
        fixed[name] = {
            "positive_fixed": positive_fixed,
            "negative_fixed": negative_fixed,
            "virtual": positive_fixed - negative_fixed,
        }
        virtual_character.append(positive_fixed - negative_fixed)

    class_sizes = (1, 3, 2)
    irreducible_characters = {
        "trivial": (1, 1, 1),
        "sign": (1, -1, 1),
        "standard": (2, 0, -1),
    }
    decomposition = {
        name: str(
            Fraction(
                sum(
                    size * value * irreducible
                    for size, value, irreducible in zip(
                        class_sizes, virtual_character, character
                    )
                ),
                6,
            )
        )
        for name, character in irreducible_characters.items()
    }

    positive_sorted = tuple(sorted(positive, key=block_cycle_label))
    negative_sorted = tuple(sorted(negative, key=block_cycle_label))
    s3_permutations = tuple(itertools.permutations(range(3)))
    positive_action_orbits = action_orbit_decomposition(
        positive_sorted, s3_permutations
    )
    negative_action_orbits = action_orbit_decomposition(
        negative_sorted, s3_permutations
    )
    lex_pairing = dict(zip(positive_sorted, negative_sorted))
    lex_failures = []
    for permutation in s3_permutations:
        failures = 0
        for source, target in lex_pairing.items():
            permuted_source = apply_atom_permutation(source, permutation)
            permuted_target = apply_atom_permutation(target, permutation)
            if lex_pairing[permuted_source] != permuted_target:
                failures += 1
        lex_failures.append(
            {"permutation": str(permutation), "equivariance_failures": failures}
        )

    return {
        "positive_orbits": [block_cycle_label(orbit) for orbit in positive_sorted],
        "negative_orbits": [block_cycle_label(orbit) for orbit in negative_sorted],
        "positive_count": len(positive),
        "negative_count": len(negative),
        "positive_action_orbit_sizes": [
            len(orbit) for orbit in positive_action_orbits
        ],
        "negative_action_orbit_sizes": [
            len(orbit) for orbit in negative_action_orbits
        ],
        "positive_action_orbit_decomposition": [
            [block_cycle_label(item) for item in orbit]
            for orbit in positive_action_orbits
        ],
        "negative_action_orbit_decomposition": [
            [block_cycle_label(item) for item in orbit]
            for orbit in negative_action_orbits
        ],
        "fixed_characters": fixed,
        "virtual_character_class_order": {
            "classes": ["identity", "transposition", "three_cycle"],
            "values": virtual_character,
        },
        "virtual_representation": "1 + sign - standard",
        "irreducible_multiplicities": decomposition,
        "equivariant_bijection_possible": virtual_character == [0, 0, 0],
        "lexicographic_pairing": [
            {"positive": block_cycle_label(source), "negative": block_cycle_label(target)}
            for source, target in lex_pairing.items()
        ],
        "lexicographic_equivariance_audit": lex_failures,
        "lexicographic_pairing_natural": all(
            row["equivariance_failures"] == 0 for row in lex_failures
        ),
    }


def stirling_second_kind(n: int, k: int) -> int:
    if n == k == 0:
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    table = [[0] * (k + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for row in range(1, n + 1):
        for column in range(1, min(row, k) + 1):
            table[row][column] = (
                column * table[row - 1][column] + table[row - 1][column - 1]
            )
    return table[n][k]


def squarefree_stirling_rows() -> list[dict[str, object]]:
    rows = []
    for atom_count in range(1, STIRLING_CUTOFF + 1):
        contributions = [
            (-1) ** (atom_count + block_count)
            * math.factorial(block_count - 1)
            * stirling_second_kind(atom_count, block_count)
            for block_count in range(1, atom_count + 1)
        ]
        rows.append(
            {
                "k": atom_count,
                "signed_contributions_by_block_count": ";".join(
                    map(str, contributions)
                ),
                "coefficient": sum(contributions),
                "expected": 1 if atom_count == 1 else 0,
                "identity_exact": sum(contributions)
                == (1 if atom_count == 1 else 0),
            }
        )
    return rows


def cyclic_partition_count_rows() -> list[dict[str, object]]:
    rows = []
    for atom_count in SQUAREFREE_ENUM_CUTOFFS:
        orbits = cyclic_partition_orbits(atom_count)
        for block_count in range(1, atom_count + 1):
            actual = sum(len(orbit) == block_count for orbit in orbits)
            expected = math.factorial(block_count - 1) * stirling_second_kind(
                atom_count, block_count
            )
            sign = (-1) ** (atom_count + block_count)
            rows.append(
                {
                    "k": atom_count,
                    "block_count": block_count,
                    "actual_cyclic_orbits": actual,
                    "expected_cyclic_orbits": expected,
                    "count_exact": actual == expected,
                    "sign": sign,
                    "signed_contribution": sign * actual,
                }
            )
    return rows


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("incompatible matrix dimensions")
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(len(right)))
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    if len(left) != len(right) or any(
        len(left_row) != len(right_row)
        for left_row, right_row in zip(left, right)
    ):
        raise ValueError("incompatible matrix dimensions")
    return tuple(
        tuple(left_value + right_value for left_value, right_value in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def matrix_power(matrix: Matrix, exponent: int) -> Matrix:
    if exponent < 0 or not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("matrix power requires a square matrix and nonnegative exponent")
    identity = tuple(
        tuple(int(row == column) for column in range(len(matrix)))
        for row in range(len(matrix))
    )
    result = identity
    base = matrix
    power = exponent
    while power:
        if power % 2:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        power //= 2
    return result


def even_odd_supertrace(matrix: Matrix) -> int:
    if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
        raise ValueError("the frozen block has one even and one odd state")
    return matrix[0][0] - matrix[1][1]


def contractible_block_certificate(repetition_cutoff: int) -> dict[str, object]:
    """Compute the frozen two-term contraction in the basis (even, odd)."""

    differential: Matrix = ((0, 1), (0, 0))
    homotopy: Matrix = ((0, 0), (1, 0))
    identity: Matrix = ((1, 0), (0, 1))
    transfer_coefficient: Matrix = identity
    contraction = matrix_add(
        matrix_multiply(differential, homotopy),
        matrix_multiply(homotopy, differential),
    )
    commutator_left = matrix_multiply(differential, transfer_coefficient)
    commutator_right = matrix_multiply(transfer_coefficient, differential)
    supertraces = [
        {
            "r": repetition,
            "coefficient": even_odd_supertrace(
                matrix_power(transfer_coefficient, repetition)
            ),
        }
        for repetition in range(1, repetition_cutoff + 1)
    ]
    return {
        "basis_order": ["even", "odd"],
        "differential_matrix": differential,
        "homotopy_matrix": homotopy,
        "identity_matrix": identity,
        "dh_plus_hd_matrix": contraction,
        "contraction_exact": contraction == identity,
        "transfer_rule": "T=w times identity; matrices store the coefficient of w",
        "transfer_coefficient_matrix": transfer_coefficient,
        "differential_commutes_with_transfer": commutator_left == commutator_right,
        "supertrace_coefficients": supertraces,
        "all_power_supertraces_zero": all(
            row["coefficient"] == 0 for row in supertraces
        ),
        "mixed_length_two_primitive": "absent",
    }


def scalar_supertrace_rows() -> list[dict[str, object]]:
    contractible = contractible_block_certificate(REPETITION_CUTOFF)
    block_supertraces = {
        int(row["r"]): int(row["coefficient"])
        for row in contractible["supertrace_coefficients"]
    }
    rows = []
    for repetition in range(1, REPETITION_CUTOFF + 1):
        scalar_negative = (-1) ** repetition
        odd_supertrace = -1
        paired_primitive_power = Fraction(1 + (-1) ** repetition, repetition)
        rows.append(
            {
                "r": repetition,
                "negative_scalar_repeat_coefficient": scalar_negative,
                "odd_line_supertrace_coefficient": odd_supertrace,
                "single_edge_difference": scalar_negative - odd_supertrace,
                "scalar_and_parity_agree": scalar_negative == odd_supertrace,
                "pq_paired_primitive_power_contribution": str(
                    paired_primitive_power
                ),
                "non_power_compatible_expected": "0",
                "non_power_matching_leak": str(paired_primitive_power),
                "scalar_pair_total_trace": 0,
                "contractible_even_odd_supertrace": block_supertraces[repetition],
            }
        )
    return rows


def scalar_supertrace_certificate(rows: Sequence[dict[str, object]]) -> dict[str, object]:
    row_two = next(row for row in rows if row["r"] == 2)
    contractible = contractible_block_certificate(REPETITION_CUTOFF)
    return {
        "single_negative_edge": {
            "scalar_rule": "(-w)^r",
            "odd_supertrace_rule": "-w^r",
            "even_repetition_mismatch_count": sum(
                not bool(row["scalar_and_parity_agree"]) for row in rows
            ),
            "r2_scalar_coefficient": row_two["negative_scalar_repeat_coefficient"],
            "r2_odd_supertrace_coefficient": row_two[
                "odd_line_supertrace_coefficient"
            ],
            "r2_difference": row_two["single_edge_difference"],
        },
        "scalar_two_edge_alphabet": {
            "length_one_primitives": ["[+w]", "[-w]"],
            "length_two_mixed_primitive": "[+w][-w]",
            "length_two_mixed_weight": "-w^2",
            "r2_length_one_repeat_sum": "w^2",
            "complete_degree_two_trace": "0",
        },
        "contractible_even_odd_block": contractible,
        "ledger_isomorphism_possible": False,
        "non_power_matching_r2_leak": row_two["non_power_matching_leak"],
    }


def subset_scalar_sum(values: Sequence[Fraction]) -> Fraction:
    total = Fraction(0)
    for edge in nonempty_subsets(len(values)):
        total += edge_sign(edge) * math.prod(values[atom] for atom in edge)
    return total


def rational_hash(value: Fraction) -> str:
    return hashlib.sha256(
        f"{value.numerator}/{value.denominator}".encode()
    ).hexdigest()


def random_inventory_rows() -> list[dict[str, object]]:
    rows = []
    for atom_count in RANDOM_ATOM_CUTOFFS:
        for seed in RANDOM_SEEDS:
            rng = random.Random(seed + 1009 * atom_count)
            values = tuple(
                Fraction(rng.randint(1, 9), rng.randint(10, 23))
                for _ in range(atom_count)
            )
            permutation = list(range(atom_count))
            rng.shuffle(permutation)
            shuffled = tuple(values[index] for index in permutation)
            edge_sum = subset_scalar_sum(values)
            determinant = 1 - edge_sum
            expected = math.prod(1 - value for value in values)
            shuffled_determinant = 1 - subset_scalar_sum(shuffled)
            rows.append(
                {
                    "k": atom_count,
                    "seed": seed,
                    "variable_values": ";".join(map(str, values)),
                    "presentation_permutation": str(tuple(permutation)),
                    "edge_sum_sha256": rational_hash(edge_sum),
                    "determinant_sha256": rational_hash(determinant),
                    "exact_product_identity": determinant == expected,
                    "presentation_shuffle_invariant": shuffled_determinant
                    == determinant,
                    "mixed_squarefree_log_coefficient": 0,
                    "proves_too_much": True,
                }
            )
    return rows


def write_csv(path: Path, rows: Sequence[dict[str, object]]) -> None:
    if not rows:
        raise ValueError("cannot write empty CSV")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def generate(output_directory: Path) -> dict[str, object]:
    output_directory.mkdir(parents=True, exist_ok=True)
    primitive_rows = primitive_power_ledger_rows()
    p2q2 = p2q2_certificate(primitive_rows)
    s3 = s3_character_certificate()
    stirling_rows = squarefree_stirling_rows()
    cyclic_rows = cyclic_partition_count_rows()
    supertrace_rows = scalar_supertrace_rows()
    supertrace = scalar_supertrace_certificate(supertrace_rows)
    random_rows = random_inventory_rows()

    write_csv(output_directory / "primitive_power_ledger.csv", primitive_rows)
    write_json(output_directory / "p2q2_certificate.json", p2q2)
    write_json(output_directory / "s3_character_certificate.json", s3)
    write_csv(output_directory / "squarefree_stirling_identity.csv", stirling_rows)
    write_csv(output_directory / "cyclic_partition_counts.csv", cyclic_rows)
    write_csv(output_directory / "scalar_supertrace_control.csv", supertrace_rows)
    write_json(output_directory / "scalar_supertrace_certificate.json", supertrace)
    write_csv(output_directory / "random_inventory_controls.csv", random_rows)

    cyclic_totals = {
        atom_count: sum(
            int(row["actual_cyclic_orbits"])
            for row in cyclic_rows
            if row["k"] == atom_count
        )
        for atom_count in SQUAREFREE_ENUM_CUTOFFS
    }
    summary = {
        "candidate": "SD-C17",
        "scope": "Symbolic Dynamics only",
        "zero_data_used": ZERO_DATA_USED,
        "frozen": {
            "squarefree_enumeration_cutoffs": SQUAREFREE_ENUM_CUTOFFS,
            "stirling_cutoff": STIRLING_CUTOFF,
            "repetition_cutoff": REPETITION_CUTOFF,
            "random_atom_cutoffs": RANDOM_ATOM_CUTOFFS,
            "random_seeds": RANDOM_SEEDS,
        },
        "counts": {
            "primitive_power_rows": len(primitive_rows),
            "cyclic_partition_rows": len(cyclic_rows),
            "cyclic_orbit_totals": cyclic_totals,
            "stirling_rows": len(stirling_rows),
            "scalar_supertrace_rows": len(supertrace_rows),
            "random_inventory_rows": len(random_rows),
        },
        "pq_p2q2": p2q2,
        "pqr_s3": s3,
        "scalar_supertrace": supertrace,
        "general_squarefree_identity_exact": all(
            bool(row["identity_exact"]) for row in stirling_rows
        ),
        "cyclic_partition_counts_exact": all(
            bool(row["count_exact"]) for row in cyclic_rows
        ),
        "random_controls_exact": all(
            bool(row["exact_product_identity"])
            and bool(row["presentation_shuffle_invariant"])
            for row in random_rows
        ),
        "decision": {
            "GO_SCALAR_KOSZUL_DETERMINANT": True,
            "GO_PRIMITIVE_LEVEL_INVOLUTION": False,
            "STOP_PRIMITIVE_LEVEL_INVOLUTION": True,
            "STOP_EQUIVARIANT_SIGN_REVERSAL": True,
            "STOP_PARITY_SUBSTITUTION": True,
            "STOP_ARITHMETIC_SELECTIVITY": True,
            "PROVES_TOO_MUCH": True,
            "ROUTE_B_LOCKED": True,
        },
        "strongest_positive": (
            "The squarefree subset alphabet gives the exact scalar Koszul "
            "determinant D_k=product_i(1-x_i) and all mixed squarefree log "
            "coefficients vanish."
        ),
        "strongest_failure": (
            "At p^2q^2 cancellation crosses primitive degree and r=2 power "
            "layers, while at pqr the virtual S3 character is nonzero; hence "
            "there is no natural primitive-level sign-reversing involution."
        ),
        "next_smallest_test": (
            "Freeze a genuine pre-cyclic chain complex or quotient whose "
            "contraction commutes with powers and atom permutations; otherwise "
            "promote the representation obstruction to all k."
        ),
    }
    write_json(output_directory / "summary.json", summary)

    root = output_directory.parent
    paths = sorted((root / "code").glob("*.py")) + sorted(
        path
        for path in output_directory.iterdir()
        if path.is_file() and path.name != "SHA256SUMS.txt"
    )
    checksums = [
        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(root)}"
        for path in paths
    ]
    (output_directory / "SHA256SUMS.txt").write_text(
        "\n".join(checksums) + "\n", encoding="utf-8"
    )
    return summary


if __name__ == "__main__":
    generate(Path(__file__).resolve().parents[1] / "results")
