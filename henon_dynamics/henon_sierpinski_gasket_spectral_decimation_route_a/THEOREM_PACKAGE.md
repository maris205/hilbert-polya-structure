# C184 theorem package: finite-gasket spectral decimation

## 1. Frozen object and conventions

Let \(V_0=\{q_0,q_1,q_2\}\).  Recursively, \(V_m\) is the vertex set of the
level-\(m\) Sierpiński pre-gasket, with vertices joined when they are
endpoints of a level-\(m\) cell edge.  The full vertex count is

\[
|V_m|=\frac{3^{m+1}+3}{2}.
\]

Dirichlet values vanish on \(V_0\).  On the interior
\(V_m^\circ=V_m\setminus V_0\), define the standard unnormalized graph
Laplacian

\[
(L_m f)(x)=\sum_{y\sim_m x}(f(x)-f(y)).
\]

Boundary neighbors occur in this sum with value zero.  Thus the matrix is
obtained from the full graph Laplacian by deleting the three boundary rows
and columns, not by recomputing degrees after deletion.  Every interior
diagonal entry is 4, and

\[
N_m:=\dim L_m=\frac{3^{m+1}-3}{2}.
\]

Write \(\chi_m(t)=\det(tI-L_m)\).  All eigenvalues are positive.  The heat
trace and finite spectral zeta are

\[
H_m(u)=\operatorname{Tr}(e^{-uL_m}),\qquad
\zeta_m(s)=\sum_{\lambda\in\operatorname{Spec}(L_m)}
\operatorname{mult}_m(\lambda)\lambda^{-s},
\]

where the ordinary real logarithm defines \(\lambda^{-s}\).  This
\(\zeta_m\) is a finite entire exponential sum; it is not the spectral zeta
of the limiting infinite gasket.

## 2. The complete spectral-decimation theorem

Define

\[
R(t)=t(5-t),\qquad
\phi_\pm(u)=\frac{5\pm\sqrt{25-4u}}2.
\]

For every \(m\ge1\), the spectrum of \(L_m\), with multiplicity, is the
disjoint lineage ledger below.

| series | birth generation \(j\) | seed | birth multiplicity | continuation to level \(m\) |
|---|---:|---:|---:|---|
| 2-series | \(j=1\) | 2 | 1 | every word of length \(m-1\) in \(\phi_-,\phi_+\) |
| 5-series | \(j\ge1\) | 5 | \(a_j=(3^{j-1}+3)/2\) | every word of length \(m-j\) |
| 6-series | \(j\ge2\) | 6 | \(b_j=(3^j-3)/2\) | if \(m=j\), seed 6; otherwise first \(6\mapsto3\), then every word of length \(m-j-1\) |

The special step in the last row is essential.  The two algebraic preimages
of 6 are 2 and 3, but 2 is exceptional and inadmissible as this continuation;
only 3 survives.  After 3, both inverse branches resume.

### Local elimination proof

Consider one old level-\(m\) cell with values \(x_0,x_1,x_2\) at its
corners and let \(y_{01},y_{02},y_{12}\) be the three new midpoint values.
Solving the three midpoint eigenvalue equations for a nonexceptional
fine-level eigenvalue \(\lambda\) gives, cyclically,

\[
y_{01}=
\frac{(4-\lambda)(x_0+x_1)+2x_2}
{(2-\lambda)(5-\lambda)}.
\]

Substituting these values into the old-vertex equations yields

\[
L_m(x_0,x_1,x_2)=R(\lambda)(x_0,x_1,x_2).
\]

Conversely, when \(\lambda\notin\{2,5,6\}\), this formula uniquely extends
an eigenfunction of \(L_m\) with eigenvalue \(R(\lambda)\).  Hence ordinary
eigenfunctions lift along both roots of \(R(t)=u\).  At the singular values,
the local system has kernels supported on new cell and cycle degrees of
freedom.  Row reduction of the cell-edge incidence system gives:

- one level-1 mode at eigenvalue 2;
- a level-\(j\) eigenspace of new 5-modes of dimension
  \(a_j=(3^{j-1}+3)/2\), for every \(j\ge1\);
- a level-\(j\) eigenspace of new 6-modes of dimension
  \(b_j=(3^j-3)/2\), for every \(j\ge2\).

For a 6-mode the restriction to the coarser graph is zero.  At the next
level, \(R(t)=6\) factors as

\[
R(t)-6=-(t-2)(t-3).
\]

The singular 2-root is not an extension of that old 6-eigenspace; the
3-root is.  This proves the forced step.  These local elimination and kernel
counts are the finite-graph spectral-decimation argument of Fukushima and
Shima; the source attribution is not a novelty claim.

### Completeness and dimension

At level \(m\), the weighted populations are

\[
S_m=2^{m-1}
+\sum_{j=1}^{m}2^{m-j}a_j
+b_m+\sum_{j=2}^{m-1}2^{m-j-1}b_j.
\]

The last sum is empty for \(m\le2\).  Directly \(S_1=3=N_1\).  For
\(m\ge2\), doubling the old lineages would incorrectly double the old
6-series; correcting its forced single branch and adding the new births
gives

\[
S_m=2S_{m-1}-b_{m-1}+a_m+b_m.
\]

Substitution of the displayed \(a_m,b_m\) and the induction hypothesis gives

\[
S_m=2N_{m-1}-b_{m-1}+a_m+b_m
=\frac{3^{m+1}-3}{2}=N_m.
\]

Thus the ledger contains exactly the matrix dimension and is complete.

## 3. Characteristic polynomial and determinant

The base polynomial is

\[
\chi_1(t)=(t-2)(t-5)^2.
\]

For \(m\ge2\), with \(b_1=0\),

\[
\boxed{\chi_m(t)=(-1)^{N_{m-1}}(t-5)^{a_m}(t-6)^{b_m}
\frac{\chi_{m-1}(R(t))}{(t-2)^{b_{m-1}}}.}
\]

Indeed, for every old eigenvalue other than 6, the two factors associated
with its inverse images multiply to \(-[R(t)-u]\).  For every old 6-mode,
division by \(t-2\) removes the forbidden root and leaves the allowed factor
\(t-3\).  Exact divisibility follows from
\(R(t)-6=-(t-2)(t-3)\).  The sign makes the result monic, and the new 5- and
6-births supply the remaining factors.

Let \(D_m=\det L_m\).  Evaluation at \(t=0\), with the base value
\(D_1=2\cdot5^2\), gives

\[
D_m=5^{a_m}6^{b_m}\frac{D_{m-1}}{2^{b_{m-1}}}.
\]

Writing the prime exponents separately and summing their elementary
geometric recurrences yields

\[
\boxed{D_m=
2^{(3^m-1)/2}
3^{(3^{m+1}-6m-3)/4}
5^{(3^m+6m-1)/4}.}
\]

The exponents are nonnegative integers for every \(m\ge1\); the base case
and recurrence prove the formula without finite diagonalization.

## 4. Heat trace and finite spectral zeta

Let \(\mathcal L_m\) be the complete lineage set above and let
\(q(\ell)\) be the birth multiplicity.  Then, exactly,

\[
H_m(u)=\sum_{\ell\in\mathcal L_m}q(\ell)e^{-u\lambda_\ell},
\qquad
\zeta_m(s)=\sum_{\ell\in\mathcal L_m}q(\ell)
e^{-s\log\lambda_\ell}.
\]

Dimension closure gives \(H_m(0)=\zeta_m(0)=N_m\).  Since every interior
diagonal entry of \(L_m\) is 4,

\[
-H'_m(0)=\operatorname{Tr}L_m=4N_m.
\]

Finally,

\[
\exp[-\zeta'_m(0)]
=\prod_{\ell\in\mathcal L_m}\lambda_\ell^{q(\ell)}
=\det L_m.
\]

These are ordinary finite-dimensional identities.  They neither choose an
infinite-level normalization nor establish a target functional equation,
Gamma factor, divisor, or Weil formula.

## 5. Refinement clock, Route A, and boundaries

A branch word records passage from \(L_j\) to \(L_m\).  The ambient graph
and Hilbert space change with the level.  Therefore the word is not the orbit
of one autonomous physical-time map on a frozen phase space, and its length
is not an admissible arithmetic clock.  Each finite \(L_m\) is self-adjoint,
so \(e^{-iuL_m}\) is a canonical finite unitary group, but its real time
\(u\) is not the refinement level and supplies no target operator.

The strict evaluation is

\[
(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},
\mathrm{PARTIAL\ ANALYTIC\ STRUCTURE},\mathrm{FORMAL\ HINT}).
\]

A0 failure forces overall `ROUTE_A_REJECTED`; Route B is false.

Boundary cases and nonclaims:

- Level \(m=0\) has no interior Dirichlet degrees of freedom and is outside
  the frozen \(m\ge1\) theorem.
- The three corners are removed from the matrix, but their edges still
  contribute to interior degree 4.
- The 6-series born at the terminal level remains at 6; a continued
  6-series first takes 3 and only then branches twice.
- Numerical diagonalization through level five is regression only.
- No infinite-gasket spectral-zeta or regularized-determinant theorem is
  claimed.
- No rational-prime origin, target divisor, target functional equation,
  Hilbert--Polya operator, Route-B authorization, external peer review, or
  literature-wide novelty certificate is claimed.
- Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.
