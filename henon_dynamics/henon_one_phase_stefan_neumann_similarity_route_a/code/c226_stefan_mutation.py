#!/usr/bin/env python3
"""Hostile semantic/hash mutations for the C226 receipt."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c226_stefan_evidence.json"
CHECKER = ROOT / "code/c226_stefan_checker.py"


def reseal(data: dict) -> None:
    data.pop("payload_sha256", None)
    raw = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = hashlib.sha256(raw).hexdigest()


def altered(base: dict, path: list[object], value: object) -> dict:
    data = copy.deepcopy(base)
    cursor = data
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value
    return data


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    attacks = [
        ("root", ["regression", "cases", 0, "lambda"], "9.0"),
        ("ste", ["regression", "cases", 1, "ste"], "9/10"),
        ("residual", ["regression", "cases", 2, "energy_residual"], "1.0"),
        ("flux_ratio", ["regression", "cases", 3, "interface_wall_flux_ratio"], "1.0"),
        ("series", ["regression", "cases", 0, "small_ste_lambda2_series5"], "0.0"),
        ("erfc_bound", ["regression", "cases", 0, "erfc_upper_bound"], "0.0"),
        ("bound", ["regression", "cases", 5, "lambert_lambda2_lower"], "99.0"),
        ("boundary", ["regression", "boundary_cases", 0, "lambda"], "1.0"),
        ("boundary_statement", ["regression", "boundary_cases", 1, "statement"], ""),
        ("theorem", ["theorem", "root_existence_uniqueness"], "not monotone"),
        ("analytic", ["theorem", "analytic_boundary"], "target match"),
        ("citation_title", ["citations", 1, "title"], "The Classical Stefan Problem"),
        ("citation_author", ["citations", 2, "authors"], "S. C. Gupta"),
        ("citation_year", ["citations", 2, "year"], 1981),
        ("citation_unknown_nested", ["citations", 1, "unexpected_key"], 1),
        ("route", ["route_a", "overall"], "ROUTE_A_SUCCESS_ROUTE_B_READY"),
        ("route_b", ["route_a", "route_b_invocation_allowed"], True),
        ("scope", ["scope_literal"], "TARGET_LOCAL_FACTORS"),
        ("flag", ["scope_flags", "claims_euler_factors"], True),
        ("unknown_nested", ["theorem", "unexpected_key"], 1),
        ("unknown", ["unexpected_key"], 1),
        ("stale", ["payload_sha256"], "0" * 64),
    ]
    caught: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c226-mut-") as directory:
        for idx, (name, path, value) in enumerate(attacks):
            data = altered(base, path, value)
            if name != "stale":
                reseal(data)
            target = Path(directory) / f"mutation-{idx}.json"
            target.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            result = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(target)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            assert result.returncode != 0, f"mutation escaped: {name}"
            caught.append(name)
    print(f"C226 hostile mutations: PASS {len(caught)}/{len(attacks)}")
    print(f"repaired_hash={len(attacks)-1} stale_hash=1; caught={','.join(caught)}")


if __name__ == "__main__":
    main()
