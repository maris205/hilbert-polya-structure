# Concurrent navigation updates: explicit historical resolution

2026-09-07 UTC. This is a documentary audit, with zero science executions.

The `finish.py archive` operation physically copied nineteen originals and
passed both complete live and copied `sha256sum -c` commands. After that
capture, root updated the current navigation indexes for P208 completion,
P209 admission and root-closed twenty-second. Root explicitly confirmed
those concurrent edits. The scout did not change either index, P208/P209
science, or the original historical input pins.

An immediate later live check failed exactly:

- `SYMBOLIC_DYNAMICS_STATE.md`;
- `docs/papers204_208_sequence/PIPELINE_STATE.md`.

All seventeen other original entries passed. This failure is not suppressed
or relabelled as a fully unchanged live-input set. A subsequent recorded
`postcheck.py` invocation performs the actual complete live check again
(exit **1**, preserved stdout/stderr), verifies the full nineteen physical
originals (exit **0**) and the one later SP-report pin (exit **0**).

`postcheck/CONTROL_ALIASES.json` explicitly gives each original absolute
path, old expected SHA256, physical historical path and matching old SHA256.
Those two copies are the only substituted locations in
`postcheck/RESOLVED_INPUTS.sha256`; the other eighteen referents remain at
their original live locations. The complete resolved SHA check actually
exited **0**. New navigation copies and complete unified diffs are preserved;
both diff commands exited **1**, meaning real changes, not failed retrieval.
Live inputs were stable during this postcheck.

The narrowly named verdict is `PASS_EXPLICIT_HISTORICAL_RESOLUTION`, not
`PASS_ALL_LIVE_UNCHANGED`, scientific rerun, strict runtime-reuse clearance,
or a new paper/candidate gate. The recorder source hash was unchanged during
its invocation. Full commands, environments, exits, raw output and source
and resolved-reference hashes remain under `postcheck/`.
