#!/usr/bin/env python3
"""Repaired-hash and stale-hash hostile tests for HCS-C271."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = json.loads((ROOT / "results/c271_sis_evidence.json").read_text())


def phash(data: dict) -> str:
    payload = dict(data)
    payload.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def rejected(data: dict, repair: bool = True) -> bool:
    if repair:
        data["payload_sha256"] = phash(data)
    with tempfile.TemporaryDirectory(prefix="c271-mut-") as td:
        p = Path(td) / "bad.json"
        p.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        env = dict(os.environ)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        env["C271_EVIDENCE_PATH"] = str(p)
        run = subprocess.run([sys.executable, "-B", str(ROOT / "code/c271_sis_checker.py")], env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return run.returncode != 0


def main() -> None:
    attacks = []
    d = copy.deepcopy(ORIGINAL); d["source_commit"] = "0" * 40; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["scope_flags"]["target_divisor"] = True; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["route_a"]["tuple"][1] = "A1_PASS_ANALYTIC"; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["theorem_contract"]["critical_limit"] = "t*x(t)->v"; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["regression"]["cases"][0]["beta"] = "9/1"; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["regression"]["cases"][0]["metzler_spectral_abscissa"] = "0/1"; attacks.append((d, True))
    super_i = next(i for i, x in enumerate(ORIGINAL["regression"]["cases"]) if x["regime"] == "supercritical")
    d = copy.deepcopy(ORIGINAL); d["regression"]["cases"][super_i]["endemic_coordinate"] = "1/9"; attacks.append((d, True))
    crit_i = next(i for i, x in enumerate(ORIGINAL["regression"]["cases"]) if x["regime"] == "critical")
    d = copy.deepcopy(ORIGINAL); d["regression"]["cases"][crit_i]["critical_kappa"] = "7/1"; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["regression"]["critical_uniform_samples"][0]["y"] = "1/3"; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["unknown_top_level"] = 1; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["candidate_id"] = "HCS-C000"; attacks.append((d, False))
    passed = sum(rejected(d, repair) for d, repair in attacks)
    assert passed == len(attacks)
    print(f"C271 hostile mutation: PASS {passed}/{len(attacks)}")


if __name__ == "__main__":
    main()
