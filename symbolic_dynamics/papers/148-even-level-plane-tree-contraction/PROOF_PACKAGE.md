# Proof package — P148

## Claim

Let `PT_{<=N}` be the finite disjoint union of plane rooted trees with at most
`N` vertices.  Define `E` by deleting all odd-depth vertices and promoting
their ordered child blocks to their parents, then resetting depth at the
retained root.

For every plane rooted tree `T`, target `U`, and exact source size `n`:

1. `E^k(T)` consists exactly of the original vertices at depths divisible by
   `2^k`, with nearest retained ancestry and induced contour order.
2. `h(E(T))=floor(h(T)/2)`,
   `tau(T)=ceil(log2(h(T)+1))`, and the maximum on `PT_n` is
   `ceil(log2 n)`, witnessed by the path.
3. If `m=|U|` and `I(U)` is the number of internal vertices, then

   $$
   \sum_{E(T)=U}y^{|T|-m}=\frac{y^{I(U)}}{(1-y)^{2m-1}}.
   $$

   Therefore the exact-size fibre is

   $$
   \binom{n-m-I(U)+2m-2}{2m-2}
   $$

   when `n-m>=I(U)`, and is empty otherwise.
4. The exact-size image condition is `m+I(U)<=n`.  If

   $$H(z)=\sum_U z^{|U|+I(U)},$$

   then

   $$H=z+\frac{z^2H}{1-H},$$

   and the exact-layer image counts have ordinary generating function
   `H(z)/(1-z)`.

## Status

**PROVABLE AS STATED.**  The frozen claims survive unchanged.

## Assumptions

- Trees are finite, rooted, and plane; each child list is linearly ordered.
- Height is maximum root depth, with the singleton having height zero.
- `tau(T)` is the least nonnegative `k` for which `E^k(T)` is the singleton.
- The displayed fibre series ranges coefficientwise over all finite exact
  source layers.  On the literal finite carrier `PT_{<=N}`, it is truncated
  after source size `N`.

## Notation

- `PT_n`: exact `n`-vertex source layer.
- `PT_{<=N}`: finite carrier on which `E` is a self-map.
- `d_U(v)`: outdegree of target vertex `v`.
- `I(U)`: number of target vertices with positive outdegree.
- An inserted vertex means a deleted odd-depth vertex in a one-step
  predecessor.

## Proof strategy

Use original vertex identities for the temporal theorem.  Use a recursive,
vertex-local bijection for the inverse: productive odd children partition an
ordered target child list into consecutive nonempty blocks, while odd leaves
fill arbitrary gaps.  Finally weight each target root by its contribution to
`|U|+I(U)` to derive the algebraic image series.

## Dependency map

1. The iterate theorem depends only on the one-step parity rule and induction.
2. The clock depends on the iterate theorem and the fact that a deepest path
   meets every depth from zero through `h(T)`.
3. The fibre theorem depends on the local block-and-gap bijection and the
   plane-tree outdegree identity `sum_v d_U(v)=m-1`.
4. The image criterion is coefficient nonvanishing in the fibre theorem.
5. The algebraic series depends on weighting a leaf by `z` and an internal
   root by `z^2` with a nonempty ordered child sequence.

## Proof

### Step 1: carrier closure and strict descent

The rule removes vertices and adds no new vertex.  Promoting a child block
changes only edges and order, so `|E(T)|<=|T|`; hence `E` maps
`PT_{<=N}` to itself.  If `T` is not the singleton, its root has at least one
depth-one child, and every such child is deleted.  Thus `|E(T)|<|T|`.
Consequently the singleton is the unique fixed point and the unique recurrent
state.

### Step 2: exact iterate skeleton

We prove by induction on `k` that the vertices of `E^k(T)` are precisely the
original vertices whose depths are divisible by `2^k`.  Their new depth is
the original depth divided by `2^k`.

At `k=0` the statement is the identity.  Assume it at rank `k`.  The next
application retains a current vertex exactly when its current depth is even.
An original surviving vertex at depth `d` has current depth `d/2^k`, so it
survives once more exactly when `d` is divisible by `2^(k+1)`.  Its new depth
is `d/2^(k+1)`.

At one contraction, every retained vertex is joined to its nearest retained
ancestor: the intervening vertex is the deleted parent.  Repeating this fact
shows that the edge at rank `k+1` also joins nearest surviving original
ancestors.  Concatenation of ordered child blocks is associative, so the
left-to-right order equals the order induced by the original contour.  This
completes the induction.

### Step 3: height and absorption time

A root-to-deepest-vertex path contains a vertex at every original depth
`0,1,...,h(T)`.  By Step 2, the greatest surviving current depth after `k`
steps is therefore `floor(h(T)/2^k)`.  In particular,

$$h(E(T))=\left\lfloor\frac{h(T)}2\right\rfloor.$$

The rank-`k` tree is the singleton exactly when no positive multiple of
`2^k` is at most `h(T)`, equivalently when `2^k>h(T)`.  The least such `k` is

$$\tau(T)=\left\lceil\log_2(h(T)+1)\right\rceil,$$

including `h(T)=0`.  An `n`-vertex tree has height at most `n-1`, so its clock
is at most `ceil(log2 n)`.  The `n`-vertex path has height `n-1` and attains
this bound for every `n`.

### Step 4: local predecessor bijection

Fix a target vertex `v` of outdegree `d`, with ordered target child subtrees
`U_1,...,U_d`.  Build the corresponding predecessor subtree from the bottom
up.  Each child of `v` in the predecessor lies at odd depth relative to `v`.
It is either:

- an empty odd child, meaning an odd leaf, or
- a productive odd child whose children are the roots of predecessor
  subtrees mapping to a nonempty consecutive block of
  `U_1,...,U_d`.

If `d=0`, every odd child must be empty.  An arbitrary number of them gives
the local inserted-vertex series

$$A_0(y)=\frac1{1-y}.$$

Suppose `d>0` and exactly `r` odd children are productive.  There are
`binom(d-1,r-1)` ways to split the ordered target child list into `r`
nonempty consecutive blocks.  Empty odd leaves may occur in each of the
`r+1` gaps before, between, and after the productive children.  Weighting
every odd child by `y` gives

$$
A_d(y)=\sum_{r=1}^d
 \binom{d-1}{r-1}\frac{y^r}{(1-y)^{r+1}}.
$$

Factoring out `y/(1-y)^2` and applying the binomial theorem yields

$$
A_d(y)=\frac{y}{(1-y)^2}
 \left(1+\frac{y}{1-y}\right)^{d-1}
 =\frac{y}{(1-y)^{d+1}}.
$$

The construction is reversible: a predecessor child list uniquely identifies
its empty children, productive children, and the consecutive target blocks
they carry.  Choices below distinct target vertices involve disjoint inserted
vertices and are independent.

### Step 5: global fibre series and coefficient extraction

Multiply the local factors over all target vertices.  Each of the `I(U)`
internal vertices contributes one factor `y` and each leaf contributes none.
The denominator exponent is

$$
\sum_{v\in U}(d_U(v)+1)=(m-1)+m=2m-1.
$$

Thus

$$
\sum_{E(T)=U}y^{|T|-m}=\frac{y^{I(U)}}{(1-y)^{2m-1}}.
$$

For an exact source size `n`, put `q=n-m`.  If `q<I(U)`, the coefficient is
zero.  Otherwise the negative-binomial expansion gives

$$
[y^q]\frac{y^{I(U)}}{(1-y)^{2m-1}}
=\binom{q-I(U)+2m-2}{2m-2}.
$$

This also handles the singleton target: `m=1`, `I(U)=0`, and every exact
source fibre contains the unique star of that size.

### Step 6: exact-size images

The coefficient in Step 5 is nonzero exactly when `n-m>=I(U)`.  Therefore

$$U\in E(PT_n)\quad\Longleftrightarrow\quad |U|+I(U)\le n.$$

This statement refers to the source layer `PT_n`; it does not assert that
`E` preserves that layer.

### Step 7: algebraic image generating function

Give a target tree `U` weight `z^(|U|+I(U))`.  A leaf root contributes `z`.
An internal root contributes one factor `z` for the vertex and another for
being internal, followed by a nonempty ordered sequence of independently
weighted child trees.  Hence

$$
H(z)=z+z^2\sum_{d\ge1}H(z)^d
=z+\frac{z^2H(z)}{1-H(z)}.
$$

Equivalently, `H` is the unique formal-power-series root with zero constant
term of

$$H^2-(1+z-z^2)H+z=0.$$

By Step 6, the image from `PT_n` consists exactly of targets of weight at
most `n`.  Therefore its count is the coefficient of `z^n` in

$$\frac{H(z)}{1-z}.$$

All frozen claims follow.

## Corrections or missing assumptions

None.  The finite-carrier/truncated-series convention must remain explicit in
the manuscript.

## Open risks

- Generic contraction literature is broad; the source audit is bounded and
  provides no novelty or priority certificate.
- The theorem is specific to plane order and simultaneous deletion of every
  odd generation.  It is not stated for unordered trees or arbitrary selected
  levels.

