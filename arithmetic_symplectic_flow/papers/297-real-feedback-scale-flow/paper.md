# Real feedback and common scaling: exact prime packets, inactive feedback

Candidate ID: `ANG-20260920-RFS01`.
Paper ID: `297-real-feedback-scale-flow`. Date: 2026-09-20.
Status: `EXACT BOREL PRIME PACKETS; FEEDBACK INACTIVE IN RETURN SELECTION — SCOPED ADVANCE / STOP`.
Result type: exact full-state owner/packet theorem with a negative necessity control.

## Abstract

An integer factor operation reads a real-coordinate branch, and the
current integer simultaneously scales that coordinate and a positive
scale coordinate. The full retained-lag Borel tail groupoid owns the
complete scale-time action. Solving its full return equation excludes
every nonzero transverse coordinate and gives exactly one primitive
cyclic time packet of least time log p for each prime p. No centre or
component is selected in advance. Nevertheless removing the arithmetic
feedback leaves the entire primitive packet ledger unchanged. The
selection uses the factor readout on the zero axis and the declared
scale law, not a new arithmetic restriction on mixed itineraries.
We retain the exact owner result but stop stronger natural-A0 promotion
and do not build T3. No measure-derived clock, topological embedded
circle, conservative lift or formal Route result is asserted.

## 1. Frozen identity, lineage and evidence boundary

The original [card](candidate-card.md) has SHA-256

    f1c1cbad0c050151b1991f4a39ba6b58f70c1c0011c1079782a1e845b3842340

For m>=2, let g(m) be the greatest divisor d>=2 of m having no
proper nontrivial divisor, and set g(1)=1. On the FULL source define

    Y = coproduct_(n>=1) {n} x R,
    F(n,r)=(g(n+floor(abs(r))), n*r).

The actual scale owner and physical time are

    M=Y x R_(>0),
    D(n,r,s)=(F(n,r),n*s),
    Phi^t(n,r,s)=(n,r,exp(t)*s), t in R.

| Same-object item | Exact owner | Limitation |
|---|---|---|
| Arithmetic source | Full integer roots, divisibility-defined g, actual floor feedback | Factor readout and floor choice are designed |
| Carrier | All r in R, all s>0, including every sign and floor endpoint | Standard Borel category; no smooth or symplectic assertion |
| Arrows | Entire retained-lag tail relation of D | No free affine maps, chosen history or germ quotient |
| Physical clock | Exactly t in Phi | Uniform multiplication by n is declared; measure NOT SUPPLIED |
| Packets and repetitions | Full time stabilizers and actual arrows plus Phi | Not a theorem of embedded circles in a Hausdorff quotient |
| Analytic / quantum owner | NOT SUPPLIED | No T3 or Route B inference |

The lineage is proper-factor admissibility -> an integer factor-symbolic
operation -> real-coordinate feedback -> this SAME update's scale action.
It is a specified source deformation, not a conjugacy to the prior sieve,
Logistic or Henon dynamics, and not a conservative dimensional lift.
The n projection is not an autonomous factor: for n=2, r=0 and
r=1 give next roots 2 and 3 respectively. The feedback is real as
an action, but its role in returning packets must still be tested.

The [082 readout control](../082-gpf-fixed-point-euler-control/candidate-card.md)
already has n->gpf(n) with a supplied logarithmic roof. The
[193 cone flow](../193-indecomposable-radial-quotient/candidate-card.md)
already uses integer dilation and common radial time. The closest root
formula is [287](../287-nonlinear-two-seed-residue-flow/candidate-card.md),
with n'=g(n+j), but a profinite digit, two-register seed action and
joint-Haar clock. That closer comparison was identified just after
the freeze and read before the proof record; it changes no frozen
definition. [268](../268-gpf-matrix-contact-flow/candidate-card.md) has a
different matrix-contact owner without fibre feedback, while
[288](../288-active-pair-residue-flow/candidate-card.md) has a partial
second-order witness/profinite owner. None supplies a theorem here.

Choosing the greatest factor, the floor readout, the common multiplier
and time normalization are declared designs. No prime list, per-prime
parameter, prescribed return list, zero data or Mangoldt weight is used.
Their absence does not establish arithmetic necessity or natural A0.

## 2. Full Borel owner, including missing incoming states

**Proposition 1.** The arithmetic rule is defined at every state. D
is a countable union of injective Borel branches with the frozen exact
inverses. Its full image consists of every prime-root component and
the unit-root strip {1} x (-1,1) x R_(>0). It is not onto M.

*Proof.* A minimal divisor greater than one of an integer m>=2 has
no proper nontrivial divisor. Thus the finite set defining g(m) is
nonempty, and its members are exactly prime divisors. In particular
g(p)=p and g(p^a)=p for every prime p and positive integer a;
g(m)=1 holds only at m=1. This derives the readout, not a prime table.

The sets I_0=(-1,1) and I_j=(-j-1,-j] union [j,j+1), j>=1,
partition R, with j=floor(abs(r)) on I_j. On root n and I_j,
D is the Borel bijection

    (n,r,s) -> (g(n+j),nr,ns),
    (g(n+j),R,S) -> (n,R/n,S/n), R in n I_j, S>0.

All endpoints are included on their specified side. No openness
or continuity across these branches is required. Every output root
is a prime or 1. Root 1 requires n=1 and j=0 and has exactly
the displayed image strip. Given any (p,R,S) with p prime, choose
a positive integer a with n=p^a>|R|. Then (n,R/n,S/n) is in
the j=0 branch and maps to that target. This proves the full image.
All composite-root states and the missing unit-root targets remain
in M and continue to have a forward D step. QED.

**Proposition 2.** The entire retained-lag relation

    G_D={(z,m-k,w):D^m z=D^k w, m,k>=0}

is a standard Borel groupoid with countable source fibres. Phi acts
on it by jointly Borel automorphisms for all real t.

*Proof.* For each m,k the equal-iterate set is Borel, since D is
Borel and equality is a Borel diagonal on M. The union over m,k,
with the lag recorded, is Borel in M x Z x M. Units, reversal
and the formula (z,l,w)(w,h,v)=(z,l+h,v) are Borel. To check
closure, align the two intermediate iterate counts at w by extending
them to their maximum. Determinism supplies the same forward tail,
so the outer counts differ by l+h. No onto hypothesis is used.

Each target has at most countably many immediate preimages, by the
countable injective branches. The same is true for each finite
iterate. For fixed w, the possible z with D^m z=D^k w therefore
form a countable union of countable sets. This proves countable
source fibres, with every actual lag retained.

The explicit equations give D Phi^t=Phi^t D. Thus simultaneous
application of Phi^t to both endpoints preserves every tail arrow,
including lag and all compositions. This is jointly Borel, in fact
continuous on the ambient object/endpoint coordinates, with inverse
Phi^(-t). All real times exist. QED.

There is accordingly a complete action on the orbit SET M/G_D.
We do not promote that set to a standard Borel quotient, a Hausdorff
space or a manifold, nor infer joint continuity on a coarse quotient.
The proof supplies no measure, IMAGE clock or contact form.

## 3. Entire time stabilizers, not selected centre returns

For y=(n,r), write (n_i,r_i)=F^i y and

    a_m(y)=product_(0<=i<m)n_i, a_0(y)=1.

Direct induction gives r_m=a_m r and
D^m(y,s)=(F^m y,a_m s). Every a_m is positive. Consequently

    D^m(Phi^t(y,s))=D^k(y,s)

is equivalent to BOTH

    F^m y=F^k y,       exp(t)=a_k(y)/a_m(y).             (1)

This is the full return condition: it quantifies over every pair
m,k, including nonperiodic prefixes, and follows from actual D.

**Theorem 3.** On the complete frozen carrier,

    H_(n,r,s) = (log g(n)) Z     if r=0 and n>=2,
                 {0}           otherwise.

The primitive cyclic time packets are exactly one for each prime p,
of least time log p, with repeats ell log p. All other states have
no positive time return.

*Proof.* If r!=0, the first condition in (1) includes
a_m r=a_k r, which forces a_m=a_k. Its second condition then
forces t=0. This argument applies to every branch, root, sign and
floor endpoint; no drift estimate, finite census or genericity is used.

At r=0, the root sequence is n,g(n),g(g(n)),.... For n=1 it
is constantly 1, so all a_m=1 and again H={0}. For n>=2 put
p=g(n). All roots after the first step equal p. If n=p the
source is fixed and a_m=p^m. If n is composite, it is NOT a
periodic source point: it enters (p,0) after one step. In that case
a_m=n p^(m-1) for m>=1. The equal-source presentations have
both counts positive, or both zero; exactly one zero count cannot
return to the original composite root. Thus (1) gives precisely
all integral multiples of log p in either case, not extra logarithms
from the transient n. The least positive time is log p.

To count packets, first note that actual D arrows and Phi preserve
the property r=0. After forgetting s they give actual common tails
under F. Two zero-axis roots n,n'>=2 have such a tail exactly when
g(n)=g(n'). Distinct prime fixed cores cannot meet, and no finite
preimage can join them. Conversely, the forward D image of any
zero-axis composite root reaches its prime root with a positive s;
Phi connects every pair of positive scale phases there. Hence every
prime contributes exactly one packet, not one for every transient
root or scale amplitude. No r!=0 or unit-root point can join it.
Repeating this SAME packet ell times gives ell log p. QED.

In particular, a composite root such as 4 enters the prime-2 packet;
the first-step multiplier 4 does NOT generate a distinct log-4
primitive. The entire positive scale ray is a time phase, not extra
multiplicity. These are consequences of (1), not a selected section.

**Proposition 4.** Fixed-object G_D isotropy is Z exactly on
{(1,r,s):|r|<1,s>0}, and trivial elsewhere. In contrast, the
source-F lag isotropy is Z also on all (n,0), n>=2.

*Proof.* If D^m z=D^k z with m>k, comparison of the positive
s coordinates gives a_m=a_k. Every intermediate integer root is
therefore 1. Root 1 has an incoming F step only from root 1 with
|r|<1, where F and D are already fixed. Backtracking finitely many
steps shows the original z lies in precisely this strip. Every lag
occurs there. Outside it only lag zero can fix z. For F alone,
the same r-coordinate argument excludes nonzero-r cycles except
the unit strip; every zero-axis root is fixed or eventually fixed,
so its full tail isotropy is Z. QED.

Thus zero-time D isotropy in the unit strip is not a positive cyclic
time packet, while the prime packets have trivial D isotropy at
each fixed object. No state has H=R. Topological closure or embedded
circle properties have not been proved from these algebraic facts.

## 4. Frozen controls: what actually selects the ledger

All controls retain full M and Phi but use their OWN D relation.

**FEEDBACK-OFF.** Set D_0(n,r,s)=(g(n),nr,ns). This is Borel
on every full root component and retains the same common-scale
iteration formula. Its own equation (1) excludes every r!=0 time
return. At r=0 it agrees with the main law. Hence its COMPLETE
primitive ledger is again exactly one least-log-p packet per prime.
The feedback changes source transitions, but is not necessary for
either the full time-packet exclusion or the prime packet selection.
This is an exact negative necessity control, not a claim of conjugacy
between the full systems or equality of nonreturning orbits.

In particular, FEEDBACK-OFF fixes every (1,r,s), not just the
main owner's |r|<1 strip. The point (1,1,s) is fixed in this
control, but the main D sends it to (2,1,s). Thus the difference
is not merely transient bookkeeping: feedback also changes discrete
fixed sets and fixed-object isotropy, while leaving the complete
positive time-packet ledger unchanged.

**FACTOR-OFF.** Set D_1(n,r,s)=(n+floor(abs(r)),nr,ns).
Its branches remain injective Borel maps with the indicated inverse
scalings. Its own equation (1) excludes every r!=0 positive return.
On r=0 each integer n is fixed as a source root. For n>=2,
H=(log n)Z and different n are different packets; the unit has
H={0}. Thus the COMPLETE primitive ledger is one packet for EVERY
integer n>=2. The log-4 packet is distinct from the log-2 packet,
not a second traversal of it. Factor extraction, not feedback, removes
these composite primitive labels in the main owner.

**SCALE-OFF.** Set D_2(n,r,s)=(F(n,r),s). It retains Borel
branches and its own full tail relation. Every iterate preserves s,
so D_2^m(Phi^t z)=D_2^k z forces exp(t)*s=s. Therefore all
H_z={0}. Discrete source isotropy alone supplies no positive time.

| Control | Complete relevant result | Ownership / necessity lesson |
|---|---|---|
| Full nonzero-r carrier | No positive time returns | Common multiplication excludes returns independently of g |
| Entire zero axis and composite transients | One packet per prime, no extra amplitude count | Full tail equation is needed; first-step index is not a primitive time |
| Unit-root strip | Zero-time D isotropy Z, time group {0} | Isotropy and physical return are different |
| FEEDBACK-OFF | Same complete primitive ledger | Feedback is dynamically real but unnecessary for this selection |
| FACTOR-OFF | One primitive per integer n>=2 | The chosen factor readout supplies prime selection |
| SCALE-OFF | No positive returns anywhere | Declared common scale is essential, not a derived arithmetic clock |

The precise PROVES_TOO_MUCH risk is now exhibited by FACTOR-OFF:
the same scale architecture produces an all-integer period family.
We do not claim it realizes every imaginable prescribed dataset.
Nor does FEEDBACK-OFF prove that every possible feedback is irrelevant.

## 5. Gate decision and next obligation

T0 is established in the stated full Borel category. Scoped T1 has
an explicit arithmetic readout, actual real feedback and owned time;
measure derivation and stronger arithmetic naturalness are NOT
ESTABLISHED. T2's full cyclic packet and repetition ledger is exact.
Classical A0/A1/A2 NOT APPLICABLE; formal coordinates UNASSIGNED;
Route B NOT INVOKED. T3 and quantum owners NOT SUPPLIED / NOT PURSUED.

Portfolio: **scoped advance of owner/T2; stop natural-A0 promotion;
fork the search**. The decisive gate reason is that removing feedback
does not change the complete prime packet ledger: its selection uses
g on the zero axis plus the declared multiplier. The matched times
do not close this mechanism gap. Keep this construction as a reusable
control, without deleting its nonreturning carrier or modifying g,
the multiplier, signs, unit strip or packet equivalence to improve it.

A future candidate needs a freshly frozen mechanism whose arithmetic
return constraints add something beyond a factor readout paired with
a scale design. This finding is not a universal no-go. No analytic
object, borrowed topology, physical-cost interpretation or conservative
geometry is appended to rescue the present naturalness claim.

All arguments above are exact, with no finite scientific computation,
prime cutoff, parameter fit or external theorem campaign. The
[claim ledger](claim-ledger.md), [evidence](evidence/README.md),
[internal review](evidence/independent-review.md) and
[scout provenance](evidence/scout-record.md) preserve the distinctions.
ARS/AI-assisted internal same-model checks are not external peer
review, formal verification or independent-error evidence. Old
packages/mirrors unchanged; 241/242 paused; programme goal active.
