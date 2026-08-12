# HCS-C32 Phase 3: the Morse-local Hill-information gate

Status: `PHASE3_COMPLETE_PENDING_USER_CHECKPOINT`

This directory contains the authorized Phase-3 analysis of one sharply scoped
question:

> Can the critical-value vanishing-cycle contribution of the finite-field
> Hénon action detect the actual Hill multiplier
> \(\det(I-DH_6^n)\) beyond the universal quadratic/Morse invariant?

The dynamical system is the area-preserving Hénon map

\[
H_6(q,p)=(1-6q^2-p,q)
\]

with generating function

\[
S_6(q,Q)=qQ-q+2q^3
\]

and chronological cyclic action

\[
\Phi_n(x_0,\ldots,x_{n-1})
=\sum_{i\bmod n}S_6(x_i,x_{i+1}).
\]

The directory is intentionally separated from a paper draft.  A manuscript is
not authorized until the exact gate, independent checker, and Devil's Advocate
Checkpoint 2 are complete.

## Phase-3 artifacts

- `EXACT_GATE_PROTOCOL.md`: frozen mathematical question, convention locks,
  success criterion, and STOP rules;
- `code/`: exact producer, independent checker, mutation tests, and runner;
- `results/`: machine-readable certificate and collision census;
- `SYNTHESIS_REPORT.md`: Phase-3 evidence integration;
- `DEVILS_ADVOCATE_CHECKPOINT2.md`: mandatory bias and logic stress test.
- `paper/README.md`: manuscript hold and reopening rule; no draft is silently
  promoted before the checkpoint.

## Main result

The good-prime unframed Morse-local factor cannot recover the complete Hénon
Hill determinant.  Over (mathbb F_{61}), two distinct primitive period-five
cycles have the same action value and explicitly congruent Hessian forms, but
their Hill values are (44) and (7).  The henselian Morse lemma makes their
local function germs and Morse-local Fourier representations isomorphic.

The exact decision is:

\[
\texttt{MORSE\_LOCAL\_HILL\_GATE=STOP}.
\]

This redirects the next large step to the Hénon parameter discriminant and
its global monodromy; it does not abandon Hénon dynamics.

## Scope firewall

This project does not claim a Hilbert--Pólya operator, a Riemann-zeta factor,
or a new general stationary-phase theorem.  A good-prime Morse-local
obstruction does not rule out degenerate singularities, discriminant-family
monodromy, or other Hénon deformations; those are separate candidates.
