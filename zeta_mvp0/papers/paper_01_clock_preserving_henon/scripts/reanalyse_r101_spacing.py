#!/usr/bin/env python3
"""Recompute R101 spacing fields after enforcing ordered extrapolated levels."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from hp_candidate_search.quantum_fd import spacing_diagnostics


def main() -> int:
    root = Path("results/r101_quantum_refinement")
    path = root / "summary.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    for record in data["records"]:
        spectra = np.load(root / record["spectrum_file"])
        fine = spectra["eigenvalues"]
        extrapolated = spectra["extrapolated_eigenvalues"]
        record["fine_diagnostics"] = spacing_diagnostics(fine)
        record["extrapolated_diagnostics"] = spacing_diagnostics(extrapolated)
        fine_ratio = record["fine_diagnostics"]["mean_spacing_ratio"]
        extrapolated_ratio = record["extrapolated_diagnostics"]["mean_spacing_ratio"]
        record["mean_ratio_fine_extrapolated_difference"] = abs(
            fine_ratio - extrapolated_ratio
        )
        record["passes_mean_ratio_stability_0p02"] = bool(
            abs(fine_ratio - extrapolated_ratio) < 0.02
        )
    nonradial = [record for record in data["records"] if record["spec"]["a"] != 0.0]
    data["nonradial_mean_ratio_stability"] = {
        "threshold": 0.02,
        "passing_cells": sum(
            record["passes_mean_ratio_stability_0p02"] for record in nonradial
        ),
        "total_cells": len(nonradial),
        "all_pass": all(
            record["passes_mean_ratio_stability_0p02"] for record in nonradial
        ),
        "post_hoc_diagnostic": True,
    }
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(data["nonradial_mean_ratio_stability"], indent=2, sort_keys=True))
    for record in data["records"]:
        print(
            record["label"],
            record["fine_diagnostics"]["mean_spacing_ratio"],
            record["extrapolated_diagnostics"]["mean_spacing_ratio"],
            record["mean_ratio_fine_extrapolated_difference"],
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
