#!/usr/bin/env python3
"""Exact producer-side W(E6) dual-action and ramification replay for C58.

The immutable group evidence stores the exhaustive result, not an oracle: this
script rebuilds W(E6), both permutation actions, every relevant subgroup
chain, the Picard fixed dimensions, and the conductor/different formulas from
the frozen C57 line configuration before accepting those bytes.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from math import gcd
from pathlib import Path
import subprocess
import sys
from typing import Any

from sympy import Matrix
from sympy.combinatorics import Permutation, PermutationGroup

from c58_exact import (
    StrictDataError,
    atomic_write,
    canonical_json_bytes,
    canonical_leaf_bytes,
    deep_exact,
    read_stable,
    reject_optimized_python,
    require_canonical_compact_json,
    require_exact_keys,
    strict_json_loads,
)


REPO = Path(__file__).resolve().parents[3]
C57_CODE = REPO / "henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/code"
C56_CERTIFICATE = (
    REPO / "henon_dynamics/henon_mu3_yukawa_line_field/results/c56_certificate.json"
)
C57_GROUP_SOURCE = C57_CODE / "c57_group.py"
C56_CERTIFICATE_SHA256 = (
    "26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4"
)
C57_GROUP_SOURCE_SHA256 = (
    "01608cc60b38e5283e575a4e5f2176af9421b018c297bbee2f266df482ee359d"
)
sys.path.insert(0, str(C57_CODE))
import c57_group as c57  # noqa: E402


EXCEPTIONAL, ROOTS, LINES, WEYL_GENERATORS, INCIDENCE, SIXERS, DOUBLE_SIXES = (
    c57.line_configuration()
)
IDENTITY = tuple(range(27))
I7 = Matrix.eye(7)
DOUBLE_INDEX = {value: index for index, value in enumerate(DOUBLE_SIXES)}


def normalize_carrier(value):
    """Turn the C56/C57 tuple/frozenset carriers into ordered JSON trees."""
    if type(value) is dict:
        return {
            key: normalize_carrier(value[key])
            for key in sorted(value)
        }
    if type(value) in (list, tuple):
        return [normalize_carrier(item) for item in value]
    if type(value) is frozenset:
        rows = [normalize_carrier(item) for item in value]
        return sorted(rows, key=canonical_leaf_bytes)
    if type(value) is int:
        return value
    raise TypeError(f"unsupported upstream carrier leaf: {type(value).__name__}")


def current_c57_carriers():
    return normalize_carrier(
        {
            "double_sixes": DOUBLE_SIXES,
            "exceptional": EXCEPTIONAL,
            "incidence": INCIDENCE,
            "lines": LINES,
            "roots": ROOTS,
            "sixers": SIXERS,
            "weyl_generators": WEYL_GENERATORS,
        }
    )


_C57_CARRIER_SNAPSHOT = current_c57_carriers()
_C57_CARRIER_SHA256 = hashlib.sha256(
    canonical_leaf_bytes(_C57_CARRIER_SNAPSHOT)
).hexdigest()
_C56_RAW, _C56_FINGERPRINT = read_stable(C56_CERTIFICATE, max_bytes=10_000_000)
if _C56_FINGERPRINT.sha256 != C56_CERTIFICATE_SHA256:
    raise StrictDataError("frozen C56 certificate SHA changed")
_C56_CERTIFICATE = strict_json_loads(_C56_RAW, max_bytes=10_000_000)


def verify_upstream_carriers():
    """Rebind the imported source and every action carrier before/after use."""
    _, source_fingerprint = read_stable(C57_GROUP_SOURCE, max_bytes=1_000_000)
    if source_fingerprint.sha256 != C57_GROUP_SOURCE_SHA256:
        raise StrictDataError("imported c57_group.py source SHA changed")
    current = current_c57_carriers()
    if not deep_exact(current, _C57_CARRIER_SNAPSHOT):
        raise StrictDataError("imported C57 carrier arrays mutated")
    try:
        upstream_we6 = _C56_CERTIFICATE["payload"]["we6"]
        c56_bindings = {
            "incidence": upstream_we6["line_class_intersection_matrix"],
            "lines": upstream_we6["line_classes"],
            "roots": upstream_we6["simple_roots"],
            "weyl_generators": upstream_we6["simple_reflection_line_permutations"],
        }
    except (KeyError, TypeError) as exc:
        raise StrictDataError("frozen C56 W(E6) carrier is incomplete") from exc
    for name, expected in c56_bindings.items():
        if not deep_exact(current[name], expected):
            raise StrictDataError(f"C56/C57 carrier mismatch: {name}")
    return {
        "c56_certificate_sha256": C56_CERTIFICATE_SHA256,
        "c56_carriers_deep_equal": True,
        "c57_carrier_sha256": _C57_CARRIER_SHA256,
        "c57_group_source_sha256": C57_GROUP_SOURCE_SHA256,
        "c57_import_carriers_immutable": True,
    }


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(len(right)))


def inverse(value: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * len(value)
    for index, image in enumerate(value):
        result[image] = index
    return tuple(result)


def generated(generators) -> frozenset[tuple[int, ...]]:
    subgroup = {IDENTITY}
    queue = deque([IDENTITY])
    while queue:
        value = queue.popleft()
        for generator in generators:
            new = compose(generator, value)
            if new not in subgroup:
                subgroup.add(new)
                queue.append(new)
    return frozenset(subgroup)


WEYL = generated(WEYL_GENERATORS)
INVERSES = {value: inverse(value) for value in WEYL}


def small_generators(subgroup):
    current = frozenset((IDENTITY,))
    output = []
    while len(current) < len(subgroup):
        value = min(item for item in subgroup if item not in current)
        output.append(value)
        current = generated(output)
    return output


def conjugate(value, subgroup):
    value_inverse = INVERSES[value]
    return frozenset(
        compose(value, compose(element, value_inverse)) for element in subgroup
    )


def normalizer(subgroup, generators=None):
    generators = generators or small_generators(subgroup)
    return frozenset(
        value
        for value in WEYL
        if all(
            compose(value, compose(generator, INVERSES[value])) in subgroup
            for generator in generators
        )
    )


def is_normal(ambient, subgroup):
    generators = small_generators(subgroup)
    return all(
        compose(value, compose(generator, INVERSES[value])) in subgroup
        for value in ambient
        for generator in generators
    )


def line_action(value, index):
    return value[index]


def double_action(value, index):
    return DOUBLE_INDEX[c57.act(value, DOUBLE_SIXES[index])]


def orbit_sets(subgroup, object_count, action):
    unseen = set(range(object_count))
    output = []
    while unseen:
        seed = min(unseen)
        orbit = {action(value, seed) for value in subgroup}
        output.append(frozenset(orbit))
        unseen -= orbit
    return tuple(sorted(output, key=lambda row: (len(row), tuple(sorted(row)))))


def orbit_pattern(subgroup, object_count, action):
    return tuple(len(row) for row in orbit_sets(subgroup, object_count, action))


def picard_matrix(value):
    exceptional_images = [LINES[value[index]] for index in range(6)]
    h_image = tuple(
        LINES[value[6]][coordinate]
        + exceptional_images[0][coordinate]
        + exceptional_images[1][coordinate]
        for coordinate in range(7)
    )
    columns = [h_image] + exceptional_images
    return Matrix(
        [[columns[column][row] for column in range(7)] for row in range(7)]
    )


@lru_cache(maxsize=None)
def invariant_dimensions(subgroup):
    matrices = [picard_matrix(value) - I7 for value in small_generators(subgroup)]
    equations = Matrix.vstack(*matrices) if matrices else Matrix.zeros(0, 7)
    v6 = 7 - equations.rank() - 1
    v20 = len(orbit_sets(subgroup, 27, line_action)) - 1 - v6
    return int(v6), int(v20)


def restricted_orbit_count(subgroup, ambient_orbit, action):
    unseen = set(ambient_orbit)
    count = 0
    while unseen:
        seed = min(unseen)
        orbit = {action(value, seed) for value in subgroup}
        if not orbit <= set(ambient_orbit):
            raise AssertionError("ramification subgroup leaves ambient orbit")
        unseen -= orbit
        count += 1
    return count


def local_signature(decomposition, inertia, higher_layers, object_count, action):
    rows = []
    for ambient_orbit in orbit_sets(decomposition, object_count, action):
        degree = len(ambient_orbit)
        inertia_orbits = restricted_orbit_count(inertia, ambient_orbit, action)
        ramification_index = degree // inertia_orbits
        residue_degree = inertia_orbits
        conductor = Fraction(degree - inertia_orbits, 1)
        for subgroup, multiplicity in higher_layers:
            subgroup_orbits = restricted_orbit_count(subgroup, ambient_orbit, action)
            conductor += (
                Fraction(multiplicity * len(subgroup), len(inertia))
                * (degree - subgroup_orbits)
            )
        different = conductor / residue_degree
        rows.append(
            {
                "conductor": integer_or_fraction(conductor),
                "d": integer_or_fraction(different),
                "degree": degree,
                "e": ramification_index,
                "f": residue_degree,
            }
        )
    return sorted(
        rows,
        key=lambda row: (row["degree"], row["e"], row["f"], str(row["d"])),
    )


def representation_conductor(inertia, higher_layers):
    inertia_dims = invariant_dimensions(inertia)
    inertia_codimensions = (6 - inertia_dims[0], 20 - inertia_dims[1])
    swan = [Fraction(0), Fraction(0)]
    for subgroup, multiplicity in higher_layers:
        dimensions = invariant_dimensions(subgroup)
        codimensions = (6 - dimensions[0], 20 - dimensions[1])
        for index in range(2):
            swan[index] += (
                Fraction(multiplicity * len(subgroup), len(inertia))
                * codimensions[index]
            )
    artin = [inertia_codimensions[index] + swan[index] for index in range(2)]
    return {
        "artin": [integer_or_fraction(value) for value in artin],
        "inertia_codimensions": list(inertia_codimensions),
        "inertia_invariant_dimensions": list(inertia_dims),
        "swan": [integer_or_fraction(value) for value in swan],
    }


def integer_or_fraction(value: Fraction):
    return int(value) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def exact_fraction(value: int | str) -> Fraction:
    """Undo the compact JSON carrier used for an exact rational."""
    if type(value) is int:
        return Fraction(value, 1)
    if type(value) is str and value.count("/") == 1:
        numerator, denominator = value.split("/")
        return Fraction(int(numerator), int(denominator))
    raise TypeError("expected an exact integer-or-fraction carrier")


def subgroup_lattice_containing(base, ambient):
    subgroups = {base}
    frontier = [base]
    while frontier:
        subgroup = frontier.pop()
        generators = small_generators(subgroup)
        for value in ambient:
            if value in subgroup:
                continue
            new = generated(generators + [value])
            if new <= ambient and new not in subgroups:
                subgroups.add(new)
                frontier.append(new)
    return subgroups


def quotient_is_cyclic(ambient, normal):
    if not is_normal(ambient, normal):
        return False
    generators = small_generators(normal)
    return any(
        len(generated(generators + [value])) == len(ambient) for value in ambient
    )


def tame_action_on_order_three(inertia, wild, order_three):
    generator = min(value for value in order_three if value != IDENTITY)
    generator_inverse = INVERSES[generator]
    images = {
        compose(value, compose(generator, INVERSES[value]))
        for value in inertia
        if value not in wild
    }
    if images == {generator}:
        return "central"
    if images == {generator_inverse}:
        return "inversion"
    return "other"


def p5_report():
    order_five = min(
        value
        for value in WEYL
        if value != IDENTITY and len(generated((value,))) == 5
    )
    wild = generated((order_five,))
    wild_normalizer = normalizer(wild)
    lattice = subgroup_lattice_containing(wild, wild_normalizer)
    target_27 = (1, 1, 5, 5, 5, 10)
    target_36 = (1, 5, 10, 10, 10)
    decomposition_candidates = [
        subgroup
        for subgroup in lattice
        if orbit_pattern(subgroup, 27, line_action) == target_27
        and orbit_pattern(subgroup, 36, double_action) == target_36
    ]
    if len(decomposition_candidates) != 1:
        raise AssertionError("p=5 dual-action decomposition is not unique")
    decomposition = decomposition_candidates[0]
    inertia_candidates = [
        subgroup
        for subgroup in lattice
        if subgroup <= decomposition
        and wild <= subgroup
        and is_normal(decomposition, subgroup)
        and quotient_is_cyclic(decomposition, subgroup)
        and quotient_is_cyclic(subgroup, wild)
        and gcd(len(subgroup) // len(wild), 5) == 1
    ]
    candidates = []
    target_different = [0, 0, 7, 7, 7, 15]
    for inertia in inertia_candidates:
        base = representation_conductor(inertia, ())
        wild_dims = invariant_dimensions(wild)
        wild_codim_sum = (6 - wild_dims[0]) + (20 - wild_dims[1])
        coefficient = Fraction(len(wild) * wild_codim_sum, len(inertia))
        break_length = Fraction(36 - sum(base["inertia_codimensions"]), 1) / coefficient
        equation = filtration_multiplicity_equation(
            decomposition,
            inertia,
            wild,
            None,
            target_different,
            "wild_C5_layers",
        )
        if (
            break_length.denominator != 1
            or break_length < 1
            or equation["nonnegative_integer_solutions"]
            != [{"wild_C5_layers": 3}]
            or int(break_length) != 3
        ):
            continue
        layers = ((wild, int(break_length)),)
        local_27 = local_signature(
            decomposition, inertia, layers, 27, line_action
        )
        if different_vector(local_27) != target_different:
            raise AssertionError("p=5 solved filtration misses direct different rows")
        candidates.append(
            {
                "filtration_multiplicity_equation": equation,
                "local_27": local_27,
                "local_36": local_signature(decomposition, inertia, layers, 36, double_action),
                "lower_filtration_orders": [len(inertia)]
                + [len(wild)] * int(break_length)
                + [1],
                "orders_P_I_D": [len(wild), len(inertia), len(decomposition)],
                "representation": representation_conductor(inertia, layers),
            }
        )
    if len(candidates) != 1:
        raise AssertionError("p=5 discriminant does not force one chain")
    if candidates[0]["filtration_multiplicity_equation"] != {
        "base_different_exponents": [0, 0, 4, 4, 4, 9],
        "layer_contributions": {
            "wild_C5_layers": [0, 0, 1, 1, 1, 2]
        },
        "nonnegative_integer_solutions": [{"wild_C5_layers": 3}],
        "search_box_inclusive_upper_bound": 16,
        "target_different_exponents": target_different,
        "unique": True,
    }:
        raise AssertionError("p=5 filtration multiplicity equation changed")
    filtration_equation = {
        "base_different_vector_num_den": [
            [0, 1],
            [0, 1],
            [4, 1],
            [4, 1],
            [4, 1],
            [9, 1],
        ],
        "formal_integer_solution": 3,
        "nonnegative_integer_solutions": [3],
        "solution_variable": "wild_C5_layers",
        "target_different_vector_num_den": [
            [0, 1],
            [0, 1],
            [7, 1],
            [7, 1],
            [7, 1],
            [15, 1],
        ],
        "unique": True,
        "wild_C5_per_layer_contribution_num_den": [
            [0, 1],
            [0, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [2, 1],
        ],
    }
    return {
        "candidate": candidates[0],
        "dual_action_hit_counts_by_order": {
            str(order): sum(
                1
                for subgroup in lattice
                if len(subgroup) == order
                and orbit_pattern(subgroup, 27, line_action) == target_27
                and orbit_pattern(subgroup, 36, double_action) == target_36
            )
            for order in (5, 10, 20, 40)
        },
        "filtration_equation": filtration_equation,
        "lattice_orders": {str(key): value for key, value in sorted(Counter(map(len, lattice)).items())},
        "wild_normalizer_order": len(wild_normalizer),
    }


@lru_cache(maxsize=1)
def sylow_three_subgroup_classes():
    permutation_group = PermutationGroup(
        [Permutation(list(value)) for value in WEYL_GENERATORS]
    )
    sylow = frozenset(
        tuple(value(index) for index in range(27))
        for value in permutation_group.sylow_subgroup(3).generate_dimino()
    )
    subgroups = {frozenset((IDENTITY,))}
    frontier = list(subgroups)
    while frontier:
        subgroup = frontier.pop()
        generators = small_generators(subgroup)
        for value in sylow:
            if value in subgroup:
                continue
            new = generated(generators + [value])
            if new not in subgroups:
                subgroups.add(new)
                frontier.append(new)
    remaining = set(subgroups) - {frozenset((IDENTITY,))}
    representatives = []
    while remaining:
        subgroup = max(remaining, key=lambda value: (len(value), tuple(sorted(value))))
        conjugacy_orbit = {subgroup}
        queue = deque([subgroup])
        while queue:
            current = queue.popleft()
            for reflection in WEYL_GENERATORS:
                new = frozenset(
                    compose(reflection, compose(value, reflection))
                    for value in current
                )
                if new not in conjugacy_orbit:
                    conjugacy_orbit.add(new)
                    queue.append(new)
        remaining -= conjugacy_orbit
        representatives.append(subgroup)
    return tuple(representatives)


def tame_c3_decomposition_report():
    """Classify tame inertia using both actual decomposition carriers.

    At the three tame C3 primes the degree-27 local rows give D-orbits
    3,6,18 and inertia index three, while the degree-36 resolvent factors give
    D-orbits 3,6,9,18.  We enumerate every I=C3 and every cyclic-over-I
    subgroup D of its normalizer, then quotient by N_W(I)-conjugacy.
    """
    target_line = (3, 6, 18)
    target_double = (3, 6, 9, 18)
    target_local = (
        (3, 3, 1, 2),
        (6, 3, 2, 2),
        (18, 3, 6, 2),
    )
    target_local_36 = (
        (3, 3, 1, 2),
        (6, 3, 2, 2),
        (9, 3, 3, 2),
        (18, 3, 6, 2),
    )
    class_rows = []
    for inertia in sorted(
        (row for row in sylow_three_subgroup_classes() if len(row) == 3),
        key=lambda row: (
            orbit_pattern(row, 27, line_action),
            orbit_pattern(row, 36, double_action),
            tuple(sorted(row)),
        ),
    ):
        inertia_generators = small_generators(inertia)
        inertia_normalizer = normalizer(inertia, inertia_generators)
        raw_decompositions = set()
        for frobenius in inertia_normalizer:
            decomposition = generated(inertia_generators + [frobenius])
            if (
                is_normal(decomposition, inertia)
                and quotient_is_cyclic(decomposition, inertia)
                and orbit_pattern(decomposition, 27, line_action) == target_line
                and orbit_pattern(decomposition, 36, double_action) == target_double
            ):
                raw_decompositions.add(decomposition)
        remaining = set(raw_decompositions)
        decomposition_rows = []
        while remaining:
            decomposition = min(
                remaining, key=lambda row: (len(row), tuple(sorted(row)))
            )
            conjugates = {
                conjugate(value, decomposition) for value in inertia_normalizer
            }
            remaining -= conjugates
            local_27 = local_signature(
                decomposition, inertia, (), 27, line_action
            )
            local_36 = local_signature(
                decomposition, inertia, (), 36, double_action
            )
            compact = compact_local_signature(local_27)
            compact_36 = compact_local_signature(local_36)
            degree_36_discriminant_exponent = sum(
                row["f"] * exact_fraction(row["d"]) for row in local_36
            )
            decomposition_rows.append(
                {
                    "D_order": len(decomposition),
                    "D_over_I_order": len(decomposition) // len(inertia),
                    "degree_36_discriminant_exponent": integer_or_fraction(
                        degree_36_discriminant_exponent
                    ),
                    "double_six_orbits": list(
                        orbit_pattern(decomposition, 36, double_action)
                    ),
                    "local_27": local_27,
                    "local_36": local_36,
                    "matches_degree_27_local_rows": compact == target_local,
                    "matches_degree_36_local_rows": compact_36 == target_local_36,
                    "normalizer_conjugacy_orbit_size": len(conjugates),
                    "line_orbits": list(
                        orbit_pattern(decomposition, 27, line_action)
                    ),
                }
            )
        class_rows.append(
            {
                "accepted_decompositions": sorted(
                    decomposition_rows,
                    key=lambda row: (
                        not row["matches_degree_27_local_rows"],
                        not row["matches_degree_36_local_rows"],
                        row["D_order"],
                        row["normalizer_conjugacy_orbit_size"],
                    ),
                ),
                "inertia_class_size": len(WEYL) // len(inertia_normalizer) * 2,
                "inertia_double_six_orbits": list(
                    orbit_pattern(inertia, 36, double_action)
                ),
                "inertia_invariant_dimensions_V6_V20": list(
                    invariant_dimensions(inertia)
                ),
                "inertia_line_orbits": list(
                    orbit_pattern(inertia, 27, line_action)
                ),
                "inertia_normalizer_order": len(inertia_normalizer),
            }
        )
    degree_only_classes = [
        row
        for row in class_rows
        if any(
            decomposition["matches_degree_27_local_rows"]
            for decomposition in row["accepted_decompositions"]
        )
    ]
    accepted_classes = [
        row
        for row in class_rows
        if any(
            decomposition["matches_degree_27_local_rows"]
            and decomposition["matches_degree_36_local_rows"]
            and decomposition["degree_36_discriminant_exponent"] == 24
            for decomposition in row["accepted_decompositions"]
        )
    ]
    if sorted(row["inertia_class_size"] for row in degree_only_classes) != [80, 480]:
        raise AssertionError("tame C3 degree-carrier ambiguity changed")
    if len(accepted_classes) != 1 or accepted_classes[0]["inertia_class_size"] != 80:
        raise AssertionError("degree-36 local rows do not select the fixed-point-free C3")
    return {
        "all_inertia_classes": class_rows,
        "degree_27_decomposition_orbits": list(target_line),
        "degree_36_decomposition_orbits": list(target_double),
        "degree_36_local_discriminant_exponent": 24,
        "degree_36_local_authority": "theta36_KRASNER_CERTIFIED_AUTHORITY",
        "delta36_role": "BOUNDED_NON_RESULT_NONDEPENDENCY",
        "degree_36_local_rows_target": [list(row) for row in target_local_36],
        "decomposition_degree_carriers_unique_inertia": False,
        "degree_36_local_rows_unique_inertia": True,
        "degree_only_surviving_inertia_classes": sorted(
            degree_only_classes, key=lambda row: row["inertia_class_size"]
        ),
        "direct_degree_27_local_target": [list(row) for row in target_local],
        "selected_inertia_class": accepted_classes[0],
        "selected_inertia_tom_index": 6,
        "surviving_inertia_classes": sorted(
            accepted_classes, key=lambda row: row["inertia_class_size"]
        ),
    }


def simultaneous_triple_classes(triples):
    remaining = set(triples)
    output = []
    while remaining:
        triple = min(
            remaining,
            key=lambda value: tuple(
                (len(group), tuple(sorted(group))) for group in value
            ),
        )
        remaining.remove(triple)
        conjugacy_orbit = {triple}
        queue = deque([triple])
        while queue:
            current = queue.popleft()
            for reflection in WEYL_GENERATORS:
                new = tuple(
                    frozenset(
                        compose(reflection, compose(value, reflection))
                        for value in subgroup
                    )
                    for subgroup in current
                )
                if new not in conjugacy_orbit:
                    conjugacy_orbit.add(new)
                    queue.append(new)
        remaining -= conjugacy_orbit & remaining
        output.append((triple, len(conjugacy_orbit)))
    return output


def p3_triples():
    target_27 = (3, 6, 9, 9)
    target_36 = (3, 3, 3, 9, 18)
    selected = []
    for wild in sylow_three_subgroup_classes():
        descriptor = (
            len(wild),
            orbit_pattern(wild, 27, line_action),
            orbit_pattern(wild, 36, double_action),
        )
        if descriptor in {
            (3, (3,) * 9, (1, 1, 1) + (3,) * 11),
            (9, (3, 3, 3, 9, 9), (3, 3, 3, 9, 9, 9)),
        }:
            selected.append(wild)
    triples = set()
    for wild in selected:
        wild_generators = small_generators(wild)
        wild_normalizer = normalizer(wild, wild_generators)
        inertia_raw = {wild: wild_generators}
        for tame_generator in wild_normalizer:
            inertia = generated(wild_generators + [tame_generator])
            if gcd(len(inertia) // len(wild), 3) == 1:
                inertia_raw.setdefault(inertia, small_generators(inertia))
        remaining = set(inertia_raw)
        inertia_representatives = []
        while remaining:
            inertia = min(remaining, key=lambda value: (len(value), tuple(sorted(value))))
            remaining.remove(inertia)
            conjugates = {conjugate(value, inertia) for value in wild_normalizer}
            remaining -= conjugates
            inertia_representatives.append((inertia, inertia_raw[inertia]))
        for inertia, inertia_generators in inertia_representatives:
            inertia_normalizer = normalizer(inertia, inertia_generators)
            for frobenius in inertia_normalizer:
                decomposition = generated(inertia_generators + [frobenius])
                if len(decomposition) % 18:
                    continue
                if (
                    orbit_pattern(decomposition, 27, line_action) == target_27
                    and orbit_pattern(decomposition, 36, double_action) == target_36
                ):
                    triples.add((wild, inertia, decomposition))
    return simultaneous_triple_classes(triples)


def compact_local_signature(rows):
    return tuple((row["degree"], row["e"], row["f"], row["d"]) for row in rows)


def different_vector(rows):
    values = different_fraction_vector(rows)
    if any(value.denominator != 1 for value in values):
        raise AssertionError("different-exponent vector is not integral")
    return [int(value) for value in values]


def different_fraction_vector(rows):
    return [exact_fraction(row["d"]) for row in rows]


def filtration_multiplicity_equation(
    decomposition,
    inertia,
    wild,
    deep,
    target,
    wild_label,
    deep_label=None,
):
    base_fraction = different_fraction_vector(
        local_signature(decomposition, inertia, (), 27, line_action)
    )
    wild_once = different_fraction_vector(
        local_signature(decomposition, inertia, ((wild, 1),), 27, line_action)
    )
    wild_contribution = [
        right - left for left, right in zip(base_fraction, wild_once)
    ]
    contributions = [(wild_label, wild_contribution)]
    if deep is not None:
        deep_once = different_fraction_vector(
            local_signature(decomposition, inertia, ((deep, 1),), 27, line_action)
        )
        contributions.append(
            (
                deep_label,
                [right - left for left, right in zip(base_fraction, deep_once)],
            )
        )
    bound = max(target) + 1
    solutions = []
    if deep is None:
        for wild_layers in range(bound + 1):
            observed = [
                base_fraction[index] + wild_layers * wild_contribution[index]
                for index in range(len(base_fraction))
            ]
            if observed == list(map(Fraction, target)):
                solutions.append({wild_label: wild_layers})
    else:
        deep_contribution = contributions[1][1]
        for wild_layers in range(bound + 1):
            for deep_layers in range(bound + 1):
                observed = [
                    base_fraction[index]
                    + wild_layers * wild_contribution[index]
                    + deep_layers * deep_contribution[index]
                    for index in range(len(base_fraction))
                ]
                if observed == list(map(Fraction, target)):
                    solutions.append(
                        {
                            wild_label: wild_layers,
                            deep_label: deep_layers,
                        }
                    )
    return {
        "base_different_exponents": [
            integer_or_fraction(value) for value in base_fraction
        ],
        "layer_contributions": {
            label: [integer_or_fraction(value) for value in vector]
            for label, vector in contributions
        },
        "nonnegative_integer_solutions": solutions,
        "search_box_inclusive_upper_bound": bound,
        "target_different_exponents": target,
        "unique": len(solutions) == 1,
    }


def run_length(values):
    return [[key, count] for key, count in sorted(Counter(values).items())]


def fraction_pairs(values):
    return [
        [exact_fraction(value).numerator, exact_fraction(value).denominator]
        for value in values
    ]


def formal_two_layer_solution(equation, wild_label, deep_label):
    base = list(map(exact_fraction, equation["base_different_exponents"]))
    target = list(map(exact_fraction, equation["target_different_exponents"]))
    wild = list(
        map(exact_fraction, equation["layer_contributions"][wild_label])
    )
    deep = list(
        map(exact_fraction, equation["layer_contributions"][deep_label])
    )
    right = [target[index] - base[index] for index in range(len(base))]
    solution = None
    for left in range(len(base)):
        for right_index in range(left + 1, len(base)):
            determinant = (
                wild[left] * deep[right_index]
                - wild[right_index] * deep[left]
            )
            if determinant:
                candidate = (
                    (
                        right[left] * deep[right_index]
                        - right[right_index] * deep[left]
                    )
                    / determinant,
                    (
                        wild[left] * right[right_index]
                        - wild[right_index] * right[left]
                    )
                    / determinant,
                )
                if all(
                    base[index]
                    + candidate[0] * wild[index]
                    + candidate[1] * deep[index]
                    == target[index]
                    for index in range(len(base))
                ):
                    solution = candidate
                    break
        if solution is not None:
            break
    if solution is None or any(value.denominator != 1 for value in solution):
        raise AssertionError("two-layer different equation has no formal integer solution")
    return [int(value) for value in solution]


def p3_report():
    direct_target = (
        (3, 3, 1, 3),
        (6, 6, 1, 7),
        (9, 9, 1, 18),
        (9, 9, 1, 18),
    )
    target_different = [row[3] for row in direct_target]
    integral_candidates = []
    rejected_non_C3_squared_wild = []
    for triple, conjugacy_orbit_size in p3_triples():
        wild, inertia, decomposition = triple
        if len(wild) != 9:
            rejected_non_C3_squared_wild.append(
                {
                    "orders_P_I_D": [len(wild), len(inertia), len(decomposition)],
                    "reason": "direct_inertia_pair_requires_Sylow_C3_squared",
                    "simultaneous_conjugacy_orbit_size": conjugacy_orbit_size,
                }
            )
            continue
        order_three_subgroups = set()
        for value in wild:
            if value == IDENTITY:
                continue
            subgroup = generated((value,))
            if len(subgroup) == 3 and subgroup < wild:
                order_three_subgroups.add(subgroup)
        order_three_subgroups = sorted(
            order_three_subgroups, key=lambda subgroup: tuple(sorted(subgroup))
        )
        if len(order_three_subgroups) != 4:
            raise AssertionError("p=3 C3-squared does not contain four C3 subgroups")
        equations_by_subgroup = {
            subgroup: filtration_multiplicity_equation(
                decomposition,
                inertia,
                wild,
                subgroup,
                target_different,
                "wild_C3_squared_layers",
                "deep_C3_layers",
            )
            for subgroup in order_three_subgroups
        }
        profiles_by_subgroup = {
            subgroup: {
                "different_equation": equations_by_subgroup[subgroup],
                "double_six_orbits": list(
                    orbit_pattern(subgroup, 36, double_action)
                ),
                "invariant_dimensions_V6_V20": list(
                    invariant_dimensions(subgroup)
                ),
                "line_orbits": list(orbit_pattern(subgroup, 27, line_action)),
                "normal_in_decomposition": is_normal(decomposition, subgroup),
                "normal_in_inertia": is_normal(inertia, subgroup),
                "tame_action": tame_action_on_order_three(
                    inertia, wild, subgroup
                ),
                "tom_index": {
                    (0, 8): 6,
                    (4, 10): 7,
                    (2, 6): 8,
                }[invariant_dimensions(subgroup)],
            }
            for subgroup in order_three_subgroups
        }
        candidate_chains = []
        for wild_layers in range(1, 20):
            layer_choices = [(None, 0)] + [
                (subgroup, order_three_layers)
                for subgroup in order_three_subgroups
                for order_three_layers in range(1, 30)
            ]
            for order_three, order_three_layers in layer_choices:
                layers = [(wild, wild_layers)]
                if order_three is not None:
                    layers.append((order_three, order_three_layers))
                representation = representation_conductor(inertia, layers)
                if sum(
                    (exact_fraction(value) for value in representation["artin"]),
                    Fraction(0, 1),
                ) != 46:
                    continue
                local_27 = local_signature(
                    decomposition, inertia, layers, 27, line_action
                )
                local_36 = local_signature(
                    decomposition, inertia, layers, 36, double_action
                )
                if any(
                    type(row["d"]) is not int or type(row["conductor"]) is not int
                    for row in local_27 + local_36
                ):
                    continue
                order_three_type = None
                if order_three is not None:
                    order_three_type = profiles_by_subgroup[order_three]
                candidate_chains.append(
                    {
                        "filtration_multiplicity_equation": (
                            equations_by_subgroup.get(order_three)
                        ),
                        "local_27": local_27,
                        "local_36": local_36,
                        "matches_direct_pmaximal_27": compact_local_signature(local_27)
                        == direct_target,
                        "order_three_layers": order_three_layers,
                        "order_three_type": order_three_type,
                        "passes_last_graded_quotient_action": (
                            order_three is not None
                            and profiles_by_subgroup[order_three][
                                "normal_in_decomposition"
                            ]
                            and profiles_by_subgroup[order_three][
                                "normal_in_inertia"
                            ]
                            and profiles_by_subgroup[order_three]["tame_action"]
                            == "inversion"
                            and order_three_layers == 6
                        ),
                        "uses_unique_different_row_solution": (
                            order_three is not None
                            and equations_by_subgroup[order_three][
                                "nonnegative_integer_solutions"
                            ]
                            == [
                                {
                                    "deep_C3_layers": order_three_layers,
                                    "wild_C3_squared_layers": wild_layers,
                                }
                            ]
                        ),
                        "representation": representation,
                        "wild_layers": wild_layers,
                    }
                )
        if candidate_chains:
            integral_candidates.append(
                {
                    "all_C3_subgroup_profiles": [
                        profiles_by_subgroup[subgroup]
                        for subgroup in order_three_subgroups
                    ],
                    "candidate_chains": candidate_chains,
                    "inertia_double_orbits": list(
                        orbit_pattern(inertia, 36, double_action)
                    ),
                    "inertia_line_orbits": list(
                        orbit_pattern(inertia, 27, line_action)
                    ),
                    "orders_P_I_D": [len(wild), len(inertia), len(decomposition)],
                    "simultaneous_conjugacy_orbit_size": conjugacy_orbit_size,
                    "wild_double_orbits": list(
                        orbit_pattern(wild, 36, double_action)
                    ),
                    "wild_line_orbits": list(orbit_pattern(wild, 27, line_action)),
                }
            )
    accepted = []
    for row in integral_candidates:
        for chain in row["candidate_chains"]:
            if (
                chain["matches_direct_pmaximal_27"]
                and chain["passes_last_graded_quotient_action"]
                and chain["uses_unique_different_row_solution"]
            ):
                accepted.append(
                    {
                        "chain": chain,
                        "orders_P_I_D": row["orders_P_I_D"],
                        "simultaneous_conjugacy_orbit_size": row[
                            "simultaneous_conjugacy_orbit_size"
                        ],
                    }
                )
    accepted.sort(key=lambda row: row["orders_P_I_D"])
    if [row["orders_P_I_D"] for row in accepted] != [[9, 18, 18], [9, 18, 36]]:
        raise AssertionError("p=3 accepted decomposition ambiguity changed")
    expected_equation = {
        "base_different_exponents": [2, 5, 8, 8],
        "layer_contributions": {
            "deep_C3_layers": [0, 0, 1, 1],
            "wild_C3_squared_layers": [1, 2, 4, 4],
        },
        "nonnegative_integer_solutions": [
            {"deep_C3_layers": 6, "wild_C3_squared_layers": 1}
        ],
        "search_box_inclusive_upper_bound": 19,
        "target_different_exponents": target_different,
        "unique": True,
    }
    if any(
        not deep_exact(
            row["chain"]["filtration_multiplicity_equation"], expected_equation
        )
        for row in accepted
    ):
        raise AssertionError("p=3 filtration multiplicity equation changed")

    def aggregate_deep_profiles(candidate):
        grouped = {}
        for profile in candidate["all_C3_subgroup_profiles"]:
            grouped.setdefault(profile["tom_index"], []).append(profile)
        rows = []
        for tom_index, profiles in sorted(grouped.items()):
            first = profiles[0]
            equation = first["different_equation"]
            invariant = first["invariant_dimensions_V6_V20"]
            line_orbits = first["line_orbits"]
            double_orbits = first["double_six_orbits"]
            if any(
                profile["different_equation"] != equation
                or profile["invariant_dimensions_V6_V20"] != invariant
                or profile["line_orbits"] != line_orbits
                or profile["double_six_orbits"] != double_orbits
                for profile in profiles
            ):
                raise AssertionError("one C3 ToM profile has inconsistent carriers")
            nonnegative = sorted(
                [
                    solution["wild_C3_squared_layers"],
                    solution["deep_C3_layers"],
                ]
                for solution in equation["nonnegative_integer_solutions"]
            )
            rows.append(
                {
                    "double_six_orbit_rle": run_length(double_orbits),
                    "fixed_dimensions_V6_V20": invariant,
                    "formal_integer_solution": formal_two_layer_solution(
                        equation,
                        "wild_C3_squared_layers",
                        "deep_C3_layers",
                    ),
                    "line_orbit_rle": run_length(line_orbits),
                    "multiplicity": len(profiles),
                    "nonnegative_integer_solutions": nonnegative,
                    "per_layer_different_contribution_num_den": fraction_pairs(
                        equation["layer_contributions"]["deep_C3_layers"]
                    ),
                    "tom_index": tom_index,
                }
            )
        return rows

    deep_profile_rows = aggregate_deep_profiles(integral_candidates[0])
    if any(
        aggregate_deep_profiles(candidate) != deep_profile_rows
        for candidate in integral_candidates[1:]
    ):
        raise AssertionError("deep C3 profile exhaustion depends on (I,D)")
    deep_exhaustion = {
        "base_different_vector_num_den": [[2, 1], [5, 1], [8, 1], [8, 1]],
        "profiles": deep_profile_rows,
        "selected_tom_index": 7,
        "solution_variable_order": [
            "wild_C3_squared_layers",
            "deep_C3_layers",
        ],
        "target_different_vector_num_den": [
            [3, 1],
            [7, 1],
            [18, 1],
            [18, 1],
        ],
        "wild_C3_squared_per_layer_contribution_num_den": [
            [1, 1],
            [2, 1],
            [4, 1],
            [4, 1],
        ],
    }
    observed_selected_actions = {
        profile["tame_action"]
        for candidate in integral_candidates
        for profile in candidate["all_C3_subgroup_profiles"]
        if profile["tom_index"] == 7
    }
    if observed_selected_actions != {"central", "inversion"}:
        raise AssertionError("selected deep C3 tame-action alternatives changed")
    deep_exhaustion["selected_profile_tame_action_by_inertia_tom_index"] = {
        "140": "inversion",
        "142": "central",
    }
    if deep_exhaustion != {
        "base_different_vector_num_den": [[2, 1], [5, 1], [8, 1], [8, 1]],
        "profiles": [
            {
                "double_six_orbit_rle": [[3, 12]],
                "fixed_dimensions_V6_V20": [0, 8],
                "formal_integer_solution": [7, -18],
                "line_orbit_rle": [[3, 9]],
                "multiplicity": 2,
                "nonnegative_integer_solutions": [],
                "per_layer_different_contribution_num_den": [
                    [1, 3],
                    [2, 3],
                    [1, 1],
                    [1, 1],
                ],
                "tom_index": 6,
            },
            {
                "double_six_orbit_rle": [[1, 6], [3, 10]],
                "fixed_dimensions_V6_V20": [4, 10],
                "formal_integer_solution": [1, 6],
                "line_orbit_rle": [[1, 9], [3, 6]],
                "multiplicity": 1,
                "nonnegative_integer_solutions": [[1, 6]],
                "per_layer_different_contribution_num_den": [
                    [0, 1],
                    [0, 1],
                    [1, 1],
                    [1, 1],
                ],
                "tom_index": 7,
            },
            {
                "double_six_orbit_rle": [[1, 3], [3, 11]],
                "fixed_dimensions_V6_V20": [2, 6],
                "formal_integer_solution": [7, -18],
                "line_orbit_rle": [[3, 9]],
                "multiplicity": 1,
                "nonnegative_integer_solutions": [],
                "per_layer_different_contribution_num_den": [
                    [1, 3],
                    [2, 3],
                    [1, 1],
                    [1, 1],
                ],
                "tom_index": 8,
            },
        ],
        "selected_tom_index": 7,
        "selected_profile_tame_action_by_inertia_tom_index": {
            "140": "inversion",
            "142": "central",
        },
        "solution_variable_order": [
            "wild_C3_squared_layers",
            "deep_C3_layers",
        ],
        "target_different_vector_num_den": [
            [3, 1],
            [7, 1],
            [18, 1],
            [18, 1],
        ],
        "wild_C3_squared_per_layer_contribution_num_den": [
            [1, 1],
            [2, 1],
            [4, 1],
            [4, 1],
        ],
    }:
        raise AssertionError("deep C3 global ToM profile exhaustion changed")
    pair_normal_multiplicities = []
    for candidate in sorted(
        integral_candidates,
        key=lambda row: (
            row["orders_P_I_D"],
            row["simultaneous_conjugacy_orbit_size"],
            canonical_leaf_bytes(row["all_C3_subgroup_profiles"]),
        ),
    ):
        grouped = {}
        for profile in candidate["all_C3_subgroup_profiles"]:
            grouped.setdefault(profile["tom_index"], []).append(profile)
        selected_actions = {
            profile["tame_action"] for profile in grouped[7]
        }
        if selected_actions == {"inversion"}:
            inertia_tom_index = 140
        elif selected_actions == {"central"}:
            inertia_tom_index = 142
        else:
            raise AssertionError("selected deep C3 tame action is ambiguous")
        decomposition_tom_index = (
            inertia_tom_index
            if candidate["orders_P_I_D"][2] == 18
            else 206
        )
        pair_normal_multiplicities.append(
            {
                "decomposition_tom_index": decomposition_tom_index,
                "inertia_tom_index": inertia_tom_index,
                "orders_P_I_D": candidate["orders_P_I_D"],
                "profiles": [
                    {
                        "multiplicity": len(profiles),
                        "nonnegative_integer_solution_multiset": sorted(
                            [
                                solution["wild_C3_squared_layers"],
                                solution["deep_C3_layers"],
                            ]
                            for profile in profiles
                            for solution in profile["different_equation"][
                                "nonnegative_integer_solutions"
                            ]
                        ),
                        "normal_in_decomposition_multiplicity": sum(
                            profile["normal_in_decomposition"]
                            for profile in profiles
                        ),
                        "normal_in_inertia_multiplicity": sum(
                            profile["normal_in_inertia"] for profile in profiles
                        ),
                        "tame_actions": [
                            [action, multiplicity]
                            for action, multiplicity in sorted(
                                Counter(
                                    profile["tame_action"]
                                    for profile in profiles
                                ).items()
                            )
                        ],
                        "tom_index": tom_index,
                    }
                    for tom_index, profiles in sorted(grouped.items())
                ],
                "simultaneous_conjugacy_orbit_size": candidate[
                    "simultaneous_conjugacy_orbit_size"
                ],
            }
        )
    pair_normal_multiplicities.sort(
        key=lambda row: (
            row["decomposition_tom_index"],
            row["inertia_tom_index"],
        )
    )
    selected_deep_is_normal_everywhere = all(
        row["chain"]["order_three_type"]["tom_index"] == 7
        and row["chain"]["order_three_type"]["normal_in_inertia"]
        and row["chain"]["order_three_type"]["normal_in_decomposition"]
        for row in accepted
    )
    return {
        "accepted_after_direct_and_serre_filters": accepted,
        "all_integral_discriminant_candidates": sorted(
            integral_candidates, key=lambda row: row["orders_P_I_D"]
        ),
        "direct_pmaximal_27_target": [list(row) for row in direct_target],
        "deep_C3_exhaustion": deep_exhaustion,
        "deep_C3_normal_in_all_surviving_decomposition_groups": (
            selected_deep_is_normal_everywhere
        ),
        "deep_C3_pair_normal_multiplicities": pair_normal_multiplicities,
        "filtration_multiplicity_equation": expected_equation,
        "rejected_non_C3_squared_wild": sorted(
            rejected_non_C3_squared_wild, key=lambda row: row["orders_P_I_D"]
        ),
        "serre_law": {
            "formula": "theta_i(s*tau*s^-1)=theta_0(s)^i*theta_i(tau)",
            "last_nonzero_grade": 7,
            "tame_character": -1,
            "central_competitor_rejected": True,
            "required_action": "inversion",
        },
    }


def cyclic_subgroup_classes(order: int):
    subgroups = set()
    for value in WEYL:
        if value == IDENTITY:
            continue
        if order == 2:
            if compose(value, value) != IDENTITY:
                continue
        elif order == 3:
            if compose(value, compose(value, value)) != IDENTITY:
                continue
        else:  # pragma: no cover - internal API is deliberately narrow
            raise ValueError("only cyclic orders 2 and 3 are supported")
        subgroup = generated((value,))
        if len(subgroup) == order:
            subgroups.add(subgroup)
    remaining = set(subgroups)
    output = []
    while remaining:
        representative = min(remaining, key=lambda row: tuple(sorted(row)))
        conjugacy_orbit = {representative}
        queue = deque([representative])
        while queue:
            current = queue.popleft()
            for reflection in WEYL_GENERATORS:
                new = conjugate(reflection, current)
                if new not in conjugacy_orbit:
                    conjugacy_orbit.add(new)
                    queue.append(new)
        remaining -= conjugacy_orbit
        representative_normalizer = normalizer(representative)
        normalizer_order = len(representative_normalizer)
        if len(conjugacy_orbit) * normalizer_order != len(WEYL):
            raise AssertionError("cyclic subgroup orbit-stabilizer mismatch")
        generator = min(value for value in representative if value != IDENTITY)
        generator_inverse = INVERSES[generator]
        inversion_witness = any(
            compose(value, compose(generator, INVERSES[value]))
            == generator_inverse
            for value in representative_normalizer
        )
        if order == 3 and not inversion_witness:
            raise AssertionError("C3 normalizer does not realize inversion")
        output.append(
            {
                # For the prime orders used here the normalizer acts by the
                # full automorphism group of the cyclic subgroup.  Thus all
                # nonidentity elements form one W(E6)-class.  Record that
                # element-class size (the convention used by the C58
                # discriminator), while retaining the subgroup orbit size so
                # the normalizer calculation remains independently visible.
                "class_size": len(conjugacy_orbit) * (order - 1),
                "double_six_orbits": list(
                    orbit_pattern(representative, 36, double_action)
                ),
                "invariant_dimensions_V6_V20": list(
                    invariant_dimensions(representative)
                ),
                "line_orbits": list(orbit_pattern(representative, 27, line_action)),
                "normalizer_order": normalizer_order,
                "normalizer_realizes_inversion": inversion_witness,
                "order": order,
                "subgroup_class_size": len(conjugacy_orbit),
            }
        )
    return sorted(
        output,
        key=lambda row: (
            row["line_orbits"],
            row["double_six_orbits"],
            row["class_size"],
        ),
    )


def action_arrays(*, one_based: bool = True):
    double_generators = [
        [DOUBLE_INDEX[c57.act(generator, value)] for value in DOUBLE_SIXES]
        for generator in WEYL_GENERATORS
    ]
    picard_generators = []
    for root in ROOTS:
        matrix = c57.picard_matrix(root)
        picard_generators.append(
            [
                [int(matrix[row, column]) for column in range(matrix.cols)]
                for row in range(matrix.rows)
            ]
        )
    line_generators = [list(value) for value in WEYL_GENERATORS]
    if one_based:
        double_generators = [
            [value + 1 for value in generator] for generator in double_generators
        ]
        line_generators = [
            [value + 1 for value in generator] for generator in line_generators
        ]
    return {
        "double_six_generators": double_generators,
        "line_generators": line_generators,
        "picard_generators": picard_generators,
    }


@lru_cache(maxsize=1)
def exhaustive_tom_dual_action_report():
    """Scan every TomLib subgroup class in a separate GAP implementation."""

    actions = action_arrays(one_based=True)
    line_lists = json.dumps(actions["line_generators"], separators=(",", ":"))
    double_lists = json.dumps(
        actions["double_six_generators"], separators=(",", ":")
    )
    script = f"""
if LoadPackage("tomlib") <> true then Error("tomlib unavailable"); fi;;
SizeScreen([1000000,1000000]);;
W27gens := List({line_lists},PermList);;
W36gens := List({double_lists},PermList);;
W27 := Group(W27gens);;
W36 := Group(W36gens);;
phi36 := GroupHomomorphismByImages(W27,W36,W27gens,W36gens);;
if Size(W27)<>51840 or not IsBijective(phi36) then
  Error("frozen actions do not identify W(E6)");
fi;;
tom := TableOfMarks("U4(2).2");;
tomGroup := UnderlyingGroup(tom);;
toW := IsomorphismGroups(tomGroup,W27);;
if toW=fail or not IsBijective(toW) then Error("ToM identification failed"); fi;;
tomOrders := OrdersTom(tom);;
TomImage := index -> Image(toW,RepresentativeTom(tom,index));;
OrbitSizes := function(group,degree)
  return SortedList(List(Orbits(group,[1..degree]),Length));
end;;
BoolInt := function(value) if value then return 1; fi; return 0; end;;
TomIndex := function(group)
  local candidate;
  for candidate in [1..Length(tomOrders)] do
    if tomOrders[candidate]=Size(group) and
       IsConjugate(W27,group,TomImage(candidate)) then
      return candidate;
    fi;
  od;
  Error("subgroup missing from table of marks");
end;;
Print("COUNT|",Length(tomOrders),"\\n");
for index in [1..Length(tomOrders)] do
  decomposition := TomImage(index);;
  lineOrbits := OrbitSizes(decomposition,27);;
  doubleOrbits := OrbitSizes(Image(phi36,decomposition),36);;
  if lineOrbits=[3,6,9,9] and doubleOrbits=[3,3,3,9,18] then
    wild := SylowSubgroup(decomposition,3);;
    normalFlag := IsNormal(decomposition,wild);;
    cyclicFlag := false;;
    quotientId := [0,0];;
    if normalFlag then
      quotient := FactorGroup(decomposition,wild);;
      cyclicFlag := IsCyclic(quotient);;
      quotientId := IdGroup(quotient);;
    fi;;
    groupId := IdGroup(decomposition);;
    wildId := IdGroup(wild);;
    Print("P3|",index,"|",Size(decomposition),"|",groupId[1],"|",groupId[2],
      "|",wildId[1],"|",wildId[2],"|",BoolInt(normalFlag),"|",BoolInt(cyclicFlag),
      "|",quotientId[1],"|",quotientId[2],"\\n");
    for subgroupClass in ConjugacyClassesSubgroups(decomposition) do
      inertia := Representative(subgroupClass);;
      if OrbitSizes(inertia,27)=[3,6,9,9] and IsNormal(decomposition,inertia) and
         IsCyclic(FactorGroup(decomposition,inertia)) then
        inertiaWild := SylowSubgroup(inertia,3);;
        if IsNormal(decomposition,inertiaWild) and IsNormal(inertia,inertiaWild) and
           IsCyclic(FactorGroup(inertia,inertiaWild)) then
          Print("PAIR3|",index,"|",TomIndex(inertia),"|",
            Size(decomposition)/Size(inertia),"\\n");
        fi;
      fi;
    od;
  fi;;
  if lineOrbits=[1,1,5,5,5,10] and doubleOrbits=[1,5,10,10,10] then
    wild := SylowSubgroup(decomposition,5);;
    groupId := IdGroup(decomposition);;
    Print("P5|",index,"|",Size(decomposition),"|",groupId[1],"|",groupId[2],
      "|",BoolInt(IsNormal(decomposition,wild)),"|",Size(Normalizer(W27,wild)),"\\n");
    for subgroupClass in ConjugacyClassesSubgroups(decomposition) do
      inertia := Representative(subgroupClass);;
      if OrbitSizes(inertia,27)=[1,1,5,5,5,10] and
         IsNormal(decomposition,inertia) and
         IsCyclic(FactorGroup(decomposition,inertia)) then
        inertiaWild := SylowSubgroup(inertia,5);;
        if IsNormal(decomposition,inertiaWild) and IsNormal(inertia,inertiaWild) and
           IsCyclic(FactorGroup(inertia,inertiaWild)) then
          Print("PAIR5|",index,"|",TomIndex(inertia),"|",
            Size(decomposition)/Size(inertia),"\\n");
        fi;
      fi;
    od;
  fi;;
od;;
characterTable := CharacterTable("U4(2).2");;
characterOrders := OrdersClassRepresentatives(characterTable);;
characterSizes := SizesConjugacyClasses(characterTable);;
for index in [1..Length(tomOrders)] do
  if tomOrders[index]=2 then
    group := TomImage(index);;
    lineOrbits := OrbitSizes(group,27);;
    doubleOrbits := OrbitSizes(Image(phi36,group),36);;
    involution := First(Elements(group),element->Order(element)=2);;
    centralizerOrder := Size(Centralizer(W27,involution));;
    classSize := Size(W27)/centralizerOrder;;
    matches := Filtered([1..NrConjugacyClasses(characterTable)],candidate->
      characterOrders[candidate]=2 and characterSizes[candidate]=classSize);;
    if Length(matches)<>1 then Error("order-two class match not unique"); fi;;
    Print("C2|",index,"|",Number(lineOrbits,value->value=1),"|",
      Number(lineOrbits,value->value=2),"|",
      Number(doubleOrbits,value->value=1),"|",
      Number(doubleOrbits,value->value=2),"|",Size(Normalizer(W27,group)),
      "|",classSize,"|",matches[1],"\\n");
    if lineOrbits=Concatenation([1,1,1],List([1..12],i->2)) and
       doubleOrbits=Concatenation([1,1,1,1],List([1..16],i->2)) then
      Print("ARCH|",index,"|",Size(group),"|",Size(Normalizer(W27,group)),
        "|",classSize,"|",characterOrders[matches[1]],"|",characterSizes[matches[1]],
        "|",Size(characterTable)/characterSizes[matches[1]],"|",Length(matches),
        "|",matches[1],"|",Size(characterTable),"\\n");
    fi;;
  fi;;
od;;
QUIT;
"""
    completed = subprocess.run(
        ["/usr/bin/gap", "-q"],
        input=script.encode("ascii"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=180,
    )
    if completed.returncode != 0:
        raise StrictDataError(
            "independent GAP ToM exhaustion failed: "
            + completed.stderr.decode("utf-8", "replace")[-1000:]
        )
    class_count = None
    p3_rows = []
    p5_rows = []
    p3_pairs = []
    p5_pairs = []
    order_two_rows = []
    arch_rows = []
    for raw_line in completed.stdout.decode("ascii").splitlines():
        pieces = raw_line.strip().split("|")
        if pieces[0] == "COUNT" and len(pieces) == 2:
            class_count = int(pieces[1])
        elif pieces[0] == "P3" and len(pieces) == 11:
            values = list(map(int, pieces[1:]))
            p3_rows.append(
                {
                    "id_group": values[2:4],
                    "order": values[1],
                    "tame_quotient_cyclic": bool(values[7]),
                    "tame_quotient_id_group": values[8:10],
                    "tom_index": values[0],
                    "wild_sylow_3_id_group": values[4:6],
                    "wild_sylow_3_normal": bool(values[6]),
                }
            )
        elif pieces[0] == "P5" and len(pieces) == 7:
            values = list(map(int, pieces[1:]))
            p5_rows.append(
                {
                    "id_group": values[2:4],
                    "order": values[1],
                    "sylow_5_normal": bool(values[4]),
                    "sylow_5_normalizer_order": values[5],
                    "tom_index": values[0],
                }
            )
        elif pieces[0] == "PAIR3" and len(pieces) == 4:
            p3_pairs.append(list(map(int, pieces[1:])))
        elif pieces[0] == "PAIR5" and len(pieces) == 4:
            p5_pairs.append(list(map(int, pieces[1:])))
        elif pieces[0] == "C2" and len(pieces) == 9:
            values = list(map(int, pieces[1:]))
            order_two_rows.append(
                {
                    "character_table_element_class_index": values[7],
                    "double_six_orbit_rle": [[1, values[3]], [2, values[4]]],
                    "element_class_size": values[6],
                    "line_orbit_rle": [[1, values[1]], [2, values[2]]],
                    "normalizer_order": values[5],
                    "tom_index": values[0],
                }
            )
        elif pieces[0] == "ARCH" and len(pieces) == 11:
            values = list(map(int, pieces[1:]))
            arch_rows.append(
                {
                    "character_table_group_order": values[9],
                    "character_table_name": "U4(2).2",
                    "element_centralizer_order": values[6],
                    "element_class_index": values[8],
                    "element_class_matching_indices": [values[8]],
                    "element_class_order": values[4],
                    "element_class_size": values[5],
                    "subgroup_normalizer_order": values[2],
                    "subgroup_order": values[1],
                    "subgroup_tom_index": values[0],
                    "unique_order_and_class_size_match": values[7] == 1,
                }
            )
    p3_rows.sort(key=lambda row: row["tom_index"])
    p5_rows.sort(key=lambda row: row["tom_index"])
    p3_pairs.sort()
    p5_pairs.sort()
    order_two_rows.sort(key=lambda row: row["tom_index"])
    expected_p3 = [
        [140, 18, [18, 4]],
        [142, 18, [18, 3]],
        [206, 36, [36, 10]],
    ]
    expected_p5 = [
        [147, 20, [20, 3]],
        [247, 60, [60, 5]],
        [295, 120, [120, 34]],
    ]
    if (
        class_count is None
        or [[row["tom_index"], row["order"], row["id_group"]] for row in p3_rows]
        != expected_p3
        or [[row["tom_index"], row["order"], row["id_group"]] for row in p5_rows]
        != expected_p5
        or p3_pairs != [[140, 140, 1], [142, 142, 1], [206, 140, 2], [206, 142, 2]]
        or p5_pairs != [[147, 147, 1]]
        or order_two_rows
        != [
            {
                "character_table_element_class_index": 16,
                "double_six_orbit_rle": [[1, 16], [2, 10]],
                "element_class_size": 36,
                "line_orbit_rle": [[1, 15], [2, 6]],
                "normalizer_order": 1440,
                "tom_index": 2,
            },
            {
                "character_table_element_class_index": 2,
                "double_six_orbit_rle": [[1, 12], [2, 12]],
                "element_class_size": 45,
                "line_orbit_rle": [[1, 3], [2, 12]],
                "normalizer_order": 1152,
                "tom_index": 3,
            },
            {
                "character_table_element_class_index": 3,
                "double_six_orbit_rle": [[1, 8], [2, 14]],
                "element_class_size": 270,
                "line_orbit_rle": [[1, 7], [2, 10]],
                "normalizer_order": 192,
                "tom_index": 4,
            },
            {
                "character_table_element_class_index": 17,
                "double_six_orbit_rle": [[1, 4], [2, 16]],
                "element_class_size": 540,
                "line_orbit_rle": [[1, 3], [2, 12]],
                "normalizer_order": 96,
                "tom_index": 5,
            },
        ]
        or len(arch_rows) != 1
    ):
        raise StrictDataError(
            "exhaustive GAP ToM decomposition/inertia hits changed: "
            f"class_count={class_count!r}, p3={p3_rows!r}, p5={p5_rows!r}, "
            f"pairs3={p3_pairs!r}, pairs5={p5_pairs!r}, arch={arch_rows!r}, "
            f"stdout={completed.stdout.decode('utf-8', 'replace')[-2000:]!r}, "
            f"stderr={completed.stderr.decode('utf-8', 'replace')[-1000:]!r}"
        )
    if (
        not all(row["wild_sylow_3_normal"] for row in p3_rows)
        or [row["tame_quotient_cyclic"] for row in p3_rows]
        != [True, True, False]
        or p3_rows[2]["tame_quotient_id_group"] != [4, 2]
        or [row["sylow_5_normal"] for row in p5_rows] != [True, False, False]
        or any(row["sylow_5_normalizer_order"] != 40 for row in p5_rows)
    ):
        raise StrictDataError("wild-normalizer/tame-quotient ToM filter changed")
    arch = arch_rows[0]
    if arch != {
        "character_table_group_order": 51840,
        "character_table_name": "U4(2).2",
        "element_centralizer_order": 96,
        "element_class_index": 17,
        "element_class_matching_indices": [17],
        "element_class_order": 2,
        "element_class_size": 540,
        "subgroup_normalizer_order": 96,
        "subgroup_order": 2,
        "subgroup_tom_index": 5,
        "unique_order_and_class_size_match": True,
    }:
        raise StrictDataError("archimedean ToM/character-table match changed")
    return {
        "complex_conjugation_character_match": arch,
        "order_two_profiles_without_picard": order_two_rows,
        "p3_all_tom_decomposition_pattern_hits": p3_rows,
        "p3_valid_decomposition_inertia_pairs": p3_pairs,
        "p5_all_tom_decomposition_pattern_hits": p5_rows,
        "p5_valid_decomposition_inertia_pairs": p5_pairs,
        "table_of_marks_class_count": class_count,
        "table_of_marks_name": "U4(2).2",
    }


def build_group_report():
    upstream_lock = verify_upstream_carriers()
    tom_exhaustion = exhaustive_tom_dual_action_report()
    if len(WEYL) != 51840 or len(LINES) != 27 or len(DOUBLE_SIXES) != 36:
        raise AssertionError("frozen W(E6) action counts changed")
    order_three = cyclic_subgroup_classes(3)
    tame_selected = [
        row
        for row in order_three
        if row["line_orbits"] == [3] * 9
        and row["double_six_orbits"] == [3] * 12
    ]
    tame_competitor = [
        row
        for row in order_three
        if row["line_orbits"] == [3] * 9
        and row["double_six_orbits"] == [1, 1, 1] + [3] * 11
    ]
    if len(tame_selected) != 1 or len(tame_competitor) != 1:
        raise AssertionError("dual action no longer separates the tame C3 classes")
    if tame_selected[0]["class_size"] != 80 or tame_competitor[0]["class_size"] != 480:
        raise AssertionError("tame C3 conjugacy class sizes changed")
    tame_decomposition = tame_c3_decomposition_report()
    surviving_descriptors = {
        (
            tuple(row["inertia_line_orbits"]),
            tuple(row["inertia_double_six_orbits"]),
        )
        for row in tame_decomposition["degree_only_surviving_inertia_classes"]
    }
    if surviving_descriptors != {
        (tuple(tame_selected[0]["line_orbits"]), tuple(tame_selected[0]["double_six_orbits"])),
        (tuple(tame_competitor[0]["line_orbits"]), tuple(tame_competitor[0]["double_six_orbits"])),
    }:
        raise AssertionError("decomposition filter and C3 class table disagree")
    selected_descriptor = tame_decomposition["selected_inertia_class"]
    if (
        selected_descriptor["inertia_line_orbits"] != tame_selected[0]["line_orbits"]
        or selected_descriptor["inertia_double_six_orbits"]
        != tame_selected[0]["double_six_orbits"]
    ):
        raise AssertionError("degree-36 local rows selected the wrong C3 class")

    order_two = cyclic_subgroup_classes(2)
    order_two_profiles = []
    for gap_row in tom_exhaustion["order_two_profiles_without_picard"]:
        matches = [
            row
            for row in order_two
            if [[key, value] for key, value in sorted(Counter(row["line_orbits"]).items())]
            == gap_row["line_orbit_rle"]
            and [
                [key, value]
                for key, value in sorted(Counter(row["double_six_orbits"]).items())
            ]
            == gap_row["double_six_orbit_rle"]
            and row["normalizer_order"] == gap_row["normalizer_order"]
            and row["class_size"] == gap_row["element_class_size"]
        ]
        if len(matches) != 1:
            raise AssertionError("GAP/Python order-two profile match is not unique")
        order_two_profiles.append(
            {
                **gap_row,
                "fixed_dimensions_V6_V20": matches[0][
                    "invariant_dimensions_V6_V20"
                ],
            }
        )
    if order_two_profiles != [
        {
            "character_table_element_class_index": 16,
            "double_six_orbit_rle": [[1, 16], [2, 10]],
            "element_class_size": 36,
            "fixed_dimensions_V6_V20": [5, 15],
            "line_orbit_rle": [[1, 15], [2, 6]],
            "normalizer_order": 1440,
            "tom_index": 2,
        },
        {
            "character_table_element_class_index": 2,
            "double_six_orbit_rle": [[1, 12], [2, 12]],
            "element_class_size": 45,
            "fixed_dimensions_V6_V20": [2, 12],
            "line_orbit_rle": [[1, 3], [2, 12]],
            "normalizer_order": 1152,
            "tom_index": 3,
        },
        {
            "character_table_element_class_index": 3,
            "double_six_orbit_rle": [[1, 8], [2, 14]],
            "element_class_size": 270,
            "fixed_dimensions_V6_V20": [4, 12],
            "line_orbit_rle": [[1, 7], [2, 10]],
            "normalizer_order": 192,
            "tom_index": 4,
        },
        {
            "character_table_element_class_index": 17,
            "double_six_orbit_rle": [[1, 4], [2, 16]],
            "element_class_size": 540,
            "fixed_dimensions_V6_V20": [3, 11],
            "line_orbit_rle": [[1, 3], [2, 12]],
            "normalizer_order": 96,
            "tom_index": 5,
        },
    ]:
        raise AssertionError("order-two ToM profiles changed")
    reflection = [
        row
        for row in order_two
        if row["line_orbits"] == [1] * 15 + [2] * 6
    ]
    infinity = [
        row
        for row in order_two
        if row["line_orbits"] == [1] * 3 + [2] * 12
        and row["double_six_orbits"] == [1] * 4 + [2] * 16
    ]
    if len(reflection) != 1 or len(infinity) != 1:
        raise AssertionError("reflection or complex-conjugation class is not unique")
    if reflection[0]["invariant_dimensions_V6_V20"] != [5, 15]:
        raise AssertionError("root-reflection fixed dimensions changed")
    if infinity[0]["invariant_dimensions_V6_V20"] != [3, 11]:
        raise AssertionError("complex-conjugation fixed dimensions changed")

    p3 = p3_report()
    p5 = p5_report()
    p3_accepted = p3["accepted_after_direct_and_serre_filters"]
    for row in p3_accepted:
        if row["chain"]["representation"]["swan"] != [5, 18]:
            raise AssertionError("p=3 Swan conductor changed")
        if row["chain"]["representation"]["artin"] != [11, 35]:
            raise AssertionError("p=3 Artin conductor changed")
    if p5["candidate"]["representation"]["swan"] != [3, 12]:
        raise AssertionError("p=5 Swan conductor changed")
    if p5["candidate"]["representation"]["artin"] != [7, 29]:
        raise AssertionError("p=5 Artin conductor changed")

    actions = action_arrays()
    report = {
        "action_sha256": {
            key: hashlib.sha256(canonical_leaf_bytes(value)).hexdigest()
            for key, value in actions.items()
        },
        "complex_conjugation": {
            "character_table_match": tom_exhaustion[
                "complex_conjugation_character_match"
            ],
            "class_record": infinity[0],
            "element_class_index": 17,
            "subgroup_tom_index": 5,
            "V6_signature": [3, 3],
            "V20_signature": [11, 9],
        },
        "counts": {
            "double_sixes": len(DOUBLE_SIXES),
            "line_action_faithful": len(WEYL) == 51840,
            "line_action_kernel_order": 1,
            "lines": len(LINES),
            "sixers": len(SIXERS),
            "weyl_order": len(WEYL),
        },
        "p3": {
            **p3,
            "all_tom_decomposition_pattern_hits": tom_exhaustion[
                "p3_all_tom_decomposition_pattern_hits"
            ],
            "accepted_inertia_tom_index": 140,
            "central_competitor_tom_index": 142,
            "order_36_decomposition_tom_index": 206,
            "decomposition_orders_not_resolved": [18, 36],
            "p3_tame_quotient_filter_excludes_206_as_inertia": (
                next(
                    row
                    for row in tom_exhaustion[
                        "p3_all_tom_decomposition_pattern_hits"
                    ]
                    if row["tom_index"] == 206
                )["tame_quotient_cyclic"]
                is False
            ),
            "valid_decomposition_inertia_pairs": tom_exhaustion[
                "p3_valid_decomposition_inertia_pairs"
            ],
        },
        "p5": {
            **p5,
            "all_tom_decomposition_pattern_hits": tom_exhaustion[
                "p5_all_tom_decomposition_pattern_hits"
            ],
            "inertia_and_decomposition_tom_index": 147,
            "valid_decomposition_inertia_pairs": tom_exhaustion[
                "p5_valid_decomposition_inertia_pairs"
            ],
            "wild_normalizer_filter_unique": (
                tom_exhaustion["p5_valid_decomposition_inertia_pairs"]
                == [[147, 147, 1]]
                and [
                    row["sylow_5_normal"]
                    for row in tom_exhaustion[
                        "p5_all_tom_decomposition_pattern_hits"
                    ]
                ]
                == [True, False, False]
            ),
        },
        "reflection": reflection[0],
        "order_two_tom_profiles": order_two_profiles,
        "status": "PASS",
        "tame_C3": {
            "all_order_three_classes": order_three,
            "decomposition_filter": tame_decomposition,
            "degree_only_competitor": tame_competitor[0],
            "degree_only_competitor_artin_V6_V20": [4, 14],
            "local_degree_36_selected": tame_selected[0],
            "selected_artin_V6_V20": [6, 12],
        },
        "tom_dual_action_exhaustion": tom_exhaustion,
        "upstream_lock": upstream_lock,
    }
    if not deep_exact(verify_upstream_carriers(), upstream_lock):
        raise StrictDataError("upstream bindings changed during group replay")
    return report


def canonical_evidence_group_report(audit=None):
    """Build the compact ToM carrier consumed by the independent checker.

    The Python replay above supplies a second implementation of every
    mathematical discriminator.  This carrier uses the stable TomLib labels
    and record layout so the checker can compare all leaves with its own GAP
    reconstruction.
    """
    if audit is None:
        audit = build_group_report()
    if audit["counts"] != {
        "double_sixes": 36,
        "line_action_faithful": True,
        "line_action_kernel_order": 1,
        "lines": 27,
        "sixers": 72,
        "weyl_order": 51840,
    }:
        raise AssertionError("W(E6) audit counts changed")
    actions = action_arrays(one_based=True)

    order_three = []
    for row in cyclic_subgroup_classes(3):
        fixed = row["invariant_dimensions_V6_V20"]
        tom_index = {
            (0, 8): 6,
            (4, 10): 7,
            (2, 6): 8,
        }.get(tuple(fixed))
        if tom_index is None:
            raise AssertionError("unknown C3 table-of-marks class")
        order_three.append(
            {
                "fixed_dimensions": fixed,
                "normalizer_order": row["normalizer_order"],
                "orbits_27": row["line_orbits"],
                "orbits_36": row["double_six_orbits"],
                "tom_index": tom_index,
            }
        )
    order_three.sort(key=lambda row: row["tom_index"])

    order_two = []
    for row in cyclic_subgroup_classes(2):
        fixed = row["invariant_dimensions_V6_V20"]
        tom_index = {
            (5, 15): 2,
            (2, 12): 3,
            (4, 12): 4,
            (3, 11): 5,
        }.get(tuple(fixed))
        if tom_index is None:
            raise AssertionError("unknown C2 table-of-marks class")
        order_two.append(
            {
                "fixed_dimensions": fixed,
                "normalizer_order": row["normalizer_order"],
                "orbits_27": row["line_orbits"],
                "orbits_36": row["double_six_orbits"],
                "tom_index": tom_index,
            }
        )
    order_two.sort(key=lambda row: row["tom_index"])

    deep_exhaustion = audit["p3"]["deep_C3_exhaustion"]
    if set(deep_exhaustion) != {
        "base_different_vector_num_den",
        "profiles",
        "selected_profile_tame_action_by_inertia_tom_index",
        "selected_tom_index",
        "solution_variable_order",
        "target_different_vector_num_den",
        "wild_C3_squared_per_layer_contribution_num_den",
    }:
        raise AssertionError("deep C3 exhaustion carrier keys changed")
    selected_action_by_inertia = deep_exhaustion[
        "selected_profile_tame_action_by_inertia_tom_index"
    ]
    selected_action_rows = [
        {
            "inertia_tom_index": int(tom_index),
            "tame_action": tame_action,
        }
        for tom_index, tame_action in sorted(
            selected_action_by_inertia.items(), key=lambda item: int(item[0])
        )
    ]
    checker_deep_exhaustion = {
        key: value
        for key, value in deep_exhaustion.items()
        if key != "selected_profile_tame_action_by_inertia_tom_index"
    }

    deep_orbits_27 = [1] * 9 + [3] * 6
    deep_orbits_36 = [1] * 6 + [3] * 10
    p3_common = {
        "core_order": 1,
        "deep_C3_profiles": deep_exhaustion["profiles"],
        "deep_id_group": [3, 1],
        "deep_orbits_27": deep_orbits_27,
        "deep_orbits_36": deep_orbits_36,
        "fixed_dimensions_deep": [4, 10],
        "fixed_dimensions_inertia": [0, 3],
        "fixed_dimensions_wild": [0, 4],
        "inertia_orbits_27": [3, 6, 9, 9],
        "inertia_orbits_36": [3, 3, 3, 9, 18],
        "normalizer_order": 72,
        "refinement_codimensions_deep": [0, 0, 6, 6],
        "refinement_codimensions_wild": [2, 4, 8, 8],
        "selected_deep_tom_index": deep_exhaustion["selected_tom_index"],
        "wild_id_group": [9, 2],
        "wild_orbits_27": [3, 3, 3, 9, 9],
        "wild_orbits_36": [3, 3, 3, 9, 9, 9],
    }
    p3_records = [
        {
            **p3_common,
            "central_deep_c3": False,
            "inertia_id_group": [18, 4],
            "selected_deep_tame_action": selected_action_by_inertia["140"],
            "tom_index": 140,
        },
        {
            **p3_common,
            "central_deep_c3": True,
            "inertia_id_group": [18, 3],
            "selected_deep_tame_action": selected_action_by_inertia["142"],
            "tom_index": 142,
        },
    ]
    p5_record = {
        "fixed_dimensions_inertia": [2, 3],
        "fixed_dimensions_wild": [2, 4],
        "inertia_id_group": [20, 3],
        "inertia_orbits_27": [1, 1, 5, 5, 5, 10],
        "inertia_orbits_36": [1, 5, 10, 10, 10],
        "normalizer_order": 40,
        "refinement_codimensions_wild": [0, 0, 4, 4, 4, 8],
        "tom_index": 147,
        "wild_central": False,
        "wild_id_group": [5, 1],
        "wild_normal": True,
        "wild_normalizer_order": 40,
        "wild_orbits_27": [1, 1, 5, 5, 5, 5, 5],
        "wild_orbits_36": [1, 5, 5, 5, 5, 5, 5, 5],
    }
    tame_common = {
        "decomposition_id_group": [18, 5],
        "decomposition_orbits_27": [3, 6, 18],
        "decomposition_orbits_36": [3, 6, 9, 18],
        "decomposition_order": 18,
        "decomposition_tom_index": 141,
        "inertia_orbits_27": [3] * 9,
        "quotient_order": 6,
    }
    tame_tom6 = {
        **tame_common,
        "inertia_fixed_dimensions": [0, 8],
        "inertia_orbits_36": [3] * 12,
        "inertia_tom_index": 6,
    }
    tame_tom8 = {
        **tame_common,
        "inertia_fixed_dimensions": [2, 6],
        "inertia_orbits_36": [1] * 3 + [3] * 11,
        "inertia_tom_index": 8,
    }
    if audit["tame_C3"]["decomposition_filter"][
        "decomposition_degree_carriers_unique_inertia"
    ]:
        raise AssertionError("tame C3 degree-only ambiguity unexpectedly vanished")
    p3_all_hits = [
        {
            **row,
            "decomposition_orbits_27": [3, 6, 9, 9],
            "decomposition_orbits_36": [3, 3, 3, 9, 18],
        }
        for row in audit["p3"]["all_tom_decomposition_pattern_hits"]
    ]
    pair_profile_carriers = {
        (
            row["decomposition_tom_index"],
            row["inertia_tom_index"],
        ): row
        for row in audit["p3"]["deep_C3_pair_normal_multiplicities"]
    }
    p3_pair_records = []
    for decomposition_tom, inertia_tom, quotient_order in audit["p3"][
        "valid_decomposition_inertia_pairs"
    ]:
        carrier = pair_profile_carriers[(decomposition_tom, inertia_tom)]
        profile_summary = []
        for profile in carrier["profiles"]:
            tame_action_counts = dict(profile["tame_actions"])
            if sum(tame_action_counts.values()) != profile["multiplicity"]:
                raise AssertionError("deep C3 tame-action multiplicities changed")
            profile_summary.append(
                {
                    "central_action_multiplicity": tame_action_counts.get(
                        "central", 0
                    ),
                    "inversion_action_multiplicity": tame_action_counts.get(
                        "inversion", 0
                    ),
                    "multiplicity": profile["multiplicity"],
                    "normal_in_decomposition_multiplicity": profile[
                        "normal_in_decomposition_multiplicity"
                    ],
                    "normal_in_inertia_multiplicity": profile[
                        "normal_in_inertia_multiplicity"
                    ],
                    "not_inertia_normal_multiplicity": (
                        profile["multiplicity"]
                        - profile["normal_in_inertia_multiplicity"]
                    ),
                    "tom_index": profile["tom_index"],
                }
            )
        p3_pair_records.append(
            {
                "decomposition_tom_index": decomposition_tom,
                "deep_C3_profile_summary": profile_summary,
                "deep_C3_subgroup_count": sum(
                    row["multiplicity"] for row in profile_summary
                ),
                "inertia_tom_index": inertia_tom,
                "residue_quotient_order": quotient_order,
            }
        )
    p3_decomposition_records = []
    for hit in p3_all_hits:
        contained = [
            {
                "inertia_tom_index": row["inertia_tom_index"],
                "residue_quotient_order": row["residue_quotient_order"],
            }
            for row in p3_pair_records
            if row["decomposition_tom_index"] == hit["tom_index"]
        ]
        p3_decomposition_records.append(
            {
                "contained_inertia": contained,
                "id_group": hit["id_group"],
                "normalizer_order": 72,
                "tom_index": hit["tom_index"],
            }
        )
    p5_all_hits = [
        {
            **row,
            "decomposition_orbits_27": [1, 1, 5, 5, 5, 10],
            "decomposition_orbits_36": [1, 5, 10, 10, 10],
        }
        for row in audit["p5"]["all_tom_decomposition_pattern_hits"]
    ]
    p5_pair_records = [
        {
            "decomposition_tom_index": decomposition_tom,
            "inertia_tom_index": inertia_tom,
            "residue_quotient_order": quotient_order,
        }
        for decomposition_tom, inertia_tom, quotient_order in audit["p5"][
            "valid_decomposition_inertia_pairs"
        ]
    ]
    order_two_character_maps = [
        {
            "character_table_group_order": 51840,
            "character_table_name": "U4(2).2",
            "element_centralizer_order": profile["normalizer_order"],
            "element_class_index": profile[
                "character_table_element_class_index"
            ],
            "element_class_matching_indices": [
                profile["character_table_element_class_index"]
            ],
            "element_class_order": 2,
            "element_class_size": profile["element_class_size"],
            "subgroup_generator_centralizer_order": profile[
                "normalizer_order"
            ],
            "subgroup_normalizer_order": profile["normalizer_order"],
            "subgroup_order": 2,
            "subgroup_tom_index": profile["tom_index"],
            "unique_order_and_class_size_match": True,
        }
        for profile in audit["order_two_tom_profiles"]
    ]
    return {
        "action_generators": {
            "double_six_point_images": actions["double_six_generators"],
            "line_point_images": actions["line_generators"],
            "picard_matrices": actions["picard_generators"],
        },
        "actions": {
            "double_six_action_bijective": True,
            "double_six_degree": 36,
            "line_degree": 27,
            "picard_action_bijective": True,
            "picard_lattice_rank": 7,
            "weyl_group_order": 51840,
        },
        "order2_classes": order_two,
        "order2_character_table_map": order_two_character_maps,
        "order3_classes": order_three,
        "p3_filter": {
            "all_tom_decomposition_pattern_hits": p3_all_hits,
            "deep_C3_exhaustion": checker_deep_exhaustion,
            "deep_C3_selected_action_by_inertia": selected_action_rows,
            "decomposition_candidates": p3_decomposition_records,
            "inertia_candidates": p3_records,
            "valid_decomposition_inertia_pairs": p3_pair_records,
        },
        "p5_filter": {
            "all_tom_decomposition_pattern_hits": p5_all_hits,
            "inertia_candidates": [p5_record],
            "valid_decomposition_inertia_pairs": p5_pair_records,
        },
        "schema_id": "hcs-c58-checker-group-report-v1",
        "tame_c3_dual_filter": [tame_tom6, tame_tom8, tame_tom6],
    }


def payload_group_projection(audit):
    """Project the producer replay onto the certificate's stable group contract."""
    carrier = canonical_evidence_group_report(audit)
    p3_candidates = carrier["p3_filter"]["inertia_candidates"]
    order_three = carrier["order3_classes"]
    order_two = carrier["order2_classes"]
    selected_tame = next(row for row in order_three if row["tom_index"] == 6)
    competitor_tame = next(row for row in order_three if row["tom_index"] == 8)
    return {
        "complex_conjugation": next(
            row for row in order_two if row["tom_index"] == 5
        ),
        "decomposition_candidates_p3": carrier["p3_filter"][
            "decomposition_candidates"
        ],
        "gap_report_sha256": hashlib.sha256(
            canonical_leaf_bytes(carrier)
        ).hexdigest(),
        "labelled_carrier_sha256": audit["action_sha256"],
        "p3_rejected_central": p3_candidates[1],
        "p3_selected": p3_candidates[0],
        "p5_selected": carrier["p5_filter"]["inertia_candidates"][0],
        "reflection": next(row for row in order_two if row["tom_index"] == 2),
        "tame_C3_competitor": competitor_tame,
        "tame_C3_dual_pair_candidates": carrier["tame_c3_dual_filter"],
        "tame_C3_selection_authority": {
            "competitor_degree36_conductor": 36
            - len(competitor_tame["orbits_36"]),
            "selected_by_independent_local_exponent": 24,
            "selected_degree36_conductor": 36
            - len(selected_tame["orbits_36"]),
        },
        "tame_C3_selected": selected_tame,
    }


def build_evidence():
    actions = action_arrays(one_based=True)
    return {
        "double_six_generators": actions["double_six_generators"],
        "group_report": build_group_report(),
        "line_generators": actions["line_generators"],
        "picard_generators": actions["picard_generators"],
        "schema_id": "hcs-c58-group-evidence-v1",
    }


def compact_report(evidence_raw: bytes, evidence: dict[str, Any]):
    group = evidence["group_report"]
    return {
        "action_sha256": group["action_sha256"],
        "complex_conjugation_element_class_index": group["complex_conjugation"][
            "element_class_index"
        ],
        "complex_conjugation_subgroup_tom_index": group["complex_conjugation"][
            "subgroup_tom_index"
        ],
        "complex_conjugation_character_match": group["complex_conjugation"][
            "character_table_match"
        ],
        "evidence_sha256": hashlib.sha256(evidence_raw).hexdigest(),
        "group_report_sha256": hashlib.sha256(
            canonical_leaf_bytes(group)
        ).hexdigest(),
        "p3_accepted_decomposition_orders": [
            row["orders_P_I_D"][2]
            for row in group["p3"]["accepted_after_direct_and_serre_filters"]
        ],
        "p3_all_tom_decomposition_pattern_hits": [
            [row["tom_index"], row["order"], row["id_group"]]
            for row in group["p3"]["all_tom_decomposition_pattern_hits"]
        ],
        "p3_artin_V6_V20": [11, 35],
        "p3_deep_C3_normal_in_all_surviving_decomposition_groups": group["p3"][
            "deep_C3_normal_in_all_surviving_decomposition_groups"
        ],
        "p3_deep_C3_exhaustion": group["p3"]["deep_C3_exhaustion"],
        "p3_deep_C3_pair_normal_multiplicities": group["p3"][
            "deep_C3_pair_normal_multiplicities"
        ],
        "p3_filtration_multiplicity_equation": group["p3"][
            "filtration_multiplicity_equation"
        ],
        "p3_swan_V6_V20": [5, 18],
        "p3_valid_decomposition_inertia_pairs": group["p3"][
            "valid_decomposition_inertia_pairs"
        ],
        "p5_all_tom_decomposition_pattern_hits": [
            [row["tom_index"], row["order"], row["id_group"]]
            for row in group["p5"]["all_tom_decomposition_pattern_hits"]
        ],
        "p5_artin_V6_V20": group["p5"]["candidate"]["representation"]["artin"],
        "p5_filtration_multiplicity_equation": group["p5"]["candidate"][
            "filtration_multiplicity_equation"
        ],
        "p5_filtration_equation": group["p5"]["filtration_equation"],
        "p5_swan_V6_V20": group["p5"]["candidate"]["representation"]["swan"],
        "p5_valid_decomposition_inertia_pairs": group["p5"][
            "valid_decomposition_inertia_pairs"
        ],
        "p5_wild_normalizer_filter_unique": group["p5"][
            "wild_normalizer_filter_unique"
        ],
        "order_two_tom_profiles": group["order_two_tom_profiles"],
        "payload_group_projection": payload_group_projection(group),
        "reflection_artin_V6_V20": [1, 5],
        "status": "PASS",
        "tame_C3_artin_V6_V20": group["tame_C3"][
            "selected_artin_V6_V20"
        ],
        "tame_C3_decomposition_degrees_unique": group["tame_C3"][
            "decomposition_filter"
        ]["decomposition_degree_carriers_unique_inertia"],
        "tame_C3_degree_36_local_rows_unique": group["tame_C3"][
            "decomposition_filter"
        ]["degree_36_local_rows_unique_inertia"],
        "weyl_order": group["counts"]["weyl_order"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--build-evidence", type=Path)
    modes.add_argument("--evidence", type=Path)
    arguments = parser.parse_args()
    reject_optimized_python()

    rebuilt = build_evidence()
    if arguments.build_evidence is not None:
        evidence_raw = canonical_json_bytes(rebuilt, pretty=True)
        atomic_write(arguments.build_evidence, evidence_raw)
        evidence = rebuilt
    else:
        evidence_raw, _ = read_stable(arguments.evidence, max_bytes=1_000_000)
        evidence = strict_json_loads(evidence_raw, max_bytes=1_000_000)
        if evidence_raw != canonical_json_bytes(evidence, pretty=True):
            raise StrictDataError("C58 group evidence is not canonical pretty JSON")
        require_exact_keys(
            evidence,
            {
                "double_six_generators",
                "group_report",
                "line_generators",
                "picard_generators",
                "schema_id",
            },
            "C58 group evidence",
        )
        if evidence.get("schema_id") != "hcs-c58-group-evidence-v1":
            raise StrictDataError("C58 group evidence schema mismatch")
        if not deep_exact(evidence, rebuilt):
            raise StrictDataError("C58 group evidence differs from exact replay")

    report = compact_report(evidence_raw, evidence)
    report_raw = canonical_leaf_bytes(report)
    print(report_raw.decode("utf-8"))
    print("report_sha256", hashlib.sha256(report_raw).hexdigest())


if __name__ == "__main__":
    main()
