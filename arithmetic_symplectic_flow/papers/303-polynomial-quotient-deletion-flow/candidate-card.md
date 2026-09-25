# Frozen candidate — polynomial quotient exchange with divisor deletion

Candidate ID: `ANG-20260920-PQD01`.
Paper ID: `303-polynomial-quotient-deletion-flow`. Date: 2026-09-20.
Version: 1. Initial status: `OPEN — FULL POLYNOMIAL WORD OWNER, IMAGE CLOCK AND ALL FIXED WORDS`.

## 1. Entire polynomial source and precise partial rule

Let A=Z[X], including zero, all signed constants and all degrees.
Use its discrete topology and the ENTIRE X_word=A^(N_0), with
product topology. All infinite tails and all nonintegral-division
states remain; no prime, irreducible-polynomial or periodic subspace
is selected. Here X in a polynomial is a formal indeterminate,
not the dynamical state variable.

For first three letters (P,Q,U) and remaining infinite tail eta,
if Q!=0 perform unique ordinary polynomial division in Q[X]:

    P=V*Q+R,    R=0 or deg R<deg Q.

At a nonzero constant Q, the remainder is zero. At P=0,
the quotient and remainder are both zero. The domain consists
EXACTLY of Q!=0 and V,R both in Z[X]. Otherwise the entire
prefix fibre is terminal, with no forward step or added loop.
Do not substitute pseudo-division or drop a nonintegral quotient.
On the domain set

    B=U*Q+R,
    T(P,Q,U,eta)=(B,V,eta).

The current divisor Q is deleted. This is a three-to-two prefix
action; the quotient becomes the second next-state letter, so the
entire polynomial coefficients affect future admissibility. No
fixed polynomial is merely evaluated on another seed.

For EVERY old Q!=0 and target prefix (B,V), divide B=U*Q+R
in Q[X]. If U,R are integral, the proposed strict inverse is

    h_Q(B,V,eta)=(V*Q+R,Q,U,eta).

Otherwise this Q-labelled inverse domain is empty. Retain ALL
such branches, including units Q=1,-1; old Q is part of the
actual predecessor, not an extra free arrow label. Verify uniqueness
of each branch, completeness of inverse domains and the full image
of T. Retain targets whose own next division fails. Frozen boundary
tests include prefix (1,2,0), and the all-zero infinite word.

## 2. Complete alphabet law and IMAGE ownership

Freeze the following explicit rational probabilities as DESIGN inputs,
not a unique canonical arithmetic law:

    rho(0)=1/2,
    rho(m)=1/[4*|m|*(|m|+1)] for m!=0,
    sigma(m)=1/[2*|m|*(|m|+1)] for m!=0,
    lambda_d=1/[(d+1)*(d+2)] for d>=0.

Set pi(0 polynomial)=1/2. For nonzero P=sum_(i=0)^d a_i X^i,
a_d!=0, set

    pi(P)=(1/2)*lambda_d*sigma(a_d)*product_(i<d)rho(a_i).

Use mu=pi^(N_0). Normalization, existence, full support and point
masses are obligations; all coefficients and degrees are retained.
This is not Haar, and no invariance under the partial update is
presumed. Local compactness is NOT assumed for the full countable-
alphabet product; test that boundary rather than deleting symbols.

Every admissible prefix (P,Q,U) has proposed image cylinder (B,V),
with its entire tail. Derive the Borel inverse IMAGE factor from
the common-tail product law. Its proposed prescription is the ratio
of the source and target cylinder masses, UNPROVED at freeze.
Use c=-log J only after proving this law, in the direction
target cylinder -> predecessor cylinder. No 298 clock transfers.

Use the FULL retained-lag partial-tail groupoid

    G={(z,m-n,w): T^m z=T^n w, m,n>=0}, source w, range z,

with every iterate actually defined. Topology uses actual finite
branch pairs over common open domains and all cylinder refinements.
No arbitrary prefix swaps, extra polynomial action, cyclic-word
quotient, germ quotient or conull reduction. Verify presentation
independence and additivity, aligning only valid histories, and
a continuous all-point version fixed by full support at null words.

Use ALL extension objects X_word x R, arrows (w,s)->(z,s+c(g)),
and physical time s->s+t for every real t. Prove jointly continuous
two-sided complete time. Coarse Hausdorffness / classical circles
remain OPEN. A non-locally-compact etale owner is not called LCH.

## 3. Lineage and decisive all-fixed-word discriminator

The exact [prior-work](../../docs/prior_work/README.md) interface to
check is the constant-integer sector: for P=a,Q=b!=0,U=u,
the domain is b divides a and the actual update is

    (a,b,u,eta)->(u*b,a/b,eta).

For 1<b<a this is the proper-divisor admissibility symbol, extended
to polynomial quotient/remainder composition. Negative constants,
zero and units remain in the full object. It is an autonomous
symbolic deformation, not a Logistic/Henon conjugacy or positive-
dimensional conservative lift. No supplied prime or zero data enters.

After the full owner/clock checks, classify ALL FIXED full words,
not a chosen constant tail. Keep arbitrary polynomial remainders,
units, signed constants and zero letters. For every fixed core
compute full source isotropy, H_z=c(G_z^z), extension fixed-object
isotropy, least positive time if any and actual packet multiplicity.
Positive primitive means H_z=T_z Z with a least T_z>0; repetitions
traverse that SAME packet. Equal degree, norm, weight or time must
not identify different words. Test possible mergers through full
inverse excursions rather than a restricted fixed-point graph.

One surplus unit packet, wrong constant-prime time or excess fixed
multiplicity decisively stops target promotion. Then finish only
the two controls below and the frozen boundaries; leave higher/
eventual returns OPEN. No period census, tuned alphabet law, chosen
remainder, irreducible quotient, trace, determinant or T3 rescue.

## 4. Changed-source controls, each with its OWN clock

EXACT-DIVISION: domain Q!=0 and P=VQ with V in Z[X]; otherwise
retain terminals. Set T_e(P,Q,U,eta)=(UQ,V,eta), keeping the
same complete carrier and measure. Derive all actual inverse
branches and its OWN IMAGE law. Classify ALL fixed full words
and their full time groups/packet identities, not other periods.

NO-DELETION: use the main division domain and rule, but retain
the divisor in the output:

    T_r(P,Q,U,eta)=(Q,UQ+R,V,eta).

Derive its actual inverse domains, IMAGE law and ALL time groups.
Test whether the clock is a coboundary of the measure of the
first-three-letter cylinder, not a borrowed deletion clock. Classify
ALL fixed words and retain their source/extension isotropy even
if the time group is zero. No general other-period census.

## 5. Provenance, review and authority

The coefficient-evolution gap was recorded in
[302's source record](../302-integral-affine-word-flow/evidence/scout-record.md),
SHA-256 `ffde2721d93dedcb773598024ce7d3d5f2de1180bb915a8a71f1338fb2a74cd1`.
The binary-source scout supplied this now-complete definition in
303 before freeze, with no return or Jacobian audit. Root read
[298's word-rewriting card](../298-subtract-factor-word-flow/candidate-card.md)
and [283's fixed-polynomial card](../283-nonlinear-residue-clock-screen/candidate-card.md)
as narrow comparisons. The product-measure template is shared;
the polynomial coefficient action, domains and every clock/return
claim require fresh proofs. No global novelty certification.

All polynomial/source/deletion/measure naturalness remains OPEN.
T0--T3 are broadened owner labels only; classical A0/A1/A2 NOT
APPLICABLE; formal coordinates UNASSIGNED; Route B NOT INVOKED.
No scientific numerics, cutoff, precision parameter or external
literature campaign. Analytic/Hamiltonian/quantum NOT SUPPLIED.
Root owns all files except evidence/independent-review.md. ARS
raw-card, manuscript and final adverse checks are inherited-model/
shared-context internal review, not peer review or independent-error
evidence. Old packages/mirrors unchanged; 241/242 paused; goal active.
Markdown only; no PDF/LaTeX, staging, commit, upload or publication.

## 6. Appended outcome — original definition unchanged

Status: `OWNED POLYNOMIAL WORD CLOCK; UNIT RETURNS AND REMAINDER MULTIPLICITY — STOP / FORK`.
The preceding original 163 lines remain byte-preserved, SHA-256
`0ab77852d39b1cef717baf490539749f4fca383720751c7a116065433e6b59cf`.

The [paper](paper.md) proves the full integral-division domain,
all old-Q inverse branches, surjectivity onto every word including
terminals, probability normalization, full support and null singleton
words. The source is nowhere locally compact; the complete tail
owner is Hausdorff/second-countable/etale but NOT LCH. Its own
Borel prefix IMAGE law gives a continuous all-point cocycle and
complete real time. The constant-integer divisibility interface holds.

ALL fixed full words are (Q^2+R,Q,Q,...), Q!=0 and every
integral R of degree below Q (including zero). Their full source
isotropy is Z, H=(-log pi(Q))Z and extension fixed-object isotropy
is zero. Different cores cannot merge by full T-tail arrows,
even when their ordinary shift tails agree. Units ±1 already give
distinct primitive log-16 packets, and constant prime 2 gives
log 48. Each nonconstant Q also retains infinitely many remainder
packets of equal time. All null words remain.

EXACT-DIVISION owns its clock and has exactly (Q^2,Q,Q,...)
as fixed words, still including unit and wrong-constant-time packets.
NO-DELETION owns a global coboundary clock, so all H=0; its
complete fixed family (Q,Q,1,eta), Q!=0 and arbitrary eta,
retains source AND extension isotropy Z. Terminal isotropy is
trivial even when incoming arrows exist.

Portfolio: **stop target promotion / fork**. T0/scoped measured
T1/all-fixed T2 established. Higher/eventual returns, coarse topology
and stronger naturalness OPEN / NOT PURSUED. T3 NOT SUPPLIED /
NOT PURSUED; classical A0/A1/A2 NOT APPLICABLE; formal coordinates
UNASSIGNED; Route B NOT INVOKED. No input or packet convention
changed. A separate finite factor/gcd definition has no ID or
result here; the matrix lane is unadmitted. See the
[claim ledger](claim-ledger.md) and [evidence](evidence/README.md).
