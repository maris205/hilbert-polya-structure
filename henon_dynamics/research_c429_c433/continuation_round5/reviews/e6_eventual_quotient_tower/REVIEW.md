# R5 E6: eventual native quotient tower

2026-09-09 UTC. Independent current-team, nonauthor actual-file review of
the separately allocated A3/R5 bridge. All R3/R4 proofs and reviews remain
frozen. This is the only new workspace file written for this allocation.

## Verdict and exact accepted claim

**PASS: zero mathematical must-fixes and zero source-applicability
must-fixes.**

The complete [proof package](../../a3_eventual_quotient_tower/PROOF_PACKAGE.md)
and [report](../../a3_eventual_quotient_tower/REPORT.md) establish the stated
eventual quotient theorem, relative to the named A1 and D1 inputs, which the
coordinator has now fully read and accepted. Their creation-time conditional
labels do not leave an additional mathematical premise open in this review.

For each odd prime $p$, set $K_0=\overline{\mathbb F}_p((s))$ and retain the
original map $P_s(z)=(1+s)z+z^2$. In one fixed separable closure, the
canonical small-cycle fields $L_e/K_0$ have native characters
$\rho_e:G_{K_0}\to\mathbb Z/p^e\mathbb Z$. There is a unique continuous
surjective character $\chi_\infty:G_{K_0}\to\mathbb Z_p$ satisfying

$$
\forall j\ge1\ \exists E_j\ge j\ \forall e\ge E_j\ \forall g\in G_{K_0}:
\qquad
\rho_e(g)\bmod p^j=\chi_\infty(g)\bmod p^j.
\tag{R1}
$$

The equality is simultaneous on the whole absolute Galois group and on
every sufficiently late level. It is stronger than pointwise convergence
with a threshold depending on $g$, or stabilization along a subsequence.

The kernels define actual nested fields $K_j\subset K_0^{\mathrm{sep}}$ of
degrees $p^j$, with $K_j$ equal to the unique degree-$p^j$ subfield of $L_e$
for all $e\ge E_j$. Their union is a Galois $\mathbb Z_p$-extension with
the quotient map induced by $\chi_\infty$.

This does not assert $E_j=j$, $K_j=L_j$, nesting of all $L_e$, or eventual
containment of a prescribed full field $L_j$ in every later $L_e$.
It is a bridge within the existing integrated local contract, not a
separate paper-admission decision or a global PC424-D result.

## 1. Actual interfaces and application to the completed algebraic closure

The A1
[all-anchor proof](../../../continuation_round4/a1_optimal_cycle_measures/PROOF_PACKAGE.md)
was read, including its exact finite identity (MC2), general-field
specialization, nonzero multiplier denominator, and divergent contact
bound. Its final
[E2 review](../../../continuation_round4/reviews/e2_optimal_measure_contacts/REVIEW.md)
was also read. This input applies to every complete algebraically closed
ultrametric field of characteristic $p$ and every multiplier $1+s$ with
$0<|s|<1$, so it applies to the completion $\mathcal C$ chosen in A3.

The actual D1
[compact-limit proof](../../../continuation_round4/d1_isometric_cycle_limit/PROOF_PACKAGE.md),
including its direct aperiodicity argument, and its complete
[E1 review](../../../continuation_round4/reviews/e1_isometric_cycle_limit/REVIEW.md)
were inspected. The needed application is the classical metric one:

$$
S=\bigcup_{e\ge1}\Pi_e,\qquad C=\overline S^{\,\mathcal C},
\qquad
\Omega=\bigcap_N\overline{\bigcup_{e\ge N}\Pi_e}^{\,C}.
$$

The all-anchor identity supplies a close pair for each higher level, with
a uniform absolute-distance bound tending to zero. D1 gives compact
$C$, nonempty compact $\Omega$, full-sequence Hausdorff convergence
$\Pi_e\to\Omega$, and $P(\Omega)=\Omega$.

There is no missing local-compactness hypothesis. The disk
$|z|\le R=|s|^{(p-1)/p}<1$ is complete, and

$$
P(x)-P(y)=(x-y)(1+s+x+y),\qquad |1+s+x+y|=1
\tag{R2}
$$

makes it an invariant isometric disk. Compactness of the particular
cycle closure is proved by the imported contact criterion, not assumed
for that whole disk or for a Berkovich compactification.

The infinite, rather than finite, odometer alternative is also an accepted
output with verified hypotheses. D1 uses the exact finite contact average
to separate each old cycle from all sufficiently high cycles. This
excludes finite limits of period $p^k$ for $k\ge1$. A singleton limit
would be fixed by $P$, but the fixed points $0,-s$ are off the common
closed sphere of radius $R$. Thus the supplied native conjugacy is

$$
h:\Omega\xrightarrow{\sim}\mathbb Z_p,\qquad h(Px)=h(x)+1.
\tag{R3}
$$

No extra periodic-point isolation theorem or full-field nesting is needed.
The R3 full local inertia and first-oriented-quotient theorems remain
accepted inputs. The R4 conductor and second-layer break formulas are
unnecessary to this new argument.

## 2. Algebraic closure and individual Galois isometries

The base $K_0$ is complete for its nontrivial $s$-adic absolute value.
Its valuation extends uniquely to an algebraic closure. The completion
of that closure is algebraically closed as well as complete. These are
exactly the hypotheses of
[Conrad, Introduction and Theorem 1.1](https://math.stanford.edu/~conrad/248APage/handouts/algclosurecomp.pdf);
the result is not restricted to characteristic zero or finite residue
fields. The handout also states the extension of algebraic isometries
to the completion. Its separate characteristic-zero fixed-field theorem
is not used here.

The separable closure is not silently identified with an algebraic
closure in characteristic $p$. For every algebraic element $a$, some
$a^{p^n}$ is separable over $K_0$. Its image under a given
$g\in G_{K_0}$ uniquely determines the image of $a$, because purely
inseparable roots are unique. This gives the asserted unique extension
of $g$ to the chosen algebraic closure.

Uniqueness of the valuation makes this extension an isometry, and
completion extends it to an isometric field automorphism of $\mathcal C$.
The inverse is the extension of $g^{-1}$; composition agrees with the
group law by uniqueness. Because $P$ has coefficients in $K_0$, these
actions commute with $P$ on the dense algebraic field and on the completion.

Every $\Pi_e$ is Galois-stable. Applying $g$ and $g^{-1}$ to the union,
its closure and each tail closure therefore proves that $C$ and $\Omega$
are preserved as sets. This yields individual isometries of the compact
limit, but the proof correctly treats continuity in $g$ as a further step.

## 3. Joint Galois continuity from algebraic finite nets

Fix $\varepsilon>0$. Since $C$ is compact and $S$ is dense, finitely many
points $a_1,\ldots,a_m\in S$ give a strict $\varepsilon$-net for all of
$C$. Each point lies in a finite separable extension. Its stabilizer is
open in the profinite group $G=G_{K_0}$, and their finite intersection
$U_\varepsilon$ is an open subgroup.

For $u\in U_\varepsilon$ and any $x\in C$, choose a net point with
$|x-a_i|<\varepsilon$. The ultrametric inequality and isometry give

$$
|ux-x|
\le\max\{|ux-u a_i|,\ |u a_i-a_i|,\ |a_i-x|\}
=|x-a_i|<\varepsilon.
\tag{R4}
$$

Thus one neighborhood of the identity moves every point of $C$ by
less than $\varepsilon$. This proves uniform control over nonalgebraic
limit points, not only continuity on the dense algebraic subset.

For a general pair $(g_0,x_0)$, take $g=g_0u$ with
$u\in U_\varepsilon$ and $|x-x_0|<\varepsilon$. Then

$$
|gx-g_0x_0|=|ux-x_0|
\le\max\{|ux-x|,\ |x-x_0|\}<\varepsilon.
$$

This is a neighborhood proof of joint continuity of $G\times C\to C$.
It does not require $G$ to be metrizable or replace its topology by a
sequential surrogate. Its restriction gives continuous orbit maps on
$\Omega$.

## 4. Translation character, uniqueness of phase, and native orientation

For $g\in G$, the continuous map $f_g=hgh^{-1}$ commutes with addition by
one. A continuous map $f:\mathbb Z_p\to\mathbb Z_p$ with
$f(z+1)=f(z)+1$ satisfies $f(m)=f(0)+m$ for all nonnegative integers.
These integers are dense, so

$$
f(z)=f(0)+z\qquad(z\in\mathbb Z_p).
$$

Consequently

$$
h(gx)=h(x)+\chi_\infty(g)
\tag{R5}
$$

defines a unique translation amount for each $g$, independent of $x$.
Composition gives the additive homomorphism law. Evaluating (R5) at any
fixed $\omega_0\in\Omega$ and using Section 3 proves continuity of
$\chi_\infty$.

If $h'$ is another conjugacy satisfying the same native equation (R3),
then $h'h^{-1}$ is itself a translation by the same dense-integer
argument. Conjugating translations by that map does not change their
amounts. Changing the origin therefore has no effect on $\chi_\infty$.
A multiplication by a unit would change native increment $1$ to that
unit and is allowed only for the unit $1$. No sign or scalar ambiguity
survives at any quotient depth.

The finite characters $\rho_e$ likewise use the original one-step map.
Commutation with $P$ makes their index independent of the starting root,
and composition adds indices. Full local inertia supplies their
surjectivity; finite Galois factorization supplies their continuity.

## 5. Every quotient size exists, including skipped metric sizes

For fixed $j\ge1$, put $q_j=h\bmod p^j$. This is a continuous surjection
onto $\mathbb Z/p^j\mathbb Z$, with $p^j$ compact clopen fibers, and

$$
q_j(Px)=q_j(x)+1,\qquad
q_j(gx)=q_j(x)+\chi_\infty(g)\bmod p^j.
\tag{R6}
$$

D1's metric partitions may have lengths $p^{k_m}$ with some integers
omitted. This causes no gap: unbounded nondecreasing $k_m$ are cofinal,
so choose $k_m\ge j$ and reduce its native cyclic labels modulo $p^j$.
With the phase chosen consistently with $h$, this gives precisely $q_j$.
Any phase shift changes labels only by a constant and does not affect
the fiber partition or character increments. A mod-$p^j$ fiber may be a union of
metric cells; it need not occur as a single chosen-radius class.

Alternatively, (R3) directly constructs $q_j$ for every $j$ without
reference to that chosen sequence of metric partitions. The proof's
finite-quotient transfer needs only these compact clopen fibers.

## 6. Hausdorff transfer is well-defined and uniform in the whole group

Distinct fibers of $q_j$ have strictly positive mutual distance:
the distance function attains a minimum on their compact product, and
a zero minimum would give a common point. There are finitely many
fiber pairs. Choose $\delta_j>0$ no larger than their minimum separation.
Then

$$
x,y\in\Omega,\quad |x-y|<\delta_j
\quad\Longrightarrow\quad q_j(x)=q_j(y).
\tag{R7}
$$

Full-sequence Hausdorff convergence gives $E_j\ge j$ such that
$d_H(\Pi_e,\Omega)<\delta_j$ for every $e\ge E_j$.
For $\alpha\in\Pi_e$, choose any nearby $x\in\Omega$ and define
$q_{e,j}(\alpha)=q_j(x)$. Two choices $x,y$ satisfy
$|x-y|<\delta_j$ by the ultrametric inequality, so (R7) proves
independence of the choice. The reverse directed Hausdorff bound proves
surjectivity onto every label.

Native isometry (R2) and every Galois isometry send a permissible nearby
point to another permissible nearby point. They preserve $\Omega$.
Thus

$$
q_{e,j}(P\alpha)=q_{e,j}(\alpha)+1,\qquad
q_{e,j}(g\alpha)=q_{e,j}(\alpha)+\chi_\infty(g)\bmod p^j.
\tag{R8}
$$

No continuous or globally compatible selection of nearby points is needed:
the label was shown to be independent of each choice before equivariance
was invoked. In particular, $\delta_j$ and $E_j$ do not depend on $g$.

Using $g\alpha=P^{\circ\rho_e(g)}\alpha$ and the first identity in (R8)
computes the second left-hand side instead as
$q_{e,j}(\alpha)+\rho_e(g)\bmod p^j$. A representative of
$\rho_e(g)\in\mathbb Z/p^e\mathbb Z$ gives the same label for every choice
because $e\ge j$. Comparison proves (R1) for all $g$ at once.

The resulting identification is of oriented finite torsors with Galois
action, not merely an equality of their cardinalities or an unoriented
abstract isomorphism of field extensions.

## 7. Surjectivity and the fields inside the separable closure

The continuous image $H=\chi_\infty(G)$ is compact and hence closed in
$\mathbb Z_p$. Taking $j=1$ in (R1) makes its reduction the nonzero,
indeed surjective, native mod-$p$ character of a sufficiently late cycle.
Thus $H$ contains a unit $u$. It contains all integer multiples of $u$,
whose closure is $\mathbb Z_p$; closedness proves $H=\mathbb Z_p$.
Nontriviality alone without the mod-$p$ condition would not have sufficed.

Write $H_j=\ker(\chi_\infty\bmod p^j)$. These are open normal subgroups
of index $p^j$. Algebraic Galois correspondence gives
$K_j=(K_0^{\mathrm{sep}})^{H_j}$, cyclic of degree $p^j$.
Equation (R1) identifies $H_j$ exactly with
$\ker(\rho_e\bmod p^j)$ whenever $e\ge E_j$, so it gives equality
with $L_e^{\langle\sigma_e^{p^j}\rangle}$ inside the fixed closure.

The inclusions $H_{j+1}\subset H_j$ give the nested fields.
Restriction between their finite Galois groups is ordinary reduction,
since all identifications are induced by the same $\chi_\infty$.
Their union is Galois, and its automorphism group is the inverse limit
of these finite cyclic quotients, hence $\mathbb Z_p$. The restriction
map from $G$ has kernel $\bigcap_jH_j=\ker\chi_\infty$, as claimed.

These standard topological and field correspondences apply to arbitrary
Galois extensions, including $K_0^{\mathrm{sep}}/K_0$:
[Stacks, Lemmas 9.22.1--9.22.3 and Theorem 9.22.4](https://stacks.math.columbia.edu/tag/0BMI).
No finite Galois correspondence is applied to a coordinate of $\Omega$.
Such coordinates are elements of $\mathcal C$ and need not be algebraic.

Finally, if a second character satisfies the theorem's eventual identities,
choose for each fixed $j$ one $e$ beyond both thresholds. The two reductions
then agree on every $g$, because both equal $\rho_e\bmod p^j$.
Equality for all $j$ proves equality of the characters. This verifies
the theorem's intrinsic uniqueness, not just uniqueness after selecting $h$.

## 8. Scope, source subtraction, and final binding

The first field $K_1$ is the previously accepted common degree-$p$ field
from levels $e\ge2$, by taking a sufficiently late level in (R1).
It is not the separate prime-period field $L_1$; the accepted disjointness
$L_1\cap L_2=K_0$ confirms that distinction. This is a concrete reason
not to read the conclusion as $K_j=L_j$ or $E_j=j$.

Conrad's completion theorem and the algebraic Galois correspondence are
classical source inputs. The dense-integer centralizer argument, algebraic
finite-net continuity argument, and separated-clopen transfer were checked
directly. The contact identity and compact-odometer construction remain
the separately accepted A1/D1 work and are not claimed again as new here.
No worldwide priority determination or paper admission is made.

The final inspected artifact hashes are:

| Artifact | SHA-256 |
| --- | --- |
| A3/R5 proof package | b20fc9dbfe32ca492a373bc86ced69738518f7cabd295f6903c3bd52d5b77c68 |
| A3/R5 report | f0e309729c02e2298d4abaa3b911ec6eb0ed408372e26f8dcf026dfc505acd38 |
| A1/R4 contact proof | 038cdb412d1b83b94c1ebcfb742090e3937251225077a0f6842d7933c458174e |
| A1/R4 E2 review | b62997eed372a05332db065c6ef1c26623a05d3813b278dab5352c373becf8bf |
| D1/R4 compact-limit proof | e2daa9770024c62e7b7fb09855d4c23eaa0c4cd0aa5416ad268288dbe569aedd |
| D1/R4 E1 review | f644b8e003aa14d597b74e6019602e1856d5ef11eba6e242ac15efbda30e9595 |

Research-review guidance supplied the independent logical and source-
applicability audit. The repository batch rules and this explicit
allocation restrict it to current-team proof-only work; no external-model
workflow was run. There were zero mathematical program executions,
certificate reruns, new agents, author or prior-review edits, shared-state
or Git changes, manuscript/PDF work, or external-model uploads.

**Final disposition:** accept the canonical continuous surjective native
character, exact eventual stabilization of every fixed finite quotient,
and the resulting nested algebraic $\mathbb Z_p$-extension. No repair is
required. Quantitative thresholds, nesting of the original full fields,
full Witt coordinates, all-level ramification, global dynatomic components
and paper admission remain outside the theorem.

NO_BAD_EULER_OR_ROOT_NUMBER remains unconditional.
