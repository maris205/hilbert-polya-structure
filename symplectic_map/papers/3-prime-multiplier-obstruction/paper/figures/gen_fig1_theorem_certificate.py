from __future__ import annotations

import textwrap

import matplotlib.pyplot as plt

from frozen_data import checklist_by_id, load_core, require
from paper_plot_style import OKABE_ITO, add_panel_tag, rounded_box, save_fig, status_color


def wrap(text: str, width: int) -> str:
    return textwrap.fill(text, width=width)


def draw_card(ax, x, y, w, h, header, body, status, body_size=7.15):
    face, edge = status_color(status)
    rounded_box(ax, x, y, w, h, face, edge, linewidth=1.1)
    ax.text(x + 0.02, y + h - 0.025, header, ha="left", va="top", fontsize=8.1, fontweight="bold")
    status_display = status.replace("_", " ")
    ax.text(
        x + w - 0.02,
        y + 0.022,
        status_display,
        ha="right",
        va="bottom",
        fontsize=6.45,
        color=edge,
        fontweight="bold",
    )
    ax.text(
        x + 0.02,
        y + h - 0.075,
        body,
        ha="left",
        va="top",
        fontsize=body_size,
        linespacing=1.16,
    )


def main() -> None:
    core = load_core()
    source_lock = core["source_lock"]
    proof_audit = core["proof_audit"]
    negative = core["negative_ledger"]
    bridge = core["bridge_audit"]

    require(proof_audit["status"] == "PASS", "proof_audit must PASS")
    require(bridge["status"] == "PASS", "symplectic_bridge_audit must PASS")
    checks = checklist_by_id(proof_audit["checklist"])
    for key in [
        "periodic_point_integrality",
        "chain_content_factor",
        "rational_algebraic_integer_step",
        "quadratic_derivative_content",
        "p2_residue_explicitly_open",
        "modulus_only_nonclaim",
    ]:
        require(checks[key]["status"] == "PASS", f"missing PASS for {key}")
    require(negative["raw_rational_prime_all_periods"]["status"] == "ABSENT_BY_THEOREM", "raw theorem gate changed")
    require(negative["p2_rational_exponent_prime_period_ge_2"]["status"] == "OPEN", "p=2 open boundary changed")
    require(negative["complex_modulus_only_target"] == "OUTSIDE_THEOREM", "complex modulus boundary changed")
    for key, value in bridge["checks"].items():
        require(value is True, f"bridge check {key} failed")

    fig = plt.figure(figsize=(14.2, 6.1))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.18, 1.12, 1.0], wspace=0.18)

    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[0, 1])
    ax2 = fig.add_subplot(gs[0, 2])
    for ax in (ax0, ax1, ax2):
        ax.set_axis_off()
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

    add_panel_tag(ax0, "(a)")
    theorem_cards = [
        (
            "frozen parameter",
            wrap(
                f"P(U)={source_lock['parameter']['minimal_polynomial_candidate']}; "
                f"{checks['quadratic_derivative_content']['evidence']}.",
                38,
            ),
            "PASS",
        ),
        (
            "integrality of the orbit",
            wrap(checks["periodic_point_integrality"]["evidence"], 38),
            checks["periodic_point_integrality"]["status"],
        ),
        (
            "chain-rule content factor",
            wrap(checks["chain_content_factor"]["evidence"], 38),
            checks["chain_content_factor"]["status"],
        ),
        (
            "rationality step",
            wrap(checks["rational_algebraic_integer_step"]["evidence"], 38),
            checks["rational_algebraic_integer_step"]["status"],
        ),
        (
            "all-period conclusion",
            wrap(source_lock["predeclared_exact_predictions"]["candidate_divisibility"], 38),
            "ABSENT_BY_THEOREM",
        ),
    ]
    y_positions = [0.80, 0.61, 0.42, 0.23, 0.04]
    for idx, (header, body, status) in enumerate(theorem_cards):
        y = y_positions[idx]
        draw_card(ax0, 0.04, y, 0.92, 0.15, header, body, status)
        if idx < len(theorem_cards) - 1:
            ax0.annotate(
                "",
                xy=(0.50, y - 0.005),
                xytext=(0.50, y - 0.035),
                arrowprops=dict(arrowstyle="->", color=OKABE_ITO["gray"], lw=1.2),
            )

    add_panel_tag(ax1, "(b)")
    raw_target = source_lock["definitions"]["raw_rational_prime_target"]
    exp_target = source_lock["definitions"]["rational_exponent_prime_target"]
    mod_target = source_lock["definitions"]["complex_modulus_only_target"]
    gate_cards = [
        (
            "raw rational-prime target",
            wrap(raw_target, 36) + "\n\n" + wrap(negative["raw_rational_prime_all_periods"]["basis"], 36),
            negative["raw_rational_prime_all_periods"]["status"],
            0.68,
            0.28,
        ),
        (
            "rational exponent-prime target",
            wrap(exp_target, 36)
            + "\n\nodd p: "
            + negative["odd_rational_exponent_prime_all_periods"]["status"].replace("_", " ")
            + "\np=2, n=1: "
            + negative["p2_rational_exponent_prime_period_1"]["status"]
            + "\np=2, n>=2: "
            + negative["p2_rational_exponent_prime_period_ge_2"]["status"],
            negative["p2_rational_exponent_prime_period_ge_2"]["status"],
            0.34,
            0.29,
        ),
        (
            "modulus-only target",
            wrap(mod_target, 36),
            negative["complex_modulus_only_target"],
            0.07,
            0.21,
        ),
    ]
    for header, body, status, y0, h in gate_cards:
        draw_card(ax1, 0.04, y0, 0.92, h, header, body, status, body_size=7.2)

    add_panel_tag(ax2, "(c)")
    ax2.fill_between([0.06, 0.46], [0.40, 0.40], [0.91, 0.91], color=OKABE_ITO["soft_green"], alpha=0.75)
    ax2.fill_between([0.54, 0.94], [0.40, 0.40], [0.91, 0.91], color=OKABE_ITO["soft_green"], alpha=0.75)
    ax2.plot([0.06, 0.94], [0.45, 0.45], color=OKABE_ITO["black"], lw=1.0)
    ax2.plot([0.5, 0.5], [0.40, 0.91], color=OKABE_ITO["vermillion"], lw=2.0, linestyle="--")
    ax2.text(0.26, 0.87, bridge["domain"][0], ha="center", va="center", fontsize=8.8)
    ax2.text(0.74, 0.87, bridge["domain"][1], ha="center", va="center", fontsize=8.8)
    ax2.text(0.5, 0.925, "q=0", ha="center", va="bottom", fontsize=8.8, color=OKABE_ITO["vermillion"])
    ax2.text(0.08, 0.475, "zero section  p=0", ha="left", va="bottom", fontsize=7.7)
    rounded_box(ax2, 0.06, 0.03, 0.88, 0.09, OKABE_ITO["soft_blue"], OKABE_ITO["blue"], linewidth=1.0)
    ax2.text(
        0.08,
        0.075,
        wrap(source_lock["symplectic_bridge"]["formula"], 44),
        ha="left",
        va="center",
        fontsize=7.5,
    )
    rounded_box(ax2, 0.56, 0.62, 0.36, 0.15, OKABE_ITO["soft_blue"], OKABE_ITO["blue"], linewidth=1.0)
    ax2.text(
        0.58,
        0.695,
        wrap(source_lock["symplectic_bridge"]["zero_section_return_spectrum"], 24),
        ha="left",
        va="center",
        fontsize=7.0,
        linespacing=1.15,
    )
    caveat_text = "\n".join(
        textwrap.fill(f"• {item}", width=48, subsequent_indent="  ")
        for item in bridge["mandatory_limitations"][:3]
    )
    rounded_box(ax2, 0.06, 0.18, 0.88, 0.15, OKABE_ITO["soft_yellow"], OKABE_ITO["orange"], linewidth=1.0)
    ax2.text(0.08, 0.305, caveat_text, ha="left", va="top", fontsize=6.75, linespacing=1.12)
    ax2.annotate(
        r"$(\lambda,\lambda^{-1})$",
        xy=(0.73, 0.45),
        xytext=(0.72, 0.56),
        fontsize=8.5,
        arrowprops=dict(arrowstyle="->", color=OKABE_ITO["blue"], lw=1.2),
        color=OKABE_ITO["blue"],
    )

    save_fig(fig, "fig1_theorem_certificate")
    plt.close(fig)


if __name__ == "__main__":
    main()
