# LPI01 — independent card-only derivation

Candidate: `ANG-AUDIT-20260923-LPI01`; Paper439; session2026-09-23.
Full germ/density owner, bounded-period isolation and three full controls.

## 1. Actual input and separation

- candidate-card.md original92-line prefix SHA256 6ecdba27de29a5c5b09c802960bae247c1b3465a2c52af418d4dcf1869553794.
- evidence/scope-review.md SHA256 535a40761419d3c87459d2e6d4aa125af914539fce06f22d3f94ea314beb02cc — 92 frozen lines.
- Root reported full reading of CP1 and separately released this analysis.
  I reread precisely card1–92 to its scientific EOF and measured that prefix.
  No439 author paper, README, ledger, appended Outcome, current peer/sibling
  report, earlier389 source or external resource was read. Earlier429 and
  other shared history remain exposure, not borrowed proofs for this owner.
- Retained stream and ARS/router/workflow/DA/runtime instructions apply.
  The card discloses root's preliminary reasoning and collision reads; I do
  not claim independently audited chronology or blind preregistration.
  Same continuing AI reviewer, inherited settings, NOT_CALIBRATED, not
  cross-model/human/external peer validation. Served model/settings unknown
  beyond the session's inherited configuration, not independently attested.
- Methods: exact density/iterate identities, finite clock-band arguments,
  connectedness and complete symbolic orbit classifications. No scientific
  program, numerical census, auxiliary agent, network, Git, PDF or publication.
  Only this raw file is written; the card and CP1 are left unchanged.

## 2. Every-point germ clock and actual inverse IMAGE

In local density coordinates write dmu=r(x)|dx|, r continuous and positive.
For the uniquely assigned C1 germ F_i at a legal source point define

    j_i(x)=r(F_i x)|det DF_i(x)|/r(x)>0,
    kappa(x)=log j_i(x),
    J_i(y)=1/j_i(theta_i y)                                  (1)

on each ACTUAL inverse chart theta_i, with its source restriction and image.
This is independent of coordinate notation and finite at every owned point.
The clock need not be positive, constant, integer-valued or globally continuous.
The declared germ at a cut/null point is used there; no a.e. replacement occurs.
On such a chart, change of variables, restricted to the assigned Borel source,
gives mu(theta_i E)=integral_E J_i dmu for EVERY Borel E in its actual image,
also for infinite integrals. Countably many relatively compact charts make
the continuous-density measure locally finite and sigma-finite.

Local injectivity neighborhoods may be used as a countable inverse-chart
cover; splitting this cover for bookkeeping never changes T, the assigned
germ at a point or a cut assignment. Actual inverse restrictions, not an
invented globally single-valued inverse, are retained. Their images are Borel
by the continuous inverse on each local chart. The countable chart/branch
cover gives Borel kappa and all legal finite-history sets.

For a legal n-step inverse word theta_a with actual target Y_a, chain rules
and cancellation of intermediate densities give

    mu(theta_a E)=integral_E exp(-S_n(theta_a y)) dmu(y),
    E Borel subset Y_a.                                    (2)

Every intermediate inverse-domain condition is imposed. On a branch-pair
map B:w->z with T^m z=T^n w, the forward IMAGE density from source w to
range z is exp(S_n(w)-S_m(z))=exp(-c(z,m-n,w)). This follows by composing
the actual forward chart along w with the inverse chart along z. Thus for
each Borel E in that pair's domain, mu(BE)=integral_E exp(-c(Bw,m-n,w))dmu(w).
No formal branch word contributes a map where its actual domains fail.

## 3. Full groupoid, signed clock and all kernels

An actual arrow is (z,m-n,w), T^m z=T^n w, both histories legal. Two
witness pairs for the same retained lag differ by adding the same integer
to both indices. Start with the smaller indices; the larger witnesses
supply a common additional legal tail, whose clock sums cancel. Hence

    c(z,m-n,w)=S_m(z)-S_n(w)                                (3)

is well-defined. For composable witnesses T^m z=T^n w and T^p w=T^s v,
align at max(n,p). If n<=p the composite witnesses are (m+p-n,s);
if n>=p they are (m,s+n-p). All continued steps are supplied by the existing
middle history, so no terminal is padded. The sums telescope to c(gh)=c(g)+c(h).
Inverse swaps endpoints and negates clock and lag. Forward x->Tx is
(Tx,-1,x), clock -kappa(x), not +kappa(x).

Countably many legal inverse-chart pairs cover the Borel arrow set in
X x Z x X, with agreeing Borel clock formulas. The extension retains ALL
X x R objects and arrows (w,h)->(z,h+c); height translation commutes with it.
No regular quotient structure is asserted. The complete kernels are

    K_lag={(z,0,w):T^n z=T^n w for some legal n},
    K_clock={(z,m-n,w):T^m z=T^n w, S_m(z)=S_n(w)},
    K_joint={(z,0,w):T^n z=T^n w, S_n(z)=S_n(w)}.            (4)

These include every unequal-endpoint arrow satisfying the equations, not
just isotropy. They need not be units. Full inverse histories are the
recursion I_0(y)={y}, I_(n+1)(y)=union_{v in I_n(y)}{theta_i(v):v in dom theta_i},
with all original restrictions, repetitions identified only when they give
the same source point. No depth or branch cutoff is taken. Source orbits
are exactly points with a legal forward meeting, equivalently the union of
all finite inverse histories of the forward images of a representative.

## 4. Entire isotropy, incoming states and complete phases

A nonzero source isotropy lag at x is equivalent to eventual periodicity:
an equality T^m x=T^n x with m>n enters a cycle, and conversely a reached
cycle supplies such legal equalities. If its least core period is d, every
returning lag is a multiple of d, and every integer multiple is witnessed.
For its signed one-cycle sum C, cancellation of the incoming prefix gives

    source isotropy=dZ,   c(x,jd,x)=jC,   ENTIRE H_x=CZ,
    extension isotropy at (x,h)={jd:jC=0}, j in Z.            (5)

These hold at EVERY point of the full incoming basin, not only on the core.
C is invariant under rotation along the cycle. If C!=0, H has least positive
generator |C|, extension isotropy0 and all repetitions n|C|, n>=1. If C=0,
source/extension isotropy dZ remains but H=0 and there is no positive primitive.
Both signs of C are allowed; reversing the sign changes no subgroup CZ.

Non-eventually-periodic points, including terminals and their full incoming
basins, have source/extension isotropy0 and H=0. A nonperiodic PREperiodic
point instead has the cycle groups (5); these categories must not be confused.
Each source orbit contains at most one finite core. Distinct cores cannot
become the same packet merely because their clocks or H groups agree.

For a reference b in ONE source orbit, choose any actual arrow g_x:x->b.
The phase of (x,h) is

    u=[h+c(g_x)] in R/H_b.                                 (6)

Two such arrows differ by isotropy at b, so this is well-defined. Conversely
equal classes give a matching isotropy arrow and hence an extension arrow.
Every class is realized at b; all real phases remain. Physical translation
adds its actual time, with entire stabilizer H_b. Thus H0 gives a free line,
and nonzero H gives the full circle R/|C|Z, even when the source is branched.
Reference choices are coordinates, not selections deleting other states;
no global Borel selector is claimed. A terminal reference reached after n
steps gives phase h-S_n(x), not a manufactured terminal loop.

## 5. Regular windows and all divisor/sign alternatives

Fix q>=1. If an open V has a fixed actual legal q-itinerary whose declared
germs apply at every successive image, the composition T^q|V is C1 and each
summand kappa(T^j x) is continuous there by (1). Thus S_q is continuous and
V is a regular q-window. A branch-face point need not have such a V. More
generally use only the card's explicitly assumed continuity of T^q and S_q
on its given open U; never infer this from unrelated piecewise smoothness.
Since X is Hausdorff, continuity makes Fix_q(U) closed relative to U.

For x in Fix_q(U), its LEAST source period d divides q: writing q=ad+r,
0<=r<d, the actual periodic orbit gives T^r x=x, hence r=0. Therefore

    S_q(x)=(q/d)C_d(x).                                    (7)

Now ASSUME the necessary benchmark's prime-only support and at-most-one
source packet per prime. Nonemptiness is a separate target, not an existence
input to the following implication. At every nonzero-clock q-fixed point,
(5) and (7) give, for some prime p and sign epsilon in{+1,-1},

    C_d(x)=epsilon log p,
    S_q(x)=epsilon n log p,   n=q/d, n a positive divisor of q. (8)

Thus every q-fixed S_q value belongs to

    Lambda_q={0} union {epsilon n log p:n divides q,p prime,epsilon=+/-1}.

This set is locally finite in R: for |value|<=B each nonzero entry has
p<=exp(B), and there are finitely many integers, hence primes, below that
bound and finitely many divisors/signs. Its nonzero entries have magnitude
at least log2. No prime table, numerical census or prime-distribution theorem
is used. A positive q-repeat need not itself have prime exponential: (8)
retains the repeat multiplier n, not just the least-q case.

## 6. Finite clock bands, local isolation and compact sets

For each finite B>0 consider all actual q-fixed points under discussion with
0<|S_q|<=B. Only primes p<=exp(B) can occur by (8). For each such p the
uniqueness hypothesis allows at most ONE source packet and hence one finite
core. Its least period divides q and is <=q, so it contributes at most q
q-fixed points. Incoming noncore states are not q-fixed and add none here.
Consequently this entire set is finite. If N_q(B) denotes its cardinality,

    N_q(B) <= q * #{p prime : p<=exp(B)}.                    (9)

The right side is q times a finite cardinality; no numerical value is computed.
Both clock signs are already included; uniqueness is per prime irrespective
of sign, so opposite-sign duplicate packets are not an extra allowance.

Take x in Fix_q(U) with a=S_q(x)!=0. Continuity gives an open V about x,
V subset U, with |S_q(y)-a|<|a|/2. Hence every q-fixed point in V has
nonzero clock of magnitude <=3|a|/2. By (9), Fix_q(V) is finite. Remove
its finitely many points other than x by shrinking V in the Hausdorff
manifold. The resulting open W satisfies

    Fix_q(W)={x}.                                          (10)

This is isolation among ALL q-fixed points nearby, including the potential
zero-clock stratum (which continuity excluded from V). It is not isolation
from periodic points with unbounded source periods, nor a uniform radius.

If K is a compact subset of Fix_q(U) and S_q never vanishes on K, then
B=max_K |S_q| is finite by continuity (the empty K case is trivial).
Every point of K lies in the finite set of (9), so K is finite. Equivalently
one may combine local isolation with compactness after controlling the clock;
mere isolatedness in a nonclosed set alone would not suffice. No compactness
or global continuity of the entire carrier/map has been assumed.

## 7. Continuous interval families without an ambient action

Let gamma:I->Fix_q(U) be continuous, I an interval, and suppose S_q(gamma(t))
is nonzero at least at one point (in particular, if it is nonzero everywhere).
The composition S_q gamma is continuous into the locally finite set Lambda_q.
An interval is connected; its continuous image in this discrete subset of R
is a singleton. Thus S_q gamma is a constant a!=0. The image gamma(I)
then lies in the finite clock band (9), and a continuous image of a connected
interval in a finite Hausdorff set is one point. Therefore gamma is constant.

A NONconstant such family is incompatible with the full benchmark. This
does not require an injective parametrization, a nonvanishing tangent vector,
an ambient commuting action or a quotient. It also does not say that every
owner possesses such a family. If its clock is identically0, this obstruction
gives no positive-packet conclusion. None of these statements implies
hyperbolicity or sufficiency for prime arithmetic. The period q stays fixed.

## 8. Control A — full varying positive fixed family

On OWN Lebesgue R2 put a(y)=2+y^2 and L(y)=log a(y)>0. The map and actual
global inverse are T(x,y)=(a(y)x,y), theta(u,v)=(u/a(v),v). Their Jacobians
are a(y) and 1/a(v). Thus EVERY-Borel inverse IMAGE has J(u,v)=1/a(v),
including all axes/null points, and the own clock is kappa(x,y)=L(y).
For EVERY integer k,

    T^k(x,y)=(a(y)^k x,y),    D_k(x,y)=kL(y),
    G_A={((x,y),k,(a(y)^k x,y)):k in Z},   c=D_k.            (11)

Invertibility proves all arrows are exactly these. Every inverse history
is the corresponding negative iterate. Lag, clock and joint kernels are
units, since kL(y)=0 iff k=0. The ONLY periodic points are (0,y), each a
separate fixed core and entire finite-core basin, since a(y)>1 and a nonzero
x cannot return or enter0. Each core has source isotropy Z, extension0,
ENTIRE H=L(y)Z, primitive L(y), repetitions nL(y), and phase h modulo L(y).

For each x!=0 its full source orbit is {(a(y)^n x,y):n in Z}, with
source/extension isotropy0,H0. Normalize x=a(y)^n u, 1<=|u|<a(y);
reference(u,y) gives real phase h+nL(y). Equivalently h+log|x| is a complete
phase on that orbit, shifted by the constant log|u|. Both x signs and every
y remain. Full extended orbits are {(T^k z,h-kL(y)):k in Z} at every point.

The full primitive ledger is indexed by ALL y in R, with L(y)=log(2+y^2).
There is one packet at L=log2 and two distinct packets at every L>log2;
no primitive below log2. Distinct y cannot meet under T. In particular for
each prime p>2, y=+/-sqrt(p-2) gives two log p packets, while nonprime
times also occur (e.g. y=sqrt2 gives primitive log4). Repetitions remain
attached to their own packets and do not merge this continuum.

Every q has a global regular window R2, Fix_q={x=0} and S_q=qL(y).
The family y->(0,y) is continuous and nonconstant with nonzero clock.
This owner violates the benchmark by its actual purity and multiplicity
ledger; no point selection repairs it. It is an EXTERNAL CONTROL.

## 9. Control B — complete zero-clock boundary

On its OWN Lebesgue R2, T(x,y)=(x,y+x^2), theta(u,v)=(u,v-u^2).
Both Jacobians are1, so every-point/every-Borel inverse IMAGE is1 and
kappa=0. For all integer k,

    T^k(x,y)=(x,y+kx^2),
    G_B={((x,y),k,(x,y+kx^2)):k in Z},    c=0.               (12)

The lag and joint kernels are units, but the clock kernel is ALL G_B,
including nonisotropy arrows. Every inverse depth exists. ALL points (0,y)
are separate fixed cores with source isotropy Z, extension isotropy Z,
ENTIRE H=0 and free phase h in R. Source fixedness is not a positive physical
period: the whole isotropy acts with zero height displacement.

For x!=0 every point is aperiodic; its full orbit is {(x,y+nx^2):n in Z},
source/extension isotropy0,H0. Writing y=r+nx^2, 0<=r<x^2, gives the
reference(x,r) and phase h. Its complete extension orbit is
{(x,y+nx^2,h):n in Z}. No nonzero-x point enters a fixed core. All heights
and all coordinates are retained, not only the area-generic stratum.

Every q again has regular window R2, fixed set{x=0}, and S_q=0. Thus a
nonisolated zero-clock fixed family must NOT be included in the positive
isolation claim. The full positive ledger is EMPTY: nonemptiness fails;
prime-only and uniqueness are merely vacuous. This is an EXTERNAL CONTROL.

## 10. Control C — entire real inverse and isolated nonhyperbolic core

Let f(y)=y+y^3. It is strictly increasing with derivative1+3y^2>0 and
limits +/-infinity at the two ends, hence is a bijection of R. Its inverse
g(v) is the UNIQUE real root of y+y^3=v, differentiable with
g'(v)=1/(1+3g(v)^2). No real inverse branch has been omitted. For the OWN
Lebesgue plane, T(x,y)=(2x,f(y)) has global inverse theta(u,v)=(u/2,g(v)),

    J(u,v)=1/[2(1+3g(v)^2)],
    kappa(x,y)=log2+log(1+3y^2)>=log2.                      (13)

Change of variables proves every-Borel IMAGE with these all-point values.
For every signed integer k use f^k (negative powers are iterates of g), and

    T^k(x,y)=(2^k x,f^k(y)),
    D_k(y)=k log2+log((f^k)'(y)),
    G_C={((x,y),k,(2^k x,f^k(y))):k in Z},    c=D_k(y).     (14)

For k>0, D_k=sum_(j=0)^(k-1)[log2+log(1+3(f^j y)^2)]>=k log2>0.
For k=-n<0, D_(-n)(y)=-D_n(f^(-n)y)<=-n log2<0; D_0=0. These formulas
prove the full signed cocycle and inverse laws, not just positive iteration.
Consequently lag, clock and joint kernels are all units. Every inverse depth
exists on the full plane; each source orbit is exactly its full T^Z orbit.

For y>0, f(y)>y; for y<0, f(y)<y, so a positive iterate can fix y only
at0. A positive iterate of 2x fixes x only at0. Thus the ONLY periodic
point is (0,0), a fixed core and its entire basin; all other points are
aperiodic, including both punctured axes. No outside point reaches0 because
the map is bijective. The core has source isotropy Z, extension0, ENTIRE
H=(log2)Z, ONE primitive log2 packet, all repeats n log2 and phase h mod log2.

Every other full source orbit has source/extension isotropy0,H0. Choose a
set-level reference b on ONE such orbit. Its points are T^n b, n in Z,
with UNIQUE n, and complete real phase h+D_n(b_y). Equivalently its full
extension orbit from(z,h) is {(T^n z,h-D_n(y)):n in Z}. This exact iterate
description includes x=0,y!=0 and y=0,x!=0; no global Borel selector is
asserted and the reference does not delete any other point or phase.

All q have regular window R2 and Fix_q={(0,0)}. Yet DT(0,0)=diag(2,1)
has an eigenvalue of modulus1, so this isolated fixed point is NOT hyperbolic.
The full owner meets nonempty/prime-only/uniqueness at prime2, but lacks
all-prime coverage and an endogenous arithmetic source. It refutes an
upgrade from the necessary isolation filter to hyperbolicity or a universal
no-go. This remains an EXTERNAL CONTROL, not an arithmetic admission.

## 11. Scope and freeze hold

The exact result is a CONDITIONAL bounded-period isolation/finite-compact-set
filter plus its interval-family obstruction under the specified benchmark.
It respects all proper divisors, both signs, zero clocks, actual inverse
domains, terminal/incoming states and full physical phases. No ambient action,
quotient selection, positive roof or time rescaling has been introduced.
Controls have their own full measures/maps/clocks, not cross-owner credits.
No mathematical blocker or unproved realization assertion is needed for
these conclusions; no forced flaw or numerical confidence score is supplied.

The result neither supplies periodic points nor proves a prime grammar,
naturalness, all-prime coverage or sufficiency for arithmetic admission.
There is no uniform conclusion for unbounded periods or irregular branch
boundaries. Portfolio CONDITIONAL FILTER / FORK. Classical NOT APPLICABLE;
arithmetic T1 NOT PASSED; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.
No operator, trace, RH, novelty or external-validation claim follows.

Freeze after complete readback; report exact lines/hash and HOLD. Root must
fully read this frozen raw before separate PAPER UNLOCK. Card/CP1 stay
untouched. Stop at authorized439; no440 or additional research is started.

EOF — card-only independent derivation; shared-history NOT_CALIBRATED.
