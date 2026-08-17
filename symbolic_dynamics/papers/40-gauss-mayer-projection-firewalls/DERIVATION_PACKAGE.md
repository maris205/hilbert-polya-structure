# Derivation package

Status: `POST_CANONICAL_DEPENDENT_RENDERING`
Candidate: `SD-C42`
Source lock: `2269e06576dd20c513c5ca9482cb49d36678e07358aaf80f2f08b33806b87041`
Mayer boundary: `a9dcbc922f8c47b0b845e7c6e76422aad3a0e744940a6529c2172176f5725bc5`
Control lock: `f19edfa13b4f4cd9511394563fc2d7f7d9c428e477ae39e1d248a821e86850d8`
Canonical control: `d0be9630e4f0710c1f602e14e517939f6eef21c582934d79f795a9871f45a30f`
Canonical prototype: `2fee7701a08ec4f7e019863c6e86bf6fb884bf0323e5593e4bf946ef35e7a995`

This package is a mathematical rendering produced after the canonical
replacement run.  The only pre-run freeze is the exact corrected-input set in
`CONTROL_LOCK.md`.  Provisional v1 results and in-flight corrective smoke
outputs were known during M1--M20; no prospective or novelty credit is
claimed here.

## 1. Typed source object

Let `X=N^N` carry the digit shift `sigma`; let
`X2=(N^2)^N` carry the one-pair shift `rho`.  Group consecutive digits by

\[
\iota(a_1,a_2,a_3,a_4,\ldots)
=((a_1,a_2),(a_3,a_4),\ldots).
\]

Then `rho iota=iota sigma^2`.  A source object is a cyclic ordered-pair word

\[
w=((a_1,a_2),\ldots,(a_{2k-1},a_{2k}))
\]

primitive under `rho`, quotienting only cyclic pair rotations.  The P40 pair
ledger is newly derived from this return map.  It is not inherited from the
SD-C04 digit-primitive ledger and is not identified with a primitive
geodesic class.

For a digit alphabet of size `D`, a least-period-`n` digit orbit produces
`gcd(n,2)` pair-return cycles of length `n/gcd(n,2)`.  Hence

\[
N_{D^2}(k)=2N_D(2k)+\mathbf1_{k\text{ odd}}N_D(k).
\]

This derives the checked `D=2` pair census `4,6,20` at lengths `1,2,3`.

## 2. Monodromy and exact repetition

Define

\[
A(a)=\begin{pmatrix}a&1\\1&0\end{pmatrix},\qquad
M(w)=A(a_1)\cdots A(a_{2k}).
\]

Because each digit matrix has determinant `-1` and there are `2k` digits,

\[
\det M(w)=1.
\]

All entries are positive, so `t=tr M>=3`.  Concatenating `r` copies gives

\[
M(w^r)=M(w)^r.
\]

Let

\[
\Delta=\Delta_{\mathbb Z[M]}=t^2-4,
\qquad
\lambda_+=\frac{t+\sqrt\Delta}{2}>1.
\]

This `Delta` is the characteristic/order discriminant of `Z[M]`; it is not a
field fundamental discriminant or the discriminant of a larger multiplier
ring.  The exact clock is

\[
T(w)=2\log\lambda_+,qquad T(w^r)=rT(w).
\]

The sole marker `u` counts original digits, so a pair length `k` repeated `r`
times has marker `u^(2kr)`.

## 3. Gauss branch, matrix, and raw-operator order

For `phi_a(z)=1/(a+z)`, set

\[
B(a)=\begin{pmatrix}0&1\\1&a\end{pmatrix},\qquad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Direct multiplication gives `A(a)=JB(a)J`, and therefore

\[
B_w=B(a_1)\cdots B(a_{2k}),\qquad M(w)=JB_wJ.
\]

The same ordered product represents
`Phi_w=phi_{a1} o ... o phi_{a2k}`.  At its attracting fixed point `x_w`, if
`B_w=[[alpha,beta],[gamma,delta]]`, then

\[
\gamma x_w^2+(\delta-\alpha)x_w-\beta=0,
\quad \gamma x_w+\delta=\lambda_+,
\quad |\Phi'_w(x_w)|=\lambda_+^{-2}.
\]

Thus the matrix clock and branch roof agree:

\[
-\log|\Phi'_w(x_w)|=2\log\lambda_+=T(w).
\]

The expanding eigenvalue has polynomial `x^2-tx+1`.  In contrast, both
`P_N=lambda_+^2` and the derivative multiplier `d=lambda_+^-2` have

\[
x^2-(t^2-2)x+1,
\]

with root selectors `P_N>1`, `0<d<1`, and `P_N d=1`.  Explicitly,

\[
P_N=\frac{t^2-2+t\sqrt\Delta}{2},\qquad
d=\frac{t^2-2-t\sqrt\Delta}{2}.
\]

The transfer operator

\[
(\mathcal L_s f)(z)=\sum_{a\ge1}(a+z)^{-2s}f(\phi_a z)
\]

obeys

\[
\mathcal L_s^2 f(z)=\sum_{a,b}j_{a,s}(z)j_{b,s}(\phi_a z)
 f(\phi_b\circ\phi_a z).
\]

Therefore stored composition order `(b,a)` is the reverse of raw dummy order
`(a,b)`.  For `K_s=L_s^2` and a stored length-`2k` word, globally reverse all
raw indices.  The direct nested product is then

\[
G_{w,s}(z)=j_{a_{2k},s}(z)
j_{a_{2k-1},s}(\phi_{a_{2k}}z)\cdots
j_{a_1,s}(\phi_{a_2}\circ\cdots\circ\phi_{a_{2k}}z).
\]

For complex `z` and `s`, this product is the definition: every factor
`(a+z)^(-2s)` uses Mayer's fixed holomorphic logarithm branch.  Equivalently
it is the corresponding holomorphic branch of `(Phi'_w(z))^s` for an even
word.  No absolute value is used to define the complex operator.  Only on the
positive real branch does it equal `|Phi'_w(z)|^s`.  With this convention,

\[
K_s^k f(z)=\sum_{w\in\mathbb N^{2k}}G_{w,s}(z)f(\Phi_w z).
\]

The non-palindromic exact fixture `w=(1,2,2,3,1,4)`, `z=1/4`, `s=1`
gives `442/623` and `16/388129` with reversal, but `146/697` and
`16/485809` with the wrong same-index raw order.  The canonical reference and
independent implementations obtain these values from direct nested
fractions, not from a pre-reversed matrix derivative.

## 4. The exactly three scalar projections

The frozen family is

\[
P_t=t,\qquad P_\Delta=t^2-4,\qquad P_N=\lambda_+^2.
\]

No fourth projection is admitted.

### 4.1 Order-discriminant firewall

Since

\[
\Delta=(t-2)(t+2),
\]

both factors exceed one for `t>3`; at `t=3`, `Delta=5`.  Therefore
`Delta` is a rational prime exactly at the boundary `t=3`.  Also

\[
(t-1)^2<t^2-4<t^2
\]

for `t>=3`, so `Delta` is not a square.  The polynomial of `P_N` is
`x^2-(t^2-2)x+1`, whose discriminant is
`t^2(t^2-4)=t^2 Delta`.  This is nonsquare because `Delta` is nonsquare.
Consequently `P_N` is irrational and cannot be a rational prime or rational
prime power.

### 4.2 Clock firewall

For `t>=3`,

\[
t^2-4>(t-2)^2
\]

because their difference is `4t-8>0`.  Thus

\[
\lambda_+=\frac{t+\sqrt{t^2-4}}2>t-1,
\qquad
\lambda_+^2>(t-1)^2\ge t.
\]

Hence
`T=log P_N>log t`; trace does not carry the source clock.  Every `t>=3` is
realized by the one-pair word `((1,t-2))`, whose matrix is

\[
\begin{pmatrix}t-1&1\\t-2&1\end{pmatrix}.
\]

Moreover `lambda_+(t)=t+O(t^-1)`, so

\[
\frac{\log\lambda_+(t)^2}{\log t}\longrightarrow2.
\]

If a constant `c` made `c log t=log lambda_+(t)^2` for all realized traces,
the limit would force `c=2`; but `lambda_+(t)^2<t^2` for finite `t` because
`lambda_+(t)<t`.  Contradiction.  This is an all-trace argument, not an
inference from the finite prototype.

### 4.3 Repetition firewall

By Cayley--Hamilton, for `q_r=tr(M^r)`,

\[
q_0=2,\quad q_1=t,\quad q_r=tq_{r-1}-q_{r-2}.
\]

In particular `q_2=t^2-2`, so `P_t(w^2)!=P_t(w)^2`.  Likewise

\[
P_\Delta(w^2)=q_2^2-4=t^2(t^2-4)=t^2P_\Delta(w)
\ne P_\Delta(w)^2.
\]

By contrast, `P_N(w^r)=P_N(w)^r` and `T=log P_N` exactly.  The norm
projection passes clock and temporal powers but fails rational-integer and
rational-prime support.

## 5. Determinant comparison and amplitude

On the exact Mayer function space and nuclear domain specified in
`MAYER_SOURCE_BOUNDARY.md`, define

\[
D_{42}(s,u)=\det(I-u^2K_s).
\]

Nuclear Fredholm theory gives, coefficientwise as a formal series in `u^2`
and analytically for sufficiently small `|u|`,

\[
-\log D_{42}(s,u)
=\sum_{n\ge1}\frac{u^{2n}}n\operatorname{Tr}(K_s^n).
\]

The raw-index reversal from Section 3 is a bijection compatible with cyclic
pair classes and repetitions, so each trace may be indexed by stored ordered
pair words.  The one-dimensional holomorphic weighted-composition trace for
one such word is

\[
\frac{d_w^s}{1-d_w},
\]

where `d_w=|Phi'_w(x_w)|` is evaluated at its positive real attracting fixed
point; the complex weight itself remains on Mayer's fixed holomorphic branch.
If a primitive pair necklace `v` has pair length `k` and is repeated `r`
times, then `n=kr`, `d_(v^r)=d_v^r`, and its `k` cyclic representatives
contribute equally.  The cyclic multiplicity cancels the `n=kr` denominator:

\[
-\log D_{42}(s,u)
=\sum_{[v]\ \mathrm{rho\mbox{-}primitive}}
 \sum_{r\ge1}
 \frac{u^{2kr}d_v^{rs}}{r(1-d_v^r)}.
\]

This is an intrinsic pair-trace regrouping for `K_s`, not a consequence of an
objectwise pair/geodesic bijection.  In the same coefficientwise/local sense,
expanding
`(1-d_v^r)^(-1)=sum_(j>=0)d_v^(jr)` and exponentiating gives

\[
D_{42}(s,u)^{-1}
=\prod_{[v]}\prod_{j\ge0}(1-u^{2k}d_v^{s+j})^{-1}.
\]

No single-valued logarithm or primitive product is asserted across determinant
zeros or for arbitrary `u`.  The specialization `u=1` uses only Mayer's
separately sourced Selberg-zeta/Fredholm identity and continuation, not the
local logarithmic series.  In the local/formal comparison, a primitive
pair word of pair length `k` contributes

\[
\prod_{j\ge0}(1-u^{2k}d_w^{s+j})^{-1},
\]

so its repetition-`r` coefficient in `-log D_42` is

\[
\frac{u^{2kr}d_w^{rs}}{r(1-d_w^r)}.
\]

A hypothetical rational-prime factor with the same digit marker would be

\[
(1-u^{2k(w_p)}p^{-s})^{-1},
\]

with coefficient `u^(2kr)p^(-rs)/r`.  The source stability denominator and
Selberg tower do not disappear under the formal assignment `p=P_N`.  Thus an
exact ledger match must preserve support, one-to-one target multiplicity,
temporal powers, clock, marker, amplitude, sign, orientation, phase, and an
operator-owned trace.  A scalar coincidence alone is insufficient.

## 6. Projection truth matrix and existential decision

| Projection | Integer-valued | Prime support | One-to-one | Powers | Clock | Target amplitude | Declared selected owner |
|---|---:|---:|---:|---:|---:|---:|---:|
| `P_t` | pass | fail | fail | fail | fail | fail | fail |
| `P_Delta` | pass | fail | fail | fail | fail | fail | fail |
| `P_N` | fail | fail | fail | pass | pass | fail | fail |

The trace-4, trace-6, and trace-10 witnesses establish duplicate primitive
species for every projection because all three are functions of `t`.  The
trace-4 object also supplies a composite full-ledger trace.  The exact
existential predicate

\[
\bigvee_{P\in\{P_t,P_\Delta,P_N\}}\operatorname{ProjectionGO}(P)
\]

is false because each row has a failed conjunct.  This collective coverage,
not any one witness in isolation, proves
`STOP_CANONICAL_INTEGER_PROJECTION`.

Separately, among integer-valued projections, neither `P_t` nor `P_Delta`
passes both clock and powers, whereas the only projection that passes both,
`P_N`, is irrational.  This proves the narrowly named
`STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION`; it does not claim that
all projections fail clock or repetition.

## 7. Operator ownership and controls

The full intrinsic pair ledger is owned by `K_s=L_s^2`, yielding
`GO_MODULAR_PRIMITIVE_LEDGER` and
`GO_SAME_OBJECT_MAYER_DETERMINANT`.  None of the three scalar selectors is a
declared reducing projector in the frozen untwisted schema.  The exact toy
matrices `K=diag(2,3)` and `P=diag(1,0)` demonstrate what a valid owned sector
would require: idempotence, commutation, compatible dimension, all frozen
power traces, multiplicity, and marker support.  All associated mutations
are rejected.

Seven A0 and six A1 controls execute as literal records.  Five out-of-contract
countermodels delimit the conclusion: odd determinant-minus-one words, a
prime-indexed direct sum, separate roof and marker changes, scalar
postselection, and a finite directed cycle.  Therefore the ownership verdict
is contract-relative:

`STOP_OPERATOR_VISIBLE_SELECTOR_NOT_OWNED`.

## 8. Derived terminal tuple

The exact post-run consequence is

```text
GO_MODULAR_PRIMITIVE_LEDGER
GO_SAME_OBJECT_MAYER_DETERMINANT
STOP_CANONICAL_INTEGER_PROJECTION
STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION
STOP_OPERATOR_VISIBLE_SELECTOR_NOT_OWNED
ROUTE_A_REJECTED
```

The GO entries concern only the intrinsic pair system and its same-object
Mayer determinant.  Route B remains forbidden.  Nothing here asserts a new
Mayer mechanism, witness priority, universal selector nonexistence, a
pair/geodesic bijection, or a rational-prime Euler ledger.
