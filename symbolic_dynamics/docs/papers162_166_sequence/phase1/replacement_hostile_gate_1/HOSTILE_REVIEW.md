# P162--P166 replacement hostile gate 1

**Reviewed objects:** the BQC tree-fibre upgrade and RTI random translation
intersection contract  
**Review posture:** fresh derivation; neither author verifier was imported  
**Lifecycle:** `HOLD_EXTERNAL`  
**Decision:** `BQC = AMBER_LOW (DO NOT SELECT)`; `RTI = GREEN_AFTER_ONE_REQUIRED_MINOR_REPAIR`

## 1. Executive decision

| candidate | mathematical audit | owner/value audit | hostile decision |
|---|---|---|---|
| `BQC` | the semigroup, sharp clock, weighted graph fibres, tree-fibre inversion, and reduced Matrix--Tree formula survive; the stated recovery of `(n,c)` is false unless `c<=n` is imposed | the extra tree axis is logically independent of the edge-bin polynomial, but after subtraction it is ordinary required-edge inclusion--exclusion over a directly owned blow-up spanning-tree determinant; a very recent partition-localized tree paper makes the neighbourhood still tighter | **`AMBER_LOW / DO_NOT_SELECT`**; the upgrade is not enough for green at the present threshold |
| `RTI` | the history-span identity, exact rank clock, sharp witness, and every-target weighted fibre atlas survive; equation (7) is not a valid displayed formula for odd-cardinality targets | erosion composition and random rank receive zero credit, but the stabilizer-indexed joint history/source polynomial is target-sensitive information not contained in either classical input; no direct conjunction owner was found in the bounded search | **`GREEN_AFTER_REQUIRED_MINOR_REPAIR`**; eligible once equation (7) is made piecewise |

Severity counts are separate from value/ownership decisions:

```text
BQC: 0 Critical / 1 Major / 0 minor
RTI: 0 Critical / 0 Major / 1 minor
```

No paper, author source, central ledger, or Git state was changed.

## 2. Independent BQC derivation

Number vertices from `0` to `n-1` and let

```text
q_c(i)=floor(i/c).
```

The loopless graph quotient sends an edge `uv` to `q_c(u)q_c(v)` when the
two images differ and ORs coincident edges.  Since

```text
q_c^t(i)=floor(i/c^t),
```

the literal `t`-fold map is the one-step quotient into consecutive blocks of
width `c^t`.  Write their actual sizes as `s=(s_1,...,s_m)`, including the
short final block.

### 2.1 Clock and ordinary fibres

An edge `uv` dies exactly at

```text
tau_c(u,v)=min{t>=0: floor(u/c^t)=floor(v/c^t)}.
```

Thus every graph is empty by `ceil(log_c n)`, and the single edge
`{0,n-1}` survives to the preceding time whenever `n>1`.  The height is
therefore sharp.

For a supported target graph `H` on the `m` block vertices, the source-edge
weight polynomial is

```text
(1+z)^(sum_i binom(s_i,2))
  product_(ij in E(H)) ((1+z)^(s_i s_j)-1).                 (B1)
```

Every target nonedge forces its cross-bin to be empty.  Formula (B1) proves
the whole image and every-target fibre atlas because all source-edge bins
are disjoint.  Unsupported targets have empty fibre.

### 2.2 Tree-restricted fibres

For `F` on the block vertices, let `K(F;s)` be the graph with a clique on
each block and a complete join between blocks exactly along `E(F)`.  A
labelled source tree has quotient exactly `H` precisely when it is a
spanning tree of `K(H;s)` and uses at least one edge in every cross-bin of
`H`.  Boolean inversion gives

```text
TreeFib_s(H)
  = sum_(F subseteq H) (-1)^(|E(H)|-|E(F)|) tau(K(F;s)).    (B2)
```

Put `D_i=sum_(ij in E(F)) s_j`, `alpha_i=s_i+D_i`, and

```text
Q_ii=D_i,
Q_ij=-s_j  if ij in E(F),
Q_ij=0     otherwise.
```

For any deleted index `r`, the full Laplacian decomposes into the
block-constant subspace and, for each block `i`, its `(s_i-1)`-dimensional
zero-sum subspace.  The latter has eigenvalue `alpha_i`.  Matrix--Tree then
gives

```text
tau(K(F;s))
  = det(Q^(r))/s_r * product_i alpha_i^(s_i-1).             (B3)
```

The verifier compares (B3), for every root, with an independently built full
`n`-vertex Laplacian cofactor before using (B2).  Disconnected `F`, one
block, singleton blocks, short last blocks, paths, cycles, and zero targets
are included.

The tree restriction is genuinely not a specialization of (B1):
connectivity and acyclicity couple distinct edge bins.  This establishes
logical independence.  It does **not**, however, establish sufficient
post-subtraction value: (B2) is the standard required-edge use of
inclusion--exclusion and (B3) lies in the directly occupied blow-up-tree
territory documented in `OWNER_AUDIT.md`.

### 2.3 Major finding BQC-M1: parameter recovery is false on the stated carrier

The proposed probe is

```text
I(n,c)=sum_i binom(s_i,2),
```

the base-two logarithm of the time-one empty fibre.  It is strictly
increasing for `1<=c<=n`.  One clean proof is that the decreasing block-size
vector for width `c+1` strictly majorizes that for width `c` when `c<n`, and
`x -> binom(x,2)` is strictly convex on the relevant integer transfers.

But for every `c>=n` the partition is the single block `(n)`.  Hence

```text
Q_n = Q_(n+1) = Q_(n+2) = ...,
I(n,n)=I(n,n+1)=...=binom(n,2).
```

The entire dynamics, not merely the proposed statistic, is identical for
all those parameters.  Phase size plus the time-one empty fibre therefore
cannot identify `(n,c)` on an unrestricted `c>=2` carrier.

Required repair, either:

1. state the parameter family as `2<=c<=n`; or
2. replace recovery of `c` by recovery of the normalized parameter
   `min(c,n)` and explicitly state the unavoidable equivalence.

This is Major because a theorem axis is false as stated, though it does not
damage (B1)--(B3).

### 2.4 BQC disposition

The upgrade is correct after BQC-M1 is repaired, but **tree-fibre inversion
is not enough to turn BQC green**.  The dynamic core remains a deterministic
quotient/direct image, the blow-up spanning-tree determinant has a direct
owner, and the residual required-bin inversion is a standard wrapper.  The
recent partition-localized spanning-tree generating-function result is not
the same fibre problem, but it narrows the defensible gap.  BQC remains
`AMBER_LOW`, meaning mathematically usable but below the batch's paper
selection threshold.

## 3. Independent RTI derivation

Let `V=F_2^d`.  For a sampled `v in V`, the literal update is

```text
A -> A intersect (A+v).
```

For history `v_1,...,v_t`, repeated distribution of intersection over
translation gives an intersection over all subset sums of the sampled
vectors.  In characteristic two those subset sums are their span `H_t`, so

```text
A_t=E_(H_t)(A_0):=intersection_(h in H_t)(A_0+h).           (R1)
```

### 3.1 Temporal law and sharpness

For a fixed `r`-subspace `H`, length-`t` histories spanning `H` are
surjective linear maps `F_2^t -> H`, hence number

```text
S(t,r)=product_(i=0)^(r-1)(2^t-2^i).                        (R2)
```

Summing over the Gaussian-binomial number of `r`-subspaces gives the rank
law.  Full span has probability

```text
0                                                   (t<d),
product_(i=0)^(d-1)(1-2^(i-t))                      (t>=d). (R3)
```

The only states fixed by every possible update are `empty` and `V`.  Once
`H_t=V`, every non-full source erodes to empty.  For the witness
`A=V\{0}` one has the stronger pointwise identity

```text
E_H(V\{0})=V\H,                                            (R4)
```

so absorption occurs iff `H=V`; (R3) is therefore the sharp worst-state
clock.  Growing a rank-`r` span succeeds with probability `1-2^(r-d)`, so

```text
E T=sum_(r=0)^(d-1) 1/(1-2^(r-d)).                          (R5)
```

### 3.2 Every-target weighted inverse atlas

For a target `B`, put `b=|B|` and

```text
Stab(B)={v:B+v=B},  s=dim Stab(B).
```

For fixed `H`, equality `E_H(A)=B` is possible only if
`H<=Stab(B)`.  Then `B` is a union of full `H`-cosets.  The source must
contain all of `B`; in each other `H`-coset it may choose any proper subset,
independently.  Thus its source-size polynomial is

```text
z^b (((1+z)^(2^r)-z^(2^r)))^(2^(d-r)-b/2^r).
```

There are `[s choose r]_2` choices of `H` and `S(t,r)` histories spanning
each one.  Consequently

```text
F_t(B;z)=z^b sum_(r=0)^s [s choose r]_2 S(t,r)
  ((1+z)^(2^r)-z^(2^r))^(2^(d-r)-b/2^r).                  (R6)
```

This also handles `t=0`, `B=empty`, `B=V`, and `d=0` under empty-product
conventions.

The polynomial is a logically independent axis.  Random-rank theory gives
only the distribution of `H_t`; generic morphology gives the forward
operator (R1).  Neither supplies the target restriction
`H<=Stab(B)`, the proper-subset choice on outside cosets, or the joint
source-cardinality/history enumeration in (R6).  Two same-size targets can
have different one-step fibres because their stabilizer dimensions differ.

### 3.3 Minor finding RTI-m1: equation (7) needs a boundary branch

At one step, only ranks zero and one can occur.  If `s>=1`, then `B` is a
union of two-point orbits and `b` is even, yielding

```text
F_1(B;1)=1+(2^s-1) 3^(2^(d-1)-b/2).
```

For odd `b`, necessarily `s=0`; the displayed exponent is then a
half-integer even though the prefactor `2^s-1` vanishes.  Formal polynomial
statements cannot use “zero times an undefined/nonintegral power” as a
boundary convention.  The valid statement is

```text
F_1(B;1) = 1,                                      if s=0;
           1+(2^s-1)3^(2^(d-1)-b/2),              if s>=1. (R7)
```

Equivalently, restrict the second line to targets with nontrivial
stabilizer.  The recovery claim remains true: at fixed `(d,b)`, (R7) is
strictly increasing over the feasible stabilizer dimensions.

This is minor because (R6) is valid on every boundary and directly implies
the repaired statement.  The verifier nevertheless found 139 explicit
odd-cardinality boundary targets through `d=3` where the original display
is formally invalid.

### 3.4 RTI disposition

After RTI-m1 is incorporated, `RTI` is **GREEN**.  Its stabilizer polynomial
is genuinely beyond the standard morphology/random-rank ingredients in the
specific theorem-value sense required here: it is a complete target- and
source-weighted inverse atlas, not a rephrased rank marginal.  The bounded
search found no direct owner of that conjunction, and P158 does not transfer
it: P158 uses random cut signatures and occupancy/surjection fibres, whereas
RTI uses a linear translation span, affine cosets, and the target's
translation stabilizer.

## 4. Fresh executable falsification

`verify_hostile.py` is standalone standard-library code and imports neither
candidate verifier.  It covers:

- BQC arbitrary graph states through `n=5` for all tested `c`, plus `n=6`
  representatives; `t=0`, unequal last blocks, `c=n`, `c>n`, and
  post-absorption times;
- BQC literal iteration versus width `c^t`, every supported and selected
  unsupported target, weighted source fibres, mass, individual edge clocks,
  and sharp global witnesses;
- every labelled source tree through `n=7` from an independent Pruefer
  generator, including one-block and singleton-block boundaries;
- BQC full `n`-vertex Laplacian cofactors versus every-root reduced formula,
  disconnected bases, and inclusion--exclusion tree fibres;
- RTI `d=0,1,2,3`, `t=0` and later times, literal histories, all targets,
  all source weights, all subspaces, mass, and both absorbing states;
- fixed-span history counts, full-rank clocks, the sharp witness through
  `d=6`, target stabilizers, recovery, and odd-cardinality boundaries.

The canonical run records `1,570,623` assertions.  Computation is a
counterexample search, not a proof; the proofs above establish the
all-parameter statements.

## 5. Required actions before any freeze

1. **BQC:** normalize `c` to `2<=c<=n`, or state recovery only up to
   `min(c,n)`.  Do not promote the candidate on the strength of the tree
   upgrade alone.
2. **RTI:** replace equation (7) by (R7), or explicitly restrict that display
   to `s>=1`; retain (R6) as the universal formula.
3. Keep both objects `HOLD_EXTERNAL`.  This gate makes no novelty or priority
   claim.

