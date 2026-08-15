"""Fail-closed loaders for the frozen Paper 7 figure inputs."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


PAPER_ROOT = Path(__file__).resolve().parent.parent
SOURCE_LOCK_PATH = PAPER_ROOT / "experiments" / "source_lock.json"
RESULT_PATH = PAPER_ROOT / "results" / "EXPERIMENT_RESULTS.json"
EXPECTED_SOURCE_LOCK_SHA256 = (
    "205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1"
)


class ContractError(RuntimeError):
    """Raised when a figure input no longer matches the frozen contract."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ContractError(f"expected a JSON object: {path}")
    return data


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractError(message)


def load_frozen_inputs() -> tuple[dict[str, Any], dict[str, Any]]:
    source = load_json(SOURCE_LOCK_PATH)
    result = load_json(RESULT_PATH)
    observed_source_sha = sha256_file(SOURCE_LOCK_PATH)
    require(
        observed_source_sha == EXPECTED_SOURCE_LOCK_SHA256,
        "source-lock hash differs from the frozen Paper 7 binding",
    )
    require(
        source.get("candidate_id") == result.get("candidate_id"),
        "candidate id differs between source lock and registered result",
    )
    require(
        result.get("source_lock_sha256") == observed_source_sha,
        "registered result is not bound to the live source lock",
    )
    require(result.get("pass") is True, "registered result did not pass")
    require(
        result.get("candidate_numerical_runs") == 0,
        "figure contract permits exact symbolic candidate records only",
    )
    require(
        result.get("external_prime_tables_accessed") is False,
        "external prime-table access is outside the figure contract",
    )
    require(
        result.get("riemann_zero_data_accessed") is False,
        "Riemann-zero access is outside the figure contract",
    )
    return source, result


def proof_contract(result: dict[str, Any]) -> dict[str, Any]:
    contract = result.get("pre_execution_gates", {}).get("proof_contract")
    require(isinstance(contract, dict), "proof contract is absent")
    require(contract.get("pass") is True, "proof contract did not pass")
    return contract


def controls_contract(result: dict[str, Any]) -> dict[str, Any]:
    controls = result.get("pre_execution_gates", {}).get("controls")
    require(isinstance(controls, dict), "controls contract is absent")
    require(controls.get("pass") is True, "controls contract did not pass")
    require(controls.get("external_data_accessed") is False, "unsafe control data")
    return controls

