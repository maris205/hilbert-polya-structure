# Exact telescoping clock on the full divisor-scan phase carrier

**Paper ID:** `226-exact-telescoping-clock`  
**Candidate ID:** `ASFS-20260918-ETC01`  
**Date / status:** `2026-09-18; OWNER-LEVEL CONSTRUCTION — A1 POSITIVE; A0 NATURALNESS OPEN; SCALAR PRODUCT ONLY; ANALYTIC OWNER OPEN`  
**Route state:** same-object geometric/orbit audit recorded; no transfer operator or formal Route coordinate; Route B `NOT INVOKED`.

## Abstract

This paper freezes and audits a new candidate whose phase set contains every
integer $d=1,\ldots,n-1$ in the $n$-fibre.  The phase $d=1$ is a neutral
initialization interval and the other phases execute the local divisor witness
$h(n,d)=\mathbf 1_{d\mid n}$.  The same witness is inserted into a
positive-dimensional Hénon-form recurrence

\[
(q,p)\longmapsto\bigl(p,2p-q+(p-1)^2+h(n,d)\bigr).
\]

The map is a global symplectomorphism on the full countable disjoint union of
planes.  Summing the exact second-order recurrence around an arbitrary period
forces every real periodic state to have $q=p=1$ and every visited witness
to vanish.  Thus the complete intrinsic ledger has one phase-cycle for each
prime, including the $n=2$ singleton, and no composite periodic state.  The
same object's roof

\[
\tau(n,d)=\log((d+1)/d)
\]

is positive and non-Zeno; for a prime $p$, its full phase sum is exactly
$\log p$.  Cyclic phase points therefore give one oriented primitive flow
orbit of length $\log p$, with repetitions $r\log p$.

The result is an exact owner-level construction and a scalar Euler-product
control, not a naturalness proof.  The adjacent-ratio timing is already
present in the earlier source-geometric-return-clock control [160](../160-source-geometric-return-clock/README.md), so 226 does not claim a new clock mechanism.  The quadratic force, full phase convention and neutral initial interval remain explicit design choices.  No transfer operator, Fredholm determinant, trace formula, Route-A tuple, Route-B coordinate, or spectral claim is supplied.  At the surviving central states the monodromy is unipotent, so the usual nondegenerate periodic-orbit denominator $\det(I-P^r)$ vanishes; this is an early analytic-owner warning, not a deeper operator result.

## 1. Candidate identity and same-object ledger

The [candidate card](candidate-card.md) was frozen before this audit.  This is
not a repair of candidate 222: changing the phase set changes the carrier and
therefore requires the fresh ID `ASFS-20260918-ETC01`.

For each $n\ge2$, let

\[
D_n=\{1,2,\ldots,n-1\},
\qquad d^+=
\begin{cases}d+1,&d<n-1,\\1,&d=n-1.
\end{cases}
\]

For the one-phase fibre $D_2=\{1\}$, this gives $1^+=1$.  Define

\[
h(n,1)=0,
\qquad h(n,d)=\mathbf 1_{\{d\mid n\}}\quad(2\le d<n),
\tag{1}
\]

and freeze

\[
M=\coprod_{n\ge2,\ d\in D_n}\mathbb R^2_{n,d},
\qquad \omega|_{\mathbb R^2_{n,d}}=dq\wedge dp,
\tag{2}
\]
\[
F(n,d,q,p)=
\bigl(n,d^+,p,\,2p-q+(p-1)^2+h(n,d)\bigr).
\tag{3}
\]

The positive roof and its endpoint-glued suspension are

\[
\tau(n,d,q,p)=\log\frac{d+1}{d},
\tag{4}
\]
\[
M_\tau=\{(z,t):z\in M, 0\le t\le\tau(z)\}/
((z,\tau(z))\sim(Fz,0)).
\tag{5}
\]

The flow is translation in the $t$-coordinate after the endpoint quotient.
The base is symplectic; the three-dimensional suspension charts are not being
called symplectic or Hamiltonian merely from that fact.

| Ledger item | Owner in this candidate | State |
| --- | --- | --- |
| Phase space and form | (2), with every $n\ge2$, every $1\le d<n$, all $q,p\in\mathbb R$ | frozen |
| Base map | Polynomial map (3), coefficient 2 fixed before audit | exact symplectic proof below |
| Arithmetic source | Local divisor witness (1), executed in the same map | operationally endogenous; naturalness open |
| Symbolic lineage | prime/composite divisor exclusion -> sequential phase scan -> Hénon-form lift | direct constrained deformation, not a conjugacy claim |
| Clock | Adjacent-integer ratio (4), on all integer/phase components | exact telescoping; duplicate engineered mechanism control |
| Primitive convention | All least-period full states modulo cyclic phase, with no centre or domain crop | complete ledger below |
| Repetition | $r$-fold traversal of one primitive oriented flow orbit | $rT$ |
| Analytic owner | None beyond the scalar product stated below | operator/trace open |
| Later lift | Hamiltonian/contact/quantum | deferred |

The clock construction is explicitly compared with 160.  In particular,
226's exact sum does not by itself establish that arithmetic intrinsically
privileges the adjacent-ratio roof.

## 2. Question and claim boundary

### Question

Can one full, positive-dimensional symplectic carrier execute the local
divisor-exclusion scan, retain its entire periodic ledger, and produce a
prime-log suspension time from a universal phase roof without defining a
prime-selected domain?

### Strongest supported result

Yes as an exact construction.  The map (3) is a global symplectomorphism; its
full periodic set is precisely the central state in the $n=2$ fibre and the
phase cycles over prime $n$; the roofed suspension is complete; and each
prime contributes exactly one oriented primitive orbit of length $\log p$.
The scalar primitive product therefore has one Euler factor per prime on its
ordinary absolute-convergence half-plane.

### Explicit nonclaims

- The phase convention, coefficient 2 and square force are constructive
  choices, not uniquely derived by the prior Logistic/Hénon papers.
- The adjacent-ratio clock is not a new natural mechanism: the same timing
  idea is present in the scoped control [160](../160-source-geometric-return-clock/README.md).
- No transfer operator, function space, Fredholm determinant, trace formula,
  analytic continuation, target-divisor matching, quantum owner or Riemann-zero
  statement is supplied.
- The scalar Euler product is not a formal Route-A A2 pass.
- No prime list, manually inserted $T_p=\log p$, von Mangoldt weight, or zero
  data enters (1)--(5).

## 3. Exact geometry and non-Zeno completeness

### Proposition 1 — Global symplectic diffeomorphism

The map $F$ in (3) is a smooth global symplectomorphism of the full carrier
$M$.

**Proof.** A countable disjoint union of Euclidean planes is a Hausdorff,
second-countable smooth two-manifold with the componentwise form (2).  Given an
output $(n,d',Q,P)$, let $d$ be the predecessor of $d'$ in the cyclic
set $D_n$.  The unique inverse is

\[
F^{-1}(n,d',Q,P)=
\bigl(n,d,\,2Q+(Q-1)^2+h(n,d)-P,\,Q\bigr).
\tag{6}
\]

Indeed, the forward coordinates satisfy $Q=p$ and
$P=2p-q+(p-1)^2+h(n,d)$, so (6) recovers $q$ and $p$.  The maps are
polynomial on each open component, and the discrete phase permutation is
bijective.  On a component,

\[
dQ\wedge dP
=dp\wedge\bigl(-dq+(2+2(p-1))dp\bigr)
=dq\wedge dp.
\]

Thus $F^*\omega=\omega$, and (6) proves global invertibility.  No centre,
momentum slice or prime fibre was selected.  QED.

### Proposition 2 — Complete variable-roof suspension

The quotient (5) carries a translation flow defined for every real time on
every full state; in particular, it has no finite-time accumulation of section
crossings along any trajectory.

**Proof.** The integer $n$ is conserved.  In the fibre $n=2$, the sole roof
is $\log2>0$.  For $n\ge3$, the finite phase set gives

\[
\tau(n,d)\ge \min_{1\le d<n}\log\frac{d+1}{d}
=\log\frac n{n-1}>0.
\tag{7}
\]

Therefore $N$ successive crossings on one trajectory accumulate at least
$N\log(n/(n-1))$ time, in both directions.  A finite time interval contains
only finitely many crossings.  At each crossing, (6) supplies the backward
state and (3) supplies the forward state, so the standard endpoint quotient
gives a complete flow.  The global infimum of the roofs over all components is
zero, but one trajectory never changes its conserved $n$; that infimum cannot
produce a Zeno path.  QED.

## 4. Full intrinsic periodic ledger

### Proposition 3 — Periodic states are exactly prime central states

The complete periodic set is

\[
\operatorname{Per}(F)=\{(2,1,1,1)\}
\cup\{(p,d,1,1):p\ge3\text{ prime},\ 1\le d<p\}.
\tag{8}
\]

The first point has least period one.  For every prime $p\ge3$, the $p-1$
listed points form one base orbit of least period $p-1$.  No composite fibre
has any periodic state.

**Proof.** Along an orbit write $(q_t,p_t)$ for the coordinates after $t$
steps.  Since $q_{t+1}=p_t$, the second coordinate of (3) yields

\[
q_{t+2}-2q_{t+1}+q_t
=(q_{t+1}-1)^2+h(n,d_t).
\tag{9}
\]

For a period-$m$ state, summing (9) over one full period cancels the left
side and gives

\[
0=\sum_{t=0}^{m-1}(q_{t+1}-1)^2
 +\sum_{t=0}^{m-1}h(n,d_t).
\tag{10}
\]

Every term is nonnegative.  Hence $q_t=1$ for all $t$, and every visited
phase has $h(n,d_t)=0$.  Phase return forces $m$ to be a multiple of
$L_n=n-1$, so for $n\ge3$ every phase $d=1,\ldots,n-1$ is visited.  All
witnesses vanish on this full scan exactly when $n$ has no divisor in
$\{2,\ldots,n-1\}$, which is exactly the definition of a prime.  For $n=2$,
the singleton phase has the prescribed neutral witness $h(2,1)=0$.  Finally,
$p_t=q_{t+1}=1$, so the listed points are the only possible momentum values;
they do close under the phase successor.  The phase cycle rules out a shorter
period for $p\ge3$, and (10) rules out all other real states.  QED.

This is a full-state result: it includes all real transverse coordinates and
momenta before classification, rather than selecting the geometric centre.

### Proposition 4 — Primitive flow packets, multiplicity and repetitions

The suspension has exactly one oriented primitive closed orbit $\gamma_p$ for
each prime $p$.  Its period is

\[
T_p=\sum_{d=1}^{p-1}\log\frac{d+1}{d}=\log p,
\tag{11}
\]

and its $r$-fold repetition has period $r\log p$.

**Proof.** A closed suspension trajectory intersects the section in a periodic
state of $F$, and a least-period base orbit gives one oriented flow orbit
after quotienting its cyclic section points.  Proposition 3 is the complete
ledger, so no packets are inserted or discarded.  For each prime, (11) is the
telescoping identity

\[
\log2+\log\frac32+\cdots+\log\frac p{p-1}=\log p.
\]

For $p=2$, this is the one-term identity $T_2=\log2$.  Repeating the same
primitive cycle $r$ times repeats the same roof sequence $r$ times and
therefore multiplies its time by $r$.  A repetition is not counted as a new
primitive map orbit.  QED.

### Proposition 5 — Scalar product (and its boundary)

With unit primitive weights, the ordinary same-object product is

\[
Z_{226}(s)=\prod_{p\ \mathrm{prime}}(1-e^{-s\log p})^{-1}
=\prod_{p\ \mathrm{prime}}(1-p^{-s})^{-1},
\qquad \Re s>1.
\tag{12}
\]

This is only a scalar orbit product on its absolute-convergence half-plane.

**Proof.** Propositions 3--4 give one primitive orbit of length $\log p$ per
prime and repetitions $r\log p$.  Hence

\[
\log Z_{226}(s)=\sum_p\sum_{r\ge1}\frac{p^{-rs}}r,
\]

which converges absolutely for $\Re s>1$, since it is bounded by the
corresponding all-integer Dirichlet sum.  Unique factorization identifies the
expanded product with the ordinary Euler product there.  No continuation or
operator determinant is inferred.  QED.

## 5. Monodromy warning and source-naturalness controls

At every surviving central state, the derivative in the $(q,p)$ plane is

\[
A=D_{(q,p)}F(1,1)=
\begin{pmatrix}0&1\\-1&2\end{pmatrix},
\qquad A=I+N,\quad N^2=0.
\]

For the prime-$p$ base cycle, $P_p=A^{p-1}$, and for every repetition
$r\ge1$, $P_p^r=A^{r(p-1)}$ has eigenvalue 1.  Consequently

\[
\det(I-P_p^r)=0.
\tag{13}
\]

Equation (13) is an early obstruction to importing a nondegenerate periodic-
orbit flat-trace formula.  It is not an operator construction, and it does not
authorize a deeper trace claim.

| Control | Exact finding | Interpretation |
| --- | --- | --- |
| Remove all divisor witnesses | Every integer fibre has the central phase cycle | The witness rule, not the Hénon recurrence alone, supplies prime selectivity |
| Replace $h$ by any nonnegative local test | The same cycle-sum proof retains exactly the labels with zero full-scan test sum | `PROVES_TOO_MUCH`: constraint engineering is generic unless a source-naturalness argument is added |
| Use the earlier 222 phase set | The first phase is absent there and the prime sum has the $\log2$ offset | Confirms that 226 is a genuinely new carrier, not an edited record |
| Use control 160 | Its adjacent-ratio clock also telescopes to $\log n$ under an explicit scan/reset timing | Clock mechanism is duplicated engineered timing, not a new A0 breakthrough |
| Replace roof by unit roof | The same prime ledger remains but periods become $p-1$ | Confirms clock and orbit ownership are separable controls, not silently interchangeable |
| Retain all $(q,p)$ | Equation (10) classifies every full real state | No centre, momentum, or prime-domain crop is used |
| Sentinel $d=1$ | It is neutral for every $n$, not only for $n=2$ | The initialization convention is a declared design choice |
| Monodromy | Equation (13) holds for every surviving primitive and repetition | Standard nondegenerate flat-trace denominator is unavailable |

The exact clock remains OPEN as a natural arithmetic mechanism. The phase
coordinate, neutral initialization, quadratic force and universal roof were
chosen before the audit, but their joint selection has not been derived from a
canonical principle in the prior-work lineage.

## 6. Gate assessment and decision

| Gate | Evidence for this exact candidate | Status | Limitation / next obligation |
| --- | --- | --- | --- |
| A0 | Divisibility witnesses are executed inside the same map and select the full prime periodic support; controls show the construction is not a prime-domain crop | `OPEN — naturalness unresolved` | The phase schedule and quadratic force remain explicit engineering choices; 160 is an adjacent precedent |
| A1 | Global symplecticity, complete all-state periodic ledger, one primitive flow orbit per prime, exact roof and repetition law | `OWNER-LEVEL POSITIVE` | Degenerate monodromy prevents importing a nondegenerate flat trace |
| A2 | Scalar product (12) only | `NOT EVALUATED` | No operator, function space, Fredholm determinant, trace normalization or continuation |
| Route B | No candidate-specific authorization or Route-A readiness | `NOT INVOKED` | Remains outside this package |

**Portfolio decision: retain as an exact same-object engineering control; stop
promotion toward a natural A0 and fork before any analytic-owner work.** A new
operator, roof, phase convention or force would require a new candidate card;
no credit is transferred from 160 or 222.

## Reproducibility and evidence

All results are exact algebraic arguments from (1)--(5), covering every integer
fibre, phase, real coordinate, and positive repetition order.  No numerical
cutoff, GPU run, prime table, fitted parameter or target-zero data was used.
The [candidate card](candidate-card.md), [claim ledger](claim-ledger.md), and
[evidence index](evidence/README.md) preserve the identity, controls and
verification scope.  A future analytic-owner audit would need a separately
frozen package and must not infer a Fredholm object from the scalar product or
from the monodromy warning.
