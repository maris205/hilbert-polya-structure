# Stabilization of the oriented first AS quotient

2026-09-09 UTC. Separate proof-only corollary allocated by the coordinator. It is not a dependency of the submitted all-level inertia proof, and does not change its frozen bytes. No new mathematical execution or AS coefficient calculation is used.

## Claim and status

For every odd prime $p$, retain the fixed base $K=\overline{\mathbb F}_p((s))$, the native map $P_s(z)=(1+s)z+z^2$, and the canonical small-cycle fields $L_e$ of degree $p^e$ established in [FULL_LOCAL_INERTIA.md](FULL_LOCAL_INERTIA.md). Embed them in one fixed separable closure of $K$.

For each level let $\sigma_e$ be the **one-native-step** automorphism, $\sigma_e\alpha_e=P_s(\alpha_e)$. Define the accepted trace resolvent with its fixed positive translation convention:

$$
w_e=\frac{\alpha_e^{p^e-1}}{M_e'(\alpha_e)},\qquad
y_e=-\sum_{i=0}^{p^e-1}(i\bmod p)\sigma_e^i(w_e),\qquad
a_e=y_e^p-y_e\in K,
$$

so $\sigma_e y_e-y_e=1$. Then

$$
[a_e]=[a_2]\quad\text{in }K/\wp(K)
\qquad\text{for all }e\ge2,
\tag{1}
$$

where $\wp(b)=b^p-b$. Consequently the unique degree-$p$ subfields $F_e$ of $L_e$ satisfy

$$
F_e=F_2\quad(e\ge2),\qquad
L_1\cap L_e=K\quad(e\ge2).
\tag{2}
$$

The intersection statement is also uniform in odd $p$. No formula for the first ramification break of $F_2/K$ at a general prime is asserted here. For $p=3$ only, the accepted pair certificate and (1) give

$$
\operatorname{red}_{\mathrm{AS}}(a_e)=2s^{-4}+s^{-2}
\quad(e\ge2),
\tag{3}
$$

whose degree-$3$ field has break $4$; the separate prime-level field has break $2$.

**Author status: PROVABLE AS STATED from the submitted uniform local proof and accepted AS/ramification interfaces; independent corollary review pending.** The full local proof itself is undergoing its separately allocated review. No new paper, global component conclusion, or higher-Witt-coordinate calculation is claimed.

## Assumptions and dependency map

1. The submitted full local theorem supplies $L_e/K$ cyclic of degree $p^e$ and the canonical perfect matching of the $p$ top clusters at levels $e$ and $2$ for $e\ge3$.
2. The matching is characterized by $v(x-y)>2(p-1)/p$, so it is invariant under absolute Galois and under one native step. Its native equivariance is made explicit below.
3. The accepted trace-one identity supplies $\sigma_e y_e-y_e=1$, with the displayed sign convention. This identifies the AS character with the native rotation index modulo $p$.
4. The E6-accepted second-layer proof gives the exact contact $v(\alpha_2-\beta_1)=2(p-1)^2/p^2$ and $v(P_s^{\circ p}(\alpha_2)-\alpha_2)=2(p-1)$.
5. To distinguish level $1$, use the prime-valuation displacement lemma from the frozen interlevel proof and the cyclic ramification congruence $b_2-b_1=p(u_2-u_1)$, with integer upper breaks. The latter is the Hasse--Arf/Herbrand interface reviewed in Elder--Keating, [Section 2 and Lemma 2.2](https://arxiv.org/html/2503.16830v1), valid over this perfect residue field.

The level-two cluster theorem is a substantive input here, not an assumption that all higher AS representatives happen to be equal. No global cycle transitivity is imported.

## 1. The cluster matching preserves the native orientation

Let $T_e$ be the set of $p$ top clusters of the roots of $M_e$. The full local proof defines the unique perfect matching $\phi_e:T_e\to T_2$ by

$$
\phi_e(C)=D
\quad\Longleftrightarrow\quad
v(x-y)>2(p-1)/p\text{ for some }x\in C,\ y\in D.
\tag{4}
$$

Existence, uniqueness and Galois equivariance are established in Section 4 of that proof. The native map is an isometry on these positive-valuation points. It therefore carries a pair satisfying (4) to another such pair. Uniqueness of the matching gives

$$
\phi_e(P_s C)=P_s\phi_e(C).
\tag{5}
$$

Thus this is an isomorphism of **oriented $C_p$-torsors**: the element $1\in\mathbb Z/p\mathbb Z$ acts by one application of $P_s$ on both sides. It is not merely an unoriented identification of two degree-$p$ fields.

Choose a starting cluster at each level and label the clusters by $i\in\mathbb Z/p\mathbb Z$ using native iteration. Equation (5) says that the matching has the form $i\mapsto i+c$ for one constant phase $c$. A different starting point changes that phase but not the generator $+1$; multiplication of labels by a nontrivial scalar is not allowed by (5).

## 2. Equality of the AS characters with the fixed sign

For $g\in G_K=\operatorname{Gal}(K^{\mathrm{sep}}/K)$, let $\rho_e(g)\in\mathbb Z/p^e\mathbb Z$ be defined by

$$
g(\alpha_e)=P_s^{\circ\rho_e(g)}(\alpha_e).
$$

This is a Galois character into the native rotation group. On $T_e$, its action is translation by $\overline{\rho_e(g)}\in\mathbb Z/p\mathbb Z$. Apply Galois equivariance to the phase-translation description of $\phi_e$:

$$
i+\overline{\rho_e(g)}+c
=i+c+\overline{\rho_2(g)}.
$$

Hence

$$
\overline{\rho_e(g)}=\overline{\rho_2(g)}
\quad\text{for all }g\in G_K.
\tag{6}
$$

The sign in the displayed definition of $y_e$ gives $\sigma_e y_e-y_e=+1$. Since $g$ restricts to $\sigma_e^{\rho_e(g)}$ on $L_e$, iteration yields

$$
g(y_e)-y_e=\overline{\rho_e(g)}.
\tag{7}
$$

Equations (6)--(7) show that $y_e-y_2$ is fixed by every $g\in G_K$. Both elements belong to $K^{\mathrm{sep}}$, so their difference is an element $b_e\in K$. It follows that

$$
a_e-a_2=(y_e-y_2)^p-(y_e-y_2)=\wp(b_e),
$$

which proves (1). This is equality of AS classes, not necessarily equality of the raw scalar Laurent series produced by the two resolvents.

Changing a starting root changes $y_e$ by an element of $\mathbb F_p$; changing a trace-one choice changes its extracted $y_e$ by an invariant translation in $K$. Both preserve its AS class. A sign reversal or nonzero scalar twist would correspond to changing the designated native generator. That change is excluded here: equations (5) and (7) keep one original native step and the same $+1$ translation convention at all levels.

The element $y_e$ is fixed precisely by $\langle\sigma_e^p\rangle$, so $K(y_e)$ is the unique degree-$p$ subfield $F_e$. Because $y_e=y_2+b_e$, we have equality $F_e=F_2$ inside the chosen separable closure, not only abstract isomorphism over $K$.

## 3. The prime-level field is not contained in level two

Put $r=(p-1)/p$ and choose roots $\alpha\in M_2^{-1}(0)$ and $\beta\in M_1^{-1}(0)$. Suppose for contradiction that $L_1\subset L_2$. Then $\eta=\alpha-\beta$ lies in $L_2$. The exact contact formula gives

$$
v_{L_2}(\eta)=p^2v(\alpha-\beta)=2(p-1)^2,
\tag{8}
$$

a positive integer prime to $p$ because $p$ is odd. Let $\sigma\alpha=P_s(\alpha)$ be the native generator of $\operatorname{Gal}(L_2/K)=C_{p^2}$ and put $\tau=\sigma^p$. The subgroup $\langle\tau\rangle$ fixes the unique degree-$p$ subfield, which under the contrary assumption is $L_1$. Therefore $\tau\beta=\beta$, and

$$
v_{L_2}(\tau\eta-\eta)
=p^2v(P_s^{\circ p}(\alpha)-\alpha)
=2p^2(p-1).
\tag{9}
$$

Apply the prime-valuation lemma to (8)--(9). The second lower break $b_2$ of this hypothetical cyclic degree-$p^2$ extension would be

$$
b_2=2p^2(p-1)-2(p-1)^2
=2(p-1)(p^2-p+1).
\tag{10}
$$

Its degree-$p$ quotient is, under the same assumption, the prime-level field of break $p-1$. Quotient compatibility therefore gives its first lower break $b_1=p-1$. But

$$
b_2-b_1=(p-1)(2p^2-2p+1)\equiv-1\pmod p.
\tag{11}
$$

For a cyclic degree-$p^2$ extension, Hasse--Arf gives integer upper breaks $u_1,u_2$, and Herbrand's formula gives $b_2-b_1=p(u_2-u_1)\in p\mathbb Z$. This contradicts (11). Hence $L_1\not\subset L_2$, and since $L_1/K$ has prime degree,

$$
L_1\cap L_2=K.
\tag{12}
$$

Equation (10) is a value under a contradiction hypothesis, not an asserted general-prime formula for the actual second break of $L_2/K$.

If $L_1$ were contained in any $L_e$ with $e\ge2$, cyclicity would identify it with the unique degree-$p$ subfield $F_e=F_2\subset L_2$, contradicting (12). This proves the second statement of (2).

## 4. The certified prime-$3$ specialization and exact scope

At $p=3$, the existing [E2 pair review](../../continuation_round2/reviews/e2_local_as/REVIEW.md) accepts $\operatorname{red}_{\mathrm{AS}}(a_2)=2s^{-4}+s^{-2}$. Equality (1), together with uniqueness of the reduced polar representative over the fixed $K$, yields (3) for all $e\ge2$. This is a theorem consequence of torsor stabilization, not a fresh coefficient computation at those levels.

The degree-$3$ common quotient consequently has break $4$, while the prime-level field has break $2$. No substitution of this prime-$3$ value into a general-$p$ assertion is made. For arbitrary odd $p$, the proved contrast is the field noncontainment (2); computing the general first break is a separate question.

The statements do not assert that $L_2\subseteq L_e$, that the full cyclic fields at all higher levels form a tower, or that higher Witt coordinates stabilize. Only the first **oriented** quotient is identified. The original global cycle-quotient transitivity problem is unaffected.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
