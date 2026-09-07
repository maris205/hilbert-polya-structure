# P209 terminal artifact infrastructure revision 01

**Prepared only; target auditor, lifecycle and guard invocations: zero.**
This is a scoped correction after the root's real `initial_01` failure,
not a terminal PASS, new manuscript review or completion. The original
preparation, accepted B, frozen/source/status bytes and LNR source recheck
remain immutable. OWNER_AMBER / HOLD_EXTERNAL.

## Correctly bounded cause

The [original real traceback](../p209_terminal_artifact/initial_01/audit.stderr)
reports a historical `referent_hash` failure for the live Git receipt path.
It does not print the round or expected digest. Full static inspection of
the original 895-line auditor and the exact frozen maps shows that Round1's
`2f6998...` key is already present in B's accepted alias table; Round2's
`a67457...` key is not. The later real private push advanced the live receipt.
The role diagnosis is static source/data reasoning, not a new debug execution
or information fabricated in the original exception.

Two exact roles are explicitly checked and registered:

| Role | Exact expected SHA-256 | Documented original |
|---|---|---|
| Round1 at-freezer-current, reaffirmed | `2f6998d2986831fa8776e31e9d336497e6ab37b114d1b13ef94879f3e2271c24` | `qa/central_lifecycle_p209_round1/GIT_SYNC_RECEIPT.before.md` |
| Round2 at-freezer-current, newly registered | `a67457d5fe6e860040ad5f72a51b839e0220b7b83af22188008c8a74850b1865` | `qa/central_lifecycle_p209_terminal_push/GIT_SYNC_RECEIPT.before.md` |

Each uses the original live path **and expected digest**, with its documented
README, CAPTURE and five-payload package seal. The older `af1754...` receipt
retains its distinct historical role. The unchanged `alias()` still rejects
different bytes for a repeated key. No input hash is refreshed, no path is
chosen by existence or digest search, and no failed check is waived.

## Exact source changes

[SOURCE_EDITS.json](SOURCE_EDITS.json) is an exact replace-once recipe against
the preserved originals. [ADAPTATION.diff](ADAPTATION.diff) concatenates the
three complete real `diff -u --` outputs; their actual exit codes are one
because the files differ. All old source lines and all changed diff blocks
were read. The source-only static check reconstructs every revised byte from
the recipe and proves all unaffected functions literally identical.

| Source | Exact changed blocks | Prepared SHA-256 |
|---|---|---|
| `audit_p209.py`, 976 lines | Revision path/original-preparation binding; new exact original/failure preservation function; two named Git roles in `load_aliases`; its invocation/result field in `main`. All 32 other original functions unchanged. | `49df6b04e21e530d55564293ca7576195bebc9c8fe771b9268acd962d786b0e8` |
| `record_audit.py`, 83 lines | `main` requires only `initial_02`, exact revision file/path, and pins old preparation/failure evidence in the outer before/after map. Three helpers unchanged. | `6f5cf3a5c2771945c8fea0dc6c5b59cbabbf5c19a1b98cefca695f9176c49a9e` |
| `lifecycle_audit.py`, 627 lines | Only `PREPARATION` changes to this revision directory. All 36 functions, lifecycle rules and gate schema unchanged. | `f2477276a738cbf13a08e8fa2824a012d5165f1eb45bf185b9c4f976cedf5269` |

There is no change to literal map, theorem, proof, source subtraction,
canonical, verifier, frozen layout, reviewer acceptance, runtime membership,
build or page-view requirements. The original `pin`, `rich_pin`, `alias`,
manifest/parser, frozen/replay/build/view/link checks remain exact originals.
The lifecycle's `actual_initial_gate()` remains byte-identical: it requires
the actual root gate's measured `auditor_sha256` to match **this revised**
source. No future result, count or hash is supplied in advance.

## Preserved evidence and actual static work

The original preparation seal remains
`3250ea718e5b0f358a8a54ba2365a53732d637a2f9686c017e1767e4cdcc7e51`
with all 347 payloads. The complete original `initial_01` seal remains
`deb48a3ed612ad9e292436e2037a879df37a0a5e2204594702f436c73bbe4b04`
with eight payloads: both executed sources, full empty stdout and unchanged
1,644-byte traceback, full before/after input maps and actual attempt/command.
The root wrapper and child both remain exit 1. The new auditor will explicitly
verify these original failures; they are not renamed PASS or overwritten.

[original_snapshot](original_snapshot) contains 389 exact physical copies,
including the **entire** original preparation and failed attempt, both
documented control packages, relevant instructions and selected exact
provenance/status records. [ORIGINAL_INPUTS.json](ORIGINAL_INPUTS.json) binds
all paths and bytes; all 389 actual raw `cmp` calls exited zero, with full
commands/streams/before-after maps in [INTAKE_CMP_COMMANDS.json](INTAKE_CMP_COMMANDS.json).
The intake and static pass checked all 2,033 immutable paths covering the old
preparation, accepted B, LNR source recheck and failed attempt. Historical
control copies remain at-assignment context, never silently repinned if root
later changes a central index.

[STATIC_RESULT.json](STATIC_RESULT.json) records successful source/schema/
byte checks and all immutable before/after maps. The [actual static receipt](checks/static_01/RECEIPT.json)
has child exit zero, empty stderr and unchanged inputs. Its 26 Python files
were parsed and compiled **without executing their code**; it imported no
target infrastructure. Three real raw diffs returned one with empty stderr.
This is static/documentary verification, not a claim that the revised artifact
gate has run or passed. Earlier orientation/display/schema projection failures
remain explicit in [ORIENTATION_FAILURES.json](ORIENTATION_FAILURES.json).

## Root execution after full source inspection

Do not rerun `initial_01`, edit the sealed original preparation or invoke its
old lifecycle helper for a successful revised result. After reading this
revision's full originals, changed source and complete diff, root may execute
from `/root/autodl-tmp/symbolic_dynamics`:

```sh
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_01/record_audit.py initial_02
```

Only that future invocation creates the exclusive
`qa/p209_terminal_artifact/initial_02` directory. The recorder retains literal
executed sources and full streams even on failure, then seals the attempt.
Any further correction requires another disclosed revision; this package
and the failed attempts remain immutable. `initial_02` does not exist at
this preparation's static check.

Only after an actual complete passing result and root original closure does
root write the artifact report, complete outer package seal and real
`P209_TERMINAL_ARTIFACT_ROOT_INSPECTION.actual.json`. The unchanged dynamic
schema is in [INPUT_CONTRACT.json](INPUT_CONTRACT.json); it must name the
actual accepted `initial_02/audit.stdout` and revised auditor digest.

Before any root lifecycle edit, use the revised helper to preserve the exact
initial package/report/root gate plus pending lifecycle/whole-paper bytes:

```sh
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_01/lifecycle_audit.py prepare
```

After successful preservation, root may change only `ROOT_LIFECYCLE.md` and
its one literal hash line in `PAPER_MANIFEST.sha256`, and write
`P209_FINAL_QA.md` outside the paper tree. All original author status/adoption,
scientific inputs, accepted reviews, freezes, canonical/build/view evidence
and initial artifact bytes remain unchanged. Then the unchanged lifecycle
protocol uses this revised preparation binding:

```sh
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_01/lifecycle_audit.py run lifecycle_01
```

Only following its actual successful full result and root-authored
`LIFECYCLE_REPORT.md` may root close the own artifact-package seal:

```sh
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_01/lifecycle_audit.py seal lifecycle_01
```

These are future root instructions, not commands run during this preparation.
This repair does not complete P209, the open fifth seat or the batch, and
does not authorize Git synchronization or external release. HOLD_EXTERNAL.
