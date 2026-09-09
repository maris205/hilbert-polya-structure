# Full local inertia from a level-two cluster comparison

2026-09-09 UTC. New proof-only supplement, separate from the frozen second-layer proof under E6 review. No mathematical execution, changed-precision run, or higher-level AS computation is used.

## Exact claim and status

For every odd prime $p$ and every integer $e\ge1$, put

$$
k=\overline{\mathbb F}_p,\quad K=k((s)),\quad R=k[[s]],
\quad v(s)=1,\quad P_s(z)=(1+s)z+z^2.
$$

Let $M_e$ be the canonical monic degree-$p^e$ Hensel factor of

$$
Q_e(z)=\frac{P_s^{\circ p^e}(z)-z}{P_s^{\circ p^{e-1}}(z)-z}
$$

whose reduction is $z^{p^e}$. Then $M_e$ is irreducible over $K$, and its splitting field is totally ramified cyclic of degree $p^e$. Equivalently, the first reduced AS quotient of the native small-cycle torsor is nonzero at every odd prime and level.

**Author status: PROVABLE AS STATED from the accepted small-cycle inputs and the second-layer theorem proved in the frozen [interlevel supplement](PROOF_SUPPLEMENT.md). Independent review of this full-level extension is pending.**

This is the original all-level **local** inertia statement. It is not the full global PC424-D component theorem: global native-cycle quotient transitivity remains a separate problem.

## Assumptions, notation and dependency map

Write $r=(p-1)/p$, and let $S_j$ be the $p^j$ roots of $M_j$ in a fixed separable closure of $K$, with the uniquely extended valuation. The accepted inputs are:

1. $S_j$ is one native $P_s$-cycle of $p^j$ distinct roots, all of valuation $r$; $Q_j=M_jV_j$ with $V_j(0,0)\ne0$.
2. The Galois action on $S_j$ is a subgroup $H_j\le C_{p^j}$ of native rotations. This follows from commuting with the single native cycle and does not assume $H_j=C_{p^j}$.
3. Prime-level inertia is full, with break $p-1$.
4. The frozen second-layer proof establishes, for every odd $p$ and $j\ge2$,

$$
[K(\alpha_j):K]\ge p^2,\qquad
v(P_s^{\circ p}(\alpha_j)-\alpha_j)=2(p-1),
\quad \alpha_j\in S_j.
\tag{1}
$$

In particular $H_2=C_{p^2}$. Input 4 is proved without any higher-level AS or discriminant computation in Theorem C and equation (23) of [PROOF_SUPPLEMENT.md](PROOF_SUPPLEMENT.md), submitted with SHA256 `7e9494aa53bb96f5927b8a6ab8e27c5d318d35a9c0f1751663acb9b91f0c1bdb`. The present proof does not replace its independent review.

The proof has four steps:

1. Identify exactly $p$ top clusters in every $S_j$, $j\ge2$, from native distances.
2. Compute the multiplier valuation at the level-two cycle.
3. Use a derivative-ratio identity to find a cross-level contact deeper than the top-cluster separation.
4. Prove that this contact produces a canonical Galois-equivariant matching of the $p$ clusters. Full inertia on level-two clusters then forces full inertia at level $e$.

The small-cycle existence, uniqueness and slope are source-owned inputs from Lindahl--Rivera-Letelier, [Theorem C](https://arxiv.org/html/1311.4478v3). The cyclic Galois-action interface, Hensel factorization and AS equivalence are the accepted first-pass A3/A4/E2 interfaces. No claim is made that these imported statements themselves prove the new cluster comparison.

## 1. The $p$ top clusters are exactly the native indices modulo $p$

For two points $x,y$ of positive valuation $r$, whether at the same or different levels,

$$
P_s(x)-P_s(y)=(x-y)(1+s+x+y).
\tag{2}
$$

The second factor is a unit, with difference from $1$ of valuation at least $r$. Thus the native map preserves $v(x-y)$, and every iterate's quotient of differences belongs to $1+\{u:v(u)\ge r\}$.

Fix $j\ge2$ and $x\in S_j$. The one-step displacement has valuation

$$
v(P_s(x)-x)=v(sx+x^2)=2r,
$$

since $1+r>2r$. If $a$ is a positive integer prime to $p$, telescoping the $a$ one-step displacements and dividing by $P_s(x)-x$ gives a sum with residue $a\ne0$. Hence

$$
v(P_s^{\circ a}(x)-x)=2r\quad\text{when }p\nmid a.
\tag{3}
$$

If $p\mid a$, telescope instead in blocks of $p$ steps. Every summand has valuation $2(p-1)$ by (1) and the isometry (2), so

$$
v(P_s^{\circ a}(x)-x)\ge2(p-1)>2r
\quad\text{when }p\mid a\text{ and }p^j\nmid a.
\tag{4}
$$

Define an equivalence relation on $S_j$ by $x\sim_j y$ if $x=y$ or $v(x-y)>2r$. It is an equivalence relation by the strong triangle inequality. Equations (3)--(4) show that its classes are precisely

$$
\mathcal C_{j,a}=
\{P_s^{\circ(a+bp)}(x):0\le b<p^{j-1}\},
\qquad a\in\mathbb Z/p\mathbb Z.
\tag{5}
$$

They do not depend on choosing $x$ except for a cyclic relabelling. There are exactly $p$ classes. Distinct classes are separated by valuation exactly $2r$; any two distinct points in one class have distance valuation greater than $2r$. The native map cyclically permutes the classes.

The absolute Galois group preserves each root set and the valuation, so it acts on these equivalence classes. Under the rotation identification $H_j\le C_{p^j}$, this action is the reduction of the rotation index modulo $p$.

## 2. The level-two multiplier has an exact valuation

Choose $\beta\in S_2$ and put $\mu=(P_s^{\circ p^2})'(\beta)$. The exact polynomial factorization

$$
P_s^{\circ p^2}(z)-z
=(P_s^{\circ p}(z)-z)M_2(z)V_2(z)
$$

gives, after differentiating and evaluating at $\beta$,

$$
\mu-1=(P_s^{\circ p}(\beta)-\beta)M_2'(\beta)V_2(\beta).
\tag{6}
$$

The complementary factor is a unit. In the derivative product for $M_2'(\beta)$, the $p(p-1)$ differences at indices prime to $p$ have valuation $2r$ by (3). The other $p-1$ differences, at indices $ap$ for $1\le a<p$, have valuation exactly $2(p-1)$: telescope $a$ $p$-step displacements, divide by the first one, and use (2) to obtain residue $a\ne0$.

Using (1) for the initial factor in (6), we obtain

$$
\begin{aligned}
v(\mu-1)
&=2(p-1)+p(p-1)\,2r+(p-1)\,2(p-1)\\
&=2(p-1)(2p-1).
\end{aligned}
\tag{7}
$$

In particular, $\mu-1\ne0$. This formula is a symbolic consequence of the already proved second-layer contacts, not a computed discriminant value.

## 3. A higher cycle has a contact deeper than $2r$ with level two

Fix $e\ge3$. Both $P_s^{\circ p^e}(z)-z$ and $P_s^{\circ p^{e-1}}(z)-z$ vanish at $\beta$, whose ordinary period is $p^2$. Differentiate their defining quotient identity and evaluate at $\beta$ to obtain

$$
Q_e(\beta)=
\frac{\mu^{p^{e-2}}-1}{\mu^{p^{e-3}}-1}
=(\mu-1)^{(p-1)p^{e-3}}.
\tag{8}
$$

The denominator is nonzero by (7). Thus this is a valid derivative identity, not an undefined evaluation of $0/0$.

Since $V_e(\beta)$ is a unit, equations (7)--(8) give

$$
\frac1{p^e}\sum_{\alpha\in S_e}v(\beta-\alpha)
=\frac{2(p-1)^2(2p-1)}{p^3}.
\tag{9}
$$

All contacts in this sum are finite, because the two ordinary periods differ. Its average is strictly greater than $2r$:

$$
\frac{2(p-1)^2(2p-1)}{p^3}-2r
=\frac{2(p-1)(p^2-3p+1)}{p^3}>0.
\tag{10}
$$

For every integer $p\ge3$, $p^2-3p+1=(p-1)(p-2)-1\ge1$, proving the strict sign. Therefore some $\alpha\in S_e$ satisfies

$$
v(\alpha-\beta)>2r.
\tag{11}
$$

Only existence of this deeper contact is needed; no exact formula for deeper within-cluster contacts is assumed.

## 4. Canonical cluster matching and Galois transitivity

Let $\alpha,\beta$ be a pair satisfying (11). By the native isometry (2),

$$
v(P_s^{\circ a}(\alpha)-P_s^{\circ a}(\beta))>2r
\quad(0\le a<p).
\tag{12}
$$

These $p$ pairs meet every top cluster in both sets, once each. Define a relation between a cluster $C$ of $S_e$ and a cluster $D$ of $S_2$ by the existence of $x\in C$, $y\in D$ with $v(x-y)>2r$.

If one such pair exists, every pair $x'\in C$, $y'\in D$ has the same strict inequality: apply the strong triangle inequality to $x'-x$, $x-y$ and $y-y'$, all with valuations greater than $2r$ (allowing a zero difference). If $C'\ne C$, its points have distance valuation exactly $2r$ from points of $C$, by Section 1. The unequal-valuation triangle rule then gives $v(x''-y)=2r$ for every $x''\in C'$. Hence one cluster of $S_2$ cannot be related to two clusters of $S_e$. Reversing the two sets proves uniqueness on the other side as well.

Together with the $p$ pairs in (12), this proves a perfect matching between the two sets of $p$ top clusters. It is canonical: it is characterized by the valuation inequality alone, not by the initially chosen pair or labels. Since absolute Galois preserves root sets and valuations, the matching is Galois-equivariant.

The second-layer theorem gives $H_2=C_{p^2}$, which acts transitively on the $p$ top clusters of $S_2$. Absolute Galois therefore acts transitively on those clusters, and the equivariant matching forces it to act transitively on the $p$ top clusters of $S_e$.

If $H_e$ were a proper subgroup of the cyclic $p$-group $C_{p^e}$, every element of $H_e$ would have rotation index divisible by $p$. Equation (5) would then make its action on the $p$ top clusters trivial. A trivial action on $p>1$ clusters cannot be transitive. Thus $H_e$ is not proper:

$$
H_e=C_{p^e}\qquad(e\ge3).
$$

For $e=1$ this is the accepted prime-level input, and for $e=2$ it is the second-layer theorem. Hence it holds for every $e\ge1$. The root action is transitive, so $M_e$ is irreducible; its splitting group is the displayed cyclic group. Its residue extension is trivial because $k$ is algebraically closed, so the extension is totally ramified. The accepted AS torsor equivalence then gives the claimed all-level nonvanishing. $\square$

## Verification boundaries and remaining global question

This argument is not an inference from the certified $(3,2)$ pair: its second-layer input and all subsequent calculations are uniform in odd $p$. It uses neither the pair's AS polynomial, the number $144$, an uncomputed higher Witt coordinate, nor a guessed pattern of contacts. The first-level exact-denominator shortcut fails beyond the second layer, as recorded in the frozen supplement; the present level-two cluster comparison is a different mechanism.

The only pending logical dependency is independent checking of the submitted second-layer theorem and this complete cluster proof. No unproved higher-contact formula is a premise. The full global dynatomic curve can contain many native cycles; this local result controls the inertia of its canonical small cycle and does not prove transitivity on the global set of cycles. That separate PC424-D obligation remains open.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
