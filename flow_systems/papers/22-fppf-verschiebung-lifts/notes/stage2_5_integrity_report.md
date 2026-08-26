# P22 Stage-2.5 integrity report

Audit date: **2026-08-24**  
Integrity closure: **2026-08-25T02:11:47Z**  
Mode: **academic-pipeline / full / Stage 2.5 Mode 1**  
Checkpoint decision: **PASS — MANDATORY STAGE-2.5 CHECKPOINT COMPLETE**

## Exact audit target

| Artifact | SHA-256 |
|---|---|
| manuscript source | `5976642a43907a3e01abdb586e9188c697d4a07e7137330a8f285538caaa02fc` |
| bibliography | `bd03813691db911316b18620ee4a1d212ac284fce7fb79af9f1b1cbc7ea71093` |
| compiled PDF | `b106aa48ca5b3906a47691d035c29ed640aca378ed24adb51f29f83264daec3d` |
| Deninger v1 source PDF | `19870cbdddbde82526939eb801c2ce14707dc7b48e54a7bc81f4a84400505002` |
| verified Material Passport | `f395557fe703fbbd62af60e7b5c2afcb63ff1c3db1c2299d0e7dbd73ef86b52c` |
| experiment-intake closure receipt | `f3a57bc82aa9c90f57b546376f026341e0560cfce8a1a1b0818dad7b20abbcb5` |

The corrected manuscript and PDF are current and mutually consistent.  The
scholar supplied the previously missing experiment-intake declaration on
2026-08-25, so the last fail-closed structural condition is now satisfied.

## Phase verdicts

| Phase | Coverage | Verdict | Main result |
|---|---:|---|---|
| A. Reference existence and metadata | 3/3 references; 100% | **PASS** | All identities, metadata, locators, and source owners verified.  No official withdrawal/retraction banner was observed within the checked records. |
| B. Citation-context fidelity | 18/18 contexts; 100% | **PASS after correction** | One initial MEDIUM compound attribution and one MINOR equation-description issue were narrowed and independently rechecked; final support is 18/18. |
| C1. Statistical/data accuracy | 0 registered surfaces | **NOT APPLICABLE** | The scan was executed; the denominator is genuinely zero. |
| C2. Internal consistency | 10/10 families | **PASS** | Abstracts, theorems, proofs, controls, conclusion, and declarations agree. |
| C3. Figure/table fidelity | 0 figures, 0 tables, 0 captions | **NOT APPLICABLE** | The artifact scan was executed; no Figure Package is needed. |
| C4. Experiment disclosure/provenance | 0 experiment-backed claims; 1/1 declaration present | **PASS** | The scholar explicitly confirmed `no_experiments_declared`; empty provenance and alignment populations are consistent. |
| D1. Originality | 22/71 paragraphs = 30.99%; 7/7 sections | **NO BLOCKING SIGNAL WITHIN SAMPLE** | 15 ORIGINAL, 1 COMMON_KNOWLEDGE, 6 PARAPHRASE, 0 CLOSE_MATCH, 0 VERBATIM. |
| D2. Self-plagiarism | author identity absent | **NOT EXECUTED / ADVISORY** | `AUTHOR TO CONFIRM` prevents an author-aware prior-work corpus. |
| D3. AI-writing heuristics | 6 indicators checked | **PASS WITH LIMITATION** | 0/6 triggered; this is not an authorship classifier. |
| E. Claim verification | 39 registered; 17 high-impact selected | **PASS** | 26 shared evidence rows cover 17/17 selected claims; 17 VERIFIED, 0 distorted, 0 unverifiable. |
| E4. Scope alignment | 17/17 selected claims | **PASS** | No `SCOPE-BROADENED` row; finite-flat and source-correction branches were explicitly planned comparators. |
| E5. Primacy/absence wording | 1 bounded absence statement | **SUPPORTED_WITHIN_SEARCH** | Databases/surfaces, query families, boundaries, date, and nearest prior result are documented; the paper expressly disclaims global priority. |
| E6. Claim-strength drift | first-pass audit | **SKIPPED AS REQUIRED** | `status=skipped_no_revision_evidence`, null bundle hash, and empty findings are persisted and schema-valid. |

## Corrections completed during this gate

| ID | Initial severity | Location | Correction and re-verification |
|---|---|---|---|
| `IL-MEDIUM-1` | MEDIUM | Introduction, source question | Separated Deninger's constructed Frobenius maps from the open fp/fppf Verschiebung lifting question.  **CLOSED.** |
| `IL-MINOR-1` | MINOR | Section 2, equation (20) locator | Replaced the overbroad Witt-addition description with the exact formula `V_N(f)(T)=f(T^N)`.  **CLOSED.** |

The correction round changed no theorem, proof, scope, bibliography entry, or
roadmap classification.  It was rebuilt into a 12-page A4 PDF with zero
undefined citations/references, zero overfull boxes, zero missing glyphs, and
zero fatal errors.  Final pages 1, 3, and 12 were visually inspected.

## Closed declaration issue

| ID | Initial severity | Category | Resolution |
|---|---|---|---|
| `IL-SERIOUS-1` | SERIOUS / gate-blocking | Experiment provenance C4-D7 | **CLOSED 2026-08-25.** The scholar replied “确认” to the exact preceding statement that P22 did not run or rely on any experiment of the author's own.  The Material Passport now records `no_experiments_declared`, `declared_by: scholar`, and `2026-08-25T02:11:47Z`; provenance and alignment arrays are empty and pass the declaration-symmetry checks. |

The paper text, proof blueprint, and empty empirical surface were not used to
infer or sign the declaration.  Closure is based on the scholar's explicit
response to the full no-experiment statement, recorded in
`stage2_5_experiment_intake_closure.md`.  There are now **no active integrity
issues**.

## Claim and evidence receipt

- `claim-registry/1.0`: 39 exact UTF-8 byte-bound claims; artifact SHA-256
  `6a518f306da618318c83b25fc6abf61f00f1e4b922239ca109f9ec620e3a15cf`.
- `claim-registry-coverage/1.0`: deterministic build and exact-input replay
  PASS; artifact SHA-256
  `0815624b0dec21557191cced4986aa43fd6c4bd3695e7eabb1d8050ea2aa114b`.
- Six mechanically open raw-LaTeX candidates were adjudicated as two macro
  parameter false citations plus four physical-line/formula fragments.  The
  detector remains explicitly `semantic_extraction_coverage=not_machine_detectable`.
- `evidence-row/1.0`: 26 rows; source-bound replay and pagination validation
  PASS; artifact SHA-256
  `6c0eebf0ba0222d8795fd50cd4f9d620dce4d47e9409f61eaab206c21f68c647`.
- Claim-strength drift sidecar: schema PASS; SHA-256
  `fdde67f3ed592656a775c0b12dd5a5b3ab8cdd6a9e66e8e2a5a6655ef6b58b0e`.

These contracts prove exact binding and replay conformance.  They do not by
themselves prove semantic extraction completeness or mathematical truth; the
independent proof/source audits remain part of the evidence chain.

## Seven AI-research failure modes

Modes 1--7 are all **CLEAR**: no implementation result exists to hide a bug;
citations are real; no experiment result is reported; no model/data shortcut
exists; no anomaly is reframed as novelty; the stated proof method is visibly
executed; and the RQ expanded from the `N=2` gate only after evidence while
retaining all site/scope controls.  None is `SUSPECTED` or `INSUFFICIENT
EVIDENCE`.  This checklist does not waive D7 or certify the proof against all
ordinary mathematical errors.

## PDF/source-access advisory

An earlier exact-hash `pdf_read_preflight/1` run passed with page counts
31/31/31.  A later rerun in a Python environment without `pypdf` emitted
`UNAVAILABLE`; this is preserved as an advisory rather than rewritten to
PASS.  Exact page locators were also checked in local extracted text and
official HTML, so reference verification did not depend on the unavailable
rerun.

## RAISE and readiness advisories

RAISE is `principles_only` because P22 is primary theoretical research.
Against the complete process-documentation ideal, all four principles remain
conservatively `fail`: named human oversight/adjudication, detailed AI
metadata, a populated reproducibility lock, and per-tool validation are
incomplete.  Under the primary-research policy this contributes **WARN**, not
a terminal block, and is not a claim of official RAISE compliance.

The paper also remains a research draft rather than a submission package:
author name, author contributions, funding, competing interests, author-aware
self-plagiarism screening, and public-material availability are still to be
confirmed.  No venue-readiness claim is made.

## Roadmap disposition

The exact governing files are the two user-designated roadmap documents:

- Route A SHA-256:
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- Route B SHA-256:
  `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`

```text
ROUTE_A_EVALUATION=NOT_TESTABLE
A0_A1_A2_A3_A4_TUPLE=NOT_ASSIGNED
ROUTE_A_ADVANCEMENT=NONE

ROUTE_B_INVOCATION_ALLOWED=false
ROUTE_B_ENTRY_AUTHORIZED=false
ROUTE_B_STATUS=ROUTE_B_NOT_TESTABLE
B1_B2_B3_B4_B5_TUPLE=NOT_ASSIGNED
HILBERT_POLYA_CLAIM_ALLOWED=false

GATE_A=NOT_REACHED
GATE_B=NOT_REACHED
GATE_C=NOT_REACHED
GATE_D=NOT_REACHED
GATE_E=NOT_REACHED
```

P22 is a reusable proved algebraic obstruction, but it has no dynamical,
operator, trace-formula, or completed-zeta inputs and earns no Route or Gate
credit.

## Mandatory checkpoint

Stage 2.5 is **PASS** and stops here as required.  Stage 3 does not start
automatically; it requires a separate user checkpoint decision.  Submission,
public release, author contact, Git action, and Route advancement remain
unauthorized.
