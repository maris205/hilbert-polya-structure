# Root focused scout — cyclic partition erosion (`CPE`)

**Date:** 2026-09-03 UTC  
**Route:** A, finite/rank-changing dynamics  
**Carrier:** the Bell phase space of set partitions of `Z/nZ`  
**Author-side decision:** `GREEN_PENDING_INDEPENDENT_HOSTILE_GATE`  
**External state:** `HOLD_EXTERNAL`

## Outcome first

Let `sigma` cyclically translate labels and order set partitions by refinement.
For a partition `pi`, define the literal self-map

```text
E(pi) = pi meet sigma(pi),
```

where the meet is common refinement, equivalently intersection of the two
equivalence relations.  The operator is not a generic refinement loop: its
overlapping translate windows give a closed iterate, an exact point clock,
and a sharp universal clock.  Partition-lattice Möbius inversion then gives
an every-time, every-target polynomial recording the source block count.
At the terminal time this large formula collapses to a divisor Möbius
transform of Touchard polynomials, giving all fixed-target basin sizes.

The proposed paper-scale residual is the conjunction of:

1. the translate-window iterate, the circular-run point clock, and sharp
   height `n-2` for every `n>=3`;
2. the source-block-refined fibre polynomial for every target and every time;
3. the complete fixed/terminal atlas: divisor-indexed recurrent partitions,
   Touchard--Möbius basin polynomials, depth censuses, and zeta function.

Ordinary partition lattices, Bell/Touchard polynomials, their Möbius function,
and cyclic block systems receive zero contribution.  A bounded search found
no source for the literal iteration or the displayed temporal-plus-fibre
conjunction.  That non-hit is not novelty evidence, so an independent hostile
gate remains mandatory.

## 1. Literal iterate and recurrence

Write relations in the fine-to-coarse order.  Since translation preserves
meets, induction gives, for every `t>=0`,

```text
E^t(pi) = meet_(j=0)^t sigma^j(pi).                    (1)
```

Consequently every orbit moves weakly down the partition lattice and every
recurrent state is fixed.  Equality `E(pi)=pi` forces
`pi=sigma(pi)` (the two relations have the same cardinality), so fixed states
are exactly the translation-invariant partitions.  They are the coset
partitions `rho_H` for subgroups `H<=Z/nZ`; hence their number is `tau(n)`.

The stable core is

```text
C(pi)=meet_(j in Z/nZ) sigma^j(pi).                   (2)
```

It is the largest translation-invariant equivalence relation refining `pi`.
Equation (1) reaches (2) by time `n-2`, not merely `n-1`.

## 2. Exact point clock and sharp height

For `delta in Z/nZ`, let

```text
G_delta(pi)={x : x is pi-equivalent to x+delta}.
```

When `G_delta(pi)` is not the whole cycle, let `L_delta(pi)` be the largest
number of cyclically consecutive points contained in it; take the maximum of
the empty collection as zero.  Directly from (1),

```text
h(pi)=max_(G_delta(pi) != Z/nZ) L_delta(pi).           (3)
```

Indeed a pair of difference `delta` survives through time `t` precisely when
`t+1` consecutive translates of that pair belonged to the original relation.
If all but one translated pair belonged to an equivalence relation,
transitivity around the `delta`-cycles would force the last pair too (the
order-two case is already duplicated by symmetry).  Thus every proper
`G_delta` has no run longer than `n-2`.

For `n>=3`, the partition with one singleton and one `(n-1)`-block has a run
of length `n-2`.  Therefore

```text
max_pi h(pi)=n-2.                                     (4)
```

The exact boundaries are height zero for `n=1,2`; all partitions in those
two boxes are already translation invariant.

## 3. Every-time, every-target block-marked fibres

Let `b(pi)` denote block count and let

```text
B_m(z)=sum_k S(m,k) z^k
```

be the Touchard polynomial.  For a target `eta`, define

```text
F_(t,eta)(z)=sum_(E^t(pi)=eta) z^b(pi).                (5)
```

For `eta<=theta`, write `mu_Pi(eta,theta)` for the partition-lattice Möbius
function and put

```text
J_t(theta)=join_(j=0)^t sigma^(-j)(theta).             (6)
```

If `m(theta,t)` is the number of blocks of `J_t(theta)`, then

```text
F_(t,eta)(z)
 = sum_(theta>=eta) mu_Pi(eta,theta) B_m(theta,t)(z). (7)
```

This is an exact image test as well: `eta` occurs at time `t` iff (7) is not
zero.  To prove it, first count sources for which `E^t(pi)>=theta`.
Equation (1) makes this equivalent to `pi>=J_t(theta)`.  Coarsenings of a
partition with `m` blocks are set partitions of those `m` blocks, with
block enumerator `B_m(z)`.  Möbius inversion over `[eta,hat1]` gives (7).
The formula includes `t=0`, empty fibres, and arbitrary nonfixed targets.

The explicit interval value used in (7) is

```text
mu_Pi(eta,theta)
 = product_(A in theta) (-1)^(r_A-1) (r_A-1)!,       (8)
```

where `r_A` is the number of `eta`-blocks inside `A`.

## 4. Terminal basin atlas and temporal census

Let the fixed target `rho_H` have `d=[Z/nZ:H]` blocks.  A source above
`rho_H` factors to a partition of the `d` quotient points.  Its stable core
is exactly `rho_H` precisely when the quotient core is discrete.  Möbius
inversion on the subgroup/divisor lattice reduces (7) to

```text
P_d(z)=sum_(e|d) mu(d/e) B_e(z),                      (9)
```

and

```text
sum_(C(pi)=rho_H) z^b(pi)=P_d(z).                    (10)
```

Thus the unmarked basin size is `P_d(1)`; the degree of the marked basin
polynomial is exactly `d`, with leading coefficient one.  The basin sizes
sum to the Bell number `B_n`, and the functional graph is the disjoint union
of the `tau(n)` rooted refinement DAGs specified by (7)--(10).

For each `t`, the exact number of states of depth at most `t` is

```text
sum_(d|n) F_(t,rho_d)(1),                             (11)
```

so differences give every depth layer.  Since all recurrent points are fixed,
the Artin--Mazur zeta function is

```text
zeta_E(u)=(1-u)^(-tau(n)).                            (12)
```

For `n>=3`, the maximum depth alone recovers `n`; the phase size `B_n`
handles all boundary boxes and gives an independent recovery coordinate.

## 5. Collision ceiling

- Partition meet, the Bell and Stirling counts, Touchard polynomials, the
  partition-lattice Möbius formula, and Möbius inversion on divisors are
  classical and receive zero credit.
- Cyclically invariant partitions as block systems/cosets of subgroups are
  standard and receive zero credit.
- The August 2026 `partition-lattice` Rust crate implements exact partition
  refinement and cyclic/orbit representations.  It is treated as adjacent
  software, not as evidence for priority; no inspected module stated this
  self-map, its iterate, point clock, or target fibres.
- P110 acts on integer partitions by shift--join; P135 applies a derived
  centralizer orbit construction to integer partitions; P143 replaces a
  Boolean relation by row-support inclusion.  None is a meet with a moving
  cyclic translate on the Bell phase space, and none transfers (3) or (7).
- Generic closure/refinement language is not a contribution.  The paper may
  claim only the literal finite dynamics and the integrated formulas above.

## 6. Exact evidence

Run

```text
python3 docs/papers162_166_sequence/scouting/root_cyclic_partition_erosion/verify_scout.py
```

The verifier independently enumerates all partitions through `n=8`, checks
the literal and window iterates, the point clock, strict recurrence, sharp
height, fixed and stable-core atlases, and terminal marked basin formulas.  It
also compares (7), coefficient by coefficient, with literal every-target
fibres for all times in every box through `n=7`.  The frozen run makes
`215,712` exact assertions and ends in `STATUS PASS`.

Finite enumeration is counterexample pressure, not an all-parameter proof or
an ownership certificate.

## Author-side gate

```text
CPE  GREEN_PENDING_INDEPENDENT_HOSTILE_GATE
HOLD_EXTERNAL
```
