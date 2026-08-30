# HCS-C253 — Moran fixation and Green atlas (Route A)

This package freezes a finite continuous-time Moran birth--death process.  For
a population of size N and type count i, the rates are
lambda_i=beta*rho*i*(N-i)/N and mu_i=beta*i*(N-i)/N, with absorbing states
0 and N.  The theorem-scale advance is an exact fixation probability for every
selection ratio, a rational Green matrix and absorption-time solution, and a
reversible killed-chain weight.  Neutral, zero-rate, singleton, and selection
boundary faces are explicit.

Eight exact rational receipts are independently reconstructed, symbolically
checked, replayed, and mutation tested.  This is source-local probability; no
target arithmetic, Euler factor, root number, automorphy, target divisor, or
Hilbert--Polya operator is claimed.  Route B is disabled.  The final paper is
paper/main.pdf.
