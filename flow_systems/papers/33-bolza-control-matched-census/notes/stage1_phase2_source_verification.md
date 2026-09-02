# Paper 33 — Stage 1 Phase 2 Independent Source Verification

Date: **2026-09-02 UTC**  
Seat: **VERIFY-SEAT-B**  
Corpus: **20 source IDs, S01–S20**  
Phase-2 disposition: **PHASE2_SOURCE_BASE_READY_WITH_WARNINGS**

## Verification boundary

This report verifies the existence, bibliographic metadata, venue class, currency, and bounded claim fitness of the fixed P33 Phase-2 corpus. It does not edit the annotated bibliography or source inventory. It does not synthesize a literature answer, decide novelty, run a census, issue a scientific result, assign a Route status, or authorize execution.

Pure-mathematics sources are graded under the contract's field-neutral ladder: an original theorem, construction, or algorithm paper is normally Level VI, with a separate A–F claim-fitness grade. The invited validated-numerics survey S18 is Level VII because it functions here as an expert review rather than as the original source of one P33 theorem.

## Hash-bound inputs and post-patch replay

| Input | SHA-256 |
|---|---|
| BATCH_ROUND10_STAGE1_PHASE2_VERIFICATION_CONTRACT.md | 41f3881f0fa428c3ce324a12f12bd514649aff652114cc436d5932fb3cb8b72e |
| ARS source_verification_agent.md | 3ffecae526acdde6d28bb8d2a9f5a88f95c00f51338c8f4d4a724ced3f7777bf |
| stage1_phase1_rq_brief.md | bc63d6b556ac3027adbbbbf08eab1908854465db4cdcc259a640e1c9c4965776 |
| stage1_phase1_methodology_blueprint.md | 81ef00c3ed27dfe4c1da4f27e32aa6b9296e64dd132da0dd9d680cadfad7ae82 |
| stage1_phase1_resolution.md | 16dd38054f1b1692fbb7c564370f399c475d87ad215e22de924be8fc1c245edc |
| stage1_phase1_checkpoint.md | a22657b85d0f2613d9c32f12ec1e92d835a0653cc8bfef48b01ff4f40dee5285 |
| stage1_phase1_devils_advocate_recheck.md | f938a7687d29fc643a9319b780a850954dddf4ac60942b325f6e434a625d538a |
| Initial pre-patch stage1_phase2_annotated_bibliography.md | 42247115b3a96bd90b4d46f1864195217856054f6bdfc3e45d460ecf7038831c |
| Initial pre-patch stage1_phase2_source_inventory.tsv | a01ee3d4056e3a27396a4de8411e9825720dbc186e157c2778993f957f156409 |
| Initial verification report (pre-recheck bytes) | 3f8aeb32dd82ce900ca43631c6f142939353b7cee6085eaf0ddeee36bb8e7e65 |
| Initial verification TSV (pre-recheck bytes) | d2b3ce8145f93e7e1a75c1b72c3c69036075400b5e8801b40872d32ad08c6f64 |
| BATCH_ROUND10_STAGE1_PHASE2_METADATA_CORRECTION_MANIFEST.md | 59506776c0c536dbfd5b3ee511dd0ac0a52ae74548d08f3cd0dfb7ec9a8fd49c |
| Current post-patch stage1_phase2_annotated_bibliography.md | 38e98f66c21e61b448aef8184600d8a46550ad58b4fa69f0a30bd51b24474792 |
| Current post-patch stage1_phase2_source_inventory.tsv | b1934dba37ff62c263bc33d617425fd85aba1d45efa204ef7ce315651e427b87 |

### Authorized post-patch replay

VERIFY-SEAT-B re-read the correction manifest and the current P33 bibliography
and inventory. Their hashes exactly match the manifest's post-patch hashes.
Operation `R10PH2-C06` changes only the S12 page range from `287--306` /
`287-306` to `287--305` / `287-305`; it changes no source ID, author, DOI,
peer-review flag, evidence grade, support class, scientific value, or claim
surface. The initial mismatch finding remains recorded below as provenance.

Post-patch status: **`RESOLVED_POST_VERIFICATION`**. The current S12 metadata
now agrees with the DOI registry, article PDF header, and author publication
list. This verifier did not edit either source table.

The structured S2 replay also detected that the initial S13 audit trail had
dropped one hexadecimal character from the API paper ID. A fresh Graph API DOI
lookup for `10.1070/IM1990v035n01ABEH000693` returned the 40-character paper ID
`fc9fef53621db8ebd135e3ec04c9ebc1cca078a2`, the exact normalized title, and
year 1990. The verifier artifacts now carry that exact ID; the source metadata,
existence outcome, evidence grade, and claim boundary are unchanged.

## Verification procedure and API audit

### Semantic Scholar

A real Semantic Scholar Graph API batch request was made for all 19 inventory records carrying a DOI.

- Batch response: HTTP 200.
- Exact or allowed-year matches: 9.
- DOI lookups returning no S2 record: 5.
- Title matches whose S2 year represented a preprint and fell outside the contract's publication-year window: 5.
- A DOI-less title search for S06 was attempted after the batch and returned HTTP 429. It was not retried or bypassed. S06 was instead checked through authoritative mathematical archives.

The nine records labeled S2_VERIFIED meet normalized-title similarity at least 0.70 and an exact or ±1 year match:

| Source | S2 paper ID | Title similarity | Year comparison |
|---|---|---:|---|
| S02 | c77541d2539e3f0e14f8161f61c6f2c3a8e39d56 | 1.000 | 2005 = 2005 |
| S03 | 693c1acc3237da4934544da273890d55a93f6267 | 1.000 | 1975 = 1975 |
| S05 | a401c3aea90def22de8f28a4e58cb4817180e92e | 1.000 | 1991 = 1991 |
| S07 | 9de301e7542fbe4dda6a9bdd5ce67e630dff337b | 0.965 | 1993 = 1993 |
| S09 | d0d378e82d4ac88c654b9b535048f01ec0a26fc1 | 1.000 | 2010 = 2010 |
| S10 | 4f046d6423b949d99a5be39de374ef5a64e0f00d | 1.000 | 2008 versus 2009 |
| S12 | 76b96ce716f2c56bdcee228ef73162f55a81fbb6 | 1.000 | 2006 = 2006 |
| S13 | fc9fef53621db8ebd135e3ec04c9ebc1cca078a2 | 1.000 | 1990 = 1990 |
| S17 | 2cabb8a7fa81dd65a234076e21b3acb98e211763 | 1.000 | 2016 versus 2017 |

No other record is labeled S2_VERIFIED. An S2 null return or preprint-year mismatch was treated as API/record behavior, not as evidence against the work.

### DOI and first-party verification

- DOI-bearing records were checked against DOI metadata and/or a first-party publisher, journal, proceedings, arXiv, or institutional endpoint.
- S11's DOI did not appear in the Crossref API response, but DOI resolution and the first-party DROPS proceedings page exactly confirmed the record.
- S01 was confirmed by the official arXiv record, including author, submission year, version, and arXiv-issued DataCite DOI.
- S06 was confirmed by EuDML and ETH E-Periodica without inventing a publisher DOI.
- Title, author, year, venue, volume/issue, and pages or article number were compared where the authoritative endpoint exposed them.

### Retraction and conflict limits

No systematic Retraction Watch, PubPeer, institutional COI, grant, or author-disclosure audit was run. Accordingly, the machine record says NOT_CHECKED instead of inferring a clean result from search silence.

Two visible correction records are reported:

- S03's J-STAGE page records a 2006 citation/PDF correction; it is not described as a retraction.
- S16 has a published 2018 correction, DOI 10.1007/s00220-018-3094-z; later claim use must select an unaffected or corrected statement.

## Overall source-base accounting

| Measure | Result |
|---|---:|
| Inventory IDs expected | 20 |
| IDs verified exactly once | 20 |
| Coverage | 100% |
| S2_VERIFIED | 9 |
| VERIFIED | 10 |
| PLAUSIBLE | 1 |
| UNVERIFIABLE | 0 |
| FABRICATED | 0 |
| Peer-reviewed works retained | 18/20 = 90% |
| Level VI | 19 |
| Level VII | 1 |
| Claim-fitness A | 4 |
| Claim-fitness B | 11 |
| Claim-fitness C | 5 |
| Claim-fitness D–F | 0 |
| Authorized metadata corrections resolved on replay | 1 (S12 page range) |

The two conservatively non-peer-reviewed items are S01, an author preprint on arXiv, and S04, a Springer book chapter whose peer-review status was not confirmed. S06 is a journal article verified through authoritative archives. No included venue presented a predatory-publisher signal at the checked first-party endpoint, but this was not a systematic Scopus, Web of Science, COPE, DOAJ, or Cabell audit.

## Per-source quality matrix

The machine-auditable wording and locators are in stage1_phase2_source_verification.tsv.

| ID | Outcome | Level / fitness | Bounded support | Stronger claim not licensed |
|---|---|---|---|---|
| S01 | VERIFIED | VI / A | Original two-parameter octagon construction and generators | Frozen specialization's nonarithmeticity, systole, census, or certificate schema |
| S02 | S2_VERIFIED | VI / B | Peer-reviewed genus-two octagon-family corroboration | Selection or closure of the frozen control |
| S03 | S2_VERIFIED | VI / A | Takeuchi arithmetic-Fuchsian criterion | Project-specific application to the frozen trace formula |
| S04 | VERIFIED | VI / B | Lindemann–Weierstrass theorem ingredient | Fuchsian, systolic, or census conclusion |
| S05 | S2_VERIFIED | VI / B | Regular-octagon matrices, length law, and enumeration precedent | Full P33 owner quotient or completeness |
| S06 | PLAUSIBLE | VI / C | Authoritative Bolza/regular-octagon historical context | Exact P33 systole claim without page-level theorem pinpointing |
| S07 | S2_VERIFIED | VI / B | Systolic/extremal Riemann-surface context | Exact Bolza replay or owner census |
| S08 | VERIFIED | VI / A | Detailed Bolza arithmetic Fuchsian group/quaternion structure | P33 manifest completeness |
| S09 | S2_VERIFIED | VI / B | Genus-two symbolic length-spectrum computation | Full conjugacy, inversion, primitivity, or serialized closure |
| S10 | S2_VERIFIED | VI / B | Exact fundamental-domain/presentation algorithms for suitable Fuchsian input | Turnkey transcendental-control conjugacy/certificate method |
| S11 | VERIFIED | VI / B | Terminating Dirichlet-domain algorithm for polygon input | Exact algebraic-number or conjugacy-certificate serialization |
| S12 | S2_VERIFIED | VI / B | General linear-time word-hyperbolic conjugacy decision and positive conjugator | Frozen-group instantiation, negative certificate, or P33-RC-1 closure |
| S13 | S2_VERIFIED | VI / A | Root-extraction solvability in hyperbolic groups | P33 maximal-root implementation or serialized no-root certificate |
| S14 | VERIFIED | VI / C | Primitive/root-conjugacy semantic context | Frozen census or general inversion-pair canonicalizer |
| S15 | VERIFIED | VI / B | Reciprocal geodesics and elements conjugate to inverses | External inversion pairing for every owner |
| S16 | VERIFIED | VI / C | Rigorous bounded-computation/completeness architecture | Geodesic-owner census; correction must be respected |
| S17 | S2_VERIFIED | VI / B | Arbitrary-precision ball arithmetic and error radii | Group conjugacy, primitivity, or completeness by itself |
| S18 | VERIFIED | VII / B | General validated floating-point methodology | Fuchsian or P33 certificate theorem |
| S19 | VERIFIED | VI / C | Hyperbolic-geometry validation precedent | Validation of closed genus-two P33 outputs |
| S20 | VERIFIED | VI / C | Formalization and independent-checking architecture | A mandated proof-assistant design or P33-RC-1 closure |

## Errata and metadata advisories

### ERR-P33-PH2-S12-01 — page range

- Source: S12, Epstein and Holt (2006).
- Initial inventory value: 287-306, bound to pre-patch inventory SHA-256 `a01ee3d4056e3a27396a4de8411e9825720dbc186e157c2778993f957f156409`.
- Verified value: 287-305.
- Basis: DOI registry metadata, the article PDF header, and Derek Holt's first-party publication list.
- Severity: Minor metadata error.
- Authorized correction: manifest operation `R10PH2-C06`, manifest SHA-256 `59506776c0c536dbfd5b3ee511dd0ac0a52ae74548d08f3cd0dfb7ec9a8fd49c`.
- Current value and binding: 287-305; post-patch inventory SHA-256 `b1934dba37ff62c263bc33d617425fd85aba1d45efa204ef7ce315651e427b87`, post-patch bibliography SHA-256 `38e98f66c21e61b448aef8184600d8a46550ad58b4fa69f0a30bd51b24474792`.
- Recheck disposition: `RESOLVED_POST_VERIFICATION`. VERIFY-SEAT-B confirmed the authorized bytes but did not edit the source tables.
- Claim impact: none on the theorem's bounded support, but the manuscript citation must use the corrected page range.

### S06 DOI advisory — no inventory correction

EuDML confirms the claimed DOI-less bibliographic record. ETH E-Periodica assigns the digitized archival object DOI 10.5169/seals-45391; this is not silently substituted as a publisher article DOI. The inventory's blank DOI field is therefore retained, with the archival identifier disclosed only as an advisory.

### Publication-year variants — no inventory correction

Several registry records use first-online or preprint years while the inventory uses the journal/book issue year: S04, S08, S10, S14, S16, S17, S19, and S20. The first-party or DOI metadata otherwise matched. These variants explain why some exact-title S2 records did not satisfy the formal year window; they are not treated as evidence of fabrication.

## Claim-surface and P33-RC-1 audit

The verified corpus is fit to support a later bounded synthesis of:

1. the two octagon construction families and exact Bolza group context;
2. the arithmeticity criterion and transcendence ingredient, kept as a multi-source project derivation rather than a quotation from Nazarenko;
3. general word-hyperbolic conjugacy and root-extraction solvability;
4. primitive, repeated, reciprocal, and inverse-related geodesic semantics;
5. exact-domain, interval-validation, bounded-completeness, serialization, and independent-checking precedents.

The corpus does not close P33-RC-1. In particular:

- S12 proves a general conjugacy algorithm and can return a conjugating element in the positive case, but does not freeze either P33 presentation, canonical normal form, negative-certificate fields, deterministic bytes, or independent validator.
- S13 proves root-extraction solvability, but does not supply P33's exact maximal-root/no-root payload or its serializer.
- S10 and S11 address fundamental/Dirichlet domains, not a complete positive-and-negative conjugacy certificate contract for the frozen groups.
- S17–S20 are rigorous-computation and checking precedents; analogy does not instantiate the missing contract.

Before any future scientific execution, a separate authorized freeze must still identify the theorem/algorithm and implementation versions, positive witness fields, negative or canonical certificate fields, termination/completeness payload, deterministic ordering and hashes, and independent-validator rules. If this cannot be done, the Phase-1 fail-closed not-evaluable path remains the only licensed execution disposition. This source-verification report does not itself issue that execution disposition.

## Phase-2 disposition

**PHASE2_SOURCE_BASE_READY_WITH_WARNINGS**

Rationale:

- all 20 inventory IDs exist and have an authoritative locator;
- 19 are S2_VERIFIED or VERIFIED, and the sole PLAUSIBLE item is a DOI-less historical article confirmed by two authoritative mathematical archives;
- the corpus retains 18/20 peer-reviewed works, above the 60% contract threshold;
- no fabrication, unverifiable source, or integrity block was found;
- the initial S12 page-range error was corrected under manifest operation `R10PH2-C06` and independently rechecked as `RESOLVED_POST_VERIFICATION`;
- S06's exact systole claim surface still requires page-level pinpointing;
- S03 and S16 correction records must be respected;
- COI and retraction status remain explicitly not systematically checked; and
- the source base supports method investigation but does not close the preexecution serialization/validator gap P33-RC-1.

This disposition permits only the next separately authorized research-pipeline step. It is not a novelty verdict, scientific result, Route assignment, census authorization, or claim that the missing certificate contract exists.

### Material Passport

- Origin skill: academic-research-suite / deep-research
- Agent role: source_verification_agent
- Seat: VERIFY-SEAT-B
- Phase: Stage 1 / Phase 2 source verification only
- Verification date: 2026-09-02 UTC
- Corpus coverage: 20/20
- Phase-2 disposition: PHASE2_SOURCE_BASE_READY_WITH_WARNINGS
- Bibliography/inventory mutation by VERIFY-SEAT-B: none
- Authorized metadata correction replay: RESOLVED_POST_VERIFICATION
- Metadata correction manifest SHA-256: 59506776c0c536dbfd5b3ee511dd0ac0a52ae74548d08f3cd0dfb7ec9a8fd49c
- Current bibliography/inventory hashes: 38e98f66c21e61b448aef8184600d8a46550ad58b4fa69f0a30bd51b24474792 / b1934dba37ff62c263bc33d617425fd85aba1d45efa204ef7ce315651e427b87
- S2 structured replay: 9/9 rows satisfy 40-hex paper ID, similarity at least 0.70, and exact or ±1 year; S13 audit-trail transcription repaired
- Phase-3 synthesis: NOT_RUN
- Scientific computation: NOT_RUN
