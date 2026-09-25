# Frozen candidate — divisor-gated product radix

Candidate ID: `ANG-20260920-DPR01`.
Paper ID: `308-divisor-product-radix-flow`. Date: 2026-09-20.
Version: 1. Initial status: `OPEN — FULL PARTIAL OWNER, IMAGE AND FIXED-ROOT PACKETS`.

## 1. Complete carrier, source and boundaries

Let Y=coproduct_(a,b>=1) {(a,b)} x [0,1], with discrete
positive-integer roots, full standard-Borel real fibres and measure
mu=counting roots x Lebesgue, density one on every fibre.
Keep all roots, unit factors, seeds, cut points and endpoints.
At the CURRENT state set

    N=a*b, q=1+floor(N*x).

The actual partial domain is precisely q dividing N. On it put

    c=N/q, T(a,b,x)=(b,c,N*x-(q-1)).

If divisibility fails, the state remains in Y as terminal:
no successor, reset, rounding or completing loop. T^0 still exists.
At x=1 the SAME rule gives q=N+1; do not add
an endpoint return. At x=0 the SAME rule gives q=1.
Retain q=1 and q=N, but when N=1 they are the
SAME branch, not two copies. In particular the specification
gives T(1,1,x)=(1,1,x) for x<1 and terminal at x=1;
this boundary definition does not classify its clock or packets.
At an internal cut k/N, use q=k+1, with the SAME
divisibility test. Incoming arrows to terminals must be retained.

The factor-symbolic interface is d|n -> q|a*b -> a*b=q*c.
The original integer n can be inspected at root (n,1),
but that slice is NOT selected as the carrier. Integer
roots set the geometric partition; real position selects q;
its quotient changes the next roots and geometric partition.
This is an autonomous deformation of divisor admissibility, not
a proved Logistic/Henon conjugacy or conservative/symplectic lift.
Product radix, digit ordering, root update and measure are designs;
strong arithmetic naturalness is OPEN. No prime predicate, factor
table, zero data, external fitting schedule or log-prime roof.

## 2. Complete proposed inverse branches

For EVERY a,b>=1 and positive divisor q of N=a*b specify

    U_(a,b,q)={(a,b)} x [(q-1)/N,q/N),
    V_(a,b,q)={(b,c)} x [0,1), c=N/q.

At target (B,C,y), enumerate EVERY A>=1 with C dividing A*B.
Set q=A*B/C and propose

    I_A(B,C,y)=(A,B,(q-1+y)/(A*B)), 0<=y<1.

Prove domain, inverse, image and enumeration completeness. Retain all
different A predecessors and ALL targets, including y=1 outside
these inverse domains. Check full image and incoming terminal arrows.
Establish the actual Borel category; do not infer global continuity,
local homeomorphisms or an etale topology from piecewise formulas.

Use only the actual partial retained-lag relation

    G={(z,m-k,w):T^m z=T^k w,m,k>=0}, source w, range z,

where ALL required iterates exist, including T^0 at terminals.
Equip it with the Borel subspace structure in Y x Z x Y.
Prove countability, groupoid operations and full branch-pair ownership.
Keep literal lag, not extra histories, free affine words, a
germ quotient or a conull-only reduction.

## 3. Own IMAGE and full-point time

For each actual inverse/branch pair theta derive from THIS measure

    mu(theta(E))=integral_E J_theta dmu, c_time=-log J_theta

for EVERY Borel subset of its exact domain. A whole-interval
mass ratio alone is not an IMAGE proof. Compute the derivative
from the actual affine formula. At retained boundary/null states,
use that same affine formula's derivative by analytic extension,
and compose it along actual finite histories. This is a declared
pointwise version, not a.e. Radon–Nikodym uniqueness. Do not assign
a derivative to an undefined terminal forward step. Prove this
prescription is independent of presentations and additive; otherwise STOP.

Extend on ALL Y x R by (w,h)->(z,h+c_time), and
let physical time translate h by every real number. Prove
complete jointly Borel translation and its compatibility with arrows.
Claim only a set-level quotient action unless more is proved.
No separate roof, running cost or borrowed symbolic clock.

## 4. First complete fixed-root and packet gate

After ownership, inspect fixed integer roots with their COMPLETE
real fibres, not selected seeds. Solve ALL full-state fixed
equations with digit, unit and endpoint consistency. Determine
the entire set whose integer roots stay fixed for all forward
iterates. Do not mistake one root-preserving step for a full
trajectory or a fixed seed for a permitted carrier restriction.

Compute full source isotropy, H_z=c(G_z^z), and extension
isotropy ker c for those strata. A positive primitive requires
H_z=T_z Z with least T_z>0; repeats have times r*T_z
on the SAME packet. Full packet equivalence must include every
actual finite preimage/history. Equal root products or times alone
do not merge distinct packets. Retain all unit/zero-time states.

Test whether the resulting times and multiplicities can belong to
the direct prime-time target. A definite wrong/extra primitive or
ownership failure triggers STOP / FORK promptly; no high-period
census or parameter adjustment after a decisive first gate. Do
not claim a complete main periodic ledger from fixed-root tests.
If these pass, state the remaining return obligation explicitly.

## 5. Three separately owned controls

RADIX-OFF: keep the main partial domain, q|a*b and root
update (a,b)->(b,a*b/q), but replace the real update by x.
Derive its OWN inverse domains, IMAGE/cocycle, ALL time groups,
and all fixed states with their complete fibre intervals/isotropy.
Do not reuse the main [0,1) branch image.

ARITHMETIC-OFF: on ALL x<1 and ALL positive roots use
q=1+floor(a*b*x) and

    T_A(a,b,x)=(b,a*b,a*b*x-(q-1)).

Every q=1,...,a*b is allowed; x=1 stays terminal. This
removes divisor selection/quotient feedback while retaining the radix.
Derive all OWN inverse domains and IMAGE. Classify ALL possible
eventual source returns using the actual integer-root recurrence;
retain any zero-time source/extension isotropy. A nonconstant branch
clock does not by itself imply positive return times.

DIGIT-REFLECT: keep the main q|a*b domain and root update,
but use real output q-a*b*x (reflection of the main output).
Keep the entire [0,1] carrier and every resulting endpoint.
Derive all OWN inverse domains/IMAGE. Solve all full fixed states
and the entire fixed-root staying sets, with units/endpoints and
literal source/extension isotropy; do not transfer main itineraries.

These controls test geometric expansion, divisor feedback and digit
orientation. They are changed owners, not repairs. No numerical
precision/cutoff or label shuffle is needed for these exact tests.
Any PROVES_TOO_MUCH claim must be bounded by a proved control;
do not assert an unconstructed arbitrary-prime-data encoding theorem.

## 6. Provenance, authority and review

Definition input: [307 scout record](../307-euclidean-cell-content-flow/evidence/scout-record.md),
SHA-256 `a84b57e8039f1c973902b63ea1b0a91c41930620dad05d36852d75ee66720e07`.
Root read the entire record before this new freeze. Its author
read 269-card lines 1–145 and 304-card lines 1–90; its
subagent read 306-card lines 1–88, not the author directly.
These bounded definition comparisons confer no global novelty,
source lock, clock or theorem. Its later 307 Section-3
transcription QA read no 307 result/paper/review. See the
[prior-work guide](../../docs/prior_work/README.md) for lineage, not credit.

T0--T3 are broadened owner labels; T3 NOT SUPPLIED / NOT PURSUED.
Classical symplectic base, positive roof/mapping torus and A0/A1/A2
are NOT APPLICABLE. Formal coordinates UNASSIGNED; B NOT INVOKED.
Root owns all files except evidence/independent-review.md. Native ARS
raw-card, synthesis and final-adverse checkpoints use inherited-model /
shared-context scrutiny, not external peer review or independent errors.
No scientific numerics, external source campaign, operator/trace claim,
PDF/LaTeX, staging, commit, publication or upload. Old packages,
positive 304, mirrors and Phase-I sources unchanged; 241/242 paused;
programme goal active.

## 7. Appended outcome — original definition above unchanged

Candidate ID: `ANG-20260920-DPR01`.
Status: `OWNED PRODUCT-RADIX CLOCK; SQUARE-TIME FIXED PACKETS — STOP / FORK`.
The original first 169 lines remain byte-preserved, SHA-256
`d1508daa2421d536da8ad3f8b028b46af2ae358b2b853a7477cffffa7b6fc5e4`.

The [paper](paper.md) proves all inverse branches and the full
partial Borel owner. Its image is all roots x [0,1),
retaining incoming arrows to non-endpoint terminals. Each inverse
owns IMAGE 1/(a*b), from full Borel change of variables;
actual finite-history derivatives own the all-point cocycle and time.

ALL fixed states are (n,n,1/(n+1)) for n>=2 and
the entire unit interval (1,1,x), 0<=x<1. They also
exhaust the states whose roots remain fixed for ALL forward
iterates. At nonunit fixed states source isotropy is Z,
H=2*log(n) Z and extension isotropy zero. Unit states
retain source/extension Z and H=0. Distinct constant tails
cannot merge under the full owner, including finite inverse histories.

Already n=2 gives a true primitive log 4 packet: no
shorter time exists in its same isotropy image. Every n>=2
fixed packet has composite exponentiated time n^2. This decides
the direct prime-time gate, not all higher main returns or
all asymptotic timing questions. No high-period census was pursued.

RADIX-OFF owns changed interval images and globally zero clock;
each fixed root retains its entire digit interval. ARITHMETIC-OFF
owns its radix clock but all eventual returns are unit-root
fixed states, so ALL H vanish. DIGIT-REFLECT owns (0,1]
images and different fixed seeds with the same square times;
unit interior points have source period one or two and zero
time, while zero reaches terminal one. No control is a repair.

Portfolio: **stop direct prime-time promotion; retain the owned source
and fixed-root obstruction; fork a different architecture**. T0 and
owned T1 established at engineering scope; T2 target fails.
Stronger naturalness OPEN; higher main returns and T3 NOT PURSUED.
Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

See [claim ledger](claim-ledger.md), [evidence](evidence/README.md),
[internal review](evidence/independent-review.md), [package index](README.md)
and [source/frontier record](evidence/scout-record.md). Same-object ledger
intact; no future definition is credited as a result. Old
packages, positive 304 and mirrors unchanged; 241/242 paused;
goal active. Markdown only; no publication, upload or Git commit.
