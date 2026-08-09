#!/usr/bin/env python3
"""Build the A4.16a static phase-tube implementation-smoke proof objects.

This runner is intentionally non-licensing.  It uses Arb interval arithmetic
and exact rational subdivision geometry to cover the normalized energy-one
slow tube for three representative epsilon slabs.  The two static claims
tested by the smoke are:

* the fast polar angle has positive numerator and denominator and satisfies
  ``theta_dot < 18`` on every feasible tube box; and
* every feasible positive ``P_+ = 0`` point has ``0.12 < Q_+ < 0.17``.

No ODE enclosure, full-orbit tube-residence claim, all-slab claim, or
scientific release is made here.  The independent checker is a separate
implementation and does not import this module.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

from flint import arb, ctx, fmpq


ROOT = Path(__file__).resolve().parents[1]
RUNNER = Path(__file__).resolve()
CHECKER = ROOT / "scripts/check_r401_val_l3_phase_tube_independent.py"
PLAN = ROOT / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"
L1_RESULT = ROOT / "results/r401_val_l1_branch"
L1_SUMMARY = L1_RESULT / "summary.json"
L1_MANIFEST = L1_RESULT / "manifest.json"
L1_CHECKER = L1_RESULT / "independent_checker.json"
L1_POSTCHECK = L1_RESULT / "POSTCHECK_STATUS.json"
L1_RELEASE = L1_RESULT / "RELEASE_PROVENANCE.json"
L1_RELEASE_CHAIN = (
    L1_RELEASE,
    L1_SUMMARY,
    L1_MANIFEST,
    L1_CHECKER,
    L1_POSTCHECK,
)

SCHEMA_VERSION = 1
PROTOCOL_ID = "R401-VAL-L3-PHASE-TUBE-SMOKE-DRAFT"
ARTIFACT_STATUS = "DRAFT_NON_LICENSING"
PASS_STATUS = "PASS_STATIC_COMPONENT_SMOKE"
COMPONENT_SCOPE = "STATIC_ONLY"
REPRESENTATIVE_SLABS = ("S000", "S025", "S050")
PRECISIONS = (128, 256)

ANGLE_COORDINATES = ("qminus", "qplus", "pminus", "pplus")
SECTION_COORDINATES = ("qminus", "qplus", "pminus")
ANGLE_ROOT: dict[str, tuple[Fraction, Fraction]] = {
    "qminus": (Fraction(-15, 1000), Fraction(15, 1000)),
    "qplus": (Fraction(-18, 100), Fraction(18, 100)),
    "pminus": (Fraction(-6, 100), Fraction(6, 100)),
    "pplus": (Fraction(-1415, 1000), Fraction(1415, 1000)),
}
SECTION_ROOTS: dict[str, dict[str, tuple[Fraction, Fraction]]] = {
    "SECTION_LOW": {
        "qminus": (Fraction(-15, 1000), Fraction(15, 1000)),
        "qplus": (Fraction(0), Fraction(12, 100)),
        "pminus": (Fraction(-6, 100), Fraction(6, 100)),
    },
    "SECTION_WINDOW": {
        "qminus": (Fraction(-15, 1000), Fraction(15, 1000)),
        "qplus": (Fraction(12, 100), Fraction(17, 100)),
        "pminus": (Fraction(-6, 100), Fraction(6, 100)),
    },
    "SECTION_HIGH": {
        "qminus": (Fraction(-15, 1000), Fraction(15, 1000)),
        "qplus": (Fraction(17, 100), Fraction(18, 100)),
        "pminus": (Fraction(-6, 100), Fraction(6, 100)),
    },
}

ENERGY_LEVEL = Fraction(1)
TUBE_RADIUS_SQUARED = Fraction(36, 10_000)
ANGLE_CEILING = Fraction(18)
EPSILON_CAP = Fraction(101, 1000)
PERIOD_MAX = Fraction(69, 100)
MAX_DEPTH = 24
MAX_NODES = 250_000


def canonical_json_bytes(payload: Any) -> bytes:
    return (
        json.dumps(
            payload,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
        + b"\n"
    )


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def atomic_write(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    temporary.write_bytes(payload)
    os.replace(temporary, path)


def fraction_record(value: Fraction) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def interval_record_exact(
    interval: tuple[Fraction, Fraction],
) -> list[dict[str, str]]:
    return [fraction_record(interval[0]), fraction_record(interval[1])]


def box_record(
    box: dict[str, tuple[Fraction, Fraction]],
    coordinates: Iterable[str],
) -> dict[str, list[dict[str, str]]]:
    return {coordinate: interval_record_exact(box[coordinate]) for coordinate in coordinates}


def as_fmpq(value: Fraction) -> fmpq:
    return fmpq(value.numerator, value.denominator)


def point_ball(value: Fraction | int) -> arb:
    return arb(as_fmpq(Fraction(value)))


def interval_ball(interval: tuple[Fraction, Fraction]) -> arb:
    lower, upper = interval
    midpoint = (lower + upper) / 2
    radius = (upper - lower) / 2
    return arb(as_fmpq(midpoint), as_fmpq(radius))


def hull(left: arb, right: arb) -> arb:
    return arb.union(left, right)


def square_interval(value: arb) -> arb:
    """A dependency-aware square enclosure for a real Arb ball."""

    lower = value.lower()
    upper = value.upper()
    zero = arb(0)
    if lower >= zero:
        return hull(lower * lower, upper * upper).nonnegative_part()
    if upper <= zero:
        return hull(upper * upper, lower * lower).nonnegative_part()
    maximum = max(abs(lower).upper(), abs(upper).upper())
    return hull(zero, maximum * maximum).nonnegative_part()


def exprel_nonnegative(value: arb, *, order: int = 16) -> arb:
    """Enclose (exp(value)-1)/value on a nonnegative input interval."""

    if value.lower() < arb(0):
        raise ArithmeticError("exprel input is not certified nonnegative")
    total = arb(1)
    term = arb(1)
    for degree in range(1, order + 1):
        term = term * value / (degree + 1)
        total += term
    radius = abs(value).upper()
    factorial = 1
    for factor in range(2, order + 3):
        factorial *= factor
    remainder = radius ** (order + 1) * radius.exp() / factorial
    return total + arb(0, remainder.upper())


def printed_ball(value: arb, bits: int) -> str:
    digits = 52 if bits == 128 else 92
    return value.str(digits, radius=True, more=True)


@dataclass(frozen=True)
class Model:
    a: arb
    c: arb
    pi: arb
    lambda_slow: arb
    lambda_fast: arb
    omega_slow: arb
    omega_fast: arb
    e_slow: tuple[arb, arb]
    e_fast: tuple[arb, arb]


def build_model() -> Model:
    a = point_ball(Fraction(51, 50))
    pi_value = arb.pi()
    c = 2 * ((1 + a).sqrt() - 1)
    discriminant = c * (c * c + 4).sqrt()
    lambda_slow = (c * c + 2 - discriminant) / 2
    lambda_fast = (c * c + 2 + discriminant) / 2
    slow_raw = (1 - lambda_slow, -c)
    fast_raw = (lambda_fast - 1, c)
    slow_norm = square_interval(slow_raw[0]) + square_interval(slow_raw[1])
    fast_norm = square_interval(fast_raw[0]) + square_interval(fast_raw[1])
    slow_norm = slow_norm.sqrt()
    fast_norm = fast_norm.sqrt()
    return Model(
        a=a,
        c=c,
        pi=pi_value,
        lambda_slow=lambda_slow,
        lambda_fast=lambda_fast,
        omega_slow=2 * pi_value * lambda_slow.sqrt(),
        omega_fast=2 * pi_value * lambda_fast.sqrt(),
        e_slow=(slow_raw[0] / slow_norm, slow_raw[1] / slow_norm),
        e_fast=(fast_raw[0] / fast_norm, fast_raw[1] / fast_norm),
    )


@dataclass(frozen=True)
class Metrics:
    energy: arb
    tube_squared: arb
    angle_denominator: arb | None
    N_plus: arb | None
    angle_numerator: arb | None
    theta_dot: arb | None


def evaluate_metrics(
    model: Model,
    epsilon: arb,
    box: dict[str, tuple[Fraction, Fraction]],
    *,
    section: bool,
) -> Metrics:
    qm = interval_ball(box["qminus"])
    qp = interval_ball(box["qplus"])
    pm = interval_ball(box["pminus"])
    pp = arb(0) if section else interval_ball(box["pplus"])

    physical_q1 = model.e_slow[0] * qm + model.e_fast[0] * qp
    physical_q2 = model.e_slow[1] * qm + model.e_fast[1] * qp
    warped_1 = (
        -model.c * physical_q1
        - physical_q2
        - model.a * epsilon * square_interval(physical_q1)
    )
    warped_2 = physical_q1
    warped_squared = square_interval(warped_1) + square_interval(warped_2)
    # Every factor is mathematically nonnegative.  Arb's midpoint-radius
    # multiplication can display a tiny negative lower endpoint when one
    # factor contains zero, so intersect with the proved half-line.
    exponential_argument = (
        model.pi * square_interval(epsilon) * warped_squared
    ).nonnegative_part()
    potential = (
        2
        * model.pi
        * model.pi
        * warped_squared
        * exprel_nonnegative(exponential_argument)
    )
    energy = (
        square_interval(pm) + square_interval(pp)
    ) / 2 + potential
    tube_squared = (
        square_interval(model.omega_slow * qm) + square_interval(pm)
    )

    if section:
        return Metrics(energy, tube_squared, None, None, None, None)

    j11 = -model.c - 2 * model.a * epsilon * physical_q1
    exponential = exponential_argument.exp()
    factor = 4 * model.pi * model.pi * exponential
    gradient_physical_1 = factor * (j11 * warped_1 + warped_2)
    gradient_physical_2 = -factor * warped_1
    gradient_fast = (
        model.e_fast[0] * gradient_physical_1
        + model.e_fast[1] * gradient_physical_2
    )
    angle_denominator = (
        square_interval(model.omega_fast * qp) + square_interval(pp)
    )
    N_plus = square_interval(pp) + qp * gradient_fast
    # This is the numerator of theta_dot, namely omega_fast * N_plus.
    angle_numerator = model.omega_fast * N_plus
    theta_dot = angle_numerator / angle_denominator
    return Metrics(
        energy,
        tube_squared,
        angle_denominator,
        N_plus,
        angle_numerator,
        theta_dot,
    )


def terminal_classification(
    metrics: Metrics,
    box: dict[str, tuple[Fraction, Fraction]],
    *,
    goal: str,
) -> str | None:
    if metrics.tube_squared.lower() > point_ball(TUBE_RADIUS_SQUARED):
        return "TUBE_EXCLUDED"
    if (
        metrics.energy.upper() < point_ball(ENERGY_LEVEL)
        or metrics.energy.lower() > point_ball(ENERGY_LEVEL)
    ):
        return "ENERGY_EXCLUDED"
    if goal == "ANGLE_COVER":
        assert metrics.angle_denominator is not None
        assert metrics.N_plus is not None
        assert metrics.angle_numerator is not None
        assert metrics.theta_dot is not None
        if (
            metrics.angle_denominator.lower() > arb(0)
            and metrics.N_plus.lower() > arb(0)
            and metrics.angle_numerator.lower() > arb(0)
            and metrics.theta_dot.upper() < point_ball(ANGLE_CEILING)
        ):
            return "ANGLE_CERTIFIED"
        return None
    if goal == "SECTION_WINDOW_COVER":
        qlower, qupper = box["qplus"]
        if qlower >= Fraction(12, 100) and qupper <= Fraction(17, 100):
            return "LANDING_CLOSED_WINDOW"
    return None


def decisive_metrics_record(metrics: Metrics, classification: str, bits: int) -> dict[str, str]:
    if classification == "TUBE_EXCLUDED":
        return {"tube_squared": printed_ball(metrics.tube_squared, bits)}
    if classification == "ENERGY_EXCLUDED":
        return {"energy": printed_ball(metrics.energy, bits)}
    if classification == "ANGLE_CERTIFIED":
        assert metrics.angle_denominator is not None
        assert metrics.N_plus is not None
        assert metrics.angle_numerator is not None
        assert metrics.theta_dot is not None
        return {
            "D_plus": printed_ball(metrics.angle_denominator, bits),
            "N_plus": printed_ball(metrics.N_plus, bits),
            "theta_numerator": printed_ball(metrics.angle_numerator, bits),
            "theta_dot": printed_ball(metrics.theta_dot, bits),
        }
    if classification == "LANDING_CLOSED_WINDOW":
        return {}
    raise ValueError(f"unknown terminal classification {classification}")


def split_coordinate(
    box: dict[str, tuple[Fraction, Fraction]],
    root_box: dict[str, tuple[Fraction, Fraction]],
    coordinates: tuple[str, ...],
) -> str:
    def normalized_width(coordinate: str) -> Fraction:
        lower, upper = box[coordinate]
        root_lower, root_upper = root_box[coordinate]
        return (upper - lower) / (root_upper - root_lower)

    return max(coordinates, key=normalized_width)


def split_box(
    box: dict[str, tuple[Fraction, Fraction]],
    coordinate: str,
) -> tuple[Fraction, dict[str, tuple[Fraction, Fraction]], dict[str, tuple[Fraction, Fraction]]]:
    lower, upper = box[coordinate]
    midpoint = (lower + upper) / 2
    if not lower < midpoint < upper:
        raise ArithmeticError("non-strict exact midpoint")
    left = dict(box)
    right = dict(box)
    left[coordinate] = (lower, midpoint)
    right[coordinate] = (midpoint, upper)
    return midpoint, left, right


def build_tree(
    model: Model,
    epsilon: tuple[Fraction, Fraction],
    *,
    bits: int,
    tree_id: str,
    goal: str,
    root_box: dict[str, tuple[Fraction, Fraction]],
) -> dict[str, Any]:
    coordinates = ANGLE_COORDINATES if goal == "ANGLE_COVER" else SECTION_COORDINATES
    epsilon_ball = interval_ball(epsilon)
    stack: list[tuple[str, str | None, int, dict[str, tuple[Fraction, Fraction]]]] = [
        (tree_id, None, 0, root_box)
    ]
    nodes: list[dict[str, Any]] = []
    terminal_counts: dict[str, int] = {}
    internal_count = 0
    terminal_count = 0
    maximum_depth = 0
    minimum_D_lower: arb | None = None
    minimum_N_lower: arb | None = None
    minimum_theta_numerator_lower: arb | None = None
    maximum_theta_dot_upper: arb | None = None
    while stack:
        node_id, parent_id, depth, box = stack.pop()
        if len(nodes) >= MAX_NODES:
            raise RuntimeError(f"{tree_id}: node budget {MAX_NODES} exhausted")
        maximum_depth = max(maximum_depth, depth)
        metrics = evaluate_metrics(
            model,
            epsilon_ball,
            box,
            section=goal != "ANGLE_COVER",
        )
        classification = terminal_classification(metrics, box, goal=goal)
        node: dict[str, Any] = {
            "node_id": node_id,
            "parent_id": parent_id,
            "depth": depth,
        }
        if classification is not None:
            node["classification"] = classification
            node["decisive_intervals"] = decisive_metrics_record(
                metrics, classification, bits
            )
            terminal_counts[classification] = terminal_counts.get(classification, 0) + 1
            terminal_count += 1
            if classification == "ANGLE_CERTIFIED":
                assert metrics.angle_denominator is not None
                assert metrics.N_plus is not None
                assert metrics.angle_numerator is not None
                assert metrics.theta_dot is not None
                D_lower = metrics.angle_denominator.lower()
                N_lower = metrics.N_plus.lower()
                numerator_lower = metrics.angle_numerator.lower()
                theta_upper = metrics.theta_dot.upper()
                minimum_D_lower = (
                    D_lower if minimum_D_lower is None else min(minimum_D_lower, D_lower)
                )
                minimum_N_lower = (
                    N_lower if minimum_N_lower is None else min(minimum_N_lower, N_lower)
                )
                minimum_theta_numerator_lower = (
                    numerator_lower
                    if minimum_theta_numerator_lower is None
                    else min(minimum_theta_numerator_lower, numerator_lower)
                )
                maximum_theta_dot_upper = (
                    theta_upper
                    if maximum_theta_dot_upper is None
                    else max(maximum_theta_dot_upper, theta_upper)
                )
            nodes.append(node)
            continue
        if depth >= MAX_DEPTH:
            raise RuntimeError(f"{tree_id}: unresolved node at depth {depth}")
        coordinate = split_coordinate(box, root_box, coordinates)
        midpoint, left, right = split_box(box, coordinate)
        node.update(
            {
                "classification": "SPLIT",
                "split_coordinate": coordinate,
                "split_point": fraction_record(midpoint),
            }
        )
        internal_count += 1
        nodes.append(node)
        # Push right first so the serialized depth-first order is left first.
        stack.append((node_id + "1", node_id, depth + 1, right))
        stack.append((node_id + "0", node_id, depth + 1, left))

    if goal == "ANGLE_COVER":
        if any(
            value is None
            for value in (
                minimum_D_lower,
                minimum_N_lower,
                minimum_theta_numerator_lower,
                maximum_theta_dot_upper,
            )
        ):
            raise RuntimeError(f"{tree_id}: no certified angle leaf for extrema")
        angle_extrema: dict[str, str] | None = {
            "minimum_D_plus_lower": printed_ball(minimum_D_lower, bits),
            "minimum_N_plus_lower": printed_ball(minimum_N_lower, bits),
            "minimum_theta_numerator_lower": printed_ball(
                minimum_theta_numerator_lower, bits
            ),
            "maximum_theta_dot_upper": printed_ball(maximum_theta_dot_upper, bits),
            "theta_numerator_definition": "omega_fast_times_N_plus",
        }
    else:
        angle_extrema = None
    tree_payload: dict[str, Any] = {
        "tree_id": tree_id,
        "goal": goal,
        "coordinates": list(coordinates),
        "root_box": box_record(root_box, coordinates),
        "split_rule": "largest_normalized_width_then_coordinate_order_exact_midpoint",
        "node_count": len(nodes),
        "internal_count": internal_count,
        "terminal_count": terminal_count,
        "unresolved_count": 0,
        "maximum_depth": maximum_depth,
        "terminal_counts": dict(sorted(terminal_counts.items())),
        "angle_extrema": angle_extrema,
        "complete": True,
        "nodes": nodes,
        "content_hash_definition": (
            "sha256(canonical_json(tree_without_content_sha256))"
        ),
    }
    if len(nodes) != internal_count + terminal_count:
        raise RuntimeError(f"{tree_id}: inconsistent node accounting")
    tree_payload["content_sha256"] = sha256_bytes(
        canonical_json_bytes(tree_payload)
    )
    return tree_payload


def outer_containment_gates(model: Model, bits: int) -> dict[str, Any]:
    sqrt_two = point_ball(2).sqrt()
    warped_radius = 1 / (sqrt_two * model.pi)
    qplus_bound = (
        warped_radius
        + model.a * point_ball(EPSILON_CAP) * square_interval(warped_radius)
    ) / model.lambda_fast.sqrt()
    qminus_bound = point_ball(Fraction(6, 100)) / model.omega_slow
    angular_ceiling = 4 * model.pi / point_ball(PERIOD_MAX)
    values = {
        "qminus_bound": qminus_bound,
        "qplus_bound": qplus_bound,
        "pplus_bound": sqrt_two,
        "four_pi_over_period_max": angular_ceiling,
    }
    gates = {
        "qminus_bound_lt_0.015": qminus_bound.upper() < point_ball(Fraction(15, 1000)),
        "qplus_bound_lt_0.18": qplus_bound.upper() < point_ball(Fraction(18, 100)),
        "pplus_bound_lt_1.415": sqrt_two.upper() < point_ball(Fraction(1415, 1000)),
        "theta_ceiling_18_lt_four_pi_over_0.69": point_ball(18) < angular_ceiling.lower(),
    }
    return {
        "derivation": {
            "qminus": "r_minus<=0.06 implies |Q_minus|<=0.06/omega_minus",
            "qplus": "K=1 and exprel(s)>=1 imply |W|<=1/(sqrt(2)pi); triangle inequality for A Q=W+(a epsilon q1^2,0) and the fast singular direction gives the displayed bound",
            "pplus": "K=1 with nonnegative potential implies |P_plus|<=sqrt(2)",
            "winding": "theta_dot<18 and T<=0.69 imply Delta theta<4pi",
        },
        "values": {key: printed_ball(value, bits) for key, value in values.items()},
        "gates": gates,
        "all_pass": all(gates.values()),
    }


def project_relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def validate_l1_release_chain() -> dict[str, str]:
    required = L1_RELEASE_CHAIN
    if any(not path.is_file() or path.is_symlink() for path in required):
        raise FileNotFoundError("accepted A4.12 five-object release chain is incomplete")
    summary = json.loads(L1_SUMMARY.read_text(encoding="utf-8"))
    manifest = json.loads(L1_MANIFEST.read_text(encoding="utf-8"))
    checker = json.loads(L1_CHECKER.read_text(encoding="utf-8"))
    postcheck = json.loads(L1_POSTCHECK.read_text(encoding="utf-8"))
    release = json.loads(L1_RELEASE.read_text(encoding="utf-8"))
    gates = {
        "summary": summary.get("protocol_id") == "R401-VAL-L1-V2"
        and summary.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and summary.get("final_status") is None,
        "manifest": manifest.get("protocol_id") == "R401-VAL-L1-V2"
        and manifest.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and manifest.get("final_status") is None,
        "checker": checker.get("protocol_id") == "R401-VAL-L1-V2"
        and checker.get("checker_status") == "PASS"
        and checker.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and checker.get("final_status") is None,
        "postcheck": postcheck.get("protocol_id") == "R401-VAL-L1-V2"
        and postcheck.get("checker_status") == "PASS"
        and postcheck.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and postcheck.get("final_status") is None,
        "release": release.get("protocol_id") == "R401-VAL-L1-V2"
        and release.get("release_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and release.get("final_status") is None,
    }
    if not all(gates.values()):
        raise RuntimeError(f"accepted A4.12 status gate failed: {gates}")
    actual = {project_relative(path): sha256_file(path) for path in required}
    release_files = release.get("files")
    if not isinstance(release_files, dict):
        raise RuntimeError("A4.12 release provenance has no files map")
    for path in (L1_SUMMARY, L1_MANIFEST, L1_CHECKER, L1_POSTCHECK, PLAN):
        relative = project_relative(path)
        if release_files.get(relative) != sha256_file(path):
            raise RuntimeError(f"A4.12 release provenance mismatch: {relative}")
    return actual


def source_bindings() -> dict[str, Any]:
    return {
        "runner_sha256": sha256_file(RUNNER),
        "checker_sha256": sha256_file(CHECKER),
        "l1_final_plan_sha256": sha256_file(PLAN),
        "l1_release_chain_sha256": validate_l1_release_chain(),
    }


def load_plan() -> dict[str, dict[str, Any]]:
    validate_l1_release_chain()
    payload = json.loads(PLAN.read_text(encoding="utf-8"))
    records = {str(record["slab_id"]): record for record in payload["slabs"]}
    missing = [item for item in REPRESENTATIVE_SLABS if item not in records]
    if missing:
        raise ValueError(f"plan missing representative slabs: {missing}")
    return records


def slab_epsilon(record: dict[str, Any]) -> tuple[Fraction, Fraction]:
    lower = Fraction(str(record["epsilon_lower"]))
    upper = Fraction(str(record["epsilon_upper"]))
    if not Fraction(0) <= lower < upper <= EPSILON_CAP:
        raise ValueError("slab epsilon interval lies outside [0,0.101]")
    return lower, upper


def run_one(bits: int, slab_id: str, plan_record: dict[str, Any]) -> dict[str, Any]:
    previous_precision = ctx.prec
    ctx.prec = bits
    started = time.monotonic()
    try:
        model = build_model()
        epsilon = slab_epsilon(plan_record)
        containment = outer_containment_gates(model, bits)
        if not containment["all_pass"]:
            raise RuntimeError("analytic outer-containment gate failed")
        trees = [
            build_tree(
                model,
                epsilon,
                bits=bits,
                tree_id="ANGLE",
                goal="ANGLE_COVER",
                root_box=ANGLE_ROOT,
            )
        ]
        for tree_id, root_box in SECTION_ROOTS.items():
            trees.append(
                build_tree(
                    model,
                    epsilon,
                    bits=bits,
                    tree_id=tree_id,
                    goal="SECTION_WINDOW_COVER",
                    root_box=root_box,
                )
            )
        tree_by_id = {tree["tree_id"]: tree for tree in trees}
        low_ok = set(tree_by_id["SECTION_LOW"]["terminal_counts"]) <= {
            "ENERGY_EXCLUDED",
            "TUBE_EXCLUDED",
        }
        high_ok = set(tree_by_id["SECTION_HIGH"]["terminal_counts"]) <= {
            "ENERGY_EXCLUDED",
            "TUBE_EXCLUDED",
        }
        window_ok = tree_by_id["SECTION_WINDOW"]["terminal_counts"] == {
            "LANDING_CLOSED_WINDOW": 1
        }
        angle_ok = (
            tree_by_id["ANGLE"]["terminal_counts"].get("ANGLE_CERTIFIED", 0) > 0
            and set(tree_by_id["ANGLE"]["terminal_counts"])
            <= {"ANGLE_CERTIFIED", "ENERGY_EXCLUDED", "TUBE_EXCLUDED"}
        )
        implementation_pass = all(
            tree["complete"] for tree in trees
        ) and low_ok and high_ok and window_ok and angle_ok
        if not implementation_pass:
            raise RuntimeError("tree terminal contract failed")
        return {
            "schema_version": SCHEMA_VERSION,
            "protocol_id": PROTOCOL_ID,
            "artifact_status": ARTIFACT_STATUS,
            "implementation_status": PASS_STATUS,
            "component_scope": COMPONENT_SCOPE,
            "composite_s0_passed": False,
            "scientific_licensing_enabled": False,
            "final_status": None,
            "slab_id": slab_id,
            "precision_bits": bits,
            "epsilon": interval_record_exact(epsilon),
            "period_window": interval_record_exact((Fraction(64, 100), PERIOD_MAX)),
            "outer_containment": containment,
            "trees": trees,
            "counts": {
                "tree_count": len(trees),
                "node_count": sum(int(tree["node_count"]) for tree in trees),
                "internal_count": sum(int(tree["internal_count"]) for tree in trees),
                "terminal_count": sum(sum(tree["terminal_counts"].values()) for tree in trees),
                "unresolved_count": sum(int(tree["unresolved_count"]) for tree in trees),
            },
            "source_bindings": source_bindings(),
            "claim_boundary": (
                "static representative-slab Arb implementation smoke only; "
                "conditional on K=1 and whole-orbit residence in r_minus<=0.06; "
                "no ODE tube proof, all-slab proof, global orbit exclusion, "
                "trace formula, Hilbert-Polya, or RH claim"
            ),
            "wall_seconds": time.monotonic() - started,
        }
    finally:
        ctx.prec = previous_precision


def prepare_output_directory(path: Path) -> None:
    if path.exists() and any(path.iterdir()):
        raise FileExistsError(f"output directory is not empty: {path}")
    path.mkdir(parents=True, exist_ok=True)


def run_matrix(output_dir: Path) -> dict[str, Any]:
    prepare_output_directory(output_dir)
    plan = load_plan()
    proof_entries: list[dict[str, Any]] = []
    total_started = time.monotonic()
    for bits in PRECISIONS:
        for slab_id in REPRESENTATIVE_SLABS:
            proof = run_one(bits, slab_id, plan[slab_id])
            relative = f"proof_{bits}_{slab_id}.json"
            payload = canonical_json_bytes(proof)
            atomic_write(output_dir / relative, payload)
            proof_entries.append(
                {
                    "path": relative,
                    "sha256": sha256_bytes(payload),
                    "size_bytes": len(payload),
                    "precision_bits": bits,
                    "slab_id": slab_id,
                    "node_count": proof["counts"]["node_count"],
                    "internal_count": proof["counts"]["internal_count"],
                    "terminal_count": proof["counts"]["terminal_count"],
                    "unresolved_count": proof["counts"]["unresolved_count"],
                    "tree_content_sha256": {
                        tree["tree_id"]: tree["content_sha256"]
                        for tree in proof["trees"]
                    },
                }
            )
            print(
                f"{bits}:{slab_id} nodes={proof['counts']['node_count']} "
                f"status={PASS_STATUS}",
                flush=True,
            )
    summary = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_status": ARTIFACT_STATUS,
        "implementation_status": PASS_STATUS,
        "component_scope": COMPONENT_SCOPE,
        "composite_s0_passed": False,
        "scientific_licensing_enabled": False,
        "final_status": None,
        "matrix": {
            "precisions": list(PRECISIONS),
            "slabs": list(REPRESENTATIVE_SLABS),
            "proof_count": len(proof_entries),
        },
        "totals": {
            "node_count": sum(int(item["node_count"]) for item in proof_entries),
            "internal_count": sum(int(item["internal_count"]) for item in proof_entries),
            "terminal_count": sum(int(item["terminal_count"]) for item in proof_entries),
            "unresolved_count": sum(int(item["unresolved_count"]) for item in proof_entries),
            "wall_seconds": time.monotonic() - total_started,
        },
        "proofs": proof_entries,
        "source_bindings": source_bindings(),
        "claim_boundary": (
            "A4.16a static implementation smoke; it cannot license the local "
            "phase/flow-box theorem without the frozen protocol, independent "
            "postcheck, all-slab replay, and continuous branch-tube enclosure"
        ),
    }
    summary_payload = canonical_json_bytes(summary)
    atomic_write(output_dir / "summary.json", summary_payload)
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_status": ARTIFACT_STATUS,
        "implementation_status": PASS_STATUS,
        "component_scope": COMPONENT_SCOPE,
        "composite_s0_passed": False,
        "scientific_licensing_enabled": False,
        "final_status": None,
        "files": [
            *proof_entries,
            {
                "path": "summary.json",
                "sha256": sha256_bytes(summary_payload),
                "size_bytes": len(summary_payload),
            },
        ],
    }
    atomic_write(output_dir / "manifest.json", canonical_json_bytes(manifest))
    return summary


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="new or empty directory receiving strict JSON proof objects",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_args(argv)
    try:
        if arguments.output_dir.is_symlink():
            raise ValueError("output directory must not be a symlink")
        summary = run_matrix(arguments.output_dir.resolve())
    except Exception as error:  # preserve a concise CLI failure contract
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        f"artifact_status={summary['artifact_status']} "
        f"implementation_status={summary['implementation_status']} "
        f"proofs={summary['matrix']['proof_count']} "
        f"nodes={summary['totals']['node_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
