# Candidate Registry — SD-C29

## Candidate

**Name:** Möbius incidence atom compiler
**Family:** Symbolic Dynamics
**Status:** exact A1 construction; ordinary-determinant similarity no-go

The candidate starts from the fixed source \(P=(\mathbb N_{\ge1},\mid)\).
For every source coordinate \(n\), it forms

\[
q_n=\zeta\varepsilon_n\mu,
\qquad
q_n(a,b)=\mathbf 1_{a\mid n\mid b}\mu(b/n),
\]

and retains only those \(n\) that cover \(1\). The retained cyclic coefficient
is one on every repetition of one atom and zero on all mixed or
composite-letter words.

## Route

    (A0_ANALYTIC_ARITHMETIC_ORIGIN,
     A1_PASS_ANALYTIC,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

    ROUTE_A_REJECTED
    ROUTE_B_LOCKED

## Positive evidence

- 256/256 source-cover classifications agree with the separated evaluator.
- 900/900 pair products satisfy \(q_nq_m=\delta_{nm}q_n\).
- 1016/1016 cyclic classes pass the exact selector.
- All marker, power-trace, finite Fredholm, and de Rham ratio rows pass.
- \(H_\eta\) trace norms obey the proved uniform bound for \(\eta>1/2\).

## Ceiling

Every finite family is explicitly similar to coordinate idempotents. For
\(\eta>1\), the countable zeta and Möbius transforms are bounded inverses, so
the full family is boundedly similar to a diagonal atom table. Ordinary traces
and determinants see no oblique-incidence information.
