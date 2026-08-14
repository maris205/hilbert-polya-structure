# PROOF PACKAGE — SD-C17

## Status

`PROVABLE AS STATED`, subject to the explicit no-lift axioms in Theorem 9.
No claim is made against every conceivable chain-enhanced symbolic model.

## Assumptions and notation

Let \(A\) be a finite set of at least two tensor atoms.  For
\(\varnothing\ne S\subseteq A\), put

\[
  x_S=\prod_{a\in S}x_a,
  \qquad \epsilon(S)=(-1)^{|S|+1},
  \qquad w(S)=\epsilon(S)x_S.
\]

Words are identified under cyclic rotation only.  A necklace is primitive if
its least cyclic period equals its word length.  Temporal powers use scalar
powers \(w(\gamma)^r\).

## Dependency map

1. The scalar determinant uses finite inclusion--exclusion.
2. The primitive Euler expansion uses unique primitive-root decomposition of
   cyclic words.
3. The first no-lift obstruction uses the exact \(pq\) and \(p^2q^2\)
   ledgers.
4. Naturality failure uses the \(S_3\) fixed character at \(pqr\).
5. Homological failure uses the Koszul computation of Tor, two bar-boundary
   counterexamples, and the supertrace of an acyclic complex.
6. The combined theorem invokes only the preceding finite obstructions.

## Theorem 1 — scalar Koszul determinant

For every finite atom set \(A\),

\[
  \mathcal F_A(x)
  :=\sum_{\varnothing\ne S\subseteq A}(-1)^{|S|+1}x_S
  =1-\prod_{a\in A}(1-x_a).
\]

Consequently the one-vertex weighted adjacency has determinant

\[
  D_A(x,z)=1-z\mathcal F_A(x),
  \qquad D_A(x,1)=\prod_{a\in A}(1-x_a).
\]

### Proof

Expanding the product chooses either \(1\) or \(-x_a\) from each factor.
The term indexed by \(S\) is \((-1)^{|S|}x_S\).  Moving all nonempty terms
to the other side gives the formula.  The determinant is that of the scalar
operator \(\mathcal F_A(x)\) on \(\mathbb C\).  ∎

## Theorem 2 — primitive/repetition expansion

As a formal power series in \(z\),

\[
  -\log(1-z\mathcal F_A)
  =\sum_{\gamma\ \mathrm{primitive}}
    \sum_{r\ge1}\frac{z^{r|\gamma|}w(\gamma)^r}{r}.
\]

### Proof

Expand the left side as
\(\sum_{n\ge1}z^n\mathcal F_A^n/n\).  A based word whose primitive root has
length \(\ell\) and repetition number \(r\) occurs through the \(\ell\)
distinct rotations of that primitive root.  Its total coefficient is
\(\ell/(r\ell)=1/r\).  The edge weights multiply, so its repeated weight is
\(w(\gamma)^r\).  Summing over primitive necklaces gives the formula.  ∎

## Theorem 3 — primitive-power obstruction

Take two atoms \(p,q\) and abbreviate
\(a=\{p\}\), \(b=\{q\}\), \(c=\{p,q\}\).  At content \(pq\), the primitive
necklaces are

\[
  [ab]\quad(+),\qquad [c]\quad(-).
\]

At content \(p^2q^2\), the primitive necklaces are exactly

\[
  [aabb]\quad(+),\qquad [abc]\quad(-),\qquad [acb]\quad(-).
\]

Thus the primitive contribution at \(p^2q^2\) is \(-1\).  The complete
trace-log coefficient is nevertheless zero because the second repetitions of
the two \(pq\) primitives contribute \(1/2+1/2=1\).

### Proof

At content \(p^2q^2\), a word contains either no \(c\), one \(c\), or two
\(c\)'s.  With no \(c\), the cyclic binary word has two \(a\)'s and two
\(b\)'s.  Its necklaces are \([aabb]\), which is primitive, and \([abab]\),
which is \([ab]^2\).  With one \(c\), one \(a\) and one \(b\) remain; the two
cyclic orders \([abc]\) and \([acb]\) are primitive.  With two \(c\)'s, the
word \([cc]=[c]^2\) is imprimitive.  The signs follow by multiplying the
edge signs.  Finally,

\[
  \frac{(+x_px_q)^2}{2}
  +\frac{(-x_px_q)^2}{2}=x_p^2x_q^2.
\]

It cancels the primitive coefficient \(-x_p^2x_q^2\).  ∎

### Corollary 3.1

There is no content-preserving sign-reversing bijection on primitive cycles
that explains the scalar determinant coefficient degree by degree and
commutes with temporal powers.

## Theorem 4 — \(S_3\)-equivariant obstruction

At squarefree content \(pqr\), the positive primitive set is

\[
  C_+=\{[pqr],[p][q][r],[p][r][q]\},
\]

and the negative primitive set is

\[
  C_-=\{[p][qr],[q][pr],[r][pq]\}.
\]

Under atom permutations, their orbit decompositions have sizes \(1+2\) and
\(3\), respectively.  In conjugacy-class order
\((1),(12),(123)\), the virtual fixed character is

\[
  \chi_{C_+}-\chi_{C_-}=(0,0,3)
  =\chi_{\mathbf1}+\chi_{\mathrm{sgn}}-\chi_{\mathrm{Std}}.
\]

Therefore no \(S_3\)-equivariant sign-reversing bijection exists.

### Proof

The one-block partition is fixed by all permutations.  The two cyclic
orientations of three singleton blocks form a two-point orbit: a
transposition exchanges them and a three-cycle acts by cyclic rotation, hence
fixes both necklaces.  The three singleton--pair partitions form the natural
three-point orbit.  Their fixed counts are therefore

\[
  \chi_{C_+}=(3,1,3),\qquad
  \chi_{C_-}=(3,1,0).
\]

An equivariant bijection would give equal fixed counts for every group
element, contradicting the three-cycle count.  Decomposition into the three
irreducible \(S_3\) characters gives the stated virtual representation.  ∎

## Theorem 5 — Koszul homology retains mixed cells

Let \(R_A=\Bbbk[x_a:a\in A]\), let \(\Bbbk\) be the augmentation module, and
let \(V\) have basis \(e_a\).  Then

\[
  \operatorname{Tor}^{R_A}_i(\Bbbk,\Bbbk)
  \cong \Lambda^i_{\Bbbk}V.
\]

In particular, \(e_p\wedge e_q\ne0\) for distinct atoms.  No chain reduction
quasi-isomorphic to the bar resolution can leave only degree-one atom classes.

### Proof

The Koszul complex \(K(R_A;x_a)=R_A\otimes\Lambda V\) is a free resolution of
the augmentation module.  Tensoring it over \(R_A\) with \(\Bbbk\) sends
every \(x_a\) to zero, so the induced differential vanishes.  Its homology is
therefore \(\Lambda V\) in every exterior degree.  Since Tor is invariant
under chain homotopy equivalence, a bar-to-Koszul Morse reduction must retain
these mixed homology classes.  ∎

## Proposition 6 — cyclic primitivity is not a chain layer

The bar multiplication faces do not preserve either primitive or imprimitive
cyclic words.

### Proof

In the monomial bar complex on two generators \(a,b\), the cyclic word
\([a|b|ab]\) is primitive.  The face merging its first two entries is
\([ab|ab]\), which is the square of \([ab]\) and hence imprimitive.
Conversely, \([a|b|a|b]=[a|b]^2\) is imprimitive, while the same merge gives
\([ab|a|b]\), a primitive length-three word.  Thus neither span is stable
under the bar differential, so there is no primitive subcomplex or quotient
obtained by simply deleting repetitions.  ∎

## Proposition 7 — scalar sign is not supertrace parity

For a scalar negative edge of unsigned weight \(w\), repetition \(r\)
contributes \((-w)^r=(-1)^rw^r\).  An odd one-dimensional chain line with
operator \(w\) contributes \(-w^r\) to the supertrace.  They disagree at
every positive even \(r\), already by \(2w^2\) at \(r=2\).

### Proof

This is the direct comparison of the two displayed signs.  ∎

## Theorem 8 — an acyclic equivariant sector is determinant-invisible

Let \((C,d)\) be a finite-dimensional \(\mathbb Z/2\)-graded acyclic complex,
and let \(T\) be an even chain map.  Then for every \(r\ge1\),

\[
  \operatorname{Str}(T^r\mid C)=0.
\]

Consequently its graded Fredholm determinant is

\[
  \operatorname{sdet}(I-zT)
  :=\exp\!\left(-\sum_{r\ge1}
        \frac{z^r}{r}\operatorname{Str}(T^r)\right)=1.
\]

### Proof

Choose a contracting homotopy \(h\) with \(dh+hd=I\).  Because \(T\)
commutes with \(d\),

\[
  T^r=d(T^rh)+(T^rh)d.
\]

The right side is a graded commutator of the odd maps \(d\) and \(T^rh\).
The supertrace of a graded commutator is zero.  The determinant identity
follows term by term.  ∎

## Theorem 9 — primitive-cycle no-lift

There is no reduction of SD-C17 satisfying all of the following:

1. cancellation is local to primitive cyclic content classes;
2. positive and negative scalar primitives are paired or replaced by acyclic
   chain sectors;
3. the reduction commutes with temporal powers and preserves every trace;
4. it is equivariant under finite atom permutations;
5. it deletes all mixed subset classes while retaining nontrivial atom
   determinant factors.

### Proof

If cancellation is a primitive sign pairing, Theorem 3 contradicts (1)--(3)
at \(p^2q^2\), and Theorem 4 independently contradicts (4) at \(pqr\).  If
scalar signs are reinterpreted as chain degrees, Proposition 7 contradicts
trace preservation at the second power.  If mixed sectors are instead made
genuinely acyclic, Theorem 8 makes their graded determinant equal to one;
they cannot secretly supply the nontrivial scalar Euler factor.  Finally,
Theorem 5 shows that a quasi-isomorphic bar-to-Koszul reduction retains mixed
exterior homology, while Proposition 6 prevents taking primitive cycles as a
separate chain layer.  Every permitted form of (2) violates at least one of
(1), (3), (4), or (5).  ∎

## Proposition 10 — universality and arithmetic nonselectivity

The identity in Theorem 1 holds over every commutative coefficient ring and
for every formal inventory \(\{x_a\}\).  It uses no factorization or entropy
property.  Therefore the scalar cancellation alone cannot distinguish tensor
atoms from randomized, composite, or synthetic labels.

This is a `PROVES_TOO_MUCH` obstruction, not evidence against the exact
determinant theorem.

## Open risk and exact boundary

Theorem 9 does not exclude a richer symbolic object whose nontrivial
representation-valued traces retain the \(S_k\) character discarded by
scalar dimension.  Such an object must be frozen as a new candidate.  It
cannot be claimed as a reinterpretation of the scalar subset shift.
