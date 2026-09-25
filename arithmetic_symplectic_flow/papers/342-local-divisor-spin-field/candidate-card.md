# Frozen candidate — moving particle and reactive divisor-spin field

Candidate ID: `ANG-20260920-DSF01`.
Paper ID: `342-local-divisor-spin-field`. Date: 2026-09-20.
Version 1. Initial status: `OPEN — FULL SPIN-FIELD FLOW AND LOCAL RETURN GATE`.

## 1. Entire carrier, measure and proposed Poisson description

Let I={(n,d) in Z²:n>=2,2<=d<n}. Freeze

    Y=R²_q x R²_p x product_(lambda in I) S²_lambda,
    mu=dq_1 dq_2 dp_1 dp_2 x product_(lambda in I) sigma_lambda,

where EVERY S_lambda is a full unit sphere and sigma is normalized spherical
area. Use ordinary product topology and Borel structure. Keep ALL energies, momenta,
signed coordinates, sphere poles and spin sequences, including every unvisited spin.
No chosen initial medium, reference field, centre, energy shell or conull restriction.

For smooth functions of q,p and finitely many spins specify

    {F,G}=sum_j(F_qj G_pj-F_pj G_qj)
           +sum_lambda S_lambda dot (grad_Slambda F cross grad_Slambda G).

Compatibility with the actual locally finite equations below is an obligation. No
infinite-dimensional determinant or finite-dimensional symplectic form is presumed. The typed
broadened owner is the ACTUAL time-action groupoid of this proposed particle/Poisson-field
flow, if established. It is NOT a classical finite-dimensional symplectic suspension.

## 2. Arithmetic permission and exact autonomous equations

On all integer pairs set

    w(n,d)=1_{n>=2,2<=d<n,d divides n}.

Fix one common bump and vector, with no tunable parameter:

    beta(u)=exp(1-1/(1-16*u²)) when |u|<1/4, and0 otherwise,
    A(u,v)=beta(u)*beta(v)*(u,v,1).

At the CURRENT q read n=floor(q_1+1/2), d=floor(q_2+1/2),
u=q_1-n, v=q_2-d. If lambda=(n,d) belongs to I, define

    H=|p|²/2+w(n,d)*A(u,v) dot S_lambda,
    qdot=p,
    pdot=-w(n,d)*grad_(u,v)[A(u,v) dot S_lambda],
    Sdot_lambda=w(n,d)*A(u,v) cross S_lambda,
    Sdot_eta=0 for all eta!=lambda.

If (n,d) is not in I, define H=|p|²/2, qdot=p,
pdot=0, and ALL Sdot=0. At half-integer cuts use the displayed floor
value. At bump boundaries use its smooth zero-extension derivatives, not a collision.
All source points and all other legitimate fields remain; free regions are not terminals.
No reflection, reset, sampling, endpoint gluing or infinity point is added.

Spin direction enters actual particle force; the particle position enters the spin's
axis of evolution. A departed spin is not reset; any revisit uses its
current state. The arithmetic mask is a declared fixed interaction graph, not a
claim that this graph or its prime structure is dynamically generated.

## 3. Maximum time domains and complete actual inverse

Phi^t z means the unique maximal solution of those exact autonomous equations.
Existence, uniqueness, sphere preservation, regularity and dependence must first be proved.
Let I_z be its maximal interval containing0, and

    D_t={z:the entire segment from0 to t lies in I_z}.

The proposed inverse is I_t=Phi^(-t):D_(-t)->D_t, from the ACTUAL
target with its complete spin memory. Nonuniqueness is a STOP; never select a
favourable solution. Finite lifetime retains only the real partial flow domains, without
adding a cemetery object or waiting loop. Every Phi^0 and finite incoming
history remains. An asymptotic arrival is not automatically a finite-time arrow.

## 4. Finite-block all-point IMAGE, separate from physical time

For a legal target y and a fixed t choose the smallest integer R>=2
such that the COMPLETE inverse-time position segment lies in (-R+1,R-1)².
Let I_R=I intersect[-R,R]². On the finite block q,p and ALL
full spheres indexed by I_R, solve the same inverse equations and use

    dq dp x product_(lambda in I_R) sigma_lambda

as volume. Its absolute inverse-flow Jacobian defines j_t(y); no value is
preassigned. All other spin coordinates follow the original equations, not a new rule.

Prove every finite segment is covered, each sufficiently large block is an actual
local inverse version, and enlarging the block does not change j_t. Prove
the version at poles, cuts, zero momenta and all null states, and

    mu(I_t E)=integral_E j_t dmu

for EVERY Borel E in its real inverse domain, with finite-composition consistency.
If this fails, do not change measure or delete spins. IMAGE is a
measure obligation, NOT the definition of physical time; no IMAGE-height extension replaces Phi.

## 5. Physical-time groupoid, entire isotropy and packet identity

Freeze G={(Phi^t z,t,z):z in D_t}, inherited Borel structure from
Y x R x Y. Source is z, range Phi^t z, and C=t.
Keep distinct times even when endpoints coincide. Prove time addition, inverse and
all actual domains. Do not use a time-one map, germ quotient or extra roof.

For every studied z the ENTIRE source return group is

    H_z={t:z in D_t, Phi^t z=z}.

Only H_z=L Z with least L>0 defines a primitive positive-time packet;
rL is the r-fold traversal of that SAME full orbit. Keep equilibria,
nonreturning states, every other stabilizer and all actual incoming points.
Identify phases only by the actual oriented time action. Do not quotient by
particle projection, integer labels, shared period, unused spins, spin rotations, lattice
translations or velocity reversal. Unvisited memory is part of the object.

## 6. Three independently owned controls

Each uses ENTIRE Y and mu but its OWN vector field, maximum time
domain, inverse, finite-block IMAGE, time groupoid, return groups and full packets.

DIVISIBILITY-OFF: replace w by1 at every lambda in I, retaining all
other formulas. Outside I the free rule still applies.

DIVISIBILITY-SHIFT: replace w by w_+(n,d)=1_{n>=2,2<=d<n,d divides n+1}.
Use this mask's OWN particle and spin equations everywhere.

REACTION-OFF: retain MAIN qdot,pdot, but set ALL Sdot=0. Every
spin sequence still belongs to the state and affects force at its own cell.
This is an autonomous ODE comparator; do not presume it has the MAIN
Poisson-Hamiltonian owner. No fixed medium is selected to replace its full carrier.

## 7. Lineage, local return window and stop discipline

The [prior-work](../../docs/prior_work/README.md) interface (n,d)->q=(n,d)
retains ALL p and ALL spin fields; permission is exactly the proper-divisor
symbol. The arrow is symbolic admissibility -> current-cell interaction permission ->
actual particle/spin reaction -> subsequent position and remembered medium jointly determining
the next motion. This is not long division, a fitted sequential schedule or
a claimed Logistic/Henon conjugacy. Classical base/roof/mapping-torus fields are NOT APPLICABLE.
The sphere, vector A, bump, kinetic energy and product measure are declared
design. Arbitrary-mask PROVES_TOO_MUCH risk and strong arithmetic naturalness remain OPEN.
No prime table, per-prime parameter, log-prime roof, zeros or von Mangoldt data.

First close or refute the full owner and finite-block measure prescription. Then
the ONLY local return window is

    |q-(4,2)|_infinity<1/8, |p|<1/8, S_(4,2)^z<-3/4,

with EVERY other spin arbitrary. It is a probe, not the carrier. Audit
actual nonconstant full-state closed trajectories contained in this window, with their
ENTIRE return groups, phases, all finite incoming and memory multiplicity, for main
and each own control. An exact general multiplicity obstruction can close this
gate early. Equilibria alone do not prove absence of nonconstant closed orbits.
Failure to find a contained orbit does not rule out leaving and returning.

Analytic local-generator and return arguments only; no numerical/high-period/energy/parameter campaign.
A needed standard existence theorem may receive narrowly scoped PRIMARY-source verification;
linear imaginary eigenvalues alone never prove nonlinear periodic orbits. Freeze before
that verification. If the bounded checks cannot decide, record OPEN and stop
the bounded audit, not the programme. Any changed mask, field, clock, owner
or memory quotient needs a new ID. No trace/operator/quantization rescue or T3.

## 8. Exact source access and review authority

The source author read ONLY332 original1–123 and233 original1–109, neither
EOF, without total-line/hash measurement. Heading discovery exposed appended-outcome TITLES
332:192 and233:151, not bodies. Initial OPEN states, constraints and unproved
questions inside the prefixes were visible. No cited old source was opened.
The author supplied332's original definition and had previously read that same233
prefix. This is shared-history definition comparison, not novelty or nonconjugacy evidence.
The new full spin memory/reaction differs definitionally from332's fixed magnetic medium
and233's multiplicative mode interactions. No old result, clock or authorization transfers.

Root also read276 original1–151/182 and284 original1–143/174 (wc-l totals),
not outcomes; heading scans exposed outcome TITLES152/144. Their definition/provenance text
was visible. Root's separate scan/reduction idea supplied no new complete mechanism;
those reads do not contribute a theorem to this object. The separate finite-
quotient source scout returned NONE and is recorded independently, not as this verdict.

Root had private preliminary mathematical thoughts after the definition-level delivery and
before freeze; this card does not claim zero pre-freeze thought or blind ideation.
It precedes all REPORTED theorem claims, scientific computations and gate verdicts. No
preliminary result is given to the reviewer. Source author supplied definitions only.

Root owns integration and all files except evidence/independent-review.md. Reviewer first
reads this ORIGINAL card, privately derives main/controls, reports metadata ALL RAW
READY, then releases only after root's FIRST lock and explicit RAW RELEASE.
Manuscript access needs a separate unlock after ALL RAW FINAL. Any external
theorem use must disclose exact source and distinguish it from an original proof.
ARS three checkpoints remain inherited-model/shared-history NOT_CALIBRATED, not external peer review
or independent-error evidence. No auxiliary reviewer, external model or scientific numerics.

T0--T3 are broadened owner labels; formal Route UNASSIGNED, B NOT INVOKED.
Markdown only; no PDF/LaTeX generation, publication/upload, config edit or Git staging/commit.
Preserve old/dirty work, positive304/partial-positive320 and paused241/242. Goal stays active.

## Appended outcome — original version 1 above remains unchanged

Candidate ID: `ANG-20260920-DSF01`.
Status: `OWNED SPIN REACTION; CONTINUUM PRIMITIVE COPIES — STOP / FORK`.

Original193-line SHA256:
`c244e56d14adedb074d777123f4dbf37f3daa3178808f6c0093edf0a34c6bc9f`.
The original OPEN was the freeze state; this separately appended result does
not alter its equations, full carrier, inverse prescription, clock or packet convention.

The complete locally finite equations own a unique global flow, complete actual
inverse and full Borel finite-block IMAGE with j_t=1 at every point.
Actual physical time remains t. A checked standard Lyapunov centre theorem
gives nonconstant full-state periodic trajectories in the frozen window, with entire
return group L Z and least L>0. Varying any unused spin
creates continuum distinct primitive packets at the SAME L, not repetitions.
All incoming finite-time points lie on their own full periodic orbit.

Each control has its own full owner and scoped return ledger. DIVISIBILITY-OFF
has the same local periodic/multiplicity mechanism; SHIFT has only equilibria among
window-contained periodic trajectories; REACTION-OFF has an explicit local primitive oscillator
with the same unused-memory multiplicity. Leave-and-return trajectories are not classified.

Portfolio STOP / FORK for finite intrinsic primitive multiplicity failure. This
does not deny closed motion or prove a general reactive-medium no-go. Strong
arithmetic naturalness remains OPEN; same-object ledger intact. T0 owned; T1 physical
clock owned / naturalness OPEN; T2 local existence positive / multiplicity FAIL;
T3 NOT AUDITED. Classical A0/A1/A2 NOT APPLICABLE, formal UNASSIGNED,
B NOT INVOKED. No next complete tuple pending; programme goal active.

See [paper](paper.md), [ledger](claim-ledger.md) and [evidence](evidence/README.md) for
proof limits, source dependency, review locks and file checks. Internal model
review is shared-history NOT_CALIBRATED, not peer review. Markdown only.
