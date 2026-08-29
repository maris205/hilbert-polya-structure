# Experiment plan

## Claim-led objective

Establish one complete result for the nonautonomous two-level crossing: a
Weber scalar reduction, the exact infinite-time connection matrix, its
probability/phase invariants and limits, and a transparent finite-window
control.  The central claim is `P_diabatic=exp(-2*pi*g^2/v)`; no numerical fit
defines this law.

## Frozen grid

Use five exact rational `(v,g)` cases: `(1,1/2)`, `(4,1/3)`, `(1/4,3/4)`,
`(2,-1/2)`, and `(3/2,0)`.  For each, integrate both basis vectors on
`[-T,T]` for `T=2,4,8` with 2048 fixed RK4 steps in 80-digit arithmetic.
Serialize 68 significant digits.  Record every matrix entry, `P_window`, the
asymptotic probability, discrepancy, and Gram residual.

## Independent controls

The checker duplicates the ODE stepper rather than importing producer code.
SymPy checks the Weber signs, Pauli square, SU(2) determinant/unitarity,
`dP/delta`, and the `sigma_z` coupling-sign gauge.  Clean replay compares
canonical bytes.  Mutation tests repair hashes after changing semantic,
nested-unknown, and top-level fields, and separately test a stale hash.

## Release gates

Run the five scripts, compile LuaLaTeX twice at fixed epoch `1787875200`,
remove all sidecars, verify embedded subset fonts and 2–6 pages, and ensure
the three round PDFs are byte-distinct with `main.pdf == main_round2.pdf`.
The self-excluded manifest must close exactly 27 payload files.  Route-A is
reported as rejected and Route B remains disabled.
