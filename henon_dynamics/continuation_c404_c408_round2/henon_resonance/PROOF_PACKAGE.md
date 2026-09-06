# Resonant Hénon–Frobenius counts: proof package

Date: 2026-09-06. Status: **PROVABLE AS STATED**, by the complete arguments below. This is one unnumbered candidate, not a released paper or a formal Route-A evaluation. The analytic statements are consequences of the same counting theorem, not separate paper contracts. Independent review and bounded primary-source comparison remain separate admission gates.

## 1. Claim and exact contract

Let $q=p^e$ be a prime power, let $K=\overline{\mathbb F}_q$, and choose

$$
a\in\mathbb F_q^*,\qquad g\in\mathbb F_q[y],\qquad
2\le m:=\deg g<q,\qquad p\nmid m.
$$

All lower coefficients of $g$ are unrestricted. Write $b\in\mathbb F_q^*$ for its leading coefficient. On the entire affine plane $\mathbb A^2(K)$ set

$$
H(x,y)=(y,y^q+g(y)-a x),\qquad
\Phi(x,y)=(x^q,y^q),\qquad S=H^{-1}\circ\Phi.
$$

The clock is one positive integer $n$. The observable is the number of geometric points of the coincidence scheme

$$
E_n=\{H^n(P)=\Phi^n(P)\}\subset\mathbb A^2_K,
\qquad N_n=\#E_n(K).
$$

This is neither the count of ordinary $H$-periodic points over a fixed finite field nor a fixed-variety Hasse–Weil count. It is also exactly the fixed scheme of $S^n$.

**Theorem 1 (all resonant periods).** For every map above and every $n\ge1$, put

$$
r=p^{v_p(n)},\qquad s=n/r,\qquad Q=q^n.
$$

Then $E_n$ is finite and reduced, and

$$
\boxed{
N_n=\frac{(m-1)q^{2n}+(q-m)q^{2n-r}}{q-1}.
}
$$

More precisely, the two literal affine fixed equations have unique highest homogeneous terms

$$
H_1^{(n)}-x^Q:\ -x^Q,
\qquad
H_2^{(n)}-y^Q:\ s b^r\overline m^{\,r-1}y^{d_n},
$$

where $\overline m$ denotes the image of $m$ in $\mathbb F_p$ and

$$
d_n=q^{n-r}D_r,\qquad
D_j=\frac{(m-1)q^j+(q-m)}{q-1}\quad(j\ge1).
$$

Thus their actual degrees are $Q$ and $d_n$, and their leading forms have no common projective point at infinity. The formula depends only on $q,m,n$, not on $a$, $b$, or any lower coefficient.

**Theorem 2 (the same system's zeta).** Define

$$
Z_S(t)=\exp\!\left(\sum_{n\ge1}N_n\frac{t^n}{n}\right),
\quad A=\frac{m-1}{q-1},\quad B=\frac{q-m}{q-1},\quad u=q^2t.
$$

As analytic germs at zero, and with every logarithm normalized to vanish there,

$$
Z_S(u/q^2)
=(1-u)^{-m/q}\prod_{k\ge1}(1-u^{p^k})^{e_k},
\qquad
e_k=\frac{B}{p^k}\bigl(q^{-p^{k-1}}-q^{-p^k}\bigr)>0.
$$

The product converges on $|u|<1$. For every fixed integer $M\ge1$, the circle $|t|=q^{-2}$ is a natural boundary even for meromorphic continuation of $Z_S(t)^M$. In particular, $Z_S$ is not rational or algebraic over $\mathbb C(t)$.

## 2. Proof strategy, classical inputs, and proposed increment

The decisive device is the difference of two commuting **linear pullback operators on a polynomial ring**, not the difference of nonlinear point maps. It permits the characteristic-$p$ binomial identity at exactly the required periods. A leading-degree lemma then controls every cancellation, including all powers of $p$ in the period.

Dependency map:

1. The inverse formula and coefficient field make $H$ commute with $\Phi$, identifying one actual dynamical system $S$.
2. An elementary degree lemma for $\delta=H^*-\Phi^*$ proves the leading term of $\delta^j(y)$ for every positive integer $j$.
3. The characteristic-$p$ binomial identity for commuting linear operators, followed by a difference-of-powers factorization, turns that lemma into the exact degree of $H_2^{(n)}-y^{q^n}$ for every $n$.
4. The classical coprime-leading-monomial criterion and the standard-monomial basis compute the affine quotient length; equivalently one may use plane Bézout after checking no common point at infinity.
5. The Jacobian criterion turns quotient length into geometric point count.
6. A convergent logarithmic series, a $p$-adic divisibility decomposition, and radial orders at roots of unity prove the zeta claims without an algebraic-group theorem.

Classical tools are the polynomial-ring binomial identity, polynomial automorphism differentiation, elementary Gröbner/complete-intersection facts, and elementary analytic continuation. The proposed increment is the coefficient-uniform nonlinear leading-degree lemma and its resulting **all-period resonant count**, especially the complete $p$-divisibility tower. Natural-boundary arguments for distorted periodic counts have prior literature; no priority claim is made for that analytic mechanism in isolation.

## 3. Algebraic setup and the genuine single map

The polynomial inverse is

$$
H^{-1}(x,y)=\bigl(a^{-1}(x^q+g(x)-y),x\bigr).
$$

Every coefficient is in $\mathbb F_q$, so $H\Phi=\Phi H$. It follows that

$$
S^n=H^{-n}\Phi^n,
\qquad
S(x,y)=\bigl(a^{-1}(x^{q^2}+g(x^q)-y^q),x^q\bigr).
$$

Composing the two morphisms in the equalizer with $H^n$ identifies the fixed scheme of $S^n$ with $E_n$, not just their sets of $K$-points.

The map $S$ is a finite radicial morphism, being a polynomial automorphism composed with Frobenius. Its function-field degree is $q^2$, entirely inseparable. This observation identifies the map but does **not** supply its periodic count. In the standard additive structure of $\mathbb A^2$, it is not a group endomorphism: its first coordinate contains the nonzero term $a^{-1}b x^{mq}$, where $mq$ is not a power of $p$. We make no assertion here excluding every possible group conjugacy or quotient presentation.

Let $R=\mathbb F_q[x,y]$, regarded also as an $\mathbb F_q$-vector space. Define

$$
T(f)=f\circ H,\qquad U(f)=f\circ\Phi=f(x^q,y^q)=f^q,
\qquad \delta=T-U.
$$

Both $T$ and $U$ are $\mathbb F_q$-linear ring endomorphisms and commute. Their difference $\delta$ is $\mathbb F_q$-linear, but in general is **not** a ring endomorphism or a derivation. All products and powers of these operators below mean composition as linear operators. In particular,

$$
\delta(y)=g(y)-a x,\qquad \delta(x)=y-x^q.
$$

The identity $U(f)=f^q$ uses every coefficient of $f$ lying in $\mathbb F_q$. Treating arbitrary coefficients in $K$ as if they were fixed by $q$-power Frobenius would invalidate this step.

## 4. The leading-degree lemma

**Lemma 3.** Suppose $P\in R$ has unique highest homogeneous term $c y^D$, with $c\ne0$ and $p\nmid D$. Then $\delta(P)$ has unique highest homogeneous term

$$
c\overline D b\,y^{q(D-1)+m}.
$$

**Proof.** Write $P=c y^D+P_0$, with $\deg P_0\le D-1$, and set $h=g(y)-a x$. Both $T(P_0)$ and $U(P_0)$ have degree at most $q(D-1)$, since the coordinate degrees of $H$ and $\Phi$ are at most $q$.

The remaining difference is

$$
c\bigl((y^q+h)^D-y^{qD}\bigr)
=c\sum_{j=1}^{D}\binom Dj y^{q(D-j)}h^j.
$$

Its $j=1$ term has unique top monomial $c\overline D b\,y^{q(D-1)+m}$, with nonzero coefficient. For $j\ge2$, the degree is at most $q(D-j)+jm$, strictly smaller because $m<q$. The degree bound $q(D-1)$ for $\delta(P_0)$ is also strictly smaller because $m>0$. No other term can cancel the specified monomial. $\square$

**Lemma 4.** For every integer $j\ge1$, the polynomial $\delta^j(y)$ has unique highest homogeneous term

$$
c_jy^{D_j},\qquad c_j=b^j\overline m^{\,j-1}\ne0,
$$

where

$$
D_1=m,\qquad D_{j+1}=qD_j-(q-m),
\qquad
D_j=q^j-(q-m)\frac{q^j-1}{q-1}.
$$

**Proof.** At $j=1$, the claim follows from $\delta(y)=g(y)-a x$ and $m\ge2$. The displayed recurrence implies $D_j\equiv m\pmod p$ for every $j$, hence $p\nmid D_j$. Lemma 3 therefore applies at each induction step. It gives the stated recurrence and $c_{j+1}=c_j\overline m b$. Solving the recurrence gives the displayed closed form. It also proves

$$
0<D_j<q^j.
$$

These inequalities and integrality follow either from the recurrence or from the geometric sum; no divisibility of a rational expression in the field is being assumed. $\square$

This is the point at which $p\nmid m$ is essential. If $p\mid m$, the first binomial term can vanish, and one must calculate a different higher-order term. The theorem does not silently cover that case.

## 5. From operator differences to every period

Fix $n\ge1$ and write $n=rs$ as in Theorem 1. The commuting linear operators $T,U$ belong to an algebra of characteristic $p$. Since $r$ is a power of $p$, the binomial identity in this algebra gives

$$
T^r-U^r=(T-U)^r=\delta^r.
$$

No binomial identity for nonlinear self-maps of $\mathbb A^2$ has been used. The usual difference-of-powers identity in the same commuting algebra gives

$$
T^n-U^n
=\sum_{i=0}^{s-1}T^{ri}U^{r(s-1-i)}\delta^r.
$$

For a polynomial with unique highest homogeneous term $c y^D$, applying either $T$ or $U$ yields unique highest homogeneous term $c y^{qD}$. For $T$, this uses the monic $y^q$ term of its second coordinate and the degree bound on every lower term; for $U$, it is direct substitution. Constants in $\mathbb F_q$ are unchanged.

By Lemma 4, each summand of the last formula applied to $y$ therefore has unique highest homogeneous term

$$
c_r y^{q^{r(s-1)}D_r}=c_r y^{q^{n-r}D_r}.
$$

There are $s$ such terms. Since $p\nmid s$, their sum has the nonzero top coefficient $s c_r$. Consequently

$$
\deg\bigl(T^n(y)-U^n(y)\bigr)=d_n=q^{n-r}D_r.
$$

On the other hand, $T^n(x)=T^{n-1}(y)$ has degree $q^{n-1}$: induction on the monic Hénon recurrence gives this degree and leading coefficient one. Since $q^{n-1}<Q$, the first fixed polynomial has unique highest homogeneous term $-x^Q$.

At $n=1$, $r=s=1$, and the second equation is exactly $g(y)-a x$. The formula gives $d_1=m$ and $N_1=qm$, consistent with eliminating $y=x^q$ to obtain $g(x^q)-a x=0$. Its derivative is $-a\ne0$; thus even this boundary case has simple roots.

## 6. Quotient length, no hidden infinity correction, and reducedness

Let

$$
F_1=T^n(x)-x^Q,\qquad F_2=T^n(y)-y^Q.
$$

For any graded monomial order, their leading monomials are $x^Q$ and $y^{d_n}$. These are relatively prime. The classical coprime-leading-monomial criterion makes the pair a Gröbner basis, and the standard monomials of its quotient are exactly

$$
x^i y^j,\qquad 0\le i<Q,\quad 0\le j<d_n.
$$

Thus

$$
\dim_K K[x,y]/(F_1,F_2)=Qd_n.
$$

Equivalently, homogenizing the two equations to their **actual** degrees gives leading forms $-x^Q$ and $s c_r y^{d_n}$ on the line at infinity. They cannot vanish together at a point of that projective line. Plane Bézout then gives the same length. The decrease from degree $Q$ to $d_n$ in the second literal equation is precisely the resonant cancellation; applying a degree-$Q$ count before resolving it would be incorrect.

Because $Q$ is a positive power of $p$, the derivatives of $x^Q,y^Q$ vanish. Therefore

$$
\det\frac{\partial(F_1,F_2)}{\partial(x,y)}
=\det D(H^n)=a^n\ne0.
$$

Every point of the finite zero scheme is smooth of dimension zero. Over $K$ its local algebra is $K$, so its scheme length equals the number of geometric points. We conclude

$$
N_n=Qd_n=q^{2n-r}\frac{(m-1)q^r+(q-m)}{q-1},
$$

which proves Theorem 1. $\square$

The argument proves finiteness and reducedness for every period, not merely the periods checked computationally. In particular, no reduced-point/ideal-length substitution is inferred from finite numerical agreement.

## 7. Zeta product and the natural boundary

The normalized count is

$$
\frac{N_n}{q^{2n}}=A+Bq^{-p^{v_p(n)}},\qquad A>0,\quad B>0,\quad A+B=1.
$$

It lies between $A$ and $A+B/q=m/q$. Hence $N_n^{1/n}\to q^2$, and the defining logarithmic series converges absolutely on $|u|<1$ after $u=q^2t$.

For every positive integer $n$, the finite telescoping identity

$$
q^{-p^{v_p(n)}}
=q^{-1}+\sum_{k\ge1}
\bigl(q^{-p^k}-q^{-p^{k-1}}\bigr){\bf1}_{p^k\mid n}
$$

holds. On any closed subdisc $|u|\le\rho<1$, absolute convergence permits insertion in the logarithmic series and interchange of sums. Since

$$
\sum_{p^k\mid n}\frac{u^n}{n}=-\frac1{p^k}\log(1-u^{p^k}),
$$

we obtain

$$
\log Z_S(u/q^2)
=-\frac mq\log(1-u)+\sum_{k\ge1}e_k\log(1-u^{p^k}).
$$

The positive numbers $e_k$ are summable. The log series defining each factor, and hence the product in Theorem 2, converge locally uniformly on $|u|<1$. In particular the resulting analytic function is nonzero there and equals the original germ.

Now let $\xi$ be a primitive $p^a$-th root of unity with $a\ge1$. For $k<a$, $1-\xi^{p^k}\ne0$; also $1-\xi\ne0$. Those finitely many logarithmic moduli stay bounded as $\rho\uparrow1$. For $k\ge a$, $\xi^{p^k}=1$, and

$$
0\le\frac{\log(1-\rho^{p^k})}{\log(1-\rho)}\le1,
\qquad
\lim_{\rho\uparrow1}
\frac{\log(1-\rho^{p^k})}{\log(1-\rho)}=1.
$$

Dominated convergence for the summable positive weights $e_k$ gives the exact radial order

$$
\lim_{\rho\uparrow1}
\frac{\log|Z_S(\rho\xi/q^2)|}{\log(1-\rho)}
=\sigma_a:=\sum_{k\ge a}e_k.
$$

It satisfies

$$
0<\sigma_a\le\frac{B}{p^a}
\sum_{k\ge a}\bigl(q^{-p^{k-1}}-q^{-p^k}\bigr)
=\frac{Bq^{-p^{a-1}}}{p^a}<1,
\qquad \sigma_a\longrightarrow0.
$$

A nonzero meromorphic function near $\xi$ has the form $(u-\xi)^j h(u)$ with an integer $j$ and $h$ holomorphic and nonvanishing at $\xi$. Its radial logarithmic order is therefore the integer $j$. The strictly fractional value $\sigma_a$ excludes a meromorphic continuation of our germ to a neighborhood of $\xi$.

For any fixed integer $M\ge1$, take $a$ sufficiently large that $0<M\sigma_a<1$. The same argument excludes a meromorphic continuation of $Z_S(u/q^2)^M$ at every primitive $p^a$-th root of unity of such orders. These roots are dense on the unit circle: their grids have mesh at most $2/p^a$, because excluding numerators divisible by $p$ removes only isolated grid points. An extension across any nonempty arc would give a neighborhood of one of these forbidden points. This proves the asserted natural boundary for every $M$.

An algebraic function over $\mathbb C(u)$ has only finitely many possible branch points or poles in the finite plane, as follows from its minimal polynomial and discriminant. It cannot have this natural boundary. Theorem 2 follows. $\square$

## 8. Scope, necessary hypotheses, and open risks

- The theorem includes all $n$, every allowed prime power $q$, every nonzero $a,b\in\mathbb F_q$, and every lower coefficient of $g$. There is no exclusion of periods divisible by $p$.
- The hypotheses $2\le m<q$ and $p\nmid m$ are used explicitly. The case $p\mid m$ is not settled by this proof; already the first leading-binomial-term argument fails there. The additive case is not rebranded as the new result.
- The monic $y^q$ term and coefficients in $\mathbb F_q$ are structural assumptions. Arbitrary leading coefficient in that degree or a coefficient field not fixed by $\Phi$ is not included.
- No complete classification of all resonant Hénon maps, arbitrary two-clock resonances, or every inseparable lower degree is claimed.
- The zeta belongs to the fixed-point dynamics of $S$, not to a single finite-type variety under Frobenius alone. Its natural boundary does not contradict Hasse–Weil rationality.
- A finite-dimensional characteristic-zero determinant realization would force rationality and is therefore excluded for this exact periodic observable. No infinite-dimensional operator realization or target arithmetic correspondence is supplied.
- The algebraic-group and distorted-zeta literature must receive its actual scope in the source audit. Standard-coordinate nonadditivity alone is not a proof that every hidden algebraic-group presentation is impossible.
- There is no target Euler factor, root number, zero correspondence, automorphy, Hilbert–Pólya claim, or Route-B promotion here. The current outcome is an exact source-system theorem awaiting independent internal review and admission, not an automatic target-arithmetic success.

The proof was developed within the current AI team. No external model or human-peer-review certification is claimed, and no empirical or bibliographic quota substitutes for the quantified proof.
