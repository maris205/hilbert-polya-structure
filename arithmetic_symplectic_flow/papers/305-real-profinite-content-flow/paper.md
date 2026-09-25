# Diagonal content feedback has an owned zero joint clock

Paper ID: `305-real-profinite-content-flow`.
Candidate ID: `ANG-20260920-RPC01`. Date: 2026-09-20.
Status: `OWNED BOREL FEEDBACK; JOINT IMAGE CLOCK ZERO — STOP / FORK`.
Route state: broadened owner audit; classical A0/A1/A2 NOT APPLICABLE;
formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

The entire real–profinite product carries a current-state integer-cell
and residue rule. Their gcd divides both coordinates after the same
translation, and the new real coordinate selects the next cell.
All inverse branches, boundary points and noninteger profinite states
are retained. The action is total Borel and countable-to-one but
not onto or continuous in the usual product topology. Each actual
inverse has real IMAGE factor d and finite Haar factor 1/d,
so its joint IMAGE is exactly one on every Borel subset.
The frozen all-point branch prescription therefore gives zero clock
on the full retained-lag groupoid. Every time group is trivial:
no positive primitive time packet exists, irrespective of unclassified
higher source returns. All fixed points nevertheless form the full
unit strip, with nontrivial source and extension isotropy. Three
separately owned controls isolate the cancellation and preserve the
distinction between zero time and absence of recurrence.

## 1. Frozen identity and question

The [original card](candidate-card.md) freezes the definition before
this proof. The first question is whether a common arithmetic
content quotient produces a nondegenerate clock for the SAME
real–profinite action and product measure. No clock from either
factor alone is eligible as the joint clock.

| Field | Exact owner | Scope |
| --- | --- | --- |
| Carrier | Y=R x K, K the profinite completion of Z | ALL real signs/endpoints and ALL profinite states |
| Measure | mu=real Lebesgue x normalized additive Haar nu | Full support, sigma-finite; not a real probability |
| Source | n=1+floor(abs(r)), j=x mod n, d=gcd(n,j) | Current-state arithmetic; gcd(n,0)=n |
| Action | T(r,x)=((r-j)/d,(x-j)/d) | Same affine operation on both coordinates |
| Groupoid | All actual tail triples with lag retained | Countable Borel category, not imported LCH etale topology |
| Time | Own inverse IMAGE prescription and full real extension | No roof, runtime, selected history or conull restriction |
| Packets | H_z=c(G_z^z), actual full tail/time equivalence | Positive primitive means a least positive generator |
| Classical symplectic / mapping torus / Hamiltonian owner | NOT APPLICABLE / NOT SUPPLIED | No geometric lift theorem |
| Trace / zeta / determinant / operator | NOT SUPPLIED / NOT PURSUED | No T3 or Route credit |

The [prior-work arrow](../../docs/prior_work/README.md) is proper-divisor/
gcd prime-composite observables -> current cell/residue admissibility
-> common-content quotient on both coordinates -> real feedback.
This is a specified arithmetic-symbolic deformation, not a prime
subshift, a Logistic/Henon conjugacy or a generic arithmetic-space
label. The real coordinate does affect future branch selection.
Necessity of the cell readout, gcd operation and measure remains OPEN.

## 2. Elementary finite-coordinate ownership

K is the inverse limit of Z/qZ over divisibility. Integers are
dense: every finite compatible residue condition has an integer
representative. For every m>=1, the closed subgroup mK is exactly
the kernel of reduction modulo m and has m cosets. To see the
kernel equality, approximate any point in that kernel by integers
in the same residue condition modulo a common multiple of m and
each test modulus. These representatives are multiples of m; the
compact image mK contains their limit.

Multiplication by m is injective: if mx=0, reduction modulo mq
implies x=0 modulo q for every q. It is thus a homeomorphism
from K onto mK. The quotient of an element of mK is unique.
Translation invariance and total mass one give nu(mK)=1/m.
More generally,

    nu(mE)=nu(E)/m, EVERY Borel E subset K.

One direct verification starts with a residue cylinder a+qK:
its image ma+mqK has mass 1/(mq), compared with 1/q.
The cylinder algebra generates the Borel sets of K; uniqueness
of finite measures extends the identity to every Borel E.
No prime decomposition, prime table or place-selected normalization
is needed for this finite-coordinate scaling law.

At a main-source state x=j+n y, d divides n and j.
Consequently (x-j)/d=(n/d)y is uniquely in K. The rule T is
therefore defined on ALL Y, including n=1, zero and endpoints.

## 3. Complete Borel branches and non-surjectivity

Let B_n={r:n-1<=abs(r)<n}, with B_1=(-1,1).
These Borel cells partition R and each has Lebesgue length two;
for n>=2 the two half-open components have opposite endpoint
inclusions. For 0<=j<n set d=gcd(n,j). The disjoint domain
pieces and exact target pieces are

    U_(n,j)=B_n x (j+nK),
    V_(n,j)=((B_n-j)/d) x ((n/d)K).

On U_(n,j), T is a Borel bijection onto V_(n,j), with inverse

    I_(n,j)(u,y)=(d*u+j,d*y+j).

Substitution and n(r), j=x mod n verify both directions. Every
predecessor has exactly one current n,j and is captured; different
predecessors over overlapping targets remain distinct. This proves
the exact image T(Y)=union_(n,j) V_(n,j), and countably many
possible predecessors at each target. It does not prove onto Y.

Indeed (u,y)=(1,1) has no predecessor. Membership of y=1 in
(n/d)K forces n/d=1, so d=n and j=0. But B_n/n has
abs(u)<1, excluding u=1. The map is therefore NOT onto.
There are no terminal domain states; a state with no predecessor
still has its own forward image.

Nor is T continuous in the usual product topology. Points
(1-1/k,0), k>=2, lie in the unit cell and are unchanged.
Their images tend to (1,0), whereas T(1,0)=(1/2,0).
The Borel category is essential to this frozen formulation; no
endpoint deletion or alternative topology is used to repair it.

Y is a standard-Borel space: R and the compact metrizable
countable inverse limit K are Polish. T is Borel by its countable
Borel branch partition. The product measure is full support and
sigma-finite, locally finite in the product topology.

## 4. Joint IMAGE cancellation on every Borel set

Write h=n/d. The whole branch masses are

    mu(U_(n,j))=2/n,
    mu(V_(n,j))=(2/d)*(1/h)=2/n.

They are finite and positive, but their equality alone would not
prove the required IMAGE law. On each product rectangle A x E
inside V_(n,j), the inverse acts by u->d*u+j and y->d*y+j.
Real Lebesgue IMAGE is multiplied by d; the finite-coordinate
law of Section 2 multiplies Haar IMAGE by 1/d. Thus

    mu(I_(n,j)(A x E))=d*(1/d)*mu(A x E)=mu(A x E).

Both measures on V_(n,j) are finite; rectangle generation and
uniqueness extend this identity to EVERY Borel subset. Therefore

    J_(n,j)=1,     kappa(r,x)=0 on every domain branch.

This is exact same-owner cancellation, not a convention borrowed
from a separate real or finite action. Each coordinate's nontrivial
scale is present, and neither may be discarded to recover a
desired nonzero clock.

The card prescribes the same branch constant at all endpoints
and null points. The resulting all-point value is consequently
one there as well. A Radon–Nikodym derivative specified only
almost everywhere would not by itself determine arbitrary null-state
values. We use the frozen affine branch prescription, not an
unproved general uniqueness claim for Borel cocycles.

## 5. Full retained-lag owner and zero positive-time ledger

Use G={(z,m-k,w):T^m z=T^k w,m,k>=0}, source w, range z.
For each lag it is a countable union of Borel equalizer sets.
T and its iterates are countable-to-one by the complete branch
enumeration; source and range fibres of G are therefore countable.
The Borel subspace of Y x Z x Y is a countable Borel groupoid.
Multiplication and inversion are the actual triple operations, with
histories aligned along existing common tails; totality of T makes
all required further iterates available. Identical triples with
different presentations are one arrow, not extra branch labels.

Every finite branch map and inverse is measure-preserving on its
actual domain by Section 4. Their branch pairs therefore have
IMAGE one. The frozen history formula gives

    c(z,m-k,w)=0, ALL arrows of G.

Presentation independence and additivity follow immediately; they
also follow by cancellation of common histories. This is a global
statement, independent of any periodic-point enumeration.

On ALL extension objects Y x R_s, arrows preserve s because
c=0. Translation (z,s)->(z,s+t) is jointly Borel, two-sided
complete and commutes with every arrow. It descends to a set-level
action on orbit classes. No standard-Borel, Hausdorff or continuous
coarse quotient is claimed. For every source state,

    H_z=c(G_z^z)={0},
    extension fixed-object isotropy = G_z^z.

Time translation on orbit classes is free: equivalence preserves
the exact s-coordinate, so a translated class can equal itself
only at t=0. There are NO positive primitive time packets and
hence no positive repetitions. This does not assert trivial source
isotropy, nor require solving its higher-period classes.

## 6. ALL fixed points and retained zero-time isotropy

Every (r,x) with abs(r)<1 has n=1,j=0,d=1 and is fixed.
Conversely suppose n>=2 and T(r,x)=(r,x). If d=1 the real
equation gives j=0, contradicting gcd(n,0)=n>=2. For d>=2
the same equation gives r=-j/(d-1). Since d divides n and
j and 0<=j<n, we have j<=n-d. Hence

    abs(r)<= (n-d)/(d-1) < n-1,

where strictness follows from
(d-1)(n-1)-(n-d)=n(d-2)+1>0. This contradicts r in B_n.
Thus the COMPLETE fixed locus is

    Fix(T)=(-1,1) x K.

Every fixed state has all integer lag isotropy Z, zero time
group and extension fixed-object isotropy Z. Different fixed states
have different constant actual T-tails and cannot merge into one
source orbit. These many zero-time recurrent states remain in the
owner; they are not positive closed-time packets. Nonfixed eventual
returns and higher periods are OPEN / NOT PURSUED after the
decisive global clock stop; every such state's H is already known.

## 7. Separately owned controls

### REAL-OFF: retain the finite scale alone

Keep n,j,d, full Y and mu, but use T_R(r,x)=(r,(x-j)/d).
Its complete inverse family is

    target V_R=B_n x ((n/d)K),
    I_R(u,y)=(u,d*y+j).

These domains must not be replaced by the main V_(n,j).
The own inverse IMAGE is 1/d, so kappa_R=+log d. For an
actual m-step history let D_m be its product of d values.
Own branch-pair IMAGE is D_k(w)/D_m(z), giving
c_R=log D_m(z)-log D_k(w), with valid common-tail cancellation.

EVERY (r,0) is fixed: j=0 and d=n(r). For n>=2,
its source isotropy is Z, H=(log n)Z and extension isotropy
is trivial. These fixed states have distinct actual constant tails,
so changing r does not identify them. Already a single integer
cell supplies continuum many positive log-n packets in this control,
and composite n occur. At n=1 the entire strip, not just
x=0, is fixed, with source/extension Z and H=0. Other
fixed or higher-return states are not classified by this control.
Its positive clock is not a clock for the main joint action.

### FINITE-OFF: retain the real scale alone

Use T_K(r,x)=((r-j)/d,x), still reading n,j from the current
full state. Its complete inverse family is

    target V_K=((B_n-j)/d) x (j+nK),
    I_K(u,y)=(d*u+j,y).

Its own inverse IMAGE is d, hence kappa_K=-log d and
c_K=log D_k(w)-log D_m(z) on actual histories. The unit
strip is fixed with source/extension Z and zero H. The main
fixed-point real-coordinate argument also excludes fixed points
outside that strip. No full higher-return or positive-packet result
is asserted for this changed action. Dropping the finite scale
changes the owner, not just its description.

### CONTENT-OFF: remove common-content division

Use T_0(r,x)=(r-j,x-j), with the same n,j readout. Its
complete inverse family has target (B_n-j) x nK and
I_0(u,y)=(u+j,y+j). Both coordinate actions are translations,
so its OWN IMAGE is one and full cocycle zero: every H=0.
The real fixed equation is exactly j=0, giving ALL fixed states

    {(r,x): x in n(r)K}.

They have source/extension isotropy Z and zero time. Thus removing
content changes the source and its fixed locus, but does not
produce a nonzero joint clock. Null endpoints are retained under
the same branch-prescription rule in every control.

## 8. Gate assessment, limits and decision

| Gate | Established evidence | Decision / limit |
| --- | --- | --- |
| T0 | Total countable-to-one Borel action, all inverses and full retained-lag owner | ESTABLISHED in Borel category; not onto or usual-topology continuous |
| T1 | Same-owner Borel IMAGE factor one on every branch and full zero cocycle | Clock owned; positive arithmetic-time promotion FAILS |
| T2 | ALL H zero and no positive time packet; complete fixed locus and its isotropy | Global positive-packet absence established; higher source returns not pursued |
| T3 | No trace/zeta/operator supplied | NOT PURSUED after clock stop |
| Classical / formal | No symplectic suspension or formal evaluation | A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED |

Portfolio: **stop positive-prime-time promotion; retain the exact
joint-module obstruction; fork to a separately defined source**.
The arithmetic feedback is genuine at the stated design level,
but it cannot overcome the opposite measure scalings of the SAME
diagonal operation. This is not a no-go theorem for all coupled
real/profinite dynamics, arbitrary arithmetic carriers or changed
measures. Strong naturalness remains OPEN, not decided by failure.
No reweighting, omitted coordinate, roof or return restriction repairs
this frozen object. Its ledger remained intact through the stop.

The scope is intentionally clock-first: all Borel sets, real values,
profinite states and branches, not a finite cutoff. The positive
304 theorem remains untouched and supplies no clock or Route credit
here. A later source needs its own card before claims or computations.
See the [source/frontier record](evidence/scout-record.md).

## Reproducibility and internal review

All arguments are exact; no scientific numerical run, precision
parameter, external literature lemma or arithmetic/zero dataset was
used. The [evidence index](evidence/README.md) binds the original
card, exact manuscript, [claim ledger](claim-ledger.md) and
[internal review](evidence/independent-review.md). The [package index](README.md)
gives the scoped handoff. AI-assisted authorship and native ARS
three-checkpoint review use inherited model/shared context, not
external peer review, formal verification or independent-error evidence.
Old packages/mirrors unchanged; 241/242 paused; programme goal active.
Markdown only; no staging, commit, upload or publication.
