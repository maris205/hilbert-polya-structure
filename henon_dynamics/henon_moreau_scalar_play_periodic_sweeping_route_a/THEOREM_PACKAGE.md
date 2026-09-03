# Proof Package

## Claim

Fix `r>=0`. Let `u in W1,1([0,T])` satisfy `u(0)=u(T)=m`. Assume that for some `tau in [0,T]`, `u` is nondecreasing from `m` to `M` on `[0,tau]` and nonincreasing from `M` to `m` on `[tau,T]`; plateaus and almost-everywhere corners are allowed. Put `D=M-m`.

For each feasible initial state `z in [m-r,m+r]`, the scalar sweeping problem

`y(t) in C(t)=[u(t)-r,u(t)+r]`, `-ydot(t) in N_(C(t))(y(t))` almost everywhere, `y(0)=z`,

has a unique absolutely continuous solution. On every monotone segment beginning at `t0`,

`y(t)=Proj_[u(t)-r,u(t)+r](y(t0))`.

The one-period Poincaré map based at a minimum is

`P(z)=min(m+r,max(M-r,z))`.

It is increasing, one-Lipschitz, and idempotent. Therefore every initial state reaches a periodic response in at most one period. The fixed responses are:

- if `D<2r`, every `z in [M-r,m+r]` is fixed and the corresponding periodic play output is constant;
- if `D=2r`, the fixed interval collapses to the single constant output `m+r=M-r`;
- if `D>2r`, `m+r` is the unique fixed state and it generates the unique nonconstant periodic play loop.

For two solutions with the same input, initial order and initial distance are preserved/nonincreased. If `phi` is an orientation-preserving absolutely continuous surjection and both `u` and `u composed phi` are `W1,1`, then the play response to `u composed phi` is `y composed phi`.

With `s=u-y`, every solution satisfies

`Var(u)=Var(y)+Var(s)` and `integral s dy=r Var(y)`.

For every periodic response in the frozen single-excursion class,

`Var(y)=2 max(D-2r,0)` and `integral s dy=2r max(D-2r,0)`.

At `r=0`, `y=u` and `s=0`. At `D=0`, `P` is the identity on `[m-r,m+r]`. All statements include extrema plateaus and `W1,1` corners.

## Status

PROVABLE AS STATED

## Assumptions

- The convex-analysis normal cone is `N_C(y)={v: v(z-y)<=0 for every z in C}`.
- The input has exactly one ordered rise and one ordered fall; a plateau may belong to either adjoining segment.
- Time changes are orientation-preserving absolutely continuous surjections for which the composed input remains `W1,1`.
- Variation and Stieltjes integrals use the absolutely continuous representatives.

## Notation

- `C(t)=[u(t)-r,u(t)+r]` is the moving interval.
- `y` is the play output and `s=u-y in [-r,r]` the complementary stop variable.
- `Proj_[a,b](z)=min(b,max(a,z))`.
- `P` is the return map from one minimum to the next.

## Proof Strategy

Solve the normal-cone inclusion explicitly on monotone segments by projection, concatenate at the turning plateau, and reduce the full periodic theorem to an elementary clamp map. Derive variation and dissipation from the complementary a.e. motion of `y` and `s`.

## Dependency Map

1. Existence and uniqueness use the monotone-segment projection lemma.
2. The Poincaré map is the composition of the increasing and decreasing segment formulas.
3. The chamber atlas and entrainment use the fixed set and idempotence of that clamp.
4. Order, nonexpansion, and reparameterization use projection monotonicity and dependence only on ordered input values.
5. Variation and dissipation use the pointwise alternatives `ydot=0` or `sdot=0` and the active-boundary sign.

## Proof

### Step 1: the monotone-segment solution

Suppose first that `u` is nondecreasing on `[t0,t1]` and `y0 in C(t0)`. Define

`y(t)=max(y0,u(t)-r)`.

The upper constraint holds because `y0<=u(t0)+r<=u(t)+r`, and the lower constraint is built into the maximum. Before the moving lower endpoint reaches `y0`, `ydot=0`. When it pushes the state, `y=u-r` and `ydot=udot>=0`, so `-ydot<=0` lies in the normal cone at the lower endpoint. Thus the inclusion holds almost everywhere.

If `u` is nonincreasing, the same calculation at the upper endpoint gives

`y(t)=min(y0,u(t)+r)`.

These are exactly the projections of `y0` onto the current intervals. Any solution in the interior has zero derivative. At a moving active endpoint, the normal-cone sign fixes its derivative to the endpoint velocity; otherwise feasibility would fail immediately. Hence the displayed solution is unique. The argument is almost-everywhere and therefore includes plateaus and corners. Concatenation at `tau` gives the unique full-period solution.

### Step 2: exact Poincare clamp

Starting from `z` at the minimum, the increasing branch ends at

`z_up=max(z,M-r)`.

The decreasing branch then ends at

`P(z)=min(z_up,m+r)=min(m+r,max(M-r,z))`.

This proves the claimed map without sampling the detailed speed of the input.

### Step 3: fixed sets and one-period entrainment

If `D<2r`, then `M-r<m+r`, and `P` is projection onto `[M-r,m+r]`. Its fixed set is exactly that interval. If `D=2r`, the interval has one point. If `D>2r`, then `M-r>m+r`; the displayed nested min/max equals `m+r` for every feasible `z`, so this is the unique fixed state.

In every chamber, direct substitution gives `P(P(z))=P(z)`. After one forcing period the state is therefore fixed under all later returns, and the subsequent response is periodic. For `D<=2r`, a fixed state is never reached by either moving endpoint, so its periodic output is constant. For `D>2r`, the unique fixed output moves from `m+r` to `M-r` on the rise and back on the fall, and is nonconstant.

### Step 4: order, nonexpansion, and rate independence

For a fixed interval, scalar projection is increasing and one-Lipschitz. Each segment evolution is such a projection in the initial state, and concatenation preserves both properties. Thus `z1<=z2` implies `y1(t)<=y2(t)`, and

`|y1(t)-y2(t)|<=|z1-z2|`.

The segment formulas depend only on the current ordered input value, not on its traversal speed. Let `phi` be as assumed. Substituting `u(phi(t))` into those formulas gives `y(phi(t))`; uniqueness identifies this with the response to the reparameterized input. Constant parts of `phi` and input plateaus merely repeat the same projection.

### Step 5: variation and dissipation

Set `s=u-y`. Almost everywhere, either the state is not being pushed and `ydot=0`, or it is on an active boundary and `sdot=0`. Therefore `udot=ydot+sdot` with at most one nonzero summand, so

`|udot|=|ydot|+|sdot|`.

Integration gives `Var(u)=Var(y)+Var(s)`. On an active increasing lower boundary, `s=r` and `ydot>=0`; on an active decreasing upper boundary, `s=-r` and `ydot<=0`. Off the active boundary `ydot=0`. Hence almost everywhere

`s ydot=r |ydot|`,

which integrates to `integral s dy=r Var(y)`.

For a fixed periodic response with `D<=2r`, `y` is constant and its variation is zero. If `D>2r`, it rises through distance `D-2r` and falls through the same distance. Thus

`Var(y)=2(D-2r)`.

The two cases combine into the displayed positive-part formula and its dissipation consequence.

### Step 6: degenerate faces

If `r=0`, the interval is the singleton `{u(t)}`, so `y=u` and `s=0`; all variation and dissipation identities survive. If `D=0`, the moving interval is constant and every feasible initial state remains fixed, so `P` is the identity. At `D=2r`, the positive part vanishes and the unique periodic output is constant, so no hidden dissipation occurs at equality.

Therefore every part of the claim follows. ∎

## Corrections or Missing Assumptions

- None. The admissibility clause on time reparameterizations is necessary for an honest `W1,1` statement.

## Open Risks

- This is a source-local reconstruction and makes no priority claim.
- The complete periodic-response classification has no arithmetic labels.
- The normal-cone formulation is a dissipative variational structure, not a natural self-adjoint quantization.
- No assertion is made for multi-extremum forcing, vector play, discontinuous input, or arbitrary nonconvex sweeping sets.
