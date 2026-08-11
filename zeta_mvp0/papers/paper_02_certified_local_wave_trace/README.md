# Paper 02 — Certified local relative wave trace

Working title: **A Local Relative Gutzwiller Trace and a Certified Fast
Branch for a Clock-Preserving Hénon Schrödinger Pair**.

Author: **Liang Wang**  
School of Artificial Intelligence and Automation, Huazhong University of
Science and Technology, Wuhan 430074, P. R. China.

Paper 02 is the active theorem-engineering continuation of Paper 01.  Its
strongest accepted statements and latest bounded implementation evidence are:

1. a fixed-energy, eigenvalue-only local relative trace formula for the fast
   Lyapunov orbit, subject to a sufficiently small energy band;
2. `A4.12 / R401-VAL-L1-V2`: one connected real-analytic primitive full-return
   branch, unique in frozen local boxes for
   \(0\le\epsilon\le0.101\);
3. `A4.13 / R401-VAL-L1-MG-V2`: on that branch,
   \(\det(I-D\Pi_\epsilon)=4-\operatorname{tr}M_\epsilon>3\).
4. `A4.14 / R401-VAL-L2-S0`: the frozen complement engine closes all six
   representative trees on `S000`, `S025`, and `S050` at 128 and 256 MPFR
   bits, with the explicitly bounded status `PASS_IMPLEMENTATION_SMOKE`.
5. `A4.15 / R401-VAL-L2-A1`: all 102 frozen complement trees close on the
   51-slab interval \(0\le\epsilon\le0.101\) at both precisions, yielding
   `PASS_LOCAL_COMPLEMENT_ALL_SLABS` after independent exact-rational replay.
6. `A4.16 / R401-VAL-L3-S0-COMPOSITE-DRAFT`: the exact representative
   `S000/S025/S050 x 128/256` phase-anchor and branch-tube matrix passes as
   `DRAFT_NON_LICENSING / PASS_IMPLEMENTATION_SMOKE`.  This is implementation
   evidence only, not an accepted 51-slab A4.16 theorem.
7. `A4.16 / R401-VAL-L3-A1` machine-binding and exact-schema implementation:
   the ordered 53-role same-byte handshake, closed formal schemas, strict
   static/branch serializers, persistent CAPD binary, temp-only role-19
   machine capture, zero-write role-24 independent verifier, and
   fixed-destination role-19 publisher exist as engineering surfaces.  After
   separate authorization, the exact machine candidate was published once as
   canonical input role 10 and independently replayed by role 24.  Role 23 now
   also implements temp-only capture and fixed-destination write-once
   publication for the unchanged 18-key S0-compatibility object.  That object
   has now been published once as canonical input role 13.  The prospective
   role-11 pre-freeze test-evidence producer, independent checker, and
   no-replace publisher are implemented and independently cleared, but role 11
   itself is still absent.  The final static and branch resource calibrations
   use public S0 inputs only.  This is still `NON_LICENSING`: no role-12
   `ACCEPT_FOR_FREEZE` review, role-54 main freeze, scientific dispatch, or
   canonical A4.16 result exists.

The local determinant result was independently replayed from exact rational
decimal payloads: 202 determinant enclosures, 202 phase-slope enclosures, 815
directed display payloads, and 8302 aggregate checks passed with zero
failures.

The representative complement archive contains 3,016 evaluated nodes.  Its
183 energy-exclusion leaves and 1,349 necessary-return-exclusion leaves cover
the exact eight-shell complements of the selected L1 boxes; there are no
root-candidate, invalid, or unresolved leaves.  A producer-independent
exact-decimal checker passed 89,962 checks with zero failures.  This proves a
finite three-slab statement and does not interpolate to the other 48 slabs.

The accepted all-slab archive contains 52,790 evaluated nodes across 102
trees: 3,368 energy-exclusion leaves, 23,435 necessary-return-exclusion
leaves, and 25,987 internal split nodes.  Every frontier is empty.  The
independent checker passed 158,782 checks with zero failures and sealed one
102-entry canonical manifest root.  Together with the accepted L1
existence-and-uniqueness result inside each protected box, this proves
pointwise reduced-root uniqueness throughout the frozen local box on all 51
slabs.

## Accepted all-slab production (A4.15)

The all-slab complement run is accepted under `R401-VAL-L2-A1`.  Its main
freeze has SHA-256
`c64d7b3cb7d6cfef403edfe35b7459ba5291608104aea4653ae8c0feec710cf2`
and binds the exact ordered 102-tree matrix, 23 source/evidence inputs, the
CAPD commit and full ordered build flags, the evaluator binary, 32 logical
CPUs, the 60-GiB memory limit, and the storage admission watermarks.

Pre-freeze verification passed 353 tests, two independent reviews, a pair of
102-tree synthetic generations, crash/resume and quarantine tests, and a
read-only replay of all 3,016 public S0 nodes.  `initialize-only` sealed
`results/r401_val_l2_all_slabs/run_config.json` with SHA-256
`f2d3eef4a76f18246c15789e32fe597266e3fe855c5e9a8bd2b5c3e67dfdf70d`;
no A1 evaluator node was dispatched during initialization.

Formal execution began at `2026-08-07T06:23:25Z` and archived all trees on
`2026-08-09`.  The final generation has SHA-256
`a658e754000ea29aa0f2289aa03f45b565e216c96584fb3de6d494f9c27c95e0`;
the ordered tree-manifest root is
`240c81a09d4ffd327fb1f3ba660d6df32c8bb300a3bf62f1481d0c9d3e37605c`.
The producer retained null scientific authority, while the frozen checker
assigned `PASS_LOCAL_COMPLEMENT_ALL_SLABS` after 158,782 successful checks.
The 19-role write-once release then passed a full `--verify-only` replay and
the repository-wide release audit.

The accepted certificate is
[`A415_ALL_SLAB_LOCAL_COMPLEMENT_CERTIFICATE.md`](research/route_a_wave_trace/A415_ALL_SLAB_LOCAL_COMPLEMENT_CERTIFICATE.md),
and the production report and release are under
`results/r401_val_l2_all_slabs/`.  This result concerns only the frozen local
reduced chart; it is not global energy-shell uniqueness, a trace formula, a
Hilbert--Pólya construction, a zeta-zero reconstruction, or RH.

## Representative phase-tube implementation smoke (A4.16)

The non-licensing A4.16 S0 composite binds the exact three-slab by
two-precision matrix shared by two independently checked components.  The
static phase-anchor archive contains 84,172 nodes, zero unresolved leaves,
and 122,300 independent interval checks.  The CAPD branch-tube archive
contains six complete-period `SolutionCurve` records; its largest certified
\(r_-^2\) upper endpoint is
`0.0001124580903773778485... < 0.0016`.

The separate composite checker passes all six cells, verifies 18 manifest
and component-control bindings, and records zero failures.  Its summary and
checker SHA-256 values are respectively
`ab0d7921623a5d4ba61d148ce833d22e14da75c77385897c328b20e41d64257f`
and
`197a087ecc75c95f186764f5365d3fc6769cb4cfe99793bfc1abc61afc037470`.
The bounded record is
[`A416_REPRESENTATIVE_PHASE_TUBE_SMOKE.md`](research/route_a_wave_trace/A416_REPRESENTATIVE_PHASE_TUBE_SMOKE.md).

This representative smoke does not assign a milestone, theorem, or final
programme value.  It does not cover the other 48 slabs and does not prove
that arbitrary energy-shell candidates remain in the local tube.

## Formal machine-binding, capture, publication, and exact-schema increments (non-licensing)

The current L3-A1 engineering surface now closes the prospective machine,
main-freeze, run-config, static/branch cell, aggregate, checker/postcheck, and
release schemas without opening scientific execution.  The machine validator
uses the exact authority `MACHINE_ADMISSION_ONLY`, recomputes live Python/Arb,
Conda, CAPD, compiler, ELF/runtime-library, resource, and filesystem bindings,
and requires `production_authorized=false`,
`scientific_licensing_enabled=true` only as a machine-admission capability,
and null scientific statuses.  It does not itself authorize production or
assign any scientific result.  The
existing 53-role same-byte handshake and every formal dispatcher remain
fail-closed while the canonical authority chain remains incomplete.

The subsequent capture increment splits compiler evidence into a declarative
`build_recipe`, an executed `fresh_rebuild_receipt`, and
`transfer_evidence`.  Role 19 performs one owned argv-list rebuild with
`shell=false` under a fresh direct-child `/tmp` directory, checks exact ELF
identity, and proves byte equality to the persistent role-17 binary without
overwriting or changing it.  It may write a compact candidate only to a new
temporary path.  Role 24 independently replays that candidate with zero
writes and zero subprocesses; its verify-only success is explicitly
`NON_AUTHORITATIVE_VERIFY_ONLY` and cannot publish or promote role 10.

The publication implementation increment added a distinct role-19 publisher.
It accepts a temporary candidate and expected digest but
no destination override, derives only the fixed role-10 path, replays the full
live machine and stable current on-disk role-19 source path/hash/identity
binding, enforces a pre-open regular/`0644`/one-link
`1..1048576`-byte cap, and uses an explicit-`0644` same-parent staging inode
plus `renameat2(RENAME_NOREPLACE)`.  Every existing
canonical entry is fatal, including byte-identical content.  The source
candidate remains unchanged.  Role 19 emits only
`PUBLISHED_WRITE_ONCE_PENDING_INDEPENDENT_VERIFY` and never invokes role 24;
its transient receipt has `scientific_licensing_enabled=false`,
`production_authorized=false`, and null scientific result statuses.  The
operator must run role 24 separately on the canonical inode.  A failure
after rename preserves the write-once evidence for read-only/manual audit and
never authorizes rollback, overwrite, repair, or idempotent republish.

After that implementation was independently accepted and pushed, an explicit
operator authorization selected a fresh candidate bound to the final
role-19 source bytes.  Role 19 published those exact bytes once as canonical
`R401_VAL_L3_A1_MACHINE_FREEZE.json`; role 24 then independently replayed the
canonical inode.  The role-10 SHA-256 is
`0d5c46726ee8142e0e53f97c904213dfc9b795ac300b423277bc27a711f5c21e`,
its size is `54526`, mode is `0644`, and link count is `1`.  Publication is
commit `5086e33c7c66f33785338e90b340347e086d9941`; role 54 and every scientific
status remain absent or null.

The separate role-13 implementation preserves the original compatibility
artifact as exact closed 18-key `NON_LICENSING` compact JSON.  Capture may
write only a new `0600`, one-link candidate below `/tmp`.  Publication accepts
that candidate, its expected digest, and the exact live Paper 02 authority
root, derives only the fixed role-13 destination, enforces the 1-MiB cap,
rebuilds the candidate from four live source bindings, and uses an
explicit-`0644` same-parent stage plus
`renameat2(RENAME_NOREPLACE)`.  Even identical existing destination bytes are
fatal.  After rename there is no rollback, overwrite, repair, or idempotent
republish.  Its exact 21-key receipt is limited to
`ROLE23_ADAPTER_PUBLICATION_ONLY`; independent verification, licensing,
production, and dispatch are false and every scientific status is null.  At
the implementation-test boundary this surface had not yet been executed
against the repository and canonical role 13 was absent.  The stable
adapter/test SHA-256
values are
`a00117303874eec16c7d116f344179c1e586856046cb725efb92c7b8c22640b0` and
`f93832a2de731bad2972a08534adf5c8001c84805e57f01c5970a810bae2e95d`;
the focused implementation replay passed `72/72` in `1.42 s`, with Python
compilation and the implementation-owner diff check passing.  On the same
locked role-13 and bound-document bytes, the nine L3-A1 modules pass
`521/521` in `165.35 s` and the complete Paper 02 suite passes `916/916` in
`223.44 s`; both broader runs remained non-dispatching and, at that historical
boundary, left canonical role 13 absent.  After those bytes and all four
source bindings were committed and pushed, a fresh candidate was published
once and independently replayed.  Canonical role 13 is commit
`be2a732625d9cab97879539873a756e1eabd366d`, SHA-256
`d2844c9fd98f76bd41dda937e8f19f978aa48468c17c5a24ebd25baf125f5e30`,
size `8820`, mode `0644`, and link count `1`.

Static cells now have an exact four-file surface (`proof.json`, `stdout.txt`,
`stderr.txt`, `record.json`) with a strict 26-string ABI and
`CJ_COMPACT_V1`.  Branch runtime/checker limits are expressed consistently as
`timeout_ms=600000`, `term_grace_ms=2000`, and
`pipe_close_grace_ms=1000`; branch task, argument, record, and manifest hashes
use the strict sorted indent-2 `CJ_PRETTY_2_V1` bytes.  The independent
machine-binding/formal-schema cross-review returned `ACCEPT` with P0=0, P1=0,
and P2=0.  This is an implementation verdict, not `ACCEPT_FOR_FREEZE`.

The deterministic persistent evaluator now exists at
`validated/bin/capd_r401_phase_branch_tube_mp_a1`: SHA-256
`25aec3d7d68883c2a97f765682a40cabc3feb91f159f67ac2910b6f82025e521`,
size `2419064` bytes, mode `0755`, and GNU build ID
`3cff449e0a265fe63d1fa1d1350ea48f324ba386`.  It is byte-identical to the
temporary binary used by the already-public branch calibration.  The binary
is an implementation input only; it is not a machine freeze or result.

The final public-only static calibration ran six sequential jobs and an
eight-worker public S0 stress schedule.  All `14/14` invocations had exactly
26 strings, returned the certified status, and had empty stderr.  Its compact
payload has SHA-256
`8afc8a0a0929da077a1a1ad19ddc0c19e754c49646c4b3d806f3f4cf5522de92`
and size `30030` bytes.  The exact candidate arithmetic is
`24891273216 + 8 x 59949056 + 8589934592 = 33960800256 < 51539607552`
bytes, leaving `17578807296` bytes headroom.  The branch public payload remains
SHA-256
`2cd389315867cff7598c2977543a8e1f3d0a3dc60d99b51f1e7826f9f95af99a`
and transfers exactly to the persistent binary by SHA-256.  Neither
calibration selected a held-out or all-slab cell.

The preceding machine-binding increment recorded a `419/419` core regression
immediately before its final embedded branch-resource binding and an
`814/814` Paper 02 regression on those historical bytes.  During subsequent
machine-capture hardening, a pre-final broader run exposed delayed descendant
cleanup (`456` pass, `1` fail), so that receipt was withdrawn.  The repaired
role-19 module now passes `107/107`, the complete nine-module set passes
`457/457`, and role 24 passes `94/94` on the final scheduler bytes.  The two
focused modules total `201/201`; 24 parallel timeout-cleanup replays pass and
the temporary subreaper state is restored on return.  Separately, the complete
Paper 02 regression passes `852/852` in `207.85 s` on the locked
machine-capture code and documentation set.  At that capture-increment
boundary, the locked role-19 and role-24 SHA-256 values were respectively
`48e6fba9a7c567faddc15c49f7e0d3a3b7a0ff77afae6d80e87d0b1b101638ad`
and
`e1ab0e0f23fdf73406425243cc2203c02cae69cd382dd84e76631a0b63b9a0e7`.

The preceding capture increment's live temporary candidate is
`/tmp/a416-machine-capture-subreaper-final.UF30tt/machine-candidate.json`,
SHA-256
`eb3395cb3de902685da62b9d18b74e0ba2109d2cce08da2e29a48f966ca7b0e7`,
size `54526`, mode `0644`, and link count `1`.  Role 24 independently
reproduces the digest and size under `NON_AUTHORITATIVE_VERIFY_ONLY`; the
fresh-build staging directory is absent and the persistent role-17 binary was
not overwritten.  Both known pre-fix candidates now reject against the final
capture-increment role-19 source bytes.

Adding the publisher changed role-19 bytes, so the preceding temporary
candidate became historical evidence and was not used as role 10.  A fresh
candidate was captured after the publisher bytes stabilized, replayed by role
24, and selected by the separate one-shot authorization described above.

The stable publisher source and role-26 test SHA-256 values are respectively
`262985fcb1fc82890501b635bfce163712f1821e2d92276aee9f363ee0473a82`
and
`d5a4a018547e3f80f2f1a5375e530eb39120e686cc489925a1cf049a5e3dbf5f`.
The publisher-focused suite passes `23/23` tests with `107` deselected in
`13.70 s`, the complete static-scheduler module passes `130/130` in
`40.35 s`, and Python compilation plus `git diff --check` pass.  These are
isolated engineering tests; no publisher invocation targeted the repository
role-10 path and no scientific evaluator ran.

On the same locked publisher bytes, the final nine-module L3-A1 regression
passes `480/480` tests in `164.03 s`, and the complete Paper 02 regression
passes `875/875` in `218.37 s`.  Neither broader run published role 10 or
role 54, created a production result, or dispatched a scientific evaluator.

Canonical roles 10 and 13 now exist; role 10 passed the separate role-24
verify-only replay and role 13 passed its closed 18-key compatibility replay.
The role-11 producer, independent checker, and fixed-destination publisher are
implemented with exact locked totals (`100`, `621`, and `1016` passed), but no
role-11 candidate or canonical object exists at this implementation boundary.
No role-12 review, role-54 main freeze, production run config, scientific
dispatch, or A4.16 all-slab result exists.  The final static calibration
payload remains temporary, and no scientific authority was promoted.
Full current hashes,
resource evidence, and claim boundaries are recorded in
[`A416_L3_A1_MACHINE_BINDING_INCREMENT.md`](research/route_a_wave_trace/A416_L3_A1_MACHINE_BINDING_INCREMENT.md);
the separate capture/verify milestone is recorded in
[`A416_L3_A1_MACHINE_CAPTURE_INCREMENT.md`](research/route_a_wave_trace/A416_L3_A1_MACHINE_CAPTURE_INCREMENT.md);
the historical role-10 fixed-destination publisher boundary and its later
authorized-publication postscript are recorded in
[`A416_L3_A1_MACHINE_PUBLICATION_INCREMENT.md`](research/route_a_wave_trace/A416_L3_A1_MACHINE_PUBLICATION_INCREMENT.md);
the distinct unexecuted role-13 implementation boundary is recorded in
[`A416_L3_A1_S0_COMPATIBILITY_PUBLICATION_INCREMENT.md`](research/route_a_wave_trace/A416_L3_A1_S0_COMPATIBILITY_PUBLICATION_INCREMENT.md);
the role-11 exact test-evidence surface is recorded in
[`A416_L3_A1_PREFREEZE_TEST_EVIDENCE_INCREMENT.md`](research/route_a_wave_trace/A416_L3_A1_PREFREEZE_TEST_EVIDENCE_INCREMENT.md);
the preceding control-plane increment remains recorded in
[`A416_L3_A1_FORMAL_PREFLIGHT_INCREMENT.md`](research/route_a_wave_trace/A416_L3_A1_FORMAL_PREFLIGHT_INCREMENT.md).

## Open bridges

- committing and pushing the locked role-11 producer/checker/test bytes,
  followed on that clean snapshot by a fresh temporary test-evidence capture,
  independent verify-only replay, and separately authorized no-replace role-11
  publication; completion of the remaining final 53-input chain, independent
  `ACCEPT_FOR_FREEZE` review, role-54 main freeze generated only after all 53
  inputs, and only then a separately authorized 51-slab A4.16 phase-tube
  production; the current scientific evidence remains representative only;
- the full global shell return-exclusion tree on \(0.60<T<0.75\);
- global tube routing for candidates outside the local full-period tube;
- the frozen independent event-projected determinant/Taylor-width
  cross-check;
- an explicit theorem-domain bound \(\delta_{\rm tr}>0.01\);
- every endogenous prime-time, von-Mangoldt, Hilbert--Pólya, zeta-zero, and RH
  claim.

The representative A4.16 engine and the non-dispatching L3-A1 exact-schema,
temp-capture, machine-verification, and fixed-destination publisher surfaces
are implemented.  Canonical role 10 has been published once and independently
postverified.  The role-13 compatibility object has also been published once
and replayed without promoting scientific authority.  The role-11 evidence
surface is implemented and independently cleared, while canonical role 11 is
still absent.  The next authority stages are a clean role-11 evidence capture
and separate publication, independent role-12 review, and only then generation
of role 54.
A4.15 remains the highest accepted theorem in this chain.  Global routing is
a separate later bridge.

## Layout

- `manuscript/`: evolving paper plan and, once opened, LaTeX source;
- `research/`: theorem, protocol, refinement, and audit records;
- `src/` and `scripts/`: Python implementation and runners;
- `validated/`: CAPD/MPFR sources and dependency pin;
- `tests/`: relevant regression and release-contract tests;
- `results/`: accepted proof objects plus explicitly marked invalid or
  superseded provenance archives;
- `artifacts/`: future compiled manuscript artifacts.

The exact CAPD-linked executables bound by authoritative release manifests
are mirrored so a fresh clone can verify those manifests.  Other rebuildable,
invalid, or superseded binaries remain ignored.  The source pin and build
flags are recorded in `validated/CAPD_DEPENDENCY.md` and the result manifests.

## Read-only verification

From this paper directory:

```bash
python scripts/audit_release_hashes.py
PYTHONDONTWRITEBYTECODE=1 python \
  scripts/build_r401_val_l2_a1_release_provenance.py \
  --project-root "$PWD" --verify-only
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider \
  tests/test_r401_val_l1_contract.py \
  tests/test_r401_val_l2_s0_contract.py \
  tests/test_r401_val_l2_a1_release_provenance.py
```

The first command verifies every archived `RELEASE_PROVENANCE.json` without
rewriting immutable checker or postcheck files.  The second command performs
the deeper A1 release replay and requires the ignored bulk tree and manifest
archive to be present locally.  The contract suites pin the L1 and L2
protocol/source/authority semantics.  Re-running a checker that writes into a
result directory should be done only in a disposable clone.

The accepted A4.14 proof objects are under
`results/r401_val_l2_s0_local_complement/`; its release provenance also binds
the exact CAPD-linked executable mirrored in that directory.  The 102-tree A1
compact certificate, aggregate, checker, postcheck, and release objects are
under `results/r401_val_l2_all_slabs/` and are mirrored in Git.  The full A1
raw archive (52,790 records plus 102 tree payloads and manifests) remains in
the local authoritative result directory and is intentionally excluded from
ordinary Git because of its size; a fresh clone therefore supports the
compact 19-role hash audit but needs a separately transferred immutable bulk
archive for raw-node replay or the deep A1 `--verify-only` command.
