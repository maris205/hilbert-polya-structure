# Two-round substantive improvement log — HCS-C302

## Round 0 — exact finite distributions

The original manuscript freezes the distinct-key, first-pivot,
comparison-only model.  It proves the PGF recurrence for every `n` and derives
the exact harmonic-number mean and variance, including `n=0,1` and the
deterministic two-key case.

## Round 1 — contraction with the varying-subproblem gap closed

The first revision adds exact `(n+1)` centering and the finite toll grid.  It
proves the `sqrt(2/3)` quadratic-Wasserstein contraction and fixed-point
uniqueness.  Hostile review correctly rejected the phrase “apply the same
estimate” as insufficient for finite-size convergence.  The revision now
defines `d_n`, proves uniform `L2` boundedness from the variance formula,
splits small endpoint subproblems at a fixed cutoff, and obtains the explicit
limsup inequality `D <= sqrt(2/3)(D+eta)`, hence `D=0`.

## Round 2 — third-moment license and release boundary

The second revision does not cube an `L2` variable without justification.  It
constructs the endogenous binary-tree toll series and uses conditional
Rosenthal bounds with level sums `(2/3)^r` and `(1/2)^r` to prove `L3`
convergence.  It then evaluates the beta derivatives, establishes
`m_3=16*zeta(3)-19>67/1500`, and rules out Gaussianity.  The revision also
adds exact evidence sizes, endpoint and alternate-cost boundaries, primary
literature ownership, C291 separation, the all-fail Route-A tuple, locked
Route B, and AI-use disclosure.

The final `main.pdf` is byte-identical to round 2.
