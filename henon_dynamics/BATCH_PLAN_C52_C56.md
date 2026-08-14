# Batch plan: HCS-C52 through HCS-C56

Status: **adaptive batch in progress; C52--C53 complete, C54 locked**

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

The dependency graph after the first two realized gates is

\[
 C52\longrightarrow C53\longrightarrow C54\longrightarrow C55
 \longrightarrow C56.
\]

C52 and C53 are complete.  C54 is locked from the actual C53 rational
descent; C55 and C56 remain contingent and must be re-scoped after the
preceding gate rather than forced to follow a failed branch.

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

## HCS-C53: explicit rational descent and compatible rank-ten core

### Realized theorem

An explicit Hilbert--90 basis descends the ordered Fermat-cubic/twisted-
quadric equations to \(\mathbf Q\) for every \(n\ge2\).  This is an
all-order equation theorem only; smoothness and motivic packets remain
certified on \(n=2,3,4\).

For \(n=4\), Galois conjugation transports the order-24 dihedral source
group nontrivially, but its Reynolds graph correspondence is invariant.
Restriction/corestriction therefore descends the C52 rank-10 and rank-158
middle Chow projectors to \(\mathbf Q\).  The raw rank-10 summand defines,
outside a finite bad set, an \(\ell\)-independent degree-ten polynomial

\[
 P_p(T)=\det(1-\operatorname{Frob}_pT\mid M_0)\in\mathbf Z[T]
\]

of weight five with exact reciprocal coefficients.  At good split primes
the two \(K\)-factors coincide, so the \(n=4\) half-root is one ordinary
\(\mathbf Q\)-factor locally.  At inert primes the quadratic Artin identity
is generally not a square; no global root, continuation, functional equation,
or automorphy is inferred.

### Why the original target was changed

Exact reconstruction of the full rank-ten polynomial at one prime remains
computationally expensive and the preliminary \(p=7\) trace is retained only
as an uncertified regression anchor.  The rational descent and compatible-
system theorem are stronger than another finite trace table and do not depend
on that computation.

### Route-A impact and handoff

C53 gives the first \(\mathbf Q\)-rational compatible core and improves A3
packet control, while A2 and A4 are inherited.  C54 now asks a genuinely
global question suggested by the exact descent: classify the full all-order
monomial source group and determine exactly when the descended rational local
power is an ordinary finite-rank compatible-system multiplicity.

## HCS-C54: universal dihedral source symmetry and denominator rigidity

### Locked positive theorem

For every \(n\ge2\), the full projective monomial ideal stabilizer of the
ordered source pair is

\[
 G_n\cong\operatorname{Dih}(C_{3n}),\qquad |G_n|=6n.
\]

This is not a claim about the full PGL automorphism group.  Under the C53
descent it becomes a generally nonconstant finite etale \(\mathbf Q\)-group
scheme of rank \(6n\), split by \(K\), with exactly two rational points.

For every packet-admissible smooth row, require an ordinary semisimple
finite-rank compatible system to reproduce the complete good-split local
factor with exponent \(4/n\) while preserving the weight-zero/weight-one
decomposition.  Then such a system exists if and only if

\[
 n\mid4,
\]

so for \(n\ge2\) only \(n=2,4\) survive.  The negative implication uses
Chebotarev--Brauer--Nesbitt and the two pure ranks separately; the total rank
alone falsely accepts \(n=3\).  The converse uses honest direct copies and
therefore matches every local power trace, not just the first coefficient.

### Exact n=3 and counterpacket gates

The complete \(G_3=\operatorname{Dih}(C_9)\) Cayley/Fermat character shows
that no nonzero common central source-isotypic sector clears the \(4/3\)
denominator on both weights.  Split-invisible virtual rational classes such
as \(U-U\otimes\chi_{K/\mathbf Q}\) restrict to zero over \(K\), have rank
zero, and cannot repair the obstruction.  The common character statement is
first a \(K\)-theorem; a common rational group form requires the explicitly
twisted Fermat descent rather than silently mixing two rational models.

### Scope and handoff

The all-order equation and group theorem are unconditional.  For \(n\ge5\),
smoothness, motives, and packets are not asserted; the denominator theorem is
conditional on packet admissibility.  No fixed-prime table, global/inert root,
automorphy, functional equation, or RH claim is part of C54.  Its next gate is
not another denominator paper: C55 compares the parameterized Yukawa/IVHS
invariants of the C53 rank-ten Calabi--Yau-type core with a genuine rational
Calabi--Yau-threefold family before any motivic-identification claim.

## HCS-C55: rank-ten Yukawa comparison and honest Calabi--Yau realization gate

### Dominant question

Is the rational rank-ten Calabi--Yau-type motive of C53 the third cohomology
of a genuine Calabi--Yau threefold, rather than merely a Hodge-size match?

### First comparison target

Construct the four-parameter invariant deformation of the C53 core and
compute its polarized infinitesimal variation of Hodge structure, especially
the Yukawa cubic in a source-canonical tangent basis.  Independently compute
the same invariant for an explicit rational Calabi--Yau quotient family with
\((h^{1,1},h^{2,1})=(1,4)\).  Compare their Yukawa moduli up to the allowed
linear change of tangent coordinates and polarization scale.

### Positive and negative theorem branches

- **Positive:** an exact family-level identification of the IVHS/Yukawa data
  authorizes a search for an algebraic correspondence or a common geometric
  construction; it does not by itself prove a motivic isomorphism.
- **Negative:** a certified invariant mismatch rules out that entire family
  as a realization of the Hénon core, which is substantially stronger than
  a mismatched finite-prime trace.

If the initial rational quotient family is excluded, C55 may pivot to an
explicit \((2,2,3)\) Calabi--Yau or a quotient/resolution construction, but it
must retain a parameterized invariant or correspondence theorem.  Merely
sharing Betti number ten is not evidence.

### Minimal controls and kill gate

- Exact parameter spaces and smooth/free loci over \(\mathbf Q\).
- Polarization-normalized IVHS and Yukawa tensors on both sides.
- Coordinate-invariant comparison data, not fitted bases.
- **KILL:** Hodge-number coincidence, isolated point counts, or an unnamed
  categorical resemblance is not a paper.

## HCS-C56: adaptive realization closure or nonfactorwise analytic gate

### Adaptive rule

C56 is deliberately not locked before C55.  It must be a theorem-sized
consequence of the realized C55 branch, not a fifth installment of the same
calculation.

- If C55 finds a genuine geometric realization, C56 must construct and test
  the induced compatible local factors, bad-prime data, completed functional
  equation, and relation to the normalized-semifinite determinant.  Expected
  Hasse--Weil continuation may not be used as a proved input without an
  automorphy theorem.
- If C55 proves an IVHS/Yukawa mismatch or a broader realization no-go, C56
  may instead return to the analytic lane and decide a declared nonfactorwise
  completion class, strictly extending C51's factorwise-center obstruction.
- A second legitimate fallback is the exact conic-fibration/flattening gate
  isolated during C53 reconnaissance, but only if it yields an exhaustive
  geometric theorem rather than one plane or one prime.

### Publication veto

No formal Gamma product, numerical zero plot, isolated rank-ten prime table,
or mere increase of regularized determinant order qualifies.  If none of the
three branches yields a theorem, the \(\mu_3\) full-kernel lane must close and
hand off to a new self-dual dynamical form.

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
