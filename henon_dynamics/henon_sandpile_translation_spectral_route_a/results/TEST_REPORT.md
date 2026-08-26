# C176 test report

Commands and required terminal statuses:

```text
python code/c176_sandpile_producer.py       -> C176_PRODUCER_PASS
python code/c176_sandpile_checker.py        -> C176_INDEPENDENT_CHECK_PASS (135,049 assertions)
python code/c176_sympy_crosscheck.py        -> C176_SYMPY_PASS (5,248 checks)
python code/c176_replay.py                  -> C176_REPLAY_PASS
python code/c176_mutation.py                -> C176_MUTATION_PASS (17/17 rejected)
python code/c176_release_manifest.py        -> C176_MANIFEST_PASS (27 payload files)
```

The producer burns one vertex at a time, uses a Bareiss determinant, and topples the lowest unstable vertex. The checker independently burns all eligible vertices, uses Leibniz determinants, and compares lowest- and highest-unstable stabilization. It verifies one recurrent representative per quotient signature, actual translation by `adj(Delta)b mod D`, every cycle, fixed count, inversion reversal, and self-adjoint boundary. SymPy independently computes unimodular Smith decompositions and both order formulas.

Replay compares fresh bytes. Sixteen semantic mutations repair the payload hash; one additional mutation leaves it stale. Paper gates require distinct round PDFs, `main.pdf == main_round2.pdf`, byte-identical fixed-epoch fresh builds, embedded fonts, clean logs, and full visual snapshots.
