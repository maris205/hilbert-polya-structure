# C98: Exact conditional first-passage kernel atlas

C98 converts the C90 joint-survival receipt into all 400 exact kernels
`P(T_j=b | T_i=a)`.  Among 6800 candidate conditioning rows, 4980 are
attainable and normalized; the remaining 1820 have zero conditioning mass and
are explicitly stored as `null`, never as invented probability laws.  Every
kernel satisfies total expectation, total variance, and cellwise Bayes
balance against its reverse pair.  The twenty diagonal kernels are identity
kernels.

The canonical evidence SHA-256 is
`49179ea34f6f10b7e20c68914cdd7aa5bb5df775cefade69f1a40163f2e933cb`.
The independent checker also rebuilds 6800 equal-threshold joint-survival
cells directly from C88 packed support indicators.  SymPy, clean replay, and
16 hostile mutations pass.

Run from this directory:

```text
python -B code/c98_conditional_kernel.py
python -B code/c98_conditional_kernel_checker.py
python -B code/c98_sympy_crosscheck.py
python -B code/c98_replay_checker.py
python -B code/c98_mutation_test.py
```

The scope is finite combinatorics under `NO_BAD_EULER_OR_ROOT_NUMBER`; no
arithmetic/local data, Euler factors, root numbers, automorphy, full Burnside
ring/table of marks, or Hilbert--Polya operator is claimed.
