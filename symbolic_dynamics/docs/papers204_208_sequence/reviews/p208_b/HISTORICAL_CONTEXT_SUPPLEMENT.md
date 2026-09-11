# P208 B: exact historical-input preservation for the accepted delta

2026-09-06 UTC. This is an archival clarification requested in root's exact
no-manuscript-change response. No scientific source, initial search receipt,
review proof, verifier, canonical, manuscript or old auditor is rewritten.

The initial history search hashed and searched 1,917 original files, then
snapshotted its 329 matching files. Those original before/after receipts
were valid at the search time. The initial artifact auditor also correctly
checked their current paths at its execution time, and root independently
rechecked them. None of those checks implies that active scout originals
must never change after that historical search.

The delta now preserves every one of the 1,917 original search inputs in
`delta/history_inputs/`, retaining its complete workspace-relative path.
`delta/HISTORY_INPUT_MAPPING.json` maps each original absolute pathname to
the initial search SHA-256 and its exact archived location. Existing matching
snapshots were used when available; otherwise the current original was
copied only after matching the initial search digest. Every copied file was
checked before/after against the same initial hash. All 1,917 current
originals still matched at this actual archiving time, recorded separately
in `delta/HISTORY_ORIGINALS_AT_ARCHIVE.json`.

Subsequent review-evidence reuse resolves these historical references to
the archived bytes. It does not silently substitute newer source content
and does not create a new owner-absence or whole-paper-reading claim.
If newer source content changes an applicable theorem or adapter, that is
a separate source/value issue to inspect; the earlier audit remains an
honest historical record.

The initial B package is also fully preserved. Its original outer manifest
is `delta/initial_snapshot/SHA256SUMS`, SHA-256
`64a58b80ac92f98caff178a34a8ef6199c83eace414c043d72d4ce81eeff78a5`.
Its original FINDINGS bytes are `delta/initial_snapshot/FINDINGS.json`,
SHA-256 `f9c7ef9a99651eb6252231ee0ba15ac75d7348b921698c0ac65326318d31df02`.
`delta/INITIAL_PAYLOAD_MAPPING.json` accounts for all 1,546 original payloads:
the original FINDINGS resolves to that archive, and the other 1,545 payloads
remain unchanged at their original paths. The old outer manifest itself
was a nonself seal and was not one of its 1,546 referents.

The current FINDINGS adds only this same reviewer's accepted-delta state;
the current outer manifest is regenerated only after the original bytes
are archived. No failed or superseded execution receipt is upgraded or
deleted. The initial `REPORT.md`, `SEAL_RECEIPT.json` and `seal_package.py`
retain their original initial-stage wording and predicates. In particular,
that old auditor is not weakened to manufacture a current post-delta PASS.
The new scoped documentary auditor consumes the explicit history/initial
mappings and checks the current delta lifecycle separately.

The complete delta baseline in `delta/INPUTS_BEFORE.json` distinguishes
unchanged live science/runtime/build dependencies from exact historical
document references. Both documentary audit phases recheck every validated
path, all relevant configuration presence/absence, every root response and
replay original, and the complete TeX/resource inventory. There is no
permission to ignore a changed numerical dependency or a missing archive.
The new audit is not a mathematical rerun, source-only build or page view.
