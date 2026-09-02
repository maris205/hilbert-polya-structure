# Paper 31 — Stage 1 Phase-2 independent source verification

Verification seat: VERIFY-SEAT-A

Verification date: 2026-09-02 UTC

Scope: ARS deep-research Phase 2 source-corpus verification only

## Disposition

PHASE2_SOURCE_BASE_READY_WITH_WARNINGS

This disposition says only that the 22-source corpus is sufficiently real, traceable, and topically bounded for a later Phase-3 evidence synthesis. It is not a scientific result, novelty judgment, Route-A tuple, permission to compute, or validation of the frozen 9,453-pair owner ledger.

## Frozen inputs, correction binding, and byte identity

No bibliography, inventory, Phase-1 file, README, or pipeline-state file was edited by this seat.

| Input | SHA-256 |
|---|---|
| Batch verification contract | 41f3881f0fa428c3ce324a12f12bd514649aff652114cc436d5932fb3cb8b72e |
| Metadata correction manifest | 59506776c0c536dbfd5b3ee511dd0ac0a52ae74548d08f3cd0dfb7ec9a8fd49c |
| stage1_phase1_rq_brief.md | b5927371ff7422b084dee6c8644ba14981b88b8f15cab9997f5df254cdd312b1 |
| stage1_phase1_methodology_blueprint.md | 046e4b826ffd0cfbf2e697d13bbf8d925dc775ef262798af4c4f2ef8e9ca23d2 |
| stage1_phase1_resolution.md | 624780725fc006517bfc391c0945e8a2ae67a09c482f6b28d4d1278bc49b204e |
| stage1_phase1_checkpoint.md | a81744824bc900a29c95edba3af0ef9c071f70e912927153477a8add35855ec1 |
| Initial verification MD before post-patch recheck | 076b3ba2a07175d7ae413b9426f348770b0b25c683ad884014592c74ff2a45a0 |
| Initial verification TSV before post-patch recheck | 326b377edd25c0a309153ca2a04e85861feaeb20e42ee83494f3454784ba6f32 |
| stage1_phase2_annotated_bibliography.md pre-patch | e2bd432bc655a607898b9c0d74c7acc899c94695bf9dc23b471a124c4f0e46ec |
| stage1_phase2_annotated_bibliography.md current post-patch | c4655ba9c039dc27a1a7fc05347b79f834454423ca80aa1c0dc19fb13f968976 |
| stage1_phase2_source_inventory.tsv pre-patch | 36f0af561157620b57c7d5ceaca616990ddedd3ab64921857fc44e23bbbbad74 |
| stage1_phase2_source_inventory.tsv current post-patch | cf4eef7d626ebc5d217d1597dc1f5e2ba0c5c8dc33b108a86b9be19d60536132 |

Post-patch status: RESOLVED_POST_VERIFICATION. Correction R10PH2-C04 is bound to the manifest above. The current bibliography and inventory hashes match its declared post-patch hashes, and P31-S16 now records 287–305 in both files.

The Phase-1 boundary used for claim fitness is ownership-only calibration at Gamma_0(11): global oriented primitive owner table G remains distinct from incidence table I and cell-local count table C; a bounded search failure is never a negative conjugacy certificate; every positive or negative pair decision requires its frozen replayable certificate surface. Nothing in Phase 2 promotes A2 or a determinant claim.

## Verification protocol

1. Each DOI-bearing inventory record was looked up independently through the Crossref REST work record and resolved to its DOI or first-party publisher/journal metadata. Title, author list, year, venue, volume, issue, and pages were compared with the inventory.
2. First-party or authoritative records were separately inspected where they materially strengthened the check: AMS for P31-S19, MathNet for P31-S21, World Scientific plus the Warwick institutional repository for P31-S16, and publisher DOI records for the other DOI sources.
3. Semantic Scholar was not queried. No Semantic Scholar verification label is assigned; the run-level condition is S2_NOT_QUERIED.
4. The field-neutral evidence level is VI for this pure-mathematics corpus. The A–F claim-fitness grade is independent and is relative only to the narrow support class assigned in the TSV; it is not a score for the complete P31 claim.
5. Venue assessment is bounded to the recognized journal, scholarly publisher, or institution visible in first-party/DOI metadata. No exhaustive indexing, COPE-membership, or predatory-list audit was performed.
6. No conflict-of-interest database and no retraction/Crossmark database was queried. Every row therefore records UNKNOWN_NOT_CHECKED for COI and NOT_CHECKED for retraction status. These values are limitations, not clean certificates.
7. Support was bounded by the inspected title, abstract, authoritative metadata, and available first-party text. Verification of existence does not endorse the manuscript's eventual theorem, implementation, or output.
8. For the post-patch recheck, the correction manifest was hash-verified, its pre/post bindings were replayed against the current files, and P31-S16 was re-read in both the bibliography and the inventory. No other source row or support boundary was changed.

## Coverage and integrity audit

| Audit item | Result |
|---|---|
| Inventory IDs expected | 22 |
| Verification rows written | 22 |
| Unique IDs represented exactly once | 22/22 |
| VERIFIED | 22 |
| PLAUSIBLE | 0 |
| UNVERIFIABLE | 0 |
| FABRICATED | 0 |
| Semantic Scholar verification | S2_NOT_QUERIED; no source-level label assigned |
| Exact metadata matches after authorized correction | 22 |
| Active metadata mismatches | 0 |
| Resolved post-verification corrections | 1, P31-ERR-01 / R10PH2-C04 |
| Inventory peer-reviewed count | 19/22 = 86.36% |
| Foundational sources exempted from recency penalties | 16 |

No source-existence integrity block was found. The peer-reviewed share exceeds the batch contract's 60% threshold. Foundational age is not treated as a defect when the assigned support class is the original mathematical construction, theorem, or historical algorithm.

## Per-source claim-fitness adjudication

The machine-auditable TSV is the normative row ledger. The following table makes its claim boundary human-readable.

| Source | Outcome / grade | Exact support admitted | Stronger support excluded |
|---|---|---|---|
| P31-S01 | VERIFIED / B | finite-index modular-subgroup classification | fixed-pair Gamma_0(11) decision, owner bytes, negative certificates |
| P31-S02 | VERIFIED / B | arithmetic-geometric special-polygon machinery | complete positive/negative subgroup conjugacy certificates |
| P31-S03 | VERIFIED / B | special polygons and finite subgroup data | primitive-owner policy or all-pairs completeness |
| P31-S04 | VERIFIED / C | congruence recognition | conjugacy inside a fixed congruence subgroup |
| P31-S05 | VERIFIED / C | congruence-subgroup identification | frozen orientation, conjugacy, and replay interface |
| P31-S06 | VERIFIED / B | computable Fuchsian fundamental domains | complete terminating P31 pair-certificate procedure |
| P31-S07 | VERIFIED / B | ideal-class/integral-matrix correspondence | Gamma_0(11), determinant-one, orientation, inversion, serialization |
| P31-S08 | VERIFIED / B | refinement of the ambient correspondence | subgroup-constrained conjugacy completeness |
| P31-S09 | VERIFIED / B | hyperbolic SL(n,Z) classes and ideal classes | congruence-subgroup refinement or owner bytes |
| P31-S10 | VERIFIED / B | ambient SL_2(Z) continued-fraction conjugacy | Gamma_0(11) constraint and replayable obstruction |
| P31-S11 | VERIFIED / B | arithmetic-group conjugacy framework | concrete P31 witness/obstruction payload |
| P31-S12 | VERIFIED / B | general arithmetic-group algorithms | frozen deterministic specialization and negative-certificate replay |
| P31-S13 | VERIFIED / B | modern ambient GL(n,Z) conjugacy algorithms | SL orientation, Gamma_0(11), inversion policy, P31 serialization |
| P31-S14 | VERIFIED / C | indefinite-form and class-number structure | a specified-pair certificate or G/I/C estimand separation |
| P31-S15 | VERIFIED / B | modular-geodesic continued-fraction coding | Gamma_0(11) solver or project owner ledger |
| P31-S16 | VERIFIED / B | linear conjugacy algorithm in word-hyperbolic groups | primitive-root owner policy or P31 certificate bytes |
| P31-S17 | VERIFIED / B | finite-list conjugacy in hyperbolic groups | frozen presentation, oriented encoding, certificate translation |
| P31-S18 | VERIFIED / B | centralizers and reversing symmetries | P31's oriented-versus-inverse equivalence choice |
| P31-S19 | VERIFIED / C | Pell equations and unit background | peer-reviewed conjugacy theorem or negative certificate |
| P31-S20 | VERIFIED / C | computational number-theory implementation background | P31 equivalence, 9,453-pair completeness, or G/I/C weighting |
| P31-S21 | VERIFIED / A | direct Gamma_0(N) primitive hyperbolic class-count formula | specified-pair decision, canonical orientation, certificate serialization |
| P31-S22 | VERIFIED / B | modular-group conjugacy/class-number connection | Gamma_0(11), inversion policy, or all-pairs replay contract |

P31-S21 and P31-S22 were checked as recent bibliography additions, not merely inherited from the original search table. P31-S21 is the closest direct Gamma_0(N) source in this corpus, but its A grade is deliberately narrow: it is fit for the class-counting support class only. It cannot be transformed into a complete pairwise certificate theorem.

## Post-patch correction resolution

| Finding | Initial state and pre hashes | Authorized operation | Current state and post hashes | Status |
|---|---|---|---|---|
| P31-ERR-01, P31-S16 venue pages | Inventory/bibliography recorded 287–306; bibliography e2bd432bc655a607898b9c0d74c7acc899c94695bf9dc23b471a124c4f0e46ec; inventory 36f0af561157620b57c7d5ceaca616990ddedd3ab64921857fc44e23bbbbad74 | R10PH2-C04 under manifest 59506776c0c536dbfd5b3ee511dd0ac0a52ae74548d08f3cd0dfb7ec9a8fd49c | Both files record 287–305; bibliography c4655ba9c039dc27a1a7fc05347b79f834454423ca80aa1c0dc19fb13f968976; inventory cf4eef7d626ebc5d217d1597dc1f5e2ba0c5c8dc33b108a86b9be19d60536132 | RESOLVED_POST_VERIFICATION |

The initial finding remains in the audit history. Crossref DOI metadata, the World Scientific/author article record, and the Warwick Research Archive record agree on 287–305 and 19 pages. The corrected bibliography and inventory now agree with those records; there is no active P31 page-range mismatch.

## Corpus warnings carried forward

1. None of the 22 sources, individually or as metadata-level verification, supplies the complete frozen primitive-owner quotient plus canonical positive and negative certificate interface for all 9,453 pairs.
2. Ambient GL_2(Z), SL_2(Z), or word-hyperbolic conjugacy cannot be treated as Gamma_0(11) conjugacy without a theorem-backed subgroup restriction and replay mapping.
3. Class-counting formulas, including P31-S21, are census precedents. They cannot certify an individual pair or prove zero unresolved rows.
4. The literature does not define the project's distinct G, I, and C tables or the resulting moment estimands. Those remain internal definitions and proof obligations.
5. Retraction status and source-level conflicts remain explicitly unexamined. Phase 3 must preserve this limitation rather than infer a clean screen.

## Phase-2 close

The post-patch corpus still meets the size, peer-review-share, existence, metadata, and topical-coverage gates. P31-ERR-01 is RESOLVED_POST_VERIFICATION, while the material claim-boundary warnings remain unchanged. The authorized output therefore remains PHASE2_SOURCE_BASE_READY_WITH_WARNINGS. No synthesis, novelty conclusion, Route judgment, scientific computation, or manuscript prose is issued here.
