# Frozen candidate — binomial–Bernstein divisor feedback

Candidate ID: `ANG-20260920-BBD01`.
Paper ID: `310-binomial-bernstein-divisor-flow`. Date: 2026-09-20.
Version: 1. Initial status: `OPEN — INTEGRAL/IMAGE OWNER AND COMPLETE FIXED-ROOT GATE`.

## 1. Full carrier, measure and actual feedback

Let Y=coproduct_(a,b>=1) {(a,b)} x [0,1], with discrete
positive-integer roots, standard Borel structure and fixed measure

    mu=counting roots x (Lebesgue_(0,1)+delta_0+delta_1).

Both endpoint atoms have mass one. All roots, unit factors,
seeds, cuts and endpoints remain; there is no root-dependent weight.
From the CURRENT roots define

    N_(a,b)=binom(a+b-2,a-1),
    P_(a,b)(x)=integral_0^x t^(a-1)*(1-t)^(b-1) dt
                  / integral_0^1 t^(a-1)*(1-t)^(b-1) dt.

The normalization is part of the actual function P, NOT a
change from the fixed fibre measure to that integral kernel.
Set q=1+floor(b*x). Precisely when q divides N_(a,b),
put c=N_(a,b)/q and

    T(a,b,x)=(b,c,P_(a,b)(x)).

Otherwise keep the state as terminal, with T^0 but no
successor, reset, escape or completing loop. At x=0 use
q=1 and real output 0. At x=1 use q=b+1
and output 1, still subject to (b+1)|N. Every a=1,
b=1 and c=1 case uses the same law. Source N=1
remains; q=1=N is ONE branch, not two counted copies.
The specification gives identity at (1,1,x<1) and terminal
at (1,1,1), without a time/packet claim. At internal
cut k/b use q=k+1; failed divisibility makes that point
terminal without removing incoming arrows or the state itself.

The precise lineage is divisor admissibility -> two-letter composition
count N -> real position chooses q|N -> N=q*c
changes the next roots and hence the next real function.
Verify N_(2,n)=n for every n>=1: it supplies an
inspection interface for the original divisor symbols, NOT a
selected carrier. The same roots determine the composition count
and both exponents of P; prove their exact normalization relation.
No prime predicate, prime/zero table, per-prime parameter or roof.
The binomial replacement, integral action, probe scale b, root
update and measure are declared designs; stronger naturalness OPEN.
No Logistic/Henon conjugacy, conservative or symplectic lift is implied.

## 2. Complete source branches and candidate inverse

For every a,b>=1 use

    I_(b,q)=[(q-1)/b,q/b) for 1<=q<=b,
    I_(b,b+1)={1}.

For every allowed q|N specify U_(a,b,q)={(a,b)} x I_(b,q),
with target at root (b,c), c=N/q,

    [P_(a,b)((q-1)/b),P_(a,b)(q/b)) if q<=b,
    {1} if q=b+1.

Define Q_(a,b)(y)=inf{x in [0,1]:P_(a,b)(x)>=y}.
Prove P is a well-defined monotone bijection and Q its actual
inverse, rather than assuming these from notation. At any target
(B,C,y), enumerate EVERY A>=1 with C|N_(A,B), set
q=N_(A,B)/C, require 1<=q<=B+1 and membership in the
proposed branch target, and retain (A,B,Q_(A,B)(y)).
Prove exact images, completeness, overlaps, endpoints and full image.
Keep every distinct predecessor. Establish the actual Borel category;
do not infer onto, global continuity or etale/local-homeomorphism status.

Use only the actual partial retained-lag relation

    G={(z,m-k,w):T^m z=T^k w,m,k>=0}, source w, range z,

with every required iterate defined and T^0 at all terminals.
Use the Borel subspace structure of Y x Z x Y and
prove countable groupoid ownership. One triple's presentations are not
extra arrows. No free polynomial action, extra histories or germ quotient.

## 3. Own layered IMAGE, all-point version and time

For each actual inverse theta derive from THIS mu

    mu(theta(E))=integral_E J_theta dmu, EVERY Borel E in its domain.

On 0<y<1 use abs(Q'(y)), including retained internal
cut points. At an endpoint in the inverse domain use the
actual source/target atomic mass ratio, NOT an interior derivative
limit. Prove finite positivity on every actual point and the
stratified full-Borel law; whole-branch masses alone are insufficient.
The internal-cut prescription is declared, not a.e.-only uniqueness.

On actual forward states set kappa(z)=-log J_(I_z)(Tz),
and use c=sum_(i<m) kappa(T^i z)-sum_(i<k) kappa(T^i w).
Prove all-point presentation independence, composition and branch-pair
IMAGE agreement, including null cuts and terminal histories. Never
evaluate a derivative for an undefined forward step. Extend on
ALL Y x R by (w,h)->(z,h+c) and translate h
by every real t. Prove complete jointly Borel time; claim
only set-level quotient action unless further topology is established.
No extra roof, runtime clock or prescribed log-prime parameter.

## 4. Complete fixed-root gate and early stop

After ownership, inspect fixed integer roots with their COMPLETE
real fibres, including all units, internal cuts and both atoms.
Solve ALL root equations and ALL full-state fixed equations.
Classify the ENTIRE set whose roots remain fixed for every
forward iterate, including any asymptotic but nonperiodic trajectories.
Do not confuse convergence to a fixed point with exact eventual return.

For those sets compute source isotropy, H_z=c(G_z^z),
extension kernel and actual full packet equivalence. A positive
primitive requires H_z=T_z Z with least T_z>0; repetitions
r*T_z traverse that SAME packet. Retain all finite preimages;
equal numerical time or root labels do not merge different cores.

An ownership failure or a definite wrong/extra primitive decides
STOP / FORK promptly. Do not pursue high-period changing-root
censuses, tune a normalization or remove an endpoint after the
first decisive gate. If these tests pass, state the remaining
return obligation; do not assume a complete prime ledger.

## 5. Three separately owned controls

GEOMETRY-OFF: keep N,q, the main partial domain and quotient
root update, but use real output x. Derive all OWN
inverse target domains and IMAGE/cocycle. Classify ALL fixed states,
fixed-root staying fibres, their isotropy and ALL time groups.
The main P-image intervals cannot be borrowed.

OUTPUT-REFLECT: keep the main domain and roots, but use real
output 1-P_(a,b)(x). Derive all OWN inverse targets, layered
IMAGE and endpoint laws. Solve ALL fixed states and the entire
fixed-root infinite staying sets, with literal source/extension groups.
Do not transfer main itineraries merely because derivative magnitudes agree.

PERMISSION-OFF: remove divisor permission and quotient-root feedback;
on the ENTIRE Y, including x=1, define

    T_A(a,b,x)=(b,N_(a,b),P_(a,b)(x)).

The digit no longer restricts this action. Derive all OWN
inverse domains and layered IMAGE. Solve ALL fixed states and
complete fixed-root staying fibres, distinguishing asymptotic attraction
from exact source isotropy. Other changing-root returns are outside
this control's bounded gate unless needed for a specific obstruction.

Controls test geometric transport, orientation and divisor feedback.
They are changed owners, not repairs. No numerical cutoff,
precision run or prime-label shuffle is needed. Any PROVES_TOO_MUCH
claim needs an explicit proved scope, not arbitrary-data rhetoric.

## 6. Provenance, authority and internal review

Definition input: [309 scout record](../309-content-power-complement-flow/evidence/scout-record.md),
SHA-256 `9be14c35a76d0642f3aca416d9e56a90964260bd06d6167eda48bc1cdd59c139`.
Root read the whole record before this freeze. The final
N=binom(a+b-2,a-1) is used; its earlier uncompleted binomial
sketch was withdrawn before any ID or audit. The input author
read 308-scout Section 3 lines 53–191, 303-card lines 1–115
and 283-card lines 1–110. Only its subagent read 302-card
lines 1–85 and the line-86 heading, not the author directly.
Later transcription QA read only 309-scout Section 3, not its
result/paper/review. No old clock, source lock or theorem transfers.
The [prior-work guide](../../docs/prior_work/README.md) supplies lineage, not credit.

T0--T3 are broadened owner labels; T3 NOT SUPPLIED / NOT PURSUED.
Classical symplectic base, positive roof/mapping torus and A0/A1/A2
are NOT APPLICABLE. Formal coordinates UNASSIGNED; B NOT INVOKED.
Root owns all files except evidence/independent-review.md. Native ARS
raw-card, synthesis and final-adverse checkpoints use inherited-model /
shared-context scrutiny, not external peer review or independent errors.
No scientific numerics, external campaign, operator/trace, PDF/LaTeX,
staging, commit, publication or upload. Positive 304 and old
packages/mirrors unchanged; 241/242 paused; programme goal active.

## 7. Appended outcome — original definition above unchanged

Candidate ID: `ANG-20260920-BBD01`.
Status: `OWNED BERNSTEIN CLOCK; SUB-LOG-2 FIXED PACKET — STOP / FORK`.
The original first 180 lines remain byte-preserved, SHA-256
`632d753cd4f8c99103116026613f877b459115598fadd6254fea612194425f5e`.

The [paper](paper.md) proves the exact integral normalizer,
strict monotone inverse, exhaustive actual branches and full rootwise
image. The partial countable-to-one Borel source is not onto or
ordinary continuous. Its own IMAGE uses inverse derivatives inside
and actual unit mass ratios at endpoint atoms. Actual partial
histories own the all-point cocycle and complete real translation.

Binomial growth excludes EVERY fixed root n>=5. The four
remaining root-preserving cells are [0,1), [0,1/2),
[1/3,2/3) and {1}. Their complete infinite-staying sets
are respectively [0,1), [0,1/2), {1/2} and {1}.
At n=2 all positive staying seeds strictly approach zero
without ever reaching it: source/H/extension isotropy are zero.
Unit fixed states and the n=2/n=4 fixed atoms retain
source/extension Z but H=0.

The remaining fixed state (3,3,1/2) has source Z,
H=log(15/8) Z and trivial extension isotropy. Its least
positive time is a genuine primitive, not a repetition or
chosen representative. Since 1<15/8<2, it is neither
log of an integer >=2 nor a positive repetition of
such a time. Different fixed tails cannot merge through finite
preimages. The direct-prime-time target therefore fails immediately.

GEOMETRY-OFF has global zero clock and owns its fixed fibres.
OUTPUT-REFLECT retains the same sub-log-2 fixed packet but changes
unit phases and endpoint termination. PERMISSION-OFF owns a total
source with two full staying fibres; its positive midpoint has
least time log(3/2), while other interior seeds converge without
return. These are changed owners, not candidate repairs.

Portfolio: **stop direct-prime-time promotion; retain the owned integral
clock and complete fixed-root obstruction; fork a different architecture**.
T0/owned T1 are engineering results; T2 fails at the
fixed-root target gate. Stronger naturalness OPEN; changing-root periods
and T3 NOT PURSUED. Classical A0/A1/A2 NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED. Same-object ledger intact.

See [claim ledger](claim-ledger.md), [evidence](evidence/README.md),
[internal review](evidence/independent-review.md), [package index](README.md)
and [source/frontier record](evidence/scout-record.md). Future proposals
remain separate and unadmitted. Positive 304 and old packages
unchanged; 241/242 paused; goal active. Markdown only; no
publication, upload or Git commit.
