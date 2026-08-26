# P68 Stage 2.5 integrity and priority audit

Audit date: 2026-08-26 (UTC)  
Audited package: `papers/68-complete-bipartite-homshift-conjugacies/`  
Release posture: **HOLD — no upload, contact, release, submission, or priority claim**

## 1. Disposition

**Overall Stage 2.5 verdict: FAIL (correctable bibliographic metadata; no
mathematical failure found).**

The strict integrity protocol does not permit an inaccurate bibliography field
to be converted into a note-only pass.  The author-hosted 2019 lecture exists
and supports every cited context, but its printed title is “Lecture 4: An
introduction to hom-shifts,” not the BibTeX title “Hom-Shifts, Lecture 4.”
Accordingly Phase A contains one `MISMATCH`.  The theorem/proof audit, all ten
citation contexts, citation graph, tables, formulas, and deterministic controls
otherwise pass this bounded audit.  The correction is bibliographic, not
mathematical.

This audit does not alter `main.tex`, `sections/`, `references.bib`, any PDF, or
the pre-existing claim-registry sidecars.  Detailed queries and direct URLs are
in [SOURCE_SEARCH_LEDGER.md](SOURCE_SEARCH_LEDGER.md).

## 2. Audit frame and calibration

- Evidence hierarchy used: publisher/DOI or primary repository; author-hosted
  document; manuscript theorem/proof; deterministic control receipt.  Search
  snippets and third-party metadata were not treated as final evidence.
- Source verification and claim support are separate from novelty screening.
- “No exact result found” means only that the bounded public search described
  here did not locate one through 2026-08-26.
- No global novelty, plagiarism, authorship, or priority certificate is issued.
- Claim-verification labels below distinguish `VERIFIED-EXTERNAL`,
  `VERIFIED-MANUSCRIPT-PROOF`, `VERIFIED-INTERNAL-CROSSREFERENCE`, and
  `NEEDS-CORRECTION`.

## 3. Phase A — bibliographic integrity

| Item | Result | Finding |
|---|---|---|
| `ChandgotiaMarcus2018` | VERIFIED | all fields match publisher/DOI evidence |
| `Chandgotia2019Lectures` | **MISMATCH** | source and content verified; title field differs from title page |
| `ChandgotiaThorat2026` | VERIFIED | authors/title/year/arXiv/class match |
| `BealBlockGorman2025` | VERIFIED | authors/title/year/arXiv/class match |

Totals: 3 verified, 1 mismatch, 0 not found.  The mismatch and correction are
documented field by field in the source ledger.

## 4. Phase B — citations and claim-to-source fidelity

### 4.1 Citation graph

- Four BibTeX keys; four distinct cited keys.
- Ten external citation occurrences; all ten inspected against source content
  (100%, exceeding the 30% minimum).
- Ghost/undefined citations: 0.  Dangling/uncited bibliography entries: 0.
- Context support: 10/10 supported.  The lecture-title mismatch is metadata,
  not a context-support failure.

### 4.2 Owner subtraction

| Prior owner/source | What P68 expressly leaves with that source | P68 residual scope | Verdict |
|---|---|---|---|
| [Chandgotia–Marcus](https://doi.org/10.2140/pjm.2018.294.41) | general hom-shift mixing/graph geometry | complete-bipartite two-sided classification, subgroup FD, pressure/periodic package | ADEQUATE |
| [Chandgotia lecture](https://nishantchandgotia.github.io/Teaching/2019_Jagiellonian/coursekrakow/l4.pdf) | checkerboard phase and complete-bipartite MME/product picture | explicit invertible dimer code and stronger linked contracts | ADEQUATE, after title fix |
| [Chandgotia–Thorat](https://arxiv.org/abs/2605.02226) | four-cycle-free finite-dependence obstruction | complete-bipartite phase/subgroup dichotomy outside that hypothesis | ADEQUATE |
| [Béal–Block Gorman](https://arxiv.org/abs/2509.24754) | one-sided/tree Hom-shift conjugacy via amalgamation | two-sided intrinsic translation-equivariant radius-one dimer code | ADEQUATE |

## 5. Phase C — internal integrity and computation disclosure

### 5.1 Formula/table/numeric consistency

Every displayed quantitative surface and the single manuscript table was
traced to a proof and, where applicable, to a deterministic control.

| Surface | Manuscript proof location | Control location/result | Verdict |
|---|---|---|---|
| two checkerboard phases/cocycle | `sections/2_phase_counts.tex:16–33` | finite restrictions use one global phase | CONSISTENT |
| all-finite-shape count and `h_top=1/2 log(mn)` | `sections/2_phase_counts.tex:35–64` | `code/verify_complete_bipartite.py:146–160`; six shapes, `(2,2)` and `(2,3)` | CONSISTENT |
| global vs merely local counts `13/25`, `12/25` | explanatory distinction at `sections/2_phase_counts.tex:66–70` | script lines 156–160 | CONSISTENT |
| phase full-shift model | `sections/2_phase_counts.tex:76–96` | packing logic reused by dimer control | CONSISTENT |
| `mn=rs` and radius-one inverse | `sections/3_conjugacy.tex:6–55` | script lines 162–173; `K_(2,6)↔K_(3,4)`, all 288 `2×2` torus points | CONSISTENT |
| example `X_(2,6) ≅ X_(3,4)` | `sections/3_conjugacy.tex:65–70` | same exhaustive finite control | CONSISTENT |
| finite-dependence equation `p=p^2` | `sections/4_finite_dependence.tex:9–47` | script lines 184–188 | CONSISTENT |
| pressure and unique full-action equilibrium | `sections/5_pressure.tex:11–76` | weighted `2×2` sum = 26450, script lines 181–182 | CONSISTENT |
| fixed points `0` or `2(mn)^[E:L]` | `sections/6_periodic_data.tex:8–24` | script lines 175–179 | CONSISTENT |
| proof-engine table | `sections/6_periodic_data.tex:33–48` | each row maps to the theorem/proof above | CONSISTENT |

The numeric values 13, 25, 12, 288, and 26450 occur only as finite regression
receipts/examples; no empirical inference or asymptotic theorem is inferred
from them.

### 5.2 Re-run and frozen-output comparison

The control was re-run in a temporary output file using the package command.
Byte comparison with `code/verify_complete_bipartite.out` returned `cmp=0`.

- Script SHA-256:
  `42c3e23e2cfd27618ccca28155be4f854010a05850fc7c1af2b1b8fe96aac8bd`
- Frozen output SHA-256:
  `918c56ef57b9c09ce27872e58a3e76667766351378e40b5d450d9cbced2a0bbf`
- Frozen result: all checks pass.

These computations are **proof-regression controls**, not experiments.  The
general infinite-system statements are proved in the manuscript and do not
depend on a finite cutoff.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

For P68 there is no experiment in the ordinary empirical sense, so the quoted
boundary is included to prevent the control rerun from being misreported as an
ARS experiment validation.

### 5.3 Declarations and provenance

| Item | Recorded state | Audit state |
|---|---|---|
| Authorship | anonymous internal draft | **UNRESOLVED — actual identities and contribution roles unavailable** |
| Funding | not specified | **UNRESOLVED** |
| Competing interests | none declared | `DECLARED_NONE_BUT_NOT_INDEPENDENTLY_VERIFIABLE` |
| AI assistance/disclosure | no specific statement supplied | **UNRESOLVED** |
| Data | no external dataset | NOT APPLICABLE to this theoretical paper |
| Code | deterministic standard-library control included | VERIFIED PRESENT |

No missing identity, funding, COI, or AI-use information is silently converted
to a pass.

## 6. Phase D — overlap/authorship screening

- Phase D1 denominator: 58 nonempty prose/theorem/proof paragraph-like blocks.
- Sample: 18 blocks = 31.0%.
- Coverage: abstract plus every major section (Introduction; Phase/counts;
  Conjugacy; Finite dependence; Pressure; Periodic data; Scope; Conclusion),
  with at least one block per section.
- Search form: quoted 8–12-word phrases after TeX normalization.
- Result: 18/18 `NO_EXACT_RELEVANT_MATCH`; irrelevant lexical coincidences
  were rejected.  Exact queries are recorded in the source ledger.
- Phase D2: `NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE`.

This is only a bounded textual-overlap screen.  Search engines may normalize
math, punctuation, accents, and hyphenation, and they do not index private or
all subscription material.  The result neither proves authorship nor certifies
originality.

## 7. Phase E — semantic claim registry and verification

The pre-existing registry uses schema `claim-registry/1.0`.  It contains 31
claims/candidates: 20 `HIGH-IMPACT`, 3 `RANDOM`, and 8 not selected.
`claim_registry_coverage.json` reports `candidate_unregistered_count=0`.

**semantic completeness=not_machine_detectable.**  Zero uncovered machine
triggers means the extractor's candidate patterns were registered; it cannot
prove that every semantically meaningful claim was detected.  This audit
checks all 20 HIGH-IMPACT claims plus all 3 RANDOM claims (23 total), exceeding
`min(10,total)`.

### 7.1 All HIGH-IMPACT claims

| Claim ID | Exact claim location | Support inspected | Verdict |
|---|---|---|---|
| P68-SEM-001 | Introduction `sections/1_introduction.tex:33–35` | count proof `sections/2_phase_counts.tex:35–64` | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-002 | Introduction `:36–39` | theorem and inverse `sections/3_conjugacy.tex:6–55` | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-003 | Introduction `:40–42` | theorem/proof `sections/4_finite_dependence.tex:9–47` | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-004 | Introduction `:43–44` | pressure `sections/5_pressure.tex:11–76`; fixed points `sections/6_periodic_data.tex:8–24` | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-005 | Phase lemma `sections/2_phase_counts.tex:16–24` | path-parity proof `:27–33` | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-006 | finite-shape proposition `sections/2_phase_counts.tex:35–41` | proof `:51–64`; regression lines 146–160 | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-007 | continuation of equation (2.1), `sections/2_phase_counts.tex:39–47` | same proof/control as SEM-006 | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-008 | phase full-shift proposition `sections/2_phase_counts.tex:76–85` | packing/unpacking proof `:87–96` | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-009 | classification theorem header `sections/3_conjugacy.tex:6–7` | complete proof `:19–55` | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-010 | classification item (1), `sections/3_conjugacy.tex:8–10` | construction and entropy necessity `:19–55` | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-011 | classification item (2), `sections/3_conjugacy.tex:11–12` | construction and entropy necessity `:19–55` | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-012 | radius-one contract `sections/3_conjugacy.tex:13–16` | local rules/inverse `:20–50`; finite regression | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-013 | FD theorem header `sections/4_finite_dependence.tex:9–11` | proof `:24–47` | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-014 | deterministic phase, `sections/4_finite_dependence.tex:13` | remote equal indicators and `p=p²`, `:25–34` | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-015 | no full support, `sections/4_finite_dependence.tex:14–16` | clopen phase support argument `:33–34` | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-016 | subgroup iff statement, `sections/4_finite_dependence.tex:17–20` | necessity/sufficiency `:36–46` | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-017 | pressure formula `sections/5_pressure.tex:11–16` | weighted pattern proof `:32–41` | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-018 | unique equilibrium mixture `sections/5_pressure.tex:18–25` | Gibbs/entropy/full-action proof `:43–75` | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-019 | product-law components in (5.2), `sections/5_pressure.tex:20–28` | dimer Bernoulli optimization `:43–75` | VERIFIED-MANUSCRIPT-PROOF |
| P68-SEM-021 | fixed-point formula `sections/6_periodic_data.tex:8–14` | quotient-phase proof `:17–24` | VERIFIED-MANUSCRIPT-PROOF |

### 7.2 RANDOM claims

| Claim ID | Location | Source/support | Verdict |
|---|---|---|---|
| P68-CAND-005 | Introduction roadmap `sections/1_introduction.tex:54–58` | named sections exist and contain stated results | VERIFIED-INTERNAL-CROSSREFERENCE |
| P68-CAND-006 | Conjugacy `sections/3_conjugacy.tex:72–74` | [Béal–Block Gorman](https://arxiv.org/html/2509.24754v1), method/category content | VERIFIED-EXTERNAL |
| P68-CAND-010 | Scope `sections/7_scope.tex:7–9` | [Chandgotia–Thorat](https://arxiv.org/html/2605.02226v2); `K_(m,n)` four-cycle hypothesis subtraction | VERIFIED-EXTERNAL |

## 8. Priority/nearest-neighbour audit

Three core advances were searched with four alternate-term queries each:
(i) product classification/dimer code, (ii) subgroup finite dependence, and
(iii) pressure/periodic data.  The full query ledger is in the companion file.

- Nearest neighbours are the four cited sources in the owner-subtraction table.
- No exact public statement of the combined residual package was located.
- Collision risk: **MEDIUM**.  The exact terminology is narrow, public indexing
  is incomplete, and absence from search results is weak negative evidence.
- Search-bounded conclusion only: no exact indexed collision was found through
  2026-08-26.  This is not a global novelty or priority certificate.
- Specialist exact-neighbour review remains required before release.

## 9. Seven-mode AI failure checklist

| Failure mode | Evidence examined | Status |
|---|---|---|
| 1. Implementation bug producing a claim | script source, exact rerun, frozen-output `cmp=0`; proofs do not depend on code | CLEAR for claim support |
| 2. Citation hallucination or miscitation | every BibTeX entry and 10/10 contexts | **SUSPECTED/CONFIRMED-METADATA-ISSUE**: one real source has an inaccurate title field; no ghost source |
| 3. Hallucinated experimental result | manuscript/control disclosure; no empirical data or experiment | CLEAR / NOT APPLICABLE |
| 4. Shortcut or model-metric reliance | theorem proofs use exact combinatorics/entropy, not learned metrics | CLEAR / NOT APPLICABLE |
| 5. Bug reframed as scientific insight | general arguments pre-exist finite controls; no code surprise is elevated | CLEAR |
| 6. Fabricated methodology/provenance | proof engines, script, frozen output, hashes, and limitations are present | CLEAR, subject to unresolved AI disclosure |
| 7. Frame lock / ignored nearest neighbour | alternate terminology and one-/two-sided categories searched; four owners subtracted | CLEAR WITH MEDIUM collision note |

## 10. Objective correction list

Required before a Stage 2.5 pass can be reconsidered:

1. In `references.bib`, change the `Chandgotia2019Lectures` title to the
   author-document title **“Lecture 4: An introduction to hom-shifts”**; rebuild
   and recheck the bibliography rendering.
2. Supply or explicitly disclose the unavailable author identities and
   contribution roles, funding statement, and AI-assistance statement.  If the
   information is genuinely not available at this internal stage, preserve the
   unresolved labels rather than asserting “none.”
3. Keep external release on hold pending a specialist exact-neighbour audit.

No theorem, proof, table, numeric value, or citation-context correction was
identified.  After item 1, the package could move from strict `FAIL` to
`PASS_WITH_NOTES` only if the unresolved declarations and specialist gate are
handled according to the release policy; this report itself does not grant
that later status.
