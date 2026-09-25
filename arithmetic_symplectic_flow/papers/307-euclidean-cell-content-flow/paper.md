# Euclidean content feedback cannot have finite positive packet multiplicity

Paper ID: `307-euclidean-cell-content-flow`.
Candidate ID: `ANG-20260920-ECC01`. Date: 2026-09-20.
Status: `OWNED CONTENT CLOCK; RADIAL PACKET-MULTIPLICITY OBSTRUCTION — STOP / FORK`.
Route state: broadened owner audit; classical A0/A1/A2 NOT APPLICABLE;
formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

The complete real plane selects a current integer pair by absolute
integer cells. A canonical Bezout basis operation and common-content
normalization act on that same real vector. All branches, quadrants,
axes and boundaries remain. Exact inverse branches own Lebesgue IMAGE
factor d, the current gcd, and a full Borel clock. All fixed
states and the entire unit-cell staying set have zero time but
nontrivial source isotropy. More decisively, every nonzero finite
periodic itinerary admits a continuum of positive radial dilations
with identical cells, least period and clock, even from included
integer boundaries. Their finite cycles cannot be tail-equivalent
because their maximum norms differ. Hence any positive primitive
packet, if one exists, occurs with continuum multiplicity at its
same time. This rules out a nonempty finite-multiplicity prime
ledger without claiming existence or absence of positive returns.
Three separately owned controls expose normalization and basis-choice
dependence. The candidate stops at this structural multiplicity gate.

## 1. Frozen owner and arithmetic-symbolic lineage

The [original card](candidate-card.md) fixes Y=R^2 and ordinary
two-dimensional Lebesgue measure. At z=(u,v) put

    a=1+floor(abs(u)), b=1+floor(abs(v)),
    d=gcd(a,b), alpha=a/d, beta=b/d.

If beta=1 use s=0,t=1. Otherwise choose the unique
0<=s<beta with s*alpha=1 mod beta, and set
t=(1-s*alpha)/beta. Define

    E=[[s,t],[-beta,alpha]], C=diag(1/d,1)*E,
    T(u,v)=((s*u+t*v)/d,-beta*u+alpha*v).

| Field | Same frozen owner | Scope |
| --- | --- | --- |
| Carrier/measure | ALL R^2, ordinary Lebesgue | All signs, axes, origin and boundaries |
| Source | Current integer-cell pair, gcd and canonical Bezout coefficients | No separate integer root, prime predicate or external schedule |
| Action | Current C acts on the actual real vector | Updated vector supplies next cell |
| Groupoid | Full actual retained-lag Borel tail relation | No all-matrix action, germ quotient or selected histories |
| Clock | Actual inverse IMAGE, frozen branch constants at every point | No roof/runtime or inserted prime time |
| Packets | Full isotropy image and actual tail/time equivalence | No radial quotient or chosen centre |
| Symplectic suspension / Hamiltonian owner | NOT APPLICABLE / NOT SUPPLIED | No conservative-lift credit |
| Trace / zeta / operator | NOT SUPPLIED / NOT PURSUED | No T3 or formal Route evaluation |

The exact [prior-work arrow](../../docs/prior_work/README.md) is divisor
admissibility -> common divisor of a current integer pair ->
primitive pair and content -> the SAME Euclidean basis operation
on the real state -> real feedback. This is a specified ANG
symbolic deformation, not a Logistic/Henon conjugacy. Cell readout,
Bezout convention, normalization order and measure remain designs.

## 2. Integer interface, complete branches and category

The primitive pair alpha,beta is coprime. Bezout's identity from
the Euclidean algorithm makes alpha invertible modulo beta; reducing
its inverse gives exactly one s in the specified range. The
beta=1 convention also satisfies s*alpha+t*beta=1. Therefore

    det E=1, E*(a,b)=(d,0), C*(a,b)=(1,0).

This verifies the intended integer basis/content operation. The
representative (a,b) is NOT the actual real point (u,v), and
need not belong to its own cell; the same matrix acts on
both, not an asserted identity between their trajectories.

Let B_n={r:n-1<=abs(r)<n}, B_1=(-1,1). The disjoint Borel
cells U_(a,b)=B_a x B_b partition the whole plane. Every
point gets finite, well-defined coefficients, so T is total Borel.
Since det C=1/d, each linear branch is invertible, with

    I_(a,b)(r,w)=(a*r-t*w,b*r+s*w),
    V_(a,b)={(r,w):a*r-t*w in B_a,b*r+s*w in B_b}.

Direct substitution using a=d*alpha,b=d*beta verifies both directions.
Every predecessor has one unique current cell and occurs in this
enumeration; distinct predecessors over overlapping targets remain.
The exact full image is union_(a,b) V_(a,b), and T is
countable-to-one, as are its iterates.

It is NOT onto. A predecessor of (r,w)=(1,0) would
be (a,b), but a is excluded from B_a and b from B_b.
In fact no (r,0) with abs(r)>=1 has a predecessor.
All such points nevertheless remain in the total forward action.

T is also not continuous in the usual plane topology. At
(1,1/2), the cell is (a,b)=(2,1) and T=(1/2,0).
Approaching from (1-epsilon,1/2), epsilon>0 small, uses the
unit cell and images tending to (1/2,-1/2). No boundary
deletion or retopologization is performed. On d>1 branches the
area determinant is 1/d, not one; this is not a symplectic
base map. Its appropriate owner here is countable Borel.

## 3. Own IMAGE clock and full real extension

Each B_n has length two, hence mu(U_(a,b))=4 and
mu(V_(a,b))=4/d. More importantly, the inverse linear map has
determinant a*s+b*t=d, so for EVERY Borel A subset V_(a,b),

    mu(I_(a,b)(A))=d*mu(A), J_(a,b)=d, kappa=-log d.

The whole-set ratio agrees, but linear change of variables proves
the all-Borel statement. The frozen prescription uses this same
constant at included boundaries/null states; it is not uniqueness
deduced from an a.e. Radon–Nikodym class. Branchwise IMAGE is
not global invariance of a many-to-one T.

Let P_m(z) be the product of actual gcd values along m
steps, P_0=1. The full actual tail groupoid is

    G={(z,m-k,w):T^m z=T^k w,m,k>=0}.

It is Borel as a countable union of equalizers at each lag,
and has countable source/range fibres by the inverse enumeration.
On finite branch pairs the inverse IMAGE and clock are

    J_(z,m-k,w)=P_m(z)/P_k(w),
    c(z,m-k,w)=log P_k(w)-log P_m(z).

Common future products cancel between two presentations of the same
triple; alignment of actual histories also proves additivity. T
is total, so needed common extensions are defined. This pointwise
argument and the branch prescription retain null intersections without
assigning extra arrows or clocks. No free matrix words are added.

On ALL Y x R_h, an arrow w->z changes h by c.
Translation h->h+tau is jointly Borel, complete for every real
tau and commutes with arrows. Only its set-level action on
orbit classes is claimed. Coarse Hausdorffness, standard-Borel quotient
and embedded classical circles are not established. As frozen,
H_z=c(G_z^z), and extension fixed-object isotropy is ker c.

## 4. ALL fixed states and the whole unit-cell staying set

### 4.1 Complete fixed locus

The origin is fixed in cell (1,1). If z!=0 is fixed
in cell (a,b), C must have eigenvalue one. Since its
trace is s/d+alpha and determinant 1/d, this requires

    s+a=d+1.

Here a is a positive multiple of d and s>=0. Either
a=d,s=1, or a=d+1,s=0. In the first case alpha=1;
s=1 requires beta>1, giving t=0. The second coordinate
fixed equation forces u=0, whose cell requires a=1. Thus
d=1 and b>=2, giving precisely (0,v) with abs(v)>=1.
In the second case d divides both a and a-1, so d=1,
a=2. The convention s=0 forces beta=1 and b=1.
The eigenline is u=v, incompatible with B_2 x B_1.
There are no other cases. Consequently

    Fix(T)={(0,0)} union {(0,v):abs(v)>=1}.

All these states have d=1 throughout their constant histories,
source isotropy Z, H=0 and extension isotropy Z. Different
fixed states cannot merge by full tails. Zero time does not
erase these genuine source returns or the boundary points v=+/-1.

### 4.2 Every orbit staying in the unit cell

On U_(1,1)=(-1,1)^2, T equals R(u,v)=(v,v-u).
Its six successive phase vectors are

    (u,v), (v,v-u), (v-u,-u),
    (-u,-v), (-v,u-v), (u-v,u), then (u,v).

Thus the EXACT set whose whole forward orbit stays in that
cell is the open hexagon

    Q={abs(u)<1,abs(v)<1,abs(v-u)<1}.

Necessity follows already from the first two steps, and the
listed six vectors prove sufficiency. R has primitive sixth roots
of unity as eigenvalues, so R^j-I is invertible for
1<=j<6. Every nonzero state of Q has least source period
6, retained-lag isotropy 6Z, H=0 and extension isotropy 6Z.
The origin instead has period one and isotropy Z. Boundaries
of Q are not discarded; they simply fail the stated staying
condition and remain in the full plane action.

## 5. Structural obstruction for EVERY possible positive packet

### 5.1 Radial preservation, including integer boundaries

Let z_0,...,z_(q-1) be any nonzero periodic orbit of least
period q, with its actual cells (a_i,b_i). Because T(0)=0,
none of its phase vectors is zero. For every positive absolute
coordinate xi of these finitely many vectors, its cell bound is

    n-1<=xi<n.

There is epsilon>0 with (1+epsilon)*xi<n simultaneously for
all such coordinates. For 1<=lambda<=1+epsilon, lower bounds
remain satisfied and the upper strict bounds remain strict. Zero
coordinates stay in their unit cells. This includes xi=n-1
at an INCLUDED integer boundary; no generic-interior assumption enters.

Every lambda*z_i therefore has the SAME cell as z_i.
Linearity within that cell gives inductively

    T^i(lambda*z_0)=lambda*z_i, 0<=i<=q.

The least period is still q: an earlier equality would divide
by lambda>0 and contradict the original least period. The gcd
sequence and its product D=product_(i<q) d_i are identical.

### 5.2 Full packet identity does not remove the continuum

At a pure q-periodic state source isotropy is qZ. The
generator q has clock -log D, so

    D=1: H=0, extension isotropy qZ;
    D>1: H=(log D)Z, extension isotropy 0.

In the latter case log D is the least positive time;
smaller factors of D are not automatically shorter isotropy lags.
Repetitions are r log D on that SAME packet.

If two radial copies were full-tail equivalent, their periodic
cycles would be the same finite set: intersecting deterministic
cycles coincide. Let M=max_i norm(z_i)>0. The two finite
cycles have maximum norms lambda*M and lambda'*M, so equality
forces lambda=lambda'. Finite inverse excursions do not evade
this test because their composition is still a full-tail arrow.
Different positive lambda thus give distinct source cycles and
distinct time packets, all with the SAME primitive time log D.
There are continuum many lambda in the indicated interval.

Finally, nontrivial source isotropy at any state means equality
of two distinct forward iterates, hence eventual arrival at a
finite periodic core. Its isotropy-clock image agrees with that
core by conjugating through the actual finite-history arrow; clock
values of that arrow and its inverse cancel. The origin core
has zero time. Thus EVERY positive primitive packet must reduce
to a nonzero periodic core with D>1, and the radial result
applies. No other kind of positive isotropy packet is missed.

### 5.3 Precise decision, not a fabricated existence claim

We have proved the dichotomy:

    either there are no positive primitive time packets,
    or EVERY occurring positive primitive time has continuum multiplicity.

Accordingly this owner cannot realize a nonempty finite-multiplicity
prime ledger. In particular, even a putative time log p would
have continuum many packets, not one. We have NOT established
which side of the dichotomy occurs, nor exhibited a D>1
periodic orbit. That existence question remains OPEN / NOT PURSUED
because either side already fails the frozen multiplicity gate.
This is a structural obstruction on the full carrier, not a
finite orbit table, selected-centre computation or radial quotient.

## 6. Three independently owned controls

CONTENT-OFF uses E without the first-coordinate normalization. Its
complete inverse is (alpha*r-t*w,beta*r+s*w), on exactly the
target set where those coordinates lie in B_a x B_b.
Its own determinant/IMAGE is one; the entire cocycle and ALL
H vanish. The unit-cell action is still R, so its complete
staying set is Q, with source/extension 6Z at nonzero states
and Z at the origin. Other source returns are not classified.

BEZOUT-SHIFT uses s'=s+beta,t'=t-alpha. The identity
s'*alpha+t'*beta=1 still holds; its integer representative still
maps to (1,0) after normalization. Its complete inverse is
(a*r-t'*w,b*r+s'*w), on its OWN cell-membership target.
The inverse IMAGE remains d and its own history cocycle uses
its actual, potentially different gcd itinerary. Equal branch IMAGE
does not identify the actions. In the unit cell this map is
(u,v)->(u,v-u): its fixed states there are ALL (0,v),
abs(v)<1, with source/extension Z and zero H. They are
also the entire unit-cell staying set, because v-k*u eventually
leaves the cell when u!=0. The main hexagon's six-cycles
are not transferred to this comparator.

UNIT-MATRIX uses R on the ENTIRE plane. Its inverse is
(r-w,r), own IMAGE one and full cocycle zero. All nonzero
states have least source period six, source/extension 6Z and
H=0; the origin is fixed with source/extension Z. These
are its ALL fixed/periodic states and ALL time groups, not
a disk restriction or an inherited arithmetic mechanism.

## 7. Gate assessment and handoff

| Gate | Same-owner evidence | Status / limit |
| --- | --- | --- |
| T0 | Exact integer interface, all total Borel branches and retained-lag groupoid | ESTABLISHED; not onto, continuous or symplectic |
| T1 | Actual inverse IMAGE d, derived from the same real basis/content action | Owned engineering clock; stronger naturalness OPEN |
| T2 | All fixed/unit-staying returns; radial obstruction for EVERY positive packet | Finite positive multiplicity IMPOSSIBLE; positive-return existence OPEN |
| T3 | No trace, zeta or operator supplied | NOT PURSUED after structural stop |
| Classical / formal | No classical suspension or formal evaluation | A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED |

Portfolio: **stop finite-multiplicity prime-time promotion; retain the
structural radial obstruction; fork a genuinely different source**.
The arithmetic basis operation and same-object clock are real
positive ownership results, but they do not remove the continuum
of actual scaled cycles. Selecting representatives or adding a
radial quotient changes the object. No such repair is made.
The conclusion concerns this frozen action/cell/packet structure,
not all nonlinear arithmetic dynamics or all geometric carriers.

## Reproducibility and internal review

All statements use exact linear algebra, cell inequalities and
full-tail arguments, with no scientific numerical run, period cutoff,
precision parameter, prime/zero data or external literature premise.
The [evidence index](evidence/README.md) binds the card, paper,
[claim ledger](claim-ledger.md) and [internal review](evidence/independent-review.md).
The [package index](README.md) and [source/frontier record](evidence/scout-record.md)
separate this result from any unadmitted next definition. AI-assisted
native ARS raw-card, manuscript and adverse checks use inherited-model/
shared-context limits, not external peer review or independent-error
evidence. Old packages/mirrors unchanged; 241/242 paused; programme
goal active. Markdown only; no staging, commit, upload or publication.
