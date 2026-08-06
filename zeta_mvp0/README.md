# zeta_mvp0 — a staged Hilbert--Pólya structure programme

Last updated: 2026-08-06.

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
| \(P^*_{\rm loc}\) | proved/certified at the stated local level | Paper 02 local eigenvalue-only relative trace and validated fast branch | mirrored, including release-bound proof objects and read-only hash audit | it is not a rational-prime trace |
| \(P_0\) | open | none | no evidence package | endogenous \(r\log p\) times and von-Mangoldt weights |
| Z | unauthorized | none | no evidence package | requires \(P_0\) before any zero comparison |
| RH | not claimed | none | no evidence package | the full chain is incomplete |

## Papers

| Paper | Working title | Status | Strongest licensed result |
|---|---|---|---|
| [`paper_01_clock_preserving_henon`](papers/paper_01_clock_preserving_henon/README.md) | Clock-preserving Hénon operators | frozen manuscript package | exact clock, Q/W and operator-level \(S\); rational-prime \(P_0\) remains open |
| [`paper_02_certified_local_wave_trace`](papers/paper_02_certified_local_wave_trace/README.md) | Certified local relative wave trace | mirrored working manuscript and evidence package | local relative-trace theorem; A4.12 branch; A4.13 gap; bounded A4.14 implementation certificate |

Each fully imported paper directory is independently auditable and contains
its manuscript, theorem/protocol documents, executable source, tests, and
result certificates.  Paper 01 and Paper 02 now satisfy that repository
inventory.  Failed attempts are retained only when they are needed for
provenance and are marked non-licensing.

The future roadmap is recorded in
[`docs/PROGRAMME_ROADMAP.md`](docs/PROGRAMME_ROADMAP.md).  A planned paper is
not created as an apparently completed directory before its own thesis and
evidence package exist.

## Latest staged milestone

The programme records Paper 02 milestone A4.13 /
`R401-VAL-L1-MG-V2` as accepted and mirrored under
`PASS_LOCAL_MONODROMY_GAP`: all 202 frozen local-branch monodromy enclosures
prove

\[
  \det(I-D\Pi_\epsilon)=4-\operatorname{tr}M_\epsilon>3.
\]

An independent exact-rational checker passed 8302 checks with zero failures.
The mirrored release audit verifies the authoritative A4.12/A4.13 hashes and
excludes the explicitly superseded monodromy archive from proof authority.
Mathematically, this remains a local-branch theorem only.  The independent event-projected
determinant cross-check, all-slab local complement, phase cover, global shell cover,
\(\delta_{\rm tr}\), and \(P_0\) remain open.

Paper 02 milestone A4.14 / `R401-VAL-L2-S0` is now accepted as
`PASS_IMPLEMENTATION_SMOKE`.  All six frozen complement trees on `S000`,
`S025`, and `S050` close at 128 and 256 MPFR bits: 3,016 evaluated nodes,
1,532 excluded leaves, no root candidate/invalid/unresolved leaf, and 89,962
independent exact-decimal checks with zero failures.  This remains a
three-slab implementation certificate, not the all-51-slab complement
theorem, and it does not promote the analytic trace threshold.

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
release-bound proof objects and executables, independent checkers, and contract tests.  Its
read-only release audit and selected contract suite can be run directly from
the Paper 02 directory; binaries from invalid or superseded attempts remain
intentionally untracked.
