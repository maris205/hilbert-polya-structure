# Proof Package: Finite-Memory Divisor Obstruction

## Claim

Let \(G\) be a finite directed multigraph with positive edge roofs,
locally-constant complex weights, and a fixed finite-dimensional unitary
cocycle.  If

\[
D(s)=\det(I-M(s))\not\equiv0,
\]

then \(D\) is a finite exponential polynomial and its zeros satisfy
\(n_D(R)=O(R)\) in \(|s|\le R\), counted with multiplicity.  A finite product
or meromorphic quotient of such determinants cannot have the divisor of the
completed Riemann function up to a zero-free entire factor.

## Status

**PROVED**

## Assumptions

- the graph, memory range, and representation dimension are finite;
- all edge roofs are positive real numbers;
- all weights and cocycles are independent of the Riemann zeros;
- identically zero determinants are excluded.

## Notation

\[
M(s)_{uv}=\sum_{e:u\to v}w_e e^{-s\tau_e}U_e,
\qquad N=|V|d.
\]

Let \(n_D(R)\) count zeros of \(D\) in the closed disk \(|s|\le R\).

## Strategy

1. Expand the finite determinant to obtain a finite exponential polynomial.
2. Bound it by an entire function of exponential type.
3. Apply Jensen's formula about a point where the determinant is nonzero.
4. Compare the resulting linear bound with Riemann–von Mangoldt.

## Dependency Map

The finite expansion uses only the Leibniz determinant formula.  The zero-count
step uses Jensen's formula.  The incompatibility step uses the classical
Riemann–von Mangoldt asymptotic.

## Proof

### Step 1: finite exponential-polynomial form

Every scalar entry of \(M(s)\) is a finite sum of terms
\(c e^{-s\tau_e}\).  The Leibniz expansion

\[
\det(I-M(s))
=\sum_{\pi\in S_N}\operatorname{sgn}(\pi)
\prod_{j=1}^{N}(I-M(s))_{j,\pi(j)}
\]

contains finitely many products.  Distributing those products produces
finitely many terms \(a e^{-\lambda s}\), where \(\lambda\) is a sum of
finitely many edge roofs.  After collecting coincident exponents,

\[
D(s)=\sum_{j=1}^{K}a_j e^{-\lambda_js}.
\]

### Step 2: exponential-type bound

Put \(\Lambda=\max_j\lambda_j\) and \(C=\sum_j|a_j|\).  For every
\(s\in\mathbb C\),

\[
|D(s)|\le
\sum_j|a_j|e^{\lambda_j|\operatorname{Re}s|}
\le C e^{\Lambda|s|}.
\]

Thus \(D\) is entire of exponential type at most \(\Lambda\).

### Step 3: Jensen bound

Because \(D\not\equiv0\), choose \(s_0\) with \(D(s_0)\ne0\), and define
\(F(z)=D(s_0+z)/D(s_0)\).  Jensen's formula applied at radii \(R\) and \(2R\)
implies

\[
n_F(R)\log2
\le \log\max_{|z|=2R}|F(z)|.
\]

The exponential-type bound gives

\[
\log\max_{|z|=2R}|F(z)|
\le \log C-\log|D(s_0)|+\Lambda(|s_0|+2R)
=O(R).
\]

The disk \(|s|\le R\) is contained in
\(|s-s_0|\le R+|s_0|\), so changing the radius by the fixed amount
\(|s_0|\) yields \(n_D(R)=O(R)\).

### Step 4: finite products and quotients

The divisor of a finite product is the sum of the factor divisors; the divisor
of a meromorphic quotient is their difference.  Its total zero and pole
variation in a disk is therefore still \(O(R)\).  Multiplication by
\(e^{g(s)}\), with \(g\) entire, changes no zeros or poles.

### Step 5: contradiction with the completed Riemann divisor

Riemann–von Mangoldt gives

\[
N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}+O(\log T)
\]

for nontrivial zeros with \(0<\operatorname{Im}\rho\le T\).  These zeros lie
in a bounded real strip, so a disk of radius \(R+O(1)\) contains
\(\Theta(R\log R)\) of them.  This exceeds \(O(R)\).  Therefore no determinant
in the stated class, nor a finite product or quotient of them, has the
completed Riemann divisor up to a zero-free entire factor.

Reference for the zero-distribution benchmark:
[NIST DLMF §25.10](https://dlmf.nist.gov/25.10).

## Corrections and Edge Cases

1. The conclusion is not “all finite-alphabet shifts have rational zeta.”
   Infinite-memory Hölder weights lead to an infinite-dimensional operator and
   fall outside the hypotheses.
2. In the commensurable-roof case, \(D=P(e^{-hs})\), so the vertical
   periodicity makes the \(O(R)\) count especially transparent.
3. A nontrivial finite-group sector can cancel a positive leading block.  For
   one vertex, two equal-roof loops labelled by \(0,1\in\mathbb Z/2\), the
   sign character gives
   \[
   M_{\rm sign}(s)=e^{-s\tau}(1-1)=0.
   \]
   The regular representation still contains the trivial sector
   \(2e^{-s\tau}\), and every sector remains within the theorem.

## Open Risks

The theorem deliberately makes no statement about countable graphs,
infinite-dimensional cocycles, or infinite-memory potentials.  Complexity
hidden in such data must pass the arithmetic-origin gate anew; it is not a
free “finite-state escape.”
