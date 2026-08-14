# HCS-C52 methodology blueprint

Status: **B0--B2 method implemented and independently replayed**

## Mathematical source lock

1. Work over \(K=\mathbf Q(\rho)\), with
   \(\rho^2+\rho+1=0\).
2. Retain the exact source equations
   \[
   C=\sum_{i=0}^{7}x_i^3,
   \qquad
   Q=\sum_{i=0}^{6}x_ix_{i+1}+\rho x_7x_0.
   \]
3. Use the C50--C51 characteristic-zero smoothness theorem and the C51
   normalization \(O_4=H^5(X)(2)\); do not re-fit either from prime data.
4. Preserve the chronological closing edge.  No averaged transition or
   symmetrized replacement of \(Q\) is admissible.

## B0: inherited source and model

- Recompute or verify the exact inherited certificate/payload hashes at
  implementation time.
- Parse the field, equations, dimension, degree \(6\), smoothness scope,
  Tate twist, and Hodge ledger from frozen artifacts.
- Reject a source mismatch rather than silently repairing history inside
  C52.

## B1: monomial group and Chow projectors

### Monomial stabilizer

Write a projective monomial map as

\[
 x_i\longmapsto \rho^{e_i}x_{\sigma(i)},
 \qquad e_i\in\mathbf F_3.
\]

The support of \(Q\) first restricts \(\sigma\) to automorphisms of the
eight-cycle.  Solve the remaining phase equations exactly, modulo common
projective scalar.  The target is 24 maps and an explicit presentation

\[
 G_{\mathrm{mon}}≅\operatorname{Dih}(C_{12}).
\]

The formal proof must derive completeness of the enumeration.  Matching an
order histogram alone does not identify the stabilizer.

### Middle Chow--Künneth projector

Let \(h=c_1(\mathcal O_X(1))\).  Since \(\deg X=6\), set

\[
 \pi_{2i}=\frac1{6}h^{5-i}\times h^i
 \quad(0\le i\le5),
 \qquad
 \pi_5=\Delta_X-\sum_{i=0}^{5}\pi_{2i}.
\]

Prove in \(\mathrm{CH}^5(X\times X)_{\mathbf Q}\) that the six Tate
projectors are mutually orthogonal and idempotent.  Projective monomial
automorphisms fix \(h\), so \(\pi_5\) commutes with every graph.

Define

\[
 e_G=\frac1{|G|}\sum_{g\in G}[\Gamma_g],
 \qquad
 \pi_{\mathrm{core}}=\pi_5e_G,
 \qquad
 \pi_{\mathrm{lev}}=\pi_5-\pi_5e_G.
\]

Idempotence and orthogonality must be proved in the declared Chow category,
not inferred only from one realization.

## B2: exact equivariant Cayley-ring calculation

Use the Cayley polynomial

\[
 \mathscr F=yC+zQ,
\]

with bidegrees

\[
 \deg x_i=(0,1),\qquad
 \deg y=(1,-3),\qquad
 \deg z=(1,-2),
\]

and the Jacobian quotient

\[
 R=K[x_0,\ldots,x_7,y,z]/J(\mathscr F).
\]

The required pieces are

\[
 H^{4,1}_{\mathrm{prim}}\simeq R_{1,-3},
 \qquad
 H^{3,2}_{\mathrm{prim}}\simeq R_{2,-3}.
\]

For a lift \(M_g\in\mathrm{GL}_8\) satisfying

\[
 (C,Q)(M_gx)=A_g(C,Q)(x),
\]

the residue action must include the orientation multiplier

\[
 \frac{\det M_g}{\det A_g}.
\]

This makes the action independent of the scalar representative in
\(\mathrm{PGL}_8\).  Omitting it is a semantic failure, even if dimensions
remain correct.

The exact target character on \(H^{3,2}\) is

\[
 \operatorname{tr}(r^k)
 =(83,-1,-3,-1,-7,-1,3,-1,-7,-1,-3,-1),
\]

\[
 \operatorname{tr}(sr^k)=3.
\]

The four one-dimensional multiplicities should be
\((4,1,3,3)\), and the five two-dimensional multiplicities should be
\((7,8,6,8,7)\).  The dimension check is

\[
 4+1+3+3+2(7+8+6+8+7)=83.
\]

The \(H^{4,1}\) generator must be checked to be trivial, not assumed from
its one-dimensionality.

## Graph-algebra optimality proof

On the trivial representation, every
\(a=\sum_g a_gg\in\mathbf Q[G]\) acts by its augmentation

\[
 \varepsilon(a)=\sum_g a_g.
\]

Because \(H^{4,1}\) and four copies in \(H^{3,2}\) are all trivial, any
graph-algebra idempotent that retains the extreme line has augmentation
one and retains the entire trivial block.  Complex conjugation supplies the
opposite Hodge pieces, so the smallest graph-algebra middle summand
containing the extreme pair has rank

\[
 1+4+4+1=10.
\]

The complement therefore has rank \(168-10=158\).  This argument covers
all elements of \(\mathbf Q[G]\), not merely central idempotents, but it
does not cover algebraic cycles outside the graph algebra.

## Producer/checker separation

- The producer constructs the finite bidegree relation matrices with custom
  exact pair arithmetic in \(\mathbf Q(\rho)\) and dense rational RREF.
- The checker independently rebuilds them with SymPy `DomainMatrix` over a
  separately constructed exact algebraic number field; the two modular
  embeddings in characteristic \(211\) are controls, not the
  characteristic-zero proof.
- Group enumeration, multiplication, inverse, order, and character inner
  products must be independently reconstructed.
- Hash verification alone is provenance evidence, not semantic evidence.
- Missing keys, unknown keys, type smuggling, and a claimed rank-10
  projector formed from \(e_G\) without \(\pi_5\) must fail closed.

## Claim and source discipline

- “Calabi--Yau-type” refers only to the Hodge ledger after a Tate twist.
- “Chow projector” requires a rational-equivalence correspondence identity.
- Same-projector realizations follow from a single \(K\)-rational
  algebraic correspondence; prime-specific linear projectors do not
  qualify, and no strict compatible system with computed local
  polynomials is claimed.
- The group theorem concerns the projective monomial source stabilizer, not
  the full automorphism group.
- SOURCE_AUDIT.md records exact primary locators for finite-group graph
  projectors, equivariant Cayley-ring formulas, Calabi--Yau-type Fano
  prior work, and nearby explicit decompositions.  Its novelty statement
  remains targeted and non-exhaustive.

## Large-door decision

B0--B2 either prove the amber rank-10/rank-158 Chow decomposition and
graph-algebra optimum, or C52 stops.  B3 local Frobenius and B4 new
incidence cycles are intentionally excluded and handed to C53.
