# Nonlinear content exchange: one prime packet, not prime coverage

**Candidate:** `ANG-20260922-NER01`; paper400, 2026-09-22.
Outcome: `OWNED SINGLE LOG2 PACKET; GLOBAL PRIME COVERAGE FAILS — STOP / FORK`

MAIN has exactly one positive packet, of primitive time log2. Prime-only,
nonemptiness and at-most-one-per-prime hold; all-prime coverage fails globally.
Strong naturalness OPEN. Classical NOT APPLICABLE; T3 NOT AUDITED and no
operator assigned; formal UNASSIGNED; Route B NOT INVOKED.

## Abstract

A current floor-pair gcd changes both places of a nonlinear planar exchange.
All four frozen owners admit their complete inverse branches, every-Borel
Lebesgue IMAGE identity and prescribed all-point clocks. Their complete
one- and two-step return sets are determined. A direct strict reciprocal-box
inequality, not a longer orbit search, excludes every other MAIN cycle.
The only positive packet is log2: a genuine scoped positive result, but
not the all-prime target. The denominator-off control has a global clock
potential, including its axes, so its source isotropy survives with H={0}.
No measure, boundary version, source or phase is changed to obtain these results.

## 1. Full arithmetic source and four actual laws

The [84-line frozen card](candidate-card.md) fixes X=[0,infinity)^2 with
its usual Borel structure and two-dimensional Lebesgue mu. Put
gamma(a,b)=gcd(a,b), except gamma(0,0)=1; all d=gamma(a,b) are positive.
M, L and N read a=floor x,b=floor y,d=gamma(a,b) at the current real state.

| Owner | Actual T(x,y) | Forward terminals |
|---|---|---|
| M MAIN | (y,(d+y)/(x+d y)) | origin only |
| D CONTENT-OFF | (y,(1+y)/(x+y)) | origin only |
| L CROSS-DENOMINATOR-OFF | (y,(d+y)/x) | entire x=0 axis |
| N NUMERATOR-CONTENT-OFF | (y,(1+y)/(x+d y)) | origin only |

Each displayed denominator is positive on its active domain, so these are
unambiguous partial Borel maps into the same X. All axes, units, unbounded
points, failed divisibility readouts and half-open integer cuts remain.
Terminals have zero iterates, not fictitious absorbing loops. There is no
extra integer root, selected orbit or passive transverse coordinate.
In every cell(n+xi,m+eta), 0<=xi,eta<1 and 1<m<n, the actual content is
gcd(n,m). Thus m|n iff this content equals m, and in M that same value
changes the real numerator and denominator. The new state supplies the next
digits. This proves the stated symbolic interface, not canonical naturalness.

## 2. Full inverse domains and same-measure IMAGE

For M/L/N enumerate every a,b>=0 with its own d. At target(u,v) set:

| Owner | Reconstructed r, inverse theta(u,v)=(r,u) | J_theta |
|---|---|---|
| M | r=(d+u)/v-d u | (d+u)/v^2 |
| D | r=(1+u)/v-u | (1+u)/v^2 |
| L | r=(d+u)/v | (d+u)/v^2 |
| N | r=(1+u)/v-d u | (1+u)/v^2 |

For M/L/N the exact domain is v>0, b<=u<b+1, a<=r<a+1, r>=0,
and the reconstructed point lies in that owner's active domain. L requires
r>0; M/N exclude only(r,u)=(0,0). For D there is a single inverse with
u>=0,v>0,r>=0 and(r,u)!=0, without artificial digit labels.

These inequalities imply every frozen source check. The reconstructed
floors are a,b, so their content is the declared d. For M,
r+d u=(d+u)/v; for N it is(1+u)/v; D gives r+u=(1+u)/v.
All are positive, excluding the origin and giving the forward equality.
L has r=(d+u)/v>0 and the same equality directly. Conversely solving any
actual source equation yields exactly this inverse and its inequalities.
Thus every predecessor is included, uniquely associated with its source
digits; passing branches may overlap in target but not duplicate a source.
There are no one-step T-predecessors when the target's second coordinate is0;
these remain source objects. One-step terminal incoming is determined by the same domains,
not by whether the target itself can take a next step.

To prove the table's density, each rational inverse has the form
(C(u)/v-e u,u), with C=d+u or1+u, and e=d,1 or0 as appropriate.
Its derivative determinant is C(u)/v^2. This is positive finite on EVERY
actual point, including all cuts and axes, by u>=0,v>0,C(u)>0.
For fixed u the change v->r is strictly monotone on the ambient v>0
domain. One-dimensional substitution and Fubini, restricted to any Borel
set E in the actual domain, give mu(theta E)=integral_E J_theta dmu.
The identity allows infinite integrals. The full-point version at null
faces is the stipulated rational derivative, not a conclusion of a.e.
uniqueness. No density or measure has been reassigned in any owner.

## 3. Complete history, actual clock and global kernels

For each owner take exactly G={(z,m-n,w):T^m z=T^n w, histories legal},
source w, range z, with equal triples identified. Finite iterate domains
and equalities are Borel, hence G is Borel in X times Z times X.
At source r enumerate every legal T^n r and every finite inverse word of
length m passing its own domain at EVERY intermediate stage. If it gives q,
retain(q,m-n,r), outgoing from r; its inverse is incoming to r. This is an
exhaustive, countable enumeration, including all empty and terminal histories.

Inversion swaps endpoints and changes lag sign. To compose two witnesses,
extend the shorter intermediate history to the longer already-legal one.
The common equality gives the sum of lags, without extending past a terminal.
Equality of triples then proves associativity and witness independence.

Along a legal history put Tz_i=(y_i,v_i), and define positive q_i by
q_i=x_i+d_i y_i for M/N, q_i=x_i+y_i for D, and q_i=x_i for L.
The inverse density at Tz_i is q_i/v_i for EACH owner, using its own law
and its own numerator in section2. Consequently, with empty product1,

    K_m(z)=product_(0<=i<m) q_i/v_i,    S_m(z)=-log K_m(z),
    ell(z,m-n,w)=m-n,    c(z,m-n,w)=log[K_n(w)/K_m(z)].

All factors are positive finite, even for a last step into a terminal.
Adding the same legal common tail multiplies both K products by the same
factor. Any two witnesses of a given triple align in this way. Thus c is
all-point well-defined; aligned composition gives addition, and inverse
negates it. The actual branch-pair IMAGE density from w to z is
K_m(z)/K_n(w), by substitution through their common future. Hence this c
is the negative log of the SAME source transport, not an attached roof.

The global kernels and intersection have exact all-source tests:
ker ell is the set(z,0,w) with T^m z=T^m w for some legal m;
ker c consists of the legal triples satisfying K_m(z)=K_n(w);
their intersection has equal-depth coalescence and K_m(z)=K_m(w).
The explicit q_i/v_i formula applies to every one of these tests. They
are not assertions that either kernel consists only of identity arrows.

## 4. Source isotropy, signed returns and all phases

A source has nonzero retained-lag isotropy exactly when its actual forward
history is eventually periodic. If the eventual least cycle has length p,
the entire group is pZ; otherwise it is{0}, also for terminating histories.
Indeed an equality of two distinct iterates produces a cycle; all and only
multiples of its least period occur after the transient. No path/germ labels
produce extra stabilizers. This is an exact ledger, not a census of cycles.

Every cycle of every owner lies strictly inside X: every image has positive
second coordinate, and its first coordinate is the preceding second one.
For M/N let e_i=d_i, and for D let e_i=1, so q_i=x_i+e_i y_i.
On a cycle the product of v_i is the product of x_i. Its total clock is

    C_cycle=-sum_i log(1+e_i y_i/x_i)<0.

Here M/N use d_i and D uses1. Thus for every eventual cycle of these three
owners c(kp)=k C_cycle, H_z=abs(C_cycle) Z, and extension isotropy is
trivial. Noneventually-periodic sources have H_z={0} and trivial isotropy.
The full ker c may still connect different units; section3 gives its test.

L instead has a global positive Borel function

    b(x,y)=xy if x,y>0; b(x,0)=x if x>0;
    b(0,y)=y if y>0; b(0,0)=1.

At an interior L-step, b(z)/b(Tz)=xy/(y v)=x/v=J_theta(Tz).
At a horizontal-axis step into a vertical terminal the same equality is
x/v. No step is evaluated at a vertical terminal or the origin. Hence
c(z,k,w)=log b(w)-log b(z) on ALL actual L arrows. This is derived from
the original prescribed densities, not a new measure or null-point repair.
Thus H_z={0} for every L source, while ALL its source isotropy survives as
extension isotropy. Its global ker c is exactly b(z)=b(w) among actual
arrows, and intersection with ker ell adds the equal-depth test. Zero
return clock does not remove eventual periods or their retained lag labels.

All X times R and all arrows(w,h)->(z,h+c) remain. Height translation
commutes with these arrows. The complete time stabilizer is H_z: a time
shift fixes the quotient point exactly when an isotropy arrow supplies it.
Above each complete source orbit, all phases form R/H_z, a line for H=0
or a circle for H=L Z,L>0. An arrow w->z identifies phase h with h+c
modulo H_z; alternative arrows differ by isotropy and give the same phase.
For L this is explicitly the invariant coordinate h+log b(z), with time
acting by translation. Ineffective L source isotropy is still present.
Different actual cycles are different packets, even at equal times; a common
future would make them the same cycle. Repetitions use that cycle's generator,
not a chosen phase, a unit lag roof or equal-time identification. No nice
coarse topology or invariant product-volume flow is claimed.

## 5. Complete one- and two-step return sets

Let phi=(1+sqrt5)/2. The full results, not just a selected cell, are:

| Owner | Fix(T)=Fix(T^2) | Exact period2 | H at these cores |
|---|---|---|---|
| M | {(1,1)} | empty | log2 Z |
| D | {(1,1)} | empty | log2 Z |
| L | {(phi,phi),(2,2)} | empty | {0} at both |
| N | {(1,1)} | empty | log2 Z |

For a fixed source write x=y=t>0, n=floor t and d=max(1,n).
M's equation factors as(t-1)((d+1)t+d)=0, so t=1; D is the d=1
case. N has(d+1)t^2-t-1=0. For n=0 its positive root1 is outside
the cell; n=1 admits1; for n>=2 the polynomial at t=n is positive
and increases thereafter, excluding that whole cell. L has t^2-t-d=0:
n=0 excludes its root phi; n=1 admits phi; n=2 admits2; for n>=3,
the polynomial at n is n(n-2)>0 and increases thereafter. These exhaust
all nonnegative integer cells, with the prescribed floor values at integers.

If T^2(x,y)=(x,y), then T(x,y)=(y,x) and x,y>0. M/L/N use the
same d at both steps because gcd is symmetric. For M the equations are
x^2+dxy=d+y, y^2+dxy=d+x; for L omit the dxy terms; for N
replace the right-hand d by1. D is M with d=1. Subtraction always gives
(x-y)(x+y+1)=0. Therefore x=y and the two-step set is exactly the
fixed set already proved. No terminal identity was counted as a step.

At(1,1), each of M/D/N has its OWN inverse density2, total clock -log2,
source isotropy Z and extension isotropy{0}; least positive time is log2.
The point has only itself as predecessor: target u=1 forces b=1,d=1,
then r=1 in M/N; D's sole inverse also gives1. Thus its full source
orbit is a singleton, though every integer lag and every circle phase remain.
In L, source isotropy and extension isotropy at BOTH fixed points are Z,
but H={0}; these are not positive packets. At(phi,phi) the only predecessor
is itself. At(2,2) the exact direct predecessors are(2,2) and(3/2,2):
b=2 allows d=2 or1, and the source floor checks give precisely those two.
All further incoming is the untruncated source-checked inverse recursion of
section3, not just these first predecessors. Eventual sources in each basin
have the same least-cycle isotropy and the full phase convention above.

## 6. A short global bound: MAIN covers only the prime2

For q>1, x,y in[1/q,q], and ANY d>=1, put v=(d+y)/(x+d y).
Both denominator and all compared quantities are positive. Strict upper
and lower bounds follow from

    q(x+d y)-(d+y)=d(qy-1)+qx-y
                   >=(q-1)y+qx-1>0,
    q(d+y)-(x+d y)=d(q-y)+qy-x
                   >=q-x+(q-1)y>0.

Thus 1/q<v<q. In any finite MAIN cycle, all coordinates are positive by
section4. Let q be the maximum of every coordinate and its reciprocal over
that entire finite cycle. It is finite and >=1. If q>1, each second
coordinate, and hence each first coordinate, is strictly inside(1/q,q),
contradicting attainment of that maximum. Thus q=1 and the cycle is(1,1).
The same displayed bound with d=1 proves D's own global cycle statement.
This argument does not assert that every infinite orbit converges, or that
converging but non-eventual histories can be identified with the fixed source.

Together with the unique-predecessor proof, MAIN's entire positive ledger
is exactly ONE packet log2, including all of its real circle phases.
Every other MAIN source has trivial isotropy and H={0}. Therefore the
prime-only condition, nonemptiness and at-most-one packet per prime really
hold globally. The all-prime goal fails: there is no log3 packet, nor any
other prime packet. This is a GLOBAL COVERAGE STOP, not a nonprime or excess
multiplicity counterexample and not an inference from an empty short window.
D has the same positive ledger by its own proofs; this does not identify
the two full maps or establish arithmetic naturalness. N's larger-period
source sets are unclassified; L's global zero clock is proved without a
source-period census. Neither control convicts or repairs MAIN.

## 7. Evidence, provenance and limits

Actual scientific input: final card1–84 through actual EOF, wc84, SHA256
`2074eb5583fd84c8cfabb8ebb02160ba560e6887c1b6e493eff94c71b38d21eb`.
Root reported full CP1 readiness/release and explicitly accepted the direct
global inequality as a short structural consequence, not a census extension.
The author read no scope/raw/peer evidence or other new manuscript.
Definition inputs were395 batch-summary1–87 through EOF and320 original
card1–96, not original EOF; heading-only exposure included its outcome title159.
No320 outcome body or proof was used; no old total/hash was measured.
Prior source authorship, shared history, and pre-freeze informal unit-diagonal/
Lyness-density expectations were disclosed. This is internal NOT_CALIBRATED
work, not blind discovery, external peer review or a global novelty claim.
Retained ARS drafting guidance enforced same-owner and claim/review boundaries.
AI agents supplied the mathematical derivation and drafting; the workflow's
internal reviews are also AI-agent work. No human or external verification is certified.
All calculations are exact arguments from the card; no scientific program,
numerical orbit search, external retrieval, Git mutation, PDF or publication.
No coefficients, source, version or measure were changed after freeze.
Strong naturalness remains OPEN; no trace/operator or formal Route evaluated.
The [claim ledger](claim-ledger.md) separates the owned single-prime result,
global coverage obstruction, control outcomes and unclassified source cycles.
