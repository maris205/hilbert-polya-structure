# Paper 02 — Certified local relative wave trace

Working title: **A Local Relative Gutzwiller Trace and a Certified Fast
Branch for a Clock-Preserving Hénon Schrödinger Pair**.

Author: **Liang Wang**  
School of Artificial Intelligence and Automation, Huazhong University of
Science and Technology, Wuhan 430074, P. R. China.

Paper 02 is the active theorem-engineering continuation of Paper 01.  Its
strongest accepted statements are:

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

## Open bridges

- exclusion of reduced roots outside the accepted local boxes on all 51
  slabs (A4.14 closes only S000, S025, and S050);
- the local phase/flow-box cover that makes the section complete modulo time
  translation;
- the full global shell return-exclusion tree on \(0.60<T<0.75\);
- the frozen independent event-projected determinant/Taylor-width
  cross-check;
- an explicit theorem-domain bound \(\delta_{\rm tr}>0.01\);
- every endogenous prime-time, von-Mangoldt, Hilbert--Pólya, zeta-zero, and RH
  claim.

The next L2 production would attack only the first item.  A4.14 is accepted
as a representative implementation certificate, not as an all-parameter
complement theorem.

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
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider \
  tests/test_r401_val_l1_contract.py \
  tests/test_r401_val_l2_s0_contract.py
```

The first command verifies every archived `RELEASE_PROVENANCE.json` without
rewriting immutable checker or postcheck files.  The two contract suites pin
the L1 and L2 protocol/source/status semantics.  Re-running a checker that
writes into a result directory should be done only in a disposable clone.

The accepted A4.14 proof objects are under
`results/r401_val_l2_s0_local_complement/`; its release provenance also binds
the exact CAPD-linked executable mirrored in that directory.  The future
102-tree scheduler/checker remains explicitly non-licensing until its
release and recovery contracts pass a separate formal-freeze review.
