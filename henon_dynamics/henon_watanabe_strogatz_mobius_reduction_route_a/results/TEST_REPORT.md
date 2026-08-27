# C189 test report

Commands are listed in `code/README.md`.

| gate | result |
|---|---|
| producer | `C189_PRODUCER_PASS`; 96 Riccati rows, 48 action rows, 128 cross-ratio cells |
| independent checker | `C189_CHECKER_PASS`; 2,646 assertions and 40 independent landmark reconstructions |
| separate SymPy derivation | `C189_SYMPY_PASS`; 18 generic identities |
| canonical replay | `C189_REPLAY_PASS`; 185,717 bytes |
| repaired-hash mutations | `C189_MUTATION_PASS`; 24/24 rejected |
| stale-hash mutation | `C189_MUTATION_PASS`; 1/1 rejected |

The checker does not import producer code.  It reconstructs every rational
circle point, Riccati velocity, disk automorphism, collision partition,
cross ratio, constant discriminant, fixed root, and period coefficient from
the frozen inputs.  For each row with three distinct clusters, it also solves
an independent exact three-landmark projective reconstruction.  SymPy
separately verifies the generic lift and invariant identities.

PDF determinism, fonts, clean logs, and two-page rendering pass as recorded in
`paper/COMPILE_REPORT.md`.  Manifest closure is executed only after all
payload files are final.
