"""Hash-locked source loader for all Paper 8 figures."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parents[1]

EXPECTED_HASHES = {
    "notes/PROOF_PACKAGE.md": "ee02fe72071c0bbea26f5f34c28130374fe1a919195cfbe154f6f5a39ab420af",
    "results/EXPERIMENT_RESULTS.json": "0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0",
    "results/result_manifest.json": "045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f",
    "experiments/OFFICIAL_EXPERIMENT_RESULTS.md": "4cf1645505a835a9d0aa62d84e7b6b47fc708b1347a954eeac26eb9710b9187d",
    "experiments/OFFICIAL_VALIDATION_REPORT.md": "ac9ac741cffd89dc8ab32db654ae59dc901b823a4b496be0607c7ce05fd403c3",
}

EXPECTED_CLASSIFICATION = (
    "INTRINSIC_TORSION_CAPACITY_CERTIFIED_A0_FAIL_PROVES_TOO_MUCH"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def source_path(relative_path: str) -> Path:
    return PROJECT_ROOT / relative_path


def validate_source_hashes() -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative_path, expected in EXPECTED_HASHES.items():
        path = source_path(relative_path)
        if not path.is_file() or path.is_symlink():
            raise RuntimeError(f"required regular source missing: {relative_path}")
        actual = sha256_file(path)
        if actual != expected:
            raise RuntimeError(
                f"source hash mismatch for {relative_path}: {actual} != {expected}"
            )
        observed[relative_path] = actual
    return observed


def load_sources() -> tuple[dict[str, Any], dict[str, Any], str]:
    validate_source_hashes()
    raw = json.loads(source_path("results/EXPERIMENT_RESULTS.json").read_text())
    manifest = json.loads(source_path("results/result_manifest.json").read_text())
    proof = source_path("notes/PROOF_PACKAGE.md").read_text()

    if raw.get("pass") is not True:
        raise RuntimeError("raw exact result is not passing")
    if raw.get("classification") != EXPECTED_CLASSIFICATION:
        raise RuntimeError("unexpected scientific classification")
    if raw.get("registered_periods") != list(range(1, 13)):
        raise RuntimeError("registered period range is not exactly 1..12")
    if raw.get("periods_above_twelve_computed") != []:
        raise RuntimeError("tail computation firewall violated")
    if raw["general_theorem_contract"].get("tail_periods_computed") != []:
        raise RuntimeError("theorem contract contains computed tail periods")
    if raw.get("candidate_numerical_runs") != 0:
        raise RuntimeError("unexpected candidate numerical run")
    if manifest.get("pass") is not True or manifest.get("errors") != []:
        raise RuntimeError("final result manifest is not closed and passing")
    manifest_result_hash = manifest["immutable_execution_hashes"][
        "experiment_results_sha256"
    ]
    if manifest_result_hash != EXPECTED_HASHES["results/EXPERIMENT_RESULTS.json"]:
        raise RuntimeError("manifest does not bind the expected raw result")
    required_proof_markers = (
        "There are three\ncases.",
        "The three cases exhaust all \\(n>12\\)",
        "This proves existence at \\(n=10\\)",
        "\\operatorname{Per}(T_A)=\\operatorname{Tor}(\\mathbb T^2)",
    )
    missing = [marker for marker in required_proof_markers if marker not in proof]
    if missing:
        raise RuntimeError(f"proof markers missing: {missing}")
    return raw, manifest, proof


def ledger_payload(raw: dict[str, Any]) -> list[dict[str, Any]]:
    exceptions = set(raw["boundary_summary"]["exception_set"])
    rows = sorted(raw["ledger_records"], key=lambda item: item["period"])
    payload: list[dict[str, Any]] = []
    for row in rows:
        n = row["period"]
        selected = row["selected_primitive_prime"]
        if n in exceptions:
            mechanism = "none"
            carrier_prime = None
        elif selected is not None:
            mechanism = "primitive"
            carrier_prime = selected
        elif n == 10:
            mechanism = "jordan"
            carrier_prime = 5
        else:
            raise RuntimeError(f"unclassified small period: {n}")
        payload.append(
            {
                "period": n,
                "delta": row["delta_direct"],
                "factorization_text": row["factorization_text"],
                "factorization": row["factorization"],
                "selected_primitive_prime": selected,
                "mechanism": mechanism,
                "carrier_prime": carrier_prime,
            }
        )
    if [row["period"] for row in payload] != list(range(1, 13)):
        raise RuntimeError("ledger is not exactly n=1..12")
    return payload


def boundary_payload(raw: dict[str, Any]) -> dict[str, Any]:
    boundary = raw["boundary_summary"]
    expected = {
        "exception_set": [1, 6, 12],
        "jordan_period_ten_points": 20,
        "jordan_period_ten_cycles": 2,
        "period_1_carriers": 0,
        "period_6_carriers": 0,
        "period_12_carriers": 0,
    }
    for key, value in expected.items():
        if boundary.get(key) != value:
            raise RuntimeError(f"unexpected boundary field {key}")
    profiles = {
        int(prime): {int(period): count for period, count in profile.items()}
        for prime, profile in boundary["profiles"].items()
    }
    if profiles[2] != {3: 3} or profiles[3] != {4: 8}:
        raise RuntimeError("unexpected mod-2 or mod-3 profile")
    if profiles[5] != {2: 4, 10: 20}:
        raise RuntimeError("unexpected mod-5 Jordan profile")
    return {"boundary": boundary, "profiles": profiles}


def clock_payload(raw: dict[str, Any]) -> dict[str, Any]:
    clock = raw["clock_specificity"]
    if clock["range"] != "ALL_POSITIVE_INTEGERS_PRIME_AND_COMPOSITE":
        raise RuntimeError("unexpected clock range")
    if (
        clock["regularity"]
        != "UNBOUNDED_AND_DISCONTINUOUS_IN_EVERY_TORSION_NEIGHBORHOOD"
    ):
        raise RuntimeError("unexpected clock regularity")
    witnesses = clock["discontinuity_witnesses"]
    expected = [
        ("1/19", 19, 342),
        ("1/55", 55, 990),
        ("1/127", 127, 2286),
    ]
    observed = [
        (
            item["coordinate_displacement"],
            item["coprime_denominator"],
            item["exact_perturbed_order"],
        )
        for item in witnesses
    ]
    if observed != expected:
        raise RuntimeError("unexpected discontinuity witnesses")
    orbit = clock["orbit_sum_monodromy"]
    if orbit["order"] != 5 or orbit["period"] != 10 or orbit["pass"] is not True:
        raise RuntimeError("unexpected orbit/monodromy witness")
    return {"clock": clock, "witnesses": witnesses, "orbit": orbit}
