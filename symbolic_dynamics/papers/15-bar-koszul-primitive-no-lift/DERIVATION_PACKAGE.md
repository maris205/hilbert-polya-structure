# DERIVATION PACKAGE — Koszul Subset Shift and No-Lift Ledger

## 1. From tensor words to squarefree subsets

Paper 14 used every nonempty ordered tensor word.  For a finite atom set
\(A\), the polynomial monoid algebra \(R_A=\Bbbk[x_a:a\in A]\) has a
normalized bar resolution and a smaller Koszul resolution.  The latter has
one exterior basis line \(e_S\) for each subset \(S\subseteq A\), with
homological degree \(|S|\).

Decategorizing that basis by degree suggests the signed inventory

\[
  \mathcal F_A(x)=
  \sum_{\varnothing\ne S\subseteq A}(-1)^{|S|+1}x_S.
\]

The symbolic candidate makes each nonempty subset a return edge of a
one-vertex shift.  This is a well-defined scalar shift, but it has forgotten
the Koszul differential and exterior orientation.  That distinction is
carried through every later calculation.

## 2. Determinant derivation

Inclusion--exclusion gives

\[
  \prod_{a\in A}(1-x_a)
  =1+\sum_{\varnothing\ne S\subseteq A}(-1)^{|S|}x_S
  =1-\mathcal F_A(x).
\]

The scalar adjacency is \(L_A=\mathcal F_A\) on \(\mathbb C\), hence

\[
  D_A(x,z)=1-z\mathcal F_A(x),
  \qquad D_A(x,1)=\prod_{a\in A}(1-x_a).
\]

For all tensor atoms, specialize \(x_{F_p}=e^{-sh(F_p)}=p^{-s}\).  Absolute
summation of the subset alphabet follows from

\[
  \sum_{S\ne\varnothing}|x_S|
  =\prod_p(1+p^{-\sigma})-1,
  \qquad \sigma=\operatorname{Re}s>1.
\]

Therefore

\[
  D_\infty(s,1)=\prod_p(1-p^{-s})=\zeta(s)^{-1}
\]

in the ordinary Euler-product half-plane.  No continuation is produced.

## 3. General squarefree coefficient

The coefficient of the squarefree monomial \(x_1\cdots x_k\) in the
primitive trace-log can be enumerated by cyclic set partitions.  A length
\(m\) word is a set partition into \(m\) nonempty blocks plus a cyclic order.
There are

\[
  (m-1)!\,S(k,m)
\]

such necklaces, where \(S(k,m)\) is a Stirling number of the second kind.
Their scalar sign is

\[
  \prod_{j=1}^m(-1)^{|S_j|+1}=(-1)^{k+m}.
\]

Thus the squarefree coefficient is

\[
  c_k=\sum_{m=1}^k(-1)^{k+m}(m-1)!S(k,m).
\]

Since

\[
  -\log D_A(x,1)=\sum_{a\in A}-\log(1-x_a)
\]

contains no mixed squarefree monomial, \(c_k=0\) for every \(k\ge2\).  This
is an exact scalar identity.  It does not supply an orbitwise matching.

## 4. Why the first apparent pairing is false evidence

For \(A=\{p,q\}\), let \(a=[p]\), \(b=[q]\), and \(c=[pq]\).  At content
\(pq\),

\[
  $[ab]_{+}+[c]_{-}=0$.
\]

This makes a primitive sign involution look plausible.  The next repeated
content separates the ledgers:

\[
\begin{array}{c|c}
\text{primitive at }p^2q^2&\text{sign}\\ \hline
[aabb]&+1\\
[abc]&-1\\
[acb]&-1
\end{array}
\]

The primitive sum is \(-1\).  The imprimitive words \([abab]=[ab]^2\) and
\([cc]=[c]^2\) contribute through the trace-log repetition factors:

\[
  \frac{(+1)^2}{2}+\frac{(-1)^2}{2}=1.
\]

Only the total is zero.  Any pairing that holds the negative sign fixed under
powers computes \(-1/2+1/2=0\) at this layer and therefore changes the frozen
scalar trace.

## 5. Character rather than dimension

At content \(pqr\), scalar dimension again cancels: \(|C_+|=|C_-|=3\).
The \(S_3\) action remembers more.  Positive cycles have orbit type
\(S_3/S_3\sqcup S_3/C_3\); negative cycles have orbit type \(S_3/C_2\).
Hence

\[
  \mathbb C[C_+]\cong 2\mathbf1\oplus\mathrm{sgn},
  \qquad
  \mathbb C[C_-]\cong\mathbf1\oplus\mathrm{Std}.
\]

The virtual residual

\[
  \mathbf1\oplus\mathrm{sgn}-\mathrm{Std}
\]

has dimension zero but character value three on a three-cycle.  Scalar
specialization is therefore the dimension homomorphism that erases the first
nontrivial obstruction.

## 6. Bar, Koszul, and primitive layers

The genuine Koszul resolution does not remove mixed cells.  After tensoring
with the augmentation field, its differential vanishes and

\[
  \operatorname{Tor}^{R_A}_*(\Bbbk,\Bbbk)=\Lambda^*V.
\]

Algebraic discrete Morse theory can reduce the bar resolution to this smaller
complex while preserving homology; it cannot further erase
\(e_p\wedge e_q\) by a quasi-isomorphism.

Nor can one take a chain complex of primitive necklaces first.  Adjacent
multiplication has the two opposite leaks

\[
  [a|b|ab]\longmapsto[ab|ab],
  \qquad
  [a|b|a|b]\longmapsto[ab|a|b],
\]

from primitive to imprimitive and from imprimitive to primitive.

## 7. Scalar versus graded determinant

For a negative scalar edge,

\[
  (-w)^r=(-1)^rw^r.
\]

For an odd chain line,

\[
  \operatorname{Str}(w^r)=-w^r.
\]

At even \(r\), the signs are opposite.  A genuine contractible even/odd pair
with identical operator weight has zero supertrace at every power, so

\[
  \operatorname{sdet}(I-zT)=1.
\]

The scalar two-letter alphabet \(\{+w,-w\}\) reaches a zero aggregate trace
by a different primitive ledger: it contains the mixed length-two primitive
\([+w][-w]\).  Aggregate equality does not identify the two objects.

## 8. Final logical fork

The reduction program has only two honest outcomes.

- Preserve scalar weights and temporal powers: the \(p^2q^2\) and \(S_3\)
  obstructions prevent primitive-natural cancellation.
- Introduce a true chain complex: mixed Koszul/HKR classes remain, or an
  acyclic cancellation sector has graded determinant one.

Either branch blocks an atom-only primitive explanation of the scalar Euler
factor.  A representation-valued determinant that retains the virtual
\(S_k\) character is a new in-family candidate, not a repair of SD-C17.
