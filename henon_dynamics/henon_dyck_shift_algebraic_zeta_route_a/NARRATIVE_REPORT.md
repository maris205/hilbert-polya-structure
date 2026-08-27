# Narrative report

The central advance is closure across all parameters rather than another
finite table.  The context-free circular-code series obeys
`g_N=Nz^2/(1-g_N)`, whose small solution is
`g_N=(1-sqrt(1-4Nz^2))/2`.  The source specialization gives
`zeta_N=(1-g_N)/(1-Nz-g_N)^2`.  Thus, with
`s=sqrt(1-4Nz^2)`, the one-vertex edge-type Dyck zeta is

`2(1+s)/(1+s-2Nz)^2`.

Extracting `z d/dz log zeta` yields explicit odd and even binomial-tail
formulas for every fixed count.  Möbius inversion provides primitive words and
only then division by the period provides cycles.  Direct enumeration audits
that convention by reducing all cyclic factors of the periodic extension.

The finite `2n` audit is a theorem, not a cutoff guess.  The nonzero reduction
of one period has normal form `B A` (unmatched closes followed by unmatched
opens).  In powers, a mismatch can first occur only at an `A B` interface; if
the first interface is compatible, excess opens or closes drift monotonically,
or cancel equally, so later copies create no new comparison.  Hence any zero
factor has a zero cyclic subfactor in two consecutive periods.

At `N=1` the radical cancels and the system has zeta `1/(1-2z)`, exactly the
full two-shift boundary.  For `N>1`, `z=1/(N+1)` is a double pole strictly
inside the branchpoints `+-1/(2 sqrt(N))`.  Quadratic conjugation changes the
function, proving nonrationality, while binomial tails give fixed-count and
primitive-cycle asymptotics.  These symbolic singularities are not identified
with target arithmetic singularities.

Krieger--Matsumoto Proposition 3.1 proves, specifically for Markov-Dyck
shifts, that topological entropy equals the exponential periodic-point growth
rate.  Combining that source-locked theorem with the fixed-count asymptotic
gives `h_top(D_N^E)=log(N+1)`.  This is not asserted as a general principle for
arbitrary dynamical systems.

The exact route record is `overall=ROUTE_A_REJECTED` with
`route_b_invocation_allowed=false`.
