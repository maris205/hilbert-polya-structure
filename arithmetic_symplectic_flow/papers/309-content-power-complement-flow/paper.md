# Content–power feedback: a layered clock with zero time on every return

Paper ID: `309-content-power-complement-flow`.
Candidate ID: `ANG-20260920-CPC01`. Date: 2026-09-20.
Status: `OWNED LAYERED CLOCK; ALL RETURN TIMES ZERO — STOP / FORK`.
Evidence class: exact ownership and global return obstruction.
Classical A0/A1/A2 NOT APPLICABLE; formal coordinates UNASSIGNED;
Route B NOT INVOKED.

## Abstract

On all positive-integer pairs with full interval fibres, the
current real position supplies a gcd probe. The content changes
the next root and its quotient acts as a real power,
followed by complementation. Ordinary interior length and unit endpoint
atoms define one layered measure. We prove every inverse branch
and its actual IMAGE clock, including atomic rather than derivative
endpoint values. The integer root product decreases by the power
exponent. Consequently every state reaches a period-one or period-two
core in finite time; every such core has exponent one and
zero clock. All isotropy time groups vanish, although the local
clock is not identically zero. An explicit Borel coboundary records
the transient cancellation. Three separately owned controls distinguish
power transport, complement and root descent; removing root descent
permits a positive-time fixed core in the tested control fibre.
The main positive-packet target therefore stops at a global gate.
Stronger arithmetic naturalness and all T3 objects remain unestablished.

## 1. Identity, question and exact lineage

The sole definition is the original [card](candidate-card.md), based
on the definition-only [308 frontier](../308-divisor-product-radix-flow/evidence/scout-record.md).
Input locks, actual access and review history are in [evidence](evidence/README.md).
No old theorem, clock, geometric lift or Route coordinate transfers.

| Item | Same-object owner | Boundary |
| --- | --- | --- |
| Carrier | Y=positive-integer pairs x [0,1], full standard Borel structure | No selected roots, seeds or conull deletion |
| Measure | Counting roots x (interior Lebesgue + delta_0 + delta_1) | Endpoint masses are frozen input |
| Arithmetic/source | j=floor(b*x), d=gcd(a,j), e=a/d, T=(b,d,1-x^e) | Current real/integer feedback |
| Coding | Actual digit j and its half-open cell | Not a separate shift |
| Clock | Own inverse IMAGE; interior derivative and endpoint mass ratio | One fixed all-point prescription |
| Time/packets | Actual retained-lag real extension on ALL Y x R | Full isotropy/time equivalence |
| Classical geometry | Symplectic base, positive roof and mapping torus | NOT APPLICABLE |
| Analytic/later owner | No zeta, trace, determinant or quantum object | T3 NOT SUPPLIED / NOT PURSUED |
| Controls | POWER-OFF, COMPLEMENT-OFF, ROOT-SWAP | Each is its own changed source |

The [prior-work arrow](../../docs/prior_work/README.md) retained here is
divisor admissibility -> current common content -> factor quotient
acting on a real variable -> next integer/real feedback.
Writing P_r(x)=x^r, the exact factor interface is

    a=d*e, P_a=P_e composed with P_d.

Indeed (x^d)^e=x^(d*e) on the entire interval, including
both endpoints. The actual source uses P_e and carries d
to the next root. The complement 1-x is a declared,
prime-independent geometric operation; arithmetic does not force it.
Probe partition, update order and layered measure are also designs.
No Logistic/Henon conjugacy or conservative/symplectic realization follows.

Question: can this source own a positive-time return once all
roots, seeds and atoms remain? A nonzero local clock is
not enough. No prime selector, prime/zero table, per-prime parameter,
fit or inserted roof is permitted. Strong naturalness stays OPEN.

## 2. Every source branch and complete inverse enumeration

For every (a,b,x), let j=floor(b*x), d=gcd(a,j),
e=a/d, with gcd(a,0)=a. The total action is

    T(a,b,x)=(b,d,1-x^e).

The digit cells are I_(b,j)=[j/b,(j+1)/b) for j<b,
and I_(b,b)={1}. Thus x=0 uses j=0 and x=1
uses j=b. No point is terminal. Every positive-root/unit case
uses these same formulas; exponent e is a positive integer.

On U_(a,b,j)={(a,b)} x I_(b,j), the exact target is

    V_(a,b,j)={(b,d)} x (1-((j+1)/b)^e,1-(j/b)^e] for j<b,
    V_(a,b,b)={(b,d)} x {0}.

Strict decrease of 1-x^e on [0,1] and its unique
nonnegative inverse prove these half-open domains and bijections:

    I_(a,b,j)(b,d,y)=(a,b,(1-y)^(1/e)), y in V.

At target (B,D,y), enumerate ALL A>=1 and j=0,...,B
with gcd(A,j)=D; use e=A/D and retain the inverse
precisely when (1-y)^(1/e) lies in I_(B,j). Any
predecessor must satisfy these equations, and each retained one
substitutes back correctly. Actual digits prevent double counting of
one state, while different predecessors on overlapping targets remain.

For completeness, the exact image in a target root (B,D)
has the following explicit real set W_(B,D):

    (1-1/B,1]
    union over 1<=k<=floor((B-1)/D), e>=1, gcd(e,k)=1 of
        (1-((D*k+1)/B)^e,1-(D*k/B)^e]
    union {0} if D divides B.

The first interval comes from j=0, forcing A=D and
e=1. Interior positive digits have j=D*k, A=D*e
and exactly gcd(e,k)=1. The endpoint digit j=B has
gcd(A,B)=D, possible precisely when D|B, and maps to
zero. Thus this union is both necessary and sufficient.
In particular (1,2,0) is missing: total does not mean onto.

The map is Borel and countable-to-one. It is not globally
continuous in the ordinary topology: at root (2,2), approaching
x=1/2 from below gives next root (2,2), while the
cut itself has next root (2,1). No etale or local-
homeomorphism category is assumed.

## 3. Layered IMAGE and the full real-time owner

### 3.1 Interior, atoms and pointwise values

Interior points map to interior points, and endpoints map to
endpoints. For theta_e(y)=(1-y)^(1/e), ordinary monotone
substitution gives on 0<y<1

    J_I(y)=(1/e)*(1-y)^(1/e-1).

It is finite and strictly positive at every retained interior
point. At an endpoint in this inverse's domain, the inverse
and target atoms both have unit mass, hence J_I=1.
For any Borel E in the exact target, split it into
interior and endpoint parts. Substitution proves IMAGE on the first;
the actual atomic ratios prove it on the second. Summing gives

    mu(I(E))=integral_E J_I dmu, EVERY Borel E subset V.

An interior derivative at an endpoint would be wrong in general:
(2,1,1) maps to (1,1,0) with e=2. The inverse
derivative at zero would be 1/2, but the actual atomic
IMAGE is 1. This is not an adjustable clock convention.
At internal null cut points we use the frozen analytic branch
value, not an a.e.-uniqueness claim or a global derivative of T.

Define the actual forward IMAGE factor by

    rho(a,b,x)=e*x^(e-1) if 0<x<1; rho=1 if x=0 or 1.

It is positive finite everywhere and satisfies J_I(Tz)=1/rho(z).
The inverse-arrow clock kappa(z)=log rho(z) is not identically
zero: at (2,2,3/4), it is log(3/2). No derivative
is substituted for an endpoint atom, and no whole-cell ratio
replaces the nonconstant interior density.

### 3.2 Retained lag, branch pairs and complete time

Use G={(z,m-k,w):T^m z=T^k w}, source w and range z.
Every iterate exists. Borel equalities of iterates give a Borel
subset of Y x Z x Y; countable finite-iterate fibres
give countable source fibres. Actual history alignment proves groupoid
composition, without free power maps, extra histories or a germ quotient.

Let D_m(z)=product_(i<m) rho(T^i z), with D_0=1.
On an actual branch pair from w to z, the IMAGE
and its clock are

    J(z,m-k,w)=D_k(w)/D_m(z),
    c(z,m-k,w)=log D_m(z)-log D_k(w).

Finite chain rules prove the interior statement. Endpoint histories
remain in the atomic stratum, where every factor is one.
These exhaust the strata: equal forward endpoints cannot match an
interior history. Borel restrictions and internal null intersections
use the same prescribed factors. Presentations of a triple differ
by common future steps, whose factors cancel pointwise; aligning
middle histories likewise proves multiplicativity and cocycle additivity.
This is branchwise IMAGE, not global invariance of mu under T.

All extension objects Y x R remain, with arrows
(w,h)->(z,h+c). Translation h->h+t is complete, jointly
Borel and commutes with arrows. Only set-level quotient time is
claimed; no coarse quotient topology, trace or analytic owner is supplied.

## 4. Global root descent, every periodic core and every time group

### 4.1 Every state reaches a core in finite time

Set P(a,b,x)=a*b, a positive integer. Its exact update is

    P(Tz)=b*d=P(z)/e <= P(z).

Every step with e>1 strictly lowers P. A nonincreasing
positive-integer sequence has only finitely many strict drops, so
along EVERY full orbit there is a finite index after which
e=1 always. This is eventual stabilization, not a uniform
bound on the time of the last drop.

Thereafter d=a and T acts as

    (a,b,x)->(b,a,1-x).

The next step also has e=1, so two steps return
the full state. Every state is therefore eventually periodic,
with least eventual source period either one or two.

### 4.2 Exact core set, fixed point and phases

Every periodic orbit has constant P and therefore e=1 at
every phase. The COMPLETE periodic-core set is

    R={(a,b,x): a divides floor(b*x),
                 b divides floor(a*(1-x))}.

Necessity follows from the first two phases with exponent one.
Conversely these conditions make both successive gcds equal their
first roots; hence T^2z=z and the conditions repeat.
This is an exact condition on ALL real seeds, not an
interior-only or selected-centre test. Equivalently its (a,b) fibre
is the union of I_(b,k*a) intersected with 1-I_(a,l*b)
over integers k,l>=0 with k*a<=b and l*b<=a, using
the original half-open cells and singleton endpoint cells.

At x=0 the condition is b|a; at x=1 it is
a|b. Thus, for every b|a, (a,b,0) and (b,a,1)
are phases of ONE endpoint two-cycle. No endpoint is discarded.
The interior conditions also retain full families, for example both
roots involving 1 permit the corresponding interior two-phase cycles.

A fixed point must have a=b=n and x=1/2. For
n>=2, floor(n/2) is strictly between 0 and n and
cannot be divisible by n. For n=1 it is zero.
Thus the UNIQUE full fixed point is o=(1,1,1/2).
Every other point of R has least source period two.
Two periodic cores tail-merge exactly when they are phases of
the same one- or two-cycle: intersecting deterministic finite cycles
coincide. Distinct cycles are not merged by equal roots or clocks.

### 4.3 ALL isotropy and explicit transient cancellation

On R, rho=1 both in the interior (e=1) and
at the atoms. Every core clock is therefore zero. For
any state z, finite-history conjugation identifies its isotropy-clock
image with that of its eventual core. Consequently

    H_z={0}, for EVERY z in Y.

More precisely, let r(z)=1 if its eventual core is o,
and r(z)=2 otherwise. Actual equalities of iterates give literal
source isotropy r(z) Z. Every such lag has zero clock,
so extension fixed-object isotropy is also r(z) Z, not trivial.
This holds even at transient points: recurrence of their tails
supplies isotropy although the initial point itself need not be periodic.

In fact o has no other preimage. A predecessor of (1,1,1/2)
has second root 1 and an interior seed, hence j=0,
d=A=1, e=1 and seed 1/2. Thus r(z)=1 only
at o; EVERY other state has source/extension isotropy 2Z.

The entire cocycle has an explicit Borel coboundary. Let N(z)
be the first entrance time into R; it is finite everywhere
and Borel because R is Borel. Put

    B(z)=sum_(0<=i<N(z)) kappa(T^i z), with empty sum 0.

Then kappa(z)=B(z)-B(Tz), since kappa vanishes on R.
Finite sums telescope along any actual branch pair to

    c(z,m-k,w)=B(z)-B(w).

This derives transient cancellation for the FROZEN clock; it does
not replace the clock or claim that every branch value is zero.
In particular the earlier log(3/2) example remains nonzero.

No H_z has a positive generator. Thus NO positive primitive
time packet exists anywhere in this full owner, despite extensive
source recurrence. This is a global return theorem, not an
inference from a finite fixed-point list or numerical period cutoff.

## 5. Three changed owners and their exact controls

### 5.1 POWER-OFF

Retain j,d and the root update but use real output 1-x.
Its exact target for j<b is
(1-(j+1)/b,1-j/b], and for j=b is {0}, at
root (b,d). Inverse real coordinate is 1-y; enumerate ALL
A,j with gcd(A,j)=D and require 1-y in I_(B,j).
Interior derivative and endpoint atomic ratio both give IMAGE 1.
Thus its entire clock is zero and ALL H vanish.

Its own P update is still b*d<=a*b. Stabilization forces
d=a, so every state eventually reaches its own one- or
two-cycle. Its complete periodic set is exactly R, derived
anew from the two control phases; its fixed point is o.
Source/extension isotropy is Z or 2Z according to the actual
control eventual core. Basins are not transferred from the main
power action merely because their periodic sets coincide.
Here the same direct predecessor check also gives only o
in its fixed-point basin; all other source/extension groups are 2Z.

### 5.2 COMPLEMENT-OFF

Retain j,d,e but use real output x^e. Its branch
target for j<b is [(j/b)^e,((j+1)/b)^e), and
for j=b is {1}, at root (b,d). Inverse is
y^(1/e), enumerated with its OWN cell condition. Its interior
IMAGE is (1/e)*y^(1/e-1); at endpoint atoms it is 1.
Splitting any Borel set into these strata proves the full law.

The actual root product again descends, and its eventual e=1
action is (a,b,x)->(b,a,x). Hence every state eventually
has period one or two. Its COMPLETE periodic set is

    R_plus={(a,b,x): a divides floor(b*x), b divides floor(a*x)}.

Its ALL fixed points are (n,n,x) with
x in [0,1/n) union {1}, including every x in
[0,1] at n=1. Other points of R_plus have least
source period two. Its own core IMAGE is one, so
ALL H are zero and source/extension isotropy is the same
literal Z or 2Z at each state's actual eventual core.
No main complement itinerary or basin has been imported.

Its period-one basin can also be stated exactly: ALL x=1
states, together with the already fixed (n,n,x<1/n).
An x=1 state reaches (g,g,1), g=gcd(a,b), within
two steps. A predecessor of an interior or zero fixed seed
at root (n,n) must have j<n divisible by n, hence
j=0 and A=n; its only preimage is itself. Therefore
source/extension isotropy is Z exactly on this stated basin,
and 2Z everywhere else. ALL time images remain zero.

### 5.3 ROOT-SWAP

Retain j,d,e and real output 1-x^e, but update
roots to (b,a). The real branch target intervals are the
same formula as Section 2, now at root (b,a), not (b,d).
At target (B,A,y), enumerate EVERY j=0,...,B with
e=A/gcd(A,j), and retain inverse (A,B,(1-y)^(1/e))
only when its seed belongs to I_(B,j). These are ALL
predecessors. Interior inverse derivative and endpoint mass ratios
give its OWN layered IMAGE and actual-history cocycle. Main
root descent does not hold for this changed update.

In the full tested root (2,2), digit j=0 uses e=1
on [0,1/2), whose putative fixed seed 1/2 is excluded.
Digit j=1 uses e=2 on [1/2,1); solving x=1-x^2
gives the unique admissible fixed seed

    gamma=(sqrt(5)-1)/2, with 1/2<gamma<1.

The other quadratic root is negative. Digit j=2 is the
endpoint 1, mapped to zero, and zero maps to one.
These endpoints are not fixed. Thus gamma is the ONLY
full fixed seed in this complete root fibre.

At that interior state the actual forward IMAGE is 2*gamma,
so source isotropy is Z and

    H=log(sqrt(5)-1) Z, least L=log(sqrt(5)-1)>0,
    extension isotropy={0}.

Full finite-preimage attachments preserve this constant core's isotropy
image and cannot supply a shorter lag. This is a genuine
positive control packet. Its time is below log 2 and is
not a rescue of the main prime-time target. No global
periodic ledger is claimed for ROOT-SWAP. The contrast isolates
root descent, not absence of nontrivial power geometry.

## 6. Gate assessment, limits and portfolio decision

| Gate | Evidence for CPC01 | Scope |
| --- | --- | --- |
| T0 | Full total Borel source, complete inverses, layered IMAGE and real extension | Not onto or ordinary continuous; no etale claim |
| T1 | Actual content/power feedback owns a nonconstant local clock | Strong arithmetic naturalness OPEN |
| T2 | EVERY state eventually has source period 1 or 2; ALL H=0 | Global positive-packet absence, not absence of source recurrence |
| T3 | NOT SUPPLIED / NOT PURSUED | No borrowed analytic owner |
| Classical/formal | A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED | No geometric lift or Route credit |

Portfolio: **stop positive-prime-time promotion; retain the layered owner
and global descent obstruction; fork a different architecture**. No
high-period numerical search is needed after this structural gate.
The controls are separately owned, not repairs. They do not
force the chosen probe, complement or measure, and prove no
arbitrary-data encoding theorem. This is not a universal no-go
for nonmonotone arithmetic feedback or the positive 304 result.

## Reproduction and AI-assisted review disclosure

All inputs are the frozen formulas, full carrier and measure.
Proof methods are inverse substitution, stratified change of variables,
integer descent, exact two-phase conditions and cocycle telescoping.
No scientific numerical command, precision/cutoff, external literature lemma,
prime table or zero data is used. See [claim ledger](claim-ledger.md),
[evidence/locks](evidence/README.md), [internal review](evidence/independent-review.md),
[source/frontier record](evidence/scout-record.md) and [package index](README.md).
ARS raw-card, synthesis and final-adverse review is native inherited-
model/shared-context AI-assisted scrutiny, not external peer review,
independent-error evidence or formal verification; no venue calibration.
Same-object ledger intact. Old packages, mirrors and Phase-I sources
unchanged; 241/242 paused; goal active. Markdown only; no publication,
upload or Git commit.
