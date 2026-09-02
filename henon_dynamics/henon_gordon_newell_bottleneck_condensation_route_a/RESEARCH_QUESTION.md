# Research question — HCS-C285

For an arbitrary finite irreducible routing matrix that need not be
reversible, can one close in one theorem the fixed-population
Gordon–Newell stationary law, its complete occupancy calculus, physical
service flows, exact time reversal, and the unique-versus-tied bottleneck
thermodynamic limit, without hiding zero, equal-weight, or small-population
faces?

The frozen answer is yes for single-class closed networks with one positive
rate exponential single server at each station:

- `Z_N` is the complete homogeneous polynomial `h_N(w)`;
- all joint factorial moments are its weight derivatives;
- station and directed edge event flows are exact multiples of
  `Z_(N-1)/Z_N`;
- routing reversal is `p*_ij=e_j p_ji/e_i` and is not assumed equal to `P`;
- all nonbottleneck occupancies converge jointly to independent geometric
  variables;
- the tied bottleneck shares converge jointly to an independent uniform
  Dirichlet vector, with the unique bottleneck as the degenerate `r=1` case.

The theorem does not ask whether this classical queueing model is new. Gordon
and Newell own the classical product-form and bottleneck lineage. The research
task is an exact source-local closure with explicit proof, boundaries,
independent executable reconstruction, and a strict Route-A stopping result.

## Falsification gates

The package fails if any one of the following survives:

1. an irreducible nonreversible rational routing case violates exact global
   balance under the proposed monomial weights;
2. the Fraction left nullspace of a finite generator differs from the product
   law;
3. direct enumeration, generating-function convolution, and Newton recurrence
   disagree on `Z_N`;
4. event-flow self-route semantics are confused with state-change generator
   semantics;
5. time reversal is not involutive, or reversibility is asserted at `N=0`
   as a routing criterion;
6. a tied maximal weight is silently split or replaced by a deterministic
   equal share;
7. finite `N<=32` regression evidence is described as proof of an all-`N`
   or thermodynamic theorem;
8. any prime, target zero, Euler factor, root number, or Route-B artifact
   enters the owner.
