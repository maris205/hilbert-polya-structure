# Batch E — reproducibility and mechanical verification

Batch `MEASURED-HISTORY-20260922-E`;2026-09-22.
Final strict verification: **PASS**, after all five reviews and overview integration.

## Scientific evidence versus machine checks

The five [papers and outcomes](../batch-summary.md) contain exact proofs, not
scientific numerical experiments. Each own source, measure, version, actual
arrow convention and control is fixed in its candidate card. There is no
orbit cutoff, precision extrapolation, statistical power claim or downloaded
prime/zero dataset. Proof reproduction consists of checking the stated
infinite sums, Borel identities, finite-product formulas and exact bounds.

The [checkpoint log](../batch-log.md) records actual CP1 releases, raw freezes,
later paper unlocks and raw/review hashes. Each review records its personally
read four final surfaces and their whole-file hashes. This is shared-history
internal model scrutiny, NOT_CALIBRATED, not independent human peer review.

The [read-only verifier](verify-batch.cjs) checks preservation, linkage and
evidence identity. It does NOT decide whether a theorem is true, whether
the lineage is natural, or whether a formal Route coordinate has passed.

## Commands and exact coverage

Run from `arithmetic_symplectic_flow`:

```bash
node --check papers/370-divisor-renewal-clock/evidence/verify-batch.cjs
node papers/370-divisor-renewal-clock/evidence/verify-batch.cjs --brief
```

Omit `--brief` to print all current Markdown input hashes and line counts.
`--pre-handoff` is explicitly NONFINAL and reports missing final artifacts;
it never returns PASS. No command here writes a file or executes old verifiers.
All report files were created with apply_patch, not redirected command output.

Checks include all20 paper/card/claim-ledger/README identity and status surfaces,
the20 corresponding review-bound current hashes,10 frozen raw/final-review
receipts,7 original/clarified card prefixes, local Markdown targets, final LF,
closed code fences,22 unchanged old348–369 package bundles,5 immutable anchors,
and2 previous-overview archives reconstructed byte for byte from their new
handoff position. The original OPEN card header remains historical data;
current status is checked only in its appended post-freeze outcome.

Verifier SHA256:
`fa72d37df234a85d7171e5e6ac2391d8073e28f2f9ed2e6041cc7bed3656caa0`.
Its receipt parser supports clear same-line file aliases as well as basenames;
it binds the CURRENT hash and does not substitute a historical card prefix.
This format compatibility did not modify any frozen mathematical review.

Observed strict output: PASS;5 packages,20 identity/status surfaces,
38 Markdown files,143 local links,7 frozen prefixes,22 preserved packages,
5 immutable anchors,2 preserved overview archives,10 raw/review receipts,
20 review-bound surface hashes, and no pending items. Exit status0.
The report was then updated with those observed totals; the same command
was rerun for that changed input before final handoff.

## Limits and preservation

Local link checks verify file existence, not external URLs or fragment anchors.
Only the new overview blocks are link-checked; the remainder is preserved by
byte hashes. Governance anchors and old papers are not reinterpreted by hashing.
The scope is selected348–369 packages and the specified older283/governance
anchors, not an assertion of a clean or fully hashed repository. Existing
tracked and untracked user work is retained; no Git stage/commit/branch/push
or external publication was performed. Markdown-only research scope is kept.
No sixth round, fresh candidate or formal Route evaluation is authorized here.
