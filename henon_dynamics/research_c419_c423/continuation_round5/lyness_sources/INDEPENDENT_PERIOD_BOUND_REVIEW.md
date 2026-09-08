# Independent internal review: the rational native-period bound

Date: 2026-09-08 UTC. Reviewer: current-team author of the disjoint
integral-strata package, **not** an author of this period-bound proof.

Verdict: **PASS_INTERNAL_AUXILIARY_PROOF_ONLY**. No mandatory mathematical
correction was found in the stated $N\le48$ theorem. The full integral
LY4 classification remains unclosed. This is neither admission nor human
peer review, a global-priority finding, or independent CPU certification.

## Scope and actual access

Read in full:

- [FROZEN_AUXILIARY_SCOPE.md](FROZEN_AUXILIARY_SCOPE.md).
- [PROOF_PACKAGE.md](PROOF_PACKAGE.md), all six proof steps, classical
  input declarations, exceptional-domain clauses and final limitations.

The review specifically checked the plane invariant identity, local
germs, reduced and nonreduced supports, component permutation, singular
points, Galois descent, both normalization genera and the native clock.
It did not substitute the author's outcome summary for these arguments.

The inspected local bytes have these SHA-256 values (integrity identifiers,
not mathematical certificates):

| Input | SHA-256 |
| --- | --- |
| `FROZEN_AUXILIARY_SCOPE.md` | `362e46165c48e067a7f73d6d5ce2ab2a9ee3955f0dbffda90676a0bb5c1ff010` |
| `PROOF_PACKAGE.md` | `828353a22d498568601fb645c8029c0d50300d3b83805f6de72592b0b2a0bc9a` |

For two external inputs, the reviewer also actually opened:

- [Jogia–Roberts–Vivaldi, author PDF](https://web.maths.unsw.edu.au/~jagr/IntegrabilityRS.pdf):
  Theorem 3 and its proof on printed pages 5–6, with the explicit
  coefficient-field restriction on roots of unity. This verifies the
  translation/affine-automorphism alternatives over the given field;
  it does not prove any singular-fiber step in the reviewed package.
- [Gasull–Mañosa–Xarles](https://arxiv.org/html/1004.5511): introduction,
  especially its recall of the rational torsion order list. Only that
  general torsion input was used. Its own two-dimensional Lyness period
  classification was not imported into third-order LY4.

The original long Mazur proof was not read in this review. Mazur's
theorem is a declared standard input, not independently reproved here.
The separate coordinator source-ownership audit is not a substitute for
this proof review and is not certified for exhaustive novelty by it.

## 1. Reduction and ordinary clock

The nonzero, no-$-1$ rational hypotheses make $u=\kappa_0$ nonzero.
The formula
$$x_{2j+1}=(g_j+1)(g_{j+1}+1)/u$$
recovers every omitted coordinate and is injective on the fixed-$u$
even-time states. It therefore justifies conjugacy along the orbit,
not merely a projection that could lose its least period.

For $R(X,Z)=(Z,f(Z)/X)$, the ordinary recurrence gives
$f(g_{j+1})=g_jg_{j+2}\ne0$. This explicitly rules out an orbit on
the identically-zero-$f$ parameter case. No exception is being removed
solely to make the algebraic model nondegenerate.

The least period of $L_a^2$ is exactly $N/\gcd(N,2)$; injectivity of
the reconstruction makes this equal to the least period $m$ of $R$.
Thus the final factor of two is necessary and correctly retained.

## 2. Invariant identity and local curve germs

The quadratic coefficient and constant coefficient of the stated
$B_h(X,Z)$ as a polynomial in $X$ are exactly
$$A(Z)=(Z+1)(Z+u+1),\qquad
C(Z)=(Z+u+1)((u+1)Z+au+1).$$
Their identity $C=Af$ is valid as a rational identity even when
$Z=-u-1$. The proof never divides by that last factor. The middle
coefficient cancels in the displayed quadratic substitution, and the
symmetry of $B_h$ then gives
$$B_h(R(X,Z))=f(Z)B_h(X,Z)/X^2.$$
This is a sufficient hand verification; no symbolic program is needed.

At an orbit point, $X,Z,Z+1,f(Z)$ are all nonzero. At its image the
inverse $R^{-1}(X,Z)=(f(X)/Z,X)$ has nonzero denominator and regular
$f(X)$. Restricting to appropriate open neighborhoods makes both maps
regular inverses. The displayed multiplier is a local unit. Thus the
whole local hypersurface scheme is transported isomorphically; passing
to reduced supports preserves that conclusion.

Consequently reduced singular points cannot become nonsingular points
along an ordinary orbit. A component through such an orbit point also
cannot be contracted there. These conclusions are stronger than a
generic birational assertion and are exactly what the later case split
needs. They do not permit continuation through an excluded zero or
$-1$ coordinate.

## 3. All fibers: genus, components and singularities

The reduced geometric support of a nonzero bihomogeneous polynomial
of bidegree $(2,2)$ has some effective bidegree $(d,e)$ with
$0\le d,e\le2$. Every geometric irreducible component consumes at
least one unit of total bidegree, so $r\le d+e\le4$.

The divisor exact sequence on $\mathbb P^1\times\mathbb P^1$ gives
$p_a=(d-1)(e-1)$, including disconnected reduced supports. The
normalization exact sequence then gives, with the signs as written,
$$\delta=p_a+r-1-\sum_j g_j\le r\le4.$$
For a reduced curve over the algebraic closure in characteristic zero,
every singular point contributes at least one to this normalization
length. Counting geometric singular points by at most four is
therefore justified, including intersections of distinct components,
not only singularities of irreducible components.

For one irreducible component, bidegree zero in a ruling direction
forces a single ruling line. Otherwise both bidegrees are positive and
at most two, and its normalization genus is at most one. A genus-one
component requires bidegree $(2,2)$, leaving no bidegree for another
component. In that case $r=1$ and the same normalization formula
forces $\delta=0$. Thus the genus-one branch really is a smooth,
geometrically irreducible complete fiber. There is no unhandled
singular genus-one normalization in this bidegree.

Taking the reduced support before these calculations is legitimate:
the local isomorphism was proved for the original scheme and hence
also for its reduction. Multiplicities of a nonreduced fiber cannot
create extra orbit states on its support. No generic-fiber hypothesis
has been used in this argument.

## 4. Rational automorphism bounds

The genus-zero argument separates scalar matrices, nontrivial Jordan
blocks and two distinct eigenvalues. For a periodic non-eigenline,
the eigenvalue ratio must have the same finite order as the point.
Its sum with its inverse is both rational and an algebraic integer
in $[-2,2]$, leaving the stated orders $1,2,3,4,6$. This proof is
valid over $\mathbb Q$ and does not assume real eigenvalues.

In genus one, the rational normalization point supplies a rational
zero. A rational curve automorphism is a translation by a rational
point followed by a rational group automorphism. The reviewed source
allows the extra group automorphisms only when their required roots
of unity lie in the coefficient field; over $\mathbb Q$ only $+1$
and $-1$ survive. The negative-sign affine map squares to the identity.
In the translation case periodicity of a point forces the translating
rational point to be torsion, and its exact order is the period.
Mazur's declared input then gives at most twelve. No unjustified
assertion of pure translation on every specialized fiber is needed.

## 5. Component descent and exhaustion of the orbit cases

If the starting point is singular, the local-germ result makes every
orbit point singular, so the four-point bound directly gives $m\le4$.

At a nonsingular rational point there is a unique geometric component.
Galois fixes the point and permutes components, so it must preserve
that unique component. Its descent to $\mathbb Q$ is therefore
justified. Normalization is an isomorphism near this smooth point;
the lift is rational, rather than merely a point over an unspecified
extension field.

The local isomorphism gives a nonempty open part of each visited
component on which $R$ and its inverse are defined. This promotes the
local transport to a birational map of the components, not a separate
pointwise choice. A periodic orbit thus induces a component cycle of
length $r_0\le r\le4$, with $r_0\mid m$. The return map on the chosen
component and its normalization is defined over $\mathbb Q$.

All orbit points under consideration are smooth, so normalization
does not identify two of them. The return-period computation
$s=m/r_0$ is consequently exact. Genus zero gives $m\le4\cdot6=24$.
Genus one forces $r_0=1$ and gives $m\le12$. Restoring the native
clock yields $N\le48$ in every allowed case. No parameter or reduced
fiber type is omitted by this final split.

## Decision, limits and execution receipt

Required mathematical fixes: **none found in this bounded review**.
The auxiliary theorem survives with its original rational domain and
native period bound unchanged. No claim of optimality is justified or
needed. It remains a classical-structure consequence, not a new
independent research contract.

The theorem does not prove the integral exhaustion E from the other
lane, does not parametrize higher-period integral torsion strata, and
does not close LY4. Passing this proof review cannot be counted as a
fourth admission, a formal Route-A evaluation, or target-arithmetic
progress.

No mathematical program was run or imported. No old calculation or
finite census was rerun. Actual actions were full document reads,
the two bounded primary-source openings with a theorem-locator read,
and a read-only `sha256sum` of the two local reviewed inputs. One
initial read used a nonexistent guessed freeze filename; it failed,
was corrected to the linked `FROZEN_AUXILIARY_SCOPE.md`, and supplies
no evidence about the mathematical claim. This review file alone was
authored under the coordinator's explicit expanded review-path
assignment; the author's proof and frozen scope were not edited.

The proof-writer rigor checks governed the explicit hypotheses,
degenerate cases and claim boundary. Current-team internal review is
not human peer review, and `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
