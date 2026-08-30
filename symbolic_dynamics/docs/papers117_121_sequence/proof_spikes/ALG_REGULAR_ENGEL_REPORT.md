# Phase-2b proof spike: a fixed regular Engel map on unitriangular groups

**Status:** theorem package proved; hostile owner gate pending  
**External status:** `HOLD_EXTERNAL`

## System

Let `U_n(q)` be the upper unitriangular group over `F_q`, let `N` be the
regular nilpotent shift, and fix `J=I+N`.  With commutator convention
`[X,J]=X^{-1}J^{-1}XJ`, define

\[
  E(X)=[X,J].
\]

Write `gamma_k` for the lower-central filtration consisting of matrices whose
first `k-1` superdiagonals vanish.  Thus `gamma_1=U_n(q)` and
`gamma_n={I}`.

Generic nilpotence of unitriangular groups, the lower-central filtration,
Engel words, and the centralizer of a regular Jordan block receive zero
credit.  The proposed residual is the exact finite dynamical tree, including
all filtration-sensitive predecessor counts and every transient layer.

## Exact filtration map

For every `1<=k<n`,

\[
  E(\gamma_k)=\gamma_{k+1}
\]

and every target in `gamma_(k+1)` has exactly `q^(n-k)` preimages in
`gamma_k`.

First, `[gamma_k,gamma_1]` lies in `gamma_(k+1)`, so the image inclusion is
automatic.  The kernel is the centralizer of `J` in `gamma_k`.  Since the
full matrix centralizer of one regular Jordan block is `F_q[N]`,

\[
  C_{\gamma_k}(J)
  =\{I+a_kN^k+\cdots+a_{n-1}N^{n-1}\},
\]

which has size `q^(n-k)`.

The fibres of `E|gamma_k` are left cosets of this centralizer.  Indeed,
writing `phi(X)=J^{-1}XJ`, equality
`X_1^{-1}phi(X_1)=X_2^{-1}phi(X_2)` is equivalent to
`X_2X_1^{-1}=phi(X_2X_1^{-1})`.  Hence

\[
 |E(\gamma_k)|
 =\frac{|\gamma_k|}{q^{n-k}}
 =q^{\binom{n-k}{2}}
 =|\gamma_{k+1}|.
\]

The inclusion is therefore equality, and every fibre has the displayed
size.

## Every restricted depth layer

Let

\[
 K_{k,t}=\{X\in\gamma_k:E^t(X)=I\}.
\]

Repeated use of the uniform fibres gives, for `0<=t<=n-k`,

\[
 |K_{k,t}|
 =q^{S_{k,t}},\qquad
 S_{k,t}=\sum_{j=k}^{k+t-1}(n-j),
\]

with the empty sum equal to zero.  Consequently the exact depth-`t` layer in
`gamma_k` is

\[
 \boxed{
 L_{k,0}=1,\qquad
 L_{k,t}=
 (q^{n-k-t+1}-1)
 q^{\sum_{j=k}^{k+t-2}(n-j)}
 \quad(1\le t\le n-k).
 }

In particular, the full phase has maximum depth `n-1`, attained by

\[
  (q-1)q^{\binom n2-1}

\]

states, and the identity is the only recurrent state.

## Full multitype predecessor tree

The map has one rooted functional component.  More precisely, for every
target `Y` and every filtration level `k`,

\[
 \#\{X\in\gamma_k:E(X)=Y\}
 =
 \begin{cases}
 q^{n-k},&Y\in\gamma_{k+1},\\
 0,&Y\notin\gamma_{k+1}.
 \end{cases}

\]

Thus the entire in-tree is determined by the lower-central type of a target,
not merely by its distance from the root.  The layer formula is recovered by
multiplying these type-dependent fibre sizes along the filtration.

## Independent triangular-coordinate route

Write an element of `gamma_k` by its superdiagonal coordinate vectors.
On the first active diagonal, commutation with `J` induces the discrete
difference

\[
  (a_1,\ldots,a_{n-k})
  \longmapsto
  (a_1-a_2,\ldots,a_{n-k-1}-a_{n-k}).

\]

It is onto and has a one-dimensional constant kernel.  Once that diagonal
is chosen, the next target diagonal is the same surjective difference of the
next source diagonal plus a polynomial already determined by lower choices.
Solving successively through the superdiagonals gives one new free constant
at each stage, hence `n-k` free field coordinates and `q^(n-k)` solutions.
This route proves surjectivity and fibre size without orbit--stabilizer or a
matrix-centralizer count.

## Control and owner boundary

`alg_regular_engel.py` exhausts `q=2,n<=6`, `q=3,n<=4`, and `q=5,n<=4`.
For every lower-central restriction it compares the literal image with
`gamma_(k+1)`, checks uniform fibres, exact depth histograms, centralizer
sizes, and filtration increase.  A fresh run passed **103,599 assertions**.

Current primary-source searches found the standard lower-central filtration,
regular-unipotent centralizers, conjugacy-orbit dimension results, Engel/word
map literature, and a 2025--2026 unitriangular automorphism-orbit paper, but
no direct source for this repeated fixed-regular commutator functional tree.
That is only a bounded no-hit.  In particular, Goodwin's regular-unipotent
centralizer/orbit work is a close proof-engine owner and must be subtracted
explicitly.  A hostile gate must decide whether the two-parameter dynamical
tree is a genuine residual or only a mechanical finite-field corollary of
those standard orbit facts.
