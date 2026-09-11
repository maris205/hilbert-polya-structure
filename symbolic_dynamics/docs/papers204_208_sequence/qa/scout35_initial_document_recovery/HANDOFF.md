# Scout35 two-document recovery handoff

**LATER_RECONSTRUCTION_FROM_ACTUAL_HISTORY_AND_MATCHING_OLD_PIN**.

Exactly two old documentary versions are now physically available:

| Reconstructed file | Bytes | Historical SHA-256 |
|---|---:|---|
| [REPORT.md](reconstructed_initial/REPORT.md) | 2,927 | a5e5ad74f7e135b7e8c9d3d281b67a04b7a2f1d6ce19f1afb4e17a09d780cb42 |
| [SOURCE_AND_HISTORY.md](reconstructed_initial/SOURCE_AND_HISTORY.md) | 6,858 | a7f4a2a485687075b882f9f88e643ef50675ff326b192cf38b45f31bff44f409 |

Both match their exact entries in the unchanged initial 27-payload
manifest. That source manifest is captured under inputs/ and retains SHA
01dded327a041789a4a0c81f9b69b2f7d8c6d26c22f9c30b57dcb375d7c0ac48.

This does not mean the two initial versions were physically preserved
inside the old final 31-payload package: they were not. Their physical
availability begins with this later supplement. The old Scout35
manifests, documents, proof, code and scientific disposition remain
untouched. No retrospective snapshot date or old all-initial-bytes
preservation claim is made.

## Evidence and exact delta

- [RECONSTRUCTION.actual.json](RECONSTRUCTION.actual.json) contains the full
  current inputs and exact reconstructed texts, with both full old hashes.
- [ORIGINAL_DOCUMENT_EDIT.patch](ORIGINAL_DOCUMENT_EDIT.patch) preserves the
  actual two-document correction hunks for provenance, not execution.
- [ACTUAL_FORWARD_DIFFS.json](ACTUAL_FORWARD_DIFFS.json) contains full new
  diffs from each reconstructed old text to its captured current version.
  Both normal diff exits are one.
- [PHYSICAL_RECOVERY_CHECK.actual.json](PHYSICAL_RECOVERY_CHECK.actual.json)
  records an actual read-only check: both physical reconstructions match,
  all four captured source inputs equal their current originals, and
  applying the three original document hunks in memory reaches both exact
  current document texts.
- [RECOVERED_CHECKSUMS.actual.json](RECOVERED_CHECKSUMS.actual.json) records
  the actual strict two-file checksum check; both entries returned OK.
- [RECOVERY_STATUS.md](RECOVERY_STATUS.md) states the historical gap,
  later-reconstruction boundary and retained parse-time preparation failure.

The exact expected SHA-256 roles are also in
[RECOVERED_DOCUMENTS.sha256](RECOVERED_DOCUMENTS.sha256). They are a new,
explicit two-file role list, not a modified old manifest.

The read-only verifier may be run from the workspace as:

```sh
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3 -I -S -B docs/papers204_208_sequence/qa/scout35_initial_document_recovery/validate_recovery.py
```

It is new documentary code for these two documents only; neither the old
checker nor a modified old checker is imported or executed. No science,
new source search, protected manuscript, index or Git operation occurred.
All file creation used apply_patch within this recovery directory.

The complete nonself recovery seal is RECOVERY_SHA256SUMS. Its final
digest is reported in the handoff message, outside the seal's own
payload to avoid a circular hash claim.
