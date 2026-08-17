# Primitivity type firewall

Status: `POST_CANONICAL_DEPENDENT_RENDERING`
Candidate: `SD-C42`
Source lock: `2269e06576dd20c513c5ca9482cb49d36678e07358aaf80f2f08b33806b87041`
Control result: `d0be9630e4f0710c1f602e14e517939f6eef21c582934d79f795a9871f45a30f`
Prototype result: `2fee7701a08ec4f7e019863c6e86bf6fb884bf0323e5593e4bf946ef35e7a995`

This file is a post-run consequence of the exact corrected inputs in
`CONTROL_LOCK.md`; it has no prospective or novelty status.

## Typed spaces and return map

Let

\[
X=\mathbb N^{\mathbb N},\qquad
\sigma(a_1,a_2,a_3,\ldots)=(a_2,a_3,a_4,\ldots)
\]

be the digit space and one-digit shift.  Let

\[
X_2=(\mathbb N^2)^{\mathbb N},\qquad
\rho((a_1,a_2),(a_3,a_4),\ldots)=((a_3,a_4),(a_5,a_6),\ldots)
\]

be the ordered-pair space and one-pair shift.  The grouping bijection

\[
\iota(a_1,a_2,a_3,a_4,\ldots)
 =((a_1,a_2),(a_3,a_4),\ldots)
\]

satisfies the typed identity

\[
\rho\circ\iota=\iota\circ\sigma^2.
\]

Thus `sigma^2` acts on `X`; `rho` acts on `X2`.  Writing `rho=sigma^2`
without the conjugacy is only shorthand and is not used in a proof.  The
canonical control and prototype independently checked the fixture
`(1,2,3,4,5,6,7,8)`, rejected a two-pair shift on `X2`, and rejected an
unreversed block-order mutation.

## Three noninterchangeable primitive types

1. `SigmaPrimitiveDigit` is a cyclic digit word of least period under
   `sigma`.
2. `RhoPrimitivePair` is a cyclic ordered-pair word of least period under
   `rho`, quotienting only cyclic pair rotation.
3. `GeodesicPrimitiveClass` is a primitive hyperbolic/geodesic conjugacy
   class.

Paper 40 proves statements about `RhoPrimitivePair`.  The inherited SD-C04
card supplies the one-digit Gauss branches, the operator
`L_s`, digit-word data, and the analytic determinant `det(I-L_s^2)`.  It does
not supply a pair-primitive ledger or A1 credit for `rho`.  The identity at
`u=1` is a Fredholm-determinant/Selberg-zeta identity; it is not an objectwise
bijection among these three primitive types.

## Exact sigma-to-rho splitting law

If a `sigma` orbit has least period `n`, then its restriction to `sigma^2`
has

\[
\gcd(n,2)
\]

cycles, each of length `n/gcd(n,2)`.  Therefore an odd-period orbit stays one
cycle, whereas an even-period orbit splits into two phase cycles.  If
`N_D(n)` counts primitive digit necklaces over `D` digits and `N_{D^2}(k)`
counts primitive ordered-pair necklaces, then

\[
N_{D^2}(k)=2N_D(2k)+\mathbf 1_{k\ \mathrm{odd}}N_D(k).
\]

Proof: points of one least-period-`n` orbit are indexed by
`Z/nZ`; `sigma^2` adds `2`, whose number of cycles is `gcd(n,2)` and whose
cycle length is `n/gcd(n,2)`.  A `rho` cycle of length `k` can therefore come
from a digit cycle of period `2k` (two phases), or, only when `k` is odd, from
a digit cycle of period `k` (one phase).  This gives the formula after
passing to primitive cyclic classes.

For `D=2`, the independently recomputed digit counts for lengths one through
six are `2,1,2,3,6,9`; the resulting pair counts at lengths one through three
are exactly `4,6,20`.  The canonical result also checks two diagnostic cases:

- `((1,2))` and `((2,1))` are distinct `rho` phases of one
  `sigma`-period-two orbit.
- `((2,2))` is pair-primitive by the odd-period contribution, although its
  flattened digit word `(2,2)` is `sigma`-imprimitive.

The odd/even-swapped counting rule was executed as a negative mutation and
rejected.

## Reversal, stored order, and primitive classes

For a pair word

\[
w=((a_1,a_2),\ldots,(a_{2k-1},a_{2k})),
\]

digit reversal is metadata:

\[
R(w)=((a_{2k},a_{2k-1}),\ldots,(a_2,a_1)).
\]

Objects are quotiented by pair rotation, never by `R`.  The global raw-index
reversal used to rewrite the nested `L_s^{2k}` summation in stored
composition order is a bijection on words.  It intertwines a pair rotation
with a pair rotation in the opposite orientation; hence it descends to cyclic
pair classes and preserves pair primitivity.  This bookkeeping bijection does
not identify a word with its reverse and does not bridge to geodesic
primitivity.

The trace-4 pair `((1,2))`, `((2,1))` is therefore a legitimate pair-ledger
collision, not one factor after an undeclared reversal quotient.  The
trace-6 pair `((1,4))`, `((2,2))` is not reversal-related, and the trace-10
pair `((2,4))`, `((1,1),(1,2))` is additionally cross-pair-length.

## Firewall consequence

No theorem, Route coordinate, Euler factor, or multiplicity claim may move
between `SigmaPrimitiveDigit`, `RhoPrimitivePair`, and
`GeodesicPrimitiveClass` without a separate bridge lemma.  None is supplied
here.  In particular, the two GO codes in the final terminal tuple refer only
to the intrinsic pair ledger and its same-space Mayer determinant; they grant
no primitive-geodesic or rational-prime ledger credit.
