# Unary divisor transfer breaks power sectors but creates a full-support periodic state

**Paper ID:** `237-unary-divisor-coherence`  
**Candidate ID:** `ANG-20260918-UDC01`  
**Date / status:** 2026-09-18; `GLOBAL OWNER AND SECTOR LEAKAGE; MIXED-SUPPORT RETURN — STOP / FORK`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

We replace two-input multiplicative mode interaction by unary coherent
transfer along the full proper-divisor incidence graph. The new owner is
the entire unit sphere of ordinary complex ell squared, with logarithmic
diagonal dispersion and a fixed symmetric divisor matrix. An exact
Hilbert--Schmidt estimate and an interaction-picture construction give a
two-sided global norm-preserving action on the full space. An occupied
6-mode excites the 2-mode, so the powers-of-6 invariant sector of the
earlier three-wave models is genuinely broken. However, the lowest
Rayleigh energy is attained. Its minimizing state lies in the strong
generator domain and can be chosen strictly positive at every integer
coordinate. A positive eigenvalue then gives an actual nonconstant
periodic orbit of the full action, with support at every integer and an
exact least physical period. This violates the frozen prime-support
criterion. Breaking the old invariant sector therefore does not suffice
for this candidate. No prime-length, full packet, trace or Route result is
claimed; the complete state space and clock are retained at the stop.

## 1. Exact owner and lineage

The [version-1 card](candidate-card.md) was frozen before this audit.
The mathematical object is neither a coefficient choice in
[234](../234-multiplicative-sector-obstruction/paper.md) nor another
diagonal-dispersion fork of
[235](../235-quadratic-dispersion-flow/paper.md).

| Item | UDC01 definition | Owner boundary |
| --- | --- | --- |
| Space and shell | H0=ell squared of all integer n>=2; M={norm=1} | All modes and sphere states retained |
| Arithmetic interaction | Undirected proper-divisor incidence, one edge weight 1/(mn) | Unary linear transfer, not two-input fusion/fission |
| Action and time | Mild equation (2) below, with H=L-K | Physical time is its actual parameter |
| Packets | Every nonconstant primitive point orbit, modulo time translation | No global-phase quotient or selected-sector carrier |
| Repetition | r traversals of the same primitive orbit | Physical time rT |
| Classical geometry | No finite-dimensional symplectic base or mapping torus | Classical A0/A1/A2 NOT APPLICABLE |
| Generator and later analysis | H is the classical mode-flow generator | No target spectrum, trace, zeta or determinant |

The explicit [lineage arrow](../../docs/prior_work/README.md) is
proper-divisor symbolic witness a|n, 2<=a<n, to the complete incidence
edge a<->n, then to a coherent unary transfer that uses those same edges.
It retains the factor observable but replaces its symbolic temporal rule.
There is no claim of sieve, Logistic or Henon conjugacy or geometric lift.
A prime has no smaller nonunit divisor neighbor; it is **not** an isolated
vertex, because it has multiple neighbors above it.

This differs from the real finite triangular fragmentation/cotangent
control in [192](../192-six-architecture-source-frontier/paper.md), from
the diagonal factor-homology action in
[186](../186-multiplicative-bar-clock/paper.md), and from the prior
indecomposable quotient in
[193](../193-indecomposable-radial-quotient/paper.md). No result from those
objects is transferred. The source replacement, log dispersion and edge
decay are declared designs; naturalness remains OPEN.

## 2. Frozen definitions

Let H0=ell squared({2,3,...}; complex), with inner product conjugate-linear
in its first entry, and set Q(z)=norm(z) squared. Define

\[
(Lz)_n=(\log n)z_n,\quad
D(L)=\left\{z:\sum_{n\ge2}(\log n)^2|z_n|^2<\infty\right\},
\quad (S_tz)_n=e^{-it\log n}z_n.
\]

The fixed symmetric matrix is

\[
K_{mn}=\begin{cases}
1/(mn),&m\ne n,\ m\mid n\text{ or }n\mid m,\\
0,&\text{otherwise},
\end{cases}\quad m,n\ge2,\qquad H=L-K.\tag{1}
\]

Each edge weight occurs once in each matrix orientation. It is not a sum
over all factorizations of one endpoint. We do not add n=1 or identify
coordinates by factorization class. The prescribed equation is

\[
z(t)=S_tz_0+i\int_0^tS_{t-s}Kz(s)\,ds.\tag{2}
\]

Its strong version, where justified, is i dz/dt=Hz. The candidate carrier
is the entire Q=1 sphere M, not the strong generator domain.

For the return test define the quadratic form

\[
q(z)=q_L(z)-\langle z,Kz\rangle,
\qquad q_L(z)=\sum_{n\ge2}(\log n)|z_n|^2,\tag{3}
\]

on Y={z:q_L(z)<infinity}, with form norm norm(z)_Y squared=q_L(z).
This finite-energy domain is used only for a
variational proof inside the full carrier. The form need not be finite
at every mild state. All inputs are integer divisibility, the uniform
weights in (1), log n and norm level 1. No prime table, prime-specific
parameter, von Mangoldt weight or Riemann-zero input is used.

## 3. Global ownership and genuine sector leakage

### Lemma 1 — Bounded symmetric divisor interaction

K is a bounded self-adjoint operator on H0, with

\[
\|K\|^2\le\|K\|_{\mathrm{HS}}^2
=2\left(\sum_{a\ge2}a^{-4}\right)
   \left(\sum_{b\ge2}b^{-2}\right)
\le\frac5{32}<\frac14.\tag{4}
\]

In particular norm(K)<1/2<log 2. H is self-adjoint on the stated D(L).

**Proof.** A proper-divisor edge has a unique smaller endpoint a and
larger endpoint ab with b>=2. Summing the squares of both oriented matrix
entries yields the exact middle expression in (4). Integral bounds give

\[
\sum_{a\ge2}a^{-4}\le\frac1{16}+\int_2^\infty x^{-4}\,dx
=\frac5{48},\qquad
\sum_{b\ge2}b^{-2}\le\frac14+\int_2^\infty x^{-2}\,dx
=\frac34.
\]

Thus the square-summable matrix defines a bounded operator by
Cauchy--Schwarz; finite matrix approximants and symmetry give K*=K.
Also log 2=integral from 1 to 2 of 1/x is strictly greater than 1/2.

For clarity, self-adjointness here is an elementary generator-domain
statement, not a quantum conclusion. Coordinate tests in the adjoint
definition give D(L*)=D(L) and L*=L. Since K is bounded, the functional
associated with H on D(L) is bounded exactly when the one associated
with L is bounded, after adding the bounded K term. Hence
D(H*)=D(L*)=D(L) and H*=L-K=H. ∎

### Theorem 2 — Full global classical mode action

Equation (2) has a unique mild solution for every z_0 in H0 and every real
time. Its solution maps Phi_t are a jointly continuous, complex-linear,
unitary action, and preserve the whole sphere M.

**Proof.** S is a strongly continuous isometric group, by approximation
with finite sequences. In the interaction variable u(t)=S_(-t)z(t),
(2) becomes

\[
\dot u(t)=iB_tu(t),\qquad B_t=S_{-t}KS_t.\tag{5}
\]

The bounded operators B_t are self-adjoint, uniformly bounded by norm(K),
and strongly continuous in t. Picard iteration on the integral equation
gives a unique H0-valued continuously differentiable solution, with a
uniform local interval on each bounded ball. Along this equation,

\[
\frac{d}{dt}\|u(t)\|^2
=2\operatorname{Re}\langle u,iB_tu\rangle=0.
\]

Thus the norm is fixed. The bounded derivative makes u Cauchy at any
finite endpoint, and its limit restarts the local construction. This
proves continuation both forward and backward. Transforming back gives
the unique full-space mild solution of (2) and norm conservation.

Time-translated mild solutions solve the same autonomous equation (2),
by splitting its integral and using the S group law. Uniqueness gives
Phi_(t+s)=Phi_t composed with Phi_s, with inverse Phi_(-t). Linearity
and norm preservation, by polarization, give unitarity. The uniform
linear estimates and strong continuity of S give joint continuity.
No strong time derivative of z at arbitrary data outside D(L) is used. ∎

Consequently the complete transformation groupoid has objects z in M
and arrows (z,t) from z to Phi_tz. The Hilbert-space generator belongs
to this classical action; its existence is not a Route-B coordinate or
a Hilbert--Polya spectral realization.

### Proposition 3 — The old power-sector invariant is broken

Let E_6 be the subspace of states supported on powers of 6. The trajectory
through e_6 leaves E_6 immediately. In fact

\[
\left.\frac{d}{dt}z_2(t)\right|_{t=0}=\frac{i}{12},\qquad
\left.\frac{d}{dt}z_3(t)\right|_{t=0}=\frac{i}{18}.\tag{6}
\]

**Proof.** At this finite-support state L has zero 2- and 3-coordinates,
whereas K_(2,6)=1/12 and K_(3,6)=1/18. The derivative at zero follows
directly from (2): the S term is differentiable at e_6 and the integrand
is continuous in H0. Both resulting outside-sector derivatives are
nonzero, proving the claim. ∎

This is genuine unary arithmetic support transfer. It also affects pure
prime modes: at e_p the 2p-coordinate derivative is i/(2p squared).
Primes are therefore not isolated dynamical modes. The negative results
of 234 cannot simply be cited for this new architecture, because its
power-sector invariance hypothesis is absent.

## 4. The replacement obstruction: a full-support standing wave

### Theorem 4 — Positive lowest energy and an attained full-support state

There exist u in M intersect D(L) and a real number lambda such that

\[
Hu=\lambda u,\quad u_n>0\text{ for every }n\ge2,
\qquad 0<\log2-\|K\|\le\lambda<\log2.\tag{7}
\]

Here lambda is the minimum of q on the full norm-one finite-energy
domain. No finite-dimensional spectral approximation is needed.

**Proof.** Define

\[
\lambda=\inf\{q(v):v\in Y,\ \|v\|=1\}.
\]

By Lemma 1, q(v)>=log 2-norm(K)>0 on the sphere. Testing v=e_2
gives q(v)=log 2, so the infimum is finite and at most log 2. A
minimizing sequence has bounded q_L, because its K pairing has absolute
value at most norm(K). The finite-energy embedding Y into H0 is compact
on such bounded sets: for every N>=2,

\[
\sum_{n>N}|v_n|^2\le\frac{q_L(v)}{\log(N+1)}.\tag{8}
\]

A diagonal subsequence converges on finite coordinate sets; (8) makes
it converge strongly in H0. Its limit v has norm 1, q_L(v) is no
larger than the liminf by finite partial sums, and the bounded K pairing
converges strongly. Thus v is a minimizer of q in Y.

All matrix entries of K are nonnegative. The pairing satisfies

\[
\langle |v|,K|v|\rangle
\ge\operatorname{Re}\langle v,Kv\rangle,
\qquad q_L(|v|)=q_L(v).
\]

The double series is absolutely convergent by Cauchy--Schwarz on the
Hilbert--Schmidt matrix against the rank-one array |v_m v_n|. Therefore
u=|v| is also a minimizing norm-one state and is nonnegative coordinatewise.

The form q and norm squared are continuously differentiable real
functionals on Y. The sphere constraint has a nonzero differential.
Taking its multiplier identity in finite-coordinate real and imaginary
directions gives

\[
(\log n)u_n-(Ku)_n=\lambda u_n\quad(n\ge2).\tag{9}
\]

The multiplier equals q(u)=lambda by evaluating on the radial direction.
This is initially only a coordinate identity. But K is bounded and
u is in H0, so its right side implies Lu=lambda u+Ku is in H0.
Hence u belongs to D(L), and (9) becomes a strong eigenvalue equation.

The graph of positive K entries is connected. Every integer n>=2 is
connected to 2 through the edges n--2n--2, with repeated vertices omitted
when necessary. If some u_n were zero, (9) would give
sum_m K_(n,m)u_m=0. Its summands are nonnegative and its row sum converges
by Cauchy--Schwarz, so every neighbor of n would also have zero amplitude.
Connectivity propagates this to all coordinates, contradicting norm(u)=1.
Thus u_n>0 for every n.

Finally lambda is strictly below log 2. For 0<epsilon<1, the trial state
sqrt(1-epsilon squared)e_2+epsilon e_4 has energy

\[
\log2+(\log2)\varepsilon^2
-\frac14\varepsilon\sqrt{1-\varepsilon^2}<\log2\tag{10}
\]

for sufficiently small positive epsilon, since its right derivative at
zero is -1/4. This proves the final strict inequality in (7). ∎

### Corollary 5 — An actual primitive mixed-source periodic packet

The full action has the nonconstant orbit

\[
\Phi_tu=e^{-i\lambda t}u,\qquad
T=\frac{2\pi}{\lambda},\qquad
\{t:\Phi_tu=u\}=T\mathbb Z.\tag{11}
\]

Its support is every integer n>=2 at every time, so it cannot be assigned
to any single-prime power sector under the frozen source criterion.

**Proof.** Since u is in D(L) and Hu=lambda u, the curve in (11)
solves the full strong equation. Variation of constants with S gives
the prescribed mild equation (2); uniqueness identifies it with Phi.
Lambda>0 and u is nonzero, so the curve is nonconstant and it returns
exactly when exp(-i lambda t)=1. This proves the full return group and
least period. Every coordinate remains nonzero by Theorem 4. ∎

No phase quotient is involved. A global phase rotation of a nonzero
state is a genuine orbit in the frozen sphere; its actual return time is
derived, not assumed. Traversing it r times takes rT. We neither assert
uniqueness of the minimizer nor infer the complete periodic spectrum or
the multiplicity of other packets.

## 5. Controls and limits

| Control or distinction | Exact conclusion | Boundary |
| --- | --- | --- |
| Zero interaction K=0 | Pure n mode has period 2pi/log n, including composites | Different owner; logarithmic frequency is not log-prime period |
| Pure composite e_6 in UDC01 | Nonzero outside-power derivatives in (6) | A real escape from the old invariant sector, not prime-selective returns |
| Pure prime e_p in UDC01 | Nonzero transfer into 2p | Primes are not isolated graph vertices or protected pure modes |
| Full energy minimization | A nonnegative minimizer has full support by graph connectivity | Not an arbitrary eigenvector assigned a prime label afterward |
| Deleting composite modes | Changes the main carrier and incidence matrix | Forbidden same-ID repair |
| Quotienting global phase | Would turn the exhibited orbit into a fixed projective point | Different carrier and packet convention, not a repair |
| Cutoff and precision | No finite matrix, spectral fit or computed eigenvalue | Exact compactness proves an infinite-model eigenstate |

The new obstruction is specific: positive connected incidence together
with this confining diagonal form produces a full-support periodic
standing wave. We do not infer that all sector-breaking or noncompact
arithmetic dynamics has such a state. The proof did not need a full
spectral decomposition or a periodic-orbit census. No naturalness, trace,
determinant, target spectrum or prime-log timing theorem is supplied.

The separately frozen nonlinear
[SDT01 screen in 236](../236-cross-sector-frontier/candidate-card.md)
uses amplitude-dependent proper-divisor transfer. Its vector field,
invariant probes and physical periods belong to that different object.
No result from its audit is used above.

## 6. Gate assessment and decision

| Obligation | Evidence for UDC01 | Result / scope |
| --- | --- | --- |
| T0 | Full unitary action on all H0 and M, with exact domain and generator | ESTABLISHED for this classical mode owner |
| T1 | Explicit unary divisor source; genuine power-sector leakage | Source/clock naturalness OPEN |
| T2 | Full-support primitive packet and least physical time (11) | Prime-support target FAIL; remaining ledger NOT CLASSIFIED |
| T3 | Generator belongs to the action, but no trace/zeta/determinant construction | NOT ADVANCED to a trace or target identity |
| Classical A0/A1/A2 | No finite-dimensional symplectic suspension | NOT APPLICABLE |
| Formal Route / B | No formal evaluation or quantum-owner audit | UNASSIGNED / NOT INVOKED |

**Decision: STOP / FORK.** Breaking the old E_6 invariance is established,
but an intrinsic mixed-support orbit of the same full action still fails
the frozen packet interpretation. The norm sphere, matrix, generator and
physical time have not changed. Retain this owner construction and its
new obstruction as controls; do not pursue a trace to rescue the candidate.

## Evidence, reproducibility and disclosure

The [card](candidate-card.md), [claim ledger](claim-ledger.md) and
[evidence record](evidence/README.md) contain definitions, exact claims and
observed checks. All sums, trials and tail bounds here are symbolic exact
arguments. No numerical eigenvalue, cutoff limit inferred from data, GPU
run, PDF or publication artifact is used. The scalar lambda is defined
by an attained infinite-dimensional infimum, not a reported numerical value.

Data availability: the complete inputs and proofs are in this package.
Ethics: no human subjects or private data. Contributions: AI-assisted
formalization, drafting and bounded model checking; no human CRediT role
is inferred. Funding and conflict declarations were not supplied. This
is an internal research record, not external peer review, publication
readiness or a correctness certificate. ARS informed the separation of
proof layers, adverse controls and evidence, not Route authority.
