# Literature and Novelty Audit — SD-C27

**Search boundary:** primary and authoritative records checked through
2026-08-14  
**Primary family:** Symbolic Dynamics  
**Claim type:** diagnostic synthesis and exact model-specific theorem, not a
new general transfer-operator theory and not an RH theorem

## 1. Sources used in proofs or historical positioning

### Ruelle 1976 — holomorphic transfer determinants

David Ruelle, “Zeta-functions for expanding maps and Anosov flows,”
*Inventiones Mathematicae* 34 (1976), 231–242,
DOI `10.1007/BF01403069`.

Primary manuscript:
<https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B45%5D.pdf>

Use: foundational link among holomorphic transfer operators, periodic
points, fixed-point denominators, and dynamical zeta functions.  Paper25
specializes the local trace to affine disk contractions.

### Atiyah–Bott 1967 — alternating traces on elliptic complexes

Michael F. Atiyah and Raoul Bott, “A Lefschetz Fixed Point Formula for
Elliptic Complexes. I,” *Annals of Mathematics* 86 (1967), 374–407,
DOI `10.2307/1970694`.

Primary record:
<https://annals.math.princeton.edu/1967/86-2/p07>

Use: conceptual authority for alternating traces on a complex and the
exterior numerator.  Paper25 needs only the elementary one-dimensional
identity
\(\operatorname{tr}\Lambda^0A-\operatorname{tr}\Lambda^1A=
\det(I-A)\).

### Bandtlow–Jenkinson 2008 — Bergman nuclearity and trace formula

Oscar F. Bandtlow and Oliver Jenkinson, “Explicit Eigenvalue Estimates for
Transfer Operators Acting on Spaces of Holomorphic Functions,” *Advances in
Mathematics* 218 (2008), 902–925,
DOI `10.1016/j.aim.2008.02.005`, arXiv:0802.1638.

Primary manuscript: <https://arxiv.org/abs/0802.1638>

Use: trace-class behavior for countable holomorphic map-weight systems with
common compact containment, and the periodic-word trace denominator
\(\det(I-D\phi_\alpha)^{-1}\).  This is the direct analytic input for the
shared and disjoint Bergman operators.

### Ruelle 1990 — generalized Fredholm determinants

David Ruelle, “An Extension of the Theory of Fredholm Determinants,”
*Publications Mathématiques de l’IHÉS* 72 (1990), 175–193,
DOI `10.1007/BF02699133`.

Primary record:
<https://www.numdam.org/item/PMIHES_1990__72__175_0/>

Use: boundary source for contracting/Hölder transfer determinants.  It does
not authorize identifying a symbolic determinant with one ordinary Hilbert
space Fredholm determinant without an operator-level proof.

### Hadfield–Kandel–Schiavina 2020 — exterior-form cancellation

Charles Hadfield, Santosh Kandel, and Michele Schiavina, “Ruelle Zeta
Function from Field Theory,” *Annales Henri Poincaré* 21 (2020),
3835–3867, DOI `10.1007/s00023-020-00964-8`.

Primary record:
<https://link.springer.com/article/10.1007/s00023-020-00964-8>

Use: a modern explicit presentation of alternating exterior-power traces
cancelling periodic-orbit stability determinants.  It confirms that the
successful \(0|1\) mechanism is classical Lefschetz/Ruelle technology.

### Elias 1975 — universal self-delimiting coding

Peter Elias, “Universal Codeword Sets and Representations of the Integers,”
*IEEE Transactions on Information Theory* 21 (1975), 194–203,
DOI `10.1109/TIT.1975.1055349`.

Use: primary source for universal self-delimiting integer codes.  The gamma
code is frozen as an explicit logarithmic implementation, not claimed as a
new code.

### Parry–Pollicott 1990 — symbolic zeta background

William Parry and Mark Pollicott, *Zeta Functions and the Periodic Orbit
Structure of Hyperbolic Dynamics*, Astérisque 187–188 (1990),
DOI `10.24033/ast.28`.

Primary record: <http://www.numdam.org/item/AST_1990__187-188__1_0/>

Use: authoritative background for primitive-orbit products, trace
logarithms, and symbolic determinant conventions.

### Simon 1977 — trace-class Fredholm determinants

Barry Simon, “Notes on Infinite Determinants of Hilbert Space Operators,”
*Advances in Mathematics* 24 (1977), 244–273,
DOI `10.1016/0001-8708(77)90057-3`.

Use: authority for the entire Fredholm determinant of a trace-class operator
and the local trace-log expansion.  This supports the ordinary tensor-fiber
entire-versus-pole obstruction.

## 2. Direct 2026 overlap used only as a firewall

Lucian Randolph, “On the Riemann Hypothesis: The Critical Line as the
Universal Cascade Floor,” Zenodo preprint (May 2026),
DOI `10.5281/zenodo.19744754`.

Status: **non-peer-reviewed preprint; not theorem authority**.

The preprint considers the local operator \(p^{-s}f(z/p)\) and records the
spectral determinant

\[
 \prod_{m\ge0}(1-p^{-s-m}),
\]

which differs from the symbolic one-loop factor \(1-p^{-s}\).  Its later
terminology does not consistently preserve that ownership distinction.
Paper25's bounded delta is to insert the canonical one-form operator, prove
that a **graded ratio of two honest degreewise Fredholm determinants** gives
the one-loop factor, and then prove that this ratio retracts to the atom
loop.  No theorem in SD-C27 depends on this preprint.

## 3. Collision and noncollision ledger

| Paper25 statement | Closest established source | Novelty boundary |
|---|---|---|
| compactly contained affine IFS operators are nuclear with fixed-point traces | Ruelle 1976; Bandtlow–Jenkinson 2008 | low; explicit code specialization only |
| exterior grading cancels \(\det(I-D\phi^r)^{-1}\) | Atiyah–Bott; modern Ruelle form factorizations | low; classical mechanism |
| scalar normalization forces \(q=0\) | implicit in the trace formula | medium; explicit two-power rigidity and rank-one boundary |
| ordinary trace-class tensor moments \(1-q^r\) are impossible | trace-class determinant theory | medium; short entire-versus-pole theorem |
| shared graded renewal keeps mixed words | standard symbolic full-shift determinant | medium; exact integration with the code-fiber test |
| disjoint graded renewal retracts to atom loops for every inventory | direct-sum cohomology | medium; source-integrity collapse theorem |
| integer histories have logarithmic self-delimiting length | Elias 1975 | none; implementation choice |
| prime/RH mechanism | none | explicitly not claimed |

## 4. Recent-search boundary

The source search used combinations of:

- Riemann zeta with holomorphic composition or transfer operators;
- Ruelle/Fredholm determinants with prime Euler factors;
- prefix-free or self-delimiting codes with dynamical zeta functions;
- Lefschetz/exterior grading with arithmetic symbolic dynamics;
- recent 2025–2026 transfer-operator work.

No primary source was found through 2026-08-14 that combines all four parts
of the SD-C27 diagnostic: logarithmic self-delimiting integer histories, an
explicit scalar all-repetition obstruction, a canonical de Rham repair, and
the shared-versus-disjoint source-integrity collapse.  This is a bounded
search result, not proof of global novelty.

## 5. Novelty assessment

| Component | Score | Assessment |
|---|---:|---|
| analytic transfer technology | 2/10 | established |
| canonical exterior cancellation | 2/10 | established |
| scalar/tensor rigidity formulation | 6/10 | concise model-specific theorem |
| shared/disjoint collapse synthesis | 7/10 | strongest diagnostic contribution |
| arithmetic/RH mechanism | 0/10 | absent by design |

**Overall novelty score:** 6/10.

Recommendation: proceed as a rigorous obstruction/repair paper.  The honest
claim is not a new determinant theory, but an exact classification of what
the analytic-function-space loophole buys and where arithmetic selection is
lost.

## 6. Citation discipline locks

- Ruelle/Bandtlow–Jenkinson carry analytic trace claims.
- Atiyah–Bott and Hadfield–Kandel–Schiavina carry historical exterior
  cancellation context, not the model-specific theorem.
- Simon carries the trace-class determinant property.
- Randolph is labelled non-peer-reviewed and carries no proof.
- Internal predecessor labels locate the research sequence but are not
  substituted for external citations.
- No citation is used for a stronger conclusion than its stated scope.
