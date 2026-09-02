# P32 Stage 1 Phase 5 Ethics and Research-Integrity Review

Review date: **2026-09-02 UTC**  
Seat: **`R10-P5-ETH`**  
AI-assisted research-integrity verdict: **`CONDITIONAL`**  
Calibration: **`NOT_CALIBRATED`**

## Scope and input binding

This is a read-only Phase-5 review of `stage1_phase4_research_report.md`,
SHA-256
`b04d98c2bb6003b6a24d96fb005353f06b4b5ab5e776a21f1d3f5a4f9c9ed656`.
The exact Phase-4 manifest/checkpoint, frozen Phase-2 verification MD/TSV, and
Route documents were used as closed-corpus context. The review performed no
new retrieval, panel construction, cover computation, coefficient test, limit,
report revision, or institutional-authority resolution.

The verdict addresses AI-assisted research integrity only. It is not a finding
about the proposed owner interface, formal algebra, analytic limit, citation
locator compliance, human-subject authorization, publication acceptance, or
Route status.

The seat used the current Codex model family and was blind to other Phase-5
first-pass outputs. This creates procedural role separation only, not proof of
statistically independent errors. The judgments are `NOT_CALIBRATED`.

## Seven-dimension assessment

| Dimension | Status | Evidence and boundary |
|---|---|---|
| 1. AI disclosure and transparency | `WARN` | **AI Disclosure and Verification Limitation** discloses AI-supported literature search, verification, synthesis, and drafting, plus the metadata/abstract/locator limits. It omits the exact AI product/model, version/date, accountable human reviewer, and concrete human-review checkpoints. |
| 2. Attribution and reference integrity | `WARN` | All 26 frozen IDs are cited and listed, and no direct quotation is used. The verifier records 25 `VERIFIED` and one `PLAUSIBLE` source, with no fabricated source. The report correctly carries `anchor:none`; therefore source identity/accounting is distinguishable from claim-to-passage clearance. |
| 3. Dual-use screening | `PASS` | Risk level: **None**. The work concerns pure geometry, group algorithms, formal products, and convergence design. It includes no concrete harmful operational method, exploit, surveillance workflow, discrimination mechanism, or personal-data procedure. |
| 4. Fair representation | `PASS` | The report preserves the preprint, DOI-less `PLAUSIBLE`, correction-bound, background-only, and peer-reviewed distinctions. It states the strongest counterargument and does not stigmatize or misrepresent any person or community. |
| 5. Data ethics and reproducibility | `PASS_WITH_LIMITS` | **Declarations** state that only frozen literature and project-design artifacts were used and that no owner panel, calculation, grid, or limit was executed. No personal data or human-related dataset is present. Hashes and fixed schedules aid reproducibility, but AI configuration and prompt/review provenance are not fully recorded. |
| 6. Funding and conflicts of interest | `PASS_WITH_LIMITS` | **Declarations** state `Funding: None` and `Competing interests: None declared`. Phase-2 separately records source-level COI as `UNKNOWN_NOT_CHECKED` for 26/26 sources; the report explicitly says general COI screening was not run. |
| 7. Human-subjects boundary | `NOT_APPLICABLE` | **Declarations** state that the work is theoretical/exact computational mathematics with no participants, personal data, animals, or interventions. The present report itself executes literature synthesis only. No human-subject authorization or institutional pathway is claimed. |

## Findings and required disposition

### `P32-ETH-001` — disclosed AI use lacks exact reproducibility and oversight fields

- Severity: **Conditional**.
- Evidence: **AI Disclosure and Verification Limitation** accurately states the
  AI-assisted task classes and the bounded meaning of verification, but uses
  only the generic terms “AI-assisted research tools” and “Human oversight was
  applied throughout.”
- Condition before delivery: identify the AI product/model family and version
  or dated configuration; list the actual AI task classes; identify the
  responsible human reviewer and the phases reviewed; and integrate the
  metadata/abstract/`anchor:none` qualification into the disclosure's
  “verified against cited sources” statement.
- Boundary: the condition is recorded for later authorized revision; this seat
  makes no report edit.

### `P32-ETH-002` — the `PLAUSIBLE` and correction-bound records must retain their exact status

- Severity: **Advisory**.
- Evidence: **Corpus Construction and Verification**, **Limitations and Future
  Work**, and Phase-2 records keep P32-S13 at `PLAUSIBLE`, P32-S06 as a
  non-peer-reviewed preprint, and P32-S17 bound to its correction scope. All
  citation anchors are `none`; retraction and source-level COI checks are absent
  for 26/26 rows.
- Action: a later source-finalization pass must not silently promote P32-S13 to
  `VERIFIED`, P32-S06 to peer-reviewed support, or affected P32-S17 claims to
  unaffected status. Exact passages and any structured retraction status must
  be separately frozen before stronger use.

### `P32-ETH-003` — no integrity-only block found

- Severity: **No action**.
- Evidence: the verification ledger contains 25 `VERIFIED`, one transparently
  labeled `PLAUSIBLE`, zero `FABRICATED`, and zero `UNVERIFIABLE` records. AI
  use is disclosed, direct quotations are absent, declarations are present, and
  no human-subject or personal-data activity is reported.
- Disposition: no frozen evidence supports fabrication, plagiarism, systematic
  source misrepresentation, undisclosed AI use, or concrete harm-enabling
  content. `BLOCKED` is not warranted.

## AI-disclosure verification

| Check | Result |
|---|---|
| Disclosure statement present | **Yes** |
| AI task scope stated | **Yes, at task-class level** |
| Scope accurate against frozen records | **Broadly yes, only with the adjacent verification limitation** |
| Tool/model and version/date stated | **No** |
| Responsible human and review checkpoints stated | **No; generic oversight only** |
| Hallucination/locator limitation acknowledged | **Yes** |
| AI-generated scientific data presented | **No** |

## Attribution and reference-integrity accounting

- Frozen reference inventory: **26**.
- Citation-list/inventory closure: **26/26** IDs cited and **26/26** listed.
- Source-identity outcomes: **25/26 `VERIFIED`** and **1/26 `PLAUSIBLE`**
  (P32-S13, DOI-less authoritative journal record); **0 `FABRICATED`** and
  **0 `UNVERIFIABLE`**.
- Metadata: **26/26** exact after the authorized P32-S02 page correction.
- Peer-reviewed sources: **22/26**.
- Phase-4 claim intents: **8**.
- Locator-level claim-to-passage clearance: **0/8** claim intents; all 26 prose
  citation pairs retain `anchor:none`.
- Direct quotations: **0**.
- Retraction/Crossmark checks: **0/26**; rows remain `NOT_CHECKED` apart from
  the separately known P32-S17 correction boundary, which is not a retraction
  clearance.
- Source-level COI checks: **0/26**; all rows remain
  `UNKNOWN_NOT_CHECKED`.
- Clearly identifiable author self-citations: **0/26**; the P32-S06 author
  “K. Wang” is not an exact identity match to report author Liang Wang, so no
  self-citation is inferred from surname alone.
- Frozen-record fabrication findings: **0**. These values certify only the
  frozen identity/metadata states, not passage-level claim faithfulness.

## Responsible-use and human-subjects boundary

Dual-use risk is **None**; no Responsible Use statement is required. No
human-subject activity is present. No authority context, profile, pathway,
consent requirement, or institutional authorization was selected or inferred.

> **Human-subjects boundary:** This review does not authorize recruitment,
> consent, access to identifiable data, intervention, or data collection.

## Ethics decision log

| Item | Verdict | User decision | Reasoning |
|---|---|---|---|
| `P32-ETH-001` | `CONDITIONAL` | `PENDING`; Phase-6 revision is not authorized | No user adjudication has yet been recorded. |

## Closed ledger

```text
PAPER=P32
SEAT=R10-P5-ETH
REPORT_SHA256=b04d98c2bb6003b6a24d96fb005353f06b4b5ab5e776a21f1d3f5a4f9c9ed656
AI_ASSISTED_RESEARCH_INTEGRITY_VERDICT=CONDITIONAL
DUAL_USE_RISK=NONE
HUMAN_SUBJECT_ACTIVITY=NONE_REPORTED
HUMAN_SUBJECT_AUTHORIZATION_CLAIM=NONE
REFERENCE_IDENTITY_CLOSURE=25/26_VERIFIED_PLUS_1/26_PLAUSIBLE
CLAIM_TO_PASSAGE_CLEARANCE=0/8
REVIEW_CALIBRATION=NOT_CALIBRATED
MODEL_DIVERSITY=SINGLE_CODEX_FAMILY
INDEPENDENCE=PROCEDURAL_ONLY
NEW_RETRIEVAL=NOT_RUN
REPORT_EDIT=NOT_RUN
```
