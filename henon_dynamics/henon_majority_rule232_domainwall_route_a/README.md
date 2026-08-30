# HCS-C251 — cyclic majority rule 232 and exact wall erosion

This package freezes the synchronous radius-one majority cellular automaton
on every labelled binary cycle (X_n={0,1}^n).  The map is

\[
 (F_nx)_i=\mathbf 1\{x_{i-1}+x_i+x_{i+1}\ge 2\}.
\]

The theorem-scale increment is an exact wall-coordinate reduction.  With
(w_i=x_i\oplus x_{i+1}),

\[
w_i'=w_i(1\oplus w_{i-1}\oplus w_{i+1}).
\]

Every finite block of adjacent walls loses one wall at each end per tick.
Consequently every non-alternating state reaches the fixed language (no
`010` or `101`) in at most $\lfloor(n-1)/2\rfloor$ updates, while for even
$n$ the alternating word and its complement form the unique primitive
period-two orbit.  No other period occurs.  The fixed-state count is closed
for all $n$:

\[
 \#\operatorname{Fix}(F_n)=\operatorname{tr}(M^n)=L_n+2\cos(n\pi/3),
\quad \chi_M(\lambda)=(\lambda^2-\lambda-1)(\lambda^2-\lambda+1).
\]

The parity-twisted run matrices $B_m$ additionally give exact all-$n$
counts of states by transient depth.  Exhaustive receipts cover $n\le14$,
and transfer traces cover the declared $n\le64$ grid.

## Reproduce

```bash
cd henon_dynamics/henon_majority_rule232_domainwall_route_a
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c251_majority_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c251_majority_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c251_majority_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c251_majority_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c251_majority_mutation.py
```

The manuscript is `paper/main.tex`; the release PDF is
`paper/main.pdf`.  `code/c251_release_manifest.py` closes the file and hash
ledger after compilation.

## Boundary

This is a source-local finite-state theorem.  It does not analyze
asynchronous updates, infinite-volume Gibbs measures, target arithmetic,
Euler factors, root numbers, automorphy, target divisors, functional
equations, or a Hilbert--Pólya operator.  The Route-A tuple is
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and Route B is
disabled.
