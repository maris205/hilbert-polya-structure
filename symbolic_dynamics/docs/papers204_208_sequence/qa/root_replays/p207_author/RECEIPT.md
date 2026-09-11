# Root's actual P207 author-code pair

2026-09-06 UTC. Root read all 748 producer lines, the entire 241-line
recorder, complete author receipt and exporter, and original mathematical
proofs. This is a root replay of author code, not a new independent review.

Actual command, workspace cwd:

```text
python -B docs/papers204_208_sequence/qa/replay_p207_author.py papers/207-upper-neighbor-rank-dynamics docs/papers204_208_sequence/qa/root_replays/p207_author
```

The scoped harness checks P207's closed 85-entry author-owned seal, copies
the standalone producer/canonical outside the paper, and executes two fresh
children under recorded settings. Both children completed 1,384,012
assertions, with empty stderr. Both actual raw canonical comparisons and
the pair comparison exited zero. Every one of the 85 inputs was unchanged.
The [complete receipt](RECEIPT.json) records every command, exit, dependency
pin, input/output byte size and hash. Both outputs are 288,808 bytes,
SHA-256 `306d4e7dea07ad10234f06c69912561425792ed61fadeff3b165b09d1a106992`.
The producer hash is
`5018b0fe6d6a032e0eadeb7cd53a6de47c789193580fa1707312b592cd4a3c93`.

The adapter is needed because this paper has a closed author-owned seal
and nested certificate provenance, not the historical package-wide
MANIFEST/INPUT_PINS layout. No old parser, receipt or manifest was changed.
The 30/36/9-entry nested initial/pair/export manifests and both 17-entry
live provenance pin lists were additionally checked in their exact bases.

Two earlier manual hash-inspection commands used the wrong cwd: first the
paper-relative 85-entry owned seal was checked from the workspace, and then
the pair-relative 36-entry manifest was checked from the paper directory.
They failed path resolution (the latter found only the same verify.py name).
They are not successful integrity checks and were not producer executions.
The correct paper/attempt-relative checks above and in the root harness
passed; no target bytes or old receipts were edited to make them pass.

The finite local certificate remains a declared computer-assisted premise.
No source gap, manuscript finding or external HOLD is closed by this pair.
