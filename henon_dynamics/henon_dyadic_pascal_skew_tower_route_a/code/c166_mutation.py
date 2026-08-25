#!/usr/bin/env python3
"""Repaired-hash semantic mutations plus a stale-hash control for C166."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def rehash(data):
    data.pop("payload_sha256", None)
    data["payload_sha256"] = sha256(json.dumps(
        data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def changed(base, path, value=None):
    data = json.loads(json.dumps(base))
    target = data
    for key in path[:-1]:
        target = target[key]
    old = target[path[-1]]
    target[path[-1]] = old + 1 if value is None else value
    return data


def main():
    root = Path(__file__).resolve().parents[1]
    base = json.loads((root / "results/c166_pascal_tower_evidence.json").read_text())
    variants = []
    numeric_paths = [
        ("exact_validation", "parameter_rows"),
        ("exact_validation", "coefficient_clock_cases"),
        ("exact_validation", "direct_parameter_rows"),
        ("exact_validation", "direct_state_period_cases"),
        ("exact_validation", "reversor_matrix_rows"),
        ("sentinels", 0, "M"),
        ("sentinels", 0, "primitive_cycle_count"),
        ("sentinels", 0, "half_clock_witness", "k"),
        ("sentinels", 1, "half_clock_witness", "binomial_mod_q"),
        ("sentinels", 2, "fixed_count_at_half_M"),
        ("sentinels", 3, "fixed_count_at_M"),
        ("sentinels", 4, "coefficient_residues_at_M", 0),
    ]
    variants.extend(changed(base, path) for path in numeric_paths)
    replacements = [
        (("pascal_theorem", "clock_formula"), "M=2^(r+d)"),
        (("pascal_theorem", "necessity"), "finite checks suffice"),
        (("pascal_theorem", "fixed_point_criterion"), "some states may be fixed"),
        (("pascal_theorem", "least_period"), "period divides M"),
        (("pascal_theorem", "zeta"), "mutated zeta"),
        (("pascal_theorem", "koopman_determinant"), "mutated determinant"),
        (("reversor_theorem", "substitution"), "sigma(t)=t/(1+t)"),
        (("reversor_theorem", "involution"), "unverified"),
        (("reversor_theorem", "reversal"), "sigma commutes with T"),
        (("reversor_theorem", "antiunitary"), "Theta U Theta^-1=U"),
        (("reversor_theorem", "finite_dimensional_unitary"), False),
        (("reversor_theorem", "target_operator_claimed"), True),
        (("hard_gate", "rejected_candidate"), "none"),
        (("hard_gate", "complexity_claimed"), True),
        (("scope_literal",), "ROUTE_B"),
        (("source_lock", "clock"), "rescaled clock"),
        (("source_lock", "determinant_convention"), "unspecified"),
        (("route_a", "tuple", 3), "A4_ROUTE_B_READY"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("claim_boundary", "euler_factors"), True),
        (("claim_boundary", "hilbert_polya_operator"), True),
        (("sentinels", 0, "reversor_matrix_sha256"), "0" * 64),
        (("source_commit",), "0" * 40),
    ]
    variants.extend(changed(base, path, value) for path, value in replacements)
    stale = changed(base, ("sentinels", 0, "M"))
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c166-mutation-") as temp:
        for index, data in enumerate(variants):
            rehash(data)
            path = Path(temp) / f"mutation-{index}.json"
            path.write_text(json.dumps(data, sort_keys=True, indent=2) + "\n")
            run = subprocess.run([sys.executable, str(root / "code/c166_pascal_tower_checker.py"),
                                  "--evidence", str(path), "--mutation-fast"],
                                 capture_output=True, text=True)
            rejected += run.returncode != 0
        stale_path = Path(temp) / "stale.json"
        stale_path.write_text(json.dumps(stale, sort_keys=True, indent=2) + "\n")
        run = subprocess.run([sys.executable, str(root / "code/c166_pascal_tower_checker.py"),
                              "--evidence", str(stale_path), "--mutation-fast"],
                             capture_output=True, text=True)
        stale_rejected = run.returncode != 0
    assert rejected == len(variants) and stale_rejected
    print(json.dumps({"status": "C166_MUTATION_PASS",
                      "repaired_hash_rejected": rejected,
                      "stale_hash_rejected": 1,
                      "total": len(variants) + 1}, sort_keys=True))


if __name__ == "__main__":
    main()
