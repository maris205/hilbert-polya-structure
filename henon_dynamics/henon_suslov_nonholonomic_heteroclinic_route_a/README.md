# HCS-C255 — Suslov heteroclinics and clean rotations

This package closes the classical Euler–Poincaré–Suslov rigid body after the
constraint axis is aligned with the third body axis.  A rotation in the
allowed plane diagonalizes the restricted inertia, so the frozen matrix loses
no genericity within the classical three-dimensional problem.

For nonprincipal constraint axes, every positive reduced energy ellipse has
two permanent rotations and two explicit heteroclinic arcs.  The arcs have a
closed `tanh/sech` parametrization.  Crucially, the permanent reduced states do
not disappear in reconstruction: every nonzero one is a periodic `SO(3)`
rotation, and its left translates form a clean continuum.  The principal-axis
boundary makes every reduced state permanent.

The reduced Poisson bracket and invariant half-plane density are exact but
singular on the permanent-rotation line.  The strict evaluator tuple is
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, with
`ROUTE_A_REJECTED`, Route B false, and scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Run the six scripts in `code/` to reproduce the evidence and release.  The
compiled paper is [paper/main.pdf](paper/main.pdf).
