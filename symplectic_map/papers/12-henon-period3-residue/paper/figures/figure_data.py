"""Proof-only contract loader for Paper 12 publication figures."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
CONTRACT_PATH = HERE / "figure_contract.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_contract() -> dict[str, Any]:
    payload = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if payload.get("schema") != "paper12.figure_contract.v1":
        raise RuntimeError("unexpected Paper 12 figure-contract schema")
    if payload.get("evidence_mode") != "PROOF_ONLY_REGISTERED_EVIDENCE_NOT_USED":
        raise RuntimeError("figure contract is not proof-only")
    figures = payload.get("figures")
    if not isinstance(figures, list) or len(figures) != 3:
        raise RuntimeError("figure contract must contain exactly three figures")
    stems = [item.get("stem") for item in figures]
    if len(set(stems)) != 3:
        raise RuntimeError("figure stems must be distinct")
    return payload


def figure_contract(number: int) -> dict[str, Any]:
    payload = load_contract()
    matches = [item for item in payload["figures"] if item["number"] == number]
    if len(matches) != 1:
        raise RuntimeError(f"missing or duplicate figure number {number}")
    return matches[0]
