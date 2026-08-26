# P71 Stage 2.5 integrity and priority audit

Audit date: 2026-08-26 (UTC)  
Audited package: `papers/71-zip-shift-degree-pressure/`  
Release posture: **HOLD — no upload, contact, release, submission, or priority claim**

## 1. Disposition

**Overall Stage 2.5 verdict: FAIL (correctable bibliography/source-boundary
issues; no mathematical failure found).**

The strict protocol records one bibliographic `MISMATCH`: the authoritative
AIP record for *Zip Cellular Automata* has article number 015201, omitted from
the BibTeX entry.  In addition, the current-work boundary should expressly
identify (i) the 2025 S-expansiveness zip-shift preprint and (ii) a publicly
listed 2024–present project titled “Formalismo Termodinâmico para Mapas Zip
Shift.”  The project description is not theorem text and does not establish
prior publication, but it raises the pressure-package collision risk enough
that a generic “current work” sentence is insufficient for release review.

All 17 citation contexts, the citation graph, theorem/proof links, tables,
formulas, and deterministic controls pass this bounded audit.  No proof change
was identified.  This audit does not modify `main.tex`, `sections/`,
`references.bib`, PDFs, or pre-existing claim-registry sidecars.  Exact queries
and direct source URLs appear in
[SOURCE_SEARCH_LEDGER.md](SOURCE_SEARCH_LEDGER.md).

## 2. Audit frame and calibration

- Primary evidence order: DOI/publisher or arXiv record/full text; official
  institutional/author page; manuscript theorem/proof; deterministic control.
- Search snippets and third-party indexes were not accepted as final source
  evidence.
- Source support, mathematical proof support, and novelty screening are
  separate questions.
- “No exact theorem located” is bounded to the public searches documented here
  through 2026-08-26.
- No global novelty, authorship, plagiarism, or priority certificate is issued.

## 3. Phase A — bibliographic integrity

| Item | Result | Finding |
|---|---|---|
| `LameiMehdipour2025` | VERIFIED | all arXiv fields match |
| `MehdipourJangjooye2025` | VERIFIED | all arXiv fields match |
| `MartinsMattosVarao2026` | VERIFIED | published title/authors/journal/year/DOI/arXiv match |
| `Bowen1973` | VERIFIED | AMS metadata matches |
| `BarreiraSaussolSchmeling2002` | VERIFIED | publisher/DOI metadata matches |
| `MehdipourSalarinoghabiGibrim2026` | **MISMATCH** | AIP article number 015201 is omitted |
| `MehdipourLamei2026` | VERIFIED | publisher metadata matches |

Totals: 6 verified, 1 mismatch, 0 not found.  Field-level comparisons are in
the source ledger.

## 4. Phase B — citation and claim-to-source fidelity

### 4.1 Citation graph and contexts

- Seven BibTeX keys and seven distinct cited keys.
- Seventeen external citation occurrences; 17/17 inspected against relevant
  source content (100%, above the 30% minimum).
- Ghost/undefined citations: 0.  Dangling/uncited bibliography entries: 0.
- Context support: 17/17.  The missing AIP article number is a metadata
  completeness defect, not a claim-support defect.

### 4.2 Owner subtraction

| Prior owner/source | What remains with that source | P71 residual use/claim | Verdict |
|---|---|---|---|
| [Lamei–Mehdipour](https://arxiv.org/abs/2502.11272) | zip-space definition, sliding blocks, local-homeomorphism and periodic setting | degree potential and linked thermodynamic/rigidity/spectrum package | ADEQUATE |
| [Mehdipour–Jangjooye Shaldehi](https://arxiv.org/abs/2505.24647) | uniform `n`-to-one square entropy and intrinsic ergodicity | nonuniform degree fluctuations/profile pressure | ADEQUATE |
| [Martins–Mattos–Varão](https://arxiv.org/abs/2407.01828) | metric- and folding-entropy formulae for Bernoulli extended shifts | substitute equilibrium weights and connect to `P'`; no reattribution | ADEQUATE |
| [Bowen](https://doi.org/10.1090/S0002-9947-1973-0338317-X) | entropy notion for noncompact sets | exact degree-exponent computation for this model | ADEQUATE |
| [Barreira–Saussol–Schmeling](https://doi.org/10.1016/S0022-314X(02)00003-3) | adjacent digit-frequency multifractal method/context | direct future-symbol reduction retaining fibre multiplicity | ADEQUATE |
| [Zip cellular automata](https://doi.org/10.1063/5.0300898) and [zip encoding](https://doi.org/10.21494/ISTE.OP.2026.1442) | adjacent system-class directions | neither is presented as P71's pressure theorem | ADEQUATE after BibTeX completion |
| [Lamei–Mehdipour–Vargas 2025](https://arxiv.org/abs/2510.12980) | S-expansiveness, shadowing, factor/topological direction | no exact weighted-pressure/profile theorem found | **MISSING FROM CURRENT SOURCE BOUNDARY** |
| [UFV public thermodynamic-formalism project](https://nit.ufv.br/pesquisador/pouya-mehdipour/) | active same-family project; no theorem text available on page | collision signal only; cannot be owner-subtracted theorem-by-theorem | **DISCLOSURE REQUIRED BEFORE RELEASE** |

Ordinary natural-extension facts are correctly treated as infrastructure, not
as an isolated contribution.  Martins–Mattos–Varão Theorems A–B are explicitly
owner-subtracted in the introduction, pressure corollary, and scope section.

## 5. Phase C — internal integrity and computation disclosure

### 5.1 Formula/table/numeric consistency

| Surface | Manuscript proof location | Control/result | Verdict |
|---|---|---|---|
| local degree `d_tau(x)=k_(x_-1)` | `sections/2_model_extension.tex:23–38` | used consistently by all later identities | CONSISTENT |
| explicit natural extension and lifted potential | `sections/2_model_extension.tex:40–95` | coordinate inverse and invariant-measure argument are explicit | CONSISTENT |
| `P(t)=log sum_z k_z^(t+1)` and equilibrium `p_t` | `sections/3_pressure.tex:11–57` | script exact/finite identities and derivative checks | CONSISTENT |
| `P'` mean, `P''` variance, strict convexity | `sections/3_pressure.tex:23–57` | script lines 59–71; tolerances stated | CONSISTENT |
| `P(0)=log|S|`, `P(-1)=log|Z|` | `sections/3_pressure.tex:59–67` | direct substitution in finite sum | CONSISTENT |
| metric/folding bridge | `sections/3_pressure.tex:69–90` | source Theorems A–B plus displayed equilibrium weights | CONSISTENT / OWNER-SUBTRACTED |
| weighted fixed-point identity and `|Fix|=|S|^n` | `sections/4_periodic_rigidity.tex:6–32` | profiles `(1,3)`, `(1,2,3)`, `n≤5`, `t=-1,0,1,2` exactly checked | CONSISTENT |
| zeta `1/(1-uQ)` | `sections/4_periodic_rigidity.tex:34–55` | algebraically follows from periodic identity | CONSISTENT |
| fixed histogram `N_k=k m_k`, profile recovery | `sections/4_periodic_rigidity.tex:61–112` | repeated/nonrepeated profiles checked, script lines 73–78 | CONSISTENT |
| exact Bowen spectrum/Legendre form | `sections/5_multifractal.tex:23–155` | `(1,3)` interior controls, direct/Legendre difference `<1e-12` | CONSISTENT |
| endpoint/max formulas | `sections/5_multifractal.tex:157–168` | binary maximum check | CONSISTENT |
| examples `(1,3)` and `(2,2)` | `sections/6_examples.tex:3–38` | equal entropy/unequal pressure check | CONSISTENT |
| comparison table | `sections/6_examples.tex:40–55` | every row follows from preceding formulas | CONSISTENT |

The finite enumeration ranges and floating tolerances are disclosed.  They are
not used to infer the general theorem.

### 5.2 Re-run and frozen-output comparison

The package control was re-run to a temporary file.  Byte comparison against
`code/verify_degree_pressure.out` returned `cmp=0`.

- Script SHA-256:
  `6de6496c78ca610d955f7b6a4aa08d31f162b0c7ad3bfcbaf80bcb787119aab2`
- Frozen output SHA-256:
  `4ade498585b0750acea4b487dec11b7c19b2e322f8a5ef1d4262d6c4f39f2aba`
- Frozen result: all checks pass.

These are **proof-regression controls**, not experiments.  The full pressure,
equilibrium, periodic, profile-recovery, zeta, and Bowen-spectrum statements
are proved symbolically without a finite cutoff.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

There is no empirical experiment in P71; the quoted boundary prevents a
deterministic identity check from being misreported as ARS validation of an
experimental design.

### 5.3 Declarations and provenance

| Item | Recorded state | Audit state |
|---|---|---|
| Authorship | anonymous internal draft | **UNRESOLVED — identities and roles unavailable** |
| Funding | not specified | **UNRESOLVED** |
| Competing interests | none declared | `DECLARED_NONE_BUT_NOT_INDEPENDENTLY_VERIFIABLE` |
| AI assistance/disclosure | no specific statement supplied | **UNRESOLVED** |
| Data | no external dataset | NOT APPLICABLE to this theoretical paper |
| Code | deterministic standard-library control included | VERIFIED PRESENT |

No unavailable declaration is silently upgraded to “passed.”

## 6. Phase D — overlap/authorship screening

- Phase D1 denominator: 68 nonempty prose/theorem/proof paragraph-like blocks.
- Sample: 21 = 30.9%.
- Coverage: abstract and every major section (Introduction; Model/natural
  extension; Pressure; Periodic/rigidity; Multifractal; Examples; Scope;
  Conclusion), at least one block each.
- Search form: quoted 8–12-word phrases after TeX normalization.
- Result: 21/21 `NO_EXACT_RELEVANT_MATCH`.  Exact phrases are logged in
  `SOURCE_SEARCH_LEDGER.md`.
- Phase D2: `NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE`.

The public engine does not exhaust subscription/private/non-indexed texts and
may normalize formulas, punctuation, hyphens, and accents.  This phase is a
bounded overlap screen, not a plagiarism, authorship, originality, or priority
certificate.

## 7. Phase E — semantic claim registry and verification

The pre-existing `claim-registry/1.0` contains 42 items: 26 `HIGH-IMPACT`, 3
`RANDOM`, and 13 not selected.  Its coverage sidecar reports
`candidate_unregistered_count=0`.

**semantic completeness=not_machine_detectable.**  Candidate-trigger coverage
does not prove semantic completeness.  This audit checks all 26 HIGH-IMPACT
claims and all 3 RANDOM claims (29 total), exceeding `min(10,total)`.

### 7.1 All HIGH-IMPACT claims

| Claim ID | Exact location | Source/support inspected | Verdict |
|---|---|---|---|
| P71-SEM-001 | Introduction `sections/1_introduction.tex:27–30` | pressure theorem/proof `sections/3_pressure.tex:11–57` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-002 | Introduction `:29–33` | equations (3.3)–(3.5), proof `sections/3_pressure.tex:17–57` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-003 | Introduction `:34–36` | spectrum theorem/proof `sections/5_multifractal.tex:71–155` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-004 | Introduction `:37–40` | rigidity theorem/proof `sections/4_periodic_rigidity.tex:61–112` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-005 | Introduction `:41–45` | periodic proposition `sections/4_periodic_rigidity.tex:6–31` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-006 | continuation of weighted identity, Introduction `:43–45` | same periodic proof and exact control | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-007 | Introduction `:49–54` | natural extension proof `sections/2_model_extension.tex:53–95`; [Martins–Mattos–Varão](https://arxiv.org/html/2407.01828v2) Theorems A–B | VERIFIED-LOCAL+EXTERNAL; owner subtraction explicit |
| P71-SEM-008 | local-degree lemma `sections/2_model_extension.tex:23–30` | direct preimage proof `:32–38`; [zip definition source](https://arxiv.org/html/2502.11272v1) | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-009 | natural extension proposition `sections/2_model_extension.tex:53–62` | coordinate/invariant-measure proof `:65–95` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-010 | pressure formula `sections/3_pressure.tex:11–15` | Gibbs proof `:40–57` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-011 | unique equilibrium and weights `sections/3_pressure.tex:17–27` | Gibbs equality/entropy-rate proof `:40–57` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-012 | derivatives/strict convexity `sections/3_pressure.tex:29–37` | differentiation/variance proof `:54–57` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-013 | metric/folding corollary `sections/3_pressure.tex:69–89` | [Martins–Mattos–Varão Theorems A–B](https://arxiv.org/html/2407.01828v2) plus equilibrium substitution | VERIFIED-EXTERNAL+DERIVATION |
| P71-SEM-014 | weighted periodic theorem `sections/4_periodic_rigidity.tex:6–15` | word parametrization/factorization `:17–32` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-015 | zeta corollary `sections/4_periodic_rigidity.tex:34–49` | logarithmic-series proof `:52–55` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-016 | rigidity theorem header `sections/4_periodic_rigidity.tex:61–62` | full proof `:74–112` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-017 | conjugacy item `sections/4_periodic_rigidity.tex:63–65` | local-degree/fixed-point necessity and one-block construction `:74–100` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-018 | profile item `sections/4_periodic_rigidity.tex:66–67` | histogram recovery and construction `:74–100` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-019 | pressure-curve item `sections/4_periodic_rigidity.tex:68–69` | exponential-sum recovery `:102–112` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-020 | one-block conjugacy contract `sections/4_periodic_rigidity.tex:70–71` | explicit coordinate map `:86–100` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-021 | degree histogram `N_k=k m_k`, `sections/4_periodic_rigidity.tex:74–84` | fixed-point/local-degree argument same lines; regression script 73–78 | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-022 | spectrum theorem `sections/5_multifractal.tex:71–87` | future reduction and Carathéodory/type/entropy proof `:23–155` | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-023 | endpoints/full-entropy maximum `sections/5_multifractal.tex:157–168` | theorem specialization and binary control | VERIFIED-MANUSCRIPT-PROOF |
| P71-SEM-024 | current source boundary `sections/7_scope.tex:14–20` | cited AIP/APAM works support stated adjacency; [S-expansiveness preprint](https://arxiv.org/abs/2510.12980) and [UFV project](https://nit.ufv.br/pesquisador/pouya-mehdipour/) are additional exact-family neighbours | **PARTIAL — CURRENT-WORK BOUNDARY INCOMPLETE** |
| P71-SEM-025 | limitations/search posture `sections/7_scope.tex:22–31` | alternate-term search found no exact theorem; live project is disclosed only generically | SUPPORTED-WITH-REQUIRED-SOURCE-UPDATE |
| P71-SEM-026 | conclusion `sections/8_conclusion.tex:3–9` | synthesis of pressure, periodic, rigidity, and spectrum theorems | VERIFIED-MANUSCRIPT-PROOF |

### 7.2 RANDOM claims

| Claim ID | Location | Source/support | Verdict |
|---|---|---|---|
| P71-CAND-005 | Introduction `sections/1_introduction.tex:56–59` | [Bowen](https://doi.org/10.1090/S0002-9947-1973-0338317-X) and [BSS](https://doi.org/10.1016/S0022-314X(02)00003-3), source content | VERIFIED-EXTERNAL |
| P71-CAND-006 | roadmap `sections/1_introduction.tex:61–64` | named pressure/entropy section contains proofs | VERIFIED-INTERNAL-CROSSREFERENCE |
| P71-CAND-010 | pressure proof `sections/3_pressure.tex:82–89` | [Martins–Mattos–Varão Theorem A](https://arxiv.org/html/2407.01828v2) | VERIFIED-EXTERNAL |

## 8. Priority/nearest-neighbour audit

Three core advances were each queried under four alternate formulations:
(i) degree pressure/equilibrium/curvature, (ii) profile recovery/periodic
weights/conjugacy, and (iii) degree-exponent multifractals.  Exact queries are
in the source ledger.

- No public document was located that states the exact combined P71 formula,
  equilibrium, weighted periodic/zeta, full profile-recovery equivalence, and
  Bowen-spectrum package.
- Nearest published/preprint owners are correctly identified for zip
  formalism, uniform entropy, extended-shift entropies, Bowen entropy, and
  digit multifractals.
- A current [S-expansiveness zip-shift preprint](https://arxiv.org/abs/2510.12980)
  and an [active exact-family thermodynamic-formalism project](https://nit.ufv.br/pesquisador/pouya-mehdipour/)
  materially raise collision risk.
- Collision risk: **HIGH for the pressure portion**.  The project page does not
  expose theorem statements, so it neither verifies nor refutes exact
  collision.
- Search-bounded conclusion only: no exact indexed theorem package was found
  through 2026-08-26.  This is not a global novelty or priority certificate.
- Specialist exact-neighbour review is mandatory before release; release
  remains `HOLD`.

## 9. Seven-mode AI failure checklist

| Failure mode | Evidence examined | Status |
|---|---|---|
| 1. Implementation bug producing a claim | script source, exact rerun, frozen `cmp=0`; proofs independent of code | CLEAR for claim support |
| 2. Citation hallucination or miscitation | all seven records and 17/17 contexts | **SUSPECTED/CONFIRMED-METADATA-ISSUE**: one real article lacks identifier 015201; no ghost source |
| 3. Hallucinated experimental result | no experiment/data; controls explicitly finite regression only | CLEAR / NOT APPLICABLE |
| 4. Shortcut or model-metric reliance | exact finite sums, entropy inequalities, and topological arguments | CLEAR / NOT APPLICABLE |
| 5. Bug reframed as insight | general proofs precede/supersede numerical controls; no code-only theorem | CLEAR |
| 6. Fabricated methodology/provenance | proof packages, controls, hashes, source ledger present | CLEAR, subject to unresolved AI disclosure |
| 7. Frame lock / ignored exact-family work | alternate-term search found live thermodynamic project and S-expansiveness neighbour absent from bibliography | **SUSPECTED — source boundary must be widened; HIGH collision risk** |

## 10. Objective correction list

Required before a Stage 2.5 pass can be reconsidered:

1. Add AIP article number `015201` to
   `MehdipourSalarinoghabiGibrim2026` in `references.bib` and rebuild.
2. Add [Lamei–Mehdipour–Vargas 2025](https://arxiv.org/abs/2510.12980) to the
   current-work boundary and state precisely that its S-expansiveness,
   shadowing, and factor results are not P71's claim.
3. Identify the [UFV 2024–present thermodynamic-formalism project](https://nit.ufv.br/pesquisador/pouya-mehdipour/)
   in the audit/source-boundary disclosure.  Say explicitly that the public
   page contains a project objective, not theorem text, and do not infer
   non-collision from its silence.
4. Obtain a specialist exact-neighbour comparison focused on the pressure
   formula/profile-recovery contracts.  Preserve external `HOLD` until that
   gate is resolved.
5. Supply or expressly leave unresolved actual author identities/roles,
   funding, and AI-assistance disclosure.  Do not treat “none declared” as an
   independently verified COI result.

No theorem, proof, displayed formula, table value, or citation-context change
was identified.  The package cannot be upgraded by this report; after the
objective corrections, a separate gate may reassess it as `PASS_WITH_NOTES` or
`PASS`.
