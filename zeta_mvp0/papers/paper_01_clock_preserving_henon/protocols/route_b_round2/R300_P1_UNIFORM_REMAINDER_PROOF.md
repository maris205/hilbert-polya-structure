# Proof Package: Uniform Relative Heat Remainder for One Hénon Warp

## Claim

Fix \(a>-1\) and \(h>0\), and define

\[
r_a=\frac{1}{1+\sqrt{1+a}},\qquad
\Psi_a(x,y)=(-2ar_ax-ax^2-y,x),
\]

\[
V_a(q)=2\pi e^{\pi|\Psi_a(q)|^2},\qquad
H_{a,h}=-\frac{h^2}{2}\Delta+V_a.
\]

Let

\[
\Theta_a(t)=\operatorname{Tr}(e^{-tH_{a,h}}),\qquad
I_a(t)=\int_{\mathbb R^2}e^{-tV_a(q)}|\nabla V_a(q)|^2\,dq,
\]

and put

\[
L=\log\frac{1}{2\pi t}.
\]

There are constants \(t_0=t_0(a,h)>0\) and \(C=C(a,h)>0\) such that,
for \(0<t<t_0\),

\[
\boxed{
\Theta_a(t)-\Theta_0(t)
=-\frac{t^2}{48\pi}\bigl(I_a(t)-I_0(t)\bigr)
+R_{a,h}(t),
\qquad
|R_{a,h}(t)|\le CtL^4.}
\tag{1}
\]

Consequently,

\[
\boxed{
\begin{aligned}
\Theta_a(t)-\Theta_0(t)
=-\frac{a^2}{24\pi}\Bigg[&L^2+
\bigl(2(1-\gamma)+4\pi r_a^2\bigr)L\\
&+\frac{\pi^2}{6}-2\gamma+\gamma^2
+4\pi r_a^2(1-\gamma)\Bigg]
+O_{a,h}(tL^4).
\end{aligned}}
\tag{2}
\]

Here \(\gamma\) is Euler's constant.  The assertion includes \(a=0\), in
which case both sides of the relative identity vanish.  For \(a\ne0\), the
coefficient of \(L^2\) is strictly negative.

## Status

`PROVABLE AS STATED`.

The proof below is a direct Brownian-bridge argument specialized to the
single polynomial Hénon warp.  It does not invoke a compact-set heat-kernel
expansion on a region whose radius depends on \(t\).

## Assumptions

- \(a>-1\) and \(h>0\) are fixed while \(t\downarrow0\).
- \(H_{a,h}\) is the Friedrichs realization on \(L^2(\mathbb R^2)\).
- \(B=(B_s)_{0\le s\le1}\) denotes a standard two-dimensional Brownian
  bridge with covariance
  \[
  \mathbb E[B_i(s)B_j(r)]
  =\delta_{ij}\bigl(\min(s,r)-sr\bigr).
  \]
- We use the standard Feynman--Kac Brownian-bridge formula for a continuous,
  nonnegative potential.  Its assumptions hold because every \(V_a\) is
  smooth and nonnegative.

## Notation

- \(Q_a=\Psi_a^{-1}\), so
  \[
  Q_a(u,v)=(v,-2ar_av-av^2-u).
  \]
- \(W(z)=2\pi e^{\pi|z|^2}\), where \(z=(u,v)\).
- \(\varepsilon=h\sqrt t\) is the Brownian amplitude.
- \(M(B)=\sup_{0\le s\le1}|B_s|\).
- \(\Phi_a(q)=\log(V_a(q)/(2\pi))=\pi|\Psi_a(q)|^2\).
- \(E_1(\lambda)=\int_\lambda^\infty e^{-w}\,dw/w\).

## Proof Strategy

First put both heat traces in the common coordinate \(z=\Psi_a(q)\).  Their
zeroth Brownian-amplitude terms then agree pointwise, so the complete
classical term cancels before any absolute-value estimate is made.  Next
Taylor-expand the exact Brownian functional in the scalar amplitude
\(\varepsilon\), not in the spatial variable on a fixed compact set.  Bridge
symmetry removes the odd orders.  Explicit Hénon displacement and normalized
derivative estimates show that the spatial integral of the fourth amplitude
derivative is \(O(L^4)\).  A Gaussian bridge tail bound, combined with a
pathwise Jensen inequality, controls the discarded Brownian paths without
multiplying a small probability by an infinite spatial volume.

## Dependency Map

1. Equation (1) depends on Lemmas 1--6.
2. Lemma 1 uses area preservation and the Brownian-bridge Feynman--Kac
   formula.
3. Lemma 2 uses only the exact polynomial formula for one Hénon warp and
   multivariate Faà di Bruno.
4. Lemmas 3--5 use the Gaussian bridge maximum tail, the fourth derivative
   of \(e^{-A}\), and one-dimensional incomplete-Gamma bounds.
5. Lemma 6 computes the second amplitude derivative and uses an integration
   by parts justified by the weighted derivative bounds in Lemma 2.
6. Equation (2) additionally uses the already established exact formula for
   \(I_a-I_0\) and two elementary Gamma moments.

## Proof

### Lemma 1: exact common-coordinate representation

For every \(t>0\),

\[
\Theta_a(t)
=\frac{1}{2\pi h^2t}
\int_{\mathbb R^2}F_a(\varepsilon,z)\,dz,
\tag{3}
\]

where

\[
F_a(\theta,z)
=\mathbb E\exp\left[-t\int_0^1
V_a\bigl(Q_a(z)+\theta B_s\bigr)\,ds\right].
\tag{4}
\]

Moreover,

\[
F_a(0,z)=e^{-tW(z)}
\tag{5}
\]

is independent of \(a\).

#### Proof

The Jacobian matrix of \(\Psi_a\) has determinant one, and the displayed
formula for \(Q_a\) is its global polynomial inverse.  Thus \(dq=dz\).  The
diagonal Brownian-bridge Feynman--Kac formula gives

\[
K_{a,h}(t;q,q)
=\frac{1}{2\pi h^2t}
\mathbb E\exp\left[-t\int_0^1
V_a(q+h\sqrt t B_s)\,ds\right].
\]

The heat semigroup is trace class.  One direct check is the
Golden--Thompson bound

\[
\Theta_a(t)
\le \frac{1}{2\pi h^2t}\int e^{-tV_a(q)}\,dq
=\frac{E_1(2\pi t)}{2\pi h^2t}<\infty.
\tag{6}
\]

Integrating the diagonal and changing variables \(q=Q_a(z)\) proves (3).
At \(\theta=0\),

\[
V_a(Q_a(z))=2\pi e^{\pi|z|^2}=W(z),
\]

which proves (5).  In particular, the zeroth-order terms for \(a\) and
\(0\) cancel pointwise in their common \(z\)-coordinate. ∎

### Lemma 2: Hénon displacement and normalized derivatives

Fix \(\delta>0\).  There are constants \(L_0=L_0(a,\delta)\) and
\(C_{a,\delta,k}\) such that the following statements hold.  For
\(z=(u,v)\), \(w=(\xi,\eta)\), and \(|w|\le1\),

\[
\Psi_a(Q_a(z)+w)
=\bigl(u-2a(r_a+v)\xi-a\xi^2-\eta,\ v+\xi\bigr),
\tag{7}
\]

\[
|\Phi_a(Q_a(z)+w)-\pi|z|^2|
\le C_{a,0}(1+\pi|z|^2)(|w|+|w|^2),
\tag{8}
\]

and, for \(1\le k\le4\),

\[
\|D^kV_a(Q_a(z)+w)\|
\le C_{a,\delta,k}V_a(Q_a(z)+w)
\bigl(1+\pi|z|^2\bigr)^k
\tag{9}
\]

whenever \(|w|\le\delta/L\) and \(L\ge L_0\).  The displacement bounds
(7)--(8) themselves do not require this last restriction.

#### Proof

Substitution of \(Q_a(z)+w\) into \(\Psi_a\) gives (7).  Hence

\[
|\Psi_a(Q_a(z)+w)-z|
\le C_a(1+|z|)|w|+C_a|w|^2.
\]

Taking the difference of the squared norms proves (8).

The polynomial \(\Phi_a\) has degree four.  Its derivatives of orders one
through four are bounded at a point \(q\) by constants times
\((1+|\Psi_a(q)|^2)^k\), and all higher derivatives of \(\Phi_a\) vanish.
The multivariate Faà di Bruno formula for
\(V_a=2\pi e^{\Phi_a}\) therefore gives

\[
V_a(q)^{-1}\|D^kV_a(q)\|
\le C_{a,k}(1+|\Psi_a(q)|^2)^k.
\]

For \(|w|\le\delta/L\), (8) implies
\(1+|\Psi_a(Q_a(z)+w)|^2\le C_{a,\delta}(1+|z|^2)\), uniformly in \(z\)
for all sufficiently large \(L\).  This proves (9). ∎

The same calculation also gives the weighted estimates used below.  If
\(\beta_1,\ldots,\beta_m\ne0\), and
\(N=\sum_j|\beta_j|\), then

\[
\int e^{-tV_a(q)}\prod_{j=1}^m
|\partial^{\beta_j}V_a(q)|\,dq
\le C_{a,\boldsymbol\beta}
t^{-m}(1+L)^N.
\tag{10}
\]

Indeed, put \(\sigma=\pi|z|^2\), \(w=tW(z)=2\pi t e^\sigma\), and use
\(dq=dz\).  Radial integration gives

\[
\int_{\mathbb R^2}g(\pi|z|^2)\,dz
=\int_0^\infty g(\sigma)\,d\sigma,
\]

and then (10) follows from

\[
\int_{2\pi t}^\infty e^{-w}w^{m-1}
\left(1+\log\frac{w}{2\pi t}\right)^N\,dw
=O_{m,N}((1+L)^N).
\tag{11}
\]

### Lemma 3: good and bad bridge events

Choose a fixed \(\delta>0\), small enough for the estimates below, and set

\[
G_t=\left\{M(B)\le\frac{\delta}{h\sqrt t\,L}\right\}.
\tag{12}
\]

There are positive constants \(c_h,C_h\) such that

\[
\mathbb P(G_t^c)
\le C_h\exp\left(-\frac{c_h}{tL^2}\right).
\tag{13}
\]

For every continuous path \(w_s\),

\[
\int_{\mathbb R^2}
e^{-t\int_0^1V_a(q+w_s)ds}\,dq
\le \int_{\mathbb R^2}e^{-tV_a(q)}\,dq
=E_1(2\pi t).
\tag{14}
\]

#### Proof

A one-dimensional Brownian bridge can be written as \(W_s-sW_1\).  The
reflection principle and a union bound over the two coordinates therefore
give \(\mathbb P(M>R)\le Ce^{-cR^2}\), which yields (13).  The bridge also has
finite moments of every order.

The function \(x\mapsto e^{-tx}\) is convex.  Jensen's inequality in the
path-time variable gives

\[
e^{-t\int_0^1V_a(q+w_s)ds}
\le\int_0^1e^{-tV_a(q+w_s)}ds.
\]

Integrate in \(q\), use translation invariance for each fixed \(s\), and
then use the area-preserving coordinate \(z=\Psi_a(q)\).  This proves (14),
because

\[
\int e^{-tW(z)}dz
=\int_{2\pi t}^{\infty}\frac{e^{-w}}w\,dw
=E_1(2\pi t)=L-\gamma+O(t).
\]

The order of integration in (14) is essential: it prevents a small bridge
probability from being multiplied by the infinite volume of
\(\mathbb R^2\). ∎

### Lemma 4: integrated fourth amplitude derivative

For

\[
A_a(\theta,z,B)
=t\int_0^1V_a(Q_a(z)+\theta B_s)\,ds,
\qquad
f_a(\theta,z,B)=e^{-A_a(\theta,z,B)},
\]

one has

\[
\int_{\mathbb R^2}
\sup_{|\theta|\le\varepsilon}
\mathbb E\left[
\mathbf1_{G_t}|\partial_\theta^4 f_a(\theta,z,B)|
\right]dz
\le C_aL^4.
\tag{15}
\]

#### Proof

For \(1\le k\le4\),

\[
A_a^{(k)}(\theta)
=t\int_0^1D^kV_a(Q_a(z)+\theta B_s)
[B_s,\ldots,B_s]ds.
\tag{16}
\]

Differentiating \(e^{-A}\) four times gives

\[
\partial_\theta^4e^{-A}
=e^{-A}\left[(A')^4-6(A')^2A''+3(A'')^2
+4A'A'''-A^{(4)}\right].
\tag{17}
\]

On \(G_t\), \(|\theta B_s|\le\delta/L\).  Split the \(z\)-space using

\[
\sigma=\pi|z|^2,
\qquad
\sigma_*(t)=L+8\log L.
\]

On the main region \(0\le\sigma\le\sigma_*\), (8) gives

\[
c_aY\le tV_a(Q_a(z)+\theta B_s)\le C_aY,
\qquad
Y=e^{\sigma-L},
\tag{18}
\]

after decreasing \(t_0\) if necessary.  Equations (9), (16), and (17) imply

\[
|\partial_\theta^4f_a|
\le C_aM^4(1+\sigma)^4
\sum_{m=1}^4Y^me^{-c_aY}.
\tag{19}
\]

Since \(\mathbb E[M^4]<\infty\), radial integration and the substitution
\(Y=e^{\sigma-L}\) show that

\[
\int_0^{\sigma_*}(1+\sigma)^4
\sum_{m=1}^4Y^me^{-c_aY}\,d\sigma
\le C_aL^4.
\tag{20}
\]

There is no additional factor of \(L\): every summand contains at least one
factor \(Y\), and \(d\sigma=dY/Y\).

On the tail \(\sigma>\sigma_*\), put

\[
\alpha_L=C_a\left(\frac{\delta}{L}+\frac{\delta^2}{L^2}\right).
\]

After increasing \(C_a\) once, (8) gives

\[
tV_a(Q_a(z)+\theta B_s)
\ge \exp\left[
-L+(1-\alpha_L)\sigma-\alpha_L
\right].
\tag{21}
\]

The analogous upper bound replaces both minus signs involving \(\alpha_L\)
by plus signs.  Put

\[
y=\exp\left[
-L+(1-\alpha_L)\sigma-\alpha_L
\right].
\]

For fixed sufficiently small \(\delta\) and large \(L\), the lower endpoint
of \(y\) is at least \(L^7\).  The upper potential in (16) is at most a
constant times \(y^{p_L}\), where

\[
p_L=\frac{1+\alpha_L}{1-\alpha_L}
=1+O_{a,\delta}(L^{-1}).
\]

The change of variables contributes the uniformly bounded Jacobian factor
\((1-\alpha_L)^{-1}\).  Thus the tail integral in (15) is bounded by a finite
sum of incomplete-Gamma tails of the form

\[
C_{a,\delta}\int_{L^7}^{\infty}
(1+L+\log y)^4y^{mp_L-1}e^{-c_ay}\,dy,
\qquad 1\le m\le4.
\tag{22}
\]

This is \(O_{a,N}(L^{-N})\) for every fixed \(N\).  Combining (20) and
(22) proves (15).  The displayed bounds also justify differentiating under
the bridge expectation and the spatial integral. ∎

### Lemma 5: exact amplitude expansion with uniform remainder

For each fixed \(a>-1\),

\[
\int_{\mathbb R^2}
\left|
F_a(\varepsilon,z)-F_a(0,z)
-\frac{\varepsilon^2}{2}\partial_\theta^2F_a(0,z)
\right|dz
\le C_{a,h}t^2L^4.
\tag{23}
\]

#### Proof

First restrict the expectation defining \(F_a\) to \(G_t\).  The event is
invariant under \(B\mapsto-B\), while

\[
f_a(-\theta,z,B)=f_a(\theta,z,-B).
\]

Hence the restricted expectation is an even function of \(\theta\).  Taylor's
theorem, (15), and \(\varepsilon=h\sqrt t\) give an integrated good-event
remainder bounded by

\[
\frac{\varepsilon^4}{24}C_aL^4
\le C_{a,h}t^2L^4.
\tag{24}
\]

It remains to restore \(G_t^c\).  By (13)--(14),

\[
\int\mathbb E\left[
\mathbf1_{G_t^c}f_a(\varepsilon,z,B)
\right]dz
\le C_hE_1(2\pi t)
e^{-c_h/(tL^2)}.
\tag{25}
\]

The same bound at \(\theta=0\) is immediate.  The bad-event expectation may
also be differentiated twice.  Here is the required neighborhood domination.
Fix \(z,t\) and \(\theta_0>0\).  The exact
polynomial displacement (7) implies, for \(|\theta|\le\theta_0\),

\[
\frac{\|DV_a(Q_a(z)+\theta B_s)\|}
{V_a(Q_a(z)+\theta B_s)}
\le C_{a,z,\theta_0}(1+M)^4,
\]

\[
\frac{\|D^2V_a(Q_a(z)+\theta B_s)\|}
{V_a(Q_a(z)+\theta B_s)}
\le C_{a,z,\theta_0}(1+M)^8.
\]

Consequently, with \(A=A_a(\theta,z,B)\),

\[
|A'|\le C_{a,z,\theta_0}(1+M)^5A,
\qquad
|A''|\le C_{a,z,\theta_0}(1+M)^{10}A.
\]

Since

\[
f_a''=e^{-A}\bigl((A')^2-A''\bigr),
\]

and both \(xe^{-x}\) and \(x^2e^{-x}\) are bounded on \([0,\infty)\),

\[
\sup_{|\theta|\le\theta_0}|f_a''(\theta,z,B)|
\le C_{a,z,\theta_0}(1+M)^{10}.
\tag{25a}
\]

The Brownian-bridge maximum has Gaussian tails, so the right side is
integrable.  The analogous first-derivative bound follows from the estimate
for \(A'\).  Dominated differentiation therefore proves

\[
\left.\partial_\theta^2
\mathbb E[\mathbf1_{G_t^c}f_a(\theta,z,B)]\right|_{\theta=0}
=\mathbb E[\mathbf1_{G_t^c}f_a''(0,z,B)].
\tag{25b}
\]

At \(\theta=0\), the second derivative reads

\[
\partial_\theta^2f_a(0)
=e^{-tV_a}\left[
t^2\left(\nabla V_a\cdot\int_0^1B_sds\right)^2
-t\int_0^1D^2V_a[B_s,B_s]ds
\right].
\]

Equation (10), followed by the Gaussian tail moment bound, yields

\[
\int\mathbb E\left[
\mathbf1_{G_t^c}|\partial_\theta^2f_a(0)|
\right]dz
\le C_{a,h}L^2e^{-c_h/(2tL^2)}.
\tag{26}
\]

After multiplication by \(\varepsilon^2\), (25)--(26) are smaller than the
right-hand side of (23) for all sufficiently small \(t\).  This proves
(23). ∎

### Lemma 6: the second amplitude coefficient

For every fixed \(a\),

\[
\frac{1}{2\pi h^2t}\frac{\varepsilon^2}{2}
\int_{\mathbb R^2}\partial_\theta^2F_a(0,z)dz
=-\frac{t^2}{48\pi}I_a(t).
\tag{27}
\]

#### Proof

The bridge covariances give

\[
\mathbb E\left[
\left(\int_0^1B_i(s)ds\right)
\left(\int_0^1B_j(s)ds\right)
\right]=\frac{\delta_{ij}}{12},
\]

\[
\int_0^1\mathbb E[B_i(s)B_j(s)]ds
=\frac{\delta_{ij}}6.
\]

Therefore

\[
\partial_\theta^2F_a(0,z)
=e^{-tV_a(Q_a(z))}
\left[
\frac{t^2}{12}|\nabla V_a(Q_a(z))|^2
-\frac t6\Delta V_a(Q_a(z))
\right].
\tag{28}
\]

Because \(dz=dq\), substitution into the left side of (27) gives

\[
\frac{t^2}{48\pi}I_a(t)
-\frac{t}{24\pi}\int e^{-tV_a}\Delta V_a\,dq.
\]

The weighted estimate (10) shows that
\(e^{-tV_a}|\nabla V_a|\),
\(e^{-tV_a}|\nabla V_a|^2\), and
\(e^{-tV_a}|\Delta V_a|\) are integrable.  Apply integration by parts with
cutoffs \(\chi_R\) satisfying \(\chi_R\to1\) pointwise and
\(\|\nabla\chi_R\|_\infty=O(R^{-1})\).  The cutoff cross term tends to zero
by dominated convergence using the first of these integrable functions.
Therefore

\[
\int e^{-tV_a}\Delta V_a\,dq
=t\int e^{-tV_a}|\nabla V_a|^2dq
=tI_a(t).
\tag{29}
\]

The two terms combine to give (27). ∎

### Completion of equation (1)

Apply Lemma 5 to \(a\) and to \(0\), insert both expansions into (3), and
subtract.  Equation (5) cancels the complete classical term before the
remainders are bounded.  Lemma 6 supplies the second-order difference.
Finally,

\[
\frac{1}{2\pi h^2t}\,O_{a,h}(h^4t^2L^4)
=O_{a,h}(tL^4).
\]

This proves (1). ∎

### Completion of equation (2)

The exact carrier identity is

\[
I_a(t)-I_0(t)
=\frac{2a^2}{t^2}
\left[A_2(2\pi t)+4\pi r_a^2A_1(2\pi t)\right],
\tag{30}
\]

where

\[
A_k(\lambda)=\int_\lambda^\infty
we^{-w}\left(\log\frac w\lambda\right)^k\,dw.
\]

The Gamma moments

\[
\int_0^\infty we^{-w}\log w\,dw=1-\gamma,
\]

\[
\int_0^\infty we^{-w}(\log w)^2dw
=\frac{\pi^2}{6}-2\gamma+\gamma^2
\]

give

\[
A_1(2\pi t)=L+1-\gamma+O(t^2),
\]

\[
A_2(2\pi t)=L^2+2(1-\gamma)L
+\frac{\pi^2}{6}-2\gamma+\gamma^2+O(t^2).
\]

Substituting these into (1) proves (2), because \(t^2=O(tL^4)\) as
\(t\downarrow0\). ∎

## Corrections or Missing Assumptions

- The former statement with an unproved “uniform noncompact remainder
  hypothesis” is no longer needed for the single warp: Lemmas 1--6 prove the
  required bound directly.
- The theorem is for fixed \(a\) and fixed \(h>0\).  It does not assert a
  bound uniform in an unbounded \(a\)-range or in a varying semiclassical
  parameter \(h=h(t)\).
- The proof uses positivity.  It does not directly extend to a magnetic
  operator, whose Feynman--Kac representation contains a stochastic phase.
- The exponent \(L^4\) is specific to the first omitted, fourth-amplitude
  order for one Hénon warp.  An iterate \(\Psi_a^n\) requires a new derivative
  audit.

## Open Risks

- The cited general Feynman--Kac source states the noncompact Friedrichs
  semigroup formula.  A publication version should either cite its standard
  Euclidean Brownian-bridge disintegration corollary explicitly or include
  the one-line conditioning argument.
- The result proves an analytic relative spectral invariant.  It supplies no
  rational-prime times, von Mangoldt amplitudes, explicit formula, or
  Riemann-hypothesis implication.

## Standard analytic input citations

- S. Boldt and B. Güneysu, “Feynman--Kac formula for perturbations of order
  \(\le1\), and noncommutative geometry,” *Stochastics and Partial
  Differential Equations: Analysis and Computations* **11** (2023),
  1519--1552, https://doi.org/10.1007/s40072-022-00269-3.
- J. Stubbe, “Universal monotonicity of eigenvalue moments and sharp
  Lieb--Thirring inequalities,” *Journal of the European Mathematical
  Society* **12** (2010), 1347--1353,
  https://doi.org/10.4171/JEMS/233.  Its heat-trace phase-space bound applies
  because \(\int e^{-tV_a}=E_1(2\pi t)<\infty\).
