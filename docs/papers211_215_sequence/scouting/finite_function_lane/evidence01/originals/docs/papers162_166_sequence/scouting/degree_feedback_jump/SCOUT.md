# Degree-feedback jump: bounded exact scout

Date: 2026-09-03  
Decision: **KILL_POWER_MAP_CORE_AND_NO_SECOND_AXIS**  
External status: **HOLD_EXTERNAL / no novelty claim**

## Outcome

DFJ has three clean all-parameter observations: monotone functional-digraph
supports, an exact fixed-point species, and invariant uniformly leaf-decorated
permutation classes.  The last observation is fatal rather than promotive:
those invariant classes realize ordinary power maps, including permutation
squaring on the full `S_n` slice.  Every fibre over a permutation target is
therefore the classical permutation-square-root count.  The one genuinely
state-dependent remainder has irregular global tails and non-permutation
fibres already through six labels; no closed all-time phase portrait or
every-target fibre atlas emerged.

Thus the clean temporal and fibre results are owned power-map/root results,
while the residual fixed-point EGF is one static structural axis.  Two
independent paper-level axes do not survive subtraction.

## Literal system

For an endofunction `f:[n]->[n]`, put

`d_f(v)=#{u:f(u)=v}`

and update all vertices simultaneously by

`T(f)(v)=f^(1+d_f(v))(v)`.

The indegrees in the exponent are computed from the old `f`.

## Universal monotone data

Every `T(f)(v)` lies on the forward `f`-orbit of `v`.  Consequently:

1. `Im(T(f)) subseteq Im(f)`, so rank never increases;
2. every weak component of `T(f)` is contained in a weak component of `f`;
3. every cyclic vertex of `T(f)` was already cyclic for `f`;
4. `T` commutes with every relabelling of `[n]`.

These statements are exact, but they provide only nested supports.  Equality
of the support statistics does not freeze the full update, and recurrent
power-map actions remain.

## The embedded power-map family

Let `pi` be a permutation of a `c`-label core.  Attach exactly `r` private
leaves to each core vertex and point every leaf to its core vertex; call the
resulting endofunction `F_(pi,r)`.  Every core vertex has indegree `r+1` and
every leaf has indegree zero.  Hence, for every `t>=0`,

`T^t(F_(pi,r)) = F_(pi^((r+2)^t),r)`.

The leaf attachments stay fixed, while the core executes the power map
`pi -> pi^(r+2)`.  The case `r=0` is the whole permutation slice and gives

`T^t(pi)=pi^(2^t)`.

If the cycle lengths of `pi` have maximum 2-adic valuation `a`, and `M` is
the lcm of their odd parts, the squaring orbit has exact preperiod `a` and
period `ord_M(2)` (period one when `M=1`).  For example, a 7-cycle already
gives a three-cycle of DFJ states because `ord_7(2)=3`.  Uniform leaf lifts
embed every integer power `k>=2` by taking `r=k-2`.

This is not a new invariant permutation action: it is an explicit embedding
of the generic power-map engine.

## Exact fixed locus

The pointwise fixed condition is

`T(f)=f  iff  f^(d_f(v))(f(v))=f(v) for every v`.

If `d_f(v)>0`, this says that the parent `f(v)` is periodic with period
dividing `d_f(v)`.  It follows that a fixed functional digraph has height at
most two.  Around a core cycle of length `ell`:

- every core vertex has indegree divisible by `ell`;
- every depth-one vertex has a number of leaf children divisible by `ell`;
- all depth-two vertices are leaves.

This yields a closed labelled EGF.  Define the residue exponential

`E_(ell,a)(z)=sum_(j>=0) z^(ell*j+a)/(ell*j+a)!`,

with residues read modulo `ell`, and set

`B_ell(z)=z E_(ell,0)(z)`,

`C_ell(z)=z E_(ell,ell-1)(B_ell(z))`.

Then the fixed endofunction EGF is

`Fix(z)=exp(sum_(ell>=1) C_ell(z)^ell/ell)`.

Its labelled counts for `n=0,...,6` are

`1, 1, 3, 16, 113, 816, 7627`,

matching the literal fixed states.  This is a clean structural result, but it
is only the fixed locus and does not supply a global iterate, period census,
or independent inverse theory.

## Fibres

If a target `tau` is a permutation, any source `f` with `T(f)=tau` must also
have rank `n`, hence must be a permutation.  Therefore

`#{f:T(f)=tau}=#{pi in S_n:pi^2=tau}`.

Write `a_ell` for the number of `ell`-cycles of `tau`.  The classical
cycle-pairing formula is the product over `ell` of

`R_ell(a)=0` when `ell` is even and `a` is odd,

`R_ell(a)=a! ell^(a/2)/(2^(a/2)(a/2)!)`

when `ell` and `a` are even, and

`R_ell(a)=sum_(j=0)^floor(a/2)
             a! ell^j/((a-2j)! 2^j j!)`

when `ell` is odd.  All 873 permutation targets through `S_6` match this
formula.  In particular, the identity fibre consists exactly of involutions,
with sizes

`1, 2, 4, 10, 26, 76` for `n=1,...,6`.

Outside the permutation slice, fibres immediately depend on fine attachment
geometry.  At `n=6`, the targets

`(1,0,0,0,1,3)` and `(1,0,0,0,1,4)`

have the same rank, sorted indegrees, cycle lengths, vertex-depth multiset,
and weak-component sizes, but their DFJ indegrees are respectively one and
two.  A target-resolved inverse theorem would have to recover finer rooted
attachment data; no stable formula appeared.

## Exhaustive phase portrait through six labels

| `n` | states | image | recurrent | fixed | max tail | transformation cycles |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 1 | 1 | 0 | `1^1` |
| 2 | 4 | 3 | 3 | 3 | 1 | `1^3` |
| 3 | 27 | 18 | 18 | 16 | 1 | `1^16 2^1` |
| 4 | 256 | 124 | 121 | 113 | 2 | `1^113 2^4` |
| 5 | 3,125 | 1,455 | 900 | 816 | 3 | `1^816 2^30 4^6` |
| 6 | 46,656 | 18,126 | 8,931 | 7,627 | 3 | `1^7627 2^580 4^36` |

The appearance of only periods `1,2,4` through `n=6` is a small-order
artifact: the 7-cycle supplies period three, and the permutation slice has
the full multiplicative-order spectrum.  The complete depth, image, fibre,
rank-transition, component-splitting, and cyclic-support-loss histograms are
frozen in `CANONICAL.txt`.

## Exact evidence

The independent verifier:

- exhausts all 50,069 endofunctions on `1<=n<=6`;
- constructs the complete DFJ functional graph at every `n`;
- checks image, weak-component, and cyclic-support monotonicity for every
  source;
- checks the fixed criterion and two relabelling generators for every source;
- checks every permutation target against the square-root formula;
- checks 4,440 uniform-leaf power-map iterate cells;
- independently expands the fixed EGF;
- executes **352,328 assertions**.

Two fresh replays matched `CANONICAL.txt` byte for byte.  The canonical
transcript SHA256 is
`d1004ba0258ed477abcbe848ac3223801aac56c5b1c8e6b14c2b3d539de6f891`;
the verifier SHA256 is
`47e36f8ee8cb45c2ac680a4c15a67a8b8e3c7e8ec0e93b2200ed335b8101c688`.

## Decision

**KILL_POWER_MAP_CORE_AND_NO_SECOND_AXIS.**  The fixed-locus species is the
only clean residual theorem.  The complete temporal theory visible on large
invariant classes and the complete fibres visible on permutation targets are
generic power-map and transformation-root theory.  The remaining
non-permutation dynamics has neither a sharp all-parameter temporal law nor
an every-target fibre/image atlas.  No paper or reserve is authorized.
