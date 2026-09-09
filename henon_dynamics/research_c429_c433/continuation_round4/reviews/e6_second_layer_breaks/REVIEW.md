# E6 independent review: actual second-layer breaks and differents

2026-09-09 UTC. Separately allocated nonauthor, proof-only review. The earlier
first-quotient review is frozen and is not enlarged by this document.

## Verdict and scope

**PASS: zero mathematical must-fixes and zero source must-fixes.**

The complete 202-line
[SECOND_LAYER_BREAKS.md](../../a3_first_quotient_ramification/SECOND_LAYER_BREAKS.md)
proves its stated actual ramification filtrations and field different
exponents, taking the now coordinator-accepted first-quotient theorem as an
input. The author file's conditional status records the state at its creation;
that named dependency has now been accepted. No author edit is needed.

For every odd prime $p$, the object is the original
$P_s(z)=(1+s)z+z^2$ over $K=\overline{\mathbb F}_p((s))$, with its canonical
small-cycle fields $L_1,L_2$ in one fixed separable closure and $B=L_2L_1$.
The accepted conclusions are:

| Extension | Upper breaks | Lower breaks |
| --- | --- | --- |
| $L_2/K$ | $2(p-1),\ 2p(p-1)$ | $2(p-1),\ 2(p-1)(p^2-p+1)$ |
| $B/K$ | $p-1,\ 2(p-1),\ 2p(p-1)$ | $p-1,\ p^2-1,\ p^2-1+2p^2(p-1)^2$ |

The different exponents, in the extension's integer-normalized valuation,
are

$$
d_{L_2/K}=(p-1)(2p^3-2p^2+3p-1),
\qquad
d_{B/K}=p^2(p-1)(2p^2-2p+3).
\tag{R1}
$$

These conclusions concern actual fields, not a root-generated order or a
contradictory hypothetical containment. They do not determine all higher
layers, any full Witt vector, or the global cycle quotient.

## 1. Inputs checked and dependency boundary

The imported
[first-quotient proof](../../a3_first_quotient_ramification/PROOF_PACKAGE.md)
and its frozen
[E6 review](../e6_first_quotient_conductor/REVIEW.md)
give $u_1=2(p-1)$, $[B:K]=p^3$, the first two upper intervals in $B$, and
the once-$p$ cancellation lemma with its verified later-break rule.
The coordinator has independently read and accepted that theorem.

The actual [round-three supplement, Section 6 and equation (23)](../../../continuation_round3/a3_interlevel_contacts/PROOF_SUPPLEMENT.md)
was inspected again. It supplies, without using the old pair discriminant,

$$
v(\alpha-\beta)=\frac{2(p-1)^2}{p^2},
\qquad
v(P_s^{\circ p}(\alpha)-\alpha)=2(p-1),
\tag{R2}
$$

where $\alpha$ is a level-two root, $\beta$ is a level-one root, and $v(s)=1$.
The second identity is an exact finite valuation, not only a lower bound.
The actual [oriented-stabilization proof, Section 3](../../../continuation_round3/a3_interlevel_contacts/ORIENTED_QUOTIENT_STABILIZATION.md)
supplies disjointness and records the older hypothetical second-break
expression. That section was read to check the historical distinction.

No $p=3$ AS coefficient, polynomial discriminant, order index, or B4
author-side calculation is a premise. The old pair statement and its accepted
E6 audit were consulted only for the explicitly labeled consistency check.

## 2. The full upper filtration in the compositum

Use the actual independent native generators

$$
G=\operatorname{Gal}(B/K)
=\langle\sigma\rangle\times\langle\gamma\rangle
\simeq C_{p^2}\times C_p,
\qquad \tau=\sigma^p,\quad N=\langle\tau\rangle.
$$

Here $\sigma$ acts on $\alpha$ by $P_s$ and fixes $\beta$, while $\gamma$
acts on $\beta$ and fixes $\alpha$. Disjointness, not ramification
independence, gives this direct product. The first-quotient proof has already
established that the first upper break of $B/K$ is $p-1$.

Let $u_2$ initially be the unknown second upper break of $L_2/K$. The cyclic
inequality $u_2\ge p u_1>u_1$ gives a genuine nonempty last interval.
For every $u>p-1$, upper-numbering quotient compatibility says that $G^u$
has trivial image on $L_1$ and its prescribed full ramification-group image
on $L_2$. Its restriction to the first factor is consequently an
isomorphism onto that image. There is no possible diagonal twist or hidden
kernel when the second projection is trivial.

Together with the accepted first-break statement, this proves the complete
filtration, including endpoints:

$$
G^u=
\begin{cases}
G,&0\le u\le p-1,\\
\langle\sigma\rangle,&p-1<u\le u_1,\\
N,&u_1<u\le u_2,\\
1,&u>u_2.
\end{cases}
\tag{R3}
$$

Thus the three indices in the nontrivial intervals are $1,p,p^2$.
The argument does not apply an invalid product rule for ramification in a
compositum. It proves the groups using the actual two quotient maps.

Writing $\psi_B$ for upper-to-lower numbering gives

$$
c_0=p-1,\qquad
c_1=(p-1)+p(u_1-(p-1))=p^2-1,
\qquad
c_2-c_1=p^2(u_2-u_1).
\tag{R4}
$$

The specific element $\tau$ is a generator of the last nontrivial group
$N$. It belongs through upper $u_2$ and not beyond it, so its lower break
is exactly $c_2$, not merely bounded by $c_2$. In particular $c_2>c_1>c_0$.
No assumption about the break of an arbitrary quotient lift is used.

## 3. Exact displacement and final Herbrand conversion

Set $\eta=\alpha-\beta$. In $v_B=p^3v$, the accepted cancellation analysis
has already established

$$
a=v_B(\eta)=2p(p-1)^2,\qquad
n=a+(p-1)^2,
$$

and

$$
v_B(g\eta-\eta)=n+\ell_B(g)
\quad\text{whenever }\ell_B(g)>p-1.
\tag{R5}
$$

This is the later-break consequence of the once-$p$ lemma. It is not the
prime-to-$p$ leading-valuation lemma applied to the divisible value $a$.
The first prime-to-$p$ uniformizer exponent is $n$, not $a$.

Because $\tau$ fixes $\beta$ and acts as $P_s^{\circ p}$ on $\alpha$, (R2)
gives the exact value

$$
v_B(\tau\eta-\eta)=2p^3(p-1).
\tag{R6}
$$

There is only one moving summand, so cancellation between two roots cannot
alter (R6). The valuation multiplier is $p^3$, not $p^2$. Applying (R5)
to $\tau$ is legitimate by its already established later break, yielding

$$
c_2=2p^3(p-1)-n.
$$

For $\sigma$, the accepted one-step value gives $c_1=2p^2(p-1)-n$.
Subtracting avoids any ambiguity in the common uniformizer exponent:

$$
c_2-c_1=2p^2(p-1)^2.
\tag{R7}
$$

The final slope for $\psi_B$ in (R3) is $p^2$. Hence (R4)--(R7) force

$$
u_2-u_1=2(p-1)^2,\qquad u_2=2p(p-1).
\tag{R8}
$$

This proves the stated $B/K$ breaks and identifies the actual second upper
break of $L_2/K$ by quotient compatibility. For the latter cyclic extension,
the second slope of its own Herbrand function is $p$, not $p^2$. Therefore

$$
b_1=u_1=2(p-1),\qquad
b_2=b_1+p(u_2-u_1)
=2(p-1)(p^2-p+1).
\tag{R9}
$$

All three normalizations are kept distinct: the base valuation, the
integer-valued $v_{L_2}$, and the integer-valued $v_B$.

## 4. Field different: definition, applicability, and endpoints

The intended different is that of the maximal valuation ring $O_D/O_K$,
for $D=L_2$ or $B$. One can justify the derivative calculation without
assuming that the periodic root is an integral generator.

Indeed let $m=[D:K]$ and let $\pi$ be a uniformizer of $D$. Since
$v(\pi)=1/m$, the value group of $K(\pi)$ forces
$[K(\pi):K]\ge m$, and thus $K(\pi)=D$. In the basis
$1,\pi,\ldots,\pi^{m-1}$, the terms $a_i\pi^i$ have distinct integer
valuations modulo $m$. An integral linear combination therefore has every
$a_i\in O_K$. This proves $O_D=O_K[\pi]$. Its minimal polynomial is monic
Eisenstein and separable.

The monogenic different formula gives

$$
d_{D/K}=v_D(f'(\pi))
=\sum_{g\ne1}v_D(\pi-g\pi)
=\sum_{g\ne1}(\ell_D(g)+1)
=\sum_{i\ge0}(|G_i|-1).
\tag{R10}
$$

The last equality counts the integer indices $0,\ldots,\ell_D(g)$.
It explains the contribution of $G_0$ and all endpoint conventions.
The residue field being infinite does not change this ideal valuation.

For $L_2/K$, the groups have orders $p^2$ at integers $0,\ldots,b_1$,
then $p$ at $b_1+1,\ldots,b_2$. Consequently

$$
\begin{aligned}
d_{L_2/K}
&=(b_1+1)(p^2-1)+(b_2-b_1)(p-1)\\
&=(2p-1)(p^2-1)+2p(p-1)^3\\
&=(p-1)(2p^3-2p^2+3p-1).
\end{aligned}
\tag{R11}
$$

For $B/K$, the group orders are $p^3$ through $c_0$, $p^2$ from
$c_0+1$ through $c_1$, and $p$ from $c_1+1$ through $c_2$. Thus

$$
\begin{aligned}
d_{B/K}
&=(c_0+1)(p^3-1)+(c_1-c_0)(p^2-1)+(c_2-c_1)(p-1)\\
&=p(p^3-1)+p(p-1)(p^2-1)+2p^2(p-1)^3\\
&=p^2(p-1)(2p^2-2p+3).
\end{aligned}
\tag{R12}
$$

The algebra and all interval lengths in both sums check directly.
The stated tower consistency also holds:

$$
d_{B/K}-p\,d_{L_2/K}=p(p-1).
$$

Every nonidentity element of $\langle\gamma\rangle=\operatorname{Gal}(B/L_2)$
leaves the filtration at upper, and hence first lower, break $p-1$.
Lower numbering is subgroup-compatible in the same valuation $v_B$,
so its different is $(p-1+1)(p-1)=p(p-1)$. The factor $p$ multiplying
$d_{L_2/K}$ is the ramification index of $B/L_2$.

## 5. Primary-source applicability

[Elder--Keating, Section 2](https://arxiv.org/html/2503.16830v1#S2)
uses arbitrary perfect residue fields, states the general Galois quotient
and subgroup compatibility, and gives the cyclic upper/lower formulas.
Its Theorem 2.3 implies $u_2\ge p u_1$. These statements apply to the
present algebraically closed residue field. In particular, the cyclic
formula is used for $L_2$, while (R4) for noncyclic $B$ follows from the
general Herbrand definition and the explicitly proved groups.

For (R10), the author-cited
[Stacks Lemma 49.12.2](https://stacks.math.columbia.edu/tag/0BWD)
gives the derivative generator in the one-variable complete-intersection
case, and [Lemma 49.12.3](https://stacks.math.columbia.edu/tag/0BWG)
identifies the relevant different. Its
[hypotheses](https://stacks.math.columbia.edu/tag/0BWE)
hold here: the monic presentation is finite flat and a local complete
intersection over a Noetherian DVR. The generic extension is separable.
The [Dedekind trace-dual definition](https://stacks.math.columbia.edu/tag/0BW0)
is consistent with this maximal-order calculation. No number-field-only or
finite-residue theorem was substituted.

These are classical ingredients. The present field-specific conclusion is
obtained from the accepted dynamical displacement and first-quotient inputs.
No broad literature-priority conclusion is made by this bounded review.

## 6. Historical hypothetical value and the pair check

The round-three noncontainment proof derived the numerical expression in
(R9) under the contrary hypothesis $L_1\subset L_2$. In that argument its
first lower break would have been $p-1$, and the difference of the two
proposed lower breaks was $-1$ modulo $p$, giving a contradiction.
The earlier expression was not an unconditional determination of $b_2$.

The current proof instead uses the genuine disjoint compositum, its
once-$p$ cancellation lemma, and the accepted actual first break
$2(p-1)$. Equations (R6)--(R9) are an independent new deduction of the
actual second break. Its difference from the actual first break is now
$2p(p-1)^2$, as required. There is no resurrection of a false hypothesis.

At $p=3$, direct substitution gives

$$
L_2:\quad (u_1,u_2)=(4,12),\quad(b_1,b_2)=(4,28),\quad d=88;
$$

$$
B:\quad (v_0,v_1,v_2)=(2,4,12),\quad
(c_0,c_1,c_2)=(2,8,80),\quad d=270.
$$

The first line agrees with the accepted
[pair deduction](../../../continuation_round2/a3_wild_local_tower/PAIR_RAMIFICATION.md).
The old polynomial discriminant valuation $144$ belongs to the order
$O_K[\alpha]$, not to the maximal-order field different. Its accepted
additive $O_K$-module index length $28$ gives $144=88+2\cdot28$.
Since the residue degree is one, the field discriminant exponent equals
the field different exponent $88$; this does not make the two orders equal.
None of these pair data is used to prove the uniform formulas.

## 7. Final binding and disposition

The final inspected hashes are:

| Binding artifact | SHA-256 |
| --- | --- |
| A3 second-layer proof | a79c9fea9e9ee01f8888bd0f088b20bb18fb505b60ccdeab8f1516125192a4ed |
| Accepted A3 first-quotient proof | a7a2823857d4bfe05006171809e310df196316f9777bb315052e348094dc7154 |
| Frozen E6 first-quotient review | a8a43f4d82656f7e8f4c39aea9295db2aaa696ad573806548d4821cfce14922f |

The research-review skill supplied the full-argument audit and claim
separation. The repository batch skill and this allocation require a
current-team, proof-only review; no generic external-model step was run.
Only this new assigned review was written. No mathematical execution,
certificate rerun, new agent, author-file edit, earlier-review edit,
shared-state change, Git operation, manuscript or PDF was produced.

**Disposition:** accept the actual second-layer and compositum ramification
formulas, including both field differents, as a proved local auxiliary
corollary of the accepted first-quotient theorem and round-three interfaces.
No repair is required. All-higher-level ramification, higher Witt
coordinates, a nested full-field tower, global PC424-D and any new paper
admission remain outside this result.

NO_BAD_EULER_OR_ROOT_NUMBER remains unconditional.
