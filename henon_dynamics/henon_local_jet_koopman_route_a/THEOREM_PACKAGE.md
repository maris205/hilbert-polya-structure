# Exact theorem package — C114

Let \(\mathfrak m=(u,v)\), let
\(A_4=\mathbb Q[u,v]/\mathfrak m^5\), and order its basis by total degree as

\[
1;\ u,v;\ u^2,uv,v^2;\ u^3,u^2v,uv^2,v^3;
u^4,u^3v,u^2v^2,uv^3,v^4.
\]

For \(F(u,v)=(u^2+3u/2-v/2,u)\), define
\(K[p]=[p\circ F]\) in \(A_4\).

## Proposition 1 — finite pullback

Because \(F(0)=0\), pullback maps \(\mathfrak m^5\) into itself.  Thus \(K\)
is a well-defined 15-dimensional rational operator.  Its exact matrix is the
one stored in the canonical evidence; columns are images of basis elements.

## Proposition 2 — associated-graded blocks

The total-degree filtration is invariant.  On degree \(d\), the induced block
is the degree-\(d\) pullback of

\[
L(u,v)=(3u/2-v/2,u),
\]

whose eigenvalues are \(1\) and \(1/2\).  Hence the degree-\(d\) block has
eigenvalues \(1,1/2,\ldots,2^{-d}\), trace
\((2^{d+1}-1)/2^d\), and determinant
\(2^{-d(d+1)/2}\), for \(0\le d\le4\).

## Corollary — exact finite spectral data

Across all five blocks, eigenvalue \(2^{-k}\) has multiplicity \(5-k\).
Consequently

\[
\chi_K(\lambda)=\prod_{k=0}^{4}(\lambda-2^{-k})^{5-k},
\qquad
\det(I-zK)=\prod_{k=0}^{4}(1-2^{-k}z)^{5-k}.
\]

In particular, \(\operatorname{tr}K=129/16\) and
\(\det K=2^{-20}=1/1048576\).  More generally,

\[
\operatorname{tr}(K^n)=\sum_{k=0}^{4}(5-k)2^{-kn},\qquad 1\le n\le8,
\]

and all eight rational values are recorded in the evidence.

## Nonlinear-control statement

The full jet matrix differs from the linearized pullback matrix in eleven
entries.  Their difference is strictly degree raising and has nilpotence
index four.  The matrices therefore have identical diagonal graded blocks
and characteristic polynomials, while remaining distinct operators.

These statements concern only \(A_4\).  They do not establish a global
function-space owner, nuclearity, a Fredholm determinant, a global spectrum,
or any arithmetic or Route-B claim.
