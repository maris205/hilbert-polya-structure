# Experiment Report — SD-C27

## Outcome

The exact suite supports

`(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)`

with `ROUTE_A_REJECTED` and Route B locked. No target-zero or target-root data
were used.

This paper records a genuine A2 advance: the canonical holomorphic de Rham
(0|1) pair cancels the affine fixed-point denominator at every repetition,
and its graded ratio is an exact determinant on (Re s>1). The arithmetic
ceiling is equally exact: shared recurrence retains all mixed return words,
while disjoint recurrence retracts to the supplied countable atom inventory.

## Exact census

| Audit | Result |
|---|---:|
| gamma-code branches | 4,095 |
| scalar power rows | 3,066 |
| ordinary matrix firewalls | 5 |
| de Rham chain/characteristic rows | 40 |
| de Rham power-supertrace rows | 320 |
| local telescoping rows | 20 |
| ordinary/graded ownership rows | 20 |
| shared/disjoint determinant rows | 21 |
| shared/disjoint power rows | 168 |
| primitive necklace rows | 1,183 |
| mixed primitive survivors | 1,174 |
| arbitrary inventory rows | 42 |
| marker rows | 4,095 |
| nuclearity/cohomology rows | 21 |
| tests | 53/53 PASS |

Every gamma branch has exact derivative (q_n=2^{-\ell(n)}), satisfies the
common compact-containment bound, and is produced by a source compiler that
does not import the post-freeze inventory evaluator. The 4,096-word registry
including (n=1) has zero prefix collision.

## Scalar and ordinary-matrix firewalls

The scalar choice (alpha=1-q) makes the first normalized trace equal one.
For (r=2), the exact residual is

\[
 \frac{(1-q)^2}{1-q^2}-1=-\frac{2q}{1+q}.
\]

At atom 2, (q=1/8) and the residual is `-2/9`. All 511 first-power rows
match; all 2,555 rows with powers two through six fail exactly.

An ordinary tensor fiber would require

\[
 \det(I-tB)=\frac{1-t}{1-qt},
\]

which has a pole for every frozen (q>0), whereas a trace-class Fredholm
determinant is entire. The five exact controls also show that fitting the
first two moments of a two-dimensional matrix forces a nonzero third-moment
residual.

## Canonical de Rham escape

All 40 finite complexes satisfy (DM_0=M_1D) exactly. For every fixture and
degree,

\[
 \det(I-zL_0)=(1-z\sum_jw_j)\det(I-zL_1).
\]

All 320 power rows independently verify

\[
 \operatorname{Tr}L_0^r-\operatorname{Tr}L_1^r=(\sum_jw_j)^r,
 \qquad 1\le r\le8.
\]

The 20 centered local products telescope exactly to (1-zw). This is a
graded relative determinant. In all 20 ownership controls, the ordinary
ungraded block determinant—product of the two degree determinants—differs
from the graded ratio.

## Shared flooding and disjoint collapse

For identical labels and weights, shared cohomology gives

\[
 D_{\rm sh}(z)=1-z\sum_jw_j,
\]

whereas disjoint cohomology gives

\[
 D_{\rm dis}(z)=\prod_j(1-zw_j).
\]

The 21 determinant rows and 168 power rows use the first four atoms of each
finite inventory fixture and materialize the exact mixed difference from
(r=2) onward. Enumeration through length six yields 1,183 primitive necklaces on
two, three, and four labels; 1,174 are mixed, and every mixed row survives
the de Rham grading in the shared object. The exterior numerator cancels
local stability, not branch combinatorics.

The disjoint object has one (H^0) state per supplied label. All 42 shared
and disjoint full-inventory controls—prime, square, Fibonacci, all integer,
matched random, matched hash, and decidable modular—use the identical compiler,
record exact full-inventory sums and (z=1) products, and receive zero selectivity
credit. The disjoint Euler product is determinant-equivalent to the countable
atom-loop inventory and is labeled `PROVES_TOO_MUCH`.

## Marker and analytic domain

The return variable counts completed code branches. All 4,095 original digit
histories retain degree (u^{\ell(n)}) with (ell(n)>1). Replacing this by
one return marker changes the marked object or declares a countable
whole-codeword alphabet.

Both form degrees are honest trace-class holomorphic transfer operators on
the uniform domain (Re s>1), where the graded ratio is defined. For the
prime inventory, constant cohomology retains eigenvalues (p^{-s}), so
absolute trace-class continuation through (Re s\le1) is unavailable.
Removing constants makes the graded determinant one. Analytic continuation
of (1/\zeta(s)) is not continuation of this Fredholm pair.

## Reproducibility and scope

The canonical runner performs two complete generator, 53-test, and analysis
runs, requires byte-identical snapshots of the 30 code/result artifacts, and
then checks Route schema, scientific predicates, control characters, caches,
and a 32-entry code/result SHA-256 ledger. Provenance starts with a documented
two-stage placeholder.

The result does not classify every signed complex, nontensor nuclear
operator, anisotropic space, or nonlocal orbit weight. It constructs no
functional equation, critical-line mechanism, self-adjoint carrier, RH
implication, or Route-B object.
