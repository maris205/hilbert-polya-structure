# C101: Exact three-target first-passage coupling

C101 derives the exact joint first-passage-time law for every unordered triple
of the twenty frozen C88 targets.  The 1,140 triples have 17^3 cells each,
for 5,600,820 exact permutation-count cells.  Pair and single marginals are
recovered from the C90 and C88 receipts, and exact low-order moments,
covariances, and third interaction cumulants are recorded.

Run from this directory:

```text
python -B code/c101_triple_coupling.py
python -B code/c101_triple_coupling_checker.py
python -B code/c101_sympy_crosscheck.py
python -B code/c101_replay_checker.py
python -B code/c101_mutation_test.py
python -B code/c101_release_manifest.py
```

Scope: finite permutation combinatorics under
`NO_BAD_EULER_OR_ROOT_NUMBER`; no arithmetic local data, Euler factors, root
numbers, automorphy, full Burnside/table of marks, or Hilbert--Polya operator
is claimed.
