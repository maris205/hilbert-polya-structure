# Proof package

## Frozen theorem

Let `x=(x1,x2)` be a cadlag path on `[0,T]` with `x(0)` in the
nonnegative quadrant, and let

`R=[[1,-rho],[-sigma,1]]`, where `rho,sigma>=0`.

A Skorokhod solution is a pair `(z,y)` of cadlag paths such that

- `z=x+R y` is coordinatewise nonnegative;
- `y(0)=0` and each `y_i` is nondecreasing;
- `integral_[0,t] z_i(s) dy_i(s)=0` for `i=1,2`, with `z_i(s)` evaluated
  after any jump at `s`.

Then the following are equivalent:

1. `rho*sigma<1`;
2. every such input on every finite horizon has exactly one Skorokhod
   solution.

In that chamber the regulator is the unique fixed point

`y1=L(x1-rho*y2)`, `y2=L(x2-sigma*y1)`,

where `L(f)(t)=sup_(0<=s<=t)[-f(s)]_+`.

If `rho,sigma>0`, set `w1=sqrt(rho)`, `w2=sqrt(sigma)`,
`q=sqrt(rho*sigma)` and

`||u||_w=max(||u1||_infinity/w1,||u2||_infinity/w2)`.

The fixed-point map has Lipschitz constant exactly `q` on the whole function
space.  For two inputs and their solutions,

`||y-y'||_w <= ||x-x'||_w/(1-q)`,

`||z-z'||_w <= 2||x-x'||_w/(1-q)`.

Starting Picard iteration at zero gives a coordinatewise nondecreasing
sequence and

`||y^(n+1)-y^n||_w <= q^n ||y^(1)||_w`,

`||y-y^n||_w <= q^n ||y^(1)||_w/(1-q)`.

The solution map is causal, maps continuous inputs to continuous solutions,
and commutes with every continuous nondecreasing onto time change preserving
the endpoints.

The threshold is sharp in two ways.  If `rho*sigma=1` (hence both couplings
are positive), zero input has the distinct solutions

`y=(rho*h,h)`, `z=0`

for every nondecreasing cadlag `h` with `h(0)=0`.  If `rho*sigma>=1`, an
input equal to zero before some time and jumping there to `(-1,-1)` has no
solution.  If one coupling is zero, the well-posed triangular solution is
obtained by two successive scalar regulators; if both vanish, the two
coordinates reflect independently.

## Status

`PROVABLE_AS_STATED`.

## Scalar regulator lemma

For scalar cadlag `f` with `f(0)>=0`, the unique pair `r>=0`, `g=f+r>=0`
with nondecreasing cadlag `r`, `r(0)=0`, and post-jump complementarity
`integral g dr=0` is

`r=L(f)=sup_(s<=t)[-f(s)]_+`.

Indeed, this running supremum is the least nondecreasing correction making
`f+r` nonnegative.  It can increase only when a new negative running minimum
of `f` is reached, at which time the corrected state is zero, including after
a downward jump.  Conversely, feasibility forces any regulator to dominate
`L(f)`.  If it first rose strictly above `L(f)`, its corrected state at that
increase would be positive, contradicting complementarity.  Thus it equals
`L(f)`.

The elementary inequality

`||L(f)-L(g)||_infinity <= ||f-g||_infinity`

follows because positive part and running supremum are both one-Lipschitz.

## Fixed-point equivalence and sufficiency

Suppose `(z,y)` solves the two-dimensional problem.  Holding the other
regulator fixed, the first coordinate reads

`z1=(x1-rho*y2)+y1`.

The scalar lemma and its complementarity condition give
`y1=L(x1-rho*y2)`; the second coordinate is identical with `rho` replaced by
`sigma`.  Conversely, any fixed point of these two equations produces a
nonnegative state and coordinatewise complementarity by the scalar lemma.  It
also has the required initial value: at time zero, `x(0)>=0` makes the fixed
point equations imply `y1(0)<=rho*y2(0)` and
`y2(0)<=sigma*y1(0)`.  Since `rho*sigma<1`, both initial regulator values are
zero.
Thus the coupled path problem and the fixed-point problem are equivalent.

Assume first that both couplings are positive.  Let `Phi_x` denote the
fixed-point map.  For two regulators `u,v`, the scalar Lipschitz inequality
gives

`||Phi_x(u)_1-Phi_x(v)_1||_infinity <= rho ||u2-v2||_infinity`,

and its second-coordinate analogue.  Dividing by `w1,w2` shows

`||Phi_x(u)-Phi_x(v)||_w <= q ||u-v||_w`.

The bound is exact: constant function differences supported in either input
coordinate attain each weighted cross coefficient `q`.  Since bounded cadlag
paths are complete in the uniform norm, Banach's theorem gives a unique fixed
point.  Running supremum preserves cadlag paths, so the fixed point belongs to
the required path space.  Because `Phi_x` is order preserving and
`0<=Phi_x(0)`, iteration from zero is monotone.  The displayed successive and
tail estimates are the standard contraction estimates.

For two inputs,

`||Phi_x(u)-Phi_x'(v)||_w <= ||x-x'||_w+q||u-v||_w`.

Apply this at the two fixed points to obtain the regulator bound.  The
weighted operator norm of `R` is at most `1+q`, because each normalized row
has coefficients `1` and `q`.  Consequently

`||z-z'||_w <= ||x-x'||_w+(1+q)||y-y'||_w
             <= 2||x-x'||_w/(1-q)`.

If `rho=0`, first solve `y1=L(x1)` and then
`y2=L(x2-sigma*y1)`.  If `sigma=0`, reverse the order.  This includes normal
reflection and completes sufficiency throughout `rho*sigma<1`.  The weighted
formula is deliberately not applied when a weight vanishes.

## Causality, continuous inputs and time change

Every value of `L(f)(t)` uses only `f` through time `t`; uniqueness therefore
makes the coupled map causal.  For continuous input, every Picard iterate is
continuous, and the contraction makes the convergence uniform, so both
regulator and state are continuous.

Let `lambda:[0,T'] -> [0,T]` be continuous, nondecreasing and onto, with
matching endpoints.  Its image of `[0,t]` is `[0,lambda(t)]`, hence

`L(f composed lambda)=L(f) composed lambda`.

Composition of the fixed-point equations and uniqueness prove that regulation
commutes with `lambda`.  Flat parts merely pause the path.

## Necessity and sharp boundary

At `rho*sigma=1`, the vector `(rho,1)` lies in the kernel of `R`.  Therefore,
for zero input and any nondecreasing cadlag `h` with `h(0)=0`, setting
`y=(rho*h,h)` gives `z=0`.  Every such pair is complementary; taking distinct
`h` proves nonuniqueness.

For any `rho*sigma>=1`, consider the simultaneous jump from zero to
`x=(-1,-1)`.  Immediately after the jump, feasibility would require

`y1 >= 1+rho*y2`, `y2 >= 1+sigma*y1`.

Substitution yields

`(1-rho*sigma)y1 >= 1+rho`,

which is impossible.  Thus at and beyond the wall some inputs have no
solution.  This proves necessity and the exact strict threshold.

## Event convention and finite certificate

For a step input, a jump from previous regulator `y^-` is a two-variable
linear complementarity problem for `d=y-y^-` and the post-jump state.  The
finite certificate exhausts all four active sets over six rational matrices
and 36 events, checks the path fixed point and pause insertion, records 27
Picard rows, and closes three nonunique and three no-solution witnesses.  Its
693 scalar leaves are checked independently by 886 assertions; a separate
SymPy lane closes 5,125 exact identities; two isolated producer runs are
byte-identical; and 68 stale/repaired-hash, parser and semantic attacks are
rejected.  None of these finite counts proves the all-input statement above.

## Route-A obstruction HEN-O330

The free couplings and arbitrary driving path have no intrinsic rational-prime
payload.  Contacts are input-driven, not arithmetic primitive orbits.  The
M-matrix determinant is not an Euler product or target divisor, and the
nonlinear dissipative regulator supplies no natural target-zero quantization.
The strict tuple is

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.

Route A is rejected and Route B is locked under
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local data, Euler factor,
root number, automorphy, target divisor or counting law, functional equation,
target-zero match, Hilbert–Pólya operator or Route-B input is claimed.

## Risks and exclusions

- Off-diagonal signs and post-jump evaluation are part of the theorem.
- The exact contraction statement requires both couplings positive; triangular
  faces are solved separately.
- The paper does not claim finite-step Picard termination.
- The deterministic theorem is not a stochastic invariance principle.
- Source owners retain priority for the classical Skorokhod framework.
