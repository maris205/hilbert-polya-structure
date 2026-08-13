# HCS-C45 — Normalized Hénon Galois Norm at the Critical Boundary

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
proof.

## Scope

The normalized norm is an analytic determinant germ, not yet an ordinary
rational or Fredholm determinant.  Its local divisor multiplicities may be
fractional after division by \(d_p\), and no functional equation or
continuation across the critical boundary is proved.

## Route-A decision

\[
(\mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
 \mathrm{A4\_NATURAL\_QUANTIZATION}).
\]

Overall: `ROUTE_A_EXPLORATORY_CRITICAL_BOUNDARY_GERM`.  Route B is not yet
authorized.

## Successor

HCS-C46 tests whether the normalized root is the determinant of an ordinary
finite-dimensional local object.  An exact \(p=7\) norm factorization will
decide this by checking whether the rational norm is a cube.

