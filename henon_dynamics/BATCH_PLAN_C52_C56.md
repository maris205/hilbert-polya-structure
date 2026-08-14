# Batch plan: HCS-C52 through HCS-C56

Status: **adaptive batch in progress; C52--C55 complete, C56 conditionally
locked pending final committed C55 rebind**

Date: 2026-08-15

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

The dependency graph after the first four realized gates is

\[
 C52\longrightarrow C53\longrightarrow C54\longrightarrow C55
 \longrightarrow C56.
\]

C52 through C55 are complete.  C55 realizes a four-dimensional rational
equivariant deformation germ, a relative rank-ten CY3-type Reynolds
variation, and a smooth geometrically irreducible rational Yukawa cubic
surface, without constructing or excluding an honest Calabi--Yau
threefold.  C56 is conditionally locked to the arithmetic of the
twenty-seven-line scheme of that surface.  The lock becomes effective only
after the released C55 certificate, the committed C55 coefficient object,
and the live C56 input agree exactly and every line-scheme computation is
replayed.

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

### Realized universal and denominator theorems

For every \(n\ge2\), the full projective monomial ideal stabilizer of the
ordered source pair is

\[
 G_n\cong\operatorname{Dih}(C_{3n}),\qquad |G_n|=6n.
\]

This is not a claim about the full PGL automorphism group.  Under the C53
descent it becomes a generally nonconstant finite etale \(\mathbf Q\)-group
scheme of rank \(6n\), split by \(K\), with exactly two rational points.

For every packet-admissible smooth row, require an ordinary actual
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

### Realized n=3 and counterpacket gates

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
automorphy, functional equation, or RH claim is part of C54.  Its next gate
was not another denominator paper: C55 constructs the parameterized
Yukawa/IVHS invariant of the C53 rank-ten Calabi--Yau-type core and gives an
exact necessary gate for comparison with a genuine rational
Calabi--Yau-threefold family before any motivic-identification claim.

## HCS-C55: rational Yukawa surface and honest Calabi--Yau VHS gate

### Dominant question

What is the exact projective Yukawa invariant of the rational rank-ten
Calabi--Yau-type core, and can it pass the necessary polarized-VHS tests for
the third cohomology of a genuine Calabi--Yau threefold?

### Realized theorem

C55 constructs a pointed smooth locally closed four-dimensional
\(\mathbf Q\)-germ \(B_{\rm core}\) as a transverse slice in the smooth fixed
Hilbert germ of the descended \(n=4\) cubic--quadric complete intersection.
Its Kodaira--Spencer map identifies

\[
T_{B_{\rm core},0}\simeq H^1(T_X)^{\mathscr G}.
\]

This is neither a dimension statement for the whole fixed Hilbert locus nor
a literal family \(C+\sum_i t_ip_i=Q=0\).

The intrinsic norm of the universal action graph for the nonconstant
rank-\(24\) finite etale group scheme is self-transpose and idempotent.  Its
image on \(R^5f_*\mathbf Q(1)\) is a polarizable rank-\(10\) VHS with Hodge
numbers

\[
(h^{3,0},h^{2,1},h^{1,2},h^{0,3})=(1,4,4,1)
\]

and the projected period map is locally immersive.  Exactly one Tate twist,
\(\mathbf Q(1)\), is used.  No relative Chow--Kunneth projector and no
Calabi--Yau threefold are constructed.

For the Cayley polynomial \(F=yC+zQ\), exact producer/checker replays certify
the invariant tangent basis, the one-dimensional rational top trace, and the
projective Yukawa tensor

\[
Y_{ijk}=\operatorname{Tr}_{R_{5,-6}}(y^5p_ip_jp_k)
\]

up to its single unavoidable nonzero scale.  In the locked rational tangent
basis this is a primitive integral \(20\)-term cubic.  Its gradient quotient
has Hilbert series \((1+t)^4\) and length \(16\), so its zero locus

\[
S_H\subset\mathbf P^3_{\mathbf Q}
\]

is a smooth geometrically irreducible cubic surface.  Here rational means
defined over \(\mathbf Q\), not rational as a variety over \(\mathbf Q\).

### Realized necessary gate and unresolved comparator

The first admitted comparators are the four-parameter
Braun--Candelas--Davies \(\mathrm{Dic}_3\) and \(\mathbb Z_{12}\) quotient
families, both honest generically smooth Calabi--Yau threefold families with
\((h^{1,1},h^{2,1})=(1,4)\).  An isomorphism with the third-cohomology
polarized rational VHS of such a family necessarily identifies the two
Yukawa cubics through

\[
Y_{\rm CY}(c;u)=\lambda Y_H(Au),
\qquad A\in\operatorname{GL}_4(\mathbf C),\quad\lambda\ne0.
\]

This condition is necessary, not sufficient: even a match would not identify
higher Yukawa jets, the Gauss--Manin connection, monodromy, integral
structure, or a motive.  No complete four-variable B-model tensor is
currently available for either named comparator, and the mirror-side
one-parameter calculation is not a substitute.  The realized comparator
status is therefore **NOT-COMPARABLE-WITH-CURRENT-DATA**.  C55 neither
establishes nor rules out an honest-CY3 realization.

The Route-A tuple remains
**(A1_WEAK, A2_ANALYTIC_DETERMINANT,
A3_PARTIAL_ANALYTIC_STRUCTURE, A4_NATURAL_QUANTIZATION)** with overall
**ROUTE_A_EXPLORATORY**.  C55 proves no new continuation, functional
equation, automorphy, RH statement, or Hilbert--Polya operator.

## HCS-C56: twenty-seven-line field and maximal \(E_6\) arithmetic

### Conditional lock

C56 studies a new arithmetic object attached to the released C55 Yukawa
surface: its finite etale Fano scheme of geometric lines and the Galois
closure of the corresponding degree-\(27\) line field.  C55 constructs and
controls the projective cubic; C56 determines the arithmetic monodromy of
its lines.  It is therefore a separate theorem-sized paper, not a
continuation of the C55 Cayley-ring calculation.

The lock is conditional on a three-way exact rebind of the normalized
primitive C55 coefficient vector: the released certificate, the committed
implementation object, and the live C56 input must agree.  Temporary
reconnaissance artifacts are chronology only and are not theorem evidence.

### Locked theorem target

For the released surface \(S_H/\mathbf Q\), prove that its Fano line scheme
is connected and finite etale of degree \(27\),

\[
F_1(S_H)\simeq\operatorname{Spec}E,
\qquad [E:\mathbf Q]=27.
\]

Prove that the Galois closure \(\widetilde E\) satisfies

\[
\operatorname{Gal}(\widetilde E/\mathbf Q)\cong W(E_6),
\qquad |W(E_6)|=51840.
\]

Deduce

\[
\rho(S_{H,\overline{\mathbf Q}})=7,
\qquad \rho(S_H/\mathbf Q)=1,
\]

and that \(S_H\) has no \(\mathbf Q\)-defined line.  More precisely, every
finite extension defining one geometric line must have degree divisible by
\(27\).

These conclusions depend only on the rational projective
\(\operatorname{GL}_4\)-class and common scaling of the C55 cubic.  They do
not imply that \(S_H(\mathbf Q)\) is empty, settle rationality of the surface,
or establish an honest-CY3, VHS, motive, \(L\)-function, or
Hilbert--Polya realization.

### Exact controls and kill gates

- Reconstruct all six Grassmann charts from the rebound released cubic.
- Prove that the \(U_{01}\) quotient has length \(27\), and that the five
  charts covering \(p_{01}=0\) give unit ideals.
- Certify the degree-\(27\) lexicographic eliminant and all back-substitution
  identities.
- Prove irreducibility over \(\mathbf Q\) by the squarefree modular
  subset-sum sieve at \(7,19,29,37\), whose degree intersection is exactly
  \(\{0,27\}\).
- Verify smooth reduction and the \(p=37\) Frobenius cycle type
  \((2,5,5,5,10)\); together with transitivity, a cited subgroup lemma, and
  an independent exact \(W(E_6)\) permutation/parity enumeration, it must
  force the full Weyl group.
- **KILL:** a failed C55 rebind, a line lost outside the main chart, a proper
  degree surviving the modular sieve, a ramified or changed Frobenius
  witness, or an inference of full \(W(E_6)\) merely from genericity,
  transitivity, or an element of order five stops the claimed branch.

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
