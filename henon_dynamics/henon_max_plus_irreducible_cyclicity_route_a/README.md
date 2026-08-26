# HCS-C188: irreducible max-plus cyclicity

This package freezes every irreducible rational max-plus matrix
`A in (Q union {-inf})^(n x n)`.  With `lambda` the maximum cycle mean,
`B=A-lambda`, and `gamma` the lcm of the cyclicities of the strongly connected
components of the critical graph, the classical cyclicity theorem gives the
minimal ultimate matrix-power period exactly `gamma`.

The release integrates that theorem with exact CSR representation, the least
transient, vector and projective orbit periods, attraction cones, the
eigencone, ultimate column spans, the primitive boundary, a fixed-support
unbounded-transient family, and the reducible multirate obstruction.  It is one
all-parameter dynamical classification, not a collection of example papers.

## Exact theorem

There is a matrix-dependent finite `T` such that

```text
B^(t+gamma) = B^t  for every t >= T,
```

and `gamma` is the least positive eventual matrix period.  Moreover,

```text
T = min { t >= 0 : B^(t+gamma) = B^t }.
```

One equality suffices because right max-plus multiplication by every later
power propagates it.  With the standard critical matrices `C,S,R`, there is a
possibly different matrix-dependent `T_CSR` for which
`B^t = C S^t R` for all `t >= T_CSR`.

Every vector orbit and every nonzero projective orbit has ultimate period
dividing `gamma`; the period can be strictly smaller.  For `p | gamma`, its
attraction cone is the exact two-sided max-plus linear solution set

```text
Attr_p(B) = {x : B^(T+p) x = B^T x}.
```

The exact-period-`p` stratum removes all `Attr_q` for proper divisors `q|p`.

## Sharp transient boundary

For

```text
B_m = [[0,-m],[0,-1]],  m >= 1,
```

the support and dimension are fixed and the lower-right entry of `B_m^t` is
`max(-t,-m)`.  Its minimal transient is exactly `m`.  Hence no transient bound
depending only on dimension and support, but not weights, can hold.  The
primitive condition `gamma=1` means eventual constancy, not transient zero.

## Reproduce

Run from the repository root:

```bash
python henon_dynamics/henon_max_plus_irreducible_cyclicity_route_a/code/c188_max_plus_producer.py
python henon_dynamics/henon_max_plus_irreducible_cyclicity_route_a/code/c188_max_plus_checker.py
python henon_dynamics/henon_max_plus_irreducible_cyclicity_route_a/code/c188_sympy_crosscheck.py
python henon_dynamics/henon_max_plus_irreducible_cyclicity_route_a/code/c188_replay.py
python henon_dynamics/henon_max_plus_irreducible_cyclicity_route_a/code/c188_mutation.py
python henon_dynamics/henon_max_plus_irreducible_cyclicity_route_a/code/c188_release_manifest.py
```

The exact regression contains 177 matrices, 901 vector rows, 441 simple
cycles, and 189 critical components.  The independent checker uses Karp's
cycle-mean formula, closure-based critical edges, Tarjan SCCs, the distance-gcd
cyclicity formula, and binary powers; it does not import the producer.

## Route-A verdict

`(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`, overall
`ROUTE_A_REJECTED`; Route B is false.  Scope literal:
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Rational max-plus weights and critical cycles have no intrinsic rational-prime
semantics, CSR supplies no target divisor, and a tropical semimodule is not a
source-native Hilbert-space quantization.  This package claims neither global
novelty nor external review.
