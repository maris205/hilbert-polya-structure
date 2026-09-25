# Batch H — mechanical verification record

Batch `GEOMETRIC-RETURN-20260922-H`, papers 385–389; 2026-09-22.
Status: **PASS — STRICT FINAL MECHANICAL VERIFICATION**.

This is a mechanical artifact record, not a proof review, scientific
experiment, checkpoint release or Route result. The [batch log](../batch-log.md)
owns authority, actual outcomes and review receipts. The [read-only verifier](verify-batch.cjs)
does not modify files or execute archived verifiers.

## Final command and actual result

After root issued FINAL-READY and stopped writes to the scientific surfaces
and handoff metadata, this command was run from `arithmetic_symplectic_flow`:

```bash
node papers/385-divisor-fractional-return/evidence/verify-batch.cjs --brief
```

It exited 0 and returned these measured counts, with no pending items:

```json
{
  "result": "PASS",
  "packages": 5,
  "identitySurfaces": 20,
  "statusSurfaces": 20,
  "markdown": 38,
  "relativeLinks": 927,
  "frozenPrefixes": 9,
  "preservedPackages": 37,
  "preservedAnchors": 5,
  "preservedOverviewArchives": 2,
  "boundEvidenceReceipts": 15,
  "boundSurfaceReceipts": 20,
  "pending": []
}
```

The 927 local link checks include both complete overviews and the final
batch-log link addition; the previous 926-link count is not reused. Only
this verification record was edited after the completed strict run above.
The same strict command must be rerun after this edit and return PASS before
handoff, covering this record itself as a changed input.

The unchanged verifier was fully read through EOF when prepared: 294 lines,
SHA256 `554250638940bf6bc468c1dabe19b256e26ff33e77c2b44db8f68a2704b3485f`.
The batch log binds the actual 15 scope/raw/review hashes, and those final
reviews bind all 20 current scientific surfaces. No candidate outcome is
inferred from a checksum or from a review marker.

## Preliminary mode and final boundary

Syntax and preliminary checks used:

```bash
node --check papers/385-divisor-fractional-return/evidence/verify-batch.cjs
node papers/385-divisor-fractional-return/evidence/verify-batch.cjs --pre-handoff --brief
```

Those earlier checks returned syntax exit 0 and
`PRE_HANDOFF_CHECKS_COMPLETE_NOT_FINAL`. Their early snapshot contained 21
new Markdown files and 835 local links, with unfinished artifacts and receipts
explicitly pending. It is historical preparation, not the final result above.
Pre-handoff mode can never return final PASS; existing invalid anchors, links,
outcomes or submitted receipts still fail even in that mode.

## Verified mechanical checks

- Preserve all 37 old packages 348–384 and five inherited fixed-file anchors.
  Archived script literals are parsed only as data; no old verifier runs.
- Preserve the nine original/clarified card prefixes across the five new
  cards. Card 389's 63-line clarified prefix was read from its actual bytes;
  its SHA256 is `19bee24c132e6e7c10c51825b0b934546bac5d811b25e23d2d4c37f6e1929633`.
- Check the five IDs across all 20 scientific surfaces. Match each explicit
  `Outcome:` field to its actual root-recorded outcome, without assuming
  STOP or advancement in advance. On cards, inspect only the append after
  the longest frozen prefix; other surfaces use the first 20 lines.
- Bind 15 CP1/raw/final-review hashes and the 20 current final-file hashes
  recorded in their corresponding reviews. Review markers are artifact
  checks, not a mathematical endorsement or external peer review.
- Check local Markdown link destinations, LF/final-newline format and
  code-fence balance in all new Markdown files and both full overviews.
- Recover both opening overview hashes by discarding the new H block and
  reversing only G's Current-to-Preceding heading change. Preserve old prose.

The final batch-log receipt formats are one row per paper:

```text
| 385 | `CP1_SHA256` | `RAW_SHA256` | `REVIEW_SHA256` |
| 385 | `outcome: ACTUAL SHARED OUTCOME PHRASE` |
```

Repeat for 386–389. Outcome text may use bold/code markup and a final period,
but its normalized phrase must match all four scientific surfaces. Reviewed
file hashes may use the explicit filenames or unambiguous same-line aliases
Paper, Card, README, or optional-FINAL ledger.

## Limits

Local link checks test destination existence, not remote availability,
fragment anchors or every feature of a full CommonMark renderer. No proof
is rederived, no infinite claim follows from finite checking, and no numerical
experiment, literature search, Git mutation or external action is performed.
Root owns the actual research results, review acceptance and final handoff.
Mechanical PASS is not a target pass, mathematical endorsement or formal
Route coordinate. No old scientific package, fixed anchor, verifier, scientific
surface or other handoff metadata was edited in this final QA step; no further
research round was started.
