# Paper 29 — Stage 1 Phase 2 independent source verification

Date: **2026-09-02 UTC**

Seat: **VERIFY-SEAT-C**

Post-patch recheck status: **`RESOLVED_POST_VERIFICATION`**

Disposition: **`PHASE2_SOURCE_BASE_READY_WITH_WARNINGS`**

## Verification fence

This is an independent ARS Phase-2 source-verification artifact. It verifies
the existence, metadata, venue, currency, conflict-of-interest limits,
retraction-check status, and bounded claim fitness of the 22 records supplied
by `BIB-SEAT-A`. It does **not** perform Phase-3 synthesis, infer novelty,
apply a candidate mechanism, inspect Paper-29 performance, run scientific
computation, or assign a Route-A tuple. A verified source is not thereby a
verified owner mechanism or a certified primitive-owner quotient.

No Semantic Scholar query was performed, so no record is labeled
`S2_VERIFIED`. No API-degradation claim is made. DOI-bearing records were
checked against their DOI-resolved publisher or official journal records;
the one DOI-less record was checked against its first-party arXiv record.

## Hash-bound inputs

| Input | SHA-256 |
|---|---|
| `BATCH_ROUND10_STAGE1_PHASE2_VERIFICATION_CONTRACT.md` | `41f3881f0fa428c3ce324a12f12bd514649aff652114cc436d5932fb3cb8b72e` |
| `stage1_phase1_rq_brief.md` | `47899a9f82875df3be569da62c4699b3a11d4f7a4f2423d9830f66ad9aa4218f` |
| `stage1_phase1_methodology_blueprint.md` | `99e88f3569a51cc40bb649919265fc46e15ec3080f67eaf76d1f3fdabf4e69d6` |
| `stage1_phase1_checkpoint.md` | `1365f31ce44ebc45510700a1a1db2d9079c71408cbc41f8e390ee7753f477435` |
| `stage1_phase2_annotated_bibliography.md` (post-patch) | `c4d71637e5676337326d2eb78dcdd64d78b4b116a397c50c54a081d7c5e2650b` |
| `stage1_phase2_source_inventory.tsv` (post-patch) | `67ed7713bd6881d11466dc16755c7660a458c52e07ee072d086d6467f8ad7bd8` |

The bibliography and inventory remained read-only to VERIFY-SEAT-C during the
post-patch pass.

## Post-patch independent recheck

| Audit binding | SHA-256 / result |
|---|---|
| Correction manifest | `59506776c0c536dbfd5b3ee511dd0ac0a52ae74548d08f3cd0dfb7ec9a8fd49c` |
| Initial verification MD | `fc14da5e0d10947d5e39744bf3921187324d27f2a840aa5da8c17c579d8f026a` |
| Initial verification TSV | `ae0e09d2cd51586dea0981d80ac5f1ed773f3a70a0a57e5752036fecb2aceaf4` |
| Bibliography pre-patch / post-patch | `cd4ddfe1deee545a6212105a1d66fcce90c1fe265262d10e2f861ef79bd13c51` / `c4d71637e5676337326d2eb78dcdd64d78b4b116a397c50c54a081d7c5e2650b` |
| Inventory pre-patch / post-patch | `b6ae9947fa3bf71dfea8c4d2dc28c46c22eadb0440580366ff53caefbaae9f60` / `67ed7713bd6881d11466dc16755c7660a458c52e07ee072d086d6467f8ad7bd8` |
| `R10PH2-C01` | `RESOLVED_POST_VERIFICATION`: P29-S09 now carries the official first-party arXiv title in both patched inputs. |
| Corpus invariant | 22 unique inventory IDs; 22 verification TSV rows; no ID added or removed. |

The manifest itself and all four pre/post input hashes were re-computed from
the local files or matched to the manifest before this status migration. The
patched P29-S09 title is exact, so the prior metadata defect is closed without
changing existence, peer-review status, support class, or claim boundary.

## Method and audit coverage

- Inventory cardinality: **22 unique IDs** (`P29-S01` through `P29-S22`).
- DOI-bearing records: **21/22**, all checked through DOI-resolved publisher
  or official journal/book records.
- DOI-less records: **1/22** (`P29-S09`), checked on the first-party arXiv
  abstract record.
- Existence outcomes: **22 `VERIFIED`**, 0 `PLAUSIBLE`, 0 `UNVERIFIABLE`,
  0 `FABRICATED`, and 0 `S2_VERIFIED`.
- Core metadata: **22/22 records match after bounded normalization**.
  `P29-S09` was independently rechecked after the authorized title repair and
  is `RESOLVED_POST_VERIFICATION`. `P29-S11` and `P29-S13` retain external
  display conflicts, recorded below, but the inventory values agree with the
  stronger record set.
- Peer-reviewed journal/correction records: **17/22 = 77.3%**. The arXiv
  preprint, research book chapter, and three monographs remain explicitly
  outside that numerator.
- Independent second-source checks: **9/22 = 40.9%**, exceeding the 30%
  contract floor. These checks covered title, authors, year, venue, DOI, and,
  where material, page range.
- Mathematical evidence grading: every included item is recorded as
  field-neutral **Level VI**. The separate A–F grade is fitness for the exact
  bounded claim surface, not a biomedical-style experimental ranking.
- Venue assessment is bounded to publisher/journal identity, stated review
  status, and observable red flags. It is not an exhaustive commercial-index,
  COPE, or Cabells audit.
- No structured live retraction database query was run. Therefore every row
  is explicitly `NOT_CHECKED`; no row is described as retraction-clean.
- Source-level conflict declarations and funding statements were not audited
  in full text across the corpus. Every row is therefore `UNKNOWN_NOT_AUDITED`;
  no absence-of-conflict inference is made.

## Outcome summary

| Audit dimension | Result |
|---|---:|
| `VERIFIED` existence | 22 |
| Exact metadata after bounded normalization | 22 |
| Metadata errata unresolved | 0 |
| Metadata errata resolved post-verification | 1 |
| Field-neutral Level VI | 22 |
| Claim-fitness A | 7 |
| Claim-fitness B | 10 |
| Claim-fitness C | 5 |
| `DIRECT_PREREQUISITE` | 7 |
| `ADJACENT_METHOD` | 7 |
| `BACKGROUND_ONLY` | 8 |
| `EXCLUDE_FROM_CLAIM_USE` | 0 |

The A–F totals above are tied to the narrow “can support” surface in the next
table. They do not mean that any source earns full-mechanism status.

## Per-source claim-fitness and support boundary

| Source | Existence / metadata | Level / grade | Exact `support_class` | Can support | Cannot support |
|---|---|---|---|---|---|
| [P29-S01](https://doi.org/10.1016/j.aim.2020.107377) | `VERIFIED`; exact | VI / A | `DIRECT_PREREQUISITE` | Exact Picard-group quotient identity and primitive-geodesic terminology. | A Gaussian ideal-owner map, owner quotient, or `S_H`. |
| [P29-S02](https://doi.org/10.2140/ant.2022.16.1845) | `VERIFIED`; exact | VI / A | `DIRECT_PREREQUISITE` | The exact `PSL_2(Z[i])` geodesic object and Gaussian arithmetic setting. | Formal owner admissibility, split-ideal selection, or finite refinement. |
| [P29-S03](https://doi.org/10.1093/imrn/rnaa128) | `VERIFIED`; exact | VI / B | `BACKGROUND_ONLY` | Relevance of Gaussian arithmetic and ideals to Picard prime-geodesic analysis. | A unique primitive-class-to-prime-ideal assignment. |
| [P29-S04](https://doi.org/10.1515/form.2001.034) | `VERIFIED`; exact | VI / B | `BACKGROUND_ONLY` | Historical Picard-manifold prime-geodesic context. | An unconditional owner algorithm or Paper-29 certificate. |
| [P29-S05](https://doi.org/10.3792/pjaa.77.130) | `VERIFIED`; exact | VI / B | `BACKGROUND_ONLY` | Hyperbolic 3-manifold/Bianchi prime-geodesic context. | Computable conjugacy, primitive-root, or owner certificates. |
| [P29-S06](https://doi.org/10.1002/mana.201700190) | `VERIFIED`; exact; correction-bound | VI / C | `BACKGROUND_ONLY` | Broad hyperbolic-3/Bianchi prime-geodesic context only when bound to S07. | Corrected error-term exponents by itself, or any owner-map claim. |
| [P29-S07](https://doi.org/10.1002/mana.201800467) | `VERIFIED`; exact | VI / B | `BACKGROUND_ONLY` | The explicit correction/addendum relationship and corrected analytic boundary for S06. | Owner selection, quotient certification, or `S_H`. |
| [P29-S08](https://doi.org/10.1093/imrn/rnab048) | `VERIFIED`; exact | VI / B | `DIRECT_PREREQUISITE` | Primitive conjugacy-class and inversion/unoriented concepts in hyperbolic 3-manifolds. | Automatic transfer from compact lattices to a complete Picard-group decision procedure. |
| [P29-S09](https://arxiv.org/abs/2407.17959) | `VERIFIED`; exact; `RESOLVED_POST_VERIFICATION` | VI / C | `BACKGROUND_ONLY` | Current first-party preprint context for the exact Picard quotient and Gaussian conventions. | Peer-reviewed support, owner-map admissibility, or quotient completeness. |
| [P29-S10](https://doi.org/10.1090/S0025-5718-2015-02939-1) | `VERIFIED`; exact | VI / B | `ADJACENT_METHOD` | Explicit arithmetic-Kleinian fundamental-domain and presentation algorithms. | A complete conjugacy, maximal-root, or unoriented-owner algorithm. |
| [P29-S11](https://doi.org/10.2307/1971091) | `VERIFIED`; inventory exact; source-display conflict noted | VI / B | `ADJACENT_METHOD` | General effective decision procedures for arithmetic groups. | A concrete terminating Paper-29 quotient implementation or serialized certificate. |
| [P29-S12](https://doi.org/10.1016/j.top.2005.06.002) | `VERIFIED`; exact | VI / B | `ADJACENT_METHOD` | Algorithmic conjugacy in oriented geometrizable 3-manifold groups. | An unproved reduction to the level-(3) Bianchi matrix relation or canonical owner IDs. |
| [P29-S13](https://doi.org/10.1142/S0218196706002986) | `VERIFIED`; inventory exact; secondary page conflict noted | VI / C | `ADJACENT_METHOD` | Complexity-aware conjugacy algorithms under word-hyperbolic hypotheses. | Treating the nonuniform Picard lattice as satisfying those hypotheses without proof. |
| [P29-S14](https://doi.org/10.1112/jlms.12246) | `VERIFIED`; exact | VI / C | `ADJACENT_METHOD` | Constructive integral-matrix conjugacy and conjugator witnesses in `GL(n,Z)`. | Equating `GL(n,Z)` conjugacy with level-(3) `PSL_2(Z[i])` conjugacy. |
| [P29-S15](https://doi.org/10.1016/S0049-237X(08)71335-1) | `VERIFIED`; exact | VI / C | `ADJACENT_METHOD` | Primary arithmetic-group conjugacy methodology. | Peer-reviewed-journal weight, exact Picard applicability, or primitive-root closure. |
| [P29-S16](https://doi.org/10.1016/0001-8708(71)90027-2) | `VERIFIED`; exact | VI / B | `DIRECT_PREREQUISITE` | Presentations for relevant special linear/Bianchi-group cases and a word/matrix interface basis. | Conjugacy, primitivity, inversion invariance, or ideal-owner selection by itself. |
| [P29-S17](https://doi.org/10.1007/978-1-4757-6720-9) | `VERIFIED`; exact | VI / A | `BACKGROUND_ONLY` | Authoritative arithmetic-Kleinian, trace-field, and hyperbolic-3 background. | A registered direct owner formula or executable quotient certificate. |
| [P29-S18](https://doi.org/10.1007/978-3-662-03626-6) | `VERIFIED`; exact | VI / A | `BACKGROUND_ONLY` | Authoritative Bianchi/Picard action and imaginary-quadratic arithmetic definitions. | A proof that a Gaussian ideal owner refines finite collisions. |
| [P29-S19](https://doi.org/10.1007/978-3-662-02945-9) | `VERIFIED`; exact | VI / A | `DIRECT_PREREQUISITE` | Exact computational number-field/ideal factorization and splitting procedures. | Selecting which class invariant owns one literal split prime ideal. |
| [P29-S20](https://doi.org/10.1090/S0273-0979-1992-00284-7) | `VERIFIED`; exact | VI / B | `ADJACENT_METHOD` | Effective algebraic-number-theory problem and certificate context. | Candidate-map invariance, split-branch choice, or owner performance. |
| [P29-S21](https://doi.org/10.5802/jtnb.433) | `VERIFIED`; exact | VI / A | `DIRECT_PREREQUISITE` | Practical number-field and ideal-arithmetic algorithms with an implementation context. | A source-defined primitive conjugacy-class owner mechanism. |
| [P29-S22](https://doi.org/10.1090/mcom/3913) | `VERIFIED`; exact | VI / A | `DIRECT_PREREQUISITE` | Maximal-power detection and a witness ideal for an integral ideal. | Loxodromic group-element root detection, conjugacy closure, or owner selection. |

## Independent second-source cross-checks

The following nine key records received a second check independent of the
primary DOI/publisher landing page.

| Source | Independent authoritative locator | Facts cross-checked |
|---|---|---|
| P29-S01 | [Chalmers institutional record](https://research.chalmers.se/en/publication/518804) | title, authors, year, venue, volume/article number, DOI |
| P29-S02 | [CaltechAUTHORS record](https://authors.library.caltech.edu/records/0jfwd-29w48) | title, author, year, venue, volume/issue/pages, DOI |
| P29-S03 | [Hungarian Academy repository](https://real.mtak.hu/162289/) | title, four-author list, year, venue, volume/issue/pages, DOI |
| P29-S05 | [Tohoku University record](https://tohoku.elsevierpure.com/en/publications/prime-geodesic-theorem-via-the-explicit-formula-of-%CF%88-for-hyperbol/) | title, author, year, journal, volume/issue/pages, DOI |
| P29-S08 | [Bryn Mawr institutional repository](https://repository.brynmawr.edu/math_pubs/29/) | title, authors, journal, DOI, version context |
| P29-S10 | [Université de Bordeaux institutional record](https://oskar-bordeaux.fr/handle/20.500.12278/189576) | title, author, year, journal, volume/issue/pages, DOI |
| P29-S11 | [Dan Segal institutional publication record](https://www.asc.ox.ac.uk/person/professor-dan-segal) | author/title pair and bibliographic identity; used to adjudicate `Some` versus the Annals web display `Strong` |
| P29-S13 | [Warwick Research Archive record](https://wrap.warwick.ac.uk/id/eprint/33405/) | title, journal, year, volume/issue, and authoritative 287–305 page range |
| P29-S22 | [Denis Simon author/CNRS page](https://simond.users.lmno.cnrs.fr/) | authors, year, journal, volume/issue/pages, DOI |

## Venue, currency, COI, and retraction findings

1. The 17 journal/correction records are attached to established mathematics
   journals and recognized scholarly publishers; no observable predatory-venue
   red flag was found. This bounded finding does not assert a fresh audit of
   every index, editorial-board member, or ethics-policy field.
2. `P29-S09` is an authoritative first-party arXiv record but is not counted as
   peer reviewed. `P29-S15` is a research book chapter, and `P29-S17`–`S19`
   are monographs from an established academic publisher; peer review is not
   asserted for those five records.
3. The five 2021–2026 records (`S02`, `S03`, `S08`, `S09`, `S22`) satisfy the
   default currency window. Older sources are restricted to direct-object,
   historical, theorem, correction, or foundational algorithm claims and are
   currency-exempt only on those stated surfaces.
4. COI status remains `UNKNOWN_NOT_AUDITED` for every record. Funding observed
   on an institutional or publisher page was not converted into a conflict
   judgment.
5. Retraction status remains `NOT_CHECKED` for every record because no
   structured live retraction query was completed. The S06–S07 correction link
   is recorded as a known post-publication correction, not as a retraction
   clearance.

## Metadata errata and external-record discrepancies

| ID | Record | Finding | Disposition |
|---|---|---|---|
| ERR-P29-01 | P29-S09 | The first-party arXiv title begins **“On the Symmetric Square Large Sieve …”**. The authorized patch added the omitted initial “On the” to both the bibliography and inventory. | `RESOLVED_POST_VERIFICATION`. Both post-patch input hashes match the correction manifest; source existence remains `VERIFIED`, and no further metadata edit is requested. |
| DISP-P29-01 | P29-S11 | The current Annals web landing page displays **“Strong general algorithms. I: Arithmetic groups.”** JSTOR's DOI record and the author's Oxford institutional publication record give **“Some general algorithms. I: Arithmetic groups.”** | Source-side display conflict. The inventory's `Some` title is retained as the stronger record-set value; no inventory erratum is proposed. |
| DISP-P29-02 | P29-S13 | Some secondary DBLP metadata displays pages **287–306**. The publisher first-page record, Warwick institutional record, author record, and the inventory give **287–305**. | Secondary-record discrepancy. The inventory's 287–305 range is retained; no inventory erratum is proposed. |

No other title, author, year, venue, DOI, volume, issue, or page error was found
in the bounded verification pass.

## Paper-level Phase-2 disposition

**`PHASE2_SOURCE_BASE_READY_WITH_WARNINGS`**

The corpus clears the full-mode count and peer-review thresholds, every source
exists on an authoritative record, all 22 inventory IDs are accounted for, and
the verified set is fit to enter a later Phase-3 evidence-synthesis gate. The
P29-S09 title erratum is closed as `RESOLVED_POST_VERIFICATION`. Warnings
remain for the S11/S13 external display conflicts, the mandatory S06–S07
correction binding, unknown source-level COI, and the absence of a structured
live retraction check.

This disposition does not certify that a direct Gaussian prime-ideal owner
mechanism exists, that any candidate passes the frozen admissibility grammar,
or that a complete primitive/unoriented quotient procedure has been assembled.
Those are downstream theorem/interface questions. This is not a novelty
verdict, scientific result, computation authorization, or Route-A assignment.
