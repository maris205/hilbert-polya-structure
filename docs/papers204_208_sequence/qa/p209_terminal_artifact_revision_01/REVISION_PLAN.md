# P209 terminal artifact infrastructure revision 01

2026-09-07 UTC. Root-authorized response to the **actual** `initial_01`
artifact failure. This revision is preparation only. It does not run an
auditor, lifecycle helper, guard, scientific producer, build, renderer or
view. All writes are confined to this new revision directory. No children,
Git, central edit or acceptance creation. OWNER_AMBER / HOLD_EXTERNAL.

## Exact correction

The original auditor, recorder and lifecycle helper were read completely
(895, 79 and 627 lines). The failed executed source is preserved, not fixed
in place. Its `frozen_and_author()` reaches the full frozen provenance map
and correctly rejects an unavailable historical Git receipt at its changed
live path. The root wrapper and child both actually returned exit 1.

Explicitly verify and register only these two original-path-plus-hash roles for
`docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md`:

| Expected historical hash | Documented physical original |
|---|---|
| `2f6998d2986831fa8776e31e9d336497e6ab37b114d1b13ef94879f3e2271c24` | `qa/central_lifecycle_p209_round1/GIT_SYNC_RECEIPT.before.md` |
| `a67457d5fe6e860040ad5f72a51b839e0220b7b83af22188008c8a74850b1865` | `qa/central_lifecycle_p209_terminal_push/GIT_SYNC_RECEIPT.before.md` |

These are at-freezer-current documentary observations, distinct from the
older `af1754...` historical receipt. Each path is explicitly bound by its
original README and CAPTURE record. Missing files or wrong digests still
fail; no fallback, search-by-hash, weakened parser or refreshed old pin.
Static inspection found that the first key already exists in the accepted
B alias table. Its explicit registration is a same-byte reassertion, not
a second new key. Round2's `a67457...` key is absent from that B table;
the old traceback does not itself identify a round, so the missing Round2
role is a static source/data diagnosis, not an invented observed trace label.

The new auditor's `PREPARATION` points here. It additionally pins and checks
the unchanged 347-payload original preparation, and the complete actual
`initial_01` failure (executed sources, streams, inputs, command and seal).
The new recorder accepts only `initial_02` and writes that new attempt only
after root's complete source inspection and actual invocation. The lifecycle
helper changes only its preparation-directory binding, so its existing
dynamic root-gate schema must bind the actual revised auditor source hash;
no future hash/result/count is prefilled.

All unaffected integrity/freeze/review/replay/build/view/link/lifecycle
functions must remain literal originals. Full raw diffs and static source,
schema, original-byte and snapshot checks are required before sealing.
If full source inspection exposes a broader issue, communicate it before
expanding this change. The original 347 package, accepted B and LNR source
recheck remain immutable. Root owns execution, reports and lifecycle closure.
