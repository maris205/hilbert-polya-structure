# Batch K — mechanical verification record

Batch `NONLINEAR-RETURN-20260922-K`, papers 400–404; card freeze label 2026-09-22.
Verification session date: 2026-09-23, supplied by the session context; this
is not an independently measured UTC execution timestamp.
Status: **PASS — STRICT MECHANICAL VERIFICATION**.

This is an artifact-integrity record, not a mathematical review, scientific
experiment, checkpoint release or Route result. The [batch log](../batch-log.md)
owns authority, actual outcomes and review receipts. The [read-only verifier](verify-batch.cjs)
does not modify files or execute archived verifiers.

## Commands, result and completion boundary

Run from `arithmetic_symplectic_flow`:

```bash
node papers/400-nonlinear-exchange-return/evidence/verify-batch.cjs --brief
```

Root released FINAL-READY after recording acceptance of all five CP2/CP3
reviews and freezing the scientific surfaces. The QA agent independently ran
the command above on the released inputs; it exited 0 with `PASS` and no
pending items. This record was then updated; the same strict command is rerun
after the write to cover the changed record. Any later root handoff-metadata
edits require another run on those changed inputs.

Verifier source SHA-256:
`d2bc63a0abe07c8ac30a408b237bc1de12214bece3669529229510e2cfc6417c`
(300 lines, unchanged during final verification).

Measured strict result:

```json
{
  "result": "PASS",
  "packages": 5,
  "identitySurfaces": 20,
  "statusSurfaces": 20,
  "markdown": 38,
  "relativeLinks": 956,
  "frozenPrefixes": 6,
  "preservedPackages": 52,
  "preservedAnchors": 5,
  "preservedOverviewArchives": 2,
  "boundEvidenceReceipts": 15,
  "boundSurfaceReceipts": 20,
  "pending": []
}
```

The Markdown count covers the five new packages; the local-link count also
covers both complete overview files, including their preserved history.
The earlier syntax and pre-handoff checks were preparatory only. Pre-handoff
mode can return only `PRE_HANDOFF_CHECKS_COMPLETE_NOT_FINAL`, never PASS;
those checks were not used as the strict completion result.

## Checks satisfied by the strict result

- Preserve all 52 old packages 348–399 and five inherited fixed-file anchors.
  Archived verifier literals are read as data, never executed.
- Preserve the six original/clarified frozen prefixes across the five new
  cards, including both the original 87-line and clarified 100-line prefixes
  for 402. Final review binding additionally checks the entire current cards.
- Match all five candidate IDs across 20 delivered surfaces. Compare each
  explicit `Outcome:` field with its root-recorded actual outcome, without
  predicting STOP or advancement. Check card outcomes only after the longest
  frozen prefix; other surfaces use their first 20 lines.
- Bind 15 CP1/raw/final-review file hashes and the 20 final-surface hashes in
  those reviews. Hash/marker checks bind records, not private exposure history
  or substantive mathematical correctness.
- Check local Markdown link destinations, LF/final-newline format and
  code-fence balance in all new Markdown files and both complete overviews.
- Recover both opening overview hashes by discarding the new K block and
  reversing only J's Current-to-Preceding heading change, preserving old prose.

The final batch-log receipt formats are one row per paper:

```text
| 400 | `CP1_SHA256` | `RAW_SHA256` | `REVIEW_SHA256` |
| 400 | `outcome: ACTUAL SHARED OUTCOME PHRASE` |
```

Repeat for 401–404. Outcome text may have bold/code markup and a final period,
but its normalized phrase must match all four surfaces. Reviewed file hashes
may use explicit filenames or unambiguous same-line aliases Paper, Card,
README, or optional-FINAL ledger. These conventions do not predetermine results.

## Scope and exposure limits

Mechanical work reads old verifier code and identity/preservation metadata;
the running checker scans file bytes and structural fields without proving
the research claims. Shared-history internal review is NOT_CALIBRATED; this
record cannot certify blind, cross-model or external peer review, or confirm
private read histories merely from authors' disclosure text.

Local links are checked for destination existence, not remote availability,
fragment targets or every feature of a full CommonMark renderer. No proof
is rederived, no infinite claim follows from finite checks, and no numerical
experiment, external search, Git mutation or publication action is performed.
Root owns the scientific outcomes, review acceptance and final handoff.
This PASS records artifact integrity for the checked inputs; it does not
authorize a new research round or establish a scientific gate or Route pass.
