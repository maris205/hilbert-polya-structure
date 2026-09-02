# EDP independent hostile gate

## Decision

**KILL — `KILL_GENERIC_PULLBACK_RBELL_AND_P110_COLLISION`.**

The proposed formula package is mathematically correct after one small boundary
repair.  It nevertheless does not clear the paper-value gate.  For an arbitrary
finite self-map, pullback on equivalence relations already gives the iterate,
the principal-filter image, its Bell size, and every supported fibre as an
ordinary extension count.  EDP merely specializes this generic theorem to a
rank staircase.  Its two-variable fibre polynomial is the same extension
argument with one distinguished old block, hence a marked/shifted `r`-Bell
enumerator rather than an independent axis.  After those ingredients receive
zero residual credit, the remaining initial-prefix depth histogram has the same
partition/Bell/sharp-depth silhouette already occupied by P110 and is too thin
for a standalone paper.

This is a value kill, not a mathematical counterexample.  Severity against the
scout as written is **0 Critical / 0 Major / 1 Minor**.  External status remains
**HOLD_EXTERNAL**.  No paper allocation or theorem contract is recommended.

## Object reconstructed independently

Let `Pi(X)` be the equivalence relations on a finite set `X`.  For a self-map
`f:X -> X`, define

```
T_f(R) = {(x,y): (f(x),f(y)) in R}.
```

EDP uses `X=[n]` and `p(1)=1`, `p(i)=i-1` for `i>1`.  The review used literal
canonical tuples of blocks and literal pairwise relation pullback.  It did not
import the scout verifier, its restricted-growth encoding, or any author
routine.

## The generic theorem that collapses the package

For every finite self-map `f` and every `t>=0`:

1. `T_f^t(R)=(f^t)^*(R)`.  This is functoriality of inverse image, proved by
   expanding membership in both relations.
2. The image of `T_f^t` is exactly

   ```
   {eta in Pi(X): ker(f^t) <= eta}.
   ```

   Necessity is immediate.  Conversely, if `eta` contains the kernel, it
   descends to a well-defined equivalence relation on `im(f^t)`; extend that
   relation arbitrarily to `X` and pull it back.
3. Therefore the image interval is canonically `Pi(im(f^t))` and has
   `Bell(rank(f^t))` elements.
4. If the descended target has `b` blocks and `m=|X\im(f^t)|`, every source is
   obtained by extending those `b` old blocks across `m` invisible points.
   Its cardinality is

   ```
   E_m(b) = sum_{j=0}^m binom(m,j) Bell(j) b^(m-j).
   ```

   Choose `j` invisible elements that form new-only blocks, partition them,
   then attach every remaining invisible element independently to an old
   block.  This is precisely the standard distinguished-block/`r`-Bell
   extension mechanism.

Items 1--4 hold for all finite self-maps, not merely for EDP.  Thus changing
the endpoint scheduler changes only the ranks and kernels; it does not create
new image or inverse-geometry axes.

## Specialization to EDP

Put `h=min(t,n-1)`.  Direct induction gives

```
p^t(i)=max(1,i-t),
im(p^t)={1,...,n-h},
ker(p^t)={{1,...,h+1},{h+2},...,{n}}.
```

Consequently `eta` is supported at time `t` exactly when its first `h+1`
labels lie in one block, and

```
|im(T^t)| = Bell(n-h).
```

The images form the claimed nested Bell staircase and stabilize at the unique
indiscrete partition.

### Exact target-resolved polynomial

For supported `eta`, let `b` be its number of blocks and let
`a=|root(eta)|-h`, the size of the descended root block.  Among the `h`
invisible source labels, choose `j` to form new-only blocks.  If their partition
has `k` blocks it contributes `z^k`; every remaining invisible label either
joins the distinguished old root block with weight `u`, or one of the other
`b-1` old blocks with total weight `b-1`.  Multiplying by the `b` old blocks and
the `a` root elements forced by the descended target gives

```
Phi_(t,eta)(z,u)
 = z^b u^a sum_{j=0}^h binom(h,j) B_j(z) (u+b-1)^(h-j).
```

This proves the root-size exponent: it is `a` before the invisible labels are
assigned, not `|root(eta)|` and not `a+h`.  Setting `z=u=1` gives exactly
`E_h(b)`.  For unsupported targets the fibre and polynomial are both zero.

Equivalently, after suppressing the forced factor, the exponential generating
function in `h` is

```
exp((u+b-1)x + z(exp(x)-1)),
```

which makes the shifted Bell-polynomial engine explicit.

### Point depths

Let `m(pi)` be the largest initial prefix contained in the block of `1`.
Then `T^t(pi)` is indiscrete exactly when `{1,...,n-h}` is contained in one
source block, so

```
D(pi)=n-m(pi).
```

For `1<=t<=n-1`, contracting the forced block on
`{1,...,n-t}` gives `Bell(t+1)` partitions with depth at most `t`; contracting
`{1,...,n-t+1}` gives `Bell(t)` with depth at most `t-1`.  Hence

```
#{pi:D(pi)=0}=1,
#{pi:D(pi)=t}=Bell(t+1)-Bell(t).
```

The maximum is `n-1`.  All states flow to the sole fixed point, so the stable
image is the indiscrete partition and the dynamical zeta function is
`1/(1-u)`.

## Boundary and adversarial checks

- **`n=1`:** `p` and `T` are the identity on the one-state space for every
  time; `h=0`, the image size is always one, depth is zero, and the unique
  fibre polynomial is `zu`.  This exposes the only textual defect below.
- **`t=0`:** `h=0`; every target is supported and the formula reduces to the
  singleton source monomial `z^b u^|root(eta)|`.
- **`t>=n-1`:** only the indiscrete target is supported.  Its polynomial
  enumerates all `Bell(n)` source partitions and is independent of any further
  increase in `t`.
- **Unsupported targets:** literal enumeration found no source.  The
  principal-filter characterization proves this for all parameters.
- **Overlapping image description:** there is no union ambiguity.  It is the
  single principal filter above `ker(p^t)`, and deflation is a bijection to
  `Pi_[n-h]`.
- **Mass checks:** coefficient sums agree with literal source enumeration for
  every supported target tested; summing all target fibres returns `Bell(n)`.

## Finding

### Minor m1 — the one-step corollary misses the singleton exception

`SCOUT.md` says, without a qualifier, that the one-step indegree is `b+1`.
For `n=1`, time one still has `h=0`, the unique target has `b=1`, and its actual
indegree is one, not two.  Formula (7) itself is correct because it uses
`h=min(t,n-1)`.  The sentence should read “for `n>=2`, one-step indegree is
`b+1`; for `n=1` it is one.”  This is a local prose repair and does not change
the kill decision.

## Independent computation

`verify_hostile.py` performs two distinct audits:

- all `288` endofunctions on labelled sets of sizes `1..4`, checking the
  generic iterate, principal-filter image, Bell rank, and every supported
  unweighted fibre; and
- every one of the `5,295` partitions through `n=8`, at times `0..n+2`,
  checking literal EDP iterates, all supported and unsupported targets, every
  coefficient of the `(z,u)` polynomial, fibre mass, image staircase, fixed
  locus, point depths, saturated times, and all boundary clauses.  A separate
  DP comparison tests the closed extension sum through `h=14`, `b=8`.

The frozen run records **294,653 assertions**.  Two fresh-process replays were
required to match `CANONICAL.txt` byte for byte.  The verifier deliberately
uses a block-tuple representation rather than the scout's RGF implementation.

## Claim ceiling after subtraction

The largest defensible residual statement is:

> For the predecessor map on `[n]`, pullback depth is governed by the largest
> initial prefix in the root block, giving layers
> `Bell(t+1)-Bell(t)` for `1<=t<=n-1`.

That is a correct short observation, but it is not paper-sized once generic
pullback images/fibres, shifted `r`-Bell enumeration, and P110's existing
partition/Bell/sharp-depth asset are removed.  Verdict: **KILL**, with all
external use held.
