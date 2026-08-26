# P71 post-correction integrity disposition

Audit date: 2026-08-26 UTC  
Protocol: ARS-Codex 0.1.27 Stage 2.5 integrity and priority review  
Disposition: **PASS_WITH_NOTES** for the internal integrity gate  
External posture: **HOLD**; no external release, upload, contact, submission, or
priority claim is authorized.

This document supersedes the pre-correction dispositions for current package
status. It preserves the historical audit, correction receipt, and separate
review tracks.

## 1. Exact bindings, declarations, and C4 boundary

| Item | Current binding/result |
|---|---|
| Canonical PDF | `main.pdf`, 9 pages, 409426 bytes, SHA-256 `971b33083dc14ceb99831f94786167c1186bf9b8365557472fb2a9f493174a9e` |
| Registry draft | `stage2_5/draft_for_claim_registry_round1.md`, SHA-256 `d085ef0f563ff9da62b83d522354128f48764156d4d84d32674223e0093a8e68` |
| Claim registry | `stage2_5/claim_registry_round1.json`, SHA-256 `360becd24c4fbbb6fee3da7a8ac098aa09cd4cbc13849da742fc201c6bb5f3e9` |
| Coverage sidecar | `stage2_5/claim_registry_coverage_round1.json`, SHA-256 `fa69c1669596d957c31d49d145a13de4f044b8837ea7f8ec2d7e82891015f101` |
| Active passport/declaration | `docs/papers67_71_sequence/stage2_5/MATERIAL_PASSPORT.yaml`, SHA-256 `097d6d3cc38d0dc8a97889ba40966bd82d422c8a4c4bc8ae0851015b85ea6f99`; bounded Stage-2.5 status `VERIFIED` |

The active passport records `no_experiments_declared`, an empty experiment
provenance list, and an empty experiment-alignment list for this theoretical
batch. This report points to that active record and does not create, duplicate,
or infer an author declaration.

The mandatory C4 boundary is reproduced verbatim:

> This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

P71 contains deterministic finite proof-regression controls, not an empirical
experiment. Numerical differentiation and finite-word enumeration are neither
proof premises nor measurements of a scientific effect.

Declaration status is intentionally non-inferential:

| Item | Status |
|---|---|
| Author identities and contribution roles | UNRESOLVED; manuscript remains anonymous |
| Funding statement | UNRESOLVED; no author-supplied statement is in scope |
| Independent conflict-of-interest verification | UNRESOLVED |
| AI-assistance disclosure | UNRESOLVED |
| Phase D2 author-overlap search | `NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE` |

## 2. Consolidated current source ledger: 9/9 records

Every current BibTeX record was independently searched and field-checked
against DOI/publisher, arXiv, or official institutional primary evidence. A
relevant abstract, theorem passage, or project description was opened where a
record supports a factual context. Current result: **9 VERIFIED, 0 MISMATCH, 0
NOT_FOUND**.
`NOT_FOUND` is reserved for three materially different unsuccessful searches;
all nine records reached exact primary evidence, so that fallback was not used.

| Key | Queries | Direct primary URL and content anchor | Current field result |
|---|---|---|---|
| `LameiMehdipour2025` | `"2502.11272"`; `"Zip Shift Space" Lamei Mehdipour` | [arXiv record](https://arxiv.org/abs/2502.11272); [full text](https://arxiv.org/html/2502.11272v1), abstract/definition/local-homeomorphism/sliding-block sections | authors, title, year, identifier, class: VERIFIED |
| `LameiMehdipourVargas2025` | `"2510.12980"`; `"S-Expansiveness and Zip Shift Maps in Symbolic Dynamics"` | [arXiv record](https://arxiv.org/abs/2510.12980), abstract on S-expansiveness, shadowing, and factor theorem | authors as listed, title, year, identifier, class: VERIFIED |
| `MehdipourJangjooye2025` | `"2505.24647"`; `"Square Entropy and Uniform n-to-1 Bernoulli Transformations"` | [arXiv record](https://arxiv.org/abs/2505.24647); [full text](https://arxiv.org/html/2505.24647v1), abstract/principal results | authors, title, year, identifier, class: VERIFIED |
| `MartinsMattosVarao2026` | `"10.1007/s10884-025-10479-7"`; `"Folding and Metric Entropies for Extended Shifts"`; `"2407.01828"` | [publisher DOI](https://doi.org/10.1007/s10884-025-10479-7); [arXiv record](https://arxiv.org/abs/2407.01828); [full text](https://arxiv.org/html/2407.01828v2), definition and Theorems A--B | authors, published title, journal, year, DOI, arXiv id: VERIFIED |
| `Bowen1973` | `"10.1090/S0002-9947-1973-0338317-X"`; `"Topological Entropy for Noncompact Sets" Bowen` | [AMS DOI record](https://doi.org/10.1090/S0002-9947-1973-0338317-X), title/scope/definition | author, title, journal, volume 184, pages 125--136, year, DOI: VERIFIED |
| `BarreiraSaussolSchmeling2002` | `"10.1016/S0022-314X(02)00003-3"`; `"Distribution of Frequencies of Digits via Multifractal Analysis"` | [publisher page](https://www.sciencedirect.com/science/article/pii/S0022314X02000033); [DOI](https://doi.org/10.1016/S0022-314X(02)00003-3), abstract | authors, title, journal, volume 97(2), pages 410--438, year, DOI: VERIFIED |
| `MehdipourSalarinoghabiGibrim2026` | `"10.1063/5.0300898"`; `"Zip Cellular Automata" Mehdipour Salarinoghabi Gibrim`; `site:pubs.aip.org "Zip cellular automata"` | [AIP publisher page](https://pubs.aip.org/aip/adv/article/16/1/015201/3376058/Zip-cellular-automata); [DOI](https://doi.org/10.1063/5.0300898), abstract | authors, title, journal, volume 16(1), corrected article number 015201, year, DOI: VERIFIED |
| `MehdipourUFVProject2024` | `"Formalismo Termodinâmico para Mapas Zip Shift"`; `site:nit.ufv.br/pesquisador/pouya-mehdipour "Formalismo Termodinâmico"`; `Pouya Mehdipour UFV zip shift projeto 2024` | [official UFV profile](https://nit.ufv.br/pesquisador/pouya-mehdipour/), 2024--present project entry and Portuguese objective | researcher, exact title, institutional page, start/status note, URL: VERIFIED as project metadata; page is not theorem text |
| `MehdipourLamei2026` | `"10.21494/ISTE.OP.2026.1442"`; `"Zip Shift Encoding of M-to-1 Local Homeomorphisms"` | [publisher page](https://www.openscience.fr/Zip-Shift-encoding-of-M-TO-1-local-homeomorphisms); [publisher PDF](https://www.openscience.fr/IMG/pdf/iste_apam26v17n2_2.pdf), abstract/introduction | authors, title, journal, volume 17(2), pages 20--29, year, DOI: VERIFIED |

Ghost/dangling replay: 9 BibTeX keys, the same 9 distinct cited keys, 19
citation occurrences, 0 undefined/ghost keys, and 0 uncited entries.

## 3. Consolidated current citation-context ledger: 19/19

| Current source location | Key | Context claim and inspected source anchor | Verdict |
|---|---|---|---|
| `sections/1_introduction.tex:6-9` | `LameiMehdipour2025` | formal zip space, sliding blocks, local homeomorphism, periodic setting; [full text](https://arxiv.org/html/2502.11272v1) | VERIFIED |
| `sections/1_introduction.tex:8-11` | `MartinsMattosVarao2026` | same system as extended shift; Bernoulli metric/folding entropies; [definition and Theorems A--B](https://arxiv.org/html/2407.01828v2) | VERIFIED |
| `sections/1_introduction.tex:14-16` | `MehdipourJangjooye2025` | square entropy and uniform intrinsic ergodicity; [full text](https://arxiv.org/html/2505.24647v1) | VERIFIED |
| `sections/1_introduction.tex:50-54` | `MartinsMattosVarao2026` | metric/folding formulae are prior; manuscript substitutes equilibrium weights; [Theorems A--B](https://arxiv.org/html/2407.01828v2) | VERIFIED |
| `sections/1_introduction.tex:56-57` | `Bowen1973` | noncompact-set entropy supplies the level-set notion; [AMS record/scope](https://doi.org/10.1090/S0002-9947-1973-0338317-X) | VERIFIED |
| `sections/1_introduction.tex:57-59` | `BarreiraSaussolSchmeling2002` | digit-frequency multifractals are adjacent context; [publisher abstract](https://www.sciencedirect.com/science/article/pii/S0022314X02000033) | VERIFIED |
| `sections/2_model_extension.tex:12-15` | `LameiMehdipour2025` | displayed formula is a full one-block zip shift; [definition](https://arxiv.org/html/2502.11272v1) | VERIFIED |
| `sections/2_model_extension.tex:14-17` | `MartinsMattosVarao2026` | same formula defines the extended shift; [definition](https://arxiv.org/html/2407.01828v2) | VERIFIED |
| `sections/3_pressure.tex:69-71` | `MartinsMattosVarao2026` | corollary uses their entropy formulae; [Theorems A--B](https://arxiv.org/html/2407.01828v2) | VERIFIED |
| `sections/3_pressure.tex:82-89` | `MartinsMattosVarao2026` | metric and folding entropy ownership; [Theorems A--B](https://arxiv.org/html/2407.01828v2) | VERIFIED |
| `sections/5_multifractal.tex:3-12` | `Bowen1973` | Bowen entropy for possibly noncompact level sets; [AMS record/scope](https://doi.org/10.1090/S0002-9947-1973-0338317-X) | VERIFIED |
| `sections/6_examples.tex:35-38` | `MehdipourJangjooye2025` | uniform profile lies on their uniform theory boundary; [full text](https://arxiv.org/html/2505.24647v1) | VERIFIED |
| `sections/7_scope.tex:3-5` | `LameiMehdipour2025` | formal definitions/local homeomorphism/sliding blocks/periodic setting are prior; [full text](https://arxiv.org/html/2502.11272v1) | VERIFIED |
| `sections/7_scope.tex:5-7` | `MehdipourJangjooye2025` | uniform intrinsic ergodicity/square entropy are prior; [full text](https://arxiv.org/html/2505.24647v1) | VERIFIED |
| `sections/7_scope.tex:7-12` | `MartinsMattosVarao2026` | exact map and Theorems A--B are owner-subtracted; [full text](https://arxiv.org/html/2407.01828v2) | VERIFIED |
| `sections/7_scope.tex:14-16` | `MehdipourSalarinoghabiGibrim2026` | zip cellular automata are adjacent; [AIP abstract](https://pubs.aip.org/aip/adv/article/16/1/015201/3376058/Zip-cellular-automata) | VERIFIED |
| `sections/7_scope.tex:15-17` | `MehdipourLamei2026` | finite-to-one local-homeomorphism encoding is adjacent; [publisher PDF](https://www.openscience.fr/IMG/pdf/iste_apam26v17n2_2.pdf) | VERIFIED |
| `sections/7_scope.tex:16-22` | `LameiMehdipourVargas2025` | S-expansiveness, shadowing, and stated factor theorem are theirs; [arXiv abstract](https://arxiv.org/abs/2510.12980) | VERIFIED |
| `sections/7_scope.tex:24-32` | `MehdipourUFVProject2024` | named project's thermodynamic-formalism/phase-transition objective; page is expressly not treated as a theorem; [official UFV description](https://nit.ufv.br/pesquisador/pouya-mehdipour/) | VERIFIED |

## 4. Phase C internal consistency and control provenance

The degree indexing, pressure and derivative table values, periodic weighted
sums, zeta identity, profile-recovery examples, and binary spectrum checks were
cross-read against their proofs and deterministic script. The current script
`code/verify_degree_pressure.py` has SHA-256
`6de6496c78ca610d955f7b6a4aa08d31f162b0c7ad3bfcbaf80bcb787119aab2`.
Its live output is byte-identical to `code/verify_degree_pressure.out`, whose
SHA-256 is
`4ade498585b0750acea4b487dec11b7c19b2e322f8a5ef1d4262d6c4f39f2aba`,
and ends `ALL CHECKS PASS`. These are proof-regression controls only.

## 5. Phase D originality screen

The current, post-correction denominator is 70 nonempty
prose/theorem/proof paragraph-like blocks. The current sample is 22/70 =
31.43%, with the abstract and every major section represented. The following
quoted 8--12-word queries were searched; each returned
`NO_EXACT_RELEVANT_MATCH` in the bounded public-web screen:

Section coverage is: abstract 1; introduction 3; model/natural extension 4;
pressure 2; periodic/rigidity 4; multifractal 3; examples 1; scope/control 3;
conclusion 1. No major section has zero sampled blocks.

1. `"The full pressure curve is also a complete invariant inside this family"`
2. `"A zip shift records future symbols in one alphabet and past symbols"`
3. `"A nonuniform fibre profile changes the question: the orbit sees a sequence"`
4. `"This paper gives one closed theorem package for that observable"`
5. `"The natural extension of a full zip shift is the ordinary full"`
6. `"These coordinate formulae are continuous and inverse to one another"`
7. `"Invariance makes these finite-dimensional distributions consistent, so they define the lift"`
8. `"This ordinary fact is not the invariant used below"`
9. `"For any shift-invariant measure, its entropy rate is bounded by"`
10. `"Thus the curve contains both alphabet sizes, while its curvature records"`
11. `"The same exponential sum appears without a variational argument when periodic"`
12. `"Every fixed point arises uniquely in this way. Its local degrees"`
13. `"Conjugacy preserves local degree pointwise because it bijects the preimage sets"`
14. `"This recovers the whole profile from the curve and proves"`
15. `"At later times its surviving old-past coordinates remain inside that block"`
16. `"Countable stability of Bowen entropy gives the upper bound"`
17. `"Equality holds by distributing mass uniformly within each fibre"`
18. `"The ordinary topological entropy cannot distinguish fibre profiles with the same"`
19. `"The formal zip-shift definitions, local homeomorphism results, sliding block codes"`
20. `"public description says that the project aims to study"`
21. `"These are regression checks only; all formulae are proved symbolically"`
22. `"Its logarithm generates a pressure curve that simultaneously determines equilibrium measures"`

Query 20 is the post-correction scope-paragraph sample and produced an empty
exact-phrase result. This is a bounded overlap heuristic, not a plagiarism
determination or an originality certificate. Phase D2 is
`NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE`. Public search does not cover private
drafts, all subscription databases, referee files, or unindexed work; engines
also normalize accents, TeX, punctuation, and hyphenation.

## 6. Phase E claim registry, evidence rows, and replay

The registry contains 42 items: 26 `HIGH-IMPACT`, 3 `RANDOM`, and 13 not
selected. **semantic completeness=not_machine_detectable**. Machine trigger
coverage is complete (`candidate_unregistered_count=0`), but that cannot prove
semantic completeness. All 29 selected claims were audited.

The 23 selected no-reference claims have one explicit `anchorless` empty-state
row each. Their mathematical support is the following local proof map, not an
invented citation:

| Claim IDs | Current proof anchor | Verdict |
|---|---|---|
| `P71-SEM-001`, `P71-SEM-002` | `sections/3_pressure.tex:11-57` | VERIFIED |
| `P71-SEM-003` | `sections/5_multifractal.tex:23-168` | VERIFIED |
| `P71-SEM-004` | `sections/4_periodic_rigidity.tex:61-112` | VERIFIED |
| `P71-SEM-005`, `P71-SEM-006` | `sections/4_periodic_rigidity.tex:6-32` | VERIFIED |
| `P71-SEM-008` | `sections/2_model_extension.tex:23-38` | VERIFIED |
| `P71-SEM-009` | `sections/2_model_extension.tex:53-95` | VERIFIED |
| `P71-SEM-010`, `P71-SEM-011`, `P71-SEM-012` | `sections/3_pressure.tex:11-57` | VERIFIED |
| `P71-SEM-013` | `sections/3_pressure.tex:69-89`, including the explicitly cited Theorems A--B input | VERIFIED |
| `P71-SEM-014` | `sections/4_periodic_rigidity.tex:6-32` | VERIFIED |
| `P71-SEM-015` | `sections/4_periodic_rigidity.tex:34-55` | VERIFIED |
| `P71-SEM-016`, `P71-SEM-017`, `P71-SEM-018`, `P71-SEM-019`, `P71-SEM-020`, `P71-SEM-021` | `sections/4_periodic_rigidity.tex:61-112` | VERIFIED |
| `P71-SEM-022`, `P71-SEM-023` | `sections/5_multifractal.tex:23-168` | VERIFIED |
| `P71-SEM-026` | `sections/8_conclusion.tex:3-14`, synthesis checked against the cited proof sections above | VERIFIED |

The selected cited claims expand to eight exact claim/ref tuples. Each uses a
true session-held primary-source excerpt:

| Claim/ref tuple | Direct source and exact content anchor | Verdict |
|---|---|---|
| `P71-R1-CAND-003` / `MehdipourJangjooye2025` | [arXiv abstract](https://arxiv.org/html/2505.24647v1): “we define the so-called square entropy and prove that n-to-1 full zip shift maps are intrinsically ergodic” | VERIFIED |
| `P71-SEM-007` / `MartinsMattosVarao2026` | [arXiv introduction](https://arxiv.org/html/2407.01828v2): “our two main results, Theorems A and B, are the calculation of the metric and folding entropy, respectively” The natural-extension clause is proved locally. | VERIFIED |
| `P71-R1-CAND-005` / `BarreiraSaussolSchmeling2002` | [publisher article](https://www.sciencedirect.com/science/article/pii/S0022314X02000033): “Distribution of Frequencies of Digits via Multifractal Analysis” | VERIFIED |
| `P71-R1-CAND-005` / `Bowen1973` | [AMS record](https://doi.org/10.1090/S0002-9947-1973-0338317-X): “Topological Entropy for Noncompact Sets” | VERIFIED |
| `P71-R1-CAND-008` / `LameiMehdipour2025` | [arXiv abstract](https://arxiv.org/html/2502.11272v1): “We introduce a new extension in symbolic dynamics on two sets of alphabets, called the zip shift space.” | VERIFIED |
| `P71-R1-CAND-008` / `MartinsMattosVarao2026` | [arXiv Section 2](https://arxiv.org/html/2407.01828v2): “In this section, we present the formal definition of the extended shift” | VERIFIED |
| `P71-R1-CAND-017` / `LameiMehdipourVargas2025` | [arXiv abstract](https://arxiv.org/abs/2510.12980): “are S-expansive and possess the shadowing property. Furthermore, we prove that any S-expansive local homeomorphism is a factor of a zip shift map.” | VERIFIED |
| `P71-R1-CAND-018` / `MehdipourUFVProject2024` | [official UFV description](https://nit.ufv.br/pesquisador/pouya-mehdipour/): “O objetivo principal é mostrar que esses mapas representam sistemas com transições de fase.” This supports a project objective only, not a theorem. | VERIFIED |

Authoritative Phase-E artifacts:

| Artifact | Result |
|---|---|
| `stage2_5/evidence_rows_round1.json` | 31 `evidence-row/1.0` rows for 29 selected claims; SHA-256 `df1fd0702b3e631fd4afe5125ee26f1692edff1a1eb6db5c246f1639d1b34462` |
| `stage2_5/evidence_source_map_round1.json` | seven cited sources, with two distinct Martins excerpts selected by claim; SHA-256 `c6051013848f792869a5a2985450133c807bf9d74844c89d615ea8336275c93c` |
| Row states | 8 positive `agent_extracted` rows; 23 explicit `anchorless` empty-state rows; 0 manuscript self-source rows |
| `stage2_5/evidence_tuple_join_post_correction.json` | full expected/actual tuple sequence, 31/31 rows, 0 mismatches, official runtime replay PASS; SHA-256 `ff832ad49d72e4f27cda0ca1a5242054b3091b8484331764ff61a8e47f8b0caf` |

`evidence_rows.py validate --source-map` returns `PASS: 31 evidence row(s)`.
The `post_correction` row/map files are byte-identical auxiliary aliases; the
`round1` names above are canonical for strict validation.

### E6 claim-strength drift sidecar

`stage2_5/claim_strength_drift_findings_post_correction.json` validates against
`claim-strength-drift-findings/1.0`; SHA-256
`55070272790d783bdbd3e653bcdbd5c9d89a096bd629a3712b9a408943b97683`.
Its status is `skipped_no_revision_evidence`, its exact final-draft hash is the
registry-draft hash above, its revision-evidence-bundle hash is `null`, and its
findings list is empty as required by that branch of the schema. This is an
explicit protocol skip because no ARS Revision-Evidence Bundle was supplied;
it is not a claim that semantic drift was machine-excluded.

## 7. Search-bounded priority and owner subtraction

Each residual core advance was queried under at least three alternate terms:

- pressure/equilibrium/curvature: `"zip shift" "topological pressure" local degree`,
  `"extended shift" thermodynamic formalism folding entropy`,
  `"preimage-count potential" pressure symbolic dynamics`,
  `"zip shift" equilibrium state pressure`;
- profile/periodic/conjugacy: `"zip shift" conjugacy "fibre profile"`,
  `"zip shift" "degree-weighted" periodic zeta`,
  `"finite-to-one shift" "local degree" conjugacy invariant`,
  `"zip shift" periodic point degree profile`;
- spectrum: `"zip shift" multifractal spectrum local degree`,
  `"degree exponent" Bowen entropy preimage multiplicity`,
  `"Birkhoff spectrum" "log local degree" symbolic`,
  `"zip shift" "multifractal" entropy`.

Nearest owners are Lamei--Mehdipour for the formal system, Martins--Mattos--
Varão for metric/folding entropy of the same map, Mehdipour--Jangjooye Shaldehi
for uniform square entropy/intrinsic ergodicity, Bowen and Barreira--Saussol--
Schmeling for the general spectrum framework, and Lamei--Mehdipour--Vargas for
S-expansiveness/shadowing/factor results. The official UFV 2024--present
project has the exact-family thermodynamic-formalism and phase-transition
objective. Its public page exposes no theorem text, so no theorem-level
comparison is possible from that page.

No indexed source found through 2026-08-26 states the exact combined
pressure/equilibrium/weighted-periodic/profile-recovery/Bowen-spectrum package.
This is search-bounded only, not a global novelty or priority certificate.
Collision risk remains **HIGH for the pressure portion**; the specialist
exact-neighbour gate remains pending.

## 8. Seven-mode final disposition

Only the protocol's allowed final status vocabulary is used.

| Failure mode | Evidence | Status |
|---|---|---|
| 1. Implementation bug producing a claim | exact proofs, rerun, and frozen-output `cmp=0`; code is non-premise regression support | CLEAR |
| 2. Citation hallucination or miscitation | 9/9 current records, 19/19 contexts, 8 cited-tuple source replays | CLEAR |
| 3. Hallucinated experimental result | active passport plus manuscript/control disclosure; no experiment claim | CLEAR |
| 4. Shortcut or model-metric reliance | exact finite sums, entropy inequalities, and topological arguments use no learned metric | CLEAR |
| 5. Bug reframed as insight | general proofs are independent of finite enumerations and numerical differentiation | CLEAR |
| 6. Fabricated methodology/provenance | theoretical proof engines, manuscript anchors, active passport, control source, frozen output, and exact hashes are traced; human declarations are handled separately below | CLEAR |
| 7. Frame lock / ignored nearest neighbour | the same-family project and S-expansiveness paper were found, cited, and owner-subtracted; unavailable project theorem text remains a separate collision-risk/specialist gate | CLEAR |

## 9. Objective remaining gates

1. Obtain actual author identities/roles and author-supplied funding, COI, and
   AI-assistance disclosures; do not infer them.
2. Obtain a specialist exact-neighbour comparison focused on the pressure,
   equilibrium, spectrum, and pressure-profile recovery contracts, including
   current work associated with the official UFV project.
3. Keep the public project classified as an objective, not theorem evidence;
   do not infer either collision or non-collision from the public page's silence.
4. Keep collision language search-bounded and external release on `HOLD` until
   explicit authorization and the specialist gate are both resolved.

No current manuscript, bibliography, theorem, proof, or PDF correction is
required by this strict closure. The unresolved items are release/declaration
and specialist exact-neighbour items; the Phase-E tuple carrier itself is now
complete and replayable.  After the five paper dispositions were sealed, the
package-level `SHA256SUMS` was regenerated and replay-checked as the current
comprehensive manifest.
