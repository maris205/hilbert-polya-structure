# Frozen candidate — quotient/remainder arithmetic reciprocal flow

Candidate ID: `ANG-20260920-QRF01`.
Paper ID: `299-quotient-remainder-reciprocal-flow`. Date: 2026-09-20.
Version: 1. Initial status: `OPEN — BOREL OWNER, IMAGE VERSION AND FIXED PACKETS`.

## 1. Entire carrier and autonomous arithmetic rule

Freeze X=N_0 x [0,1), with its product Borel structure: the first
coordinate q is discrete and the second r is the full half-open real
interval. Write v(q,r)=q+r. Retain every rational, irrational, integer
endpoint, zero, composite quotient and terminal point. No selected
continued-fraction digit alphabet or recurrent subset replaces X.

Set d(0)=0, d(1)=1, and for q>=2 let d(q) be the greatest integer
covering 1 in the divisibility order that divides q. This finite
arithmetic operation, its existence and its relation to primes must
be justified from divisibility, not a supplied prime table. Put

    h_q=q-d(q), u=h_q+r;
    T(q,r)=(floor(1/u), 1/u-floor(1/u)) when u>0.

When u=0 there is no forward step. All such objects remain; do not
add infinity, an escape reset, an absorbing loop or a return edge.
The nonnegativity of u and exact terminal set are obligations. The
next quotient is recalculated from the entire reciprocal at EVERY
step; q is neither a fixed external label nor a carried scan phase.

For k=0 define the branch domain

    B_(q,0)={q} x ([0,1) intersect (1-h_q,infinity)).

For k>=1 use

    B_(q,k)={q} x ([0,1) intersect
               (1/(k+1)-h_q, 1/k-h_q]).

Empty branches add no arrows. The proposed complete image is

    E_(q,k)={(k,rho): 0<=rho<1, w=k+rho>0,
                         0<=d(q)+1/w-q<1},
    theta_(q,k)(k,rho)=(q,d(q)+1/w-q).

These domains, inverses and endpoint conventions must be checked.
Floor jumps forbid assuming a local homeomorphism in the displayed
product topology. The requested category is STANDARD BOREL only.

## 2. Full measure, arrows and pointwise clock specification

The source measure is counting(q) times Lebesgue(r), hence the
ordinary Lebesgue measure under the Borel value coordinate v in
[0,infinity). Prove the needed sigma-finiteness, full support and
nonatomicity; invariance or finite total mass is not presumed.

Freeze the ENTIRE partial retained-lag tail groupoid

    G_T={(x,m-k,y): T^m x=T^k y, both iterates defined, m,k>=0}.

Its arrow is y -> x; T^0 is the identity on EVERY object, including
terminals. Use the Borel structure inherited from X x Z x X and
all actual finite inverse-branch pairs. No free prefix, arbitrary
fractional-linear arrow, germ quotient or extra word label is added.
Show Borelness, countable fibres, the groupoid laws and that these
branch pairs give the actual arrows. Surjectivity is not assumed.

Derive the Borel IMAGE density of each theta on arbitrary Borel
subsets of its actual domain by ordinary real change of variable.
For the all-point version, freeze the following completion: each
branch uses the absolute derivative of its displayed real analytic
formula w -> d(q)+1/w, including retained endpoints; forward
branches use the reciprocal derivative. Compose these analytic
derivatives along actual finite branch pairs, then take c=-log J.
No numerical Jacobian or prime return length is prescribed.

This analytic branch completion is an EXPLICIT version choice.
Do not claim a.e. IMAGE data alone fix arbitrary null restrictions
or isolated endpoint charts. Prove composition and presentation
independence for the full retained-lag owner. State exactly which
continuity or analytic completion owns the tested null fixed states.
An inverse density must not be confused with the forward density.

Extension objects are X x R, with arrows (y,s)->(x,s+c(g)).
Physical time is s->s+t for every real t. Establish the complete
jointly Borel action and its compatibility with all arrows; no
topological groupoid flow, Hausdorff quotient, positive roof or
classical symplectic/mapping-torus owner is assumed.

## 3. First discriminators and separately owned controls

After checking the owner and clock, classify ALL fixed source
points, including q=0, q=1, primes, composites and integer endpoints.
For each fixed point compute the ENTIRE source lag isotropy, time
group H_x=c(G_x^x), fixed-object extension isotropy and actual packet
identity. A primitive cyclic packet needs H_x=T_x Z with least
T_x>0; its repeated traversals are ell*T_x in that SAME packet.
Equal periods, integer products or passages through finite preimages
do not identify distinct cores without actual tail arrows.

One unwanted unit packet, wrong prime time or extra fixed packet
is decisive: STOP target promotion and finish only the controls below.
Do not classify higher/eventual returns, adjust the arithmetic readout,
fit a measure or roof, or launch T3 to rescue a failed first test.

1. FACTOR-OFF: replace d(q) by 0 for every q, retaining X, measure,
   all terminal objects and the same analytic IMAGE convention.
   Audit its full reciprocal action and all time-return groups.
2. QUOTIENT-READOUT: replace d(q) by q for every q, retaining all
   source states and the same measure/version convention. Derive
   its OWN branch clock and classify only all its fixed points.
3. Test the original branch endpoint (q,r)=(4,0), the null terminal
   (0,0), and the control's boundary (1,0). Keep singleton branch
   restrictions if they occur; disclose the analytic version choice.

Source/readout/reciprocal/measure/version naturalness remains OPEN.
The card is informed by definition-stage endpoint and fixed-point
considerations; no blind selection or withheld-design claim is made.
No scientific numerical run, cutoff, precision or external literature
campaign is part of this bounded exact audit.

## 4. Lineage, comparisons and nontransfer

The [prior-work](../../docs/prior_work/README.md) arrow is current
prime/composite divisor observable -> active quotient/remainder
symbolic deformation -> arithmetic subtraction and reciprocal update
-> its same-source measured Borel time. This is a stated replacement,
not a Logistic/Henon conjugacy or positive-dimensional conservative lift.
The binary-source scout supplied the complete main formulas before
freeze, without a Jacobian or return theorem; root fixes audit scope,
controls and the explicit analytic endpoint-version boundary here.

[127](../127-prime-continued-fraction-digit-boundary/candidate-card.md)
only observes prime digits of the unmodified Gauss map on irrationals,
with no lineage mechanism or flow owner. Here d(q) changes every
transition and all real endpoints stay. [284](../284-least-divisor-borel-flow/candidate-card.md)
uses restricted affine maps on profinite seeds and a different
maximal-domain clock completion. [295](../295-canonical-residue-generated-flow/candidate-card.md)
uses strict all-radix affine generation, not this deterministic partial
reciprocal source. None supplies arrows, clocks or packet results here.

No prime table, von Mangoldt/zero data, per-prime parameter or assigned
log-prime roof enters. Greatest-factor evaluation is still a declared
readout, not proof of natural arithmetic origin or physical runtime.

## 5. Authority, review and handoff

T0-T2 are broadened owner labels only. T3 / analytic operator / trace /
quantization NOT SUPPLIED / NOT PURSUED. Classical A0/A1/A2 NOT
APPLICABLE; formal coordinates UNASSIGNED; Route B NOT INVOKED.
Root owns integration and every file except the native reviewer's
evidence/independent-review.md. Raw-card, manuscript and final adverse
checks are internal inherited-model/shared-context review, not external
peer review, formal verification or independent-error evidence.
All old packages/mirrors unchanged; 241/242 paused; goal active.
Markdown only; no PDF/LaTeX, staging, commit, upload or publication.

## Appended audit outcome — 2026-09-20

Final status: `OWNED RECIPROCAL IMAGE CLOCK; UNIT PACKET AND WRONG PRIME TIMES — STOP / FORK`.

The original 154-line version-1 bytes above remain unchanged, SHA-256
`30b59f86e36d599376d6c96cc0969eadedc4ec3c695bed60a74c2007d5b49577`.
The [paper](paper.md) proves the full standard Borel partial source,
counting–Lebesgue measure and actual IMAGE law. The entire retained-
lag groupoid owns a consistent analytic-completed all-point cocycle
and a complete jointly Borel real action. It is not a topological
or classical suspension claim. The endpoint version is explicit;
a.e. data alone do not force values on arbitrary null restrictions.

ALL fixed points are x_q=(q,alpha_q-q), with q=1 or prime and
alpha_q=(q+sqrt(q^2+4))/2. Each is a distinct actual packet with
source isotropy Z, trivial extension fixed-object isotropy and
H=(2 log alpha_q)Z. Every alpha_q^2 is irrational; the least time
is not log N for any integer N. The unwanted unit packet alone
stops the target, and the prime-core times are also wrong.

FACTOR-OFF has reciprocal-involution source returns but H={0}
everywhere, including its analytically completed singleton boundary.
QUOTIENT-READOUT has the same fixed-time formula at EVERY integer
q>=1. Each comparator owns its own clock. All main terminals and
the finite endpoint path 4->1/2->2 remain; it is not a return.

Portfolio: **stop target promotion / fork**. T0/scoped measured T1
and ALL-fixed-core T2 are established; stronger naturalness OPEN.
Other main returns and coarse quotient topology OPEN / NOT PURSUED.
T3 NOT SUPPLIED / NOT PURSUED, classical A0/A1/A2 NOT APPLICABLE,
formal UNASSIGNED, B NOT INVOKED. Same-object ledger intact.
[Claims](claim-ledger.md), [evidence](evidence/README.md),
[review](evidence/independent-review.md) and
[definition/admission record](evidence/scout-record.md) preserve
limits. The separate adjacent-factor/parity exchange is only an
untested definition awaiting its own freeze; no second ID or result.
Old packages unchanged; 241/242 paused; programme goal active.
