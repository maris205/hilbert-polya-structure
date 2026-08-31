#!/usr/bin/env python3
"""Repaired-hash semantic and stale-hash hostile mutations for C265."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c265_hawkes_evidence.json"
CHECKER = ROOT / "code/c265_hawkes_checker.py"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mutations(original: dict):
    specs = []

    def add(name, fn):
        item = copy.deepcopy(original); fn(item); item["payload_sha256"] = payload_hash(item); specs.append((name, item))

    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C999"))
    add("source", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("epoch", lambda d: d.__setitem__("fixed_epoch", 1))
    add("scope", lambda d: d.__setitem__("scope_literal", "BROKEN_SCOPE"))
    add("scope_flag", lambda d: d["scope_flags"].__setitem__("claims_euler_factors", True))
    add("evaluator", lambda d: d["evaluator"].__setitem__("sha256", "0" * 64))
    add("doi", lambda d: d["citation"].__setitem__("doi", "10.invalid/test"))
    add("predictability", lambda d: d["frozen_object"].__setitem__("predictable_intensity", "lambda_t"))
    add("fourier", lambda d: d["frozen_object"].__setitem__("fourier_convention", "divide by 2pi"))
    add("tuple", lambda d: d["route_a"]["tuple"].__setitem__(4, "A4_NATURAL_QUANTIZATION"))
    add("verdict", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_EXPLORATORY"))
    add("route_b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("affine", lambda d: d["theorem"].__setitem__("affine_transform", "B'=1-bB+z exp(-aB)"))
    add("laplace", lambda d: d["theorem"].__setitem__("stationary_laplace_ode", "L'/L=0"))
    add("dirac", lambda d: d["theorem"].__setitem__("complete_counting_covariance", "continuous only"))
    add("case_count", lambda d: d["regression"].__setitem__("stable_case_count", 319))
    add("mean", lambda d: d["regression"]["stable_cases"][17].__setitem__("mean_intensity", "99/1"))
    add("variance", lambda d: d["regression"]["stable_cases"][33].__setitem__("intensity_variance", "1/7"))
    add("intensity_cov", lambda d: d["regression"]["stable_cases"][49].__setitem__("intensity_covariance_coefficient", "1/9"))
    add("count_cov", lambda d: d["regression"]["stable_cases"][65].__setitem__("counting_continuous_covariance_coefficient", "5/11"))
    add("dirac_mass", lambda d: d["regression"]["stable_cases"][81].__setitem__("counting_dirac_mass", "4/3"))
    add("spectrum", lambda d: d["regression"]["stable_cases"][97].__setitem__("bartlett_zero_frequency", "8/5"))
    add("moment", lambda d: d["regression"]["stable_cases"][113]["moments_m0_to_m10"].__setitem__(5, "7/13"))
    add("window", lambda d: d["regression"]["stable_cases"][129]["window_variance_maclaurin_T1_to_T10"].__setitem__(4, "2/17"))
    add("cluster", lambda d: d["regression"]["cluster_rows"][77].__setitem__("rooted_tree_count", 3))
    add("boundary", lambda d: d["regression"]["boundary_rows"][3].__setitem__("classification", "STATIONARY"))
    add("object_separation", lambda d: d.__setitem__("object_separation", d["object_separation"][:2]))
    return specs


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    specs = mutations(original)
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c265_mutation_") as tmp:
        for name, data in specs:
            path = Path(tmp) / f"{name}.json"
            path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            result = subprocess.run([sys.executable, "-B", str(CHECKER), str(path)], capture_output=True, text=True)
            if result.returncode == 0:
                raise AssertionError(f"mutation survived: {name}")
            rejected += 1
        stale = copy.deepcopy(original)
        stale["candidate_id"] = "HCS-C000"
        stale_path = Path(tmp) / "stale_hash.json"
        stale_path.write_text(json.dumps(stale, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        result = subprocess.run([sys.executable, "-B", str(CHECKER), str(stale_path)], capture_output=True, text=True)
        if result.returncode == 0:
            raise AssertionError("stale hash survived")
        rejected += 1
    total = len(specs) + 1
    print(f"C265 hostile mutations: PASS {rejected}/{total} (repaired semantic={len(specs)}, stale-hash=1)")


if __name__ == "__main__":
    main()
