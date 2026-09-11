# Independent proof rederivation — minimum inverse-position feedback

**Date:** 2026-09-03 UTC  
**Status:** `COHERENT AS STATED`  
**External status:** `HOLD_EXTERNAL`  
**Independence rule:** this derivation starts from the literal map below.  It
does not import the earlier scout program, canonical transcript, or proof
text.

## 1. Frozen object and notation

Let `[n]={0,...,n-1}` and let `X_n=[n]^[n]`.  A state `f` is both an
endofunction and the word `f(0)...f(n-1)`.  Define

```text
M(f)(i) = min {j in [n] : f(j)=i}    when i is present,
          i                           when i is absent.
```

The target is the exact finite dynamics of repeated application of `M`, not
composition powers of a fixed `f`.  Tail means the least nonnegative time at
which an orbit enters its periodic part.

## 2. Algebraic normalization: a canonical inner inverse, not a mutual inverse

Put `q=M(f)`.  If `i` is in `im(f)`, then `q(i)` is the least member of the
kernel class `f^(-1)(i)`.  Hence

```text
f(q(f(j))) = f(j)                    for every j,
```

or `f q f=f`.  Thus the present-symbol portion of `q` is the increasing-chain
choice of a kernel transversal.  The absent-symbol default extends that
partial section by `q(i)=i`.

This extension need not be a mutual semigroup inverse: for `f=(0,0)`,
`M(f)=(0,1)` and `M(f) f M(f)=f != M(f)`.  Therefore results about inverse
matchings do not by themselves give the iteration studied here.

The related map on positions is

```text
e_f(j)=M(f)(f(j)).
```

It sends every position to the least position in its `ker(f)` block.  It is
an idempotent, `e_f^2=e_f`, and `ker(e_f)=ker(f)`.  This is the precise
kernel-representative-retraction (`KRR`) relation; it is structural
background, not a second claimed dynamical system.

## 3. First image and functional components

Let `g=M(f)`.  Whenever `g(i)!=i`, the value `g(i)` is the first position of
symbol `i` in `f`.  Distinct symbols cannot have the same first position, so

```text
{g(i): g(i)!=i}
```

has no repetitions.  In the functional digraph with arrow `i -> g(i)`, each
vertex has at most one incoming nonloop arrow.  Every weak component is
therefore exactly one of:

1. a directed cycle of length at least two; or
2. a loop-rooted directed path, with a singleton loop allowed.

This off-diagonal injectivity condition is only necessary.  For example,
among the `63,840` off-diagonal-injective targets at `n=7`, the literal fibre
test below rejects `12,960`.

## 4. Exact component action

### 4.1 Cycles

On a directed cycle every symbol occurs once.  Its first position is its
unique preimage, so `M` replaces the cycle permutation by its inverse.  A
two-cycle is fixed; every cycle of length at least three is exchanged with
its reverse orientation.

### 4.2 Paths

Write a path in root-to-leaf order as

```text
P=(p_0,p_1,...,p_(s-1)),
g(p_0)=p_0,   g(p_j)=p_(j-1) for j>=1.
```

In the word `g`, the root symbol `p_0` occurs at positions `p_0` and `p_1`;
each `p_j`, `1<=j<=s-2`, occurs at position `p_(j+1)`; and `p_(s-1)` is
absent.  Consequently:

```text
p_0 > p_1 :  M reverses the whole path;
p_0 < p_1 :  M fixes p_0 as a singleton and reverses the remaining path.
```

No component merge is possible, and a split is irreversible.

For `s>=2`, a path is recurrent if and only if

```text
p_0 > p_1  and  p_(s-1) > p_(s-2).
```

Indeed, the two inequalities make the path and its reversal exchange.  If
the first fails, the root immediately splits.  If the first holds and the
second fails, one reversal makes the new root comparison increasing, after
which that endpoint splits.  Singletons are fixed.

## 5. Sharp path, image, and carrier clocks

Let `D(P)` be the tail of a path and let `P^-` denote deletion of the last
entry.  Induction on `s` proves

```text
D(P) <= 2s-2,
```

with equality, for `s>=2`, exactly when

```text
p_0 > p_1 > ... > p_(s-1).
```

The induction has only three cases.

- A recurrent path has `D(P)=0`.
- If `p_0<p_1`, one step splits `p_0` and leaves the reversal of an
  `(s-1)`-path.  Thus `D(P)<=1+[2(s-1)-2]=2s-3`.
- If `p_0>p_1` but the path is not recurrent, then
  `p_(s-1)<p_(s-2)`.  One step reverses the whole path and the next splits
  `p_(s-1)`, leaving the original prefix `P^-`.  Hence
  `D(P)=2+D(P^-)<=2s-2`.  Equality holds exactly when `P^-` is strictly
  decreasing; the endpoint inequality then makes all of `P` strictly
  decreasing.

Components update in parallel, so a state's tail is the maximum of its
component tails.

Every first-position vector contains the value zero: the symbol `f(0)` has
first occurrence zero.  The unique full-label path attaining `2n-2` is the
strictly decreasing order `(n-1,...,0)`, whose coordinate values are
`{1,...,n-1}` and contain no zero.  It is therefore not in `im(M)`.  If an
image has no full-label path, its largest path has at most `n-1` labels and
tail at most `2n-4`.  It follows, integrally, that

```text
max {tail(g): g in im(M)} <= 2n-3.
```

For `n>=2`, the source

```text
f=(1,2,...,n-1,1)
```

maps to the increasing path `(0,1,...,n-1)`.  The latter has tail `2n-3`,
so the image bound is sharp, and the source has tail `2n-2`.  Since every
arbitrary source spends one step entering `im(M)`, the full-carrier height is
exactly `2n-2`.  At `n=1` the unique state is fixed and both heights are zero.

## 6. Recurrent connected census and EGF

On a fixed `s`-set, directed cycles contribute `(s-1)!` for `s>=2`.
Recurrent paths are linear orders satisfying the two endpoint inequalities.

- `s=1`: one singleton component.
- `s=2`: no recurrent path and one directed two-cycle.
- `s=3`: the middle entry must be the smallest, giving two paths; adding the
  two directed three-cycles gives four connected components.
- `s>=4`: the comparisons concern disjoint pairs of positions.  Swapping
  the first pair and swapping the last pair act freely and independently on
  all `s!` orders, so exactly `s!/4` satisfy both.

Thus the connected recurrent counts are

```text
c_1=1,  c_2=1,  c_3=4,
c_s=(s-1)!+s!/4  for s>=4.
```

A recurrent state is an unordered labelled set of these connected
components.  Its EGF is therefore

```text
exp(sum_(s>=1) c_s x^s/s!)
 = exp(-log(1-x)+x^3/3+x^4/[4(1-x)])
 = 1/(1-x) exp(x^3/3+x^4/[4(1-x)]).
```

It gives

```text
R_0,...,R_7 = 1,1,2,8,38,220,1540,12460.
```

## 7. Fixed counts, positive iterates, and zeta

A recurrent path of size greater than one is exchanged with its distinct
reversal.  A directed cycle is fixed by inversion only at length two.
Therefore a fixed state is exactly a set of singleton loops and directed
two-cycles: equivalently, an involution.  If `I_n` is the involution number,

```text
sum I_n x^n/n! = exp(x+x^2/2).
```

Every recurrent state has period one or two, and any point fixed by a
positive iterate is recurrent.  Hence, for `k>=1`,

```text
Fix(M^k) = I_n  when k is odd,
           R_n  when k is even.
```

Substitution into the Artin--Mazur definition gives the formal finite-map
identity

```text
zeta_n(z)=(1-z)^(-I_n) (1-z^2)^(-(R_n-I_n)/2).
```

This conversion is generic bookkeeping and receives no contribution credit.

## 8. Every-target one-step fibre

Fix any target `g in X_n` and put

```text
U={i:g(i)!=i}.
```

If `{g(i):i in U}` has a repetition, no source exists.  Otherwise let

```text
F={i:g(i)=i and i notin g(U)}.
```

For a source over `g`, every `i in U` must be present with first position
`g(i)`.  A fixed coordinate `i` is either absent or is present with first
position `i`.  If `i in g(U)`, position `i` is already forced to another
symbol, so the present alternative is impossible; this explains exactly why
the optional set is `F`, not all fixed coordinates.

Choose the optional-present set `A subseteq F`, put `P_A=U union A`, and set

```text
r_A(i)=g(i) for i in U,       r_A(i)=i for i in A,
R_A={r_A(i):i in P_A}.
```

Positions in `R_A` are forced.  At an unforced position `j`, the legal
letters are precisely the present symbols whose first occurrence is already
open, namely those `i` with `r_A(i)<j`.  Choices at distinct positions are
independent.  Therefore

```text
|M^(-1)(g)| = sum_(A subseteq F)
  product_(0<=j<n, j notin R_A) #{i in P_A:r_A(i)<j}.
```

A zero factor rejects an impossible optional declaration.  The same formula
is consequently an if-and-only-if first-image test, including unsupported
targets and all fixed/present collisions.

## 9. Bell maximum

Fix the kernel partition of a hypothetical source.  For each block with
minimum position `j`, its symbol label is forced by `g`: it is the unique
off-diagonal `i` with `g(i)=j`, when one exists, and otherwise can only be the
fixed symbol `j`.  Thus at most one source with that kernel partition lies
over a given target.  Since there are `B_n` partitions,

```text
|M^(-1)(g)| <= B_n.
```

For `g=id`, every set partition gives a source: label each block by its least
position.  Its present labels first occur at themselves and every nonminimum
label is absent, so its image is the identity.  This construction is
injective and exhausts all `B_n` partitions.  Hence the maximum fibre is
exactly `B_n`, attained at least at the identity.  The verified prefix is

```text
1,2,5,15,52,203,877  (n=1,...,7).
```

No uniqueness assertion for the maximizing target is needed here.

## 10. Small boundaries

- `n=1`: one fixed state; `R_1=I_1=B_1=1`; both heights zero.
- `n=2`: four states, image size three, two recurrent/fixed states, no
  two-cycle orbit, carrier height two, image height one, maximum fibre two.
- `n=3`: 27 states, image size 14, eight recurrent states, four fixed states,
  two dynamical two-cycles, carrier height four, image height three, maximum
  fibre five.

The canonical transcript records every state edge, tail, period, and target
fibre for these three sizes.

## 11. Boundaries and non-claims

- The off-diagonal injection property is not an image characterization; the
  fibre formula is.
- Kernel transversals, least block representatives, restricted-growth/set-
  partition encodings, labelled component EGFs, involution counts, Bell
  numbers, and Artin--Mazur conversion are classical ingredients.
- The result is a finite exact theorem package for this literal default rule.
  It is not a worldwide novelty, priority, or freedom-to-operate claim.
- The candidate can advance only as `GREEN_OWNER_THIN / HOLD_EXTERNAL`.
