# zeta_mvp0 — a staged Hilbert--Pólya structure programme

Last updated: 2026-08-09.

`zeta_mvp0` is the first structured Hilbert--Polya search line in this
repository.  Its organizing rule is:

\[
\text{bold candidate generation}
\longrightarrow
\text{explicit structural gates}
\longrightarrow
\text{independent verification}
\longrightarrow
\text{carefully bounded claims}.
\]

## Gate dashboard

| Gate | Status | Strongest evidence | Repository availability | What is still missing |
|---|---|---|---|---|
| Q | proved | Paper 01 exact classical clock | mirrored in the Paper 01 package | — |
| W | proved at two-term level | Paper 01 bracketing/quantization package | mirrored in the Paper 01 package | constant and oscillatory structure |
| \(S_{\rm op}\) | proved | fixed self-adjoint compact-resolvent operator and strict ground-state ordering | mirrored in the Paper 01 package | no implication for zeta zeros |
| \(P^*_{\rm loc}\) | proved/certified at the stated local level | Paper 02 local relative trace, validated fast branch, monodromy gap, and 51-slab local complement | compact release mirrored; bulk A1 tree/raw archive requires separate transfer | it is not a full phase/global cover or a rational-prime trace |
| \(P_0\) | open | none | no evidence package | endogenous \(r\log p\) times and von-Mangoldt weights |
| Z | unauthorized | none | no evidence package | requires \(P_0\) before any zero comparison |
| RH | not claimed | none | no evidence package | the full chain is incomplete |

## Papers

| Paper | Working title | Status | Strongest licensed result |
|---|---|---|---|
| [`paper_01_clock_preserving_henon`](papers/paper_01_clock_preserving_henon/README.md) | Clock-preserving Hénon operators | frozen manuscript package | exact clock, Q/W and operator-level \(S\); rational-prime \(P_0\) remains open |
| [`paper_02_certified_local_wave_trace`](papers/paper_02_certified_local_wave_trace/README.md) | Certified local relative wave trace | compact release package mirrored; bulk A1 proof archive transferred separately | local relative-trace theorem; A4.12 branch; A4.13 gap; A4.15 all-slab local complement |

Each fully imported paper directory contains its manuscript,
theorem/protocol documents, executable source, tests, and compact result
certificates.  Paper 01 is fully mirrored.  Paper 02 mirrors its compact
release chains; the A4.15 bulk raw archive is separately transferable and is
not represented as present in an ordinary clone.  Failed attempts are
retained only when they are needed for provenance and are marked
non-licensing.

The future roadmap is recorded in
[`docs/PROGRAMME_ROADMAP.md`](docs/PROGRAMME_ROADMAP.md).  A planned paper is
not created as an apparently completed directory before its own thesis and
evidence package exist.

## Latest staged milestone

The programme records Paper 02 milestones A4.13 and A4.15 as accepted.
A4.13 / `R401-VAL-L1-MG-V2` proves from all 202 frozen local-branch
monodromy enclosures that

\[
  \det(I-D\Pi_\epsilon)=4-\operatorname{tr}M_\epsilon>3.
\]

Its independent exact-rational checker passed 8,302 checks with zero failures.
A4.15 / `R401-VAL-L2-A1` closes the eight-shell local complement on all 51
slabs at 128 and 256 MPFR bits.  Its 102 trees contain 52,790 evaluated nodes:
3,368 energy exclusions, 23,435 return exclusions, and 25,987 internal split
nodes.  All frontiers close, and the independent checker passes 158,782
checks with zero failures under `PASS_LOCAL_COMPLEMENT_ALL_SLABS` while
retaining `final_status = null`.

Paper 02 milestone A4.14 / `R401-VAL-L2-S0` is now accepted as
`PASS_IMPLEMENTATION_SMOKE`.  All six frozen complement trees on `S000`,
`S025`, and `S050` close at 128 and 256 MPFR bits: 3,016 evaluated nodes,
1,532 excluded leaves, no root candidate/invalid/unresolved leaf, and 89,962
independent exact-decimal checks with zero failures.  This remains a
three-slab implementation certificate, not the all-51-slab complement
theorem, and it does not promote the analytic trace threshold.

Paper 02 also records the representative A4.16 composite under
`R401-VAL-L3-S0-COMPOSITE-DRAFT`.  The exact
`S000/S025/S050 x 128/256` matrix binds 84,172 static proof-tree nodes and
six full-period CAPD branch-tube records.  Its independent checker passes all
six cells and 18 manifest/control bindings with zero failures.  The value is
`DRAFT_NON_LICENSING / PASS_IMPLEMENTATION_SMOKE`: it is not an accepted
51-slab A4.16 theorem, and A4.15 remains Paper 02's highest accepted theorem.

The compact A4.15 certificate, aggregate, checker, postcheck, and 19-role
release chain are mirrored here.  The 1.2-GiB raw node archive and the bulk
tree payloads/manifests remain outside ordinary Git and require a separate
immutable transfer for full raw replay.  Mathematically, A4.15 remains a
local reduced-chart theorem.  The phase/flow-box cover, global return cover,
independent event-projected determinant/Taylor-width gate,
\(\delta_{\rm tr}\), and \(P_0\) remain open.

The representative A4.16 smoke establishes implementation feasibility for
the phase anchor and accepted-branch tube only.  A prospectively frozen
51-slab production and arbitrary-candidate global tube routing remain open;
the smoke does not promote any trace, Hilbert--Pólya, zeta-zero, or RH claim.

## Current claim boundary

The current H\'enon-warped operator family has an exact area-preserving
classical clock, a self-adjoint compact-resolvent realization, a local
semiclassical relative-trace construction, and validated local periodic-orbit
data.  It does **not** yet provide an endogenous prime-power trace, a zeta-zero
spectrum, or a proof of RH.  Numerical agreement cannot promote any of those
claims.

## Update policy

This README is updated at every accepted milestone.  A milestone is listed
as accepted only after its protocol, evidence, independent checker, claim
boundary, and release hashes agree.  Superseded or invalid attempts never
silently become evidence for a later claim.

Every update must also state one of three repository-availability labels:

- **mirrored:** the complete cited evidence package is present here;
- **placeholder / transfer pending:** the result is recorded in the
  programme ledger but cannot yet be reproduced from this repository;
- **roadmap only:** no paper directory or result claim exists.

Research governance is recorded in:

- [`docs/EVIDENCE_POLICY.md`](docs/EVIDENCE_POLICY.md);
- [`docs/GLOBAL_CLAIM_LEDGER.md`](docs/GLOBAL_CLAIM_LEDGER.md);
- [`docs/DECISION_LOG.md`](docs/DECISION_LOG.md).

## Repository workflow

All work in this programme is synchronized to
`git@github.com:maris205/hilbert-polya-structure.git` over SSH.  A research
stage that has become a paper receives exactly one immediate subdirectory of
`papers/`; protocols, source, tests, proof objects, manuscript files, and
claim boundaries remain inside that paper package.  Programme-level READMEs
and ledgers are updated in the same commit whenever repository availability
or a licensed milestone changes.

## Reproduction

Each paper README gives its own minimal environment and commands.  Paper 01
does not require CAPD.  Paper 02 mirrors the pinned CAPD/MPFR sources,
compact release-bound objects and executables, independent checkers, and
contract tests.  Its compact read-only release audit can run from an ordinary
clone.  Deep A4.15 tree/raw replay additionally requires the separately
transferred bulk archive; binaries from invalid or superseded attempts remain
intentionally untracked.
