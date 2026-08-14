"""Generate all figures from the frozen exact-audit package."""

from gen_fig1_good_reduction_certificate import main as generate_fig1
from gen_fig2_exact_period_audit import main as generate_fig2
from gen_fig3_scope_route_decision import main as generate_fig3


def main() -> None:
    generate_fig1()
    generate_fig2()
    generate_fig3()


if __name__ == "__main__":
    main()

