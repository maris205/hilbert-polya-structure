# Polynomial quotient deletion owns a word clock but retains unit and remainder packets

Paper ID: `303-polynomial-quotient-deletion-flow`.
Candidate ID: `ANG-20260920-PQD01`. Date: 2026-09-20.
Status: `OWNED POLYNOMIAL WORD CLOCK; UNIT RETURNS AND REMAINDER MULTIPLICITY — STOP / FORK`.
Route state: broadened owner audit; classical A0/A1/A2 NOT APPLICABLE;
formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

The full infinite word source over Z[X] executes an integral
polynomial division, exchanges its quotient with the next register,
and consumes the current divisor. This is an actual coefficient
update, not evaluation of a fixed polynomial or a prime-test switch.
It owns all local inverse branches, a full-support product-measure
IMAGE cocycle and complete continuous real time. Its full topology
is not locally compact. All fixed words can be classified exactly:
they are (Q^2+R,Q,Q,...), where Q!=0 and R is any integral
remainder of degree below deg Q, including zero. Each is a
distinct primitive packet of least time -log pi(Q). Constant units
already give log-16 primitives, constant 2 gives log 48, and
every nonconstant Q retains infinitely many different remainder
packets at the same time. Target promotion stops. Exact-division
and divisor-retention controls use their own clocks and clarify
the distinct roles of remainders and letter consumption.

## 1. Identity and same-object claim boundary

The [original card](candidate-card.md) freezes one ANG object,
not a classical symplectic realization. The question is whether
the full coefficient dynamics supplies owned time and a suitable
primitive packet ledger without selecting primes, remainders or tails.

| Field | Exact owner | Scope |
| --- | --- | --- |
| Carrier | All infinite words in the discrete alphabet A=Z[X] | All zero/unit/signed/degree/tail states |
| Evolution | Integral ordinary division P=VQ+R; (P,Q,U,eta)->(UQ+R,V,eta) | Partial three-to-two prefix rule |
| Arithmetic | Integer divisibility -> integral polynomial quotient/remainder admissibility | No prime or irreducibility predicate |
| Measure | Explicit full alphabet law pi and product probability mu | Declared design, not Haar |
| Arrows and clock | Entire valid-history tail groupoid, inverse IMAGE, c=-log J | All-point continuous version |
| Time and packets | Real extension, full isotropy image and actual tail equivalence | No selected representative or separate roof |
| Classical geometry / Hamiltonian / contact / quantum | NOT APPLICABLE / NOT SUPPLIED | No Logistic/Henon conjugacy claimed |
| Trace / zeta / determinant / operator | NOT SUPPLIED / NOT PURSUED | No T3 rescue |

Strong naturalness of the polynomial replacement, deletion and
alphabet law is OPEN. Neither complete ownership nor integer
coefficients alone prove natural A0 or a prime-only orbit theorem.

## 2. Ordinary division, full branches and retained terminals

Let A=Z[X], including zero, and W=A^(N_0) with the full
product topology. In Q[X], for Q!=0, polynomial division gives
unique V,R with P=VQ+R and R=0 or deg R<deg Q.
Existence follows by successive cancellation of the leading term;
uniqueness follows because a nonzero multiple of Q cannot equal
a polynomial of lower degree. At constant Q!=0, R=0 and V=P/Q.
At P=0 both V and R are zero. No sign normalization is applied.

The partial domain D consists of all prefixes (P,Q,U) with
Q!=0 and these V,R in Z[X]. It is a union of full clopen
cylinders. Outside D keep terminal words without an outgoing step.
On D write B=UQ+R and set

    T(P,Q,U,eta)=(B,V,eta).

For a target prefix (B,V) and ANY Q!=0, divide B=UQ+R
by the same convention. If U,R are integral, the actual inverse is

    h_Q(B,V,eta)=(VQ+R,Q,U,eta).

The reconstructed first letter has quotient V and remainder R
by uniqueness of division, so the predecessor is in D and maps
to the target. Conversely every predecessor has some nonzero Q
and necessarily these U,R. These are therefore ALL inverse
branches. The different old Q values are different actual middle
letters; they are not free labels for an identical predecessor.
Each admissible cylinder C(P,Q,U) maps homeomorphically onto
C(B,V), with the entire tail unchanged. T is a local homeomorphism.

Taking old Q=1 gives the predecessor (V,1,B,eta) of EVERY
target (B,V,eta). Thus T:D->W is onto, although not defined
at every word and not globally injective. Surjectivity does not
turn a terminal into a state with a future. In particular,

    (2,1,1,0,eta) -> (1,2,0,eta),
    (0,1,0,0,0,...) -> (0,0,0,...).

Both right-hand words are terminal: the first has nonintegral
quotient 1/2, the second has zero divisor. Their incoming arrows
are nevertheless retained. Units Q=1,-1, zero remainders, U=0
and outputs V=0 follow the same rule, without added loops.

On constant-integer prefixes P=a,Q=b!=0,U=u the exact rule is

    b divides a: (a,b,u,eta)->(u*b,a/b,eta).

For 1<b<a this tests precisely a proper-divisor symbol. The
quotient really enters the next state; on nonconstant letters the
remainder is carried into UQ+R and affects future division. This
is the specified [prior-work](../../docs/prior_work/README.md) deformation
from integer divisibility to polynomial admissibility and coefficient
evolution. It is not a chronological sieve equivalence or a lift
of a previously studied Logistic/Henon map.

## 3. Complete probability, topology and IMAGE law

Use exactly the frozen laws

    rho(0)=1/2, rho(m!=0)=1/[4*|m|*(|m|+1)],
    sigma(m!=0)=1/[2*|m|*(|m|+1)],
    lambda_d=1/[(d+1)*(d+2)], d>=0.

Since sum_(j>=1) 1/[j(j+1)]=1 by telescoping, rho sums to
one on Z, sigma to one on nonzero Z, and lambda to one on
nonnegative degrees. Set pi(0)=1/2 and, for the unique nonzero
P=sum_(i=0)^d a_i X^i with a_d!=0, set

    pi(P)=(1/2)*lambda_d*sigma(a_d)*product_(i<d)rho(a_i).

For fixed d, independently summing the leading and lower coefficient
laws gives total mass (1/2)*lambda_d. Summing d and adding zero
therefore gives one. Every polynomial has positive mass; every
individual mass is at most 1/2. The countable product probability
mu=pi^(N_0) has cylinder masses equal to the corresponding finite
products, uniquely determining its Borel law. This is the ordinary
countable product construction, not a fitted periodic-state measure.
Every cylinder has positive mass, so mu has full support. Every
singleton word has mass at most (1/2)^n for every prefix length n,
and hence has zero mass.

A is countable and discrete. The first-differing-coordinate metric
on W is complete, and eventually-zero words give a countable
dense set; cylinders give a countable clopen basis. Thus W is
Hausdorff, second countable and completely metrizable. It is nowhere
locally compact. A compact neighborhood containing a cylinder of
length k would project at coordinate k onto all of the infinite
discrete alphabet A. A compact set cannot have that image. This
argument uses the FULL free next coordinate, not infinite dimension
as a slogan or a deletion of unbounded polynomial degrees.

For an admissible prefix put B=UQ+R. Any Borel subset E of
C(B,V) corresponds to a Borel tail set E_tail. Product measure
gives mu(E)=pi(B)pi(V)mu(E_tail), whereas
mu(h_Q(E))=pi(P)pi(Q)pi(U)mu(E_tail). Hence the actual
INVERSE IMAGE factor is

    j(P,Q,U)=pi(P)*pi(Q)*pi(U)/[pi(B)*pi(V)].

All factors are positive, including zero-polynomial factors. This
is a Borel-set identity in the direction target -> predecessor,
not just a finite-cylinder ratio or a forward derivative. The
global source is not assumed T-invariant; branch clocks need not
all have one sign. No old integer-word IMAGE law is imported.

## 4. Full partial-tail cocycle and time

Retain G={(z,m-n,w):T^m z=T^n w}, with m,n>=0 and all
iterates defined. Source is w and range is z; retain integer lag.
Use actual finite branch pairs on common open terminal domains,
with cylinder refinements. These give local source/range homeomorphisms
and hence an etale topology. Aligning already-defined middle histories
gives composition and chart refinements; it never assumes a terminal
has a future step. Range, source and discrete lag separate distinct
triples, so the groupoid is Hausdorff and second countable. It is
NOT an LCH groupoid: its local source charts have the same
non-locally-compact boundary as the full object space.

Let J_m(z)=product_(i=0)^(m-1) j(T^i z), with J_0=1, for
the ACTUAL m-step history. Terminal-to-z inverse composition scales
measure by J_m(z). Thus a branch pair from w to z has

    J_g=J_m(z)/J_n(w),
    c(g)=log J_n(w)-log J_m(z).

Two valid presentations of the same lag extend both sides by
the same existing common tail, so its factors cancel. The same
alignment proves additivity under composition. Each factor is locally
constant on the appropriate prefix history, so c is continuous.
Full support makes the continuous density version unique on every
open chart, including null fixed words. There is no separate
choice of a return-point clock or a conull replacement of G.

On ALL extension objects W x R use arrows
(w,s)->(z,s+c(g)). Real translation (z,s)->(z,s+t) for every
t is jointly continuous, two-sided complete and commutes with
the arrows. The etale orbit projection is open, so the quotient
time action is continuous with its quotient topology. No locally
compact, Hausdorff coarse flow or embedded-circle statement is made.

For each z the full time-return group is H_z=c(G_z^z).
Only H_z=T_z Z with least T_z>0 defines a positive primitive
packet. Extension fixed-object isotropy is the kernel of this
cocycle on source isotropy. Repetition is ell traversals of the
SAME packet, not a coincidence of lengths between different words.

## 5. ALL fixed words, complete time groups and the stop

**Theorem.** The fixed full words are exactly

    z_(Q,R)=(Q^2+R,Q,Q,Q,...),
    Q in Z[X] nonzero, R in Z[X], R=0 or deg R<deg Q.

To prove completeness, let (P,Q,U,eta) be fixed. Equality after
the two-letter output forces every letter from position 2 onward
to equal U. Equality in position 1 gives V=Q, and hence
P=Q^2+R. Equality in position 0 gives P=UQ+R, so
(U-Q)Q=0. Z[X] has no zero divisors, since leading coefficients
of nonzero products multiply to a nonzero integer. Therefore U=Q.
Conversely every displayed word has that ordinary division and
is fixed. No tail or remainder was selected beforehand.

At z_(Q,R) the prefix IMAGE factor simplifies to pi(Q): the
head factor pi(Q^2+R) and one pi(Q) cancel. Every integer
lag occurs in source isotropy, with no extra branch labels, so

    G_z^z=Z,    c(ell)=-ell log pi(Q),
    H_z=(-log pi(Q))Z,    extension fixed-object isotropy=0.

Because 0<pi(Q)<1, the least positive time is -log pi(Q).
Distinct pairs (Q,R) give distinct full words and unequal constant
T-tails. No full tail arrow connects such cores. Excursions through
other words or finite preimages cannot merge them, because their
composition would still require equality of the constant tails.
Real phases give one packet per core, not an extra identification
between cores. All cores are null but retained under the proved
continuous version of the same measure's clock.

For a nonzero integer b viewed as a constant polynomial,

    pi(b)=1/[8*|b|*(|b|+1)],
    z_(b,0)=(b^2,b,b,...),   T_b=log[8*|b|*(|b|+1)].

Both polynomial units b=1,-1 already produce distinct primitive
log-16 packets. Constant prime b=2 gives log 48, not log 2.
These frozen tests suffice to stop target promotion. In addition,
for EVERY nonconstant Q all integer constants are allowed remainders,
so there are countably infinitely many distinct packets with that
same least time. For example Q=X has pi(X)=1/96 and hence
infinitely many log-96 packets indexed by its integer remainders.
They are not merged with each other or with a constant-3 packet
of the same numerical time. These are exact fixed-family results,
not an enumeration of every packet in W.

The all-zero word is terminal, not fixed or given a return loop.
Every terminal has trivial source isotropy because no positive
iterate is defined there, and therefore H=0 and trivial extension
isotropy. Incoming arrows do not change that fact. Higher periods
and general eventual-return classification remain OPEN / NOT PURSUED.

## 6. Separately owned controls

### EXACT-DIVISION

Now require Q!=0 and P=VQ with integral V, and send
(P,Q,U,eta) to (UQ,V,eta). For a target (B,V), every actual
inverse chooses Q!=0 dividing B in Z[X], then U=B/Q and
P=VQ. These are all its branches. Q=1 still gives an inverse
at every target, and all excluded prefixes remain terminal.

The same COMMON-TAIL product argument on this changed map gives
its OWN inverse factor pi(P)pi(Q)pi(U)/[pi(UQ)pi(V)].
It therefore owns its continuous full-tail cocycle and real extension.
Solving its full fixed equation gives exactly (Q^2,Q,Q,...),
Q!=0. Each has source isotropy Z, H=(-log pi(Q))Z and
zero extension fixed-object isotropy. Distinct cores remain different
packets. Thus remainders create the extra family per nonconstant Q,
but even their removal leaves all unit and wrong-constant-time
packets. No other EXACT-DIVISION periods are classified.

### NO-DELETION

Retain the main division domain but use

    T_r(P,Q,U,eta)=(Q,B,V,eta), B=UQ+R.

A target prefix (Q,B,V) has a predecessor precisely if Q!=0
and division B=UQ+R has integral U,R. The unique predecessor
is (VQ+R,Q,U,eta). This is a partial homeomorphism between
the specified clopen domains; it does not claim every word lies
in its image. It retains the whole carrier and all terminals.

Define the positive continuous prefix function

    F(z)=pi(z_0)*pi(z_1)*pi(z_2).

Its actual inverse IMAGE factor is F(predecessor)/F(target),
since both sides keep the same tail after three letters. Products
therefore telescope: every full control arrow from w to z has
c_r=log F(w)-log F(z). Thus EVERY control time group is zero.
This is its own coboundary clock, not the main deletion clock.

ALL fixed words of this control are (Q,Q,1,eta), Q!=0,
with arbitrary infinite eta. Indeed fixedness first gives P=Q,
so division has quotient 1 and remainder 0; it then forces U=1.
Conversely these words are fixed. Each has source AND extension
fixed-object isotropy Z despite H=0. Terminal isotropy is trivial.
Other source periods are not classified; the all-state zero-time
claim follows from the global coboundary, not a return census.

The realised PROVES_TOO_MUCH risk is fixed unit returns and
unbounded remainder multiplicity under a declared alphabet law.
Positive time here depends on letter consumption and that law;
coefficient arithmetic alone does not establish the desired clock.
Changing weights, deleting units, selecting R=0 or retaining a
different output tuple changes the owner and requires a fresh card.

## 7. Gate assessment and decision

| Gate | Same-object evidence | Status / limit |
| --- | --- | --- |
| T0 | Full polynomial domain, all inverse branches, terminals and etale tail topology | ESTABLISHED non-LCH owner |
| T1 | Exact constant-divisor interface; complete product measure and IMAGE clock | SCOPED MEASURED RESULT; stronger naturalness OPEN |
| T2 | ALL fixed words, full isotropy image and actual nonmerging | ESTABLISHED FIXED FAMILY; unit/time/multiplicity target FAILS |
| T3 | No trace/zeta/determinant/operator | NOT SUPPLIED / NOT PURSUED |
| Classical A0/A1/A2 | No classical symplectic realization | NOT APPLICABLE; formal coordinates UNASSIGNED |
| Route B | No formal readiness or evaluation | NOT INVOKED |

Portfolio: **stop target promotion / fork**. The unit log-16
packets already decide the gate; the constant-prime clock and
remainder multiplicity independently reinforce it. No higher-period
census, retuned law or analytic rescue follows. The full same-object
ledger remains intact. A separate finite factor-refinement/gcd-word
definition is only pending input in the [scout record](evidence/scout-record.md),
not another result or an alteration of this candidate.

## Reproducibility and internal review

The proofs are exact over all polynomial degrees, coefficients,
tails and tested fixed words. There is no cutoff, precision setting,
scientific computation or external data. The alphabet law is a
declared input; ownership does not make it natural or unique.
[Evidence](evidence/README.md) records input/output locks, methods
and Markdown QA; see the [claim ledger](claim-ledger.md),
[package index](README.md) and [internal review](evidence/independent-review.md).
ARS uses raw-card, manuscript and final adverse checkpoints with
inherited-model/shared-context limits, not external peer review or
independent-error evidence. Historical packages/mirrors are unchanged;
241/242 paused; programme goal active. Markdown only.
