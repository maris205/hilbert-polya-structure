# A canonical eventual quotient tower from the compact local cycle limit

2026-09-09 UTC. New proof-only R5 bridge. Earlier files are read-only. The conclusion strengthens the same integrated local contract and is not a separate paper claim.

## Claim and status

For every odd prime $p$, put

$$
k=\overline{\mathbb F}_p,\qquad K_0=k((s)),\qquad
P=P_s=(1+s)z+z^2.
$$

Fix a separable closure $K_0^{\mathrm{sep}}$, an algebraic closure containing it, and its completion $\mathcal C$. Choose the absolute value so that $0<|s|<1$. Let $\Pi_e\subset K_0^{\mathrm{sep}}$ be the canonical small cycle of ordinary least period $p^e$, and let $L_e=K_0(\Pi_e)$. The accepted full-inertia theorem makes $L_e/K_0$ cyclic of degree $p^e$.

The field $\mathcal C$ is algebraically closed as well as complete, so the complete algebraically closed field hypotheses of the R4 inputs apply. We use the classical completion theorem and the unique-extension/isometric-action facts stated in [Conrad, *Completion of algebraic closure*, Introduction and Theorem 1.1](https://math.stanford.edu/~conrad/248APage/handouts/algclosurecomp.pdf). No fixed-field theorem for the completion is used.

Let $G=G_{K_0}$ with its profinite topology. The native rotation character

$$
\rho_e:G\longrightarrow\mathbb Z/p^e\mathbb Z
$$

is determined by $g\alpha=P^{\circ\rho_e(g)}\alpha$ for $\alpha\in\Pi_e$. Thus one original application of $P$ has label $+1$.

**Theorem.** There is a unique continuous character $\chi_\infty:G\to\mathbb Z_p$ such that

$$
\forall j\ge1\ \exists E_j\ge j\ \forall e\ge E_j\ \forall g\in G:
\qquad \rho_e(g)\bmod p^j=\chi_\infty(g)\bmod p^j.
\tag{T1}
$$

This character is surjective and is the translation character of the native compact cycle limit. For

$$
K_j=(K_0^{\mathrm{sep}})^{\ker(\chi_\infty\bmod p^j)}
\quad(j\ge1),
\tag{T2}
$$

one has $[K_j:K_0]=p^j$, the fields are nested, and the unique degree-$p^j$ subfield of $L_e$ equals $K_j$ for every $e\ge E_j$. Moreover,

$$
K_\infty=\bigcup_{j\ge1}K_j
\quad\text{is Galois over }K_0,
\qquad\operatorname{Gal}(K_\infty/K_0)\simeq\mathbb Z_p,
\tag{T3}
$$

with the quotient map induced by $\chi_\infty$.

**Status: PROVABLE AS STATED relative to the named R4 all-anchor-contact and compact-odometer theorems below. Their separate coordinator acceptance, and independent review of this new bridge, are not presumed from author agreement.** No extra mathematical hypothesis is introduced beyond those two explicit complete inputs and the already accepted local fields.

## Assumptions and dependency map

The inputs actually read are:

1. The reviewed all-level local inertia theorem and oriented first quotient identify $L_e/K_0$, its native character, and a nonzero first character for $e\ge2$. See [full local inertia](../../continuation_round3/a3_interlevel_contacts/FULL_LOCAL_INERTIA.md) and [oriented stabilization](../../continuation_round3/a3_interlevel_contacts/ORIENTED_QUOTIENT_STABILIZATION.md). The later first-quotient conductor calculation is unnecessary here.
2. A1's R4 [all-anchor-contact proof](../../continuation_round4/a1_optimal_cycle_measures/PROOF_PACKAGE.md), SHA256 `038cdb412d1b83b94c1ebcfb742090e3937251225077a0f6842d7933c458174e`, establishes its exact finite identity (MC2) and contact convergence for every allowed multiplier and complete algebraically closed field. We apply it only to $s$ and $\mathcal C$.
3. D1's R4 [compact-limit proof](../../continuation_round4/d1_isometric_cycle_limit/PROOF_PACKAGE.md), SHA256 `e2daa9770024c62e7b7fb09855d4c23eaa0c4cd0aa5416ad268288dbe569aedd`, with its [complete E1 review](../../continuation_round4/reviews/e1_isometric_cycle_limit/REVIEW.md), converts that input to the following facts. Writing
   $$
   S=\bigcup_{e\ge1}\Pi_e,\qquad C=\overline S^{\,\mathcal C},
   $$
   the classical metric space $C$ is compact, and
   $$
   \Omega=\bigcap_{N\ge1}\overline{\bigcup_{e\ge N}\Pi_e}^{\,C}
   \tag{4}
   $$
   is nonempty and compact, with $d_H(\Pi_e,\Omega)\to0$. Also $P(\Omega)=\Omega$, and there is a homeomorphism
   $$
   h:\Omega\longrightarrow\mathbb Z_p,
   \qquad h(Px)=h(x)+1.
   \tag{5}
   $$
   The finite-cycle alternative is excluded by D1's explicit finite-average contact argument. It is not ruled out here by an unverified isolation hypothesis.

The topology is the ordinary absolute-value metric on these compact classical sets; compactness of an ambient classical disk is not assumed. D1's construction uses a cofinal inverse system of finite cyclic quotients of lengths $p^{k_m}$ with $k_m\to\infty$, even if some exponents are skipped.

The proof below adds uniform Galois continuity, the translation character, finite-quotient transfer to every sufficiently late cycle, and the exact algebraic-field consequence. The compact odometer and the contact identity themselves are imported, not re-proved or counted again.

Classical Galois topology and correspondence are as in [Stacks, Section 9.22, Lemmas 9.22.1--9.22.3 and Theorem 9.22.4](https://stacks.math.columbia.edu/tag/0BMI). The compact-group and centralizer facts used below are elementary and proved explicitly. No broad novelty claim is made for these general tools.

## 1. The finite native characters are well-defined

The polynomial $P$ and each canonical small factor are defined over $K_0$, so $G$ preserves every set $\Pi_e$ and commutes with $P$ on it. Since $\Pi_e$ is one native cycle, the rotation index defining $\rho_e$ exists and is unique. Changing a starting root from $\alpha$ to $P^{\circ a}\alpha$ leaves that index unchanged, because

$$
g(P^{\circ a}\alpha)=P^{\circ a}(g\alpha).
$$

Composition adds rotation indices, so $\rho_e$ is a homomorphism. Its action factors through the finite Galois extension $L_e/K_0$, hence it is continuous. Full local inertia makes it surjective. The native generator $\sigma_e$ of $\operatorname{Gal}(L_e/K_0)$ corresponds to $1$.

For $e\ge j$, denote its unique degree-$p^j$ subfield by

$$
F_{e,j}=L_e^{\langle\sigma_e^{p^j}\rangle}.
\tag{6}
$$

As a subfield of $K_0^{\mathrm{sep}}$, this is precisely the fixed field of $\ker(\rho_e\bmod p^j)$. This notation does not assume any relation between $L_e$ and a field at another level.

## 2. Galois acts uniformly continuously on the compact classical closure

Every $g\in G$ extends uniquely from $K_0^{\mathrm{sep}}$ to the chosen algebraic closure: purely inseparable roots have unique images. The valuation on the algebraic closure is the unique extension of the valuation on the complete field $K_0$, so this extension of $g$ is an isometry. It therefore extends uniquely to an isometric field automorphism of $\mathcal C$, with inverse obtained from $g^{-1}$. It commutes with $P$ by continuity.

Since $g\Pi_e=\Pi_e$ for every $e$, it preserves $S$, $C$, every tail closure in (4), and hence $\Omega$. Thus it restricts to a homeomorphism of $\Omega$ commuting with $P$.

The needed joint continuity cannot be replaced merely by the existence of these individual isometries. Here it follows uniformly from algebraic finite nets. Fix a real number $\varepsilon>0$. Compactness of $C$ and density of $S$ give a finite set

$$
A_\varepsilon\subset S
\quad\text{such that every }x\in C\text{ has }|x-a|<\varepsilon
\text{ for some }a\in A_\varepsilon.
$$

Each selected point is separable algebraic over $K_0$. Its stabilizer in $G$ is open; the intersection $U_\varepsilon$ of these finitely many stabilizers is an open subgroup fixing every selected point. For $g\in U_\varepsilon$ and $x\in C$, choose such an $a$. Then

$$
|gx-x|
\le\max\{|gx-ga|,|ga-a|,|a-x|\}
<\varepsilon.
\tag{7}
$$

Thus the action of elements near the identity converges uniformly to the identity on all of $C$, not just pointwise on its algebraic dense subset. For general $g_0\in G$, $x_0\in C$, if $g=g_0u$ with $u\in U_\varepsilon$ and $|x-x_0|<\varepsilon$, then

$$
|gx-g_0x_0|=|ux-x_0|
\le\max\{|ux-x|,|x-x_0|\}<\varepsilon.
$$

This proves continuity of $G\times C\to C$ and its restriction to $G\times\Omega$. In particular, no algebraicity of a limit point was assumed to obtain its orbit-map continuity.

## 3. The Galois action is a canonical translation character

Choose any homeomorphism $h$ as in (5), shifting it by a constant if desired to send a selected $\omega_0\in\Omega$ to zero. For $g\in G$, put

$$
f_g=h\circ g\circ h^{-1}:\mathbb Z_p\longrightarrow\mathbb Z_p.
$$

It is continuous and satisfies $f_g(z+1)=f_g(z)+1$. Every continuous map $f:\mathbb Z_p\to\mathbb Z_p$ with this property is a translation: for each nonnegative integer $m$, induction gives $f(m)=f(0)+m$, and such integers are dense in $\mathbb Z_p$. Taking limits gives $f(z)=f(0)+z$ for every $z$. Therefore there is a unique element $\chi_\infty(g)\in\mathbb Z_p$ such that

$$
h(gx)=h(x)+\chi_\infty(g)
\quad(x\in\Omega).
\tag{8}
$$

Composition in $G$ adds the translation amounts, so $\chi_\infty$ is a homomorphism. It is continuous because

$$
\chi_\infty(g)=h(g\omega_0)-h(\omega_0),
$$

and Section 2 proves continuity of the orbit map.

The character is independent of the chosen origin and of the chosen conjugacy (5). Indeed, if $h'$ is another native conjugacy, $h'\circ h^{-1}$ also commutes with addition by one, so the same argument makes it a translation. Conjugating a translation by a translation does not change its amount. A coordinate change by a unit $u\in\mathbb Z_p^\times$ would send the native $+1$ action to $+u$ and respects (5) only when $u=1$. Thus no scalar or sign ambiguity is present, at any depth.

## 4. Every fixed finite quotient transfers to all sufficiently late cycles

Fix $j\ge1$, and write

$$
q_j:\Omega\longrightarrow\mathbb Z/p^j\mathbb Z,
\qquad q_j(x)=h(x)\bmod p^j.
\tag{9}
$$

This is onto and continuous, with finitely many compact clopen fibers. It is a native cyclic quotient: $q_j(Px)=q_j(x)+1$. By (8), it is also a Galois quotient, with action by translation by $\chi_\infty(g)\bmod p^j$.

This quotient exists for every $j$, even if the chosen metric-radius partitions in D1 skip the size $p^j$. One may choose a cofinal quotient with length $p^{k_m}$ where $k_m\ge j$, then compose its native labels with reduction modulo $p^j$. Refinement preserves those labels, so this is exactly (9). Its fibers may be unions of metric cells; they need not themselves be classes of one originally selected radius relation.

Because the finitely many fibers in (9) are disjoint compact subsets of a metric space, any two of them have a positive minimum distance. Choose $\delta_j>0$ such that

$$
x,y\in\Omega,\quad |x-y|<\delta_j
\quad\Longrightarrow\quad q_j(x)=q_j(y).
\tag{10}
$$

Hausdorff convergence of the full sequence supplies $E_j\ge j$ such that

$$
d_H(\Pi_e,\Omega)<\delta_j
\quad\text{for every }e\ge E_j.
\tag{11}
$$

The threshold depends on $j$ and the fixed system, not on $g$ or a selected subsequence. For every $e\ge E_j$, define

$$
q_{e,j}:\Pi_e\longrightarrow\mathbb Z/p^j\mathbb Z
$$

by choosing any $x\in\Omega$ with $|\alpha-x|<\delta_j$ and setting $q_{e,j}(\alpha)=q_j(x)$. This is well-defined: two choices have mutual distance less than $\delta_j$ by the ultrametric inequality, so (10) gives the same label. It is onto, because the other directed Hausdorff bound in (11) supplies a nearby point of $\Pi_e$ for every point of $\Omega$.

Both equivariances follow from the actual isometries. All the cycle roots lie on the accepted common sphere $|z|=|s|^{(p-1)/p}<1$, so its closure, including $\Omega$, remains in the open unit disk. On this disk,

$$
P(x)-P(y)=(x-y)(1+s+x+y),\qquad |1+s+x+y|=1.
$$

If $x$ is an allowed choice for $\alpha$, then $Px$ is therefore an allowed choice for $P\alpha$. Likewise $gx$ is an allowed choice for $g\alpha$, since $g$ is an isometry preserving $\Omega$. Thus

$$
\begin{aligned}
q_{e,j}(P\alpha)&=q_{e,j}(\alpha)+1,\\
q_{e,j}(g\alpha)&=q_{e,j}(\alpha)+\chi_\infty(g)\bmod p^j.
\end{aligned}
\tag{12}
$$

No globally consistent choice of nearby point is needed; independence of every such choice was proved before equivariance.

On the other hand, by the definition of $\rho_e$ and the first equation of (12),

$$
q_{e,j}(g\alpha)
=q_{e,j}(P^{\circ\rho_e(g)}\alpha)
=q_{e,j}(\alpha)+\rho_e(g)\bmod p^j.
\tag{13}
$$

Comparing (12) and (13) proves (T1), simultaneously for every $g\in G$. Equivalently, the native quotient of the actual cycle $\Pi_e$ by $p^j$-step shifts is isomorphic to (9) as an oriented $\mathbb Z/p^j\mathbb Z$-torsor with Galois action. This is exact eventual equality of characters, not just abstract isomorphism of cyclic fields.

## 5. Surjectivity and the algebraic tower

The continuous image $H=\chi_\infty(G)$ is compact because $G$ is profinite, and is closed in the Hausdorff group $\mathbb Z_p$. Taking $j=1$ in (T1) and any $e\ge\max(E_1,2)$ shows that its reduction modulo $p$ equals the accepted nonzero native first character. Thus $H$ contains a $p$-adic unit $u$. It contains every integer multiple of $u$, whose closure is all of $\mathbb Z_p$, because the integers are dense and multiplication by a unit is a homeomorphism. Since $H$ is closed, $H=\mathbb Z_p$.

Each reduction $\chi_\infty\bmod p^j$ is consequently a continuous surjection onto the finite cyclic group of order $p^j$. Its kernel is open and normal, and the finite Galois correspondence gives the field $K_j$ in (T2), cyclic of degree $p^j$. Equality (T1) identifies its kernel with $\ker(\rho_e\bmod p^j)$ for every $e\ge E_j$. By (6), this proves

$$
F_{e,j}=K_j\qquad(e\ge E_j)
\tag{14}
$$

inside the chosen separable closure.

The kernels for $j+1$ are contained in the kernels for $j$, so $K_j\subset K_{j+1}$. The restriction maps on their cyclic Galois groups are ordinary reductions: they are induced by the same character $\chi_\infty$, not by unrelated choices of generators. The union is Galois, and infinite Galois correspondence gives

$$
\operatorname{Gal}(K_\infty/K_0)
\simeq\varprojlim_j\mathbb Z/p^j\mathbb Z=\mathbb Z_p.
$$

Its kernel in $G$ is $\bigcap_j\ker(\chi_\infty\bmod p^j)=\ker\chi_\infty$, so this is the claimed quotient map. This proves (T2)--(T3).

Finally, uniqueness in the theorem does not depend on selecting the limit as part of the definition. If another continuous character satisfies (T1), fix $j$ and choose an $e$ beyond both of its thresholds. Their reductions then both equal $\rho_e\bmod p^j$. Equality for all $j$ makes the two $\mathbb Z_p$-valued characters identical. $\square$

## Boundaries and verification

The first stabilized field $K_1$ is the already reviewed common degree-$p$ subfield of the levels $e\ge2$, not the separate prime-period field $L_1$. Indeed, choose $e$ beyond $E_1$ and use (14) and oriented first-quotient stabilization. The accepted noncontainment $L_1\cap L_2=K_0$ shows these two fields differ. This illustrates why no identification $K_j=L_j$ or threshold $E_j=j$ was assumed.

The theorem does not say that the fields $L_e$ themselves form a tower, or that any fixed $L_j$ lies in all later $L_e$. Its statement fixes the quotient degree first and only then takes the original cycle level sufficiently large. No quantitative threshold is claimed.

Type-I points of $\Omega\subset\mathcal C$ are classical elements of the completed algebraic closure, not necessarily algebraic over $K_0$. The construction never applies finite Galois correspondence to such a coordinate. All fields in (T2)--(T3) lie in $K_0^{\mathrm{sep}}$ and are defined by continuous character kernels. No theorem identifying fixed fields inside the completion is invoked.

The compact-group argument determines oriented finite quotient characters. It does not calculate a full Witt vector, an all-level ramification sequence, global dynatomic components, or target arithmetic data. The contact identity and the compact odometer remain the named complete R4 dependencies, with their individual review/adjudication gates preserved. This new bridge awaits its own nonauthor review.

Mathematical executions: **zero**. No new agents, old-file or shared-state edits, mathematical runs, Git operations, manuscript/PDF, or external-model call occurred. Only the allocated R5 report and this proof were written.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
