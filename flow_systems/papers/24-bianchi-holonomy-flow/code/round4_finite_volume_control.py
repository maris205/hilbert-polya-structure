#!/usr/bin/env python3
"""Build the P24 Round-4 finite-volume non-arithmetic control ledger.

The frozen control is the complement of the three-twist knot ``5_2``.  The
theorem-level geometry and arithmeticity claims are source-bound: HIKMOT's
verified census theorem covers ``m015``; SnapPy's rigorous positive isometry
check identifies ``5_2`` with ``m015``; and Reid's theorem says that the
figure-eight complement is the only arithmetic knot complement in S^3.

This program does *not* re-prove those papers.  It executes the invariant
contract and a high-precision complex-length ledger with SnapPy 3.3.2.  Since
the local environment does not contain SageMath's interval types, every
computed shape, volume, cusp parameter and geodesic length is explicitly
labelled non-interval numerical evidence.  No prime, zero or fitted arithmetic
data are read.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Any

import snappy


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SNAPPY_VERSION = "3.3.2"
CONTROL_NAME = "5_2"
CENSUS_NAME = "m015"
FIGURE_EIGHT_NAME = "4_1"
PRIMARY_LENGTH_CUTOFF = 3.05
CROSSCHECK_LENGTH_CUTOFF = 2.10
CROSSCHECK_BITS = 106
DATE = "2026-08-27"

HIKMOT_URL = "https://arxiv.org/abs/1310.3410"
HIKMOT_DOI = "https://doi.org/10.1080/10586458.2015.1029599"
REID_DOI = "https://doi.org/10.1112/jlms/s2-43.1.171"
SNAPPY_VERIFY_URL = "https://snappy.computop.org/verify.html"
SNAPPY_MANIFOLD_URL = "https://snappy.computop.org/manifold.html"
SNAPPY_PYPI_URL = "https://pypi.org/project/snappy/3.3.2/"

SOURCE_CHAIN = (
    {
        "claim": "m015 admits a complete finite-volume hyperbolic structure",
        "status": "PROVED_BY_PUBLISHED_VERIFIED_CENSUS_THEOREM",
        "source": HIKMOT_URL,
        "doi": HIKMOT_DOI,
        "locator": "Theorem 5.1",
    },
    {
        "claim": "5_2 and m015 are the same hyperbolic manifold",
        "status": "RIGOROUS_TRUE_RESULT_FROM_PINNED_SOFTWARE",
        "source": SNAPPY_MANIFOLD_URL,
        "locator": "Manifold.is_isometric_to; True answers are rigorous",
    },
    {
        "claim": "5_2 complement is non-arithmetic",
        "status": "PROVED_BY_REID_THEOREM_FOR_KNOT_COMPLEMENTS",
        "source": REID_DOI,
        "locator": "figure-eight is the only arithmetic knot complement",
    },
)

RESULT_PATHS = {
    "invariants": Path("results/five_two_control_invariants_round4.json"),
    "length_groups": Path("results/five_two_primitive_length_groups_round4.csv"),
    "alt_crosscheck": Path("results/five_two_alt_crosscheck_round4.csv"),
    "metrics": Path("results/round4_metrics.json"),
}
RECEIPT_PATH = Path("experiments/round4_receipt.json")


def json_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def csv_bytes(fieldnames: list[str], rows: list[dict[str, Any]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def real_text(value: Any) -> str:
    return str(value)


def complex_parts(value: Any) -> tuple[str, str]:
    return real_text(value.real()), real_text(value.imag())


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def combined_hash(outputs: dict[Path, bytes]) -> str:
    digest = hashlib.sha256()
    for path in sorted(outputs, key=lambda item: item.as_posix()):
        digest.update(path.as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(outputs[path])
        digest.update(b"\0")
    return digest.hexdigest()


def dependency_check() -> None:
    if snappy.__version__ != SNAPPY_VERSION:
        raise RuntimeError(
            f"P24 Round 4 requires snappy=={SNAPPY_VERSION}; found {snappy.__version__}"
        )


def topology_contract() -> tuple[dict[str, Any], Any, Any]:
    dependency_check()
    control = snappy.Manifold(CONTROL_NAME)
    census = snappy.Manifold(CENSUS_NAME)
    figure_eight = snappy.Manifold(FIGURE_EIGHT_NAME)

    if not control.is_isometric_to(census):
        raise AssertionError("rigorous positive isometry check 5_2 -> m015 failed")
    if control.num_cusps() != 1 or not control.is_orientable():
        raise AssertionError("frozen control must be orientable and one-cusped")

    cusp = control.cusp_info(0)
    link = control.link()
    control_two_bridge = tuple(int(x) for x in control.is_two_bridge())
    figure_eight_two_bridge = tuple(int(x) for x in figure_eight.is_two_bridge())
    if control_two_bridge == figure_eight_two_bridge:
        raise AssertionError("control and figure-eight two-bridge identifiers collided")

    group = control.fundamental_group(simplify_presentation=True)
    contract = {
        "schema": "p24-five-two-control-invariant-contract/1.0",
        "date": DATE,
        "control_id": "P24_R4_FIVE_TWO_COMPLEMENT",
        "link_table_name": CONTROL_NAME,
        "census_name": CENSUS_NAME,
        "isometric_to_census": True,
        "isometry_check_semantics": "RIGOROUS_WHEN_TRUE_PER_SNAPPY_DOCUMENTATION",
        "orientable": bool(control.is_orientable()),
        "cusps": int(control.num_cusps()),
        "cusp_topology": str(cusp["topology"]),
        "cusp_complete": bool(cusp["is_complete"]),
        "link_components": len(link.link_components),
        "diagram_crossings": len(link.crossings),
        "dt_code": [list(map(int, component)) for component in link.DT_code()],
        "two_bridge_identifier": list(control_two_bridge),
        "figure_eight_two_bridge_identifier": list(figure_eight_two_bridge),
        "named_knot_distinct_from_figure_eight": True,
        "homology": str(control.homology()),
        "num_ideal_tetrahedra": int(control.num_tetrahedra()),
        "has_finite_vertices": bool(control.has_finite_vertices()),
        "triangulation_isosig": control.triangulation_isosig(),
        "census_triangulation_isosig": census.triangulation_isosig(),
        "isometry_signature_unverified_numeric_path": control.isometry_signature(),
        "fundamental_group_generators": list(group.generators()),
        "fundamental_group_relators": list(group.relators()),
        "peripheral_curves": [list(pair) for pair in group.peripheral_curves()],
        "source_chain": list(SOURCE_CHAIN),
        "source_chain_verification": (
            "MANUAL_PRIMARY_SOURCE_AUDIT;THE_EXECUTABLE_CHECKS_BIND_THE_NAMED_OBJECT;"
            "THE_CODE_DOES_NOT_REPROVE_THE_PUBLISHED_THEOREMS"
        ),
        "finite_volume_hyperbolic_status": "PROVED_BY_SOURCE_CHAIN",
        "one_cusp_status": "EXACT_TOPOLOGICAL_CONTRACT_PLUS_SOURCE_CHAIN",
        "nonarithmetic_status": "PROVED_BY_SOURCE_CHAIN",
        "torsion_free_manifold_status": "PROVED_BY_MANIFOLD_HYPERBOLIC_STRUCTURE",
        "clock": "UNIT_SPEED_HYPERBOLIC_ARCLENGTH",
        "primitive_object": "PRIMITIVE_UNORIENTED_LOXODROMIC_CONJUGACY_CLASS",
        "repetition_rule": "POSITIVE_POWERS_OF_A_PRIMITIVE_CLASS",
        "arithmetic_owner": "NONE_CONTROL_IS_NONARITHMETIC",
        "forbidden_target_data_used": False,
        "local_interval_verification": "NOT_RUN_SAGEMATH_INTERVAL_BACKEND_UNAVAILABLE",
        "snappy_version": snappy.__version__,
        "snappy_release_source": SNAPPY_PYPI_URL,
        "snappy_verified_computation_boundary": SNAPPY_VERIFY_URL,
    }
    return contract, control, census


def numerical_invariants(control: Any) -> dict[str, Any]:
    high = control.high_precision()
    cusp = high.cusp_info(0)
    volume = high.volume()
    cusp_shape = cusp["shape"]
    shape_rows = []
    for index, shape in enumerate(high.tetrahedra_shapes("rect"), start=1):
        real, imag = complex_parts(shape)
        shape_rows.append({"tetrahedron": index, "shape_re": real, "shape_im": imag})
    volume_text = real_text(volume)
    cusp_re, cusp_im = complex_parts(cusp_shape)
    return {
        "status": "HIGH_PRECISION_NUMERICAL_OBSERVATION_NOT_INTERVAL_VERIFIED",
        "precision_family": "SNAPPY_MANIFOLD_HP_DEFAULT",
        "solution_type": str(high.solution_type()),
        "volume": volume_text,
        "cusp_shape_re": cusp_re,
        "cusp_shape_im": cusp_im,
        "tetrahedron_shapes": shape_rows,
        "claim_boundary": (
            "THE_PUBLISHED_SOURCE_CHAIN_PROVES_EXISTENCE_AND_FINITE_VOLUME;"
            "THE_DECIMAL_INVARIANTS_HERE_ARE_NOT_RIGOROUS_INTERVAL_ENCLOSURES"
        ),
    }


def primary_length_groups(control: Any) -> tuple[list[dict[str, Any]], list[Any]]:
    high = control.high_precision()
    spectrum = list(
        high.length_spectrum(
            PRIMARY_LENGTH_CUTOFF,
            full_rigor=True,
            grouped=True,
            include_words=True,
        )
    )
    rows: list[dict[str, Any]] = []
    for index, geodesic in enumerate(spectrum, start=1):
        length = geodesic.length
        trace_squared = 2 + 2 * length.cosh()
        length_re, length_im = complex_parts(length)
        trace_re, trace_im = complex_parts(trace_squared)
        rows.append(
            {
                "group_id": f"G{index:04d}",
                "representative_word": str(geodesic.word),
                "multiplicity": int(geodesic.multiplicity),
                "length_re": length_re,
                "holonomy_angle": length_im,
                "psl_trace_squared_re": trace_re,
                "psl_trace_squared_im": trace_im,
                "topology": str(geodesic.topology),
                "parity": str(geodesic.parity),
                "primitive_status": (
                    "PRIMITIVE_BY_PINNED_SNAPPY_LENGTH_SPECTRUM_DEDUPLICATION;"
                    "NOT_INTERVAL_VERIFIED"
                ),
                "orientation_status": "UNORIENTED_CLASS_WITH_COMPLEX_LENGTH_BRANCH",
                "completeness_boundary": (
                    "LENGTH_RE_LT_3.05_UNDER_SNAPPY_FULL_RIGOR_ENUMERATION;"
                    "FLOATING_HIGH_PRECISION_NOT_SAGE_INTERVAL_CERTIFIED"
                ),
                "arithmetic_owner": "NONE_CONTROL_IS_NONARITHMETIC",
                "target_data_used": "false",
            }
        )
    return rows, spectrum


def alternative_crosscheck(
    control: Any, primary_rows: list[dict[str, Any]], primary_spectrum: list[Any]
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    alternative = list(
        control.length_spectrum_alt(
            max_len=CROSSCHECK_LENGTH_CUTOFF,
            bits_prec=CROSSCHECK_BITS,
            verified=False,
        )
    )
    rows: list[dict[str, Any]] = []
    group_counts: Counter[str] = Counter()
    residuals: list[float] = []
    for index, geodesic in enumerate(alternative, start=1):
        distances = [float(abs(geodesic.length - item.length)) for item in primary_spectrum]
        group_index = min(range(len(distances)), key=distances.__getitem__)
        residual = distances[group_index]
        group_id = primary_rows[group_index]["group_id"]
        group_counts[group_id] += 1
        residuals.append(residual)
        length_re, length_im = complex_parts(geodesic.length)
        rows.append(
            {
                "alt_row_id": f"A{index:04d}",
                "group_id": group_id,
                "class_within_group": group_counts[group_id],
                "representative_word_alt": str(geodesic.word),
                "length_re_alt": length_re,
                "holonomy_angle_alt": length_im,
                "absolute_complex_length_residual": f"{residual:.17e}",
                "alternative_algorithm": "SNAPPY_LENGTH_SPECTRUM_ALT",
                "bits_precision": CROSSCHECK_BITS,
                "verified_interval_mode": "false",
                "target_data_used": "false",
            }
        )

    expected = {
        row["group_id"]: int(row["multiplicity"])
        for row in primary_rows
        if float(row["length_re"]) < CROSSCHECK_LENGTH_CUTOFF
    }
    observed = {key: group_counts[key] for key in expected}
    if observed != expected:
        raise AssertionError(
            f"alternative primitive multiplicities disagree: observed={observed}, expected={expected}"
        )
    maximum = max(residuals, default=0.0)
    if maximum >= 1e-25:
        raise AssertionError(f"cross-algorithm complex-length residual too large: {maximum}")
    return rows, {
        "crosscheck_groups": len(expected),
        "crosscheck_primitive_classes": len(alternative),
        "maximum_absolute_complex_length_residual": maximum,
        "multiplicity_vector_agrees": True,
    }


@lru_cache(maxsize=1)
def build_payload() -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    contract, control, _census = topology_contract()
    invariants = numerical_invariants(control)
    length_rows, primary_spectrum = primary_length_groups(control)
    cross_rows, cross_metrics = alternative_crosscheck(control, length_rows, primary_spectrum)
    primitive_classes = sum(int(row["multiplicity"]) for row in length_rows)
    if len(length_rows) != 18 or primitive_classes != 31:
        raise AssertionError(
            f"frozen primary ledger changed: groups={len(length_rows)}, classes={primitive_classes}"
        )
    if len(cross_rows) != 9:
        raise AssertionError(f"frozen crosscheck prefix changed: {len(cross_rows)}")

    invariant_payload = {
        "contract": contract,
        "numerical_invariants": invariants,
    }
    metrics = {
        "schema": "p24-round4-metrics/1.0",
        "date": DATE,
        "control_id": contract["control_id"],
        "finite_volume_hyperbolic_status": "PROVED_BY_SOURCE_CHAIN",
        "cusped_status": "PROVED_ONE_COMPLETE_TORUS_CUSP",
        "nonarithmetic_status": "PROVED_BY_SOURCE_CHAIN",
        "geometry_match_axes": [
            "ORIENTABLE_HYPERBOLIC_3_MANIFOLD",
            "FINITE_VOLUME",
            "NONCOMPACT_WITH_CUSP",
            "TORSION_FREE_MANIFOLD",
            "UNIT_SPEED_GEODESIC_FLOW",
            "ARCLENGTH_CLOCK",
            "PRIMITIVE_LOXODROMIC_CLASSES_WITH_COMPLEX_LENGTH",
        ],
        "unmatched_axes": [
            "ARITHMETIC_OWNER",
            "EXACT_CUSP_COUNT_OF_BIANCHI_LEVEL3_QUOTIENT",
            "COVOLUME",
            "LENGTH_DISTRIBUTION",
            "GENERATOR_MARKING",
            "FULL_PRIMITIVE_LEDGER",
        ],
        "primary_length_cutoff": PRIMARY_LENGTH_CUTOFF,
        "primary_length_groups": len(length_rows),
        "primary_primitive_classes_by_group_multiplicity": primitive_classes,
        "shortest_length": length_rows[0]["length_re"],
        "largest_emitted_length": length_rows[-1]["length_re"],
        "ledger_status": "HIGH_PRECISION_NUMERICAL_OBSERVATION_NOT_INTERVAL_VERIFIED",
        "primitive_semantics": (
            "PINNED_SNAPPY_3_3_2_DEDUPLICATES_GEODESICS_UP_TO_MULTIPLICITY;"
            "PUBLISHED_SOURCE_CHAIN_DOES_NOT_CERTIFY_THIS_FINITE_LEDGER"
        ),
        "crosscheck_length_cutoff": CROSSCHECK_LENGTH_CUTOFF,
        "crosscheck_bits": CROSSCHECK_BITS,
        **cross_metrics,
        "local_sage_interval_backend": "UNAVAILABLE",
        "source_chain_claim": (
            "THE_5_2_COMPLEMENT_IS_A_GENUINE_FINITE_VOLUME_ONE_CUSP_NONARITHMETIC_CONTROL"
        ),
        "cross_system_arithmetic_verdict": "OPEN",
        "formal_route_a_tuple": "UNASSIGNED",
        "route_a_scope": "A0-A1_ONLY",
        "a2_a4_evaluation": "NOT_EVALUATED",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "gates_a_e": "NOT_REACHED",
        "manuscript": "NOT_STARTED",
        "forbidden_target_data_used": False,
        "claim_boundary": (
            "SOURCE_PROVED_CONTROL_GEOMETRY_AND_NONARITHMETICITY;"
            "NUMERICAL_COMPLEX_LENGTH_PREFIX_ONLY;NO_BIANCHI_LENGTH_MATCH;"
            "NO_ORBIT_TO_PRIME_IDEAL_MAP;NO_FORMAL_ROUTE_ADVANCEMENT"
        ),
    }
    return invariant_payload, length_rows, cross_rows, metrics


def core_outputs() -> tuple[dict[Path, bytes], dict[str, Any]]:
    invariant_payload, length_rows, cross_rows, metrics = build_payload()
    length_fields = list(length_rows[0].keys())
    cross_fields = list(cross_rows[0].keys())
    outputs = {
        RESULT_PATHS["invariants"]: json_bytes(invariant_payload),
        RESULT_PATHS["length_groups"]: csv_bytes(length_fields, length_rows),
        RESULT_PATHS["alt_crosscheck"]: csv_bytes(cross_fields, cross_rows),
        RESULT_PATHS["metrics"]: json_bytes(metrics),
    }
    return outputs, metrics


def receipt_for(outputs: dict[Path, bytes], metrics: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "p24-round4-reproduction-receipt/1.0",
        "date": DATE,
        "status": "REPRODUCIBLE",
        "core_sha256": combined_hash(outputs),
        "files": {
            path.as_posix(): {"sha256": sha256(data), "bytes": len(data)}
            for path, data in sorted(outputs.items(), key=lambda item: item[0].as_posix())
        },
        "dependency": f"snappy=={SNAPPY_VERSION}",
        "reproduction_command": "bash experiments/reproduce_round4.sh",
        "tests_expected": 9,
        "primary_length_groups": metrics["primary_length_groups"],
        "primary_primitive_classes": metrics[
            "primary_primitive_classes_by_group_multiplicity"
        ],
        "crosscheck_primitive_classes": metrics["crosscheck_primitive_classes"],
        "source_theorem_replay_boundary": (
            "EXTERNAL_PUBLISHED_THEOREMS_ARE_CITED_AND_MANUALLY_AUDITED;"
            "THE_RECEIPT_REPLAYS_ONLY_LOCAL_EXECUTABLE_ARTIFACTS"
        ),
        "interval_verification": "NOT_RUN_SAGEMATH_UNAVAILABLE",
        "forbidden_target_data_used": False,
        "formal_route_a_tuple": "UNASSIGNED",
        "route_b_invocation_allowed": False,
    }


def rendered_outputs() -> dict[Path, bytes]:
    core, metrics = core_outputs()
    result = dict(core)
    result[RECEIPT_PATH] = json_bytes(receipt_for(core, metrics))
    return result


def write_outputs(output_root: Path) -> None:
    for relative, data in rendered_outputs().items():
        path = output_root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


def verify_existing(output_root: Path) -> None:
    mismatches: list[str] = []
    for relative, expected in rendered_outputs().items():
        path = output_root / relative
        if not path.exists():
            mismatches.append(f"missing:{relative}")
        elif path.read_bytes() != expected:
            mismatches.append(f"different:{relative}")
    if mismatches:
        raise SystemExit("verification failed: " + ", ".join(mismatches))
    print("P24 Round-4 existing artifacts VERIFIED")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, default=PROJECT_ROOT)
    parser.add_argument("--verify-existing", action="store_true")
    args = parser.parse_args()
    if args.verify_existing:
        verify_existing(args.output_root)
    else:
        write_outputs(args.output_root)
        core, metrics = core_outputs()
        print(
            "P24 Round 4 complete: "
            f"groups={metrics['primary_length_groups']} "
            f"primitive_classes={metrics['primary_primitive_classes_by_group_multiplicity']} "
            f"crosscheck_classes={metrics['crosscheck_primitive_classes']} "
            f"core_sha256={combined_hash(core)}"
        )


if __name__ == "__main__":
    main()
