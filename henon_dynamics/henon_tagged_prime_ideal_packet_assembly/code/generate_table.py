#!/usr/bin/env python3
"""Generate the frozen HCS-P50 LaTeX collision ledger."""

from __future__ import annotations

import json
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "results" / "c50_certificate.json"
OUTPUT = PROJECT / "figures" / "collision_ledger.tex"


def orbit_label(name: str) -> str:
    return {
        "period_1": r"$\gamma_1$",
        "period_3": r"$\gamma_3^{-}$",
        "period_4": r"$\gamma_4$",
    }[name]


def main() -> int:
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    rows = []
    for prime in [29, 109, 131, 38039]:
        atoms = certificate["collision_ledger"][str(prime)]
        for atom in atoms:
            rows.append(
                " & ".join(
                    [
                        str(prime),
                        orbit_label(atom["orbit"]),
                        str(atom["cyclotomic_index"]),
                        atom["prime_ideal"].replace("_", "\\_"),
                        str(atom["residue_degree"]),
                        str(atom["ideal_valuation"]),
                        str(atom["residue_order"]),
                    ]
                )
                + r" \\"
            )
    content = "\n".join(
        [
            r"\begin{tabular}{rrrrrrr}",
            r"\toprule",
            r"$p$ & orbit & $n$ & trace prime ideal & $f$ & $v_{\mathfrak q}$ & order \\",
            r"\midrule",
            *rows,
            r"\bottomrule",
            r"\end{tabular}",
            "",
        ]
    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(content, encoding="utf-8")
    print(OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
