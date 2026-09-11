# P209 manuscript-B root replay-pair preparation

Status: `PREPARED_NOT_EXECUTED`. This is a bounded infrastructure preparation,
not an independent manuscript review, scientific run, build, verdict,
accepted delta or terminal acceptance. Root owns any later execution.
Preparation has created no path under `qa/root_replays/p209_b_strict/`.

## Provenance and fixed inputs

The preparer is the twenty-seventh/twenty-ninth finite-system scout, assigned
this separate infrastructure task after sealing the twenty-ninth lane. The
sealed scouting lane and every review, paper, index, prior preparation and
Git state were left untouched. This preparation read the complete actual
sealed B recorder (693 lines), launcher (145), bootstrap (59), verifier
(191) and parameters for adapter requirements. Reading the verifier is
disclosed familiarity, not an independent assessment or proof contribution.
No mathematical implementation was imported or executed. The sealed A root
preparation was fully inspected as the strict infrastructure reference; the
new wrappers are adapted directly from B's own originals, not from A's
mathematical checker.

B declared its initial package immutable before any B file was copied or
bound here. `PIN_CAPTURE.json` records actual whole-package hash and path-set
closure for B's 1,298 payloads and Round 1's 2,003 payloads. B's own
2,004-row `INPUT_PINS.sha256` was parsed and checked to contain exactly all
Round 1 payloads plus its manifest, without duplicates. This is documentary
closure; root must still independently inspect the original proof/source
evidence and preflight B's original package before execution.

| Fixed anchor | SHA256 |
| --- | --- |
| B initial `SHA256SUMS`, 1,298 payloads | `d88b831e60414d47ae0b2afb2583b73d02fc9764877a00952f4a9d90d13488ea` |
| Round 1 `SHA256SUMS`, 2,003 payloads | `c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57` |
| B `record_review.py` | `01623b42719e6159ae31c0e422079929766de61e4f07459c6d579b7f952fa272` |
| B `launch_review.py` | `f190bf2e91b130428a97025bfd708f9a652e80f31ca41706dd81d0259c15693d` |
| B `bootstrap.py` | `dc2f0ef968f2b451ceaf390ac7a8189005881246624a0f94ab64879efa18a80b` |
| B `verify.py` | `d5fd105ddfc162323f06cd530fbd696b0093643a7a0c24c64747cd9c9be30467` |
| B `PARAMETERS.json` | `3b292d4c771041cd07f82c5da2bf534bfa77e67fc971e78df3d08910e937b8e4` |
| B `INPUT_PINS.sha256` | `eee2b677a37c82bc3e99b209f0d310231f1bd0358752724ce7f9d0f3588f200f` |
| Existing B `CANONICAL.json`, 800,966 bytes | `612e1463162deba868cf7cf81d61c8f017713f9b28c4c38b81b00d376bac992c` |

`FIXED_INPUTS.json` is the complete preparation-fixed original input map:
2,021 paths, 812,541 bytes, SHA256
`09a5033597e9b218296f624c256fe2d370331e08269bf1fcc2928352104fb7c8`.
Each entry records exact SHA256, size, resolved path and symlink status.
It contains the 2,004 Round 1 files, B's twelve named source/provenance
inputs, its three `infrastructure_originals` files, mandatory existing
canonical and immutable initial seal. No moving review file is treated as
a fixed input. The eight critical B hashes are also explicit constants in
both wrappers. The full B initial package is checked here and remains
root's independent preflight obligation; the later recorder consumes only
the fixed source/provenance scope, not all B review outputs.

The five physical source/configuration copies in `original_snapshot/` are
the B recorder, launcher, bootstrap, verifier and parameters. Every copy
was compared against its original by an actual `/usr/bin/cmp --` command,
with pinned inputs before/after, exit 0 and zero-byte stdout/stderr. No
checker or bootstrap line was edited. These snapshot copies are provenance,
not the runtime capsule: later capsules contain only unchanged live sealed
B `bootstrap.py` and `verify.py`, pinned and byte-checked before use.

## Exact adapter changes and preserved machinery

| New artifact | Lines/bytes | SHA256 |
| --- | --- | --- |
| `root_record_pair.py` | 707 lines | `0629216719a87b20482911a55a77fcb9e3ce7e53bf774f139f6c147d6a014865` |
| `root_launch_pair.py` | 177 lines | `554e4c269a956ab8bbbd74664e4456563c43ff4265ad4b7897d3cc283343e991` |
| `ADAPTATION.diff` | 15,552 bytes | `0686757cf1a8d00d5ea7205347c164ae7bc974ab836aea91792cfbc4dbf96f08` |

`ADAPTATION.diff` is the complete concatenation of the two actual ordinary
unified-diff outputs, not a selected patch summary. The recorder diff is
8,575 bytes and the launcher diff is 6,977 bytes. Both actual `diff -u`
commands exited 1 (intentional difference), with empty stderr. `checks/`
preserves all seven commands' full argv, cwd, minimal environment, initial
attempts, original exits, exact full streams and before/after input pins.

Changes are fixed input/output paths and role labels; exact pair-only
entry guards; mandatory existing canonical with all adoption branches
removed; new wrapper/fixed-manifest input coverage; and verification of
all 2,021 preparation-fixed inputs before copying or recorder launch,
repeated by the recorder before any child. The launcher also pins itself,
the recorder, fixed manifest, Python and `env`, then checks copied code
against its initial pins. The recorder checks that its original input path
set exactly equals the fixed map, retaining the original full Round 1 seal
check and cutoff guard.

The actual static AST/source-block check reports exactly three changed
recorder functions (`science`, `pair`, `main`) and two changed launcher
functions (`check_closed_recorder`, `main`). All 20 other recorder function
bodies and both other launcher functions remain exact source blocks;
imports are identical. In particular `one_producer`, runtime inventories,
configuration checks, observations, coverage, command/cleanup machinery,
linkage, manifests and the entire build helper are unchanged. Build code
remains unreachable through the exact pair-only entry guard.

The unchanged producer guard uses B schema
`p209-b-ports-constructive-carrier-v1`, boxes n=0..5, total 3,414 states,
`states`/`rows` fields and the B summary keys. The existing canonical was
read only for JSON shape: it declares 54,794 checks and has 800,966 bytes. Those
are facts about sealed existing bytes, not a new execution result. B's
verifier allows default arguments or `--max-n 5`; the unchanged bootstrap
uses the default. No cutoff, predicate, theorem or checker implementation
was modified.

Exactly two fresh scientific capsules would be run later. Each starts
with just `bootstrap.py` and `verify.py`; the original isolation, exact
environment/cwd, exclusive absent cache, pre-child pins, full stdout/stderr,
observed input closure and before/after equality remain. Pair, run1 versus
canonical and run2 versus canonical comparisons are actual `cmp` children
with complete receipts. Canonical adoption is always false, and no branch
writes canonical bytes. The inherited diagnostic name
`ADOPTED_CANONICAL_BYTES` does not permit adoption.

Runtime and configuration inventories are captured at actual invocation,
before children and after completion, as in A/B's original strict recorder;
they are not falsely presented as runtime files executed by preparation.
The scope remains early/late modules and maps, sampled direct-child maps,
conservative Python/OS library, loader, locale, gconv and configuration
inventories. It is not continuous tracing, grandchild tracing or an
OS-hermetic reconstruction. The outer `UNCLOSED_NO_SEAL` policy is retained:
without a verifiable completed recorder receipt and complete seal, keep
attempt/raw streams but produce no settled-stream hashes, final seal or
PASS, and infer no process-tree termination. All failures must be retained.

## Actual preparation checks and seal

`prepare_checks.py` was run only with `pin_inputs` and `comparisons`, in
that order, using `/usr/bin/python3.10 -I -S -B` under the exact four-key
minimal environment. Both completed exit 0. It performs documentary
hashing, manifest/path-set validation, JSON shape checking, five actual
source comparisons, two actual diffs and static AST parsing. It never
imports or executes the B verifier, original infrastructure or adapters.
`STATIC_CHECK.json` records `PASS_STATIC_PREPARATION_ONLY`, five copies,
2,021 unchanged fixed inputs, the function checks, output-root absence and
zero scientific executions. Generated records are not edited afterward.

`seal_preparation.py seal` is the final documentary recheck and one-time
nonself seal writer. It rechecks both complete original seals and the
captured payload pins, all 2,021 fixed inputs, source copies, actual command
receipts/streams and whole diff; it records `FINAL_CHECK.json`, then seals
every payload here. Its `audit` mode is read-only and may be rerun before
root execution. Neither mode imports/runs any original or adapter code.
All files here, including helpers, source snapshots, full streams and
documentary records, are covered by `SHA256SUMS`, excluding only itself.

## Root execution: not performed by the preparer

Root must first independently verify this complete preparation seal, pin
both wrappers and fixed map, read every source/diff line, inspect original
B scientific/proof evidence and independently preflight B's original seal
and input closure. The preparer's static PASS does not discharge these
obligations. A preparation-only read-only audit, from the workspace root:

```sh
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p209_b_root_preparation/seal_preparation.py audit
```

Only the exact later invocation `pair root_b_pair_01` is allowed. It owns
`qa/root_replays/p209_b_strict/root_b_pair_01/` and separate outer receipt
`qa/root_replays/p209_b_strict/launcher_root_b_pair_01/`, under the current
batch. Existing launcher/pair paths, aliases of the output root and
existing exclusive cache prefixes are refused. No other label or build
is authorized. Preparation has created neither the output root nor either
execution directory. From `/root/autodl-tmp/symbolic_dynamics`, the exact
root-only execution command is:

```sh
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/root_replays/p209_b_strict/launcher_root_b_pair_01/never_created_launcher_cache /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p209_b_root_preparation/root_launch_pair.py pair root_b_pair_01
```

An eventual `PASS_ROOT_REVIEW_B_PAIR` would mean root replayed unchanged B
code; it would not be a new independent reviewer, accepted delta or
terminal acceptance. A retry requires a separately disclosed new scope;
do not overwrite this preparation, its originals or any execution output.
No external call, child agent, model override, upload or specialist contact
was made. The project research skill requires the preparation/execution
separation and preservation of prior evidence used here. `HOLD_EXTERNAL`
remains in force.
