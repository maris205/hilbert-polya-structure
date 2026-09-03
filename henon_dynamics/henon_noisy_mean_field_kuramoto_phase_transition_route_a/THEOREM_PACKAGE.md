# Theorem package: noisy mean-field Kuramoto phase transition

## 1. Frozen model and conventions

Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), represented by \([ -\pi,\pi)\), and use unnormalized Lebesgue measure \(d\theta\). A probability density therefore satisfies \(\int_{\mathbb T}p\,d\theta=1\), and the uniform density is \(p_*=1/(2\pi)\). Fix \(D>0\) and \(K\geq0\). Define

\[
 z[p]=\int_{\mathbb T}e^{i\theta}p(\theta)\,d\theta
      =r[p]e^{i\psi[p]},
\]

where the phase is irrelevant when \(r[p]=0\), and

\[
 b[p](\theta)=K\int_{\mathbb T}\sin(\phi-\theta)p(\phi)\,d\phi
              =Kr[p]\sin(\psi[p]-\theta).
\]

The dynamics is

\[
 \tag{K} \partial_t p=D\partial_\theta^2p-\partial_\theta(b[p]p).
\]

The sign, circle length, probability normalization, and order-parameter convention are frozen here.

## 2. Main theorem

**Theorem (complete identical-frequency noisy Kuramoto atlas).** Let \(0<\gamma<1\), \(D>0\), \(K\geq0\), and let \(p_0\in C^{2+\gamma}(\mathbb T)\) be nonnegative with unit mass.

1. Equation (K) has a unique global classical probability solution. It preserves mass and nonnegativity and satisfies \(p(t,\theta)>0\) for every \(t>0\). If \(p_0>0\), positivity includes \(t=0\).

2. With
   \[
   C[p](\theta)=\int_{\mathbb T}\cos(\theta-\phi)p(\phi)\,d\phi,
   \qquad
   \mu[p]=D\log p-KC[p],
   \]
   the equation has the gradient form
   \[
   \partial_t p=\partial_\theta(p\partial_\theta\mu[p]).
   \]
   For \(0<s<t\) (and also \(s=0\) when \(p_0>0\)),
   \[
   \mathcal F[p(t)]-\mathcal F[p(s)]
   =-\int_s^t\!\int_{\mathbb T}p\,|\partial_\theta\mu[p]|^2\,d\theta\,d\tau,
   \]
   where
   \[
   \mathcal F[p]=D\int_{\mathbb T}p\log p\,d\theta-\frac K2|z[p]|^2.
   \]

3. Every nonnegative \(C^2\) stationary probability density is strictly positive. The complete stationary list is the uniform density and the von Mises profiles
   \[
   q_{\kappa,\psi}(\theta)=
   \frac{e^{\kappa\cos(\theta-\psi)}}{2\pi I_0(\kappa)},
   \quad \psi\in\mathbb T,\quad \kappa>0,
   \]
   subject to
   \[
   \tag{SC} \kappa=aR(\kappa),\qquad
   a=K/D,\qquad R(\kappa)=I_1(\kappa)/I_0(\kappa).
   \]
   If \(0\leq K\leq2D\), the uniform density is the only stationary density. If \(K>2D\), (SC) has exactly one positive concentration \(\kappa(a)\); its phase orbit \(\{q_{\kappa(a),\psi}:\psi\in\mathbb T\}\) is the complete nonuniform stationary set.

4. On the real Fourier basis, the linearization at \(p_*\) has eigenvalue \(0\) on the constant mass direction, eigenvalue
   \[
   \lambda_1=K/2-D
   \]
   on \(\operatorname{span}\{\cos\theta,\sin\theta\}\), and eigenvalue \(-Dn^2\) on \(\operatorname{span}\{\cos n\theta,\sin n\theta\}\) for every \(n\geq2\). On the probability tangent space the constant direction is removed. Thus the first harmonic changes sign exactly at \(K=2D\); no Hopf conclusion is asserted.

5. Put \(\delta=a-2\). As \(\delta\downarrow0\) along the nonuniform branch,
   \[
   \kappa^2=4\delta+\frac23\delta^2+O(\delta^3),
   \qquad
   r^2=\delta-\frac56\delta^2+O(\delta^3).
   \]

## 3. Proof of the global probability flow

Write (K) as a semilinear uniformly parabolic equation. The map \(p\mapsto b[p]\) depends only on the two real first Fourier coefficients and is bounded from every Hölder space to \(C^\infty\); for a probability density,

\[
 \|\partial_\theta^j b[p]\|_\infty\leq K\qquad(j\geq0).
\]

The heat-semigroup fixed-point argument therefore gives a unique local classical solution for \(C^{2+\gamma}\) data. Integration of (K) over the circle gives mass conservation. The parabolic comparison principle preserves nonnegativity, and the strong maximum principle makes every nonzero nonnegative solution strictly positive for \(t>0\).

To exclude a finite maximal time, expand the equation as

\[
 p_t=Dp_{\theta\theta}-b[p]p_\theta-(\partial_\theta b[p])p.
\]

At a spatial maximum, \(p_\theta=0\), \(p_{\theta\theta}\leq0\), and \(|\partial_\theta b[p]|\leq K\); hence

\[
 \|p(t)\|_\infty\leq e^{Kt}\|p_0\|_\infty
\]

on every finite time interval. The coefficients \(b[p]\) and all of their spatial derivatives remain uniformly bounded. Interior and periodic Schauder estimates then bound the classical norm away from the initial time, so the local solution continues through every finite time. This proves existence, uniqueness, mass, and positivity.

## 4. Free energy and exact dissipation

Because \(\partial_\theta C[p]=\int\sin(\phi-\theta)p(\phi)d\phi=b[p]/K\) when \(K>0\) (with the equality interpreted trivially at \(K=0\)),

\[
 Dp_{\theta\theta}-\partial_\theta(b[p]p)
 =\partial_\theta\!\left[p\partial_\theta(D\log p-KC[p])\right].
\]

The first variation of the interaction term is \(-KC[p]\), since

\[
 |z[p]|^2=\iint_{\mathbb T^2}\cos(\theta-\phi)p(\theta)p(\phi)\,d\theta d\phi.
\]

Thus \(\delta\mathcal F/\delta p=D(1+\log p)-KC[p]\). The additive constant \(D\) disappears after differentiation. For positive classical solutions, periodic integration by parts gives

\[
 \frac d{dt}\mathcal F[p(t)]
 =\int\mu[p]\,\partial_\theta(p\partial_\theta\mu[p])\,d\theta
 =-\int p|\partial_\theta\mu[p]|^2\,d\theta.
\]

Integration in time proves the stated identity. Initial zeros are handled by beginning at \(s>0\), where strict positivity and smoothing already hold.

## 5. Stationary flux and von Mises exhaustion

Let \(p\) be a nonnegative stationary \(C^2\) probability density. Uniform ellipticity and the strong maximum principle imply \(p>0\). The stationary probability flux

\[
 J=b[p]p-Dp_\theta
\]

is constant. Dividing by \(p\) and integrating once around the circle gives

\[
 0=\int\frac{p_\theta}{p}\,d\theta
  =\frac1D\int b[p]\,d\theta-\frac JD\int\frac{d\theta}{p(\theta)}.
\]

The first integral on the right vanishes because \(b[p](\theta)=Kr\sin(\psi-\theta)\). The last integral is positive, so \(J=0\). Therefore

\[
 \partial_\theta\log p=\frac{Kr}{D}\sin(\psi-\theta)
 =\partial_\theta\!\left(\frac{Kr}{D}\cos(\theta-\psi)\right).
\]

Normalization yields \(p=q_{\kappa,\psi}\), where \(\kappa=Kr/D\). Direct integration of the first Fourier moment gives

\[
 z[q_{\kappa,\psi}]=e^{i\psi}\frac{I_1(\kappa)}{I_0(\kappa)}.
\]

Thus \(r=R(\kappa)\) and the stationary equation is exactly (SC). Conversely every solution of (SC) inserted into the displayed profile has zero flux, so the classification is bidirectional.

## 6. Strict Bessel-ratio/Turán lemma

**Lemma.** The function

\[
 q(\kappa)=\frac{I_1(\kappa)}{\kappa I_0(\kappa)}
\]

is strictly decreasing from \(1/2\) to \(0\) on \((0,\infty)\). Equivalently,

\[
 I_1(\kappa)^2-I_0(\kappa)I_2(\kappa)>0
\qquad(\kappa>0).
\]

**Proof.** Put \(x=\kappa^2\). The positive entire series are

\[
 I_0(\kappa)=\sum_{m\geq0}b_mx^m,qquad
 \frac{I_1(\kappa)}\kappa=\sum_{m\geq0}a_mx^m,
\]

with

\[
 b_m=\frac1{4^m(m!)^2},\qquad
 a_m=\frac1{2\,4^m m!(m+1)!},\qquad
 \frac{a_m}{b_m}=\frac1{2(m+1)}.
\]

The last ratios strictly decrease. Indeed, pairing the \((m,n)\) and \((n,m)\) terms in the derivative of the quotient gives

\[
 A'(x)B(x)-A(x)B'(x)
 =\sum_{m>n}(m-n)(a_mb_n-a_nb_m)x^{m+n-1}<0
\]

for \(x>0\), where \(A=I_1(\sqrt x)/\sqrt x\) and \(B=I_0(\sqrt x)\). Hence \(q=A/B\) is strictly decreasing and \(q(0+)=a_0/b_0=1/2\). Also \(0<R(\kappa)<1\), because \(R\) is the strict expectation of \(\cos\theta\) under the positive von Mises density, so \(q(\kappa)<1/\kappa\) and its limit is zero.

For the explicit Turán form, the termwise Bessel recurrences give

\[
 R'=1-R^2-R/\kappa,qquad I_2=I_0-2I_1/\kappa.
\]

Thus \(q'<0\) is equivalent to \(\kappa(1-R^2)<2R\), which after multiplying by \(I_0^2/\kappa\) is precisely \(I_1^2-I_0I_2>0\). This supplies, rather than assumes, the strict Turán inequality needed here. ∎

Now (SC) with \(\kappa>0\) is \(q(\kappa)=1/a\). If \(a\leq2\), then \(1/a\geq1/2\) (with \(a=0\) handled directly), so no positive solution exists. If \(a>2\), strict decrease from \(1/2\) to zero gives exactly one. This proves the stationary threshold and uniqueness modulo phase.

## 7. Uniform Fourier spectrum

Let \(p=p_*+\varepsilon u\) with \(\int u=0\). Since \(z[p_*]=0\), the linearized operator is

\[
 Lu=Du_{\theta\theta}-p_*\partial_\theta b[u],qquad
 b[u](\theta)=K\,\operatorname{Im}\!\left(z[u]e^{-i\theta}\right).
\]

For \(u=a\cos\theta+c\sin\theta\), one has \(z[u]=\pi(a+ic)\), hence

\[
 -p_*\partial_\theta b[u]=\frac K2u.
\]

Every harmonic of order \(n\geq2\) has zero first moment, so the nonlocal term vanishes and \(Lu=-Dn^2u\). Constants give the conserved mass eigenvalue zero. This proves the complete Fourier statement.

## 8. Critical expansion with analytic remainder

Exact series division gives

\[
 \frac{R(\kappa)}\kappa
 =\frac12-\frac{\kappa^2}{16}+\frac{\kappa^4}{96}
  -\frac{11\kappa^6}{6144}+O(\kappa^8).
\]

Put \(x=\kappa^2\). The function \((2+\delta)R(\sqrt x)/\sqrt x-1\) is analytic near \((x,\delta)=(0,0)\), and its \(x\)-derivative there is \(-1/8\). The analytic implicit-function theorem therefore gives an analytic \(x(\delta)\). Substitution yields

\[
 x=4\delta+\frac23\delta^2+\frac1{18}\delta^3+O(\delta^4).
\]

Because \(\kappa=(2+\delta)r\),

\[
 r^2=\frac{x}{(2+\delta)^2}
 =\delta-\frac56\delta^2+\frac{43}{72}\delta^3+O(\delta^4).
\]

The two asserted orders follow.

## 9. Boundary atlas and nonclaims

- **\(K=0\):** (K) is the heat equation; only the uniform stationary density remains, and the nonconstant spectrum is \(-Dn^2\).
- **\(K=2D\):** the first harmonic is neutral in the linearization, but strict decrease of \(q\) excludes every \(\kappa>0\) stationary profile.
- **\(K>2D\):** there is one concentration and a full \(S^1\) phase orbit, not multiple positive concentrations.
- **\(D=0\):** excluded. Atomic stationary measures and deterministic Kuramoto dynamics are outside the theorem.
- **Dynamics:** no claim is made that arbitrary solutions converge, no rate is claimed, and no Hopf or time-periodic branch is inferred from the linearization.
- **Scope:** Fourier data and free energy are source-local. They are not target arithmetic data, an Euler product, a root number, an automorphic object, a target-zero operator, or Route B.

## 10. Evidence ownership

The finite artifact independently records 17 coefficient rows, 9 quotient coefficients, 7 certified Bessel tail brackets, 4 certified nonzero-root brackets, and 162 Fourier rows. All entries are exact rationals. Positive series and geometric tail majorants certify the interval statements. These finite rows test conventions and implementations; Sections 3–8 prove the all-parameter continuum theorem.

The reconstruction follows the cited noisy-oscillator and reversible mean-field-rotator lineage and makes no priority claim.
