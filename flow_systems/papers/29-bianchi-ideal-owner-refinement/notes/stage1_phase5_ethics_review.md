# P29 Stage 1 Phase 5 Ethics and Research-Integrity Review

Review date: **2026-09-02 UTC**  
Seat: **`R10-P5-ETH`**  
AI-assisted research-integrity verdict: **`CONDITIONAL`**  
Calibration: **`NOT_CALIBRATED`**

## Scope and input binding

This is a read-only Phase-5 review of `stage1_phase4_research_report.md`,
SHA-256
`ea2454415ec3ee9455bb10cfa702910d48bb9cb66b091c89d1ca73911cbcc112`.
The frozen Phase-4 manifest, checkpoint, Phase-2 verification MD and TSV, and
Route-A/Route-B boundary documents were used only as closed-corpus context.
No web search, new retrieval, scientific execution, source relabeling, report
revision, or institutional-authority resolution was performed.

The verdict covers AI-assisted research integrity only. It is not scientific
validation, locator-level citation clearance, human-subjects clearance,
publication acceptance, or Route evaluation.

The seat used the current Codex model family and was procedurally isolated from
the other Phase-5 first-pass seats. That separation is not evidence of
statistically independent errors. The judgments below are categorical and
`NOT_CALIBRATED`.

## Seven-dimension assessment

| Dimension | Status | Evidence and boundary |
|---|---|---|
| 1. AI disclosure and transparency | `WARN` | The report's **AI Disclosure and Verification Limitation** identifies AI-assisted literature search, source verification, synthesis, and drafting; it also acknowledges `anchor:none` and the lack of passage-level verification. The tool/model name, version or dated configuration, the human reviewer identity/responsibility, and the stages of human sign-off are not specified. |
| 2. Attribution and reference integrity | `WARN` | The report cites and lists all 22 frozen IDs and uses no direct quotations. The Phase-2 records support source identity, metadata, and bounded claim fitness, but not exact claim-to-passage fidelity. The report states this limitation. No frozen evidence indicates fabrication; absence of locators is not fabrication. |
| 3. Dual-use screening | `PASS` | Risk level: **None**. The report is a pure-mathematics evidence synthesis and certificate-design program. It supplies no concrete harm-enabling method, vulnerability, surveillance mechanism, weaponizable procedure, or personal-data workflow. |
| 4. Fair representation | `PASS` | The report distinguishes direct prerequisites, adjacent methods, background sources, a preprint, monographs, and correction-bound records. It does not discuss human communities or vulnerable populations and uses no stigmatizing framing. Competing mathematical roles are bounded rather than dismissed. |
| 5. Data ethics and reproducibility | `PASS_WITH_LIMITS` | The report uses frozen project artifacts and cited literature, reports no personal data, dataset collection, scraping, or scientific computation, and binds its report and source ledgers by hash. Reproducibility of the AI contribution is incomplete because no model/version/date or prompt/procedure record is named in the report. |
| 6. Funding and conflicts of interest | `PASS_WITH_LIMITS` | **Author Declarations** state `Funding: None` and `Competing interests: None declared`. The frozen verification ledger separately records source-level COI as `UNKNOWN_NOT_AUDITED` for 22/22 sources; the report does not turn that absence of audit into a clean source-level finding. |
| 7. Human-subjects boundary | `NOT_APPLICABLE` | **Author Declarations** state that human subjects and personal data are not applicable; the executed method is literature synthesis over mathematical objects and project artifacts. No recruitment, interaction, intervention, identifiable data, or human-related dataset is reported. This review makes no human-subject authorization claim and resolves no institutional pathway. |

## Findings and required disposition

### `P29-ETH-001` — AI disclosure is present but not sufficiently specific

- Severity: **Conditional**.
- Evidence: **AI Disclosure and Verification Limitation**, first paragraph,
  names the task classes but only says “AI-assisted research tools” and
  “Human oversight was applied throughout.” The following paragraph correctly
  narrows verification to metadata, abstracts, authorized scope notes, the
  verification ledger, and synthesis.
- Condition before delivery: record the exact AI product/model family and
  version or dated configuration; identify which tasks it performed; identify
  the responsible human reviewer and the actual approval stages; and state the
  verification limitation in the same disclosure so that “all findings were
  verified” cannot be read as claim-to-passage clearance.
- Boundary: this condition authorizes no Phase-6 edit. It is an actionable item
  for a later authorized revision.

### `P29-ETH-002` — locator and retraction limits must remain visible

- Severity: **Advisory**.
- Evidence: **Executed Methodology**, **Limitations and Future Work**, and the
  disclosure section all state that exact theorem/page/section locators were
  not frozen. The Phase-2 verifier records all 22 retraction fields as
  `NOT_CHECKED` and binds P29-S06 to the P29-S07 correction.
- Action: any future theorem-level source-finalization pass should preserve the
  S06/S07 binding, inspect exact source passages, and report structured
  retraction status separately. Until then, retain the current warnings and do
  not advertise retraction-clean or locator-cleared status.

### `P29-ETH-003` — no integrity block found

- Severity: **No action**.
- Evidence: 22/22 frozen references have `VERIFIED` existence outcomes; no row
  is `FABRICATED` or `UNVERIFIABLE`; no direct quotation appears; AI use is
  disclosed; funding and competing-interest declarations are present; and the
  work involves no human-subject activity.
- Disposition: the record contains no evidence of fabricated references,
  plagiarism, systematic source misrepresentation, undisclosed AI use, or
  concrete harm-enabling content. A `BLOCKED` verdict is not warranted.

## AI-disclosure verification

| Check | Result |
|---|---|
| Disclosure statement present | **Yes** |
| AI task scope stated | **Yes, at task-class level** |
| Scope accurate against frozen pipeline artifacts | **Broadly yes, only when read with the adjacent limitation paragraph** |
| Tool/model and version/date stated | **No** |
| Human oversight responsibility and checkpoints stated | **No; only a generic assertion** |
| Hallucination/locator limitation acknowledged | **Yes** |
| AI-generated scientific data presented | **No** |

## Attribution and reference-integrity accounting

- Frozen reference inventory: **22**.
- Citation-list/inventory closure: **22/22** IDs cited and **22/22** listed.
- Source-identity outcomes: **22/22 `VERIFIED`**.
- Metadata: **22/22** matched after bounded normalization; one title repair is
  `RESOLVED_POST_VERIFICATION`, while two external-display discrepancies remain
  documented.
- Independent second-source checks: **9/22**.
- Peer-reviewed journal/correction records: **17/22**.
- Phase-4 claim intents: **8**.
- Locator-level claim-to-passage clearance: **0/8** claim intents; all 22 prose
  citation pairs carry `anchor:none`.
- Direct quotations: **0**.
- Structured live retraction checks: **0/22**; all rows remain `NOT_CHECKED`.
- Source-level COI audits: **0/22**; all rows remain
  `UNKNOWN_NOT_AUDITED`.
- Clearly identifiable author self-citations: **0/22**; no self-citation-rate
  flag is triggered from the frozen list.
- Frozen-record fabrication findings: **0**. This is identity/metadata closure,
  not full-text claim-faithfulness clearance.

## Responsible-use and human-subjects boundary

Dual-use risk is **None**, so no Responsible Use statement is required by this
review. The work reports no human-subject activity. No authority context was
selected, replayed, or inferred, and no institutional authorization is claimed.

> **Human-subjects boundary:** This review does not authorize recruitment,
> consent, access to identifiable data, intervention, or data collection.

## Ethics decision log

| Item | Verdict | User decision | Reasoning |
|---|---|---|---|
| `P29-ETH-001` | `CONDITIONAL` | `PENDING`; Phase-6 revision is not authorized | No user adjudication has yet been recorded. |

## Closed ledger

```text
PAPER=P29
SEAT=R10-P5-ETH
REPORT_SHA256=ea2454415ec3ee9455bb10cfa702910d48bb9cb66b091c89d1ca73911cbcc112
AI_ASSISTED_RESEARCH_INTEGRITY_VERDICT=CONDITIONAL
DUAL_USE_RISK=NONE
HUMAN_SUBJECT_ACTIVITY=NONE_REPORTED
HUMAN_SUBJECT_AUTHORIZATION_CLAIM=NONE
REFERENCE_IDENTITY_CLOSURE=22/22_VERIFIED
CLAIM_TO_PASSAGE_CLEARANCE=0/8
REVIEW_CALIBRATION=NOT_CALIBRATED
MODEL_DIVERSITY=SINGLE_CODEX_FAMILY
INDEPENDENCE=PROCEDURAL_ONLY
NEW_RETRIEVAL=NOT_RUN
REPORT_EDIT=NOT_RUN
```
