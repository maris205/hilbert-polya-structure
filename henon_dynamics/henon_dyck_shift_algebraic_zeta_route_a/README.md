# HCS-C205: algebraic zeta of the one-vertex edge-type Dyck shift

For every `N>=1`, this package closes the periodic-point theory of the
edge-type Dyck shift of the graph with one vertex and `N` loop edges.  Starting
from the Krieger--Matsumoto zeta formula, it gives all fixed counts in binomial
form, all primitive points and orbits, the `N>1` double dominant pole and
asymptotic, branchpoints and nonrationality, topological entropy `log(N+1)`,
and the exceptional `N=1` full two-shift boundary.

The exact ledger covers `N=1..6`, periods 1--24, and 33 direct periodic-word
enumerations.  Reproduce with the five `c205_dyck_shift_*` scripts and close
with `c205_release_manifest.py`.

The fixed-point convention counts origin-marked periodic sequences.  Division
by the period occurs only after Möbius inversion.  Scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`; the exact route record is
`overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`.
