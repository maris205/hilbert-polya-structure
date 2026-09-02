# Paper 32 — Stage 1 Phase-2 independent source verification

Verification seat: VERIFY-SEAT-A

Verification date: 2026-09-02 UTC

Scope: ARS deep-research Phase 2 source-corpus verification only

## Disposition

PHASE2_SOURCE_BASE_READY_WITH_WARNINGS

This disposition says only that the 26-source corpus is real, sufficiently traceable, and broad enough for a later Phase-3 evidence synthesis if all warnings below remain attached. It is not a proof of the independent-owner formal identity, compact-uniform analytic control, canonical panel, frozen normalization, or any Route-A status.

## Frozen inputs, correction binding, and byte identity

No bibliography, inventory, Phase-1 file, README, or pipeline-state file was edited by this seat.

| Input | SHA-256 |
|---|---|
| Batch verification contract | 41f3881f0fa428c3ce324a12f12bd514649aff652114cc436d5932fb3cb8b72e |
| Metadata correction manifest | 59506776c0c536dbfd5b3ee511dd0ac0a52ae74548d08f3cd0dfb7ec9a8fd49c |
| stage1_phase1_rq_brief.md | ac064dab60a47a656c9278093d3a58c8c32a3893ba220c8b8702667f56035ea8 |
| stage1_phase1_methodology_blueprint.md | 862e0deb45c59185f9725b562408622f2e69140f3872e65aee7c60f4b23b0fed |
| stage1_phase1_resolution.md | 77efea18e9e0bde3cdfc6ab9e06635fc1f5af66f9d1c110566f26a52db6cf193 |
| stage1_phase1_checkpoint.md | 6d5fb1b44fb2a15d98390381a59e4178655b459475a020e3b1d242929b75610f |
| Initial verification MD before post-patch recheck | 95ad09ca0258b315a25fc7d3cb711e0bffa6b801225ee3c328a849a84074fe29 |
| Initial verification TSV before post-patch recheck | beb7c5d620807d118635f6159c07455ae7591e7d0f291cbdd38f567b3f5448c8 |
| stage1_phase2_annotated_bibliography.md pre-patch | 435056bfd8fa7cfdd279a25079105025ab349c65604515fcc43fbe8e14bc9dfa |
| stage1_phase2_annotated_bibliography.md current post-patch | 2480eb3c3fce30fd9535cf7004c99f3cbc0babfc80b81bc1966827fac621a2a7 |
| stage1_phase2_source_inventory.tsv pre-patch | fa875cbe05a2a73957fb80c6276d981540334d0efca76e74ce595b775ae1ad5c |
| stage1_phase2_source_inventory.tsv current post-patch | c375c1e7e8310d6d5a1aa4509147a2d4b61b75fe3283b6d148fd0c61f2e76d8e |

Post-patch status: RESOLVED_POST_VERIFICATION. Correction R10PH2-C05 is bound to the manifest above. The current bibliography and inventory hashes match its declared post-patch hashes, and P32-S02 now records 287–305 in both files.

The Phase-1 claim boundary used for fitness distinguishes the independent-owner formal ring from any analytic content-one scalar subproduct; leaves SG2OwnerCanonical-v1 unbound until a complete canonical interface and prefix certificate exist; treats k at most 8 only as a diagnostic subset of the frozen k at least 1 schedule; and requires compact-uniform control on the frozen rectangles before any scalar or limit statement. Verification of literature does not fill those project-specific interfaces.

## Verification protocol

1. Each DOI-bearing record was independently queried through the Crossref REST work record and resolved to DOI/publisher/journal metadata. Title, author list, year, venue, volume, issue, and pages were compared with the inventory.
2. Authoritative or first-party records were inspected for the source families that required more than a DOI comparison: MathNet for P32-S05, arXiv for P32-S06 and the P32-S17 erratum companion, the Journal of the Indian Mathematical Society record for P32-S13, the Annals article page for P32-S17, Stockholm University DiVA for P32-S24, and NIST DLMF for P32-S26.
3. Semantic Scholar was not queried. No Semantic Scholar verification label is assigned; the run-level condition is S2_NOT_QUERIED.
4. The field-neutral evidence level is VI for this pure-mathematics corpus. A–F claim-fitness grades are independent and relative only to the narrow support class shown in the TSV; they do not rate support for the entire P32 construction.
5. Venue assessment is bounded to recognized journal, scholarly-publisher, preprint-server, thesis-repository, and institutional-reference metadata. No exhaustive indexing, COPE-membership, or predatory-list audit was performed.
6. No conflict-of-interest database and no retraction/Crossmark database was queried. All rows therefore state UNKNOWN_NOT_CHECKED for COI and NOT_CHECKED for retraction. The 2022 P32-S17 correction is handled as a known claim-scope erratum, not as a substitute for a retraction screen.
7. Support classes were assigned from the inspected authoritative metadata, abstracts, correction notice, and available first-party text. A verified citation is not an endorsement of the manuscript's proposed identity or normalization.
8. For the post-patch recheck, the correction manifest was hash-verified, its pre/post bindings were replayed against the current files, and P32-S02 was re-read in both the bibliography and inventory. No other source row, the independent P32-S17 erratum binding, or any support boundary was changed.

## Coverage and integrity audit

| Audit item | Result |
|---|---|
| Inventory IDs expected | 26 |
| Verification rows written | 26 |
| Unique IDs represented exactly once | 26/26 |
| VERIFIED | 25 |
| PLAUSIBLE | 1, P32-S13 DOI-less authoritative journal record |
| UNVERIFIABLE | 0 |
| FABRICATED | 0 |
| Semantic Scholar verification | S2_NOT_QUERIED; no source-level label assigned |
| Exact metadata matches after authorized correction | 26 |
| Active metadata mismatches | 0 |
| Resolved post-verification corrections | 1, P32-ERR-01 / R10PH2-C05 |
| Inventory peer-reviewed count | 22/26 = 84.62% |
| Foundational/formal-foundational recency exemptions | 16 |

No source-existence integrity block was found. The peer-reviewed share exceeds the batch contract's 60% threshold. P32-S13 is PLAUSIBLE rather than VERIFIED because it has no DOI and was confirmed through the exact journal record; this is a confidence-label distinction, not evidence of fabrication.

## Per-source claim-fitness adjudication

The machine-auditable TSV is the normative one-row-per-ID ledger. The following table states the admitted and excluded claim surfaces.

| Source | Outcome / grade | Exact support admitted | Stronger support excluded |
|---|---|---|---|
| P32-S01 | VERIFIED / B | combinatorial structure and normal-form background for cocompact hyperbolic groups | marked genus-two owner interface, maximal roots, prefix completeness |
| P32-S02 | VERIFIED / B | terminating conjugacy algorithm in word-hyperbolic groups | deterministic owner serialization, maximal roots, certified prefix |
| P32-S03 | VERIFIED / B | conjugacy of finite subsets in hyperbolic groups | SG2OwnerCanonical-v1 or enumerate-prefix completeness |
| P32-S04 | VERIFIED / B | finite-list conjugacy algorithms | theorem-to-code binding, orientation, roots, enumeration completeness |
| P32-S05 | VERIFIED / A | exact root-extraction solvability surface in hyperbolic groups | frozen return schema, uniqueness binding, owner composition, prefix certificate |
| P32-S06 | VERIFIED / C | recent surface-group normal forms, conjugacy, and root-finding candidate | peer-reviewed validation or silent equivalence to the frozen marked presentation |
| P32-S07 | VERIFIED / B | finite abelian surface-cover structure | owner order, lift multiplicity, period, normalization |
| P32-S08 | VERIFIED / B | Riemannian covering and group-action background | independent-owner lift factor or frozen scaling |
| P32-S09 | VERIFIED / B | closed geodesics distributed by homology | canonical owner enumeration or diagnostic-panel certification |
| P32-S10 | VERIFIED / B | homology distribution on compact Riemann surfaces | ownerwise lift order or target-blind panel |
| P32-S11 | VERIFIED / B | closed-orbit asymptotics in homology classes | primitive-owner compatibility or compact-uniform product tail |
| P32-S12 | VERIFIED / C | modern cover splitting and decomposition language | project normalization, owner topology, universal endpoint |
| P32-S13 | PLAUSIBLE / B | foundational Selberg trace/zeta context | ownerwise renormalized factor, topology, or limit order |
| P32-S14 | VERIFIED / B | primitive-orbit dynamical zeta context | formal-to-scalar identification or chosen normalization |
| P32-S15 | VERIFIED / B | Axiom-A prime-orbit asymptotics | owner-content-uniform bound needed for limit interchange |
| P32-S16 | VERIFIED / B | finite-index Selberg-zeta Artin formalism | coefficientwise owner recovery, frozen clock, infinite tower |
| P32-S17 | VERIFIED / B | first-part meromorphic-continuation result only | corrected Section 7 spectral-gap claim or dependent counting consequences |
| P32-S18 | VERIFIED / B | independent microlocal meromorphic-continuation route | homology-cover normalization or ownerwise equality |
| P32-S19 | VERIFIED / B | renewal/geodesic-counting candidate tools | already-established absolute compact-uniform owner-stratified tail |
| P32-S20 | VERIFIED / C | foundational prime-geodesic growth context | explicit summable compact-uniform tail or owner-content control |
| P32-S21 | VERIFIED / B | homology-refined closed-orbit asymptotics | canonical genus-two panel or simultaneous limits |
| P32-S22 | VERIFIED / B | exponential geodesic-growth error terms | the exact frozen sum, uniformity, and every limit order |
| P32-S23 | VERIFIED / C | ordered-division-ring and well-ordered-support background | P32 support convention, comparison map, owner product, normalization |
| P32-S24 | VERIFIED / C | inverse-limit/countably-many-variable topology precedent | P32 directed system, localizations, scalar gate, normalization |
| P32-S25 | VERIFIED / C | unrelated formal-geometry completion background | P32 owner product, scalar specialization, normalization |
| P32-S26 | VERIFIED / B | elementary scalar logarithmic/binomial expansions and domains | d=0 substitution, Hahn order, owner normalization, project endpoint |

P32-S23 through P32-S26 are therefore formally demoted to background-only support. They cannot be cited as evidence for the project-specific independent-owner product, the 1/N or 1/N^3 choices, a scalar-specialization map, or any limit conclusion.

## Post-patch correction resolution and continuing correction binding

| ID | Initial state and pre hashes | Authorized operation or independent adjudication | Current state and post hashes | Status |
|---|---|---|---|---|
| P32-ERR-01, P32-S02 venue pages | Inventory/bibliography recorded 287–306; bibliography 435056bfd8fa7cfdd279a25079105025ab349c65604515fcc43fbe8e14bc9dfa; inventory fa875cbe05a2a73957fb80c6276d981540334d0efca76e74ce595b775ae1ad5c | R10PH2-C05 under manifest 59506776c0c536dbfd5b3ee511dd0ac0a52ae74548d08f3cd0dfb7ec9a8fd49c | Both files record 287–305; bibliography 2480eb3c3fce30fd9535cf7004c99f3cbc0babfc80b81bc1966827fac621a2a7; inventory c375c1e7e8310d6d5a1aa4509147a2d4b61b75fe3283b6d148fd0c61f2e76d8e | RESOLVED_POST_VERIFICATION |
| P32-WARN-02, P32-S17 claim scope | The 2013 article can be overread as an unqualified spectral-gap/counting source | arXiv:2203.04917 states that the Section 7 spectral-gap part contained a mistake, while the first meromorphic-continuation part is unaffected | Every use remains bound to the 2022 erratum; only the unaffected first-part meromorphic-continuation surface is admitted unless another source repairs a stronger claim | CONTINUING_CLAIM_SCOPE_WARNING |

The initial P32-ERR-01 finding remains in the audit history. DOI/publisher, author-copy metadata, and the Warwick institutional record agree on 287–305 and 19 pages, and the corrected bibliography and inventory now agree with those records. The 2022 P32-S17 erratum remains a correction companion, not a twenty-seventh corpus source.

## Required warnings carried forward

1. P32-S06 is a 2025 arXiv preprint, last observed as version 2 dated 2025-12-27. It is not peer reviewed, and its symmetric surface-group presentation cannot be silently mapped to the frozen marked presentation.
2. P32-S17 may support only the meromorphic-continuation part that its 2022 erratum identifies as unaffected. Spectral-gap and dependent periodic-orbit counting uses are excluded at this verification stage.
3. P32-S23–P32-S26 are background sources only. Formal-topology or scalar-series resemblance is not evidence for P32's project-specific formal algebra, owner normalization, or recovery identity.
4. The corpus contains useful ingredients for conjugacy, roots, covers, zeta functions, homology counting, and formal topology, but no single verified source supplies SG2OwnerCanonical-v1, the prefix-complete enumeration certificate, the exact independent-owner formal algebra, or a compact-uniform tail compatible with every frozen limit order.
5. The exact 1/N and 1/N^3 scalings remain project definitions and derivation obligations. Literature verification cannot be used to declare them correct.
6. Retraction status and source-level conflicts remain explicitly unexamined, apart from the separately known P32-S17 correction. Phase 3 must preserve those limitations.

## Phase-2 close

The post-patch corpus still meets the size, peer-review-share, existence, metadata, and thematic-coverage gates. P32-ERR-01 is RESOLVED_POST_VERIFICATION; the non-peer-reviewed preprint, continuing P32-S17 correction binding, DOI-less PLAUSIBLE source, and background-only formal cluster retain the warning disposition. The authorized output remains PHASE2_SOURCE_BASE_READY_WITH_WARNINGS. No cross-source synthesis, novelty conclusion, Route judgment, scientific computation, or manuscript drafting is issued here.
