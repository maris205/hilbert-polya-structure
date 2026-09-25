# Batch L — mechanical verification record

Batch `NONLINEAR-PACKET-20260923-L`, papers 405–409.
Session date: 2026-09-23; not an independently measured UTC timestamp.
Status: **PASS — STRICT MECHANICAL VERIFICATION**.

This artifact-integrity record is not a mathematical review, scientific
experiment, checkpoint release or Route result. The [batch log](../batch-log.md)
owns authority, actual outcomes and review receipts. The [read-only verifier](../tools/verify_batch.py)
does not modify files or execute archived verifiers.

## Commands, pending history and completion boundary

Commands run from `arithmetic_symplectic_flow`. The preparatory command was:

```bash
python3 papers/405-signed-remainder-permission/tools/verify_batch.py --pre-handoff --brief
```

Pre-handoff mode can return only `PRE_HANDOFF_CHECKS_COMPLETE_NOT_FINAL`,
never PASS. Missing planned files and receipts remain pending; invalid
existing preservation anchors, links, outcomes or receipts fail. Missing
opening receipt rows remain pending, but all 57 old bundles are still checked
against independent fixed literals. These checks do not establish completion.

The initial record was PENDING. Its pre-handoff run checked 12 Markdown
files, 876 local links, five available identity surfaces, 57 old packages,
five fixed anchors and eight frozen prefixes; scientific delivery and final
receipts were still pending. This was not a final PASS. During source review,
root identified inherited raw/review filenames from the preceding batch.
Before strict verification, the QA agent corrected the evidence tuple and
final-review read path to this batch's actual filenames. No scientific
evidence was renamed or edited. The final script below includes that fix.

After root released FINAL-READY, the QA agent ran strict mode:

```bash
python3 papers/405-signed-remainder-permission/tools/verify_batch.py --brief
```

The command exited 0 with `PASS` and no pending items on the released inputs.
This record was then updated; the same strict command is rerun after the
write to cover the changed record. Later root handoff-metadata edits require
another run on those changed inputs. The QA agent did not rederive proofs or
independently certify root's recorded acceptance of the five reviews.

Verifier provenance: read-only Python adaptation of the archived batch-K
`evidence/verify-batch.cjs`; archived verifiers were never executed.
Final verifier: 349 lines; SHA-256
`498efe8c230b9d2bb0bf65b84a24932dd3bab334f56f34c1ca794291f56050b9`.

Measured strict output:

```json
{
  "result": "PASS",
  "scope": "Mechanical byte/identity/status/link/receipt checks only; not mathematical proof.",
  "reviewCalibration": "NOT_CALIBRATED",
  "batch": "NONLINEAR-PACKET-20260923-L",
  "packages": 5,
  "identitySurfaces": 20,
  "statusSurfaces": 20,
  "markdown": 38,
  "relativeLinks": 960,
  "frozenPrefixes": 8,
  "preservedPackages": 57,
  "preservedAnchors": 5,
  "preservedOverviewArchives": 2,
  "boundEvidenceReceipts": 15,
  "boundSurfaceReceipts": 20,
  "pending": []
}
```

The Markdown count covers the five new packages. The local-link count also
includes both complete overview files and their preserved historical links.

## Checks satisfied by the strict result

- Preserve all 57 old packages 348–404 and five inherited fixed-file anchors.
  Archived verifier literals are read as data, never imported or executed.
- Preserve eight frozen prefixes: the five originals 405/96 lines, 406/93,
  407/105, 408/75 and 409/85, plus CP1-clarified 405/101, 408/81 and 409/94.
  Original bytes were measured before adaptation; append-only clarifications
  retain those originals. Review bindings cover the complete final cards.
- Match all five candidate IDs across 20 delivered surfaces. Compare the
  explicit `Outcome:` field with the root-recorded actual outcome, without
  predicting STOP or advancement. Cards use appended fields after the longest
  frozen prefix; the other three surfaces use their first 20 lines.
- Bind 15 CP1/raw/final-review file hashes and 20 current surface hashes in
  final reviews, with CP2/CP3 PASS markers. The three evidence files are
  `evidence/scope-review.md`, `evidence/independent-review-raw.md` and
  `evidence/independent-review.md`, respectively. These checks bind records,
  not private exposure history or mathematical correctness.
- Check local Markdown destinations, LF/final newline and code-fence balance
  in all new Markdown files and both complete overviews.
- Recover both opening overview hashes by removing the new L block and
  reversing only K's Current-to-Preceding heading change; preserve old prose.

Expected batch-log rows, repeated for each paper 405–409:

```text
| 405 | `CP1_SHA256` | `RAW_SHA256` | `REVIEW_SHA256` |
| 405 | `outcome: ACTUAL SHARED OUTCOME PHRASE` |
```

Opening old-bundle rows retain the previous `number | file count | SHA256`
format for 400–404. Outcomes tolerate bold/code markup and a final period,
but normalized phrases must match all four surfaces. Review hash receipts
allow filenames or unambiguous same-line aliases Paper, Card, README and
optional-FINAL ledger. The script does not prescribe scientific outcomes.

## Scope and exposure limits

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
