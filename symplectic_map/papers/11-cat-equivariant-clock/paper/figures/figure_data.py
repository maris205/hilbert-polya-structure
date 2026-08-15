"""Hash-locked, read-only data contract for Paper 11 publication figures."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


FIGURE_DIR = Path(__file__).resolve().parent
PAPER_ROOT = FIGURE_DIR.parent.parent

EXPECTED_HASHES = {
    "experiments/source_lock.json":
        "331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b",
    "notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md":
        "2f75d6934e3d61bdc941ee6689102a1cb08a959270a7cd87965579f1ec5cc622",
    "notes/PROOF_PACKAGE.md":
        "3d723fdb02c89f9b2f281da807bcd745c5991393d25e223f95d6673961c20948",
    "notes/NOVELTY_ASSESSMENT.md":
        "1dbd6e4dc07fbc1e126334f6484a71b77852f0583749ba64259bd0e603669c95",
    "notes/CLAIMS_EVIDENCE_MATRIX.md":
        "0ea191ebb1f6f0f915db096a68606099d4a315d80d333adadd3e396b11885490",
    "notes/CITATION_VERIFICATION.md":
        "1bfc33598d9ff5e5a8636a9ba5f8365ef9c3176614ba90a2b64ae1eb6dc4154b",
    "notes/INDEPENDENT_POSTRUN_SCOPE_AUDIT.md":
        "f7b365c9e6c8933cf3cbcaf3c96692cbacdaabcc84400bdc629f1d482cb243e4",
    "results/EXPERIMENT_RESULTS.json":
        "bef8aa5d632ed11b1ca58a123bbfe967a5426e2049d862118a373e4c1dc005fe",
    "results/result_manifest.json":
        "a0b409061c34eff0d68fdc326fe4ec6ff9295895444b857ee161fd77e417292c",
    "results/INDEPENDENT_RESULT_INTEGRITY.md":
        "c91737c8bf860bd559eebebe08420fc5d095800c47d132381f584e918e714a20",
    "results/POSTRUN_ANALYZER_REVIEW.md":
        "ba63afc8c88903f15ec6ac5d82f0cd65430710ca9c132b489a7cd4f70e7660a8",
    "experiments/OFFICIAL_EXPERIMENT_RESULTS.md":
        "06f547fdfbbfb3bd51a57041758a49f18acceca9dda8e19967c2364500d64918",
    "experiments/OFFICIAL_VALIDATION_REPORT.md":
        "754a36c0e2e6b5c5002ecb8b3473d0af0e077b4f5b88da2bc6851bdafad23221",
    "../10-cat-centralizer-quotient/paper/FINAL_INTEGRITY.md":
        "e0a4803ff8e2063ebf5766803212579b44cd80c15572b166c1389f0242f8e6ce",
    "../10-cat-centralizer-quotient/paper/PIPELINE_STATE.json":
        "dc7550b39e42cdeeeacd4ae64f9fb4142b0f2e2e4b315d0e73f1932077e0b09c",
    "../10-cat-centralizer-quotient/paper/paper_final.pdf":
        "f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378",
}

CANDIDATE_ID = "cat_equivariant_retention_tradeoff_v1"
CLASSIFICATION = (
    "EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED / "
    "A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED"
)
LOCKED_MODULI = (2, 3, 5, 7, 11, 4, 6, 9, 10)
PRIME_CONTROLS = (2, 3, 5, 7, 11)
COMPOSITE_CONTROLS = (4, 6, 9, 10)
EXPECTED_NRM = (
    (2, 3, 3, 1),
    (3, 8, 4, 2),
    (5, 20, 10, 2),
    (7, 48, 8, 6),
    (11, 100, 5, 20),
    (4, 12, 3, 4),
    (6, 24, 12, 2),
    (9, 72, 12, 6),
    (10, 60, 30, 2),
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def validate_source_hashes() -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, expected in EXPECTED_HASHES.items():
        path = (PAPER_ROOT / relative).resolve()
        if not path.is_file() or path.is_symlink():
            raise RuntimeError(f"frozen figure input is not a regular file: {relative}")
        actual = sha256_file(path)
        if actual != expected:
            raise RuntimeError(
                f"frozen figure input changed: {relative}: {actual} != {expected}"
            )
        observed[relative] = actual
    return observed


def strict_json(path: Path) -> Any:
    """Load integer-only strict JSON with duplicate and trailing-data checks."""

    def reject_duplicate(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise RuntimeError(f"duplicate JSON key in {path.name}: {key}")
            result[key] = value
        return result

    def reject_float(value: str) -> Any:
        raise RuntimeError(f"floating JSON value is forbidden in {path.name}: {value}")

    def reject_constant(value: str) -> Any:
        raise RuntimeError(f"nonfinite JSON constant in {path.name}: {value}")

    decoder = json.JSONDecoder(
        object_pairs_hook=reject_duplicate,
        parse_float=reject_float,
        parse_constant=reject_constant,
    )
    text = path.read_text(encoding="utf-8")
    value, end = decoder.raw_decode(text)
    if text[end:].strip():
        raise RuntimeError(f"trailing data in {path.name}")
    return value


def exact_int(value: Any, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise RuntimeError(f"{label} is not an exact integer: {value!r}")
    return value


def exact_fraction(record: Any, label: str) -> tuple[int, int]:
    if not isinstance(record, dict) or set(record) != {"denominator", "numerator"}:
        raise RuntimeError(f"{label} is not an exact rational record")
    numerator = exact_int(record["numerator"], f"{label} numerator")
    denominator = exact_int(record["denominator"], f"{label} denominator")
    if denominator <= 0 or numerator <= 0:
        raise RuntimeError(f"{label} is not positive")
    return numerator, denominator


def _single_factor(record: Any, label: str) -> tuple[int, tuple[int, int]]:
    if not isinstance(record, list) or len(record) != 1:
        raise RuntimeError(f"{label} must have exactly one factor")
    factor = record[0]
    if not isinstance(factor, dict) or factor.get("inverse_power_sign") != -1:
        raise RuntimeError(f"{label} inverse-sign record changed")
    support = exact_int(factor.get("support"), f"{label} support")
    exponent = factor.get("exponent")
    if isinstance(exponent, int) and not isinstance(exponent, bool):
        rational = (exponent, 1)
    else:
        rational = exact_fraction(exponent, f"{label} exponent")
    return support, rational


def _format_fraction(value: tuple[int, int]) -> str:
    numerator, denominator = value
    return str(numerator) if denominator == 1 else f"{numerator}/{denominator}"


def load_frozen_payload() -> dict[str, Any]:
    """Validate the closed evidence package and return exact display records."""

    source_hashes = validate_source_hashes()
    source = strict_json(PAPER_ROOT / "experiments/source_lock.json")
    raw = strict_json(PAPER_ROOT / "results/EXPERIMENT_RESULTS.json")
    manifest = strict_json(PAPER_ROOT / "results/result_manifest.json")
    paper10_pipeline = strict_json(
        (PAPER_ROOT / "../10-cat-centralizer-quotient/paper/PIPELINE_STATE.json").resolve()
    )

    if source.get("candidate_id") != CANDIDATE_ID or source.get("lock_version") != 2:
        raise RuntimeError("source candidate identity or lock version changed")
    if source.get("intended_terminal_certificate") != CLASSIFICATION:
        raise RuntimeError("source classification changed")
    if source.get("route_b_status") != "ROUTE_B_NOT_OPENED":
        raise RuntimeError("source Route-B boundary changed")
    if tuple(source["frozen_audit"]["ordered_moduli"]) != LOCKED_MODULI:
        raise RuntimeError("source-locked modulus order changed")

    if raw.get("candidate_id") != CANDIDATE_ID or raw.get("pass") is not True:
        raise RuntimeError("raw result identity or pass state changed")
    if raw.get("source_lock_sha256") != EXPECTED_HASHES["experiments/source_lock.json"]:
        raise RuntimeError("raw result source-lock binding changed")
    if exact_int(raw.get("registered_audit_count"), "registered audit count") != 1:
        raise RuntimeError("registered audit count changed")
    if exact_int(raw.get("candidate_numerical_run_count"), "numerical run count") != 0:
        raise RuntimeError("candidate numerical-run count changed")

    if manifest.get("pass") is not True or manifest.get("classification") != CLASSIFICATION:
        raise RuntimeError("strict result manifest state changed")
    if manifest.get("source_lock_sha256") != EXPECTED_HASHES["experiments/source_lock.json"]:
        raise RuntimeError("manifest source-lock binding changed")
    if manifest.get("candidate_rerun_performed") is not False:
        raise RuntimeError("manifest reports a candidate rerun")

    if paper10_pipeline.get("status") != "COMPLETE_LOCAL_FINAL_REVIEW_PASS":
        raise RuntimeError("Paper-10 terminal status changed")

    audit = raw.get("audit")
    if not isinstance(audit, dict) or audit.get("pass") is not True:
        raise RuntimeError("registered audit is absent or not passing")
    if audit.get("classification") != CLASSIFICATION:
        raise RuntimeError("raw classification changed")
    if tuple(audit.get("arithmetic_modulus_order", ())) != LOCKED_MODULI:
        raise RuntimeError("raw modulus order changed")
    if exact_int(audit.get("arithmetic_modulus_record_count"), "record count") != 9:
        raise RuntimeError("raw modulus-record count changed")

    for field in (
        "adaptive_matrix_or_group_candidate_search_count",
        "candidate_numerical_run_count",
        "candidate_rerun_count",
        "cross_q_coefficient_ring_identification_count",
        "external_data_load_count",
        "external_prime_data_access_count",
        "network_access_count",
        "new_zeta_definition_count",
        "numeric_log_q_evaluation_count",
        "numeric_q_power_minus_s_evaluation_count",
        "numeric_s_evaluation_count",
        "random_seed_count",
        "riemann_zero_data_access_count",
        "route_b_open_count",
        "stack_simulation_beyond_exact_finite_formulas_count",
    ):
        if exact_int(audit.get(field), field) != 0:
            raise RuntimeError(f"forbidden counter changed: {field}")
    if audit.get("ambient_ring_varies_with_q") is not True:
        raise RuntimeError("ambient-ring externality changed")
    if audit.get("external_modulus_specialization_required") is not True:
        raise RuntimeError("external-specialization boundary changed")
    if audit.get("intrinsic_prime_selector") is not False:
        raise RuntimeError("intrinsic-prime-selector boundary changed")
    if audit.get("common_modulus_clock_found") is not False:
        raise RuntimeError("common-clock boundary changed")

    controls = audit.get("controls")
    expected_controls = {f"K{index:03d}" for index in range(1, 13)}
    if not isinstance(controls, dict) or set(controls) != expected_controls:
        raise RuntimeError("registered K001--K012 inventory changed")
    if any(value is not True for value in controls.values()):
        raise RuntimeError("one or more registered controls failed")

    records = audit.get("arithmetic_modulus_records")
    if not isinstance(records, list) or [row.get("q") for row in records] != list(LOCKED_MODULI):
        raise RuntimeError("arithmetic record order changed")

    normalized: list[dict[str, Any]] = []
    for record, expected in zip(records, EXPECTED_NRM):
        q, n_expected, r_expected, m_expected = expected
        if record.get("q") != q or record.get("pass") is not True:
            raise RuntimeError(f"row identity/pass changed at q={q}")
        expected_record = record.get("expected")
        if expected_record != {"m": m_expected, "n": n_expected, "r": r_expected}:
            raise RuntimeError(f"expected n/r/m tuple changed at q={q}")
        torsor = record.get("torsor")
        engine = record.get("enumeration_engine")
        formula_engine = record.get("formula_engine")
        if not all(isinstance(item, dict) for item in (torsor, engine, formula_engine)):
            raise RuntimeError(f"row components missing at q={q}")
        if record.get("engine_pair_validation", {}).get("pass") is not True:
            raise RuntimeError(f"dual engines no longer agree at q={q}")

        n = exact_int(torsor.get("n"), f"n q={q}")
        r = exact_int(torsor.get("r"), f"r q={q}")
        m = exact_int(torsor.get("m"), f"m q={q}")
        if (n, r, m) != (n_expected, r_expected, m_expected) or n != r * m:
            raise RuntimeError(f"torsor n/r/m relation changed at q={q}")

        source_factor = _single_factor(
            engine["source_dynamics"]["ordinary_zeta_factors"],
            f"source factor q={q}",
        )
        point_cardinality = _single_factor(
            engine["orbifold"]["point_cardinality_factors"],
            f"point-cardinality q={q}",
        )
        point_orbifold = _single_factor(
            engine["orbifold"]["point_orbifold_factors"],
            f"point-orbifold q={q}",
        )
        orbit_cardinality = _single_factor(
            engine["orbifold"]["orbit_cardinality_factors"],
            f"orbit-cardinality q={q}",
        )
        orbit_orbifold = _single_factor(
            engine["orbifold"]["orbit_orbifold_factors"],
            f"orbit-orbifold q={q}",
        )
        expected_factors = {
            "source": (r, (m, 1)),
            "point_cardinality": (r, (m, 1)),
            "point_orbifold": (r, (1, r)),
            "orbit_cardinality": (1, (n, 1)),
            "orbit_orbifold": (1, (1, 1)),
        }
        observed_factors = {
            "source": source_factor,
            "point_cardinality": point_cardinality,
            "point_orbifold": point_orbifold,
            "orbit_cardinality": orbit_cardinality,
            "orbit_orbifold": orbit_orbifold,
        }
        if observed_factors != expected_factors:
            raise RuntimeError(f"support/exponent ledger changed at q={q}")
        if engine["action_groupoid"].get("induced_period") != 1:
            raise RuntimeError(f"stack period changed at q={q}")
        if engine["action_groupoid"].get("static_inertia_sector_count") != 1:
            raise RuntimeError(f"regular inertia sector count changed at q={q}")
        if engine["g_permutation"].get("exact_labelled_a_recovered") is not True:
            raise RuntimeError(f"labelled twist recovery changed at q={q}")

        normalized.append(
            {
                "q": q,
                "kind": "prime" if q in PRIME_CONTROLS else "composite",
                "n": n,
                "r": r,
                "m": m,
                "source": source_factor,
                "point_cardinality": point_cardinality,
                "point_orbifold": point_orbifold,
                "orbit_cardinality": orbit_cardinality,
                "orbit_orbifold": orbit_orbifold,
                "q2_exception": q == 2,
                "point_cardinality_label": (
                    f"({point_cardinality[0]},"
                    f"{_format_fraction(point_cardinality[1])})"
                ),
            }
        )

    reduction_names = (
        "point_cardinality",
        "point_orbifold",
        "orbit_cardinality",
        "orbit_orbifold",
    )
    positive_pairs = [
        (row["q"], name)
        for row in normalized
        for name in reduction_names
        if row[name][0] == row["r"] and row[name][1] == (1, 1)
    ]
    if positive_pairs != [(2, "point_cardinality")]:
        raise RuntimeError(f"locked q=2 scope exception changed: {positive_pairs}")
    for name in reduction_names:
        if all(row[name][0] == row["r"] and row[name][1] == (1, 1) for row in normalized):
            raise RuntimeError(f"a family-uniform scalar reduction appeared: {name}")
    r_by_q = {row["q"]: row["r"] for row in normalized}
    if r_by_q[2] != r_by_q[4] or r_by_q[2] != 3:
        raise RuntimeError("r2=r4=3 collision changed")
    if r_by_q[6] != r_by_q[9] or r_by_q[6] != 12:
        raise RuntimeError("r6=r9=12 collision changed")

    structural = audit.get("structural_unit_control")
    if not isinstance(structural, dict) or structural.get("pass") is not True:
        raise RuntimeError("structural C6 control changed")
    if structural.get("is_arithmetic_modulus_row") is not False:
        raise RuntimeError("structural control entered the modulus namespace")
    if structural.get("is_candidate") is not False:
        raise RuntimeError("structural control entered the candidate namespace")
    structural_engine = structural.get("enumeration_engine")
    structural_formula = structural.get("formula_engine")
    if not isinstance(structural_engine, dict) or not isinstance(structural_formula, dict):
        raise RuntimeError("structural engine records missing")
    structural_expected = {
        "action_kernel_order": 1,
        "action_effective": True,
        "g_permutation_exact_label_recovery": True,
        "source_factors": [{"exponent": 1, "support": 2}, {"exponent": 1, "support": 3}],
        "coarse_quotient_factors": [{"exponent": 2, "support": 1}],
        "stack_components": [
            {"multiplicity": 1, "subgroup_order": 2},
            {"multiplicity": 1, "subgroup_order": 3},
        ],
        "static_inertia_sector_count": 5,
        "stack_dynamics_static": True,
    }
    for key, expected_value in structural_expected.items():
        if structural_engine.get(key) != expected_value:
            raise RuntimeError(f"structural field changed: {key}")
        if structural_formula.get(key) != expected_value:
            raise RuntimeError(f"structural formula field changed: {key}")

    source_review = (
        PAPER_ROOT / "notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md"
    ).read_text(encoding="utf-8")
    if "**SOURCE_LOCK_PASS**" not in source_review or not source_review.rstrip().endswith("SOURCE_LOCK_PASS"):
        raise RuntimeError("source-lock PASS authority changed")
    result_review = (
        PAPER_ROOT / "results/INDEPENDENT_RESULT_INTEGRITY.md"
    ).read_text(encoding="utf-8")
    if result_review.count("EQUIVARIANT_CLOCK_RESULT_REVIEW_V1 ") != 1:
        raise RuntimeError("independent result authority is not unique")
    analyzer_review = (
        PAPER_ROOT / "results/POSTRUN_ANALYZER_REVIEW.md"
    ).read_text(encoding="utf-8")
    if analyzer_review.count("EQUIVARIANT_CLOCK_POSTRUN_ANALYZER_REVIEW_V1 ") != 1:
        raise RuntimeError("postrun analyzer authority is not unique")
    scope_review = (
        PAPER_ROOT / "notes/INDEPENDENT_POSTRUN_SCOPE_AUDIT.md"
    ).read_text(encoding="utf-8")
    required_scope_markers = (
        "PASS_WITH_SCOPE_CORRECTION",
        "unique locked exception",
        "no single scalar-reduction type has source support and unit",
        "r_2=r_4=3",
    )
    if any(marker not in scope_review for marker in required_scope_markers):
        raise RuntimeError("postrun scope-audit marker missing")
    paper10_integrity = (
        PAPER_ROOT / "../10-cat-centralizer-quotient/paper/FINAL_INTEGRITY.md"
    ).resolve().read_text(encoding="utf-8")
    if "COMPLETE_LOCAL_FINAL_REVIEW_PASS" not in paper10_integrity:
        raise RuntimeError("Paper-10 terminal-integrity marker changed")

    return {
        "source_hashes": source_hashes,
        "source": source,
        "raw": raw,
        "manifest": manifest,
        "audit": audit,
        "rows": normalized,
        "prime_rows": [row for row in normalized if row["kind"] == "prime"],
        "composite_rows": [row for row in normalized if row["kind"] == "composite"],
        "structural": structural_engine,
        "classification": CLASSIFICATION,
        "positive_pairs": positive_pairs,
        "scope_correction": {
            "verdict": "PASS_WITH_SCOPE_CORRECTION",
            "q2_exception": True,
            "q2_point_cardinality": (3, (1, 1)),
            "family_uniform_nonattainment": True,
            "modulus_collision": {"r": 3, "q_values": (2, 4)},
        },
    }
