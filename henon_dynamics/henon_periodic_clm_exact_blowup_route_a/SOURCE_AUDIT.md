# Source and collision audit

## Primary source check

The publisher record for Constantin–Lax–Majda identifies the 1985 CPAM paper, pages 715–724, DOI `10.1002/cpa.3160380605`, and describes an exactly solved one-dimensional vorticity model with finite-time breakdown phenomena. The arXiv record `2010.01201` identifies Lushnikov–Silantyev–Siegel, its 2021 *Journal of Nonlinear Science* publication and DOI `10.1007/s00332-021-09737-x`, and explicitly includes periodic boundary conditions in its generalized-CLM study.

## Convention control

Hilbert-transform signs vary in the literature. This package never imports a formula without rederiving it from `H(e^{ikx})=-i sign(k)e^{ikx}`. The evidence independently verifies `H sin=-cos`, the periodic Tricomi identity, the Riccati sign, both exact solutions, and the pole relation.

## Arithmetic-control audit

Fourier labels are analytic modes, not an arithmetic carrier. The exact ledger therefore compares prime, composite, and unit modes after removing the label, applies the fixed permutation `k -> 1+((5(k-1)+3) mod 16)`, checks every neighboring mean--amplitude threshold cell, and replays the simpler zero-mean parent. All four controls are reconstructed by the independent checker. Their invariance is negative evidence at A0, not evidence for a target.

## Repository collision boundary

- C309 owns finite matrix Riccati/Möbius dynamics.
- C324 owns Hunter–Saxton geometric blow-up.
- C278 owns Camassa–Holm peakons.
- C363 owns Keller–Segel mass concentration.

C377 owns only the arbitrary-mean periodic-Hilbert closure, exact first-pole clocks, and conditionally transverse profiles. It claims neither global literature novelty nor any consequence for three-dimensional Euler.
