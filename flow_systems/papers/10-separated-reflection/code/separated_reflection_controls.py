#!/usr/bin/env python3
"""Deterministic finite controls for Paper 10 separated reflections.

The controls enumerate finite topology, measurable-space, cyclic-group,
coproduct, and nonnegative-mass examples.  They are regression and
falsification witnesses only.  They do not prove any theorem about a Deninger
packet, an infinite coproduct, an infinite circle, or an ``ell^1`` space.

Only the Python standard library is used.  The generator uses no network,
randomness, external data, target-zero data, fitted parameter, or timestamp.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable, Sequence


SCHEMA = "paper10-separated-reflection-controls/1"

EXPECTED_ACTIVE_TUPLE_HASHES = {
    "notes/candidate_lock.md": (
        "4cc6cae36630e13623d638a5eac7daaab084eef9549f4ca3bd44b026a32d26cf"
    ),
    "notes/phase1_design_amendment.md": (
        "e0e3fb42c2285b8c5da521f05588581e7981de8957e33aa3cf237f653d1c432f"
    ),
    "notes/research_protocol.md": (
        "4fe51d7dc9514dea101178995dec73e120ab7032b11c06ecd4bc0efadf9cbc58"
    ),
}

IMPLEMENTATION_RELATIVE_PATHS = (
    "code/separated_reflection_controls.py",
    "code/test_separated_reflection_controls.py",
    "code/README.md",
    "experiments/reproduce.sh",
    "experiments/README.md",
    "results/README.md",
)

ARTIFACT_FILENAMES = (
    "continuous_map_controls.csv",
    "measurable_map_controls.csv",
    "dirac_collapse_controls.csv",
    "indiscrete_group_characters.csv",
    "proxy_direction_controls.csv",
    "coproduct_k0_controls.csv",
    "component_mass_controls.csv",
    "ell1_gate_controls.csv",
    "label_neutrality_controls.csv",
    "external_log_label_controls.csv",
)

SOURCE_SIZES = (1, 2, 3, 5)
MEASURABLE_TARGET_SIZES = (2, 3)
CHARACTER_TARGET_ORDERS = (2, 3, 4, 5, 6)
COMPONENT_COUNTS = (2, 3, 5, 8)
ELL1_PREFIX_LENGTHS = (1, 2, 4, 8, 16)
LOG_EXPONENT_LEVELS = (1, 2, 4, 8, 12, 16)


def sha256(path: Path) -> str:
    """Return a file's SHA-256 digest."""

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def bool_text(value: bool) -> str:
    """Return a stable lowercase boolean for CSV output."""

    return "true" if value else "false"


def fraction_text(value: Fraction) -> str:
    """Return an exact rational string."""

    return f"{value.numerator}/{value.denominator}"


def encode_set(values: Iterable[int]) -> str:
    """Encode a finite integer set deterministically."""

    return "{" + ",".join(str(value) for value in sorted(values)) + "}"


def encode_partition(classes: Iterable[Iterable[int]]) -> str:
    """Encode an ordered family of finite equivalence classes."""

    normalized = sorted(tuple(sorted(group)) for group in classes)
    return "|".join(encode_set(group) for group in normalized)


def powerset(values: Sequence[int]) -> tuple[frozenset[int], ...]:
    """Return the full powerset in cardinality/lexicographic order."""

    materialized = tuple(values)
    return tuple(
        frozenset(selection)
        for size in range(len(materialized) + 1)
        for selection in itertools.combinations(materialized, size)
    )


def indiscrete_topology(size: int) -> tuple[frozenset[int], ...]:
    """Return the topology ``{empty, X}`` on ``range(size)``."""

    if size < 1:
        raise ValueError("control sources must be nonempty")
    return (frozenset(), frozenset(range(size)))


def discrete_topology(size: int) -> tuple[frozenset[int], ...]:
    """Return the discrete topology on ``range(size)``."""

    if size < 1:
        raise ValueError("control spaces must be nonempty")
    return powerset(tuple(range(size)))


def sierpinski_topology() -> tuple[frozenset[int], ...]:
    """Return the two-point Sierpinski topology with ``{1}`` open."""

    return (frozenset(), frozenset({1}), frozenset({0, 1}))


def is_t0(size: int, topology: Sequence[frozenset[int]]) -> bool:
    """Test the finite Kolmogorov separation condition."""

    return all(
        any((left in opened) != (right in opened) for opened in topology)
        for left in range(size)
        for right in range(left + 1, size)
    )


def inverse_image(mapping: Sequence[int], opened: frozenset[int]) -> frozenset[int]:
    """Return a finite inverse image."""

    return frozenset(index for index, value in enumerate(mapping) if value in opened)


def is_continuous(
    mapping: Sequence[int],
    source_topology: Sequence[frozenset[int]],
    target_topology: Sequence[frozenset[int]],
) -> bool:
    """Check continuity by inverse images of every target open set."""

    source_opens = frozenset(source_topology)
    return all(inverse_image(mapping, opened) in source_opens for opened in target_topology)


def generated_sigma_algebra(
    size: int, generators: Sequence[frozenset[int]]
) -> tuple[frozenset[int], ...]:
    """Generate a finite sigma-algebra by closure under complement/union."""

    universe = frozenset(range(size))
    current = set(generators) | {frozenset(), universe}
    changed = True
    while changed:
        before = len(current)
        current |= {universe - subset for subset in tuple(current)}
        current |= {
            left | right
            for left in tuple(current)
            for right in tuple(current)
        }
        changed = len(current) != before
    return tuple(sorted(current, key=lambda subset: (len(subset), tuple(sorted(subset)))))


def is_measurable(
    mapping: Sequence[int],
    source_sigma: Sequence[frozenset[int]],
    target_sigma: Sequence[frozenset[int]],
) -> bool:
    """Check finite measurability by inverse images."""

    source_sets = frozenset(source_sigma)
    return all(inverse_image(mapping, event) in source_sets for event in target_sigma)


def kolmogorov_classes(
    size: int, topology: Sequence[frozenset[int]]
) -> tuple[tuple[int, ...], ...]:
    """Return classes of points with equal open-neighborhood filters."""

    signatures = {
        point: tuple(index for index, opened in enumerate(topology) if point in opened)
        for point in range(size)
    }
    grouped: dict[tuple[int, ...], list[int]] = {}
    for point in range(size):
        grouped.setdefault(signatures[point], []).append(point)
    return tuple(tuple(points) for points in grouped.values())


def write_csv(
    path: Path, fieldnames: Sequence[str], rows: Iterable[dict[str, object]]
) -> int:
    """Write deterministic UTF-8 CSV and return the data-row count."""

    materialized = list(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(fieldnames),
            lineterminator="\n",
            extrasaction="raise",
        )
        writer.writeheader()
        writer.writerows(materialized)
    return len(materialized)


def _continuous_map_rows() -> list[dict[str, object]]:
    targets = (
        ("discrete_2", discrete_topology(2), True),
        ("sierpinski_2", sierpinski_topology(), True),
        ("indiscrete_2_negative", indiscrete_topology(2), False),
    )
    rows: list[dict[str, object]] = []
    for size in SOURCE_SIZES:
        source_topology = indiscrete_topology(size)
        for target_name, target_topology, target_t0 in targets:
            if is_t0(2, target_topology) != target_t0:
                raise AssertionError("target separation ledger is inconsistent")
            for mapping in itertools.product(range(2), repeat=size):
                continuous = is_continuous(mapping, source_topology, target_topology)
                constant = len(set(mapping)) == 1
                expected = constant if target_t0 else True
                rows.append(
                    {
                        "source_size": size,
                        "source_topology": "indiscrete",
                        "target": target_name,
                        "target_t0": bool_text(target_t0),
                        "map_values": "".join(str(value) for value in mapping),
                        "image_size": len(set(mapping)),
                        "constant": bool_text(constant),
                        "continuous": bool_text(continuous),
                        "expected_continuity": bool_text(expected),
                        "expectation_match": bool_text(continuous == expected),
                        "scope": "finite exhaustive topology control; not an actual-packet proof",
                    }
                )
    return rows


def _measurable_map_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for size in SOURCE_SIZES:
        source_sigma = generated_sigma_algebra(size, indiscrete_topology(size))
        for target_size in MEASURABLE_TARGET_SIZES:
            target_sigma = discrete_topology(target_size)
            for mapping in itertools.product(range(target_size), repeat=size):
                measurable = is_measurable(mapping, source_sigma, target_sigma)
                constant = len(set(mapping)) == 1
                rows.append(
                    {
                        "source_size": size,
                        "source_sigma": "{empty,X}",
                        "source_sigma_cardinality": len(source_sigma),
                        "target_size": target_size,
                        "target_sigma": "power_set",
                        "target_countably_separated": "true",
                        "map_values": "".join(str(value) for value in mapping),
                        "image_size": len(set(mapping)),
                        "constant": bool_text(constant),
                        "measurable": bool_text(measurable),
                        "collapse_match": bool_text(measurable == constant),
                        "scope": "finite exhaustive measurable control; not an actual-packet proof",
                    }
                )
    return rows


def _dirac_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for size in SOURCE_SIZES:
        borel = generated_sigma_algebra(size, indiscrete_topology(size))
        for left in range(size):
            for right in range(size):
                equal_on_borel = all(
                    (left in event) == (right in event) for event in borel
                )
                for event in borel:
                    rows.append(
                        {
                            "source_size": size,
                            "point_x": left,
                            "point_y": right,
                            "measurable_event": encode_set(event),
                            "delta_x": int(left in event),
                            "delta_y": int(right in event),
                            "equal_on_event": bool_text(
                                (left in event) == (right in event)
                            ),
                            "equal_on_entire_borel_ledger": bool_text(equal_on_borel),
                            "proper_singleton_measurable": bool_text(
                                size == 1 or frozenset({left}) in borel
                            ),
                            "dirac_domain": "measurable_events_only",
                            "scope": "finite Dirac ledger; no Radon/support claim",
                        }
                    )
    return rows


def cyclic_hom_mapping(source_order: int, target_order: int, exponent: int) -> tuple[int, ...]:
    """Return ``x -> exponent*x mod target_order`` after well-definedness check."""

    if source_order < 1 or target_order < 1:
        raise ValueError("cyclic orders must be positive")
    if source_order * exponent % target_order != 0:
        raise ValueError("exponent does not define a homomorphism")
    return tuple(exponent * value % target_order for value in range(source_order))


def _group_operation_is_continuous(order: int) -> bool:
    product_mapping = tuple(
        (left + right) % order for left in range(order) for right in range(order)
    )
    inverse_mapping = tuple((-value) % order for value in range(order))
    return is_continuous(
        product_mapping,
        indiscrete_topology(order * order),
        indiscrete_topology(order),
    ) and is_continuous(
        inverse_mapping,
        indiscrete_topology(order),
        indiscrete_topology(order),
    )


def _group_character_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    target_kinds = ("finite_cyclic_discrete", "finite_circle_mesh_discrete_proxy")
    for source_order in SOURCE_SIZES:
        operations_continuous = _group_operation_is_continuous(source_order)
        for target_order in CHARACTER_TARGET_ORDERS:
            for exponent in range(target_order):
                if source_order * exponent % target_order != 0:
                    continue
                mapping = cyclic_hom_mapping(source_order, target_order, exponent)
                nontrivial = len(set(mapping)) > 1
                for target_kind in target_kinds:
                    continuous = is_continuous(
                        mapping,
                        indiscrete_topology(source_order),
                        discrete_topology(target_order),
                    )
                    control_type = (
                        "trivial_continuous_character"
                        if not nontrivial
                        else "algebraic_character_noncontinuous_negative"
                    )
                    rows.append(
                        {
                            "source_group": f"C{source_order}",
                            "source_topology": "indiscrete",
                            "group_operations_continuous": bool_text(
                                operations_continuous
                            ),
                            "target_kind": target_kind,
                            "target_order": target_order,
                            "target_hausdorff": "true",
                            "hom_exponent": exponent,
                            "map_values": "|".join(str(value) for value in mapping),
                            "image_size": len(set(mapping)),
                            "algebraic_homomorphism": "true",
                            "nontrivial": bool_text(nontrivial),
                            "continuous_actual_topology": bool_text(continuous),
                            "control_type": control_type,
                            "scope": "finite cyclic/mesh control; not a classification of the full circle",
                        }
                    )
    return rows


def _proxy_direction_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for size in SOURCE_SIZES:
        identity = tuple(range(size))
        directions = (
            (
                "actual_indiscrete_to_standard_discrete_proxy",
                indiscrete_topology(size),
                discrete_topology(size),
            ),
            (
                "standard_discrete_proxy_to_actual_indiscrete",
                discrete_topology(size),
                indiscrete_topology(size),
            ),
        )
        for direction, domain_topology, codomain_topology in directions:
            continuous = is_continuous(identity, domain_topology, codomain_topology)
            forward = direction == "actual_indiscrete_to_standard_discrete_proxy"
            rows.append(
                {
                    "set_size": size,
                    "map": "chosen_identity_after_label_freeze",
                    "direction": direction,
                    "domain_topology": "indiscrete" if forward else "discrete_proxy",
                    "codomain_topology": "discrete_proxy" if forward else "indiscrete",
                    "continuous": bool_text(continuous),
                    "expected_continuity": bool_text(
                        size == 1
                        or direction == "standard_discrete_proxy_to_actual_indiscrete"
                    ),
                    "noncanonical_label_choice": "true",
                    "scope": "finite direction control; discrete proxy is not a circle theorem",
                }
            )
    return rows


def copied_coproduct(component_count: int) -> dict[str, object]:
    """Construct a tagged finite coproduct of nontrivial indiscrete components."""

    if component_count not in COMPONENT_COUNTS:
        raise ValueError("unsupported component count")
    component_sizes = tuple(2 + (index % 3) for index in range(component_count))
    offsets: list[tuple[int, ...]] = []
    cursor = 0
    for size in component_sizes:
        offsets.append(tuple(range(cursor, cursor + size)))
        cursor += size
    opens = tuple(
        frozenset(
            point
            for component_index in selected
            for point in offsets[component_index]
        )
        for selected_size in range(component_count + 1)
        for selected in itertools.combinations(range(component_count), selected_size)
    )
    classes = kolmogorov_classes(cursor, opens)
    borel = generated_sigma_algebra(cursor, opens)
    return {
        "component_sizes": component_sizes,
        "total_points": cursor,
        "opens": opens,
        "borel": borel,
        "classes": classes,
    }


def _coproduct_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for component_count in COMPONENT_COUNTS:
        model = copied_coproduct(component_count)
        classes = tuple(model["classes"])
        rows.append(
            {
                "component_count": component_count,
                "component_sizes": "|".join(
                    str(value) for value in model["component_sizes"]
                ),
                "total_points": model["total_points"],
                "topology_open_count": len(model["opens"]),
                "borel_event_count": len(model["borel"]),
                "k0_class_count": len(classes),
                "k0_classes": encode_partition(classes),
                "within_component_points_erased": "true",
                "distinct_labels_separated": "true",
                "quotient_topology": "discrete_label_set",
                "owner": "modeling_choice_tagged_coproduct",
                "scope": "finite copied control; not the global Deninger suspension",
            }
        )
    return rows


def mass_profiles(component_count: int) -> tuple[tuple[str, tuple[Fraction, ...]], ...]:
    """Return exact nonnegative finite mass vectors, including zeros."""

    zeros = tuple(Fraction(0) for _ in range(component_count))
    first = tuple(Fraction(1) if index == 0 else Fraction(0) for index in range(component_count))
    last = tuple(
        Fraction(1) if index == component_count - 1 else Fraction(0)
        for index in range(component_count)
    )
    increasing = tuple(Fraction(index, 2) for index in range(component_count))
    alternating = tuple(
        Fraction(1, 3) if index % 2 == 0 else Fraction(0)
        for index in range(component_count)
    )
    return (
        ("all_zero", zeros),
        ("unit_first", first),
        ("unit_last_same_total", last),
        ("increasing_with_zero", increasing),
        ("alternating_with_zeros", alternating),
    )


def _component_mass_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for component_count in COMPONENT_COUNTS:
        topology_fingerprint = f"components={component_count};opens={2**component_count}"
        even_indices = tuple(index for index in range(component_count) if index % 2 == 0)
        for profile, weights in mass_profiles(component_count):
            total = sum(weights, Fraction(0))
            even_mass = sum((weights[index] for index in even_indices), Fraction(0))
            rows.append(
                {
                    "component_count": component_count,
                    "profile": profile,
                    "weights_exact": "|".join(fraction_text(weight) for weight in weights),
                    "zero_component_count": sum(weight == 0 for weight in weights),
                    "total_mass_exact": fraction_text(total),
                    "even_component_union": "|".join(str(index) for index in even_indices),
                    "even_component_mass_exact": fraction_text(even_mass),
                    "nonnegative": bool_text(all(weight >= 0 for weight in weights)),
                    "finite_total": "true",
                    "finite_ell1_gate": "true",
                    "topology_fingerprint": topology_fingerprint,
                    "topology_selects_weights": "false",
                    "scope": "finite exact mass ledger; infinite classification needs ell1 summability",
                }
            )
    return rows


def ell1_profile(profile: str, index: int) -> Fraction:
    """Return a nonnegative sequence term for a frozen symbolic profile."""

    if index < 0:
        raise ValueError("sequence indices must be nonnegative")
    if profile == "geometric_half":
        return Fraction(1, 2 ** (index + 1))
    if profile == "constant_one":
        return Fraction(1)
    if profile == "harmonic":
        return Fraction(1, index + 1)
    if profile == "finite_support_with_zeros":
        fixed = (Fraction(2), Fraction(0), Fraction(1, 3), Fraction(0))
        return fixed[index] if index < len(fixed) else Fraction(0)
    raise ValueError("unknown ell1 profile")


def _ell1_rows() -> list[dict[str, object]]:
    metadata = {
        "geometric_half": (
            "ELL1_BY_SYMBOLIC_PROFILE",
            "sum_{k>=0}2^-(k+1)=1",
        ),
        "constant_one": (
            "NOT_ELL1_BY_SYMBOLIC_PROFILE",
            "partial_sum_N=N",
        ),
        "harmonic": (
            "NOT_ELL1_BY_SYMBOLIC_PROFILE",
            "harmonic_series_diverges",
        ),
        "finite_support_with_zeros": (
            "ELL1_BY_SYMBOLIC_PROFILE",
            "finite_support_total=7/3",
        ),
    }
    rows: list[dict[str, object]] = []
    for profile, (symbolic_gate, justification) in metadata.items():
        for prefix_length in ELL1_PREFIX_LENGTHS:
            terms = tuple(ell1_profile(profile, index) for index in range(prefix_length))
            rows.append(
                {
                    "profile": profile,
                    "prefix_length": prefix_length,
                    "prefix_terms_exact": "|".join(fraction_text(term) for term in terms),
                    "prefix_sum_exact": fraction_text(sum(terms, Fraction(0))),
                    "all_terms_nonnegative": bool_text(all(term >= 0 for term in terms)),
                    "finite_prefix_sum_finite": "true",
                    "finite_prefix_decides_infinite_gate": "false",
                    "symbolic_gate": symbolic_gate,
                    "symbolic_justification": justification,
                    "scope": "finite prefix display plus declared symbolic formula; not an infinite proof",
                }
            )
    return rows


def is_prime(number: int) -> bool:
    """Deterministic primality test for small control labels."""

    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def first_primes(count: int) -> tuple[int, ...]:
    """Return the first ``count`` primes."""

    values: list[int] = []
    candidate = 2
    while len(values) < count:
        if is_prime(candidate):
            values.append(candidate)
        candidate += 1
    return tuple(values)


def first_composites(count: int) -> tuple[int, ...]:
    """Return the first ``count`` composite integers."""

    values: list[int] = []
    candidate = 4
    while len(values) < count:
        if not is_prime(candidate):
            values.append(candidate)
        candidate += 1
    return tuple(values)


def _label_neutrality_rows() -> list[dict[str, object]]:
    arbitrary_pool = ("alpha", "beta", "cedar", "delta", "ember", "fjord", "gamma", "helix")
    rows: list[dict[str, object]] = []
    for component_count in COMPONENT_COUNTS:
        label_families = (
            ("prime", tuple(str(value) for value in first_primes(component_count))),
            ("composite", tuple(str(value) for value in first_composites(component_count))),
            ("arbitrary", arbitrary_pool[:component_count]),
        )
        for family, labels in label_families:
            rows.append(
                {
                    "component_count": component_count,
                    "label_family": family,
                    "labels": "|".join(labels),
                    "labels_distinct": bool_text(len(set(labels)) == component_count),
                    "topology_open_count": 2**component_count,
                    "borel_event_count": 2**component_count,
                    "k0_class_count": component_count,
                    "abstract_signature": (
                        f"tagged={component_count};opens={2**component_count};k0={component_count}"
                    ),
                    "abstract_mechanism_detects_primality": "false",
                    "arithmetic_provenance_external": bool_text(family == "prime"),
                    "scope": "label-neutral copied control; no source-global credit",
                }
            )
    return rows


def next_prime_greater_than(bound: int) -> int:
    """Return the least prime strictly larger than ``bound``."""

    candidate = bound + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


def _external_log_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for exponent in LOG_EXPONENT_LEVELS:
        bound = 2**exponent
        prime = next_prime_greater_than(bound)
        rows.append(
            {
                "exponent_k": exponent,
                "integer_bound_2_power_k": bound,
                "selected_prime_label": prime,
                "prime_exceeds_bound": bool_text(prime > bound),
                "external_scalar": f"log({prime})",
                "exact_lower_bound": f"log({prime})>{exponent}*log(2)",
                "finite_growth_witness": "true",
                "symbolic_unbounded_template": "for increasing k choose prime p>2^k",
                "topology_selects_log_label": "false",
                "mass_ledger_selects_log_label": "false",
                "actual_source_observable_credit": "false",
                "scope": "finite witnesses plus symbolic template; not an unboundedness proof",
            }
        )
    return rows


def _artifact_specs() -> tuple[
    tuple[str, Sequence[str], Callable[[], list[dict[str, object]]]], ...
]:
    return (
        (
            "continuous_map_controls.csv",
            (
                "source_size",
                "source_topology",
                "target",
                "target_t0",
                "map_values",
                "image_size",
                "constant",
                "continuous",
                "expected_continuity",
                "expectation_match",
                "scope",
            ),
            _continuous_map_rows,
        ),
        (
            "measurable_map_controls.csv",
            (
                "source_size",
                "source_sigma",
                "source_sigma_cardinality",
                "target_size",
                "target_sigma",
                "target_countably_separated",
                "map_values",
                "image_size",
                "constant",
                "measurable",
                "collapse_match",
                "scope",
            ),
            _measurable_map_rows,
        ),
        (
            "dirac_collapse_controls.csv",
            (
                "source_size",
                "point_x",
                "point_y",
                "measurable_event",
                "delta_x",
                "delta_y",
                "equal_on_event",
                "equal_on_entire_borel_ledger",
                "proper_singleton_measurable",
                "dirac_domain",
                "scope",
            ),
            _dirac_rows,
        ),
        (
            "indiscrete_group_characters.csv",
            (
                "source_group",
                "source_topology",
                "group_operations_continuous",
                "target_kind",
                "target_order",
                "target_hausdorff",
                "hom_exponent",
                "map_values",
                "image_size",
                "algebraic_homomorphism",
                "nontrivial",
                "continuous_actual_topology",
                "control_type",
                "scope",
            ),
            _group_character_rows,
        ),
        (
            "proxy_direction_controls.csv",
            (
                "set_size",
                "map",
                "direction",
                "domain_topology",
                "codomain_topology",
                "continuous",
                "expected_continuity",
                "noncanonical_label_choice",
                "scope",
            ),
            _proxy_direction_rows,
        ),
        (
            "coproduct_k0_controls.csv",
            (
                "component_count",
                "component_sizes",
                "total_points",
                "topology_open_count",
                "borel_event_count",
                "k0_class_count",
                "k0_classes",
                "within_component_points_erased",
                "distinct_labels_separated",
                "quotient_topology",
                "owner",
                "scope",
            ),
            _coproduct_rows,
        ),
        (
            "component_mass_controls.csv",
            (
                "component_count",
                "profile",
                "weights_exact",
                "zero_component_count",
                "total_mass_exact",
                "even_component_union",
                "even_component_mass_exact",
                "nonnegative",
                "finite_total",
                "finite_ell1_gate",
                "topology_fingerprint",
                "topology_selects_weights",
                "scope",
            ),
            _component_mass_rows,
        ),
        (
            "ell1_gate_controls.csv",
            (
                "profile",
                "prefix_length",
                "prefix_terms_exact",
                "prefix_sum_exact",
                "all_terms_nonnegative",
                "finite_prefix_sum_finite",
                "finite_prefix_decides_infinite_gate",
                "symbolic_gate",
                "symbolic_justification",
                "scope",
            ),
            _ell1_rows,
        ),
        (
            "label_neutrality_controls.csv",
            (
                "component_count",
                "label_family",
                "labels",
                "labels_distinct",
                "topology_open_count",
                "borel_event_count",
                "k0_class_count",
                "abstract_signature",
                "abstract_mechanism_detects_primality",
                "arithmetic_provenance_external",
                "scope",
            ),
            _label_neutrality_rows,
        ),
        (
            "external_log_label_controls.csv",
            (
                "exponent_k",
                "integer_bound_2_power_k",
                "selected_prime_label",
                "prime_exceeds_bound",
                "external_scalar",
                "exact_lower_bound",
                "finite_growth_witness",
                "symbolic_unbounded_template",
                "topology_selects_log_label",
                "mass_ledger_selects_log_label",
                "actual_source_observable_credit",
                "scope",
            ),
            _external_log_rows,
        ),
    )


def _active_tuple(paper_dir: Path) -> dict[str, str]:
    observed = {
        relative: sha256(paper_dir / relative)
        for relative in EXPECTED_ACTIVE_TUPLE_HASHES
    }
    if observed != EXPECTED_ACTIVE_TUPLE_HASHES:
        raise ValueError(
            "active design tuple mismatch: expected "
            f"{EXPECTED_ACTIVE_TUPLE_HASHES}, observed {observed}"
        )
    return observed


def _implementation_hashes(paper_dir: Path) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for relative in IMPLEMENTATION_RELATIVE_PATHS:
        path = paper_dir / relative
        if not path.is_file():
            raise FileNotFoundError(f"missing implementation file: {relative}")
        hashes[relative] = sha256(path)
    return hashes


def _build_manifest(
    output_dir: Path,
    row_counts: dict[str, int],
    paper_dir: Path,
) -> dict[str, object]:
    artifacts = {
        filename: {
            "bytes": (output_dir / filename).stat().st_size,
            "rows": row_counts[filename],
            "sha256": sha256(output_dir / filename),
        }
        for filename in ARTIFACT_FILENAMES
    }
    continuous_rows = _continuous_map_rows()
    measurable_rows = _measurable_map_rows()
    dirac_rows = _dirac_rows()
    character_rows = _group_character_rows()
    proxy_rows = _proxy_direction_rows()
    coproduct_rows = _coproduct_rows()
    mass_rows = _component_mass_rows()
    ell1_rows = _ell1_rows()
    label_rows = _label_neutrality_rows()
    log_rows = _external_log_rows()
    return {
        "schema": SCHEMA,
        "regression_status": "PASS",
        "active_tuple_files": _active_tuple(paper_dir),
        "implementation_files": _implementation_hashes(paper_dir),
        "artifacts": artifacts,
        "parameters": {
            "source_sizes": list(SOURCE_SIZES),
            "topological_targets": [
                "discrete_2",
                "sierpinski_2",
                "indiscrete_2_negative",
            ],
            "measurable_target_sizes": list(MEASURABLE_TARGET_SIZES),
            "character_target_orders": list(CHARACTER_TARGET_ORDERS),
            "component_counts": list(COMPONENT_COUNTS),
            "ell1_prefix_lengths": list(ELL1_PREFIX_LENGTHS),
            "log_exponent_levels": list(LOG_EXPONENT_LEVELS),
        },
        "controls": [
            "exhaustive maps from finite indiscrete sources to discrete, Sierpinski, and indiscrete targets",
            "trivial Borel sigma-algebras and exhaustive maps to finite discrete measurable targets",
            "Dirac equality on every measurable event without singleton-measurability promotion",
            "indiscrete cyclic-group characters to finite cyclic targets and finite circle meshes",
            "actual-indiscrete versus discrete-proxy map directionality",
            "tagged coproduct topology, Borel algebra, and Kolmogorov classes",
            "arbitrary exact nonnegative finite component masses including zero components",
            "finite-prefix displays separated from symbolic ell1 gates",
            "prime, composite, and arbitrary label neutrality",
            "external log-label growth witnesses with no topology, mass, or actual-source credit",
        ],
        "metrics": {
            "total_csv_rows": sum(row_counts.values()),
            "all_topology_expectations_match": all(
                row["expectation_match"] == "true" for row in continuous_rows
            ),
            "nonconstant_continuous_maps_to_t0": sum(
                row["continuous"] == "true"
                and row["constant"] == "false"
                and row["target_t0"] == "true"
                for row in continuous_rows
            ),
            "nonconstant_continuous_maps_to_indiscrete_negative_target": sum(
                row["continuous"] == "true"
                and row["constant"] == "false"
                and row["target"] == "indiscrete_2_negative"
                for row in continuous_rows
            ),
            "nonconstant_measurable_maps_to_discrete_targets": sum(
                row["measurable"] == "true" and row["constant"] == "false"
                for row in measurable_rows
            ),
            "all_dirac_pairs_equal_on_borel": all(
                row["equal_on_entire_borel_ledger"] == "true"
                for row in dirac_rows
            ),
            "nontrivial_continuous_finite_characters": sum(
                row["nontrivial"] == "true"
                and row["continuous_actual_topology"] == "true"
                for row in character_rows
            ),
            "algebraic_noncontinuous_negative_controls": sum(
                row["control_type"]
                == "algebraic_character_noncontinuous_negative"
                for row in character_rows
            ),
            "proxy_direction_expectations_match": all(
                row["continuous"] == row["expected_continuity"] for row in proxy_rows
            ),
            "coproduct_k0_counts_match_labels": all(
                int(row["component_count"]) == int(row["k0_class_count"])
                for row in coproduct_rows
            ),
            "all_mass_vectors_nonnegative_finite": all(
                row["nonnegative"] == "true" and row["finite_total"] == "true"
                for row in mass_rows
            ),
            "all_finite_prefixes_marked_nondecisive": all(
                row["finite_prefix_decides_infinite_gate"] == "false"
                for row in ell1_rows
            ),
            "all_label_families_share_abstract_signatures": all(
                len(
                    {
                        row["abstract_signature"]
                        for row in label_rows
                        if int(row["component_count"]) == component_count
                    }
                )
                == 1
                for component_count in COMPONENT_COUNTS
            ),
            "all_external_log_witnesses_exceed_exact_bounds": all(
                row["prime_exceeds_bound"] == "true" for row in log_rows
            ),
        },
        "determinism": {
            "python_dependencies": "standard_library_only",
            "network": False,
            "randomness": False,
            "external_datasets": False,
            "target_zero_data": False,
            "fitting": False,
            "timestamps": False,
        },
        "object_boundary": (
            "Finite indiscrete models, T0/non-T0 targets, cyclic meshes, the "
            "chosen discrete proxy, and tagged copied coproducts are separate "
            "typed controls. No topology, sigma-algebra, mass, log label, or "
            "character is transported to an actual Deninger owner."
        ),
        "interpretation_boundary": (
            "These exact finite controls are not mathematical proofs of "
            "P10-1--P10-10, actual packet/orbit/Q_p collapse, an infinite "
            "ell1 classification, full-circle character collapse, unboundedness "
            "of log p, source-global aggregation, or any Route coordinate."
        ),
        "forbidden_evidence_not_used": [
            "Riemann-zero tables",
            "target-zero fitting",
            "fitted clocks, residues, masses, or weights",
            "external network or package data",
            "random search",
        ],
    }


def run(output_dir: Path, paper_dir: Path | None = None) -> dict[str, object]:
    """Generate every CSV and the manifest, then return the manifest."""

    output_dir = output_dir.resolve()
    if paper_dir is None:
        paper_dir = Path(__file__).resolve().parents[1]
    else:
        paper_dir = paper_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    row_counts: dict[str, int] = {}
    for filename, fieldnames, row_factory in _artifact_specs():
        row_counts[filename] = write_csv(
            output_dir / filename, fieldnames, row_factory()
        )
    manifest = _build_manifest(output_dir, row_counts, paper_dir)
    manifest_path = output_dir / "separated_reflection_controls_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def verify(output_dir: Path, paper_dir: Path | None = None) -> dict[str, object]:
    """Verify manifest, artifacts, active tuple, implementation, and metrics."""

    output_dir = output_dir.resolve()
    if paper_dir is None:
        paper_dir = Path(__file__).resolve().parents[1]
    else:
        paper_dir = paper_dir.resolve()
    manifest_path = output_dir / "separated_reflection_controls_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema") != SCHEMA:
        raise ValueError("manifest schema mismatch")
    if manifest.get("regression_status") != "PASS":
        raise ValueError("manifest regression status is not PASS")
    if manifest.get("active_tuple_files") != _active_tuple(paper_dir):
        raise ValueError("active tuple SHA-256 mismatch")
    if manifest.get("implementation_files") != _implementation_hashes(paper_dir):
        raise ValueError("implementation SHA-256 mismatch")

    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, dict) or set(artifacts) != set(ARTIFACT_FILENAMES):
        raise ValueError("artifact filename ledger mismatch")
    row_counts: dict[str, int] = {}
    for filename in ARTIFACT_FILENAMES:
        path = output_dir / filename
        if not path.is_file():
            raise ValueError(f"missing artifact: {filename}")
        record = artifacts[filename]
        if sha256(path) != record.get("sha256"):
            raise ValueError(f"artifact SHA-256 mismatch: {filename}")
        if path.stat().st_size != record.get("bytes"):
            raise ValueError(f"artifact byte-size mismatch: {filename}")
        with path.open("r", encoding="utf-8", newline="") as handle:
            row_count = sum(1 for _ in csv.DictReader(handle))
        if row_count != record.get("rows"):
            raise ValueError(f"artifact row-count mismatch: {filename}")
        row_counts[filename] = row_count

    expected = _build_manifest(output_dir, row_counts, paper_dir)
    if manifest != expected:
        raise ValueError("manifest metric or metadata ledger mismatch")
    return manifest


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="directory for generated CSV and manifest files",
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="verify existing artifacts without rewriting them",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    manifest = verify(args.output_dir) if args.verify_only else run(args.output_dir)
    print(
        f"PASS schema={manifest['schema']} "
        f"rows={manifest['metrics']['total_csv_rows']} "
        f"artifacts={len(manifest['artifacts'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
