# C386 analytic proof: the full rank-one alpha-Szego threshold

## Claim, status, and frozen object

Status: **PROVABLE AS STATED**, with the rank-zero boundary explicitly separated.
This is a source-theorem and reproducibility package, not a claim of literature
priority. Xu's threshold theorem is classical; the package retains its exact
rank hypothesis, supplies a turning-point-safe explicit orbit proof, and audits
the blindness of the native shifted-Hankel determinant to the cascade rate.

On the circle with normalized measure $d\theta/(2\pi)$, let $\Pi$ retain
nonnegative Fourier modes. Fix $\alpha\in\mathbb R$ and physical time $t$ in
$$i\partial_tu=\Pi(|u|^2u)+\alpha(u\mid1).$$
The phase space is the invariant manifold
$$\mathcal L(1)=\{u(z)=b+cz/(1-pz):b,c,p\in\mathbb C,\ c\ne0,\ |p|<1\}.$$
No finite Fourier truncation defines the equation. The Fourier coefficients are
$u_0=b$ and $u_n=cp^{n-1}$ for every $n\ge1$. We separately adjoin the rank-zero
constant solutions. We use $\|u\|_{H^s}^2=\sum_{n\ge0}(1+n)^{2s}|u_n|^2$.

The claims are global rank-one well-posedness; conservation of $Q,M,E_\alpha$;
an exact compactness/cascade dichotomy for every real $\alpha$; an explicit
two-sided sech-squared radial orbit and exact high-Sobolev growth rate on the
cascade level; all rank-zero and zero-perturbation exceptions; and a native
rank-one determinant which does not record the cascade rate. No classification
of arbitrary Hardy-space initial data or of higher-rank manifolds is claimed.

## Assumptions and notation

Write $d=1-|p|^2>0$, $\rho=|c|>0$, $B=|b|^2$, and
$$Q=B+\rho^2/d,\qquad M=\rho^2/d^2>0,$$
$$E_\alpha=\tfrac14\|u\|_4^4+\tfrac\alpha2|b|^2,\qquad
\delta=E_\alpha-Q^2/4-\alpha Q/2.$$
Thus $\rho=\sqrt M d$ and $B=Q-Md$. All constants in a single trajectory
depend on its initial data unless a uniform dependence is explicitly stated.
The root $\sqrt M$ is positive. Time is neither rescaled nor fitted.

## Proof strategy and dependencies

1. Geometric-series Fourier convolution gives the complete three-complex-variable
   ODE and the conservation laws.
2. A logarithmic differential bound excludes finite-time exit from the manifold.
3. The conserved energy defect gives a quantitative compactness bound off its
   zero level; on the zero level a scalar second-order equation closes the orbit.
4. Uniqueness for this second-order equation, including its turning point, gives
   the sech-squared formula. An elementary Abelian sum gives exact Sobolev growth.
5. The shifted Hankel matrix is evaluated directly, without importing a general
   Lax theorem or treating an antilinear operator as a complex-linear determinant.

## 1. Exact nonlinear reduction and conservation

Absolute convergence of the geometric Fourier series and all its derivatives
holds on compact subsets of $|p|<1$. Convolving it in $\Pi(|u|^2u)$ and comparing
the coefficients of $1,z/(1-pz),z^2/(1-pz)^2$ gives
$$\begin{aligned}
i\dot b&=(B+2\rho^2/d+\alpha)b+\rho^2c\bar p/d^2,\\
i\dot c&=(2B+\rho^2/d^2)c+2b\rho^2p/d,\\
i\dot p&=c\bar b+\rho^2p/d.
\end{aligned}\tag{1}$$
The derivative of $u$ contains $c\dot p\,z^2/(1-pz)^2$; this factor must not be
dropped when comparing the third coefficient. Formula (1) is also valid at
$p=0$ and $b=0$. Direct substitution gives
$\dot Q=\dot M=\dot E_\alpha=0$; an explicit form useful for verification is
$$4E_\alpha=B^2+4B\rho^2/d+
\rho^4(1+|p|^2)/d^3+4\rho^2\Re(bp\bar c)/d^2+2\alpha B.\tag{2}$$
These identities can alternatively be checked by the Hamiltonian equation for
$E_\alpha$, phase invariance for $Q$, and angular translation invariance for $M$.
Here the direct algebraic identities are the proof input.

The ODE is locally Lipschitz in six real variables when $d>0$.
Let $X=bp\bar c$. Formula (1) gives
$$\dot d=2\Im X,\qquad
\dot\rho=2\sqrt M\Im X,\qquad
|\dot\rho/\rho|\le2\sqrt{QM}.\tag{3}$$
Consequently $\rho(t)\ge\rho(0)e^{-2\sqrt{QM}|t|}$ on every finite interval.
Since $|b|\le\sqrt Q$, $\rho=\sqrt M d\le\sqrt M$, and $d=\rho/\sqrt M$,
no finite-time trajectory can leave a compact subset of the ODE domain. The
finite-dimensional continuation theorem yields a unique solution for all real
$t$. Its geometric Fourier series solves the original PDE in every $H^s$.
This proves global existence only for the named invariant manifold.

## 2. Exact energy defect and off-threshold compactness

Subtracting $Q^2/4+\alpha Q/2$ from (2) gives the exact identity
$$\delta=\frac{Md}{2}
\left(\left|b+\frac{c\bar p}{d}\right|^2-\alpha\right).\tag{4}$$
If $\delta\ne0$, then for every real $t$
$$d(t)\ge
\frac{2|\delta|}{M((\sqrt Q+\sqrt M)^2+|\alpha|)}>0.\tag{5}$$
Indeed $|b+c\bar p/d|\le\sqrt Q+\sqrt M$, so (4) bounds $|\delta|$ by the
denominator in (5) times $d/2$. This gives a positive lower bound on $|c|$ and
keeps $p$ in a strict subdisk. Boundedness of $b,c$ then puts the orbit in a
compact subset of $\mathcal L(1)$, and geometric summation bounds every $H^s$.
The bound is uniform for compact initial-data sets on which $|\delta|$ is
bounded away from zero. No uniform bound across the cascade hypersurface is
asserted.

For $\alpha<0$, (4) has $\delta>0$ on $\mathcal L(1)$, so all orbits are
relatively compact. The same is true uniformly for each compact set of initial
data, by continuity and positivity of its minimum defect.

For $\alpha=0$, the only remaining case is $\delta=0$. Equation (4) gives
$b=-c\bar p/d$, whence $Q=M$, and with $A=c/d$ we have
$$u(z)=A\frac{z-\bar p}{1-pz},\qquad |A|^2=Q=M.$$
This function has constant modulus on the circle. Its complete solution is
$$u(t,z)=e^{-iQt}u(0,z),\qquad p(t)=p(0),$$
as verified in (1). Thus these orbits are also relatively compact. This closes
every $\alpha\le0$ trajectory without asserting a general quasiperiodic theorem.

## 3. Cascade threshold and the turning-point-safe radial theorem

Assume $\alpha>0$ and $\delta=0$. Define
$$\kappa^2=4QM-(\alpha-Q-M)^2.\tag{6}$$
Equation (4) yields $2\Re X=d(\alpha-Q-M)+2Md^2$. Combining this with
$|X|^2=(Q-Md)Md^2(1-d)$ and (3) gives
$$\dot d^{\,2}=d^2(\kappa^2-4\alpha Md).\tag{7}$$
Because $d>0$, (7) implies $\kappa^2\ge4\alpha Md>0$; take $\kappa>0$.
The identity
$$\kappa^2-4\alpha M=-(Q-M-\alpha)^2\le0\tag{8}$$
also gives $d_*:=\kappa^2/(4\alpha M)\le1$.

Squaring a first-order equation does not exclude a solution sticking at a
turning point. We therefore derive a second-order equation directly from (1).
Put $T=\alpha-Q-M$. Differentiating $X$ gives
$$\dot X=i(FX+G),\quad F=-T-4Md,$$
$$G=-M^2d^2(1-d)-(Q-Md)Md^2+2(Q-Md)Md(1-d).$$
Thus $\ddot d=2(F\Re X+G)$ and substitution of the real part above gives
$$\ddot d=\kappa^2d-6\alpha Md^2.\tag{9}$$
This polynomial equation holds even when $\dot d=0$. At $d=d_*$ its acceleration
is $-\kappa^2d_*/2<0$, so the turning point cannot be stationary.

Define $v_0=\dot d(0)/(\kappa d(0))$. By (7), $|v_0|<1$ and
$$t_*=\frac2\kappa\operatorname{artanh}(v_0).$$
The function
$$d(t)=d_*\operatorname{sech}^2\!\left(\frac\kappa2(t-t_*)\right),\qquad
\rho(t)=\frac{\kappa^2}{4\alpha\sqrt M}
\operatorname{sech}^2\!\left(\frac\kappa2(t-t_*)\right)\tag{10}$$
has exactly the prescribed $d(0),\dot d(0)$ and solves (9).
Uniqueness of the polynomial second-order initial-value problem proves (10)
for every real $t$. In particular $p=0$ at the turning point is allowed when
$d_*=1$; no division by $p$ has occurred.

Equation (10) tends to zero at both infinite-time ends. Hence the trajectory is
not relatively compact in $\mathcal L(1)$. Conversely, (5) makes every
off-threshold orbit relatively compact. We have proved the full equivalence
$$\text{non-relative-compactness in }\mathcal L(1)
\quad\Longleftrightarrow\quad
E_\alpha=Q^2/4+\alpha Q/2\qquad(\alpha>0).\tag{11}$$

## 4. Exact Sobolev exponent and conserved-momentum escape

As $d\downarrow0$, the elementary Riemann-sum identity
$$d^{2s+1}\sum_{n\ge1}(n+1)^{2s}(1-d)^{n-1}\longrightarrow\Gamma(2s+1)
\qquad(s>1/2)\tag{12}$$
follows by setting $x=dn$: on each bounded positive interval the summands
converge uniformly to $x^{2s}e^{-x}$, and exponential majorants control the tail
while $x^{2s}$ controls the interval near zero. This is a sum-to-integral limit,
not an assertion based on a finite frequency cutoff.
It follows that on the cascade level
$$\|u(t)\|_{H^s}^2\sim M\Gamma(2s+1)d(t)^{1-2s},\qquad
\lim_{t\to\pm\infty}\frac{\log\|u(t)\|_{H^s}}{|t|}
=(s-\tfrac12)\kappa.\tag{13}$$
More precisely, replace $d(t)$ by
$(\kappa^2/(\alpha M))e^{-\kappa|t-t_*|}$ in the first asymptotic formula.
The critical norm is exactly $\|u(t)\|_{H^{1/2}}^2=Q+M$.
Also $\|u(t)-b(t)\|_2^2=Md(t)\to0$ while
$\sum_{n\ge1}n|u_n(t)|^2=M$ remains fixed. Thus high-frequency momentum escapes
without finite-time blowup and without loss of total momentum. For each fixed
$N$, the momentum in modes $1,\ldots,N$ tends to zero.

The checkable example $u(0,z)=\sqrt\alpha+z$ has $Q=1+\alpha$, $M=1$,
$\kappa=2\sqrt\alpha$, $t_*=0$, and $d(t)=\operatorname{sech}^2(\sqrt\alpha t)$.
Its growth rate is $(2s-1)\sqrt\alpha$.

## 5. Rank zero, reversal, and the native determinant obstruction

If $c=0$, then $u=b$ is constant in space and
$$b(t)=b(0)e^{-i(|b(0)|^2+\alpha)t}.$$
The energy equality in (11) then holds for every constant, but no Sobolev norm
grows. These are rank-zero solutions and are excluded from (11). The parameter
$p$ is redundant on this face. The zero function is stationary. A nonzero
constant is stationary when $|b|^2+\alpha=0$; otherwise its least temporal
period is $2\pi/||b|^2+\alpha|$.

The physical reversal on Hardy functions is the coefficient conjugation
$\mathcal Cu(z)=\overline{u(\bar z)}$, not pointwise conjugation on the circle
alone. It preserves nonnegative Fourier modes, is antiunitary, and the real
coefficient convolution verifies that $\mathcal Cu(-t)$ solves the same
$\alpha$ equation. This is a reversible nonlinear Hamiltonian flow; no
linear quantum Hamiltonian has been constructed from it.

Define the antilinear Hankel operator $H_u f=\Pi(u\bar f)$ and its shifted
version $K_u=S^*H_u$. Its matrix is $(u_{j+k+1})_{j,k\ge0}= (cp^{j+k})$.
For $v=(1,p,p^2,\ldots)$ and the inner product linear in its first argument,
$$K_uf=c\langle v,f\rangle v,\qquad
K_u^2f=\frac{|c|^2}{d}\langle f,v\rangle v.$$
Thus $K_u^2$ is complex-linear, positive, rank one, and has its sole nonzero
eigenvalue $M=|c|^2/d^2$. For every complex $w$,
$$\det(I-wK_u^2)=1-wM,\qquad \operatorname{tr}(K_u^{2r})=M^r\ (r\ge1).\tag{14}$$
Its isospectrality follows here from direct conservation of $M$; we need not
invoke the full infinite-dimensional Lax-pair theorem. The antilinear $K_u$
itself is not assigned a complex Fredholm determinant.

For $u_0=\sqrt\alpha+z$, all $\alpha>0$ give the same determinant $1-w$ but
different physical growth rates $\kappa=2\sqrt\alpha$. Even at fixed
$\alpha>0$, $u_0=z$ has $M=1$ and is a bounded single-mode phase orbit, whereas
$u_0=\sqrt\alpha+z$ has the same $M$ and cascades. Therefore this native
determinant cannot classify recurrence or recover the cascade rate. It is an
auxiliary isospectral invariant, not the time-evolution determinant or a
primitive-periodic-orbit product. Its one zero cannot match the full target
divisor through a zero-free entire prefactor.

## Sources, corrections, and remaining boundaries

Primary source: H. Xu, *Large-time blowup for a perturbation of the cubic Szego
equation*, Analysis & PDE 7 (2014), 717--731,
https://doi.org/10.2140/apde.2014.7.717 ; author preprint
https://arxiv.org/abs/1307.5284 (v3, Theorems 1.3, 3.1--3.3).
Classical origin: P. Gerard and S. Grellier, *The cubic Szego equation*,
https://doi.org/10.24033/asens.2133 .

The source's norm-growth paragraph compresses the turning point into a
logarithmic-derivative estimate. We do not use a positive derivative lower
bound at that turning point; (9)--(10) supply the complete argument. We also do
not assert a uniform norm bound across off-threshold data approaching the
threshold. The proof does not depend on either compressed statement.

No generic periodic-orbit census, higher-rank threshold, global Hardy-data
classification, arithmetic origin, target-zero fit, Euler factor, root number,
Weil compression, Hilbert--Polya operator, or Route-B conclusion is claimed.
The strict tuple is $(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FORMAL\_HINT)$.
The firewall remains `NO_BAD_EULER_OR_ROOT_NUMBER`.
