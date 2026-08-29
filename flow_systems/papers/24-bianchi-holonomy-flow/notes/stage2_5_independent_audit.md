# Stage 2.5 independent integrity audit — Paper 24

Audit date: 2026-08-29 UTC  
Protocol: ARS-Codex academic-research-suite, Stage 2.5 initial integrity gate  
Audited manuscript SHA-256: `e43ba0f77332b79df4d84346dcb6e3041c20f4bdded5a91f42caac348ea9fd11`  
Audited bibliography SHA-256: `11e7dd42f07ecf22744f5d9c829d13a22212e0d43cb2591c0e9dfd66bde86d87`

## Current controlling status — 2026-08-29 addendum

**PASS AT MANDATORY CHECKPOINT — Stage 3 not authorized.**  The later fresh
Stage-2.5 pass recorded in [stage2_5_integrity_report.md](stage2_5_integrity_report.md)
supersedes the historical FAIL-CLOSED decision retained below.  Current closure
is: 7/7 references VERIFIED; 64/64 selected claims VERIFIED; 66/66 required
tuple carriers structurally present and still explicitly `anchorless`; one
scholar declaration plus 7 experiment-provenance entries; and 11 aligned direct
experiment-backed claims.  The former experiment-intake issue is CLOSED, and
there is no active blocking integrity issue.  The workflow remains stopped at
the mandatory checkpoint and must not enter Stage 3 without explicit
authorization.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

Everything from the next heading onward is retained as the historical audit
trajectory.  Its missing-declaration, blocker, failure-mode, issue-table, and
FAIL-CLOSED language is **superseded for current status**, not deleted or
silently rewritten.

## Historical decision — superseded

**FAIL-CLOSED — BLOCK pending scholar-owned experiment intake.** Phases A–D retain their stated results. The paper reports own computational results while no `experiment_intake_declaration` or `experiment_provenance[]` is present and no positive pre-#260 legacy proof exists, so ARS Phase C4/D7 still fails closed (**`IL-SERIOUS-1`**). The earlier invalid Phase-E sample remains superseded as a historical audit event, but the registry/evidence chain has since been stably rebuilt and independently checked: the controlling [Phase-E semantic audit](stage2_5_phase_e_semantic_audit.md) records a clean PASS for **64/64 selected distinct claims** and **66/66 required evidence tuples**. That Phase-E PASS removes the former rebuild requirement; it does not close `IL-SERIOUS-1` or change the overall Stage-2.5 verdict. No MINOR IDs.

| Surface | Coverage | Result |
|---|---:|---|
| Phase A: registered references | 7/7 (100%) | 7 VERIFIED; 0 NOT_FOUND; 0 MISMATCH |
| Phase B: citation contexts | 9/9 (100%) | 9 supported; 0 distorted; 0 unverifiable |
| Phase C: registered numerical/data surfaces | 6/6 (100%) | all internally consistent and replayed |
| Phase C4: scholar-owned experiment intake | 0/1 passport declaration | absent; D7 structural FAIL |
| Phase D: body-paragraph originality | 21/69 (30.4%) | no exact third-party prose match found |
| Phase E: Claim Registry and evidence selection | stable registry: 76 rows; 64 selected distinct claims; 66 required tuples | **PASS:** 64/64 claims VERIFIED; 66/66 tuples present; historical sample remains superseded |
| Ghost/unused citation check | 7/7 BibTeX keys cited | none |

The paragraph denominator is a reproducible prose-block count: numbered-section body text from `Introduction` through `Conclusion`, split on blank lines, retaining blocks with at least 12 alphabetic words, and excluding declarations and pure display/table markup. Semantic claim-registry completeness remains `not_machine_detectable`. The historical mechanical coverage report recorded zero candidate gaps in its bounded citation/quantitative trigger grammar, but that result did not validate the now-superseded high-impact classification or evidence-row selection. The stable rebuild's coverage replay passes against the unchanged manuscript; as before, bounded mechanical coverage is not proof of semantic extraction completeness.

## Phase A — 100% reference verification

Legend: A = author, Y = year, T = title, V = venue/publisher, N = volume/issue/pages or book series/version. Each field receives an explicit `VERIFIED`, `NOT_FOUND`, or `MISMATCH` verdict. DOI URLs were also checked against the official DOI registry; every DOI resolves to the same work as the publisher record.

| Key; exact query | Top primary/official record | A | Y | T | V | N | DOI/URL | Hallucination scan |
|---|---|---|---|---|---|---|---|---|
| `PfaffRaimbault2020`; `"The Torsion in Symmetric Powers on Congruence Subgroups of Bianchi Groups"` | [AMS, Trans. AMS 373(1)](https://www.ams.org/tran/2020-373-01/) | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED: 373(1), 109–148 | VERIFIED: `10.1090/tran/7875` | TF/PAC/IH/PH/SH: none |
| `Pfaff2015`; `"Selberg Zeta Functions on Odd-Dimensional Hyperbolic Manifolds of Finite Volume"` | [DOI/publisher record](https://doi.org/10.1515/crelle-2013-0047) | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED: printed journal number 703, 115–145 | VERIFIED | none; the registry's year-volume modeling is a normalization, not a different work |
| `LinLipnowski2022`; `"The Seiberg-Witten Equations and the Length Spectrum of Hyperbolic Three-Manifolds"` | [AMS, JAMS 35(1)](https://www.ams.org/journals/jams/2022-35-01/home.html?active=allissues) | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED: 35(1), 233–293 | VERIFIED: `10.1090/jams/982` | none |
| `HIKMOT2016`; `"Verified Computations for Hyperbolic 3-Manifolds"` | [Taylor & Francis article](https://www.tandfonline.com/doi/full/10.1080/10586458.2015.1029599) | VERIFIED: all six authors | VERIFIED | VERIFIED | VERIFIED | VERIFIED: 25(1), 66–78 | VERIFIED | none |
| `Reid1991`; `"Arithmeticity of Knot Complements" 10.1112/jlms/s2-43.1.171` | [London Mathematical Society/OUP article](https://academic.oup.com/jlms/article/s2-43/1/171/888921/Arithmeticity-of-Knot-Complements) | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED: s2-43(1), 171–184 | VERIFIED | none |
| `MaclachlanReid2003`; `"The Arithmetic of Hyperbolic 3-Manifolds" 10.1007/978-1-4757-6720-9` | [Springer book](https://link.springer.com/book/10.1007/978-1-4757-6720-9) | VERIFIED | VERIFIED | VERIFIED | VERIFIED: Springer, New York | VERIFIED: GTM 219 | VERIFIED | none |
| `SnapPyDocs2026`; `"SnapPy 3.3.2 documentation" "Verified computations"` | [Official SnapPy verification documentation](https://snappy.computop.org/verify.html) | VERIFIED: corporate project author | VERIFIED: accessed/versioned 2026 record | VERIFIED: composite documentation/page title | VERIFIED | VERIFIED: version 3.3.2; pages n/a | VERIFIED: official HTTPS URL | none |

Hallucination-pattern result: no Total Fabrication (TF), Plausible-Author/Conference spoof (PAC), Incomplete Hallucination (IH), Partial Hallucination (PH), Subtle Hallucination (SH), author spoofing, venue exploitation, mashup fabrication, temporal masking, or DOI misdirection was found.

## Phase B — citation-context audit

All citation commands were audited, not sampled.

| TeX line | Key and manuscript assertion | Supporting primary/official locator | Verdict |
|---:|---|---|---|
| 65 | `MaclachlanReid2003`: arithmetic Kleinian/Bianchi and congruence setting | Springer book, Chs. 10–11 | VERIFIED |
| 67 | `PfaffRaimbault2020`: Bianchi congruence subgroups and torsion questions | [Author preprint](https://arxiv.org/abs/1503.04785), Introduction and §2 | VERIFIED |
| 69 | `Pfaff2015`: finite-volume Selberg-zeta theory requires geometric/representation data | [Author preprint](https://arxiv.org/abs/1205.1754), abstract and §§3–5 | VERIFIED |
| 97 | `LinLipnowski2022`: complex length/holonomy-trace participation | [Author preprint](https://arxiv.org/abs/1810.06346), Introduction and §2 | VERIFIED |
| 132 | `Pfaff2015`: regularized traces, scattering, and representation data in finite-volume theory | same preprint, abstract and §§3–5 | VERIFIED |
| 135 | `PfaffRaimbault2020`: arithmetic/topological interaction in Bianchi congruence towers | same preprint, Introduction and §2 | VERIFIED; manuscript does not overextend it to Gaussian specificity |
| 139 | `HIKMOT2016`: interval certification of complete cusped hyperbolic structures | publisher article, Theorem 5.1 and §§3–5 | VERIFIED |
| 141 | `SnapPyDocs2026`: verified intervals distinguished from high-precision numerics | official `Verified computations` page and `verify_hyperbolicity` documentation | VERIFIED |
| 144 | `Reid1991`: the non-figure-eight `5_2` complement is non-arithmetic via knot-complement classification | official article, main theorem; local named-knot identity is separately artifact-bound | VERIFIED |

Citation-context counts: 9/9 supported; 0 `MINOR_DISTORTION`; 0 `MAJOR_DISTORTION`; 0 `UNVERIFIABLE`. All seven bibliography keys occur in the manuscript, and every cited key exists in the bibliography.

## Phase C — numerical and data-surface audit

All manuscript-registered surfaces were checked against committed exact artifacts, receipts, source, and fresh read-only replays.

| Surface and TeX locator | Local evidence and independent consistency check | Verdict |
|---|---|---|
| Universal identity and first-jet laws, lines 45–49, 174–205, 253–271 | Direct algebraic proofs; `round8_congruence_specificity_metrics.json`; exact ring-arithmetic tests | VERIFIED |
| Frozen enumeration: 22,409 reduced words → 11,481 unique exact matrices, lines 291–295 | `round7_trace_discriminant_ledger.csv` has exactly 11,481 rows; every row records determinant, level, identity, conjugacy, inversion, and power checks as true | VERIFIED |
| Collision profile, lines 303–332 | `round8_d9_jet_collision_profile.csv`: 145 scalar rows; sums give 11,481 matrices, 517 joint descriptors, and 10,964 joint collisions. Independently, `11,481−145=11,336` and `11,336−10,964=372`; maxima are 505 and 84; singleton joint buckets are 0 | VERIFIED |
| Cross-ring/neighbor-level controls, lines 336–354 | `round8_universal_congruence_controls.csv`: 5 subpanels/4 families; row sum 6,396; principal-congruence sum 6,392; all principal rows pass; 4 ambient witnesses split 3 nonintegral/1 integral; canonical Route-A types remain exactly 2/3 | VERIFIED |
| Power/repetition checks, lines 232–249 and 293 | Exact recurrence proved; all 11,481 ledger rows pass `r=1,…,5`; no primitive-root inference is promoted | VERIFIED |
| Reproducibility and target firewall, lines 358–360 | Fresh `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s code -p 'test_*.py' -v`: **71/71 PASS**. Fresh `bash experiments/reproduce_round8.sh`: **14/14 PASS**, two temporary builds byte-identical, committed artifacts VERIFIED. Target-table firewall tests pass | VERIFIED |

No unexplained missing values, impossible denominators, count inconsistencies, precision promotion, or exact/numerical category drift was found. The manuscript correctly labels the finite ledger as finite and the algebraic formulas as exact.

### Phase C4 — experiment provenance and claim alignment

**Boundary:** "This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."

A repository-wide key search within Paper 24 found no research passport containing `experiment_intake_declaration`, `experiment_provenance[]`, or claim-level `planned_experiment_ids[]`. There is also no `repro_lock.ars_version` proving that the intake predates ARS issue #260. The manuscript nevertheless reports own computational runs and result ledgers, so the fail-closed D7 rule treats the paper as post-#260 and triggers condition 1. The six local data surfaces, tests, receipts, and byte-identical replay remain technically verified; they do not substitute for the scholar's disclosure and provenance attestation.

No `EA-NNN` alignment row is emitted: the required provenance join side is absent, and inventing an experiment identity, ownership statement, result pointer, negative-result declaration, or limitation declaration would be improper. The scholar must provide an `experiments_declared` intake and complete `experiment_provenance[]` entries (including `experiment_id`, `title`, `repro_lock`, `planned_vs_executed`, `negative_results`, and `known_limitations`), then bind the experiment-backed claims through `planned_experiment_ids[]`. Phase C4 and the affected failure modes must then be re-run.

## Phase D — originality spot-check

Quoted searches were run as exact-phrase web queries. `NO_EXACT_3P_MATCH` means no exact third-party match for the full fragment; broad search-engine hits sharing a few generic words were not counted as matches.

| # | Section; TeX line | Exact 8–12-word fragment | Web-search verdict |
|---:|---|---|---|
| 1 | Introduction, 62 | “a congruence identity can look arithmetically distinctive inside one ring” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 2 | Introduction, 82 | “The finite audit has no target prime or zero labels” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 3 | Introduction, 84 | “The contribution is deliberately asymmetric. The positive result is a” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 4 | Geometric/algebraic setting, 94 | “The computation samples an elementary-generator word ball inside this group” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 5 | Geometric/algebraic setting, 115 | “Eligibility is not ownership: a useful owner coordinate must control” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 6 | Related work, 150 | “The manuscript separates three questions that can otherwise be conflated” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 7 | Related work, 152 | “its cross-ring behavior is predicted before the control replay” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 8 | Related work, 156 | “None of these properties alone gives injectivity, primitivity, or arithmetic ownership” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 9 | Universal theorems, 212 | “Large collisions are therefore structural rather than an implementation defect” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 10 | Universal theorems, 214 | “Second, the non-zero-divisor hypothesis marks the cancellation boundary” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 11 | Universal theorems, 218 | “The first jet resolves information discarded by determinant” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 12 | Universal theorems, 230 | “the jet lies in the trace-zero tangent space at the identity” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 13 | Exact certificate, 291 | “The computation starts from a prespecified elementary-generator word ball” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 14 | Exact certificate, 301 | “A non-divisible entry stops the row rather than coercing a quotient” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 15 | Exact certificate, 309 | “The maximum bucket probes a different failure mode from total collisions” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 16 | Exact certificate, 358 | “Verification reads committed artifacts, checks schema and hashes, regenerates exact core results” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 17 | Adversarial assessment, 372 | “An arithmetic-specific owner statistic should deteriorate when its source is removed” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 18 | Adversarial assessment, 396 | “Duplicate matrices are already removed, so word equality alone cannot explain” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 19 | Adversarial assessment, 410 | “Negative identity-level information is monotone under restriction; finite injectivity evidence” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 20 | Limitations, 424 | “It requires a source-owned prime-ideal rule, including norm multiplicities” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |
| 21 | Conclusion, 430 | “The next meaningful step is a source-derived ideal-valued refinement” | NO_EXACT_3P_MATCH → ORIGINAL_HEURISTIC |

Additional checks: an exact-email search identifies the author's public corpus, including the publisher record for [“The emergence of prime distribution from low-dimensional deterministic chaos”](https://doi.org/10.1080/27684830.2026.2684334). None of the 21 queried fragments matched an attributable prior work. A local 10-word-shingle scan against other repository manuscripts found only the literal Route-A tuple (`A0…A4`) in other roadmap papers; this is a declared formal status code, not appropriated prose. Paper 24 and Paper 25 share no exact 8-word body-text shingle.

**Limitation:** Phase D is a search-engine heuristic, not Turnitin or iThenticate, and cannot certify absence from paywalled, unindexed, or private corpora.

## Phase E — STABLE REBUILD PASS; HISTORICAL SAMPLE SUPERSEDED

The current controlling result is the independent [Stage-2.5 Phase-E semantic audit](stage2_5_phase_e_semantic_audit.md). Against the unchanged manuscript bytes and stable rebuilt sidecars, it checked every selected distinct claim: **61 HIGH-IMPACT + 3 RANDOM = 64/64 claims VERIFIED**. Verdict totals are 64 `VERIFIED`, zero `MINOR_DISTORTION`, zero `MAJOR_DISTORTION`, zero `UNVERIFIABLE`, and zero `UNVERIFIABLE_ACCESS`.

The exact registry projection is also closed: **66/66 required `(claim_id, ref_slug)` tuples** are present, comprising 63 project-internal tuples and the three external-source tuples attached to `P24-E1-012`. The evidence rows and coverage replay pass the official ARS validators. All persisted rows remain explicitly `anchorless`; the semantic PASS neither embeds the external excerpt candidates nor upgrades provenance. Semantic extraction completeness remains `not_machine_detectable`.

### Historical audit trajectory — retained

Independent sidecar validation had established that the previously persisted Paper-24 evidence sidecar contained 11 selected claim rows, not the 12 then reported, and that its random sentinel was one row short. More importantly, that historical registry assigned many numerical, causal, and methods-critical claims to non-`HIGH-IMPACT` tiers even though ARS #549 requires every such claim to be `HIGH-IMPACT` and checked without a cap. Therefore the earlier `4 HIGH-IMPACT + 8 RANDOM`, `12/76`, “all VERIFIED,” and manually unpacked `12/12` statements remain **superseded** and must not be reused as Stage-2.5 evidence.

At that audit point, 76 was retained only as the historical extracted-row count and the report required a rebuild against unchanged manuscript bytes, uncapped high-impact reclassification, a recomputed random sentinel, regenerated/replay-validated sidecars, and fresh claim verification. That required chain has now closed in the linked semantic audit. The stable result above replaces the old sampling denominator without erasing why the old result was rejected.

## Seven AI-research failure modes

| Mode | Status | Concrete local evidence |
|---|---|---|
| 1. Implementation bug passing self-review | **INSUFFICIENT EVIDENCE / BLOCKING** | Exact Gaussian/ring types, fail-closed assertions, 71/71 full tests, 14/14 Round-8 tests, two byte-identical temporary rebuilds, and independent arithmetic pass, but no scholar-owned run provenance/attestation is registered |
| 2. Hallucinated citation | CLEAR | 7/7 identities and all fields verified against publisher/official records; 9/9 contexts supported; no DOI misdirection |
| 3. Hallucinated experimental result | **INSUFFICIENT EVIDENCE / BLOCKING** | Every reported count maps to committed CSV/JSON evidence and receipts and was independently recomputed, but the scholar has not declared which runs/results are owned evidence |
| 4. Shortcut reliance | CLEAR | The paper explicitly runs source-removed/cross-ring/neighbor-level controls and accepts the negative specificity result; no external target labels are available to exploit |
| 5. Bug reframed as novel insight | **INSUFFICIENT EVIDENCE / BLOCKING** | The negative result follows from a symbolic theorem and fresh replay agrees, but the mandatory scholar-owned run history needed to close this mode is absent |
| 6. Methodology fabrication | **INSUFFICIENT EVIDENCE / BLOCKING** | Manuscript methods match the executable paths/configs/artifacts, but no scholar-owned experiment intake binds those procedures to declared executions |
| 7. Early-stage frame-lock | CLEAR | The manuscript rejects the original Gaussian-specific framing, stops Route-A credit at the typed proxy, states open obligations, and does not force a positive orbit/spectral conclusion |

Modes 1, 3, 5, and 6 are blocked by one shared missing-input defect, not four independent scientific discrepancies. Modes 2, 4, and 7 are CLEAR.

## Issue list

### SERIOUS — scholar action required

| ID | Surface | Exact location | Finding | Required correction | Protocol basis |
|---|---|---|---|---|---|
| **IL-SERIOUS-1** | Experiment intake/provenance | Paper-24 passport/intake: absent; experiment-backed manuscript surfaces at `paper/manuscript.tex:291–360` | Own computational results are reported without `experiment_intake_declaration`, `experiment_provenance[]`, or claim bindings; no positive pre-#260 legacy proof exists | Scholar supplies the declaration and provenance/claim bindings described in Phase C4; then re-run C4 and Modes 1/3/5/6 | ARS Stage 2.5 Phase C4, D7 condition 1 |

No MINOR findings. Phases A–D are otherwise clean within their registered and sampled populations, and the stable Phase-E rebuild is clean. Nevertheless, Stage 2.5 remains **FAIL-CLOSED** and may not authorize release or Stage 3 while `IL-SERIOUS-1` remains unresolved, except through the separately recorded ARS fail-loop override policy.
