# Addendum: genuinely mixed cycles require `a^2=1`

2026-09-08 UTC, according to the execution clock. This strengthening was
proposed by the coordinator and independently checked, line by line, by
the arithmetic-lane author. It is now supplied for **nonauthor substantive
review**. It does not claim that such review has already accepted it.

The main proof remains byte-for-byte frozen at SHA-256
`66bca7ae41a1fe409e8c7967f5b37e2ce0e1c05ddabf439272a70857bc22aeb3`.
Its six-value necessary condition is correct but weaker than the following
statement. No code, scan, or additional diagnostic supports or is needed
for this addendum.

## Strengthened proposition

Under the full frozen Laurent-family assumptions of `PROOF_PACKAGE.md`,
if an ordinary periodic cycle has nonconstant product of its two
principal-part signs, then

\[
\boxed{a^2=1.}
\]

This is a necessary condition. No assertion that both determinant values
or any particular remaining parameter choices admit such a cycle is made.
For `a` outside `{1,-1}`, the pure-sign C418 reconstruction in the main
proof gives the entire periodic set, including in the monomial-pair case.

## Proof

The main proof first shows that a mixed cycle forces the monomial-pair
case, and derives its exact equations (19). Write

\[
w_i=e_i d_i\in\{1,-1\},\qquad C_w=\frac{\alpha-w\beta}{2}.
\]

Eliminating the offsets as in its equation (20) gives, for every index,

\[
C_{w_i}
=e_{i+1}\mathbf 1_{w_{i+1}\ne w_i}
 +a e_{i-1}\mathbf 1_{w_{i-1}\ne w_i}.                 \tag{A1}
\]

Because the cyclic sign word is mixed, it has well-defined maximal
constant-sign runs, each bordered by the other sign. The quantity `C_w`
is the same at every index with sign `w`, irrespective of its run.

**No run has length at least three.** An interior index of such a run
has both indicators in (A1) zero, so `C_w=0`. Its first index has only
the predecessor indicator nonzero, so `C_w=a e_(i-1)`, which is nonzero
because `a!=0`. This is a contradiction.

**A run of length two forces `a=+1` or `-1`.** At its first index,
(A1) gives `C_w=a e_prev`; at its last index it gives `C_w=e_next`.
Both outside signs `e_prev,e_next` are `+1` or `-1`. Thus
`a=e_next/e_prev` is `+1` or `-1`.

Suppose, to obtain a contradiction, that `a` is neither sign. Every run
must then have length one, so `w` alternates. Formula (A1) becomes

\[
C_{w_i}=e_{i+1}+a e_{i-1}.                              \tag{A2}
\]

The four possible values `+/-1 +/-a` are pairwise distinct: their
nonzero differences, up to sign, are `2`, `2a`, `2(1+a)` and `2(1-a)`.
None vanishes since the field has characteristic not two and
`a` is nonzero and not either sign. Consequently, for all indices of
the same `w_i`, equation (A2) uniquely determines both neighboring
signs `e_(i-1),e_(i+1)` separately. Every occurrence of either sign of
`w` is the successor of the other. It follows that `e_i` is constant
on each `w` class, and hence is two-periodic. So is `d_i=w_i e_i`.

The first equation of (19) determines

\[
b_i=\frac{e_{i+1}+a e_{i-1}-\alpha}{2e_i},
\]

which is likewise two-periodic. Therefore the actual rational coordinate
sequence `y_i=e_i U+d_i V+b_i` has period dividing two.

If its alternating values are `p,q`, subtract their two recurrence
equations to obtain

\[
(p-q)(p+q+a+1)=0.
\]

If `p=q`, uniqueness of the principal-part labels makes their sign
products equal. If `p!=q`, the sum `p+q=-(a+1)` is constant. Since
`U,V,1` are independent, both principal-part signs of `p,q` must be
opposite, so their products again agree. Either case contradicts that
the cycle is mixed. Thus `a in {1,-1}`, proving the proposition.

Every step holds in any characteristic other than two. In particular,
there is no division by three, no characteristic-zero ordering of
coefficients, and no exceptional-prime sample replacing the proof.

## Consequences within the same contract

1. The exact 64-state atlas in the frozen main proof needs genuinely
   mixed components only at `a=1` or `a=-1`; its guards and point labels
   are unchanged.
2. At these two values, the necessary coefficient condition (7) simplifies
   to `(alpha-beta)/2,(alpha+beta)/2 in {-2,-1,0,1,2}` as a set of field
   elements. Small-characteristic coincidences remain included. This
   condition is not presented as sufficient.
3. For the **entire** frozen Laurent family, an ordinary period greater
   than two requires `a^4=1`: the inherited pure-sign rows already have
   this restriction, and a mixed cycle now satisfies the stronger
   `a^2=1`. The one-pole boundary is exactly the inherited theorem.

## Integer adjacency convention

In the main proof's formula (13), all edge guards are evaluated in `k`,
but the resulting adjacency matrix `A` is a matrix over **the integers**:
its entries are the ordinary integers zero and one recording whether an
edge exists. In particular, `tr(A^n)` is an integer point count, not a
trace reduced modulo the characteristic of `k`. The polynomial
`det(I-zA)` lies in `Z[z]`, and its reciprocal zeta identity is interpreted
as a formal power series over `Q` (indeed it has integer coefficients).
This convention applies equally in every positive characteristic covered
by the theorem. It clarifies the counting convention without changing
any graph labels, guards, edges, or mathematical proof bytes.

## Scope and current admission disposition

These consequences do not produce a flattened list of mixed cycle words,
sharp bounds, or irreducible parameter strata. They strengthen the global
compatibility theorem but do not themselves decide paper-level admission.
The addendum belongs to AR2-1, not a second candidate or a separate zeta
contract. The coordinator has judged the complete parameterwise graph
theorem **AUXILIARY_ONLY** after subtraction of C418 and external sources;
the absence of a flattened table is not mislabelled as a mathematical
gap in the stated theorem. This addendum is still to be closed by the
nonauthor reviewer and does not independently alter that disposition.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
