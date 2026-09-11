# LZK theorem contract: least-zero Kempe dynamics on `K_{r,s}`

**Stage:** replacement breadth / theorem spike.  **Disposition:**
`PROVISIONAL_AMBER / HOLD_EXTERNAL`.  This document makes no novelty,
priority, or paper-allocation claim.  Kempe changes, chromatic polynomials,
surjection counts, and generic least-label scheduling receive zero
contribution credit.

## 1. Frozen literal system

Fix integers `r,s>=1` and a labelled complete bipartite graph

```text
L={0,...,r-1},       R={r,...,r+s-1}.
```

For `q>=3`, the phase space `X_{r,s,q}` is the set of proper colourings
`x:L union R -> {0,1,...,q-1}`.  The labels, the ordered colour pair `(0,1)`,
and the following scheduler are part of the definition.

- If colour `0` is absent, set `F(x)=x`.
- Otherwise let `v` be the least-labelled vertex of colour `0`.  In the
  subgraph induced by vertices of colours `0` and `1`, take the connected
  component containing `v` and interchange `0` and `1` simultaneously on
  that whole component.  All other colours hold.

This is a deterministic self-map.  It is neither the random choice of a
vertex/colour pair nor a sweep: exactly one component selected from the old
colouring is switched at each epoch.

The `q=2` case is not folded into the sharp-tail claim.  It is stated
separately in Section 7.

## 2. Support-side lemma and closed update

In a proper colouring of `K_{r,s}`, every used colour occurs on exactly one
side.  Write `Z_a=x^{-1}(a)`.  The literal BFS definition above has precisely
three cases.

1. If `Z_0` is empty, the state holds.
2. If `Z_0` and `Z_1` are nonempty and lie on opposite sides, the selected
   Kempe component is `Z_0 union Z_1`; hence `F` swaps all zeroes and ones.
3. If colour `1` is absent or lies on the same side as colour `0`, the
   selected component is the singleton containing `min Z_0`; hence that one
   zero becomes a one.

The reason is structural, not an additional rule.  Opposite nonempty support
sets induce the complete bipartite graph `K_{|Z_0|,|Z_1|}`.  Same-side
support sets induce no edges.

## 3. Complete functional graph and sharp clock

The recurrent states are exactly:

- the fixed colourings with no zero; and
- the strict two-cycle states in which zero and one are both used on
  opposite sides.

Every other state is transient.  For a transient state,

```text
tau(x)=|Z_0|.
```

Indeed, the same-side branch changes the least remaining zero into a one at
each step and cannot enter the opposite-side branch.  Therefore

```text
max_x tau(x)=max(r,s).
```

For `q>=3` this is sharp: colour every vertex of a largest side by `0` and
every vertex of the other side by `2`.  No orbit has a longer tail because a
proper colouring places all zeroes on one side.

This proves the full period support `{1,2}` and rules out any Garden tree
feeding a two-cycle.

## 4. Exact recurrent and depth census

Let

```text
Onto(n,k)=sum_{j=0}^k (-1)^j binom(k,j)(k-j)^n,
```

with `Onto(0,0)=1`.  The total phase-space size is the usual chromatic
specialisation

```text
|X_{r,s,q}| = chi_{K_{r,s}}(q)
            = sum_{k=1}^{min(r,q)} binom(q,k) Onto(r,k)(q-k)^s.
```

The number of fixed states is

```text
Fix_{r,s,q}=chi_{K_{r,s}}(q-1).
```

For `a+b<=q-2`, put

```text
M_q(a,b)=(q-2)!/(a! b! (q-2-a-b)!).
```

The number of **points** on strict two-cycles is

```text
CycPt_{r,s,q}
 = 2 sum_{a,b>=0, a+b<=q-2}
       M_q(a,b) Onto(r,a+1) Onto(s,b+1).                 (1)
```

There is no hidden unordered division in (1).  The factor `2` records the
two disjoint orientations `0 on L,1 on R` and `1 on L,0 on R`.  Consequently
the number of two-cycles is exactly half of (1), namely the same sum without
the leading `2`.

There is also an all-depth formula.  For `u,v>=1` and `d>=1`, define

```text
A_{u,v,q}(d)
 = binom(u,d) sum_{a,b>=0, a+b<=q-2} M_q(a,b)
     [Onto(u-d,a)+Onto(u-d,a+1)] Onto(v,b).              (2)
```

The number of states of exact positive depth `d` is

```text
A_{r,s,q}(d)+A_{s,r,q}(d).                               (3)
```

For (2), choose the `d` zeroes on the designated side, choose disjoint exact
supports of sizes `a,b` from colours `2,...,q-1`, and separate the cases in
which colour `1` is absent or used on the zero side.  The opposite side may
not use colour `1`; otherwise the state is already recurrent.

## 5. Every-time, every-target fibres

Fix a target `y` and `t>=0`.

### 5.1 Opposite-side recurrent target

If zero and one are nonempty and on opposite sides, then

```text
|F^{-t}(y)|=1.
```

The unique source is `y` when `t` is even and the zero/one swap of `y` when
`t` is odd.  No transient state can feed this component.

### 5.2 Transient target

Suppose `Z_0(y)` is nonempty and zero and one are not on opposite sides.  Let
`z=min Z_0(y)` and let

```text
a(y)=#{v : v is on the side of z, v<z, and y(v)=1}.
```

Then

```text
|F^{-t}(y)|=binom(a(y),t),                                (4)
```

interpreted as zero when `t>a(y)`.  A source is obtained by choosing exactly
`t` of those earlier one-vertices and recolouring them zero.  The scheduler
removes precisely those chosen zeroes in increasing label order before it
can touch an old zero of `y`.  This construction is reversible and proves
both directions of (4).

### 5.3 Fixed target

If zero is absent, let `m_1(y)=|Z_1(y)|`.  Then

```text
|F^{-t}(y)|=sum_{j=0}^{min(t,m_1(y))} binom(m_1(y),j).     (5)
```

Here `j` one-vertices are recoloured zero in the source; they are exhausted
after `j` steps and the orbit holds for the remaining `t-j` epochs.  The
`j=0` term is the self-source and is mandatory.  Formulas (4)--(5) also give
`|F^0{}^{-1}(y)|=1` at `t=0`.

For one step, (4)--(5) give the image criterion and the sharp uniform bound

```text
max_y |F^{-1}(y)|=max(r,s)+1.                             (6)
```

It is attained by any zero-free target whose whole largest side has colour
`1`.  The other side may be coloured arbitrarily from
`{2,...,q-1}`.  Thus there are `(q-2)^s` maximisers when `r>s`,
`(q-2)^r` when `s>r`, and `2(q-2)^r` when `r=s`.

## 6. Claim ceiling and residual

The admissible internal residual is the conjunction of:

1. the frozen least-zero Kempe scheduler on the full labelled colouring
   carrier;
2. the support-side dichotomy producing a strict two-cycle core and a sharp
   `#zero` transient clock;
3. the all-depth support/onto census (2)--(3); and
4. the target-resolved all-time binomial atlas (4)--(6).

The following are explicitly zero credit: the fact that a Kempe interchange
preserves properness; Kempe equivalence or mixing results; the chromatic
polynomial of `K_{r,s}`; inclusion--exclusion for onto maps; and generic
functional-graph/zeta bookkeeping.  `OWNER_AMBER` is binding until a direct
external search clears or kills the exact deterministic map.

## 7. Boundary cases

- `q=2`, `r,s>=1`: there are exactly two proper colourings.  Zero and one
  occupy opposite sides, and the two states form one strict two-cycle.  The
  maximum tail is `0`, every `t`-target fibre has size `1`, and there are no
  fixed states.  This is why the sharp statement in Section 3 assumes
  `q>=3`.
- `r=0` or `s=0` is outside the frozen carrier.  On an edgeless graph the
  same syntax would merely change the least zero to one and would erase the
  support-side/two-cycle mechanism.
- At `t=0`, every target has its unique self-source, including transient and
  zero-free targets.

## 8. Exact verification obligations

`verify_replacement_lane.py` independently checks the literal BFS against
the closed three-case update, closure, pointwise depth and periods, (1)--(5),
the sharp tail and one-step fibre, and the `q=2` boundary.  The canonical
boxes include `(q,r,s)=(3,3,4),(4,3,4),(5,3,4)` and smaller asymmetric cases.

