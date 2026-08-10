# A4.16 L3-A1 temp-only machine-capture and independent-verify increment

Date: 2026-08-10 (UTC)

Protocol family: `R401-VAL-L3-A1`

Authority: **NON_LICENSING / engineering implementation candidate /
temp-only capture / read-only verification / no canonical publication / no
scientific dispatch**

## Outcome and authority

This increment implements the next bounded engineering surface after
`A416_L3_A1_MACHINE_BINDING_INCREMENT.md`:

1. role 19 can assemble and self-validate one strict machine-freeze candidate
   at a new temporary path;
2. the compiler evidence is separated into an immutable build recipe, an
   executed fresh-rebuild receipt, and no-overwrite transfer evidence; and
3. role 24 can independently replay one supplied candidate with zero writes
   and zero subprocesses.

These capabilities do not publish or promote a freeze.  Their exact boundary
is:

```text
artifact_role = MACHINE_FREEZE
status = FROZEN_FOR_PRODUCTION
authority = MACHINE_ADMISSION_ONLY
scientific_licensing_enabled = true
production_authorized = false
component_status = null
milestone_status = null
theorem_status = null
final_status = null
canonical_machine_role10_exists = false
main_freeze_role54_exists = false
dispatch_authorized = false
```

The status and authority fields describe the closed candidate schema and its
machine-admission capability.  They do not make a `/tmp` byte image the
canonical role-10 input and do not authorize production.

## Role ordering and publication boundary

The ordered main-freeze input map has exactly 53 roles.  The canonical
`R401_VAL_L3_A1_MACHINE_FREEZE.json` is role 10 in that input map.  This
increment writes no role-10 path.

The main freeze is not among the 53 inputs.  It is downstream role 54 in the
68-role release map and may be generated only after all 53 input roles have
their final bytes.  A temporary candidate, even after both implemented
validators accept it, cannot substitute for role 10 in that handshake.
Byte-identical no-replace publication as role 10 requires a separate explicit
authorization and is outside this increment.

## Role-19 temp-only capture

From the Paper 02 directory, the implemented capture surface is:

```text
python scripts/run_r401_val_l3_a1_all_slabs.py \
  --capture-machine-freeze \
  --static-calibration ABSOLUTE_TMP_STATIC_CJ_COMPACT_PATH \
  --branch-calibration ABSOLUTE_TMP_BRANCH_CJ_PRETTY_2_PATH \
  --output ABSOLUTE_MISSING_TMP_CANDIDATE_PATH \
  [--capd-checkout ABSOLUTE_CAPD_CHECKOUT] \
  [--compiler ABSOLUTE_COMPILER]
```

Capture is exact-exclusive with mock, initialize, resume, production, and
scientific-execution flags.  It accepts only the final already-public static
and branch calibration serialization domains, rejects a non-`/tmp`, existing,
canonical, result-namespace, linked, or aliased output, and creates the target
exclusively.  The resulting bytes use `CJ_COMPACT_V1`: sorted keys, compact
separators, strict JSON, and one final LF.

Role 19 owns every subprocess used by capture; role 24 owns none.  The fresh
compiler invocation uses an argv list with explicit `shell=False` and a pinned
seven-variable environment:

```text
PATH=/usr/bin:/bin
LANG=C.UTF-8
LC_ALL=C.UTF-8
TZ=UTC
PYTHONHASHSEED=0
PYTHONNOUSERSITE=1
PYTHONDONTWRITEBYTECODE=1
```

On Linux, role 19 saves the caller's child-subreaper state and serializes
capture-command lifetimes.  It terminates and reaps only the owned process
group, using bounded `SIGTERM`, `SIGKILL`, and `waitpid(-owned_pgid)`
deadlines; it never calls `waitpid(-1)`.  Every exit restores and verifies the
original child-subreaper state.

The build output is exactly
`/tmp/<fresh-directory>/capd_r401_phase_branch_tube_mp_a1`.  It is never the
persistent role-17 path.  Capture parses the fresh ELF, compares it byte for
byte with the public-calibration and persistent binaries, checks the
persistent binary before and after, records that its device/inode identity is
unchanged and no overwrite occurred, validates the complete candidate through
the closed producer schema before exclusive temporary publication, and then
removes the owned fresh-build directory.  The receipt retains its paths only
as inert evidence.  Role 24 supplies the separate independent replay.

Capture does not run the rebuilt branch evaluator or either scientific
evaluator.  It creates no run config, scientific cell, aggregate, checker,
postcheck, report, release, or canonical freeze.

Successful producer stdout is one sorted-key JSON line with exactly these
keys and value contracts:

```text
artifact_role = TEMP_MACHINE_FREEZE_CANDIDATE
artifact_status = CAPTURED_VALIDATED_TEMP_ONLY
authority = MACHINE_ADMISSION_ONLY
candidate_sha256 = <64-lowerhex SHA-256 of candidate bytes>
component_status = null
final_status = null
machine_artifact_role = MACHINE_FREEZE
machine_status = FROZEN_FOR_PRODUCTION
milestone_status = null
output_path = <exact CLI spelling of the temporary target>
production_authorized = false
scientific_dispatch_performed = false
serializer = CJ_COMPACT_V1
theorem_status = null
```

This transient summary is not the machine object, is not written beside the
candidate, and has no publication or dispatch authority.

## Exact machine and compiler schemas

The machine-freeze object retains the exact 23-key top-level set:

```text
artifact_role
authority
branch_binary
capd
capture
claim_boundary
compiler
component_status
filesystem
final_status
machine_observations
machine_requirements
milestone_status
production_authorized
protocol_id
python_arb
resource_admission
resource_evidence
runtime_libraries
schema_version
scientific_licensing_enabled
status
theorem_status
```

Its `compiler` object has exactly:

```text
executable_path
executable_sha256
version
build_recipe
fresh_rebuild_receipt
transfer_evidence
```

`build_recipe` has exactly:

```text
cwd
environment
umask
staging_output_token
argv_template
argv_template_sha256
```

The token is exactly `@STAGING_BINARY@`, occurs exactly once as the last argv
template element, and prevents either the declaration or execution receipt
from naming the persistent target as build output.

`fresh_rebuild_receipt` has exactly:

```text
cwd
environment
umask
staging_directory
staging_output_path
argv
argv_sha256
shell_used
stdout
stderr
stdout_sha256
stderr_sha256
return_code
output_sha256
output_size_bytes
output_mode
output_build_id
output_dt_needed
output_dt_needed_sha256
output_soname
```

`shell_used` is exactly Boolean `false`; return code is zero; stdout and
stderr are empty; mode is `0755`; the GNU build ID and sorted `DT_NEEDED`
values equal the persistent binary; and `output_soname` is null.

`transfer_evidence` has exactly:

```text
staging_output_sha256
staging_output_size_bytes
staging_output_mode
branch_calibration_binary_sha256
persistent_before_sha256
persistent_before_size_bytes
persistent_before_mode
persistent_before_device_id
persistent_before_inode
persistent_after_sha256
persistent_after_size_bytes
persistent_after_mode
persistent_after_device_id
persistent_after_inode
byte_for_byte_equal
persistent_identity_unchanged
persistent_overwrite_performed
```

All four SHA-256 values equal the role-17 branch-binary digest; all three
size/mode pairs agree; the persistent before/after device and inode agree with
the same live role-17 file; and the last three values are respectively
`true`, `true`, and `false`.

## Role-24 independent verify-only CLI

The independent entry point is:

```text
python scripts/build_r401_val_l3_a1_release_provenance.py \
  --verify-machine-freeze ABSOLUTE_JSON_PATH
```

This mode is mutually exclusive with release `--verify-only` and cannot be
redirected to another project by `--project-root`.  It accepts a compact
canonical candidate at an exact absolute regular single-link path, including
a direct temporary candidate or later byte-identical canonical role-10 bytes.
It rejects relative, normalized, doubled-separator, backslash, trailing-slash,
NUL, duplicate-key, noncanonical-byte, symlink, hard-link, and
path/inode/namespace-TOCTOU variants.

Role 24 independently mirrors the machine schema and uses the current Paper
02 root and live role-19 scheduler, role-15 static evaluator, role-16 branch
source, role-17 branch binary, and role-34 L1 plan.  It imports no producer,
depends on no role-54 main freeze, writes no byte, and spawns no subprocess.
In particular it does not perform a second rebuild; any independently repeated
build belongs to a future role-11 pre-freeze test.

Successful stdout is exactly one line:

```text
machine_freeze_verification=PASS_MACHINE_FREEZE_VERIFY_ONLY authority=NON_AUTHORITATIVE_VERIFY_ONLY candidate_sha256=<64-lowerhex> size_bytes=<positive-int> promotion_authorized=false
```

The digest and size are recomputed from the captured canonical raw snapshot
and returned only as transient metadata.  They are not inserted into the
machine object, create no self-hash, and authorize no output artifact.  Its
claim boundary is read-only machine-freeze schema and live-binding replay
only: no freeze publication, evaluator dispatch, production authorization,
scientific component, theorem, or release authority.

## Verification evidence

The final implementation and test hashes are:

| Object | SHA-256 |
|---|---|
| role-19 scheduler / capture producer | `48e6fba9a7c567faddc15c49f7e0d3a3b7a0ff77afae6d80e87d0b1b101638ad` |
| static-scheduler / capture tests | `6d8f8cd2d73ab8e6e003b7f1763a88fed917ba4863ad55b24f91ae8a7f28681f` |
| role-24 release builder / independent verifier | `e1ab0e0f23fdf73406425243cc2203c02cae69cd382dd84e76631a0b63b9a0e7` |
| release / machine-verifier tests | `a4b0e1c3aa514c01e10ee14c63db7973237e245da74c70643e6e33639c663c40` |

From repository root `/root/autodl-tmp/zeta/hilbert-polya-structure`, the
role-19 focused command was exactly:

```text
pytest -q zeta_mvp0/papers/paper_02_certified_local_wave_trace/tests/test_r401_val_l3_a1_static_scheduler.py
```

It passed `107/107` tests in `26.62 s`.  The exact broader command was:

```text
pytest -q \
  zeta_mvp0/papers/paper_02_certified_local_wave_trace/tests/test_r401_val_l3_a1_adversarial_e2e.py \
  zeta_mvp0/papers/paper_02_certified_local_wave_trace/tests/test_r401_val_l3_a1_branch_checker.py \
  zeta_mvp0/papers/paper_02_certified_local_wave_trace/tests/test_r401_val_l3_a1_branch_scheduler.py \
  zeta_mvp0/papers/paper_02_certified_local_wave_trace/tests/test_r401_val_l3_a1_composite_contract.py \
  zeta_mvp0/papers/paper_02_certified_local_wave_trace/tests/test_r401_val_l3_a1_release_provenance.py \
  zeta_mvp0/papers/paper_02_certified_local_wave_trace/tests/test_r401_val_l3_a1_s0_compatibility.py \
  zeta_mvp0/papers/paper_02_certified_local_wave_trace/tests/test_r401_val_l3_a1_static_cell.py \
  zeta_mvp0/papers/paper_02_certified_local_wave_trace/tests/test_r401_val_l3_a1_static_checker.py \
  zeta_mvp0/papers/paper_02_certified_local_wave_trace/tests/test_r401_val_l3_a1_static_scheduler.py
```

All `457/457` tests passed in `152.37 s`.  The release/machine-verifier module
was then rerun alone on the final role-19 bytes and passed `94/94` tests in
`35.20 s`.  Python compilation and `git diff --check` also passed.  None of
these commands dispatched a scientific evaluator.

A separate final read-only replay passed the two focused modules together,
`201/201` in `61.89 s`, and passed `24/24` parallel timeout cases.  It also
confirmed that the process-control helper restored the caller's subreaper
enabled state to `false` after return.  These are engineering test results,
not a pre-freeze verdict or publication authority.

Distinct from both focused and nine-module runs, the complete Paper 02
regression on the locked machine-capture code and documentation set passed
`852/852` tests in `207.85 s`.  It performed no scientific dispatch.

The final live temporary receipt is:

| Binding | Exact value |
|---|---|
| candidate path | `/tmp/a416-machine-capture-subreaper-final.UF30tt/machine-candidate.json` |
| candidate SHA-256 | `eb3395cb3de902685da62b9d18b74e0ba2109d2cce08da2e29a48f966ca7b0e7` |
| size | `54526` bytes |
| mode / link count | `0644` / `1` |
| producer status | `CAPTURED_VALIDATED_TEMP_ONLY` |
| role-24 verification | `PASS_MACHINE_FREEZE_VERIFY_ONLY / NON_AUTHORITATIVE_VERIFY_ONLY` |
| promotion authorized | `false` |

Role 24 independently recomputed the same digest and `size_bytes=54526`.  Its
exact success line was:

```text
machine_freeze_verification=PASS_MACHINE_FREEZE_VERIFY_ONLY authority=NON_AUTHORITATIVE_VERIFY_ONLY candidate_sha256=eb3395cb3de902685da62b9d18b74e0ba2109d2cce08da2e29a48f966ca7b0e7 size_bytes=54526 promotion_authorized=false
```

A separate read-only stat/hash check reproduced the candidate digest, size,
mode, and link count.  The receipt names fresh staging directory
`/tmp/a416-l3a1-machine-build.ll_xlt9i`; that directory is absent after
capture.  The receipt retains `shell_used=false`,
`byte_for_byte_equal=true`, `persistent_identity_unchanged=true`, and
`persistent_overwrite_performed=false`.

Before the final subreaper/group-wait repair, the same nine-module command had
reached `456` passes and one descendant-cleanup failure.  All hashes and
candidate receipts from that pre-fix attempt are withdrawn and stale under the
final role-19 binding; none is cited as acceptance evidence.

## Exact absence and claim boundary

At completion of this increment:

- no canonical `R401_VAL_L3_A1_MACHINE_FREEZE.json` exists;
- no canonical `R401_VAL_L3_A1_FREEZE.json` exists;
- no canonical S0 compatibility replay or formal pre-freeze test record
  exists;
- no canonical production run config, result root, operational generation,
  report, or release exists; and
- no representative, held-out, or all-slab scientific evaluator was
  dispatched.

This increment asserts no A4.16 all-slab theorem, global tube routing, trace
formula, Hilbert--Polya operator, zeta-zero reconstruction, RH conclusion, or
implication toward RH.

## Remaining gate

After stable bytes and regression evidence are recorded, the next authority
steps remain separate: authorize one no-replace publication of independently
verified bytes as role 10; complete and freeze all other mandatory inputs,
including roles 11--13; obtain the sole exact independent line
`Verdict: ACCEPT_FOR_FREEZE`; and only then generate the main freeze as role
54.  Initialize-only and every scientific dispatch remain prohibited until
their own later authorization gates close.

## Subsequent publisher-ordering note

The later
`A416_L3_A1_MACHINE_PUBLICATION_INCREMENT.md` implements, but does not run, a
fixed-destination role-19 publisher.  Because the machine object binds the
exact role-19 capture-tool digest, adding that publisher changes role-19 bytes
and makes the temporary candidate cited above historical rather than
publishable.  The role numbering is not a construction topology: final role
19 must precede fresh capture, role-24 temporary verification, role-10
publication, and role-24 canonical verification.  Role 19 contains no role-10
hash, so this ordering introduces no cycle.

No canonical role 10 was created by either implementation increment.  The
main freeze is not among the 53 inputs; it remains downstream role 54 and may
be generated only after all 53 inputs, including roles 10--13, have stable
final bytes and the required independent review.
