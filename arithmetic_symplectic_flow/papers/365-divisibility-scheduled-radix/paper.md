# Divisibility-scheduled radix paths: complete ownership and a retained-phase stop

**Paper:** `365-divisibility-scheduled-radix`; **candidate:** `ANG-20260921-DSR01`.
**Date/status:** 2026-09-21; exact owner theorem and negative positive-packet result.
**Decision:** STOP this candidate at T2; fork only under a fresh frozen contract.
**Status:** OWNED CLOCK; RETAINED PHASE EXCLUDES RETURNS — STOP / FORK.
**Route:** classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## Abstract

We construct the frozen divisibility-scheduled variable-radix source over the
full profinite integers, including every terminating history and every null
phase. Its conditional product probabilities form a measurable kernel; all
inverse branches and history replacements have exact every-Borel IMAGE laws.
Their prescribed all-point logarithms define one clock on the actual-lag
groupoid. The clock kernel equals the full zero-lag relation. Nevertheless,
retained arithmetic phase forces all source isotropy to be trivial, hence all
physical translation stabilizers vanish: there are no positive primitive packets.
Three independently measured controls distinguish this obstruction from digit
branching, phase-only transport and a genuinely periodic finite-phase owner.
No arithmetic-origin theorem beyond the explicit divisibility mechanism, trace,
operator or invariant physical flow measure is claimed.

## 1. Identity, question and provenance

The sole scientific input is the complete [frozen card](candidate-card.md),
106 lines, SHA-256 `a97872251dc4605ea0e60fd65c2ebfee83fedddf221c6200c3517cc4c3d000e8`.
The question is whether its complete measured source and owned clock admit
positive packets without deleting arithmetic phase or any exceptional history.

| Field | Same frozen owner | Status |
| --- | --- | --- |
| Carrier | All finite/infinite radix paths over K=Z-hat | Constructed below |
| Evolution | Partial phase-plus-shift T, undefined only at the empty terminal | Exact |
| Arithmetic | b(q), the first failed integer-divisibility test | Retained |
| Measure | Haar phases and full conditional uniform digit products | Exact |
| Arrows/clock | Actual legal lag triples; c from their prefix IMAGE | Exact |
| Physical time | Real translation on the full cocycle-extension orbit set | Exact set action |
| Classical symplectic map/roof | None | NOT APPLICABLE |
| Operator/trace | None supplied | T3 NOT AUDITED |

The lineage is divisor queries -> current-state digit permissions -> autonomous
phase transport q->q+1. Embedded integer phases perform their actual divisibility
tests; neither a prime list nor a per-prime roof is input. This identifies an
explicit lineage mechanism, not a proof of strong naturalness or prime detection.
The card discloses root's phase-obstruction anticipation; this is not blind discovery.

## 2. Arithmetic schedule and the complete probability kernel

Write h for normalized additive Haar measure on K. Integer translation embeds
Z injectively in K: a nonzero integer cannot vanish modulo every positive integer.
Also intersection_(d>=2) dK={0}, by the residue projections. Thus every q!=0
has a least failed divisor b(q)>=2. For each finite d its level is the clopen set

    {b=d} = (intersection_(2<=e<d) eK) minus dK.

Together with {b=infinity}={0}, this proves Borel measurability. Infinity is a
terminal instruction, never a uniform distribution on infinitely many digits.
The stopping time satisfies N(-n)=n for n>=0 and N(q)=infinity otherwise;
uniqueness follows from the injective integer embedding. In particular N is Borel.

Let A=N_0 union {dagger}, with the discrete sigma algebra. The frozen subset
X of K times A^N_0 requires at each i: a_i is an integer below b(q+i) if
N(q)>i, and a_i=dagger otherwise. These are countably many Borel conditions,
so X is a standard Borel space. Each fibre is nonempty, including the singleton
empty padded word at q=0. Finite fibres have exactly product_(i<N(q)) b(q+i)
words. No finite fibre is replaced by an infinite continuation.

For every i define a probability on A by assigning mass 1/b(q+i) to each
allowed digit when N(q)>i, and mass one to dagger when N(q)<=i. Each coordinate
mass is Borel in q; take their independent product. Finite-cylinder probabilities
are finite products of Borel functions. The monotone-class extension from
cylinders proves a measurable probability kernel nu_q on A^N_0, supported on X_q.
Applying the same argument to rectangles and then all product-Borel sets proves
that q->nu_q(E_q) is measurable for every Borel E subset X. Consequently

    mu(E)=integral_K nu_q(E_q) dh(q)

is a probability measure. This construction fixes nu_q at EVERY q, not just
almost everywhere. Haar singletons have mass zero, since their mass is <=1/M
for every quotient K/MK. All terminating phases and their words are therefore
mu-null but remain in X with their specified, positive finite-fibre probabilities.

## 3. Complete inverse branches and every-Borel IMAGE

T(q,a)=(q+1,shift a) is Borel on D=X minus {(0,empty)}. For each j>=0,
its inverse chart is theta_j(r,w)=(r-1,jw), on the exact Borel domain

    E_j={ (r,w): r!=1 and j<b(r-1) }.

The stopping lengths satisfy N(r-1)=N(r)+1 whenever r-1!=0, with infinity+1
interpreted as infinity. Thus this prefix is always legal, including finite
words ending at the terminal. T theta_j=id on E_j; theta_j T=id on the
source subset with first digit j. These disjoint source subsets cover D, so
all predecessors are listed. The fibre r=1 has no predecessor, not a terminal.

For fixed r and every Borel fibre subset C, product independence gives
nu_(r-1)(jC)=nu_r(C)/b(r-1). This holds also at every null or terminating phase.
Translation invariance of h, followed by integration of this fibre identity, gives

    mu(theta_j E)=integral_E 1/b(r-1) dmu(r,w),  E Borel subset E_j.       (1)

Thus j_j=1/b(r-1) is the prescribed positive full-point version on its full
domain. Its values at null phases are supported by the frozen fibre identities,
not inferred from uniqueness of a Radon--Nikodym derivative almost everywhere.

For a finite digit word u of length m let Phi_u(r,w)=(r-m,uw), on ALL tails
where the m predecessor phases are nonzero and the digits satisfy their bounds.
Put B_m(q)=product_(i<m) b(q+i) on legal m-step histories, with B_0=1.
Iterating the same conditional identity gives IMAGE B_m(r-m)^(-1).
For two words u,v of lengths m,n, prefix replacement Phi_u Phi_v^(-1)
on their common legal tail domain consequently has every-Borel IMAGE

    J_(u,v)=B_n(r-n)/B_m(r-m).                                       (2)

Precisely, mu(R E)=integral_E J_(u,v) dmu for every Borel source-chart E,
where r is its common-tail phase. No restriction to cylinder sets or typical
phases is used. Countably many finite words cover all legal histories.

## 4. Actual groupoid, full kernels and clock ownership

Retain exactly the triples (z,m-n,w) with legal T^m z=T^n w; identify equal
triples only. The equality conditions are Borel, so their countable union is a
Borel groupoid. The above prefix charts cover it, and each source fibre is
countable. Inversion reverses triples; composition adds lags. To compose witness
pairs, advance the earlier of their intermediate shifts to the later legal one;
legality follows from that intermediate source's longer existing history.

Set S_m=log B_m and c=S_m(z)-S_n(w). Two witnesses for the same lag differ
by equal shifts (s,s); their common-tail factors cancel. This proves witness
independence. Aligning intermediate witnesses makes the same factors cancel in
composition, proving the cocycle identity. Equations (1)--(2) give c=-log J
at EVERY point of every chart, including null and terminating histories.

Let k=m-n and q_z,q_w be the phases. Every arrow satisfies q_w=q_z+k.
If k>0, its witnesses obey m=n+k, so cancellation gives

    c(z,k,w)=log B_k(q_z)>0.

If k<0, c(z,k,w)=-log B_(-k)(q_w)<0; for k=0 it is zero.
All factors are finite and >=2 on those legal segments. Therefore, for the
ENTIRE arrow set, not merely isotropy,

    ker c = ker lag = { (z,0,w): T^n z=T^n w for some legal n }.

Their intersection is the same relation. It includes distinct digit histories
at the same phase whose tails eventually agree synchronously.

## 5. Every isotropy, incoming history, terminal and physical phase

For an isotropy arrow at z the phase equality is q_z+m=q_z+n. Integer
injectivity forces m=n, hence its triple is the identity. Thus G_z^z={id}
and H_z=c(G_z^z)={0} for EVERY source. In the full extension on X times R,
an arrow sends (w,h) to (z,h+c). Extension isotropy is also trivial.
Real translation descends to the orbit SET Q. Its stabilizer at [z,h] equals
H_z: an equality after translation is exactly a source-isotropy clock value.
Each source orbit supplies one physical orbit set-theoretically R/H_z=R,
with every height retained. No topology of an embedded line is asserted.

The complete m-step incoming list at (r,w) is all Phi_u(r,w), where
r-j!=0 for 1<=j<=m and u ranges over EVERY allowed prefix of that length.
If r is the positive integer n, exactly 0<=m<=n-1 are allowed. If r is a
nonpositive integer or a noninteger profinite phase, every m>=0 is allowed.
Forward histories stop only at the prescribed empty word, never at phase 1.
Thus phase projections of source orbits are: all positive integers; all
nonpositive integers; or a full noninteger coset q+Z. Within a nonterminating
case, sources are related exactly when their phase-aligned tails eventually
agree, not merely because their phases lie in the same coset.

All finite words at all phases -n form ONE source orbit ending at (0,empty).
For such a source z, its arrow from the terminal has c=S_n(z); its physical
line has coordinate h-S_n(z). Distinct same-depth words remain distinct states
and are connected by the full zero-clock kernel. This entire null orbit remains.
All infinite-tail source orbits likewise retain every legal incoming prefix and
real phase. There is no positive primitive time anywhere, hence no positive
packet or nontrivial positive repetition ledger to transfer to a later gate.

## 6. Three separate own controls

### PHASE-OFF

The full binary shift with its own Bernoulli measure has prefix IMAGE 1/2;
finite-prefix replacements have IMAGE 2^(n-m) on every Borel set, by the
independent product law. Its actual-lag clock is c=k log2. Hence ker c equals
the entire zero-lag synchronized-tail relation, as does its intersection with
ker lag. Unequal shifts of a source agree iff its tail is eventually periodic.
For least eventual edge period l, the source isotropy is lZ, its clock image
is l log2 Z, and extension isotropy is trivial; aperiodic isotropy is trivial.
Two eventually periodic sources share a source orbit iff their primitive words
agree up to cyclic rotation: align their common periodic tails in either direction.
Therefore ALL primitive binary necklaces give one packet each, least time
l log2, with powers only repetitions. All incoming finite words and rotations
are included; aperiodic source orbits give physical lines. In particular two
constant words give two log2 packets, while a^(l-1)b is primitive for every
l>=2 (b occurs once) and gives composite index 2^l. Null paths are not deleted.

### DIGIT-OFF

For the full Haar K, partial Q(q)=q+1 outside 0 has the unique inverse
r->r-1 outside 1. Translation proves its own every-Borel IMAGE 1, including
all legal history replacements, so its entire clock is zero. The actual arrows
retain lags, but q+k=q has only k=0: source and extension isotropy are trivial,
H=0, ker c is the entire groupoid, ker lag and the intersection are identities.
Its source orbits are precisely the nonpositive integers, the positive integers,
and each noninteger coset q+Z. Incoming depths and the terminal are exactly as
above, now with one predecessor at each legal depth. Every source orbit gives
one physical line; none gives a positive packet. MAIN's radix clock is not reused.

### FINITE-PHASE

Use its own phase masses 1/2 and full conditional alternating 2/3 products.
Prefixing at predecessor phase r has every-Borel IMAGE 1/b_C(r), since phase
flip preserves its own phase measure and conditional products give that factor.
All digits at both phases and all incoming histories are retained; there is
neither a terminal nor a missing incoming phase. History IMAGE and c follow
by the same product cancellation, now with B_(2j)(r)=6^j,
B_(2j+1)(0)=2*6^j and B_(2j+1)(1)=3*6^j. The sign of c is the sign of
nonzero lag, so ker c=ker lag, their full zero-lag relation, and intersection.

Every orbit meets phase 0. Pair its successive digits into the SIX symbols
{0,1} times {0,1,2}; T_C^2 is exactly their full shift. Between phase-0 sources,
lag is even; any common-tail witnesses can both be advanced once if necessary
to make them even. Thus tail equivalence on that section is exactly six-symbol
tail equivalence, not a selected sublanguage. A least eventual pair period k
gives FULL source isotropy 2kZ, clock image k log6 Z, and trivial extension
isotropy. Otherwise source isotropy and H are zero and the physical orbit a line.
For a phase-1 source, shift once before pairing; conjugation retains its isotropy.
All positive packets are therefore precisely primitive six-symbol necklaces:
least time k log6, one packet per necklace, repetitions r*k log6. Their complete
odd/even incoming prefixes and phase-1 rotations are included in the same packet.
Already the six constant pair words give six distinct log6 packets. These are
this control's returns, not returns of MAIN's full profinite phase.

## 7. Gate assessment, limits and decision

T0 full Borel carrier, conditional measure and actual arrows are established.
T1 the same divisibility-driven prefix transport owns the exact clock; strong
naturalness remains OPEN. T2 is an exact negative: the retained phase forces
H_z=0 everywhere and no positive packets. T3 is NOT AUDITED; classical A0/A1/A2
are NOT APPLICABLE, formal coordinates UNASSIGNED, and B NOT INVOKED.
The same-object ledger stayed intact. The controls show that removing phase
or replacing it by a finite phase is a changed owner, not a repair credited here.
STOP/FORK follows; no extra search, new candidate or changed source is authorized
by this paper. There are no numerical cutoffs, fitted data or novelty claims.

## Reproducibility and instruction-use record

Inputs read in full: the 106-line [card](candidate-card.md) and the 107-line
[paper template](../paper-template.md). Proofs above are first-principles exact
arguments; no independent-proof file, review, other scientific package or web
source was read for this manuscript. ARS router/workflow/runtime/adversarial
instructions previously read in full were reused for scope and claim discipline;
no new external review is implied. Author `/root/algebraic_henon_author`, internal
AI, NOT_CALIBRATED. Root owns claim-surface integration and review acceptance.
