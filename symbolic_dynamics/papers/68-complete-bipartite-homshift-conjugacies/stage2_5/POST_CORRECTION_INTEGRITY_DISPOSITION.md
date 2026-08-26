# P68 post-correction integrity disposition

Audit date: 2026-08-26 UTC  
Protocol: ARS-Codex 0.1.27 Stage 2.5 integrity and priority review  
Disposition: **PASS_WITH_NOTES** for the internal integrity gate  
External posture: **HOLD**; no external release, upload, contact, submission, or
priority claim is authorized.

This document supersedes the pre-correction dispositions for current package
status. It does not erase the historical audit, correction receipt, or review
tracks.

## 1. Exact bindings, declarations, and C4 boundary

| Item | Current binding/result |
|---|---|
| Canonical PDF | `main.pdf`, 7 pages, 348079 bytes, SHA-256 `9527da716429ba4644271086dee8eebdd5a1c201a73cb2a0a39046cc957de61a` |
| Registry draft | `stage2_5/draft_for_claim_registry_round1.md`, SHA-256 `bb07f6f44433f69e76697dba6aa1b096e695905d9a1485a199e38396b3478806` |
| Claim registry | `stage2_5/claim_registry_round1.json`, SHA-256 `8b55f2d8ee474a114600f6fd19e5d439d3766ccea04b30e0b2cd28cef5b43e8e` |
| Coverage sidecar | `stage2_5/claim_registry_coverage_round1.json`, SHA-256 `5031794e104f343e2a864d0f0968e4156a7f6b8b29b5a129ad81608af6e32df2` |
| Active passport/declaration | `docs/papers67_71_sequence/stage2_5/MATERIAL_PASSPORT.yaml`, SHA-256 `097d6d3cc38d0dc8a97889ba40966bd82d422c8a4c4bc8ae0851015b85ea6f99`; bounded Stage-2.5 status `VERIFIED` |

The active passport records `no_experiments_declared`, an empty experiment
provenance list, and an empty experiment-alignment list for this theoretical
batch. This report points to that active record and does not create, duplicate,
or infer an author declaration.

The mandatory C4 boundary is reproduced verbatim:

> This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

P68 contains deterministic finite proof-regression controls, not an empirical
experiment. The controls are neither proof premises nor evidence of scientific
effect size.

Declaration status is intentionally non-inferential:

| Item | Status |
|---|---|
| Author identities and contribution roles | UNRESOLVED; manuscript remains anonymous |
| Funding statement | UNRESOLVED; no author-supplied statement is in scope |
| Independent conflict-of-interest verification | UNRESOLVED |
| AI-assistance disclosure | UNRESOLVED |
| Phase D2 author-overlap search | `NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE` |

## 2. Consolidated current source ledger: 4/4 records

Every current BibTeX record was searched independently. All field comparisons
below are against a DOI/publisher, arXiv, or author-hosted primary record; the
content anchor was also opened. Current result: **4 VERIFIED, 0 MISMATCH, 0
NOT_FOUND**.
`NOT_FOUND` is reserved for three materially different unsuccessful searches;
all four records reached exact primary evidence, so that fallback was not used.

| Key | Queries | Direct primary URL and content anchor | Current field result |
|---|---|---|---|
| `ChandgotiaMarcus2018` | `"10.2140/pjm.2018.294.41"`; `"Mixing Properties for Hom-Shifts" Chandgotia Marcus` | [publisher/DOI](https://doi.org/10.2140/pjm.2018.294.41); [publisher PDF](https://msp.org/pjm/2018/294-1/pjm-v294-n1-p03-p.pdf), abstract/opening scope | authors, title, journal, volume 294(1), pages 41--69, year 2018, DOI: VERIFIED |
| `Chandgotia2019Lectures` | `"Hom-Shifts, Lecture 4" Nishant Chandgotia`; `"Lecture 4: An introduction to hom-shifts" Chandgotia`; `site:nishantchandgotia.github.io coursekrakow l4.pdf` | [author PDF](https://nishantchandgotia.github.io/Teaching/2019_Jagiellonian/coursekrakow/l4.pdf), title page and complete-bipartite slides | author, exact corrected title, year/course, URL: VERIFIED |
| `ChandgotiaThorat2026` | `"2605.02226"`; `"Finitely Dependent Processes on Subshifts" Chandgotia Thorat` | [arXiv record](https://arxiv.org/abs/2605.02226); [full text](https://arxiv.org/html/2605.02226v2), abstract/introduction theorem scope | authors, title, year, identifier, class: VERIFIED |
| `BealBlockGorman2025` | `"2509.24754"`; `"One-Sided Hom Shifts" Béal Block Gorman` | [arXiv record](https://arxiv.org/abs/2509.24754); [full text](https://arxiv.org/html/2509.24754v1), abstract/conjugacy method | authors, title, year, identifier, class: VERIFIED |

Ghost/dangling replay: 4 BibTeX keys, the same 4 distinct cited keys, 10
citation occurrences, 0 undefined/ghost keys, and 0 uncited entries.

## 3. Consolidated current citation-context ledger: 10/10

| Current source location | Key | Context claim and inspected source anchor | Verdict |
|---|---|---|---|
| `sections/1_introduction.tex:3-6` | `ChandgotiaMarcus2018` | graph geometry affects hom-shift mixing; [publisher PDF abstract/opening](https://msp.org/pjm/2018/294-1/pjm-v294-n1-p03-p.pdf) | VERIFIED |
| `sections/1_introduction.tex:9-11` | `Chandgotia2019Lectures` | checkerboard phase/MME background; [complete-bipartite lecture slides](https://nishantchandgotia.github.io/Teaching/2019_Jagiellonian/coursekrakow/l4.pdf) | VERIFIED |
| `sections/1_introduction.tex:27-29` | `ChandgotiaThorat2026` | cited obstruction assumes no four-cycles; [arXiv theorem scope](https://arxiv.org/html/2605.02226v2) | VERIFIED |
| `sections/1_introduction.tex:47-50` | `BealBlockGorman2025` | one-sided conjugacy and amalgamation methods; [arXiv abstract/method](https://arxiv.org/html/2509.24754v1) | VERIFIED |
| `sections/3_conjugacy.tex:72-74` | `BealBlockGorman2025` | one-sided category is organized by amalgamation; [arXiv full text](https://arxiv.org/html/2509.24754v1) | VERIFIED |
| `sections/4_finite_dependence.tex:49-53` | `ChandgotiaThorat2026` | four-cycle-free finite-dependence obstruction; [arXiv theorem](https://arxiv.org/html/2605.02226v2) | VERIFIED |
| `sections/7_scope.tex:3-6` | `Chandgotia2019Lectures` | phase/MME product picture is prior background; [lecture slides](https://nishantchandgotia.github.io/Teaching/2019_Jagiellonian/coursekrakow/l4.pdf) | VERIFIED |
| `sections/7_scope.tex:6-7` | `ChandgotiaMarcus2018` | general mixing questions are prior work; [publisher PDF](https://msp.org/pjm/2018/294-1/pjm-v294-n1-p03-p.pdf) | VERIFIED |
| `sections/7_scope.tex:7-9` | `ChandgotiaThorat2026` | ownership and hypothesis of four-cycle-free obstruction; [arXiv theorem](https://arxiv.org/html/2605.02226v2) | VERIFIED |
| `sections/7_scope.tex:9-12` | `BealBlockGorman2025` | one-sided/tree amalgamation versus the manuscript's two-sided dimer code; [arXiv full text](https://arxiv.org/html/2509.24754v1) | VERIFIED |

## 4. Phase C internal consistency and control provenance

The finite-shape count, dimer inverse, subgroup fixed-point formula, pressure
specializations, theorem statements, proof-engine table, and examples were
cross-read against their proofs and deterministic script. The current script
`code/verify_complete_bipartite.py` has SHA-256
`42c3e23e2cfd27618ccca28155be4f854010a05850fc7c1af2b1b8fe96aac8bd`.
Its live output is byte-identical to `code/verify_complete_bipartite.out`,
whose SHA-256 is
`918c56ef57b9c09ce27872e58a3e76667766351378e40b5d450d9cbced2a0bbf`,
and ends `ALL CHECKS PASS`. These are proof-regression controls only.

## 5. Phase D originality screen

The current denominator is 58 nonempty prose/theorem/proof paragraph-like
blocks. The current sample is 18/58 = 31.03%, with the abstract and every
major section represented. The 18 quoted 8--12-word queries are the following;
each returned `NO_EXACT_RELEVANT_MATCH` in the bounded public-web search:

Section coverage is: abstract 1; introduction 4; phase/counts 3; conjugacy 2;
finite dependence 2; pressure 2; periodic/proof-engine discussion 2; scope 1;
conclusion 1. No major section has zero sampled blocks.

1. `"The code uses the configuration's intrinsic checkerboard phase to pair sites"`
2. `"Graph-homomorphism shifts form a concrete class of nearest-neighbour shifts of finite"`
3. `"Does a conjugacy remember the two part sizes separately, or only"`
4. `"A finitely dependent process makes sufficiently remote coordinates independent, whereas"`
5. `"One-sided hom-shift conjugacy uses a different coding category and is"`
6. `"The parity of the length of a lattice path from"`
7. `"Completeness of the bipartite target makes the resulting global configuration valid"`
8. `"Packing and unpacking are continuous and commute with translations"`
9. `"Therefore translating the input translates the anchored dimers and"`
10. `"using a fixed parity origin would not commute with odd translations"`
11. `"All coordinates are independent, so the law is 0-dependent"`
12. `"while the index-two even subaction admits an independent law"`
13. `"We include the uniqueness argument because it records the role of"`
14. `"knowing the target part at one site determines it at every site"`
15. `"An odd period would identify a site with a site in"`
16. `"The construction supplies the missing mechanism and also explains why"`
17. `"There are three limitations. First, completeness of the bipartite target"`
18. `"A translation-equivariant dimerization converts that freedom into the alphabet"`

This is a bounded overlap heuristic, not a plagiarism determination or an
originality certificate. Phase D2 is
`NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE`. Public search does not cover private
drafts, all subscription databases, referee files, or unindexed work; engines
also normalize accents, TeX, punctuation, and hyphenation.

## 6. Phase E claim registry, evidence rows, and replay

The registry contains 31 items: 20 `HIGH-IMPACT`, 3 `RANDOM`, and 8 not
selected. **semantic completeness=not_machine_detectable**. Machine trigger
coverage is complete (`candidate_unregistered_count=0`), but that cannot prove
semantic completeness. All 23 selected claims were audited.

The 20 selected no-reference claims have one explicit `anchorless` empty-state
row each. Their mathematical support is not an invented citation; it is the
following proof map:

| Claim IDs | Current proof anchor | Verdict |
|---|---|---|
| `P68-SEM-001` | `sections/2_phase_counts.tex:35-64` | VERIFIED |
| `P68-SEM-002` | `sections/3_conjugacy.tex:6-55` | VERIFIED |
| `P68-SEM-003` | `sections/4_finite_dependence.tex:9-47` | VERIFIED |
| `P68-SEM-004` | `sections/5_pressure.tex:11-76`; `sections/6_periodic_data.tex:8-24` | VERIFIED |
| `P68-SEM-005` | `sections/2_phase_counts.tex:16-33` | VERIFIED |
| `P68-SEM-006`, `P68-SEM-007` | `sections/2_phase_counts.tex:35-64` | VERIFIED |
| `P68-SEM-008` | `sections/2_phase_counts.tex:76-96` | VERIFIED |
| `P68-SEM-009`, `P68-SEM-010`, `P68-SEM-011`, `P68-SEM-012` | `sections/3_conjugacy.tex:6-55` | VERIFIED |
| `P68-SEM-013`, `P68-SEM-014`, `P68-SEM-015`, `P68-SEM-016` | `sections/4_finite_dependence.tex:9-47` | VERIFIED |
| `P68-SEM-017`, `P68-SEM-018`, `P68-SEM-019` | `sections/5_pressure.tex:11-75` | VERIFIED |
| `P68-SEM-021` | `sections/6_periodic_data.tex:8-24` | VERIFIED |

The 3 selected cited tuples use exact, session-held primary-source excerpts:

| Claim/ref tuple | Direct source and exact content anchor | Verdict |
|---|---|---|
| `P68-R1-CAND-003` / `ChandgotiaThorat2026` | [arXiv abstract](https://arxiv.org/html/2605.02226v2): “The space of graph homomorphisms from $\\mathbb{Z}^{d}$ to a fixed undirected simple graph without four cycles.” The local fact that nondegenerate `K_(m,n)` has a four-cycle is checked directly. | VERIFIED |
| `P68-R1-CAND-009` / `ChandgotiaMarcus2018` | [publisher PDF, introduction](https://msp.org/pjm/2018/294-1/pjm-v294-n1-p03-p.pdf): “Such questions arise while studying mixing properties of hom-shifts” | VERIFIED |
| `P68-R1-CAND-011` / `BealBlockGorman2025` | [arXiv abstract](https://arxiv.org/html/2509.24754v1): “a tree-shift of finite type, is conjugate to a one-sided Hom shift if and only if its total amalgamation satisfies some regularity conditions” | VERIFIED |

Authoritative Phase-E artifacts:

| Artifact | Result |
|---|---|
| `stage2_5/evidence_rows_round1.json` | 23 `evidence-row/1.0` rows; SHA-256 `f32038047107167d1fe61fd625fc054c21ebb7e7e64bccca55c62c3ba1b8536e` |
| `stage2_5/evidence_source_map_round1.json` | three session-held cited-source excerpts; SHA-256 `110827277b363deccdddd3afbbc372d237da883dcf776bd8181b3b1f0f2d073d` |
| Row states | 3 positive `agent_extracted` rows; 20 explicit `anchorless` empty-state rows; 0 manuscript self-source rows |
| `stage2_5/evidence_tuple_join_post_correction.json` | full expected/actual tuple sequence, 23/23 rows, 0 mismatches, official runtime replay PASS; SHA-256 `d7a5e6755ebfbed042545d3bec416ccba86f26ac2729be6fc704b9878f83a64a` |

`evidence_rows.py validate --source-map` returns `PASS: 23 evidence row(s)`.
The `post_correction` row/map files are byte-identical auxiliary aliases; the
`round1` names above are canonical for strict validation.

### E6 claim-strength drift sidecar

`stage2_5/claim_strength_drift_findings_post_correction.json` validates against
`claim-strength-drift-findings/1.0`; SHA-256
`33f9821758978d92cafa840e310bd592df2443d8e8ce12a6671d355a7c7e8f88`.
Its status is `skipped_no_revision_evidence`, its exact final-draft hash is the
registry-draft hash above, its revision-evidence-bundle hash is `null`, and its
findings list is empty as required by that branch of the schema. This is an
explicit protocol skip because no ARS Revision-Evidence Bundle was supplied;
it is not a claim that semantic drift was machine-excluded.

## 7. Search-bounded priority and owner subtraction

Each residual core advance was queried under at least three alternate terms:

- classification/dimer code: `"complete bipartite hom-shift" conjugacy product mn`,
  `"Hom(Z^d,K_{m,n})" conjugacy`, `"graph homomorphism shift" "dimer code" bipartite`,
  `"complete bipartite graph" hom-shift conjugacy classification`;
- subgroup finite dependence: `"complete bipartite hom-shift" "finitely dependent"`,
  `"checkerboard phase" "finitely dependent" process subgroup`,
  `"Hom(Z^d,K_{m,n})" "finite dependence"`;
- pressure/periodic data: `"complete bipartite hom-shift" pressure equilibrium one-site potential`,
  `"Hom(Z^d,K_{m,n})" "topological pressure"`,
  `"complete bipartite graph hom-shift" "periodic point"`.

The nearest public owners are Chandgotia's complete-bipartite phase/MME
lectures, Chandgotia--Marcus on mixing, Chandgotia--Thorat on the distinct
four-cycle-free obstruction, and Béal--Block Gorman on one-sided/tree
conjugacy. No exact indexed statement of the residual combined theorem package
was found through 2026-08-26. This is search-bounded only, not a global novelty
or priority certificate. Collision risk is **MEDIUM**; the specialist
exact-neighbour gate remains pending.

## 8. Seven-mode final disposition

Only the protocol's allowed final status vocabulary is used.

| Failure mode | Evidence | Status |
|---|---|---|
| 1. Implementation bug producing a claim | exact proofs, rerun, and frozen-output `cmp=0`; code is non-premise regression support | CLEAR |
| 2. Citation hallucination or miscitation | 4/4 current records, 10/10 contexts, 3 cited-tuple source replays | CLEAR |
| 3. Hallucinated experimental result | active passport plus manuscript/control disclosure; no experiment claim | CLEAR |
| 4. Shortcut or model-metric reliance | combinatorial, topological, and entropy proofs contain no learned metric | CLEAR |
| 5. Bug reframed as insight | infinite-system proofs are independent of finite controls | CLEAR |
| 6. Fabricated methodology/provenance | theoretical proof engines, manuscript anchors, active passport, control source, frozen output, and exact hashes are traced; human declarations are handled separately below | CLEAR |
| 7. Frame lock / ignored nearest neighbour | alternate terms and one-/two-sided and graph-hypothesis variants searched; owners subtracted | CLEAR |

## 9. Objective remaining gates

1. Obtain actual author identities/roles and author-supplied funding, COI, and
   AI-assistance disclosures; do not infer them.
2. Complete the specialist exact-neighbour/source gate under current hom-shift,
   checkerboard-code, finite-dependence, and pressure terminology.
3. Keep collision language search-bounded and keep external release on `HOLD`
   until explicit authorization and the specialist gate are both resolved.

No current manuscript, bibliography, theorem, proof, or PDF correction is
required by this strict closure. The unresolved items are release/declaration
and specialist-gate items, not hidden Phase-E tuple defects.  After the five
paper dispositions were sealed, the package-level `SHA256SUMS` was regenerated
and replay-checked as the current comprehensive manifest.
