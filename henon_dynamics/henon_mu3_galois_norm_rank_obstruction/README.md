# HCS-C45 — Normalized Hénon Galois Norm at the Riemann Critical Abscissa

HCS-C44 proves that the conjugate-paired Hénon moments have unbounded
cyclotomic trace fields.  This project applies the two minimal canonical
rational descents—Galois trace and Galois norm—to the complete local
determinant.

The ordinary norm is rational but has virtual local degree

\[
2(p-1),
\]

so it cannot come from a uniformly bounded-rank graded local operator.  The
normalized logarithmic norm behaves very differently.  If
\(d_p=(p-1)/2\), define on \(|z|<1\)

\[
G_p(z)=\exp\!\left(\frac{1}{d_p}\Log_0 N_p(z)\right).
\]

Then the Euler product

\[
\mathcal G(s)=\prod_{p\equiv1\ (3)}G_p(p^{-s})
\]

is canonically holomorphic and nonzero on

\[
\boxed{\operatorname{Re}s>\tfrac12}.
\]

This is a genuine analytic advance from the C43 half-plane
\(\operatorname{Re}s>1\).  No Riemann zero data or fitted scale enters the
proof: the canonical Euler germ reaches the Riemann critical abscissa from
the right.  This is an abscissa-of-convergence statement.  In the canonical
clock \(z=p^{-s}\), the unit-circle local divisors lie on
\(\operatorname{Re}s=0\), not on the boundary of this convergence theorem.

## Scope

The ordinary norm is a rational determinant.  Its normalized logarithmic
root is an analytic normalized-log Euler germ, not yet an ordinary rational,
Fredholm, or operator-algebraic determinant.  Its local divisor
multiplicities may be fractional after division by \(d_p\), and no functional
equation or continuation across \(\operatorname{Re}s=1/2\) is proved.

## Route-A decision

\[
(\mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
 \mathrm{A4\_NATURAL\_QUANTIZATION}).
\]

Overall: `ROUTE_A_EXPLORATORY`.  Route B is not yet authorized.

## Successor

HCS-C46 tests whether the normalized root is an ordinary rational determinant.
The exact \(p=7\) norm factorization decides the gate by checking whether the
rational norm is a cube and by computing its local branch orders.
