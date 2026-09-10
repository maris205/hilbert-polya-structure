# C100: Exact first-passage dependence geometry

C100 reconstructs the joint PMF of `(T_i,T_j)` for all 400 ordered C90 target pairs using finite differences of joint survival cells and C88 marginal boundary values.  Each row stores exact integer joint cells, marginal cells, means, variances, mixed product moment, covariance, a rational normalized-covariance proxy `Cov/(Var_i+Var_j)`, exact Pearson correlation data (squared rational and signed radical), total variation and L1 distance from the product marginals, and a rational Frechet interval-width/violation geometry.

The relation spectrum is 20 diagonal, 164 strict-comparable, and 216 incomparable pairs.  Pair transpose identities and diagonal identities are checked explicitly.  Scope is finite combinatorics under `NO_BAD_EULER_OR_ROOT_NUMBER`; no arithmetic/local, Euler, root-number, automorphy, full Burnside/table-of-marks, or Hilbert--Polya claim is made.

Run from this directory:

```text
python -B code/c100_pair_dependence_geometry.py
python -B code/c100_pair_dependence_geometry_checker.py
python -B code/c100_sympy_crosscheck.py
python -B code/c100_replay_checker.py
python -B code/c100_mutation_test.py
```
