#!/usr/bin/env python3
"""Rerun R107 with the frozen R107A Ritz guard-mode remediation."""

from pathlib import Path

from run_r107_fourth_order_quantum import main


if __name__ == "__main__":
    raise SystemExit(main(Path("results/r107a_ritz_remediation")))
