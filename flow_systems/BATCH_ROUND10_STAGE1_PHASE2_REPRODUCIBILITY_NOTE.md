# Round 10 Stage 1 Phase-2 correction-chain reproducibility note

Date: **2026-09-02 UTC**  
Scope: **provenance limitation; no scientific or Route content**

The final repository retains the correction manifest, the initial verifier
report hashes, every declared pre-patch hash, every current post-patch source
file, the final verifier artifacts, and the original seats' post-patch
adjudications. It does **not** retain complete copies of the pre-patch
bibliography/inventory files or a byte-complete unified patch for all six
operations.

Consequently, a later third party can independently recompute and verify:

- all 20 current bibliography/inventory/verifier hashes;
- all 116 current source rows, IDs, peer-review flags, and verification rows;
- the six current corrected fields or correction-companion bindings;
- the frozen manifest, receipt, authorization, and final dispositions.

A later third party cannot reconstruct every pre-patch byte solely from the
final tree. In particular, the P30 append-and-limitation-renumbering operations
are retained as exact scoped manifest entries plus pre/post hashes, not as a
stored preimage or byte-complete patch. Therefore references to a pre-to-post
"replay" describe the original verification seats' execution-time historical
replay. They are not a claim that the final repository alone contains every
pre-patch byte required for a fresh external replay.

This disclosed provenance limitation does not change the current-corpus
checks, source counts, source-existence outcomes, support boundaries, or any
of the five `PHASE2_SOURCE_BASE_READY_WITH_WARNINGS` dispositions. It must be
carried forward if the correction history is described in Phase 3 or later.

PREPATCH_COMPLETE_BYTES_RETAINED=false
POSTPATCH_CURRENT_BYTES_VERIFIABLE=true
HISTORICAL_REPLAY=SEAT_ATTESTED
SCIENTIFIC_COMPUTATION=NOT_RUN
ROUTE_STATUS_CHANGED=false
