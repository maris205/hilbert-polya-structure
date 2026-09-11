# Ready for root read-only review; no checkpoint executed

Current entry: [PLAN.md](PLAN.md), complete [executor](checkpoint.py), and
[preview03/PLAN.json](preview03/PLAN.json). Older preview01/02 remain as
superseded read-only evidence and cannot authorize the revised source.

- Exact selection: 117 files, 3,926,033 bytes; eight sealed lanes, root
  reception, current controls and the two explicitly approved old acceptance
  metadata files. Planned delta: 116 additions and one modification; no
  selected baseline path is missing. These are preview counts, not staged
  or committed results.
- Current plan SHA256:
  `b6118e7ec9956145b2f733da52bbdb26506ff9a893073af3fb1feb01a19112a0`.
- Current preview's complete manifest SHA256:
  `12e849fa73b1e6b9986fa515d3d2d6a58a5fe4bd1fc4f5bda9e76744b856da9e`.
- Current preview actually ran 11 allowlisted local read-only Git queries.
  Complete native stdin/stdout/stderr/spawn/returncode records are beneath
  preview03. It did not requery the remote or mutate Git.
- Eight complete lane seals / 91 payload rows, 152 explicit inherited pin
  rows and 14 protected file roles were read-checked. These are selected
  archived dependencies, not a host or whole-history inventory/copy.
- Pure/static check source [pure_checks.py](pure_checks.py) completed 76
  checks with zero Git commands and zero fixture writes. It did not execute
  capture, stage, commit, push or a live cancellation test.

Future captures use only this exact approved plan/source, freeze the small
selected payload under a fresh `/root` temporary directory, and use an
isolated index. Full unfiltered tree-delta checking proves that nonselected
baseline paths do not change; no complete baseline/object-body stream is
generated. Stage/commit/push require separate actual prior phase seals.
The accepted bare has no origin; only the explicitly verified mirror URL
is used. All failures remain; there is no automatic repair, retry, cleanup,
force push or config write.

No capture/stage/commit/push has been run. Root must approve after reading
the complete current source and exact plan. Current selected controls remain
unchanged from root's 18-closed refresh; any later change requires a new
preview and approval before capture. See [limits](READONLY_LIMITS.md),
including the preserved discovery mistakes and the unexecuted cancellation
correction. `OWNER_AMBER / HOLD_EXTERNAL`.
