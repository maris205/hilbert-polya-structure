# Hilbert–Pólya Structure

This repository collects source-locked, reproducible research on dynamical,
arithmetic, and operator-theoretic structures related to the Hilbert–Pólya
programme.  Candidate generation is deliberately adventurous; promotion of
a candidate is deliberately conservative.

## Research streams

| Stream | Scope | Entry point |
|---|---|---|
| Hénon dynamics | Arithmetic and symbolic obstructions, transfer operators, and candidate searches | [`henon_dynamics/`](henon_dynamics/README.md) |
| Logistic-origin HP-Dynamics | Logistic-map foundations plus synchronized symbolic, renewal, quantum-graph, and Hénon/FIO Route-A breadth pivots | [`logistic_dynamics/`](logistic_dynamics/README.md) |
| `zeta_mvp0` | A staged operator programme with one independently auditable directory per paper | [`zeta_mvp0/`](zeta_mvp0/README.md) |

Within `zeta_mvp0`, each paper has its own manuscript, protocols, executable
source, tests, result certificates, and claim boundary.  The programme README
is updated whenever a paper is imported, a milestone is accepted or revoked,
or an evidence boundary changes.

## `zeta_mvp0` papers

The programme currently contains two paper packages, each directly under
`zeta_mvp0/`:

| Paper | Main contribution | Directory |
|---|---|---|
| Paper 01 — Clock-preserving Hénon operators | A fixed self-adjoint, discrete-spectrum Schrödinger family with the programme's two-growing-term counting law, operator estimates, and controlled classical/spectral diagnostics | [`zeta_mvp0/paper_01_clock_preserving_henon/`](zeta_mvp0/paper_01_clock_preserving_henon/README.md) |
| Paper 02 — Certified local relative wave trace | A local relative wave-trace theorem together with certified existence and local uniqueness results for a fast periodic-orbit branch in the frozen reduced chart | [`zeta_mvp0/paper_02_certified_local_wave_trace/`](zeta_mvp0/paper_02_certified_local_wave_trace/README.md) |

The former intermediate `zeta_mvp0/papers/` directory was removed on
2026-08-12.  Historical evidence retains the paths at which it was captured;
the precise migration and control boundary is recorded in
[`PAPER_LAYOUT_MIGRATION_2026-08-12.md`](zeta_mvp0/docs/PAPER_LAYOUT_MIGRATION_2026-08-12.md).

## Relation to the Riemann hypothesis

The Hilbert–Pólya route seeks a fixed self-adjoint operator together with a
complete, multiplicity-preserving correspondence in which the spectral
parameter $-i(\rho-\tfrac12)$ of every nontrivial zeta zero $\rho$ belongs to
the operator spectrum, and conversely.  A self-adjoint operator has real
spectrum, so such a correspondence would force every zero to have the form
$\rho=\tfrac12+i\lambda$ and would prove the Riemann hypothesis.

This repository addresses structural prerequisites for that route:

1. Paper 01 supplies a concrete self-adjoint operator family and the intended
   average spectral clock.
2. Paper 02 develops the local spectral-to-classical interface: a relative
   wave trace can detect a rigorously controlled classical periodic orbit.
3. The validation packages make the current local statements reproducible
   and keep numerical, local, global, and arithmetic claims separate.

The decisive arithmetic bridge for this repository's periodic-orbit and
explicit-formula strategy remains open.  In particular, the dynamics has not
yet been shown to generate an intrinsic infinite prime-power orbit family
whose relevant limiting or asymptotic periods realize $r\log p$, together
with the required von-Mangoldt-type amplitudes and phases, or to reproduce
the full Riemann explicit formula.  Nor has any complete two-way
correspondence between the operator spectrum and all zeta zeros been proved.
These are necessary gates for the strategy pursued here, not conclusions
that can be inferred from a finite zero fit, a random-matrix statistic, or
one certified periodic-orbit branch.

## Claim boundary

No result in this repository currently proves the Hilbert–Pólya conjecture,
identifies a self-adjoint spectrum with the nontrivial zeros of the Riemann
zeta function, or proves the Riemann hypothesis.  A numerical zero fit,
random-matrix statistic, or classical prime correlation cannot promote such
a claim without the named analytic and arithmetic gates.

Author of the `zeta_mvp0` programme: **Liang Wang**, School of Artificial
Intelligence and Automation, Huazhong University of Science and Technology,
Wuhan 430074, P. R. China.
