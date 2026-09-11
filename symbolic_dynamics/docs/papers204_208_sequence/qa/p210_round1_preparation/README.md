# P210 Round1 freezer preparation — root execution only

This is a bounded PREPARATION, not a physical freeze, another independent
review, or paper/batch acceptance. The freezer has never been imported or
executed, including refusal paths. Only `static_check.py` ran: native exit 0,
30,878 reported checks, 1,649 bounded current inputs fully reread unchanged,
489 complete live/Round0 author byte comparisons and two complete root
canonical raw-output comparisons. Its entire actual tool result, including
the untruncated combined output, is preserved in
[STATIC_01_NATIVE.actual.json](STATIC_01_NATIVE.actual.json). No separate
stderr capture or syscall trace is claimed. There were no static failures.

The AST/data check is implemented separately, never imports/executes the
freezer, and is not a test of the freezer's runtime behavior. It checks the
complete current 493-payload Round0, 552-payload accepted A, 59-payload root
strict pair and 987-payload pre-Round1 whole manifest, plus all 484 initial A
payloads under the two exact documentary aliases. No large host-input audit
was rerun or copied into this preparation. Existing root scientific, build,
view, runtime and resource-membership evidence is reused only under the
actual hash-bound root acceptance, not recomputed or newly certified here.

## Pinned authority and source

The root-owned actual closure is
`../P210_A_ROOT_DELTA_INSPECTION.actual.json`, SHA256
`38e5ca5009a583f5b126a29b60a98d9a936e28cf62d4c800310b98fec49d1650`.
It exists and passed the independent static contract check. The explicitly
named [contract](ROOT_CLOSURE_CONTRACT.json) is only a required-field schema,
not a placeholder attestation. [INPUT_PINS.json](INPUT_PINS.json) contains
28 exact direct input hashes, including this actual closure and all four
root evidence referents. Full manifest referents are checked separately.

The final [freezer source](freeze_p210_round1.py) has 441 lines, SHA256
`2be483fc6a03be1e64bce7f800a301a0e5b398fa6107cb4678c5c891eb5b23fd`.
Its infrastructure was adapted only after full reading of the original
P210 Round0 and P209 Round1 V2 sources; their exact hashes are in the direct
pins. No original science checker, recorder, auditor or freezer was run by
this preparation. The independent [static checker](static_check.py) is
SHA256 `01132d60c7f4914ca12023024c0a836164676585b17bd1720d82733b2053fe3c`.

## Exact future action

Only after the root independently accepts this final source and complete
preparation seal, run once from `/root/autodl-tmp/symbolic_dynamics`:

```sh
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/papers/210-weakly-increasing-run-aggregation/frozen_round1/never_created_freezer_cache /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p210_round1_preparation/freeze_p210_round1.py freeze-round1-after-accepted-a --expected-root-closure-sha256 38e5ca5009a583f5b126a29b60a98d9a936e28cf62d4c800310b98fec49d1650
```

The cache path must be absent and remains unwritten under `-B`. The launcher
provides exactly four safe environment values. The program checks names
before reading those four values and never serializes inherited values.
Actual closure hash, typed fields, two precise A aliases, all direct and
manifest inputs, exact current E1 census, all 57 original Markdown link
roles, 33 exact original external pins, 14 anchor Markdown links and disk
space must pass before the first `TARGET.mkdir()`.

The only target is the currently absent
`papers/210-weakly-increasing-run-aggregation/frozen_round1`. The plan is
493 unchanged Round0 core payloads, 13 physical acceptance anchors, this
freezer source and one provenance JSON: 508 nonself payloads plus one seal,
509 physical files. Every physical copy uses exclusive creation and full
source/destination byte equality. All original inputs are pinned and fully
reread before the new complete nonself seal. The old carried
`FROZEN_LINK_MAP.json` is unchanged historical Round0 evidence; the new
Round1/core and anchor resolution maps are explicit in the new provenance.

The 13 anchors are the Round0 seal; accepted A seal and Delta; initial and
current findings; reviewed input pins; root response and actual final
closure; root strict-pair seal; the pre-Round1 whole manifest and lifecycle;
and the physically preserved initial A seal and Delta. Initial Delta links
retain its original `reviews/p210_a/DELTA.md` origin, not its history-copy
directory. The two initial A aliases never substitute for any of the 33
Round0 external originals: no Round0 historical alias fallback exists.

## Preservation and remaining gates

No live author bytes, author seals, Round0 bytes, lifecycle or whole manifest
are changed. The old 987-entry whole manifest is complete BEFORE target
creation only. The exact pre-update lifecycle body
`bf11c369b64eb1d76b4d0dfc0afe603f0970049b1e0f2bb4a0b1533355da5a32`
is physically anchored, including its historically correct pending text.
The root separately owns subsequent live lifecycle/whole-manifest updates
and must use this precise old-byte anchor when interpreting the old seal.

An existing target is always refused. Before creation, failure produces only
an actual output diagnostic. After creation, partial outputs are preserved;
an exclusive `ROUND1_FAILURE.json` is added only if no seal exists. There is
no rollback, deletion, overwrite or automatic retry. A failure after a seal
exists leaves that sealed tree untouched; the root must inspect the actual
result, not infer success from a directory alone.

One resolved Major E1 remains in full: the authenticated old recorder
source/prehash and three old parent start times remain unavailable. No
secret-bearing backup or recovery claim is introduced. Physical Round1,
distinct materially different B, accepted B delta/Round2, terminal build
pair/all-page views, and paper/five-paper completion remain separate gates.
`OWNER_AMBER / HOLD_EXTERNAL` remains in force.
