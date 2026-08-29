# Stage 2.5 independent integrity audit — Paper 25

Audit date: 2026-08-29 UTC  
Protocol: ARS-Codex academic-research-suite, Stage 2.5 initial integrity gate  
Audited manuscript SHA-256: `283695c485a2a48abfab1ef0fe3d479f597f68f3082e20f4a5a1894ca37baefb`  
Audited bibliography SHA-256: `acec840393408f146f5e6eed9723cd4e12275108a6059fe0fdb0c2bc508e7248`

## Decision

**FAIL-CLOSED — BLOCK.** Phases A–D retain their stated results. `BowenLanford1970` omits the author's generational suffix `III`; under the no-gray-zone rule this is a SERIOUS author-field `MISMATCH` (**`IL-SERIOUS-1`**). The paper also reports own computational results without `experiment_intake_declaration`, `experiment_provenance[]`, or positive pre-#260 legacy proof, so ARS Phase C4/D7 fails closed (**`IL-SERIOUS-2`**). The earlier invalid Phase-E sample remains superseded as a historical audit event, but the registry/evidence chain has since been stably rebuilt and independently checked: the controlling [Phase-E semantic audit](stage2_5_phase_e_semantic_audit.md) records a clean PASS for **48/48 selected distinct claims** and **49/49 required evidence tuples**. That Phase-E PASS removes the former rebuild requirement; it closes neither existing SERIOUS issue and does not change the overall Stage-2.5 verdict. No MINOR IDs.

| Surface | Coverage | Result |
|---|---:|---|
| Phase A: registered references | 8/8 (100%) | 7 VERIFIED; 0 NOT_FOUND; 1 MISMATCH |
| Phase B: citation contexts | 10/10 (100%) | 10 supported; 0 distorted; 0 unverifiable |
| Phase C: registered numerical/data surfaces | 7/7 (100%) | all internally consistent and replayed |
| Phase C4: scholar-owned experiment intake | 0/1 passport declaration | absent; D7 structural FAIL |
| Phase D: body-paragraph originality | 22/70 (31.4%) | no exact third-party prose match found |
| Phase E: Claim Registry and evidence selection | stable registry: 72 rows; 48 selected distinct claims; 49 required tuples | **PASS:** 48/48 claims VERIFIED; 49/49 tuples present; historical sample remains superseded |
| Ghost/unused citation check | 8/8 BibTeX keys cited | none |

The paragraph denominator is a reproducible prose-block count: numbered-section body text from `Introduction` through `Conclusion`, split on blank lines, retaining blocks with at least 12 alphabetic words, and excluding declarations and pure display/table markup. Semantic claim-registry completeness remains `not_machine_detectable`. The historical mechanical coverage report recorded zero candidate gaps in its bounded citation/quantitative trigger grammar, but that result did not validate the now-superseded high-impact classification or evidence-row selection. The stable rebuild's coverage replay passes against the unchanged manuscript; as before, bounded mechanical coverage is not proof of semantic extraction completeness.

## Phase A — 100% reference verification

Legend: A = author, Y = year, T = title, V = venue/publisher, N = volume/issue/pages. Each field receives an explicit `VERIFIED`, `NOT_FOUND`, or `MISMATCH` verdict. Every DOI resolves to the same work as the publisher record.

| Key; exact query | Top primary/official record | A | Y | T | V | N | DOI | Hallucination scan |
|---|---|---|---|---|---|---|---|---|
| `GaspardRice1989Semiclassical`; `"Semiclassical quantization of the scattering from a classically chaotic repellor" 10.1063/1.456018` | [AIP/JCP article](https://pubs.aip.org/jcp/article/90/4/2242/463979/Semiclassical-quantization-of-the-scattering-from) | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED: 90(4), 2242–2254 | VERIFIED | TF/PAC/IH/PH/SH: none |
| `GaspardRice1989Exact`; `"Exact quantization of the scattering from a classically chaotic repellor" 10.1063/1.456019` | [AIP/JCP article](https://pubs.aip.org/jcp/article/90/4/2255/464015/Exact-quantization-of-the-scattering-from-a) | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED: 90(4), 2255–2262 | VERIFIED | none |
| `Wirzba1999`; `"Quantum mechanics and semiclassics of hyperbolic n-disk scattering systems" 10.1016/S0370-1573(98)00036-2` | [Elsevier/ScienceDirect article](https://www.sciencedirect.com/science/article/abs/pii/S0370157398000362) | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED: 309(1–2), 1–116 | VERIFIED | none |
| `Ikawa1988`; `"Decay of solutions of the wave equation in the exterior of several convex bodies" 10.5802/aif.1137` | [Annales de l'Institut Fourier/Centre Mersenne](https://aif.centre-mersenne.org/articles/10.5802/aif.1137/) | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED: 38(2), 113–146 | VERIFIED | none |
| `BowenLanford1970`; `"Zeta functions of restrictions of the shift transformation" 10.1090/pspum/014/9985` | [AMS, Global Analysis vol. 14](https://bookstore.ams.org/PSPUM/14) | **MISMATCH:** official `O. E. Lanford III`; BibTeX `Oscar E. Lanford` omits `III` | VERIFIED | VERIFIED | VERIFIED | VERIFIED: PSPM 14, 43–49 | VERIFIED | **SH: author-suffix distortion**; no fabrication or DOI misdirection |
| `Ruelle1976`; `"Zeta-functions for expanding maps and Anosov flows" 10.1007/BF01403069` | [Springer article](https://link.springer.com/article/10.1007/BF01403069) | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED: 34, 231–242 | VERIFIED | none |
| `CvitanovicEckhardt1989`; `"Periodic-orbit quantization of chaotic systems" 10.1103/PhysRevLett.63.823` | [APS/Physical Review Letters](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.63.823) | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED: 63(8), 823–826 | VERIFIED | none |
| `Livsic1972`; `"Cohomology of Dynamical Systems" 10.1070/IM1972v006n06ABEH001919` | [MathNet/Steklov official record](https://www.mathnet.ru/eng/im2373) | VERIFIED: official `A. N. Livshits`/DOI `A. N. Livšic`; transliteration normalized | VERIFIED | VERIFIED | VERIFIED | VERIFIED: 6(6), 1278–1301 | VERIFIED | none |

Strict entry counts: seven `VERIFIED`, one `MISMATCH`, zero `NOT_FOUND`. No Total Fabrication (TF), Plausible-Author/Conference spoof (PAC), Incomplete Hallucination (IH), Partial Hallucination (PH), author spoofing, venue exploitation, mashup fabrication, temporal masking, or DOI misdirection was found. The one Subtle Hallucination (SH) pattern is the omitted author suffix.

## Phase B — citation-context audit

All citation commands were audited, not sampled. The Phase-A suffix defect does not alter the mathematical content of the Bowen–Lanford source, so its context can still be substantively verified while the bibliography remains blocked.

| TeX line | Key and manuscript assertion | Supporting primary/official locator | Verdict |
|---:|---|---|---|
| 60 | `Ikawa1988`: periodic rays/Poincaré maps in wave decay outside convex bodies | official article, Introduction and theorem statements | VERIFIED |
| 62 | `GaspardRice1989Semiclassical`: periodic-orbit semiclassical construction organizes repellor resonances | AIP article, §§II–IV | VERIFIED |
| 64 | `GaspardRice1989Exact`: exact quantum scattering uses a multiple-scattering matrix/determinant | AIP article, abstract and §§II–III | VERIFIED |
| 104 | `Wirzba1999`: symbolic, stability, semiclassical, and exact multiscattering objects are distinct | Elsevier article, §§2–4 | VERIFIED |
| 115 | `BowenLanford1970`: finite-type shift zeta has reciprocal-determinant form | AMS source, pp. 43–49 | VERIFIED content; bibliographic author field remains MISMATCH |
| 117 | `Ruelle1976`: flow zeta/transfer constructions retain roof and dynamical timing | [Author's IHES preprint](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/RUELLE/1965-1976/MP_75_106/MP_75_106.pdf), §§1–3 | VERIFIED |
| 123 | `GaspardRice1989Exact`: three-hard-disk S-matrix resonances use the multiscattering determinant | AIP article, abstract and §§II–III | VERIFIED |
| 125 | `Wirzba1999`: determinant/cumulant and semiclassical-limit distinctions | Elsevier article, §§4–6 | VERIFIED |
| 203 | `CvitanovicEckhardt1989`: periodic-orbit cycle expansions in chaotic quantization | APS article, pp. 823–826 | VERIFIED |
| 247 | `Livsic1972`: periodic-orbit sums are cohomological obstructions | MathNet article, main criteria and official abstract; manuscript uses only the elementary necessary telescoping direction | VERIFIED |

Citation-context counts: 10/10 supported; 0 `MINOR_DISTORTION`; 0 `MAJOR_DISTORTION`; 0 `UNVERIFIABLE`. All eight bibliography keys occur in the manuscript, and every cited key exists in the bibliography.

## Phase C — numerical and data-surface audit

All manuscript-registered surfaces were checked against committed exact artifacts, receipts, source, and fresh read-only replays.

| Surface and TeX locator | Local evidence and independent consistency check | Verdict |
|---|---|---|
| Geometry/no-eclipse contract and exact symmetric witnesses, lines 93–101, 207–233 | Direct capsule-distance proof gives `d>4a/√3`; all three frozen ratios satisfy it. `round8_exact_roof_witnesses.csv` has 6 rows and preserves exact radical formulas | VERIFIED |
| Unit-roof `q`-symbol theorem and replay, lines 137–180 | Direct eigenvalue/Möbius proof. `round7_q_symbolic_counts.csv` has 84 rows; `round7_q_symbolic_prefix.csv` has 182; all exact-equality flags pass; `q=3` total through degree 12 is 747 | VERIFIED |
| Hyperbolic half-density surface, lines 182–200 | Direct two-eigenvalue proof. `round5_universal_half_density_ledger.csv` has 6,723 rows = 2,241 owners × repetitions 1,2,3; each repetition contributes 2,241 rows; residual gates pass | VERIFIED |
| Physical owner/stability/conditioning ledger, lines 313–325 | 2,241 accepted rows; `round4_conditioning_metrics.json` partitions them into 2,202 direct Newton + 39 fallback; `round4_fallback_audit.csv` has exactly 39 rows and all acceptance/firewall fields pass | VERIFIED |
| Scalar-clock replay, lines 329–346 | `round8_physical_roof_replay.csv` has 2,241 rows. Independent grouping gives 747 per geometry and, for each of `29/5`, `6`, `31/5`, exactly 3 matches + 744 disagreements | VERIFIED |
| Exact gap/minimax/dimensionless quantities, lines 228–307 | Algebra gives `2−√3 = 0.2679491924…`, half-gap `0.1339745962…`, and frozen relative mismatch `(2−√3)/4 = 0.0669872981…`; summary JSON records the same exact/decimal values | VERIFIED |
| Reproducibility and target firewall, lines 323, 350–352 | Fresh `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s code -p 'test_*.py' -v`: **65/65 PASS**. Fresh `bash experiments/reproduce_round8.sh verify`: **12/12 PASS**, two temporary builds byte-identical, committed artifacts VERIFIED. Target-data firewalls pass | VERIFIED |

No unexplained missing values, impossible denominators, row-count drift, exact/numerical category drift, or discarded difficult rows was found. The manuscript correctly distinguishes exact radical witnesses from high-precision general orbit solutions.

### Phase C4 — experiment provenance and claim alignment

**Boundary:** "This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."

A repository-wide key search within Paper 25 found no research passport containing `experiment_intake_declaration`, `experiment_provenance[]`, or claim-level `planned_experiment_ids[]`. There is also no `repro_lock.ars_version` proving that the intake predates ARS issue #260. The manuscript reports own computational runs, numerical billiard solutions, and result ledgers, so the fail-closed D7 rule treats the paper as post-#260 and triggers condition 1. The seven local data surfaces, tests, receipts, and byte-identical replay remain technically verified; they do not substitute for the scholar's disclosure and provenance attestation.

No `EA-NNN` alignment row is emitted: the required provenance join side is absent, and inventing an experiment identity, ownership statement, result pointer, negative-result declaration, or limitation declaration would be improper. The scholar must provide an `experiments_declared` intake and complete `experiment_provenance[]` entries (including `experiment_id`, `title`, `repro_lock`, `planned_vs_executed`, `negative_results`, and `known_limitations`), then bind the experiment-backed claims through `planned_experiment_ids[]`. Phase C4 and the affected failure modes must then be re-run.

## Phase D — originality spot-check

Quoted searches were run as exact-phrase web queries. `NO_EXACT_3P_MATCH` means no exact third-party match for the full fragment; broad hits sharing generic words were not counted.

| # | Section; TeX line | Exact 8–12-word fragment | Web-search verdict |
|---:|---|---|---|
| 1 | Introduction, 57 | “Confusing the unit symbolic clock with the physical clock can turn” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 2 | Introduction, 71 | “Two symmetric periodic orbits already have different physical mean roofs” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 3 | Introduction, 73 | “These positive results belong to different typed objects” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 4 | Introduction, 85 | “The central negative theorem is not based on poor numerical agreement” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 5 | Related/background, 94 | “Its primitive owner is an oriented cyclic collision word” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 6 | Related/background, 129 | “All three objects can mention the same collision words” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 7 | Related/background, 131 | “Allowing a separate fitted constant for each owner would reproduce lengths” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 8 | Exact unit-roof result, 157 | “Every closed word is a traversal of a unique primitive cyclic word” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 9 | Exact unit-roof result, 170 | “The phase relation is exact and nonspecific: it holds” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 10 | Exact unit-roof result, 174 | “The poles are those of the finite adjacency matrix” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 11 | Exact stability result, 200 | “This is a stability identity, not a global flow determinant” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 12 | Physical-roof obstruction, 225 | “symmetry around the center--centroid line gives equal incoming and outgoing angles” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 13 | Physical-roof obstruction, 279 | “It quantifies the irreducible error of the frozen one-parameter hypothesis” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 14 | Physical-roof obstruction, 291 | “The obstruction therefore occurs at bare clock level and cannot be repaired” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 15 | Physical-roof obstruction, 307 | “not a statistical effect and does not vanish with numerical precision” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 16 | Locked replay, 313 | “Every row passes two-solver agreement, reflection, visibility, and length checks” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 17 | Computational method, 323 | “The Round-8 replay does not rerun an unconstrained optimization” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 18 | Computational method, 325 | “This method distinguishes numerical from exact equality. Symmetric formulas” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 19 | Computational method, 360 | “Recording and retaining them closes that procedural loophole” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 20 | Adversarial assessment, 395 | “Ownership and timing must be established first, analytic wiring second” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 21 | Limitations, 401 | “The two-orbit proof avoids this limitation for noncohomology” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 22 | Conclusion, 413 | “The next viable physical step is a genuinely nonconstant-roof operator” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |

Additional checks: an exact-email search identifies the author's public corpus, including the publisher record for [“The emergence of prime distribution from low-dimensional deterministic chaos”](https://doi.org/10.1080/27684830.2026.2684334) and official preprint records. None of the 22 queried fragments matched an attributable prior work. A local 10-word-shingle scan against all other repository manuscripts found zero Paper-25 body matches. Paper 24 and Paper 25 share no exact 8-word body-text shingle.

**Limitation:** Phase D is a search-engine heuristic, not Turnitin or iThenticate, and cannot certify absence from paywalled, unindexed, or private corpora.

## Phase E — STABLE REBUILD PASS; HISTORICAL SAMPLE SUPERSEDED

The current controlling result is the independent [Stage-2.5 Phase-E semantic audit](stage2_5_phase_e_semantic_audit.md). Against the unchanged manuscript bytes and stable rebuilt sidecars, it checked every selected distinct claim: **45 HIGH-IMPACT + 3 RANDOM = 48/48 claims VERIFIED**. Verdict totals are 48 `VERIFIED`, zero `MINOR_DISTORTION`, zero `MAJOR_DISTORTION`, zero `UNVERIFIABLE`, and zero `UNVERIFIABLE_ACCESS`.

The exact registry projection is also closed: **49/49 required `(claim_id, ref_slug)` tuples** are present, comprising 47 project-internal tuples and the two external-source tuples attached to `P25-E1-015`. The evidence rows and coverage replay pass the official ARS validators. All persisted rows remain explicitly `anchorless`; the semantic PASS neither embeds the external excerpt candidates nor upgrades provenance. Semantic extraction completeness remains `not_machine_detectable`. The `BowenLanford1970` block is outside the selected Phase-E population, so the clean semantic result does not cure its Phase-A author-field mismatch.

### Historical audit trajectory — retained

The previous `4 HIGH-IMPACT + 7 RANDOM`, `11/72`, “all VERIFIED,” and manually unpacked high-impact table were produced under the invalid selection logic identified by independent sidecar validation. In particular, the old classification did not demonstrate that every numerical, causal, methods-critical, headline, and disputed claim entered the uncapped `HIGH-IMPACT` tier required by ARS #549. Those statements and their claim-level verdict aggregate remain **superseded**, even though the separately audited Phase-C numerical/data surfaces remain valid.

At that audit point, 72 was retained only as the historical extracted-row count and the report required a rebuild against unchanged manuscript bytes, uncapped high-impact reclassification, a recomputed random sentinel, regenerated/replay-validated sidecars, and fresh claim verification. That required chain has now closed in the linked semantic audit. The stable result above replaces the old sampling denominator without erasing why the old result was rejected.

## Seven AI-research failure modes

| Mode | Status | Concrete local evidence |
|---|---|---|
| 1. Implementation bug passing self-review | **INSUFFICIENT EVIDENCE / BLOCKING** | 65/65 full tests, 12/12 Round-8 tests, two byte-identical temporary rebuilds, exact checks, independent partitions, and fail-closed validation pass, but no scholar-owned run provenance/attestation is registered |
| 2. Hallucinated citation | **SUSPECTED / BLOCKING** | All works exist, but the official AMS author is `O. E. Lanford III`; the BibTeX author field omits `III` (`IL-SERIOUS-1`) |
| 3. Hallucinated experimental result | **INSUFFICIENT EVIDENCE / BLOCKING** | Every numerical claim maps to committed CSV/JSON evidence and receipts and was independently recomputed, but the scholar has not declared which runs/results are owned evidence |
| 4. Shortcut reliance | CLEAR | The central conclusion is an exact two-orbit obstruction, not a fitted score; no prime/zero/resonance target enters design; neighboring geometries and source-absent controls are explicit |
| 5. Bug reframed as novel insight | **INSUFFICIENT EVIDENCE / BLOCKING** | The negative clock result follows analytically and fresh replay agrees, but the mandatory scholar-owned run history needed to close this mode is absent |
| 6. Methodology fabrication | **INSUFFICIENT EVIDENCE / BLOCKING** | Manuscript methods correspond to executable paths/configs/artifacts, but no scholar-owned experiment intake binds those procedures to declared executions |
| 7. Early-stage frame-lock | CLEAR | The paper separates symbolic, physical, and quantum objects, rejects scalar credit transfer, leaves the physical Route-A tuple unassigned, and states the viable nonconstant-roof successor |

Mode 2 is `SUSPECTED`; Modes 1, 3, 5, and 6 are `INSUFFICIENT EVIDENCE` because of the one shared missing scholar-intake defect; Modes 4 and 7 are CLEAR. Both categories block Stage 2.5.

## Issue list

### SERIOUS — must fix

| ID | Surface | Exact location | Finding | Required correction | Official source |
|---|---|---|---|---|---|
| **IL-SERIOUS-1** | Reference author metadata | `paper/references.bib:46`, key `BowenLanford1970` | Official author is `O. E. Lanford III`; current entry drops `III` | Encode the suffix in BibTeX, e.g. `author = {Bowen, Rufus and Lanford, III, Oscar E.}`; then rebuild and re-run Phase A/B | [AMS volume 14 table of contents](https://bookstore.ams.org/PSPUM/14) |
| **IL-SERIOUS-2** | Experiment intake/provenance | Paper-25 passport/intake: absent; experiment-backed manuscript surfaces at `paper/manuscript.tex:176–200,313–352` | Own computational results are reported without `experiment_intake_declaration`, `experiment_provenance[]`, or claim bindings; no positive pre-#260 legacy proof exists | Scholar supplies the declaration and provenance/claim bindings described in Phase C4; then re-run C4 and Modes 1/3/5/6 | ARS Stage 2.5 Phase C4, D7 condition 1 |

No MINOR findings. The stable Phase-E rebuild is clean, but Stage 2.5 remains **FAIL-CLOSED**: after `IL-SERIOUS-1` is repaired and `IL-SERIOUS-2` is supplied by the scholar, run fresh reference/context and Phase-C4/failure-mode verification. Do not release Paper 25 or authorize Stage 3 on the Phase-E PASS alone, except through the separately recorded ARS fail-loop override policy.
