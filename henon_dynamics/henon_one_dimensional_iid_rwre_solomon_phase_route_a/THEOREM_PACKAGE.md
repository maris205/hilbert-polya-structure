# HCS-C348 theorem package

## Frozen model and probability spaces

Let \((\Omega,\mathcal F,\mathbf P)\) carry iid variables
\(\omega=(\omega_x)_{x\in\mathbb Z}\), with

\[
0<\omega_x<1,\qquad
\rho_x=\frac{1-\omega_x}{\omega_x},\qquad
\mathbf E|\log\rho_0|<\infty.
\]

For a fixed complete environment \(\omega\), the **quenched law**
\(P_\omega^z\) is the law of the nearest-neighbour Markov chain started at
\(z\) with

\[
P_\omega(X_{n+1}=x+1\mid X_n=x)=\omega_x,
\qquad
P_\omega(X_{n+1}=x-1\mid X_n=x)=1-\omega_x.
\]

The **annealed law** is
\(\mathbb P^z(d\omega,dX)=\mathbf P(d\omega)P_\omega^z(dX)\).
The environment is sampled once and then frozen; it is not resampled at each
visit.  Source time is the number of nearest-neighbour steps.

## Main theorem

Put \(T_y=\inf\{n\geq0:X_n=y\}\) and
\(m=\mathbf E\log\rho_0\).

### Theorem (scale function, direction, speed, and solvable faces)

Under the frozen assumptions above:

1. For integers \(a<x<b\), set \(R_a=1\) and
   \(R_k=\prod_{j=a+1}^{k}\rho_j\) for \(a<k<b\).  Then
   \[
   P_\omega^x(T_b<T_a)
   =\frac{\sum_{k=a}^{x-1}R_k}{\sum_{k=a}^{b-1}R_k}.
   \]

2. For \(\mathbf P\)-almost every environment, the following trichotomy holds
   \(P_\omega^0\)-almost surely:
   \[
   \begin{array}{c|c}
   m<0&X_n\longrightarrow+\infty,\\
   m=0&\liminf X_n=-\infty,\quad\limsup X_n=+\infty,\\
   m>0&X_n\longrightarrow-\infty.
   \end{array}
   \]

3. Under \(\mathbb P^0\), and hence under \(P_\omega^0\) for
   \(\mathbf P\)-almost every \(\omega\), \(X_n/n\) converges almost surely
   to the deterministic velocity
   \[
   v=\begin{cases}
   \dfrac{1-\mathbf E\rho_0}{1+\mathbf E\rho_0},
       &\mathbf E\rho_0<1,\\[6pt]
   -\dfrac{1-\mathbf E\rho_0^{-1}}{1+\mathbf E\rho_0^{-1}},
       &\mathbf E\rho_0^{-1}<1,\\[6pt]
   0,&\text{otherwise}.
   \end{cases}
   \]
   The first two cases cannot occur simultaneously.  In particular, a walk
   may be transient while its velocity is zero.

4. If \(\omega_0\sim\operatorname{Beta}(\alpha,\beta)\) with
   \(\alpha,\beta>0\), then the walk is right transient, recurrent, or left
   transient according as \(\alpha>\beta\), \(\alpha=\beta\), or
   \(\alpha<\beta\).  Its velocity is
   \[
   v=\begin{cases}
   \dfrac{\alpha-\beta-1}{\alpha+\beta-1},&\alpha>\beta+1,\\[5pt]
   -\dfrac{\beta-\alpha-1}{\alpha+\beta-1},&\beta>\alpha+1,\\[5pt]
   0,&|\alpha-\beta|\leq1.
   \end{cases}
   \]

5. In the constant environment \(\omega_x=p\in(0,1)\), the formula reduces
   to \(v=2p-1\), including \(p=1/2\).

## Analytic proof

### 1. Finite-interval scale function

Let \(h(i)=P_\omega^i(T_b<T_a)\).  The Markov property gives

\[
h(i)=\omega_i h(i+1)+(1-\omega_i)h(i-1),
\qquad h(a)=0,\quad h(b)=1.
\]

Writing \(\Delta_i=h(i)-h(i-1)\) yields
\(\Delta_{i+1}=\rho_i\Delta_i\).  Thus
\(\Delta_{k+1}=R_k\Delta_{a+1}\).  Summing the differences and imposing
\(h(b)=1\) gives exactly the claimed quotient.  Every denominator is positive,
so the solution is unique.

### 2. Direction from the two-sided potential

Define

\[
V(0)=0,
\quad V(n)=\sum_{j=1}^{n}\log\rho_j\ (n>0),
\quad V(n)=-\sum_{j=n+1}^{0}\log\rho_j\ (n<0).
\]

The strong law gives \(V(n)/n\to m\) at both ends.  Insert the corresponding
scale sums in the finite-interval formula and let the barriers tend to
infinity.  If \(m<0\), the scale weights decay to the right and grow to the
left; the walk hits every positive level and visits each fixed level only
finitely often, hence \(X_n\to+\infty\).  The case \(m>0\) follows by
reflection.

If \(m=0\), the iid partial sums of \(\log\rho\) oscillate at both ends unless
they vanish identically; in the latter case \(\omega_x=1/2\) almost surely.
In either case both one-sided scale sums diverge.  Sending the two barriers to
infinity shows that every integer is hit almost surely, which gives the stated
oscillation.

### 3. Crossing times and their ergodic law

Assume first that every positive level is hit, which holds in the right
transient and recurrent chambers.  Put

\[
T_i=\inf\{n:X_n=i\},\qquad \tau_i=T_i-T_{i-1}\quad(i\geq1).
\]

By the quenched strong Markov property, conditional on a fixed environment the
successive post-hitting path segments, and hence the \(\tau_i\), are independent
with one-crossing laws shifted in space.  Equivalently, on a product extension
one may take iid auxiliary rows \(U_i\), independent of \(\omega\), and a
measurable simulator \(F\) such that
\[
\tau_i=F(\theta^{i-1}\omega,U_i).
\]
The simultaneous shift of the iid environment coordinates and the iid rows is
a Bernoulli shift, hence mixing and ergodic; the crossing array is its factor.
This proves stationarity and ergodicity without asserting that the annealed
crossing times are independent.  For a local check, \(\tau_i\wedge K\) depends
only on the one-segment row \(U_i\) and the environment sites reachable from
\(i-1\) before time \(K\), so separated finite blocks of truncated crossings
are independent.

For a fixed environment let
\(a_i=E_\omega^iT_{i+1}\).  First-step decomposition gives

\[
a_i=1+(1-\omega_i)(a_{i-1}+a_i),
\qquad
a_i=1+\rho_i+\rho_i a_{i-1}.
\]

Iterating toward \(-\infty\), with monotone truncation if the answer is
infinite, yields

\[
E_\omega^0T_1
=1+2\sum_{k\leq0}\prod_{j=k}^{0}\rho_j.
\]

Tonelli's theorem and independence therefore give

\[
\mathbb E\tau_1
=1+2\sum_{r\geq1}(\mathbf E\rho_0)^r
=\frac{1+\mathbf E\rho_0}{1-\mathbf E\rho_0}
\]
when \(\mathbf E\rho_0<1\), and \(\mathbb E\tau_1=\infty\) when
\(\mathbf E\rho_0\geq1\).

### 4. Finite- and infinite-mean time change

If \(\mu=\mathbb E\tau_1<\infty\), Birkhoff's theorem gives
\(T_n/n\to\mu\).  Moreover \(\tau_n/n\to0\) almost surely: indeed

\[
\sum_{n\geq1}\mathbb P(\tau_n>\varepsilon n)
=\sum_{n\geq1}\mathbb P(\tau_1>\varepsilon n)<\infty
\]

by integrability, and the first Borel--Cantelli lemma needs no independence.
Let \(M_t=\max_{s\leq t}X_s\).  Nearest-neighbour motion implies
\(M_t=\max\{n:T_n\leq t\}\).  Inverting \(T_n/n\to\mu\) gives
\(M_t/t\to1/\mu\).  During the unfinished crossing from \(M_t\) to
\(M_t+1\), the depth below \(M_t\) is at most \(\tau_{M_t+1}\); hence it is
\(o(t)\).  Therefore \(X_t/t\to1/\mu\).

If \(\mathbb E\tau_1=\infty\), apply Birkhoff to every bounded variable
\(\tau_i\wedge K\):

\[
\liminf_{n\to\infty}\frac{T_n}{n}
\geq\mathbb E(\tau_1\wedge K).
\]

Letting \(K\to\infty\) proves \(T_n/n\to\infty\), not merely divergence in
expectation.  Thus \(M_t/t\to0\).  In the right transient chamber
\(X_t\to+\infty\), so eventually \(0\leq X_t\leq M_t\), and hence
\(X_t/t\to0\).  This is the required analytic closure of the transient
zero-speed case.

In the recurrent chamber the same infinite-mean argument controls the positive
running maximum.  Applying it to the reflected walk controls the negative
running minimum, so \(|X_t|/t\to0\).  Finally, when the original walk is left
transient, reflect space: the reflected bias is
\(\rho'_x=\rho_{-x}^{-1}\).  This gives the second velocity formula.
The inequality
\((\mathbf E\rho_0)(\mathbf E\rho_0^{-1})\geq1\) shows that the two ballistic
conditions are disjoint.

The preceding limits were proved under the annealed law.  If \(A\) denotes any
one of these probability-one path events, then
\[
1=\mathbb P^0(A)=\int P_\omega^0(A)\,\mathbf P(d\omega).
\]
Therefore \(P_\omega^0(A)=1\) for \(\mathbf P\)-almost every environment.  This
is the asserted quenched-a.e. conclusion; no every-environment statement is
being made.

### 5. Beta and constant faces

For \(\omega\sim\operatorname{Beta}(\alpha,\beta)\), direct Beta integrals give

\[
\mathbf E\log\rho=\psi(\beta)-\psi(\alpha),
\quad
\mathbf E\rho=\frac{\beta}{\alpha-1}\ (\alpha>1),
\quad
\mathbf E\rho^{-1}=\frac{\alpha}{\beta-1}\ (\beta>1),
\]

with the corresponding moment infinite when its denominator condition fails.
The digamma function is strictly increasing.  Substitution into the direction
and speed formulas proves every Beta chamber, including
\(\alpha=\beta\) and \(|\alpha-\beta|=1\).  If \(\omega_x=p\), then
\(\rho=(1-p)/p\) and
\((1-\rho)/(1+\rho)=2p-1\); reflection covers \(p<1/2\).

## Evidence and theorem boundary

The canonical finite receipt contains 400 integer-Beta cells, 280 rational
two-atom laws, all 780 environment words of interior length at most four over
the five-point rational alphabet, and all 2,930 associated starting-point
hitting probabilities.  These rows test scale conventions, moment thresholds,
and formula transcription.  They do not prove the infinite-line almost-sure
theorem; the analytic proof above owns that theorem.

The package does not cover non-iid, dynamic, higher-dimensional,
non-nearest-neighbour, or environments with atoms at zero or one.  It proves no
central limit theorem, slowdown exponent, localization result, or large
deviation principle.

## Collision and Route-A boundary

C342 concerns finite directed labelled graphs, independent Dirichlet transition
rows, and the annealed representation of edge reinforcement.  C348 instead
freezes one iid scalar environment on the whole integer line and proves a
quenched/annealed direction--speed phase diagram.  C273 has homogeneous iid
increments rather than a frozen spatial medium; C253 is a finite Moran
absorption chain.

The strict Route-A tuple is
\((A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FAIL)\), with overall verdict
`ROUTE_A_REJECTED` and Route B false.  Random sites, crossing times, and scale
products are source probability objects, not rational-prime carriers,
primitive arithmetic orbits, target Euler factors, a target divisor, or a
Hilbert--Pólya operator.
