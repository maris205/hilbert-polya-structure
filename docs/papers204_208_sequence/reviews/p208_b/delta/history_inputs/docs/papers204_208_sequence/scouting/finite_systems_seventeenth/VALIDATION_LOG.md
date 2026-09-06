# Package verification, not a scientific execution log

No mathematical producer or state enumeration was written or run. There are
no scientific process failures, timeouts, canonical outputs or successful
scientific replay runs to report. The source-discovery limitations and the
pre-creation directory-check exit 2 are disclosed in the source ledger.

The only execution after artifact creation is read-only package validation:

1. From the workspace root, check all ten entries of
   `HISTORICAL_SHA256SUMS` with `sha256sum -c`.
2. From this directory, check all six entries of `SHA256SUMS` with
   `sha256sum -c`.
3. Compare the sorted nonself regular-file inventory with the manifest's
   sorted path inventory; reject missing, extra or duplicate paths.

Checksums pin artifact bytes. They do not establish that every pinned file
was read in full, that a historical experiment was reproduced, or that an
independent mathematical review took place. No claim depends on matching
two scientific runs, because no scientific run was authorized by intake.

This log is sealed before the final package-only check. The actual final
command, exit and output are delivered in the coordinator handoff rather
than editing a sealed artifact to record its own successful seal.
