# P207 A — accepted root reproduction input

2026-09-06 UTC. Root inspected the complete initial REPORT/FINDINGS,
SOURCE_AND_PROOF, REPLAY_LOG, BUILD_REPORT, actual build/recorded-input
receipts, full 409-line independent verifier, full 185-line author-artifact
auditor and full independent execution recorder. Root is a P207 author;
these executions reproduce nonauthor A evidence, not a third review.

The initial review manifest has 118 complete nonself entries, SHA-256
`434f9d595fcd3a8a47fff00028c05a72cd7d450c4690fa87067836ea1cafe791`.
All 106 frozen-input and ten supplementary source/context pins passed.
The exact manuscript/input role checks and all external referent hashes
were checked again before **and after** the pair, as recorded in
[RECEIPT.json](RECEIPT.json). All 119 review files, including its manifest,
are unchanged. No reviewer package or frozen input was written.

Actual command, workspace cwd:

```sh
python3 -B docs/papers204_208_sequence/qa/replay_p207_review.py docs/papers204_208_sequence/reviews/p207_a docs/papers204_208_sequence/qa/root_replays/p207_a_controlled
```

The launcher, both new mathematical children and all three raw `cmp`
commands exited zero. Each child passed 1,326,321 assertions and emitted
37,971 bytes with empty stderr. Both stdout streams equal the canonical
and each other by raw bytes, SHA-256
`d4c1f4264d628f38c83d85e0532d036056fad89695ab399e25c9d19e6d09243e`.
The independent source SHA-256 is
`2b0e0d9c0bde25c7f9e5dc132b15d58f8ab20f6760c6898ba6abf12e330b5ee2`.
The executed scoped recorder source is snapshotted as `harness_input.py`,
SHA-256 `26679467ce3a39d460c3799406194b82ab78c806ec2902662f7f7399c626b075`.
The verifier has no input-file or repository-code reads/imports. Its finite
and source/value scopes remain exactly those of A; no larger box was used.

## Controlled runtime and preserved earlier pair

Each child ran with `-I -B`: Python ignores PYTHON environment options,
disables user-site imports, and retains optimization level zero. The
actual same-flag runtime probe records `debug=true`, `optimize=0`,
`isolated=1`, `no_user_site=1`, `ignore_environment=1`. Interpreter
executable/hash, version, link-dependency output and non-Python environment
overrides are recorded. This is a disclosed stricter replay setting than
A's inherited environment, not a claim that A used isolated mode.

An earlier root pair in [p207_a](../p207_a/RECEIPT.json) also actually passed
both 1,326,321-assertion runs and raw comparisons. A utility-only audit by
the otherwise reserved B reviewer identified environment-recording and
post-execution external-pin omissions in that first recorder. The actual
read-only current-environment probe found optimization zero and no
PYTHONOPTIMIZE value; the concern was not a failed mathematical assertion.
Nevertheless root preserved that first pair and its old recorder snapshot
unchanged, patched only the root utility, and produced this additional
controlled pair. The utility audit did not inspect P207 mathematics or
start manuscript B. It also motivated explicit manifest/freeze coverage,
strict output-root restrictions and captured failure receipts.

No failed numerical run is relabelled PASS. The earlier helper/path
discovery failures, including an attempted read of the not-yet-synced A
source report in the Git mirror, occurred before the respective work and
changed no evidence. No final build/view or accepted A delta is implied
by this reproduction receipt. `OWNER_AMBER / HOLD_EXTERNAL`.
