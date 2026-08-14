# PROOF PACKAGE — SD-C16

## Notation

Let `M={F_n:n>=1}` with `F_m tensor F_n=F_mn`.  Write `A(M)` for the set of
tensor atoms, `h(F_n)=log n`, and

\[
(f*g)(n)=\sum_{d\mid n}f(d)g(n/d)
\]

for tensor-divisor convolution.  The symbols `mu_tensor` and
`Lambda_tensor` always refer to this tensor-divisor axis.  They are distinct
from the temporal-period Möbius transform used in ordinary orbit counting.

## Theorem 1 — universal valuation classification

For every abelian group `A`, restriction to atoms is a natural bijection

\[
\operatorname{Hom}_{\mathrm{Mon}}(M,A)
\cong\prod_{p\in A(M)}A.
\]

Every monoidal charge has the unique form

\[
q(F_n)=\sum_p v_p(n)q(F_p).
\]

### Proof

Unique tensor factorization gives the displayed formula for every
homomorphism.  Conversely, any assignment on atoms extends by that formula,
is additive under tensor product, and is unique.  Exponentiating in an
abelian character group gives
`chi(F_n)=prod_p chi(F_p)^{v_p(n)}`.

## Corollary 2 — prime-exclusive abelian selector no-go

No abelian monoidal charge can be nonzero on an atom and zero on every
decomposable object.

### Proof

For an atom `p`, composite vanishing gives

\[
2q(F_p)=q(F_{p^2})=0,
\qquad
3q(F_p)=q(F_{p^3})=0.
\]

Subtracting the first relation from the second gives `q(F_p)=0`.  This proof
works in every abelian group, including torsion groups.  In multiplicative
notation, `chi(p)^2=chi(p)^3=1` similarly forces `chi(p)=1`.

The requested blanket composite control is therefore itself inconsistent
with the prime-power repetition ledger required by Route A.

## Theorem 3 — thin divisor cocycles are coboundaries

If `kappa(d,n)` is an abelian cocycle on the thin tensor-divisor category,
then

\[
\kappa(d,n)=b(n)-b(d),\qquad b(n)=\kappa(1,n).
\]

### Proof

The unique chain `1|d|n` and the cocycle law give
`kappa(1,d)+kappa(d,n)=kappa(1,n)`.  Rearrangement proves the claim.
Consequently every induced character twist is diagonal gauge conjugacy and
does not alter a Fredholm determinant.

## Proposition 4 — entropy character dichotomy

A regular real additive charge depending only on entropy is
`q_t(F_n)=t log n`.  Its unitary twist is a vertical parameter translation:

\[
n^{-s}e^{i\theta t\log n}=n^{-(s-i\theta t)}.
\]

If such a charge is integer-valued on every full shift, then `t=0`.

### Proof

Regular additive endomorphisms of the positive entropy semigroup extend
linearly, giving `q_t=t h`.  If `t log 2` and `t log 3` were both nonzero
integers, then `log 2/log 3` would be rational and hence `2^a=3^b` for
nonzero integers `a,b`, contradicting unique factorization.

## Proposition 5 — pure-shuffle rigidity

Any transfer construction natural under isomorphism of the structured
inventory satisfies

\[
L_{\sigma X}=P_\sigma L_XP_\sigma^{-1}
\]

for a presentation relabeling `sigma`.  Traces, determinants, root multisets,
and character-response norms are therefore invariant.  A shuffled list can
collapse only if the shuffle changes the grammar, in which case the test
measures the externally supplied list order rather than tensor arithmetic.

## Theorem 6 — tensor Möbius entropy innovation

Let `mu_tensor` be the convolution inverse of the constant-one function and
define

\[
\Lambda_\otimes=\mu_\otimes*h.
\]

Then

\[
\Lambda_\otimes(p^r)=\log p,
\qquad
\Lambda_\otimes(n)=0
\]

whenever `n` has at least two distinct tensor atoms.

### Proof

Convolution inversion is equivalent to

\[
h(F_n)=\sum_{d\mid n}\Lambda_\otimes(d).
\]

If `n=prod_j p_j^{a_j}`, the prime-power divisors contribute
`sum_j a_j log p_j=log n`.  Setting all mixed-factor terms to zero therefore
solves the recursion.  Induction over divisibility gives uniqueness.

This is the classical identity `mu*log=Lambda` transported to the frozen
tensor monoid; it is not claimed as a new arithmetic identity.

## Theorem 7 — reduced tensor bar determinant

Let the code alphabet consist of all nonempty ordered words
`a=(F_{a_1},...,F_{a_k})` with every `a_j>=2`, and assign weight

\[
(-1)^{k+1}\exp\left(-s\sum_j h(F_{a_j})\right).
\]

Let `sigma_bar` be the real solution of `zeta(sigma_bar)=2`.  For
`Re(s)>sigma_bar`, the edge sum is absolutely convergent and

\[
F_{\mathrm{bar}}(s)
=\frac{\zeta(s)-1}{\zeta(s)}.
\]

On the one-dimensional vertex space,

\[
D_{\mathrm{bar}}(s,z)=1-zF_{\mathrm{bar}}(s),
\qquad
D_{\mathrm{bar}}(s,1)=\zeta(s)^{-1}.
\]

### Proof

Absolute summation over internal word length gives

\[
\sum_{k\ge1}\sum_{a_1,\ldots,a_k\ge2}
\left|(a_1\cdots a_k)^{-s}\right|
=\sum_{k\ge1}B(\Re s)^k,
\]

which converges exactly when `B(Re(s))<1`.  In that domain, Fubini's theorem
and the geometric series yield `F_bar=B/(1+B)`.  The weighted one-vertex
adjacency is scalar, so its Fredholm determinant is `1-zF_bar`.  At `z=1`,
`1-F_bar=1/(1+B)=1/zeta`.

## Theorem 8 — endpoint-first incidence completion

For every `n>=2`,

\[
c(n):=\sum_{k\ge1}\sum_{a_1\cdots a_k=n}(-1)^{k+1}
=-\mu_\otimes(n).
\]

Consequently

\[
F^{\mathrm{inc}}_{\mathrm{bar}}(s)
=-\sum_{n\ge2}\mu_\otimes(n)n^{-s}
\]

is absolutely convergent for `Re(s)>1` and agrees with `F_bar` in their
common domain.

### Proof

The coefficient of `n^{-s}` in
`B-B^2+B^3-...` is the displayed finite ordered-factorization sum.  Formal
Dirichlet-series multiplication gives
`1-(B-B^2+...)=(1+B)^{-1}`.  The coefficient of `(1+B)^{-1}` is the
incidence inverse of the constant-one function, namely `mu_tensor(n)`.
Therefore `c(n)=-mu_tensor(n)` for `n>1`.  Absolute convergence after
endpoint grouping follows from

\[
\sum_{n\ge1}|\mu_\otimes(n)|n^{-\sigma}
=\frac{\zeta(\sigma)}{\zeta(2\sigma)}<\infty
\qquad(\sigma>1).
\]

The proof does not authorize raw word summation below `sigma_bar`.

## Corollary 9 — canonical roof derivative

On `Re(s)>1`,

\[
\frac{d}{ds}\log D_{\mathrm{bar}}(s,1)
=-\frac{\zeta'(s)}{\zeta(s)}
=\sum_{n\ge1}\Lambda_\otimes(n)n^{-s}.
\]

The derivative inserts only the frozen roof.  The tensor Mangoldt
coefficient is a derived endpoint coefficient, not an input potential.

## Proposition 10 — universal inversion and route obstruction

For any countable weighted nonunit inventory with absolutely convergent
partition `B_X`, the same reduced-word grammar gives

\[
F_X=\frac{B_X}{1+B_X},\qquad D_X=\frac1{1+B_X}.
\]

### Proof

The proof of Theorem 7 uses only the ordered-word product rule and geometric
series identity.  It does not use unique factorization, atoms, or the
arithmetic form of the weights.

Thus the determinant is genuine but universally tautological.  It supplies
no arithmetic selectivity, new meromorphic continuation, divisor theorem,
or RH implication.

## Primitive-cycle boundary

For `|zF_bar|<1`, the trace-log

\[
\log D_{\mathrm{bar}}(s,z)
=-\sum_{r\ge1}\frac{z^rF_{\mathrm{bar}}(s)^r}{r}
\]

enumerates repetitions of cyclic necklaces of bar-code edges.  Those
primitive necklaces are not tensor atoms.  Hence the exact determinant
identity does not establish the orbitwise prime correspondence demanded by
strong Route A.

The sign in this trace is an ordinary scalar potential.  Repeating one edge
`a` exactly `r` times contributes
`epsilon(a)^r exp(-rsT(a))`.  This differs from a supertrace on an odd chain
sector, which would retain one fixed negative grading sign for every `r`.
Accordingly, none of the endpoint identities proves a chain contraction or a
homological contractible-pair cancellation.

## Frozen evaluation

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```
