# Replacement algebraic lane for P147--P151

**Stage:** literal-system breadth scout and exact falsification.  
**External status:** `HOLD_EXTERNAL`.  
**Paper numbering:** deliberately unassigned.

## Outcome

The replacement lane tested **eight new literal systems** and replayed the old
`DNT` reserve.  The exact falsifier executed **1,048,472 assertions**.  The
tests are counterexample pressure only; none is offered as proof, novelty,
priority, or owner clearance.

`ZTL` is the only candidate recommended for immediate contract freeze.  Its
classical Lyness five-period identity receives zero credit.  What survives is
the complete graph of the zero-totalized map on the entire affine plane over
every odd finite field: a sharp exceptional tree, the full cycle census and
zeta function, and a codomain-wide `0/1/q` inverse atlas.

`QNC` is a genuinely independent, two-axis, paper-sized **reserve**.  It has a
sharp local-ring absorption theorem and a singular quadratic-congruence fibre
atlas, but the bounded search is not enough to clear the very broad
local/p-adic polynomial-dynamics literature.  It should not displace a
better-cleared finalist merely to fill a slot.

The other six new systems and `DNT` are killed.  Two apparently strong
replacements were especially informative: `OTL` has exact periods eight and
fifteen but contains `ZTL` literally on its zero slice, while `GAE` is exactly
conjugate to P100.

| handle | literal carrier and update | early signal | decision |
|---|---|---|---|
| `ZTL` | `F_q^2`, `(x,y) -> (y,(1+y)inv0(x))`, `q` odd | depth 3; periods `1,2,4,5`; complete zeta and `0/1/q` fibres | **FREEZE RECOMMENDED / OWNER-SUBTRACTED** |
| `RIC` | `F_p`, `x -> x+inv0(x)` | discriminant fibres; irregular functional graphs | **KILL DIRECT OWNER** |
| `NID` | the `0`- and `1`-balls in `Z/p^eZ`, `x -> 3x^2-2x^3` | error valuation doubles | **KILL DIRECT ALGORITHM OWNER** |
| `RDC` | divisors `d|N`, `d -> N/rad(d)` | complete product graph, but depth at most two | **KILL THEOREM-THIN** |
| `DLV` | `F_p^2`, `(x,y)->(x(1+y),y(1-x))` | invariant lines and quadratic fibres | **KILL GENERIC QUADRATIC FOLIATION** |
| `OTL` | `F_q^3`, `(x,y,z)->(y,z,(1+y+z)inv0(x))` | depth 5; periods through 15; `0/1/q` fibres | **KILL SAME ROOT AS ZTL** |
| `GAE` | `Z/p^eZ`, `x -> x+gcd(x,p^e)` | digit-sum clock and every-target fibres | **KILL EXACT CONJUGACY TO P100** |
| `QNC` | `pZ/p^eZ`, `x -> x(x+p)` for odd `p` | sharp depth `e-1`; full square-root fibre atlas | **PAPER-SIZED RESERVE / OWNER PENDING** |
| `DNT` | all subgroups of `D_{2^{m+1}}`, `H -> N_G(H)` | sharp depth `m`; binary inverse tree | **KILL RE-ENTRY / DIRECT OWNER COMPRESSION** |

## Exact audit scope

The canonical run is in `CANONICAL.txt`; the executable source is
`verify_algebraic_replacement.py`.

| handle | boxes | enumerated states | assertions |
|---|---:|---:|---:|
| `ZTL` | 17 fields | 12,089 | 83,802 |
| `RIC` | 24 primes | 1,058 | 5,362 |
| `NID` | 15 prime-power boxes | 21,094 | 147,725 |
| `RDC` | 13 exponent boxes | 311 | 1,944 |
| `DLV` | 13 primes | 8,253 | 57,824 |
| `OTL` | 12 fields | 98,496 | 573,394 |
| `GAE` | 26 prime-power boxes | 12,030 | 84,288 |
| `QNC` | 22 prime-power boxes | 13,826 | 85,634 |
| `DNT` | 8 dihedral groups | 1,056 | 8,496 |
| **total** | 150 boxes | 168,213 state-box incidences | **1,048,472** |

The field boxes include `F9`, `F25`, `F27`, and `F49` where relevant, so the
claimed `q`-uniform formulas were pressured beyond prime fields.

## 1. `ZTL`: zero-totalized Lyness dynamics

### Literal system and first anomaly

For an odd finite field `F_q`, put `inv0(0)=0` and `inv0(x)=x^{-1}` otherwise.
Define

```text
L_q(x,y) = (y,(1+y)inv0(x)).
```

The rational Lyness map has order five away from its singular divisors.  The
nontrivial signal is that the zero-totalized affine map does not degenerate
into arbitrary finite-field dynamics: its whole functional graph has one
small exceptional in-tree and otherwise only periods `1,2,4,5`.

### Proposed all-parameter theorem spine

Let

```text
r_q = #{a in F_q : a^2-a-1=0}.
U_q = {(x,y): xy(x+1)(y+1)(x+y+1) != 0}.
```

Then `|U_q|=(q-2)(q-3)`, `L_q^5=id` on `U_q`, and the recurrent axis set has
size `2q-1`.  The exact cycles are:

* `1+r_q` fixed points: `(0,0)` and the diagonal roots of `a^2-a-1`;
* two 2-cycles, `(0,1)<->(1,0)` and `(0,-1)<->(-1,0)`;
* `(q-3)/2` 4-cycles indexed by inversion pairs in
  `F_q^*\{1,-1}`;
* `((q-2)(q-3)-r_q)/5` 5-cycles on `U_q`.

All transient points feed the 2-cycle `(-1,0)<->(0,-1)`.  Besides the leaf
`(-1,-1)->(-1,0)`, for every `a notin {0,-1}` there is the chain

```text
(-1,-1-a) -> (-1-a,a) -> (a,-1) -> (-1,0).
```

Consequently the temporal polynomial is

```text
D_q(z)=q^2-3q+5 +(q-1)z +(q-2)z^2 +(q-2)z^3,
```

and the Artin--Mazur zeta function is

```text
(1-z)^(-(1+r_q))
(1-z^2)^(-2)
(1-z^4)^(-(q-3)/2)
(1-z^5)^(-((q-2)(q-3)-r_q)/5).
```

For every target `(u,v)`, the fibre size is `q` at `(-1,0)`, zero when
`u=-1` and `v!=0`, and one otherwise.  Thus the image has size `q^2-q+1`
and the maximum fibre `q` is unique.

### Deductive proof engine

The proof needs no enumeration.  Expand the first five rational iterates on
`U_q`; then split the complement into the two axes and the three displayed
exceptional layers.  Direct substitution gives every arrow and disjointness
gives completeness.  The inverse theorem is the single equation

```text
(1+x)inv0(t)=y
```

after the first target coordinate fixes the source's second coordinate.
Cycle division then gives the zeta exponents.

### Collision and owner risk

The Lyness period-five identity and cluster `A_2` interpretation are classical
and receive zero credit.  The bounded primary-source search found finite-field
Lyness and integrable birational-map work, but no source owning the conjunction
of this exact `inv0` convention with the complete affine functional graph,
exceptional tree, zeta, and every-target fibres.  A bounded miss is not novelty
clearance.  Internally, P103's double adjugate is the nearest singular algebraic
map, but its matrix carrier, two-step retraction, and determinantal proof are
different.  `OTL` is killed precisely to prevent a second Lyness-root paper.

## 2. `QNC`: quadratic collapse on a prime-power nilradical

### Literal system and independent signals

For an odd prime `p` and `e>=2`, let

```text
X_{p,e}=p Z / p^e Z,
Q_{p,e}(x)=x(x+p) mod p^e.
```

This has two independent quantitative axes.  Its forward clock is controlled
by a one-time exceptional valuation at the outer shell; its inverse graph is
controlled by singular square roots modulo `p^{e-2}`.

### Temporal theorem

Zero is the unique recurrent point and the sharp maximum absorption time is
`e-1`.  For `e=2`,

```text
D_{p,2}(z)=1+(p-1)z.
```

For `e>=3`,

```text
D_{p,e}(z)=1+(2p-1)z
 +2(p-1) sum_{t=2}^{e-2} p^{t-1} z^t
 +(p-2)p^{e-2} z^{e-1}.
```

Indeed, if `v_p(x)=a>=2`, then `v_p(Q(x))=min(e,a+1)`.  If `x=pu` with
`u` a unit, then

```text
v_p(Q(x))=min(e,2+v_p(u+1)),
```

after which the valuation rises by one per step.  This also supplies explicit
sharp witnesses and all depth layers.

### Every-target inverse atlas

Targets not divisible by `p^2` have empty fibres.  Write `y=p^2w` and
`k=e-2`.  Completing the square gives

```text
u(u+1)=w mod p^k
iff (2u+1)^2 = Delta:=1+4w mod p^k.
```

Every solution modulo `p^k` has `p` source lifts.  If
`s=v_p(Delta)<k`, the number `R_k(Delta)` of square roots is zero for odd
`s`; for `s=2r` it is `2p^r` exactly when the unit part is a quadratic
residue modulo `p`, and zero otherwise.  For `Delta=0 mod p^k`, it is
`p^{floor(k/2)}`.  Hence

```text
|Q^{-1}(y)| = p R_k(1+4w).
```

The image size is the number of squares modulo `p^k`:

```text
1 +(p-1)/2 sum_{r=0}^{floor((k-1)/2)} p^{k-2r-1}.
```

The maximum fibre is `p^{k/2+1}` when `k` is even, and
`2p^{(k-1)/2+1}` when `k` is odd.  The even case has the unique discriminant
zero target; the odd case has `(p-1)/2` maximizers.

### Collision and owner risk

This is not P100: the map is polynomial on the nilradical, its depth is linear
in precision rather than a digit sum, and its inverse axis is a singular
quadratic-congruence atlas.  It is not P142: the carrier has `p^{e-1}` ring
elements rather than `e+1` divisors, and the discriminant fibres have no
valuation-tent analogue.  Nevertheless, general polynomial dynamics on
`Z_p`, reductions modulo `p^e`, and quadratic functional graphs are mature.
No exact-map owner appeared in the bounded search, but that establishes only a
paper-sized reserve, not external novelty.

## 3. Strong-looking systems killed by exact reduction

### `OTL`: third-order totalized Lyness map

On `F_q^3`, set

```text
T(x,y,z)=(y,z,(1+y+z)inv0(x)).
```

Exact computation exposed depth five, recurrent periods among
`1,2,3,4,6,8,15`, `(q-1)(q-2)(q-3)/8` exact 8-cycles, recurrent size
`q^3-3q^2+2q+5`, image size `q^3-q(q-1)`, and `0/1/q` fibres.  Its depth
layers are

```text
q^3-3q^2+2q+5, 2q-2, 2q-3,
(q-2)(q+1), q(q-2), (q-2)(q-1).
```

It is nevertheless a same-root kill.  On the invariant zero slice,

```text
T^3(a,b,0)=(L^2(a,b),0),
```

where `L` is exactly `ZTL`.  The period-15 anomaly is the period-five Lyness
boundary seen every third step.  Freezing both would split one mechanism into
two papers.

### `GAE`: gcd addition

On standard representatives modulo `p^e`, define `A(0)=0` and

```text
A(x)=x+gcd(x,p^e) mod p^e.
```

It has digit-sum absorption, image size `p^e-p^{e-1}`, unique maximum fibre
`e+1`, and a clean every-target fibre rule.  But `C(x)=-x mod p^e` gives

```text
C A C^{-1}(y)=y-p^{v_p(y)},
```

exactly P100's least-valuation digit erasure.  Every theorem transfers, so this
is a permanent internal-conjugacy kill.

## 4. Other new negative controls

### `RIC`

For `x -> x+inv0(x)` over `F_p`, a target `y` has the roots of
`x^2-yx+1=0`, plus the totalized zero preimage when appropriate.  This gives a
complete discriminant fibre atlas, but Ugolini and Park--Gao directly study
functional graphs of the same `x+x^{-1}` family.  The changed value at the
projective boundary is not paper-sized residual progress.

### `NID`

On the two residue balls `x=0,1 mod p`, the map `3x^2-2x^3` doubles the
valuation of `x(1-x)`, giving sharp depth `ceil(log_2 e)`.  That is exactly the
standard Newton iteration for lifting idempotents.  Both map and main theorem
are algorithmically owned.

### `RDC`

For `N=prod p_i^{e_i}`, exponent coordinates turn `d->N/rad(d)` into

```text
a_i -> e_i       if a_i=0,
a_i -> e_i-1     if a_i>0.
```

The recurrent product, image Boolean corner, and every-target fibres are
exact, but the clock is at most two and the proof is definition-level.  There
is no owner-subtracted paper spine.

### `DLV`

The map `(x,y)->(x(1+y),y(1-x))` preserves `s=x+y`; on each line it is
`x->x(1+s-x)`.  Image size `p(p+1)/2` and discriminant fibres are exact, but a
uniform functional-graph theorem would amount to solving the generic
one-parameter quadratic family.  The early profiles vary rather than expose a
map-specific clock.

## 5. `DNT` re-entry audit

Let `G_m` be the dihedral group of order `2^{m+1}` and iterate
`H->N_{G_m}(H)` on all subgroups.  Write `R_k=<r^{2^k}>` and
`H_{k,j}=<r^{2^k},r^j s>`.  Direct conjugation gives

```text
R_k -> G_m,
H_{0,0} -> G_m,
H_{k,j} -> H_{k-1,j mod 2^{k-1}}  (k>=1).
```

Thus the full group is the unique fixed point, the sharp depth is `m`, the
temporal polynomial is

```text
1 +(m+3)z + sum_{k=2}^m 2^k z^k,
```

the image has `2^m-1` states, the full group has fibre `m+4`, and every
internal dihedral target has fibre two.  The theorem is complete but has poor
re-entry value: the literal question is a normalizer tower, Cavior owns the
dihedral subgroup classification, and the remaining calculation is immediate
conjugation.  Earlier portfolio scouts already recorded the same owner
compression.  `DNT` is permanently killed, not reserved.

## 6. Final ranking and gate

1. **`ZTL`: freeze recommended.**  Two independent axes survive classical
   Lyness subtraction, and no direct all-affine graph owner was found.
2. **`QNC`: paper-sized reserve.**  It is genuinely independent and has two
   quantitative axes, but needs a specialist local-ring owner audit before a
   contract.
3. **All others: kill.**  `OTL` and `GAE` are exact internal reductions;
   `RIC`, `NID`, and `DNT` have direct-owner compression; `RDC` is thin; `DLV`
   has no uniform theorem spine.

Nothing here authorizes public release, submission, specialist contact, or an
authorship claim.  The lane remains `HOLD_EXTERNAL`.
