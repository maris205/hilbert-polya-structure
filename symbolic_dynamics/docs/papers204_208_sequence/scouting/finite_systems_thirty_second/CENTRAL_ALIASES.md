# Exact historical control aliases

The three intake controls were physically copied before first body read.
All initial live/copy hashes matched the SCOPE.md values. Root later
changed its live state and pipeline; they are not called unchanged.
Commands 18–20 performed actual raw `cmp` with these exact root-preserved
historical paths, with before/after input pins and all comparison exits 0:

| Intake filename under controls/ | Root historical alias under docs/papers204_208_sequence/qa/central_lifecycle_p209_b_initial/ | SHA-256 |
|---|---|---|
| SYMBOLIC_DYNAMICS_STATE.md | SYMBOLIC_DYNAMICS_STATE.before.md | 62eb6631e29d5b47ae5941093707c9bb58fdb916b1fa58d969987dd881e260da |
| PIPELINE_STATE.md | PIPELINE_STATE.before.md | 29c6884ea88f6c2c5275d132244ad19150f745f896d3419c931fdfdd2cfb9441 |
| GIT_SYNC_RECEIPT.md | GIT_SYNC_RECEIPT.before.md | a67457d5fe6e860040ad5f72a51b839e0220b7b83af22188008c8a74850b1865 |

An actual later live hash check, before commands 18–20, observed STATE
`94cc7fa657ecee1d4b3d18b26d05813b8b5e3979f127f62ea8e77bfaa82640e0`
and PIPE
`a1ad9005e147bef705761f16ae861a52b392fc2020fa46af7bb86cce4f52e7bd`.
These were not substituted for initial inputs and are not dependencies of
the scientific proof or pilot. The live Git receipt still had its intake
hash at that check; no new Git action was performed by this scout.
