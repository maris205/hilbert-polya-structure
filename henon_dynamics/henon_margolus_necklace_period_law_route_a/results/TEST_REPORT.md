# C165 test report

Run from the package root on the released bytes:

```text
python code/c165_margolus_producer.py
  C165_PRODUCER_PASS: 16 family rows, 136 fixed cells,
  50 period cells, 87,380 directly enumerated configurations

python code/c165_margolus_checker.py
  C165_CHECKER_PASS: 723 assertions

python code/c165_sympy_crosscheck.py
  C165_SYMPY_PASS: 481 checks

python code/c165_replay.py
  C165_REPLAY_PASS: 68,025 bytes, byte-identical

python code/c165_mutation.py
  C165_MUTATION_PASS: 57 repaired-hash semantic rejections
  plus one stale-hash rejection, 58/58 total
```

The checker imports no producer implementation.  It reconstructs both swap
layers and the complete claim-bearing ledger.  SymPy uses separate matrix,
polynomial, Moebius, and trace-log operations.  Replay writes only to a
temporary directory.  Mutation cases repair the canonical payload hash
before invoking the checker, so rejection cannot be attributed merely to a
stale digest.

The all-parameter proof is in `THEOREM_PACKAGE.md`; no finite cutoff is used
as theorem authority.
