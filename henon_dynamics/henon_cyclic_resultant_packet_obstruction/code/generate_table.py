#!/usr/bin/env python3
"""Generate the paper's selected exact-resultant LaTeX table from JSON."""

from __future__ import annotations

import json
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
SOURCE = PROJECT / "results" / "c49_certificate.json"
TARGET = PROJECT / "figures" / "packet_ledger.tex"
SELECTION = {
    "period_1": (2, 3, 4, 7),
    "period_3": (2, 3, 5, 6),
    "period_4": (2, 3, 4, 6),
}


def main() -> int:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    lines = [
        r"\begin{tabular}{lrrrrl}",
        r"\toprule",
        r"orbit & $n$ & $|C_n|$ & half norm & half type & scope \\",
        r"\midrule",
    ]
    for orbit_name, indices in SELECTION.items():
        rows = {row["index"]: row for row in data["orbits"][orbit_name]["rows"]}
        for index in indices:
            row = rows[index]
            half = row["canonical_half_norm"]
            if half is None:
                half_text = r"--"
                half_type = "not forced square"
            else:
                half_text = str(half)
                half_type = "prime" if row["half_norm_is_rational_prime"] else "composite"
            scope = "$n=2$ control" if index == 2 else "theorem row"
            label = orbit_name.replace("period_", "period ")
            lines.append(
                f"{label} & {index} & {row['primitive_cyclotomic_norm_abs']} & "
                f"{half_text} & {half_type} & {scope} \\\\"
            )
    lines.extend([r"\bottomrule", r"\end{tabular}"])
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(TARGET)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
