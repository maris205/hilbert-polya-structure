# Pre-P Relative Trace Carrier Audit

## Scope and status

This audit concerns the pair

\[
 H_j=\frac12(-i\nabla-A_B)^2+V_j(q),\qquad j=0,1,
\]

with

\[
 V_0(q)=2\pi e^{\pi|q|^2},\qquad
 V_1(q)=2\pi e^{\pi|\Psi(q)|^2},\qquad
 \Psi=\widetilde H_a^n,
\]

for fixed \(a>-1\), \(a\ne0\), fixed \(n\ge1\), and fixed magnetic field \(B\).
The immediate question is whether the pair supplies a mathematically valid
signed relative spectral object that could eventually host a prime-power
trace.  It is not an attempt to infer primes from the already observed level
statistics.

| Subroute | Status | Reason |
|---|---|---|
| First-resolvent Krein pair | **Not established; disfavored** | The first resolvent difference is automatically in \(\mathcal S_p\) for \(p>1\), but trace-class membership is unsupported and its principal-symbol \(L^1\) diagnostic diverges. |
| Resolvent-power spectral shift | **Proved C-admissibility** | Every individual resolvent power of integer order \(m\ge2\) is trace class; hence their difference is trace class, and the odd choice \(m=3\) permits Yafaev's invariance-principle construction. |
| Discrete relative counting shift | **Proved C-admissibility** | It has the canonical normalization \(\xi(E)=N_0(E)-N_1(E)\). |
| Relative heat trace | **Proved C-admissibility for every \(t>0\)** | Both heat semigroups are trace class. |
| Relative wave trace | **Rigorous as a tempered distribution** | It is not presently an ordinary operator trace. |
| Periodic-orbit interface | **Conditional** | It requires an energy-localized trace theorem and control of the radial orbit families. |
| Endogenous prime powers | **Open** | No \(r\log p\) periods or \((\log p)p^{-r/2}\) amplitudes have been derived. |

The net conclusion is that this route supplies a rigorous **signed spectral
container**, but not an arithmetic P gate.

## 1. Operator-theoretic normalization

Both operators are defined independently by their closed, lower-semibounded
quadratic forms.  They are self-adjoint and have compact resolvent.  The
project's Weyl theorem gives, with a safe fixed exponent \(K\),

\[
 N_j(E)=\frac{E}{2\pi}\log\frac{E}{2\pi}
       -\frac{E}{2\pi}
       +O\!\left(E^{3/4}(\log E)^K\right).
\]

For the \(n\)-fold Hénon warp one may take the existing safe logarithmic
power \(K=1+2^{n-1}\).  The two growing terms are identical, but the
operators are not thereby a short-range perturbation pair.

It is unsafe to begin with the formal identity

\[
 H_1=H_0+(V_1-V_0)
\]

and invoke the bounded-perturbation resolvent identity: the multiplication
operator \(V_1-V_0\) is unbounded in both relative directions and the form
domains need not coincide.

## 2. Exact Schatten thresholds

The common counting law implies, after inversion,

\[
 \lambda_{j,k}\asymp \frac{k}{\log k}.
\]

Hence, for nonreal \(z\),

\[
 s_k\!\left((H_j-z)^{-1}\right)
 \asymp\frac{\log k}{k}.
\]

It follows that

\[
 (H_j-z)^{-1}\in\mathcal S_p\quad\Longleftrightarrow\quad p>1,
\]

and in particular

\[
 (H_j-z)^{-1}\notin\mathcal S_1.
\]

By linearity of the Schatten ideal,

\[
 (H_1-z)^{-1}-(H_0-z)^{-1}\in\mathcal S_p,
 \qquad p>1.
\]

This statement does **not** imply membership in \(\mathcal S_1\).

For a positive integer \(m\),

\[
 s_k\!\left((H_j-z)^{-m}\right)
 \asymp\left(\frac{\log k}{k}\right)^m.
\]

Therefore

\[
 (H_j-z)^{-m}\in\mathcal S_1
 \quad\Longleftrightarrow\quad m>1,
\]

and, without requiring any cancellation,

\[
 (H_1-z)^{-m}-(H_0-z)^{-m}\in\mathcal S_1,
 \qquad m=2,3,\ldots.
\]

The useful spectral-shift choice is

\[
 \boxed{m=3}.
\]

Yafaev's theorem applies when the difference of an odd power of the
resolvents is trace class.  Thus the pair admits a generalized
resolvent-power spectral-shift framework even if its first resolvent
difference is not trace class.

## 3. First-resolvent obstruction

### 3.1 The perturbation is not short range

For one centered Hénon iterate,

\[
 \Psi(x,y)=(-2ar_ax-ax^2-y,x).
\]

Along \(q_R=(R,0)\),

\[
 |q_R|^2=R^2,\qquad |\Psi(q_R)|^2\sim a^2R^4,
\]

so \(V_1(q_R)/V_0(q_R)\) grows super-exponentially in \(R^2\).  In the
opposite direction, take

\[
 \widehat q_R=(R,-2ar_aR-aR^2),
\]

for which \(\Psi(\widehat q_R)=(0,R)\).  Then
\(V_0(\widehat q_R)/V_1(\widehat q_R)\) grows super-exponentially.  Localized
bumps on these two sequences also show why no one-sided relative form bound
should be assumed.

Consequently:

- \(V_1-V_0\) does not decay and is not bounded;
- neither potential gives a natural global domination of the other;
- the usual short-range Schr\"odinger perturbation hypotheses fail;
- the pair has pure point spectrum, so a scattering-phase interpretation of
  the spectral shift is not available.

This is precisely outside the regime treated, for example, by Frank and
Pushnitski's Schatten results for decaying short-range potentials.

### 3.2 Divergent principal-symbol trace-norm diagnostic

Set \(B=0\) temporarily and fix \(c>0\).  The leading resolvent symbols are

\[
 r_j(q,p)=\frac{1}{|p|^2/2+V_j(q)+c}.
\]

The two-dimensional momentum integral is exact:

\[
 \int_{\mathbb R^2}|r_1(q,p)-r_0(q,p)|\,dp
 =2\pi\left|\log\frac{V_1(q)+c}{V_0(q)+c}\right|.
\]

At large \(q\), the logarithm is governed by

\[
 \pi\bigl||\Psi(q)|^2-|q|^2\bigr|,
\]

whose spatial integral diverges for a non-isometric Hénon polynomial
automorphism.  Hence the absolute phase-space integral of the first
resolvent-symbol difference diverges.  A fixed magnetic field does not alter
the diagnostic, because \(p\mapsto p-A_B(q)\) is a momentum-fiber
translation.

This is not yet a proof that

\[
 (H_1-z)^{-1}-(H_0-z)^{-1}\notin\mathcal S_1.
\]

Such a proof requires a global pseudodifferential or coherent-state lower
bound.  It is, however, a strong obstruction and makes trace-class first
resolvent comparability the claim to prove, not an admissible assumption.

For comparison, when \(m>1\),

\[
 \int_{\mathbb R^2}|r_1(q,p)^m-r_0(q,p)^m|\,dp
 =\frac{2\pi}{m-1}
 \left|(V_1+c)^{1-m}-(V_0+c)^{1-m}\right|,
\]

which is spatially integrable.  This matches the exact \(m\ge2\) trace-class
threshold.

### 3.3 Why equal sublevel volume does not repair the problem

Area preservation gives

\[
 |\{V_0<E\}|=|\{V_1<E\}|.
\]

This cancels an integrated, signed phase-volume contribution.  A trace norm
instead measures the absolute microlocal mismatch.  Therefore

\[
 \text{equal Weyl volume}
 \not\Rightarrow \text{short-range closeness}
 \not\Rightarrow R_1(z)-R_0(z)\in\mathcal S_1.
\]

## 4. The admissible function calculus

### 4.1 Unconditional trace-class functions

Whenever both \(f(H_j)\) are trace class, their difference is trace class.
The spectral density is of order \(\log E\), so a convenient sufficient
condition is

\[
 |f(E)|\le C(1+E)^{-1-\varepsilon}.
\]

In particular, the following are safe:

- bounded compactly supported \(f\), for which both operators are finite
  rank;
- Schwartz functions;
- \(f(E)=e^{-tE}\), \(t>0\);
- \(f(E)=(E+c)^{-s}\), \(s>1\).

Yafaev's \(m=3\) theorem additionally supplies the generalized spectral-shift
trace formula for its resolvent-power function class, including smooth
compactly supported tests after a harmless extension below the spectral
bottom.

### 4.2 Canonical discrete spectral shift

Because both spectra are discrete and bounded below, normalize

\[
 \boxed{\xi(E)=N_0(E)-N_1(E)}
\]

and set \(\xi=0\) below both spectral bottoms.  For
\(f\in C_c^\infty(\mathbb R)\), integration by parts gives the exact identity

\[
 \operatorname{Tr}(f(H_1)-f(H_0))
 =\int_{\mathbb R} f'(E)\xi(E)\,dE.
\]

The current Weyl theorem yields only

\[
 \xi(E)=O\!\left(E^{3/4}(\log E)^K\right).
\]

Thus \(\xi\) is a rigorous signed staircase, but its available analytic
bound is much too large to identify a Riemann explicit-formula fluctuation.

The same bound permits scalar regularized integrals

\[
 \int f'(E)\xi(E)\,dE
\]

for some functions decaying more slowly than those for which the two
operators are individually trace class.  For example, power decay
\(f(E)\sim E^{-s}\) is integrable against the current bound for \(s>3/4\).
For \(3/4<s\le1\), this is only a regularized scalar trace; it does not prove
that \(f(H_1)-f(H_0)\) belongs to \(\mathcal S_1\).

## 5. Relative heat and wave traces

### 5.1 Relative heat trace

For every \(t>0\),

\[
 \Theta_{\rm rel}(t)
 =\operatorname{Tr}(e^{-tH_1}-e^{-tH_0})
\]

is an ordinary trace and

\[
 \Theta_{\rm rel}(t)
 =-t\int_0^\infty e^{-tE}\xi(E)\,dE.
\]

The current remainder implies the safe small-time bound

\[
 \Theta_{\rm rel}(t)
 =O\!\left(t^{-3/4}(\log(1/t))^K\right),
 \qquad t\downarrow0.
\]

This does not imply a finite limit at \(t=0\).  The corresponding classical
partition functions are exactly equal: the Hénon warp preserves the
configuration measure and the magnetic vector potential translates each
momentum fiber.  The relative heat trace therefore begins beyond the common
classical phase-volume term.

### 5.2 Relative wave trace

The propagators \(e^{-itH_j}\) are infinite-rank unitaries, not trace-class
operators.  Their spectral traces are nevertheless tempered distributions:

\[
 \langle W_j,\varphi\rangle
 =\sum_k\widehat\varphi(\lambda_{j,k}),
 \qquad \varphi\in\mathcal S(\mathbb R).
\]

The spectral growth makes the sum absolutely convergent for every Schwartz
test function.  Consequently

\[
 W_{\rm rel}=W_1-W_0\in\mathcal S'(\mathbb R)
\]

is rigorously defined.  Equivalently, use the trace-class damped family

\[
 W_{\rm rel}^{(\varepsilon)}(t)
 =\operatorname{Tr}\!\left(
 e^{-(\varepsilon+it)H_1}-e^{-(\varepsilon+it)H_0}
 \right),\qquad \varepsilon>0,
\]

and take its distributional boundary value as \(\varepsilon\downarrow0\).

### 5.3 Candidate singularities

- The singularity at \(t=0\) contains Weyl and local geometric information.
  Equal classical volume cancels the designed main clock but need not cancel
  all quantum singular terms.
- At \(t\ne0\), an energy-localized trace can receive contributions from
  closed classical trajectories when the fixed-point set of the Hamilton
  flow is clean, or when the relevant periodic orbits are isolated and
  nondegenerate.
- The radial reference has continuous periodic-orbit families.  Subtracting
  its spectrum does not automatically isolate Hénon Gutzwiller orbits.
- The classical Duistermaat--Guillemin theorem is a guiding framework, not a
  ready-made theorem for this noncompact exponential potential.  A uniform
  high-energy or semiclassical parametrix remains to be proved.

## 6. Prime-time obstruction

The zeta explicit formula has phases of the form

\[
 E\,r\log p,
\]

and hence fixed Fourier times \(t=r\log p\).  The exponential well instead
has the natural high-energy scales

\[
 R_E\asymp\sqrt{\log E},\qquad
 \tau_E\asymp\sqrt{\frac{\log E}{E}}.
\]

For a fixed Hénon iterate, polynomial distortion changes the length by at
most a polylogarithmic factor.  Fixed-complexity physical periods therefore
tend toward zero on the natural scale.  In a periodic-orbit phase,

\[
 \frac{dS_\gamma(E)}{dE}=T_\gamma(E),
\]

so an orbit family with \(T_\gamma(E)\to0\) cannot supply the required linear
phase \(E\log p\).

This is not an impossibility theorem: orbit complexity could grow with
energy.  It identifies the missing bridge precisely.  One would need a
structural family \(\gamma_{p,r}(E)\) for which

\[
 T_{\gamma_{p,r}}(E)\longrightarrow r\log p
\]

and whose trace amplitude becomes

\[
 A_{\gamma_{p,r}}(E)
 \longrightarrow C\,(\log p)p^{-r/2}
\]

with the correct repetition, sign, and phase laws.  No such construction is
currently known.

An energy-dependent time normalization is not by itself a remedy: it is not
the wave trace of one fixed self-adjoint generator.  Replacing \(H\) by
\(F(H)\) changes both the classical periods and, unless \(F\) is
asymptotically trivial, the proved Riemann--von Mangoldt mean clock.

## 7. Hard pass and kill criteria

### 7.1 First-resolvent Krein branch

**Pass:** prove

\[
 (H_1-z)^{-1}-(H_0-z)^{-1}\in\mathcal S_1
\]

with a full-space, cutoff-independent trace-norm estimate.

**Kill:** prove non-membership in \(\mathcal S_1\).  This kills only the
standard first-resolvent Krein formulation; it does not kill the \(m=3\)
resolvent-power spectral shift.

### 7.2 Relative trace as a fluctuation mechanism

**Pass:** establish an energy-localized relative trace formula, control the
radial orbit families, and show that nonzero-time singularities agree with
independently computed Hénon periods, actions, Maslov phases, and stability
matrices.

**Kill:** stable traces contain only the \(t=0\) singularity; nonzero peaks
move arbitrarily with grid, box, spectral window, or energy; or all features
are explained by radial degeneracy or artificial boundaries.

### 7.3 Arithmetic P gate

**Pass:** derive \(r\log p\) times and
\((\log p)p^{-r/2}\) amplitudes from invariant dynamics without loading
primes or zeta zeros.

**Kill:** primes must be entered term by term; \(a,B,n\) are selected from
zero fits; matches are only post hoc; small zero-input perturbations destroy
the association; or an energy-dependent clock is used without one fixed
self-adjoint generator.

## 8. Claim boundary for Paper 7

The following statement is supported:

> The pair admits a canonical discrete relative counting shift, a
> trace-class relative heat semigroup, and a tempered relative wave trace.  A
> generalized spectral-shift framework is available because the difference
> of third resolvent powers is trace class.

The following statement is not supported:

> The pair is first-resolvent comparable, or its relative trace already
> contains the Riemann prime-power explicit formula.

In gate language,

\[
 \boxed{\text{C admissible; periodic-orbit interface conditional;
 P open; Z untested.}}
\]

## Primary sources

1. D. R. Yafaev, “A Trace Formula for the Dirac Operator,” *Bulletin of the
   London Mathematical Society* **37** (2005), 908--918.
   [doi:10.1112/S0024609305004911](https://doi.org/10.1112/S0024609305004911).
   The relevant theorem treats pairs for which the difference of an odd power
   of the resolvents is trace class, i.e.
   \((H_1-z)^{-m}-(H_0-z)^{-m}\in\mathcal S_1\) for odd \(m\).
2. R. L. Frank and A. Pushnitski, “Schatten Class Conditions for Functions of
   Schrödinger Operators,” *Annales Henri Poincaré* **20** (2019),
   3543--3562.
   [doi:10.1007/s00023-019-00838-8](https://doi.org/10.1007/s00023-019-00838-8).
   Its short-range assumptions document the standard regime that the present
   warp does not satisfy.
3. J. J. Duistermaat and V. W. Guillemin, “The Spectrum of Positive Elliptic
   Operators and Periodic Bicharacteristics,” *Inventiones Mathematicae*
   **29** (1975), 39--79.
   [doi:10.1007/BF01405172](https://doi.org/10.1007/BF01405172).
4. M. Combescure, J. Ralston, and D. Robert, “A Proof of the Gutzwiller
   Semiclassical Trace Formula Using Coherent States Decomposition,”
   *Communications in Mathematical Physics* **202** (1999), 463--480.
   [doi:10.1007/s002200050591](https://doi.org/10.1007/s002200050591).
