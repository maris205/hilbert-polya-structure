# C391 analytic proof: supercritical inverse-square dynamics

## Claim, status, and assumptions

**PROVABLE AS STATED.** Fix $\sigma>0$, $g=\sigma^2+1/4$, and $\kappa\in\mathbb C$ with $|\kappa|=1$. On $\mathcal H=L^2((0,\infty),dx)$ the differential expression is $\ell=-\partial_x^2-g/x^2$. Every self-adjoint realization extending the minimal operator is classified below. Its simple negative spectrum is a bilateral geometric ladder, its remaining spectrum is purely absolutely continuous of multiplicity one, and its scattering and domain-scale cycle are explicit. Ordinary heat and Fredholm determinant constructions fail for specific proved reasons. These classical formulas are attributed to Dereziński--Richard [DR]; this package supplies a convention-complete derivation, source-clock obstruction, and independent reproducibility audit, not priority for the formulas.

Units are $\hbar=2m=1$. The classical source is $h(x,p)=p^2-g/x^2$ on $T^*(0,\infty)$, with its original Hamiltonian time. The quantum evolution is $e^{-itH_{\sigma,\kappa}}$, also with its original time. The extra boundary parameter is physical input; the classical differential expression does not choose it. No ultraviolet cutoff, confining potential, boundary fit, target zero, prime table, or Route B is admitted. The critical case $\sigma=0$ and non-self-adjoint $|\kappa|\ne1$ are outside the theorem, not limits silently included in it.

## Notation and dependency map

Let $D_{\max}=\{f\in L^2:\ell f\in L^2\text{ distributionally}\}$, and let $D_{\min}$ be the graph closure of $C_c^\infty(0,\infty)$. A remainder belongs to $D_{\min}$ near zero if its product with a smooth cutoff equal to one near zero belongs to $D_{\min}$. Define

$$D_\kappa=\{f\in D_{\max}:f-c(\kappa x^{1/2-i\sigma}+x^{1/2+i\sigma})\in D_{\min}\text{ near }0\text{ for some }c\in\mathbb C\}.$$

Write $H_{\sigma,\kappa}=\ell|_{D_\kappa}$, $\varsigma=\kappa\Gamma(-i\sigma)/\Gamma(i\sigma)=e^{i\theta}$, where any real lift $\theta$ is allowed. Powers of a complex spectral momentum use the logarithm in $\operatorname{Re}\rho>0$; powers of a positive momentum use its real logarithm. The functions $I_\nu,J_\nu,K_\nu$ are the ordinary Bessel functions, not the rescaled one-dimensional Bessel notation of [DR].

1. Hamilton's equations give an exact quadratic position law and the incomplete classical clock.
2. Endpoint classification and the boundary form classify every self-adjoint domain.
3. Bessel expansions and their Wronskian give the resolvent and all eigenvalues.
4. Stone's formula gives the continuous spectral measure; [DR, Proposition 6.10] supplies the time-dependent wave-operator limit with its hypotheses checked.
5. Direct dilation of the domain gives the discrete scaling group.
6. The spectral theorem then proves the heat, compactness, and bilateral-zeta obstructions.

## 1. Classical source clock and collision atlas

Hamilton's equations are $\dot x=2p$, $\dot p=-2g/x^3$. The energy $E=p^2-g/x^2$ is conserved. For $y=x^2$,

$$\ddot y=8E,\qquad y(t)=x_0^2+4x_0p_0t+4Et^2,\qquad p(t)=\dot y(t)/(4\sqrt{y(t)}).$$

These identities reconstruct a solution on exactly the connected component of $\{t:y(t)>0\}$ containing zero. Direct differentiation of the reconstruction gives both Hamilton equations. If $E\ne0$, the discriminant of this quadratic is $16g>0$; hence each finite endpoint is a simple zero. If $E=0$, the linear slope is $4x_0p_0=\pm4\sqrt g\ne0$. At negative energy the component is a bounded interval; at nonnegative energy it is a half-line. Every orbit therefore has at least one finite collision endpoint. It has no periodic continuation inside $T^*(0,\infty)$, since $x=0$ is not in the phase space. No bounce or boundary phase is supplied by these equations. A complete quantum unitary group is not a completion of this classical flow without new boundary input.

## 2. Exhaustive self-adjoint boundary classification

The two independent zero-energy solutions are $u_\pm=x^{1/2\pm i\sigma}$. Both are square integrable near zero. Variation of constants for $\ell f=F\in L^2$ gives $f=a u_-+b u_++r$, with $r\in D_{\min}$ near zero: the integrals of $u_\pm F$ converge by Cauchy--Schwarz, and their vanishing tails are $o(x^{3/2})$, with derivative $o(x^{1/2})$. The coefficients are unique modulo the minimal domain. At infinity the real potential is integrable on every tail and the endpoint is limit point. Weyl's limit-point/limit-circle theorem therefore gives deficiency indices $(1,1)$ and no boundary condition at infinity. This also agrees with [DR, Section 2.2].

For $f=a_fu_-+b_fu_+$ and $v=a_vu_-+b_vu_+$ modulo their minimal remainders, the limiting Wronskian is

$$W_0(\overline f,v)=2i\sigma(\overline{b_f}b_v-\overline{a_f}a_v).$$

Green's identity says that the boundary form of $H_{\max}$ equals this expression up to the fixed overall sign determined by which argument is subtracted. Its maximal isotropic lines are exactly $a=\kappa b$, $|\kappa|=1$: a nonzero isotropic vector satisfies $|a|=|b|$, so neither component vanishes, and the ratio is unique. Every such line is maximal because the boundary coefficient space has complex dimension two. Thus the $D_\kappa$ exhaust all self-adjoint extensions, with no identification of different $\kappa$.

There is no Friedrichs extension. To see unboundedness of the minimal quadratic form without using the spectral result, take $f(x)=x^{1/2}\chi(\log x)$ for real $\chi\in C_c^\infty(\mathbb R)$. Substitution $s=\log x$ gives

$$\langle f,\ell f\rangle=\int_{\mathbb R}(|\chi'(s)|^2-\sigma^2|\chi(s)|^2)\,ds.$$

A long plateau makes this negative. Normalized dilations move this same negative value to arbitrarily large negative magnitude. Since every extension contains $D_{\min}$, none is semibounded. Complex conjugation preserves $D_\kappa$: the transformed coefficients have ratio $1/\overline\kappa=\kappa$. It commutes with $H_{\sigma,\kappa}$ and reverses $e^{-itH}$ in the usual position-preserving sense.

## 3. Green function, all negative levels, and normalization

For $z=-\rho^2$, $\operatorname{Re}\rho>0$, put $T_\rho=\varsigma(\rho/2)^{2i\sigma}$,

$$u_\rho(x)=\sqrt x\,[I_{i\sigma}(\rho x)-T_\rho I_{-i\sigma}(\rho x)],\qquad v_\rho(x)=\sqrt x\,K_{i\sigma}(\rho x).$$

The small-argument expansions and $\Gamma(1\pm i\sigma)=\pm i\sigma\Gamma(\pm i\sigma)$ give the coefficient ratio $\kappa$ for $u_\rho$. The large-argument decay selects $v_\rho$ uniquely at infinity. The identities $W_x(\sqrt x I_{\pm i\sigma}(\rho x),\sqrt x K_{i\sigma}(\rho x))=-1$ give $W(u_\rho,v_\rho)=T_\rho-1$. Consequently

$$G_\kappa(-\rho^2;x,y)=\frac{u_\rho(\min(x,y))v_\rho(\max(x,y))}{1-T_\rho}.\tag{1}$$

The derivative jump is $-1$, as required for $-\partial_x^2$. Near zero the kernel is bounded by a constant times $\sqrt{xy}$ on compact squares; on tails the usual exponential Green-kernel bounds imply boundedness on $L^2$. The formula therefore gives the inverse when $T_\rho\ne1$. If $T_\rho=1$, its decaying factor satisfies the boundary condition and is an eigenfunction. For $\rho$ in the right half-plane, $|T_\rho|=e^{-2\sigma\arg\rho}$, so $T_\rho=1$ forces $\rho>0$.

Since

$$K_{i\sigma}(w)=\tfrac12\Gamma(i\sigma)(w/2)^{-i\sigma}+\tfrac12\Gamma(-i\sigma)(w/2)^{i\sigma}+o(1),$$

the condition is equivalent to the complete ladder

$$E_j=-\rho_j^2=-4\exp[-(\theta+2\pi j)/\sigma],\qquad j\in\mathbb Z.\tag{2}$$

A lift change $\theta\mapsto\theta+2\pi$ only reindexes $j$. The eigenvalues are simple because there is one square-integrable solution at infinity. They approach zero as $j\to+\infty$ and minus infinity as $j\to-\infty$; none is a ground state. The derivative of $1-T_\rho$ is nonzero at each root, giving simple resolvent poles as well. There are no further negative spectral points by (1).

The identity

$$\int_0^\infty xK_{i\sigma}(\rho x)^2\,dx=\frac{\pi\sigma}{2\rho^2\sinh(\pi\sigma)}$$

has the following direct derivation. For $f_a(x)=\sqrt xK_{i\sigma}(ax)$ and $f_b(x)=\sqrt xK_{i\sigma}(bx)$, $a,b>0$, $a\ne b$, the equation gives $W(f_a,f_b)'=(b^2-a^2)f_af_b$. The Wronskian vanishes at infinity. The two small-argument coefficients above give $W_0=\sigma|\Gamma(i\sigma)|^2\sin(\sigma\log(a/b))$. Since $|\Gamma(i\sigma)|^2=\pi/(\sigma\sinh\pi\sigma)$, integration yields

$$\int_0^\infty xK_{i\sigma}(ax)K_{i\sigma}(bx)\,dx=\frac{\pi\sin(\sigma\log(a/b))}{(a^2-b^2)\sinh(\pi\sigma)}.$$

Taking $b\to a$ proves the stated diagonal identity; exponential tail decay and the integrable $O(x)$ endpoint bound justify the limit. It also gives orthogonality of distinct ladder modes. Hence the normalized eigenfunction is

$$\psi_j(x)=\rho_j\sqrt{\frac{2\sinh(\pi\sigma)}{\pi\sigma}}\sqrt x\,K_{i\sigma}(\rho_jx).\tag{3}$$

## 4. Complete continuous spectrum and scattering convention

For $k>0$ set $t(k)=\varsigma(k/2)^{2i\sigma}$, $a=e^{\pi\sigma/2}$, $b=e^{-\pi\sigma/2}$, and

$$\phi_k(x)=e^{-i\pi/4}\sqrt{kx}\,\frac{J_{i\sigma}(kx)-t(k)J_{-i\sigma}(kx)}{b-t(k)a}.\tag{4}$$

Because $|t(k)|=1$ and $a>b>0$, $|b-ta|\ge a-b>0$. Thus no exceptional positive spectral parameter occurs. Taking the two boundary values of (1), using the $I$--$J$ connection and $K$--Hankel identity, yields Stone's density in momentum form

$$d\mathsf E_{H}(k^2;x,y)=\phi_k(x)\overline{\phi_k(y)}\,dk.\tag{5}$$

The normalization is also fixed by the unit incoming amplitude in (6) below. The boundary values are locally continuous on each compact positive momentum interval in weighted spaces $\langle x\rangle^{-s}L^2$, $s>1/2$; this follows from the bounded nonzero denominator, the displayed endpoint behavior and the oscillatory Bessel tail. These are the limiting-absorption hypotheses of Stone's formula, and are precisely the nonexceptional case in [DR, Theorem 6.1 and Proposition 6.7]. Formula (5) rules out singular continuous spectrum on $(0,\infty)$. A singular measure supported at the sole remaining point zero would be an atom. Neither $u_+$ nor $u_-$, nor any nonzero combination, is square integrable at infinity, so zero is not an eigenvalue and carries no atom. Positive-energy solutions have nondecaying oscillatory tails, so there are no positive eigenvalues.

For explicit control of the zero-energy exclusion, any nonzero combination $f=a u_-+b u_+$ obeys $f(e^{\pi/\sigma}x)=-e^{\pi/(2\sigma)}f(x)$. Its squared norm on each consecutive annulus $[e^{n\pi/\sigma},e^{(n+1)\pi/\sigma}]$ is therefore $e^{2n\pi/\sigma}$ times a strictly positive first-annulus norm. The sum diverges at infinity; an oscillatory cancellation cannot create a zero mode.

The spectral theorem, (1), and (5) now give the full unitary resolution

$$\|f\|^2=\sum_{j\in\mathbb Z}|\langle\psi_j,f\rangle|^2+\int_0^\infty|\langle\phi_k,f\rangle|^2dk.$$

The integral transform is initially read weakly on compactly supported test functions and extended by this identity. There is one generalized eigenfunction per momentum, so the absolutely continuous multiplicity is one and its spectrum is $[0,\infty)$. This is an infinite-dimensional theorem, not a finite-cutoff inference.

The large-$x$ expansion of (4) is

$$\phi_k(x)=(2\pi)^{-1/2}\big(e^{-ikx}+R(k)e^{ikx}\big)+O(x^{-1}),\qquad R(k)=-i\frac{a-t(k)b}{b-t(k)a}.\tag{6}$$

Incoming means $e^{-ikx}$; outgoing means $e^{ikx}$. The incoming and outgoing numerator moduli agree, giving $|R(k)|=1$. For the free Dirichlet half-line Hamiltonian $H_D=-\partial_x^2$, the reflection amplitude is $-1$. With

$$W_\pm=\mathop{\mathrm{s-lim}}_{t\to\pm\infty}e^{itH_{\sigma,\kappa}}e^{-itH_D},\qquad S=W_+^*W_-,$$

the scalar scattering multiplier in the sine representation is $S(k)=-R(k)$. The wave operators exist and are complete by [DR, Proposition 6.10], applied with $(m,\kappa)=(i\sigma,\kappa)$ and $(m',\kappa')=(1/2,0)$: both real parts lie strictly between minus one and one; both realizations are self-adjoint; neither is exceptional because the denominators above never vanish. Its Hankel formula agrees with (4)--(6) and Proposition 6.9, fixing the constant phase rather than identifying reflection with relative scattering. Completeness means $W_\pm^*W_\pm=I$ and $W_\pm W_\pm^*=P_{\mathrm{ac}}(H)$; the negative ladder is not in their range.

## 5. Domain-scale limit cycle

For $(U_\tau f)(x)=e^{\tau/2}f(e^\tau x)$, substitution into the coefficient expansion gives

$$U_\tau D_\kappa=D_{\kappa e^{-2i\sigma\tau}},\qquad U_\tau H_{\sigma,\kappa}U_\tau^{-1}=e^{-2\tau}H_{\sigma,\kappa e^{-2i\sigma\tau}}.\tag{7}$$

The stabilizer of one self-adjoint domain is exactly $\tau\in(\pi/\sigma)\mathbb Z$. No self-adjoint domain is invariant under every real dilation. This is a cycle in domain space, not periodicity of the physical time evolution. In momentum, $t(ke^{\pi/\sigma})=t(k)$, hence $R$ and $S$ have log-period $\pi/\sigma$. It is the least positive log-period: the fractional linear map $t\mapsto(a-tb)/(b-ta)$ is injective since $a^2-b^2\ne0$, and $t$ has exactly that least period. Formula (2) has the same ratio $|E_{j+1}|/|E_j|=e^{-2\pi/\sigma}$. All of these scales are determined by $\sigma$ and the chosen boundary phase, not by rational primes.

## 6. Evolution, heat, and determinant obstruction

Every $H_{\sigma,\kappa}$ is self-adjoint, so $e^{-itH}$ is a unitary group for every real $t$. It has no nonzero full return time: on the nonzero absolutely continuous subspace, $e^{-itk^2}$ cannot equal one almost everywhere unless $t=0$. For every $t>0$, $e^{-tH}$ is unbounded because its values $e^{-tE_j}$ on the normalized eigenvectors diverge as $j\to-\infty$. Thus there is not even a bounded global heat operator, much less a heat trace.

The resolvent $(H-z)^{-1}$ is not compact: on a bounded positive spectral interval of nonzero measure it is unitarily multiplication by $(k^2-z)^{-1}$, bounded away from zero. An infinite orthonormal sequence with disjoint spectral supports has images separated in norm. No resolvent is therefore Schatten class, and the ordinary determinant of $I-w(H-z)^{-1}$ is unavailable. Unitary evolution is also noncompact; this is not repaired by labeling a finite mode determinant as global.

Even the restricted negative-ladder series $\sum_{j\in\mathbb Z}(-E_j)^{-s}$ converges for no complex $s$: the $j\to+\infty$ terms fail to vanish if $\operatorname{Re}s\ge0$, while the $j\to-\infty$ terms fail if $\operatorname{Re}s\le0$. Its bilateral product $\prod_j(1-w/E_j)$ has no ordinary nonzero neighborhood of convergence, since the factors do not tend to one along $E_j\to0$. A finite truncation can be evaluated, but is not an analytic continuation of a series with a convergence germ. Relative resolvents or explicitly renormalized objects are different constructions and are not excluded by this ordinary-determinant statement; none is promoted here to a target divisor.

## 7. Evidence boundary and route verdict

The complete claims above depend on endpoint analysis, Bessel identities, Stone's theorem, the spectral theorem, and the explicitly checked external wave-operator theorem. Exact rational receipts check classical quadratics, the boundary form and the scattering Möbius map. Independent high-precision special-function checks test boundary matching, eigenfunction normalization, Green jumps and spectral-density conventions on finite declared grids. They are regression, not interval certificates or proofs of completeness. Symbolic identities, two-directory byte replay, typed repaired-hash attacks, strict YAML attacks, optimized-mode refusal and deterministic manuscripts audit the implementation, not mathematical originality.

The strict tuple is $(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION})$, overall `ROUTE_A_REJECTED`. A4 records only the natural Schrödinger expression and its explicitly parameterized self-adjoint realizations. Arithmetic source, arithmetic primitive correspondence, target divisor, target functional equation and a Hilbert--Pólya operator are absent. Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; every target claim flag and Route-B authorization is false.

## Sources and open risks

[DR] J. Dereziński and S. Richard, *On Schrödinger Operators with Inverse Square Potentials on the Half-Line*, Annales Henri Poincaré 18 (2017), DOI 10.1007/s00023-016-0520-7; author preprint arXiv:1604.03340v2. Exact input locations: Section 2.2, Proposition 2.2, Theorem 5.5(ii), Theorem 6.1, Proposition 6.7, and Propositions 6.9--6.10. The boundary and spectrum formulas are classical prior work. No unresolved mathematical assumption is used inside the frozen self-adjoint supercritical family; extending to $\sigma=0$, nonunit boundary parameters, ultraviolet regularization, or alternative relative determinants is not part of this theorem.
