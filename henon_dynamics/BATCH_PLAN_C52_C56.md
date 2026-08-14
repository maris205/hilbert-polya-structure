# Batch plan: HCS-C52 through HCS-C56

Status: **planning-only, contingent architecture**

Date: 2026-08-14

## Batch objective

The frozen C51 result separates the normalized Hénon moment packets into
weight-zero and weight-one rails, proves the source rank identity
\(4^n-1\) for smooth \((2,3)\) complete intersections, and identifies an
exact projector gate inside

\[
 O_4=H^5(X_4)(2),\qquad
 h(O_4)=(1,83,83,1).
\]

The next batch asks whether this Hodge gate opens into a genuine algebraic
and arithmetic factor, whether the source varieties exist smoothly in all
orders, and whether the resulting tower admits a nonfactorwise completion.
Each paper below has its own theorem-sized stop/go gate.  They are not five
installments of one proof.

The dependency graph is

\[
 C52\longrightarrow C53,\qquad
 C52\longrightarrow C54\longrightarrow C55,\qquad
 (C53+C55)\longrightarrow C56.
\]

Only C52 is locked.  C53--C56 are contingent and must be re-scoped after
the preceding gate rather than forced to follow a failed branch.

## HCS-C52: dihedral Chow projector and graph-algebra optimum

### Dominant question

What is the full projective monomial **source** stabilizer of the explicit
fivefold

\[
 X_4:\quad \sum_{i=0}^{7}x_i^3=0,
 \qquad
 \sum_{i=0}^{6}x_ix_{i+1}+\rho x_7x_0=0,
\]

and what is the smallest middle-cohomology block containing its extreme
Hodge lines that can be cut out by the graph algebra of that stabilizer?

### Locked positive theorem target

Prove that the projective monomial source stabilizer is the order-24 group

\[
 G_{\mathrm{mon}}\cong
 \operatorname{Dih}(C_{12})
 =\langle r,s\mid r^{12}=s^2=1,\ srs=r^{-1}\rangle.
\]

After the algebraic middle Chow--Künneth projector \(\pi_5\), the Reynolds
graph correspondence

\[
 e_G=\frac1{24}\sum_{g\in G_{\mathrm{mon}}}[\Gamma_g],
 \qquad
 \pi_{\mathrm{core}}=\pi_5e_G
\]

cuts out a rank-10 \(K\)-rational Chow summand with Hodge ledger

\[
 (4,1)^1+(3,2)^4+(2,3)^4+(1,4)^1.
\]

After one Tate twist this is of Calabi--Yau-threefold Hodge type
\((1,4,4,1)\); this wording does not assert the existence of a
Calabi--Yau threefold realizing it.  The complementary middle summand has
rank \(158\) and is purely level one after the C51 normalization.

### Locked negative theorem target

Prove that no idempotent in \(\mathbf Q[G_{\mathrm{mon}}]\) can isolate the
rank-two extreme pair.  The trivial representation occurs once in
\(H^{4,1}\) and four times in \(H^{3,2}\), so every graph-algebra element
acts through the same augmentation scalar on the entire rank-10 trivial
isotypic block.

This is a graph-algebra optimum theorem, not a no-go for all algebraic
correspondences and not a classification of the full automorphism group of
\(X_4\).

### Minimal exact controls and kill gate

- B0 locks the C47--C51 source, \(K=\mathbf Q(\rho)\), the closing edge,
  smoothness scope, twist, and Hodge ledger.
- B1 independently enumerates all monomial maps, reconstructs the group
  table, and verifies the six Lefschetz projectors, \(\pi_5\), and the two
  orthogonal graph projectors.
- B2 recomputes the exact Cayley/Jacobian-ring representations over
  \(\mathbf Q(\rho)\), including the residue-orientation multiplier, and
  proves character multiplicities, ranks, and the augmentation lemma.
- **GO:** B0--B2 pass independently and the Chow-category identities are
  proved.
- **KILL:** any failure of the group order, residue-twisted character,
  rank totals, or Chow idempotence stops C52.  It is not repaired by a
  finite-prime fit.

B3 Frobenius polynomials and B4 correspondences outside the graph algebra
belong to C53 and are not part of the C52 claim.

### Duplication firewall and Route-A impact

C20/C21 and the classical curve-decomposition literature concern curves,
Jacobians, or ordered covers; they do not supply this fivefold middle Chow
projector.  General Calabi--Yau-type descriptions of \((2,3)\) Fano
fivefolds are prior structure and are not claimed as new.  Exact external
locators and the novelty comparison are frozen in the C52
`SOURCE_AUDIT.md`.

C52 improves A3 through algebraic packet control.  It inherits A2 and A4
unchanged but proves no new Euler half-plane, functional equation, Riemann
divisor, or self-adjoint generator.  Overall Route-A status remains
exploratory.

### Branch handoff

The rank-10 summand, rather than the unavailable rank-two graph summand, is
the sole C53 input.

## HCS-C53: arithmetic decomposition or indecomposability of the core

### Dominant question

Does the rank-10 core admit a non-graph \(K\)-rational algebraic
correspondence that isolates a lower-rank arithmetic factor?

### Positive theorem target

Construct an explicit algebraic correspondence whose multiplication
relation yields a nontrivial rational idempotent on the core, ideally a
rank-two extreme motive.  Promotion to modular, CM, or automorphically
induced factors requires a correspondence or compatible-system theorem;
stable numerical factorization is insufficient.

### Negative theorem target

Reconstruct one exact good-prime rank-10 Frobenius polynomial and prove
that it is irreducible over some \(\mathbf Q_\ell\).  This rules out every
proper \(\mathbf Q_\ell\)-subrepresentation and hence every nontrivial
rational-coefficient algebraic projector on the core.  It does not rule
out decomposition after extending coefficients or prove full symplectic
monodromy.

### Minimal exact controls and kill gate

- Equivariant Lefschetz traces or an independent exact cohomology engine
  reconstruct all ten coefficients; five traces suffice only after
  reciprocity is separately proved.
- Newton identities, weight-five reciprocity, determinant, both embeddings
  of \(K\), and a second-prime trace control must agree.
- A positive branch needs a Chow-level correspondence identity.  A negative
  branch needs an exact modulo-\(\ell\) irreducibility certificate.
- **KILL:** a table of prime traces or repeated \(2+8\) numerical factors
  without either theorem is not a paper.

### Duplication firewall, Route-A impact, and handoff

C52 proves only the graph-algebra block; C48--C51 never reconstruct this
projected rank-10 local polynomial.  A positive automorphic decomposition
would strengthen A3 for one \(n=4\) core only.  A negative theorem closes
the low-rank modular shortcut and hands C56 a genuinely high-rank factor.

## HCS-C54: all-order source smoothness or singularity spectrum

### Dominant question

For which \(n\) is the chronological source
\(X_n=(2,3)\subset\mathbf P^{2n-1}\) smooth in characteristic zero?

### Positive theorem target

First classify the rank of the twisted cyclic quadric.  Then prove that
the singularity equations are equivalent to a twisted periodic orbit of

\[
 (u,v)\longmapsto (v,v^2-u),
\]

together with the projective quadric constraint, and derive an all-\(n\)
smoothness theorem or an exact arithmetic classification of the singular
indices.

### Negative theorem target

Exhibit an exact nonzero characteristic-zero singular orbit and prove a
twisted repetition or monodromy mechanism producing infinitely many
singular indices.  This would kill the naive smooth all-moment tower rather
than merely identify one failed row.

### Minimal exact controls and kill gate

- Recover the inherited smooth rows \(n=2,3,4\).
- Separate characteristic-zero singularities from finite bad reduction.
- Use Groebner/resultant scans only to conjecture the recurrence theorem;
  every released singular index needs an exact algebraic witness.
- **KILL:** bounded computation at \(n=5\) or \(n\le N\) with no uniform
  theorem is too incremental and must not become HCS-C54.

### Duplication firewall, Route-A impact, and handoff

C48--C50 prove only fixed-row smoothness; C51's all-\(n\) rank formula is
conditional on smoothness.  C54 is the missing genuine-dynamics theorem.
A smooth or classified tower enables C55.  An infinite singular set sends
C55 to intersection cohomology and vanishing cycles instead.

## HCS-C55: infinite archimedean regularization or exact anomaly

### Dominant question

Can the finite C51 Hodge/Gamma ledger be promoted to a canonical infinite
archimedean factor determined by the chronological source tower?

### Positive theorem target

For the smooth indices supplied by C54, derive an all-order generating
function for the Hodge multiplicities, meromorphically continue its
spectral zeta to the regularization point, and prove that the chosen
source-normalized Abel/Hadamard/zeta prescription gives a branch-defined
meromorphic Gamma product with the required reflection law.

### Negative theorem target

Prove that two natural chronology-preserving regularizations differ by a
nonconstant exponential polynomial or a nonzero reflection/branch anomaly.
If C54 is singular, replace ordinary cohomology by a precisely declared
intersection-cohomology or nearby-cycle object and prove either a pure
repair or an unavoidable new-weight obstruction.

### Minimal exact controls and kill gate

- An exact all-\(n\) Hodge generating formula with the C51 rows as checks.
- Pole, residue, finite-part, branch, and regulator-comparison ledgers.
- A symbolic reflection identity or a symbolic nonzero anomaly.
- **KILL:** another finite Gamma table, a formal infinite product, or merely
  increasing \(\operatorname{Det}_{10}\) to a higher finite order is too
  incremental.

### Duplication firewall, Route-A impact, and handoff

C51 explicitly stops at a finite expected Gamma ledger.  General
regularized-product machinery is prior method; the new delta must be the
exact Hénon multiplicity tower and its theorem-level regularization or
anomaly.  This is the batch's direct A3 archimedean gate and supplies C56's
infinite-sector input.

## HCS-C56: nonfactorwise completion or scoped route closure

### Dominant question

After allowing algebraic projector blocks, denominator clearing, and the
C55 regularization, can the source-native Euler germ acquire a genuine
global reflection without changing the frozen prime clock?

### Positive theorem target

Construct a branch-defined completed object with meromorphic continuation
and prove

\[
 \widehat{\mathcal Z}_{H}(s)
 =\varepsilon\widehat{\mathcal Z}_{H}(-s),
\]

including finite-bad factors and compatibility with the inherited
normalized-semifinite determinant.  Expected \(n=3,4\) Hasse--Weil
functional equations cannot be used as proved inputs.

### Negative theorem target

For a frozen class consisting of source compatible pure-motive factors,
the clock \(u=ns+j\), consistent Tate twists, finite Artin/Tate
corrections, and the C55 regularization, prove that the one-sided center
tower has a nonzero reflection anomaly that cannot be cancelled across
orders.  This must strictly extend C51's factorwise-center obstruction to
the declared nonfactorwise class.

### Minimal exact controls and kill gate

- A complete sector-lattice involution and multiplicity ledger.
- Exact reflected logarithmic-derivative poles/residues or a local
  coefficient mismatch at independent good primes.
- Full branch, finite-bad-factor, and operator-ideal audit.
- **KILL:** a formal completed product or numerical zero plot is not a
  theorem.  If neither a global identity nor the scoped no-go is provable,
  stop the \(\mu_3\) full-kernel lane and switch the dynamical form.

### Duplication firewall, Route-A impact, and handoff

C51 excludes only a common factorwise standard center.  C56 must permit and
then decide cross-order/projector/regularized combinations.  A positive
result would be a major A3 advance, although A1 would remain weak.  A
negative result is the formal handoff to a new two-sided or otherwise
self-dual Hénon-type system in the next batch.

## Batch-wide publication vetoes

The following are controls or clues, not standalone papers:

- fixed \(n=5\) point counts or a fixed \(n=5\) smoothness certificate;
- pushing the inherited remainder from \(\Re s>1/5\) to \(\Re s>1/6\)
  solely by computing one more moment;
- replacing \(\operatorname{Det}_{10}\) by a higher regularization order
  without a new analytic theorem;
- more rank-10 prime tables without a correspondence or irreducibility
  theorem;
- another finite expected Gamma ledger;
- claiming a Calabi--Yau threefold, automorphy, a full Hasse--Weil
  functional equation, RH, or a Hilbert--Pólya operator from Hodge numbers
  or finite data.

The C52 citation and novelty audit is complete.  Each successor must add its
own source audit after its actual theorem is known; no absolute novelty
claim is authorized by this planning document.
