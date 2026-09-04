# Source audit

## Verified sources

Mitchell and Rossi, DOI `10.1063/1.2912991`, give a modern planar
Kirchhoff-vortex convention, the rotation law, and the Love-mode formula.  In
that source mapping the perturbation coordinate is fitted relative to the
instantaneous ellipse: its principal axes co-rotate, and `lambda_m` is the
frequency in that co-rotating frame.
Love's 1893 paper, DOI `10.1112/plms/s1-25.1.18`, is the classical source.
Miyazaki and Hanazaki, DOI `10.1017/S0022112094000339`, study a vertically
stratified baroclinic extension; this package cites it only to mark what the
planar theorem does not cover.

## Package-owned derivation

The paper rederives the interior linear velocity's normal boundary motion,
the Love factorization in a form that remains defined at zero vorticity, the
`m=1` and `m=2` identities, the
sign of the second factor, uniqueness and strict ordering of all thresholds,
the cubic first wall, and the threshold-ladder asymptotic.  It also states
the half-turn period correction explicitly.

## Evidence boundary

The exact 561-by-64 panel, 62 dyadic threshold brackets, and 390 rigid rows
are regression evidence.  They do not prove all-mode stability, nonlinear
behavior, or the limiting law.

## Collision audit

- C284 owns finite point-vortex relative equilibria, not a distributed
  constant-vorticity patch boundary.
- C299 owns viscous Lamb–Oseen diffusion, not inviscid ellipse rotation.
- C368 owns source/sink Polubarinova–Galin Laplacian growth, not
  area-preserving Euler contour transport.

No priority claim is made for the classical Kirchhoff or Love results.
