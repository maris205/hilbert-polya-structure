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
   static/branch serializers, persistent CAPD binary, and independent live
   machine validator pass engineering cross-review with P0=P1=P2=0.  The final
   static and branch resource calibrations use public S0 inputs only.  This is
   `NON_LICENSING`: no machine/main freeze, scientific dispatch, or canonical
   A4.16 result exists.

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

## Formal machine-binding and exact-schema increment (non-licensing)

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
fail-closed while the canonical authority chain is absent.

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

The core regression immediately before the final embedded branch resource
binary-digest/persistent-binary binding passed `419/419`.  After that binding
and all documentation corrections, the complete latest-byte Paper 02
regression passed `814/814`.

No canonical machine freeze, main freeze, S0 compatibility replay, production
run config, scientific dispatch, or A4.16 all-slab result exists.  The final
static payload remains under `/tmp` until the deterministic canonical machine
receipt capture/builder is implemented.  Full current hashes, resource
evidence, and claim boundaries are recorded in
[`A416_L3_A1_MACHINE_BINDING_INCREMENT.md`](research/route_a_wave_trace/A416_L3_A1_MACHINE_BINDING_INCREMENT.md);
the preceding control-plane increment remains recorded in
[`A416_L3_A1_FORMAL_PREFLIGHT_INCREMENT.md`](research/route_a_wave_trace/A416_L3_A1_FORMAL_PREFLIGHT_INCREMENT.md).

## Open bridges

- a deterministic machine-freeze capture/builder, producer-independent
  machine verification, the complete pre-freeze chain and independent
  `ACCEPT_FOR_FREEZE` review, main freeze generated last, canonical S0
  compatibility replay, and only then a separately authorized 51-slab A4.16
  phase-tube production; the current scientific evidence remains
  representative only;
- the full global shell return-exclusion tree on \(0.60<T<0.75\);
- global tube routing for candidates outside the local full-period tube;
- the frozen independent event-projected determinant/Taylor-width
  cross-check;
- an explicit theorem-domain bound \(\delta_{\rm tr}>0.01\);
- every endogenous prime-time, von-Mangoldt, Hilbert--Pólya, zeta-zero, and RH
  claim.

The representative A4.16 engine and the non-dispatching L3-A1 exact-schema and
machine-validation candidate are now checked.  The next engineering stage is
to build and independently verify the deterministic machine receipt, then
complete the pre-freeze review chain before generating the main freeze last.
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
