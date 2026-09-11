# Exact observed central-key cardinality

The first index-update receiver correctly reconstructed both whole actual
diffs, then failed because it expected both current navigation files in the
completed lifecycle input ledger. That ledger has the batch index only;
it did not read the current root index. Both navigation originals were still
actually read/copied/raw-compared in the separate preparation mapping.

New-only verify_update_v2.js therefore requires the exact observed one batch
input key and explicit absence of the current stream-root spelling from that
ledger, while preserving and checking both pre-update copies and complete
two-file diff reconstruction. It never invents a second consumed input.
The v1 source and actual failure remain unchanged. The subsequent attempted
sha256sum -c failed because no seal yet existed; no seal PASS was claimed.
This is control-document bookkeeping, not a changed P211 scientific/artifact
dependency or a failure of the accepted paper lifecycle gate.
