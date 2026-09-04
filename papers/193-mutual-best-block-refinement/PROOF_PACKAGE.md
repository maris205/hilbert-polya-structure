# Proof package — P193 mutual-best block refinement

## Claim

For the simultaneous mutual-nomination map on `S_n`:

1. active pairs are exactly the first/minimum pairs in nontrivial direct-sum
   indecomposable components;
2. direct-sum component count strictly increases off the identity;
3. the recursive selection-decomposition height is the exact pointwise tail;
4. maximum tail is `n-1`, attained by exactly `(n-1)!` states;
5. cumulative depth OGFs satisfy
   `A_t=(1-B_t)^(-1)`, `B_0=x`, and
   `B_(t+1)=x+x^2 A_t B_t'`;
6. a target with component sizes `(c_1,...,c_s)` has fibre zero for `c_1>1`
   and otherwise
   `c_s product_(j>=2,c_j=1) (1+c_(j-1))`;
7. the image has `(n-1)!` states and the identity uniquely maximizes the
   fibre at `2^(n-1)`.

## Status

`PROVABLE AS STATED`

The proof is all-parameter and includes `n=1`.  Enumeration is not used in
any implication.

## Assumptions

- Permutations are in one-line notation on the totally ordered alphabet
  `[n]`.
- Every nomination is computed from the state at the start of the epoch.
- Every mutually nominating pair is exchanged simultaneously.
- A direct-sum cut after `r` means the first `r` values are exactly `[r]`.
- Generating functions are ordinary formal power series; no analytic
  convergence is asserted.

## Notation

- `F_n`: literal simultaneous map.
- `comp(pi)`: number of direct-sum indecomposable components.
- `std(w)`: standardization of a distinct-letter word.
- `h(pi)`: recursively defined selection-decomposition height.
- `tau(pi)`: first time the orbit reaches the identity.
- `A_t`, `B_t`: cumulative depth OGFs for all and indecomposable
  permutations.
- `c_1,...,c_s`: ordered target component sizes.

## Proof strategy

The forward dynamics is reduced exactly, not quotient-wise, to component
surgery.  Size induction then proves the temporal statements.  Reversal of
one component surgery is controlled by the last direct-sum component of the
suffix; this same lemma supplies both the deepest recurrence and the
target-fibre factorization.

## Dependency map

1. The block-surgery lemma depends only on the two nomination extrema and the
   definition of a direct-sum cut.
2. Strict component refinement and sum compatibility depend on block surgery.
3. Exact pointwise height depends on sum compatibility and the decomposition
   `F(beta)=1 direct-sum gamma`.
4. Maximum tail uses size induction; deepest count additionally uses the
   indecomposable-parent lemma.
5. The layer recurrence uses unique direct-sum factorization, exact height,
   and the marked-last-component interpretation of the parent lemma.
6. The every-target fibre uses the parent lemma independently in consecutive
   target groups.
7. The unique fibre maximum uses only the exact product and elementary
   integer inequalities.

## Proof

### Step 1. Exact active-pair classification

No inversion crosses a direct-sum cut because all values in an earlier block
are smaller than all values in a later block.  Work in a standardized
indecomposable block `beta`.

If its size exceeds one, its minimum `1` cannot be first: otherwise position
one would be a sum cut.  The first entry nominates `1`, since `1` is its
smallest later smaller value.  The minimum nominates the first position,
since every preceding value is larger.  Thus first/minimum is active.

Suppose `(i,j)` is any active pair and `b=beta_j`.  Since `i` is the earliest
earlier value larger than `b`, every position before `i` contains a value
smaller than `b`.  Since `b` is the smallest later value below `beta_i`, no
value smaller than `b` occurs after `i`.  The `b-1` smaller values therefore
occupy exactly the `i-1` earlier positions, so `i=b`.  If `i>1`, the first
`i-1=b-1` positions form a proper sum cut.  Indecomposability forces
`i=b=1`.  Hence first/minimum is the only active pair in the block.  Blocks
are disjoint, proving simultaneous well-definedness and
`F(alpha direct-sum beta)=F(alpha) direct-sum F(beta)`.

### Step 2. Strict refinement and recurrence

For nontrivial indecomposable `beta`, exchanging its first entry with its
minimum makes the output begin in `1`.  It has a unique form
`1 direct-sum gamma`, with `gamma` of size one less.  Thus a changed old block
creates at least two new components, while old boundaries persist by sum
compatibility.  Component count strictly increases off a fixed state.

A fixed state has no nontrivial indecomposable component, hence is the
identity.  Strict increase on a finite carrier excludes every other cycle.

### Step 3. Exact recursive clock

Define `h(1)=0`.  Define `h(beta)=1+h(gamma)` for a nontrivial indecomposable
`beta` with image `1 direct-sum gamma`.  Define the height of a direct sum as
the maximum height of its components, standardizing translated component
alphabets.

The factors evolve independently and synchronously, so a direct sum reaches
identity when its slowest factor does.  A nontrivial indecomposable spends one
epoch reaching `1 direct-sum gamma`, after which the singleton is inert.
Induction on size gives `tau(pi)=h(pi)` for every source.

### Step 4. Sharp height

Size induction gives `h(pi)<=n-1`.  If `pi` is decomposable, every block has
size at most `n-1`, so its height is at most `n-2`; if it is indecomposable,
one step leaves a suffix of size `n-1`.  The cyclic shift
`omega_n=(2,3,...,n,1)` is indecomposable and maps to
`1 direct-sum omega_(n-1)`, so it has height `n-1`.

### Step 5. Indecomposable-parent lemma

Fix `gamma` of size `m` and start from `1 direct-sum gamma`.  Swap the leading
`1` with a position `r` of `gamma`.  A prefix before the moved `1` lacks the
minimum and cannot be a sum cut.  A prefix containing both exchanged entries
has the same value set as the corresponding prefix of `1 direct-sum gamma`;
it is a proper sum cut exactly when `gamma` has a sum cut at or after `r`.
Thus the parent is indecomposable exactly when `r` lies in the last
indecomposable component of `gamma`.  Its number of choices equals the size
of that component.

### Step 6. Deepest-state recurrence

A depth-`n-1` source must be indecomposable, and its suffix after one epoch
must have depth `n-2`.  Such a suffix is itself indecomposable; otherwise it
could not achieve its maximum.  Its last component therefore has size
`n-1`, so Step 5 gives `n-1` indecomposable parents.  Conversely every such
parent is deepest.  Hence `d_n=(n-1)d_(n-1)` with `d_1=1`, and
`d_n=(n-1)!`.

### Step 7. Layer recurrence

Depth at most `t` is closed under direct sums, with the maximum component
depth.  Unique factorization into a sequence of indecomposables gives
`A_t=1/(1-B_t)`.  Only the singleton is indecomposable at depth zero, so
`B_0=x`.

For a nonempty depth-at-most-`t` suffix `gamma`, its blocks consist of an
arbitrary prefix sequence, counted by `A_t`, and a final indecomposable block.
If that block has size `r`, Step 5 gives `r` parents.  Marking one of its
positions is counted by `x B_t'(x)`.  A new leading entry adds another `x`;
adding the singleton gives
`B_(t+1)=x+x^2 A_t B_t'`.  Cumulative-class subtraction gives exact layers.

### Step 8. Every-target fibre

Let the target components have sizes `(c_1,...,c_s)`.  The image of each old
source block begins with a singleton target component.  Hence the first
target component must have size one.

When `c_1=1`, group consecutive target components into old source blocks.
Every group must start at a singleton component, and Step 5 shows this is
sufficient.  A group ending at component `e` has `c_e` possible parents.  A
boundary may be inserted before `j>=2` precisely when `c_j=1`; choosing it
contributes `c_(j-1)`, while omitting it contributes `1`.  The terminal group
contributes `c_s`.  Independent summation over the optional boundaries gives

```text
c_s product_(j>=2,c_j=1) (1+c_(j-1)).
```

Thus the image is exactly the permutations beginning with `1`, of which
there are `(n-1)!`.  Fibre mass is `n!` because fibres partition `S_n`.

### Step 9. Unique maximum fibre

Set `E={i<s:c_(i+1)=1}`.  Since `1+c_i<=2^(c_i)` and
`c_s<=2^(c_s-1)`, the fibre is at most

```text
2^(c_s-1 + sum_(i in E)c_i) <= 2^(n-1).
```

Equality in the exponent bound requires every `i<s` to lie in `E`, so
`c_2=...=c_s=1`; image membership gives `c_1=1`.  The target is the identity.
Conversely its product contains `n-1` factors equal to two and has size
`2^(n-1)`.

Therefore all claims follow. ∎

## Boundary audit

- `n=1`: the identity is the only state, has height zero, image size one,
  deepest count `0!=1`, and fibre `1=2^0`.
- A singleton target group has weight one and is covered by the parent lemma.
- A target outside the image has no compatible first group, rather than a
  product with an undefined first factor.
- Ordinary, not exponential, generating functions are used because direct
  sums form ordered sequences by size.
- The inequality `c_s<=2^(c_s-1)` has equality at `c_s=1,2`; uniqueness of
  the global maximum instead comes from the separate exponent-budget equality,
  which forces every component size to be one.

## Corrections or missing assumptions

None.

## Open risks

- No external owner search has been completed.
- No closed nonrecursive scalar formula is claimed for all depth layers.
- No all-time target fibre formula or asymptotic law is claimed.
