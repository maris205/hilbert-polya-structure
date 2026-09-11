# Root closure of the Round1 documentary update

Status: `ROOT_DOCUMENTARY_RERUN_AND_FULL_ORIGINAL_COMPARISON_PASS`.
Root read the complete [documentary checker](p210_round1_central_update_check/check_central_update.py),
its [full scope and failure history](p210_round1_central_update_check/README.md),
and the exact current/old control changes. All 15 nonself preparation payloads
passed the native seal check. Root then actually ran the unchanged read-only
checker in an owned process group with system Python 3.10, `-I -S -B`, fresh
absent cache and exactly the four declared PATH/LANG/LC_ALL/TZ environment
variables. No old lifecycle receiver, science, TeX or Git operation ran.

The new root run passed 34,632 checks and 1,752 final current-path rereads,
with zero mismatch. Root decoded the entire prior lossless stdout and
compared every result field with the new complete result, excluding only
the two actual start/end timestamps. All remaining fields, including every
input key, full diffs, 579 genuine local-link rows, 71 Round1 mapped links,
old/current whole-manifest roles and theorem-section byte keys, agreed.
This is semantic JSON equality with two declared timestamp exclusions,
not raw equality of the two timestamped JSON streams.

The original decoded stdout SHA256 is
`1f7b761b05f55f94462e341f837a1a7fcf008b581b2644fa4478d3f6b379e5be`;
the complete new raw stdout SHA256 is
`463ff779316fee32df00ca870674dcf3ae8e1f2a0496f518e33465bfe7f6721b`.
See [actual root launch](P210_ROUND1_CENTRAL_ROOT_LAUNCH.actual.json),
[actual completion](P210_ROUND1_CENTRAL_ROOT_COMPLETION.actual.json), and
[full native/output package](p210_round1_central_update_root/RESULT.actual.json).

P204–P209's complete contract sections and P210's full pre-paper-path
ownership/theorem/exclusion body are unchanged. The current P210 1,496-row
whole manifest differs from its physically retained 987-row prior manifest
only by its one lifecycle row and the exact 509 physical Round1 files.
All 493 core/489 author bytes and 13 acceptance anchors remain exact.

The six physical inputs in the [separate captured package](p210_round1_central_update_check/README.md)
fix the comparison instant. In particular, their Git text still describes
the historical rejected-checkpoint/pending-correction state. The later
successful `36e7b365…` checkpoint has its own
[actual root acceptance](P210_CHECKPOINT_ROOT_INSPECTION.md); no result was
backfilled into these old six bytes. Subsequent Git-only index changes
require their own narrow check. Accepted B, Round2 and the terminal paper/
exact-five gates remain incomplete. `OWNER_AMBER / HOLD_EXTERNAL` remains.
