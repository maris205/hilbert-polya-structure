# Ramification consequences of the existing $(3,2)$ certificate

2026-09-09 UTC. Proof-only deduction from the existing pair certificate; no additional mathematical execution. The two author runs and input scope are in [PROOF_SUPPLEMENT.md](PROOF_SUPPLEMENT.md). The complete [E2 review](../reviews/e2_local_as/REVIEW.md), read before finalizing this file, accepts that certificate after one separately authorized independent calculation. Independent review of the present ramification deduction is still a separate obligation.

## Claim and status

Assume the computer-assisted certificate for $(p,e)=(3,2)$ is valid. Let $L=K(\alpha)$ be its totally ramified cyclic degree-$9$ root field, with $K=\overline{\mathbb F}_3((s))$, $v(s)=1$, and $\sigma\alpha=P_s(\alpha)$. Then:

$$
\begin{aligned}
v(P_s(\alpha)-\alpha)&=4/3, &
v(P_s^{\circ3}(\alpha)-\alpha)&=4,\\
(b_1,b_2)&=(4,28), & (u_1,u_2)&=(4,12),\\
d_{L/K}&=88, &
\operatorname{length}_R(O_L/R[\alpha])&=28.
\end{aligned}
\tag{1}
$$

Here $b_i$ and $u_i$ are the lower and upper ramification breaks, $d_{L/K}$ is the different exponent in the integer-normalized valuation $v_L=9v$, and $R=\overline{\mathbb F}_3[[s]]$.

**Status: PROVABLE AS STATED from the accepted recorded pair certificate; author proof awaiting its own independent review.** No uniform all-level consequence is asserted. In particular, the field different $88$ is not the polynomial discriminant valuation $144$.

## Assumptions and dependency map

The exact pair inputs are $v(\alpha)=2/3$, $\operatorname{Gal}(L/K)=\langle\sigma\rangle=C_9$, $v_s\operatorname{Disc}(M_2)=144$, and the degree-$3$ quotient class

$$
\operatorname{red}_{\mathrm{AS}}(a_2)=2s^{-4}+s^{-2}.
\tag{2}
$$

1. The quadratic difference identity gives all distances within each prime-to-$3$ step class.
2. The product defining the polynomial discriminant then determines the three-step distance exactly.
3. The AS quotient in (2) and quotient-compatible ramification numbering determine the first break.
4. The first two native distances recover the earliest exponent of $\alpha$ prime to $3$ in a uniformizer, and then the second break.
5. Classical different and discriminant-index identities give the last line of (1).

The ramification conventions and quotient statements used here are those of Elder--Keating, [Section 2, Lemmas 2.1--2.2](https://arxiv.org/html/2503.16830v1). Their hypotheses allow arbitrary perfect residue fields, including the algebraic closure used here. These standard ramification results are source-owned; the deduction below concerns this one certified dynamical field.

## 1. Distances determined by the polynomial discriminant

Put $r=2/3$. All nine orbit points have valuation $r$, and

$$
P_s(x)-P_s(y)=(x-y)(1+s+x+y).
\tag{3}
$$

The second factor is $1$ modulo elements of positive valuation. Thus every native iterate preserves distances between the orbit points, and its quotient of differences is $1$ modulo positive valuation.

For a positive integer $a$ not divisible by $3$, telescoping gives

$$
P_s^{\circ a}(\alpha)-\alpha
 =\sum_{j=0}^{a-1}\bigl(P_s^{\circ(j+1)}(\alpha)-P_s^{\circ j}(\alpha)\bigr).
$$

Each summand divided by $P_s(\alpha)-\alpha$ has residue $1$, by (3). The residue of the sum of these quotients is $a\ne0$ in characteristic $3$. Hence all six differences for $a\in\{1,2,4,5,7,8\}$ have valuation

$$
v(P_s(\alpha)-\alpha)
=v(s\alpha+\alpha^2)=2r=4/3.
\tag{4}
$$

The same telescoping argument, now using three-step iterates and two summands, shows that the differences at steps $3$ and $6$ have one common valuation $D$.

Since the roots of $M_2$ are exactly this orbit, its derivative at $\alpha$ is the product of all eight differences. The other derivative values have the same valuation by (3). The certificate $v_s\operatorname{Disc}(M_2)=144$ therefore gives

$$
144=9\bigl(6\cdot(4/3)+2D\bigr),\qquad D=4.
\tag{5}
$$

No valuation of a field discriminant has been substituted in this calculation.

## 2. First lower break from the actual degree-$3$ quotient

The trace resolvent satisfies $\sigma y_2-y_2=1$, so $K(y_2)=L^{\langle\sigma^3\rangle}$. Equation (2) has highest pole $4$, prime to $3$. The AS break formula gives the unique break $4$ of that degree-$3$ quotient field. Compatibility of upper numbering with quotients, together with equality of the first upper and lower breaks, gives

$$
b_1=u_1=4.
\tag{6}
$$

This quotient is not identified with the separate native period-$3$ field, whose accepted break is $2$.

## 3. A forced uniformizer exponent and the second break

Choose a uniformizer $t$ of $L$. Since $k=\overline{\mathbb F}_3$ is fixed pointwise and $L$ is complete with residue field $k$, write $O_L=k[[t]]$. By (6),

$$
\sigma(t)=t+c t^5+\text{higher terms},\qquad c\in k^\times.
$$

For any positive integer $a$, and for an automorphism $\tau$ with $v_L(\tau t-t)=b+1$ and $b\ge1$, the binomial identity in characteristic $3$ gives the exact formula

$$
v_L(\tau(t^a)-t^a)=a+3^{v_3(a)}b.
\tag{7}
$$

Indeed, write $a=3^j a_0$ with $3\nmid a_0$ and $\tau(t)=t(1+u)$, $v_L(u)=b$. Then $(1+u)^a-1=(1+u^{3^j})^{a_0}-1$ has leading term $a_0u^{3^j}$, with nonzero coefficient.

Now $v_L(\alpha)=6$, so

$$
\alpha=A_6t^6+A_7t^7+A_8t^8+\sum_{a\ge9}A_at^a,
\qquad A_6\ne0.
$$

For $\tau=\sigma$ and $b=4$, formula (7) gives orders $18$, $11$, and $12$ for the differences of $t^6,t^7,t^8$, respectively. Every term of exponent $a\ge9$ has difference order at least $a+4\ge13$. These lower bounds tend to infinity, so the infinite tail also lies in $t^{13}k[[t]]$ and cannot change either of the two lower coefficients. Equation (4) says $v_L(\sigma\alpha-\alpha)=12$. The unique possible order-$11$ term must therefore be absent, and an order-$12$ term must be present:

$$
A_7=0,\qquad A_8\ne0.
\tag{8}
$$

Let $b_2=v_L(\sigma^3t-t)-1$ be the second lower break. The cyclic degree-$9$ filtration has two distinct breaks, so $b_2>b_1=4$. Applying (7) to $\tau=\sigma^3$, the $t^6$ term has difference order $6+3b_2>8+b_2$; the $t^7$ term is absent; the nonzero $t^8$ term has order $8+b_2$; and the entire later tail has order at least $9+b_2$. Thus the order-$8+b_2$ coefficient cannot cancel, and (5) implies

$$
36=v_L(\sigma^3\alpha-\alpha)=8+b_2,
\qquad b_2=28.
$$

The relation $b_2-b_1=3(u_2-u_1)$ yields $u_2=12$.

## 4. Different and order index

The lower ramification groups have orders $9$ for integer indices $0\le i\le4$, orders $3$ for $5\le i\le28$, and order $1$ thereafter. The different formula gives

$$
d_{L/K}=\sum_{i\ge0}(|G_i|-1)=5\cdot8+24\cdot2=88.
\tag{9}
$$

Equivalently, a uniformizer generates the ring of integers of this totally ramified extension; its minimal polynomial derivative has valuation equal to the sum of the eight uniformizer-conjugate distances, namely $6(4+1)+2(28+1)=88$.

Both $R[\alpha]$ and $O_L$ are full $R$-lattices of rank $9$. Changing from an integral basis of $O_L$ to the monic basis of $R[\alpha]$ multiplies the trace-form determinant by the square of the basis-change determinant. The valuation of that determinant is the lattice quotient length. The residue degree is $1$, so the field discriminant exponent equals the different exponent. Consequently

$$
144=88+2\operatorname{length}_R(O_L/R[\alpha]),
$$

which proves the index length $28$ and completes (1).

## Scope and remaining risk

This calculation depends on the existing single-pair AS/discriminant certificate, now accepted by E2. The present deduction still requires its own independent review. It is not another mathematical execution, a new Witt-coordinate computation, an all-level ramification pattern, or a global component result. It gives an explicit control showing why polynomial discriminant and field different must be kept distinct.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
