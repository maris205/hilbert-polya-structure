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
7. `A4.16 / R401-VAL-L3-A1` formal control-plane preflight: the exact
   prospective 53-role same-byte handshake, temporary nonpromotable
   initialize-only path, pure static/branch transaction plans, atomic
   publication, and unconditional dispatch rejection pass independent
   implementation review with P0=P1=P2=0.  No canonical production object or
   new scientific result is created.

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

## Formal all-slab control-plane preflight (non-licensing)

The current L3-A1 increment implements a formal control-plane candidate but
does not open scientific execution.  It replays an exact ordered 53-role
same-byte handshake, atomically writes one temporary initialize-only
`run_config.json` outside every canonical namespace, constructs exact pure
static and branch transaction plans, and rejects both dispatch paths
unconditionally.  The candidate is nonresumable, nonpromotable, assigns no
component or theorem status, and cannot become the future production run
config.

Independent adversarial review accepted this implementation surface with
P0=0, P1=0, and P2=0.  The scheduler and focused-test SHA-256 values are
`e39caaed78468be1dc7791efde5b85f97668e07ef7117a7c2560decfea7d06bf`
and
`41655000a7904547f80aadf1726c01f1392239c1e1dea94394df6931e41ad508`.
The focused scheduler suite passed 79/79 tests, the owned L3-A1 suite passed
194/194, and the complete Paper 02 regression passed 710/710 without a
scientific evaluator dispatch.

A separate resource calibration ran the formal A1 source against only the six
already-public S0 branch inputs.  The source and temporary-binary SHA-256
values were
`66588bf25ae777c854f60a747af4299e3166efdd51db2659e33a28194abc59c5`
and
`25aec3d7d68883c2a97f765682a40cabc3feb91f159f67ac2910b6f82025e521`;
the complete CAPD/toolchain ledger is in the linked increment record.  The
worst peak RSS was `202428 KiB`, and the exact candidate calculation was
baseline `14505582592` + `6 x 207286272` + reserve `8589934592` =
`24339234816 < 51539607552` bytes, with `27200372736` bytes headroom.  No
held-out or all-slab input was selected.  The temporary binary was not
installed, the canonical calibration object remains absent, and this result
neither freezes the worker count nor adds scientific evidence.

The canonical L3 machine freeze, main freeze, S0 compatibility replay, A1
persistent CAPD binary, result root, and operational root remain absent.  The
full boundary and evidence record is
[`A416_L3_A1_FORMAL_PREFLIGHT_INCREMENT.md`](research/route_a_wave_trace/A416_L3_A1_FORMAL_PREFLIGHT_INCREMENT.md).

## Open bridges

- exact final L3-A1 schemas/contracts, the persistent A1 CAPD binary, machine
  freeze, canonical S0 compatibility replay, independent pre-freeze review,
  and only then a separately authorized 51-slab A4.16 phase-tube production;
  the current scientific evidence remains representative only;
- the full global shell return-exclusion tree on \(0.60<T<0.75\);
- global tube routing for candidates outside the local full-period tube;
- the frozen independent event-projected determinant/Taylor-width
  cross-check;
- an explicit theorem-domain bound \(\delta_{\rm tr}>0.01\);
- every endogenous prime-time, von-Mangoldt, Hilbert--Pólya, zeta-zero, and RH
  claim.

The representative A4.16 engine and the non-dispatching L3-A1 control-plane
candidate are now checked.  The next engineering stage is to finalize the
exact schemas/contracts, persistent binary, and machine freeze before any
independent pre-freeze review or formal all-slab production can be considered.
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
