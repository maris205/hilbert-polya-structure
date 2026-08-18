# Research Question Brief — Paper 46

## Narrow question

For the countable arithmetic graph on positive integers with an edge exactly
when the two endpoints sum to a power of two, what are the exact boundedness,
compactness, Hilbert--Schmidt, and trace-class thresholds of the canonical
Dirichlet-weighted adjacency operator, and how do its closed walks decompose
under the frozen unit edge clock?

## Frozen answer

For

$$
H_s(m,n)=\mathbf 1_{\{m+n=2^a\text{ for some }a\ge1\}}(mn)^{-s/2},
\qquad \sigma=\Re s,
$$

on $\ell^2(\mathbb N)$,

$$
H_s\text{ is bounded and compact}\iff \sigma>0,
$$

$$
H_s\in S_2\iff \sigma>\frac12,
\qquad
H_s\in S_1\iff \sigma>1.
$$

Every edge preserves the $2$-adic valuation.  On odd vertices let $A_s$ be
the same weighted adjacency.  Then

$$
H_s\cong\bigoplus_{k\ge0}2^{-ks}A_s.
$$

For a cyclic edge-label tuple $q_i=2^{a_i}$, the equations
$n_i+n_{i+1}=q_i$ have one candidate solution when the cycle length is odd;
when the length is even they are solvable exactly when the alternating label
sum vanishes, after which one integer parameter remains subject to explicit
positivity constraints.  This yields an independent trace-power evaluator.

## Why this is a paper-sized question

Generic Hankel and Schur methods can bound a lacunary matrix, and finite graph
literature can solve selected power-of-two edge systems.  Neither input owns
the combined canonical infinite operator, all three strict ideal walls, the
$v_2$ orthogonal self-similarity, and the complete odd/even cyclic solver.
The central theorem is the arithmetic operator/cycle package, not the generic
notion of a Hankel operator or regularized determinant.

## Explicit non-goals

- no all-$S_q$ theorem beyond the proved $q=1,2$ cases;
- no novelty claim for Peller's Hankel--Besov theory, Schur tests, or general
  trace ideals;
- no novelty claim for finite unweighted Hankel determinants or generic
  graph-label equation solvers;
- no rational-prime primitive identification;
- no Riemann-zero fit, completed zeta, functional equation, or
  Hilbert--Polya operator;
- no inference from finite cutoffs to an endpoint without a proof;
- no authority, Route, Git, README, or mirror authorization.

## Status

`PROVABLE AS STATED / PREAUTHORITY THEORY INPUT`

