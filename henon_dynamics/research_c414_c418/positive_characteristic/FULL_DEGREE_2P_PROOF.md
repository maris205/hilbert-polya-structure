# Full-support degree-2p resonant Hénon–Frobenius counts

2026-09-07. **Author status: PROVABLE AS STATED. Independent internal
proof/source/substance review is pending; no paper is admitted or numbered.**
This is one contract, generalizing the degree-six construction. Neither that
special case nor the strict-gap companion is a separate paper.

## 1. Exact family and theorem

Let $p$ be any odd prime, $q=p^e$ with $e\ge3$, and

$$g(y)=\sum_{i=0}^{2p}b_i y^i\in\mathbb F_q[y],\qquad
b:=b_{2p}\ne0,\qquad a\in\mathbb F_q^*.$$

All lower coefficients are unrestricted, including zero; $a,b$ and the
other coefficients need not belong to $\mathbb F_p$. Define

$$H(x,y)=(y,y^q+g(y)-ax),\quad\Phi(x,y)=(x^q,y^q),\quad S=H^{-1}\Phi.$$

The domain is the whole affine plane over $\overline{\mathbb F}_q$.
The clock is every positive iterate $n$ of $S$. The observable is the
ordinary geometric point count of $E_n=\{H^n(P)=\Phi^n(P)\}$, not just
its scheme length or a fixed finite-field permutation count.

Set $T=H^*$, $U=\Phi^*$ and $\delta=T-U$ on $R=\mathbb F_q[x,y]$.
For every $j\ge1$, $\delta^j y$ has unique top term $c_j y^{D_j}$,
where the following partition covers **every** allowed $g$.

**High-support class.** If some $b_i\ne0$ with $p+2\le i<2p$, put
$\ell=\max\{i:p+2\le i<2p,\ b_i\ne0\}$, $c=b_\ell$ and $h=2p-\ell$.
Then

$$D_j=\frac{(\ell-1)q^j+q(h+1)-2p}{q-1},\qquad
c_j=b(c\bar\ell)^{j-1}. \tag{1H}$$

Here $\bar\ell$ is the nonzero residue of $\ell$ in $\mathbb F_p$.

**Low-support class.** If all those coefficients vanish, then

$$g(y)=by^{2p}+c y^{p+1}+R_0(y),\qquad\deg R_0\le p,$$

where $c$ may be zero. In this case

$$D_j=\frac{p q^j+(q-2p)p^j}{q-p},\qquad
c_j=2^{j-1}b^{(p^j-1)/(p-1)}. \tag{1L}$$

All $D_j$ are positive integers and all $c_j$ are nonzero. For every $n$,
write $w=p^{v_p(n)}$. The scheme $E_n$ is finite and reduced, with

$$\boxed{N_n=\#E_n=q^{2n-w}D_w}. \tag{2}$$

The small field boundary $q=p^3$, vanishing $c$, arbitrary constant term,
arbitrary intermediate support and non-prime-field coefficients are included.
The full theorem does not claim $e=1,2$, $p=2$, different lower total
degrees, zero $a$ or $b$, or coefficients not fixed by $q$-Frobenius.

## 2. Dependencies and contribution boundary

The integer strict-gap block, proved in
[PROOF_NOTE.md](PROOF_NOTE.md), and C404's commuting-pullback conversion,
Gröbner length and Jacobian reducedness are inputs already owned within
this stream. Section 3 checks the strict-gap hypotheses for the entire
high-support class. Sections 4–5 prove the missing low-support class by
a finite perfected-ring invariant, including its possible Hasse tie.
Section 6 finishes the count argument explicitly.

The proposed new increment is this **full degree-2p coefficient-family
classification for every odd characteristic**, not the perfection functor,
a new name for C404's coprime-degree formula, or another analytic boundary
mechanism. Source comparison remains bounded; independent admission is not
inferred from the author's proof status.

## 3. High-support class: automatic strict gaps

There is no multiple of $p$ strictly between $\ell>p$ and $2p$. Therefore
the choice of $\ell$ gives exactly $g=by^{2p}+cy^\ell+R$, $\deg R<\ell$,
with $p\nmid\ell$. Here $1\le h\le p-2$ and
$\rho=p^{v_p(2p)}=p$. Since $q\ge p^3$,

$$q-2p>h,\qquad
q(p-h-1)-2p(p-1)\ge p^3-2p(p-1)>p-2\ge h.$$

These are precisely the two strict gaps of the previously proved block
lemma. It gives

$$\delta^j y=(c\bar\ell)^{j-1}y^{A_j}(by^{2p}+cy^\ell)+R_j,
\quad\deg R_j<A_j+\ell,
\quad A_1=0,\quad A_{j+1}=q(A_j+\ell-1).$$

Its top degree is $D_j=A_j+2p$, giving (1H). To restate the controlling
bounds: the leading exponent $A_j+2p$ has $p$-valuation one, so its first
nonzero binomial index is $p$; its image falls more than $h$ below the
leading degree produced by $A_j+\ell$. Higher binomial indices from that
latter exponent fall at least $q-2p>h$ below it. The entire remainder has
degree at most $q(A_j+\ell-1)$ after $\delta$, also below the retained
block. Thus lower support cannot create a top-degree coefficient tie.

## 4. Exact perfected-ring setup for the low-support class

Use the concrete domain

$$\mathcal R=\bigcup_{r\ge0}\mathbb F_q[x^{1/p^r},y^{1/p^r}].$$

Its elements are finite sums of monomials with nonnegative exponents in
$\mathbb Z[1/p]$; no infinite series are used. Give it the rational total
degree, with $\deg0=-\infty$. Its monomial representation is unique,
products add degrees, and taking a unique $p$th root divides degree by $p$.
The inclusion $R\hookrightarrow\mathcal R$ is injective.

Absolute Frobenius $L(P)=P^p$ is an automorphism of $\mathcal R$.
On $\mathbb F_q$ its inverse is the field automorphism
$\sigma(c)=c^{1/p}=c^{p^{e-1}}$. The ring homomorphisms $T,U$ extend
uniquely by taking roots. They commute with $L$ and $L^{-1}$. Moreover

$$\delta(P^p)=(TP)^p-(UP)^p=(\delta P)^p.$$

Thus, for the additive operator $\mathcal D=L^{-1}\delta$,

$$\delta^j=L^j\mathcal D^j,\qquad
\mathcal D(cP)=\sigma(c)\mathcal D(P). \tag{3}$$

This is an operator identity, not a change of the point-map clock or an
assumed polynomial conjugacy. The semilinearity in (3) is essential for
coefficients outside $\mathbb F_p$.

Put $Q=q/p$, $B=\sigma(b)\ne0$, $C=\sigma(c)$ and
$\varepsilon=(p-1)/p$. The two ring homomorphisms $V=L^{-1}T$,
$W=L^{-1}U$ act on coefficients by $\sigma$ and satisfy

$$Vx=y^{1/p},\quad Wx=x^Q,\quad
Vy=y^Q+v_0,\quad Wy=y^Q,$$

where

$$v_0=By^2+Cy^{1+1/p}+v_1,\qquad\deg v_1\le1.$$

Indeed every exponent of $R_0$ is at most $p$, and the determinant term
becomes $-\sigma(a)x^{1/p}$. This explicitly includes $c=0$ and all
non-prime-field coefficients.

For any mixed monomial $x^u y^v$ in $\mathcal R$, choose a common
denominator $p^r$ and compute substitutions by unique roots of ordinary
polynomials. Then

$$\deg V(x^u y^v)\le u/p+Qv\le Q(u+v),\qquad
\deg W(x^u y^v)=Q(u+v).$$

Finite sums and the coefficient automorphism imply the uniform bound

$$\deg\mathcal D P\le Q\deg P\quad(P\in\mathcal R). \tag{4}$$

It is independent of denominator level and of the mixed monomial support.

## 5. Low-support finite invariant: the fractional tie is harmless

Let $E\ge2$ be an integer, $E\equiv2\pmod p$, and set
$E'=Q(E-1)+2$. The finite binomial expansion gives

$$\mathcal D(y^E)=2B y^{E'}+2C y^{E'-\varepsilon}+P_E,
\qquad\deg P_E\le E'-1. \tag{5}$$

The binomial-index-one term is $2y^{Q(E-1)}v_0$. Its remaining part has
degree at most $E'-1$. Every larger index $i\ge2$ has degree at most
$Q(E-i)+2i=E'-(i-1)(Q-2)\le E'-1$. Here $Q\ge p^2\ge9$ and
$2\ne0$ in the odd characteristic.

For the exceptional fractional exponent $E-\varepsilon$, the numerator
$M=p(E-1)+1$ is a positive integer congruent to one modulo $p$. Unique
roots and the ring-homomorphism property give the exact finite identity

$$\mathcal D(y^{E-\varepsilon})
=\left((y^Q+v_0)^M-y^{QM}\right)^{1/p}.$$

Its inner polynomial has first nonzero binomial index one, degree
$Q(M-1)+2$ and a nonzero leading coefficient. Larger indices have smaller
degree. Hence

$$\deg\mathcal D(y^{E-\varepsilon})
=Q(E-1)+2/p=E'-(2-2/p)<E'-1. \tag{6}$$

The strict inequality holds for every odd prime, including $p=3$.
Equation (6) resolves the fractional Hasse-support tie without discarding
its coefficient: this term moves below the entire retained block.

Inductively,

$$\mathcal D^j y=\alpha_jy^{E_j}
+\beta_jy^{E_j-\varepsilon}+P_j,\qquad
\deg P_j\le E_j-1,\qquad\alpha_j\ne0, \tag{7}$$

with

$$E_1=2,\quad E_{j+1}=Q(E_j-1)+2,\quad
\alpha_1=B,\ \beta_1=C,$$

$$\alpha_{j+1}=2B\sigma(\alpha_j),\qquad
\beta_{j+1}=2C\sigma(\alpha_j). \tag{8}$$

The base case is the expression for $v_0$. The recurrence ensures
$E_j\equiv2\pmod p$, since $p\mid Q$. For the induction, apply
(3), (5) and (6) to the first two terms of (7), and (4) to its remainder.
That last contribution has degree at most $Q(E_j-1)=E_{j+1}-2$.
Thus only the leading term generates either retained coefficient, proving
(8); $B\ne0$, $2\ne0$ and bijectivity of $\sigma$ keep it nonzero.
If $C=0$, all $\beta_j$ vanish and the same bounds still hold.

Solving the integer recurrence gives $E_j=(Q^j+Q-2)/(Q-1)$.
The operator $\mathcal D$ increases the denominator level by at most one,
so $\mathcal D^j y$ is at level at most $j$. By (3), its $p^j$th power
is the ordinary polynomial $\delta^j y$. The unique top degree is
$p^j E_j$, giving (1L). The secondary exponent becomes the integer
$p^jE_j-(p-1)p^{j-1}$, strictly below the top; the whole remainder has
degree at most $p^jE_j-p^j$. There is no unresolved descent step.

Finally $c_j=\alpha_j^{p^j}$ obeys $c_1=b$ and
$c_{j+1}=2b^{p^j}c_j$. This proves exactly the coefficient expression in
(1L), including all coefficient Frobenius twists.

## 6. Every period, finite length and ordinary points

Both degree recurrences imply $0<D_j<q^j$. In the low class, use
$2<Q$ and $E_{j+1}=QE_j-(Q-2)$ to obtain $E_j<Q^j$.
In the high class use $D_{j+1}=q(D_j-h-1)+2p<qD_j$ and $2p<q$.

Because $T,U$ commute and fix $\mathbb F_q$, for $n=ws$, $p\nmid s$,

$$T^w-U^w=\delta^w,\qquad
T^n-U^n=\sum_{i=0}^{s-1}T^{wi}U^{w(s-1-i)}\delta^w.$$

Either substitution sends a polynomial with unique top term $c y^D$ to
one with unique top term $c y^{qD}$. All other terms have lower total
degree; coefficients are unchanged by $T,U$, unlike $\mathcal D$.
Thus $H_2^n-y^{q^n}$ has unique top term
$s c_w y^{q^{n-w}D_w}$, with nonzero coefficient. The other fixed
equation has unique top term $-x^{q^n}$ since $\deg H_1^n=q^{n-1}$.

The coprime-leading-monomial Gröbner criterion gives quotient basis
$x^u y^v$, $0\le u<q^n$, $0\le v<q^{n-w}D_w$, and hence length
$q^{2n-w}D_w$. Homogenizing to the actual degrees gives no common point
at infinity. The Jacobian determinant of the fixed equations is
$\det DH^n=a^n\ne0$, because the $q^n$ powers differentiate to zero.
The finite scheme is reduced over the algebraic closure, so its length is
its number of ordinary geometric points. Commutation $H\Phi=\Phi H$
identifies it with $\operatorname{Fix}(S^n)$, proving (2). $\square$

## 7. Source analytic consequence, verification and exclusions

Writing $N_n/q^{2n}=A+B\theta^{p^{v_p(n)}}$, the two classes have

$$
(A,B,\theta)=
\begin{cases}
((\ell-1)/(q-1),(q(h+1)-2p)/(q-1),1/q),&\text{high},\\
(p/(q-p),(q-2p)/(q-p),p/q),&\text{low}.
\end{cases}
$$

Here $A,B>0$, $0<\theta<1$, and $A+B\theta=2p/q$. For the source zeta
$Z_S(t)=\exp(\sum N_nt^n/n)$, C404's logarithmic-series argument gives

$$Z_S(u/q^2)=(1-u)^{-2p/q}
\prod_{k\ge1}(1-u^{p^k})^{e_k},\qquad
e_k=\frac B{p^k}(\theta^{p^{k-1}}-\theta^{p^k})>0.$$

The product converges locally uniformly in $|u|<1$ with logarithms zero
at the origin. At a primitive $p^a$th root with $a\ge1$, its radial logarithmic order is
the positive tail $\sum_{k\ge a}e_k$, tending to zero. Every fixed positive
integer power therefore has nonintegral radial orders at a dense set of
such roots, excluding meromorphic continuation across any arc. Thus
$|t|=q^{-2}$ is a source meromorphic natural boundary. This is an inherited
analytic mechanism, not an additional independent increment.

The follow-up closes the requested theorem by symbolic invariants, not an
expanded census. The earlier degree-six diagnostics are consistency checks
only; they do not verify the new all-prime, all-height or all-coefficient
quantifiers. The finite degree-state proof is Sections 3–5. Independent
review must check it, especially semilinearity, perfected mixed remainders,
fractional binomial descent and the automatic high-stratum gap inequalities.

The proof uses no target Euler factors, root numbers, automorphy, target
zero/divisor correspondence, Hilbert–Pólya realization or Route B authority.
The source audit is bounded and does not certify worldwide novelty. This is
AI-assisted author work; proof review and paper-level admission remain
separate pending gates, not human peer review or a publication certificate.
