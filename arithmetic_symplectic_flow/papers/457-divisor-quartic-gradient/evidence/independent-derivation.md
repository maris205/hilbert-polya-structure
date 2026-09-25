# DQG01 — card-only independent raw derivation

Date: 2026-09-24. Candidate `ANG-20260924-DQG01`.
Batch `RECURRENCE-OWNER-20260924-V`, round 3/5, exactly 455–459.
Author of this report: `/root/algebraic_henon_author`, separate reviewer.
Same-model/shared-history AI derivation: **NOT_CALIBRATED**.

## 1. Release, inputs, and bounded conclusion

Root separately released raw mathematics after reporting its full 102-line
CP1 read. I then reread the entire unchanged card, lines 1–92 through its
explicit EOF; `wc -l` and SHA256 matched the frozen input.
candidate-card.md — 92 lines — SHA256 a47a223d611a59ba999d10664b2262f7eac8c012bbd32539843fafff4f85771a.
scope-review.md — 102 lines — SHA256 53888e7047bbccb318f270b8fbdd2ecd8d28cce401bb93470b20a789d6d65df5.
Only that card supplied current science. No author paper, README, ledger,
outcome append, peer/helper answer, sibling result, or old proof was read.
ARS router/deep-research/runtime/DA/fallacies/anti-leakage and local guidance
were fully read at this CP1 as documented there, and retained for this phase.
Prior shared history and the card's disclosed informal design exposure remain;
this is not blind, external, human, or cross-model verification.

The complete fixed sets in W are: MAIN empty; G only (0,0); Q only
(sqrt(2),-sqrt(2)). The prelisted two-state word is a legal least-period-two
orbit for MAIN and G, with full primitive log 25, but is not a Q orbit.
Thus MAIN fails its necessary prime target on its own retained packet.
Below, all inverses, incoming points, and clock groups use the whole X,
not the test square. No other periodic census is performed.

## 2. Full derivative, own domains, and arithmetic interface

Write z=(x,y), X=R², m=floor x, n=floor y, and mu=Lebesgue area.
Direct differentiation of the frozen polynomial gives F_q=grad V_q and

    DF_q = [[3x²+q y², 2qxy+1], [2qxy+1, 3y²+q x²]],
    Delta_q = 3q(x⁴+y⁴)+(9-3q²)x²y²-4qxy-1.              (1)

The derivative holds q fixed and contains both coordinate directions.
For Q the map is F_0 and its determinant is Delta_0=9x²y²-1, regardless
of the quotient witnessing its arithmetic permission. In particular q=0
is not automatically a critical branch for any owner in this card.

Let C_mn=[m,m+1)×[n,n+1). MAIN's q source is the union of C_m,qm over
nonzero integers m, intersected with {Delta_q!=0}. G uses the union of
C_mn with m!=0 and floor(n/m)=q, plus the m=0 cells for q=0, intersected
with its own {Delta_q!=0}. Q uses the union of C_mn with m!=0 and m|n,
intersected only with {Delta_0!=0}. These are Borel sets and determine
unique actual quotients for MAIN/G. Q has only its one polynomial F_0.
Each partial T is Borel, with all excluded points still objects and no
outgoing step. Nothing restricts the target to be another legal source.

For the proper-divisor seed x=d,y=N, d,N integers with 1<d<N, any allowed
MAIN quotient is q=N/d>=2. G's quotient is q=floor(N/d)>=1. In both cases
q<=N/d, and rewriting (1) gives

    Delta_q = 3q N²(N²-q d²)+9d²N²+3q d⁴-4q dN-1
            >= N²(9d²-4)+3q d⁴-1 > 0.                 (2)

Here N²-q d²>=N(N-d)>0 and 4q dN<=4N² justify the bound.
Q has Delta_0=9d²N²-1>0. Thus MAIN's actual seed admission is exactly
d|N, Q retains this admission, and G admits every such seed without it.
This verifies the stated arithmetic interface without inserting primes.
Strong naturalness of the chosen formula, readouts, and measure is not proved.

## 3. All actual inverse roots and every-point IMAGE

For any target Y=(u,v), MAIN/G enumerate every integer q and every real
solution of the two displayed frozen equations F_q(x,y)=(u,v). Keep a
solution exactly when it has that owner's actual q, permission where
applicable, nonzero own Delta, and forward equality. Necessity follows
by taking the quotient at an actual predecessor; sufficiency is substitution
and the own source test. This is an exact relation, not a finite-root or
principal-root algorithm. Zero/negative q and all real roots are included.

Q instead solves the single real equation

    (u-x³)³+x-v=0,          y=u-x³,                     (3)

then applies only Q's own arithmetic/Delta_0 tests. The first coordinate
of F_0 gives y, and the second gives (3), proving both directions without
discarding roots. No unused quotient labels multiply Q's predecessors.
Actual points, not equation labels, are deduplicated. Denote each owner's
complete predecessor relation by P_O(Y), O=M,G,Q.

For every fixed polynomial use the card's rational-ball order. At each
regular source, the analytic inverse function theorem supplies an injective
open neighborhood. A rational ball containing the source has closure
inside that neighborhood and the regular locus; hence eligible balls cover.
Intersect with actual source-label sets and subtract earlier eligible pieces.
This yields a countable disjoint Borel partition of each legal source.
For Q this construction uses F_0 once, not separate unused q copies.

On each eligible ball F_q is an analytic diffeomorphism to an open image.
An actual Borel source piece has Borel image, and its inverse theta is the
restriction of the analytic inverse. The resulting atlas equals the complete
root relation just proved. Each actual inverse fibre is at most countable,
because every partition piece contributes at most one predecessor.

At every actual inverse point prescribe

    J_theta(Y)=1/|Delta_actual(theta Y)|,
    mu(theta E)=integral_E J_theta dmu                  (4)

for every Borel E in the actual image piece. The inverse derivative gives
the first identity and ordinary change of variables on the ambient ball,
restricted to E, gives the second, allowing extended integrals. J is finite
and strictly positive. Two inverse germs through the same actual source
and active polynomial agree locally by uniqueness. Assigned floor faces
use that same active germ, not a limit from a different quotient cell.
Thus (4) is a specified all-point version even at null periodic points;
the measure identity alone is not asserted to determine such a version.

Consequently the own clock is exactly

    kappa_O(z)=log|Delta_actual(z)|                    (5)

on its legal domain, with all signs and zero values retained. Terminals have
no step clock. Countable branches and (4) also prove nonsingularity of T:
the preimage of a null set is a countable union of null inverse images.
No invariant-measure or globally invertible/symplectic claim is implied.

## 4. Whole histories, kernels, and terminal classes

The following proof is applied to each own T, never with another owner's
domain or determinant. Let D_r be the domain of r legal iterates, D_0=X,
S_0=0, S_r(z)=sum_{j=0}^{r-1} kappa(T^j z), and
M_r(z)=exp S_r(z)=product_{j=0}^{r-1}|Delta_actual(T^j z)|, M_0=1.
All nonempty sums/products are used only on their actual legal domains.

G consists of all (z,r-s,w) with z in D_r, w in D_s, T^r z=T^s w.
Source is w, range z, and equal triples are identified with integer lag
retained. For each lag the relation is a countable union of equality sets
of Borel maps, so G is a Borel groupoid. Inversion reverses endpoints/lag.
To compose witnesses (r,s) and (u,v), advance the middle histories to
L=max(s,u). The combined witness is (r+L-s,v+L-u), which is legal because
the longer middle history exists and common endpoints evolve identically.

For a triple g=(z,r-s,w), define

    c(g)=S_r(z)-S_s(w)=log(M_r(z)/M_s(w)).             (6)

Any other witness for the same lag differs by equal additions to r and s;
the common endpoint's extra sums cancel. Thus c descends. The same
middle-history alignment cancels its sum in a product and proves additivity.
The actual forward arrow (Tz,-1,z) has c=-kappa(z).

Refine finite histories into actual atlas pieces. An arrow branch is locally
(T^r)^(-1) T^s with modulus M_s(w)/M_r(z)=exp(-c(g)). Chain rule and
change of variables on the corresponding smooth germs give every-Borel
IMAGE on each actual history piece, including its inherited cut version.
The clock is therefore the modulus of this same geometric history owner.

The complete source-groupoid kernels are

    K_lag = {(z,0,w) in G},
    K_c = {(z,r-s,w) in G : M_r(z)=M_s(w)},
    K_joint = K_lag intersect K_c.                   (7)

No kernel is generally reduced to units or inferred from word labels alone.
On the whole X×R, g:w->z acts by (w,h)->(z,h+c(g)); the extension's
height-preserving arrows are exactly those based on K_c. Its lag-zero
arrows lift K_lag, and imposing both conditions lifts K_joint.

For every Y in X, including terminals/cuts/critical points, put
P_O^0(Y)={Y}, P_O^(j+1)(Y)=union_{Z in P_O^j(Y)} P_O(Z).
Induction identifies this with all actual depth-j predecessors. No incoming
source is restricted to W or to the sign/labels of its target. Compatible
infinite backward histories, when present, are precisely successive choices
Y_{j+1} in P_O(Y_j); recording them does not create extra objects or arrows.

If e is a terminal, its entire source orbit is union_j P_O^j(e).
A point z therein has a unique hitting depth d(z), because no step after e
exists. The only lag between z,w is d(z)-d(w), and its clock is
S_{d(z)}(z)-S_{d(w)}(w): any earlier coalescence can be extended to e.
Thus its lag, clock, and joint kernels impose respectively equal depths,
equal entry sums, or both. Its isotropy is trivial and its complete extension
phase is h-S_{d(z)}(z) in R. Terminal status never removes these incoming data.

## 5. Entire isotropy, real phases, and primitive convention

For any deterministic partial map, a nonzero isotropy lag occurs exactly
when two unequal legal iterates of a point coincide, equivalently when its
forward history is eventually periodic. If the eventual least period is p,
extending any witness to the periodic tail shows its lag is a multiple of p;
conversely all multiples occur by adding full turns. The source isotropy
is pZ. If the signed sum around the least cycle is C, entry sums cancel and

    c(kp)=kC,       H=c(Iso_G(z))=CZ.                 (8)

This is the entire image, not the subgroup contributed by one displayed
word. Identified inverse labels cannot add free isotropy to actual triples.
Extension isotropy is all pZ if C=0 and trivial if C!=0.
Non-eventually-periodic orbits, including terminal-ending ones, have trivial
source/extension isotropy and H={0}; their inter-object clocks may be nonzero.

For any source orbit choose a base b and an actual arrow a_z:z->b.
The complete extension-orbit coordinate is h+c(a_z) modulo H_b.
Another arrow changes it by an isotropy clock; conversely equal coordinates
modulo H_b provide an isotropy arrow and hence an extension connection.
This is an orbitwise description, not a global selector or nice quotient.
Height translation has stabilizer exactly H_b. For (8) with C!=0 it gives
one closed packet over the whole source orbit, primitive |C| and repetitions
j|C| for all positive integers j. For C=0 its phase is R and there is no
positive return, despite the retained source/extension isotropy.
Distinct source orbits remain distinct even when their positive lengths agree.

## 6. Complete fixed-point test in the closed W=[-2,2]²

For an actual MAIN/G fixed point first use its active integer q. Adding
and subtracting the two fixed equations, with s=x+y and d=x-y, gives

    s[(q+1)s²+(3-q)d²]=0,
    d[(3-q)s²+(q+1)d²-8]=0.                           (9)

These are equivalent to the fixed equations by invertible addition and
subtraction, and cover all axes, signs, diagonal cuts, and square boundary.
We classify their algebraic branches before imposing actual floors/guards.

(a) If d=0, either x=y=0 or q=-1 and x=y=t. For t!=0 the actual
equal floors give q=1 when m!=0; when m=0 MAIN is illegal and G gives 0.
Thus the formal q=-1 line supplies no actual nonzero fixed point.
At the origin MAIN is illegal (m=0), whereas G uses its actual q=0.

(b) If s=0 and d!=0, x=t,y=-t with (q+1)t²=2. Thus q>=0 and
|t|=sqrt(2/(q+1)). At q=0, 1<|t|<2: for t>0 the actual quotient
is -2, while for t<0 MAIN fails divisibility and G gives -1, not 0.
At q=1, |t|=1 and both actual quotients are -1, not 1.
For q>=2, 0<|t|<1: t>0 has m=0 (MAIN illegal, G quotient 0);
t<0 has m=-1,n=0 and quotient 0. None realizes its proposed q.

(c) If s,d are both nonzero, q=1 is inconsistent in (9). Otherwise

    s²=(q-3)/(q-1),       d²=(q+1)/(q-1).             (10)

Both are strictly positive only for integer q<=-2 or q>=4; the zero
endpoints q=-1,3 belong to earlier cases. In either allowed range
x²+y²=1, xy=-1/(q-1), so each coordinate is nonzero and has modulus <1.
For q<=-2 the signs coincide: both positive give m=n=0, both negative
give m=n=-1. MAIN is illegal or gives 1; G gives 0 or 1, never q<=-2.
For q>=4 the signs differ: positive x gives m=0 and negative x gives
m=-1,n=0. MAIN is illegal or gives 0; G gives 0, never q>=4.

This exhausts (9) inside the frozen W, including all its boundary points.
At G's remaining origin, DF_0=[[0,1],[1,0]], Delta_0=-1, so it is legal.
Consequently Fix_W(M)=empty and Fix_W(G)={(0,0)}. No global fixed-set
claim outside the frozen window is needed or used as an additional census.

For Q the polynomial is F_0, independently of arithmetic quotient.
Setting q=0 in the exhaustive algebraic cases leaves only (0,0) and
(sqrt(2),-sqrt(2)), (-sqrt(2),sqrt(2)), all in W.
The origin has m=0 and is illegal. The positive-first point has (m,n)=(1,-2)
and passes divisibility; the negative-first point has (-2,1) and fails it.
At A_Q=(sqrt(2),-sqrt(2)), Delta_0=35, so

    Fix_W(Q)={A_Q},       kappa_Q(A_Q)=log 35.         (11)

The unused arithmetic quotient -2 does not enter Q's determinant.

## 7. The prelisted two-state word, independently in each owner

Write P=(1,-1), R=Q0=(-1,1) to distinguish the second state from control Q.
At P and R, MAIN's arithmetic and G's quotient both give q=-1; both MAIN
permissions hold. Direct substitution yields F_-1(P)=R, F_-1(R)=P.
Their own derivative at both states is [[2,3],[3,2]], with Delta_-1=-5.
They are distinct legal states, so their source least period is exactly 2,
with each step kappa=log 5 and signed cycle sum 2log 5=log 25.
Their presence on integer cuts invokes exactly the prescribed actual germs.

Q separately has permission at both states and Delta_0=8 there, but
F_0(P)=F_0(R)=(0,0). Thus neither required arrow of the listed word is
present for Q. The target origin is a Q terminal, not an added fixed loop.
These are statements about the frozen word only, not a period-two census.
In Q, both listed states have depth one and entry clock log 8 into the
terminal class of 0. The actual arrow (P,0,R) has clock zero but is not
isotropy, an explicit instance of the retained non-unit kernels in (7).
The complete Q terminal class is union_j P_Q^j(0), with all its depths,
entry clocks, real phases, and trivial isotropy as proved in §4.

## 8. Complete incoming packets and their full kernels/phases

For the MAIN and G two-cycle set C={P,R}; for G's fixed origin use C={0};
for Q's fixed point use C={A_Q}. For each owner/core separately define

    B_0=C,   B_(j+1)=union_{Y in B_j} P_O(Y),
    B=union_{j>=0} B_j.                               (12)

Every P_O is the unrestricted all-real inverse relation from §3. Induction
proves B_j={z:T_O^j z in C legally}. These sets are nested since T permutes
the core. B is exactly its full source orbit: a coalescing history with a
core point enters C, and any point entering C has an actual core arrow.
All real incoming states at all depths are therefore covered, without a
finite enumeration, basin-singularity assumption, or restriction to W.

Each of these cores has constant step clock K and source period p:

| Owner/core | p | K | Entire H | Extension isotropy | Positive primitive |
| --- | --- | --- | --- | --- | --- |
| MAIN / {P,R} | 2 | log 5 | (2log 5)Z | trivial | log 25 |
| G / {P,R} | 2 | log 5 | (2log 5)Z | trivial | log 25 |
| G / {0} | 1 | 0 | {0} | Z | none |
| Q / {A_Q} | 1 | log 35 | (log 35)Z | trivial | log 35 |

For completeness the following gives every arrow/kernel/phase in (12),
not just core isotropy. Index the p core states c_i by T c_i=c_(i+1),
with c_0=P for two-cycles. If z first enters c_i at time e(z), put

    alpha(z)=i-e(z) mod p,
    beta(z)=S_{e(z)}(z)-e(z)K.                        (13)

Later entries give the same quantities. For z,w in this same B, every
integer k satisfying k=alpha(w)-alpha(z) mod p is realized by sufficiently
long histories in the core, and no other lag can be realized. For every
such actual triple the full clock is

    c(z,k,w)=beta(z)-beta(w)+kK.                      (14)

To prove this, use large r,s past both entry times. Equality of the core
indices is alpha(z)+r=alpha(w)+s mod p, and the sums equal beta+rK and
beta+sK. Smaller witnesses give the same value by cocycle descent.

Thus the full basin lag kernel consists exactly of k=0 with equal alpha;
its clock kernel imposes beta(z)-beta(w)+kK=0 together with the stated
lag congruence, and its joint kernel imposes k=0, equal alpha, and equal
beta. Source isotropy is the entire pZ and has image pK Z as in the table.
No incoming root label or path can produce an extra isotropy generator.

The complete real phase over this B is

    h-beta(z)+alpha(z)K mod pK Z.                     (15)

Indeed a forward path to c_0 has length ell=-alpha(z) mod p and clock
-S_ell(z)=-beta(z)-ell K, proving (15). Changing the representative of
alpha changes its value by pK. At G's zero-clock core p=1,K=0, (15)
is the real number h-beta(z), not a circle and not a positive-time packet.
Its nontrivial source/extension Z isotropy is still retained.

In a two-cycle R and P are different objects. Their odd-lag connecting
arrow with clock ±log 5 is not isotropy at P; isotropy there has even lag.
Consequently the entire height stabilizer is (log 25)Z, never (log 5)Z.
P and R, their incoming paths, all heights, and cyclic rotations belong
to one closed packet per owner, with repetitions j log 25, j>=1.
Q's fixed packet similarly has repetitions j log 35. G's zero-clock basin
is a different source orbit from its two-cycle basin and is not discarded.

## 9. Gate decision, retained limits, and reproducibility

MAIN has a fully owned positive primitive log 25, which is not the logarithm
of an ordinary prime since 25=5². It cannot be called merely a repetition
of a prime-5 packet: its own ENTIRE H has least positive generator log 25.
This one adverse MAIN primitive suffices to fail the necessary prime target
and gives STOP / FORK. The empty MAIN fixed window is not a global absence
claim and is not the reason for stopping. G and Q are diagnostic owners,
not sources of transferred credit or of MAIN's negative conclusion.

Full-source, all-point IMAGE, actual histories, zero clocks, incoming points,
phases, multiplicity, and repetitions remain on the frozen owner. Strong
naturalness, other periodic packets, and prime coverage are not established.
T0 transport/clock ownership is proved here; the necessary prime target fails.
T1 is NOT PASSED; T3 NOT AUDITED; classical NOT APPLICABLE; formal Routes
UNASSIGNED; Route B NOT INVOKED. No new candidate or later route is started.

Method: first-principles polynomial identities, exact integer/floor cases,
analytic local inverse/change-of-variables arguments, and deterministic
history proofs. No scientific code, numerical evaluation, extended period
search, external source, network, Git, PDF, or old-file write was used.
Only this raw report was written; the original card and CP1 were not edited.
Freeze after full self-read and measured receipt, then HOLD for root's full
read and a distinct PAPER UNLOCK before any author-surface comparison.
