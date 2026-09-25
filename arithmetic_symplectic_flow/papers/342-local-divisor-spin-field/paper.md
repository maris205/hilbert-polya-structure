# A reactive divisor-spin field has owned periodic motion and continuum copies

Candidate: `ANG-20260920-DSF01`. Package: `342-local-divisor-spin-field`.
Status: `OWNED SPIN REACTION; CONTINUUM PRIMITIVE COPIES — STOP / FORK`.
Date: 2026-09-20. This is a broadened time-action-groupoid audit, not a
classical symplectic suspension or a formal Route evaluation.

## 1. Question, frozen object and scope

Can proper-divisor symbolic permission control a genuinely reactive conservative medium,
while the same full object has intrinsic primitive closed packets? The
[original card](candidate-card.md) freezes a particle coupled to a countable field
of full unit spins. The answer to existence and ownership is positive;
the answer to finite intrinsic prime-packet multiplicity is negative already in
the prescribed small window. Unvisited memory gives continuum many distinct primitive
packets at exactly the same least period. These are not repetitions or
different phases of one packet.

This is an analytic result, not a finite orbit computation. A standard
finite-dimensional Lyapunov centre theorem supplies local nonlinear periodic existence; we
verify its hypotheses below and distinguish that dependency from our own argument.
We neither classify all global trajectories nor produce a trace or operator.

| Frozen field | Same-object owner |
| --- | --- |
| Carrier | Y=R²_q x R²_p x product_(lambda in I) S²_lambda; I={(n,d):n>=2,2<=d<n} |
| Measure | Lebesgue particle volume times ALL normalized sphere areas |
| Arithmetic | Fixed proper-divisor mask w(n,d), sampled at the current cell |
| Motion | Exact autonomous particle/spin equations in the original card |
| Time | Actual solution time t, never a logarithmic IMAGE clock |
| Arrows | (Phi^t z,t,z), including every real time and all stabilizers |
| Packets | Entire full-state oriented orbits with H_z=L Z, least L>0 |
| Classical base/roof/lift | NOT APPLICABLE; no finite-dimensional symplectic suspension asserted |

All sphere poles, unvisited spins, energies, momenta and finite incoming arrows
remain. The local window is a probe, never a reduced carrier. No
prime table, prime-dependent coefficient, log-prime roof, zero or von Mangoldt weight
is supplied. The bump, vector interaction, carrier and measure are designed.

## 2. The full flow exists and owns its inverses

Write the card's potential without cell cuts as

    V(q,S)=sum_(lambda=(n,d) in I) w(lambda) A(q_1-n,q_2-d) dot S_lambda.

The translated supports have disjoint interiors and a positive gap. On any
bounded q-region only finitely many terms can occur; at any q at
most one term is nonzero. The bump is smooth and flat at
its support boundary. In particular the potential and equations agree smoothly
through the floor cuts: they vanish in an open strip around each
cut. No discontinuous switching or choice of solution is hidden here.

On a bounded q-region these are ordinary smooth finite-dimensional equations for
q,p and the finitely many possibly active spins. The card's bracket gives

    qdot=p, pdot=-grad_q V, Sdot_lambda=w(lambda) A(q-lambda) cross S_lambda.

The last sign follows directly from {S_i,S_j}=epsilon_(ijk) S_k. The Hamiltonian
is locally cylindrical, not globally a function of one fixed finite set
of spins. Its derivation is compatible on overlapping finite blocks. We do
not infer a finite-dimensional symplectic manifold for the entire product.

Each sphere is preserved because S dot (A cross S)=0. Along every
local solution H=|p|²/2+V is conserved: the particle terms cancel and each
spin term is A dot (A cross S)=0. Uniformly in all fields,

    |V| <= C_0=3/sqrt(8),
    |p(t)| <= sqrt(2(E+C_0)), where E=H(z).

Indeed beta<=1 and |u|,|v|<=1/4 on an active support. The translated
first derivatives also have a uniform finite bound. Thus on any finite
time interval q and p stay bounded. Only finitely many cells can
be reached, all their spin coordinates lie in compact spheres, and the
ordinary finite-block continuation theorem extends the solution. The same argument
works backwards. Uniqueness and compatibility give a global full-state flow:

    I_z=R, D_t=Y for every z,t, and I_t=Phi^(-t) on ALL Y.

This includes zero momentum, poles, cuts and arbitrary spin sequences. There
is no finite escape, terminal free region, collision rule or added endpoint.

For initial points in a bounded particle neighborhood, the energy bound is
uniform independently of the other spins. A fixed compact time interval
therefore requires one common finite block. Finite-dimensional continuous dependence,
together with unchanged exterior coordinates, proves joint continuity in the ordinary
product topology. Each Phi^t is a homeomorphism with inverse Phi^(-t).

The countable product of spheres is compact metrizable. Consequently Y is
locally compact, second countable and Hausdorff, and mu is a full-support
sigma-finite Radon measure. G is the continuous graph of (t,z)->Phi^t z,
homeomorphic to R x Y. Its multiplication adds actual times, its inverse
reverses time and endpoints, and C=t is a continuous additive cocycle.
It is a time-action groupoid, not an etale germ construction. Distinct
times remain distinct arrows even at an equilibrium.

## 3. All-point IMAGE with the frozen finite-block prescription

On any finite block the particle divergence is zero: qdot is independent
of q and pdot is independent of p. For each active sphere,
S->A(q) cross S is an infinitesimal rotation and has zero divergence
relative to sphere area. Dependence of one component on different coordinates
does not contribute to its own divergence. Thus the finite flow preserves
the exact volume dq dp times all normalized areas in that block.

Fix t and a full target y. Its inverse q-segment is compact,
so the card's smallest R exists. In a neighborhood where this segment
stays in (-R+1,R-1)², the actual inverse equals the finite-block inverse on
I_R and the identity on every other spin. All active cells on
that segment belong to I_R. A larger block adds only stationary coordinates
there. Its absolute inverse-volume Jacobian therefore has the same value:

    j_t(y)=1, for EVERY y in Y and EVERY real t.

This is an intrinsic volume statement at poles too, not a determinant
in singular polar coordinates. Smooth zero extension deals with all cell and
bump boundaries. The integer R-selection need not be smooth: each eligible
local version gives the same value 1.

For completeness, let U_R be the targets whose entire inverse q-segment
lies in the displayed open square. These sets are open, increase with
R, cover Y, and are finite-coordinate cylinders: the finite-block inverse staying
in the square is an equivalent test by uniqueness. For a Borel
subset of U_R the inverse is the volume-preserving finite-block map times
identity on the remaining product. The finite change-of-variables theorem and product
measure give its full Borel IMAGE identity. Partition Y into the disjoint
sets U_R minus the preceding U_R. Injectivity makes their inverse images
disjoint; countable additivity gives, for EVERY Borel E,

    mu(Phi^(-t) E)=mu(E)=integral_E j_t dmu.

Composition uses the actual global inverses and j_(s+t)=1=1*1. No null set
is deleted and no infinite determinant is invoked. The logarithmic measure
cocycle is zero; the physical clock remains C=t. These different quantities
are not identified, and no height extension has been inserted.

## 4. Actual nonlinear local periodic trajectories

Let lambda_0=(4,2), u=q_1-4, v=q_2-2. MAIN has w(lambda_0)=1.
Inside the frozen window only this spin can act; all other spins
are constant. Its six-dimensional core has Hamiltonian

    h=|p|²/2+beta(u) beta(v) (u S_x+v S_y+S_z).

There is a core equilibrium at u=v=p=0, S=(0,0,-1). The full
equilibrium set also contains every exterior field; we do NOT apply a
finite-dimensional isolated-equilibrium theorem to that infinite product.

In south-pole coordinates s=(S_x,S_y), S_z=-sqrt(1-|s|²), one has
beta(0)=1, beta'(0)=0, beta''(0)=-32 and

    h+1=|p|²/2+16(u²+v²)+u s_x+v s_y+|s|²/2+O(3).

The Hessian is positive definite: each position/spin block has diagonal
32,1 and off-diagonal 1, hence determinant 31. A local analytic canonical
spin chart, with {Q,P}=1, is

    S_x=Q sqrt(1-(Q²+P²)/4),
    S_y=-P sqrt(1-(Q²+P²)/4), S_z=-1+(Q²+P²)/2.

It produces exactly the card's spin bracket, including {S_x,S_y}=S_z.
Thus the local core is an analytic Hamiltonian system on an open
subset of R^6, with the original time parameter.

Set z=u+i v and sigma=s_x+i s_y. The linearized equations are

    zddot=-32 z-sigma, sigmadot=i(z+sigma).

A mode exp(i omega t) requires

    f(omega)=(omega-1)(omega²-32)-1
            =omega³-omega²-32 omega+31=0.

The exact signs f(-6)=-29, f(-5)=41, f(0)=31, f(1)=-1,
f(5)=-29, f(6)=19 locate three distinct roots omega_- in (-6,-5),
omega_0 in (0,1), omega_+ in (5,6). Their sum is 1,
so omega_++omega_-=1-omega_0>0. Therefore Omega=omega_+ is strictly larger
than both other absolute frequencies. The six real-system eigenvalues are the
three pairs plus/minus i omega_j, all simple and nonzero. No integer
multiple i k Omega for k other than plus/minus 1 is an
eigenvalue, including k=0.

We invoke the classical Lyapunov centre theorem: a smooth Hamiltonian equilibrium
with a simple imaginary pair and the stated integer nonresonance has nearby
nonconstant periodic solutions. A primary-source statement is in Ahmad, Groves
and Nilsson, [Section 1.1](https://link.springer.com/article/10.1007/s00332-024-10073-z);
the classical statement is also recorded in Golebiewska and Rybicki,
[Section 1, version 1](https://arxiv.org/html/2406.14053v1).
Only this finite-dimensional classical result is used, not either paper's
generalization, resonant result or infinite-dimensional framework. The precise nonlinear
existence step is this cited theorem, not the imaginary spectrum alone.

All hypotheses have now been checked on the owned core. Its small
periodic trajectories can be chosen wholly inside |u|,|v|<1/8, |p|<1/8,
S_z<-3/4. Extending by ANY constant exterior field gives an actual
trajectory of the frozen full flow by uniqueness and locality.

For any such nonconstant periodic state, H_z is a closed subgroup
of R by continuity. It contains a positive time but is not
R, since that would make the trajectory constant. Hence its ENTIRE
return group is L Z for a least L>0. This establishes a
genuine primitive full-state packet, not merely a sampled period. We do
not give an exact formula for L or identify L with the
linear period 2 pi/Omega.

## 5. The decisive full-memory multiplicity obstruction

Fix one of the actual nonconstant core periodic trajectories just established.
For each exterior field xi in product_(lambda!=lambda_0) S²_lambda, locality gives
its full-state lift, with xi constant for all time. Every lift has
EXACTLY the core's return group L Z; there is no hidden extra
spin condition on a return. Its positive repetitions are rL on that
same full orbit, not new primitive packets.

Two different exterior fields cannot be time phases of one another: every
coordinate on which they differ is constant along these entire trajectories.
Already varying the single unused spin at (3,2) over S² and fixing
the other unused spins displays continuum many distinct primitive packets with
the SAME least period L. This subfamily demonstrates multiplicity; it does
not replace the original all-fields carrier.

All finite incoming arrows are owned too. If Phi^t x belongs to
one of these periodic orbits, x=Phi^(-t)(Phi^t x) belongs to that very
orbit. A different field or a transient exterior trajectory cannot join it
at finite time. An asymptotic approach, if any, is irrelevant to this
finite-time claim.

More generally any full-state periodic trajectory has a bounded position path
and visits finitely many cells in a period. Spins outside those cells
are constant for the entire periodic extension. Any such trajectory therefore
admits the same unused-field multiplicity mechanism. The explicitly proved local
family makes that conditional observation nonvacuous.

This is incompatible with an intrinsic ledger having finite primitive multiplicity
for each intended prime packet. No comparison of L with log p
is needed. A common-period quotient, selected reference field, spin quotient,
particle projection or representative per packet would change the frozen object.
Continuum multiplicity is not remedied by calling the discarded coordinates memory
or by treating these states as negligible for a measure calculation.

## 6. Separately owned controls

Each control retains ALL Y, mu and its own actual solution time.
For DIVISIBILITY-OFF and DIVISIBILITY-SHIFT, the same local finite-block argument
applies to their respective fixed masks: each has its OWN conserved Hamiltonian,
uniform potential bound, global flow, inverse and all-point j_t=1. For
REACTION-OFF, spins are constant and particle energy in that fixed field
is conserved along each full trajectory. Its particle divergence and its
zero spin divergence again give its OWN global flow and Borel IMAGE
identity. It is not asserted to have MAIN's spin-Poisson Hamiltonian owner.

| Own control | Dynamics in the contained window | Entire return and packet result |
| --- | --- | --- |
| DIVISIBILITY-OFF | Its own local coefficient at (4,2) is 1; same displayed core equations | The checked local theorem applies to this control; nonconstant H=L Z and continuum exterior-field copies |
| DIVISIBILITY-SHIFT | Its own coefficient is 0 since 2 does not divide 5; qdot=p, pdot=0, all spins constant | A trajectory wholly contained in this window can be periodic only for p=0; these are equilibria with H=R |
| REACTION-OFF | Its own spins are all fixed; an invariant south-spin one-dimensional oscillator exists | Explicit nonconstant primitive period T(a), H=T(a) Z, and continuum exterior-field copies |

The first control's conclusion follows by checking its own local equations,
not by borrowing MAIN's global orbits. The shifted control's conclusion concerns
trajectories contained for their entire periodic motion in the window. It
does NOT exclude or classify trajectories that leave this window and return.
For a shifted equilibrium global invertibility makes every finite incoming point
that same state, while all times give its isotropy R.

Here is an independent existence and least-period argument for REACTION-OFF.
Set its active spin to (0,0,-1) and take v=p_v=0. This is
an invariant slice because beta'(0)=0. Its own particle Hamiltonian reduces to

    h_1=p_u²/2-beta(u).

Choose 0<a<1/8 sufficiently small that 2(1-beta(a))<1/64. At energy
-beta(a) the motion is between -a and a and satisfies

    p_u²=2(beta(u)-beta(a)),
    T(a)=4 integral_0^a [2(beta(u)-beta(a))]^(-1/2) du.

The bump is even and strictly decreasing on (0,1/4). The integral
is positive and finite, since beta'(a)<0 makes the turning-point singularity
integrable. The four monotone quarter traversals give the first full phase-space
return after T(a), so the ENTIRE return group is T(a) Z.
The strict momentum bound and south spin put the entire nonconstant orbit
in the frozen window. Every exterior field is independently allowed and
stationary. Distinct such fields again give distinct primitive packets at T(a),
with finite incoming states confined to their own full orbit by invertibility.

## 7. Claim, lineage and route boundaries

| Claim | Disposition | Limit |
| --- | --- | --- |
| T0 full typed owner | ESTABLISHED | Locally finite Poisson-field flow and actual time-action groupoid; not classical ASFS |
| T1 physical clock and reaction | ESTABLISHED as the declared equations | Strong arithmetic naturalness is OPEN; the divisibility graph is designed input |
| T2 existence and repetition | ESTABLISHED locally | Nonconstant primitive packets exist, but full intrinsic finite multiplicity FAILS |
| T3 trace/zeta/operator | NOT AUDITED | None constructed or borrowed |
| Formal Route A / B | UNASSIGNED / NOT INVOKED | No formal coordinate, readiness or quantum lift |

The preserved lineage arrow is proper-divisor symbolic permission -> current-cell
interaction -> mutual particle/spin evolution -> future position and remembered medium.
This goes beyond a fixed force medium but is not an implementation
of long division, dynamically generated primality, or a Logistic/Henon conjugacy.
The positive ownership and periodic-existence results do not close a strong
endogenous prime-origin A0. No numerical evidence or heuristic frequency fit is
used. Arbitrary-mask PROVES_TOO_MUCH remains a relevant control risk.

| Established / negative / open | Exact scope |
| --- | --- |
| Established | Global uniqueness; all finite-block inverses; full Borel IMAGE; local nonlinear periodic full states |
| Negative | Continuum distinct primitive packets at one least period from retained unused spins |
| Open / unclassified | Global trajectory classification, exact main least periods, strong arithmetic naturalness, any spectral theory |
| Not claimed | No-period theorem, impossibility for reactive media generally, formal Route success, calibrated independent review |

## 8. Portfolio decision, reproducibility and handoff

Portfolio: **STOP / FORK** this frozen candidate. The decisive reason is
full-state primitive multiplicity, not a failure to construct motion or local
closed trajectories. Its same-object ledger remains intact throughout the audit.
A future architecture must confront unused-medium multiplicity before parameter or
period fitting; deleting memory or changing its equivalence needs a new ID.
This is a design constraint, not a proof that every such architecture fails.

Exact inputs are the original version-1 card and the two narrowly checked
classical-theorem statements cited above. Methods are finite-dimensional ODE continuation,
intrinsic divergence and product measure, exact linear algebra, the stated local
existence theorem, full-flow stabilizers and an exact oscillator integral. There
are no scientific numerical commands, cutoff experiment, simulated orbit or generated
publication artifact. File checks and their limits belong in [evidence](evidence/README.md).

[The claim ledger](claim-ledger.md) separates theorem scope from portfolio and
Route status. [The source record](evidence/scout-record.md) records bounded access,
definitions, the parallel Pre-P0 NONE and review provenance. The separately
locked [model review](evidence/independent-review.md) is a shared-history, inherited-model
check, NOT_CALIBRATED and not external peer review or independent-error evidence.
The research programme remains active; this local stop earns no transferable
credit and no next candidate is silently frozen here.
