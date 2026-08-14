"""Figure 3: boundary controls and the source-locked Route-A decision."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from frozen_data import FIGURE_DIR, load_frozen_package
from paper_plot_style import COLORS, apply_style, save_figure


def main() -> None:
    data = load_frozen_package()
    negative = data["negative"]
    control = data["control"]
    scope = data["scope"]

    apply_style()
    fig, (ax, route_ax) = plt.subplots(1, 2, figsize=(7.15, 4.2), gridspec_kw={"width_ratios": [1.55, 1]})

    candidate_class = data["candidate"]["classification"]
    planted = control["planted_bad_prime_positive"]
    nonunit = control["non_area_preserving_scope"]["nonunit_dissipative_example"]
    cat = scope["irrational_unit_scope_control"]
    row_labels = [
        "frozen integral Hénon",
        f"planted a={planted['parameter']}",
        f"nonunit δ={nonunit['delta']}",
        "cat-map scope control",
    ]
    col_labels = ["polynomial\nautomorphism", "determinant\none", "empty rational\nbad set", "rational modulus\nother than one"]
    frozen_moduli = candidate_class["exact_rational_modulus_set"]
    planted_moduli = planted["multiplier_moduli"]
    matrix = np.array(
        [
            [
                int(candidate_class["carrier_geometry"].startswith("PASS_GLOBAL_POLYNOMIAL")),
                int(data["source_lock"]["map"]["jacobian_determinant"] == 1),
                int(data["scope"]["bad_set_provenance"]["candidate"] == []),
                int(any(value != "1" for value in frozen_moduli)),
            ],
            [
                int(bool(planted["fixed_point_identity_pass"])),
                int(planted["determinant"] == "1"),
                int(planted["expected_bad_support"] == []),
                int(any(value != "1" for value in planted_moduli)),
            ],
            [
                int(control["non_area_preserving_scope"]["family"].startswith("J_")),
                int(nonunit["delta"] == "1"),
                int(nonunit["unit_status"] == "ALGEBRAIC_UNIT"),
                int(any(value not in {"-1", "1"} and "sqrt" not in value for value in nonunit["multipliers"])),
            ],
            [
                int(bool(cat["matrix"])),
                int(cat["determinant"] == "1"),
                int(all(str(value).lstrip("-").isdigit() for row in cat["matrix"] for value in row)),
                int(bool(cat["spectral_radius_is_rational"])),
            ],
        ]
    )
    cmap = plt.matplotlib.colors.ListedColormap(["#E6E9ED", COLORS["blue"]])
    ax.imshow(matrix, aspect="auto", vmin=0, vmax=1, cmap=cmap)
    ax.set_xticks(range(len(col_labels)), labels=col_labels, rotation=18, ha="right")
    ax.set_yticks(range(len(row_labels)), labels=row_labels)
    ax.tick_params(length=0)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            label = "yes" if matrix[i, j] else "no"
            color = "white" if matrix[i, j] else COLORS["muted"]
            ax.text(j, i, label, ha="center", va="center", color=color, weight="bold", fontsize=7.5)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.text(0.0, 1.08, "Boundary controls", transform=ax.transAxes, fontsize=9.1, weight="bold")
    ax.text(
        0.0,
        -0.16,
        "The support theorem governs exact rational moduli only.",
        transform=ax.transAxes,
        fontsize=7.2,
        color=COLORS["muted"],
    )

    route_ax.axis("off")
    decision = negative["route_a_decision"]
    y_values = [0.88, 0.67, 0.46, 0.25]
    if not decision["carrier_geometry"].startswith("PASS_") or "A0_FAIL" not in decision["a0"]:
        raise RuntimeError("source-locked route labels changed")
    labels = [
        ("Carrier geometry", "PASS: global polynomial\nsymplectic automorphism", COLORS["green"]),
        ("Route A / A0", "FAIL: all-period theorem leaves\nonly rational modulus 1", COLORS["red"]),
        ("A1 and A2--A4", "stopped after A0", COLORS["muted"]),
        ("Final", "Route A rejected for the exact\nrational-prime modulus clock", COLORS["red"]),
    ]
    for (heading, value, color), y in zip(labels, y_values):
        route_ax.text(0.03, y + 0.075, heading, transform=route_ax.transAxes, fontsize=7.5, weight="bold", color=color)
        route_ax.text(
            0.03,
            y,
            value.replace("_", " "),
            transform=route_ax.transAxes,
            fontsize=6.7,
            va="top",
            wrap=True,
            bbox={"boxstyle": "round,pad=0.42", "facecolor": color + "12", "edgecolor": color, "linewidth": 0.9},
        )
        if y != y_values[-1]:
            route_ax.annotate(
                "",
                xy=(0.07, y - 0.10),
                xytext=(0.07, y - 0.015),
                xycoords=route_ax.transAxes,
                arrowprops={"arrowstyle": "-|>", "color": COLORS["muted"], "linewidth": 0.9},
            )
    route_ax.text(0.03, 0.98, "Source-locked decision", transform=route_ax.transAxes, fontsize=9.1, weight="bold")
    route_ax.text(
        0.03,
        0.06,
        f"Irrational-unit control: {scope['irrational_unit_scope_control']['spectral_radius']} is outside the rational-support claim.",
        transform=route_ax.transAxes,
        fontsize=6.8,
        color=COLORS["muted"],
        wrap=True,
    )

    save_figure(fig, FIGURE_DIR / "fig3_scope_route_decision")
    plt.close(fig)


if __name__ == "__main__":
    main()
