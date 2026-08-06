# Proof Package

> **Superseded for Paper 7.** This file records the earlier nonmagnetic,
> uncentered proof route.  The authoritative statement is
> `paper/sections/04_quantum_weyl.tex`, Theorem `thm:magnetic-weyl`.  In
> particular, the Paper 7 quantum theorem does not display the classical
> (+1) as a resolved quantum constant.

## Claim

Let \(a\ne0\), let \(n\ge1\) be fixed, and put

\[
 \Psi_{a,n}=H_a^n,
 \qquad H_a(x,y)=(1-ax^2-y,x),
\]

\[
 \mathcal H_{a,n}
 =-\frac12\Delta+2\pi e^{\pi|\Psi_{a,n}(q)|^2}
 \quad\text{on }L^2(\mathbb R^2).
\]

Then its Friedrichs realization is self-adjoint, lower semibounded, and has
compact resolvent.  Its exact classical count is

\[
 \mathcal N_{\rm cl}(E)
 =\frac{E}{2\pi}\log\frac{E}{2\pi}
  -\frac{E}{2\pi}+1,
 \qquad E>2\pi.
\]

Writing \(D=2^n\), its quantum counting function satisfies

\[
 N_{a,n}(E)
 =\frac{E}{2\pi}\log\frac{E}{2\pi}-\frac{E}{2\pi}
 +O_{a,n}\!\left(
 E^{3/4}(\log E)^{1+D/2}\right).
\]

In particular, both growing Riemann--von Mangoldt coefficients survive
quantization for every fixed Hénon iterate.

## Status

**PROVABLE AS STATED.**  The statement deliberately stops at the Q/W gates.

## Assumptions

- \(a\ne0\) and \(n\) are fixed as \(E\to\infty\).
- The operator is the Friedrichs realization of its natural closed quadratic
  form.
- Local square counts use strict inequalities; non-strict global counts are
  recovered by an \(E+1\) squeeze.

## Notation

- \(L=\log(E/2\pi)\), \(R=\sqrt{L/\pi}\), and
  \(\Omega_E=\{q:|\Psi_{a,n}(q)|<R\}\).
- \(N_<(E)\) and \(N_\le(E)\) denote strict and non-strict quantum counts.
- \(Q\) denotes a square of side \(\ell=E^{-1/4}\).
- \(V_Q^-\) and \(V_Q^+\) are the infimum and supremum of the potential on
  \(Q\).

## Proof Strategy

Use area preservation for the exact classical identity.  For the quantum
statement, bound the polynomially warped allowed domain and potential
gradient by powers of \(R\asymp\sqrt{\log E}\), then repeat the
energy-dependent Dirichlet--Neumann square bracketing with the Neumann zero
mode treated by strict counting.

## Dependency Map

1. Polynomial-automorphism lemma gives properness, area preservation, degree,
   boundary length, and gradient bounds.
2. Properness gives confinement and compact resolvent.
3. Area preservation gives the exact classical count.
4. Square lattice counting gives the local kinetic error.
5. Boundary length controls the number of relevant squares.
6. The gradient bound controls the Riemann-sum potential gap.
7. Strict/non-strict squeezing transfers the result to the stated convention.

## Proof

### Step 1 — polynomial-automorphism geometry

The Jacobian matrix of \(H_a\) is

\[
 DH_a(x,y)=
 \begin{pmatrix}-2ax&-1\\1&0\end{pmatrix},
 \qquad \det DH_a=1,
\]

and

\[
 H_a^{-1}(u,v)=(v,1-av^2-u).
\]

Thus \(H_a\), and hence every fixed iterate \(\Psi_{a,n}\), is a proper
area-preserving polynomial automorphism.  Both \(\Psi_{a,n}\) and its inverse
have degree \(D=2^n\).

Parametrize \(\partial\Omega_E\) by

\[
 q(\theta)=\Psi_{a,n}^{-1}(R\cos\theta,R\sin\theta).
\]

The derivative of the degree-\(D\) polynomial inverse is
\(O_{a,n}((1+R)^{D-1})\) on \(B_R\).  Therefore

\[
 \operatorname{length}(\partial\Omega_E)
 \le C_{a,n}(1+R)^D
 =O_{a,n}(L^{D/2}).
\]

For \(\Phi(q)=\pi|\Psi_{a,n}(q)|^2\),

\[
 \nabla\Phi(q)=2\pi D\Psi_{a,n}(q)^T\Psi_{a,n}(q).
\]

At \(q=\Psi_{a,n}^{-1}(u)\), the matrix
\(D\Psi_{a,n}(q)\) is the inverse of
\(D\Psi_{a,n}^{-1}(u)\).  Every two-dimensional matrix here has determinant
one, so its inverse norm is bounded by a fixed multiple of its norm.  Hence,
for \(|u|\le R+1\),

\[
 |\nabla\Phi(\Psi_{a,n}^{-1}u)|
 \le C_{a,n}(1+R)^D.
\]

### Step 2 — self-adjointness and compactness

Properness of \(\Psi_{a,n}\) implies \(V_{a,n}(q)\to\infty\) as
\(|q|\to\infty\).  The form

\[
 q_{a,n}[u]=\frac12\|\nabla u\|_2^2
 +\int V_{a,n}|u|^2
\]

on \(H^1(\mathbb R^2)\cap L^2(V_{a,n}dq)\) is densely defined, closed, and
lower semibounded.  The Friedrichs theorem gives a self-adjoint realization.
Confinement plus Rellich compactness on bounded sets makes the form-domain
embedding into \(L^2\) compact, hence the resolvent is compact.

### Step 3 — exact classical count

Because \(\det D\Psi_{a,n}=1\), the change of variables
\(u=\Psi_{a,n}(q)\) gives

\[
\begin{aligned}
 \mathcal N_{\rm cl}(E)
 &=\frac1{2\pi}\int
 \bigl(E-2\pi e^{\pi|\Psi_{a,n}(q)|^2}\bigr)_+dq\\
 &=\frac1{2\pi}\int_{|u|<R}
 \bigl(E-2\pi e^{\pi|u|^2}\bigr)du\\
 &=\frac{E}{2\pi}\log\frac{E}{2\pi}
 -\frac{E}{2\pi}+1.
\end{aligned}
\]

### Step 4 — local square counts

Tile \(\mathbb R^2\) by squares of side \(\ell=E^{-1/4}\).  For \(A>0\),
the strict Dirichlet and Neumann counts of \(-\Delta/2\) on one square obey

\[
 n_{D/N}(A)=\frac{\ell^2A}{2\pi}
 +O(\ell\sqrt A+1).
\]

For \(A\le0\), define both local counts to be zero.  This convention is
essential for the Neumann zero mode.

Dirichlet--Neumann form bracketing and the potential extrema give

\[
 \sum_Q n_D(E-V_Q^+)
 \le N_<(E)
 \le \sum_Q n_N(E-V_Q^-).
\]

Only squares with \(V_Q^-<E\) enter the upper sum.

### Step 5 — number of relevant squares

The union of relevant squares lies in an \(O(\ell)\) neighborhood of
\(\Omega_E\).  Its square count is bounded by

\[
 M(E)=O_{a,n}\!\left(
 \frac{L}{\ell^2}+
 \frac{L^{D/2}}{\ell}+1\right).
\]

The total local lattice error is therefore

\[
\begin{aligned}
 O\bigl(M(E)(\ell\sqrt E+1)\bigr)
 =O_{a,n}\bigl(&E^{3/4}L+E^{1/2}L\\
                &+E^{1/2}L^{D/2}+E^{1/4}L^{D/2}\bigr).
\end{aligned}
\]

This is bounded by
\(O_{a,n}(E^{3/4}L^{1+D/2})\).

### Step 6 — potential oscillation

We first justify that Step 1 applies uniformly on the whole relevant-square
union, rather than only on \(\Omega_E\).  Let \(q_0\in Q\cap\Omega_E\), let
\(q\in Q\), and follow the segment \(q_t=q_0+t(q-q_0)\).  Suppose, for a
contradiction, that \(u_t=\Psi_{a,n}(q_t)\) first exits \(B_{R+1}\).  Up to
that first-exit time, the inverse-polynomial estimate and the determinant-one
identity give

\[
 \|D\Psi_{a,n}(q_t)\|
 \le C_{a,n}(1+R)^{D-1}.
\]

Consequently

\[
 |u_t-u_0|
 \le C_{a,n}\ell(1+R)^{D-1}=o(1),
\]

whereas traveling from \(|u_0|<R\) to \(|u_t|=R+1\) requires a displacement
larger than one.  This contradiction proves that every relevant square maps
into \(B_{R+1}\) for all sufficiently large \(E\).  The argument uses fixed
\(D\), equivalently fixed \(n\).

On the relevant-square union, Step 1 and
\(V=2\pi e^\Phi\) give

\[
 \sup|\nabla V|
 \le C_{a,n}E L^{D/2}
\]

for sufficiently large \(E\); the extra exponential produced by moving a
distance \(O(\ell)\) is bounded because
\(\ell L^{D/2}\to0\).  Hence each relevant square has oscillation

\[
 V_Q^+-V_Q^-
 \le C_{a,n}E\ell L^{D/2}.
\]

The relevant-square union has area
\(O_{a,n}(L+\ell L^{D/2})=O_{a,n}(L)\).  Thus the gap between either principal
Riemann sum and the exact phase integral is

\[
 O_{a,n}(E\ell L^{1+D/2})
 =O_{a,n}(E^{3/4}L^{1+D/2}).
\]

Combining Steps 4--6 proves the stated estimate for \(N_<(E)\).

### Step 7 — non-strict count

The eigenvalues are discrete and

\[
 N_<(E)\le N_\le(E)\le N_<(E+1).
\]

Changing the smooth classical count from \(E\) to \(E+1\) costs
\(O(\log E)\), which is absorbed by the proved remainder.  Therefore the same
estimate holds for \(N_\le(E)\).  This proves the claim. \(\square\)

## Corrections or Missing Assumptions

- The iterate \(n\) cannot grow with \(E\) under this proof without a separate
  distortion analysis.
- The displayed logarithmic power is a safe bracketing envelope, not claimed
  optimal.
- An independent audit checked the polynomial-degree, boundary-length,
  determinant-one gradient, grid-counting, strict-count, and first-exit
  estimates.  The first-exit paragraph above is the resulting proof repair.

## Open Risks

- Publication still requires normal referee-level checking even though the
  internal independent proof audit found no remaining mathematical gap.
- The theorem says nothing about classical entropy or quantum spacing.
- A prime-power trace mechanism remains completely open.
