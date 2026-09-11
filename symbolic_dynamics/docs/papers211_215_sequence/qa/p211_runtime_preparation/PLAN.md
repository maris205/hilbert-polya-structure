# P211 runtime protocol — implemented infrastructure, production HOLD

2026-09-08 UTC. Owner: /root/round211_rational_scout. Only this preparation
directory was writable. **PREPARED_AND_PURE_TESTED / ROOT_APPROVAL_PENDING**.
This implements the prior [readiness plan](../runtime_readiness/PLAN.md);
it neither approves nor invokes a P211 scientific run, canonical, build or review.

## Frozen implementation and accepted baselines

The complete P210 B runner and P209 outer launcher were directly read again,
together with their original acceptance reports. Exact physical baseline
copies remain under `baseline/`. Four final native comparisons verify both
copies and both old preparation-to-actual-execution-copy identities.

`runtime_core.py` (285 lines) retains 14 accepted P210 B functions unchanged
by AST, including owned-group settlement, exclusive raw writes and refusal to
seal UNFINALIZED native output. Only `command` is adapted: explicit
cwd/deadline/stderr policy, receipt PID/epochs, truthful failure reception and
a conservative non-OSError pre-return exception branch. That new branch
retains ATTEMPT/UNFINALIZED facts without inventing a native exit or hashing
unknown-writer streams. The complete source relationship is in
`REUSE_MAP.json` and discovery02's native `02_core_diff/stdout.raw`.

`p211_runtime.py` (539 lines) supplies four separate process roles:
outer native capture -> launcher -> recorder -> source-only child.
The complete P209 baseline-to-adapter diff is retained in discovery02's
`02_outer_adapter_diff/stdout.raw`; this is a disclosed new adaptation of
its complete-stream/closed-child envelope, not an unchanged P209 launcher.
No old scientific implementation is imported, copied into a capsule or run.

Current execution-source hashes:

- `runtime_core.py`: 2fd41cfac779f8d5f4e23089fcc9f2b6b041cbebe19e7003b2db6b4815909934
- `p211_runtime.py`: bff2dcf25ee846b04eac0bbd46eb7b3e58c728c6d7e8e9ce591c9cef1ae4e421

Root's first complete source reading preceded the device correction.
The **four exact first-draft-to-final diffs** are therefore separately
preserved in `final_checks01/commands/01_revision_diff_*/stdout.raw`.
All have actual native diff exit 1 and empty stderr. The pre-correction
executable sources remain in discovery01/tests01 physical source snapshots.

## Exact bounded input plan

Use `discovery02/RUNTIME_LOCK.json`, SHA256
1499a93909e39b49c16408985053936b7eb7efcf664e91fd75fa77de607be2ab
(144,329 bytes). It contains **122 lexical/resolved ordinary-file keys**,
not a recursively copied runtime tree. Selection combines inspected
infrastructure imports, the declared standalone science import interface
`itertools,json,math,sys`, four separately launched import-only probes,
selected executable/extension ELF linkage and explicit configuration.

The lock includes interpreter/native utilities, observed source/extension
modules and mapped files, loader configuration, locale and gconv resources,
and applicable zip/venv/path-injection absence. Both previously omitted
launcher resources, `LC_CTYPE` and `gconv-modules.cache`, are explicit.
Locale/gconv/config direct-directory membership is recorded; gconv's whole
module tree is not copied or blindly hashed. Nine declared loader search
directory presence/type/resolution/symlink states are **actually rechecked
before and after** every stage, not merely stored in the lock.

`/dev/null` is a separate **character-device configuration role**, including
major 1, minor 3 and mode. It is not treated as a regular hashed file.
The infrastructure-only O_RDWR DEVNULL open is allowed and recorded;
scientific ordinary writes and scientific process/signal audit events are
refused. Device/configuration states are recaptured with the input closure.

Every Python layer must actually have exactly:
`PATH=/usr/bin:/bin, LANG=C.UTF-8, LC_ALL=C.UTF-8, TZ=UTC`,
system Python 3.10 with `-I -S -B`, optimization zero and a distinct
nonexistent `-X pycache_prefix`. Actual environment, cwd, interpreter argv,
flags, import path, encodings/locale and cache state are recorded.
All actual fixture-stage original argv were separately checked against their
exact launch vectors. Module/open checks reject consumed existing bytecode;
unknown external ordinary files or changed declared configuration fail.
Native `ldd` internally sets its documented tracing variables according to
its pinned script; this is not a claim that every native grandchild has ENV4.

The probe does **not** read/import the scientific source. Root must inspect
its entire static/conditional import and data closure before signing a role
binding. The current adapter deliberately supports only a two-file,
standalone source/parameter interface. Additional A/B imports or local helpers
require a separately reviewed bounded revision/lock; they are not dropped
from the dependency set or imported speculatively here.

## Root-owned author binding and exact execution steps

`BINDING.pending.json` is deliberately disabled. Its science hashes/sizes
and top-level keys are **author-supplied metadata**, later reported confirmed
by root; this preparer did not read or hash either scientific file.
Root must create a separate immutable approved binding containing:

1. Exact role/mode, source and lowercase `parameters.json` hashes/bytes,
   the reviewed parameter/assertion/cutoff contract, schema checks,
   adapter-source hashes, lock hash and only relevant provenance inputs.
2. A new absent direct-child attempt under
   `docs/papers211_215_sequence/qa/root_replays/`; exact positive deadlines;
   the prescribed empty scientific stderr policy.
3. Initial mode: the named paper canonical must be absent. Pair mode: the
   existing role-specific canonical's exact full bytes/hash must be bound.
   Author/A/B canonicals are distinct; no inter-role byte equality is assumed.
4. Root approval of the complete adapter, the source/import/config closure
   and schema. The boolean gate alone is not an independent approval report.

The author interface is exactly
`[abs(capsule/verify.py), "--parameters", abs(capsule/parameters.json)]`,
with capsule cwd. A sibling-parameter interface is separately supported only
when explicitly bound; no mode flag is passed into science. Fresh capsules
contain exactly the two registered source/data files. Both physical copies
receive actual native comparisons before science.

After root approval, the command grammar is:

```text
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC
/usr/bin/python3.10 -I -S -B
-X pycache_prefix=ABS_ATTEMPT/never_created_outer_cache
ABS_PREPARATION/p211_runtime.py outer ABS_BINDING BINDING_SHA256 ABS_ATTEMPT
```

This is one argv vector, not separate shell commands. Root must preserve the
actual enclosing command/cwd/tool-native return as well. The native outer
capture preserves launcher's complete separate streams; launcher captures
recorder streams; recorder captures complete scientific stdout/stderr.
The outer process's control return at the product boundary is a separately
required root receipt, not fabricated by an inner PASS.

Initial recorder census: two source comparisons, linkage before, one
producer, linkage after (**five native attempts**). It stores actual stdout
as a candidate only. Root must independently receive that closed initial
attempt, then explicitly copy/compare its exact stdout into the still-absent
paper canonical. No existing canonical is overwritten or silently adopted.

A separately approved pair binding then requires nine recorder commands:
two source comparisons, two linkage records, two producers, run1/canonical,
run2/canonical and run1/run2 native comparisons. Each enclosing launcher and
outer contributes one additional recorded native command. Full compact,
sorted-key, ensure_ascii JSON+LF is checked, with duplicate/nonfinite JSON
rejected. Runtime schema checks are not a replacement for verifier/proof review.

## Failure preservation and evidence limits

- discovery01 passed 18 documentary/probe/linkage commands under the first
  draft, but tests01 stopped after 14 predicate groups when the new ordinary
  open guard rejected subprocess DEVNULL before launcher spawn. Its original
  trace, incomplete inner ATTEMPT/raw files, failed result and physical source
  snapshots remain unchanged. It is **not** strict-production evidence.
- The correction adds the device role, raw open-event preservation, truthful
  pre-return exception handling and actual loader-directory-state consumption.
  discovery02 passed 22 documentary/probe/linkage commands under new hashes.
  No old lock or failed receipt was edited.
- tests02 passed 21 pure-infrastructure predicate groups. Its two complete
  pipelines execute a fixed-output toy fixture three times, **zero scientific
  runs**. There are 41 complete native receipts and 43 ATTEMPT records:
  the two exceptions are explicitly controlled audit-refusal and
  settlement-report-withholding tests. Genuine nonzero exit, timeout,
  spawn failure, cache/environment refusal and all three pair comparisons
  retain their real outcomes and separate raw streams.
- The settlement-withholding test first actually settled its native process,
  then deliberately reported unknown quiescence to the code under test.
  The code refused hashes/seal; a separate actual settlement attestation
  permits sealing the enclosing pure-test artifact. This is **not** a test
  of a genuinely escaped or unkillable writer. The audit-refusal test likewise
  retains an unknown pre-return outcome rather than an invented native exit.
- First-draft REUSE_MAP metadata was not among the four native source copies.
  Its exact former 1,608 bytes are explicitly restored after the correction
  by removing only the documented added line; the original before-pin matches.
  `historical_metadata/` is labelled a hash-verified restoration, not a
  falsely claimed pre-edit physical snapshot. Executable first-draft sources
  were physically copied before the failing test.
- Observation is post-hook Python-open evidence and discrete module/map
  samples with declared configuration and linkage checks. It is not a
  continuous OS/startup/native-open/escaped-descendant trace or a hermetic
  execution environment. Missing nested closure or detected unsettled groups
  prevent sealing; undetected direct native escape is not claimed excluded.
  No automatic retry, cutoff expansion, or posthoc dependency adoption exists.

The complete helper tool returns are retained as decoded tool objects,
not relabelled separate outer raw stdout/stderr. Inner native raw streams
are physical. `final_checks01` separately within this author desk
rechecks all four prior package manifests, 122 current lock keys, nine
directory states, all 41 tests02 native receipts/raw streams, nine fixture
process stages and actual original argv. This is an **author infrastructure
check**, not an independent manuscript review or fresh science.

The project research skill caused the explicit root approval pause.
Infrastructure authorship and prior KIP source-only familiarity must be
disclosed if this agent later serves on a manuscript review. This task adds
no KIP proof or scientific verifier contribution. No old evidence, paper,
central index, Git state or external system was changed. HOLD_EXTERNAL.
