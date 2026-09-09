# E6 independent proof review: the common first-quotient break

2026-09-09 UTC. Nonauthor, proof-only review of the frozen A3 round-four
first-quotient package. This file is the only new workspace artifact written
for this allocation. Earlier proofs and reviews remain unchanged.

## Verdict and exact accepted claim

**PASS: zero mathematical must-fixes and zero source must-fixes.**

The inspected proof establishes, from the already reviewed round-three
interfaces, that for every odd prime $p$, with

$$
K=\overline{\mathbb F}_p((s)),\qquad P_s(z)=(1+s)z+z^2,
$$

the unique degree-$p$ subfield $F_e$ of the canonical cyclic small-cycle
field $L_e/K$ has unique lower and upper break

$$
\boxed{b(F_e/K)=2(p-1)\quad\text{for every }e\ge2.}
$$

Here “conductor” denotes the break/Swan conductor used in the author package,
not the Artin-conductor exponent with its additional one. The reduced polar
representative of the native-oriented first AS class therefore has highest
pole exactly $2(p-1)$. This review does not compute its coefficients.

The essential new step is the once-$p$-divisible leading-exponent
cancellation lemma. The author proves both its individual displacement
conclusion and the simultaneous first-graded-rank restriction. The latter
is necessary to resolve the equal-conductor possibility in the elementary
abelian quotient. The proof does not silently replace a quotient break by
the break of an arbitrary chosen lift.

## 1. Frozen scope, inputs, and independence

The whole new [proof package](../../a3_first_quotient_ramification/PROOF_PACKAGE.md)
and [report](../../a3_first_quotient_ramification/REPORT.md) were read. The
allocation concerns their first-quotient theorem only.

The accepted inputs are:

1. The full local inertia theorem: $L_j/K$ is cyclic and totally ramified of
   degree $p^j$, with its stated native generator.
2. For $\alpha$ at level two and $\beta$ at level one, the exact cross-contact
   and native displacement identities, in the base normalization $v(s)=1$:
   $$
   v(\alpha-\beta)=\frac{2(p-1)^2}{p^2},\qquad
   v(g\alpha-\alpha),\ v(h\beta-\beta)\ge\frac{2(p-1)}p,
   $$
   when finite, with equality for a single native step.
3. The level-one break $b(L_1/K)=p-1$, the disjointness
   $L_1\cap L_2=K$, and the oriented stabilization $F_e=F_2$ for $e\ge2$.

The underlying round-three
[contact proof](../../../continuation_round3/a3_interlevel_contacts/PROOF_SUPPLEMENT.md),
[full-inertia proof](../../../continuation_round3/a3_interlevel_contacts/FULL_LOCAL_INERTIA.md),
and their existing E6 audits supplied the first two interfaces. The actual
[oriented-stabilization proof](../../../continuation_round3/a3_interlevel_contacts/ORIENTED_QUOTIENT_STABILIZATION.md)
and its [E2 review](../../../continuation_round3/reviews/e2_oriented_quotients/REVIEW.md)
were inspected for the third. No first-quotient conductor formula is imported
from them.

In particular, the $p=3$ pair AS certificate is not a premise of this audit.
The independent B4 author-side route is not treated as nonauthor acceptance
and is not evidence for a missing step here. A separately announced
`SECOND_LAYER_BREAKS.md` is outside this frozen review scope. No proposed
level-two second-break or different formula is assumed or certified here.

## 2. Uniformizer expansion: the cancellation lemma is valid

Let $D/K$ be as in the lemma, with actual coefficient field

$$
k=\overline{\mathbb F}_p\subset K\subset D,
\qquad O_D=k[[\pi]].
$$

This is a fixed coefficient field, not a residue-field section moved by
the automorphisms. Completeness and the identical residue field give the
displayed expansion for any uniformizer. Every $K$-automorphism fixes each
coefficient. A $p$-power-order automorphism has leading uniformizer
multiplier one, since $k^\times$ has no nontrivial $p$-power torsion.

For an automorphism of lower break $c>0$, write

$$
g\pi=\pi(1+u),\qquad v_D(u)=c.
$$

If $j=p^t m>0$, $p\nmid m$, then in characteristic $p$

$$
(1+u)^j-1=(1+u^{p^t})^m-1
$$

has first term $m u^{p^t}$, so the exact monomial rule is

$$
v_D\bigl(g(\pi^j)-\pi^j\bigr)=j+p^{v_p(j)}c.
\tag{R1}
$$

This verifies rather than assumes the behavior of exponents divisible by
$p$. The positive valuation of the element excludes negative exponents.

Now let $a=v_D(x)$ satisfy $v_p(a)=1$, and suppose all nonidentity
displacements have valuation strictly above $a+p b_0$, where $b_0$
is the first lower break and $p\nmid b_0$. For an element of break $b_0$,
the leading monomial contributes at exactly $a+p b_0$. Every later
$p$-divisible exponent contributes above this value. If the first nonzero
prime-to-$p$ exponent $j$ were smaller than

$$
n=a+(p-1)b_0,
\tag{R2}
$$

its contribution would be the unique lowest term. If there were no such
term at $n$, the leading monomial could not cancel. Both possibilities
contradict the strict displacement hypothesis. Hence $n$ is exactly the
first nonzero prime-to-$p$ exponent. Its asserted coprimality follows from
$a\equiv0\pmod p$ and $n\equiv-b_0\pmod p$.

The simultaneous part of the argument also holds. The map

$$
\theta(g)=\operatorname{res}
\left(\frac{g\pi-\pi}{\pi^{b_0+1}}\right)
$$

is additive on $G=G_{b_0}$, with kernel $G_{b_0+1}$. Composition preserves
the leading coefficient because $b_0\ge1$ and coefficients are fixed.
At order $a+p b_0$, the only possible contributions are those at exponents
$a$ and $n$, with coefficient

$$
c_a\overline{a/p}\,\theta(g)^p+c_n\bar n\,\theta(g).
\tag{R3}
$$

The first coefficient is nonzero. All values of $\theta$ are roots of this
degree-$p$ polynomial. The image is a nonzero additive $p$-group, so its
order is at least $p$ and at most $p$; it is exactly $p$. This is a
bound on the entire first graded quotient, not merely one cyclic subgroup.

For a later-break element with $c>b_0$, the exponent $n$ contributes
at $n+c$. All $p$-divisible terms have order at least $a+p c$, and

$$
a+p c-(n+c)=(p-1)(c-b_0)>0.
$$

Later prime-to-$p$ terms also have larger order. The remaining orders tend
to infinity, so no infinite-series tail can change the unique leading term.
Thus the exact later-displacement formula $v_D(gx-x)=n+c$ is justified.
It is correctly not asserted for elements on the first grade.

## 3. Application to the compositum: every hypothesis is verified

Disjointness gives

$$
B=L_2L_1,\quad [B:K]=p^3,\quad
G=\langle\sigma\rangle\times\langle\gamma\rangle
\simeq C_{p^2}\times C_p.
$$

Both extensions are Galois, so the two independent native generators
exist as claimed. The residue field remains $k$, and the integer
normalization is $v_B=p^3v$. For $\eta=\alpha-\beta$, the inputs give

$$
a=2p(p-1)^2,\qquad A=2p^2(p-1),\qquad v_p(a)=1.
\tag{R4}
$$

The last equality uses odd $p$. For every $g\ne1$, the two root
displacements have valuation at least $A$ in $B$, or are zero, so
$v_B(g\eta-\eta)\ge A$. Cancellation can raise this value and does not
invalidate the bound. For $\sigma$ and $\gamma$ exactly one summand moves,
so their displacements have value exactly $A$.

The first break satisfies $1\le b_0\le p-1$: total wild ramification gives
positivity and integrality, while the degree-$p$ quotient $L_1/K$ forces
the upper bound by upper-numbering quotient compatibility. Before the first
drop, upper and lower numbering coincide. In particular $p\nmid b_0$
already follows from this interval, independently of the supplementary
AS-character explanation in the author text.

Finally,

$$
A-a=2p(p-1)>p(p-1)\ge p b_0.
$$

The lemma applies with a strict inequality. It supplies a first graded
quotient of order $p$, and the later formula

$$
v_B(g\eta-\eta)=a+(p-1)b_0+\ell_B(g)
\quad\text{if }\ell_B(g)>b_0.
\tag{R5}
$$

## 4. Quotient filtration and all low-conductor cases

Set $F=F_2$, $b=b(F/K)$, $E=FL_1$, and
$N=\operatorname{Gal}(B/E)=\langle\sigma^p\rangle$. The group of $E/K$
is elementary abelian of order $p^2$. The cyclic $L_2/K$ has upper
breaks $b,u_2$, with $u_2\ge p b\ge p$.

Choose $p-1<u'<u_2$. The projection of $G^{u'}$ to $L_1$ is trivial,
and its projection to $L_2$ contains $\sigma^p$. Within the actual direct
product, an element with these two images is the specified element of $N$.
Thus $N\subset G^{u'}$. Monotonicity puts $N$ in all groups through,
and for a nonempty interval after, upper $p-1$.

This two-projection argument is sound; it does not assume that ramification
groups of a compositum are products. While $N\subset G^u$, quotient
compatibility gives equality of the indices for $B/K$ and $E/K$.

Suppose $b\le p-1$. All characters of $E/K$ are linear combinations of
the two independent AS characters. Combining reduced representatives with
poles at most $p-1$ cannot produce a larger pole. Since the $L_1$
character has break exactly $p-1$, character separation makes this the
last upper break of $E/K$.

Persistence of $N$ means that the first graded quotient of $E/K$ also
has order $p$. A group of order $p^2$ must consequently have exactly
two distinct upper breaks $b_0<p-1$ and $p-1$, each with drop $p$.
This includes $b=p-1$: cancellation between the two equal-conductor
characters may create a smaller first break, but a single rank-two drop
is incompatible with (R3). No equal-conductor case has been suppressed.

The exact upper-to-lower value at the second quotient break is therefore

$$
c=\psi_B(p-1)=b_0+p(p-1-b_0)>b_0.
\tag{R6}
$$

Choose an element inside $G^{p-1}$ with nontrivial image in the last
nontrivial group of $E/K$. Its image disappears immediately after this
break, so the chosen element leaves $G^u$ there and has lower break
exactly $c$. This establishes the necessary exact-break lift; it is not
an assertion about arbitrary lifts from a quotient.

Applying (R5) gives

$$
v_B(h\eta-\eta)=a+(p-1)b_0+c
=a+p(p-1)<A,
$$

contrary to the uniform bound. Every possibility $b\le p-1$ is excluded.

## 5. The remaining ordering and the exact value

For $b>p-1$, every character combination involving the $F$-character
has break $b$: its nonzero highest pole cannot cancel against the
strictly lower-pole $L_1$-character. The upper breaks of $E/K$ are thus
$p-1,b$, each with rank-one drop.

Choosing now $b<u'<u_2$ in the two-projection argument proves that $N$
persists through and just after $b$. Hence these are also the first two
upper breaks of $B/K$, with indices $1$ and $p$ on the intervening
intervals. In particular $b_0=p-1$ and $n=a+(p-1)^2$.

For $p-1<u\le b$, the $L_1$-projection of $G^u$ is trivial and its
$L_2$-projection is the full group of order $p^2$. The unique direct
product subgroup with these properties is

$$
G^u=\langle\sigma\rangle.
$$

Immediately after $b$, $\sigma$ no longer belongs to the ramification
group because its $L_2$-image is not in the remaining order-$p$ subgroup.
Thus this particular native generator has exactly the later lower break

$$
\ell_B(\sigma)=(p-1)+p\bigl(b-(p-1)\bigr)>b_0.
\tag{R7}
$$

Its displacement is exactly $A$, so (R5) also gives

$$
\ell_B(\sigma)=A-a-(p-1)^2
=2p(p-1)-(p-1)^2=p^2-1.
\tag{R8}
$$

Equating (R7) and (R8) yields $b=2(p-1)$. The accepted equality
$F_e=F_2$ transports this result to all $e\ge2$. The argument uses only
the first two upper intervals of $B$; it does not require a guessed last
break, a full product filtration, or a higher-layer numerical pattern.

## 6. Source applicability and claim limits

The primary source
[Elder--Keating, Section 2](https://arxiv.org/html/2503.16830v1#S2)
explicitly works over arbitrary perfect residue fields. Its general Galois
discussion states upper-numbering quotient compatibility; its cyclic
discussion gives integral abelian upper breaks and the upper/lower relation.
Lemma 2.1 identifies a reduced prime-to-$p$ AS pole with the degree-$p$
break. Theorem 2.3, specialized to length two, gives
$u_2=\max\{p b,m_1\}\ge p b$. Its setup and Section 1 supply the AS--Witt
description needed for cyclic extensions. This checks applicability when
$k=\overline{\mathbb F}_p$; no finite-residue-field restriction is being
imported. These are classical inputs, not new claims of this package.

The theorem determines a break, not a full AS polynomial. Since $2(p-1)$
is prime to odd $p$, the native-oriented reduced first AS representative
has that highest pole with nonzero coefficient. Orientation fixes the
character, whereas the field alone allows its nonzero scalar multiples.
Neither observation computes the leading coefficient or the lower poles.

The report maintains these limits. Its $p=3$ representative is explicitly
an older certificate, not part of this proof. No higher Witt coordinates,
nesting of the full fields $L_e$, general higher ramification sequence,
global cycle-quotient transitivity, or new paper admission is established
by this review. The global `PC424-D` issue is not closed here.

## 7. Final binding, execution record, and disposition

The research-review skill guided the independent logical audit and explicit
claim boundaries. Its generic external-model step was superseded by this
allocation's explicit no-external-model, nonauthor-review instructions.
No additional reviewer was spawned, and no source was uploaded to a model.
No mathematical program, certificate rerun, build, manuscript/PDF, Git
operation, shared-state update, or author-file edit was performed.

The final inspected source hashes are:

| Artifact | SHA-256 |
| --- | --- |
| A3/R4 `PROOF_PACKAGE.md` | `a7a2823857d4bfe05006171809e310df196316f9777bb315052e348094dc7154` |
| A3/R4 `REPORT.md` | `c1d99020bf1b9a8c109a6db4d095f2175b1a2d2e2b9e96835604256fd569674c` |
| R3 `ORIENTED_QUOTIENT_STABILIZATION.md` | `18366e789a1cb693000a2a50d42452e7e7658091cd67ece1c715d38e2a4ae479` |
| R3 E2 oriented-quotient review | `cfa8f8a8529c011d9d78b4fe691a98927987c02d86a7bf0a613d43c056093265` |

**Disposition:** accept the frozen first-quotient theorem and its stated
reduced-pole consequence as a proved local auxiliary result, relative to
the accepted round-three inputs. No author correction is required.
Broader research admission remains the coordinator's separate decision.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
