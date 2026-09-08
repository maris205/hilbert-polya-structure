# Bounded proof and collision package

Date: 2026-09-07. These are scout certificates, not a manuscript and not an admission. The original contracts are in [FROZEN_CONTRACTS.md](FROZEN_CONTRACTS.md).

## Claims and statuses

1. PC3-A: for every odd prime $p$, classify the ordinary Artin–Mazur zeta function of $f_p(z)=z^p+1/z$ on $\mathbb P^1(\overline{\mathbb F}_p)$. The tested conjecture is nonrationality for every $p$. Status: **NOT CURRENTLY JUSTIFIED**. Only structural and first-return checks below are proved.
2. PC3-B: for every ordinary elliptic curve $E/\overline{\mathbb F}_p$, odd $p$, $g\ge2$, and $A\in M_g(\mathbb Z)$ with nonzero determinant and no root-of-unity eigenvalue, classify the ordinary fixed-point counts and rationality of the induced map on $E^g/\{\pm1\}$. Status: **PROVABLE AS STATED**, as a short consequence of existing algebraic-group/FAD results. Research disposition: **REJECT — SHORT CLASSICAL COMPANION**.

Both conclusions concern the full original clock. No tame zeta function, iterate-only replacement, weighted point count, or finite-field table is substituted for the observable.

## Assumptions and notation

All geometric points are distinct points over $k=\overline{\mathbb F}_p$. For a map $f$, write $N_f(n)=\#\operatorname{Fix}(f^n)$ and

$$Z_f(t)=\exp\left(\sum_{n\ge1}N_f(n)\frac{t^n}{n}\right).$$

For a nonzero integer $a$, put $|a|_p=p^{-v_p(a)}$. In PC3-B write

$$D_\pm(n)=\det(A^n\pm I_g),\qquad K_\pm(n)=\#\ker(A^n\pm I_g:E^g\to E^g).$$

The eigenvalue restriction implies $D_\pm(n)\ne0$ for every $n$: an eigenvalue satisfying $\lambda^n=1$ or $\lambda^n=-1$ would be a root of unity. In particular all these kernels are finite, as are all fixed-point sets on the quotient. This also covers integer-matrix automorphisms with $\det A=\pm1$; a degree-greater-than-one hypothesis is not silently added.

## Strategy and dependencies

- PC3-A: local-coordinate ramification checks; the dynamically affine classification; a symbolic repeated-root calculation. The unproved step is an all-cycle wild-return multiplicity theorem.
- PC3-B: orbit-stabilizer counting, integer Smith normal form, ordinary elliptic torsion, an even-exterior-power identity, and the published FAD recurrence obstruction. A subsequence is used only inside a contradiction proof; the theorem and count formula remain on every native $n$.
- Primary theorem dependency for PC3-B: Byszewski–Cornelissen–Houben, [arXiv:2209.00085v2](https://arxiv.org/html/2209.00085v2), Theorem 5.3.1 and §11.3 Proposition 22. Their statements and relevant proofs were actually read. The former puts a confined abelian endomorphism's counts into FAD form; the latter excludes linear recurrence when its distortion exponents do not all vanish.
- The quotient count is already the situation of Lemma 3.1 in [arXiv:1904.04942v1](https://arxiv.org/html/1904.04942v1). The proof below makes its branch-point accounting explicit. Theorem B of that paper is not asserted to cover arbitrary $A$.

## Part A. What is proved for PC3-A

### Step A1. Degree, separability, and the critical orbit

The numerator $z^{p+1}+1$ is coprime to $z$, so $\deg f_p=p+1$. On $k^*$,

$$f_p'(z)=-z^{-2}\ne0.$$

At $z=0$, use the target coordinate $w=1/f_p(z)$:

$$w=\frac{z}{1+z^{p+1}}=z+O(z^{p+2}).$$

Thus $0$ is not critical and maps to infinity. At infinity use $u=1/z$ in both source and target:

$$\frac1{f_p(1/u)}=\frac{u^p}{1+u^{p+1}}.$$

Consequently infinity is fixed and has local degree $p$. It is the unique critical point. Its local fixed-point multiplicity is one for every iterate, because a local map with order at least two minus $u$ has a nonzero linear term. The only critical local degree is $p<p+1$, so there is no totally ramified point anywhere.

This is the continued fraction $[z^p,z]$, within the structural classification of Faber, [Theorem 1.1](https://arxiv.org/html/1102.1433v2). That classification is a structural owner, not a periodic-count theorem.

### Step A2. No dynamically affine conjugacy

Bridy lists the five dynamically affine families, up to projective conjugacy, in [§§1–2](https://arxiv.org/html/1306.5267v2). The polynomial families all have a totally ramified fixed point, while either sign of a power map has a totally ramified point. Step A1 rules out these possibilities.

For a Lattès realization, write $\pi:E\to\mathbb P^1$ and $\psi:E\to E$ for the finite quotient and affine isogeny. The degree identity from $f\pi=\pi\psi$ gives $\deg\psi=p+1$, so $\psi$ is separable and unramified. If infinity were a fixed critical point of such $f$, choose $P$ over infinity. Every $\psi^n(P)$ stays in the finite fiber over infinity. Local-degree multiplicativity would give

$$e_\pi(\psi^n(P))=e_{f^n}(\infty)e_\pi(P)=p^n e_\pi(P).$$

The left side is bounded by $\deg\pi$, a contradiction for large $n$. This works also when the quotient has wild ramification; it uses no tame quotient assumption. Hence $f_p$ is not dynamically affine. This proves only the failure of that direct theorem route, not nonrationality or exhaustive novelty.

### Step A3. The very first count already has a characteristic exception

Finite fixed points are roots of

$$H_p(z)=z^{p+1}-z^2+1.$$

No root is zero. A common root of $H_p$ and $H_p'=z^p-2z$ must satisfy $z^p=2z$ and then $z^2=-1$. Dividing by $z$ gives

$$(-1)^{(p-1)/2}=2\quad\hbox{in }\mathbb F_p.$$

For an odd prime this is possible only when $p=3$. Conversely,

$$H_3(z)=(z^2+1)^2,$$

with two distinct roots, each of multiplicity two. Including the simple fixed point at infinity gives

$$N_{f_p}(1)=\begin{cases}3,&p=3,\\p+2,&p\ge5.\end{cases}$$

This is a symbolic all-prime calculation, not a finite-field experiment. It disproves the shortcut of counting all fixed-point intersection multiplicities as distinct points for every $p$; it does not disprove the frozen nonrationality conjecture.

### Step A4. Exact unclosed obligation

If a finite cycle has native least period $r$, with nonzero coordinates $z_0,\ldots,z_{r-1}$, its multiplier is

$$\mu_C=(f_p^r)'(z_0)=\frac{(-1)^r}{(z_0z_1\cdots z_{r-1})^2}.$$

The product depends on the cycle. Every nonzero multiplier lies in some finite extension of $\mathbb F_p$, hence has a finite order prime to $p$. At returns where the multiplier becomes one, higher local terms determine the intersection multiplicity, and further $p$-power returns require additional information. No uniform formula controlling these data over every cycle, every $p$, and every $n$ has been established here.

In particular the identity

$$N_{f_p}(n)=(p+1)^n+1-\sum_{x\in\operatorname{Fix}(f_p^n)}(m_n(x)-1)$$

with local multiplicity $m_n(x)$ is only a bookkeeping identity, not an all-$n$ count solution. Bridy's general separable-map transcendence statement is Conjecture 1.6, not an available theorem. No inference from that conjecture is used.

**PC3-A disposition: HOLD — all-native-period proof not closed.** No point table or higher-degree polynomial iteration was run because it would not supply the missing lemma.

## Part B. Full PC3-B closure as a classical companion

### Step B1. Ordinary kernel sizes

For any nonsingular integer matrix $B$, its Smith normal form is $UBV=\operatorname{diag}(d_1,\ldots,d_g)$, with $U,V$ unimodular and nonzero $d_i$. The corresponding maps $U,V$ on $E^g$ are automorphisms, so they preserve kernel cardinality. For an ordinary elliptic curve,

$$\#E[d_i](k)=d_i^2p^{-v_p(d_i)}.$$

Indeed the prime-to-$p$ torsion has rank two and the geometric $p$-power torsion has rank one. Multiplying over $i$ yields

$$\#\ker B=(\det B)^2|\det B|_p.$$

Therefore

$$K_\pm(n)=D_\pm(n)^2|D_\pm(n)|_p.$$

This is the ordinary-product specialization of the classical kernel calculation; it is not a new invariant-factor mechanism.

### Step B2. The quotient and branch locus

A quotient point $\{P,-P\}$ is fixed by $f_A^n$ exactly when $A^nP=P$ or $A^nP=-P$. If $P\ne-P$, its orbit has two points; exactly one of the two equations holds for each point, so it contributes two to $K_-(n)+K_+(n)$. If $P=-P$, the two equations agree and it also contributes two to that sum, while defining only one quotient point. Dividing by two gives the exact ordinary count

$$\boxed{N_A(n)=\frac12\left(D_-(n)^2|D_-(n)|_p+D_+(n)^2|D_+(n)|_p\right).}$$

No extra branch-locus correction or deletion is appropriate.

### Step B3. Nilpotence implies rationality

Suppose $\overline A\in M_g(\mathbb F_p)$ is nilpotent. Then $\overline A^n\pm I$ is invertible for every $n$, so both $p$-adic factors in Step B2 are one.

Let $\lambda_1,\ldots,\lambda_g$ be the complex eigenvalues of $A$, with multiplicity. Form the list $\mu_1,\ldots,\mu_{2g}$ by repeating each $\lambda_i$ twice. Expanding the two products gives

$$N_A(n)=\frac{\prod_{j=1}^{2g}(1-\mu_j^n)+\prod_{j=1}^{2g}(1+\mu_j^n)}2
=\sum_{\substack{J\subseteq\{1,\ldots,2g\}\\|J|\ {\rm even}}}\left(\prod_{j\in J}\mu_j\right)^n.$$

Consequently the original zeta function is

$$\boxed{Z_A(t)=\prod_{\substack{J\subseteq\{1,\ldots,2g\}\\|J|\ {\rm even}}}\left(1-t\prod_{j\in J}\mu_j\right)^{-1}.}$$

Repeated eigenvalues cause repeated factors, not an error. The empty subset contributes $(1-t)^{-1}$. The denominator is the product of the characteristic polynomials of the even exterior powers of the integer matrix $A\oplus A$, so it has integer coefficients. This proves rationality over $\mathbb Q(t)$ without a semisimplicity or positivity assumption on $A$.

### Step B4. A return subsequence removes the plus distortion

Suppose instead that $\overline A$ is not nilpotent. It has at least one nonzero eigenvalue over $\overline{\mathbb F}_p$. Let $r$ be a common multiple of the multiplicative orders of all its nonzero eigenvalues; their orders are finite and prime to $p$.

For every $m\ge1$, the eigenvalues of $\overline A^{rm}$ are zero or one, even when the matrix is not semisimple. The eigenvalues of $\overline A^{rm}+I$ are therefore one or two, all nonzero because $p$ is odd. Thus

$$|D_+(rm)|_p=1,\qquad K_+(rm)=\det((A^r)^m+I)^2.$$

The latter sequence is a finite sum of exponential sequences, obtained by expanding the determinant over the eigenvalues of $A^r$ twice. In particular it is linearly recurrent.

### Step B5. The minus distortion cannot disappear

Set $B=A^r$. Regard its eigenvalues in a finite extension of $\mathbb Q_p$ with normalized valuation $v(p)=1$. Because its characteristic polynomial is monic integral, every eigenvalue is integral. At least one is a unit, and all unit eigenvalues have residue one by the definition of $r$.

For each such unit eigenvalue $\beta$, $v(\beta-1)>0$ and $\beta$ is not a root of unity. The binomial theorem gives, for $x$ with $v(x)>0$,

$$v((1+x)^p-1)\ge\min\{1+v(x),pv(x)\}.$$

Iterating this bound shows $v(\beta^{p^k}-1)\to\infty$: while the bound is at most $1/(p-1)$ it increases by a factor $p$, and thereafter it increases by at least one at each step. Nonunit eigenvalues contribute valuation zero to $\beta^{p^k}-1$. Hence

$$v_p\det(B^{p^k}-I)\longrightarrow\infty.$$

Apply the abelian-group count theorem cited in the dependency map to the confined endomorphism $B$ of $E^g$. In its FAD representation,

$$K_-(rm)=\deg(B^m-I)\,r_m|m|_p^{s_m},$$

where $r_m>0$ is a rational gcd sequence and $s_m\ge0$ is an integer gcd sequence of period prime to $p$. Here $\deg(B^m-I)=\det(B^m-I)^2$, while Step B1 shows that the distortion ratio is exactly $|\det(B^m-I)|_p$.

If $s_m$ were identically zero, that ratio would take only finitely many nonzero values because $r_m$ does. This contradicts its convergence to zero along $m=p^k$. Thus the distortion is nontrivial. The FAD recurrence criterion cited above implies that $(K_-(rm))_{m\ge1}$ is not linearly recurrent.

### Step B6. Nonrationality on the original clock

If $Z_A(t)$ were rational, then

$$t\frac{Z_A'(t)}{Z_A(t)}=\sum_{n\ge1}N_A(n)t^n$$

would be rational, so $(N_A(n))$ would be linearly recurrent. An arithmetic subsequence of a linearly recurrent sequence is linearly recurrent: for example, a companion-matrix representation changes its matrix $M$ to $M^r$. Therefore $(N_A(rm))_m$ would be linearly recurrent. Step B2 and Step B4 would then make

$$K_-(rm)=2N_A(rm)-K_+(rm)$$

linearly recurrent, contradicting Step B5.

Combining this with Step B3 proves the full promised classification

$$\boxed{Z_A(t)\in\mathbb Q(t)\quad\Longleftrightarrow\quad \overline A\text{ is nilpotent}.}$$

This argument proves nonrationality, not a natural boundary or nonholonomicity of $Z_A$ itself. Those stronger conclusions are not claimed.

## Source collision and hypotheses that were not smuggled in

Theorem B of the 2019 dynamically affine paper handles scalar multiplication. Its general nonholonomicity theorem has additional hypotheses, including (H2); these were not assumed for $M_g(\mathbb Z)$. For instance, $A=\operatorname{diag}(2,3)$ has no root-of-unity eigenvalue, but the ring generated by $A$ contains the nonzero non-isogeny $A-2I$, so that route is not automatic.

Instead the full matrix classification above combines an already general quotient formula with an already general abelian/FAD obstruction after separating one sign on a subsequence. That is a short classical companion by the batch's substantive-novelty gate. Not locating the literal boxed matrix theorem in a title or abstract is not a novelty certificate.

## Open risks and disposition

- PC3-A needs a proved uniform cycle-multiplier/return-multiplicity mechanism. It is not promoted. The structural non-affineness proof does not establish that no other literature could cover it.
- PC3-B is closed only at the frozen rational/nonrational level. Ordinary $E$ and odd $p$ are used essentially; supersingular curves and $p=2$ are not silently added.
- No independent publication-level review was requested for this rejected companion. This is an internally checked mathematical reduction, not a new admitted result.
- No numerical computation, third deep-screen candidate, old experiment rerun, manuscript, global registry update, or Git operation occurred.
