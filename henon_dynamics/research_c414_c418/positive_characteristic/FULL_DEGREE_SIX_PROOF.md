# Full-support sextic resonance in characteristic three

2026-09-07. **Author proof status: PROVABLE AS STATED; independent internal
proof/source review and paper-level admission remain pending.** This is an
unnumbered proof-gate artifact. It is not a manuscript, a Route A evaluation
or an additional paper counted from the earlier two-term companion note.

This file is the characteristic-three special-case precursor. The current
review target is [FULL_DEGREE_2P_PROOF.md](FULL_DEGREE_2P_PROOF.md), which
contains the same theorem for every odd prime and lower degree $2p$. The
two files express one contract, not two paper candidates.

## 1. Claim, object and complete quantified family

For every $q=3^e$ with $e\ge3$, every
$a,b_6\in\mathbb F_q^*$ and every $b_5,b_4,b_3,b_2,b_1,b_0\in\mathbb F_q$,
put

$$
g(y)=\sum_{i=0}^6b_i y^i,\quad
H(x,y)=(y,y^q+g(y)-ax),\quad
\Phi(x,y)=(x^q,y^q),\quad S=H^{-1}\Phi.
$$

The domain remains the whole affine plane over $K=\overline{\mathbb F}_q$.
The clock is ordinary positive iteration of the single morphism $S$.
The observable is the number of **distinct geometric points** of

$$
E_n=\{P\in\mathbb A^2_K:H^n(P)=\Phi^n(P)\},\qquad n\ge1.
$$

Define $w=3^{v_3(n)}$. Every $E_n$ is finite and reduced, and its ordinary
point count is

$$
\boxed{N_n=q^{2n-w}D_w}, \tag{1}
$$

where the complete coefficient partition is

$$
D_j=
\begin{cases}
\displaystyle\frac{4q^j+2q-6}{q-1},& b_5\ne0,\\[6pt]
\displaystyle\frac{3q^j+(q-6)3^j}{q-3},& b_5=0.
\end{cases} \tag{2}
$$

Both cases include all lower support, including vanishing $b_4$ and all
constant terms. Coefficients need not lie in the prime field. In particular,
$q=27$ with non-prime-field leading coefficient and determinant is included.
No additional coefficient ties or exceptions are omitted from this family.
The theorem does not assert a classification for $q=9$ with $b_5\ne0$,
other characteristics, other total lower degrees, arbitrary two-clock
resonances, or the ordinary periodic points of $H$ over a fixed finite field.

There is also a more precise algebraic assertion. On
$R=\mathbb F_q[x,y]$, let $T=H^*$, $U=\Phi^*$ and $\delta=T-U$.
For every $j\ge1$, the unique highest homogeneous term of $\delta^j y$
is $c_jy^{D_j}$, where

$$
c_j=
\begin{cases}
b_6(2b_5)^{j-1},& b_5\ne0,\\
2^{j-1}b_6^{(3^j-1)/2},& b_5=0.
\end{cases} \tag{3}
$$

These coefficients are nonzero in $\mathbb F_q$. The expressions $D_j$
are positive integers, as the recurrences in the proof show.

## 2. Strategy, classical inputs and proposed increment

The count-to-zeta framework, binomial identity for commuting pullbacks,
coprime-leading-monomial criterion and reducedness argument are already in
[C404](../../continuation_c404_c408_round2/henon_resonance/PROOF_PACKAGE.md).
The nonzero-$b_5$ case is the already proved strict-gap companion stratum.
Neither those steps nor an additional natural-boundary corollary is proposed
as an independent paper increment.

The new step here closes the **entire previously missing support stratum**
$b_5=0$, with $b_4,b_3,b_2,b_1,b_0$ arbitrary. After removing one cube
from the operator in a perfected polynomial ring, a leading integral
exponent and one exceptional fractional exponent form a finite invariant.
The fractional term is shown to move strictly below the retained block at
the next step, even when its Hasse-reduced exponent ties the leading one.
This closes the full family (1)–(2), rather than imposing another support gap.

Dependency map:

1. Exact semilinearity and commutation in a concrete perfected polynomial ring.
2. Degree control for every perfected mixed monomial.
3. A two-exponent invariant for $b_5=0$, with a uniform remainder gap.
4. A two-integer-exponent invariant for $b_5\ne0$.
5. Descent to ordinary polynomial degree, all-period conversion and reducedness.

No general theorem on algebraic-group endomorphisms is applied to $H$ or $S$.
Passing to the perfected ring is a proof device, not a change of phase space
or clock and not a claimed polynomial conjugacy of the source maps.

## 3. Polynomial operators and their exact perfection

The coefficients are in $\mathbb F_q$, so $H$ and $\Phi$ commute. Hence
$T$ and $U$ commute as $\mathbb F_q$-linear ring endomorphisms of $R$.
In particular $U(P)=P^q$ for $P\in R$. Their difference $\delta$ is
linear but need not be multiplicative.

Use the explicit perfect domain

$$
\mathcal R=\bigcup_{r\ge0}\mathbb F_q[x^{1/3^r},y^{1/3^r}].
$$

Every element is a **finite** linear combination of monomials
$x^u y^v$, $u,v\in\mathbb Z[1/3]_{\ge0}$, and the usual monomial
representation is unique. There are no infinite formal series in this ring.
It is an integral domain containing $R$ injectively. Define total degree by
$\deg(x^u y^v)=u+v$, maximum over nonzero coefficients, and
$\deg0=-\infty$. Multiplication adds degrees, addition cannot increase
their maximum, and taking a unique cube root divides degree by three.

Let $L(P)=P^3$. Cubing is an automorphism of $\mathcal R$: it is injective
because this is a domain, and surjective because all monomial cube roots
are present and the finite field is perfect. Its restriction to coefficients
has inverse

$$\sigma(c)=c^{1/3}=c^{3^{e-1}},\qquad c\in\mathbb F_q.$$

Both $T$ and $U$ extend uniquely to $\mathcal R$ by taking these unique
roots. For example $T(x^{1/3^r})=T(x)^{1/3^r}$. Every ring homomorphism
commutes with cubing; uniqueness of roots then gives commutation with
$L^{-1}$. Also

$$
\delta(P^3)=(TP)^3-(UP)^3=(\delta P)^3.
$$

Thus $\delta L=L\delta$ and $\delta L^{-1}=L^{-1}\delta$. Define

$$\mathcal D=L^{-1}\delta,\qquad V=L^{-1}T,\qquad W=L^{-1}U.$$

These satisfy $\mathcal D=V-W$ and, for all $j\ge1$,

$$\boxed{\delta^j=L^j\mathcal D^j}. \tag{4}
$$

The equality uses composition of additive operators; it is not a binomial
identity for nonlinear point maps. The maps $V,W$ are ring homomorphisms,
both acting on coefficients by $\sigma$. Consequently

$$\mathcal D(cP)=\sigma(c)\mathcal D(P). \tag{5}
$$

This semilinearity is retained throughout; coefficients are not assumed fixed
by cubing. The operator $\mathcal D$ maps the level-$r$ polynomial ring into
the level-$(r+1)$ ring, so $\mathcal D^j y$ lies at a finite level at most $j$.
Applying $L^j$ in (4) returns an ordinary polynomial in $R$.

## 4. The full zero-b5 stratum

Assume $b_5=0$ and put $Q=q/3$, $B=\sigma(b_6)\ne0$,
$C=\sigma(b_4)$. The generator substitutions above are

$$
\begin{array}{ll}
Vx=y^{1/3},&Wx=x^Q,\\
Vy=y^Q+G(y)-\sigma(a)x^{1/3},&Wy=y^Q,
\end{array}
$$

where

$$
G(y)=By^2+Cy^{4/3}+\sigma(b_3)y+
\sigma(b_2)y^{2/3}+\sigma(b_1)y^{1/3}+\sigma(b_0).
$$

Write $v_0=G(y)-\sigma(a)x^{1/3}$, so $\deg v_0=2$ and

$$v_0=By^2+Cy^{4/3}+v_1,\qquad\deg v_1\le1. \tag{6}$$

### 4.1. Arbitrary perfected mixed remainders

For a monomial $x^u y^v$ with nonnegative exponents in $\mathbb Z[1/3]$,
choose a common denominator $3^r$. Ring-homomorphism compatibility with
the unique roots shows that substitution can be carried out at that finite
level. Since $\deg Vx=1/3$, $\deg Vy=Q$ and
$\deg Wx=\deg Wy=Q$,

$$
\deg V(x^u y^v)\le u/3+Qv\le Q(u+v),\qquad
\deg W(x^u y^v)=Q(u+v).
$$

The coefficient automorphism $\sigma$ does not affect degrees. Taking finite
sums gives, for **every** $P\in\mathcal R$,

$$\deg\mathcal D P\le Q\deg P. \tag{7}$$

The bound does not depend on the denominator level or the number of mixed
monomials. It is therefore an all-height remainder bound, not a truncation
assumption on the perfected series.

### 4.2. Integral leading exponent and exceptional fractional exponent

Let $E\ge2$ be an integer with $E\equiv2\pmod3$, and put
$E'=Q(E-1)+2$. An ordinary finite binomial expansion gives

$$
\mathcal D(y^E)=(y^Q+v_0)^E-y^{QE}
=2B y^{E'}+2C y^{E'-2/3}+R_E,
\qquad\deg R_E\le E'-1. \tag{8}
$$

Indeed the binomial-index-one term is
$2y^{Q(E-1)}v_0$, whose lower remainder has degree at most $E'-1$
by (6). Every binomial index $i\ge2$ has degree at most

$$Q(E-i)+2i=E'-(i-1)(Q-2)\le E'-1,$$

since $Q\ge9$. This establishes the full remainder gap in (8).

For the fractional exponent $E-2/3$, put $M=3E-2$. This is a positive
integer with $M\equiv1\pmod3$. Compatibility with unique cube roots gives
the **finite-polynomial identity**

$$
\mathcal D(y^{E-2/3})
=\left((y^Q+v_0)^M-y^{QM}\right)^{1/3}. \tag{9}
$$

No infinite binomial series is being invoked. In the polynomial inside the
root, the first nonzero binomial term has index one and degree
$Q(M-1)+2$. Terms of larger index have smaller degree, since $Q>2$.
Thus

$$
\deg\mathcal D(y^{E-2/3})
=\frac{Q(M-1)+2}{3}
=Q(E-1)+\frac23=E'-\frac43<E'-1. \tag{10}
$$

This is the decisive control of the possible Hasse-support tie. The
exceptional fractional term cannot re-enter either retained top degree.

### 4.3. Finite invariant and nonzero coefficient recursion

For every $j\ge1$ we claim

$$
\mathcal D^j y=\alpha_j y^{E_j}
+\beta_j y^{E_j-2/3}+R_j,\qquad
\deg R_j\le E_j-1,\quad \alpha_j\ne0, \tag{11}
$$

where

$$
E_1=2,\quad E_{j+1}=Q(E_j-1)+2,\quad
\alpha_1=B,\quad\beta_1=C,
$$

and

$$
\alpha_{j+1}=2B\sigma(\alpha_j),\qquad
\beta_{j+1}=2C\sigma(\alpha_j). \tag{12}
$$

At $j=1$, this is (6). The degree recurrence implies $E_j\equiv2\pmod3$
for every $j$, because $Q$ is divisible by three. Assume (11) at $j$.
Apply (5), (8) and (10) to its first two terms. Apply (7) to $R_j$;
its image has degree at most $Q(E_j-1)=E_{j+1}-2$. The only possible
terms at the two retained degrees therefore arise from the first term
in (11), and their coefficients are exactly (12). The nonzero field
automorphism $\sigma$ and $B\ne0$ imply $\alpha_{j+1}\ne0$.
This proves (11) for all $j$.

If $C=0$, all $\beta_j$ vanish and the same proof holds; no nonvanishing
assumption on $b_4$ was used. Every other coefficient is contained in the
uniform remainder bound. In particular, no specialization to prime-field
coefficients or nonzero lower coefficients is hidden in (12).

Solving the integer recurrence gives

$$E_j=\frac{Q^j+Q-2}{Q-1}.$$

By (4) the degree of the ordinary polynomial $\delta^j y$ is $3^jE_j$,
which is exactly the second case of (2). The other displayed exponent
in (11) becomes $3^jE_j-2\cdot3^{j-1}$, an integer strictly below the
top degree. The entire remainder has degree at most $3^jE_j-3^j$.
This explicitly verifies descent of the leading-term statement to ordinary
polynomials, independently of any identification of perfected point spaces.

Finally let $c_j=\alpha_j^{3^j}$. From (12),
$c_1=b_6$ and $c_{j+1}=2b_6^{3^j}c_j$. Induction yields precisely the
second coefficient formula in (3). This computation also displays the
coefficient Frobenius twists rather than discarding them.

## 5. The full nonzero-b5 stratum

Assume $b_5\ne0$. This section specializes the strict-gap companion proof,
but is included to make the full-family argument self-contained. For every
$j\ge1$ there are a positive integer $D_j$ and a remainder $P_j$ such that

$$
\delta^j y=\lambda_j(b_6y^{D_j}+b_5y^{D_j-1})+P_j,
\quad\deg P_j\le D_j-2,
$$

with $D_1=6$, $\lambda_1=1$ and

$$D_{j+1}=q(D_j-2)+6,\qquad \lambda_{j+1}=2b_5\lambda_j. \tag{13}$$

The initial assertion follows from $\delta y=g(y)-ax$. In the induction,
$D_j-6$ is divisible by $q$, so $v_3(D_j)=1$ and
$D_j-1\equiv2\pmod3$. The first nonzero binomial term of
$\delta(y^{D_j})$ has index three; its degree is
$q(D_j-3)+18$. The binomial-index-one term of
$\delta(y^{D_j-1})$ supplies the required top two terms, at degrees
$d=q(D_j-2)+6$ and $d-1$. The former degree has deficit

$$d-[q(D_j-3)+18]=q-12>1.$$

Higher binomial indices for $y^{D_j-1}$ have deficit at least $q-6>1$.
Also $\deg\delta P_j\le q(D_j-2)=d-6$. All these contributions are
strictly below the retained second term. This proves (13) with no coefficient
cancellation at either retained degree. The bounds hold at $q=27$ and every
larger permitted $q$.

Solving (13) gives the first degree formula in (2), and
$\lambda_j=(2b_5)^{j-1}$ gives the first coefficient formula in (3).
The coefficients $b_4,\ldots,b_0$ and $a$ are unrestricted within the
original assumptions; they enter only the controlled lower-degree remainder.

## 6. All-period conversion and geometric reducedness

The formulas above prove that $\delta^j y$ has a unique top term for
every $j$, with $0<D_j<q^j$. For the zero-$b_5$ case, the upper bound
also follows from $E_j<Q^j$; it starts at $2<Q$ and is preserved by
$E_{j+1}=QE_j-(Q-2)$. For the other case it follows directly from (13).

Write $n=ws$, $w=3^{v_3(n)}$, $3\nmid s$. Because the **linear** operators
$T,U$ commute, the binomial identity gives

$$T^w-U^w=\delta^w,\qquad
T^n-U^n=\sum_{i=0}^{s-1}T^{wi}U^{w(s-1-i)}\delta^w.$$

For any polynomial with unique top monomial $c y^D$, applying $T$ or
$U$ produces unique top monomial $c y^{qD}$. The coefficient is unchanged
because these two operators fix $\mathbb F_q$. All other monomials have
strictly smaller total degree after substitution. Consequently

$$H_2^n-y^{q^n}\text{ has unique top term }
s c_w y^{q^{n-w}D_w},\qquad s c_w\ne0.$$

The first fixed polynomial $H_1^n-x^{q^n}$ has unique top term
$-x^{q^n}$, since $\deg H_1^n=q^{n-1}<q^n$. The two leading monomials
are relatively prime in every graded order. The classical coprime-monomial
Gröbner criterion makes the two polynomials a Gröbner basis, with standard
monomials

$$x^u y^v,\qquad 0\le u<q^n,\quad0\le v<q^{n-w}D_w.$$

Thus the finite affine quotient has length $q^{2n-w}D_w$. Homogenization
to these actual degrees gives no common point at infinity.

Since $q^n$ powers have zero derivatives, the Jacobian determinant of the
two fixed equations is $\det DH^n=a^n\ne0$. Over the algebraically closed
field each local algebra is therefore a reduced point. This converts length
to the ordinary geometric point count (1), without an unproved transversality
assumption at wild periods. Finally, $H\Phi=\Phi H$ identifies this scheme
with $\operatorname{Fix}(S^n)$. This completes the claimed theorem. $\square$

## 7. Analytic consequence and its inherited mechanism

For the stated source observable, set
$Z_S(t)=\exp(\sum_{n\ge1}N_nt^n/n)$. Formula (1) can be written

$$\frac{N_n}{q^{2n}}=A+B\theta^{3^{v_3(n)}},$$

where

$$
(A,B,\theta)=
\begin{cases}
(4/(q-1),(2q-6)/(q-1),1/q),&b_5\ne0,\\
(3/(q-3),(q-6)/(q-3),3/q),&b_5=0.
\end{cases}
$$

In each case $A,B>0$, $0<\theta<1$, and $A+B\theta=6/q$.
The same elementary logarithmic-series calculation used in C404 gives

$$
Z_S(u/q^2)=(1-u)^{-6/q}
\prod_{k\ge1}(1-u^{3^k})^{e_k},\qquad
e_k=\frac B{3^k}(\theta^{3^{k-1}}-\theta^{3^k})>0.
$$

The product is understood as the germ with logarithms zero at the origin;
it converges locally uniformly for $|u|<1$. To check that the source
natural-boundary conclusion still applies, at a primitive $3^a$th root
of unity the radial logarithmic order is $\sum_{k\ge a}e_k>0$, by
dominated convergence. This tail tends to zero. For any fixed positive
integer $M$, the corresponding order for $Z_S^M$ is eventually strictly
between zero and one, whereas a nonzero meromorphic function has integral
order. Such roots are dense, so $|t|=q^{-2}$ is a meromorphic natural
boundary for every positive integer power of the source zeta. This analytic
mechanism is credited to the previous proof and its classical source audit;
the new count classification is the proposed increment.

## 8. Verification and admission boundaries

This continuation used symbolic invariant arguments, not a larger finite
census. The previously executed $q=27$ monomial and nonzero-$b_5$ diagnostics
are consistent with (2), but do not verify the new zero-$b_5$ full-support
lemma. Its proof is Sections 3–4, including arbitrary perfected mixed
remainders, fractional binomial descent and semilinear coefficients.

The proof closes all coefficient strata **inside the declared family**.
It does not justify claims for $q=9,b_5\ne0$, vanishing $b_6$ or $a$,
other lower degrees, characteristic other than three, or non-Frobenius-fixed
coefficient fields. No generic inverse-tree result is used for a forward
specialization claim. No universal all-polynomial Hasse automaton is claimed.

Bounded prior-source subtraction remains [SOURCE_AUDIT.md](SOURCE_AUDIT.md).
The absence of an exact owner in that limited search is not worldwide
priority evidence. Root's independent internal proof/source/substance
review is a separate pending gate. No paper number, manuscript, evaluator,
registry or global state is changed by this author proof.

All claims are source-local. There is no target Euler factor, root number,
automorphy, zero/divisor correspondence, Hilbert–Pólya realization or Route B
claim. AI-assisted discovery and proof construction are disclosed; neither
the author's checks nor current-team review is human peer review.
