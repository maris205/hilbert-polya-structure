# HCS-C56 proof package

## Claim

For the fixed HCS-C55 cubic surface $Y/\mathbf Q$, prove that its Fano scheme
of lines is $\operatorname{Spec}(E)$ for a degree-$27$ number field $E$, that
the normal closure $K$ of $E$ has
$\operatorname{Gal}(K/\mathbf Q)\cong W(E_6)$ of order $51840$, that the
geometric and arithmetic Picard ranks are $7$ and $1$, and that no
$\mathbf Q$-line exists (with $27\mid[L:\mathbf Q]$ for every finite extension
$L/\mathbf Q$ over which a line is defined).

## Status

**DOCS_FINAL_NO_MORE_EDITS: H0--H6 are exact certified premises and the proof
belongs to the project RELEASE_FROZEN.**

The current producer and independent checker certify the exact instance data
H0--H6 below.  This file supplies the written geometric, Galois, and
Hochschild--Serre implications from those data.  Release/compilation
provenance is recorded externally and is not a mathematical assumption.

## Certified exact premises

- **H0 (fixed smooth surface).** The C55 released cubic (1.1) is imported from
  the frozen C55 theorem/certificate/Route identity and is smooth over
  $\mathbf Q$.
- **H1 (direct chart morphism).** There are exact data
  $g,h_a,h_b,h_c,\lambda_a,\lambda_b,\lambda_c$ satisfying
  (2.4)--(2.5) of `THEOREM_PACKAGE.md`, and direct substitution makes the four
  restricted line equations vanish modulo $g$.
- **H2 (irreducibility witnesses).** The complete modular factorizations at
  $7,19,29,37$ are squarefree, multiply back, preserve degree, have the listed
  factor-degree multisets, and have subset-sum intersection $\{0,27\}$.
- **H3 (chart convention replay).** The five complementary chart systems with
  $p_{01}=0$ are unit ideals.  This is an independent coverage guard.
- **H4 (incidence-compatible Galois action).** The splitting field action on
  the 27 reconstructed lines preserves their intersection graph, as it must
  for lines on a cubic surface; the exact line reconstruction uses the same
  roots and chart convention as H1.
- **H5 (odd-class witness).** The factorization at $37$ produces cycle type
  $(2,5,5,5,10)$.  Exact enumeration finds 5184 elements of this type in
  $W(E_6)$, all outside the index-two subgroup $U$, and none inside $U$.
- **H6 (Picard lattice replay).** The explicit reflection model has order
  $51840$, its even kernel has order $25920$, and its fixed subspace on the
  rank-seven Picard lattice has dimension one.

## Notation

- $F_1(Y)$: the Fano scheme of lines, defined as the zero scheme of
  $\sigma_F$ on $\operatorname{Gr}(2,4)$.
- $E=\mathbf Q[d]/(g)$: the residue field of the connected line scheme.
- $K$: the splitting field of $g$, equivalently the normal closure of $E$.
- $G=\operatorname{Gal}(K/\mathbf Q)$.
- $W=W(E_6)$: the Weyl group acting faithfully on the 27 line classes.
- $U\subset W$: the index-two Coxeter-even subgroup.  This parity is not the
  ordinary sign of the 27-point permutation.

## Proof strategy

1. Use the classical 27-line theorem and simple-zero theorem to obtain a
   global finite étale scheme of rank 27.
2. Use H1--H2 to insert the connected rank-27 scheme
   $\operatorname{Spec}(E)$ as a closed subscheme; equal rank forces equality.
3. Use modular Frobenius, transitivity, and Elsenhans--Jahnel Lemma 8 to prove
   $G=W(E_6)$.
4. Compute the invariant Picard rank and use only the rank consequence of the
   Hochschild--Serre exact sequence.
5. Read line fields from $L$-points of $\operatorname{Spec}(E)$.

## Dependency map

1. The line-scheme equality depends on H0, H1, H2, Cayley--Salmon, and
   Kass--Wickelgren Corollary 53.  H3 audits but is not logically needed after
   equal-rank comparison.
2. Full $W(E_6)$ depends on the equality, H4--H5, Elsenhans--Jahnel Fact 3,
   Lemma 8, and Remarks 11--13.
3. The order $51840$ depends on full $W(E_6)$ and either H6 or the source fact
   $|U|=25920$ with $[W:U]=2$.
4. The arithmetic Picard rank depends on full $W(E_6)$, H6/the reflection
   argument, Hilbert 90, and torsion of $\operatorname{Br}(\mathbf Q)$.
5. The rational-line conclusions depend only on
   $F_1(Y)=\operatorname{Spec}(E)$ and the tower law.

## Proof

### Step 1: the global Fano scheme is finite étale of rank 27

The Fano scheme is the zero scheme of the section
$\sigma_F$ of $\operatorname{Sym}^3(\mathcal S^\vee)$ on
$\operatorname{Gr}(2,4)$.  By H0, $Y$ is a smooth cubic surface.  After base
change to $\overline{\mathbf Q}$, Cayley--Salmon gives 27 lines.
Kass--Wickelgren Corollary 53 applies to the section $\sigma_F$ and says that
each zero associated with a line disjoint from the singular locus is simple.
The singular locus is empty, so all 27 zeros are simple.

Consequently $F_1(Y)_{\overline{\mathbf Q}}$ is the disjoint union of 27
reduced points.  Because it is a closed subscheme of the projective
Grassmannian, $F_1(Y)$ is proper; a zero-dimensional proper scheme over a
field is finite.  Geometric reducedness over the characteristic-zero field
$\mathbf Q$ makes it étale.  Its rank is 27.

### Step 2: the eliminant is irreducible

Assume that $g$ factors nontrivially over $\mathbf Q$.  Gauss's lemma gives a
primitive factor $u\in\mathbf Z[d]$ with $1\le m:=\deg u\le26$.  Fix any of
the four primes in H2.  Since the leading coefficient of $g$ survives modulo
$p$, reduction preserves the degrees of both factors.  Since the complete
reduction of $g$ is squarefree, the reduction of $u$ is the product of a
subset of its distinct irreducible factors.  Hence $m\in S_p$.

This holds for all four primes, so H2 gives
$m\in\bigcap_pS_p=\{0,27\}$, contradicting
$1\le m\le26$.  Thus $g$ is irreducible.  It is separable in characteristic
zero, and $E=\mathbf Q[d]/(g)$ is a degree-$27$ field.

### Step 3: the chart object equals the whole Fano scheme

By H1, substitution of the three back-solutions into each $f_i$ has zero
remainder modulo $g$.  Therefore the coordinate assignment induces a
$\mathbf Q$-algebra homomorphism

$$
\mathbf Q[a,b,c,d]/(f_0,f_1,f_2,f_3)\longrightarrow E.
\tag{P.1}
$$

It is surjective because the image contains the generator $\bar d$ of $E$.
Thus (P.1) gives a closed immersion

$$
Z:=\operatorname{Spec}(E)\hookrightarrow F_1(Y)\cap U_{01}
\hookrightarrow F_1(Y).
\tag{P.2}
$$

The first arrow is closed.  The second arrow is initially open, but
$F_1(Y)$ is finite étale by Step 1; every open subscheme of a finite étale
scheme over a field is a union of components and hence is also closed.
Consequently the composite in (P.2) is a global closed immersion.

Both $Z$ and $F_1(Y)$ are finite étale of rank 27.  The resulting surjection
of their global finite coordinate algebras is a surjective linear map between
27-dimensional $\mathbf Q$-vector spaces and hence an isomorphism.  Therefore

$$
F_1(Y)\cong\operatorname{Spec}(E).
\tag{P.3}
$$

In particular the Fano scheme is connected, and (P.2) shows after the fact
that it is contained in $U_{01}$.  H3 supplies an independent check of that
last conclusion without being used circularly.

### Step 4: $K$ is the common line field

The 27 $\mathbf Q$-embeddings of $E$ into
$\overline{\mathbf Q}$ send $\bar d$ to the 27 roots of $g$ and parameterize
the 27 geometric points of (P.3).  H1 reconstructs $a,b,c$ as rational
functions, with rational nonzero constant denominators, in each root.  Hence
the splitting field $K$ of $g$ contains all coordinates of all lines.

Conversely, a normal field over which all lines are defined contains all
their $d$-coordinates, hence all roots of $g$ and thus $K$.  Therefore $K$ is
the least normal common field of definition and the normal closure of $E$.

### Step 5: transitivity plus the odd order-five witness forces full Weyl group

The action of $G=\operatorname{Gal}(K/\mathbf Q)$ on the roots is faithful by
the definition of a splitting field.  It is transitive because $g$ is
irreducible.  By Elsenhans--Jahnel Fact 3, preservation of the incidence
configuration of the 27 lines identifies $G$ with a subgroup of $W(E_6)$.

H2 makes the reduction at $37$ squarefree with surviving leading
coefficient.  Equivalently, the polynomial discriminant is nonzero modulo
$37$, so this prime is unramified for the root permutation.  The factor
degrees provide a Frobenius element

$$
\varphi\in G\subset W(E_6)
\quad\text{of cycle type}\quad(2,5,5,5,10).
\tag{P.4}
$$

The order of $\varphi$ is ten, so $G$ contains an element of order five.
Elsenhans--Jahnel Lemma 8 applies to the transitive subgroup $G$ and yields

$$
G=U\quad\text{or}\quad G=W(E_6).
\tag{P.5}
$$

By H5, consistent with Elsenhans--Jahnel Remarks 11--13, the class (P.4) lies
outside $U$.  Hence $G\ne U$ and (P.5) gives
$G=W(E_6)$.  Since $U$ has order 25920 and index two,

$$
[K:\mathbf Q]=|G|=51840.
\tag{P.6}
$$

No ordinary permutation-sign argument occurs here: Elsenhans--Jahnel
Remark 5 says the $W(E_6)$ action on the 27 lines lands in $A_{27}$.

Finally, $E$ cannot be Galois.  If it were, its normal closure would be $E$
and would have degree 27, contradicting (P.6).

### Step 6: geometric and arithmetic Picard ranks

Over $\overline{\mathbf Q}$, a smooth cubic surface is the blow-up of
$\mathbf P^2$ at six points.  Its Picard group therefore has basis
$H,E_1,\ldots,E_6$ and rank seven.

The six simple roots listed in H6 span the orthogonal complement of the
canonical class.  If a vector in the rational Picard space is fixed by every
root reflection, it is orthogonal to all six roots and hence is a multiple of
the canonical class.  The canonical class is fixed, so the full Weyl fixed
space is exactly one-dimensional.  Because the Galois image is $W(E_6)$,

$$
\operatorname{rank}
\operatorname{Pic}(Y_{\overline{\mathbf Q}})^{G_{\mathbf Q}}=1.
\tag{P.7}
$$

The low-degree terms of the Hochschild--Serre spectral sequence, together
with Hilbert 90, give the exact segment

$$
0\to\operatorname{Pic}(Y)
\to\operatorname{Pic}(Y_{\overline{\mathbf Q}})^{G_{\mathbf Q}}
\to\operatorname{Br}(\mathbf Q).
\tag{P.8}
$$

Since $\operatorname{Br}(\mathbf Q)$ is torsion, the cokernel of the Picard
injection in (P.8) is torsion.  Tensoring with $\mathbf Q$ proves rank equality.
The geometric Picard variety of a cubic surface is trivial, so this rank is
the arithmetic Picard number.  Equations (P.7)--(P.8) give

$$
\rho(Y_{\overline{\mathbf Q}})=7,
\qquad \rho(Y/\mathbf Q)=1.
\tag{P.9}
$$

This proves no unqualified integral equality of Picard groups.

### Step 7: fields defining one line

Let $L/\mathbf Q$ be finite.  An $L$-defined line is an $L$-point of the
Fano scheme.  By (P.3), such a point is a $\mathbf Q$-algebra map
$E\to L$.  Because $E$ is a field, the map is injective, and its image $E'$ is
a degree-27 conjugate of $E$.  The tower law gives

$$
[L:\mathbf Q]=[L:E'][E':\mathbf Q]=27[L:E'].
\tag{P.10}
$$

Thus $27\mid[L:\mathbf Q]$.  In particular $L=\mathbf Q$ is impossible, so
$Y$ has no $\mathbf Q$-line.

### Step 8: projective invariance

A rational linear coordinate change induces an automorphism of the
Grassmannian and transports the zero scheme (1.2).  A nonzero common scalar on
$F$ leaves that zero scheme unchanged.  These operations preserve the finite
étale algebra up to isomorphism, its normal closure and Galois permutation
representation, and the Picard lattice.  Corollary D follows.  This completes
the proof. $\square$

## Scope locks and corrected assumptions

- H1--H6 are certified by the current prefreeze payload and independently
  recomputed by the checker.  That exact machine state is bound into the
  frozen project release without rewriting it as a different machine status.
- The architecture's earlier suggestion that every C55 status leaf must cease
  to say `RELEASE_CANDIDATE` is rejected.  The authoritative C55 contract is
  stratified as recorded in H0.
- The subgroup parity must remain Coxeter/reflection parity.  Ordinary
  $S_{27}$ sign cannot discharge H5.
- Hochschild--Serre proves the rank comparison through a torsion cokernel; it
  does not give integral surjectivity.

## Open risks

1. A stale or differently normalized C55 coefficient array invalidates every
   eliminant and modular witness.
2. A mislabeled chart or reversed row-reduction convention can produce a
   plausible but irrelevant eliminant; direct line-equation reconstruction and
   H3 are required.
3. Factor degrees without stored factors, multiplication, squarefreeness, and
   surviving leading coefficients do not prove H2.
4. Transitivity plus order five leaves the index-two subgroup $U$ possible;
   H5 is indispensable.
5. A machine-reported fixed rank without reconstructing the Picard lattice and
   reflection action is insufficient.
