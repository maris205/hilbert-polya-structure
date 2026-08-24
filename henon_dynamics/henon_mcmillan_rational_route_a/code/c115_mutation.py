#!/usr/bin/env python3
"""Demand that the independent checker reject twelve hostile mutations."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c115_mcmillan_evidence.json"
CHECKER = PROJECT / "code/c115_mcmillan_checker.py"


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = [
        ("parameter", lambda d: d["source_model"].update({"mu": "-1"})),
        ("forward_pole", lambda d: d["source_model"].update({"forward_pole_divisor": "x**2 - 1 = 0"})),
        ("inverse_identity", lambda d: d["birational_certificates"].update({"left_inverse_composition": ["x+1", "y"]})),
        ("jacobian", lambda d: d["jacobian_certificate"].update({"determinant": "-1"})),
        ("invariant", lambda d: d["first_integral_certificate"].update({"formula": "x**2+y**2"})),
        ("invariance", lambda d: d["first_integral_certificate"].update({"I_after_M_minus_I": "1"})),
        ("fixed_count", lambda d: d["fixed_point_certificate"].update({"real_fixed_count": 3})),
        ("fixed_domain", lambda d: d["fixed_point_certificate"]["valid_fixed_points"][1].update({"forward_denominator": "0", "map_closes": False})),
        ("pole_promoted", lambda d: d["period_two_elimination"]["invalid_cleared_denominator_roots"][0].update({"excluded": False})),
        ("cycle", lambda d: d["primitive_period_two_cycle"].update({"q_minus": ["-2", "1"]})),
        ("monodromy", lambda d: d["period_two_monodromy"].update({"trace": "2"})),
        ("route_inflation", lambda d: d["verdict"].update({"A2": "A2_CERTIFIED_PREFIX"})),
    ]
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c115-mutations-") as temporary:
        root = Path(temporary)
        for index, (name, mutate) in enumerate(mutations):
            changed = json.loads(json.dumps(original))
            mutate(changed)
            path = root / f"{index:02d}_{name}.json"
            path.write_text(json.dumps(changed, sort_keys=True, indent=2) + "\n")
            process = subprocess.run([sys.executable, str(CHECKER), str(path)], text=True, capture_output=True)
            if process.returncode == 0:
                raise AssertionError(f"checker accepted hostile mutation: {name}")
            rejected += 1
    print(f"C115_MUTATION_PASS {rejected}/{len(mutations)}")


if __name__ == "__main__":
    main()
