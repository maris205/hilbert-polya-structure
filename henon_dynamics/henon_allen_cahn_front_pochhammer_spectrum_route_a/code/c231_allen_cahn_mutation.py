#!/usr/bin/env python3
"""Hostile mutation suite for C231, including nested unknown/stale attacks."""
from __future__ import annotations

from copy import deepcopy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c231_allen_cahn_evidence.json"
CHECKER = ROOT / "code/c231_allen_cahn_checker.py"


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    x = deepcopy(pristine); x["regression"]["epsilon_rows"][0]["shape_eigenvalue"] = "-999"; mutations.append(("shape_eigenvalue", x))
    x = deepcopy(pristine); x["regression"]["epsilon_rows"][1]["surface_energy"] = "0"; mutations.append(("surface_energy", x))
    x = deepcopy(pristine); x["regression"]["speed_rows"][2]["selection_product_c_times_integral"] = "1"; mutations.append(("speed_selection", x))
    x = deepcopy(pristine); x["regression"]["profile_rows"][0]["front_U"] = "0"; mutations.append(("front_profile", x))
    x = deepcopy(pristine); x["regression"]["profile_rows"][1]["kernel_mode"] = "1"; mutations.append(("kernel_mode", x))
    x = deepcopy(pristine); x["regression"]["energy_rows"][2]["potential_W"] = "1"; mutations.append(("potential", x))
    x = deepcopy(pristine); x["theorem"]["speed_selection"] = "c may be nonzero"; mutations.append(("speed_theorem", x))
    x = deepcopy(pristine); x["theorem"]["factorization"] = "broken"; mutations.append(("factorization", x))
    x = deepcopy(pristine); x["theorem"]["essential_spectrum"] = "all real"; mutations.append(("essential_spectrum", x))
    x = deepcopy(pristine); x["route_a"]["tuple"][4] = "A4_PASS"; mutations.append(("route_tuple", x))
    x = deepcopy(pristine); x["route_a"]["overall"] = "ROUTE_A_ACCEPTED"; mutations.append(("route_overall", x))
    x = deepcopy(pristine); x["route_a"]["route_b_invocation_allowed"] = True; mutations.append(("route_b", x))
    x = deepcopy(pristine); x["scope_flags"]["claims_hilbert_polya_operator"] = True; mutations.append(("scope_flag", x))
    x = deepcopy(pristine); x["frozen_object"]["primitive_periodic_orbit"] = True; mutations.append(("periodic_orbit", x))
    x = deepcopy(pristine); x["citations"][0]["title"] = "fabricated title"; mutations.append(("citation_title", x))
    x = deepcopy(pristine); x["citations"][1]["doi"] = "10.0000/fake"; mutations.append(("citation_doi", x))
    x = deepcopy(pristine); x["theorem"]["unknown_nested"] = True; mutations.append(("unknown_nested", x))
    x = deepcopy(pristine); x["unknown_top"] = True; mutations.append(("unknown_top", x))
    x = deepcopy(pristine); x["payload_sha256"] = "0" * 64; mutations.append(("stale_hash", x))
    x = deepcopy(pristine); x["regression"]["row_counts"]["epsilon"] = 4; mutations.append(("row_count", x))
    x = deepcopy(pristine); del x["regression"]["energy_rows"][0]; mutations.append(("missing_row", x))

    env = dict(os.environ); env["PYTHONDONTWRITEBYTECODE"] = "1"
    caught: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c231-mutations-") as td:
        for name, item in mutations:
            path = Path(td) / f"{name}.json"
            path.write_text(json.dumps(item, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--input", str(path)], env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if proc.returncode != 0:
                caught.append(name)
    assert len(caught) == len(mutations), f"uncaught mutations: {set(name for name, _ in mutations)-set(caught)}"
    print(f"C231 hostile mutations: PASS {len(caught)}/{len(mutations)}")
    print("caught=" + ",".join(caught))


if __name__ == "__main__":
    main()
