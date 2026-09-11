# P207 B — root's actual controlled fresh pair

2026-09-06 UTC. **PASS**, two new mathematical executions by root of
the closed nonauthor B checker; not another independent review or an
accepted delta. The full [machine receipt](RECEIPT.json) and every raw
stdout/stderr are retained in this directory.

Actual command, from the workspace root:

```text
python3 -I -B docs/papers204_208_sequence/qa/replay_p207_review.py docs/papers204_208_sequence/reviews/p207_b docs/papers204_208_sequence/qa/root_replays/p207_b_controlled
```

Both fresh children passed **2,158,999 assertions**, each with the full
1,558,382-byte canonical output, SHA-256
`b7206f01180dcbe5eca24dbaec67cc96ae5dc80f86004455d382e7723c786fda`.
The actual two producer/canonical comparisons and pair comparison all
exited zero. All 14 recorded commands exited zero and all stderr streams
were empty. The actual `-I -B` runtime probe records optimize=0,
debug=true, isolated=1, no_user_site=1 and ignore_environment=1.

Before and after the pair, all 118 nonself B package entries, 106 exact
physical Round1 inputs and 144 context inputs passed. The full package
snapshot (119 files including its manifest) was unchanged. No B file
was written by this replay. Root separately checked all seven
supplemental read pins, with exit zero.

Before the first B root run, the scoped replay utility was adapted to
require B's actual `CONTEXT_PINS.sha256`, while A requires its existing
`CONTEXT_SOURCE_PINS.sha256`. The previously optional A-only filename
would not cover B's differently named context list. No incomplete-context
B root run was made. The exact new utility is retained as
`harness_input.py`, SHA-256
`aa6eb9cccb7d0e9a4fc3ef662def02c506a7b7ce8dd9a4bf63d79ea76b9e462d`.
Historical A receipts and their copied utility versions remain unchanged.

Root read the complete B initial report, finding census, 444-line
proof/source reconstruction, source-access record, 507-line standalone
producer, 155-line execution recorder, 298-line artifact auditor and
build/replay records. This original-evidence inspection and the fresh pair
support a response to B; they do not close inaccessible source bodies,
LNR-S1, final paper gates, global priority or external release.
`OWNER_AMBER / HOLD_EXTERNAL`.
