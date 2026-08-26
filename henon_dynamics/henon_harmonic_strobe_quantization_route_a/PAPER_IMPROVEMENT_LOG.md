# Two-round paper improvement log

The three PDF snapshots are content-distinct.  The final `paper/main.pdf` is
byte-identical to `paper/main_round2.pdf`.

## Round 0: classical theorem skeleton

- Froze the oscillator, strobe clock, and rotation orientation.
- Proved the rational/irrational fixed-set dichotomy.
- Stated the elementary irrational Artin--Mazur zeta and rational continuum
  obstruction.
- Internal weakness found: the operator claims lacked their complete basis
  and same-clock derivations.

Snapshot: `paper/main_round0_original.pdf`.

## Round 1: Gaussian Koopman completion

- Added the normalized Laguerre--angular basis and its orthogonality proof.
- Distinguished dense irrational point spectrum from finite rational root
  spectrum and proved infinite radial multiplicity.
- Added the classical reversor, antiunitary lift, and exact finite-Schatten
  obstruction.
- Internal weakness found: a natural quantum claim required the explicit
  Hamiltonian convention, Hermite phases, and Egorov clock identity.

Snapshot: `paper/main_round1.pdf`.

## Round 2: quantum and scope closure

- Added the self-adjoint oscillator Hamiltonian, Hermite functional calculus,
  exact Egorov identities, and conjugation reversal.
- Corrected the parameter boundary after hostile audit: physical time is
  \(\theta\in\mathbb R\); the classical and Gaussian families are
  \(2\pi\)-periodic, while the quantum lift obeys
  \(Q_{\theta+2\pi}=-Q_\theta\) and is exactly \(4\pi\)-periodic.
- Retained the metaplectic global sign and classified rational quantum phases
  by their exact real-time representative rather than a modulo-one class.
- Proved noncompactness and ordinary Fredholm failure independently for the
  quantum propagator.
- Separated physical time from trace-class heat/Wick time.
- Added the strict A0--A4 tuple, complete limitations, bilingual abstracts,
  declarations, and both mandatory seven-mode integrity gates.

Snapshot: `paper/main_round2.pdf`; release target: `paper/main.pdf`.

No external reviewer or acceptance score is represented.  These are
evidence-anchored internal theorem and presentation passes.
