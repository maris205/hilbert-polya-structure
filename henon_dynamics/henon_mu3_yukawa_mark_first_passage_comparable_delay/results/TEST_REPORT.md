# C95 test report

| Check | Result |
|---|---|
| Producer | `PREFREEZE_G3_PASS` |
| Independent checker | `C95_INDEPENDENT_CHECK_PASS`, 102 pairs, 29,478 cells |
| SymPy | `C95_SYMPY_CROSSCHECK_PASS`, 102 normalized bivariate/delay PGFs |
| Clean replay | `C95_REPLAY_PASS` |
| Hostile mutations | `C95_MUTATION_TEST_PASS`, 17/17 rejected |

The source authority chain and scope firewall are checked in every executable test.
