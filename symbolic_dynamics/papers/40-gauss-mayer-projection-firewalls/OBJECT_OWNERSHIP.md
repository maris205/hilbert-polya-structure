# Typed object--marker--operator ownership ledger

Status: `POST_CANONICAL_DEPENDENT_RENDERING`
Candidate: `SD-C42`
Source lock: `2269e06576dd20c513c5ca9482cb49d36678e07358aaf80f2f08b33806b87041`
Control result: `d0be9630e4f0710c1f602e14e517939f6eef21c582934d79f795a9871f45a30f`

This ledger is rendered after the canonical replacement run.  It records
what the hash-frozen schema declares and what the executable controls verify;
it is not a universal classification of all twisted transfer operators.

## Ownership table

| Entity | Type and owner | Marker / repetition | Exact status |
|---|---|---|---|
| Digit space | `X=N^N`, one-digit shift `sigma` | one digit carries `u` | inherited Gauss source object |
| Pair space | `X2=(N^2)^N`, one-pair shift `rho` | one pair carries `u^2` | P40 typed refinement, with `rho iota=iota sigma^2` |
| Primitive object | cyclic `RhoPrimitivePair`, rotation quotient only | pair length `k`; repetition `r` has `u^(2kr)` | complete intrinsic pair ledger |
| Monodromy | `M(w)=A(a1)...A(a2k)` | `M(w^r)=M(w)^r` | same stored word and repetition |
| Clock | `T(w)=2 log lambda_+(M(w))` | `T(w^r)=rT(w)` | equals the branch derivative roof |
| Operator | `K_s=L_s^2` on Mayer's stated holomorphic Banach space | `K_s^k` uses the globally reversed raw dummy indices | same-object branch expansion proved |
| Marked determinant | `D_42(s,u)=det(I-u^2 K_s)` | local/formal source log coefficient `u^(2kr)d_w^(rs)/(r(1-d_w^r))` | Fredholm family in the nuclear domain; logarithm only near `u=0` |
| Trace projection | scalar `P_t=t(w)` | does not preserve temporal powers | label only; no declared selected operator |
| Order-discriminant projection | scalar `P_Delta=t(w)^2-4` | does not preserve temporal powers | label only; no declared selected operator |
| Norm projection | scalar `P_N=lambda_+^2` | preserves clock and powers, but is irrational | label only; no declared selected operator |
| Rational-prime target | hypothetical factor `(1-u^(2k)p^(-s))^(-1)` | coefficient `u^(2kr)p^(-rs)/r` | comparison target, not a source-owned determinant |

The scalar projections are diagnostics on primitive rows.  A predicate such
as “the scalar is prime” is not an idempotent projector on the function
space, and deleting rows of a Fredholm expansion does not by itself construct
a Fredholm determinant.

## Exact state-transition rule

An ownership claim is accepted only when a declared record supplies an
operator matrix `K`, a projector `P`, a common space dimension, selected
indices, multiplicity, and marker stride, and direct computation verifies

\[
P^2=P,\qquad PK=KP,\qquad
\operatorname{Tr}(PK^r)=\operatorname{Tr}((K|_{\mathrm{ran}P})^r)
\]

at every frozen repetition, with the same multiplicity and determinant-marker
degrees.  Strings such as “commutes,” a prefilled boolean, or a filtered
scalar inventory are not evidence.

The positive toy owner uses

\[
K=\begin{pmatrix}2&0\\0&3\end{pmatrix},\qquad
P=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

The canonical evaluator computes `P^2=P`, `PK=KP`, the six traces
`2,4,8,16,32,64`, multiplicity one, and marker degrees `{0,2}` for the
selected determinant.  The full-ledger projector `I` produces traces
`5,13,35,97,275,793` and marker degrees `{0,2,4}`.  Separate mutations break
idempotence, commutation, dimension, multiplicity, power traces, and marker
support; every mutation is rejected by the reference and independent paths.

## Scalar postselection audit

The frozen scalar fixture has full inventory `{3,4}`.  Applying the computed
prime predicate gives `{3}` and difference `{4}`.  These three inventories
and their multiplicities are computed and mutation-tested, but the frozen
untwisted schema has `declared_projector: null`.  Therefore the precise
conclusion is:

> No rational-prime scalar selector is declared to own a reducing sector of
> the frozen untwisted `K_s` schema.

This is a hash-backed absence-of-declaration statement.  It is not a theorem
that no twist, extension, vector-valued space, or future operator could own a
prime-indexed sector.  The prime-loop direct-sum control demonstrates why the
scope matters: a different operator may be built with a prime-indexed basis,
but that is a different source object.

## Determinant and target-amplitude boundary

Coefficientwise/formally in `u^2`, or analytically for sufficiently small
`|u|`, the same-object reciprocal determinant contributes

\[
\frac{u^{2kr}d_w^{rs}}{r(1-d_w^r)},\qquad d_w=\lambda_+(w)^{-2},
\]

where the stability denominator is part of the Mayer/Selberg tower.  The
hypothetical rational-prime factor contributes

\[
\frac{u^{2kr}p^{-rs}}r.
\]

Even the formal assignment `p=lambda_+^2` leaves the source denominator
`1/(1-d_w^r)`.  Marker, sign, multiplicity, orientation, phase, repetition,
clock, and amplitude must all be owned by one operator sector; agreement of a
single scalar label cannot earn ownership credit.  No local logarithm or
primitive product is continued through determinant zeros; the `u=1` function
identity comes only from Mayer's separately sourced theorem.

## Final ownership verdict

- `GO_SAME_OBJECT_MAYER_DETERMINANT` is justified for the full intrinsic
  `RhoPrimitivePair` ledger of `K_s=L_s^2`.
- `STOP_OPERATOR_VISIBLE_SELECTOR_NOT_OWNED` is justified for all three
  frozen scalar projections in the untwisted contract.
- No claim is made about universal nonexistence across operator twists or
  about an objectwise pair-to-geodesic bijection.
