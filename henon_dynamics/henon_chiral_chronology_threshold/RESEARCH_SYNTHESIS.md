# HCS-C21 Stage-1 research synthesis

## Material passport and claim-intent manifest

```json
{
  "experiment_provenance": [
    {
      "experiment_id": "exp-c21-producer",
      "artifact": "results/c21_certificate.json",
      "sha256": "5386c95cbc65e6a4323cfcf230de6b41f353be909d197818f9c4fbf0a75a96fc"
    },
    {
      "experiment_id": "exp-c21-independent",
      "artifact": "results/c21_independent_check.json",
      "status": "PASS",
      "checks_passed": 133
    }
  ],
  "claim_intent_manifests": [
    {
      "manifest_version": "1.0",
      "manifest_id": "M-2026-08-08T09:00:00Z-c21a",
      "emitted_by": "synthesis_agent",
      "emitted_at": "2026-08-08T09:00:00Z",
      "claims": [
        {
          "claim_id": "C-001",
          "claim_text": "The period-six chiral marker and scalar cubic factorization are Endler--Gallas prior work.",
          "intended_evidence_kind": "external_primary_source",
          "planned_refs": ["endlergallas2006chiral"]
        },
        {
          "claim_id": "C-002",
          "claim_text": "The normalized period-six ordered-edge cover is geometrically connected, has group D6 of order 12, and genus one.",
          "intended_evidence_kind": "theoretical_exact_proof",
          "planned_refs": [],
          "planned_experiment_ids": ["exp-c21-producer", "exp-c21-independent"]
        },
        {
          "claim_id": "C-003",
          "claim_text": "The exact order-six time action is trivial on weight-one cohomology.",
          "intended_evidence_kind": "theoretical_exact_proof",
          "planned_refs": [],
          "planned_experiment_ids": ["exp-c21-producer", "exp-c21-independent"]
        },
        {
          "claim_id": "C-004",
          "claim_text": "Within source-identified and certified chiral covers through period seven, a nontrivial weight-one time sector first occurs on the certified period-seven component.",
          "intended_evidence_kind": "theoretical_exact_proof",
          "planned_refs": ["gallas2007", "hcsc20"],
          "planned_experiment_ids": ["exp-c21-producer", "exp-c21-independent"]
        },
        {
          "claim_id": "C-005",
          "claim_text": "The apparent period-six/period-seven quadratic marker relation factors through period one and is not a primitive chronology-preserving bridge.",
          "intended_evidence_kind": "theoretical_exact_proof",
          "planned_refs": ["endlergallas2006chiral"],
          "planned_experiment_ids": ["exp-c21-producer", "exp-c21-independent"]
        }
      ],
      "manifest_negative_constraints": [
        {"constraint_id": "MNC-1", "rule": "Do not claim a cross-period Fredholm determinant or Hilbert--Polya operator."},
        {"constraint_id": "MNC-2", "rule": "Do not identify the period-six reversible marker with the period-six chiral ordered cover."},
        {"constraint_id": "MNC-3", "rule": "Do not claim classification of the full saturated period-seven scheme."},
        {"constraint_id": "MNC-4", "rule": "Keep Hénon period, chronological phase, Frobenius degree, and the source radical distinct."}
      ]
    }
  ]
}
```

## Literature matrix

| Source | Scalar orbit formulas | Class counts | Ordered-cover geometry | Chronological $H^1$ | Quality |
|---|---:|---:|---:|---:|---|
| Endler--Gallas (2002) | supports method | -- | -- | -- | P2 |
| Endler--Gallas (2004) | supports period-six carrier program | -- | -- | -- | P1 |
| Endler--Gallas (2006, orbital sums) | supports | supports low-period examples | -- | -- | P1 |
| Endler--Gallas (2006, chiral) | decisive $n=6$ input | identifies chiral doublet | silent | silent | P1 |
| Gallas (2007) | -- | decisive through all (n) | silent | silent | P1 |
| Friedland--Milnor (1989) | fixed-point multiplicity framework | -- | general automorphism boundary | -- | P1 |
| Hutz (2010) | formal-period terminology | -- | projective-morphism boundary only | -- | P1 |
| HCS-C12C | coarse marker genus zero | reproduces count boundary | quotient obstruction | invariant sector only | R |
| HCS-C20 | period-seven source lock | scoped component | exact (D_7), genus eight | nontrivial dimension 12 | R |
| HCS-C21 exact artifacts | reconstruct source formula | recompute $n\le7$ rows | exact $D_6$, genus one | $\tau^*=1$ at $n=6$ | reproducible internal exact result |

## Key themes

### Theme 1: the scalar period-six input is established prior art

**Evidence strength:** strong for formula provenance.

Endler and Gallas (2006) <!--ref:endlergallas2006chiral--><!--anchor:section:3-->
already give the class factorization, the first chiral marker, and the
factorization $P_6=f_{\eta}f_{-\eta}$.  Their phrase "proper in-phase
combinations" signals that chronology depends on how roots are paired, but
the inspected paper stops before defining a parameter-varying ordered-edge
normalization.  C21 therefore begins upstairs from a published carrier; it
does not rediscover the carrier.

Anchor justification: the cited section contains equations (11)--(15), the
exact formulas adopted by C21.

### Theme 2: restoring order changes geometry without guaranteeing a time spectrum

**Evidence strength:** strong exact internal evidence, not yet externally
peer reviewed.

The producer and non-importing checker jointly establish a connected
(D_6)-cover of genus one.  The critical synthesis is that two apparently
positive statements coexist:

1. ordered edges genuinely recover the radical and the full orbit, so point
   chronology has not been averaged away; and
2. the order-six automorphism is a torsion translation, so ordinary
   $H^1$ forgets the entire time character.

This resolves the apparent tension between "chronology survives" and "the
spectrum collapses": they refer to point-level dynamics and weight-one
cohomology, respectively.

Anchor justification: `results/c21_certificate.json` records the inverse
recovery, group, branch/genus, fixed-field, and representation ledgers;
`results/c21_independent_check.json` binds those exact bytes and recomputes
133 named checks.

### Theme 3: chirality and cohomological chronology have different thresholds

**Evidence strength:** strong within the stated component scope.

Gallas (2007) <!--ref:gallas2007--><!--anchor:none:--> proves that chirality
first appears at period six.  Locator warning: the full primary paper was
inspected during source audit, but no page/section locator was frozen in the
corpus record used for this synthesis.  HCS-C21 does not contradict that
result.  Instead, it changes the predicate: the unique period-six chiral
doublet has no nontrivial weight-one time sector, whereas the certified
HCS-C20 period-seven component has dimension twelve
([HCS-C20](../henon_period7_dihedral_cover/))<!--ref:hcsc20--><!--anchor:section:Exact%20D_7%20and%20genus%20theorem-->.

Anchor justification: the Gallas source supports the chiral class counts;
the HCS-C20 theorem and byte-locked certificate support the period-seven
genera and dimension calculation.

### Theme 4: a common number field need not be a dynamical bridge

**Evidence strength:** strong exact algebraic evidence; negative dynamical
interpretation.

The period-six reversible marker and period-seven chiral marker both reduce
to $D_1$, so their common field $\mathbb Q(A,\sqrt{A+1})$ is inherited
from fixed points.  The factorization into two graphs is thus explained
without any map between the full ordered covers.  A common field at the
coarse-marker level is too weak to support a Hecke, Euler-product, or
Hilbert--Pólya claim.

Anchor justification: exact symbolic substitution and fiber-product
factorization are recomputed by both C21 implementations.

## Contradictions and resolutions

| Apparent conflict | Resolution |
|---|---|
| Chirality first occurs at $n=6$, but C21 says a threshold occurs at $n=7$. | Different predicates: chiral orbit class versus nontrivial weight-one $\tau$-isotypic cohomology. |
| HCS-C12C reports genus-zero period-six marker components, while C21 reports genus one. | Different objects: coarse orbit-sum quotient versus the full ordered-edge splitting curve of the chiral doublet. |
| Exact order-six time survives on points, but $\tau^*=1$ on $H^1$. | A free finite-order automorphism of a genus-one curve is a torsion translation; translations are cohomologically trivial. |
| Period-six and period-seven markers share a quadratic field, but no primitive bridge is retained. | Both fields descend from the period-one marker; the relation is a lower-period alias. |
| Friedland--Milnor gives (2^n) fixed-point multiplicity, while exact primitive components may collide. | Total multiplicity, distinct geometric points, formal period, and primitive period are different notions. |

## Cross-paper tension inventory

```yaml
cross_paper_tensions:
  - pair_id: CP-001
    paper_a: endlergallas2006chiral
    paper_b: hcsc21_exact_artifacts
    candidate_basis: shared RQ subtopic
    overlap_topic: period-six chiral coordinate carrier versus its ordered-edge normalization
    a_finding: the scalar carrier factors into two conjugate cubics and roots require in-phase pairing
    a_evidence_pointer: Endler--Gallas 2006, Section 3, equations (11)--(15)
    b_finding: valid ordered pairings form a connected genus-one D6 splitting cover
    b_evidence_pointer: C21 certificate, ordered_cover_geometry
    pair_assessment: no_material_conflict
    resolution_status: not_applicable
    scholar_confirmation: confirmed
  - pair_id: CP-002
    paper_a: gallas2007
    paper_b: hcsc21_exact_artifacts
    candidate_basis: shared construct/outcome/measure
    overlap_topic: first period at which chirality or chronological cohomology appears
    a_finding: the first chiral doublet occurs at period six
    a_evidence_pointer: Gallas 2007 class-count formulas and n=6 row
    b_finding: the period-six chiral cover has trivial nonidentity time sector on H1, while the certified n=7 component has dimension twelve
    b_evidence_pointer: C21 certificate, chronology_threshold
    pair_assessment: conditional_difference
    resolution_status: resolved_in_synthesis
    resolution_pointer: Research Synthesis > Contradictions and resolutions, row 1
    scholar_confirmation: confirmed
  - pair_id: CP-003
    paper_a: hcsc12c
    paper_b: hcsc21_exact_artifacts
    candidate_basis: opposite finding direction
    overlap_topic: genus attached to period-six algebraic objects
    a_finding: coarse marker quotient normalizations have genus zero
    a_evidence_pointer: HCS-C12C derivation package
    b_finding: the chiral ordered-edge splitting curve has genus one
    b_evidence_pointer: C21 certificate, branch_and_genus
    pair_assessment: conditional_difference
    resolution_status: resolved_in_synthesis
    resolution_pointer: Research Synthesis > Contradictions and resolutions, row 2
    scholar_confirmation: confirmed
  - pair_id: CP-004
    paper_a: friedlandmilnor1989
    paper_b: hutz2010
    candidate_basis: shared construct/outcome/measure
    overlap_topic: fixed-point multiplicity, formal period, and primitive period
    a_finding: polynomial automorphism iterates have a degree-controlled total fixed-point multiplicity
    a_evidence_pointer: Friedland--Milnor 1989, Theorem 3.1 and Lemma 3.2
    b_finding: formal-period dynatomic multiplicities need not equal minimal-period loci
    b_evidence_pointer: Hutz 2010, dynatomic cycle construction
    pair_assessment: conditional_difference
    resolution_status: resolved_in_synthesis
    resolution_pointer: Research Synthesis > Contradictions and resolutions, row 5
    scholar_confirmation: confirmed
```

**Coverage note:** nine literature/repository sources and the C21 artifact
pair were included; four candidate pairs were assessed using shared RQ,
shared construct, or apparent opposite direction.  This is a scoped advisory
scan, not complete pairwise contradiction detection.  Cross-neighborhood
pairs may be missed, bibliographic coupling was not used to exclude any pair,
and the scholar must confirm the resolution pointers or add disputed pairs.

## Knowledge gaps

1. **Empirical/arithmetic:** no good-prime joint
   $\operatorname{Frob}^{r_F}\tau^s$ table has been computed for $E_6$.
   Such a table would be predicted to show only the trivial $\tau$-sector on
   $H^1$, but that finite-field statement is not needed for the
   characteristic-zero theorem.
2. **Theoretical:** no varying-period marked scheme ties (E_6) and (E_7)
   into a single algebraic family with an intrinsic repetition law.
3. **Methodological:** the novelty search was targeted and lacks a complete
   database/citation-network audit.
4. **Geometric:** the full saturated period-seven exact-period scheme and all
   lower-period nonchiral ordered covers have not been classified.
5. **Analytic:** no trace-class transfer operator, Fredholm determinant,
   functional equation, or Riemann divisor exists for the proposed tower.

## Evidence convergence map

```text
Strong:    [==========] published scalar provenance (multiple primary sources)
Strong:    [==========] exact C21 period-six geometry (two implementations)
Strong:    [==========] H1 chronology collapse (fixed-field + RH + checker)
Moderate:  [=======   ] n<=7 threshold (scoped adopted n=7 component)
Strong:    [==========] lower-period marker alias (exact identities)
Gap:       [          ] all-period determinant / Hilbert--Polya bridge
```

## Theoretical integration

The evidence supports a three-layer framework:

\[
\text{ordered points}
\longrightarrow
\text{equivariant cohomology}
\longrightarrow
\text{cross-period determinant}.
\]

C21 proves that the first arrow can lose all nontrivial time characters even
when the point dynamics is genuine.  It also proves that common arithmetic
fields at a coarse quotient need not lift through the second arrow, much less
the third.  This gives two useful rejection tests for future Hénon candidates:
compute the time action on cohomology before interpreting local factors, and
factor every cross-period marker coincidence through lower-period loci before
calling it arithmetic.

## Synthesis limitations

- The core theorem is an internal exact computation with independent code,
  not an externally peer-reviewed result.
- The period-seven comparison inherits HCS-C19/C20's adopted source-formula
  correction and component scope.
- The targeted literature search cannot establish global novelty.
- The synthesis intentionally draws no Riemann-zero or operator conclusion.
