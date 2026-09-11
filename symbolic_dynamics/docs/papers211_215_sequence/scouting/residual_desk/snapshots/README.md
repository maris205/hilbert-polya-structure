# Exact historical control inputs

The desk read the central state and active batch index before the root's
subsequent lifecycle refresh. Their complete text was copied here using
apply_patch from the actual native read output, then independently compared
as raw bytes with the live original using `cmp --silent`. Both native exits
were zero; see ../SNAPSHOT_NATIVE.json. This preserves the exact version read,
not an edited recovery summary. The root was notified after both comparisons
and may subsequently update the live controls.

| Original workspace-root-relative key | Historical input used by this desk |
|---|---|
| SYMBOLIC_DYNAMICS_STATE.md | snapshots/SYMBOLIC_DYNAMICS_STATE.md |
| docs/papers211_215_sequence/PIPELINE_STATE.md | snapshots/PIPELINE_STATE.md |

../INPUT_PINS.sha256 pins these preserved historical copies, not the later
mutable live keys. All other pinned local contracts/candidate originals keep
their literal current paths. Whole-file pins identify versions; read ranges
remain those in ../REPORT.md. These are desk control snapshots only, not a
Round0/Round1/Round2 freeze or scientific execution capsule.
