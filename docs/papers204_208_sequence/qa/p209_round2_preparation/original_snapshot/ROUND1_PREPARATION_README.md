# P209 Round1 freezer preparation V2

Status: `PREPARED_NOT_EXECUTED`. This is an infrastructure-only preparation,
not a freezer execution, Round1, manuscript review or new scientific/build/view
evidence. The preparer authored P209 and is not a P209 reviewer. Root owns
original acceptance inspection, read-only preflight, the later actual freezer
invocation and its command/output/exit receipt, independent closure and B
assignment. The project research skill enforces these evidence/authorship
boundaries; external actions remain `OWNER_AMBER / HOLD_EXTERNAL`.

## Preserved V1 and the detected-before-execution correction

This package is the separate sibling `qa/p209_round1_preparation_v2/`.
Nothing was appended to or changed inside the original complete ten-payload
`qa/p209_round1_preparation/`, whose seal remains
`f8396ff69a16f4c215f9a221110c1d039104b1b0764d4f570c52c794036094b1`.
Its earlier source, raw static checks and superseded prototype remain intact.

Root caught a concrete V1 preexecution blocker: its exact live-file set
omitted the already existing `PAPER_MANIFEST.sha256`. This was discovered
by inspection before any freezer invocation, not by a failed freeze.
V2 explicitly includes that unchanged documentary input, validates its
entire prior whole-paper set before target creation and preserves its exact
bytes physically. V2 also binds the now-existing `CURRENT_FINDINGS.json`
as a separate acceptance anchor. The immutable initial `FINDINGS.json`,
`REPORT.md` and all 1,227 initial review payloads are retained unchanged.

The 467-line V2 source has SHA256
`19cf0898e201f25dc5724233ff1cdef59d8a0001d6239fe5d15aeb9212f63c44`.
Exact copied originals and full actual unified diffs are included:

- `original_snapshot/freeze_p209_round0.py`: all 156 original lines,
  SHA256 `95473c820d305410ae042eed50c288fef02244e6ab41234648db641f0dd7866a`.
  Actual raw comparisons against the current original and frozen Round0
  adapter both exited 0.
- `original_snapshot/freeze_p209_round1_v1.py`: exact unexecuted 420-line
  V1, SHA256 `e62f11c0eaed932c364fe2bd44f37cc9a92a4819739fc51d306f41c01a2b0096`;
  actual raw comparison against the sealed V1 source exited 0.
- `ADAPTATION.diff`: complete Round0-to-V2 diff, 33,492 bytes,
  SHA256 `2af53a0e172346685be42d013c4ffa5f633aeb066e07ee6b8f301f455a01009f`.
- `V1_TO_V2.diff`: complete V1-to-V2 diff, 13,014 bytes,
  SHA256 `eb60f87c44df0e3795c1345ea6d00979c8d05617f7a3bd4b608f3f8f59e4284b`.

Both actual diff commands exited 1, as expected for differing files; their
complete stdout exactly equals the saved diff bytes. This is a disclosed
infrastructure adaptation, not a byte-identity claim about the freezers.

## Exact core and eleven physical anchors

The source core is exactly the 1,989 referents of
`papers/209-ordered-fibre-threading/frozen_round0/SHA256SUMS`, seal
`0f77871539b374027ab42910471cc74cefcd570e214a8242ac0a30c7a83e70ba`.
It is copied file-by-file at the same relative paths, without recursive
live-paper copying or a nested Round0. All 1,985 author payloads and original
inner manifests, `AUTHOR_MANIFEST.sha256`, `ROOT_ADOPTION.md`,
`FREEZE_ADAPTER.py`, `FROZEN_LINK_MAP.json` and historical
`PAPER_STATUS.md` bytes remain unchanged. The author seal/alias retains
`9fd20cd746f1ae03c22a87283313248ad79ffcfb9a0f1ea45458937dd5901a0e`.

The following eleven anchors go beneath `frozen_round1/ROUND1_ACCEPTANCE/`.
They are not additions to or rewrites of the historical core manifests.

| Physical name | Original source and manifest basis |
|---|---|
| `ROUND0_CORE_MANIFEST.sha256` | Paper `frozen_round0/SHA256SUMS`; Round0-relative 1,989 core referents |
| `A_REVIEW_MANIFEST.sha256` | Batch `reviews/p209_a/SHA256SUMS`; original A-review-relative basis |
| `A_DELTA.md` | Batch `reviews/p209_a/DELTA.md`; actual accepted delta |
| `A_INITIAL_FINDINGS.json` | Batch `reviews/p209_a/FINDINGS.json`; immutable initial census |
| `A_CURRENT_FINDINGS.json` | Batch `reviews/p209_a/CURRENT_FINDINGS.json`; current accepted zero-open census |
| `A_INPUT_PINS.sha256` | Batch `reviews/p209_a/INPUT_PINS.sha256`; workspace-relative exact Round0 inputs |
| `ROOT_RESPONSE.md` | Batch `P209_A_RESPONSE.md`; exact accepted response |
| `ROOT_DELTA_CLOSURE.actual.json` | Batch `qa/P209_A_ROOT_DELTA_INSPECTION.actual.json`; measured root closure |
| `ROOT_PAIR_MANIFEST.sha256` | Batch `qa/root_replays/p209_a_strict/root_a_pair_01/SHA256SUMS`; original pair-relative basis |
| `ROOT_LAUNCHER_MANIFEST.sha256` | Batch `qa/root_replays/p209_a_strict/launcher_root_a_pair_01/SHA256SUMS`; original launcher-relative basis |
| `PRE_ROUND1_PAPER_MANIFEST.sha256` | Paper `PAPER_MANIFEST.sha256`; original PAPER-relative 3,978 prior referents only |

The unchanged core plus eleven anchors, new `ROUND1_FREEZE_ADAPTER.py`,
new `ROUND1_PROVENANCE.json` and actually used physical historical aliases
give **2,002 + the number of used aliases**. The currently measured one-alias
case plans **2,003 payloads**. Only the new Round1 root `SHA256SUMS` will be
its complete nonself manifest. No future Round1 seal hash is claimed.

## Prior whole-paper manifest and later refresh

Before target creation, V2 requires exact prior whole-paper manifest SHA256
`cd8b345c2e8c7e71afa9d2d2d64e6ca74332828b4447e43ba6894c5a8398a4b2`,
hashes all 3,978 original referents and checks equality with the entire
then-current 3,979-file tree including the nonself manifest itself.
After Round1 is added, V2 rechecks the old manifest bytes and all original
referents, and excludes only Round0/Round1 when checking the original live
set. The old whole-paper file remains in that live set and is not overwritten.

The old manifest is explicitly **not** the complete current-paper manifest
after Round1 creation. Provenance schema `p209-round1-provenance-v2` records
its original live path, original PAPER-relative referent basis, exact hash,
all old referent pins and the new physical
`ROUND1_ACCEPTANCE/PRE_ROUND1_PAPER_MANIFEST.sha256` anchor.
A later root whole-paper refresh must resolve this old hash to that physical
historical anchor, rather than changing historical pins or treating its new
location as the base of its old relative rows.

## Actual A gate and unchanged initial record

`ACCEPTANCE_INPUT_CONTRACT.json` is a schema, not an acceptance record.
The actual fixed root closure now exists and was read as documentary input.
V2 requires its accepted status, P209/input-round-0 identity, three true root
closure flags, zero current findings, unchanged 1,985 author/1,989 core
counts and exact manifest/DELTA/initial-current census/response/pair/launcher
hash bindings. It checks the actual pair and launcher receipt schemas and
complete packages twice; this does not rerun or independently validate their
mathematics, runtime, build or visual evidence.

The current census must identify `/root/p209_a_reviewer`, input round 0,
`ACTUAL_EXACT_NOCHANGE_DELTA`, accepted verdict/delta status, zero counts,
an empty findings list, unchanged scientific inputs and the exact accepted
response. Its preserved initial-review seal must still validate all 1,227
initial payloads, each retained in the complete final 1,342-payload A package.
Initial `FINDINGS.phase` and unassessed `delta_status` wording are deliberately
not rewritten or tested as if they were the new current acceptance.

## Historical alias versus current observation/navigation pins

The original immutable Round0 dependency on the batch `GIT_SYNC_RECEIPT.md`
has SHA256
`af1754c9d6095c0f943b75fe7b9819ebd2b7c4db9609930ca7feccf2934786da`.
Root recovered those exact bytes from an actual prior pushed Git object at
`qa/central_lifecycle_p209_a/GIT_SYNC_RECEIPT.before.md`; its complete
three-payload source packet seal is
`21c8b0fb99e1579d6af82d7da8926e1586715563d4607fbf8bc0727c59702ecb`.
This is not represented as an original-time physical snapshot.
V2 accepts only that exact old path/hash and measured physical alias, refuses
unused/duplicate/broad aliases, and physically copies the used old bytes to
`ROUND1_HISTORICAL_ALIASES/001_GIT_SYNC_RECEIPT.md`.
The unchanged historical link map remains historical; the new provenance
maps all 243 core links to Round1 core or physical old aliases.

A separate role is the **current observation** of the live Git receipt:
`2f6998d2986831fa8776e31e9d336497e6ab37b114d1b13ef94879f3e2271c24`.
`resolve_history` records this current value in the before/after input pins
and in `current_original_sha256`; it is not the historical af175… value.
Copied Markdown also retains its original document origin, and newly checked
navigation targets are not claims of historical target-body identity.

**Before the next central lifecycle update, root must preserve the exact
current 2f699… receipt bytes and explicitly map this observation role.**
The physical af175… alias does not preserve the distinct current 2f699…
observation. Any other mutable current navigation/observation pins require
the same role-aware preservation if changed. Do not relabel these documentary
pins as historical scientific dependencies, silently refresh their recorded
hashes, or append preservation files inside either sealed preparation.

## Actual static evidence and root-only execution

`STATIC_CHECK.py` was run once in an empty, explicit environment using
`/usr/bin/python3.10 -I -S -B`; actual exit 0, completion chunk `b16f89`.
`PREPARATION_CHECKS.json` retains its exact command and complete untruncated
output, including every raw source comparison and both full diff outputs.
The check parses V2 as AST, never imports/calls it, confirms standard-library
imports and no dynamic execution/tree copy, checks acceptance/link gates
precede target creation, and checks the new count, immutable-census and
prewhole/final-live-set conditions.

It actually rechecked 5,477 input paths twice, the complete ten-payload V1
seal, complete 3,978-entry prior paper manifest, 1,989 core/1,985 author
payloads, final 1,342-payload A manifest, all 1,227 original review referents
and all 132 historical external pins with exactly one used alias.
These are static infrastructure, documentary schema and hash/set checks,
not new scientific execution, manuscript review, acceptance or root closure.
Round1 was absent. No freezer invocation or refusal-path test occurred.

Root must read the entire final source/diffs/schema, verify this complete
preparation seal and preflight the fixed inputs before invoking once:

```sh
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/papers/209-ordered-fibre-threading/frozen_round1/never_created_freezer_cache /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p209_round1_preparation_v2/freeze_p209_round1.py freeze-round1-after-accepted-a
```

Only that explicit later invocation may create Round1. Missing/inconsistent
inputs refuse before target creation. Existing freezes are never overwritten.
Partial creation failures remain with their real failure evidence and no
inferred PASS; source/root artifacts are not rolled back or deleted.
A new complete seal is written only after exact copy and unchanged-input
checks. An error after sealing is reported without altering the seal.
Root must retain actual stdout/stderr/exit and independently close the result.
Distinct B, accepted B delta, Round2 and terminal gates remain outstanding.
