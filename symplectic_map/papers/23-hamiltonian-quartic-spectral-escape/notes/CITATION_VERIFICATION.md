# Paper 23 — Bounded Citation Verification

## Verification boundary

This ledger transcribes only the public-source checks already recorded by the
immutable Paper 23 R1 novelty review and its family-sign correction.  The
source-design author performed no new network lookup.  The controlling cutoff
is 2026-08-24 UTC.

The bounded R1 search used six batches and 24 exact queries.  It did not
exhaust subscription databases, nonindexed work, private drafts, all
languages, or every citation graph.  Consequently this file supports bounded
positioning only.  It does not support “first,” “only,” “unprecedented,” or
any absolute-priority formulation.

The review records bound here are:

- `BATCH_06_PAPER23_CANDIDATE_REVIEW_R1.md`, SHA-256
  `a3c9815c2d851c8791a259c4e46a4d33663f06e6ab4faa58a981f89f7ebf3ae7`;
- `BATCH_06_PAPER23_CANDIDATE_REVIEW_R1_CORRECTION.md`, SHA-256
  `2a1278ff35eeeaf7af2f63010c8ad0f10d745cc763a8379d3a833695897f3783`;
- `BATCH_06_PAPER23_CANDIDATE_REVIEW_R2.md`, SHA-256
  `cb5b3e748fe4cc5b26f51e2b1b4ca7f93ea2e1011a0c4f2f99e47dc6884d5ed8`.

R2 was deliberately offline and supplies proof-adversarial evidence, not a
public novelty score.  The R1 correction controls the positive-sign family;
the original R1 minus-sign sentence is historical and must not be cited as a
theorem or sign-invariance claim.

## Primary-source metadata ledger

| Key | Source and identifier recorded by R1 | Access level actually used in R1 | Permitted relevance statement | Forbidden inference |
|---|---|---|---|---|
| S01 | Blanc–van Santen, *Dynamical degrees of affine-triangular automorphisms of affine spaces*, arXiv:1912.01324, DOI `10.48550/arXiv.1912.01324` | arXiv abstract and authoritative metadata | general weak-Perron realization neighbor for affine-triangular automorphisms | no claim that general Perron realization is new here; no full-text noncollision claim |
| S02 | Shao–Sun, *Dynamical degrees of affine-triangular automorphisms in dimension four*, arXiv:2509.14584, DOI `10.48550/arXiv.2509.14584` | abstract and authoritative metadata | recent dimension-four affine-triangular degree-four neighbor in another class | abstract-level access cannot prove absence from all full details |
| S03 | Favre–Firsova–Palmisano–Raissy–Vigny et al., *Hénon maps: a list of open problems*, authoritative Stony Brook HTML record | full HTML, including relevant Problem 8 / Question 38 and bibliography | context for weak-Perron questions and higher-dimensional polynomial automorphism degree growth | no candidate-specific theorem attributed to the survey |
| S04 | Berger–Turaev, *Generators of groups of Hamiltonian maps*, arXiv:2210.14710, DOI `10.1007/s11856-024-2709-7` | arXiv abstract plus institutional/publisher metadata | position/momentum shear generation and approximation context | no exact iterated degree recurrence transferred from this source |
| S05 | Forstnerič, *A theorem in complex symplectic geometry*, DOI `10.1007/BF02921802` | author-hosted full text; relevant symplectic-shear passages inspected | foundational symplectic-shear generation background | no quartic degree-growth collision inferred |
| S06 | Koch–Lomelí, *On Hamiltonian flows whose orbits are straight lines*, arXiv:1304.3377, DOI `10.3934/DCDS.2014.34.2091` | full text available; abstract and relevant shear/factorization passages inspected | context for affine-integrable Hamiltonian structure and shear factorization | no claim about this alternating product's exact dynamical degree |
| S07 | Rangarajan, *Polynomial map symplectic algorithm*, arXiv:physics/0212098 | abstract and author bibliographic metadata | polynomial symplectic-map factorization context | no selector, visibility, or exact recurrence imported |
| S08 | Déserti, *Degree growth of polynomial automorphisms and birational maps: some examples*, arXiv:1602.04642, *European Journal of Mathematics* 4 (2018), 200–211 | abstract and journal metadata | broader examples of polynomial degree growth | its polynomial-growth examples are not the present exponential Perron theorem |
| S09 | Dang–Favre, *Spectral interpretations of dynamical degrees and applications*, *Annals of Mathematics* 194 (2021), 299–359 | bibliographic pointer in the inspected authoritative survey only | general spectral context, if cited with this access limitation respected | no noncollision conclusion from an uninspected full text |

URLs, if later encoded in a bibliography, must be copied from R1 rather than
silently reconstructed.  A later publication-stage citation checker must
reverify current metadata and exact author lists before public use.

## Claim-to-source map

| Manuscript role | Permitted sources | Local proof still required |
|---|---|---|
| general weak-Perron realization context | S01 and S03 | the explicit Hamiltonian family, selectors, cone, and quartic remain local |
| nearby dimension-four affine-triangular work | S02 | class distinction and the complete local theorem |
| Hamiltonian/symplectic shear context | S04--S07 | inverses, Hessian-block symplecticity, and all degree calculations |
| general degree-growth context | S03, S08, and carefully qualified S09 | actual recurrence and visible coordinate |
| Perron–Frobenius, Cayley–Hamilton, Gauss lemma | standard named results; no novelty claim | assumptions and their application must be written explicitly |

No external citation proves a selector inequality, a cone face, carry,
no-cancellation, $q_4$ visibility, a principal-minor identity, or the mod-five
factor exclusion.

## Local predecessor lineage

| Local paper | Owned result/architecture | Paper 23 boundary |
|---|---|---|
| Paper 20 | two-mode Hamiltonian product shears, selector-to-matrix method, quadratic spectral outcome | methodology is reused, not renamed as new |
| Paper 21 | three-mode exact degree matrix, visibility, cubic characteristic polynomial and cubic Perron subfamilies | Paper 23 must not claim first use of phase matrices, cones, visibility, or modular Perron certification |
| Paper 22 | arbitrary-mode endpoint-spike cubic spectral collapse and common unit-sector explanation | closest contrast; Paper 23 contributes a concrete four-spike escape, not a new statement of the collapse theorem |

Papers 12--19 supply broader Hénon, residue, torus, trace, translate, and gcd
context but contain no direct theorem collision according to the bounded R1
portfolio audit.

## Citation STOP rules

Citation work must stop and return for review if:

1. a source is represented at a deeper access level than R1 actually used;
2. an abstract-only source is used to certify a full-text noncollision;
3. the general rank lemma, selector method, Perron theory, or symplectic
   shear construction is advertised as novel;
4. Paper 22's theorem is used instead of locally proving Paper 23's family;
5. absolute priority is inferred from the bounded query log;
6. the historical R1 minus-sign family is allowed to override its immutable
   positive-sign correction;
7. a current pre-submission collision search is omitted at a future stage
   where public submission is actually authorized.

No citation file, bibliography, network lookup, author contact, or external
effect is authorized by this ledger.
