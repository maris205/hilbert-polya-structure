# P208 root reproduction of sealed author evidence

2026-09-06 UTC. PASS_ROOT_P208_AUTHOR_REPLAY_PAIR. This is root's actual
reproduction of author code, not an independent manuscript review.

Root read the complete manuscript, proof package, standalone 371-line
verifier, source/framing documents and author recorders before execution.
The scoped recorder was then actually run as:

```
python -I -B docs/papers204_208_sequence/qa/replay_p208_author.py
```

The [actual receipt](../../docs/papers204_208_sequence/qa/root_replays/p208_author/RECEIPT.json)
records ten actual child commands, all exit zero: two isolated producers,
two canonical comparisons, one pair comparison, before/after runtime and
dynamic-link probes, and one raw runtime comparison. Each producer started
in its own directory containing only verify.py and left that source unchanged.
Python optimization was zero, isolated mode and no bytecode were enabled;
the actual interpreter/module files, tools, environment and resolved shared
libraries were captured and rechecked. This is not a hermetic historical OS.

Each run covered all 2,055 triangulations for n=3,...,10 and passed 62,101
assertions. Both complete graph/source-set outputs were compared with the
4,974,397-byte canonical by actual /usr/bin/cmp and with one another.
Canonical SHA-256: d4667d1b9be183993f48a49a5fda51f5a519cb29a473d2dbd680caa33c8ab395.
Verifier SHA-256: 12653e9025931fa9424bf06aef7c7f40ffb9a47f95df6bf5dd5b5a50ca57578b.

The before/after dependency capture checked all 483 author-seal referents,
the immutable author manifest itself and all seven original workspace
context pins: 491 named inputs, unchanged. The complete replay package has
40 nonself manifest entries. A later
[root artifact inspection](../../docs/papers204_208_sequence/qa/p208_round0_input_inspection_v2/RECEIPT.json)
rechecked every referent, both author input snapshots and current after
maps, all recorded commands/streams, probes and runtime dependencies, and
performed fresh raw author-pair/root-pair/PDF-pair comparisons. That later
inspection is not a new mathematical execution.

The historical origin archive in that inspection preserves the seven exact
admission-time workspace bytes. In particular, FINAL_THEOREM_CONTRACTS.md
is a mutable batch ledger; its original hash describes those historical
bytes, not any future expanded ledger. A future reuse must explicitly
resolve such context pins to the archived version and separately inspect
the changed live context. Neither the sealed author pin list nor old replay
receipts may be silently updated to hide this distinction.

All-size claims rest on the deductive proof and subsequent independent
review, not these finite boxes. OWNER_AMBER / HOLD_EXTERNAL.
