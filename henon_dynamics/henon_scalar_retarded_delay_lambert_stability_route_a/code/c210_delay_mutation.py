#!/usr/bin/env python3
"""Hostile semantic/schema mutations for the C210 checker."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c210_delay_evidence.json"
CHECKER = Path(__file__).with_name("c210_delay_checker.py")


def repair_hash(data: dict) -> None:
    body = dict(data); body.pop("payload_sha256", None)
    data["payload_sha256"] = sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def rejected(data: dict, path: Path) -> bool:
    path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    return subprocess.run([sys.executable, str(CHECKER), "--evidence", str(path)], capture_output=True).returncode != 0


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = [
        lambda d: d.__setitem__("source_commit", "0" * 40),
        lambda d: d["evaluator"].__setitem__("sha256", "0" * 64),
        lambda d: d.__setitem__("scope_literal", "BAD_SCOPE"),
        lambda d: d.__setitem__("headline", "synthetic"),
        lambda d: d["frozen_object"].__setitem__("determinant_convention", "Fredholm target determinant"),
        lambda d: d["frozen_object"].__setitem__("arithmetic_origin", "prime labels"),
        lambda d: d["theorem"].__setitem__("hopf_boundary", "all roots stable"),
        lambda d: d["theorem"].__setitem__("root_multiplicity", "Delta never vanishes"),
        lambda d: d["theorem"].__setitem__("spectral_mapping", "each root preserves multiplicity without collision aggregation"),
        lambda d: d["route_a"].__setitem__("tuple", ["A0_PASS"] * 5),
        lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_STRONG_CANDIDATE"),
        lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True),
        lambda d: d["scope_flags"].__setitem__("claims_euler_factors", True),
        lambda d: d["citations"][0].__setitem__("persistent_url", "https://example.invalid"),
        lambda d: d["regression"]["cases"][0].__setitem__("a", "99"),
        lambda d: d["regression"]["cases"][1].__setitem__("regime", "wrong"),
        lambda d: d["regression"]["cases"][2]["fundamental_solution_terms_t_quarters"].__setitem__(3, "0"),
        lambda d: d["regression"]["cases"][3]["reported_times"].__setitem__(1, "0"),
        lambda d: d["regression"]["cases"][9]["fundamental_solution_terms_t_quarters"].__setitem__(4, "1(t=0); exp(-3*t)(t>0)"),
        lambda d: d["regression"]["cases"][10].__setitem__("branch_point_condition", "b*tau=exp(-1)"),
        lambda d: d["regression"]["hopf_formula_controls"][0].__setitem__("omega", "2"),
        lambda d: d["summary"].__setitem__("fundamental_symbolic_cell_count", 1),
        lambda d: d.__setitem__("unknown_top_level_key", True),
        lambda d: d["regression"]["cases"][0].__setitem__("unknown_nested_key", True),
    ]
    repaired = 0
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "mutated.json"
        for i, mutate in enumerate(mutations):
            data = deepcopy(original); mutate(data); repair_hash(data)
            if not rejected(data, path):
                raise AssertionError(f"mutation {i} survived")
            repaired += 1
        stale = deepcopy(original)
        stale["regression"]["cases"][0]["zero_root_condition"] = "777"
        if not rejected(stale, path):
            raise AssertionError("stale-hash mutation survived")
    print(json.dumps({"status": "C210_MUTATION_PASS", "repaired_hash_rejections": repaired, "stale_hash_rejections": 1, "unknown_key_rejections": 2, "total_rejections": repaired + 1}, sort_keys=True))


if __name__ == "__main__":
    main()
