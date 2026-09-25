# CPI01 — independent card-only raw proof

Candidate `ANG-AUDIT-20260923-CPI01`; Paper408, round4/5 of
`NONLINEAR-PACKET-20260923-L`. Reviewer `/root/nonlocal_source_review`.
2026-09-23. Root read all108 CP1 lines, then explicitly released mathematics.
Original75-line card prefix SHA256 e510fd67204c529c745e272cb9ac38673446efb7c2fb510321084763396fb00b
Clarified81-line candidate-card.md SHA256 2a6f1a70c08b1cfc2c434cc002c0693c8fd696ddf24326e71a312f37294dceae
scope-review.md SHA256 d1294c0b27c8ee6cadd220e3abb9c9dd7e886599d3719d269bb160863b98cbe1
The complete clarified card was reread before deriving the following proof.
No408 paper, README, ledger, author/helper proof, peer proof or404 result
was accessed. The card discloses root's design algebra and404 dependency;
these are known exposures, not independent evidence or sealed expectations.
Earlier shared history remains: internal NOT_CALIBRATED, not blind,
cross-model, human or external peer review. This reviewer used no helper.
Here “basin” ALWAYS means the clarified finite-landing/common-tail saturation,
never an asymptotic attracting basin.

## 1. All-point inverse IMAGE of the frozen germs

At every legal point z, its assigned rational germ f is holomorphic and
has a finite nonzero derivative. Its real differential has determinant
|f'(z)|^2>0. The local inverse theorem supplies a smooth inverse germ at
Tz whose real Jacobian is 1/|f'(z)|^2. On an assigned injective Borel piece
P_i, the actual inverse I_i agrees pointwise with this local germ at the
corresponding preimage; no derivative of a thin Borel set is being inferred.

Cover the legal part of each rational germ by countably many open sets on
which it is a diffeomorphism, and disjointly refine their intersections
with P_i. The images of the refined Borel parts are Borel in local charts.
Applying real change of variables and summing over that partition proves
for EVERY Borel E subset T(P_i)

    mu(I_i E)=integral_E |I_i'(w)|^2 dmu(w),
    |I_i'(w)|^2=1/|f_i'(I_i w)|^2>0.                 (1)

Values on all null points and piece boundaries are the prescribed inverse
germ values, not values deduced solely from an a.e. identity. The integral
is understood as a nonnegative Lebesgue integral, possibly infinite.
The same owner therefore supplies kappa(z)=log|f_i'(z)|^2 at every legal
z. Its sign may be positive, negative or zero. No step clock is defined
at a terminal; the empty iterate has clock0. No invariant probability,
globally injective map or common density for different inverse branches
is asserted. Each legal finite inverse history has its own chain-rule
Jacobian and its own Borel IMAGE by iterating this argument.

## 2. Full common-tail groupoid, kernels and physical phases

For a legal m-step history starting at z put
J_m(z)=product_(j<m) |f_(T^j z)'(T^j z)|^2 and S_m(z)=log J_m(z),
with J_0=1. Every factor is finite and strictly positive. Define all triples
(z,m-n,w) for valid m,n>=0 with T^m z=T^n w, retaining lag and identifying
equal triples. A second witness with the same lag changes both exponents
by the same integer. Comparing the shorter pair with the longer pair adds
the same sum from their identical common tail; the longer witness certifies
that this padding exists, including for partial maps. Therefore

    c(z,m-n,w)=log(J_m(z)/J_n(w))                     (2)

is well-defined. Aligning middle exponents proves composition/additivity;
swapping endpoints negates c. All legal histories ending at a terminal
remain. In particular the actual forward arrow z->Tz has lag-1 and
clock-kappa(z), whereas the reverse arrow has clock+kappa(z).

Subject ALWAYS to actual common-tail equality, the global kernels are

    ker c: J_m(z)=J_n(w);
    ker lag: m=n;
    their intersection: both conditions.             (3)

They need not be units or equal to one another. All incoming arrows are
obtained by taking every finite forward tail at the source and every
legal finite inverse history to that tail. No selected branch, analytic
continuation across a forbidden pole/critical point, or new germ is added.

If a source point is not eventually periodic, its source isotropy is0:
a nonzero difference of two equal forward times would create a periodic
tail. This includes terminating histories. If its least eventual cycle
period is q, its full source isotropy is qZ; every difference is a multiple
of q and all multiples occur. Write C for the signed sum around that cycle.
Preperiod sums cancel, and cyclic phase changes preserve C, giving

    c(z,jq,z)=jC, H_z=CZ,
    Iso_ext(z,h)={jq:jC=0}.                           (4)

In the non-eventually-periodic case both isotropies and H are0. If C!=0,
extension isotropy is trivial and L=abs(C) is the LEAST positive generator
of the ENTIRE H. If C=0, source isotropy qZ survives upstairs, but H={0}
and no positive physical period exists. A negative C is not discarded.

The extension contains every (z,h), h real, with the frozen arrow action.
Height translation commutes with every arrow and has stabilizer precisely
H_z on the extension orbit set. Fixing an anchor p in one source orbit,
an arrow g:p->z identifies its complete phase as h-c(g) modulo H_p.
Changing g changes this coordinate only by H_p. Thus one entire source
orbit, including all incoming states, owns one physical R/H orbit. Distinct
periodic cycles cannot be joined by incoming histories: deterministic
periodic points with a common tail are on the same cycle. Equal positive
times therefore never identify their packets. No quotient manifold follows.

## 3. Germ reflection acts on the entire owner

Write Kz=conjugate(z). D is K-invariant, so terminals are K-invariant too.
The frozen germ identity says, locally at each legal z,
f_(Kz)(u)=conjugate(f_z(conjugate(u))). It gives BOTH

    T(Kz)=K(Tz), f_(Kz)'(Kz)=conjugate(f_z'(z)).        (5)

Hence kappa(Kz)=kappa(z), and every valid history, inverse solution and
terminal history has a conjugate valid history. K preserves Lebesgue area,
so it transports(1) to the actual conjugate inverse with the same positive
Jacobian. A whole branch piece need not map to one fixed branch label;
these statements concern assigned germs at actual points, including cuts.

The map (z,k,w)->(Kz,k,Kw) is an involutive groupoid automorphism preserving
c EXACTLY, not negating it. It therefore lifts to (z,h)->(Kz,h), commutes
with real height translation and sends every complete source orbit and
physical packet to its conjugate. It preserves source/extension isotropy,
the two kernels and their intersection, H and every positive primitive
time. These assertions include all heights and nonperiodic histories.
For a K-invariant source orbit, its induced map on R/H is an equivariant
involution. It is consequently a phase translation of order at most2;
if H={0} that phase translation must be0. Paired source orbits with H=0
give paired physical lines, not a pair of positive-period packets.

## 4. Complete conjugation classification on a least-q cycle

Let O={p,Tp,...,T^(q-1)p} be an actual least-q cycle. Its conjugate is also
an actual least-q cycle, with the SAME signed C by(5). There are two cases.

If KO differs from O, they are disjoint periodic cycles and give distinct
complete source orbits, hence distinct physical packets when C!=0. Their
whole basins are conjugate and cannot merge, however many inverse histories
are retained. For C=0 they instead give two distinct physical R orbits.

If KO=O, there is a unique s modulo q with Kp=T^s p. Commutation gives
K(T^j p)=T^(j+s)p, while K^2=1 gives 2s=0 modulo q. Thus:

    s=0: every cycle point is real;
    s!=0: q is even, s=q/2, and every cycle point is nonreal.       (6)

Conversely any real cycle point forces the first case throughout that
cycle. In particular an odd-period nonreal cycle cannot be self-conjugate;
an even-period nonreal cycle can be either paired or self-conjugate.
This is a classification of actual cycles, not of chosen representatives.

For phases, put p_j=T^j p and K_j=S_j(p), with K_0=0. The connecting
arrow p->p_j has lag-j and clock-K_j; thus (p_j,h) has anchor phase h+K_j.
In the self-conjugate case the induced involution is consequently

    [h] -> [h+K_s] on R/(CZ).                        (7)

For s=0 this is identity. For s=q/2, reflection makes the two half-cycle
clock sums equal, so K_s=C/2. If C!=0, (7) is the nontrivial half-period
translation on the ONE physical circle, even when C<0. If C=0, K_s=0
and it is identity on the physical line R. All incoming histories inherit
the same phase action by equivariance; no second packet is created.

## 5. Precise benchmark consequence and its limits

A distinct conjugate pair with C!=0 forces TWO different positive primitive
packets of least time abs(C). If exp(abs(C)) is an ordinary prime p, this
violates at-most-one packet per prime. If it is not an ordinary prime,
the prime-only requirement already fails. This is the exact obstruction
forced by such a pair; C=0 produces no positive primitive to count.
Self-conjugate cycles create no conjugation-forced multiplicity. They can
still fail the prime-only test, or share their time with some other cycle.
Thus self-conjugacy of all positive packets is necessary for avoiding this
particular paired obstruction, not sufficient for the full benchmark.
An empty positive ledger also fails nonemptiness; all-prime coverage is a
separate stronger requirement. Nothing asserts that every nonreal point
gives two packets, that every nonreal cycle has C!=0, or that reflection
alone excludes every owner. The R control below gives the latter boundary.

## 6. R — complete linear control and whole periodic ledger

Put rho=sqrt2 and T(z)=rho z on the FULL C. Its sole inverse is w/rho,
with all-point real Jacobian1/2, so for every Borel E,
mu(T^(-1)E)=mu(E)/2. The own forward Jacobian is2 and kappa=log2.
For every integer k the actual arrows and their clocks are exactly

    (rho^(-k) w,k,w),  c=k log2.                      (8)

All incoming points are the full rho^Z orbit. Clock kernel, lag kernel and
their intersection are units. The only periodic point is0: rho^q z=z for
q>0 forces z=0. No nonzero point can become0, so all other points are also
non-eventually-periodic. At0 source isotropy is Z, extension isotropy0,
H=(log2)Z and there is exactly ONE primitive log2 packet. It is real and
conjugation fixes its physical phase. Repetitions j log2 remain attached
to that packet; they are not other primitive packets.

At every nonzero point the two isotropies and H are0; each entire source
orbit gives a physical R. Conjugation fixes the real source orbits and
exchanges distinct nonreal source orbits, since a positive real scaling
cannot change a nonreal argument to its conjugate. Those exchanged orbits
are not positive packets. There are no terminals or omitted points.
R satisfies the THREE stated necessary conditions, but supplies only the
prime2 packet, not all-prime coverage or an endogenous arithmetic source.

## 7. N/E — own all-point IMAGE, full domains and global ledgers

For a=3/4 or1 put P_a(z)=z^2+a and D=C minus {0}, on the FULL carrier C.
The two frozen pieces H_plus and H_minus=-H_plus each map bijectively onto
C minus {a}. Their actual Borel inverses are

    I_plus(w)=the square root of w-a in H_plus,
    I_minus(w)=-I_plus(w),  w!=a.                     (9)

At EVERY target w!=a the corresponding local inverse Jacobians equal
1/(4|w-a|). Even on the square-root cut, the local germ fixes that value;
no global smooth square-root selection across the cut is claimed. Thus

    mu(I_plus E)=mu(I_minus E)=integral_E 1/(4|w-a|) dmu(w)

for every Borel E subset C minus {a}. Summing BOTH actual inverses gives
mu(T^(-1)E)=integral_(E minus {a}) 1/(2|w-a|) dmu(w) for arbitrary Borel E.
The critical value a has NO legal predecessor but remains a legal source
point. The terminal0 remains an object and has predecessors +/-i sqrt(a).
The own clock is kappa_a(z)=log(4|z|^2), z!=0; it is negative for |z|<1/2,
zero for |z|=1/2 and positive for |z|>1/2. No value is assigned at0.
Real coefficients give the required reflection of assigned germs even
when conjugation changes the half-plane piece on the imaginary axis.

Define algebraic polynomials P_(a,0)(z)=z and P_(a,j+1)=P_a(P_(a,j)), but
permit an actual m-step history ONLY on

    U_(a,m)={z:P_(a,j)(z)!=0 for 0<=j<m}, U_(a,0)=C.

For z in U_(a,m), define
Lambda_(a,m)(z)=2^m product_(j<m) P_(a,j)(z), with Lambda_(a,0)=1.
This is the exact assigned derivative of the actual prefix; it is nonzero.
The FULL groupoid and all three global kernels, separately for EACH a, are

    G_a: z in U_(a,m), w in U_(a,n), P_(a,m)(z)=P_(a,n)(w);
    c=log(|Lambda_(a,m)(z)|^2/|Lambda_(a,n)(w)|^2);
    ker c: |Lambda_(a,m)(z)|=|Lambda_(a,n)(w)|;
    ker lag: m=n; intersection: both equalities.      (10)

These are necessary AND sufficient predicates over all legal m,n, all
points and all lags, not a finite census. Nonunit intersection arrows
include (z,0,-z), z!=0, witnessed by m=n=1. No general equality of the two
kernels is presumed at other depths. All incoming histories are obtained
by applying BOTH inverses(9) whenever the target differs from a, at every
finite depth, and stopping any forward history at0. Equations(10) never
continue a forbidden iterate merely because its polynomial formula exists.

For higher cycles outside the requested window the exact generic predicate
is z in U_(a,q), P_(a,q)(z)=z, with P_(a,j)(z)!=z for all 0<j<q.
Its cycle clock is C=log|Lambda_(a,q)(z)|^2. Every finite legal preimage
has source isotropy qZ and the H/extension isotropy in(4); points not in ANY
eventual cycle have trivial source isotropy and H. This treats C<0 and C=0
without assuming either occurs or never occurs in the unenumerated cycles.
No high-period enumeration or dynamical classification has been imported.

For any listed periodic core O its FULL basin is exactly

    B_a(O)=union_(m>=0){z in U_(a,m):P_(a,m)(z) in O}. (11)

It is one source orbit. All our listed cores are nonreal. A real starting
point has only real legal forward values, so its basin contains no real
point, in particular neither0 nor the critical value a. Consequently every
basin point has both distinct nonzero predecessors, and each depth has
exactly |O| 2^m points. The nested union is countably infinite, with no
selected branch. Distinct cores have disjoint basins. If P_(a,m)(z)=p_j
in a core anchored at p, its entire height phase is

    h-S_m(z)+K_j modulo CZ, K_j=S_j(p).               (12)

All choices agree modulo H. This describes every incoming state and every
real height, not only the core points.

## 8. N — complete fixed cores and their full basins

The fixed equation z^2-z+3/4=0 has exactly
p_plus=(1+i sqrt2)/2 and p_minus=conjugate(p_plus). Both are legal,
nonreal, distinct fixed points. Their modulus squared is3/4, giving
own Jacobian |2p|^2=3 and signed cycle clock C=log3.
Each full basin B_(3/4)({p_plus/minus}) has source isotropy Z,
extension isotropy0, whole H=(log3)Z and all phases R/((log3)Z) via(12).
The two basins are disjoint, countably infinite and exchanged by conjugation.
They therefore yield exactly TWO distinct primitive log3 packets within
the complete fixed window, not one packet or many packets per incoming tree.
This already violates uniqueness per prime in the full owner, regardless
of its unenumerated higher periods. Those other states retain(9)–(12) and
the signed/zero-C cases; no claim of a full higher-period census is made.

## 9. E — complete fixed and exact-two cores and their full basins

The fixed equation z^2-z+1=0 has exactly
p_plus=(1+i sqrt3)/2 and p_minus=conjugate(p_plus). Their modulus squared
is1, so their own fixed clock is log4. Both full fixed basins have source
isotropy Z, extension isotropy0 and H=(log4)Z. They are disjoint conjugate
basins and yield two distinct primitive log4 packets. Each violates the
prime-only length requirement; log4 is not renamed a repetition of a
different packet. All basin points and all phases are given by(11)–(12).

Exact-two classification follows from the exact factorization

    P_1(P_1(z))-z=(z^2-z+1)(z^2+z+2).

The second factor has roots u_plus=(-1+i sqrt7)/2 and u_minus=conjugate(u_plus).
Neither is a fixed root; P_1(u)=-u-1 exchanges the two. Both are legal and
nonzero and have modulus squared2. These are ALL exact-two points, one
cycle O2, and its two step clocks are each log8. Thus

    q=2, C=log64, H=(log64)Z,
    source isotropy2Z, extension isotropy0.           (13)

Its full basin B_1(O2) is one countably infinite source orbit, disjoint
from both fixed basins. It yields ONE primitive log64 packet, not two
packets from its two nonreal conjugate phases. With anchor u_plus, K_1=log8
and conjugation acts on its physical circle as h->h+log8 modulo log64:
the half-period translation of(7). Every incoming point has the same full
H and phase rule(12). The fixed basins instead are exchanged as distinct
circles. Both mechanisms are retained in this ONE E owner; no phase or
incoming branch was removed to obtain the contrast. Higher cycles and
all other states retain the generic full ledger(10), without a census.

## 10. Scope, outcomes and freeze

Germ reflection preserves the full measure/clock/history owner and signed
cycle clocks. A distinct positive conjugate pair gives an unavoidable
benchmark obstruction; a self-conjugate nonreal even cycle gives one
packet with half-period phase action, not forced duplication. Zero-C and
aperiodic source orbits remain physical lines with their exact isotropy.
R passes only the weak necessary benchmark, N already fails prime uniqueness
on its fixed window, and E fails prime-only lengths on its bounded cores.
All are external controls; none supplies a lineage-admitted arithmetic source.
The full phase space, terminals, actual inverse branches and all heights
remain throughout. No attracting-basin, Julia, high-period census, novelty or
broad no-go conclusion is asserted. Classical NOT APPLICABLE; T3 NOT AUDITED;
formal Route UNASSIGNED; Route B NOT INVOKED. No scientific code, external
literature, Git mutation, operator, PDF or publication was used.
This raw precedes manuscript access. Freeze after full self-read; CP2/CP3
await root's full read and separate PAPER UNLOCK.

EOF — independent card-only raw complete; HOLD for separate paper unlock.
