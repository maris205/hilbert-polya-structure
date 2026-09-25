# Batch O — mechanical verification record

Batch `QUOTIENT-FEEDBACK-20260923-O`, papers 420–424.
Session date: 2026-09-23; not an independently measured UTC timestamp.
Status: **PASS — STRICT MECHANICAL VERIFICATION**.

This artifact-integrity record is not a mathematical review, scientific
experiment, checkpoint release or Route result. The [batch log](../batch-log.md)
owns authority, actual outcomes and review receipts. The [read-only verifier](../tools/verify_batch.py)
does not modify files or execute archived verifiers.

## Commands, pending history and completion boundary

Commands run from `arithmetic_symplectic_flow`. The preparatory command was:

```bash
python3 papers/420-divisor-reciprocal-displacement/tools/verify_batch.py --pre-handoff --brief
```

Pre-handoff mode can return only `PRE_HANDOFF_CHECKS_COMPLETE_NOT_FINAL`,
never PASS. Missing planned files and receipts remain pending; invalid
existing preservation anchors, links, outcomes or receipts fail. Missing
opening receipt rows remain pending, but all 72 old bundles are still checked
against fixed literals. These checks do not establish completion.

The initial record was PENDING. Its pre-handoff run counted 12 Markdown
files, 925 local links and five available identity surfaces. Scientific
delivery, final receipts, five opening receipt rows, the summary and new
overview blocks were still pending. All 72 old packages, five fixed anchors
and six original/clarified prefixes matched against fixed literals. That
result was not a final PASS or a mathematical assessment.

After root released FINAL-READY, the QA agent ran strict mode:

```bash
python3 papers/420-divisor-reciprocal-displacement/tools/verify_batch.py --brief
```

The command exited 0 with `PASS` and no pending items on the released inputs.
This record was then updated and read back to EOF; the same strict command
is rerun after that write to cover the changed record. Root owns completion
wording in the batch log, summary and two overviews; later edits there require
another strict run on those changed inputs. This QA does not independently
certify root's scientific acceptance of the five reviews or rederive proofs.

Verifier source: 367 lines, unchanged during final verification; SHA-256
`0f5b26118d4527a25ba6d8d27de81f6ae5823cd460e26ed83ebc1f8bf82b4a69`.

Measured strict output:

```json
{
  "result": "PASS",
  "scope": "Mechanical byte/identity/status/link/receipt checks only; not mathematical proof.",
  "reviewCalibration": "NOT_CALIBRATED",
  "batch": "QUOTIENT-FEEDBACK-20260923-O",
  "packages": 5,
  "identitySurfaces": 20,
  "statusSurfaces": 20,
  "markdown": 38,
  "relativeLinks": 1024,
  "frozenPrefixes": 6,
  "preservedPackages": 72,
  "preservedAnchors": 5,
  "preservedOverviewArchives": 2,
  "boundEvidenceReceipts": 15,
  "boundSurfaceReceipts": 20,
  "pending": []
}
```

The Markdown count covers the five new packages; the local-link count also
includes both complete overviews and their preserved historical links.

## Checks satisfied by the strict result

- Preserve all 72 old packages 348–419 and five inherited fixed-file anchors.
  Archived JavaScript and Python verifier literals are read as data, never
  imported or executed.
- Preserve six frozen prefixes: the five originals 420/88 lines, 421/91,
  422/95, 423/83 and 424/116, plus the CP1-clarified 421/99 prefix.
  Review bindings additionally cover the complete final cards.
- Match all five candidate IDs across 20 delivered surfaces. Compare the
  explicit `Outcome:` field with the root-recorded actual outcome, without
  predicting STOP or advancement. Cards use appended fields after the longest
  frozen prefix; the other three surfaces use their first 20 lines.
- Bind 15 CP1/raw/final-review file hashes and 20 current surface hashes in
  final reviews, with CP2/CP3 PASS markers. The evidence files are
  `evidence/scope-review.md`, `evidence/independent-derivation.md` and
  `evidence/independent-review.md`, respectively. Hashes bind records, not
  private exposure history or mathematical correctness.
- Check local Markdown destinations, LF/final newline and code-fence balance
  in all new Markdown files and both complete overviews.
- Recover both opening overview hashes by removing the new O block after the
  heading and reversing only N's Current-to-Preceding title change; all old
  body bytes otherwise remain preserved.

Expected final batch-log rows, repeated for each paper 420–424:

```text
| 420 | `CP1_SHA256` | `RAW_SHA256` | `REVIEW_SHA256` |
| 420 | `outcome: ACTUAL SHARED OUTCOME PHRASE` |
```

Opening old-bundle rows accept the exact full package slug or its numeric
paper prefix, with optional spacing/hash backticks; each number, full slug
when supplied, file count and digest must match its frozen literal. Outcomes
tolerate bold/code markup and a final period, but normalized phrases must
match all four surfaces. Review hash receipts allow filenames or unambiguous
same-line aliases Paper, Card, README and optional-FINAL ledger. The script
does not prescribe scientific outcomes.

## Provenance and exposure limits

This is a read-only adaptation of batch N's Python verifier. Opening 415–419
bundle hashes and both overview hashes were measured before new-batch writes:
the preceding 67 bundles and five fixed anchors matched, the full preservation
set covered 72 packages and 566 files, and 420–424 had no path collisions.
The checker scans bytes and structural fields; it does not rederive proofs.
Model/shared-history internal review is **NOT_CALIBRATED**. Neither receipt
hashes nor disclosure text certify blindness, independent model selection,
external peer review or private reading histories.

Local links are checked for destination existence, not remote availability,
fragments or every full-CommonMark feature. No infinite claim follows from
finite checks. No numerical experiment, external search, Git mutation or
publication action is performed. Root owns scientific outcomes, review
acceptance and final handoff. This PASS records artifact integrity for the
checked inputs; it neither establishes a scientific gate or Route pass nor
authorizes a new research round.
