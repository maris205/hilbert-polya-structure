# ATA01 — card-only independent raw proof

Candidate `ANG-AUDIT-20260922-ATA01`; Paper403, round4/5 of
`NONLINEAR-RETURN-20260922-K`. Reviewer `/root/nonlocal_source_review`.
2026-09-22. Root read all90 CP1 lines and explicitly released mathematics.
candidate-card.md SHA256 798ef503ad37a6204ab611af6ddea3263f10fffb7e426eefe560be2e54e6a380
scope-review.md SHA256 f2405bb4a4c59856b8c3457da4f294ed71857c0750b0f16e8c714e2f2913c45b
The entire74-line card was reread and checked before this derivation.
No403 manuscript, package README, ledger, author proof, peer proof or399
result was read. Only root release/path-control messages were received.
Earlier shared reviewer history remains exposed: internal NOT_CALIBRATED,
not blind, cross-model, human or external peer review. No helper was used.
All mathematical arguments needed here are supplied below, not inherited.

## 1. The full affine fibre, every sheet and exact IMAGE

For an integer nonsingular n-by-n matrix A, put d=abs(det A)>=1.
The lattice quotient Z^n/AZ^n has exactly d elements: a fundamental
parallelepiped for AZ^n has Euclidean volume d, compared with volume1 for
Z^n. Equivalently elementary integer row/column diagonal reduction gives
the same index. Thus f(v)=Av+b on T^n is surjective with exactly d distinct
preimages of EVERY point, including all coordinate-cut boundary points.
Given lifts of w,b and coset representatives a of Z^n/AZ^n, they are

    v=[A^(-1)(w_lift-b_lift+a)].                       (1)

Changing lifts permutes the complete list. The derivative of f in every
flat local chart is A, so its forward local volume Jacobian is d at every
point. Each actual local inverse germ has Jacobian1/d. This is true at
every preimage, not an a.e. selection of a value on a singular base set.

Choose target lifts in [0,1)^n and a fixed coset list. Formula(1) gives d
global Borel inverse sections s_a, whose images partition the whole fibre.
A cut-selected section need not be continuous on its cuts; the claim about
its Jacobian concerns the actual smooth local inverse germ. Partitioning
the chosen lifts into affine pieces and using ordinary linear volume change
gives, for normalized Haar measure m_n and EVERY Borel E,

    m_n(s_a E)=m_n(E)/d,
    m_n(f^(-1) E)=sum_a m_n(s_a E)=m_n(E).             (2)

For an arbitrary source Borel V, partition it by these sheet images. If
N_V(w)=#{v in V:f(v)=w}, summing their injective IMAGE identities gives

    d m_n(V)=integral N_V(w) dm_n(w).                  (3)

Only for injective V does (3) reduce to m_n(fV)=d m_n(V). It does NOT
say this for overlapping images of several sheets. Thus all-sheet Haar
transport is invariant although the pointwise forward Jacobian is d.
The frozen step prescription tau=log d belongs to the latter geometric
Jacobian; it is not log of the all-sheet Haar transport density, which is1.

These constructions apply separately at each legal base state x, with
A(x),b(x). Since the set of integer matrices is countable, fixed coset lists
and Borel choices of lifts yield a countable Borel sheet description over
the given countable base inverse branches. Every base predecessor and every
fibre solution remain. There is no measure or smooth volume asserted on
the standard-Borel base X or on all Y. Equations(2)–(3) are fibre statements,
not an invented product-measure IMAGE law. A terminal has no actual step.

## 2. Exact prefixes, all actual arrows and all three kernels

For a valid k-step base history starting at x, set B_0=I, beta_0=0,
and recursively, with x_j=T^j x,

    B_(j+1)(x)=A(x_j) B_j(x),
    beta_(j+1)(x)=A(x_j) beta_j(x)+b(x_j),
    D_k(x)=abs(det B_k(x))=product_(j<k) abs(det A(x_j)).

All torus sums are intrinsic because the matrices are integral. Hence

    F^k(x,v)=(T^k x, B_k(x)v+beta_k(x)),
    S_k(x,v)=log D_k(x).                              (4)

Each affine prefix has all-point local Jacobian D_k, exactly D_k sheets,
and all versions of (2)–(3) with d replaced by D_k. No content reduction,
centre selection or extra arithmetic roof enters (4).

For z=(x,v), w=(y,u), an arrow (z,k-l,w) exists precisely when the valid
histories obey BOTH

    T^k x=T^l y,
    B_k(x)v+beta_k(x)=B_l(y)u+beta_l(y) in T^n.         (5)

Its clock is c=log(D_k(x)/D_l(y)). Another witness for the same endpoints
and lag has both indices shifted by a common integer. Extending the shorter
pair adds the identical clock sum from the common FULL state; the longer
pair certifies legality. The extra terms cancel. Thus c descends to the
equal-triple quotient, including histories terminating after the witness.
Aligning middle times proves composition and additivity, and reversal gives
the inverse clock. The actual forward arrow z->Fz has lag-1 and clock-tau(z).
This sign is the given common-tail convention, not a new clock prescription.

The complete global kernels, always subject to (5), are exactly

    ker c:   D_k(x)=D_l(y);
    ker lag: k=l;
    their intersection: both conditions.              (6)

These conditions are witness independent. Neither kernel is declared units
for a general noninjective owner; unit-degree histories can also give
nonzero-lag zero-clock arrows. For a specified source w, all arrows into
all its common-tail relatives arise by taking EVERY valid forward l at w,
EVERY legal base inverse history of length k to T^l y, and all D_k fibre
solutions of the second equation(5). This is the full incoming description,
including every retained base boundary and terminal; no new branch is added.

## 3. Entire isotropy, all real phases and primitive time

For any deterministic partial map, a nonzero-lag isotropy triple forces
some forward tail to be periodic. If z has no periodic tail, source isotropy
is {0}; this includes terminating histories. If its tail has least FULL
source period q, source isotropy is exactly qZ: every equality of two tail
times has difference divisible by q, and all multiples occur. Let C be
the sum of tau over that least cycle. Preperiod sums cancel, so

    c(z,jq,z)=jC,
    H_z=CZ,
    Iso_ext(z,h)={jq:jC=0}.                           (7)

In the non-eventually-periodic case both isotropies and H are trivial.
Formula(7) holds at EVERY h. The sums defining C are nonnegative; if C>0,
the least physical period is C and extension isotropy is trivial. If C=0,
the source isotropy remains upstairs but H={0}; there is no positive period.

Height translation commutes with every groupoid arrow. At an anchor z,
(z,h) and (z,h+t) are equivalent exactly when t is an isotropy clock.
For an arrow g:z->w, the phase of (w,h) is h-c(g) modulo H_z; different
choices of g differ by H_z. Thus each ENTIRE source orbit, with all incoming
trees and all real heights, owns one transitive physical orbit R/H_z.
Distinct periodic cycles cannot merge through incoming histories: two
periodic states with a common forward tail lie on the same actual cycle.
Equal times therefore do not merge packets. No quotient-manifold structure,
strictly positive global suspension roof or non-Zeno assertion is inferred.

Fix a least base cycle of length ell at phase x0. Its exact monodromy is
g(v)=Bv+beta with B=B_ell(x0), beta=beta_ell(x0), Q=abs(det B).
A least g-period r produces a least FULL source period ell*r: projecting
a full return to the base forces a multiple of ell, and minimality of r
then forces that multiple. Its primitive cycle clock is

    C=r log Q,  H=(r log Q)Z.                         (8)

One g-cycle gives one F-cycle; its ell phase fibres do not multiply packets.
Conversely an F-cycle intersects this chosen phase in one g-cycle. The
individual noninvertible phase maps cannot merge distinct periodic cycles.
Equation(8) and all incoming preperiods therefore describe the WHOLE H,
not merely a subgroup selected from a larger return group.

## 4. Periodic-point existence: exact torsion equivalence

Let C_B=(I-B)T^n. This is a closed connected image subtorus: the integer
matrix's real image is a rational subspace, whose quotient by its full
integer lattice is the image torus. Equivalently integer diagonal reduction
identifies the image as a torus subgroup. Put pi:T^n->T^n/C_B.
Since pi(Bv)=pi(v), the induced affine action is translation by pi(beta).
Thus g^r(v)=v implies r*pi(beta)=0. Torsion of pi(beta) is necessary.

For sufficiency, suppose m*pi(beta)=0 for an integer m>=1, so m beta is
in C_B. Multiplication by m is surjective on C_B: if c=(I-B)u, choose
u' with m u'=u, and then m(I-B)u'=c. Choose c in C_B with mc=m beta.
Set delta=beta-c. Then m delta=0. Choose a with c=(I-B)a; conjugacy by
the full-torus translation v->v+a changes g to

    h(v)=Bv+delta.                                    (9)

The finite NONEMPTY grid T^n[m]={v:mv=0} is preserved by h. Any map on a
nonempty finite set has a periodic point, by repeating the forward sequence
and taking its cyclic tail. No invertibility modulo m is needed here.
Conjugating that point back proves sufficiency. Consequently

    Per(g) nonempty  <=>  pi(beta) is torsion.         (10)

The fixed-point case is sharper: g has a fixed point exactly when
pi(beta)=0, by solving (I-B)a=beta. Nonzero torsion need not permit a fixed
centre; the sufficiency proof used a torsion residual translation instead.
No expanding assumption, invertibility of I-B, diagonalizability or omission
of root-of-unity directions was made. Irrational beta may or may not have
torsion projection; the condition concerns the quotient class, not its lift.

For complete periodic degeneracies, write beta_r=sum_(j=0)^(r-1) B^j beta.
The exact sets are

    Fix(g^r)={v:(I-B^r)v=beta_r};
    P_r=Fix(g^r) minus union_(d|r,d<r) Fix(g^d);
    E_r=union_(k>=0) g^(-k)(P_r).                     (11)

Each nonempty fixed set is a FULL coset of ker(I-B^r), including all
finite components and positive-dimensional parts. P_r gives least period;
E_r gives all points with least eventual period r. All other points are
non-eventually-periodic. These predicates cover nonexpanding and degenerate
cases rather than replacing a component with one representative.

## 5. No nonempty positive ledger meets BOTH prime conditions

First Q=1 gives C=0 in (8), for every fibre period, and no positive packet.
For Q>1 with no periodic fibre point, there are also no eventually periodic
full states over this cycle and no positive packet. Empty positive data
may satisfy the two conditions vacuously, but do not provide prime coverage.

Now suppose the FULL owner's positive ledger is nonempty and every positive
primitive is log of an ordinary integer prime. Pick one actual periodic
cycle in a positive source orbit. Formula(8) says its multiplier is Q^r.
Since Q is a positive integer, primality forces Q=p prime and r=1.
The corresponding g therefore has an ACTUAL fixed point a. Translation
v=a+u conjugates g on the ENTIRE torus to u->Bu.

Choose M=p+1, so gcd(M,det B)=1. The translated finite grid
a+T^n[M] has M^n>1 distinct points. B is bijective on T^n[M]: the integer
adjugate and the inverse of det B modulo M give its inverse modulo M.
Every point of this grid is therefore periodic under g. This is a witness
subset of the retained full carrier, not a replacement carrier.
If any grid point has least g-period r'>1, it gives a primitive multiplier
p^(r'), composite, contradicting the first condition. Otherwise ALL grid
points are fixed. At least two distinct fixed points then give different
F-cycles and different primitive packets of time log p, contradicting the
second condition. Their incoming trees cannot identify them by Section3.

Thus no owner in this frozen affine-full-fibre class can have a NONEMPTY
positive ledger satisfying both stated necessary conditions. This does not
say that every affine map has periodic points, that every positive ledger
already fails the first condition alone, or that an empty ledger is prime
coverage. If pi(beta) is nonzero torsion and Q>1, all existing fibre cycles
have r>=2 and hence already have composite multipliers. The proof treats
each owned base cycle without inserting prime coefficients into the object.
It provides an admission obstruction, not full prime coverage or a result
for nonlinear fibres or geometry-dependent base permission.

## 6. Shared notation for the THREE separate controls

Each control has its own normalized Haar volume and local forward determinant2.
All their inverse sheets have Jacobian1/2 and satisfy(2); all-sheet transport
preserves their OWN Haar measure. Every j-step inverse has 2^j sheets, each
of Jacobian2^(-j), and arbitrary source sets satisfy the multiplicity law(3).
Let a=sqrt2, h=log2, and D_2=Z[1/2]/Z, the dyadic subgroup of the circle.
For all actual arrows in EACH control, c(z,k-l,w)=(k-l)h, because its OWN
step Jacobian is2. Consequently ker c=ker lag=their intersection, namely
the synchronous common-tail relation at lag0; it is not generally units.
At a point with least eventual full period q, source isotropy is qZ,
extension isotropy is0, H=qhZ and primitive L=qh. At other points both
isotropies and H are0. All phases are given by Section3 with c=(k-l)h.

## 7. S: the full affine circle

F(x)=2x+a. Use the bijective full-circle coordinate u=x+a, so u(Fx)=2u.
For every j>=0,

    F^j x=2^j x+(2^j-1)a,
    F^(-j){y}={[(u(y)+m)/2^j-a]:0<=m<2^j}.           (12)

Formula(12) lists every incoming inverse at depth j. Every common-tail
arrow is exactly a triple with 2^k u(z)=2^l u(w) modulo1, with all k,l>=0.
At lag0 this means z-w in D_2. Thus all three kernels are exactly
{(z,0,w):z-w in D_2}; for example a difference1/2 gives a nonunit arrow.

Periodic x are exactly those with u(x) rational of odd reduced denominator d.
Indeed period r means (2^r-1)u(x) is an integer. Conversely multiplication
by2 permutes residues modulo odd d and has a finite order. With ord_1(2)=1,
the least period is ord_d(2). Eventual periodicity is exactly u(x) rational:
a denominator2^e d becomes odd after e doublings, whereas an eventual
periodic equality makes 2^e(2^r-1)u(x) integral. Its least eventual period
is ord_d(2). Irrational u has no eventual period.

The fixed set is {[-a]}. The exact-two set is {[1/3-a],[2/3-a]}, one
two-cycle. For any r the entire least-period set is described by
(2^r-1)u=0 excluding all the analogous proper-divisor conditions.
Its r points per source cycle yield ONE packet per r-cycle, with H=rhZ
and primitive r log2; all incoming rational tails join their actual cycle.
The fixed packet is primitive log2. The distinct two-cycle packet is
primitive log4, not a repetition of the fixed packet, so the prime-time
condition fails. All irrational source orbits instead own full phase lines R.
Equations(12), the arrow criterion and Section6 give every other source/
extension stabilizer, every kernel arrow and every real phase without a
finite-cutoff assertion. Haar, full source circle and every sheet stay intact.

## 8. R: the full torus with rational translation

F(x,y)=(2x,y+1/2). Its own complete iterates and inverse lists are

    F^j(x,y)=(2^j x,y+j/2),
    F^(-j){(u,v)}={([(u+m)/2^j],v-j/2):0<=m<2^j}.    (13)

An arrow (z,k-l,w), z=(x,y), w=(u,v), exists exactly when
2^k x=2^l u and y-v=-(k-l)/2 modulo1. At lag0, all three kernels are
exactly x-u in D_2 AND y=v. Nonunit dyadic equal-tail arrows are retained.

Periodic points have arbitrary y and x rational of odd denominator d.
Their least full period is lcm(ord_d(2),2): the doubling return and the
half-translation return must BOTH occur. Eventual periodicity means x
rational with any reduced denominator2^e d, y still arbitrary; the least
eventual full period is the same lcm. If x is irrational, no periodic tail
exists. Thus all positive primitive times have an EVEN q>=2 and equal
q log2=log(2^q), composite; no positive packet has prime multiplier.

There are NO fixed points. The exact-two set is
{0,1/3,2/3} times the FULL circle of y values. The x=0 circle gives
two-cycles (0,y)<->(0,y+1/2), parameterized by y modulo half-translation.
The other two circles give (1/3,y)<->(2/3,y+1/2), with one such cycle
for every y modulo1. These are continuum many DISTINCT primitive log4
packets, not selected representatives of one packet or repeats of fixed
packets. All their source isotropy is2Z, extension isotropy0 and H=2hZ.
For all higher eventual periods and all aperiodic points Section6 applies.
Every inverse in (13), all common tails, all Haar sheets and all real
height phases remain; separate cycles cannot merge through preimages.

## 9. I: the full torus with irrational translation

F(x,y)=(2x,y+a). Its own formulas are

    F^j(x,y)=(2^j x,y+ja),
    F^(-j){(u,v)}={([(u+m)/2^j],v-ja):0<=m<2^j}.       (14)

A full common-tail arrow exists exactly when 2^k x=2^l u and
y-v=-(k-l)a modulo1. Its clock is (k-l)h. Hence all three kernels are
again exactly the lag0 relation x-u in D_2 AND y=v. They are nontrivial
relations even though no nonunit isotropy exists.

No positive r has ra integral, so there are NO periodic points and NO
eventually periodic points, irrespective of the first coordinate. In
particular fixed and exact-two sets are empty. Every source isotropy,
extension isotropy and H is{0}; every source orbit owns a full phase line R.
The positive primitive ledger is empty, not a successful prime realization.
The step clock is nevertheless h>0 everywhere, and there are all inverse
histories in (14) and nonzero-lag arrows between different source states.
All-sheet Haar invariance does not replace that clock by0. Conversely a
positive step clock does not manufacture a closed physical return. All
real phases and every retained point are covered by the stated formulas.

## 10. Scoped result and freeze boundary

The torsion criterion(10) is proved with all degeneracies allowed. The
nonempty two-condition admission test fails for the full affine-fibre
class, by(8) and the finite invariant witness argument, not by importing399.
The three assigned controls each retain their own Haar transport, full
carrier, clock, exact period predicates, kernels, isotropy and real phases.
No base probability, preferred section, restricted torsion carrier, new
prime source, operator, nonlinear-fibre no-go or global smooth Y was added.
Naturalness not established; classical NOT APPLICABLE; T3 NOT AUDITED;
formal UNASSIGNED; Route B NOT INVOKED. No novelty or target-coverage claim.
No scientific numerics, external lookup, Git mutation, PDF or publication.
CP2/CP3 have not occurred. Freeze this raw before any manuscript unlock.

EOF — independent raw complete; await root read and separate PAPER UNLOCK.
