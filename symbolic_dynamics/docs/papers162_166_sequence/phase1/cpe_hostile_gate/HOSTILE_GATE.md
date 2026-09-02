# Independent hostile gate — cyclic partition erosion (`CPE`)

**Audit date:** 2026-09-03 UTC  
**Literal map:** `E(pi)=pi meet sigma(pi)` on `Pi(Z/nZ)`, fine-to-coarse order  
**Verdict:** **`KILL_INTERNAL_COLLISION_P110`**  
**External state:** **`HOLD_EXTERNAL`**

## Outcome first

The displayed mathematics survives hostile rederivation.  I found no
counterexample to the translate window, point-clock indexing, the `n=1,2`
boundary, the sharp `n-2` maximum, either Möbius orientation, or the terminal
Touchard formula.  A separate bit-mask verifier makes **2,903,526** exact
assertions and passes, including every target after the claimed stabilization
cap, which the scout verifier did not test.

The candidate nevertheless fails the P162--P166 selection threshold.  The
scout's collision account contains a material factual error: P110 does not
use integer partitions or a different carrier.  P110 already acts on the
same full Bell phase space `Pi_n`, under the same cyclic relabelling, by the
dual update `pi -> pi join sigma(pi)`.  It already owns the same consecutive
translate engine, the same divisor-indexed coset fixed set, the same
`(1-u)^(-tau(n))` zeta function, and the same sharp maximum depth `n-2`.
After those are subtracted, CPE leaves a circular-run description and a
formal incidence-inversion fibre formula whose terminal specialization is a
second Möbius inversion.  The latter two are one inverse-enumeration axis, not
two independent axes.  That residual is mathematically correct but is not a
genuinely different paper-sized dynamical system under the batch anchor.

This is a portfolio/internal-collision kill, not an assertion that the meet
map is conjugate to P110's join map.  In fact the ordinary partition lattice
is not self-dual for general `n`; the two maps are distinct.  Distinct is not
sufficient here: the occupied carrier, scheduler, semilattice-window proof,
fixed atlas, zeta, and sharp clock coincide at the mechanism level.

## 1. Independent rederivation

### 1.1 Window identity

Translation is a partition-lattice automorphism.  Therefore

```text
E^(t+1)(pi)
 = E^t(pi) meet sigma(E^t(pi))
 = (meet_(j=0)^t sigma^j(pi))
     meet (meet_(j=1)^(t+1) sigma^j(pi))
 = meet_(j=0)^(t+1) sigma^j(pi).
```

With `E^0(pi)=pi`, induction proves

```text
E^t(pi)=meet_(j=0)^t sigma^j(pi)                     (A)
```

for every `t>=0`.  The window contains `t+1` translates; there is no missing
or extra endpoint.

Every nonfixed step is a strict refinement, so a recurrent state must be
fixed.  If `E(pi)=pi`, then `pi <= sigma(pi)`.  The two partitions have the
same number of blocks, hence are equal.  Thus fixedness is exactly
translation invariance.  For the regular action of `Z/nZ`, invariant
equivalence relations are the coset partitions of subgroups, one for every
divisor of `n`.  This gives `tau(n)` fixed points and no nontrivial cycles.

### 1.2 Pair clock and its indexing

Fix a difference `delta` and put

```text
G_delta={x : x ~_pi x+delta}.
```

Under the convention that `sigma` moves labels forward by one, (A) gives

```text
x ~_(E^t(pi)) x+delta
  iff x, x-1, ..., x-t all belong to G_delta.          (B)
```

Changing the sign only reverses the circular window and does not change its
length.  If a proper `G_delta` has longest cyclic true run `L`, a pair at the
end of such a run is still present at time `L-1` but is absent at time `L`.
All pairs not belonging to the translation-invariant core have disappeared
by time `L`.  Hence

```text
h(pi)=max_(G_delta proper) L_delta,                    (C)
```

with the maximum of the empty set equal to zero.  The depth is `L`, not
`L-1`.

### 1.3 The `n-2` cap and the two small boxes

For fixed `delta`, the permutation `x -> x+delta` is a union of cycles.  On
any one cycle, if every equivalence edge except one is true, transitivity
around the remaining path forces the last edge true.  Consequently a proper
`G_delta` cannot have exactly one false position.  In an order-two cycle the
two orientations of the same unordered pair already duplicate the false
position.  A proper binary circular word `G_delta` therefore has at least two
zeros and no true run longer than `n-2`.

For `n>=3`, the partition

```text
{0} | {1,2,...,n-1}
```

has, for `delta=1`, true positions `1,...,n-2` and the two defects `0,n-1`.
Its depth is `n-2`, proving sharpness.

- `n=1`: there is no nonzero difference and the unique state is fixed.
- `n=2`: the two set partitions are discrete and indiscrete, both invariant.
  For the only nonzero difference, symmetry makes its two indicators equal,
  so the tempting one-defect counterexample cannot occur.

Thus the exact universal height is zero for `n=1,2` and `n-2` for `n>=3`.

### 1.4 Every-target polynomial: order and signs

Let

```text
F_(t,eta)(z)=sum_(E^t(pi)=eta) z^b(pi)
```

and, for a test partition `theta`, sum over targets coarser than `theta`:

```text
G_t(theta)=sum_(eta>=theta) F_(t,eta)(z).
```

Using (A),

```text
E^t(pi)>=theta
 iff sigma^j(pi)>=theta for every 0<=j<=t
 iff pi>=sigma^(-j)(theta) for every 0<=j<=t
 iff pi>=J_t(theta),
```

where `J_t(theta)=join_(j=0)^t sigma^(-j)(theta)`.  If this join has `m`
blocks, its coarsenings are precisely the set partitions of those `m` blocks;
their source-block enumerator is `B_m(z)`.  Hence

```text
G_t(theta)=B_(b(J_t(theta)))(z).
```

Upper-interval Möbius inversion now gives

```text
F_(t,eta)(z)
 = sum_(theta>=eta) mu_Pi(eta,theta)
     B_(b(J_t(theta)))(z).                            (D)
```

The direction in (D) is correct.  If a block `A` of `theta` contains `r_A`
blocks of `eta`, the standard interval product gives

```text
mu_Pi(eta,theta)
 = product_(A in theta) (-1)^(r_A-1)(r_A-1)!,         (E)
```

also with the printed sign.  The independent verifier reconstructs every
value in (E) recursively from incidence before comparing with the factorial
formula.

This derivation also exposes the credit ceiling.  For any finite lattice,
any automorphism, and any chosen weight enumerator of upper intervals, the
same meet-window argument followed by incidence inversion gives (D).  The
Touchard polynomial enters only because an upper interval of `Pi_n` is a
smaller partition lattice.  The formula is useful and correct, but largely a
formal semilattice template once the map is chosen.

### 1.5 Terminal Touchard--Möbius basins

Let the fixed target `rho_H` have `d=[Z/nZ:H]` blocks.  Every source whose
core is `rho_H` coarsens `rho_H` and descends to a partition of the `d`
quotient points.  Its core is exactly `rho_H` iff the quotient core is the
discrete `d`-block congruence.

Write `P_d(z)` for the block-marked count of partitions of a `d`-cycle with
discrete core.  Every partition of the `d` points has one invariant core,
whose number of blocks is some `e|d`.  Coarsening the corresponding
congruence is equivalent to partitioning its `e` blocks, so

```text
B_d(z)=sum_(e|d) P_e(z).
```

Ordinary divisor Möbius inversion yields

```text
P_d(z)=sum_(e|d) mu(d/e) B_e(z).                      (F)
```

This proves the terminal orientation.  It also shows why (F) is not an
independent third axis: it is the fixed-target/stable-time compression of the
same fibre enumeration and uses only the divisor lattice of fixed cores.

Since a source has depth at most `t` exactly when `E^t(pi)` is fixed,
summing (D) over the fixed targets gives the claimed depth census.  Since
every periodic state is fixed, `#Fix(E^r)=tau(n)` for every `r>=1`, and the
Artin--Mazur calculation gives

```text
zeta_E(u)=exp(sum_(r>=1) tau(n)u^r/r)
         =(1-u)^(-tau(n)).
```

## 2. Findings by severity

### Critical C1 — P110 is the same occupied dynamical family

The scout says P110 acts on integer partitions and has a different carrier.
Both statements are false.  P110's own frozen README and theorem package
define

```text
Pi_n = all set partitions of Z/nZ,
J(pi)=pi join sigma(pi).
```

The collision is exact in five structural coordinates:

| Coordinate | P110 | CPE |
|---|---|---|
| carrier and scheduler | full `Pi_n`, cyclic relabelling | same |
| iterate engine | join of `t+1` consecutive translates | meet of `t+1` consecutive translates |
| recurrent atlas | cyclic subgroup cosets | same |
| periodic invariant | `(1-u)^(-tau(n))` | same |
| sharp universal depth | `0,0,n-2` | same |

P110 additionally has a deepest-shell classification, while CPE supplies
only a sharp witness.  Reversing the semilattice operation changes the
literal map and basin counts, but it does not create a genuinely fresh
dynamical type for a breadth batch whose anchor expressly excludes cosmetic
carrier or mechanism variants.

**Executable disposition:** do not freeze CPE into a numbered paper.  Retain
this gate and the scout as killed evidence; return the slot to breadth
scouting.

### Major M1 — the proposed residual does not have two independent axes

After P110 and classical ingredients are credited away, the remaining claims
are:

1. the meet-side circular-run realization of a sharp clock already known to
   have the same global value in P110; and
2. the general upper-interval incidence inversion (D), with the terminal
   divisor inversion (F) as its stable fixed-target specialization.

Items (D) and (F) are not independent axes.  The claimed “complete
fixed/terminal atlas” repeats the fixed classification and zeta already in
P110, while its new basin polynomial is downstream of the every-target
formula.  The phase size `B_n` is also a trivial carrier cardinality, not an
independent identifiability theorem.  The residual therefore misses the
batch requirement of a separate structural/inverse/extremal axis after
collision subtraction.

### Major M2 — source attribution and software scope need correction

The 2025 group-action paper is by Marina Anagnostopoulou-Merkouri, R. A.
Bailey, and Peter J. Cameron, not Cameron, C. E. Praeger, “and
collaborators.”  It directly owns the invariant-partition/subgroup
correspondence used in the fixed atlas.  The August 2026 crate does expose a
`cyclic_refine` primitive for two already periodic compact partitions, but
its documentation says that backend is not for arbitrary partitions after a
refinement leaves the periodic form.  Neither source was found to own the
literal dynamics.  Exact details and links are recorded in
`OWNER_SEARCH_SUPPLEMENT.md`.

### Minor m1 — the scout overstates its all-time verification coverage

The author verifier's fibre loop is

```text
range(0,max(1,n-1)),
```

so for `n>=2` it checks only `t=0,...,n-2`, not “all times.”  Stabilization
makes later times mathematically reducible, but the claimed coverage is still
not literal.  The hostile verifier checks all targets for `n<=6` through
`t=n+2`, plus all `n=7` targets at `t=0,5,6,9`; all pass.

### Minor m2 — fibre counts do not specify the entire rooted graph

Equations (D)--(F) determine target-resolved ancestor polynomials at each
time and terminal basin totals.  They do not by themselves reconstruct every
edge or isomorphism type of each rooted functional-graph component.  The
scout phrase that the rooted refinement DAGs are “specified by (7)--(10)”
should be read as enumerated, not structurally classified.

## 3. Internal collision screen beyond P110

- **P135:** its state is an integer partition/cycle type and its update is a
  derived-centralizer orbit-size transform.  Orbit partitions and coefficient
  fibres are shared vocabulary only; there is no literal reduction.
- **P143:** its state is an arbitrary Boolean relation and its update is
  row-support inclusion.  Its every-target incidence/inclusion--exclusion
  package makes generic inverse-poset language zero credit, but it is not the
  same map.
- **P154:** its state is a subgroup of a dihedral group and its update is the
  normalizer.  Subgroup/divisor terminal indexing and zeta bookkeeping are
  generic overlap, not a direct map collision.
- **P110:** fatal, as stated above.  It already occupies cyclic semilattice
  dynamics on the full set-partition lattice, including the same temporal
  spine and global invariants.

There is no demonstrated literal conjugacy with P110: for `n>=4`, the full
partition lattice is not self-dual (the atom/coatom counts differ), so a
blanket meet/join complement argument would be invalid.  The kill rests on
the explicit batch collision policy and shared theorem engine, not on a
false duality theorem.

## 4. Independent exact control

Run:

```bash
python3 docs/papers162_166_sequence/phase1/cpe_hostile_gate/verify_independent.py
```

The implementation represents a partition as canonical disjoint bit masks,
unlike the scout's restricted-growth strings.  It independently implements
rotation, intersection refinement, union--find join, literal iteration,
incidence-recursive partition Möbius values, and direct Touchard counts.

Frozen output:

```text
CPE_HOSTILE_GATE_INDEPENDENT_V1
representation=canonical_bitmask_blocks
temporal=all_partitions_n1..8_times0..n+2
pair_clock=all_points_all_deltas_n1..8_times0..n+1
fibres=all_targets_n1..6_times0..n+2_plus_n7_t0,5,6,9
partition_mobius=incidence_reconstruction_n1..7
terminal_basins=all_partitions_n1..9
row_sha256=63e599900e8593559886cb2d49509b475251e5e02a17549dd1e4bb9c2a7e527f
assertions=2903526
STATUS PASS
```

Finite verification is counterexample pressure, not an all-parameter proof
or an ownership certificate.

## Final decision

```text
CPE  KILL_INTERNAL_COLLISION_P110
mathematics  PASS_AS_STATED
direct_external_owner  NOT_FOUND_BOUNDED
paper_threshold_after_subtraction  FAIL
HOLD_EXTERNAL
```

No paper drafting, external posting, specialist contact, or priority claim is
authorized.
