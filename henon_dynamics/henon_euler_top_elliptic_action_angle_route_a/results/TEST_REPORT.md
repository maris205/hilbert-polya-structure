# C186 test report

Commands are listed in `code/README.md`.

| gate | result |
|---|---|
| producer | `C186_PRODUCER_PASS`; 180 rows, 1,260 exact residual cells |
| independent checker | `C186_CHECKER_PASS`; 4,268 assertions |
| separate SymPy derivation | `C186_SYMPY_PASS`; 25 checks, including the frozen Lie--Poisson/cap-momentum signs |
| canonical replay | `C186_REPLAY_PASS`; 205,002 bytes |
| repaired-hash mutations | `C186_MUTATION_PASS`; 20/20 rejected |
| stale-hash mutation | `C186_MUTATION_PASS`; 1/1 rejected |

The checker does not import producer code. It reconstructs rational amplitudes, moduli, frequencies, linearized rates, separatrix coefficients, periods, and cap-action quadratures from the frozen inputs. SymPy separately verifies the generic symbolic coefficient identities.

PDF determinism, fonts, clean logs, and two-page rendering pass as recorded in `paper/COMPILE_REPORT.md`. Manifest closure is executed only after all payload files are final.
