# Independent proof check: finite-time conjugate-area scaling

Date: 2026-09-07.

Reviewed source: `PAPER30_CONJUGATE_TIME_SCALING_PROOF_V1_20260907.md`, 378 lines, as supplied for this independent check. The author source and all status/acceptance files were left unchanged.

## Claim

For the specified sine twist map, with $h=\sqrt\varepsilon$ and the first failure of strict Dirichlet positivity denoted by $\tau_{h^2}$, the claim is the fixed-$c$ limit

$$
h^{-1}m\{\tau_{h^2}\le\lfloor c/h\rfloor\}\longrightarrow
A(c)=\frac{1}{4\pi^2}\int_{\mathbb T\times\mathbb R}
\mathbf1_{\{\tau(q,y)\le c\}}\,dq\,dy,
\qquad c>0.
$$

Here $\tau$ is the first positive zero of the pendulum Jacobi solution with initial values $(J,\dot J)=(0,1)$. The additional claims are continuity of $A$, the threshold and strict increase, the limiting total area, and

$$
A(\pi+s)=\frac{4}{\sqrt3\,\pi^2}s+O(s^2),\qquad s\downarrow0.
$$

## Status

**PROVABLE AS STATED — full mathematical package PASS.**

No false theorem, missing scientific hypothesis, circular dependency, or unresolved mathematical blocker was found. The theorem survives without weakening. This verdict includes the global localization estimate; it is not based solely on the formal symplectic-Euler scaling limit.

There is one nonblocking wording precision note at source lines 242–245: the first argument in that paragraph proves confinement only almost everywhere at the boundary time $c$, whereas its subsequent explicit invocation of Step 5 proves the advertised pointwise confinement. This does not leave a proof gap.

This report is a bounded independent mathematical check, not a literature/novelty conclusion, formal candidate evaluation, Route A/B score, page-capacity judgment, PDF acceptance, or publication authorization.

## Assumptions and notation

- $c>0$ is fixed before $h\downarrow0$; neither a uniform-in-$c$ estimate nor an exchange of the two limits is assumed.
- Initial momentum uses $p_0\in[-\pi,\pi)$, and finite recurrences use consistent real lifts. The generating function is interpreted on those lifts, not as a globally single-valued periodic function of both torus coordinates.
- $H_N$ acts on the $N-1$ interior Dirichlet coordinates and $H_1$ is empty. A zero eigenvalue counts as failure of positivity.
- $D_j=\partial q_j/\partial p_0$ with $q_0$ fixed. Continuous initial momentum is $y_0=p_0/h$.
- Continuous energy is $E(q,y)=y^2/2-\cos q$, with $E\ge-1$ automatically.
- Every comparison below concerns the exact functions in the supplied source. No numerical fit or computational surrogate is used.

## Proof strategy and dependency map

1. Abel summation and the discrete Dirichlet inequality imply torus-wide localization in the band $|p_0|\le R(c)h$.
2. Exact leading-minor identities, a uniform initial-time positivity interval, and finite-time $C^1$ convergence imply convergence of the first failure times in the extended half-line.
3. Analytic null boundaries and localization permit dominated convergence at every fixed $c>0$.
4. The energy classification supplies the exact finite-time support and its total area. It can also be placed before step 3 to give pointwise continuous support there; it does not depend on the area limit.
5. The continuous Dirichlet inequality determines the unique minimum time. Turning-point data and simple-zero stability give strict increase.
6. The analytic quadratic expansion, global localization near the unique minimum, and a uniform radial inversion give the onset coefficient with an $O(s^2)$ remainder.

## Itemized verdicts

| Item | Source location | Verdict |
|---|---|---|
| Map/action Hessian signs and endpoint conventions | lines 9–28, 69–83 | PASS |
| Torus-wide denominator bound, including momentum-cut crossings | lines 111–130, equation (4) | PASS |
| Both Abel summations, constants, and all endpoint indices | lines 132–159, equations (5)–(7) | PASS |
| Leading minors and first failure versus exact Jacobi zero | lines 163–173, equations (8)–(9) | PASS |
| Initial-zero safeguard | lines 175–183 | PASS |
| Finite-time $C^1$ approximation and extended first-time convergence | lines 187–220, equations (10)–(12) | PASS |
| Fixed-time null boundary and the floor in the area limit | lines 224–245, equations (13), (1)–(2) | PASS; wording note below |
| Exact classification $\tau<\infty\iff E<1$ | lines 249–274, equations (14)–(16) | PASS |
| Total area and continuity | lines 275–280 | PASS |
| Threshold $\pi$, unique equality case, and strict increase | lines 284–308 | PASS |
| Local Taylor coefficient and quartic remainder | lines 312–330, equation (17) | PASS |
| Global-to-local onset reduction, radial inversion, area normalization | lines 333–355, equation (3) | PASS |

There are no FAIL or OPEN mathematical items in the reviewed package. The detailed justifications follow.

## Proof check

### 1. Global Abel localization: constants and endpoints

Put $R=100(c+1)$ and $d=R-c=99c+100$. For sufficiently small $h$, $Rh<\pi$. For every relevant index $0\le j\le N$,

$$
|p_j-p_0|\le jh^2\le ch,
\qquad \operatorname{dist}(p_j,2\pi\mathbb Z)>dh
\quad\text{if }|p_0|>Rh.
$$

The latter implication uses the global $1$-Lipschitz distance function. It continues to hold at $p_0=-\pi$ and when a lift crosses either momentum cut. Since $0\le\operatorname{dist}(p_j,2\pi\mathbb Z)\le\pi$,

$$
|1-e^{ip_j}|=2\sin\!\left(\frac{\operatorname{dist}(p_j,2\pi\mathbb Z)}2\right)
\ge\frac2\pi\operatorname{dist}(p_j,2\pi\mathbb Z)>\delta,
\qquad\delta=\frac{2dh}{\pi}.
$$

For $z_j=e^{iq_j}$, the precise identity is $z_{j+1}=z_je^{ip_{j+1}}$, so $a_j=(1-e^{ip_{j+1}})^{-1}$ is correctly indexed. At the largest summation endpoint $k=N-1$, the needed denominator is $p_N$, which has already been bounded. The exact summation formula is

$$
\sum_{j=1}^kz_j
=a_1z_1-a_kz_{k+1}+\sum_{j=2}^k(a_j-a_{j-1})z_j.
$$

Thus its modulus is at most $2\delta^{-1}+(k-1)h^2\delta^{-2}$. There is no missing endpoint term or extra factor of $N$.

Writing $C_j=\sum_{i=1}^j\cos q_i$, the second summation identity uses $v_N=0$ and $C_0=0$:

$$
\sum_{j=1}^{N-1}\cos q_jv_j^2
=\sum_{j=1}^{N-1}C_j(v_j-v_{j+1})(v_j+v_{j+1}).
$$

Its absolute value is bounded by $2B\|v\|_2\|\Delta v\|_2$. The omitted $j=0$ difference in that sum only makes its squared-difference norm smaller than the full Dirichlet energy. The discrete lowest eigenvalue is $4\sin^2(\pi/(2N))\ge4/N^2$, so $\|v\|_2\le(N/2)\|\Delta v\|_2$. With $N\le c/h$,

$$
h^2BN
\le\frac{\pi c}{d}+\frac{\pi^2c^2}{4d^2}
<\frac4{99}+\frac4{99^2}<\frac12.
$$

This establishes strict positivity simultaneously for every integer $2\le N\le c/h$. Boundary data $|p_0|=Rh$ are retained in the band, so the strict assumption used in the proof causes no loss. All other rational-rotation bands are covered by the same estimate; none is tacitly discarded.

### 2. Exact minors and protection from the initial zero

On the lift, differentiating $q_{j+1}-2q_j+q_{j-1}=-h^2\sin q_j$ gives the source recurrence with $D_0=0,D_1=1$. The Hessian has diagonal $2-h^2\cos q_j$ and off-diagonal entries $-1$. Its leading determinants therefore obey

$$
M_0=1,\quad M_1=2-h^2\cos q_1=D_2,
\quad M_k=(2-h^2\cos q_k)M_{k-1}-M_{k-2}=D_{k+1}.
$$

Sylvester's criterion applies to this real symmetric matrix. In particular,

$$
\tau_{h^2}\le N\quad\Longleftrightarrow\quad
\text{some }D_j\le0\text{ for }2\le j\le N.
$$

This identity includes a negative minor arising between sampled zeros and includes a zero minor itself. It does not replace positivity failure by exact integer-time vanishing.

For $Nh\le\pi/2$, the source bound gives

$$
\lambda_{\min}(H_N)\ge\frac4{N^2}-h^2
\ge\frac{4-\pi^2/4}{N^2}>0.
$$

Consequently all relevant $D_j$ near initial time are positive, and $D_1=1$ handles the remaining index. This supplies the necessary control that an absolute $O(h)$ error for $hD_j$ alone would not supply near $J(0)=0$.

As two exact checks of the convention, at the elliptic fixed point and $0<h<\sqrt2$, define $\omega=2\arcsin(h/2)$. Then $D_j=\sin(j\omega)/\sin\omega$ and $\tau_{h^2}=\lceil\pi/\omega\rceil$, including the exact-zero case. Thus $h\tau_{h^2}\to\pi$. At the saddle, $H_N=L_N+h^2I>0$ for every $N$, so its discrete first time is infinite. Both checks agree with the claimed continuous limits.

### 3. First-time convergence, including infinity and the floor

For fixed $R,C$, the scaled map is a first-order method for $(\dot q,\dot y)=(y,-\sin q)$. Both exact and discrete velocities remain bounded by $R+C$ for times at most $C$. The vector field derivatives required for a $C^1$ local truncation estimate are bounded there, uniformly in the angular coordinate. The orbit and derivative recursions quoted in the source therefore yield uniform $O(h)$ global error on that time interval. The factor $hD_j=\partial q_j/\partial y_0$ is correct.

For any fixed $t<\tau$, $J$ has a strictly positive minimum on every closed subinterval bounded away from $0$. Uniform approximation and the safeguard in part 2 show that every $D_j$ with $jh\le t$ is positive for sufficiently small $h$. If $\tau<\infty$, uniqueness of the linear ODE makes its first zero simple, with negative derivative; $J$ is negative on a nonempty interval immediately after that zero. An actual grid point can be chosen inside any fixed such interval once $h$ is sufficiently small. It has $D_j<0$, hence the first discrete failure is no later than that grid point. These lower and upper bounds prove the stated extended convergence. When $\tau=\infty$, the lower bound applies to every finite $t$, giving precisely divergence to infinity.

Let $n_h=\lfloor c/h\rfloor$. Then $hn_h\to c$. If $\tau<c$, select $t\in(\tau,c)$ and use the upper convergence bound to obtain $h\tau_{h^2}<hn_h$ eventually. If $\tau>c$, including $\tau=\infty$, select finite $t$ with $c<t<\tau$ and obtain $h\tau_{h^2}>hn_h$ eventually. Thus the indicator converges at every datum except possibly $\tau=c$. Initial values with $n_h<2$ are irrelevant because $c>0$ is fixed and $h\downarrow0$.

### 4. Null boundary and area convergence

For fixed positive $c$, the finite-time ODE solution and its Jacobi field depend real analytically on the initial point in the connected analytic cylinder. The saddle gives $J(c;\pi,0)=\sinh c\ne0$, so the real analytic function is not identically zero. Its zero set is null, and $\{\tau=c\}$ is a subset of that zero set. Measurability of the first-zero sublevels follows, for example, by expressing the condition as the minimum of the continuous function $J$ on a compact interval away from the initial zero; the comparison in part 6 supplies a uniform exclusion of early positive zeros.

The band change of variables is one-to-one for $Rh<\pi$, has Jacobian $h$, and leaves the normalization $1/(4\pi^2)$. The fixed rectangle $\mathbb T\times[-R,R]$ has finite measure. The pointwise convergence just established and the bound by $1$ justify dominated convergence.

The continuous classification in part 5 confines every finite time to $|y|<2<R$. It therefore identifies the rectangle integral with the full-cylinder integral exactly. No uniformity in $c$ or exchange with an all-time limit is used.

### 5. Energy classification, including all exceptional data

For $E>1$, velocity has fixed nonzero sign and solves the Jacobi equation. Its reduction-of-order expression is

$$
J(t)=y_0y(t)\int_0^t\frac{du}{y(u)^2}.
$$

Differentiating this expression at $0$ gives $\dot J(0)=1$. Its sign is positive. On a nonstationary separatrix, reaching $y=0$ would mean reaching a saddle at a finite time, which uniqueness excludes. The same formula is therefore valid on every finite interval. The stationary saddle has $J=\sinh t$. These statements exhaust $E\ge1$.

For $-1<E<1$, the period integral has positive energy derivative: its differentiated integrand is positive except at a null endpoint. For $y_0\ne0$, differentiating the real-lift periodicity identity gives

$$
0=\partial_{y_0}q(T(E);q_0,y_0)+y(T(E))T'(E)y_0
=J(T(E))+y_0^2T'(E).
$$

It follows that $J(T(E))<0$, so a positive zero exists. At a turning point with $y_0=0$ and $\sin q_0\ne0$, the solution $J=-y/\sin q_0$ has initial derivative $1$ and its next zero is at the next turning point, time $T(E)/2$. The sole $E=-1$ datum is the elliptic equilibrium, with $J=\sin t$. No case is left out.

The finite-time set is consequently exactly $E<1$. In the angular chart $q\in[-\pi,\pi]$, its velocity width is $4\cos(q/2)$, so its area is $16$. Monotone convergence gives the total coefficient $4/\pi^2$. Every finite-time boundary is null, and all sublevels lie in this finite-area set; dominated convergence gives continuity of $A$ at each finite positive $c$.

### 6. Threshold, unique equality, and strict increase

For any positive zero at time $t$, integration by parts and the continuous Dirichlet inequality give

$$
\left(\frac\pi t\right)^2\int_0^tJ^2
\le\int_0^t\dot J^2
=\int_0^t\cos q\,J^2
\le\int_0^tJ^2.
$$

Since $J$ is nonzero, $t\ge\pi$. At a first zero $t=\pi$, equality forces $(1-\cos q)J^2=0$ everywhere. Positivity of $J$ on $(0,\pi)$ implies $q\equiv0\pmod{2\pi}$ throughout that interval, whence $y=0$ and uniqueness identifies the elliptic initial point. This proves the exact equality case, not merely an almost-everywhere one.

At each finite first zero, the implicit function theorem produces a nearby simple zero depending continuously on initial data. Positivity on compact preceding intervals and the universal absence of zeros before $\pi$ prevent a new earlier zero. Thus this branch is the first zero. At turning data, $\tau=2K(k)$ runs continuously and strictly from $\pi$ to infinity. For each $\pi<c_1<c_2$, choose turning data with first time strictly between them and take a sufficiently small open neighborhood. It has positive area and remains in that interval of first times. This proves strict increase, and the same construction proves positivity for every $c>\pi$.

### 7. Onset coefficient, localization, and remainder

In the local chart $(a,b)=(q_0,y_0)$, the pendulum trajectory is analytic and odd under simultaneous sign reversal. Hence, uniformly on a fixed time interval beyond $\pi$,

$$
q(t)=a\cos t+b\sin t+O(r^3),\qquad r^2=a^2+b^2.
$$

The Jacobi coefficient and solution are even in $(a,b)$. Variation of constants gives the source quadratic term. Independently evaluating it at $\pi$ uses

$$
\int_0^\pi\sin^2u\cos^2u\,du=\frac\pi8,\quad
\int_0^\pi\sin^4u\,du=\frac{3\pi}8,\quad
\int_0^\pi\sin^3u\cos u\,du=0.
$$

Thus $J(\pi)=\pi(a^2+3b^2)/16+O(r^4)$. Since $\partial_tJ(\pi;0,0)=-1$, the analytic implicit root satisfies

$$
\tau(a,b)-\pi=\frac\pi{16}(a^2+3b^2)+O(r^4).
$$

There is no cubic term, and replacing the time argument by the perturbed root changes the quadratic correction only at order $r^4$.

The reduction to this local chart is global, not assumed: any sequence of finite first times converging to $\pi$ has initial data in the compact closure of $E<1$ and hence a convergent subsequence. Joint continuous dependence gives $J(\pi)=0$ at its limit. The threshold bound forbids an earlier zero, and the equality case forces that limit to be the elliptic point. The complement of a fixed open neighborhood cannot contain such a sequence. Therefore, for sufficiently small $s>0$, the whole sublevel $\tau\le\pi+s$ lies inside the chart.

For $(a,b)=\rho(\cos\theta,\sin\theta)$, set $f(\theta)=\pi(\cos^2\theta+3\sin^2\theta)/16$. Analyticity and the positive lower bound $f\ge\pi/16$ give a uniformly positive radial derivative for small $\rho>0$. The boundary is therefore a single radial graph and obeys $\rho^2=s/f+O(s^2)$ uniformly in $\theta$. Its leading ellipse has semiaxes $4\sqrt{s/\pi}$ and $4\sqrt{s/(3\pi)}$, so its area is

$$
\pi\left(4\sqrt{s/\pi}\right)\left(4\sqrt{s/(3\pi)}\right)+O(s^2)
=\frac{16}{\sqrt3}s+O(s^2).
$$

The coordinates $(a,b)$ are the original area coordinates $(q,y)$, so there is no additional chart Jacobian or multiplicity. Dividing by $4\pi^2$ gives the claimed coefficient and error order.

## Corrections or missing assumptions

No theorem correction or additional assumption is required.

Optional precision edit, source lines 242–245: replace the first assertion there by “The integral outside the band vanishes: for $\tau<c$ this follows from (7),(12), while $\tau=c$ is null by (13). Moreover, Step 5 gives the stronger pointwise support $|y|<2$.” The existing final sentence invoking Step 5 already supplies that stronger conclusion, so this is editorial only.

## Open risks and scope boundaries

- No unresolved mathematical issue remains in this independent check of the supplied V1 package.
- The proof does not establish the all-time non-minimizing area of the discrete map or justify interchanging $c\to\infty$ and $h\downarrow0$.
- Literature novelty, candidate selection, and any manuscript-production decision require their own work and are not inferred from this mathematical PASS.
- Only this new independent-check document was written. No author-source edits, external review calls, status changes, or old-artifact changes were made.
