#!/usr/bin/env python3
"""Hostile repaired-hash, nested-schema and stale-hash tests for C224."""
from __future__ import annotations
from copy import deepcopy
from hashlib import sha256
import argparse, json, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c224_landau_zener_evidence.json"
CHECKER = Path(__file__).with_name("c224_landau_zener_checker.py")

def repair(data: dict) -> None:
    body = dict(data); body.pop("payload_sha256", None)
    data["payload_sha256"] = sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def rejected(data: dict, path: Path) -> bool:
    path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    return subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(path)], capture_output=True).returncode != 0

def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    original = json.loads(parser.parse_args().evidence.read_text())
    mutations = [
        lambda d: d.__setitem__("source_commit", "0"*40),
        lambda d: d["evaluator"].__setitem__("sha256", "0"*64),
        lambda d: d.__setitem__("scope_literal", "BAD_SCOPE"),
        lambda d: d.__setitem__("headline", "synthetic"),
        lambda d: d["frozen_object"].__setitem__("equation", "i psi'=0"),
        lambda d: d["frozen_object"].__setitem__("finite_window_status", "exact finite propagator"),
        lambda d: d["theorem"].__setitem__("scattering_probability", "P=1 always"),
        lambda d: d["theorem"].__setitem__("stokes_phase", "phase omitted"),
        lambda d: d["theorem"].__setitem__("scope_boundary", "same as C223"),
        lambda d: d["route_a"].__setitem__("tuple", ["A0_PASS"]*5),
        lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_STRONG_CANDIDATE"),
        lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True),
        lambda d: d["scope_flags"].__setitem__("claims_hilbert_polya_operator", True),
        lambda d: d["citations"][0].__setitem__("persistent_url", "https://example.invalid"),
        lambda d: d["regression"].__setitem__("window_values", ["0"]),
        lambda d: d["regression"]["scattering_rows"][0].__setitem__("P_diabatic", "2"),
        lambda d: d["regression"]["scattering_rows"][1].__setitem__("case_id", "duplicate"),
        lambda d: d["regression"]["finite_window_rows"][0].__setitem__("unknown_nested_key", True),
        lambda d: d.__setitem__("unknown_top_level_key", True),
        lambda d: d["nonclaims"].clear(),
    ]
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "mutated.json"; repaired = 0
        for i, mutate in enumerate(mutations):
            candidate = deepcopy(original); mutate(candidate); repair(candidate)
            if not rejected(candidate, path): raise AssertionError(f"repaired mutation {i} survived")
            repaired += 1
        stale = deepcopy(original); stale["regression"]["finite_window_rows"][0]["window_discrepancy"] = "999"
        if not rejected(stale, path): raise AssertionError("stale-hash mutation survived")
    print(json.dumps({"status": "C224_MUTATION_PASS", "repaired_hash_rejections": repaired, "unknown_key_rejections": 2, "stale_hash_rejections": 1, "total_rejections": repaired+1}, sort_keys=True))

if __name__ == "__main__": main()
