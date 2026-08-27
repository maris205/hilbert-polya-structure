# P24 Round-3 conclusion — target-free classical-Schottky control

## Result

Round 3 lands a reproducible rank-4 classical Schottky/Kleinian control with no
arithmetic owner and no target data in its definition, cutoff, or shuffle.
The group theorem is `[PROVED]`; the finite marked-word ledger and floating
complex-length fields are `[NUMERICALLY_CERTIFIED]`; the reported intrinsic
phase/length scores are `[NUMERICAL_OBSERVATION]`.

## Self-contained ping-pong certificate

For each of four frozen fixed-point pairs `(r_j,a_j)`, set

```text
h_j(z) = (z-a_j)/(z-r_j),
mu = (3+4i)/50000,       |mu| = 1/10000,
g_j = h_j^(-1) o (mu *) o h_j.
```

Define the two closed round disks

```text
D_j^+ = {|h_j(z)| <= 1/1000},
D_j^- = {|h_j(z)| >= 10}.
```

The code represents every coefficient as a Gaussian rational.  It verifies
exactly that `h_j g_j = diag(mu,1) h_j` and the inverse identity.  Because
`|mu|*10=1/1000`, these identities give

```text
g_j(C-hat \ D_j^-)     = interior(D_j^+),
g_j^-1(C-hat \ D_j^+) = interior(D_j^-),
```

with boundary mapped to boundary.  The Apollonius centers and radii are exact
rationals.  All 28 pairs among the eight closed disks have positive squared
separation margin; the minimum is exactly `10201/10101`.

The ping-pong lemma makes every nonempty reduced word nonidentity and proves
that the four generators freely generate.  The paired-round-disk fundamental
domain is a classical Schottky domain, hence the group is discrete,
torsion-free, purely loxodromic, and convex-cocompact.  In particular there are
no parabolics or cusps.  The quotient is an infinite-volume Kleinian
non-lattice, so it is not a finite-volume manifold matched to the Bianchi
quotient.  Possible containment in a larger arithmetic ambient group is not
decided and remains `[OPEN]`.

The nonzero argument of `mu` supplies genuine screw holonomy; this is not a
real/Fuchsian zero-holonomy surrogate.

## Frozen match contract and ledger

Only three structural axes are matched to the Round-2 Bianchi sample:

```text
positive-generator rank     = 4
oriented alphabet size      = 8
maximum reduced-word length = 5
```

No parameter was chosen by a prime list, a zero list, an arithmetic roof, an
arithmetic weight, or a target score.  Finite volume, cusp structure, covolume,
length distribution, and full-group orbit count are explicitly unmatched.

The exact and numerical ledger totals are:

```text
paired round domains                         8
pairwise closed-disk checks                 28
exact forward/inverse conjugacy identities  8
reduced words including identity        22,409
distinct exact projective matrices       22,409
cyclically reduced marked words          19,624
oriented cyclic classes                   4,148
primitive oriented classes                4,092
repetition oriented classes                  56
unoriented orientation pairs              2,074
self-inverse oriented classes                  0
maximum invariant reconstruction residual 1.097e-14
```

Primitive and repetition labels are exact consequences of cyclic words in the
proved free group.  Orientation, cyclic multiplicity, trace-invariant
collision multiplicity, holonomy, and stable/unstable multipliers are retained.
Completeness is exact only for the frozen marking and word cutoff; it is not a
metric length-spectrum cutoff.

## Target-free diagnostic

On the 4,092 primitive oriented classes, the frozen intrinsic phase/length
score is

```text
observed control holonomy = 0.02581113482706927
frozen holonomy shuffle   = 0.023492229061869797
```

The closeness of these two values is only a `[NUMERICAL_OBSERVATION]`.  It
neither establishes nor refutes the Bianchi arithmetic hypothesis.  A
cross-system kill decision is deferred until a comparison statistic is
predeclared and the Bianchi completeness mismatch is handled.

## Route boundary

```text
PROPOSAL_STAGE=1
ROUTE_A_SCOPE=A0-A1
FORMAL_ROUTE_A_TUPLE=UNASSIGNED
A2_A4_EVALUATION=NOT_EVALUATED
ARITHMETIC_HYPOTHESIS_VERDICT=OPEN
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
```

This control does not create an orbit-to-prime-ideal map, Riemann-`zeta` A0
credit, a dynamical determinant, or a quantum/operator claim.
