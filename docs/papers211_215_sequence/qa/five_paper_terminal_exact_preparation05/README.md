# P211-P215 exact-five terminal gate - bound preparation 05

This directory contains the unchanged read-only terminal auditor and a complete binding
revision created after all five individual papers became internally complete.
It does not rerun science, reviews, builds or page views. External action
remains `HOLD_EXTERNAL`.

The gate covers exactly P211, P212, P213, P214 and P215.  For every paper it
requires one accepted author replay pair, one accepted Review A replay pair,
one accepted Review B replay pair, physical Round0/Round1/Round2 receipts and
their nonself manifests, two distinct terminal source-only build records, a
root receipt for actual viewing of every final page, authoritative zero-current
finding records, and a final-QA record plus manifest.  Across the batch those
cardinalities are exactly 15 replay pairs and 10 terminal builds.

`INPUT_BINDINGS.json` binds every required P211--P215 evidence role to an exact
workspace-relative regular-file path. The auditor refuses duplicate
paper IDs, duplicate replay roles, duplicate freeze rounds, duplicate terminal
run IDs, symlinks, missing files, unsealed freeze directories, nonzero current
finding censuses, an incomplete central milestone, or an unsealed binding.

Every accepted input is read twice and emitted in `complete_input_pins` with
its path, byte count and SHA256.  Every manifest row is parsed strictly,
checked against exact physical directory membership, and its payload is added
to the same complete map.  Historical failed/HOLD/rejected artifacts are
selected read-only from the batch QA/scouting trees, required to be nonempty,
and pinned without granting them PASS credit.

The only permitted launch is from the workspace root with the clean fixed
environment and isolated system-Python command below. Root must first confirm
that P214 and P215 are individually complete and that the batch/root indexes
say `5 retained / 5 complete / 0 open`.  The resulting status remains
`PASS_EXACT_FIVE_GATE_ROOT_ACCEPTANCE_PENDING`; root must independently receive
the complete output before writing any completion milestone.

```sh
PREP_SHA256=$(sha256sum docs/papers211_215_sequence/qa/five_paper_terminal_exact_preparation05/SHA256SUMS | cut -d' ' -f1)
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC \
  /usr/bin/python3.10 -I -S -B \
  -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/five_paper_terminal_exact_run01/never_created_reader_cache \
  docs/papers211_215_sequence/qa/five_paper_terminal_exact_preparation05/inspect_five.py \
  --expected-preparation-sha256 "$PREP_SHA256"
```

The resulting JSON is still pending independent root reception; command exit
zero alone does not complete the batch.
