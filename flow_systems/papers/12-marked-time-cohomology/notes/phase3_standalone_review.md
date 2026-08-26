# Paper 12 Phase-3 independent standalone and nonredundancy review

Review date: **2026-08-15 (Asia/Shanghai)**  
Reviewer role: **independent devil's advocate, standalone/nonredundancy lane**  
Mathematical-scope verdict: **PASS at the frozen hypotheses**  
Standalone verdict: **`NOTE_OR_MERGE`**  
Finding count: **C0 / M1 / m0**

## 1. Scope, independence, and decision rule

This review applies the ARS academic-reviewer devil's-advocate and integrity
discipline to the stable Paper-12 Phase-3 tuple. It tests whether the proved
material is sufficiently nonredundant for a standalone paper; it is not a
Route evaluation, manuscript review, citation audit, or release gate.

The review was conducted without browsing, without modifying any stable
proof, source, control, lock, Route, or manuscript artifact, and without
reading any other new Paper-12 Phase-3 reviewer report. The only file written
by this lane is this report.

The controlling rule is not merely a checklist of whether formulas exist.
The active protocol expressly requires `NOTE_OR_MERGE` if the package reduces
to Paper 11's factorization plus a routine degreewise bar-complex corollary
and Deninger's already-owned stabilizer. Therefore syntactic completion of
`P12-1`--`P12-9` cannot by itself establish `STANDALONE_PASS`; the new theorem
content must also survive that semantic nonredundancy stop.

## 2. Exact-byte evidence binding

### 2.1 Active design and amendment tuple

| Artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `9213d6e27505c09dbfc24899a15dcca9670e897e754fe40efbc9c1ae7248f434` |
| `notes/candidate_lock.md` | `f0878aaf97e44041460b05c59acd5b5a45fd6d1bef2d7042e3ad273de5320d1c` |
| `notes/phase1_design_amendment.md` | `76684044f434c8084712e558c32ee47e996a84763a3eca405f7014ab3d77f949` |
| `notes/phase1_design_amendment_v2.md` | `26222c9e6888f0aa45d019a9f1fd74038285ac460ae6aa0342b8b4e01b4c3285` |

### 2.2 Phase-2 source, owner, novelty, and final gate

| Artifact | SHA-256 |
|---|---|
| `notes/phase2_framework_source_audit.md` | `32560640ce95894f3b60191593ce55cbcc50a3dd4ce713b148d96cd96bcdfdcb` |
| `notes/sources/coh-source-manifest.md` | `77adde8e38853b4623212eaf60aee68f5c0d76112d859c643c061fb5b2fddb22` |
| `notes/sources/coh-sources.sha256` | `4a64a9de52d6f2b0b192778afc19b183929818aea3698f3afb9043fab12c20a4` |
| `notes/phase2_category_owner_audit.md` | `8fad79f121439145e0ac3cac7ca67e82f3e2ad6af86da5b0f001e92da30e1d62` |
| `notes/phase2_novelty_search.md` | `c4584862824dbaadec9945fb85defd6d11ee7822849471b075ff4d90d57ca1bd` |
| `notes/phase2_final_review.md` | `032d558fecdccc492ce59733e20dd9322f573d033355aee3c74563680cea2ea7` |
| `notes/phase2_final_gate.md` | `1b05110e23f23848442742b415811205ef24616413b59989996993d4297be9ab` |

### 2.3 Inherited Papers 9--11 proofs

| Artifact | SHA-256 | Exact inheritance tested here |
|---|---|---|
| Paper 9 `notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | actual packet/orbit indiscreteness and every-unit topology owner |
| Paper 10 `notes/proof_audit.md` | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` | separated collapse and standard-to-actual one-sided topology |
| Paper 11 `notes/proof_audit.md` | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | arrow chart, `T0` time factorization, and action-blind convolution boundary |

### 2.4 Stable Phase-3 proof/control tuple

| Artifact | SHA-256 |
|---|---|
| `notes/phase3_core_proofs.md` | `9ab5c860f2ceceba27aa820ddd66564f9a7be2f2ee21bc06ea7110d1c38c16cd` |
| `notes/phase3_marked_packet_proofs.md` | `3cf4a29d97499e1875d8f5bbfb1124d88e45e972ad3dbadbe6b8fffb5a3e6d49` |
| `results/manifest.json` | `5337f13b07498872a97ed0d13f0ff0f5ffbcea9e3e37bf8e0c558c3e966e5d3a` |

Every hash above was independently recomputed immediately before this report
was written and matched the displayed value.

## 3. Strongest counter-argument

Paper 12 proves a correct collection of consequences of one exceptionally
degenerate topology, but it does not yet prove a sufficiently independent
central theorem. For every nerve degree, the transformation-groupoid chart
is the standard `X x R^n` chart. Indiscreteness then makes points with the
same time tuple topologically indistinguishable, so the Paper-11 `T0` target
argument applies degree by degree. The chain map is the ordinary bar-face
calculation. In degree one, the remaining calculation is the continuous
Cauchy equation. On isotropy, the marked coordinate is literally
`c(x,t)=t`, so its image is the stabilizer; Deninger already owns the fact
that every fixed-prime packet unit has stabilizer `(log p)Z`.

The category layer is internally coherent but does not add comparable
mathematical depth. Scaled covariance is the defining equation
`c' o F=alpha c` restricted to isotropy. Unequal-period non-descent is the
standard dilation between `R/LZ` and `R/MZ`; orientation reversal supplies a
correct nonconverse. The pointed quotient target is chosen so that, once
`H=H'`, there is only one basepoint-preserving strictly equivariant map.
Consequently its functor deliberately sends different strict morphisms to
the same arrow and is not faithful. The one-sided topology is the already
known fact that maps into an indiscrete space are continuous while a
nonconstant map out to a Hausdorff quotient is not.

Thus the package is a careful and useful boundary note, but its load-bearing
steps remain standard nerve formalism, Paper-11 factorization, standard
homogeneous-space algebra, and an already-owned source stabilizer. The
bounded absence of one source containing the entire assembled package does
not change that reduction.

## 4. Mathematical stress tests

The standalone failure is not based on a fabricated counterexample. The
following adversarial attempts were made against the actual claims.

| Attack | Attempted counterexample/calculation | Result |
|---|---|---|
| all-degree nerve chart | allow arbitrary, nonfree, nontransitive right actions and test whether composability retains hidden unit coordinates | `Psi_n` remains bijective and the subspace opens pull back to `X x U`; no counterexample |
| `T0` factorization | seek a continuous cochain that distinguishes `(x,t)` and `(y,t)` | impossible for a `T0` target because the source points have identical neighbourhoods; the non-`T0` indiscrete two-point coefficient correctly breaks the result |
| chain-map signs | test the unit-changing first face and adjacent multiplication faces | projected faces are the usual bar faces; alternating cancellation survives |
| real `H^1` | try quadratic, affine-nonadditive, or discontinuous additive profiles | quadratic/affine profiles fail the cocycle law; discontinuous additive profiles are excluded by continuity; `H_cnv^1=R[c]` survives |
| strict invariance | seek a strict marked isomorphism between `LZ` and `MZ`, `L!=M` | strict clock preservation fixes each isotropy time, forcing `LZ=MZ` and hence `L=M`; no counterexample |
| scaled covariance direction | test `alpha=M/L` against its reciprocal | `F_alpha([r],t)=([alpha r],alpha t)` gives `MZ=alpha LZ`; the reciprocal is the inverse map, not the forward scale |
| orientation reversal | test exact subgroup equality without strict preservation | `F_-([r],t)=([-r],-t)` is a valid unmarked involution, preserves `LZ`, and changes the mark sign; this confirms the stated nonconverse |
| dense period | use `H=Q` and a nontrivial positive rational scale | `qQ=Q` gives a non-strict scaled automorphism with unchanged subgroup; it confirms why universal-loss wording is excluded and lies outside the lattice object class |
| arbitrary/free/trivial periods | use `H=R`, `{0}`, or an arbitrary subgroup | the generic construction accepts them all; this confirms action/arithmetic blindness rather than refuting the scoped lattice category |
| nontransitive packet analogue | combine orbit components with stabilizers `Z` and `2Z` | unit independence fails without transitivity exactly as declared; the generic cochain collapse still survives |
| proxy topology | try to make the actual indiscrete-to-standard inverse chart continuous | impossible for the nonconstant map into the nontrivial Hausdorff quotient; standard-to-actual continuity is correct |
| owner credit | try to attribute topology/groupoid/cohomology to Deninger or the stabilizer to Paper 12 | the reports keep Deninger, Paper 9, Paper 11, and Paper 12 owners separate; no owner splice was found |

These checks support the mathematical-scope `PASS`. They do not support a
standalone decision because they test correctness, not theorem weight.

## 5. Component-by-component nonredundancy audit

### 5.1 `P12-1`--`P12-3`: correct but routine all-degree extension

For every transformation groupoid, the composable nerve has the standard
set chart `X x R^n`; the only special topology step is that every open is
`X x U`. The all-degree factorization then repeats the same
topological-indistinguishability lemma that Paper 11 used at arrow degree.
The face projection and `d^2=0` calculation are standard simplicial/bar
formalism.

Blanco--Uribe--Waldorf already provide the closest named all-face continuous
cochain complex at the audited real-coefficient strength. This does not prove
the owner-specific collapse, but it removes novelty from merely defining the
complex and differential. The residual collapse is an elementary degreewise
application of the Paper-11 mechanism, not a new higher-cohomological method.

Adjudication: **mathematically closed; insufficient standalone weight**.

### 5.2 `P12-4`--`P12-6`: Cauchy plus identity-on-stabilizer

Once one-cochains factor through time, `d^1b=0` is exactly the continuous
Cauchy equation, and degree-zero real cochains are constant. Restriction of
`c(x,t)=t` to `G_x^x` is the inclusion `H_x -> R`. The fixed-orbit and
packet formulas then insert Deninger's already-owned every-unit stabilizer.

The representative-independence check is correct and worth stating, but a
coboundary vanishes on isotropy for the elementary reason `r=s` there. The
`PACKET_COROLLARY` is a valid same-owner application, not a new derivation of
the arithmetic period.

Adjudication: **mathematically closed; arithmetic result inherited rather
than independently generated**.

### 5.3 `P12-7`: coherent categorical boundary, but primarily definitional

The three categories are well typed, their composition/inverse rules close,
and the positive covariance direction is correct. The explicit dilation and
orientation reversal are useful falsifiers. Nevertheless:

- covariance is obtained by applying the defining clock-intertwining
  equation to isotropy;
- the unequal-period example is the standard scalar isomorphism of
  homogeneous quotients;
- orientation reversal is the scalar `-1` version after forgetting the mark;
  and
- the arbitrary/dense/nontransitive controls show that the construction has
  no arithmetic selectivity before the Deninger label is inserted.

This is a clean taxonomy of which data are remembered, but it is not yet a
classification of all marked/unmarked morphisms, an equivalence of
categories, or another nonformal rigidity theorem.

Adjudication: **coherent and useful; not sufficient to reverse the routine-
reduction branch**.

### 5.4 `P12-8`: correct but deliberately lossy pointed functor

The target category is rigid by definition: a basepoint-preserving strictly
`R`-equivariant map is forced to be `[t]_H |-> [t]_(H')`, and it exists only
when `H=H'`. The resulting `S` is a functor, but all strict morphisms between
the same two objects receive that unique target arrow. The proof itself
correctly says faithfulness is not claimed.

The actual chart and its topology direction are also correct, but they
repackage the standard orbit-stabilizer bijection and Paper-10 separation
direction. The scaled stop is the standard distinction between strict
equivariance and semilinearity.

Adjudication: **correct proxy record; too coarse to supply the missing
standalone categorical theorem**.

### 5.5 `P12-9`: strong controls, negative for specificity

The controls were independently rerun after reading the manifest:

```text
unit tests:       88/88 PASS
strict verify:    PASS
CSV artifacts:   10
CSV rows:        234
negative cases:  12
manifest SHA-256: 5337f13b07498872a97ed0d13f0ff0f5ffbcea9e3e37bf8e0c558c3e966e5d3a
cache scan:       PASS
```

The finite controls support the formulas and catch sign, scale, topology,
coefficient, and promotion errors. They are not universal proofs. Their
strongest relevance to standalone status is adverse: all 24 label
permutations retain one theorem signature and are explicitly marked
`PROVES_TOO_MUCH`. This confirms that the generic mechanism does not select
the rational-Witt period or a prime label.

### 5.6 Bounded novelty search

The Phase-2 search validly reports `SUPPORTED_WITHIN_SEARCH` and no direct
source satisfying its conjunctive `D1 AND D2 AND D3 AND D4` package test.
That is not disputed. It does not establish that the assembly is a
substantive new theorem: a conjunction can have no single-source precedent
even when every implication in the conjunction is standard or immediate
from already-cited results. The active protocol anticipated exactly this
failure mode and retained the routine-reduction stop.

Adjudication: **the direct-precedent trigger is inactive, but the independent
routine-reduction trigger is active**.

## 6. Main finding

### M1 — the proved package fails the locked standalone nonredundancy stop

The proofs are correct at their frozen scope, but their load-bearing content
reduces to:

```text
standard transformation-groupoid nerve chart
  + Paper-11 T0 time factorization applied degreewise
  + standard bar differential and continuous Cauchy calculation
  + identity time coordinate restricted to isotropy
  + Deninger's already-owned every-unit p^Z / (log p)Z stabilizer
  + standard homogeneous-space dilation, reversal, and quotient formalism.
```

This is the precise reduction for which the active protocol mandates
`NOTE_OR_MERGE`. The category and proxy sections improve exposition and
prevent overclaim, but the present pointed functor is deliberately
nonfaithful and the covariance/non-descent proofs are immediate from the
chosen definitions. They do not create a sufficiently independent theorem
core under the frozen gate.

Evidence anchors:

- `text: notes/research_protocol.md §1 — "routine degreewise bar-complex corollary and Deninger's already-owned stabilizer"`
- `text: notes/phase2_category_owner_audit.md §1 — "bare all-degree continuous nerve complex has a close named primary precedent"`
- `text: notes/phase3_marked_packet_proofs.md §5.2 — "faithfulness is not claimed"`
- `dataset: results/manifest.json metrics.all_label_rows_prove_too_much=true`

Confidence: **5/5 — direct audit of the frozen protocol, inherited proofs,
both Phase-3 proofs, source/novelty conclusions, and reproduced controls**.

Decision impact: **Major**, not Critical. No frozen theorem is invalidated;
the mathematics survives as a technical note or merged section. Substantial
repositioning or a genuinely stronger theorem is required for a standalone
article, which is exactly the Major band.

Required disposition under the current locks:

1. Prefer merging the material into Paper 11 as the cohomological/marked
   boundary of the same time-factorization collapse; or
2. retain it as an explicitly scoped technical note, without standalone
   novelty language.

## 7. Concrete possible flip point, not credited to the current tuple

There is a stronger theorem latent in the setup, but it is not present in
the v2 target or proof tuple.

For a strict object, choose any unit `x` and define

```text
q_x:R->X,  q_x(t)=x dot t.
```

Transport the usual quotient topology of `R/H` to the same underlying
`R`-set `X`. This topology is basepoint-independent: if `x'=x dot u`, then

```text
q_(x')=q_x o T_u,
```

where `T_u` is translation by `u`, a homeomorphism of `R`. A strict marked
isomorphism forces

```text
F(x,t)=(F_0(x),t),
F_0(x dot t)=F_0(x) dot t,
```

so `F_0` becomes an unpointed standard homogeneous-space homeomorphism.
Conversely, every such equivariant homeomorphism uniquely lifts to a strict
marked groupoid isomorphism. This yields a full-and-faithful functor, and
with the inverse indiscrete-retopologization construction can be organized
as an equivalence with an unpointed standard homogeneous-space category.
Unlike the current pointed `S`, it retains unit translations and does not
collapse every strict arrow to the unique basepoint-preserving map.

This is the smallest plausible repair to the weakest categorical component,
but it cannot alter this review:

- it is not a theorem in the current `P12-8` lock or either stable Phase-3
  proof;
- adding it as a central claim requires a versioned v3 amendment and fresh
  source/novelty/applicability review; and
- it remains close to standard homogeneous-space formalism, so even after
  proof it would be a plausible standalone repair, not an automatic
  standalone pass. A stronger classification or other nonformal consequence
  may still be necessary.

## 8. Final gate adjudication

| Locked condition | Status | Standalone effect |
|---|---|---|
| all-degree nerve/cochain chain reduction | correct | routine degreewise extension of the inherited mechanism |
| real `H^1` and representative-independent isotropy image | correct | Cauchy plus elementary restriction |
| every-unit `PACKET_COROLLARY` | correct at the audited owner | arithmetic stabilizer/clock remain source-owned |
| strict/scaled/unmarked covariance and examples | correct | coherent but primarily definitional/formal |
| pointed quotient functor and one-sided topology | correct | deliberately lossy, nonfaithful standard proxy |
| deterministic controls | 88/88 and strict verification PASS | validate boundaries; demonstrate action/label blindness |
| bounded direct-precedent search | `SUPPORTED_WITHIN_SEARCH`; no exact package precedent found | does not defeat the routine-reduction stop |
| substantive nonredundancy beyond Papers 9--11 and standard background | **not established** | **mandatory `NOTE_OR_MERGE`** |

Final machine-readable disposition:

```text
PHASE3_MATHEMATICAL_SCOPE=PASS
PACKET_RESULT=PACKET_COROLLARY
ORBIT_ONLY=false
DIRECT_PRECEDENT_FOUND=false
NOVELTY_CEILING=SUPPORTED_WITHIN_SEARCH
ROUTINE_REDUCTION_TRIGGER=true
STANDALONE_PASS=false
STANDALONE_DECISION=NOTE_OR_MERGE
CRITICAL_OPEN=0
MAJOR_OPEN=1
MINOR_OPEN=0
PREFERRED_DISPOSITION=MERGE_WITH_PAPER11
V3_RETROPOLOGIZATION_EQUIVALENCE=CANDIDATE_ONLY_NOT_REVIEWED
ROUTE_OR_MANUSCRIPT_AUTHORIZED_BY_THIS_REVIEW=false
```

**Final verdict: `NOTE_OR_MERGE` (`C0/M1/m0`).** The stable mathematics may
be preserved, but it should not be released as a standalone Paper-12 article
under the present locks.
