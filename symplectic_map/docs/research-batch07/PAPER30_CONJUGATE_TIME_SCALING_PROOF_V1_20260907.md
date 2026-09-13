# Proof package: finite-time conjugate-area scaling for the sine twist map

Date: 2026-09-07. Author proof V1, not a formal Paper30 candidate or an
independent-review result. This is a new within-family problem; no accepted
paper, frozen proof, or earlier failed candidate is changed.

## Claim

On the torus $\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2$, consider
$$
F_\varepsilon(q,p)=(q+p-\varepsilon\sin q,\ p-\varepsilon\sin q),
\qquad \varepsilon>0.
$$
Coordinates on the right are reduced modulo $2\pi$. Put $h=\sqrt\varepsilon$.
For an orbit $(q_j,p_j)=F_\varepsilon^j(q_0,p_0)$ and $N\ge2$, let
$$
Q_N(v)=\sum_{j=0}^{N-1}(v_{j+1}-v_j)^2
       -h^2\sum_{j=1}^{N-1}\cos q_j\,v_j^2,
\qquad v_0=v_N=0.
$$
Define the first loss of Dirichlet positivity by
$$
\tau_\varepsilon(q_0,p_0)
=\min\{N\ge2:Q_N\text{ is not positive definite}\},
$$
with value $+\infty$ if the set is empty. This definition includes a zero
eigenvalue as a loss of positivity; it does not require a discrete Jacobi
solution to vanish exactly at an integer time.

Let $m=(4\pi^2)^{-1}dq\,dp$ be normalized torus area. For every fixed $c>0$,
$$
\boxed{\quad
\lim_{\varepsilon\downarrow0}\varepsilon^{-1/2}
m\{\tau_\varepsilon\le\lfloor c/\sqrt\varepsilon\rfloor\}=A(c).
\quad}                                                     \tag{1}
$$
The function $A$ is given without fitting by the pendulum initial-value problem
$$
\dot q=y,\qquad \dot y=-\sin q,\qquad
\ddot J+\cos q(t)J=0,\qquad J(0)=0,\quad \dot J(0)=1:
$$
if $\tau(q,y)$ is the first positive zero of $J$, or $+\infty$, then
$$
A(c)=\frac1{4\pi^2}\int_{\mathbb T\times\mathbb R}
                 \mathbf1_{\{\tau(q,y)\le c\}}\,dq\,dy.       \tag{2}
$$
In addition:

1. $A$ is continuous on $(0,\infty)$, is zero for $0<c\le\pi$, and is
   strictly increasing for $c>\pi$.
2. $\lim_{c\to\infty}A(c)=4/\pi^2$.
3. For $s\downarrow0$,
   $$A(\pi+s)=\frac4{\sqrt3\,\pi^2}s+O(s^2).                 \tag{3}$$

Equation (1) is a fixed-$c$ limit. It does not interchange
$c\to\infty$ with $\varepsilon\downarrow0$, estimate the all-time
non-minimizing set of the map, or assert a uniform-in-$c$ error bound.

## Status

PROVABLE AS STATED — author proof below. Independent verification is pending.
This is a mathematical status, not a novelty, research-value, page-capacity,
Route A/B, PDF, or publication verdict.

## Assumptions and notation

- Only the displayed sine twist map and the one-sided limit $\varepsilon>0$
  are considered. No target spectral data are used.
- During finite orbit estimates, $q_j,p_j$ denote consistent real lifts with
  $p_{j+1}=p_j-h^2\sin q_j$, $q_{j+1}=q_j+p_{j+1}$.
- The initial momentum representative is $p_0\in[-\pi,\pi)$.
- $H_N$ is the $(N-1)$-by-$(N-1)$ symmetric matrix of $Q_N$; $H_1$ is
  empty and is regarded as positive definite.
- $\|v\|_2^2=\sum_{j=1}^{N-1}v_j^2$ and
  $\|\Delta v\|_2^2=\sum_{j=0}^{N-1}(v_{j+1}-v_j)^2$.
- $\tau$ always denotes the continuous first zero; $\tau_\varepsilon$
  denotes the discrete first failure of positivity.

The generating function is
$S(q,Q)=\tfrac12(Q-q)^2+\varepsilon\cos q$:
$p=-S_q=Q-q+\varepsilon\sin q$ and $P=S_Q=Q-q$.
Thus the quadratic forms above are exactly the fixed-endpoint action
Hessians, with all signs and endpoint indices specified.

## Proof strategy and dependency map

1. A global Abel-summation estimate confines every early loss of positivity
   to $|p_0|\le R(c)h$. It treats the whole complementary torus, not just
   one nonresonant compact set.
2. In that band, $p=hy$ turns the map into the symplectic Euler scheme for
   the displayed pendulum. Its $C^1$ convergence and Sylvester's criterion
   give convergence of first conjugate times.
3. Analytic dependence makes every fixed-time boundary null; a change of
   variables and dominated convergence prove (1).
4. The energy integral classifies the finite continuous times. Sturm
   comparison, expressed as a Dirichlet inequality, and a local expansion
   prove the three additional properties.

The standard facts used explicitly are: the eigenvalues of a Dirichlet
tridiagonal Laplacian, Sylvester's criterion, discrete Gronwall, uniqueness
and smooth/analytic parameter dependence for smooth/analytic ODEs on a
fixed finite interval, the null-zero-set theorem for a nonzero real analytic
function, the implicit function theorem, and dominated/monotone convergence.
Their hypotheses are checked at their uses. The pendulum appears as a
scaling limit of this discrete map, not as a separate appended system.

## Proof

### Step 1. A global nonresonant positivity estimate

Fix $c>0$, set $R=100(c+1)$, and take $h>0$ small enough that $Rh<\pi$.
Suppose $|p_0|>Rh$ and $2\le N\le c/h$. For $0\le j\le N$,
$$
|p_j-p_0|\le jh^2\le ch.
$$
Distance to $2\pi\mathbb Z$ is a 1-Lipschitz function on $\mathbb R$.
Since its value at our initial representative is $|p_0|$, it follows that
$$
|1-e^{ip_j}|\ge \frac2\pi\operatorname{dist}(p_j,2\pi\mathbb Z)
>\delta,\qquad \delta=\frac2\pi(R-c)h.                     \tag{4}
$$
The first inequality uses $\sin u\ge2u/\pi$ for $0\le u\le\pi/2$.
This argument remains valid if a lifted momentum crosses $\pi$ or $-\pi$.

Write $z_j=e^{iq_j}$ and $a_j=(1-e^{ip_{j+1}})^{-1}$. Then
$z_j=a_j(z_j-z_{j+1})$, $|a_j|\le\delta^{-1}$, and
$$
|a_j-a_{j-1}|
\le\frac{|e^{ip_{j+1}}-e^{ip_j}|}{\delta^2}
\le h^2\delta^{-2}.
$$
For $1\le k\le N-1$, summation by parts gives
$$
\left|\sum_{j=1}^k z_j\right|
\le2\delta^{-1}+(k-1)h^2\delta^{-2}
\le B,\qquad B=2\delta^{-1}+Nh^2\delta^{-2}.               \tag{5}
$$
For $C_k=\sum_{j=1}^k\cos q_j$, $|C_k|\le B$. Since $v_N=0$,
$$
\sum_{j=1}^{N-1}\cos q_jv_j^2
=\sum_{j=1}^{N-1}C_j(v_j^2-v_{j+1}^2).
$$
Cauchy--Schwarz and $\sum_{j=1}^{N-1}(v_j+v_{j+1})^2\le4\|v\|_2^2$
therefore give an absolute bound $2B\|v\|_2\|\Delta v\|_2$.
The Dirichlet Laplacian has least eigenvalue $4\sin^2(\pi/(2N))$.
Since $\sin(\pi/(2N))\ge1/N$, its Poincare inequality implies
$\|v\|_2\le(N/2)\|\Delta v\|_2$. Consequently
$$
Q_N(v)\ge(1-h^2BN)\|\Delta v\|_2^2,
\qquad
h^2BN\le\frac{\pi c}{R-c}+\frac{\pi^2c^2}{4(R-c)^2}<\frac12. \tag{6}
$$
For the last strict inequality use $c/(R-c)<1/99$ and $\pi<4$.
Thus $H_N$ is positive definite for every such $N$. We have proved
$$
\{\tau_{h^2}\le\lfloor c/h\rfloor\}
\subset\{|p_0|\le R(c)h\}.                                 \tag{7}
$$
There is no exclusion of other rational rotation bands in this inclusion.

### Step 2. Discrete Jacobi minors and the short-time safeguard

Let $D_j=\partial q_j/\partial p_0$ with $q_0$ fixed. Differentiating the
second-order orbit equation yields
$$
D_0=0,\quad D_1=1,\quad
D_{j+1}=(2-h^2\cos q_j)D_j-D_{j-1}.                         \tag{8}
$$
The determinant of the leading $k$-by-$k$ block of $H_N$ obeys the same
recursion, with empty determinant 1. It is therefore $D_{k+1}$.
Sylvester's criterion, applicable to the real symmetric matrix $H_N$,
states precisely
$$H_N>0\quad\Longleftrightarrow\quad D_2,\ldots,D_N>0.        \tag{9}$$

Uniform approximation to a Jacobi solution by itself would not control a
neighborhood of its zero at time 0. Here that neighborhood is controlled
directly: since $\cos q_j\le1$,
$$
H_N\ge L_N-h^2I,
$$
where $L_N$ is the Dirichlet Laplacian. If $Nh\le\pi/2$, then
$h^2\le\pi^2/(4N^2)<4/N^2\le\lambda_{\min}(L_N)$.
Hence every orbit has $H_N>0$ on this short interval.

### Step 3. Local $C^1$ convergence and first times

On any fixed set $|y_0|\le R$, substitute $p_j=hy_j$. The lifted update is
$$y_{j+1}=y_j-h\sin q_j,\qquad q_{j+1}=q_j+hy_{j+1}.          \tag{10}$$
For $jh\le C$ its momenta satisfy $|y_j|\le R+C$; the exact pendulum
flow satisfies the same bound. On this region the vector field and its
first two derivatives are bounded (with the velocity component bounded
by $R+C$). Taylor's formula for the exact flow over one step shows that
the map (10) and its first derivative have one-step errors $O(h^2)$.
The constants are uniform in $q_0\in\mathbb T$, $|y_0|\le R$.

For completeness, the orbit error satisfies
$e_{j+1}\le(1+Lh)e_j+Kh^2$. The derivative matrices remain bounded by
$(1+Lh)^j$ times a fixed constant. Applying the same recursion to their
difference adds only $Kh e_j$ to the one-step forcing. Summing the first
recursion gives $\max_{jh\le C}e_j=O(h)$; inserting this in the derivative
recursion gives an $O(h)$ derivative error. This is the discrete Gronwall
estimate with fixed $C,R$, and proves uniform $C^1$ convergence.
In particular
$$
\sup_{jh\le C}|hD_j-J(jh;q_0,y_0)|=O(h),                    \tag{11}
$$
because $hD_j=\partial q_j/\partial y_0$.

A positive zero of $J$ is simple: otherwise $J=\dot J=0$ at one time,
and uniqueness for its linear ODE would contradict $\dot J(0)=1$.
If $t<\tau(q_0,y_0)$, positivity on a closed interval away from 0 and
(11), together with Step 2 near 0, imply positivity of all $D_j$ for
$jh\le t$ when $h$ is sufficiently small. By (9), no discrete loss
occurs by that time. If $\tau<\infty$, the simple first zero is followed
by a negative interval of $J$; (11) gives a negative $D_j$ at a grid time
arbitrarily close above $\tau$, and (9) forces a loss no later than that
grid time. Thus, in the extended half-line,
$$h\tau_{h^2}(q_0,hy_0)\longrightarrow\tau(q_0,y_0).         \tag{12}$$
For $\tau=\infty$, this means divergence past every fixed finite time;
it makes no assertion about the eventual fate at fixed $h$.

### Step 4. Null boundaries and the area limit

For each $c>0$, $J(c;q,y)$ is real analytic in $(q,y)$. The analytic
ODE has solutions for all finite times because $|\dot y|\le1$; analytic
parameter dependence holds locally near every initial condition on
that interval. It is not identically zero on the connected cylinder:
at the stationary saddle $(q,y)=(\pi,0)$ it equals $\sinh c>0$.
The zero set of a nonzero real analytic function on a connected real
analytic manifold has Lebesgue measure zero. It follows that
$$\operatorname{Leb}\{(q,y):\tau(q,y)=c\}=0.                 \tag{13}$$

By (7), a change of variables $p=hy$ gives, for small $h$,
$$
h^{-1}m\{\tau_{h^2}\le\lfloor c/h\rfloor\}
=\frac1{4\pi^2}\int_{\mathbb T\times[-R(c),R(c)]}
\mathbf1_{\{\tau_{h^2}(q,hy)\le\lfloor c/h\rfloor\}}dq\,dy.
$$
Equations (12)--(13) give pointwise convergence off a null set to
$\mathbf1_{\{\tau\le c\}}$. The domain has finite measure and the
integrands are bounded by 1, so dominated convergence applies.
No finite continuous time at most $c$ can occur with $|y|>R(c)$:
for $\tau<c$ this follows already from (7),(12); the remaining
$\tau=c$ set is null by (13). Alternatively Step 5 below confines every
finite time to $|y|<2<R(c)$. We obtain (1)--(2).

### Step 5. Exactly which pendulum data have a finite first time

The conserved energy is $E=y^2/2-\cos q$. For $E>1$, the velocity $y(t)$
is nonzero and retains its sign for all time. It solves the Jacobi
equation (differentiate the flow with respect to time). Reduction of
order, with the specified initial derivative, gives
$$J(t)=y(0)y(t)\int_0^t\frac{du}{y(u)^2}>0\quad(t>0).         \tag{14}$$
The formula also holds at every finite time on a nonconstant separatrix
$E=1$, whose velocity never reaches zero at a finite time. The remaining
data of energy 1 are the stationary saddle, where $J=\sinh t$.
Thus all data with $E\ge1$ have $\tau=\infty$.

For $-1<E<1$ the orbit librates, with period
$$
T(E)=4K(k),\qquad k^2=(E+1)/2,\qquad
K(k)=\int_0^{\pi/2}(1-k^2\sin^2\theta)^{-1/2}\,d\theta.
$$
Differentiation under the integral on any compact subinterval of
$-1<E<1$ shows $T'(E)>0$. If $y(0)\ne0$, choose a real libration lift;
$q(T(E);q_0,y_0)=q_0$. Differentiating in $y_0$ with $q_0$ fixed gives
$$J(T(E))=-y_0^2T'(E)<0.                                   \tag{15}$$
Since $J(t)>0$ for small positive time, a positive zero exists.
If $y_0=0$ but $q_0\not\equiv0,\pi$, then
$J(t)=-y(t)/\sin q_0$ solves the Jacobi initial-value problem. Its first
positive zero is the next turning point at $T(E)/2$.
At the remaining elliptic equilibrium $(0,0)$, $J=\sin t$ and
$\tau=\pi$. We have proved the exact classification
$$\tau(q,y)<\infty\quad\Longleftrightarrow\quad E(q,y)<1.    \tag{16}$$
The set on the right lies in $|y|<2$ and has area
$$
\int_{-\pi}^{\pi}4\cos(q/2)\,dq=16.
$$
Monotone convergence in (2) now proves $A(c)\to16/(4\pi^2)=4/\pi^2$.
Together with (13), the same bounded support proves continuity of $A$.

### Step 6. Threshold, equality case, and strict increase

If $\tau=t<\infty$, multiply the Jacobi equation by $J$ and integrate
on $[0,t]$. Both endpoint values are zero, so
$$
\int_0^t\dot J^2=\int_0^t\cos q\,J^2\le\int_0^t J^2.
$$
The continuous Dirichlet Poincare inequality on $[0,t]$ gives
$\int\dot J^2\ge(\pi/t)^2\int J^2$, whence $t\ge\pi$.
If $t=\pi$, equality forces $(1-\cos q)J^2$ to vanish everywhere.
The first-zero definition gives $J>0$ on $(0,\pi)$, so $q$ is the
constant $0$ modulo $2\pi$ there. The orbit is $(0,0)$ by uniqueness.
Thus the threshold sublevel has zero area and $A(c)=0$ for $c\le\pi$.

The first zero is continuous near every data point with finite $\tau$:
apply the implicit function theorem at the simple zero, keep positivity
on each closed preceding interval, and use the uniform short-time
Dirichlet comparison to rule out an earlier zero near 0.
At turning-point initial data, $\tau=T(E)/2$. This value ranges
continuously and strictly from $\pi$ to $+\infty$ as $E$ ranges from
$-1$ to 1: monotonicity was proved above, the lower limit follows from
$K(0)=\pi/2$, and the upper limit follows by monotone convergence of
the integral defining $K$ to the nonintegrable $1/\cos\theta$.
For every $\pi<c_1<c_2$, choose such data with
$c_1<\tau<c_2$. Continuity gives an open set of positive area with
the same strict inequalities, proving $A(c_2)>A(c_1)$.
The argument also gives $A(c)>0$ for every $c>\pi$.

### Step 7. The threshold coefficient

Use local initial coordinates $(a,b)=(q_0,y_0)$ near $(0,0)$ and put
$r^2=a^2+b^2$. Analytic dependence, oddness under $(a,b)\mapsto(-a,-b)$,
and the linearized pendulum yield, uniformly on a fixed interval
containing $[0,\pi]$,
$$q(t)=a\cos t+b\sin t+O(r^3).$$
Consequently $\cos q(t)=1-\tfrac12(a\cos t+b\sin t)^2+O(r^4)$.
Expanding the Jacobi equation by degree gives
$$
J(t)=\sin t+j_2(t)+O(r^4),\qquad
j_2(t)=\frac12\int_0^t\sin(t-u)(a\cos u+b\sin u)^2\sin u\,du.
$$
In particular the mixed integral at $t=\pi$ vanishes and
$$
j_2(\pi)=\frac\pi{16}(a^2+3b^2).
$$
Since $\partial_tJ(\pi;0,0)=-1$, the implicit function theorem and
the first-zero continuity from Step 6 imply
$$
\tau(a,b)=\pi+\frac\pi{16}(a^2+3b^2)+O(r^4).                \tag{17}
$$

Only this neighborhood contributes when $c$ is sufficiently close
above $\pi$. To verify this assertion, suppose a sequence of data
outside a fixed neighborhood has finite $\tau_n\downarrow\pi$.
By (16) it has a convergent subsequence in the compact closure of
$\{E<1\}$; continuous dependence gives $J(\pi)=0$ at its limit.
The Dirichlet comparison excludes any earlier zero at the limit,
so its first zero is $\pi$. Step 6 forces the limit to be $(0,0)$,
contradicting the choice of neighborhood.

Write $a=\rho\cos\theta$, $b=\rho\sin\theta$. Equation (17) has the
form $\tau-\pi=\rho^2 f(\theta)+O(\rho^4)$, where
$f(\theta)=\pi(\cos^2\theta+3\sin^2\theta)/16\ge\pi/16$.
Analyticity makes the radial derivative $2\rho f+O(\rho^3)>0$ for
small $\rho>0$, uniformly in $\theta$. The sublevel boundary for
$s=c-\pi>0$ therefore satisfies
$\rho^2=s/f(\theta)+O(s^2)$ uniformly. Its area is
$$
\frac12\int_0^{2\pi}\rho^2\,d\theta
=\frac{16}{\sqrt3}s+O(s^2),
$$
equivalently the leading ellipse has semiaxes
$4\sqrt{s/\pi}$ and $4\sqrt{s/(3\pi)}$.
Division by $4\pi^2$ proves (3). This completes the proof. $\square$

## Corrections or missing assumptions

None added to the displayed theorem. The initial informal phrase
“first conjugate point” is resolved by the explicit Dirichlet-positivity
definition; exact vanishing at an integer iterate is not being assumed.
The all-$c$ statement follows from (13), rather than assuming unverified
continuity points. The all-time measure of the discrete map remains
outside the theorem.

## Open risks and evaluation boundaries

- Independent checks must inspect the global estimate (4)--(7), the
  indexing and positivity convention (8)--(9), the zero-at-time-0 issue,
  and the normalization and remainder in (3).
- Literature matching is separate and unfinished at author-proof time.
  Qualitative conjugate-point/torsion results and the symplectic-Euler
  limit are prior machinery, not automatically new contributions.
- This file makes no claim to natural 22--30-page capacity. If the
  nonduplicated theorem package is short, it must remain a preserved
  mathematical result without being stretched into Paper30.
- No numerical experiment, PDF build, external communication, or
  acceptance-counter change has been performed for this proof.
