# Frozen candidate — Euclidean cell/content feedback

Candidate ID: `ANG-20260920-ECC01`.
Paper ID: `307-euclidean-cell-content-flow`. Date: 2026-09-20.
Version: 1. Initial status: `OPEN — ARITHMETIC INTERFACE, IMAGE AND RETURN MULTIPLICITY`.

## 1. Full real carrier and exact arithmetic operation

Let Y=R^2_(u,v), with standard Borel structure and ordinary
two-dimensional Lebesgue measure mu. Keep all quadrants, axes,
origin and integer-cell boundaries. At the CURRENT real point set

    a=1+floor(abs(u)), b=1+floor(abs(v)),
    d=gcd(a,b), alpha=a/d, beta=b/d.

Choose Bezout coefficients by the exact convention: if beta=1,
s=0,t=1. If beta>1, take the unique 0<=s<beta with
s*alpha=1 mod beta and set t=(1-s*alpha)/beta. Verify
existence/uniqueness from integer arithmetic, not a table. Define

    E_(a,b)=[[s,t],[-beta,alpha]],
    C_(a,b)=diag(1/d,1)*E_(a,b),
    T(u,v)=C_(a,b)*(u,v)=((s*u+t*v)/d,-beta*u+alpha*v).

The intended interface is the SAME Euclidean basis change and
content normalization on the integer representative (a,b) and real
vector (u,v). Prove its exact integer action and distinguish
the representative from the actual state. All unit cases use this
formula. There is no terminal, acceptance, escape/reset or free
matrix branch. Updated real coordinates select the next arithmetic
cell; no independent integer root or external schedule is added.

The precise lineage is prime/composite divisor admissibility -> common
divisor symbol of a current integer pair -> content/primitive pair
-> the SAME basis operation on the real state -> real feedback.
This is an ANG symbolic deformation, not a proved Logistic/Henon
conjugacy, symplectomorphism or conservative lift. Cell readout, Bezout
convention, normalization order and measure remain declared designs.

## 2. Every branch and actual Borel owner

For n>=1 set B_n={r:n-1<=abs(r)<n}, with B_1=(-1,1).
For ALL a,b>=1 propose

    U_(a,b)=B_a x B_b,
    I_(a,b)(r,w)=(a*r-t*w,b*r+s*w),
    V_(a,b)={(r,w):a*r-t*w in B_a,b*r+s*w in B_b}.

Prove each exact inverse/image and the completeness of enumeration
over ALL pairs (a,b). Retain every distinct predecessor on image
overlaps. Determine totality, exact image and whether onto. Half-open
boundaries remain; no usual-topology continuity/local homeomorphism
is assumed and no retopologizing or endpoint deletion is allowed.

Use only the full actual retained-lag relation

    G={(z,m-k,w):T^m z=T^k w,m,k>=0}, source w, range z,

as a Borel subspace of Y x Z x Y. Prove countable Borel
groupoid ownership and legitimate finite-history branch pairs. Different
presentations of one triple are not extra arrows. No all-rational-
matrix action, free word group, germ quotient or conull restriction.

## 3. Own IMAGE clock and all-point version

For each inverse, verify finite positive branch masses and derive

    J_(a,b)=mu(U_(a,b))/mu(V_(a,b)),
    mu(I_(a,b)(A))=J_(a,b)*mu(A), EVERY Borel A subset V_(a,b).

A whole-set ratio alone is not an all-Borel proof. Use the
same branch constant at boundaries/null states, with no separately
assigned values. This is an explicit all-point prescription, not
a.e.-only uniqueness. Set kappa(z)=-log J_(a,b) on U_(a,b),
and use actual finite-history sums

    c(z,m-k,w)=sum_(i<m) kappa(T^i z)
                 - sum_(i<k) kappa(T^i w).

Prove presentation independence, additivity and agreement with actual
branch-pair IMAGE, including null-domain intersections. Extend on
ALL objects Y x R_h by arrows (w,h)->(z,h+c) and translate
h by every real time. Prove complete jointly Borel translation;
claim only a set-level quotient action unless more is proved.
No roof, algorithm runtime or preassigned log-d/prime time.

## 4. Rapid fixed/unit and structural multiplicity gates

After owner and clock, solve ALL fixed states with cell consistency.
Audit the entire set of states whose iterates stay in U_(1,1),
including origin, all its periods and its source/extension isotropy.
Do not equate zero time with absence of source recurrence.

Then test positive-periodic packet multiplicity using the actual
piecewise-linear homogeneity and half-open cell convention. For ANY
nonzero finite periodic itinerary, determine whether radial variation
can retain that itinerary, its least source period and clock.
If it does, test whether full tail equivalence really identifies
these states or leaves distinct packets. Include points initially
on integer boundaries; do not limit the argument to generic interiors.
Show how eventual returns reduce to actual periodic cores.

Use H_z=c(G_z^z). A positive primitive requires H_z=T_z Z
with least T_z>0; repetition is repeated traversal of that SAME
packet. Extension fixed-object isotropy is ker c, not H_z.
Equal clock, gcd or cell labels do not identify different packets.

If ownership fails, a definite wrong/extra primitive appears, or a
structural theorem rules out finite nonzero target packet multiplicity,
record the scoped stop promptly. Do not enumerate high periods to
answer an already decided gate. A conditional multiplicity obstruction
must not be reported as existence or absence of positive returns;
leave that existence OPEN unless proved. If these tests pass,
state the exact next return obligation, not an assumed prime ledger.

## 5. Three separately owned controls

CONTENT-OFF: keep the same cell readout, Bezout convention and full
carrier/measure, but use T_E(u,v)=E_(a,b)*(u,v), removing only
the diag(1/d,1) normalization. Derive all inverse domains and its
OWN IMAGE/cocycle and ALL time groups. Audit the unit-cell
staying set with its actual source/extension isotropy.

BEZOUT-SHIFT: keep the same a,b,d,alpha,beta, but take
s'=s+beta,t'=t-alpha before the SAME first-coordinate normalization.
Prove the integer interface, all inverse domains and OWN IMAGE.
Inspect all fixed points in the unit cell and the distinction
from the main unit-cell dynamics. Do not transfer entire itineraries
merely because a branch's cell label or IMAGE agrees.

UNIT-MATRIX: replace the full action EVERYWHERE by
T_U(u,v)=(v,v-u), keeping ALL R^2 and Lebesgue. Derive its
complete inverse/IMAGE, all fixed/periodic states, ALL time groups
and source/extension isotropy. Do not restrict it to a small disk.

Controls are changed owners, not repairs. They test normalization,
arithmetic selection and Bezout-choice robustness. No finite numerical
cutoff, precision test or prime-label shuffle is needed. Any broad
PROVES_TOO_MUCH claim requires its exact scope and proof; no
unconstructed arbitrary-predicate comparator is allowed.

## 6. Provenance and review scope

Definition-only input: [306 scout record](../306-reciprocal-factor-quotient-flow/evidence/scout-record.md),
SHA-256 `19c147d1751fcb7441e11ffc980ec678ad0f4223593838607465678cca6c922c`.
Root read it completely before this freeze. Its author directly
read 305/282 cards and integrated a subagent's complete 228-card
comparison. These are narrow provenance checks, not global novelty
or new historical audits. The [prior-work lineage](../../docs/prior_work/README.md)
does not transfer any theorem, source lock, clock or Route credit.

No scientific numerics, prime/zero data or external literature campaign.
T0--T3 are broadened owner labels; T3 NOT SUPPLIED / NOT PURSUED.
Classical A0/A1/A2 NOT APPLICABLE; formal coordinates UNASSIGNED;
Route B NOT INVOKED. Strong naturalness OPEN. Root owns all
files except evidence/independent-review.md. Native ARS raw-card,
manuscript and adverse review use inherited-model/shared-context limits,
not external peer review or independent-error evidence. Old packages
and mirrors unchanged; 241/242 paused; programme goal active.
Markdown only; no PDF/LaTeX, staging, commit, publication or upload.

## 7. Appended outcome — original definition above unchanged

Candidate ID: `ANG-20260920-ECC01`.
Status: `OWNED CONTENT CLOCK; RADIAL PACKET-MULTIPLICITY OBSTRUCTION — STOP / FORK`.
The original first 160 lines remain byte-preserved, SHA-256
`b32c433c306eb8f6898d5ba16d096405c34ba1f2635c472158df79a6aac507db`.

The [paper](paper.md) proves the exact integer basis/content
interface, total Borel action, all inverse branches and IMAGE d.
The integer representative is not the actual state. The map
is not onto or usual-topology continuous. Its full retained-lag
owner and real extension use the frozen all-point branch constants.

ALL fixed states are the origin and (0,v) with abs(v)>=1,
each with source/extension Z and H=0. The complete unit-cell
staying set is abs(u),abs(v),abs(v-u)<1; nonzero points have
least source period six, source/extension 6Z and H=0.

Every nonzero periodic orbit has a continuum of outward radial
copies preserving ALL cells (including integer boundaries), least
period and clock. Distinct copies cannot full-tail merge because
their finite cycles have different maximum norms. Any positive
eventual packet reduces to such a periodic core. Thus positive
primitive times have zero or continuum multiplicity, never finite
nonzero multiplicity. Existence of a D>1 positive-time periodic
core remains OPEN; no such existence/absence claim was made.

CONTENT-OFF owns all H=0 and retains unit six-cycles.
BEZOUT-SHIFT owns its new branch domains and IMAGE d but
has a unit-cell fixed vertical segment. UNIT-MATRIX owns global
six-periodic nonzero states, fixed origin and all H=0.
Each control's source/extension isotropy is retained separately.

Portfolio: **stop finite-multiplicity prime-time promotion; retain the
radial obstruction; fork a different source**. T0/owned T1
established at engineering scope; T2 structural gate fails. Stronger
naturalness and positive-return existence OPEN / NOT PURSUED.
T3 NOT SUPPLIED / NOT PURSUED; classical A0/A1/A2 NOT APPLICABLE;
formal coordinates UNASSIGNED; Route B NOT INVOKED.

See [claim ledger](claim-ledger.md), [evidence](evidence/README.md),
[internal review](evidence/independent-review.md), [package index](README.md)
and [source/frontier record](evidence/scout-record.md). No future
definition is credited as another result. Same-object ledger intact;
old packages unchanged; 241/242 paused; programme goal active.
Markdown only; no publication, upload or Git commit.
