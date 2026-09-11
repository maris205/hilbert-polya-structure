# Root reproduction of the adverse independent MNC gate

2026-09-06 UTC. Root actually read the full final candidate report,
source/proof audit, execution receipt, finding ledger and standalone
`MNC_GATE/verify.py`. It imports no author or historical producer and
reads no runtime files. The T1/T2 adapter is complete on the entire
second image, and the audit explicitly preserves the correct global
fibre comparison rather than pretending it is already in Jen's prose.

Two **new root executions of this independent gate producer** each
completed 293,461 assertions. Both child exits, both canonical `cmp`
exits and the pairwise `cmp` exit were zero; each complete stdout is
24,635 bytes with SHA-256
`2443974a2021d24d02b0fd5c16aca292706f5ec6fed838281403fd3d52e86602`.
All stderr/comparator streams are empty. The 29 gate manifest entries
and 17 main context pins passed; root separately checked all three
supplementary pins, including the two absolute installed-tool paths.
The entire gate package was unchanged before/after these runs.

The machine [receipt](RECEIPT.json) records exact commands, input and
output hashes, runtime settings, every exit, and all package files.
**Disclosed harness label error:** that unchanged reusable harness was
originally named `replay_closed_author_pair.py`, and its hard-coded
`kind` field says `AUTHOR_PRODUCER`. In this pair the actual explicit
command and pinned input are `MNC_GATE/verify.py`, the independently
authored gate producer, not `CONTRAST_PROOF_WORK/verify_mnc.py`.
The original receipt is preserved without rewriting its bytes; this
note corrects the role label only. Its numerical executions and raw
comparisons remain valid. This root replay is not a third independent
review: root is a mathematical MNC contributor and only reproduces the
already process-separated reviewer's code.

Disposition: root accepts **NO_ADMISSION** under the unchanged batch
two-axis standard. MNC-V1 remains Critical/open. Preserve the author
theorems, all successful evidence and the adverse gate; no number,
reserve, manuscript, accepted delta or source clearance is created.
