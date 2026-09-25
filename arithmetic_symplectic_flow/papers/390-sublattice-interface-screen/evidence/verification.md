# Batch I — mechanical verification record

Batch `NONUNIT-RETURN-20260922-I`; papers390–394; 2026-09-22.
Status: PASS — STRICT FINAL MECHANICAL VERIFICATION.

The [read-only verifier](verify-batch.cjs) checks local artifacts, not proofs,
scientific experiments or formal Route gates. The [batch log](../batch-log.md)
binds actual outcomes, original card prefixes and CP1/raw/final evidence.

## Actual strict result

After all five CP2/CP3 records and their root readbacks were complete, the
strict command below ran from arithmetic_symplectic_flow and exited0:

```bash
node papers/390-sublattice-interface-screen/evidence/verify-batch.cjs --brief
```

```json
{
  "result": "PASS",
  "packages": 5,
  "identitySurfaces": 20,
  "statusSurfaces": 20,
  "markdown": 38,
  "relativeLinks": 966,
  "frozenPrefixes": 5,
  "preservedPackages": 42,
  "preservedAnchors": 5,
  "preservedOverviewArchives": 2,
  "boundEvidenceReceipts": 15,
  "boundSurfaceReceipts": 20,
  "pending": []
}
```

The final workflow metadata and this record were updated after that pass.
The same strict command is rerun after this write before user handoff, so
these changes do not escape verification. No scientific surface or frozen
evidence is changed by this last metadata update.

## Prepared and preliminary checks

```bash
node --check papers/390-sublattice-interface-screen/evidence/verify-batch.cjs
node papers/390-sublattice-interface-screen/evidence/verify-batch.cjs --pre-handoff --brief
```

Syntax passed. Preliminary mode returned PRE_HANDOFF_CHECKS_COMPLETE_NOT_FINAL
and explicit pending files/receipts/overview, never final PASS. The original
prepared verifier has293lines, SHA256
`62e23e3c6a27b3ae5c3f93dc3cf0aee3a4554e43f3d6903271132fa6e9feff27`.
Root has personally read it completely. It only reads local files and writes
JSON to stdout; archived scripts are parsed as anchor data, never executed.

The strict checks require20 IDs,20 matching Outcomes,20 final-review surface
bindings,15 evidence hashes,5 original prefixes,42 old348–389 bundles,
5 fixed anchors and2 overview archives. All passed in the measured run.
It checks local destination existence, not external webpages, Markdown
fragments, mathematical correctness, model independence or publication fitness.
No scientific numerical run, Git write, PDF or external publication is involved.

Final scientific reviews remain internal shared-history NOT_CALIBRATED.
390/391 are definition audits, not mathematical nonexistence proofs; no
checksum promotes them or any other round to a formal Route result.
