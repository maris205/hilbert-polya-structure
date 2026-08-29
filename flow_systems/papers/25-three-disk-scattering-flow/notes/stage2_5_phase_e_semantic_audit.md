# Stage 2.5 Phase-E semantic audit — Paper 25

Audit timestamp: `2026-08-29T02:03:24Z`  
Mode: ARS Stage 2.5, Mode 1, risk-stratified Phase E  
Protocol authority: ARS-Codex `claim_verification_protocol.md` and `evidence_row_protocol.md`  
Audit role: independent read-only semantic check of the rebuilt Claim Registry selection

## Current-status addendum — 2026-08-29

The bounded Phase-E decision below remains unchanged: 48/48 selected claims are
VERIFIED and all 49 required carriers remain explicitly `anchorless`.  After
this semantic audit was issued, the authorized `BowenLanford1970` suffix repair
was revalidated, and the scholar-owned C4/D7 intake was supplied and verified
with 7 experiment-provenance entries and 6 alignment records.  The overall
Stage-2.5 status is now **PASS AT MANDATORY CHECKPOINT**, while Stage 3 remains
**not authorized** pending the required explicit checkpoint decision.  Any
later statement in this historical semantic-audit body saying that either
former defect remains open is superseded by this addendum.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

## Decision

**Phase E: PASS for the selected registry population.** All **48/48 selected distinct registry IDs** are semantically supported within their stated scope: **45/45 HIGH-IMPACT** and **3/3 RANDOM** are `VERIFIED`; there are no `MINOR_DISTORTION`, `MAJOR_DISTORTION`, `UNVERIFIABLE`, or `UNVERIFIABLE_ACCESS` verdicts. The exact evidence-row projection contains **49/49 required tuples**, because `P25-E1-015` cites two sources. All 49 persisted rows remain truthfully `anchorless`; no external excerpt is embedded or retrospectively source-bound.

This is a bounded Phase-E result, not a whole-paper correctness certificate. Semantic extraction completeness remains `not_machine_detectable`, underlying data truth and actual execution are outside the Phase-E denominator, and the bibliography-author defect plus missing scholar-owned experiment declaration still block the overall Stage-2.5 gate.

## Frozen bindings

| Input | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `283695c485a2a48abfab1ef0fe3d479f597f68f3082e20f4a5a1894ca37baefb` |
| `paper/references.bib` | `acec840393408f146f5e6eed9723cd4e12275108a6059fe0fdb0c2bc508e7248` |
| `paper/paper.pdf` | `608b669835f55c02bf5e43c570878728865e8659a58dbd23dae02dbf16dd101f` |
| `notes/stage2_5_claim_registry.json` | `57063b60063a873d909506e6fcf8c3bd938c4fed57de06cb58beee0daca76956` |
| `notes/stage2_5_evidence_rows.json` | `26e7fd2a6f628e463c5fb8f224f17851d55bd65fb67d726aa4dcd0b72e27eb89` |
| `notes/stage2_5_claim_registry_coverage.json` | `0b68204e8a47ae36c68467dddd6fbde480f7de7063e5eabc213ff1dddc481a8d` |

The protected manuscript, bibliography, PDF, registry, evidence rows, and coverage sidecar were not edited by this audit.

## Population, tier, and verdict closure

| Tier | Registered in tier | Selected | Checked | VERIFIED | Other verdicts |
|---|---:|---:|---:|---:|---:|
| HIGH-IMPACT | 45 | 45 | 45 | 45 | 0 |
| RANDOM | 3 | 3 | 3 | 3 | 0 |
| TOP-UP | 0 | 0 | 0 | 0 | 0 |
| NOT-SELECTED | 24 | 0 | 0 | — | — |
| **Total** | **72** | **48** | **48** | **48** | **0** |

The non-high-impact remainder is 27 rows; the protocol minimum makes the sentinel three rows. The selected RANDOM IDs are `P25-E1-016`, `P25-E1-043`, and `P25-E1-064`.

Verdict totals over distinct selected claim IDs:

| Verdict | Count |
|---|---:|
| VERIFIED | 48 |
| MINOR_DISTORTION | 0 |
| MAJOR_DISTORTION | 0 |
| UNVERIFIABLE | 0 |
| UNVERIFIABLE_ACCESS | 0 |

## Exact tuple closure and evidence-state boundary

The Claim Registry is the tuple-selection authority. For each selected internal claim, the expected projection is one `(claim_id, null-ref, none-anchor)` tuple. For `P25-E1-015`, the expected projection is one tuple for each of `GaspardRice1989Exact` and `Wirzba1999`.

| Tuple class | Expected | Persisted | Exact ordered match | Evidence state |
|---|---:|---:|---|---|
| Project-internal/null-source tuples | 47 | 47 | yes | 47 `anchorless` |
| External citation tuples for `P25-E1-015` | 2 | 2 | yes | 2 `anchorless` |
| **Total** | **49** | **49** | **yes** | **49 `anchorless`** |

All 49 rows validate with the official ARS `evidence_rows.py` runtime. There are 48 distinct row `claim_id` values, the two source rows repeat identical claim metadata and verdict, and the ordered `(claim_id, ref_slug)` projection exactly equals the registry projection. `anchorless` means that the repository row contains no source excerpt, source-content hash, or source byte span. The semantic verdict does not upgrade that provenance state, and this audit does not create a human-read mark.

The coverage sidecar replay also passes. Its bounded grammar finds one citation-bearing or quantitative candidate, it is `registry_span_matched`, and `candidate_unregistered_count=0`. This does **not** prove semantic extraction completeness; the recorded value remains `not_machine_detectable`.

## Semantic support map

Each ID below was read individually against the exact manuscript span. Grouping is only a compact presentation of the primary support chain; it is not group-level inference.

Support codes:

- `P25-SCOPE`: manuscript claim boundaries, typed-object distinctions, limitations, Route-A evaluator, and the frozen negative-control conclusion; checked to prevent unit-roof or local-stability credit from being promoted to the physical flow or exact quantum scattering.
- `P25-GEO`: the no-eclipse contract, exact period-two/period-three geometry, cohomological telescoping obstruction, constant-roof nontransfer theorem, minimax bound, and dimensionless frozen mismatch.
- `P25-EXT`: the completed Phase-A/B source audit plus the two-source-locator review below for both citation tuples.
- `P25-Q`: the direct `q`-symbol adjacency-spectrum, trace, Möbius primitive-count, and Euler-determinant proof, cross-checked against the frozen `q=2,...,8` certificate.
- `P25-SYM`: the three-symbol specialization, owner/repetition bookkeeping, determinant identity, pole location, and declared unit-roof scope.
- `P25-HALF`: the two-dimensional hyperbolic symplectic eigenvalue calculation and half-density factorization, including the local-stability-only boundary.
- `P25-CERT`: the exact witness, owner/stability/conditioning, replay, receipt, and summary artifacts; 65 historical tests and 12 verify-only Round-8 tests.

| Support | Selected claim IDs checked individually | Count | Verdict |
|---|---|---:|---|
| `P25-SCOPE` with theorem/certificate cross-check | `P25-E1-001`, `004`, `005`, `006`, `017`, `023`, `026`, `039`, `040`, `041`, `043`, `045`, `052`, `055`, `056`, `058`, `064`, `067`, `072` | 19 | all VERIFIED |
| `P25-GEO` | `P25-E1-012`, `013`, `031`, `032`, `033`, `034`, `035`, `036`, `037`, `042` | 10 | all VERIFIED |
| `P25-EXT` | `P25-E1-015` | 1 | VERIFIED across two source tuples |
| `P25-Q` | `P25-E1-016` | 1 | VERIFIED |
| `P25-SYM` | `P25-E1-014`, `019`, `020`, `021`, `024`, `025` | 6 | all VERIFIED |
| `P25-HALF` | `P25-E1-027`, `028`, `029`, `030` | 4 | all VERIFIED |
| `P25-CERT` | `P25-E1-044`, `047`, `048`, `049`, `050`, `051`, `053` | 7 | all VERIFIED |
| **Total** | **every selected ID exactly once** | **48** | **48 VERIFIED** |

### Proof and certificate findings

- The no-eclipse inequality follows from the exact segment-to-third-centre clearance for the symmetric two-disk orbit; `d>4a/sqrt(3)` is sufficient for all frozen symmetric witnesses.
- The period-two owner has total length `2(d-2a)` and mean roof `d-2a`; the period-three owner has total length `3(d-sqrt(3)a)` and mean roof `d-sqrt(3)a`. Their positive gap `(2-sqrt(3))a` proves noncohomology to a constant by periodic-orbit telescoping and forbids an owner- and repetition-preserving scalar substitution. The two-point minimax lower bound is half that gap.
- For `A_q=J_q-I_q`, the eigenvalues are `q-1` once and `-1` with multiplicity `q-1`. Direct trace/Möbius inversion gives the stated primitive-owner counts and Euler determinant. The `q=3` frozen total through degree 12 is 747.
- The half-density identity follows from the reciprocal real hyperbolic eigenvalues of a two-dimensional symplectic return map. The manuscript correctly keeps this as a local stability identity rather than a physical-flow determinant.
- Fresh read-only replay produced **65/65 historical tests PASS** and **12/12 Round-8 tests PASS**. The Round-8 verifier rebuilt twice byte-identically and verified the existing 2,241-row core artifact with SHA-256 `9a29d8894b1ac81f9588fe221375bddc671898b9b08b409b0fa5a1d5a42a9014`.
- The `q`-symbol certificate has 84 count rows and 182 prefix rows for `q=2,...,8`. The half-density ledger has 6,723 rows, exactly 2,241 owners times repetitions 1, 2, and 3.
- The physical ledger has 2,241 accepted owners; the conditioning partition is 2,202 direct-Newton plus 39 fallback rows. The locked scalar-clock replay has 747 owners per geometry and, at each of `d/a=29/5`, `6`, and `31/5`, exactly 3 period-two matches plus 744 disagreements.
- The exact mismatch is `2-sqrt(3)`, the minimax half-gap is `(2-sqrt(3))/2`, and the frozen relative mismatch is `(2-sqrt(3))/4`. The artifacts, summary values, and manuscript use the same exact quantities.

## External citation tuples for `P25-E1-015`

The following short quotations are **audit-note candidates only**. Each is at most 25 whitespace-split words. They were not inserted into `stage2_5_evidence_rows.json`; therefore both persisted rows remain `anchorless`, without source bytes, hashes, or spans.

| `ref_slug` | Specific official/author locator used | Short excerpt candidate | Words | Semantic allocation |
|---|---|---|---:|---|
| `GaspardRice1989Exact` | [AIP version of record via DOI](https://doi.org/10.1063/1.456019), abstract and multiple-scattering construction; [Pierre Gaspard's author publication list](https://gaspard.pierre.web.ulb.be/articles.html), 1989 entries; accessible abstract text indexed by the paper's [ULB/OpenAIRE record](https://explore.openaire.eu/search/publication?pid=10.1063%2F1.456019) | “The scattering resonances are located in the complex wave number plane as the zeros of the determinant of the matrix M” | 21 | Supports the exact three-hard-disk `S`-matrix/multiple-scattering determinant and resonance-zero statement. The excerpt candidate is from the accessible indexed abstract, not asserted as a byte span of the access-controlled VOR. |
| `Wirzba1999` | [Author-submitted arXiv full text](https://arxiv.org/abs/chao-dyn/9712015), abstract and §§2–6; in particular the angular-momentum basis, multiscattering kernel/determinant, cumulant organization, and noncommuting-limit discussion | “The multiscattering determinant can be organized in terms of the cumulant expansion” | 12 | Supports the separation/translation-kernel representation and the distinction between the exact multiscattering determinant and its curvature-expanded semiclassical reduction. |

Compound-claim adjudication: `GaspardRice1989Exact` supports the exact `S`-matrix, multiple-scattering matrix, and determinant-zero resonance characterization; `Wirzba1999` supports the infinite angular-momentum-channel/operator formulation, separation/translation kernels, determinant/cumulant structure, and the warning that exact and semiclassical limits are distinct. Neither source is treated as supporting the manuscript's new clock-nontransfer theorem. The prior Phase-A/B audit already records publisher-level bibliographic and citation-context checks. No contradiction or strength inflation was found.

## Overstatement and unverifiability screen

No selected claim was found to exaggerate the finite 2,241-owner replay into a complete trapped-flow census, replace a nonconstant roof by a scalar clock, identify the symbolic determinant with the physical flow determinant, identify the half-density factor with an exact scattering determinant, or claim an arithmetic/spectral construction that is absent. There are no Phase-E overstatement or unverifiability IDs to issue.

The known `BowenLanford1970` author-suffix mismatch does not alter this selected-claim verdict: its citation block is not among the 48 selected registry IDs. It remains a blocking bibliography-integrity defect outside this Phase-E semantic denominator.

## Remaining blockers outside Phase E

- `IL-SERIOUS-1` remains open: `BowenLanford1970` omits Lanford's generational suffix `III`. The exact bibliography patch still requires separate authorization and reference/context revalidation.
- `IL-SERIOUS-2` remains open: the paper reports project-owned computational results but lacks the scholar-owned `experiment_intake_declaration`, experiment provenance, and claim alignment required by Phase C4/D7.

The Phase-E PASS closes neither defect and does not authorize Stage 3.
