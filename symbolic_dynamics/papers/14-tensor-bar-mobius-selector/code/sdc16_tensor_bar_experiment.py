"""Exact SD-C16 tensor-bar/Mobius experiment.

The experiment stays inside the tensor-full-shift symbolic family. It never
loads Riemann zeros and never tunes a phase, a root, or a cutoff. Arithmetic
predicates are computed from tensor factorisation of ``F_m`` (equivalently,
integer factorisation), not from a stored prime table. Formal/exact bar-word
certificates and high-precision numerical checks are deliberately separate.
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
from typing import Callable, Iterable, Iterator, Sequence


CUTOFFS = (16, 32, 64, 128)
SHUFFLE_SEEDS = tuple(range(14000, 14016))
RANDOM_INVENTORY_SEEDS = tuple(range(14100, 14116))
SOURCE_EXPONENT = 2
DETERMINANT_Z = Fraction(1, 3)
PLANTED_BLOCK_LENGTH = 12
INCIDENCE_CUTOFFS = (64, 128, 256, 512)
ENTROPY_RELABEL_SEEDS = tuple(range(14200, 14208))
BAR_FORMAL_CUTOFF = 512
BAR_RAW_WORD_LENGTHS = (1, 2, 4, 8, 16, 32, 64)
BAR_RAW_POINTS = (1.75 + 0j, 1.8 + 0j, 2.0 + 0j, 1.9 + 0.6j)
BAR_ENDPOINT_POINTS = (
    1.1 + 0j,
    1.25 + 0j,
    1.5 + 0j,
    1.7 + 0j,
    1.25 + 0.75j,
)
BAR_ENDPOINT_CUTOFFS = (100, 1_000, 10_000, 100_000)
BAR_TRACE_POINTS = (1.75 + 0j, 2.0 + 0j, 1.25 + 0j)
BAR_TRACE_Z = (0.25, 0.5, 1.0)
BAR_TRACE_REPETITIONS = (1, 2, 4, 8, 16, 32, 64, 128, 256)
UNIVERSAL_CONTROL_SEED = 14300
HIGH_PRECISION_DIGITS = 80
ZERO_DATA_USED = False


def is_tensor_indecomposable(value: int) -> bool:
    """Whether the full shift F_value is tensor indecomposable."""

    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def first_tensor_indecomposables(count: int) -> tuple[int, ...]:
    values: list[int] = []
    candidate = 2
    while len(values) < count:
        if is_tensor_indecomposable(candidate):
            values.append(candidate)
        candidate += 1
    return tuple(values)


def first_tensor_decomposables(count: int) -> tuple[int, ...]:
    values: list[int] = []
    candidate = 4
    while len(values) < count:
        if not is_tensor_indecomposable(candidate):
            values.append(candidate)
        candidate += 1
    return tuple(values)


def factor_exponents(value: int) -> tuple[tuple[int, int], ...]:
    factors: list[tuple[int, int]] = []
    remainder = value
    divisor = 2
    while divisor * divisor <= remainder:
        exponent = 0
        while remainder % divisor == 0:
            exponent += 1
            remainder //= divisor
        if exponent:
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if remainder > 1:
        factors.append((remainder, 1))
    return tuple(factors)


def divisors(value: int) -> tuple[int, ...]:
    small = []
    large = []
    divisor = 1
    while divisor * divisor <= value:
        if value % divisor == 0:
            small.append(divisor)
            if divisor * divisor != value:
                large.append(value // divisor)
        divisor += 1
    return tuple(small + list(reversed(large)))


def incidence_mobius(cutoff: int) -> tuple[int, ...]:
    """Möbius function computed only from the truncated divisibility poset."""

    if cutoff < 1:
        raise ValueError("cutoff must contain the tensor unit")
    mu = [0] * (cutoff + 1)
    mu[1] = 1
    for value in range(2, cutoff + 1):
        mu[value] = -sum(mu[divisor] for divisor in divisors(value)[:-1])
    return tuple(mu)


EntropyVector = dict[int, int]


def entropy_vector(value: int) -> EntropyVector:
    """Exact formal topological entropy in the tensor-prime log basis."""

    return dict(factor_exponents(value))


def add_scaled_vector(target: EntropyVector, source: EntropyVector, scale: int) -> None:
    for atom, coefficient in source.items():
        target[atom] = target.get(atom, 0) + scale * coefficient
        if target[atom] == 0:
            del target[atom]


def tensor_lambda_vector(
    value: int,
    mu: Sequence[int],
    entropy_labels: dict[int, EntropyVector] | None = None,
) -> EntropyVector:
    """Exact (mu_tensor * h)(value), optionally under a label control."""

    result: EntropyVector = {}
    for divisor in divisors(value):
        quotient = value // divisor
        vector = (
            entropy_vector(quotient)
            if entropy_labels is None
            else entropy_labels[quotient]
        )
        add_scaled_vector(result, vector, mu[divisor])
    return result


def encode_entropy_vector(vector: EntropyVector) -> str:
    return ";".join(f"{atom}:{coefficient}" for atom, coefficient in sorted(vector.items()))


def prime_power_base(value: int) -> int | None:
    factors = factor_exponents(value)
    return factors[0][0] if len(factors) == 1 else None


def expected_tensor_lambda(value: int) -> EntropyVector:
    base = prime_power_base(value)
    return {} if base is None else {base: 1}


def is_divisor_closed_inventory(values: Sequence[int], augment_unit: bool = False) -> bool:
    source = set(values)
    if augment_unit:
        source.add(1)
    if 1 not in source:
        return False
    return all(set(divisors(value)).issubset(source) for value in source)


def total_factor_depth(value: int) -> int:
    return sum(exponent for _, exponent in factor_exponents(value))


def distinct_factor_depth(value: int) -> int:
    return len(factor_exponents(value))


def valuation(value: int, base_atom: int) -> int:
    exponent = 0
    while value % base_atom == 0:
        exponent += 1
        value //= base_atom
    return exponent


def entropy_bin(value: int) -> int:
    """floor(log_2(value)), derived from entropy relative to F_2."""

    return value.bit_length() - 1


def no_intermediate_tensor_atom(left: int, right: int) -> bool:
    if not (left < right):
        return False
    if not (is_tensor_indecomposable(left) and is_tensor_indecomposable(right)):
        return False
    return not any(is_tensor_indecomposable(value) for value in range(left + 1, right))


def primary_inventory(count: int) -> tuple[int, ...]:
    return first_tensor_indecomposables(count)


def composite_inventory(count: int) -> tuple[int, ...]:
    return first_tensor_decomposables(count)


def shuffled_inventory(count: int, seed: int) -> tuple[int, ...]:
    values = list(first_tensor_indecomposables(count))
    random.Random(seed + 1009 * count).shuffle(values)
    return tuple(values)


def random_increasing_inventory(count: int, seed: int) -> tuple[int, ...]:
    rng = random.Random(seed + 1013 * count)
    values = rng.sample(range(2, 16 * count + 2), count)
    return tuple(sorted(values))


def prefix_preserving_shuffle(count: int, prefix_length: int) -> tuple[int, ...]:
    """A nontrivial shuffle sharing a prescribed primary prefix."""

    values = list(first_tensor_indecomposables(count))
    if prefix_length >= count - 1:
        raise ValueError("prefix leaves no nontrivial tail")
    return tuple(values[:prefix_length] + list(reversed(values[prefix_length:])))


def block_preserving_shuffle(count: int, block_length: int) -> tuple[int, ...]:
    """Shuffle blocks while preserving the source order inside every block."""

    values = list(first_tensor_indecomposables(count))
    blocks = [values[index : index + block_length] for index in range(0, count, block_length)]
    if len(blocks) < 2:
        raise ValueError("need at least two blocks")
    blocks = blocks[1:] + blocks[:1]
    return tuple(value for block in blocks for value in block)


def edge_goodness(values: Sequence[int]) -> tuple[int, ...]:
    """The intrinsic ordered-consecutive-tensor-atom edge descriptor."""

    return tuple(
        int(no_intermediate_tensor_atom(left, right))
        for left, right in zip(values[:-1], values[1:])
    )


ChargeRule = Callable[[Sequence[int]], tuple[int, ...]]


def binary_edge_rule(predicate: Callable[[int, int], bool]) -> ChargeRule:
    return lambda values: tuple(
        2 if predicate(left, right) else 3 for left, right in zip(values[:-1], values[1:])
    )


def constant_rule(values: Sequence[int]) -> tuple[int, ...]:
    return (2,) * (len(values) - 1)


def factor_depth_sum_rule(values: Sequence[int]) -> tuple[int, ...]:
    return tuple(
        total_factor_depth(left) + total_factor_depth(right)
        for left, right in zip(values[:-1], values[1:])
    )


def run_rule(values: Sequence[int], run_length: int) -> tuple[int, ...]:
    """Causal finite-radius rule: charge 2 after run_length good edges."""

    bits = edge_goodness(values)
    charges = []
    for index in range(len(bits)):
        start = index - run_length + 1
        active = start >= 0 and all(bits[start : index + 1])
        charges.append(2 if active else 3)
    return tuple(charges)


RULES: dict[str, ChargeRule] = {
    "constant": constant_rule,
    "factor_depth_sum": factor_depth_sum_rule,
    "indecomposable_pair": binary_edge_rule(
        lambda left, right: total_factor_depth(left) == total_factor_depth(right) == 1
    ),
    "factor_depth_equal": binary_edge_rule(
        lambda left, right: total_factor_depth(left) == total_factor_depth(right)
    ),
    "distinct_depth_equal": binary_edge_rule(
        lambda left, right: distinct_factor_depth(left) == distinct_factor_depth(right)
    ),
    "tensor_coprime": binary_edge_rule(lambda left, right: math.gcd(left, right) == 1),
    "v2_equal": binary_edge_rule(
        lambda left, right: valuation(left, 2) == valuation(right, 2)
    ),
    "v2_parity_equal": binary_edge_rule(
        lambda left, right: valuation(left, 2) % 2 == valuation(right, 2) % 2
    ),
    "entropy_increasing": binary_edge_rule(lambda left, right: left < right),
    "entropy_bin_equal": binary_edge_rule(
        lambda left, right: entropy_bin(left) == entropy_bin(right)
    ),
    "ordered_consecutive_tensor_atoms": binary_edge_rule(no_intermediate_tensor_atom),
    **{
        f"consecutive_run_{run_length}": (
            lambda values, run_length=run_length: run_rule(values, run_length)
        )
        for run_length in range(2, 9)
    },
}


def masses(values: Sequence[int]) -> tuple[Fraction, ...]:
    return tuple(Fraction(1, value**SOURCE_EXPONENT) for value in values)


def exact_mode_two_coefficient(values: Sequence[int], charges: Sequence[int]) -> Fraction:
    """Exact [w^2] det(I-zL(w)) for a charge field bounded below by 2."""

    if len(charges) != len(values) - 1:
        raise ValueError("charge length mismatch")
    if any(charge < 2 for charge in charges):
        raise ValueError("formula assumes all round-trip charges are at least 2")
    xs = masses(values)
    deltas = tuple(1 - DETERMINANT_Z * x for x in xs)
    product = math.prod(deltas)
    coefficient = Fraction(0)
    for index, charge in enumerate(charges):
        if charge == 2:
            amplitude = (xs[index] + xs[index + 1]) / 2
            coefficient -= (
                DETERMINANT_Z**2
                * amplitude**2
                * product
                / deltas[index]
                / deltas[index + 1]
            )
    return coefficient


def exact_euler_constant(values: Sequence[int]) -> Fraction:
    return math.prod(1 - DETERMINANT_Z * x for x in masses(values))


def exact_continuant(values: Sequence[int], charges: Sequence[int]) -> dict[int, Fraction]:
    """Full exact matching/continuant polynomial in the character variable."""

    if len(charges) != len(values) - 1:
        raise ValueError("charge length mismatch")
    xs = masses(values)
    previous_two: dict[int, Fraction] = {0: Fraction(1)}
    previous_one: dict[int, Fraction] = {0: 1 - DETERMINANT_Z * xs[0]}
    for index in range(1, len(values)):
        diagonal = 1 - DETERMINANT_Z * xs[index]
        amplitude = (xs[index - 1] + xs[index]) / 2
        edge_factor = -(DETERMINANT_Z**2) * amplitude**2
        current: dict[int, Fraction] = {}
        for degree, coefficient in previous_one.items():
            current[degree] = current.get(degree, Fraction(0)) + diagonal * coefficient
        for degree, coefficient in previous_two.items():
            shifted = degree + charges[index - 1]
            current[shifted] = current.get(shifted, Fraction(0)) + edge_factor * coefficient
        previous_two, previous_one = previous_one, {
            degree: coefficient for degree, coefficient in current.items() if coefficient
        }
    return previous_one


def polynomial_certificate(polynomial: dict[int, Fraction]) -> dict[str, object]:
    encoded = "\n".join(
        f"{degree}:{coefficient.numerator}/{coefficient.denominator}"
        for degree, coefficient in sorted(polynomial.items())
    )
    return {
        "degrees": sorted(polynomial),
        "term_count": len(polynomial),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
    }


def rational_certificate(value: Fraction, include_value: bool = False) -> dict[str, object]:
    encoded = f"{value.numerator}/{value.denominator}"
    result: dict[str, object] = {
        "exact_zero": value == 0,
        "sign": (value > 0) - (value < 0),
        "numerator_digits": len(str(abs(value.numerator))),
        "denominator_digits": len(str(value.denominator)),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
    }
    if include_value:
        result["value"] = encoded
    return result


def oriented_gauge_charges(values: Sequence[int], potential: Callable[[int, int], int]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """1+df and 1-df; every round trip is exactly 2."""

    forward = []
    backward = []
    for index in range(len(values) - 1):
        difference = potential(index + 1, values[index + 1]) - potential(index, values[index])
        forward.append(1 + difference)
        backward.append(1 - difference)
    return tuple(forward), tuple(backward)


GAUGE_POTENTIALS: dict[str, Callable[[int, int], int]] = {
    "rank": lambda index, value: index,
    "factor_depth": lambda index, value: total_factor_depth(value),
    "v2": lambda index, value: valuation(value, 2),
    "entropy_bin": lambda index, value: entropy_bin(value),
}


def cone_certificate(roundtrip_charges: Sequence[int]) -> dict[str, object]:
    """Exact neutral-ledger criterion and a Diophantine leakage witness."""

    charges = tuple(roundtrip_charges)
    if not charges:
        raise ValueError("empty charge field")
    if all(charge > 0 for charge in charges) or all(charge < 0 for charge in charges):
        return {"safe": True, "witness": None}
    if 0 in charges:
        index = charges.index(0)
        return {
            "safe": False,
            "witness": {"edges": [index], "multiplicities": [1], "total": 0},
        }
    positive_index = next(index for index, charge in enumerate(charges) if charge > 0)
    negative_index = next(index for index, charge in enumerate(charges) if charge < 0)
    left, right = sorted((positive_index, negative_index))
    interval = charges[left : right + 1]
    interval_sum = sum(interval)
    if interval_sum == 0:
        multiplicities = [1] * len(interval)
    elif interval_sum > 0:
        local_negative = next(index for index, charge in enumerate(interval) if charge < 0)
        negative_size = -interval[local_negative]
        multiplicities = [negative_size] * len(interval)
        multiplicities[local_negative] += interval_sum
    else:
        local_positive = next(index for index, charge in enumerate(interval) if charge > 0)
        positive_size = interval[local_positive]
        multiplicities = [positive_size] * len(interval)
        multiplicities[local_positive] += -interval_sum
    total = sum(
        multiplicity * charge
        for multiplicity, charge in zip(multiplicities, interval)
    )
    return {
        "safe": False,
        "witness": {
            "edges": list(range(left, right + 1)),
            "multiplicities": multiplicities,
            "connected_support": True,
            "total": total,
        },
    }


def control_inventories(count: int, include_adversarial: bool = True) -> Iterator[tuple[str, int | str, tuple[int, ...]]]:
    yield "composites", "deterministic", composite_inventory(count)
    for seed in SHUFFLE_SEEDS:
        yield "shuffled_primes", seed, shuffled_inventory(count, seed)
    for seed in RANDOM_INVENTORY_SEEDS:
        yield "random_increasing", seed, random_increasing_inventory(count, seed)
    if include_adversarial:
        yield (
            "prefix_preserving_shuffle",
            PLANTED_BLOCK_LENGTH,
            prefix_preserving_shuffle(count, min(PLANTED_BLOCK_LENGTH, count - 2)),
        )
        if count >= 2 * PLANTED_BLOCK_LENGTH:
            yield (
                "block_preserving_shuffle",
                PLANTED_BLOCK_LENGTH,
                block_preserving_shuffle(count, PLANTED_BLOCK_LENGTH),
            )


def incidence_ledger_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for cutoff in INCIDENCE_CUTOFFS:
        mu = incidence_mobius(cutoff)
        for value in range(1, cutoff + 1):
            actual = tensor_lambda_vector(value, mu)
            expected = expected_tensor_lambda(value)
            mobius_sum = sum(mu[divisor] for divisor in divisors(value))
            rows.append(
                {
                    "X": cutoff,
                    "n": value,
                    "mu_tensor": mu[value],
                    "mobius_inverse_exact": mobius_sum == int(value == 1),
                    "factor_type": (
                        "unit"
                        if value == 1
                        else "prime_power"
                        if prime_power_base(value) is not None
                        else "mixed_prime"
                    ),
                    "lambda_tensor_vector": encode_entropy_vector(actual),
                    "expected_vector": encode_entropy_vector(expected),
                    "lambda_exact": actual == expected,
                    "support_nonzero": bool(actual),
                }
            )
    return rows


def incidence_control_rows() -> list[dict[str, object]]:
    inventories: list[tuple[str, int | str, int, tuple[int, ...]]] = []
    for count in CUTOFFS:
        inventories.append(("tensor_primes", "primary", count, primary_inventory(count)))
        inventories.append(("composites", "deterministic", count, composite_inventory(count)))
        for seed in SHUFFLE_SEEDS:
            inventories.append(("shuffled_primes", seed, count, shuffled_inventory(count, seed)))
        for seed in RANDOM_INVENTORY_SEEDS:
            inventories.append(
                (
                    "random_increasing",
                    seed,
                    count,
                    random_increasing_inventory(count, seed),
                )
            )
    largest_value = max(max(values) for _, _, _, values in inventories)
    mu = incidence_mobius(largest_value)
    rows: list[dict[str, object]] = []
    for inventory_name, control_id, count, values in inventories:
        actual = [tensor_lambda_vector(value, mu) for value in values]
        expected = [expected_tensor_lambda(value) for value in values]
        prime_power_count = sum(bool(vector) for vector in expected)
        mixed_count = len(values) - prime_power_count
        nonzero_count = sum(bool(vector) for vector in actual)
        rows.append(
            {
                "inventory": inventory_name,
                "control_id": control_id,
                "N": count,
                "max_value": max(values),
                "raw_inventory_divisor_closed": is_divisor_closed_inventory(values),
                "unit_augmented_divisor_closed": is_divisor_closed_inventory(
                    values, augment_unit=True
                ),
                "ambient_tensor_monoid_used": True,
                "prime_power_count": prime_power_count,
                "mixed_prime_count": mixed_count,
                "lambda_nonzero_count": nonzero_count,
                "support_exact": actual == expected,
                "order_invariant": all(
                    tensor_lambda_vector(value, mu) == expected_tensor_lambda(value)
                    for value in sorted(values)
                ),
            }
        )
    return rows


def vector_sum(left: EntropyVector, right: EntropyVector) -> EntropyVector:
    result = dict(left)
    add_scaled_vector(result, right, 1)
    return result


def entropy_relabel_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for cutoff in INCIDENCE_CUTOFFS:
        mu = incidence_mobius(cutoff)
        normal_compatibility = all(
            entropy_vector(left * right)
            == vector_sum(entropy_vector(left), entropy_vector(right))
            for left in range(1, cutoff + 1)
            for right in range(1, cutoff // left + 1)
        )
        for seed in ENTROPY_RELABEL_SEEDS:
            permutation = list(range(2, cutoff + 1))
            random.Random(seed + 1019 * cutoff).shuffle(permutation)
            labels: dict[int, EntropyVector] = {1: {}}
            labels.update(
                {
                    source: entropy_vector(target)
                    for source, target in zip(range(2, cutoff + 1), permutation)
                }
            )
            mismatch_count = 0
            mixed_leak_count = 0
            prime_power_wrong_count = 0
            for value in range(2, cutoff + 1):
                actual = tensor_lambda_vector(value, mu, labels)
                expected = expected_tensor_lambda(value)
                if actual != expected:
                    mismatch_count += 1
                if prime_power_base(value) is None and actual:
                    mixed_leak_count += 1
                if prime_power_base(value) is not None and actual != expected:
                    prime_power_wrong_count += 1
            compatibility_pairs = 0
            tested_pairs = 0
            for left in range(1, cutoff + 1):
                for right in range(1, cutoff // left + 1):
                    tested_pairs += 1
                    if labels[left * right] == vector_sum(labels[left], labels[right]):
                        compatibility_pairs += 1
            rows.append(
                {
                    "X": cutoff,
                    "seed": seed,
                    "normal_entropy_monoid_compatible": normal_compatibility,
                    "random_label_compatible_pairs": compatibility_pairs,
                    "tested_multiplicative_pairs": tested_pairs,
                    "lambda_mismatch_count": mismatch_count,
                    "mixed_prime_leak_count": mixed_leak_count,
                    "prime_power_wrong_count": prime_power_wrong_count,
                    "control_breaks_selector": mismatch_count > 0
                    and mixed_leak_count > 0
                    and prime_power_wrong_count > 0,
                }
            )
    return rows


def incidence_summary(
    ledger_rows: Sequence[dict[str, object]],
    control_rows: Sequence[dict[str, object]],
    relabel_rows: Sequence[dict[str, object]],
) -> dict[str, object]:
    largest = max(INCIDENCE_CUTOFFS)
    largest_rows = [row for row in ledger_rows if row["X"] == largest]
    values_by_cutoff = {
        cutoff: {
            int(row["n"]): str(row["lambda_tensor_vector"])
            for row in ledger_rows
            if row["X"] == cutoff
        }
        for cutoff in INCIDENCE_CUTOFFS
    }
    cutoff_stable = all(
        values_by_cutoff[larger][value] == vector
        for index, smaller in enumerate(INCIDENCE_CUTOFFS)
        for larger in INCIDENCE_CUTOFFS[index + 1 :]
        for value, vector in values_by_cutoff[smaller].items()
    )
    inventory_boundary = {}
    for inventory_name in (
        "tensor_primes",
        "composites",
        "shuffled_primes",
        "random_increasing",
    ):
        selected = [row for row in control_rows if row["inventory"] == inventory_name]
        inventory_boundary[inventory_name] = {
            "rows": len(selected),
            "raw_divisor_closed_all": all(
                bool(row["raw_inventory_divisor_closed"]) for row in selected
            ),
            "unit_augmented_divisor_closed_all": all(
                bool(row["unit_augmented_divisor_closed"]) for row in selected
            ),
            "ambient_support_exact_all": all(bool(row["support_exact"]) for row in selected),
            "order_invariant_all": all(bool(row["order_invariant"]) for row in selected),
        }
    return {
        "object": "Lambda_tensor = mu_tensor * h on the full-shift tensor divisibility monoid",
        "data_type": "global incidence-algebra entropy weight",
        "not_a_local_cocycle": True,
        "not_a_character_or_fourier_mode": True,
        "not_a_determinant": True,
        "principal_ideal_cutoffs": INCIDENCE_CUTOFFS,
        "ledger_rows": len(ledger_rows),
        "mobius_inverse_exact_all": all(
            bool(row["mobius_inverse_exact"]) for row in ledger_rows
        ),
        "lambda_identity_exact_all": all(bool(row["lambda_exact"]) for row in ledger_rows),
        "cutoff_stable_exact": cutoff_stable,
        "largest_cutoff": {
            "X": largest,
            "prime_power_support_count": sum(
                row["factor_type"] == "prime_power" for row in largest_rows
            ),
            "mixed_prime_zero_count": sum(
                row["factor_type"] == "mixed_prime" and not row["support_nonzero"]
                for row in largest_rows
            ),
        },
        "inventory_source_lock_boundary": inventory_boundary,
        "entropy_relabel_controls": {
            "rows": len(relabel_rows),
            "normal_entropy_monoid_compatible_all": all(
                bool(row["normal_entropy_monoid_compatible"]) for row in relabel_rows
            ),
            "all_random_relabels_break_selector": all(
                bool(row["control_breaks_selector"]) for row in relabel_rows
            ),
            "minimum_mixed_leak_count": min(
                int(row["mixed_prime_leak_count"]) for row in relabel_rows
            ),
        },
        "decision": {
            "GO_GLOBAL_INCIDENCE_SELECTOR": True,
            "GO_LOCAL_CHARACTER_SELECTOR": False,
            "ROUTE_B_LOCKED": True,
        },
        "claim_boundary": (
            "The exact von-Mangoldt support is intrinsic to tensor divisibility "
            "plus compatible entropy, but it supplies no local cocycle, Bloch "
            "mode, Fredholm determinant, divisor theorem, or operator."
        ),
    }


def rule_audit_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for count in CUTOFFS:
        inventories = [("tensor_primes", "primary", primary_inventory(count))]
        inventories.extend(control_inventories(count))
        for inventory_name, control_id, values in inventories:
            for rule_name, rule in RULES.items():
                charges = rule(values)
                coefficient = exact_mode_two_coefficient(values, charges)
                certificate = rational_certificate(coefficient)
                rows.append(
                    {
                        "rule": rule_name,
                        "inventory": inventory_name,
                        "control_id": control_id,
                        "N": count,
                        "mode": 2,
                        "coefficient_exact_zero": certificate["exact_zero"],
                        "coefficient_sign": certificate["sign"],
                        "coefficient_sha256": certificate["sha256"],
                        "numerator_digits": certificate["numerator_digits"],
                        "denominator_digits": certificate["denominator_digits"],
                        "first_degree": min(charges),
                        "active_edge_count": sum(charge == 2 for charge in charges),
                        "neutral_euler_safe": cone_certificate(charges)["safe"],
                    }
                )
    return rows


def aggregate_rule_decisions(rows: Sequence[dict[str, object]]) -> list[dict[str, object]]:
    decisions: list[dict[str, object]] = []
    for rule_name in RULES:
        selected = [row for row in rows if row["rule"] == rule_name]
        primary = [row for row in selected if row["inventory"] == "tensor_primes"]
        naive_controls = [
            row
            for row in selected
            if row["inventory"] in {"composites", "shuffled_primes", "random_increasing"}
        ]
        adversarial = [
            row
            for row in selected
            if row["inventory"] in {"prefix_preserving_shuffle", "block_preserving_shuffle"}
        ]
        prime_nonzero_all = all(not bool(row["coefficient_exact_zero"]) for row in primary)
        naive_zero_all = all(bool(row["coefficient_exact_zero"]) for row in naive_controls)
        adversarial_zero_all = all(bool(row["coefficient_exact_zero"]) for row in adversarial)
        decisions.append(
            {
                "rule": rule_name,
                "prime_nonzero_all_cutoffs": prime_nonzero_all,
                "naive_controls_zero_all": naive_zero_all,
                "adversarial_shuffles_zero_all": adversarial_zero_all,
                "naive_selectivity_pass": prime_nonzero_all and naive_zero_all,
                "robust_selectivity_pass": (
                    prime_nonzero_all and naive_zero_all and adversarial_zero_all
                ),
                "leaking_naive_rows": sum(
                    not bool(row["coefficient_exact_zero"]) for row in naive_controls
                ),
                "leaking_adversarial_rows": sum(
                    not bool(row["coefficient_exact_zero"]) for row in adversarial
                ),
            }
        )
    return decisions


def local_window_codes(bits: Sequence[int], radius: int = 1) -> tuple[int, ...]:
    padded = (0,) * radius + tuple(bits) + (0,) * radius
    width = 2 * radius + 1
    codes = []
    for index in range(len(bits)):
        code = 0
        for bit in padded[index : index + width]:
            code = 2 * code + bit
        codes.append(code)
    return tuple(codes)


def truth_table_response(mask: int, codes: Sequence[int]) -> bool:
    return any((mask >> code) & 1 for code in codes)


def exhaustive_radius_one_summary() -> dict[str, object]:
    primary_codes = [local_window_codes(edge_goodness(primary_inventory(count))) for count in CUTOFFS]
    naive_codes: list[tuple[int, ...]] = []
    adversarial_codes: list[tuple[int, ...]] = []
    for count in CUTOFFS:
        for inventory_name, _, values in control_inventories(count):
            codes = local_window_codes(edge_goodness(values))
            if inventory_name in {"composites", "shuffled_primes", "random_increasing"}:
                naive_codes.append(codes)
            else:
                adversarial_codes.append(codes)
    prime_active = []
    naive_pass = []
    robust_pass = []
    for mask in range(256):
        primary_response = all(truth_table_response(mask, codes) for codes in primary_codes)
        if primary_response:
            prime_active.append(mask)
        naive_clear = all(not truth_table_response(mask, codes) for codes in naive_codes)
        adversarial_clear = all(
            not truth_table_response(mask, codes) for codes in adversarial_codes
        )
        if primary_response and naive_clear:
            naive_pass.append(mask)
        if primary_response and naive_clear and adversarial_clear:
            robust_pass.append(mask)
    return {
        "radius": 1,
        "window_width": 3,
        "truth_tables_exhausted": 256,
        "primary_active_count": len(prime_active),
        "naive_selectivity_pass_count": len(naive_pass),
        "naive_selectivity_pass_masks": naive_pass,
        "robust_selectivity_pass_count": len(robust_pass),
        "robust_selectivity_pass_masks": robust_pass,
        "certificate": (
            "The primary word has only the padded/local codes 011, 111, and "
            "110. Prefix- and block-preserving nontrivial shuffles collectively "
            "reproduce all three exact witness codes."
        ),
    }


def mealy_machines(state_count: int) -> Iterator[tuple[tuple[int, ...], tuple[int, ...]]]:
    """All binary-input, binary-output labelled deterministic machines."""

    slots = 2 * state_count
    for transitions in itertools.product(range(state_count), repeat=slots):
        for outputs in itertools.product((0, 1), repeat=slots):
            yield tuple(transitions), tuple(outputs)


def mealy_response(
    bits: Sequence[int],
    transitions: Sequence[int],
    outputs: Sequence[int],
    initial_state: int = 0,
) -> bool:
    state_count = len(transitions) // 2
    if len(outputs) != 2 * state_count:
        raise ValueError("machine table mismatch")
    state = initial_state
    active = False
    for bit in bits:
        slot = 2 * state + bit
        active = active or bool(outputs[slot])
        state = transitions[slot]
    return active


def exhaustive_mealy_summary() -> dict[str, object]:
    primary_words = [edge_goodness(primary_inventory(count)) for count in CUTOFFS]
    naive_words: list[tuple[int, ...]] = []
    adversarial_words_by_state_count: dict[int, list[tuple[int, ...]]] = {1: [], 2: []}
    for count in CUTOFFS:
        for inventory_name, _, values in control_inventories(count, include_adversarial=False):
            if inventory_name != "tensor_primes":
                naive_words.append(edge_goodness(values))
        for state_count in (1, 2):
            prefix_length = state_count + 2
            values = prefix_preserving_shuffle(count, prefix_length)
            adversarial_words_by_state_count[state_count].append(edge_goodness(values))

    by_state_count: dict[str, object] = {}
    total_robust = 0
    for state_count in (1, 2):
        total = primary_active = naive_pass = robust_pass = 0
        for transitions, outputs in mealy_machines(state_count):
            total += 1
            primary_response = all(
                mealy_response(word, transitions, outputs) for word in primary_words
            )
            if primary_response:
                primary_active += 1
            naive_clear = all(
                not mealy_response(word, transitions, outputs) for word in naive_words
            )
            adversarial_clear = all(
                not mealy_response(word, transitions, outputs)
                for word in adversarial_words_by_state_count[state_count]
            )
            if primary_response and naive_clear:
                naive_pass += 1
            if primary_response and naive_clear and adversarial_clear:
                robust_pass += 1
        total_robust += robust_pass
        by_state_count[str(state_count)] = {
            "machines_exhausted": total,
            "primary_active_count": primary_active,
            "naive_selectivity_pass_count": naive_pass,
            "robust_selectivity_pass_count": robust_pass,
        }
    return {
        "alphabet": "ordered-consecutive-tensor-atom bit",
        "output": "round-trip charge 2 when output=1, otherwise 3",
        "terminal_marker_allowed": False,
        "shift_stationarity_required": True,
        "by_state_count": by_state_count,
        "robust_selectivity_pass_total": total_robust,
        "certificate": (
            "On the homogeneous primary word, any response of a Q-state machine "
            "appears within the preperiod/cycle reached in at most Q+1 steps; a "
            "prefix-preserving nontrivial shuffle copies those steps."
        ),
    }


def dirichlet_convolution_prefix(
    left: Sequence[Fraction], right: Sequence[Fraction], cutoff: int
) -> list[Fraction]:
    """Exact Dirichlet convolution through ``cutoff``."""

    result = [Fraction(0) for _ in range(cutoff + 1)]
    for divisor in range(1, cutoff + 1):
        if left[divisor] == 0:
            continue
        for quotient in range(1, cutoff // divisor + 1):
            if right[quotient] != 0:
                result[divisor * quotient] += left[divisor] * right[quotient]
    return result


def dirichlet_inverse_prefix(
    coefficients: Sequence[Fraction], cutoff: int
) -> list[Fraction]:
    """Exact inverse of a Dirichlet series whose unit coefficient is one."""

    if coefficients[1] != 1:
        raise ValueError("Dirichlet inversion requires unit coefficient one")
    inverse = [Fraction(0) for _ in range(cutoff + 1)]
    inverse[1] = Fraction(1)
    for value in range(2, cutoff + 1):
        inverse[value] = -sum(
            inverse[divisor] * coefficients[value // divisor]
            for divisor in divisors(value)
            if divisor < value
        )
    return inverse


def bar_word_prefixes(
    coefficients: Sequence[Fraction], cutoff: int
) -> tuple[list[list[Fraction]], list[Fraction]]:
    """Alternating nonunit bar words, grouped by their product endpoint."""

    nonunit = list(coefficients[: cutoff + 1])
    nonunit[1] = Fraction(0)
    max_length = max(1, int(math.log2(cutoff)))
    word_layers: list[list[Fraction]] = []
    current = nonunit
    cumulative = [Fraction(0) for _ in range(cutoff + 1)]
    for length in range(1, max_length + 1):
        word_layers.append(current)
        sign = 1 if length % 2 == 1 else -1
        for value in range(2, cutoff + 1):
            cumulative[value] += sign * current[value]
        current = dirichlet_convolution_prefix(current, nonunit, cutoff)
    return word_layers, cumulative


def bar_formal_coefficient_rows(cutoff: int = BAR_FORMAL_CUTOFF) -> list[dict[str, object]]:
    coefficients = [Fraction(0) for _ in range(cutoff + 1)]
    coefficients[1] = Fraction(1)
    for value in range(2, cutoff + 1):
        coefficients[value] = Fraction(1)
    inverse = dirichlet_inverse_prefix(coefficients, cutoff)
    word_layers, bar_coefficients = bar_word_prefixes(coefficients, cutoff)
    mu = incidence_mobius(cutoff)
    rows = []
    for value in range(1, cutoff + 1):
        layer_counts = [int(layer[value]) for layer in word_layers]
        bar_value = Fraction(0) if value == 1 else bar_coefficients[value]
        determinant_value = Fraction(1) if value == 1 else -bar_value
        rows.append(
            {
                "n": value,
                "factor_type": (
                    "unit"
                    if value == 1
                    else "prime_power"
                    if prime_power_base(value) is not None
                    else "mixed_prime"
                ),
                "max_nonzero_word_length": (
                    0 if value == 1 else total_factor_depth(value)
                ),
                "ordered_word_counts": ";".join(map(str, layer_counts)),
                "bar_endpoint_coefficient": str(bar_value),
                "expected_minus_mu": str(-mu[value]) if value > 1 else "0",
                "bar_coefficient_exact": (
                    bar_value == (Fraction(0) if value == 1 else -mu[value])
                ),
                "determinant_coefficient": str(determinant_value),
                "expected_mu": str(mu[value]),
                "determinant_coefficient_exact": determinant_value == mu[value],
                "independent_inverse_coefficient": str(inverse[value]),
                "independent_inverse_exact": determinant_value == inverse[value],
            }
        )
    return rows


def mobius_linear_sieve(cutoff: int) -> tuple[int, ...]:
    """Independent O(N) Möbius implementation for endpoint numerics."""

    mu = [0] * (cutoff + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (cutoff + 1)
    for value in range(2, cutoff + 1):
        if not composite[value]:
            primes.append(value)
            mu[value] = -1
        for prime in primes:
            product = value * prime
            if product > cutoff:
                break
            composite[product] = True
            if value % prime == 0:
                mu[product] = 0
                break
            mu[product] = -mu[value]
    return tuple(mu)


def mp_complex(value: complex, mp: object) -> object:
    return mp.mpc(str(value.real), str(value.imag))


def mp_text(value: object, mp: object, digits: int = 30) -> str:
    return mp.nstr(value, digits)


def bar_sigma_threshold() -> str:
    import mpmath as mp

    with mp.workdps(HIGH_PRECISION_DIGITS):
        root = mp.findroot(lambda sigma: mp.zeta(sigma) - 2, (mp.mpf("1.7"), mp.mpf("1.8")))
        return mp.nstr(root, 70)


def bar_raw_convergence_rows() -> list[dict[str, object]]:
    import mpmath as mp

    rows: list[dict[str, object]] = []
    with mp.workdps(HIGH_PRECISION_DIGITS):
        sigma_bar = mp.mpf(bar_sigma_threshold())
        for source_s in BAR_RAW_POINTS:
            source = mp_complex(source_s, mp)
            absolute_base = mp.zeta(mp.mpf(str(source_s.real))) - 1
            if not absolute_base < 1:
                raise AssertionError("raw point is outside the absolute word region")
            alphabet_sum = mp.zeta(source) - 1
            closed_f = alphabet_sum / (1 + alphabet_sum)
            target_d = 1 / mp.zeta(source)
            partial = mp.mpc(0)
            previous_length = 0
            for length in BAR_RAW_WORD_LENGTHS:
                for word_length in range(previous_length + 1, length + 1):
                    partial += (-1) ** (word_length + 1) * alphabet_sum**word_length
                previous_length = length
                determinant = 1 - partial
                exact_remainder = ((-1) ** length) * alphabet_sum ** (length + 1) / (
                    1 + alphabet_sum
                )
                absolute_tail_bound = absolute_base ** (length + 1) / (1 - absolute_base)
                rows.append(
                    {
                        "s": str(source_s),
                        "sigma": source_s.real,
                        "sigma_bar": mp_text(sigma_bar, mp),
                        "raw_region_certified": source_s.real > float(sigma_bar),
                        "word_length": length,
                        "alphabet_sum": mp_text(alphabet_sum, mp),
                        "F_partial": mp_text(partial, mp),
                        "F_closed": mp_text(closed_f, mp),
                        "actual_F_residual": float(abs(closed_f - partial)),
                        "exact_remainder_residual": float(
                            abs((closed_f - partial) - exact_remainder)
                        ),
                        "absolute_geometric_tail_bound": float(absolute_tail_bound),
                        "D_partial": mp_text(determinant, mp),
                        "target_one_over_zeta": mp_text(target_d, mp),
                        "D_residual": float(abs(determinant - target_d)),
                        "closed_D_identity_residual": float(abs((1 - closed_f) - target_d)),
                        "precision_digits": HIGH_PRECISION_DIGITS,
                    }
                )
    return rows


def bar_exact_rational_certificates() -> dict[str, object]:
    endpoint_cutoff = 32
    alphabet_sum = sum(
        (Fraction(1, value * value) for value in range(2, endpoint_cutoff + 1)),
        Fraction(0),
    )
    closed_f = alphabet_sum / (1 + alphabet_sum)
    closed_d = 1 - closed_f
    rows = []
    for length in BAR_RAW_WORD_LENGTHS[:-1]:
        partial = sum(
            ((-1) ** (word_length + 1) * alphabet_sum**word_length
             for word_length in range(1, length + 1)),
            Fraction(0),
        )
        remainder = ((-1) ** length) * alphabet_sum ** (length + 1) / (
            1 + alphabet_sum
        )
        rows.append(
            {
                "word_length": length,
                "partial": rational_certificate(partial),
                "remainder": rational_certificate(remainder),
                "exact_geometric_identity": closed_f - partial == remainder,
            }
        )
    return {
        "endpoint_cutoff": endpoint_cutoff,
        "source_s": 2,
        "alphabet_sum": rational_certificate(alphabet_sum, include_value=True),
        "F_closed": rational_certificate(closed_f, include_value=True),
        "D_closed": rational_certificate(closed_d, include_value=True),
        "reciprocal_identity_exact": closed_d == 1 / (1 + alphabet_sum),
        "word_length_rows": rows,
    }


def bar_endpoint_completion_rows() -> list[dict[str, object]]:
    import mpmath as mp

    maximum_cutoff = max(BAR_ENDPOINT_CUTOFFS)
    mu = mobius_linear_sieve(maximum_cutoff)
    rows: list[dict[str, object]] = []
    with mp.workdps(HIGH_PRECISION_DIGITS):
        for source_s in BAR_ENDPOINT_POINTS:
            source = mp_complex(source_s, mp)
            target_d = 1 / mp.zeta(source)
            partial_d = mp.mpc(1)
            next_cutoff_index = 0
            for value in range(2, maximum_cutoff + 1):
                if mu[value]:
                    partial_d += mu[value] * mp.power(value, -source)
                if value == BAR_ENDPOINT_CUTOFFS[next_cutoff_index]:
                    cutoff = value
                    sigma = mp.mpf(str(source_s.real))
                    absolute_tail_bound = mp.power(cutoff, 1 - sigma) / (sigma - 1)
                    rows.append(
                        {
                            "s": str(source_s),
                            "sigma": source_s.real,
                            "cutoff": cutoff,
                            "completion_region": source_s.real > 1,
                            "D_grouped_partial": mp_text(partial_d, mp),
                            "F_grouped_partial": mp_text(1 - partial_d, mp),
                            "target_one_over_zeta": mp_text(target_d, mp),
                            "D_residual_observation": float(abs(partial_d - target_d)),
                            "absolute_tail_majorant": float(absolute_tail_bound),
                            "precision_digits": HIGH_PRECISION_DIGITS,
                            "evidence_label": "NUMERICAL_OBSERVATION",
                        }
                    )
                    next_cutoff_index += 1
                    if next_cutoff_index == len(BAR_ENDPOINT_CUTOFFS):
                        break
    return rows


def bar_trace_log_rows() -> list[dict[str, object]]:
    import mpmath as mp

    rows: list[dict[str, object]] = []
    sigma_bar = float(bar_sigma_threshold())
    with mp.workdps(HIGH_PRECISION_DIGITS):
        for source_s in BAR_TRACE_POINTS:
            source = mp_complex(source_s, mp)
            f_value = 1 - 1 / mp.zeta(source)
            readout = "raw_bar" if source_s.real > sigma_bar else "endpoint_grouped"
            for determinant_z in BAR_TRACE_Z:
                z_value = mp.mpf(str(determinant_z))
                ratio = z_value * f_value
                if not abs(ratio) < 1:
                    raise AssertionError("trace-log point outside repetition disk")
                target = -mp.log(1 - ratio)
                partial = mp.mpc(0)
                previous = 0
                for repetition_cutoff in BAR_TRACE_REPETITIONS:
                    for repetition in range(previous + 1, repetition_cutoff + 1):
                        partial += ratio**repetition / repetition
                    previous = repetition_cutoff
                    rows.append(
                        {
                            "s": str(source_s),
                            "readout": readout,
                            "z": determinant_z,
                            "abs_zF": float(abs(ratio)),
                            "repetition_cutoff": repetition_cutoff,
                            "trace_log_partial": mp_text(partial, mp),
                            "trace_log_target": mp_text(target, mp),
                            "trace_log_residual": float(abs(partial - target)),
                            "determinant_reconstruction_residual": float(
                                abs(mp.exp(-partial) - (1 - ratio))
                            ),
                            "precision_digits": HIGH_PRECISION_DIGITS,
                        }
                    )
    return rows


def generic_coefficient_control(
    kind: str, cutoff: int, seed: int = UNIVERSAL_CONTROL_SEED
) -> list[Fraction]:
    coefficients = [Fraction(0) for _ in range(cutoff + 1)]
    coefficients[1] = Fraction(1)
    rng = random.Random(seed)
    if kind == "all_objects":
        for value in range(2, cutoff + 1):
            coefficients[value] = Fraction(1)
    elif kind == "composite_only":
        for value in range(2, cutoff + 1):
            coefficients[value] = Fraction(int(not is_tensor_indecomposable(value)))
    elif kind == "prime_only":
        for value in range(2, cutoff + 1):
            coefficients[value] = Fraction(int(is_tensor_indecomposable(value)))
    elif kind == "random_positive":
        for value in range(2, cutoff + 1):
            coefficients[value] = Fraction(rng.randint(1, 5), rng.randint(2, 9))
    elif kind == "random_increasing_support":
        support = set(rng.sample(range(2, cutoff + 1), cutoff // 4))
        for value in range(2, cutoff + 1):
            coefficients[value] = Fraction(int(value in support))
    elif kind == "synthetic_signed":
        for value in range(2, cutoff + 1):
            coefficients[value] = Fraction((-1) ** value * ((value % 3) + 1), 5)
    elif kind == "shuffled_ramp":
        ramp = [Fraction((value % 7) + 1, 7) for value in range(2, cutoff + 1)]
        rng.shuffle(ramp)
        for value, coefficient in zip(range(2, cutoff + 1), ramp):
            coefficients[value] = coefficient
    else:
        raise ValueError(kind)
    return coefficients


def bar_universal_control_rows(cutoff: int = 128) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for kind in (
        "all_objects",
        "composite_only",
        "prime_only",
        "random_positive",
        "random_increasing_support",
        "synthetic_signed",
        "shuffled_ramp",
    ):
        coefficients = generic_coefficient_control(kind, cutoff)
        inverse = dirichlet_inverse_prefix(coefficients, cutoff)
        _, bar_coefficients = bar_word_prefixes(coefficients, cutoff)
        mismatch = []
        convolution = dirichlet_convolution_prefix(coefficients, inverse, cutoff)
        for value in range(2, cutoff + 1):
            if bar_coefficients[value] != -inverse[value]:
                mismatch.append(value)
        convolution_mismatch = [
            value
            for value in range(1, cutoff + 1)
            if convolution[value] != int(value == 1)
        ]
        encoded = "\n".join(
            f"{value}:{inverse[value].numerator}/{inverse[value].denominator}"
            for value in range(1, cutoff + 1)
        )
        rows.append(
            {
                "control": kind,
                "cutoff": cutoff,
                "nonunit_input_count": sum(
                    coefficients[value] != 0 for value in range(2, cutoff + 1)
                ),
                "bar_inverse_mismatch_count": len(mismatch),
                "convolution_mismatch_count": len(convolution_mismatch),
                "inverse_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
                "universal_inversion_exact": not mismatch and not convolution_mismatch,
                "proves_too_much": True,
            }
        )
    for name, alphabet_sum in (
        ("scalar_positive", Fraction(2, 5)),
        ("scalar_near_boundary", Fraction(9, 10)),
        ("scalar_signed", Fraction(-1, 4)),
    ):
        closed_f = alphabet_sum / (1 + alphabet_sum)
        rows.append(
            {
                "control": name,
                "cutoff": "not_applicable",
                "nonunit_input_count": "not_applicable",
                "bar_inverse_mismatch_count": 0,
                "convolution_mismatch_count": 0,
                "inverse_sha256": hashlib.sha256(
                    f"{(1-closed_f).numerator}/{(1-closed_f).denominator}".encode()
                ).hexdigest(),
                "universal_inversion_exact": 1 - closed_f == 1 / (1 + alphabet_sum),
                "proves_too_much": True,
            }
        )
    return rows


def exact_certificates() -> dict[str, object]:
    count = 16
    selected: dict[str, object] = {}
    inventories = {
        "tensor_primes": primary_inventory(count),
        "composites": composite_inventory(count),
        "shuffled_seed_14000": shuffled_inventory(count, 14000),
        "random_seed_14100": random_increasing_inventory(count, 14100),
        "prefix_preserving": prefix_preserving_shuffle(count, 6),
        "block_preserving": block_preserving_shuffle(count, 8),
    }
    for rule_name in (
        "constant",
        "factor_depth_sum",
        "ordered_consecutive_tensor_atoms",
        "consecutive_run_3",
        "consecutive_run_4",
    ):
        selected[rule_name] = {}
        for inventory_name, values in inventories.items():
            coefficient = exact_mode_two_coefficient(values, RULES[rule_name](values))
            selected[rule_name][inventory_name] = rational_certificate(
                coefficient, include_value=True
            )

    gauge = {}
    values = primary_inventory(count)
    baseline_coefficient = exact_mode_two_coefficient(values, constant_rule(values))
    baseline_polynomial = exact_continuant(values, constant_rule(values))
    for name, potential in GAUGE_POTENTIALS.items():
        forward, backward = oriented_gauge_charges(values, potential)
        roundtrip = tuple(left + right for left, right in zip(forward, backward))
        coefficient = exact_mode_two_coefficient(values, roundtrip)
        polynomial = exact_continuant(values, roundtrip)
        gauge[name] = {
            "roundtrip_all_two": all(charge == 2 for charge in roundtrip),
            "same_exact_coefficient": coefficient == baseline_coefficient,
            "same_full_exact_determinant": polynomial == baseline_polynomial,
            "oriented_charge_min": min(forward + backward),
            "oriented_charge_max": max(forward + backward),
            "coefficient": rational_certificate(coefficient, include_value=True),
            "determinant": polynomial_certificate(polynomial),
        }

    return {
        "source_exponent": SOURCE_EXPONENT,
        "determinant_z": f"{DETERMINANT_Z.numerator}/{DETERMINANT_Z.denominator}",
        "N": count,
        "selected_mode_two_coefficients": selected,
        "gauge_coboundaries": gauge,
        "euler_constant_primary": rational_certificate(
            exact_euler_constant(values), include_value=True
        ),
        "cone_examples": {
            "positive": cone_certificate((2, 3, 5)),
            "negative": cone_certificate((-2, -3, -5)),
            "zero_edge": cone_certificate((2, 0, 3)),
            "mixed_sign": cone_certificate((2, -3, 5)),
        },
    }


def write_csv(path: Path, rows: Sequence[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError("empty rows")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def generate(output_directory: Path) -> dict[str, object]:
    output_directory.mkdir(parents=True, exist_ok=True)
    rows = rule_audit_rows()
    decisions = aggregate_rule_decisions(rows)
    radius_summary = exhaustive_radius_one_summary()
    mealy_summary = exhaustive_mealy_summary()
    certificates = exact_certificates()
    incidence_ledger = incidence_ledger_rows()
    incidence_controls = incidence_control_rows()
    entropy_relabels = entropy_relabel_rows()
    global_incidence = incidence_summary(
        incidence_ledger, incidence_controls, entropy_relabels
    )
    bar_formal = bar_formal_coefficient_rows()
    bar_raw = bar_raw_convergence_rows()
    bar_exact = bar_exact_rational_certificates()
    bar_endpoint = bar_endpoint_completion_rows()
    bar_trace = bar_trace_log_rows()
    bar_controls = bar_universal_control_rows()

    write_csv(output_directory / "rule_audit.csv", rows)
    write_csv(output_directory / "rule_decisions.csv", decisions)
    write_json(output_directory / "finite_radius_summary.json", radius_summary)
    write_json(output_directory / "automatic_transducer_summary.json", mealy_summary)
    write_json(output_directory / "exact_certificates.json", certificates)
    write_csv(output_directory / "global_incidence_ledger.csv", incidence_ledger)
    write_csv(output_directory / "global_incidence_controls.csv", incidence_controls)
    write_csv(output_directory / "entropy_relabel_controls.csv", entropy_relabels)
    write_json(output_directory / "global_incidence_summary.json", global_incidence)
    write_csv(output_directory / "bar_formal_coefficients.csv", bar_formal)
    write_csv(output_directory / "bar_raw_convergence.csv", bar_raw)
    write_json(output_directory / "bar_exact_certificates.json", bar_exact)
    write_csv(output_directory / "bar_endpoint_completion.csv", bar_endpoint)
    write_csv(output_directory / "bar_trace_log.csv", bar_trace)
    write_csv(output_directory / "bar_universal_controls.csv", bar_controls)

    summary = {
        "candidate": "SD-C16",
        "scope": "Symbolic Dynamics only",
        "claim": (
            "global tensor-incidence selectivity versus finite-local "
            "positive-cone cocycle selectivity"
        ),
        "zero_data_used": ZERO_DATA_USED,
        "frozen": {
            "cutoffs": CUTOFFS,
            "shuffle_seeds": SHUFFLE_SEEDS,
            "random_inventory_seeds": RANDOM_INVENTORY_SEEDS,
            "source_exponent": SOURCE_EXPONENT,
            "determinant_z": str(DETERMINANT_Z),
            "planted_block_length": PLANTED_BLOCK_LENGTH,
            "incidence_cutoffs": INCIDENCE_CUTOFFS,
            "entropy_relabel_seeds": ENTROPY_RELABEL_SEEDS,
            "bar_formal_cutoff": BAR_FORMAL_CUTOFF,
            "bar_raw_word_lengths": BAR_RAW_WORD_LENGTHS,
            "bar_raw_points": tuple(map(str, BAR_RAW_POINTS)),
            "bar_endpoint_points": tuple(map(str, BAR_ENDPOINT_POINTS)),
            "bar_endpoint_cutoffs": BAR_ENDPOINT_CUTOFFS,
            "high_precision_digits": HIGH_PRECISION_DIGITS,
        },
        "audit_counts": {
            "rule_families": len(RULES),
            "rule_rows": len(rows),
            "radius_one_truth_tables": radius_summary["truth_tables_exhausted"],
            "finite_state_machines": sum(
                item["machines_exhausted"]
                for item in mealy_summary["by_state_count"].values()
            ),
            "global_incidence_ledger_rows": len(incidence_ledger),
            "global_incidence_control_rows": len(incidence_controls),
            "entropy_relabel_control_rows": len(entropy_relabels),
            "bar_formal_rows": len(bar_formal),
            "bar_raw_rows": len(bar_raw),
            "bar_endpoint_rows": len(bar_endpoint),
            "bar_trace_rows": len(bar_trace),
            "bar_universal_control_rows": len(bar_controls),
        },
        "named_rule_decisions": decisions,
        "finite_radius": radius_summary,
        "finite_state": mealy_summary,
        "global_incidence": global_incidence,
        "bar_determinant": {
            "sigma_bar": bar_sigma_threshold(),
            "raw_region": "Re(s) > sigma_bar where zeta(Re(s))-1 < 1",
            "endpoint_grouped_region": "Re(s) > 1",
            "convention": "D_bar(s,z)=1-z F_bar(s); at z=1, D_bar=1/zeta(s)",
            "formal_coefficients_exact_all": all(
                bool(row["bar_coefficient_exact"])
                and bool(row["determinant_coefficient_exact"])
                and bool(row["independent_inverse_exact"])
                for row in bar_formal
            ),
            "raw_exact_remainder_max_residual": max(
                float(row["exact_remainder_residual"]) for row in bar_raw
            ),
            "raw_closed_identity_max_residual": max(
                float(row["closed_D_identity_residual"]) for row in bar_raw
            ),
            "raw_final_max_D_residual": max(
                float(row["D_residual"])
                for row in bar_raw
                if row["word_length"] == max(BAR_RAW_WORD_LENGTHS)
            ),
            "endpoint_final_residuals": {
                str(point): next(
                    float(row["D_residual_observation"])
                    for row in bar_endpoint
                    if row["s"] == str(point)
                    and row["cutoff"] == max(BAR_ENDPOINT_CUTOFFS)
                )
                for point in BAR_ENDPOINT_POINTS
            },
            "trace_log_final_max_residual": max(
                float(row["trace_log_residual"])
                for row in bar_trace
                if row["repetition_cutoff"] == max(BAR_TRACE_REPETITIONS)
            ),
            "universal_controls_exact_all": all(
                bool(row["universal_inversion_exact"]) for row in bar_controls
            ),
            "proves_too_much": True,
            "target_zero_metrics": "not_applicable",
        },
        "decision": {
            "GO_SOURCE_DERIVED_SELECTOR": False,
            "GO_GLOBAL_INCIDENCE_SELECTOR": True,
            "GO_BAR_ANALYTIC_DETERMINANT": True,
            "STOP_FINITE_LOCAL_SELECTOR": True,
            "STOP_FINITE_STATE_SELECTOR": True,
            "PROVES_TOO_MUCH": True,
            "ROUTE_B_LOCKED": True,
        },
        "strongest_positive": (
            "The globally predeclared incidence transform mu_tensor*h gives "
            "exactly log p on every tensor prime power and zero on every "
            "mixed-prime tensor object; endpoint-grouped bar words give the "
            "analytic identity D_bar(s,1)=1/zeta(s) on Re(s)>1."
        ),
        "strongest_failure": (
            "Every positive-cone finite-local witness survives an explicitly "
            "constructed nontrivial shuffle that preserves one witness block; "
            "all exhaustively tested 1- and 2-state selectors fail the same gate."
        ),
        "next_smallest_test": (
            "Prove the planted-block obstruction at arbitrary finite radius, then "
            "determine whether the bar renewal determinant has any intrinsic "
            "global continuation/completion beyond the universal inversion identity."
        ),
    }
    write_json(output_directory / "summary.json", summary)

    paper_root = output_directory.parent
    checksum_paths = sorted((paper_root / "code").glob("*.py")) + sorted(
        path
        for path in output_directory.iterdir()
        if path.name != "SHA256SUMS.txt" and path.is_file()
    )
    checksums = []
    for path in checksum_paths:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        checksums.append(f"{digest}  {path.relative_to(paper_root)}")
    (output_directory / "SHA256SUMS.txt").write_text(
        "\n".join(checksums) + "\n", encoding="utf-8"
    )
    return summary


if __name__ == "__main__":
    generate(Path(__file__).resolve().parents[1] / "results")
