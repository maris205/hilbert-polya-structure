# Exact first-quotient break from one controlled cancellation

2026-09-09 UTC. New round-four proof. Frozen round-three proofs and reviews are read-only dependencies. No mathematical computation is used.

## Claim and status

For every odd prime $p$, put

$$
k=\overline{\mathbb F}_p,\quad K=k((s)),\quad v(s)=1,
\quad P_s(z)=(1+s)z+z^2.
$$

Let $L_e/K$ be the accepted canonical cyclic small-cycle field of degree $p^e$, and let $F_e$ be its unique degree-$p$ subfield. Then

$$
b(F_e/K)=2(p-1)\qquad(e\ge2),
\tag{T}
$$

where a cyclic degree-$p$ extension has the same unique lower and upper break, denoted $b$. Thus the highest pole of the reduced first AS class is exactly $2(p-1)$, for every stated prime and level.

**Status: PROVABLE AS STATED from the reviewed round-three interfaces; new independent whole-proof review pending.** The coefficients of the general-prime reduced AS representative are not computed here.

## Assumptions, notation, and dependency map

The following are imported from the complete reviewed proofs, not conjectural premises:

1. $L_1/K$ and $L_2/K$ are totally ramified cyclic of degrees $p$ and $p^2$. Their native generators send a small-cycle root to $P_s$ of that root. See [full local inertia](../../continuation_round3/a3_interlevel_contacts/FULL_LOCAL_INERTIA.md) and its [E6 review](../../continuation_round3/reviews/e6_full_local_inertia/REVIEW.md).
2. For roots $\beta\in L_1$ and $\alpha\in L_2$, put $r=(p-1)/p$. Then
   $$
   v(\alpha)=v(\beta)=r,\qquad
   v(\alpha-\beta)=\frac{2(p-1)^2}{p^2}.
   \tag{1}
   $$
   Every native displacement within either root set has valuation at least $2r$, and a single native step has valuation exactly $2r$. These are [the uniform contacts and elementary displacement identities](../../continuation_round3/a3_interlevel_contacts/PROOF_SUPPLEMENT.md), reviewed by E6.
3. $L_1/K$ has break $p-1$. Moreover, $L_1\cap L_2=K$ and $F_e=F_2$ for $e\ge2$, with fixed native orientation. See [oriented quotient stabilization](../../continuation_round3/a3_interlevel_contacts/ORIENTED_QUOTIENT_STABILIZATION.md) and its [E2 review](../../continuation_round3/reviews/e2_oriented_quotients/REVIEW.md).

For a totally ramified Galois extension $D/K$, use the integer-normalized valuation $v_D=[D:K]v$. For $g\ne1$ set

$$
\ell_D(g)=v_D(g\pi-\pi)-1,
$$

with $\pi$ any uniformizer. Write $G_t$ and $G^u$ for lower and upper ramification groups, and $\psi_D$ for the upper-to-lower Herbrand function. Thus

$$
\psi_D(u)=\int_0^u [G:G^t]\,dt.
\tag{2}
$$

Classical ramification facts used below are upper-numbering quotient compatibility, integral abelian upper breaks, the reduced AS description of degree-$p$ conductors, and the cyclic degree-$p^2$ bound $u_2\ge p u_1$. Their applicability to arbitrary perfect residue fields is verified in Elder--Keating, [Section 2, Lemmas 2.1--2.2 and Theorem 2.3](https://arxiv.org/html/2503.16830v1). All fields here have residue field $k$, which is perfect. These classical inputs are subtracted, not claimed as new.

The new argument is: establish a cancellation lemma for an element whose leading exponent has $p$-adic valuation one; apply it in $L_2L_1$; exclude all early-conductor orderings through the degree-$p^2$ elementary quotient; then read off the remaining break. No assumed conductor or AS coefficient enters the contact computation.

## 1. A cancellation lemma for a leading exponent divisible once by $p$

**Lemma.** Let $D/K$ be a finite totally ramified Galois $p$-extension with fixed coefficient field $k$. Let $G=\operatorname{Gal}(D/K)$ have first lower break $b_0>0$, with $p\nmid b_0$. Suppose $x\in D$ has positive valuation

$$
a=v_D(x),\qquad p\mid a,\quad p^2\nmid a,
\tag{3}
$$

and every nonidentity $g\in G$ satisfies

$$
v_D(gx-x)>a+p b_0.
\tag{4}
$$

Then:

1. In any expansion $x=\sum_{j\ge a}c_j\pi^j$ over $k$, the first nonzero exponent prime to $p$ is
   $$
   n=a+(p-1)b_0.
   \tag{5}
   $$
2. The first ramification graded quotient $G_{b_0}/G_{b_0+1}$ has order $p$.
3. If $g$ has later lower break $c=\ell_D(g)>b_0$, then
   $$
   v_D(gx-x)=n+c.
   \tag{6}
   $$

**Proof.** Choose a uniformizer $\pi$, so $O_D=k[[\pi]]$. A $p$-power-order automorphism fixes $k$ and has leading multiplier one. For $g$ with lower break $b$ write

$$
g\pi=\pi(1+u),\qquad v_D(u)=b.
$$

For every positive integer $j$, binomial expansion in characteristic $p$ gives

$$
v_D\bigl(g(\pi^j)-\pi^j\bigr)
=j+p^{v_p(j)}b.
\tag{7}
$$

Fix $g$ of break $b_0$. The leading monomial of $x$ therefore contributes at exact order $a+p b_0$, because $v_p(a)=1$. Every later monomial whose exponent is divisible by $p$ contributes at strictly larger order. If the first nonzero exponent $j$ prime to $p$ were less than $a+(p-1)b_0$, its contribution at order $j+b_0<a+p b_0$ would be unique at that lowest order; all later prime-to-$p$ exponents give strictly higher order, and all $p$-divisible exponents give order at least $a+p b_0$. This would contradict (4). If there were no nonzero prime-to-$p$ exponent at $a+(p-1)b_0$, the leading monomial's contribution at order $a+p b_0$ could not cancel, again contradicting (4). This proves (5). Since $p\nmid b_0$, the integer in (5) is indeed prime to $p$.

For completeness, the first graded quotient is controlled simultaneously, not one automorphism at a time. Define

$$
\theta(g)=\operatorname{res}\left(\frac{g\pi-\pi}{\pi^{b_0+1}}\right)
\quad(g\in G=G_{b_0}).
$$

Composition adds these leading coefficients: substituting $g\pi=\pi+O(\pi^{b_0+1})$ into the leading term of $h\pi-\pi$ leaves its coefficient unchanged modulo $\pi^{b_0+2}$. Thus $\theta$ is an additive homomorphism with kernel $G_{b_0+1}$, giving an injection of the graded quotient into $(k,+)$.

At order $a+p b_0$, only the leading term $c_a\pi^a$ and the term $c_n\pi^n$ can contribute. Their combined coefficient is

$$
c_a\overline{(a/p)}\,\theta(g)^p
+c_n\bar n\,\theta(g).
\tag{8}
$$

Here $c_a\overline{(a/p)}\ne0$. Equation (4) makes (8) vanish for every $g$. A nonzero polynomial of degree $p$ has at most $p$ roots in $k$. The nontrivial $p$-group $G_{b_0}/G_{b_0+1}$ therefore has exactly $p$ elements, proving conclusion 2.

Finally, let $g$ have break $c>b_0$. The term $c_n\pi^n$ contributes at order $n+c$. All later prime-to-$p$ terms contribute at greater order. Any term with exponent divisible by $p$ has exponent at least $a$, so its contribution has order at least $a+p c$, and

$$
a+p c-(n+c)=(p-1)(c-b_0)>0.
$$

Consequently the term of order $n+c$ is unique and cannot cancel. The orders of the remaining series terms tend to infinity, so the argument applies to the complete series, proving (6). $\square$

## 2. Apply the lemma in the disjoint compositum

Let

$$
B=L_2L_1,\qquad G=\operatorname{Gal}(B/K)
\simeq C_{p^2}\times C_p,
\qquad \eta=\alpha-\beta.
$$

The disjointness input gives $[B:K]=p^3$ and $v_B=p^3v$. Define commuting generators $\sigma,\gamma\in G$ by

$$
\sigma\alpha=P_s(\alpha),\quad \sigma\beta=\beta,
\qquad
\gamma\alpha=\alpha,\quad \gamma\beta=P_s(\beta).
$$

The exact contact in (1) gives

$$
a:=v_B(\eta)=2p(p-1)^2,
\qquad v_p(a)=1.
\tag{9}
$$

For any $g\in G$, both $g\alpha-\alpha$ and $g\beta-\beta$ are either zero or have base valuation at least $2r$. Their difference is $g\eta-\eta$. Hence

$$
v_B(g\eta-\eta)\ge A:=2p^2(p-1)
\quad(g\ne1),
\tag{10}
$$

allowing infinite valuation if a displacement vanishes. Because only one summand is nonzero for $\sigma$ and $\gamma$, the one-native-step identities give

$$
v_B(\sigma\eta-\eta)=v_B(\gamma\eta-\eta)=A.
\tag{11}
$$

Let $b_0$ be the first lower, equivalently first upper, break of $B/K$. The degree-$p$ quotient $L_1/K$ has break $p-1$, so quotient compatibility gives $b_0\le p-1$. Also $b_0$ is a positive integer prime to $p$: the first drop of a finite abelian $p$-extension is detected by a nontrivial degree-$p$ character, whose reduced AS representative has a highest pole prime to $p$. This also follows by choosing a nonzero character of the first graded quotient, which is elementary abelian by the leading-coefficient injection used in Section 1.

Now

$$
A-a=2p(p-1)>p(p-1)\ge p b_0.
\tag{12}
$$

Thus (9)--(12) satisfy the cancellation lemma. Put

$$
n=a+(p-1)b_0.
\tag{13}
$$

The first graded quotient has order $p$. Every $g$ with $\ell_B(g)>b_0$ satisfies

$$
v_B(g\eta-\eta)=n+\ell_B(g).
\tag{14}
$$

This formula is not asserted for the first-grade elements, where the leading cancellation is essential.

## 3. Exclude all cases in which the first quotient has break at most $p-1$

Write $F=F_2$, and let

$$
b=b(F/K).
$$

The cyclic extension $L_2/K$ has upper breaks $b$ and $u_2$, with $u_2\ge p b\ge p$. Let

$$
E=FL_1,\qquad
N=\operatorname{Gal}(B/E)=\langle\sigma^p\rangle.
$$

Since $F\subset L_2$ and $L_1\cap L_2=K$, $E/K$ is elementary abelian of degree $p^2$, and $N$ has order $p$.

First, $N\subset G^u$ for every $0\le u\le p-1$. To verify this without assuming a product rule for compositum ramification, choose $u'$ with $p-1<u'<u_2$. The image of $G^{u'}$ in $\operatorname{Gal}(L_1/K)$ is trivial, while its image in $\operatorname{Gal}(L_2/K)$ contains the order-$p$ subgroup $\langle\sigma^p\rangle$, by upper quotient compatibility. The element of $G=C_{p^2}\times C_p$ with these two specified images is the corresponding element of $N$. Thus $N\subset G^{u'}$, and monotonicity gives the assertion for all $u\le p-1$.

Consequently, throughout $[0,p-1]$ the quotient filtration on $E$ has the same indices as that on $B$:

$$
[G:G^u]=[G/N:(G/N)^u].
\tag{15}
$$

Suppose now, for contradiction, that $b\le p-1$. All degree-$p$ characters of $E/K$ are $\mathbb F_p$-linear combinations of those for $F/K$ and $L_1/K$. Reduced AS representatives of those two characters have poles at most $p-1$, and taking a linear combination cannot introduce a higher pole. Hence every such character has conductor at most $p-1$. One has conductor exactly $p-1$, namely the character of $L_1/K$. Character separation and upper quotient compatibility therefore make $p-1$ the last upper break of $E/K$.

The first graded quotient of $B/K$ has order $p$, and $N$ remains in the groups through $p-1$. Thus the first graded quotient of $E/K$ also has order $p$. Since $|\operatorname{Gal}(E/K)|=p^2$ and its last upper break is $p-1$, it follows that $E/K$ has exactly two distinct upper breaks

$$
b_0<p-1,\qquad p-1,
\tag{16}
$$

each reducing its ramification group by a factor $p$. In particular, the possibility $b=p-1$ is not being omitted: if the two individual characters have this same conductor, either their combinations give a smaller first break as in (16), or there is a single first drop of order $p^2$, which the cancellation lemma has ruled out.

Equations (2), (15), and (16) give the lower value corresponding to the upper break $p-1$:

$$
c=\psi_B(p-1)=b_0+p(p-1-b_0)>b_0.
\tag{17}
$$

There is an element $h\in G$ with lower break exactly $c$. Indeed, at upper $p-1$ the quotient $E/K$ has a nonidentity ramification element, whereas immediately after that break its quotient ramification group is trivial. Any lift inside $G^{p-1}$ with nontrivial image therefore leaves the group immediately after this break. Its lower break is (17).

Apply (14) to $h$. It gives

$$
\begin{aligned}
v_B(h\eta-\eta)
&=n+c\\
&=a+(p-1)b_0+b_0+p(p-1-b_0)\\
&=a+p(p-1)\\
&<a+2p(p-1)=A.
\end{aligned}
\tag{18}
$$

This contradicts (10). Every case with $b\le p-1$ is excluded. Therefore

$$
b>p-1.
\tag{19}
$$

## 4. The remaining ordering forces the exact break

With (19), every nonzero linear combination of the two degree-$p$ characters involving the character of $F$ has conductor $b$: its highest pole cannot cancel with the strictly lower pole of the $L_1$ character. The other nonzero characters have conductor $p-1$. Thus $E/K$ has upper breaks $p-1$ and $b$, each of rank one.

The subgroup $N$ persists through upper $b$. To check this, choose $b<u'<u_2$, possible because $u_2\ge p b>b$. The same two-projection argument as in Section 3 puts $N$ in $G^{u'}$, and hence in every earlier group. Consequently the first two upper breaks of $B/K$ are also $p-1$ and $b$, with indices $1$ and $p$ on the two intervening intervals. In particular,

$$
b_0=p-1,\qquad n=a+(p-1)^2.
\tag{20}
$$

For $p-1<u\le b$, quotient compatibility makes the image of $G^u$ on $L_1$ trivial and its image on $L_2$ the full cyclic group of order $p^2$. Thus

$$
G^u=\operatorname{Gal}(B/L_1)=\langle\sigma\rangle
\quad(p-1<u\le b).
$$

Immediately after $b$, the image on $L_2$ drops to its order-$p$ subgroup. Hence the native generator $\sigma$ has lower break

$$
\ell_B(\sigma)=\psi_B(b)=(p-1)+p\bigl(b-(p-1)\bigr)>b_0.
\tag{21}
$$

Its displacement is exactly $A$ by (11). Equations (14) and (20) therefore yield

$$
\begin{aligned}
\ell_B(\sigma)
&=A-n\\
&=2p^2(p-1)-2p(p-1)^2-(p-1)^2\\
&=p^2-1.
\end{aligned}
\tag{22}
$$

Combine (21) and (22):

$$
(p-1)+p\bigl(b-(p-1)\bigr)=p^2-1,
\qquad b=2(p-1).
\tag{23}
$$

This proves (T) at level two. The accepted equality $F_e=F_2$ for every $e\ge2$ proves it at all remaining levels. $\square$

## 5. AS interpretation and exact scope

A nontrivial oriented degree-$p$ AS character over $K$ is represented by a unique reduced polar AS polynomial. Its highest pole is prime to $p$ and equals the ramification break of its field. The orientation is needed for uniqueness of the representative; the underlying field alone permits a nonzero scalar change. Here $2(p-1)$ is prime to every odd $p$, so (23) says that the fixed native-oriented class has highest pole exactly $2(p-1)$ with nonzero coefficient. This is a conductor conclusion, not a symbolic computation of the full class.

At $p=3$ the accepted pair certificate gives the more precise representative $2s^{-4}+s^{-2}$, compatible with the now uniform answer. That certificate was not used in any step of this proof. No argument above infers higher Witt coordinates, a nested sequence of full fields, general higher-level ramification breaks, or transitivity of the global cycle quotient.

The prime-to-$p$ leading-exponent rule and its new once-$p$ cancellation variant have distinct hypotheses. The proof does not apply the former to $\eta$, whose value (9) is divisible by $p$. The equal-conductor case was resolved through all characters of $E$, not by assuming that the two given character conductors are its only breaks.

## Open risks and execution record

No unproved mathematical step is retained as an assumption beyond the explicitly reviewed inputs and classical facts. The new cancellation lemma and all ramification-filtration cases still require the coordinator's separately allocated nonauthor review. An author-side comparison with the independent B4 route does not replace that review.

Mathematical executions: **zero**. No code, new AS run, old rerun, source upload to a model, manuscript/PDF, shared-state change or Git action was performed. Only the allocated new report and this proof were written.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
