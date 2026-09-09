# Exact first quotient break by compositum ramification

2026-09-09 UTC. Companion to [REPORT.md](REPORT.md).

## Claim and status

For every odd prime $p$, let $L_2$ be the cyclic degree-$p^2$
native small-cycle field for $P_s(z)=(1+s)z+z^2$ over
$K=\overline{\mathbb F}_p((s))$. The unique degree-$p$
subfield $F_2/K$ has lower and upper ramification break

$$
u=2(p-1).
$$

**Status: PROVABLE AS STATED from the accepted R3 field and contact
inputs.** No coefficient of an AS representative is a premise.

## Assumptions and notation

Let $k=\overline{\mathbb F}_p$, $v(s)=1$, and
$r=(p-1)/p$. Choose roots $\alpha$ of $M_2$ and $\beta$
of $M_1$ in one separable closure. The accepted inputs are

$$
\begin{gathered}
L_2=K(\alpha),\quad \operatorname{Gal}(L_2/K)=C_{p^2},
\qquad L_1=K(\beta),\quad\operatorname{Gal}(L_1/K)=C_p,\\
L_1\cap L_2=K,\qquad b(L_1/K)=p-1,\\
v(\alpha)=v(\beta)=r,\qquad
v(\alpha-\beta)=\frac{2(p-1)^2}{p^2}.
\end{gathered}                                                   \tag{1}
$$

The generators on both fields are one application of the same
native polynomial $P=P_s$. Put

$$
B=L_2L_1,\qquad
G=\operatorname{Gal}(B/K)=\langle\sigma\rangle\times
\langle\gamma\rangle\cong C_{p^2}\times C_p,
$$

where $\sigma$ is native on $\alpha$ and fixes $\beta$, and
$\gamma$ fixes $\alpha$ and is native on $\beta$.
The extension is totally ramified, and its integer valuation is
$v_B=p^3v$. Let $\pi$ be a uniformizer, so $O_B=k[[\pi]]$.
Every automorphism fixes $k$ pointwise.

For a nonidentity $g\in G$ define its lower break by

$$
b(g)=v_B(g\pi-\pi)-1.
$$

Let $b_0=\min_{g\ne1}b(g)$ be the first lower break of $B/K$.
It is positive because $G$ is a totally ramified $p$-group.
Write $G_t$ and $G^t$ for lower and upper ramification groups.
The first lower and upper breaks agree.

The unique degree-$p$ subfield $F_2\subset L_2$ has an
unknown positive integer break $u$. Write $w$ for the second
upper break of $L_2/K$. We use the classical facts

$$
w\ge p u,\qquad
(G/H)^t=G^tH/H
\quad\text{for each normal subgroup }H\le G.              \tag{2}
$$

The first statement follows from the cyclic AS–Witt break formula;
the second is Herbrand quotient compatibility. Their equal-
characteristic, perfect-residue hypotheses and the Herbrand
integral convention are checked in
[Elder–Keating, Section 2, Lemma 2.2 and Theorem 2.3](https://arxiv.org/html/2503.16830v1).

## Strategy and dependency map

1. The exact interlevel contact gives an element of valuation divisible
   by $p$ exactly once, all of whose Galois displacements are
   unusually deep.
2. A uniformizer expansion forces a first prime-to-$p$ exponent
   and an order-$p$ first ramification quotient.
3. Finite abelian characters control the compositum filtration,
   including the persistence of its order-$p$ kernel.
4. Exclude $u\le p-1$; then read $u$ from one displacement.

## 1. A common lower bound for every displacement

Set

$$
\eta=\alpha-\beta,\qquad
a=v_B(\eta)=2p(p-1)^2,\qquad
A=2p^2(p-1).
                                                               \tag{3}
$$

In particular $v_p(a)=1$, since $p$ is odd.

For any root $x$ in either native small cycle,

$$
P(x)-x=sx+x^2,\qquad v(P(x)-x)=2r,
$$

because $1+r>2r$. The identity

$$
P(x)-P(y)=(x-y)(1+s+x+y)
$$

preserves distances between positive-valuation cycle points.
Telescoping an arbitrary number of native steps therefore gives
$v(P^i(x)-x)\ge2r$ whenever the displacement is nonzero.
Consequently for every $g\in G$,

$$
v_B(g\eta-\eta)\ge A,                                    \tag{4}
$$

where a zero displacement has valuation $+\infty$. Indeed each
of $g\alpha-\alpha$ and $g\beta-\beta$ has valuation at least
$2r$ before multiplication by $p^3$. The automorphism
$\sigma$ gives the exact equality

$$
v_B(\sigma\eta-\eta)=
p^3v(P(\alpha)-\alpha)=A.                                \tag{5}
$$

The quotient $L_1/K$ has break $p-1$, so quotient
compatibility gives $b_0\le p-1$. Thus

$$
A>a+p b_0,
\qquad
A-\big(a+p(p-1)\big)=p(p-1)>0.                           \tag{6}
$$

## 2. The cancellation lemma

We prove the needed local statement directly. Write

$$
\eta=\sum_{j\ge a}c_j\pi^j,\qquad c_a\ne0,\quad c_j\in k.
$$

For an automorphism with lower break $b$ and leading coefficient
$\theta\ne0$,

$$
g(\pi)=\pi+\theta\pi^{b+1}+\text{higher terms}.
$$

For every positive integer $j$, the characteristic-$p$ binomial
identity gives

$$
v_B(g(\pi^j)-\pi^j)=j+p^{v_p(j)}b.                       \tag{7}
$$

To verify it, write $j=p^\ell j_0$ with $p\nmid j_0$.
After factoring out $\pi^j$, the difference has leading term
$j_0\theta^{p^\ell}\pi^{p^\ell b}$, whose coefficient is
nonzero.

Choose an element with break $b_0$. The initial term $c_a\pi^a$
has displacement order $a+p b_0$. Every later term whose
exponent is divisible by $p$ has displacement order strictly
greater than $a+p b_0$, by (7). Let $n$ be the first exponent
prime to $p$ with $c_n\ne0$, if one exists. Its displacement
has order $n+b_0$.

If no such $n$ exists, or if $n>a+(p-1)b_0$, the initial
term has uniquely smallest displacement order $a+p b_0$,
contradicting (4)--(6). If $n<a+(p-1)b_0$, the term at
$n$ has uniquely smallest displacement order
$n+b_0<a+p b_0<A$, giving the same contradiction.
Therefore

$$
n=a+(p-1)b_0,\qquad p\nmid n,\quad c_n\ne0.               \tag{8}
$$

For each $g\in G=G_{b_0}$, let $\theta(g)$ be the
coefficient of $\pi^{b_0+1}$ in $g(\pi)-\pi$, allowing
$\theta(g)=0$ for later-break elements. Composition of
substitutions shows that $\theta:G\to(k,+)$ is a homomorphism:
the degree-$b_0+1$ coefficients add, and products of correction
terms have larger degree because $b_0\ge1$. Its kernel is
$G_{b_0+1}$. Thus its image has exactly the order of the first
ramification quotient.

By (4)--(6), the coefficient of degree $a+p b_0$ in
$g\eta-\eta$ must vanish for every $g$. Only the terms of
exponents $a$ and $n$ can contribute at this degree. Hence

$$
c_a(a/p)\theta(g)^p+c_n n\theta(g)=0.                     \tag{9}
$$

Both coefficients in (9) are nonzero in $k$: $v_p(a)=1$
and $p\nmid n$. The polynomial in (9) has degree $p$,
so it has at most $p$ roots in $k$. The nonzero finite additive
group $\theta(G)$ is an $\mathbb F_p$-vector space, hence
has order at least $p$. It follows that

$$
[G_{b_0}:G_{b_0+1}]=p.                                  \tag{10}
$$

Finally, let $g$ have later lower break $c>b_0$.
The term at exponent $n$ has displacement order $n+c$.
The initial term has order $a+pc$, and

$$
a+pc-(n+c)=(p-1)(c-b_0)>0.
$$

All other terms with exponent divisible by $p$ have even larger
order, and all other prime-to-$p$ exponents exceed $n$.
The term at $n$ is therefore uniquely smallest, proving

$$
v_B(g\eta-\eta)=n+c
\quad\text{whenever }b(g)=c>b_0.                         \tag{11}
$$

This completes the cancellation lemma. It does not assume that
$\eta$ generates $B$ over $K$.

## 3. Character control of the compositum filtration

Use additive finite characters with values in
$\mathbb Q/\mathbb Z$. Let $\chi$ be the character with
$\chi(\sigma)=1/p^2$ and $\chi(\gamma)=0$, and let
$\lambda(\sigma)=0$, $\lambda(\gamma)=1/p$.
The characters $\chi,p\chi,\lambda$ have upper breaks
$w,u,p-1$, respectively, by quotient compatibility.

For a nontrivial character $\rho$, call its last nontrivial upper
index its break. If two characters have distinct breaks, the break
of their sum is their maximum. Indeed, above the smaller break its
character is already zero on the ramification group, while the
larger-break character is nonzero up to its own break.
The break of a sum is always at most the maximum, even when the
two breaks coincide.

Finite abelian duality gives

$$
G^t=\bigcap_{\rho:\,\operatorname{break}(\rho)<t}
\ker(\rho),                                             \tag{12}
$$

including the trivial character without changing the intersection.
To see this, a character is trivial on $G^t$ exactly when its
break is less than $t$; characters of the finite quotient
$G/G^t$ separate its elements.

Put

$$
N=\langle\sigma^p\rangle
 =\operatorname{Gal}(B/F_2L_1).
$$

Every character nontrivial on $N$ has the form
$j\chi+\ell\lambda$ with $p\nmid j$. Its $j\chi$
part has break $w$, because multiplication by a unit modulo
$p^2$ does not change the kernel of $\chi$.

If $u\le p-1$, then (2) gives $w\ge pu\ge p>p-1$.
Thus the character $j\chi+\ell\lambda$ has break exactly
$w$. All characters whose breaks are strictly below $w$ are
therefore trivial on $N$, and (12) proves

$$
N\subseteq G^t\qquad(0\le t\le w).                      \tag{13}
$$

In particular, $N$ persists both at and strictly beyond the
upper index $p-1$.

This is the required kernel-persistence argument. Knowing only
the image of $G^t$ in $\operatorname{Gal}(L_2/K)$ would
not prove (13), because it would not exclude a diagonal subgroup.

The quotient $E=F_2L_1$ has degree $p^2$ over $K$.
All its characters are combinations of $p\chi$ and $\lambda$.
Under $u\le p-1$, all have breaks at most $p-1$, and the
character $\lambda$ has break exactly $p-1$. Thus its last
upper jump is exactly $p-1$.

## 4. Excluding an early first quotient break

Suppose $u\le p-1$. Through and immediately after upper index
$p-1$, equation (13) and quotient compatibility identify all ramification drops
of $G$ with those of the elementary quotient $E/K$.
In particular its first drop has order $p$ by (10).

An elementary group of order $p^2$ with an order-$p$ first
drop must have exactly two distinct jumps: after that first drop
its remaining group has order $p$. Its last upper jump is
$p-1$, so the two jumps are

$$
b_0<p-1,\qquad p-1.
$$

Between them the index of the ramification subgroup in $G$
is $p$. The inverse Herbrand function consequently puts the
second jump at lower index

$$
c=b_0+p(p-1-b_0)>b_0.                                   \tag{14}
$$

Choose an automorphism whose lower break is $c$; such an
element exists because there is a drop at this index.
Equations (8), (11), and (14) give

$$
v_B(g\eta-\eta)
=n+c
=a+(p-1)b_0+b_0+p(p-1-b_0)
=a+p(p-1)<A,
$$

contradicting (4) and (6). Therefore

$$
u>p-1.                                                  \tag{15}
$$

This argument includes the possibility that $F_2$ and $L_1$
have equal individual breaks but some linear combination of their
characters has a smaller break. No independence of leading AS
coefficients was assumed.

## 5. Reading the exact quotient break

Now (15) and (2) give three distinct character-break levels

$$
p-1<u<w.
$$

The character calculation in Section 3 yields the following
upper ramification groups:

$$
\begin{array}{c|c}
\text{upper index interval}&G^t\\ \hline
0\le t\le p-1&G\\
p-1<t\le u&\langle\sigma\rangle\\
u<t\le w&\langle\sigma^p\rangle\\
t>w&\{1\}.
\end{array}                                             \tag{16}
$$

Indeed all order-$p$ characters involving $p\chi$ with a
nonzero coefficient have break $u$, while the multiples of
$\lambda$ have break $p-1$. Every character nontrivial on
$N$ has break $w$, since its faithful $\chi$ part has that
break and its $\lambda$ part has smaller break.

Thus $b_0=p-1$, and $\sigma$ has lower break

$$
c=(p-1)+p(u-(p-1))>b_0.
$$

Apply (11) to $\sigma$ and use (5), (8):

$$
c=A-n=A-a-(p-1)^2
 =2p(p-1)-(p-1)^2=p^2-1.
$$

Solving the preceding Herbrand equation gives

$$
u=(p-1)+\frac{(p^2-1)-(p-1)}p=2(p-1),
$$

as claimed. Since $F_2/K$ has degree $p$, its unique lower
and upper breaks agree. $\square$

## Corollary and limits

The accepted oriented quotient stabilization gives $F_e=F_2$
inside the chosen separable closure for all $e\ge2$.
Therefore their common break is $2(p-1)$. This determines the
largest pole order of their reduced AS classes, but not its
coefficient or any lower polar coefficient.

No second-break formula for the actual $L_2/K$, higher Witt
coordinates, nested full-field tower, or global component theorem
is asserted here. In particular, the contradiction-only second
break from the R3 field-noncontainment proof is not silently
reclassified as an actual invariant.

## Source subtraction and verification

The local fields, exact cross contact, prime-level break and their
disjointness are accepted R3 inputs. Herbrand compatibility and
the cyclic inequality $w\ge pu$ are classical ramification
theory with the primary-source hypotheses checked above.
The specific cancellation polynomial, root count, and its use in
this compositum are proved in Sections 1--5. The character
argument supplies the nontrivial kernel-persistence step.

Author verification checked the exact valuation factor $p^3$,
$v_p(a)=1$ for all odd $p$, the first-grade coefficient in
(9), uniqueness of the minimum in (11), equality-conductor
cancellation cases, and the upper-to-lower index $p$ in both
regimes. There is no remaining unproved step in this author's
argument; nonauthor review remains separately required.

No mathematical program was executed, and no numerical
specialization is used in the proof.
