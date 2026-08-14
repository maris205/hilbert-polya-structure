"""Generate all source-locked Paper 4 publication figures."""

from gen_fig1_action_certificate import main as figure_one
from gen_fig2_gauge_scope_matrix import main as figure_two
from gen_fig3_henon_static_certificate import main as figure_three


def main() -> None:
    figure_one()
    figure_two()
    figure_three()


if __name__ == "__main__":
    main()
