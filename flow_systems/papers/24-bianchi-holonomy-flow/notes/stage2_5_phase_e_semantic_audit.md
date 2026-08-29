# Stage 2.5 Phase-E semantic audit — Paper 24

Audit timestamp: `2026-08-29T01:59:26Z`  
Mode: ARS Stage 2.5, Mode 1, risk-stratified Phase E  
Protocol authority: ARS-Codex `claim_verification_protocol.md` and `evidence_row_protocol.md`  
Audit role: independent read-only semantic check of the rebuilt Claim Registry selection

## Current-status addendum — 2026-08-29

The bounded Phase-E decision below remains unchanged: 64/64 selected claims are
VERIFIED and all 66 required carriers remain explicitly `anchorless`.  After
this semantic audit was issued, the scholar-owned C4/D7 intake was supplied and
verified with 7 experiment-provenance entries and 11 aligned direct claims.
The overall Stage-2.5 status is now **PASS AT MANDATORY CHECKPOINT**, while
Stage 3 remains **not authorized** pending the required explicit checkpoint
decision.  Any later statement in this historical semantic-audit body saying
that the declaration is missing or the overall gate remains blocked is
superseded by this addendum.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

## Decision

**Phase E: PASS for the selected registry population.** All **64/64 selected distinct registry IDs** are semantically supported within their stated scope: **61/61 HIGH-IMPACT** and **3/3 RANDOM** are `VERIFIED`; there are no `MINOR_DISTORTION`, `MAJOR_DISTORTION`, `UNVERIFIABLE`, or `UNVERIFIABLE_ACCESS` verdicts. The exact evidence-row projection contains **66/66 required tuples**, because `P24-E1-012` cites three sources. All 66 persisted rows remain truthfully `anchorless`; no external excerpt is embedded or retrospectively source-bound.

This is a bounded Phase-E result, not a whole-paper correctness certificate. Semantic extraction completeness remains `not_machine_detectable`, underlying data truth and actual execution are outside the Phase-E denominator, and the missing scholar-owned experiment declaration still blocks the overall Stage-2.5 gate.

## Frozen bindings

| Input | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `e43ba0f77332b79df4d84346dcb6e3041c20f4bdded5a91f42caac348ea9fd11` |
| `paper/references.bib` | `11e7dd42f07ecf22744f5d9c829d13a22212e0d43cb2591c0e9dfd66bde86d87` |
| `paper/paper.pdf` | `e8dcfa74b967054a956521daa138a4cb397292c13674c19e1c03e218438759f1` |
| `notes/stage2_5_claim_registry.json` | `6a6fc0ebc3f76814638e49e378f2d64b086d06658cf54f1ccb877c0a8eedcdd4` |
| `notes/stage2_5_evidence_rows.json` | `fe1a8634f6e0a09f0be623b23dd248257a1844a5ed54ce9ce86cfdd0ea7f9890` |
| `notes/stage2_5_claim_registry_coverage.json` | `9e8c46db07e97ecadff4cda8e33f5c3ac754843ac2d7ab294594f59e58e20634` |

The protected manuscript, bibliography, PDF, registry, evidence rows, and coverage sidecar were not edited by this audit.

## Population, tier, and verdict closure

| Tier | Registered in tier | Selected | Checked | VERIFIED | Other verdicts |
|---|---:|---:|---:|---:|---:|
| HIGH-IMPACT | 61 | 61 | 61 | 61 | 0 |
| RANDOM | 3 | 3 | 3 | 3 | 0 |
| TOP-UP | 0 | 0 | 0 | 0 | 0 |
| NOT-SELECTED | 12 | 0 | 0 | — | — |
| **Total** | **76** | **64** | **64** | **64** | **0** |

The non-high-impact remainder is 15 rows; the protocol minimum makes the sentinel three rows. The selected RANDOM IDs are `P24-E1-002`, `P24-E1-005`, and `P24-E1-040`.

Verdict totals over distinct selected claim IDs:

| Verdict | Count |
|---|---:|
| VERIFIED | 64 |
| MINOR_DISTORTION | 0 |
| MAJOR_DISTORTION | 0 |
| UNVERIFIABLE | 0 |
| UNVERIFIABLE_ACCESS | 0 |

## Exact tuple closure and evidence-state boundary

The Claim Registry is the tuple-selection authority. For each selected internal claim, the expected projection is one `(claim_id, null-ref, none-anchor)` tuple. For `P24-E1-012`, the expected projection is one tuple for each of `HIKMOT2016`, `Reid1991`, and `SnapPyDocs2026`.

| Tuple class | Expected | Persisted | Exact ordered match | Evidence state |
|---|---:|---:|---|---|
| Project-internal/null-source tuples | 63 | 63 | yes | 63 `anchorless` |
| External citation tuples for `P24-E1-012` | 3 | 3 | yes | 3 `anchorless` |
| **Total** | **66** | **66** | **yes** | **66 `anchorless`** |

All 66 rows validate with the official ARS `evidence_rows.py` runtime. There are 64 distinct row `claim_id` values, the multi-source rows repeat identical claim metadata and verdict, and the ordered `(claim_id, ref_slug)` projection exactly equals the registry projection. `anchorless` means that the repository row contains no source excerpt, source-content hash, or source byte span. The semantic verdict does not upgrade that provenance state, and this audit does not create a human-read mark.

The coverage sidecar replay also passes. Its bounded grammar finds seven citation-bearing or quantitative candidates, all seven are `registry_span_matched`, and `candidate_unregistered_count=0`. This does **not** prove semantic extraction completeness; the recorded value remains `not_machine_detectable`.

## Semantic support map

Each ID below was read individually against the exact manuscript span. Grouping is only a compact presentation of the primary support chain; it is not group-level inference.

Support codes:

- `P24-GEO`: manuscript lines 62–127, the level-three torsion proof, the declared owner/type boundary, and the already completed official source/context audit.
- `P24-EXT`: the completed Phase-A/B source audit plus the three-ref-slug locator review below for the three citation tuples.
- `P24-UNI`: manuscript lines 160–230; direct determinant expansion and cancellation; algebra independently rederived during this audit.
- `P24-POW`: manuscript lines 232–251; Cayley–Hamilton recurrence and the polynomial trace identity independently checked.
- `P24-JET`: manuscript lines 218–285; reduction modulo `m^2`, inversion, power, ambient-action boundary, and explicit non-injectivity witnesses independently checked.
- `P24-CERT`: the Round-7 ledger/metrics, Round-8 freeze/metrics/collision/control artifacts, receipt, validation note, 71 historical tests, and 14 verify-only Round-8 tests.
- `P24-SCOPE`: manuscript claim boundaries, limitations, Route-A evaluator, and the pre-result freeze; checked to ensure no finite or proxy credit is promoted to full-flow ownership, arithmetic Euler factors, or a spectrum.

| Support | Selected claim IDs checked individually | Count | Verdict |
|---|---|---:|---|
| `P24-SCOPE` with theorem/certificate cross-check | `P24-E1-001`, `003`, `004`, `005`, `014`, `015`, `016`, `017`, `023`, `054`, `056`, `057`, `058`, `062`, `063`, `064`, `068`, `069`, `070`, `071`, `072`, `073`, `076` | 23 | all VERIFIED |
| `P24-GEO` | `P24-E1-002`, `006`, `007`, `008`, `009`, `010`, `011` | 7 | all VERIFIED |
| `P24-EXT` | `P24-E1-012` | 1 | VERIFIED across three source tuples |
| `P24-UNI` | `P24-E1-018`, `019`, `020`, `021`, `022`, `024`, `025` | 7 | all VERIFIED |
| `P24-POW` | `P24-E1-026`, `027`, `031`, `032`, `033`, `034`, `035`, `036`, `037` | 9 | all VERIFIED |
| `P24-JET` | `P24-E1-029`, `030`, `038`, `039`, `040`, `041` | 6 | all VERIFIED |
| `P24-CERT` | `P24-E1-042`, `043`, `044`, `046`, `048`, `049`, `050`, `051`, `052`, `053`, `055` | 11 | all VERIFIED |
| **Total** | **every selected ID exactly once** | **64** | **64 VERIFIED** |

### Proof and certificate findings

- The determinant expansion and universal normalized-discriminant formula follow by direct expansion and cancellation by the declared non-zero-divisor. The integer, Gaussian, and Eisenstein specializations stay within that scope.
- The trace-power identity is a polynomial consequence of Cayley–Hamilton. The displayed `D_{m^2}` consequence is valid on the earlier declared domain where `D_{m^2}` is defined; see the notation note below.
- The first-jet laws follow modulo `m^2`; the signed quotient handles inversion but is explicitly not claimed as an ambient-conjugacy classifier.
- The constructive matrices in `P24-E1-041` have equal determinant zero and unequal signed residues because `i` is not congruent to `+1` or `-1` modulo 3.
- Fresh read-only replay produced **71/71 historical tests PASS** and **14/14 Round-8 tests PASS**. The Round-8 reproducer verified existing artifacts, two builds were byte-identical, and the reported primary hash was `cacf5b84d9faecdca1cdfc5e0082cbf21cf491fbfe75835d41919d4c9c5f54f3`.
- Exact artifacts support 11,481 matrices, 145 scalar values, 517 joint descriptors, 11,336 scalar collision rows, 10,964 joint collision rows, 372 resolved rows, maximum buckets 505 and 84, and zero singleton joint buckets. Arithmetic checks give `11,481-145=11,336`, `11,481-517=10,964`, `11,336-10,964=372`, `517/145≈3.57`, and `505/84≈6.01`.
- The control ledger supports 6,396 total exact rows/witnesses, 6,392 principal-congruence rows, 4/4 frozen families, and only 2/3 canonical Route-A control types. The manuscript preserves that incomplete gate rather than promoting four families into three canonical types.

## External citation tuples for `P24-E1-012`

The following short quotations are **audit-note candidates only**. Each is at most 25 whitespace-split words. They were not inserted into `stage2_5_evidence_rows.json`; therefore the three persisted rows remain `anchorless`, without source bytes, hashes, or spans.

| `ref_slug` | Specific official/author locator used | Short excerpt candidate | Words | Semantic allocation |
|---|---|---|---:|---|
| `HIKMOT2016` | [Author-submitted arXiv full text, abstract and §§3–5](https://arxiv.org/html/1310.3410v2); abstract lines 45–47, package discussion, and Theorem 5.1 | “we describe a method to rigorously prove that either M or a filling of M admits a complete hyperbolic structure” | 20 | Supports interval/verified computation certifying a complete hyperbolic structure from triangulation data. |
| `SnapPyDocs2026` | [Official SnapPy 3.3.2 verified-computation documentation](https://snappy.computop.org/verify.html), Introduction and `verify_hyperbolicity()` overview | “Many of these SnapPy methods can be supplied with a verified flag to ensure that the result is provably correct.” | 20 | Supports the manuscript’s distinction between ordinary floating-point output and verified interval results. |
| `Reid1991` | [Official OUP/LMS version-of-record page](https://academic.oup.com/jlms/article/s2-43/1/171/888921/Arithmeticity-of-Knot-Complements), main theorem; full VOR PDF is access-controlled in this automated session. Corroborating author-hosted text: [Garoufalidis–Reid PDF](https://web.ma.utexas.edu/users/areid/isospec_JTA.pdf) | “The figure-eight knot complement is the only arithmetic knot complement” | 10 | Together with the locally fixed identity of `5_2` as a non-figure-eight hyperbolic knot complement, supports its non-arithmetic control role. The candidate is corroboration, not a claimed excerpt from the inaccessible 1991 VOR. |

Compound-claim adjudication: `HIKMOT2016`, `SnapPyDocs2026`, and `Reid1991` support three separate sentences inside `P24-E1-012`; no one source is treated as supporting the entire compound block. The prior Phase-A/B audit already records the publisher-level bibliographic and citation-context checks. No contradiction or strength inflation was found.

## Nonblocking registry/notation observations

These observations do not change the Phase-E verdict and are not manuscript-edit authority.

- `P24-E-NOTE-001`: `P24-E1-021` is a mechanically registered theorem heading/label, not a standalone substantive proposition. It was checked together with the immediately following full corollary `P24-E1-022` and is counted as a verified registry ID. Consequently, “64 selected registry IDs” must not be rephrased as “64 independent scientific propositions.”
- `P24-E-NOTE-002`: in `P24-E1-031`/`P24-E1-033`, the trace identity is stated for every `gamma in SL_2(R)`, while the `D_{m^2}` consequence inherits the earlier definition’s principal-congruence/cancellable-level domain rather than rebinding `m` in the proposition. The consequence is algebraically correct on that declared domain and every frozen use lies in it, so no distortion is assigned. A later authorized editorial revision could state the inherited condition explicitly.

No selected claim was found to exaggerate a finite ledger into a complete conjugacy/orbit census, transfer proxy credit to the full Bianchi flow, claim Gaussian-specificity after the universal control, or assert an arithmetic/spectral construction that is absent.

## Remaining blocker outside Phase E

`IL-SERIOUS-1` from the independent Stage-2.5 audit remains open: the paper reports project-owned computational results but lacks the scholar-owned `experiment_intake_declaration`, experiment provenance, and claim alignment required by Phase C4/D7. The Phase-E PASS does not close that defect and does not authorize Stage 3.
