# Batch S — mechanical verification record

Batch `ADMISSION-CLOCK-20260923-S`, papers 440–444 only.
Candidate-ID and card freeze label: 2026-09-23.
Preparation/handoff record label: 2026-09-24; not an independently measured UTC timestamp.
Status: **PASS — STRICT MECHANICAL VERIFICATION**.

The supplied environment date is 2026-09-24; root's batch log discloses a
container date of 2026-09-23. Neither source is used here to prove chronology.
The verifier checks the declared handoff label, not wall-clock consistency.

This artifact-integrity record is not a mathematical review, experiment,
checkpoint release or Route result. Root owns scientific outcomes, review
acceptance and final integration. No paper 445 or further research is authorized
by this record. Model/shared-history internal review is **NOT_CALIBRATED**.

## Opening preservation and source exposure

Before new-batch writes, a separate read-only measurement parsed archived
verifier anchor literals as data, without importing or executing those programs.
All 87 old packages 348–434 and their 683 files matched stored bundle hashes.
Fresh snapshots of 435–439 added 39 files: the preservation set is 92 packages
and 722 files. All five fixed-file anchors matched. Both current overviews were
measured as complete byte sequences, and their older Q archives still recovered
the preceding opening hashes. No 440–444 path collisions existed at that time.

Bundle hashing uses SHA-256 of UTF-8 concatenated sorted relative POSIX paths,
a tab, each file's lowercase SHA-256, and a final LF per file. Symlinks and
nonregular package artifacts are rejected. The new overview transformation may
only insert S's current block and demote R's current heading; reversing those
operations must recover both complete opening byte hashes.

The QA agent read the prior 435 verifier completely through its EOF marker,
plus five lines of the root overview and four lines of the registry. Old
package contents were read only as bytes for hashing, not interpreted as
research. S configuration comes from root's opening/prefix tables and each
new card's title, ID and batch metadata. No new scientific result was read
for judgment, and no proof was rederived.

## Commands and pending history

Run from `arithmetic_symplectic_flow`:

```bash
python3 papers/440-double-remainder-fraction/tools/verify_batch.py --pre-handoff --brief
```

The [read-only verifier](../tools/verify_batch.py) reads root's
[batch log](../batch-log.md) for actual outcomes and final evidence receipts.
Pre-handoff mode can only report `PRE_HANDOFF_CHECKS_COMPLETE_NOT_FINAL`,
never PASS. Missing planned artifacts or receipts remain explicit pending items;
wrong existing hashes, broken unplanned local links or conflicting metadata fail.

The first staged run exited 0 with `PRE_HANDOFF_CHECKS_COMPLETE_NOT_FINAL`:
13 Markdown files, 989 local destinations and five available identity surfaces.
All 92 old package bundles, five immutable anchors, five original card prefixes
and five bounded ID-ownership checks matched. Actual Outcome, final evidence
and final surface bindings were zero because final receipts were still pending.
The two complete overviews still matched the opening hashes; their new handoff
blocks remained pending. There were 43 explicit pending entries, including
missing delivery artifacts, receipt/outcome fields and the final strict gate.
These numbers describe that run's inputs, not scientific completion.

Verifier source: 395 lines, unchanged during strict verification; SHA-256
`9ad78fd45d87a8fb32e87c87e68843d8a13a7baaf15e2fb1f7224060a5b6f35d`.
The QA author read the new source completely to EOF. A second same-model
agent's bounded static source comparison found no concrete migration bug;
that check neither executed the program nor reviewed scientific results.
The initial record update was followed by a staged rerun.
Those staged/static checks preceded root's final-review filename correction.
Only two path literals were then changed to use `evidence/review.md`; checking
logic was unchanged and no extra QA command was run at that amendment stage.
The released strict check below covers the corrected filename contract.

## Released strict command and measured result

After root's FINAL-READY release, the QA agent ran from the same workspace:

```bash
python3 papers/440-double-remainder-fraction/tools/verify_batch.py --brief
```

The command exited 0 with the following actual output:

```json
{
  "result": "PASS",
  "scope": "Mechanical byte/identity/status/link/receipt checks only; not mathematical proof.",
  "reviewCalibration": "NOT_CALIBRATED",
  "batch": "ADMISSION-CLOCK-20260923-S",
  "packages": 5,
  "identitySurfaces": 20,
  "statusSurfaces": 20,
  "markdown": 38,
  "relativeLinks": 1094,
  "frozenPrefixes": 5,
  "preservedPackages": 92,
  "preservedAnchors": 5,
  "preservedOverviewArchives": 2,
  "boundEvidenceReceipts": 15,
  "boundSurfaceReceipts": 20,
  "candidateIDCollisionChecks": 5,
  "pending": []
}
```

The 38 new Markdown inputs are the 20 card/paper/README/ledger surfaces,
15 scope/raw/final-review files, and this verification record, batch log and
batch summary. Local-link checks additionally cover both complete overviews.
The 92 preserved old bundles retain all 722 frozen files. Scientific outcomes
and final-review hashes come from root's supplied records; QA neither predicts
them nor independently certifies root's scientific acceptance or full reading.

This updated record is read back to EOF and the same strict command is rerun
to cover its changed bytes. Root owns subsequent completion wording in the
batch log, summary and two overviews; those changes require a final root strict
rerun. A record of artifact integrity is not a scientific gate or Route result.

## Checks satisfied by the strict result

- Preserve all 92 old bundles 348–439 and five inherited immutable anchors.
  Archived JavaScript/Python constants remain data, never executable dependencies.
- Preserve original card prefixes 440/99 lines, 441/104, 442/104, 443/99 and
  444/103. Review bindings additionally cover complete final card bytes.
- Match all five IDs on 20 delivered surfaces, and require each new ID to have
  only its expected card's first-20-line ownership declaration among local cards.
  Scientific references are not interpreted as ownership declarations.
- Bind 20 actual Outcome fields to the five root batch-log rows. Cards use
  appended metadata after the frozen prefix; other surfaces use their first
  20 lines. No STOP or advancement is predetermined.
- Bind 15 scope/raw/final-review hashes plus all 20 current surface hashes in
  final reviews, with CP2/CP3 PASS markers. Evidence filenames are
  `scope-review.md`, `independent-derivation.md` and `review.md`.
  Receipt aliases Paper, Card, README and optional-FINAL ledger must bind
  a unique exact current hash on the same line. Filename receipts also allow
  the next two lines without crossing another surface label.
- Check scoped local Markdown destinations, LF/final newline and fence balance
  in every new Markdown file and both complete overviews. Full output lists
  each scanned new Markdown input's line count and hash.
- Recover two old overview byte hashes after reversing S insertion and R's
  heading demotion. The current handoff block must contain 2026-09-24, 5/5
  and all five new package README links. Freeze IDs and batch retain 20260923.

Batch-log final rows repeat these formats for each paper 440–444:

```text
| 440 | `CP1_SHA256` | `RAW_SHA256` | `REVIEW_SHA256` |
| 440 | `outcome: ACTUAL SHARED OUTCOME PHRASE` |
```

Opening bundle rows accept the exact slug or numeric paper prefix, but the
number, supplied slug, file count and digest must match the frozen literals.
Strict completion requires zero pending items; later changed metadata or records
require another check of those changed inputs.

## Limits

Hash binding certifies recorded file bytes, not authentic private reading
history, blindness, model independence, external peer review or mathematical
truth. QA does not independently certify root's scientific acceptance.
Local-link checks concern destination existence, not remote availability,
fragments or every CommonMark feature. Finite checks imply no infinite claim.
No science computation, network action, Git mutation, publication, old-file
edit or additional research is performed by this verifier.
