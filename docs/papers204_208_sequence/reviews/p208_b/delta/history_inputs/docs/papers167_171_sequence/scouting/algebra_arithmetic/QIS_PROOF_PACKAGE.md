# Quartic inverse-span dynamics: proof package

This file separates elementary derivations from the one direct external
classification theorem.  It is suitable for proof audit, not yet for a paper.

## External input, stated exactly at the needed strength

**Inverse-image subspace classification (Kolomeec--Bykov).**  Let `p` be
prime and let `L` be an affine `F_p`-subspace of a finite field.  Patch
inversion by `iota(0)=0`.  If `|L|>2`, then `iota(L)` is an affine subspace if
and only if `L=xi F_{p^k}` for a subfield `F_{p^k}` of the ambient field and a
nonzero scalar `xi`.

Only the linear special case inside `F_{p^4}` is used below.  The source is
N. Kolomeec and D. Bykov, *On the image of an affine subspace under the inverse
function within a finite field*, arXiv:2206.14980 (2022).

## Lemma 1: monotonicity and equality

For every `F_p`-subspace `A <= K`,

\[
 \dim\mathcal J(A)\ge\dim A.
\]

If equality holds, then `J^2(A)=A`.

**Proof.**  Put `d=dim A` and `r=dim J(A)`.  The set of inverse points has
`p^d-1` elements and lies among the `p^r-1` nonzero elements of `J(A)`, so
`r>=d`.  Under equality, these finite sets have the same size, hence
`J(A)=A^{-1} union {0}`.  Applying patched inversion to this set returns `A`,
and its span is `A`.  QED.

## Lemma 2: recurrent-state criterion

A state is recurrent if and only if equality holds in Lemma 1.  Every
recurrent period is one or two.

**Proof.**  Along every forward orbit, dimensions are nondecreasing.  A
periodic orbit must return to its initial dimension, so equality holds at its
first edge.  Lemma 1 then gives `J^2(A)=A`.  Conversely, that identity makes
`A` recurrent with period dividing two.  QED.

## Lemma 3: equality cases

The recurrent states are precisely

\[
 0,\quad K,\quad \xi\mathbb F_p,\quad \xi\mathbb F_{p^2}
 \qquad(\xi\in K^\times).
\]

**Proof.**  Zero is fixed.  Every line has the displayed scalar-subfield form
and maps to its inverse scalar line.  Suppose `dim A=d>=2` and equality holds.
The cardinality argument in Lemma 1 says that patched inversion maps `A`
itself onto the linear subspace `J(A)`.  Apply the external classification:
`A=xi F_{p^k}` with `k|4`.  Its `F_p`-dimension is `k`, so the proper cases
are `k=1,2`; `k=4` is `K`.  Conversely each displayed state maps to the same
kind of state with scalar `xi^{-1}`.  QED.

## Lemma 4: inverse span of a plane

If `A` is a plane, then

\[
 \dim\mathcal J(A)=
 \begin{cases}
 2,&A=\xi\mathbb F_{p^2},\\
 3,&A\ne\xi\mathbb F_{p^2}\text{ and }p=2,\\
 4,&A\ne\xi\mathbb F_{p^2}\text{ and }p>2.
 \end{cases}
\]

**Proof.**  Scale `A` as `xi <1,alpha>`.  Scaling does not change the image
dimension.  Since `alpha` is in `F_{p^4}` but not `F_p`, its degree `r` over
`F_p` is two or four.

The `p+1` projective points of the plane have representatives `1` and
`alpha-t`, `t in F_p`.  Their inverse projective representatives are therefore

\[
 1,\quad(\alpha-t)^{-1}\quad(t\in\mathbb F_p).
\]

Choose distinct `t_1,...,t_s` and suppose

\[
 c_0+\sum_{i=1}^s{c_i\over\alpha-t_i}=0,
 \qquad s+1\le r.
\]

Multiplication by `D(alpha)=prod_i(alpha-t_i)` produces `P(alpha)=0` for a
polynomial `P` of degree at most `s<r`.  Minimality of the degree of `alpha`
forces `P=0`.  Evaluating the polynomial identity at each `t_i` gives
`c_i prod_{j!=i}(t_i-t_j)=0`, so every `c_i=0`, and then `c_0=0`.  Hence the
span dimension is `min(r,p+1)`.

For `r=2`, `<1,alpha>=F_{p^2}`.  For `r=4`, the minimum is three at `p=2` and
four at every odd prime.  Restoring the scalar `xi` proves the claim.  QED.

## Lemma 5: the transition table and sharp height

Every hyperplane maps to `K`.  A non-subfield plane maps to a hyperplane at
`p=2` and to `K` at odd `p`.  Therefore the maximum tail is exactly two for
`p=2` and exactly one for odd `p`.

**Proof.**  A hyperplane has dimension three.  Lemma 1 leaves image dimension
three or four; Lemma 3 rules out equality at three, so the image is `K`.
Lemma 4 handles planes.  Lines, scaled quadratic-field planes, zero, and `K`
are recurrent by Lemma 3.  Non-subfield planes exist because
`[4 choose 2]_p-(p^2+1)>0`, so the asserted upper bounds are attained.  QED.

## Lemma 6: recurrent and cycle counts

Let

\[
 L=p^3+p^2+p+1,\quad P=(p^2+1)(p^2+p+1),\quad Q=p^2+1.
\]

Then the number of recurrent states is `R=2+L+Q`, the number of fixed points
is

\[
 F=2+\gcd(2,L)+\gcd(2,Q),
\]

and there are `(R-F)/2` two-cycles.

**Proof.**  Gaussian coefficients count `L` lines.  Scalar quadratic-field
planes are cosets in `K^x/F_{p^2}^x`, so there are `Q`.  Add zero and `K`.

On lines, `J` induces inversion on the cyclic group `K^x/F_p^x` of order
`L`; on quadratic planes it induces inversion on the cyclic quotient of order
`Q`.  In a cyclic group of order `m`, inversion fixes exactly `gcd(2,m)`
elements.  Add the fixed states zero and `K`.  Lemma 2 excludes longer cycles.
QED.

## Lemma 7: binary hyperplane fibres

At `p=2`, every hyperplane has exactly two non-subfield plane predecessors.

**Proof.**  Lemma 4 maps all `P-Q=30` non-subfield planes to hyperplanes.
For every nonzero scalar `lambda`, direct substitution gives

\[
 \mathcal J(\lambda A)=\lambda^{-1}\mathcal J(A).
\]

The multiplicative Singer group is transitive on hyperplanes.  Explicitly,
nondegeneracy of the trace pairing writes each hyperplane as
`H_c={x:Tr(cx)=0}`, with `c` unique modulo `F_2^x`; scalar multiplication sends
these kernels transitively to one another.  Twisted equivariance therefore
makes all hyperplane fibre sizes equal.  Their sum is 30 over 15 hyperplanes,
so each size is two.  QED.

## Theorem: exact graph, zeta, and all-time fibres

The rank transition table, depth enumerators, image stabilization, cycle
counts, zeta function, and target-fibre formulas in
`QIS_DERIVATION_PACKAGE.md` all hold.

**Proof.**  Lemmas 3--5 partition every state by rank and equality type, giving
the transition table and depth enumerator.  Lemma 6 gives the periodic core;
the standard cycle product yields
`zeta(z)=(1-z)^(-F)(1-z^2)^(-(R-F)/2)`.

For fibres, rank monotonicity says that a recurrent line or recurrent proper
plane can only have a same-rank predecessor; equality then forces that
predecessor into the recurrent involution, where it is unique.  A
non-subfield plane has no predecessor for the same reason.  Odd-characteristic
hyperplanes have none because no transition class lands there.  Lemma 7 gives
the sole exceptional proper fibre.  Finally, `K` receives itself and all
hyperplanes at one step, plus all non-subfield planes immediately for odd `p`
or after two steps for `p=2`.  Once the periodic core is reached, later fibre
counts are unchanged.  This is exactly the atlas stated in the derivation
package.  QED.

## Proof audit status

- Elementary steps independently derived here: monotonicity, equality implies
  involution, rational-function independence, plane rank, Gaussian/cyclic
  counts, twisted scalar symmetry, uniform binary fibres, graph synthesis.
- External theorem used essentially: equality-case classification for patched
  inversion of a subspace.
- Machine audit: exhaustive for `p=2,3,5`, 32,754 explicit assertions plus a
  pinned SHA-256 digest of every directed edge in each graph.
- Remaining risk is ownership/positioning, not an observed mathematical gap.
