# P207 author replay evidence and root confirmation

The [author execution record](AUTHOR_EXECUTION.md) preserves the actual
initial production and two additional runs, each with 1,384,012 assertions,
all child/raw-comparison exits zero. The complete raw standard output is
CANONICAL.json (288,808 bytes), SHA-256
`306d4e7dea07ad10234f06c69912561425792ed61fadeff3b165b09d1a106992`.
The two flat files under author_replay/ are documented copies of that same
pair, not extra executions. The author's immutable 85-entry seal includes
both original nested runs, source snapshots, pin lists and exporter evidence.

Root then fully read the paper producer and recorder and performed
[two further actual runs](../../docs/papers204_208_sequence/qa/root_replays/p207_author/RECEIPT.md),
again each 1,384,012 assertions with byte-exact canonical equality and
empty stderr. The entire 85-entry author input set stayed unchanged.
Nested 30/36/9 manifests and both sets of 17 provenance pins also passed
in their correct bases; the two earlier manual wrong-cwd diagnostics are
explicitly preserved in the root receipt. No numerical failure is hidden.

The new P207-specific replay/freeze adapters support the paper's declared
finite proof-certificate layout and retain complete provenance; they do not
relax or rewrite the inherited generic schema. Root is a proof contributor,
so the new pair is author-level confirmation, not manuscript A/B.
No prior gate/source report is replaced by these numerical outputs.
OWNER_AMBER / HOLD_EXTERNAL.
