# C99: First-passage generating-polynomial and coefficient spectrum

C99 freezes the twenty C88 first-passage laws as exact integer generating polynomials
`G_i(z)=sum_t N_i(t) z^t`, with probability polynomial `G_i(z)/16!`.  Every row stores all 17 time coefficients and exact probabilities, support minimum/maximum, degree, support gcd, derivatives at `z=1` through order six, and Stirling-number recovery of the C89 ordinary raw moments through order six.

The producer reads frozen C88 and C89 receipts; the independent checker reconstructs every coefficient from C88 hit bitsets and verifies C89 only as an independent moment rebound.  Scope is finite combinatorics under `NO_BAD_EULER_OR_ROOT_NUMBER`.  No arithmetic/local data, Euler factors, root numbers, automorphy, full Burnside ring/table of marks, or Hilbert--Polya operator is claimed.

Run from this directory:

```text
python -B code/c99_generating_polynomial.py
python -B code/c99_generating_polynomial_checker.py
python -B code/c99_sympy_crosscheck.py
python -B code/c99_replay_checker.py
python -B code/c99_mutation_test.py
```
