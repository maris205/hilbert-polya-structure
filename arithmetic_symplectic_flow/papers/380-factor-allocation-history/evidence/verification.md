# Batch G — mechanical verification record

Batch `FULL-TRANSPORT-20260922-G`, papers 380–384; 2026-09-22.
Status: **PASS — STRICT FINAL MECHANICAL VERIFICATION**.

This is a mechanical artifact record, not a mathematical review, scientific
computation, checkpoint release or Route result. The [batch record](../batch-log.md)
owns authority and review receipts. The [read-only verifier](verify-batch.cjs)
does not write files or execute archived verification scripts.

## Final command and actual result

After root issued FINAL-READY and stopped writes, the following command was
run from `arithmetic_symplectic_flow` against the completed handoff files:

```bash
node papers/380-factor-allocation-history/evidence/verify-batch.cjs --brief
```

It exited 0 and returned the following actual counts, with no pending items:

```json
{
  "result": "PASS",
  "packages": 5,
  "identitySurfaces": 20,
  "statusSurfaces": 20,
  "markdown": 38,
  "relativeLinks": 923,
  "frozenPrefixes": 5,
  "preservedPackages": 32,
  "preservedAnchors": 5,
  "preservedOverviewArchives": 2,
  "boundEvidenceReceipts": 15,
  "boundSurfaceReceipts": 20,
  "pending": []
}
```

The 923 link checks include the two complete overviews and the batch-log links
added in the final metadata update; they supersede the earlier 921-link run.
Only this verification record was edited after that completed strict run.
Post-write validation uses the identical strict command and must also return
PASS before handoff, so the record itself is covered as a changed input.

The verifier is unchanged from its initially prepared, fully read 287-line
version; SHA256:
`979dceb12ce9418404db429a9d5f2402cad2697410eb3f03dfea66b1041b8420`.
The batch log binds the 15 scope/raw/review file hashes; those reviews bind
all 20 current scientific surfaces. No outcome is inferred from a checksum.

## Recorded preliminary check

The syntax check and a pre-handoff command were run on 2026-09-22:

```bash
node --check papers/380-factor-allocation-history/evidence/verify-batch.cjs
node papers/380-factor-allocation-history/evidence/verify-batch.cjs --pre-handoff --brief
```

Syntax exited 0; the preliminary result was
`PRE_HANDOFF_CHECKS_COMPLETE_NOT_FINAL`, not a final handoff result.
That snapshot checked 32 preserved packages, five fixed anchors, five frozen
prefixes, 12 current new Markdown files and 798 local links including both
entire overviews. Final outcomes, raw/review receipts, missing final artifacts
and new overview handoffs remained pending at that stage. Those preliminary
counts are retained as history, not substituted for the final result above.

Pre-handoff mode can never report final PASS. Missing planned artifacts or
receipts are explicit pending items; invalid existing anchors, links and
submitted receipts still fail. The final result above used strict mode.

## Verified handoff checks

- Preserve all 32 old packages 348–379, five inherited fixed-file anchors,
  and five frozen candidate-card prefixes for 380–384.
- Check the five current IDs across paper, card, README and claim ledger.
  Require an explicit `Outcome:` field on all four surfaces; on the card,
  inspect only the append after its frozen prefix. Other surfaces use their
  first 20 lines. Outcomes come from root's actual results, never from a
  predetermined expectation that all five objects stop or advance.
- Bind all five CP1/raw/final-review hash triples from the batch record and
  all 20 current final-surface hashes to the corresponding final review.
  Internal review markers are artifact checks, not independent proof.
- Check local inline/reference link destinations, LF/final-newline format and
  code-fence balance in all new Markdown files and both entire overviews.
- Recover both opening overview hashes by undoing only the archived F heading
  demotion and discarding the new G handoff block. Old prose stays unchanged.

The batch record's final receipt formats are one row per paper:

```text
| 380 | `CP1_SHA256` | `RAW_SHA256` | `REVIEW_SHA256` |
| 380 | `outcome: ACTUAL SHARED OUTCOME PHRASE` |
```

Repeat for 381–384. The same outcome phrase must appear in each package's four
explicit `Outcome:` fields. Bold/code markup and a final period are allowed;
the underlying phrase must match the receipt. Hash aliases in reviews may
use Paper, Card, README, or optional-FINAL ledger, provided the current hash
is unambiguously bound to that surface.

## Limits

No proof is rederived, no infinite claim is certified by finite checking,
and no numerical experiment or external literature search is performed.
The link check covers local destination existence, not remote availability,
Markdown fragment targets or every feature of a full CommonMark renderer.
Root owns the actual research outcomes and final handoff. Mechanical PASS is
not a candidate-target pass, independent mathematical review or formal Route
coordinate. Old scientific packages, fixed anchors and the verifier were not
modified; no further research round or external action was started.
