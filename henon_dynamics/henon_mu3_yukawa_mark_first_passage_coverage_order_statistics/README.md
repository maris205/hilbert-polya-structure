# C96: First-passage target-coverage order statistics

C96 decodes the twenty frozen C88 target hit bitsets on all 65,536 label supports.  It records, for every prefix size, the exact support histogram of the number of targets hit.  For each rank `r=1,...,20`, it then certifies the exact law and moments of `K_r`, the first time at which at least `r` targets have been hit under a uniform permutation of the sixteen labels.

Target 0 is the trivial subgroup and is hit by the empty support.  Therefore the coverage count starts at one and `K_1=0` deterministically; no target is silently removed.  Every rank law carries exact support counts, reduced probabilities, `16!` permutation weights, four raw moments, mean, and variance.

Scope is finite combinatorics under `NO_BAD_EULER_OR_ROOT_NUMBER`.  The package makes no claim about arithmetic or local data, Euler factors, root numbers, automorphy, a full Burnside ring/table of marks, or a Hilbert-Polya operator.

```text
python -B code/c96_coverage_order_statistics.py
python -B code/c96_coverage_order_statistics_checker.py
python -B code/c96_sympy_crosscheck.py
python -B code/c96_replay_checker.py
python -B code/c96_mutation_test.py
```
