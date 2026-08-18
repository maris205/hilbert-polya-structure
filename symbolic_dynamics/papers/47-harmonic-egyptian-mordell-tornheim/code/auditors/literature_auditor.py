#!/usr/bin/env python3
"""Standalone literature ownership consumer L."""

from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
from typing import Any

def canonical(v: Any) -> bytes:
    return (json.dumps(v, sort_keys=True, indent=2, ensure_ascii=True, separators=(",", ": "))+"\n").encode("ascii")
def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out = {}
    for k,v in pairs:
        if k in out: raise ValueError("duplicate")
        out[k]=v
    return out
def load(path: Path) -> dict[str, Any]:
    raw=path.read_bytes(); obj=json.loads(raw.decode("ascii"),object_pairs_hook=unique)
    if type(obj) is not dict or raw!=canonical(obj): raise ValueError("canonical")
    return obj
def reject(code: str) -> None:
    sys.stdout.buffer.write(canonical({"consumer":"L","rejection_code":code,"schema":"paper47-mutation-rejection-v1","status":"REJECT"})); raise SystemExit(2)
def validate_model(model: dict[str, Any]) -> None:
    if type(model.get("mt_novelty_claimed")) is not bool or model["mt_novelty_claimed"] is not False:
        reject("LITERATURE_OWNERSHIP_FAILURE")
def normal(root: Path) -> dict[str, Any]:
    validate_model(load(root/"contracts/SCIENCE_MODEL.json"))
    path=root/"preauthority/LITERATURE_NOVELTY_AUDIT.md"; text=path.read_text(encoding="utf-8")
    for marker in ["L. Tornheim", "L. J. Mordell", "Bradley", "Tsumura", "Kalinin", "zero novelty credit", "PRIORITY_NOT_PROVED", "STOP_DUPLICATE"]:
        if marker not in text: raise ValueError("ownership marker")
    return {"candidate_id":"SD-C49","payload":{"disposition":"SEARCH_BOUNDED_NO_EXACT_OPERATOR_PACKAGE",
            "external_stop_duplicate":"LIVE_CONDITIONAL_NOT_ROUTE_TERMINAL",
            "literature_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
            "novelty_boundary":"EXACT_FROZEN_GRAPH_SAME_OBJECT_REALIZATION_ONLY"},
            "schema":"paper47-literature-audit-v1","status":"PASS"}
def main() -> None:
    p=argparse.ArgumentParser(allow_abbrev=False); g=p.add_mutually_exclusive_group(required=True)
    g.add_argument("--root"); g.add_argument("--validate-model"); a=p.parse_args()
    try:
        if a.validate_model: validate_model(load(Path(a.validate_model).resolve(strict=True))); out={"consumer":"L","schema":"paper47-model-accept-v1","status":"PASS"}
        else: out=normal(Path(a.root).resolve(strict=True))
        sys.stdout.buffer.write(canonical(out))
    except SystemExit: raise
    except Exception as exc: sys.stderr.write(f"L_ERROR:{type(exc).__name__}\n"); raise SystemExit(3)
if __name__=="__main__": main()
