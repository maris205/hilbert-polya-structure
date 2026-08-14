"""Figure 3: exact Hénon identities and proof-ledger boundary."""

from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from frozen_data import FIGURE_DIR, load_frozen_package
from paper_plot_style import COLORS, apply_style, save_figure


def box(ax, x, y, w, h, heading, body, color):
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.015,rounding_size=0.02",
            facecolor=color + "16",
            edgecolor=color,
            linewidth=1.0,
        )
    )
    ax.text(x + 0.018, y + h - 0.045, heading, fontsize=8.5, weight="bold", color=color, va="top")
    ax.text(x + 0.018, y + h - 0.105, body, fontsize=7.3, va="top", linespacing=1.45)


def main() -> None:
    data = load_frozen_package()
    henon = data["henon"]
    identity = henon["henon_identity"]
    recurrence = henon["recurrence_multiplicity"]
    infinity = henon["projective_infinity"]
    sint = henon["s_integral_denominator"]
    sections = [identity, recurrence, infinity, sint]
    if any(section.get("pass") is not True for section in sections):
        raise RuntimeError("the frozen Hénon proof ledger changed")
    if any(value != "0" for value in identity["residuals"].values()):
        raise RuntimeError("a frozen Hénon identity residual is nonzero")
    records = infinity["records"]
    if any(record["projective_point_at_infinity_exists"] for record in records):
        raise RuntimeError("a static no-infinity record changed")

    apply_style()
    fig, ax = plt.subplots(figsize=(7.15, 4.75))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.text(0.02, 0.955, "Exact Hénon specialization", fontsize=9.4, weight="bold")
    ax.text(
        0.98,
        0.955,
        "no periodic equation solved",
        ha="right",
        fontsize=7.5,
        color=COLORS["muted"],
    )

    identity_body = (
        r"$H_a(q,p)=(q^2-a-p,q)$" "\n"
        r"$\det DH_a=" + identity["jacobian_determinant"] + r"$" "\n"
        r"$G=\frac{2}{3}q^3-pq$,  $L_a|_{\Gamma_H}=-G$" "\n"
        f"five exact residuals = {set(identity['residuals'].values()).pop()}"
    )
    recurrence_body = (
        r"$q_{j+1}+q_{j-1}=q_j^2-a$" "\n"
        r"period 1: both neighbor slots are $q_0$" "\n"
        r"period 2: both slots are $q_1$ (and vice versa)" "\n"
        "ordered-slot multiplicity: PASS"
    )
    periods = ", ".join(str(record["period"]) for record in records)
    infinity_body = (
        f"audited periods: {periods}\n"
        r"at $Z=0$: every leading equation is $Q_j^2=0$" "\n"
        "all projective coordinates forced zero\n"
        "dimension implication:\nfinite affine periodic scheme"
    )
    sharp = sint["sharpness_control"]
    sint_body = (
        r"outside $S$: $R^2\leq R$ forbids $R>1$" "\n"
        r"certified: $3\mathcal{A}_G\in\mathcal{O}_{K,S}$" "\n"
        "denominator support: {3}\n"
        f"sharp control: a={sharp['parameter']}, P=({', '.join(sharp['fixed_point'])}), "
        f"action={sharp['action']}"
    )
    box(ax, 0.02, 0.53, 0.46, 0.34, "Map, one-form, and sign", identity_body, COLORS["blue"])
    box(ax, 0.52, 0.53, 0.46, 0.34, "Cyclic recurrence", recurrence_body, COLORS["sky"])
    box(ax, 0.02, 0.12, 0.46, 0.34, "All-period algebraicity ledger", infinity_body, COLORS["green"])
    box(ax, 0.52, 0.12, 0.46, 0.34, "Valuation and denominator ledger", sint_body, COLORS["orange"])
    ax.text(
        0.5,
        0.045,
        data["summary"]["classification"].replace("_", " "),
        ha="center",
        fontsize=7.3,
        weight="bold",
        color=COLORS["purple"],
    )

    save_figure(fig, FIGURE_DIR / "fig3_henon_static_certificate")
    plt.close(fig)


if __name__ == "__main__":
    main()
