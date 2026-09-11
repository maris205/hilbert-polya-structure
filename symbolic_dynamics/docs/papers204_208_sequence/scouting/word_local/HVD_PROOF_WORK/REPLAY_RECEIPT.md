# Actual author replay receipt

2026-09-06 UTC. Cwd for every command below:
`/root/autodl-tmp/symbolic_dynamics`.

Both original successful executions and both fresh replays exited 0.
Complete stdout is retained, including trailing newlines, in the four
JSON files below. These are actual executions, not hash-only refreshes.
No stderr diagnostic or scientific assertion failure was returned.

| Entry point | First stdout | Fresh second stdout | Bytes each | Raw comparison |
|---|---|---|---:|---|
| `verify_partial_theorems.py` | [PARTIAL_CANONICAL.json](PARTIAL_CANONICAL.json) | [PARTIAL_REPLAY.json](PARTIAL_REPLAY.json) | 4099 | `cmp` exit 0, empty stdout |
| `probe_sentinels.py` | [SENTINELS_CANONICAL.json](SENTINELS_CANONICAL.json) | [SENTINELS_REPLAY.json](SENTINELS_REPLAY.json) | 8572 | `cmp` exit 0, empty stdout |

Actual scientific replay commands, each exit 0:

```text
python -B docs/papers204_208_sequence/scouting/word_local/HVD_PROOF_WORK/verify_partial_theorems.py
python -B docs/papers204_208_sequence/scouting/word_local/HVD_PROOF_WORK/probe_sentinels.py
```

Actual raw-file comparison commands, each exit 0 with no stdout:

```text
cmp docs/papers204_208_sequence/scouting/word_local/HVD_PROOF_WORK/PARTIAL_CANONICAL.json docs/papers204_208_sequence/scouting/word_local/HVD_PROOF_WORK/PARTIAL_REPLAY.json
cmp docs/papers204_208_sequence/scouting/word_local/HVD_PROOF_WORK/SENTINELS_CANONICAL.json docs/papers204_208_sequence/scouting/word_local/HVD_PROOF_WORK/SENTINELS_REPLAY.json
```

`sha256sum` returned these actual matching hashes, also at exit 0:

```text
b2e5f2f55c93242ae7a71a94689fdab26f6fb96d2cad532fa3dcf80447de3a00  PARTIAL_CANONICAL.json
b2e5f2f55c93242ae7a71a94689fdab26f6fb96d2cad532fa3dcf80447de3a00  PARTIAL_REPLAY.json
04456889d237746ef4f1053491e701b0b18c1e1db45f56c17cee8d647894299d  SENTINELS_CANONICAL.json
04456889d237746ef4f1053491e701b0b18c1e1db45f56c17cee8d647894299d  SENTINELS_REPLAY.json
```

The partial run checks exactly 50,069 words in the original six HVD
boxes, 21 path-fibre formula instances, 289 reduction inputs and 826
active-site equalities. Its length-seven embedding is one explicitly
derived fixed word. The sentinel run checks four named input words
with seven assertions, including the source-given noninjectivity pair
and the derived length-nine edge-count increase. No full new box,
six-rule atlas, cycle census or all-target fibre histogram was run.

These numerical PASS results are confined to the stated propositions
and examples. The admission disposition remains HOLD_PROOF. Neither
the author nor root is an independent reviewer of Proposition 3.
