# Papers 9–13 Creation, Review, and Integrity Process Record

Date: 16 August 2026 (Asia/Shanghai)  
Scope: Papers 9, 10, 11, 12, and the Paper 13 Technical Note  
Stage: ARS Stage 6 process summary (awaiting terminal acknowledgement)  
Batch technical verdict: **PASS — C0/M0/m0**  
Public release: **`PUBLIC_RELEASE_AUTHORIZED=false`**

## 1. Evidence boundary

This record is compiled from exact current workspace bytes, append-only review
reports, and the consolidated batch audit. The early raw dialogue is no longer
visible after long-session compaction. The initial prompt, turn numbers, and
exact intervention count therefore cannot be reconstructed honestly. The only
currently visible user text safe to quote verbatim is:

> “继续” (“continue”)

That message followed delivery of the Stage 5 five-paper batch and its audit,
and is treated as explicit consent to enter Stage 6. Earlier scope is described
only as artifact-backed inference, never as a fabricated quotation.

Primary upstream receipt:

- Batch audit: `papers/9-packet-separation/notes/papers9_13_batch_audit.md`
- SHA-256: `6aa915a9e85153957b269448ba23b56716c4f64d18e6b3c85f904d73b0001aea`
- Upstream hash graph: 65 current nodes, 255 edges, no self-edge, no cycle.

## 2. Papers and final deliverables

| Paper | Final position | PDF pages | PDF SHA-256 |
|---|---|---:|---|
| P9 | internally accepted article package | 21 | `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02` |
| P10 | internally accepted article package | 19 | `30c22eb8bbfd256cede958df86ce7f985889441a295d52e2ac5acfb3d59e2ce4` |
| P11 | internally accepted article package | 16 | `15d207568a61590852697511df2faf4cb06fd06047574c3dc3413e352c14840d` |
| P12 | internally accepted; `STANDALONE_PASS` retained | 18 | `9d6747e9f33c6ab3724beb35daedbb0efaff73691ed344374366f2392541ec15` |
| P13 | internally accepted **Technical Note** | 15 | `4082ca13a6daadb72ccc30a34fc5160f5920247d3fa3436562349ccc5a9c43c2` |

Each `paper/` directory contains exactly six ordinary files: README, TeX,
BibTeX, two native TikZ sources, and one PDF. There are no symlinks,
auxiliaries, second PDFs, or research-source PDFs in those packages.

Paper 13's independent substantive-weight finding remains
`NOTE_OR_MERGE`, `STANDALONE_PASS=false`, `C0/M1/m0`. That Major explains the
Technical Note disposition; it is not erased by this record.

## 3. Evidence-aligned stage chronology

| Stage | Main input | Output and decision | Iteration or correction | Final gate |
|---|---|---|---|---|
| 1. Batch intake and candidate freeze | P9–P13 protocols, candidate locks, predecessor boundaries | Five owner-typed projects; delivery consolidated at the batch boundary | Original prompt unavailable; no quotation invented | Historical `pipeline_state.md` files remain gate-time snapshots |
| 2. Phase-1 design relock | methodology, devil/domain, and source-feasibility reviews | All five Phase-1 packages ultimately closed | P9 two states; P10 two; P11 two; P12 initial/v1/v2; P13 initial/v1 | all final `C0/M0/m0` |
| 3. Phase-2 source and precedent work | retained PDFs, owner dictionaries, bounded searches | source, terminology, ownership, and novelty ceilings | searches retained `SUPPORTED_WITHIN_SEARCH` wording | no bounded search became an absolute priority claim |
| 4. Phase-3 proofs and controls | source-locked claims | stable proofs, counterexamples, and deterministic controls | P12 v2/v3/v4; P13 initial and v2 corona packages | mathematics passed; standalone adjudicated separately |
| 5. P13 control remediation | first implementation and mutation probes | replacement manifest `26a41e…094c2` | first implementation failed because token/self-comparison oracles were not independently fail-closed; one bounded repair followed | 176/176 tests, 12 CSVs, 2,665 rows, 67/67 negatives, PASS |
| 6. Publication disposition | proof, source, control, and standalone reviews | P9–P12 article packages; P13 Technical Note | P12 v4 closed its routine-reduction Major; P13 retained its Major | `PASS_TO_TECHNICAL_NOTE`, no false standalone claim |
| 7. Formal Route evaluation | stable proofs and controls | 40 Route-A YAMLs | 25 exploratory and 15 rejected | 120 A2–A4 coordinates fail; Route B count zero |
| 8. Composition and citation preflight | proof/Route tuples and source ceilings | five blueprints; English bodies plus independently written Simplified-Chinese abstracts | structure, claim order, traces, and declarations were frozen first | blueprints added no mathematical evidence |
| 9. Manuscript review and freezes | TeX, Bib, figures, PDF | five exact six-file packages | P9 C1/M8 initial review then acceptance; P12 Freeze 1→2→Correction→count relock; P13 Freeze 1 C0/M2/m1→Freeze 2→status relock | all current manuscript packages technical `C0/M0/m0` |
| 10. Bounded P12 corrections | P12 Review Freeze 2 | corrected Bib/PDF and append-only citation→peer→release chain | Stacks title corrected to “Colimits of spaces”; Han receipt corrected to 353 body + 32 keywords = 385 | both historical m1 findings closed transparently |
| 11. Citation, peer, and release closure | final manuscript tuples | per-paper citation, peer, and technical release reports | P11–P13 append-only status relocks | current citation graphs and technical gates PASS |
| 12. Consolidated batch audit | five current scholarly tuples and status files | one exact-byte package/PDF/source/Route/control/hash-graph receipt | closed the P9 report edge, P11/P12/P13 status receipts, and graph-orientation language | `PASS — C0/M0/m0`; public release remains false |

## 4. Minimum evidenced iteration counts

These are named artifact states, not inferred dialogue turns.

| Paper | Design states | Proof/disposition states | Manuscript/finalization states |
|---|---:|---:|---:|
| P9 | 2 | 1 stable proof package | 2: initial manuscript and accepted re-review |
| P10 | 2 | 1 stable proof/control package | at least 2; one final spacing-only relock is explicit |
| P11 | 2 | 1 stable proof/control package | at least 2 citation states plus one status-relock chain |
| P12 | 3 | 3: v2/v3/v4 | 4: Freeze 1, Freeze 2, Correction, count relock |
| P13 | 2 Phase-1 and 3 control-design states | 2 standalone and 2 control-implementation states | 3: Freeze 1, Freeze 2, status relock |

## 5. Integrity totals

| Item | Total |
|---|---:|
| Unit tests | 399/399 |
| CSVs | 53 |
| CSV body rows | 7,709 |
| Explicit negatives | 86 |
| Route-A | 40 |
| Exploratory / rejected | 25 / 15 |
| Route-B | 0 |
| Locally retained research PDFs | 32 |
| Reused audited manifestations | 3 |
| PDF/preflight pairs | 35 |
| Total manuscript PDF pages | 89 |
| Fonts | 39, all embedded/subset/Unicode |

All five retained manuscript PDFs are A4 PDF 1.5, unencrypted,
attachment-free, and raster-image-free; Ghostscript parsing passes. Research
PDFs remain only under `notes/sources/` and do not enter any `paper/` package.

## 6. Major direction corrections

1. **Standard ingredients cannot be repackaged as standalone work.** P12 v4's
   same-carrier standardization/H1 diagonal closed its earlier routine-reduction
   Major. P13's corona package remained an instance of a generic isometric
   diagonal lemma after subtraction, so it was honestly routed to a Technical
   Note.
2. **Controls need independently fail-closed oracles.** Correct CSV bytes did
   not rescue P13's first implementation when detectors merely looked up tokens
   or compared one formula with itself. The control package was repaired before
   downstream use.
3. **Owner and type checks outrank narrative convenience.** Packet
   transitivity, same-carrier ownership, morphism variance, and Route owners
   were versioned and relocked rather than papered over.
4. **Metadata is integrity evidence.** P12's Stacks title and Han-count
   convention were retained as historical m1 findings and closed through
   append-only reviews.
5. **Report edges must remain acyclic.** P9's transient log is historical;
   P13's final README bytes are bound by the downstream batch report rather
   than by a self- or reverse-hash construction.

## 7. User decisions and attributable value

The compacted session summary---not a surviving verbatim turn---records the
five-paper scope, broad automation, and the no-Git/no-public-sync constraint
before audit closure; frozen artifacts corroborate the batch scope and release
hold. “继续” remains the only currently visible user text quoted verbatim.
Early instructions are unavailable, so agent-discovered errors, mathematical
repairs, and review judgments are not reassigned to the user.

Observable human value-add lies in scope, autonomy, continuation, and release
boundary choices. Proof development, source verification, defect discovery,
relocking, and technical closure are attributed to the AI/review workflow
unless a fuller raw transcript later establishes otherwise.

## 8. Collaboration Depth Trajectory (advisory)

This uses Wang–Zhang rubric v1.0. It does not evaluate manuscript quality and
never blocks progression. Scores are provisional with low-to-medium confidence
because early raw turns are unavailable.

| Dimension | Score | Observation |
|---|---:|---|
| Delegation Intensity | 8/10 | whole categories were delegated rather than micro-edited |
| Cognitive Vigilance | 4/10 | strong workflow gates exist, but visible user challenges do not |
| Cognitive Reallocation | 3/10 | no visible original synthesis, counterargument, or theorem-level judgment |

**Zone 2 — Mid, automation-dominant.** Zone 3 requires all three dimensions at
seven or above; only high delegation is evidenced. Zone 1 is also excluded
because AI use was extensive. A future auditable Zone-3 pattern could include
one human challenge to a central theorem or citation at each gate, a written
human rationale for article-type and release decisions, and one original
synthesis after each major correction.

## 9. AI Self-Reflection

### 9.1 Behavioral summary

The AI used high parallelism, exact locks, and append-only reviews. Independent
reviewers repeatedly prevented premature PASS decisions. The downside was
excessive status-pointer and hash-edge relocking near the end. This reflection
is produced by the same AI system it evaluates and is not independent evidence.

### 9.2 Metrics and sycophancy risk

| Metric | Result |
|---|---|
| DA concession rate | `UNMEASURED`; compacted logs do not preserve a reliable denominator |
| Consecutive concessions | `UNMEASURED` |
| Skipped checkpoints | `UNMEASURED`; broad automation compressed nonmandatory prompts to the batch boundary |
| Visible user overrides | 0 |
| Visible health alerts | 0; the full historical total is `UNMEASURED`, and zero visible alerts do not prove no risk |
| Intent-mode transitions | `UNMEASURED`; the visible Stage-5→6 move is a stage transition, not evidence of an exploratory↔goal-oriented mode change |
| Cross-model disagreements | cross-model was not enabled |

Sycophancy risk is therefore **UNMEASURED / requires human reading**, not LOW.
Independent audits repeatedly caught real defects, but that fact cannot replace
raw-dialogue concession statistics.

### 9.3 What the AI got wrong

- The initial P12 bibliography used “Topological colimits” for Stacks Tag
  0B1W, and earlier citation PASS reports missed it.
- P12's Chinese receipt used `Script_Extensions=Han`, counting 17 punctuation
  characters and reporting 370 instead of 353 body characters.
- P13 Freeze 1 had six-key trace, parent-README status, and Han-count defects.
- P13's first control implementation admitted tautological/token-detector
  oracles and required bounded remediation.
- A P12 controls audit had a duplicate-run orchestration incident. It was
  cleaned without result drift but exposed runner-coordination weakness.
- P13 status pointers caused avoidable relock churn near terminal closure.
- The first batch-audit graph paragraph called the new report a sink under a
  `referrer→prerequisite` convention; machine review corrected it to a source.

### 9.4 Seven-mode failure audit log

No uniform batch-wide contemporaneous ARS v3.20 Stage-2.5/4.5 seven-mode log
survives. The final citation audits for P11--P13 contain per-paper seven-mode
tables, whereas P9--P10 do not. The table below is only a Stage-6 retrospective
synthesis and does not replace the missing formal records.

| Mode | Retrospective assessment | History and resolution |
|---|---|---|
| 1. implementation bug passing self-review | CLEAR | P13 control oracles were suspected by mutation probes; replacement implementation and independent rerun closed the issue |
| 2. hallucinated citation | CLEAR | graphs close; P12's real-source metadata m1 was corrected and relocked |
| 3. hallucinated experimental result | CLEAR | every finite result is CSV/manifest-bound; P13's first manifest is excluded from evidence |
| 4. shortcut reliance | CLEAR / theoretical boundary | finite controls are explicitly diagnostic and never promoted to general theorems |
| 5. bug reframed as insight | CLEAR | the oracle defect was repaired, not narrated as a contribution |
| 6. methodology fabrication | CLEAR | test, row, negative, build, and PDF receipts match stable bytes |
| 7. early frame-lock | CLEAR at final scope | proposed standalone strengthenings were downgraded when prior-art or reduction reviews required it; P13 became a Technical Note |

No user override is recorded.

## 10. Collaboration Quality Evaluation (provisional)

| Dimension | Score |
|---|---:|
| Direction Setting | 88 |
| Intellectual Contribution | 45 |
| Quality Gatekeeping | 78 |
| Iteration Discipline | 80 |
| Delegation Efficiency | 92 |
| Meta-Learning | 47 |
| **Equal-weight overall** | **72/100 — Good** |

The observable strengths were clear batch scope, efficient whole-category
delegation, a no-Git/no-public-sync boundary, and willingness to continue until
exact-byte closure. Missed opportunities were visible human sampling of core
proofs and citations, a human rationale for P13's article type, and explicit
user-authored lessons after correction cycles.

## 11. Reusable lessons

- Correct artifact bytes do not imply correct control oracles; mutation probes
  are mandatory.
- Standalone weight must be reviewed after subtracting prior papers and standard
  lemmas.
- `pipeline_state.md` is a historical gate snapshot; later exact reports define
  current status.
- README, citation, peer, release, and batch reports need an acyclic binding
  order.
- Local source-PDF retention and public-payload exclusion are separate gates;
  no public-safety claim is possible without real Git/archive/fresh-clone
  checks.
- Chinese count receipts must freeze the Unicode property, text boundary, and
  whether keywords are included.

## 12. External release gates and terminal state

Human or real publication-system decisions remain for author order,
affiliations, correspondence, ORCID, CRediT, funding, conflicts,
acknowledgments, ethics/consent applicability, and final AI/tool disclosure;
immutable identities or approved self-contained replacements for unpublished
companions; venue/article type, template, citation style, license,
accessibility, and submission-day DOI/retraction/correction/policy checks; and
real Git/index/LFS/archive/upload/attachment/hidden-path/fresh-clone source-PDF
exclusion.

This process record performs no Git, commit, push, archive, or upload. Stage 6
remains `in_progress` after delivery until the user replies “完成”, “确认”,
“结束”, “done”, “confirm”, or an unambiguous equivalent accepting the
deliverables.
