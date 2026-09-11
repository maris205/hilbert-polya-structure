# P215 physical Round0 accepted

2026-09-11 UTC. `ACCEPTED_PHYSICAL_ROUND0`. The once-authorized no-clobber
copy actually ran at `c391c0`, exit 0, with no continuing session. The exact
request and complete native output are preserved in `ACTUAL_NATIVE.json`.
It checked all 39 bound inputs before and after copying, copied and compared
37 fixed payloads, reproduced their nonself manifest and emitted the expected
copy-complete marker. This was not a scientific run, build or review.

Root's separate read-only check at `8b5998`, exit 0, received the physical
tree independently. All 37 source/destination whole-RAW pairs are equal. The
tree contains exactly 37 payload files plus `SHA256SUMS`, exactly the four
declared child directories `evidence`, `sections`, `sources` and
`verification`, zero symlinks and zero other node types. Payload files total
3,026,897 bytes; all 38 files total 3,030,152 bytes.

The 37-entry directory-relative nonself manifest reproduces byte-for-byte and
has SHA256
`ba66c3f0b3cbcb05627017e71cf0323273e078a7c20dd429480a6c247dbdf20c`.
`PHYSICAL_NATIVE.json` preserves the complete independent request and result.
The 2,724,478-byte canonical remains
`d8a654f53890a94736bb03c1aceaee3975cd53580fa5d212b3482f035a5df405`;
the adopted six-page 200,910-byte PDF remains
`68b00073dda65e211dfb1ff518729df81b5631b0a75301b37cf6d7465e9f6784`.
A later combined syntax/input check stopped immediately because `jq` is not
installed, before it parsed either JSON file or reached the input check. A
read-only Node `JSON.parse` check of both unchanged native records then passed;
the strict input check also passed separately. No freeze command was rerun.

Lifecycle prose was accepted before the copy and the three old originals stay
physically preserved. Run01's four-TFM resource HOLD, the V1 checker path
failure and the corrected later summary read remain historical failures, not
retroactive PASSes. Frozen prose truthfully retains its pre-copy pending
status; this later receipt is the authority for physical Round0 acceptance.

Review A/B, accepted deltas, Round1/2, terminal replays/builds/views, paper
completion and the exact-five batch gate remain pending. No central index,
Git state, external manuscript, publication, submission or specialist contact
was touched. `OWNER_AMBER / HOLD_EXTERNAL`.
