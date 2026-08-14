#!/usr/bin/env python3
"""Generate the HCS-P51 convergence/boundary figure from the certificate."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "results" / "c51_certificate.json"
OUTPUT_PDF = PROJECT / "figures" / "abel_pressure_domain.pdf"
OUTPUT_PNG = PROJECT / "figures" / "abel_pressure_domain.png"
TRACE = PROJECT / "figures" / "figure_trace.json"


def main() -> None:
    certificate = json.loads(CERTIFICATE.read_text())
    constants = certificate["constants"]
    phi = float(constants["golden_ratio"])
    h_lower = float(constants["pressure_lower"])
    j_star = float(constants["J_star"])
    sigma_cert = float(constants["sigma_certified"])

    sigmas = [2.70 + 0.005 * index for index in range(301)]
    ratios = [2.0 * phi * math.exp(-sigma * h_lower * math.log(j_star)) for sigma in sigmas]

    boundary_rows = [
        row
        for row in certificate["abel_boundary_lower_bounds"]
        if row["u_radius"] in (0.97, 0.99, 1.0)
    ]
    by_radius: dict[float, list[tuple[int, float]]] = {}
    for row in boundary_rows:
        by_radius.setdefault(float(row["u_radius"]), []).append(
            (int(row["cutoff"]), float(row["flatters_lower_norm"]))
        )

    plt.rcParams.update({"font.size": 9, "axes.titlesize": 10})
    figure, axes = plt.subplots(1, 2, figsize=(8.0, 3.2), constrained_layout=True)

    axes[0].plot(sigmas, ratios, color="#163a6b", linewidth=2.0)
    axes[0].axhline(1.0, color="#a22b2b", linestyle="--", linewidth=1.2)
    axes[0].axvline(sigma_cert, color="#bd7b15", linestyle=":", linewidth=1.5)
    axes[0].fill_between(
        sigmas,
        ratios,
        1.0,
        where=[sigma >= sigma_cert for sigma in sigmas],
        color="#8fc3a4",
        alpha=0.30,
    )
    axes[0].set_xlabel(r"$\Re s$")
    axes[0].set_ylabel(r"$2\varphi e^{-\Re(s)h_-\log J_*}$")
    axes[0].set_title("Certified all-orbit contraction")
    axes[0].annotate(
        rf"$\sigma_{{\rm cert}}={sigma_cert:.4f}$",
        xy=(sigma_cert, 1.0),
        xytext=(sigma_cert + 0.18, 1.10),
        arrowprops={"arrowstyle": "->", "color": "#bd7b15"},
        color="#7a4c08",
    )
    axes[0].grid(alpha=0.22)

    colors = {0.97: "#3b7c8c", 0.99: "#7a5da8", 1.0: "#b33a3a"}
    for radius in sorted(by_radius):
        points = sorted(by_radius[radius])
        axes[1].plot(
            [point[0] for point in points],
            [point[1] for point in points],
            marker="o",
            linewidth=1.8,
            color=colors[radius],
            label=rf"$|u|={radius:.2f}$",
        )
    axes[1].set_xlabel("cyclotomic cutoff $N$")
    axes[1].set_ylabel(r"Flatters lower bound on $\sum_{13\leq n\leq N}\Vert u^nD_n\Vert$")
    axes[1].set_title("One-orbit Abel boundary")
    axes[1].legend(frameon=False)
    axes[1].grid(alpha=0.22)

    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUTPUT_PDF)
    figure.savefig(OUTPUT_PNG, dpi=220)
    plt.close(figure)

    trace = {
        "certificate": str(CERTIFICATE.relative_to(PROJECT)),
        "certificate_sha256": hashlib.sha256(CERTIFICATE.read_bytes()).hexdigest(),
        "outputs": [str(OUTPUT_PDF.relative_to(PROJECT)), str(OUTPUT_PNG.relative_to(PROJECT))],
        "panel_a_claim": "certified outer geometric ratio is below one exactly to the right of sigma_certified",
        "panel_b_claim": "Flatters' theorem forces linear norm growth at |u|=1 while every |u|<1 remains Abel-summable",
        "data_rows_used": len(boundary_rows),
    }
    TRACE.write_text(json.dumps(trace, indent=2, sort_keys=True) + "\n")
    print(json.dumps(trace, sort_keys=True))


if __name__ == "__main__":
    main()
