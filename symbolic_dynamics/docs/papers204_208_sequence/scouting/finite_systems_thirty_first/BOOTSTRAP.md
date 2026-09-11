# Bootstrap evidence and recorder boundary

Working directory for all commands was
`/root/autodl-tmp/symbolic_dynamics`. Before `audit.py` existed, these
commands actually ran through the terminal tool. This file transcribes
their invocation/result; it does not pretend the later native recorder
was already installed. `BOOTSTRAP_DISCOVERY.raw` is the verbatim initial
pathname stdout transcribed from that actual terminal result, not a rerun.

1. `pwd`: exit 0, stdout `/root/autodl-tmp/symbolic_dynamics\n`, empty stderr.
2. Actual discovery argv:

   `["rg", "--files", "-g", "SYMBOLIC_DYNAMICS_STATE.md", "-g", "PIPELINE_STATE.md", "-g", "GIT_SYNC_RECEIPT.md", "-g", "WORKFLOW*", "-g", "SKILL.md", ".agents", "docs/papers204_208_sequence", "SYMBOLIC_DYNAMICS_STATE.md"]`

   Exit 0, empty stderr, complete stdout in `BOOTSTRAP_DISCOVERY.raw`.
   It was overinclusive pathname discovery; none of those returned
   review/archive/protected paths was opened by that discovery command.
3. `mkdir -p docs/papers204_208_sequence/scouting/finite_systems_thirty_first/controls`:
   exit 0, empty stdout/stderr.
4. Three actual `cp --no-clobber` commands, each exit 0 with empty
   stdout/stderr. Source/target pairs:

   - `SYMBOLIC_DYNAMICS_STATE.md` → `controls/SYMBOLIC_DYNAMICS_STATE.md`;
   - `docs/papers204_208_sequence/PIPELINE_STATE.md` → `controls/PIPELINE_STATE.md`;
   - `docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md` → `controls/GIT_SYNC_RECEIPT.md`.

   Every target abbreviation here expands under this scouting directory.
5. A single `sha256sum` command took those three original sources in that
   order, then their three full target paths in that order. It exited 0
   with empty stderr and the following complete stdout:

```text
62eb6631e29d5b47ae5941093707c9bb58fdb916b1fa58d969987dd881e260da  SYMBOLIC_DYNAMICS_STATE.md
29c6884ea88f6c2c5275d132244ad19150f745f896d3419c931fdfdd2cfb9441  docs/papers204_208_sequence/PIPELINE_STATE.md
a67457d5fe6e860040ad5f72a51b839e0220b7b83af22188008c8a74850b1865  docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md
62eb6631e29d5b47ae5941093707c9bb58fdb916b1fa58d969987dd881e260da  docs/papers204_208_sequence/scouting/finite_systems_thirty_first/controls/SYMBOLIC_DYNAMICS_STATE.md
29c6884ea88f6c2c5275d132244ad19150f745f896d3419c931fdfdd2cfb9441  docs/papers204_208_sequence/scouting/finite_systems_thirty_first/controls/PIPELINE_STATE.md
a67457d5fe6e860040ad5f72a51b839e0220b7b83af22188008c8a74850b1865  docs/papers204_208_sequence/scouting/finite_systems_thirty_first/controls/GIT_SYNC_RECEIPT.md
```

6. Three separate actual `cmp SOURCE TARGET` commands used exactly the
   source/target pairs above. Each exited 0 with empty stdout/stderr.
   Only after these comparisons did the first control `sed` read occur.

There were no shell failures during this bootstrap. The later body-scope
failure is substantive and is separately recorded, not hidden behind
successful shell exits. From command 01 onward, `commands/*/receipt.json`
records full actual child argv, cwd, exit, raw output hashes, input count,
recorder hash and timing; complete raw stdout/stderr and input before/after
pinsets accompany every receipt. A later quiet-display patch did not edit
old receipts. `audit_v1.py` and `audit_v2.py` preserve both earlier scripts.

The native recorder is documentary infrastructure, not a scientific
producer or a strict terminal-replay runtime capsule. No mathematical
execution or raw-canonical comparison is claimed.
