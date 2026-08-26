# Paper 12 independent peer review — round 1 final

## Manuscript information

- **Title:** *Marked Time Cohomology and Orbitwise Standardization of
  Indiscrete Arithmetic Action Groupoids*
- **Author:** Liang Wang
- **Review date:** 2026-08-15 (Asia/Shanghai)
- **Reviewer role:** independent ARS methodology/domain/devil's-advocate
  manuscript reviewer
- **Review focus:** theorem and proof validity; source, owner, topology, and
  category typing; variance; fixed-prime packet fidelity; Route semantics;
  citation and integrity; deterministic controls; strict figure/table trace;
  clean build; complete PDF presentation; and package/release boundaries
- **Final scientific verdict:** **ACCEPT / exact-lock PASS — C0/M0/m0**
- **Confidence:** **5/5**

This verdict applies only to the exact internal scientific candidate bound
below. Public or journal submission remains conditional on the human,
companion-identity, venue-policy, and repository/archive exclusion gates in
Section 12. The review was read-only: the reviewer did not edit the
manuscript, bibliography, figures, PDF, either README, proofs, controls,
Route records, sources, or results and did not run Git. The only review write
is this report.

## 1. Exact candidate and upstream evidence lock

### 1.1 Final Review Freeze 2 tuple

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` |
| `paper/references.bib` | `e1f4d0f6589ce0710173bad1c0089b5d6746d09010cc448d6d387ad8c9e17dcf` |
| `paper/figures/same_carrier_diagonal.tex` | `a83148600d497dd1b91510f5707a1b1a9402c35689013a1fa904978206ff5cf1` |
| `paper/figures/packet_four_way_firewall.tex` | `9a52c273e91878d4dd74f96bd27fe299be39d98cdbebdda6bc800d89184b6908` |
| `paper/paper.pdf` | `3fda5ae01fd3b7a78ddbefb11a62befa4d2ab50906b112b39e3c48e89901a294` |
| `paper/README.md` | `149bb1c9177f629fd5e04defa48ce17716cad85ea9d51dd0a8135e79b2214a7f` |
| project `README.md` | `a156deefbb059d840f73bfd6d76d468300158ad0e8c8bffef81b7a355c2cec51` |

All seven hashes were recomputed immediately before this report was frozen.
The two README hashes include the final receipt-only normalization of the
abstract-count methods: 205 `detex` whitespace-delimited English prose words
with displayed mathematics excluded, and 370 Unicode Han code points. That
normalization changed neither manuscript nor PDF content.

The final `paper/` directory contains exactly six files, exactly one PDF
(`paper.pdf`), the two declared native TikZ sources, and no build auxiliary
or research-source PDF.

### 1.2 Controlling scientific and source gates

The principal immutable inputs and final audit gates were independently read
and re-hashed.

| Evidence artifact | SHA-256 | Role |
|---|---|---|
| `notes/composition_blueprint.md` | `b343dd47d4a4e2fc7b8570c33eb3270542732a4062142b1ef79530393000e107` | composition, owner, and claim blueprint |
| `notes/proof_audit.md` | `c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab` | integrated proof audit |
| `notes/phase3_peer_review.md` | `7d3ddb6d28d425695696965b73caeaa109f5a5cc27c1c52fd8fb826138818f36` | pre-manuscript independent proof review |
| `notes/route_audit.md` | `2baf2b1ea63e5573f4b2673da6329520163ec67d76b002cb6f84fcf45c0ac102` | exact eight-owner Route audit |
| `results/manifest.json` | `7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95` | 122-test controls manifest |
| `notes/phase3_v4_final_gate.md` | `974a3f1be30aeaced279b31b3d403450e292144802370c7515e3e3ac644f41e0` | final v4 gate |
| `notes/phase3_v4_integrated_gate.md` | `2b23ecc9462431dbebd12a6af5994a09a7f7d7e37bad10f1f11d118aa3ecc9c4` | integrated v4 gate |
| `notes/phase3_v4_route_provenance_relock.md` | `20c67ace45b81523400053b388923e4a01c725b0bfdd528f2c391803ded0cb4d` | Route provenance re-lock |
| `notes/phase3_v4_status_relock.md` | `64a63d8b7565add4047875c9610a408d1e4264b8e205e600814de778b93ab90d` | standalone/status re-lock |
| `notes/phase3_v4_source_novelty_audit.md` | `cf985db1270bb6b1480f0b29a7770e0865a627ea2412adfc6c4476eeba439c22` | source and bounded-novelty gate |
| `notes/pre_manuscript_citation_audit.md` | `3a15bb9496b2cc949eb3e05f9b7cf8e73950ad77d491b39a207da740ef405564` | frozen manifestation, locator, and citation plan |
| `notes/phase3_orbitwise_standardization_h1_proofs.md` | `77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8` | final standardization, automorphism, and degree-one proof |
| `notes/phase3_v4_math_review.md` | `97dbd63fae6d35ae627520203db98d7c497a927a505599c0855231ac3f3b4e07` | final mathematics review |
| `notes/phase3_v4_controls_review.md` | `886a2648473035bb4d3600a03474680d3f692b1bdca08034096c6e7eebd664e6` | controls interpretation boundary |
| `notes/phase3_v4_standalone_review.md` | `639dc289c024588777a05d46ff9e5cd47b6e50ceeb807ef7571776d0301e6895` | standalone-fidelity review |
| `notes/citation_audit.md` | `f599dfbf67026b0985ee0e09b4e41bb24e3fe94709a1cd5e03ba657fb2a4fcaf` | final citation/source-integrity exact lock, C0/M0/m0 |
| `notes/sources/coh-source-manifest.md` | `77adde8e38853b4623212eaf60aee68f5c0d76112d859c643c061fb5b2fddb22` | source manifestation ledger |
| `notes/sources/coh-sources.sha256` | `4a64a9de52d6f2b0b192778afc19b183929818aea3698f3afb9043fab12c20a4` | five retained PDFs plus five preflight sidecars |

The final citation audit is independent of this report and binds the same
seven candidate hashes. Its final citation graph is 27 citation commands,
31 key occurrences, 14 unique keys, and exactly 14 bibliography entries.

## 2. Review method and overall assessment

The review followed the ARS academic-paper-reviewer workflow with dedicated
methodology, mathematical-domain, devil's-advocate, formatter, citation,
integrity, figure/table-trace, and full-PDF visual passes. Findings were
graded by the decision impact of each individual defect:

- **Critical:** invalidates the central result or blocks acceptance;
- **Major:** requires substantive repair of a proof, central claim,
  owner/domain boundary, or reproducibility conclusion;
- **Minor:** requires a local mathematical, explanatory, citation, or
  presentation repair.

No issue at any of those thresholds remains in the exact tuple.

The paper establishes a coherent two-topology comparison on the same
right-real-action carrier. On the actual globally indiscrete owner, its
author-defined unnormalized continuous nerve complex factors through time in
every finite degree for `T0` coefficient targets; for real coefficients,
degree one is the single time-slope line and its coboundaries vanish. Under a
common cocompact stabilizer, the paper constructs a section-free coproduct of
standard orbit topologies, proves its categorical relation to global
indiscretization, computes the abstract automorphism extension, and obtains
the full algebraic product of independent orbit slopes in standardized
degree one. The continuous identity points from standard to actual, so
contravariant pullback identifies the actual line with the constant diagonal,
which is exactly the strict time-preserving automorphism invariant subspace.

The proofs are direct, the assumptions and variance are explicit, and the
fixed-prime application preserves the four distinct owner/topology records.
Controls and Route results are stated at their proper finite/negative-evidence
ceilings. The result is specialized, but the exact standardization,
arbitrary-set automorphism extension, degree-one computation, and invariant
diagonal form a nonredundant technical contribution on the bounded claims
made.

## 3. Strengths

### S1. The author complex is explicit and internally verified

The manuscript fixes the range-first action-groupoid convention, writes all
finite nerve charts and face maps, proves the simplicial face identity, and
derives `d^2=0` rather than importing an adjacent cohomology theory. Degree
zero is included, and the signs used later agree with the original
differential.

**Evidence Anchor:** `text/equation: manuscript Proposition prop:nerve,
Definition def:complex, and Proposition prop:d-square, PDF pp. 4–5`

### S2. Actual-topology collapse and real degree one are proved at the exact domains

The all-degree factorization theorem places `T0` on the coefficient target
and does not enlarge it to arbitrary targets. The real degree-one theorem
uses the continuous Cauchy equation, obtains precisely `R[c]`, and separately
proves that actual degree-one coboundaries vanish. The manuscript does not
claim a topology on cohomology.

**Evidence Anchor:** `text/equation: manuscript Theorems thm:factorization
and thm:actual-h1, equations eq:time-pullback and eq:actual-h1, PDF pp. 5–6`

### S3. The mark and category boundaries are directionally sharp

The marked isotropy image is defined on each unit and proved to be
`lambda H_x`. Strict maps preserve it, positive scaled maps transform it
covariantly, and explicit dilation/orientation-reversal examples show why
weaker categories do not preserve the normalized period. The fixed-prime
specialization uses the source-normalized logarithmic clock and concludes
`(log p)Z` at every unit without promoting that fact across categories.

**Evidence Anchor:** `text/equation: manuscript Definition def:period,
Proposition prop:period, equations eq:scaled-covariance–eq:orientation-reversal,
and Corollary cor:packet-period, PDF pp. 6–8`

### S4. Orbitwise standardization is section-free and categorically exact

For common stabilizer `H=LZ`, the standard topology is constructed orbit by
orbit from quotient charts, proved independent of orbit origin, and then
assembled by topological coproduct. The uniqueness theorem has the correct
one-sided identity direction. `Std` and global indiscretization are proved
fully faithful/inverse on the declared categories; an unstated reverse
continuous identity is never used.

**Evidence Anchor:** `text/equation: manuscript Definition def:std,
Theorems thm:std-topology and thm:equivalence, and equation
eq:identity-direction, PDF pp. 8–10`

### S5. The automorphism extension separates canonical structure from choice

The exact sequence
`1 -> (R/H)^Q -> Aut_R(Std X) -> Sym(Q) -> 1` has a canonical kernel
description. Surjectivity and a splitting are correctly attributed to ZFC
choice of orbit origins, and the split is explicitly noncanonical. The
argument works for an arbitrary nonempty bare orbit set rather than silently
assuming countability or a preferred enumeration.

**Evidence Anchor:** `equation/text: manuscript Theorem
thm:automorphism-extension, equations eq:automorphism-extension,
eq:kernel-rotation, and eq:choice-lift, PDF pp. 9–10`

### S6. Standardized degree one and the invariant diagonal are computed without topology drift

The slope map identifies standardized degree one with the full algebraic
Cartesian product `R^Q`; potential reconstruction proves injectivity, and an
explicit potential records that standardized boundaries are generally
nonzero. The comparison functor has the correct direction
`J:G_std -> G_actual`, while `J*` is contravariant. The raw slope action is
`lambda o sigma`; the declared left action uses the inverse, and its
invariants are exactly the constant functions.

**Evidence Anchor:** `text/equation: manuscript Lemma lem:slope, Theorems
thm:standard-h1 and thm:invariant-diagonal, equations eq:J–eq:invariants,
PDF pp. 10–13`

### S7. The fixed-prime application preserves every source and topology firewall

Deninger supplies the flow, logarithmic clock, and stabilizer data; the
companion supplies the actual global-indiscrete topology; Paper 12 owns the
constructed standardization and cohomology comparison. The actual packet,
standardized packet, actual quotient, and discrete component index remain
four distinct typed records. Only the nonempty bare orbit set crosses the
declared comparison; no count, enumeration, measure, local triviality, or
actual quotient topology is transferred.

**Evidence Anchor:** `table/figure/text: manuscript Table tab:packet-types,
Corollary cor:packet-comparison, Figure fig:packet-four-way-firewall, and
Section sec:four-way, PDF pp. 3–4 and 13–14`

### S8. Reproducibility and Route claims are exact and appropriately negative

The controls report 122/122 tests, 11 CSVs, 3,486 rows, and 14/14 intentional
negatives; the prose repeatedly says these finite witnesses do not prove the
real, arbitrary-`Q`, choice, topology, source, or arithmetic theorems. The
eight Route records remain owner-specific, all A2–A4 coordinates fail, and
Route B is closed without coordinate splicing.

**Evidence Anchor:** `dataset/table: controls manifest
7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95;
manuscript Tables tab:controls and tab:route, PDF pp. 14–16`

### S9. The presentation and trace ledger make the boundaries independently inspectable

Both native TikZ figures and all three manuscript tables have prose
equivalents and strict six-key trace entries. The bilingual abstracts follow
the same twelve-fact order with the same qualifications, and the PDF places
figures/tables without interrupting proofs or moving Route material behind
the bibliography.

**Evidence Anchor:** `figure/table: paper/README.md figure_table_trace;
manuscript bilingual abstracts, Figures fig:same-carrier-diagonal and
fig:packet-four-way-firewall, and Tables tab:packet-types, tab:controls,
tab:route`

## 4. Weaknesses

None at Critical, Major, Minor, or copyedit threshold remains in the exact
candidate.

## 5. Coverage receipt for the empty Weaknesses list

**Covers:** Weaknesses

| Dimension examined | What was checked | Basis for no remaining weakness |
|---|---|---|
| Definitions and conventions | right action; range/source; multiplication and inverse; finite nerve charts; unnormalized cochains; mark; strict/scaled/unmarked morphisms | Every subsequent formula uses the declared range-first and sign conventions; no adjacent theory is silently substituted. |
| Face identities and complex | all face cases, including degree zero; alternating signs; `d^2=0` | The cancellation proof covers the full defined complex and agrees with finite controls. |
| Actual factorization and `H^1` | `T0` target hypothesis, time pullback, continuous Cauchy equation, actual boundaries | The result is neither widened to non-`T0` coefficients nor topologized; `B^1=0` is proved separately. |
| Marked periods and categories | isotropy image, normalized mark, strict preservation, positive scaling, dilation, orientation reversal | Each positive and negative statement stays in its declared category; no false descent remains. |
| Standardization | common nonzero cocompact lattice, quotient charts, origin independence, coproduct topology, uniqueness, identity direction | Mixed stabilizers and the reverse identity direction are explicitly excluded. |
| Categorical equivalence | objects, strict time-preserving maps, `Std`, global indiscretization, full/faithful claims | The equivalence is confined to the constructed common-lattice category and does not become a separated reflection. |
| Automorphisms and choice | orbit permutation, kernel rotations, surjectivity, abstract exact sequence, splitting | Canonical kernel, choice-dependent surjectivity, and noncanonical split are not conflated; no countability assumption enters. |
| Standardized cohomology | slope map, representative reconstruction, potentials, nonzero coboundary example, full `R^Q` | Degree one only is claimed; no topology, boundedness, direct-sum, or higher-degree conclusion is inferred. |
| Comparison and variance | continuous `J`, contravariant `J*`, constant diagonal, raw/right versus declared left action, invariants | Map direction and inverse in the left action are consistent in theorem, proof, figure, abstract, and conclusion. |
| Source and owner integrity | Deninger, three companions, routine topology background, comparator literature, Paper-12-owned proofs | Source-owned premises are not credited to Paper 12, and comparator theorems are not applied outside their domains. |
| Fixed-prime packet typing | actual/standard packet, actual quotient/discrete index, bare `Q_p`, period statement | No orbit count, measure, topology transfer, cross-prime conclusion, or full-suspension claim remains. |
| Route semantics | eight exact owners, A0–A4 tuples, evidence status, adversarial verdicts, Route-B flags | Six records are exploratory and two rejected; every A2–A4 fails; every determinant field is `NONE_BY_DESIGN_NO_DETERMINANT_OBJECT`; no owner splicing occurs. |
| Deterministic controls | generator/test semantics, standard-library-only execution, exact arithmetic boundary, intentional negatives, byte identity | The official serialized run passed and controls are described only as finite regression witnesses/falsifiers. |
| Citations and bibliography | 27 commands, 31 occurrences, 14 unique keys, 14 records, manifestations, locators, dates, companion status | Sets close exactly; no missing/orphan/decorative citation remains; source strength and publication/preprint distinctions are preserved. |
| Bilingual fidelity | both abstracts against the twelve-slot fact ledger and stated count methods | Both remain within target lengths, use the same order/qualifiers, and preserve all negative boundaries. |
| Figure/table trace | two figure sources, three tables, captions, adjacent prose, all five six-key YAML entries, reverse links | Each artifact has exactly `artifact_id`, `source_data`, `transformation`, `caption_claim`, `supported_manuscript_claims`, and `limitations`; every label resolves in both directions. |
| Build and visual quality | clean documented build, extracted text, final log, 18 rendered pages, fonts, PDF structure | No unresolved reference, box defect, missing glyph, clipping, overlap, split proof/sentence, or unreadable artifact remains. |
| Declarations and release integrity | author/declaration placeholders, companion identities, source-PDF exclusion, public-sync limitations | All unverified human or external facts are conspicuous conditions rather than fabricated declarations. |

## 6. Theorem-by-theorem adjudication

| Result | Final audit | Boundary verified |
|---|---|---|
| Proposition `prop:nerve` | PASS | Every finite nerve chart is identified with `X x R^n`; the global indiscrete unit coordinate is retained as an owner fact rather than erased set-theoretically. |
| Proposition `prop:d-square` | PASS | The face identity and alternating cancellation prove `d^2=0` for the author complex, including the degree-zero action/source-range laws. |
| Theorem `thm:factorization` | PASS | Every finite-degree cochain with `T0` coefficient target factors uniquely through time; no non-`T0` promotion is made. |
| Theorem `thm:actual-h1` | PASS | Real cocycles are precisely global time slopes and actual degree-one coboundaries vanish. |
| Proposition `prop:period` | PASS | The marked isotropy image is exactly `lambda H_x` with the stated source normalization. |
| Corollary `cor:packet-period` | PASS | Deninger's every-unit `p^Z` stabilizer and logarithmic clock give `(log p)Z` at every fixed-prime packet unit. |
| Theorem `thm:std-topology` | PASS | Common-period orbit topologies and their coproduct are section-free; uniqueness and the one continuous identity direction are correct. |
| Theorem `thm:equivalence` | PASS | `Std` and global indiscretization give the declared exact categorical equivalence on strict common-lattice owners. |
| Theorem `thm:automorphism-extension` | PASS | The kernel is canonically `(R/H)^Q`; arbitrary orbit permutations lift using choice; any split depends on chosen origins. |
| Lemma `lem:slope` | PASS | Orbit slope is well-defined and canonical; representative and potential formulas have the correct periodicity/sign. |
| Theorem `thm:standard-h1` | PASS | Standardized degree one is the full algebraic `R^Q`; boundaries are not falsely set to zero. |
| Theorem `thm:invariant-diagonal` | PASS | `J*` embeds the actual class line as constants and strict time-preserving automorphism invariants are exactly that diagonal. |
| Corollary `cor:packet-comparison` | PASS | The fixed-prime application uses only the bare nonempty orbit set and transfers none of its disallowed structure. |

## 7. Source, citation, domain, and integrity audit

PASS. The citation set and bibliography set are equal: 27 citation commands
contain 31 key occurrences and 14 unique keys, while `references.bib`
contains exactly those 14 records. There is no missing, orphan, duplicate,
ghost, or decorative entry.

The source hierarchy is correctly typed:

- Deninger owns the fixed-prime right flow, multiplicative isotropy, and
  logarithmic clock at the cited arXiv-v4 location;
- the three companion records own only their declared actual-topology,
  separated-reflection, and range-first/convolution contexts;
- Stacks and the Encyclopedia of Mathematics records provide routine
  coproduct/topological-group/homogeneous-space background;
- Gepner–Meier, Guillou–May, Alp–Wensley, Blanco–Uribe–Waldorf,
  Farsi–Huang–Kumjian–Packer, Fuchssteiner–Wockel, and Mackenzie remain
  bounded comparators, not imported proofs for the actual owner; and
- Paper 12 owns the author complex, standardization, automorphism extension,
  standardized degree-one computation, and same-carrier invariant theorem.

The three unpublished companion entries are honest and URL-free. Their
3/14 share exceeds the ARS self-citation advisory percentage, but each has a
distinct owner/context role and none is used to inflate priority or replace
the direct generic proofs. The bounded search conclusion remains exactly
`SUPPORTED_WITHIN_SEARCH through 2026-08-15`; it is not phrased as a claim of
being first or globally without precedent.

The final citation/source-integrity report at
`f599dfbf67026b0985ee0e09b4e41bb24e3fe94709a1cd5e03ba657fb2a4fcaf`
independently returns C0/M0/m0 on the same tuple. Its remaining conditions
are external release conditions and are carried into Section 12 below.

## 8. Route-A/Route-B audit

PASS. The eight owner records are reproduced without reordering or
coordinate donation:

| Owner | Exact tuple class | Verdict |
|---|---|---|
| `GEN-INDISC-R-ACTION-CNV` | A0 fail, A1 fail, A2 fail, A3 fail, A4 fail | Rejected |
| `DEN-EF-ACTUAL-ORBIT-CNV-P-A` | A0 analytic/arithmetic origin, A1 weak, A2 fail, A3 fail, A4 fail | Exploratory |
| `DEN-EF-ACTUAL-PACKET-CNV-P` | A0 analytic/arithmetic origin, A1 weak, A2 fail, A3 fail, A4 fail | Exploratory |
| `DEN-EF-ACTUAL-ORBIT-MARKED-PERIOD-P-A` | A0 analytic/arithmetic origin, A1 weak, A2 fail, A3 fail, A4 fail | Exploratory |
| `DEN-EF-ACTUAL-PACKET-MARKED-PERIOD-P` | A0 analytic/arithmetic origin, A1 weak, A2 fail, A3 fail, A4 fail | Exploratory |
| `DEN-EF-STANDARD-PERIOD-QUOTIENT-P` | A0 weak arithmetic relation, A1 weak, A2 fail, A3 fail, A4 fail | Exploratory |
| `DEN-EF-STANDARDIZED-PACKET-H1-DIAGONAL-P` | A0 weak arithmetic relation, A1 weak, A2 fail, A3 fail, A4 fail | Exploratory |
| `UNMARKED-PERIOD-SCALING-CONTROL` | A0 fail, A1 weak, A2 fail, A3 fail, A4 fail | Rejected |

Every record has determinant status
`NONE_BY_DESIGN_NO_DETERMINANT_OBJECT`; all required A2 metrics are negative
or not applicable; every A3 and A4 fails; every adversarial verdict is
`STOP_SCOPED`; every Route-B flag is false; and no Route-B file exists.
“Exploratory” is correctly described as a scoped negative prior, not weak
determinant, explicit-formula, spectral, or operator evidence.

## 9. Deterministic-control reproduction

PASS. After the sole-runner reservation was released, the official
`./experiments/reproduce.sh` was run once, serialized and independently of
the manuscript build. It returned status zero:

- 122/122 tests passed;
- 11 CSV files with exactly 3,486 rows verified;
- 14/14 intentional negatives were detected;
- checked-in, fresh-one, and fresh-two generated outputs were byte-identical;
- recursive-entry and no-cache gates passed;
- no cache or bytecode residue remained; and
- the manifest re-hashed unchanged to
  `7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95`.

The script and controls use the Python standard library, no network,
external dataset, randomness, timestamp, fitting, target-zero table,
determinant, trace, or analytic completion. Exact arithmetic is used except
for the declared display-value tolerance. These are finite witnesses and
falsifiers, not substitutes for the universal real/arbitrary-set proofs or
for source verification.

## 10. Bilingual, figure/table trace, build, and PDF audit

### 10.1 Bilingual consistency

PASS. The 205-word English abstract and independently written 370-Han-code-
point Simplified-Chinese abstract express the same twelve facts in the same
order: setting; all-degree `T0` factorization; actual `H^1` and zero
boundaries; packet mark; category boundary; common-lattice standardization;
automorphism kernel/choice split; standardized full product and nonzero
boundaries; `J` and invariant diagonal; bare-set/no-transfer packet
boundary; controls role; and prohibited higher/topological/analytic/operator
inferences. No owner, category, variance, or negative-boundary discrepancy
remains.

### 10.2 Strict six-key bidirectional trace

PASS. `paper/README.md` contains five artifact entries: two figures and
three tables. Each entry has exactly the six required top-level keys and no
seventh key:

`artifact_id`, `source_data`, `transformation`, `caption_claim`,
`supported_manuscript_claims`, `limitations`.

All five artifact IDs equal manuscript labels. Every cited theorem/equation/
section label exists in the source. Figure-source hashes equal the frozen
tuple. Forward tracing from each artifact to its claims and reverse tracing
from every caption/adjacent boundary statement return the matching ledger
entry. Captions, prose equivalents, and limitations agree; no figure or
table makes an unsupported inference.

### 10.3 Clean build and structural checks

PASS. A fresh temporary copy of the stable `paper/` sources was built with
the documented exact sequence:

```text
XeLaTeX -> BibTeX -> XeLaTeX -> XeLaTeX -> XeLaTeX -> copy -> cmp
```

All typesetting commands and the final copy comparison returned zero. The
additional final XeLaTeX pass cleared the transient reference-stabilization
warning. The final log has no undefined citation/reference, rerun request,
BibTeX metadata warning, overfull/underfull box, missing glyph, duplicate
label, or fatal error; only standard `unicode-math` command-ownership
warnings remain.

The clean and retained PDFs have byte-identical extracted layout text,
SHA-256
`8f9715f37f1a6d87d71855cdfb3656e2c5102f69fb2b184c24d15c76119d22d9`.
Binary PDF hashes need not agree across independent builds because creation
and subset metadata vary; source identity, stabilized text, and presentation
were checked instead. There are 14 unique cited keys and 14 bibliography
records, zero unresolved `??`, and no hidden second build PDF in `paper/`.

### 10.4 Full-page visual and PDF-structure audit

PASS. The retained PDF is 18 A4 pages, unencrypted, Ghostscript-readable,
and contains no JavaScript, form, embedded file, or raster image. All eight
used fonts are embedded, subsetted, and Unicode mapped. Extracted text and
binary-string scans expose no workspace/local source path, source-PDF
basename, TeX/Bib source name, or embedded-source marker.

All 18 pages were rendered at 150 dpi and visually inspected individually.
The English and Chinese abstracts, contents, every theorem/equation, both
figures, all three tables, declarations, and all 14 references are legible
and margin-safe. No clipping, collision, bad wrap, empty page, missing
glyph, broken figure, caption contradiction, or split proof/sentence
remains. Figure 1 precedes rather than interrupts Corollary 8.2; Figure 2 is
kept within the fixed-prime application and before Section 9; and the Route
table remains inside Section 9.2 before limitations, declarations, and
references.

The Freeze-1 spacing tokens, missing parenthesis, grammar defect, duplicated
cleveref nouns, split floats, post-bibliography Route table, duplicated
companion years, abstract fact-ledger mismatch, and transient final-label
warning are all absent from this frozen candidate.

## 11. Package hygiene and research-source PDF exclusion

PASS at the inspectable workspace/package boundary. The Paper-12 tree has
six PDFs total: five internal research copies under `notes/sources/` and the
single generated manuscript output `paper/paper.pdf`. None of the five
research-source PDFs is inside `paper/`, referenced as a public payload, or
embedded in the retained PDF. `notes/sources/.gitignore` contains exactly the
research-PDF exclusion rule and preflight-sidecar exception and re-hashes to
`87edb0df613805bc3ea528a3f3c13f7cca93498cc92a48a4612c66fc4a0ac465`.
The public-package documentation explicitly distinguishes the generated
paper PDF from excluded verification copies.

No `.aux`, `.log`, `.bbl`, `.blg`, `.out`, `.toc`, `.synctex`, `.fls`,
`.fdb_latexmk`, `manuscript.pdf`, cache, or bytecode artifact remains in the
manuscript package. The source manifestation and checksum ledgers can be
published without publishing the retained source bytes.

Git metadata is absent from this workspace snapshot, and this review did not
run Git. Therefore an actual index/stage/archive/upload/attachment/hidden-
path/fresh-clone exclusion proof cannot be claimed here. That is an explicit
external release gate, not a hidden failure of the current package.

## 12. Strongest counterargument and release conditions

### 12.1 Strongest counterargument

The strongest skeptical case is that the actual-indiscrete cohomology
collapse is mathematically elementary once the `T0` factorization is
recognized, while the fixed-prime flow, clock, stabilizer, and actual packet
topology are source- or companion-owned. The resulting contribution may
therefore appear highly specialized, and a venue seeking broad new
cohomological machinery could judge its impact too narrow.

That objection is a venue-fit concern, not a correctness defect. The paper
does not claim the source-owned premises or elementary background as its
novelty. Its nonredundant contribution is the exact same-carrier,
section-free standardization; the full/faithful category comparison; the
arbitrary-`Q` automorphism extension with an honest choice ledger; the full-
product standardized degree-one computation with nonzero boundaries; and
the invariant-diagonal theorem, all under strict owner, topology, category,
and variance firewalls. The fixed-prime corollary is explicitly an
application and transfers only the bare nonempty orbit set. On those bounded
claims, the technical advance is defensible and complete.

### 12.2 Mandatory pre-submission/public-release conditions

The following are already disclosed and do not alter the internal scientific
verdict, but they block journal-facing or standalone public release until
closed:

1. Human confirmation of the author list, academic unit, institution
   spelling and address, corresponding status/email/ORCID, CRediT roles,
   funding, competing interests, acknowledgments, and venue-specific ethics
   wording.
2. Confirmation of target venue/article type, venue template and citation
   style, venue AI policy/disclosure, availability wording, and any required
   submission-day DOI/correction refresh.
3. An honest immutable public identity for each of the three companion
   dependencies, or self-contained premises/proofs replacing every
   load-bearing dependency before standalone release.
4. Human authorization of the public repository, tag, archive, license, DOI,
   and release bytes.
5. Real repository/index, archive, upload-manifest, attachment-list, hidden-
   path, and fresh-clone evidence that no `notes/sources/*.pdf` byte enters
   the public payload.
6. A new exact-byte review if any manuscript, bibliography, figure, PDF,
   trace, declaration, or venue-template byte changes.

## 13. Questions for the author before public submission

1. Is the intended venue and article type suitable for a rigorous,
   specialized same-carrier comparison theorem whose impact is primarily
   structural rather than a new trace/determinant/operator construction?
2. Will every provisional declaration, companion identity, and real public-
   sync exclusion gate be human-confirmed before release?

No answer is required to sustain the exact internal scientific verdict;
both answers affect venue fit and release authorization.

## 14. Dimension scores

| Dimension | Score | Descriptor | Notes |
|---|---:|---|---|
| Originality (20%) | 82 | Strong | The ingredients include elementary collapse facts, but their exact same-carrier standardization, arbitrary-set automorphism extension, full-product `H^1`, and invariant diagonal are nonredundant within the stated domain. |
| Methodological rigor (25%) | 98 | Exceptional | Direct all-degree and degree-one proofs, explicit signs, category limits, choice ledger, and sharp negative directions. |
| Evidence sufficiency (25%) | 98 | Exceptional | Exact source locks, proof gates, 122 controls, Route ledger, clean build, full visual review, and bidirectional trace agree. |
| Argument coherence (15%) | 98 | Exceptional | The narrative moves from actual collapse through standardization and automorphisms to contravariant comparison without owner or variance drift. |
| Writing quality (15%) | 97 | Exceptional | Precise bilingual summaries, readable proof order, explicit limitations, stable floats, and clean 18-page PDF. |
| Literature integration | 95 | Strong | Exact manifestations and locators, honest comparator ceilings, and a bounded dated novelty claim. |
| Significance and impact | 82 | Strong | A sharp structural result for the research program, with intentionally limited breadth and no analytic promotion. |
| **Weighted average** | **94.7** | **Accept** | Exact scientific candidate passes; external release remains conditional as stated. |

## 15. Final exact-lock verdict

| Severity | Count |
|---|---:|
| Critical | **0** |
| Major | **0** |
| Minor | **0** |

**ACCEPT / exact-lock PASS — C0/M0/m0, confidence 5/5.**

No mathematical, source, owner, domain, category, variance, Route,
citation-integrity, control, trace, build, PDF, visual, or package-hygiene
defect remains in the exact tuple of Section 1. The open items in Section 12
are explicit human/external release conditions; they do not convert
provisional metadata into verified facts and do not authorize publication of
research-source PDFs.

Any later byte change to a bound candidate artifact requires a new
tuple-specific audit.

## 16. Correction Freeze append-only independent peer relock

Added: **2026-08-15 (Asia/Shanghai)**  
Mode: **independent ARS peer, methodology, mathematical-domain,
devil's-advocate, formatter, citation, integrity, figure/table-trace, and
full-PDF visual relock**  
Candidate: **CORRECTION FREEZE**

This section is an append-only correction and relock. Immediately before
this append, the complete historical peer report above was exactly
**34,758 bytes** with SHA-256
`e1f1558e170831457685a4a5c8c4d77f061b405d6c499867b6ce4f91bea6dc2b`.
Those bytes are retained verbatim as the prefix of this file. No historical
word, finding, hash, score, or verdict was silently rewritten.

### 16.1 Missed Minor and explicit supersession

The prior peer review missed one **Minor bibliographic-metadata error**. It
bound and accepted a BibTeX record that called Stacks Project Section 5.29,
Tag `0B1W`, **“Topological colimits.”** The official page title is
**“Colimits of spaces.”** The tag, official URL, Stacks authorship, no-date
handling, and the limited coproduct/quotient-topology background claim were
correct; the displayed source title was not.

Accordingly, the honest historical finding ledger for the old Review Freeze
2 tuple was **C0/M0/m1**, not C0/M0/m0. In particular, the old tuple in
Section 1.1, the old citation-audit hash in Section 1.2, the metadata-clean
conclusion in Section 7, the old retained-build/PDF lock in Section 10, and
the old-tuple zero-Minor verdict in Section 15 are superseded for current-lock
purposes. This does not erase them or retroactively make the false title an
acceptable alias. It records transparently that the earlier peer lane should
have found the Minor.

The corrected candidate was independently re-reviewed below. Reference [11]
now has the official title, so the historical Minor is closed and the
**current open-finding ledger is C0/M0/m0**.

### 16.2 Corrected exact tuple and exact old/new delta

Every corrected hash was recomputed directly from the workspace:

| Artifact | Corrected SHA-256 | Result |
|---|---|---|
| Paper-12 project `README.md` | `3f30055125e5f6593b4f8806c75ab3349675112e574f69e7238d9f7bd2ef9428` | exact |
| `paper/README.md` | `18eea91a1ed775cc03a14614af4662e3967be3aec66dd6bd58fc09819932db25` | exact |
| `paper/manuscript.tex` | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` | exact; unchanged |
| `paper/references.bib` | `b763e9c07e3265d878bfc8b4caf44fb6c92ef12e7fac59b8af0bdeb703876175` | exact; corrected title |
| `paper/figures/same_carrier_diagonal.tex` | `a83148600d497dd1b91510f5707a1b1a9402c35689013a1fa904978206ff5cf1` | exact; unchanged |
| `paper/figures/packet_four_way_firewall.tex` | `9a52c273e91878d4dd74f96bd27fe299be39d98cdbebdda6bc800d89184b6908` | exact; unchanged |
| retained `paper/paper.pdf` | `9d6747e9f33c6ab3724beb35daedbb0efaff73691ed344374366f2392541ec15` | exact; 18 pages |
| retained `pdftotext -layout` output | `38adf39f29ac54af206f5c23537025f81a2b00fae1bed294bc4098a257fc10d4` | exact |
| corrected `notes/citation_audit.md` | `79089b2487b6b21c10c1f10a4918fb29602d265877483d7a325634d15ec70a3a` | exact; PASS |

The hash transition and scope are:

| Artifact | Historical exact hash | Corrected exact hash | Delta class |
|---|---|---|---|
| project `README.md` | `a156deefbb059d840f73bfd6d76d468300158ad0e8c8bffef81b7a355c2cec51` | `3f30055125e5f6593b4f8806c75ab3349675112e574f69e7238d9f7bd2ef9428` | correction receipt/history |
| `paper/README.md` | `149bb1c9177f629fd5e04defa48ce17716cad85ea9d51dd0a8135e79b2214a7f` | `18eea91a1ed775cc03a14614af4662e3967be3aec66dd6bd58fc09819932db25` | correction receipt/history |
| `paper/manuscript.tex` | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` | same | no byte change |
| `paper/references.bib` | `e1f4d0f6589ce0710173bad1c0089b5d6746d09010cc448d6d387ad8c9e17dcf` | `b763e9c07e3265d878bfc8b4caf44fb6c92ef12e7fac59b8af0bdeb703876175` | one source-title line |
| `same_carrier_diagonal.tex` | `a83148600d497dd1b91510f5707a1b1a9402c35689013a1fa904978206ff5cf1` | same | no byte change |
| `packet_four_way_firewall.tex` | `9a52c273e91878d4dd74f96bd27fe299be39d98cdbebdda6bc800d89184b6908` | same | no byte change |
| `paper/paper.pdf` | `3fda5ae01fd3b7a78ddbefb11a62befa4d2ab50906b112b39e3c48e89901a294` | `9d6747e9f33c6ab3724beb35daedbb0efaff73691ed344374366f2392541ec15` | rebuilt reference [11] |
| layout extraction | `8f9715f37f1a6d87d71855cdfb3656e2c5102f69fb2b184c24d15c76119d22d9` | `38adf39f29ac54af206f5c23537025f81a2b00fae1bed294bc4098a257fc10d4` | title plus final-page whitespace |
| `notes/citation_audit.md` | `f599dfbf67026b0985ee0e09b4e41bb24e3fe94709a1cd5e03ba657fb2a4fcaf` | `79089b2487b6b21c10c1f10a4918fb29602d265877483d7a325634d15ec70a3a` | append-only correction/relock |

The exact old and new bibliography bytes were recovered and compared with
`diff -u`. There is one content hunk and one changed line:

```diff
-  title  = {The Stacks Project, Section 5.29 (Tag 0B1W): Topological colimits},
+  title  = {The Stacks Project, Section 5.29 (Tag 0B1W): Colimits of spaces},
```

The exact old/new layout diff likewise changes only the rendered title in
reference [11] and one whitespace-only horizontal-position character on the
final page-number line. Manuscript prose, mathematics, labels, and both
native figures are byte-identical. The two README changes are transparent
receipt/correction-history changes. No claim, proof, control, owner, Route
record, source manifestation, lock, pipeline state, or release decision was
altered.

The corrected citation audit itself preserves its exact historical
**34,843-byte** prefix; re-hashing that prefix returned
`f599dfbf67026b0985ee0e09b4e41bb24e3fe94709a1cd5e03ba657fb2a4fcaf`.
Its current full-file hash is the corrected value in the tuple above.

### 16.3 Full mathematics, owner, domain, and standalone relock

The unchanged manuscript and the controlling proof, methodology, domain,
devil's-advocate, standalone, and integrated-gate records were read again,
not merely inherited from the corrected citation audit. The relevant gate
hashes remain exactly those in Section 1.2, including
`phase3_v4_math_review.md` at
`97dbd63fae6d35ae627520203db98d7c497a927a505599c0855231ac3f3b4e07`,
`phase3_v4_standalone_review.md` at
`639dc289c024588777a05d46ff9e5cd47b6e50ceeb807ef7571776d0301e6895`,
and `phase3_v4_integrated_gate.md` at
`2b23ecc9462431dbebd12a6af5994a09a7f7d7e37bad10f1f11d118aa3ecc9c4`.

Independent equation and proof checks again support the following exact
boundaries:

- the `T0` separation argument gives all-degree time factorization, including
  the first face, and does not extend silently to non-`T0` coefficients;
- for the actual indiscrete owner,
  `Z^1 = R c`, `B^1 = 0`, and `H^1 = R[c]`, with the continuous Cauchy step
  and isotropy-period formula proved directly;
- strict, positive-scaled, unmarked, and orientation-reversing morphisms are
  kept distinct, so a forgotten mark does not retain the original scale;
- common-lattice orbitwise standardization is section-free at the topology
  level, unique under the stated cocompact/Hausdorff/open-orbit hypotheses,
  and exactly equivalent to the globally indiscretized category;
- the canonical sequence
  `1 -> (R/H)^Q -> Aut_R(Std(X)) -> Sym(Q) -> 1` has a section-free kernel,
  choice-dependent surjectivity, and only a noncanonical split;
- standardized degree-one cohomology is the full algebraic product `R^Q`,
  while standardized coboundaries can be nonzero; no topology or direct-sum
  substitution is made;
- the identity functor runs continuously from standardized to actual, while
  cohomology pulls back contravariantly from actual to standardized; raw
  pullback and the declared inverse-pullback left action are not confused;
  and
- the image is precisely the constant diagonal fixed by strict
  time-preserving automorphisms, with no extension to scaled, unmarked,
  higher-degree, topological, determinant, trace, or operator assertions.

Ownership remains clean. Deninger's source owns the fixed-prime flow and
stabilizer premise; the packet companion owns the actual packet topology;
Paper 12 owns the same-carrier standardization and comparison. The
fixed-prime application transfers only the declared bare nonempty orbit set
and does not import a count, enumeration, measure, local triviality, actual
topology, cross-prime statement, or arithmetic selection mechanism.
Comparators remain confined to their own hypotheses.

The strongest devil's-advocate objection is still limited significance: the
actual collapse is elementary once the `T0` observation is made and several
application premises are source-owned. It does not invalidate the
nonredundant conjunction of same-carrier standardization, exact category
comparison, arbitrary-set automorphism extension with a choice ledger,
full-product standardized `H^1`, and invariant diagonal. The title
correction neither weakens nor enlarges that contribution. The
standalone-fidelity verdict therefore remains PASS within the manuscript's
declared companion-premise boundary; immutable public companion identities
remain an external release condition.

### 16.4 Route, controls, citation, and trace relock

The eight Stage-12 Route-A YAMLs were parsed and independently re-hashed.
All eight match the hashes in `notes/route_audit.md`: six are
`ROUTE_A_EXPLORATORY`, two are `ROUTE_A_REJECTED`, every A2--A4 coordinate
fails, all eight `route_b_invocation_allowed` values are Boolean false, and
there is no Stage-12 Route-B file. No coordinate donation or owner splicing
is present.

The frozen controls manifest remains
`7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95`
and declares PASS. All eleven CSV bytes, recorded byte counts, schemas, and
row counts were rechecked: they total 3,486 rows and retain the 122-test and
14-negative receipt. Every active-lock, implementation, and phase-gate hash
named by the manifest resolves. This peer relock did **not** invoke a second
control reproduction: the correction is wholly outside the control package,
and this lane respected its serialized sole-runner boundary. Thus the test
count is the unchanged frozen receipt, while the present independent check
is a read-only integrity and interpretation review. The finite controls
remain witnesses and falsifiers, not universal proofs.

The corrected bibliography contains exactly 14 records. A fresh manuscript
parse found 27 citation commands, 31 key occurrences, and 14 unique keys;
the cited and bibliography key sets are identical. Official Tag `0B1W` was
reopened independently and confirms “Colimits of spaces,” while supporting
only the routine coproduct/quotient-topology background for which it is
cited. The other source identities, manifestations, locators, comparator
hypotheses, and companion roles remain aligned. The corrected citation audit
at `79089b2487b6b21c10c1f10a4918fb29602d265877483d7a325634d15ec70a3a`
independently agrees and returns PASS. Its final sidecar transcription
correction was also checked against the actual Farsi--Huang--Kumjian--Packer
sidecar hash
`908dea03b5b4523764249a6749e50ae696c0f342a21fe5522c22c1b962a0cb3b`.

The `paper/README.md` trace YAML parses to exactly five artifacts: two
figures and three tables. Every entry has exactly the six required nonempty
keys; all ten hash-addressed source records resolve; all five artifact IDs
exist in the manuscript; every cited theorem, equation, section, figure,
and table label exists; and all limitations are nonempty. Caption-to-trace
and trace-to-manuscript linkage are complete without promoting a diagram,
finite control, companion premise, or Route record into stronger evidence.

### 16.5 Clean build, PDF structure, text, fonts, and visual relock

An isolated build from copied corrected sources ran the exact five-stage
cycle

```text
xelatex -> bibtex -> xelatex -> xelatex -> xelatex
```

with exit status zero at every stage. The stabilized log has no undefined
citation, undefined reference, duplicate label, overfull/underfull box,
error, or fatal message; only the standard `unicode-math`/`mathtools`
command-overwrite notices remain. The fresh binary has SHA-256
`54d7a381edae3136da0eb175eb6f199a7fac014d9f5caab664197f2d309e7639`;
its binary difference from the retained PDF is build-metadata-only for
review purposes because the stronger content comparisons below are exact.

Retained and fresh `pdftotext -layout` outputs are byte-identical at
`38adf39f29ac54af206f5c23537025f81a2b00fae1bed294bc4098a257fc10d4`.
Their normal-flow text outputs are byte-identical at
`e25b4c50dab8272241cc6c7953302082d2f57885e9aa43f3c6927435e27fa7ef`.
All 18 retained/fresh 160-dpi page-raster pairs are byte-identical.

The retained PDF parses cleanly with Ghostscript and reports 18 unrotated,
unencrypted A4 pages, no form, no JavaScript, no custom metadata or metadata
stream, and zero embedded files. It contains no raster images: both figures
remain native vector output. All eight fonts are embedded, subset, and
Unicode-mapped. Text and binary-string scans found no local path, source PDF
basename, source hash, `.tex`/`.bib` filename, ARS marker, unresolved `??`,
or warning sentinel.

Every one of the 18 retained pages was visually inspected. The bilingual
front matter, equations, proofs, two diagrams, three tables, declarations,
links, two-page bibliography, and page numbers are legible and free of
clipping, collision, float escape, blank output, broken glyphs, or stray
artifacts. Page 18 was additionally inspected at original raster resolution:
reference [11] visibly reads **“Colimits of spaces,”** retains Tag `0B1W`
and the official URL, and does not show the false title.

### 16.6 Package, source-PDF, and release boundary

The manuscript package still contains exactly six files: its README,
manuscript source, bibliography, two native figure sources, and generated
`paper.pdf`. It contains no build auxiliary, cache, bytecode, `manuscript.pdf`,
or research-source PDF. The Paper-12 tree contains six PDFs total: the one
generated paper and five internal verification copies under
`notes/sources/`.

Running the retained checksum ledger in the source directory returned 10/10
PASS for the five PDFs and five preflight sidecars. The source-local
`.gitignore` remains exactly `*.pdf` plus the `!*.preflight.json` exception
and re-hashes to
`87edb0df613805bc3ea528a3f3c13f7cca93498cc92a48a4612c66fc4a0ac465`.
The generated PDF has no attachment and leaks no retained-source path,
basename, or checksum.

Git metadata remains absent from this workspace snapshot and this relock did
not run Git. Therefore no index, staged-delta, archive, remote-upload,
attachment-manifest, hidden-path, or fresh-clone exclusion claim is made.
Those checks, human declarations, venue requirements, companion publication
identities or replacement premises, and public archive/license/DOI approval
remain mandatory external gates. The unchanged release audit remains at
`53403b3ea8c44f30b6941653e2809432ad0e6b99f5cf983f0d929aa9d5c2760d`
and `PUBLIC_RELEASE_AUTHORIZED=false`.

This relock edited no candidate, citation, release, control, result, Route,
lock, pipeline, Git, source-manifestation, or source-PDF byte. Its only write
is this append-only section of the peer-review report.

### 16.7 Current finding register and verdict

| Severity | Historical old tuple | Current corrected tuple |
|---|---:|---:|
| Critical | 0 | **0** |
| Major | 0 | **0** |
| Minor | 1 missed title error | **0** |

**ACCEPT / CORRECTION FREEZE exact-lock PASS — C0/M0/m0, confidence 5/5.**

The prior peer lane's missed Minor is now explicitly acknowledged, corrected,
and closed. No mathematical, owner, standalone, Route, controls,
figure/table-trace, citation-alignment, integrity, build, PDF, visual, or
inspectable package/source-boundary defect remains in the corrected tuple of
Section 16.2. This is an internal scientific exact-lock verdict, not journal
acceptance or public-release authorization. Any later byte change to a bound
candidate artifact requires a new tuple-specific audit.

## 17. Append-only status and bilingual-count peer relock

Added: **2026-08-15 (Asia/Shanghai)**  
Mode: **independent ARS receipt-only peer, integrity, bilingual, package, and
release-boundary relock**  
Disposition: **ACCEPT / STATUS-COUNT exact-lock PASS — C0/M0/m0,
confidence 5/5**

This section is append-only. Immediately before it was added, the complete
peer report above was exactly **50,887 bytes / 821 lines**, with SHA-256
`f3eaef077677144470e3f0417cb418009f0d340a8cd2856ac6cff74cf337438a`.
Those bytes remain verbatim as this file's prefix. No historical finding,
hash, score, or verdict was silently rewritten.

This lane edited no manuscript, bibliography, figure, PDF, README, citation
report, release report, proof, source, control, result, Route record, lock,
pipeline state, or Git state. It ran no build, controls, Route workflow, or
Git command. Its only workspace write is this append to
`notes/peer_review_round1.md`.

### 17.1 Resolved receipt Minor and supersession boundary

The immutable prefix contained one additional, now-resolved **Minor (m1)**
in its bilingual/status receipt. It accepted the then-current README wording
and repeated a count of **370 Unicode Han code points** without naming the
property boundary that produced that value. Under the current package
README's explicit `Script=Han` metric, the Chinese prose body contains **353**
Han code points, not 370. The old value is reproducible only under the wider
`Script_Extensions=Han` interpretation, which also counts 17
Chinese-context punctuation code points. The manuscript content, rendered
abstract, and twelve-slot semantic parity were never defective; the defect
was in the receipt and metric label.

The project and package READMEs also described independent relocks as still
pending after they had completed. Their status/count-only correction closes
the same receipt-integrity Minor. For current-lock purposes, this section
supersedes the prefix's active README hashes, its 370-count statements in
Sections 1.1, 5, and 10, and its citation-report binding. It does not erase
those historical receipts or change any scholarly finding. The current
open-finding ledger is **C0/M0/m0**.

### 17.2 Current exact tuple and new citation binding

Every current byte identity below was independently recomputed:

| Artifact | SHA-256 | Result |
|---|---|---|
| Paper-12 project `README.md` | `0026d84cf0a342f1da097dc8212cca7b80a532bc1d1f8cdcf2b40317967ebb20` | exact; 6,182 bytes / 124 lines |
| `paper/README.md` | `f8d7228452fc389e0b26b0de1314f77a270dd7b39ee00590851f2154c2ccfb91` | exact; 13,852 bytes / 202 lines |
| `paper/manuscript.tex` | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` | exact; unchanged |
| `paper/references.bib` | `b763e9c07e3265d878bfc8b4caf44fb6c92ef12e7fac59b8af0bdeb703876175` | exact; unchanged |
| `paper/figures/same_carrier_diagonal.tex` | `a83148600d497dd1b91510f5707a1b1a9402c35689013a1fa904978206ff5cf1` | exact; unchanged |
| `paper/figures/packet_four_way_firewall.tex` | `9a52c273e91878d4dd74f96bd27fe299be39d98cdbebdda6bc800d89184b6908` | exact; unchanged |
| retained `paper/paper.pdf` | `9d6747e9f33c6ab3724beb35daedbb0efaff73691ed344374366f2392541ec15` | exact; unchanged 18-page PDF |
| retained `pdftotext -layout` output | `38adf39f29ac54af206f5c23537025f81a2b00fae1bed294bc4098a257fc10d4` | exact; unchanged |
| `notes/citation_audit.md` | `19772ee4e6a779aea17924714f0f00bf4fff9f481255fb35b60c5b61edeaa6bf` | exact; status/count relock PASS C0/M0/m0 |

The citation report is itself append-only: its first **56,028 bytes / 823
lines** rehash to
`79089b2487b6b21c10c1f10a4918fb29602d265877483d7a325634d15ec70a3a`.
Its enlarged 61,074-byte / 916-line identity in the table is the current
citation receipt. It independently binds the corrected README bytes,
unchanged scholarly tuple, corrected count convention, exact inverse
receipt, and external release hold.

The pre-status release audit remains an exact historical technical receipt
at
`53afb3642812e981d0bb38b7166982c8818b7ef7085d96277dddd8f632d8d99b`.
It records technical PASS C0/M0/m0 for the unchanged scholarly tuple but does
not bind the status-corrected README bytes or this enlarged peer report. A
downstream release-status relock must bind them without creating a reverse
hash edge here.

### 17.3 Exact inverse and bilingual receipts

The README correction is exactly reversible. Two current-to-predecessor
substitutions in the project README, each guarded to occur once, reconstruct
the 5,693-byte / 115-line predecessor at SHA-256
`3f30055125e5f6593b4f8806c75ab3349675112e574f69e7238d9f7bd2ef9428`.
Two corresponding once-only substitutions in the package README reconstruct
the 13,199-byte / 192-line predecessor at SHA-256
`18eea91a1ed775cc03a14614af4662e3967be3aec66dd6bd58fc09819932db25`.
The two hunks per file change only completed-audit status wording and the
bilingual count receipt; no scholarly byte is hidden inside the correction.

The current count receipt was reproduced independently from the unchanged
manuscript:

- English abstract prose: **205** whitespace-delimited words under the
  frozen `detex` method;
- Simplified-Chinese prose body: **353** Unicode `Script=Han` code points,
  obtained independently with Perl `\p{sc=Han}` and the explicit
  `U+4E00--U+9FFF` range;
- six Chinese keyword values: **32** `Script=Han` code points; and
- separately named prose-plus-keywords total: **385**.

For provenance, Perl `\p{scx=Han}` returns 370 because it includes 17
punctuation code points. That broader property is not the declared current
metric. Both 353 and 385 remain within the blueprint's 300--500 range. The
English and Chinese abstracts retain the same twelve facts, order,
quantifiers, qualifications, and negative boundaries. Bilingual content and
semantic parity therefore remain PASS; only the old receipt label is retired.

### 17.4 Unchanged scientific, build, trace, and boundary findings

The manuscript, bibliography, both native figures, and retained PDF are
byte-identical to the complete mathematical, owner, category, standalone,
Route, controls, build, PDF, and visual review in Section 16. The new citation
addendum and this peer relock change no theorem premise or proof. In
particular, all conclusions about actual and standardized degree-one
cohomology, same-carrier standardization, the automorphism extension,
contravariant pullback, the invariant diagonal, fixed-prime ownership, and
the no-topology-transfer ceiling remain exactly as previously adjudicated.

Read-only checks reconfirmed the 27 citation commands, 31 key occurrences,
14 unique cited keys, and 14 BibTeX records, with zero missing or orphan
keys. The five-artifact trace still has exactly six nonempty keys per entry
and covers the two figures and three tables in both directions. The eight
Stage-12 Route-A and zero Route-B receipt remains unchanged: six exploratory,
two rejected, every A2--A4 coordinate failed, and every Route-B flag false.
Controls were not rerun; the frozen manifest remains
`7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95`
and its reviewed 122/122, 11-CSV/3,486-row, and 14/14-negative receipt remains
applicable to the unchanged bytes.

No rebuild or repeated raster pass was necessary for a README/citation-report
receipt change. The two independent corrected-candidate build/visual receipts
already bound in Section 16 remain exact-byte evidence: clean five-stage
builds, retained/fresh layout and normal-flow text identity, 18/18
byte-identical page rasters, complete 18-page visual inspection, eight
embedded/subsetted/Unicode-mapped fonts, zero raster images or attachments,
and a clean Ghostscript parse.

Fresh enumeration found exactly six regular files under `paper/`, exactly
one PDF (`paper.pdf`), and no symlink, research-source PDF, build auxiliary,
cache, or bytecode. The retained source checksum ledger again passed 10/10
for five source PDFs and five preflight sidecars; those internal PDFs remain
outside `paper/` and excluded by the unchanged local rule. No Git or actual
public-sync claim is made.

### 17.5 Current finding register and disposition

| Severity | Historical status/count receipt | Current tuple |
|---|---:|---:|
| Critical | 0 | **0** |
| Major | 0 | **0** |
| Minor | 1 receipt/metric-status defect | **0** |

**ACCEPT / STATUS-COUNT exact-lock peer PASS — C0/M0/m0, confidence 5/5.**

The current README status is truthful, the exact predecessor bytes are
recoverable, the bilingual count method is explicit and reproducible, and
the new citation relock passes on the unchanged scholarly tuple. Human
declarations, immutable companion identities or self-contained replacement
premises, venue/submission-day checks, real repository/archive/upload and
fresh-clone source-PDF exclusion, and explicit human release authorization
remain external. Therefore `PUBLIC_RELEASE_AUTHORIZED=false`; this is not
journal acceptance or public-release authorization.
