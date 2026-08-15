"""Hash-locked, read-only data contract for Paper 10 publication figures."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


FIGURE_DIR = Path(__file__).resolve().parent
PAPER_ROOT = FIGURE_DIR.parent.parent

EXPECTED_HASHES = {
    "experiments/source_lock.json":
        "aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2",
    "notes/PROOF_PACKAGE.md":
        "2eafe71f32c452ff8a20a6818ccb43082e02b866db7353e26c36ff432f1b2a4c",
    "notes/NOVELTY_ASSESSMENT.md":
        "6ee0fe2aff13c2d4329496e32f2d6aa190a92a3c3b4904168a21828b646de0a5",
    "notes/CLAIMS_EVIDENCE_MATRIX.md":
        "03424a71fc8716618545a6c7c8b0fd05f5ad744cff034255ab0337012da0303d",
    "notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md":
        "a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5",
    "results/CODE_REVIEW.md":
        "990b1762e2aea6c379288854cca918cc4bbe87b7ea7ccadef7458ecfcf6988f0",
    "results/EXPERIMENT_RESULTS.json":
        "8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff",
    "results/INDEPENDENT_RESULT_INTEGRITY.md":
        "29264a8fd97d3acf4435ed807294bffcda0844a48728d8572083d92a3bcf5b58",
    "results/result_manifest.json":
        "db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658",
    "experiments/OFFICIAL_EXPERIMENT_RESULTS.md":
        "1ece7db3fbee75bcecaecb0ad05f89fe88699c4231bea80581f382f33ed3aa6e",
    "experiments/OFFICIAL_VALIDATION_REPORT.md":
        "f94dbfb28a71aea4dac5e89a8bc2a622bba092b66098c2fc2217ceba19a8ad5a",
}

CLASSIFICATION = (
    "CENTRALIZER_CYCLIC_TORSOR_CERTIFIED / "
    "A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED"
)
LOCKED_MODULI = (2, 3, 5, 7, 11, 4, 6, 9, 10)
PRIME_CONTROLS = (2, 3, 5, 7, 11)
COMPOSITE_CONTROLS = (4, 6, 9, 10)


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


def _exact_int(value: Any, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise RuntimeError(f"{label} is not an exact integer: {value!r}")
    return value


def load_frozen_payload() -> dict[str, Any]:
    """Validate the closed evidence package and return exact display records."""
    source_hashes = validate_source_hashes()
    source = _strict_json(PAPER_ROOT / "experiments/source_lock.json")
    raw = _strict_json(PAPER_ROOT / "results/EXPERIMENT_RESULTS.json")
    manifest = _strict_json(PAPER_ROOT / "results/result_manifest.json")

    if source.get("candidate_id") != "cat_centralizer_cyclic_torsor_v1":
        raise RuntimeError("candidate identity changed")
    if source.get("terminal_certificate") != CLASSIFICATION:
        raise RuntimeError("source classification changed")
    if source.get("route_b_status") != "ROUTE_B_NOT_OPENED":
        raise RuntimeError("source Route-B boundary changed")
    if tuple(source["frozen_audit"]["ordered_moduli"]) != LOCKED_MODULI:
        raise RuntimeError("source-locked modulus order changed")

    if raw.get("pass") is not True or manifest.get("pass") is not True:
        raise RuntimeError("result or manifest is not passing")
    if raw.get("source_lock_sha256") != EXPECTED_HASHES["experiments/source_lock.json"]:
        raise RuntimeError("raw result source-lock binding mismatch")
    if manifest.get("source_lock_sha256") != EXPECTED_HASHES["experiments/source_lock.json"]:
        raise RuntimeError("manifest source-lock binding mismatch")
    if _exact_int(raw.get("registered_exact_audits"), "registered audits") != 1:
        raise RuntimeError("registered audit count changed")
    if _exact_int(raw.get("candidate_numerical_runs"), "candidate numerical runs") != 0:
        raise RuntimeError("candidate numerical run count changed")
    if _exact_int(manifest.get("registered_exact_audits"), "manifest audits") != 1:
        raise RuntimeError("manifest audit count changed")
    if manifest.get("candidate_rerun_performed") is not False:
        raise RuntimeError("manifest reports an unauthorized rerun")

    audit = raw.get("audit")
    if not isinstance(audit, dict) or audit.get("pass") is not True:
        raise RuntimeError("registered audit is absent or not passing")
    if audit.get("classification") != CLASSIFICATION:
        raise RuntimeError("audit classification changed")
    if tuple(audit.get("locked_moduli", ())) != LOCKED_MODULI:
        raise RuntimeError("audit modulus order changed")
    if audit.get("external_modulus_label_required") is not True:
        raise RuntimeError("external-label conclusion changed")
    if audit.get("intrinsic_prime_selector") is not False:
        raise RuntimeError("intrinsic-prime-selector boundary changed")
    if audit.get("route_b_opened") is not False:
        raise RuntimeError("Route B was unexpectedly opened")

    for field in (
        "candidate_numerical_runs",
        "candidate_reruns",
        "equivariant_stacky_or_twisted_constructions",
        "external_data_loads",
        "generated_prime_or_modulus_targets",
        "hecke_transfer_fredholm_or_quantum_constructions",
        "matrix_or_parameter_searches",
        "network_accesses",
        "numeric_log_evaluations",
        "numeric_q_to_minus_s_evaluations",
        "numeric_s_evaluations",
        "random_draws",
    ):
        if _exact_int(audit.get(field), field) != 0:
            raise RuntimeError(f"forbidden counter changed: {field}")
    for field in (
        "all_q_inference_from_finite_audit",
        "external_prime_tables_accessed",
        "novelty_inference_from_finite_audit",
        "riemann_zero_data_accessed",
    ):
        if audit.get(field) is not False:
            raise RuntimeError(f"forbidden flag changed: {field}")

    controls = audit.get("controls")
    if not isinstance(controls, dict) or len(controls) != 10:
        raise RuntimeError("expected exactly ten registered controls")
    if any(value is not True for value in controls.values()):
        raise RuntimeError("one or more registered controls failed")

    rows = audit.get("rows")
    if not isinstance(rows, list) or [row.get("q") for row in rows] != list(LOCKED_MODULI):
        raise RuntimeError("nine-row modulus ledger changed")

    normalized_rows: list[dict[str, Any]] = []
    for row in rows:
        q = _exact_int(row.get("q"), "row q")
        if row.get("pass") is not True or row.get("frozen_expected_match") is not True:
            raise RuntimeError(f"row failed at q={q}")
        ledger = row.get("ledger")
        direct = row.get("direct_engine")
        algebra = row.get("algebra_engine")
        if not all(isinstance(item, dict) for item in (ledger, direct, algebra)):
            raise RuntimeError(f"row components missing at q={q}")

        exact_shell = _exact_int(ledger["exact_shell_size"], f"E size q={q}")
        cyclic = _exact_int(ledger["cyclic_locus_size"], f"CV size q={q}")
        full_c = _exact_int(ledger["full_centralizer_size"], f"C size q={q}")
        symp_c = _exact_int(ledger["symplectic_centralizer_size"], f"C1 size q={q}")
        a_order = _exact_int(ledger["A_order"], f"A order q={q}")
        a_orbits = _exact_int(ledger["cyclic_A_orbit_count"], f"A orbits q={q}")
        full_cv_q = _exact_int(ledger["full_CV_quotient_count"], f"CV/C q={q}")
        symp_cv_q = _exact_int(ledger["symplectic_CV_quotient_count"], f"CV/C1 q={q}")
        full_shell_q = _exact_int(ledger["full_centralizer_shell_orbits"], f"E/C q={q}")
        symp_shell_q = _exact_int(ledger["symplectic_centralizer_shell_orbits"], f"E/C1 q={q}")
        norm_image = _exact_int(ledger["norm_image_size"], f"norm image q={q}")
        discard = _exact_int(ledger["discard_size"], f"discard q={q}")
        reversing = ledger["prime_reversing_group_shell_orbits"]

        if cyclic != full_c or exact_shell != cyclic + discard:
            raise RuntimeError(f"torsor/shell cardinality relation failed at q={q}")
        if full_cv_q != 1 or symp_cv_q != norm_image:
            raise RuntimeError(f"quotient cardinality relation failed at q={q}")
        if a_orbits * a_order != cyclic:
            raise RuntimeError(f"cyclic A-orbit partition failed at q={q}")
        if direct["full_quotient_transition"].get("identity") is not True:
            raise RuntimeError(f"full quotient transition changed at q={q}")
        if direct["symplectic_quotient_transition"].get("identity") is not True:
            raise RuntimeError(f"symplectic quotient transition changed at q={q}")
        if len(algebra["norm_image"]) != norm_image:
            raise RuntimeError(f"norm-image inventory changed at q={q}")
        if q in PRIME_CONTROLS:
            if isinstance(reversing, bool) or not isinstance(reversing, int):
                raise RuntimeError(f"prime reversing record missing at q={q}")
        elif reversing is not None:
            raise RuntimeError(f"composite reversing record should be absent at q={q}")

        normalized_rows.append(
            {
                "q": q,
                "case": str(ledger["case"]),
                "exact_shell": exact_shell,
                "cyclic_locus": cyclic,
                "discard": discard,
                "full_centralizer": full_c,
                "symplectic_centralizer": symp_c,
                "A_order": a_order,
                "cyclic_A_orbits": a_orbits,
                "CV_over_C": full_cv_q,
                "CV_over_C1": symp_cv_q,
                "E_over_C": full_shell_q,
                "E_over_C1": symp_shell_q,
                "reversing_E": reversing,
                "norm_image": norm_image,
                "retained_fraction": str(ledger["retained_fraction"]["text"]),
            }
        )

    proof = (PAPER_ROOT / "notes/PROOF_PACKAGE.md").read_text(encoding="utf-8")
    for marker in (
        "The cyclic-vector locus is a torsor",
        "Its primitive period is $1$ for every $q$",
        "A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC",
        "Stacky/equivariant and Hecke mechanisms remain outside scope",
    ):
        if marker not in proof:
            raise RuntimeError(f"proof marker missing: {marker}")

    source_review = (
        PAPER_ROOT / "notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md"
    ).read_text(encoding="utf-8")
    if source_review.count("**Final source-lock verdict: PASS.**") != 1:
        raise RuntimeError("independent source PASS disposition is not unique")
    result_review = (
        PAPER_ROOT / "results/INDEPENDENT_RESULT_INTEGRITY.md"
    ).read_text(encoding="utf-8")
    if result_review.count("CENTRALIZER_RESULT_REVIEW_V1 ") != 1:
        raise RuntimeError("independent result authority is not unique")

    return {
        "source_hashes": source_hashes,
        "source": source,
        "raw": raw,
        "manifest": manifest,
        "audit": audit,
        "rows": normalized_rows,
        "prime_rows": [row for row in normalized_rows if row["q"] in PRIME_CONTROLS],
        "composite_rows": [row for row in normalized_rows if row["q"] in COMPOSITE_CONTROLS],
        "classification": CLASSIFICATION,
    }
