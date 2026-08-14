# Literature and novelty audit — Paper 28 / SD-C30

Search date: 2026-08-14.

## Search boundary

The audit covered five intersecting literatures:

1. incidence algebras and Möbius inversion on locally finite posets;
2. oblique projections and biorthogonal Riesz systems;
3. weighted and symmetric orthogonalization;
4. Schatten ideals and higher modified Fredholm determinants;
5. chiral/off-diagonal operator blocks and critical-line reflection.

Exact-combination searches included the phrases incidence idempotent,
Möbius projector, oblique incidence, regularized Fredholm determinant,
Schatten chiral block, critical line, and weighted transpose, with
additional 2024–2026 searches. No matching construction was found.

## Primary-source anchors

### Incidence and Möbius inversion

Rota's foundational paper introduced the modern incidence-algebra
framework and Möbius inversion for locally finite posets
\citep{Rota1964}. It supports the source compiler \(Z,\mu\), but does
not study its rank-one idempotents as Schatten operator families.

A recent poset Möbius result by Goh proves an uncertainty principle
for supports under Möbius inversion \citep{Goh2026}. It is evidence
that the locally finite setting remains active, but it does not
overlap the chiral or determinant construction here.

### Oblique projections and weighted geometry

Tang relates oblique projections to biorthogonal Riesz bases and
angles between closed subspaces \citep{Tang2000}. Antezana, Corach,
Ruiz, and Stojanoff study weighted projections and compatibility with
diagonal operator algebras \citep{AntezanaEtAl2004}. These works form
the correct adjacent operator-geometric literature. They do not
derive the divisibility Gram coefficients or the prime-frequency
fourth moment.

Löwdin's symmetric orthogonalization is the historical square-root
metric transfer \citep{Lowdin1950}. The present Hellinger/Löwdin step
uses the same positive-square-root mechanism; the new point is the
commutant classification showing that every positive common metric,
not only one selected metric, collapses the active incidence atoms.

### Trace ideals and regularized determinants

Simon is the standard source for trace ideals and modified Fredholm
determinants \citep{Simon2005}. Britz et al. give a modern treatment
of product formulas and correction polynomials for higher regularized
determinants \citep{BritzEtAl2020}. These sources justify the analytic
framework and deletion ledger; regularization itself is not novel.

Koutsonikos-Kouloumpis and Lesch provide further analytic and algebraic
proofs of higher determinant product formulas
\citep{KoutsonikosLesch2022}. Their work reinforces the need to retain
the correction terms rather than treating \(\det_q\) as an ordinary
multiplicative determinant.

## Novelty boundary

The ingredients are individually classical:

- incidence Möbius inversion;
- bounded similarity and Schatten ideals;
- oblique/biorthogonal projection geometry;
- square-root orthogonalization;
- off-diagonal self-adjoint blocks;
- higher regularized Fredholm determinants.

The plausible contribution is their source-locked synthesis and the
resulting exact dichotomy:

1. the minimal common strip is the \(\mathcal S_3\) strip
   \(1/3<\Re s<2/3\);
2. the native divisibility Gram matrix has a closed positive formula;
3. unique factorization isolates a positive fourth-moment frequency
   \(4G_{pq}^2/(pq)\);
4. the same effect occurs on composite-only and generic-poset controls;
5. all positive common orthogonalizing metrics force active atom
   coordinates and eliminate the motion.

No prior source combining these five statements was found. This is an
exact-combination novelty conclusion, not a proof of global priority.
A reasonable novelty assessment is 6/10 for the combined theorem and
2–3/10 for the individual tools.

## Claims deliberately excluded

- No source supports identifying the auxiliary \(z\)-zeros of
  \(\det_3(I-z\mathcal B_s)\) with zeta zeros.
- Critical-line self-adjointness of a \(t\)-dependent family is not a
  Hilbert–Pólya realization.
- Generic Gram motion is not evidence of arithmetic selectivity.
- The positive-metric theorem does not classify unbounded or
  indefinite metrics.

## Citation completeness

Every conceptual ingredient used in the paper has a primary-source
anchor. The exact finite computations are independently reproducible
from the frozen prototype and do not require a literature citation.
No secondary review source is used to establish a theorem.
