# C383 analytic proof: Friedrichs Aharonov–Bohm scattering

## Claim and status

**PROVABLE AS STATED**, with the operator domain and physical time-reversal class fixed below. For every real flux $\beta$, the Friedrichs magnetic Laplacian on the punctured plane has a complete angular Hankel diagonalization, purely absolutely continuous spectrum $[0,\infty)$, complete free wave operators, the channel scattering phases below, and the displayed local heat kernel. For $0<\beta<1$, the scattering correction is noncompact, the ordinary global heat trace and ordinary Fredholm scattering determinant are unavailable, and the forward angular distribution cannot be omitted. These are source-system theorems, not new discoveries of the classical Aharonov–Bohm formulas.

## Assumptions and notation

Work in $\mathcal H=L^2(\mathbb R^2,r\,dr\,d\theta)$, with puncture $r=0$, $\hbar=2M=1$, physical Schrödinger time $t$, and energy $k^2$, $k>0$. Start on $C_c^\infty(\mathbb R^2\setminus\{0\})$ with the nonnegative form
$$q_\beta[f]=\int_0^\infty\int_0^{2\pi}\left(|\partial_rf|^2+r^{-2}|(-i\partial_\theta-\beta)f|^2\right)r\,d\theta\,dr.$$
$H_\beta$ is the self-adjoint operator associated with its closed Friedrichs form. Other self-adjoint extensions, point interactions, spin, finite-radius solenoids, and confining fields are excluded. Write $e_m(\theta)=(2\pi)^{-1/2}e^{im\theta}$, $\nu_m=|m-\beta|$, and $\mu_m=|m|$. The periodic delta has integral one. Scattering angles are outgoing angle minus incoming angle. The outgoing amplitude convention is
$$f_\beta(k,\theta)=(2\pi i k)^{-1/2}\sum_{m\in\mathbb Z}(S_m-1)e^{im\theta},$$
with $\sqrt i=e^{i\pi/4}$ and distributional summation.

## Strategy and dependencies

1. Angular Fourier completeness decomposes the closed form into radial Bessel forms.
2. The Hankel Plancherel/inversion theorem for real order $\nu\ge0$ diagonalizes the Friedrichs radial operator. The Weber exponential integral evaluates its heat kernel.
3. Bessel large-argument asymptotics, first for compact smooth spectral wave packets away from $k=0$, identify the wave operators; density and uniform unitary bounds extend the limits.
4. Abel sums recover both principal value and delta terms. Infinite orthonormal channel sequences prove noncompactness.
5. Direct form conjugation proves integer gauge covariance and classifies position-preserving physical time reversal.

The transform/integral facts are the named classical analytic inputs (NIST DLMF §§10.17 and 10.22). Pankrashkin–Richard, arXiv:0911.4715, Lemma 7 and the original AB channel calculation, supplies the rigorous wave-operator existence/completeness input, with their opposite flux convention translated by angular reflection. All convention-specific phases and further consequences below are derived in the present convention. The dense-packet argument explains the phase identification; the cited theorem supplies its complete strong-limit justification.

## Proof

### 1. Friedrichs realization and complete spectrum

Parseval in $\theta$ gives $q_\beta=\sum_m q_{\nu_m}$, where
$$q_\nu[u]=\int_0^\infty (|u'|^2+\nu^2r^{-2}|u|^2)r\,dr.$$
The orthogonal sum commutes with form closure: finite angular sums with smooth radial compact support are a form core, by Fourier truncation and each radial closure. Thus $H_\beta=\bigoplus_m h_{\nu_m}$, with
$$h_\nu=-\partial_r^2-r^{-1}\partial_r+\nu^2r^{-2}.$$
For $0<\nu<1$ the Friedrichs boundary condition removes the $r^{-\nu}$ component; for $\nu=0$ it removes the logarithmic component. It does not require the regular constant component to vanish. Orders $\nu\ge1$ are limit point at zero. Infinity is limit point. These statements also follow from the two zero-energy powers and the form energy integral; the excluded singular branches have divergent form energy.

The order-$\nu$ Hankel transform
$$({\cal J}_\nu u)(k)=\int_0^\infty J_\nu(kr)u(r)r\,dr$$
is unitary from $L^2(r\,dr)$ to $L^2(k\,dk)$ and is its own inverse after identifying the variables. The Hankel spectral theorem for this regular boundary condition gives
$$\mathcal J_\nu h_\nu\mathcal J_\nu^{-1}=M_{k^2},\qquad D(h_\nu)=\{u:k^2\mathcal J_\nu u\in L^2(k\,dk)\}.$$
Hence the full transform $\mathcal F_\beta=\bigoplus_m\mathcal J_{\nu_m}$ is onto and diagonalizes $H_\beta$. Multiplication by $k^2$ on the non-atomic measure $k\,dk$ has purely absolutely continuous spectrum $[0,\infty)$, no eigenvalues, and no singular continuous spectrum. The countable direct sum preserves those conclusions. Completeness is an analytic transform theorem, not an inference from finitely many channels.

At $\beta=0$ the Friedrichs operator is the ordinary free plane Laplacian. To check the puncture, approximate a smooth function near zero by a logarithmic cutoff that rises from zero on $r\le\epsilon^2$ to one on $r\ge\epsilon$. Its Dirichlet energy is $2\pi/|\log\epsilon|$, which tends to zero; the omitted $L^2$ mass also tends to zero. Thus the point has zero $H^1$ capacity and the free form domain is unchanged.

### 2. Complete wave operators and channel phases

Define $W_\pm=\operatorname{s-lim}_{t\to\pm\infty}e^{itH_\beta}e^{-itH_0}$. In channel $m$, put $a_m=\pi(\mu_m-\nu_m)/2$. Then
$$W_{\pm,m}=e^{\mp ia_m}\mathcal J_{\nu_m}\mathcal J_{\mu_m},\qquad S_m=W_{+,m}^*W_{-,m}=e^{2ia_m}.$$
Here the product of the two Hankel maps identifies the common spectral variable; it is a radial-space unitary.

For the phase, $J_\nu(kr)=(2/\pi kr)^{1/2}\cos(kr-\pi\nu/2-\pi/4)+O((kr)^{-3/2})$. The incoming and outgoing radial coefficients are respectively proportional to $e^{+i\pi\nu/2}$ and $e^{-i\pi\nu/2}$. Matching the incoming free coefficient gives $e^{+ia_m}$; matching the outgoing coefficient gives $e^{-ia_m}$. For a smooth spectral packet supported in a compact subset of $(0,\infty)$, stationary phase places its mass at $r\asymp2|t|k$. The Bessel remainder is integrably small there in $L^2(r\,dr)$; integration by parts controls the complementary nonstationary region. The incoming exponential has the stationary point for negative time, and the outgoing exponential for positive time, proving the two strong limits on this dense packet class. Unitarity extends the limits to all radial data. Finite angular sums are dense and all approximants have norm one, so the direct-sum limits exist on all $\mathcal H$. Every displayed channel wave operator is onto; their orthogonal sum is onto, proving asymptotic completeness.

For $0<\beta<1$, the result reduces to
$$S_m=\begin{cases}e^{i\pi\beta},&m\ge1,\\e^{-i\pi\beta},&m\le0.\end{cases}$$
This includes both signs and all angular channels. At $\beta=0$, $S=I$.

### 3. Full angular distribution and away-forward cross section

Let $P_+$ project onto $m\ge1$ and $P_-$ onto $m\le0$ in $L^2(S^1,d\theta)$. Then
$$S=e^{i\pi\beta}P_++e^{-i\pi\beta}P_-.$$
Its convolution kernel (relative to $d\theta$) is
$$K_S(\theta)=\cos(\pi\beta)\delta_{2\pi}(\theta)-\frac{\sin(\pi\beta)}{2\pi}\operatorname{PV}\cot(\theta/2)-\frac{i\sin(\pi\beta)}{2\pi}.$$
To derive this identity, insert Abel factors $\rho^{|m|}$, $0<\rho<1$, into the two geometric series. Distributionally,
$$\sum_{m\ge1}e^{im\theta}=\pi\delta_{2\pi}-\frac12+\frac i2\operatorname{PV}\cot(\theta/2),$$
$$\sum_{m\le0}e^{im\theta}=\pi\delta_{2\pi}+\frac12-\frac i2\operatorname{PV}\cot(\theta/2).$$
Combining the two coefficients proves the kernel formula. Equivalently $S-I$ contains $(\cos\pi\beta-1)\delta_{2\pi}$. Keeping this term is required to represent the unitary scattering operator; the away-forward function alone is not its full kernel.

For $\theta\notin2\pi\mathbb Z$,
$$f_\beta(k,\theta)=-\frac{\sin(\pi\beta)}{\sqrt{2\pi i k}}\big(\cot(\theta/2)+i\big),\qquad
\frac{d\sigma}{d\theta}=\frac{\sin^2(\pi\beta)}{2\pi k\sin^2(\theta/2)}.$$
The cross section is only away from the forward ray; there is no multiplication or squaring of delta distributions. Its integral over all angles diverges when $0<\beta<1$.

### 4. Heat kernel and two determinant obstructions

For $t>0$ and $r,r'>0$, Weber's exponential integral gives
$$K_\beta(t;r,\theta;r',\theta')=\frac{e^{-(r^2+r'^2)/(4t)}}{4\pi t}\sum_{m\in\mathbb Z}e^{im(\theta-\theta')}I_{|m-\beta|}\!\left(\frac{rr'}{2t}\right).$$
It is the integral kernel relative to $r'\,dr'\,d\theta'$. Indeed each radial summand is the spectral integral of $e^{-tk^2}J_\nu(kr)J_\nu(kr')k\,dk$, and the angular normalizer is $1/(2\pi)$.

For $z\ge0,\nu\ge0$, the defining series and $(\nu+1)_j\ge j!$ yield
$$I_\nu(z)\le\frac{(z/2)^\nu}{\Gamma(\nu+1)}e^{z^2/4}.$$
For fixed $\nu_0$ with $a=z/[2(\nu_0+1)]<1$, summing the successive-order bound gives
$$\sum_{j\ge0}I_{\nu_0+j}(z)\le e^{z^2/4}\frac{(z/2)^{\nu_0}}{\Gamma(\nu_0+1)(1-a)}.$$
For this tail statement take the fixed fundamental flux cell $0\le\beta<1$ and integer $M\ge0$. The omitted positive and negative channel orders after $|m|\le M$ start at $M+1-\beta$ and $M+1+\beta$. Applying this inequality twice proves local uniform absolute convergence and an explicit cutoff bound. For general real flux the same displayed first orders apply only when $M+1>|\beta|$; alternatively first use integer gauge covariance and relabel the cutoff. At $z=0$ use the series limits rather than $0^0$ notation. The free check $\sum_m e^{im\phi}I_{|m|}(z)=e^{z\cos\phi}$ recovers $(4\pi t)^{-1}e^{-|x-y|^2/(4t)}$.

For fixed $t>0$, $e^{-tH_\beta}$ is unitarily equivalent in every channel to multiplication by $e^{-tk^2}$. On a positive-measure interval of $k$, this multiplier is bounded below by a positive constant. Disjoint measurable subsets give an orthonormal sequence whose images have pairwise disjoint support and norms bounded below. Thus the heat operator is not compact, hence not trace class; its positive extended trace is infinite. The local kernel is not a global trace formula.

Likewise $\|(S-I)e_m\|=2\sin(\pi\beta/2)>0$ for every integer $m$ when $0<\beta<1$. Orthogonality proves $S-I$ noncompact. No usual trace-class Fredholm determinant $\det(I+(S-I))$ exists. Symmetric finite channel products happen to equal $e^{-i\pi\beta}$, while the equally exhaustive windows $[-M,M+1]$ give $1$; these incompatible cutoff answers expose the missing canonical determinant. This does not rule out separately defined renormalized or relative determinants, which are outside the claim.

### 5. Gauge covariance and physical time reversal

For each integer $n$, $U_nf=e^{in\theta}f$ preserves single-valuedness and
$$H_{\beta+n}=U_nH_\beta U_n^{-1},\qquad KH_\beta K=H_{-\beta},$$
where $K$ is position-space complex conjugation. Both statements hold at the form level and therefore preserve the Friedrichs realizations. Integer flux changes relabel channels; arbitrary noninteger gauge factors are not single-valued on this Hilbert space.

Define physical time reversal here to be an antiunitary $T_n=U_nK$ that fixes position and reverses mechanical momentum, with no spatial reflection. Then $T_nH_\beta T_n^{-1}=H_{n-\beta}$. Equality with $H_\beta$ requires $n=2\beta$: compare the coefficient of $-i\partial_\theta$ in the differential expressions. Conversely this equality makes $T_n$ a domain-preserving symmetry and $T_n^2=I$. Thus in $[0,1)$ this physical symmetry occurs exactly at $\beta=0$ and $\beta=1/2$. Reflection $Rf(r,\theta)=f(r,-\theta)$ satisfies $RH_\beta R^{-1}=H_{-\beta}$, so $RK$ commutes with $H_\beta$ for every flux. It moves spatial points and is not a counterexample to the explicitly position-preserving classification. Abstract antiunitary equivalences inferred from continuous spectral multiplicity are also not physical time reversal by this definition.

### 6. Route-A endpoint

The classical magnetic field vanishes off the puncture. The mechanical momentum is constant along each nonsingular positive-energy trajectory, so each such trajectory is a straight line and has no periodic return. Trajectories that meet the puncture are incomplete in this idealized classical configuration and are not periodic orbits; the zero-energy stationary continuum is not an isolated primitive-orbit ledger. Integer angular labels are Fourier winding modes, not rational primes. Flux changes, label permutations, and the free parent preserve the absence of a prime mechanism.

The strict tuple is $(A0_{\rm FAIL},A1_{\rm FAIL},A2_{\rm FAIL},A3_{\rm FAIL},A4_{\rm UNITARY\_OR\_SCATTERING\_CANDIDATE})$, overall `ROUTE_A_REJECTED`. The natural unitary scattering object supports A4 only. `NO_BAD_EULER_OR_ROOT_NUMBER` remains in force and Route B is false.

## Corrections and open risks

No theorem is asserted for other self-adjoint extensions. No full heat trace, ordinary scattering determinant, forward cross-section density, or generic-flux position-preserving time reversal is asserted. Classical formula novelty is explicitly disclaimed: the package contribution is a single-convention proof and reproducibility audit joining domain, full distribution, cutoff failure, heat noncompactness, and physical-symmetry boundaries. High-precision finite checks are numerical regression, not interval certification or proof of channel completeness.
