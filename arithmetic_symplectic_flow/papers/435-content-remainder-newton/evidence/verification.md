# Batch R — mechanical verification record

Batch `NONHOMOGENEOUS-FEEDBACK-20260923-R`, papers 435–439 only.
Session date: 2026-09-23; not an independently measured UTC timestamp.
Status: **PASS — STRICT MECHANICAL VERIFICATION**.

This is an artifact-integrity record, not a mathematical review, experiment,
checkpoint release or Route result. Root owns scientific outcomes, review
acceptance, the batch log, summary and overview integration. This record does
not authorize paper 440 or another research round.

## Opening preservation and preparation history

Before new-batch writes, a read-only measurement parsed archived verifier
literals as data without importing or executing those programs. All 82
previously frozen packages 348–429, containing 644 files, matched their stored
bundle hashes; the five fixed-file anchors also matched. Fresh snapshots of
430–434 added 39 files, giving 87 old packages and 683 files to preserve.
Both current overview files were measured as complete byte sequences.

Bundle hashing uses the SHA-256 of the UTF-8 concatenation of sorted relative
POSIX paths, a tab, each file's lowercase SHA-256, and a final LF per file.
Symlinks and nonregular package artifacts are rejected. The strict check
recovered both opening overview hashes after reversing only the new-block
insertion and old Current-to-Preceding title change.

There were no 435–439 path collisions at opening. After all five frozen
paths and candidate IDs arrived, the [read-only verifier](../tools/verify_batch.py)
was adapted from batch Q's source without executing the historical program.
The [batch log](../batch-log.md) owns opening receipts, actual outcomes and
final evidence receipts. Missing planned log content is pending in pre-handoff
mode and must be present for a strict result.

## Preparatory command and measured result

Run from `arithmetic_symplectic_flow`:

```bash
python3 papers/435-content-remainder-newton/tools/verify_batch.py --pre-handoff --brief
```

The first staged command exited 0 with
`PRE_HANDOFF_CHECKS_COMPLETE_NOT_FINAL`, not PASS. It counted 12 Markdown
files, 970 local links and five available identity surfaces. All 87 old
packages, five immutable anchors, five original card prefixes and five
candidate-ID declaration checks matched. Outcome surfaces, evidence and
review bindings were zero because final receipts had not been supplied.
Both overview files still matched their opening hashes byte-for-byte, with
the new handoff blocks appropriately pending. Missing delivery artifacts,
opening log rows, final receipts and the strict-mode gate remained pending.
These are measurements of that command's inputs, not forecasts of completion.

Verifier source: 392 lines, unchanged during final verification; SHA-256
`b99b89eac0c851510a2c4f0f8caa7b9c29d44504e1af6732a878f78dc0b95b22`.
The source was read completely through its EOF marker during preparation;
its final-stage byte hash still matches that read version. This record retains
the initial pending history rather than treating a staged result as completion.

Pre-handoff mode can never report PASS, even when all artifacts exist.

## Released strict command and result

After root's separate FINAL-READY release, the QA agent ran:

```bash
python3 papers/435-content-remainder-newton/tools/verify_batch.py --brief
```

The command exited 0 with the following measured output:

```json
{
  "result": "PASS",
  "scope": "Mechanical byte/identity/status/link/receipt checks only; not mathematical proof.",
  "reviewCalibration": "NOT_CALIBRATED",
  "batch": "NONHOMOGENEOUS-FEEDBACK-20260923-R",
  "packages": 5,
  "identitySurfaces": 20,
  "statusSurfaces": 20,
  "markdown": 38,
  "relativeLinks": 1067,
  "frozenPrefixes": 5,
  "preservedPackages": 87,
  "preservedAnchors": 5,
  "preservedOverviewArchives": 2,
  "boundEvidenceReceipts": 15,
  "boundSurfaceReceipts": 20,
  "candidateIDCollisionChecks": 5,
  "pending": []
}
```

The Markdown count covers the five new packages; the local-link count also
includes both complete overviews and their preserved historical links.
This record is then read back to EOF and the same strict command is rerun
to cover the changed record. Root owns later completion wording in the batch
log, summary and two overviews; those edits require another strict run on the
changed inputs. This record does not certify root's scientific reading or
acceptance of the five reviews. QA reads verifier/record source and structural
metadata and checks whole-file bytes mechanically, without rederiving proofs.

## Checks satisfied by the strict result

- Preserve 87 old package bundles and the five inherited fixed-file anchors.
  Archived JavaScript and Python anchor literals are read only as data.
- Preserve the five original card prefixes: 435/96 lines, 436/104, 437/96,
  438/97 and 439/92. Final card bytes are also bound by review receipts.
- Match all five candidate IDs on the 20 delivered surfaces, and require each
  ID to occur only in its expected card's first-20-line ownership declarations.
  This bounded metadata check does not interpret scientific references as IDs.
- Bind the actual shared Outcome on all four surfaces to root's batch-log row.
  Cards use the appended field after their frozen prefix; paper, README and
  ledger use their first 20 lines. No STOP or advancement is predetermined.
- Bind all 15 scope/raw/final-review file hashes and all 20 current-surface
  hashes in final reviews, with explicit CP2/CP3 PASS markers. Actual filenames
  are `evidence/scope-review.md`, `evidence/independent-derivation.md` and
  `evidence/independent-review.md`. Filename receipts may bind the same or next
  two lines without crossing another surface label; unique same-line aliases
  Paper, Card, README and optional-FINAL ledger are also accepted.
- Check local Markdown destinations, LF/final newline and code-fence balance
  across all new Markdown files and both complete overviews. New missing
  targets are pending only if they are explicitly planned delivery artifacts.
- Recover both opening overview hashes after removing the new R block and
  reversing only Q's Current-to-Preceding heading change; require current links
  to all five new package READMEs. No other old body change is permitted.

Final batch-log rows repeat these formats for each paper 435–439:

```text
| 435 | `CP1_SHA256` | `RAW_SHA256` | `REVIEW_SHA256` |
| 435 | `outcome: ACTUAL SHARED OUTCOME PHRASE` |
```

Opening old-bundle rows accept the exact full package slug or its numeric
paper prefix, but each number, supplied slug, file count and digest must match
the frozen literal. A missing row is pending only in pre-handoff mode.

## Exposure and scope limits

Model/shared-history internal review is **NOT_CALIBRATED**. Hash receipts
bind file bytes and recorded versions, not authentic private reading history,
blindness, model independence, external peer review or mathematical truth.
The QA agent checks code, byte preservation and structural metadata; it does
not rederive proofs or independently certify root's scientific acceptance.

Local-link checks concern destination existence, not remote availability,
fragments or every CommonMark feature. Finite mechanical checks do not imply
infinite claims. No scientific experiment, network action, Git mutation,
publication, old-file edit or additional research is authorized by this record.
