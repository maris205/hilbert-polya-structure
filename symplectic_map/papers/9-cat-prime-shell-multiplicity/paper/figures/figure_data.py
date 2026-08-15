"""Hash-locked, read-only data contract for Paper 9 publication figures."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


FIGURE_DIR = Path(__file__).resolve().parent
PAPER_ROOT = FIGURE_DIR.parent.parent

EXPECTED_HASHES = {
    "experiments/source_lock.json":
        "662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49",
    "notes/PROOF_PACKAGE.md":
        "47216ad4021d3476bfd0850ebec24c9ceafb5af8c0573214182fd2d0da7b2daa",
    "notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md":
        "9509278ce55d908dba7d7cb4a809a335cc51d9364e8bfdfd1dc66be594775b8f",
    "results/EXPERIMENT_RESULTS.json":
        "448de06e92bd7ab4e5374e5d1f57413df45859cd3476ff14b2691b63ac364fab",
    "results/INDEPENDENT_RESULT_INTEGRITY.md":
        "aa0c7db555f11920c7305be508f6cfff62375970e112e9f720111831da20b3bd",
    "results/result_manifest.json":
        "8ca12744638a47b6e4fa3239a60a19d79229d2b9596ae4fe4b2f66a399618f92",
    "experiments/OFFICIAL_EXPERIMENT_RESULTS.md":
        "66bfefe9dcf5731cb89a0597deed5df322f9bc24f9fc3a592d4790a46d2a4dc0",
    "experiments/OFFICIAL_VALIDATION_REPORT.md":
        "32a1758362f94372a83588de63e2b5df33a8f7e45e0646de53154a2ca1afaab4",
}

CLASSIFICATION = (
    "PRIME_SHELL_MULTIPLICITY_OBSTRUCTION_CERTIFIED / "
    "A0_FAIL_GLOBAL_NORMALIZATION_ONLY / ROUTE_B_NOT_OPENED"
)
LOCKED_PRIMES = (2, 3, 5, 7, 11)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def validate_source_hashes() -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, expected in EXPECTED_HASHES.items():
        path = PAPER_ROOT / relative
        if not path.is_file() or path.is_symlink():
            raise RuntimeError(f"frozen figure input is not a regular file: {relative}")
        actual = sha256_file(path)
        if actual != expected:
            raise RuntimeError(
                f"frozen figure input changed: {relative}: {actual} != {expected}"
            )
        observed[relative] = actual
    return observed


def _strict_json(path: Path) -> Any:
    def reject_duplicate(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise RuntimeError(f"duplicate JSON key in {path.name}: {key}")
            result[key] = value
        return result

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate)


def _require_exact_int(value: Any, expected: int, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value != expected:
        raise RuntimeError(f"unexpected exact integer for {label}: {value!r}")


def load_frozen_payload() -> dict[str, Any]:
    """Validate the closure and return normalized exact display records."""
    source_hashes = validate_source_hashes()
    raw = _strict_json(PAPER_ROOT / "results/EXPERIMENT_RESULTS.json")
    manifest = _strict_json(PAPER_ROOT / "results/result_manifest.json")

    if raw.get("pass") is not True or manifest.get("pass") is not True:
        raise RuntimeError("result or manifest is not passing")
    if raw.get("source_lock_sha256") != EXPECTED_HASHES["experiments/source_lock.json"]:
        raise RuntimeError("raw result source-lock binding mismatch")
    if manifest.get("source_lock_sha256") != EXPECTED_HASHES["experiments/source_lock.json"]:
        raise RuntimeError("manifest source-lock binding mismatch")
    _require_exact_int(raw.get("registered_exact_audits"), 1, "registered audits")
    _require_exact_int(raw.get("candidate_numerical_runs"), 0, "candidate numerical runs")

    audit = raw.get("audit")
    if not isinstance(audit, dict) or audit.get("pass") is not True:
        raise RuntimeError("registered audit is absent or not passing")
    if audit.get("classification") != CLASSIFICATION:
        raise RuntimeError("classification changed")
    if tuple(audit.get("locked_primes", ())) != LOCKED_PRIMES:
        raise RuntimeError("locked prime tuple changed")

    exact_zero_fields = (
        "candidate_numerical_runs",
        "centralizer_computations_run",
        "composite_shells_enumerated",
        "generated_prime_target_arrays",
        "normalization_or_selector_searches",
        "numeric_s_or_log_evaluations",
        "parameter_or_matrix_searches",
    )
    for field in exact_zero_fields:
        _require_exact_int(audit.get(field), 0, field)
    for field in (
        "external_prime_tables_accessed",
        "riemann_zero_data_accessed",
        "all_prime_inference_from_finite_audit",
        "global_convergence_inference_from_finite_audit",
    ):
        if audit.get(field) is not False:
            raise RuntimeError(f"forbidden or inference flag changed: {field}")

    controls = audit.get("controls")
    if not isinstance(controls, dict) or len(controls) != 12:
        raise RuntimeError("expected exactly twelve controls")
    if any(value is not True for value in controls.values()):
        raise RuntimeError("one or more controls failed")

    rows = audit.get("rows")
    if not isinstance(rows, list) or [row.get("prime") for row in rows] != list(LOCKED_PRIMES):
        raise RuntimeError("five-row prime ledger changed")

    normalized_rows: list[dict[str, Any]] = []
    for row in rows:
        if row.get("pass") is not True or row.get("dual_engine_match") is not True:
            raise RuntimeError(f"row failed at p={row.get('prime')}")
        if row.get("evidence_role") != "FINITE_FALSIFICATION_CONTROL":
            raise RuntimeError("finite evidence role changed")
        mechanism = row.get("mechanism_audit")
        product = row.get("product_audit")
        if not isinstance(mechanism, dict) or not isinstance(product, dict):
            raise RuntimeError("mechanism or product record missing")
        repeats = product.get("formal_repeats")
        if [item.get("repeat") for item in repeats] != [1, 2, 3]:
            raise RuntimeError("formal repeat ledger changed")

        point_profile = {
            int(period): int(count)
            for period, count in row["point_period_profile"].items()
        }
        cycle_profile = {
            int(period): int(count)
            for period, count in row["cycle_profile"].items()
        }
        if sum(point_profile.values()) != row["shell_cardinality"]:
            raise RuntimeError("point profile no longer partitions shell")
        if sum(cycle_profile.values()) != row["m_p"]:
            raise RuntimeError("cycle profile no longer sums to m_p")
        if sum(period * count for period, count in cycle_profile.items()) != row["shell_cardinality"]:
            raise RuntimeError("cycle lengths no longer partition shell")

        equal = mechanism["equal_weight_control"]
        fractional = mechanism["fractional_shell_normalization"]
        selector = mechanism["one_orbit_selector"]
        scalar = mechanism["pure_scalar_denominator"]
        equal_sums = [Fraction(item["power_sum"]) for item in equal["power_sums"]]
        fractional_weights = [Fraction(value) for value in fractional["outer_exponents"]]
        label_coefficients = [Fraction(item["orbit_label_coefficient"]) for item in repeats]
        if sum(fractional_weights, Fraction(0)) != 1 or fractional.get("equals_one") is not True:
            raise RuntimeError("fractional shell identity changed")
        if selector["discarded_cycle_count"] != row["m_p"] - 1:
            raise RuntimeError("selector cost changed")
        if scalar["unweighted_degree"] != row["m_p"] or scalar["target_degree"] != 1:
            raise RuntimeError("scalar degree record changed")

        normalized_rows.append(
            {
                "prime": int(row["prime"]),
                "case": str(row["case"]),
                "shell_cardinality": int(row["shell_cardinality"]),
                "point_profile": point_profile,
                "cycle_profile": cycle_profile,
                "m_p": int(row["m_p"]),
                "eigenline_cycles": row["eigenline_cycles"],
                "off_eigenline_cycles": row["off_eigenline_cycles"],
                "raw_factor": str(row["raw_factor"]),
                "raw_factors": product["raw_return"]["factors"],
                "label_coefficients": label_coefficients,
                "equal_weight": Fraction(equal["weight"]),
                "equal_power_sums": equal_sums,
                "fractional_weights": fractional_weights,
                "selector_discards": int(selector["discarded_cycle_count"]),
                "scalar_degree": int(scalar["unweighted_degree"]),
                "scalar_can_equal": bool(scalar["can_equal_single_factor_by_degree"]),
            }
        )

    proof = (PAPER_ROOT / "notes/PROOF_PACKAGE.md").read_text(encoding="utf-8")
    for marker in (
        "$p=2$ is the unique prime with $m_p=1$",
        "A0_FAIL_GLOBAL_NORMALIZATION_ONLY",
        "2<\\operatorname{Re}s\\le3",
        "centralizer",
    ):
        if marker not in proof:
            raise RuntimeError(f"proof marker missing: {marker}")

    result_review = (
        PAPER_ROOT / "results/INDEPENDENT_RESULT_INTEGRITY.md"
    ).read_text(encoding="utf-8")
    if result_review.count("PRIME_SHELL_RESULT_REVIEW_V1 ") != 1:
        raise RuntimeError("independent result authority is not unique")

    return {
        "source_hashes": source_hashes,
        "raw": raw,
        "manifest": manifest,
        "audit": audit,
        "rows": normalized_rows,
        "classification": CLASSIFICATION,
        "proof_only_contract": audit["proof_only_contract"],
        "symbolic_composite_control": audit["symbolic_composite_control"],
    }


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"
