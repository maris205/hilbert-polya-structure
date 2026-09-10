# C103: Exact min/max aggregation of first-passage times

C103 derives the full laws of $\min(T_i,T_j)$ and $\max(T_i,T_j)$ for all 400
ordered pairs of the twenty C88 targets from the C90 joint survival receipt.
It certifies diagonal tails, inclusion--exclusion for the maximum CDF,
transpose transport, and $\mathbb E\min+\mathbb E\max=\mathbb ET_i+\mathbb ET_j$.

Run from this directory:

```text
python -B code/c103_minmax_aggregation.py
python -B code/c103_minmax_aggregation_checker.py
python -B code/c103_sympy_crosscheck.py
python -B code/c103_replay_checker.py
python -B code/c103_mutation_test.py
```

Scope: finite combinatorics under `NO_BAD_EULER_OR_ROOT_NUMBER`; no arithmetic
local data, Euler factors, root numbers, automorphy, full Burnside/table of
marks, or Hilbert--Pólya operator is claimed.
