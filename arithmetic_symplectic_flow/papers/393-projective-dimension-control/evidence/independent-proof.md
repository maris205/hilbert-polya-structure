# PDC01 — independent full-projective external-control audit

Candidate `ANG-CONTROL-20260922-PDC01`; `NONUNIT-RETURN-20260922-I`, round4/5.
2026-09-22; reviewer `/root/nonlocal_source_review`.
Scientific input: entire74-line frozen card, SHA256
42b57df25ae79aa9deb72de31997f96497361b0db4a24e43c733485f97cf9ecc.
Root read CP1 and explicitly released mathematics. No new manuscript,
README, claim ledger, peer proof or387/394 result was read. Exact derivation
below is card-only, shared-history internal NOT_CALIBRATED work, not blind
or external peer review. All four owners remain EXTERNAL CONTROLS.

## 1. Round projective volume and global transport

For an invertible real N-by-N matrix A, write v=r u with r>0 and u on
S^(N-1). The linear map sends radius r to r||Au|| and direction to
g_A(u)=Au/||Au||. Euclidean polar volume is r^(N-1)dr d sigma(u).
Since the angular map does not depend on r, the radial/angular derivative
is block triangular. Comparing transformed polar volume with |det A|
times original Euclidean volume gives

    J_(g_A)(u)=|det A|/||Au||^N.                                   (1)

Antipodal quotient to RP^(N-1) is a local round isometry, and g_A commutes
with antipodes. Thus the identical local density formula descends everywhere:

    J_A([v])=|det A| ||v||^N/||Av||^N, v!=0.                       (2)

Scaling v or multiplying A by any nonzero real scalar leaves(2) unchanged.
There is no selected affine chart or omitted projective hyperplane.
In particular A and A^(-1) induce global smooth diffeomorphisms. Change of
variables gives, for EVERY Borel E in RP^(N-1),

    m(F_A^k E)=integral_E J_(A^k) dm, k in Z.                       (3)

The sphere calculation and quotient cover give this identity in every local
transport chart, hence globally by disjoint Borel subdivision of charts.
It is not an assertion that m is invariant. Normalizing m by a fixed constant
would not change its Jacobian; here m is the frozen round volume.

By direct cancellation of norms,
J_(A^(k+l))(w)=J_(A^k)(F_A^l w)J_(A^l)(w), for all integers k,l.
For our N=4 owners the complete retained-lag clock is consequently

    c_k([v])=4 log(||A^k v||/||v||)-k log|det A|.                   (4)

It is additive on the actual arrows([A^k v],k,[v]), including all negative
lags. Its exponential exp(-c_k) is exactly the density in(3).

## 2. Full groupoid, kernel and height conventions

Each of the FOUR maps has its OWN transformation groupoid for the Z action,
even when distinct powers agree as point maps. Integer k is never quotiented
by finite map order. The lag kernel consists only of units, because k=0
forces z=w. The full clock kernel is exactly

    {([A^k v],k,[v]):||A^k v||^4=|det A|^k ||v||^4}.              (5)

Its intersection with the lag kernel is therefore units. Each specialized
kernel below supplies every k and every projective point satisfying(5).
All incoming arrows to x are (x,k,F_A^(-k)x), k in Z. Thus the entire source
orbit is {F_A^k x:k in Z}, with no selected iterate or hidden predecessor.

A periodic point with least source period d has source isotropy dZ. If
A^d v=lambda v, its cycle value is

    C=4 log|lambda|-d log|det A|.                                  (6)

It is independent of the representative v and of the matrix scalar. Source
isotropy maps rd to rC. If C!=0, extension isotropy is trivial and H=C Z,
whose least positive generator is L=|C|. If C=0, extension isotropy is dZ
and H={0}; zero clock does NOT make H equal R. Nonperiodic points have
trivial source/extension isotropy and H={0}. These facts follow because an
extension-height return to the same source is exactly an isotropy arrow.

For a reference x and arrow to z=F_A^k x, the complete phase of(z,h) is
h-c_k(x) modulo H_x. Changing the connecting k changes this by an element
of H_x. Hence the entire extension orbit SET over each source orbit is
R/H_x with translation. If L>0 it is ONE primitive physical packet per
source orbit, with repetitions rL and oriented source clocks rC. Equal L
does not merge different source orbits. If H={0} it is a real height line,
not a closed positive-time orbit. All real heights and phases are retained.

## 3. MAIN — diag(B,I_2), B=[[0,2],[1,0]]

Write v=(u,w), u=(s,t) in R^2, w in R^2, and let U=R^2 direct-sum0,
W=0 direct-sum R^2. Here |det A|=2 and A^2=diag(2I_2,I_2).
B has eigenlines e_+=[(sqrt2,1,0,0)] and e_-=[(-sqrt2,1,0,0)].
Both are irrational projective lines: their first/second coordinate ratio
is irrational, so no nonzero rational-coordinate vector represents either.

The ENTIRE periodic set is P(U) union P(W), two disjoint projective lines.
Indeed if both u and w are nonzero and A^k v=alpha v for k!=0, the w
component forces alpha=1. But B^k has eigenvalues of modulus2^(k/2), never1
for nonzero k, so it cannot fix nonzero u. Mixed points are all nonperiodic.
On P(W) every point is fixed. On P(U), A^2 is projectively identity, and
only e_+,e_- are fixed; every other point there has least source period2.
This proves exhaustiveness, not just a list of exhibited eigenvectors.

At either e_sign, |lambda|=sqrt2, J_A=2/(sqrt2)^4=1/2 and c_1=log2.
Thus I=Z, extension isotropy trivial, H=(log2)Z and L=log2, giving the
positive physical multiplier exp(L)=2 at BOTH irrational eigenlines.
They are distinct fixed source orbits, hence TWO distinct equal-time packets.

At EACH point of the full P(W)=RP^1, lambda=1, J_A=2 and c_1=-log2.
Its source isotropy is Z, extension isotropy trivial and H=(log2)Z.
The positive primitive time is again log2, despite the opposite sign of the
oriented cycle clock. Every projective point is its own distinct packet.
Thus there are continuum-many further log2 packets, not a selected one.

At EVERY other point of P(U), the least source period is2 and A^2 v=2v.
The full cycle Jacobian is1/4 and C=2log2=log4. Consequently I=2Z,
extension isotropy trivial, H=(log4)Z and L=log4. Each pair {[u],[Bu]}
is one packet with both phases, not two packets. There are continuum-many
such pairs. Their least time is NOT a repetition of either fixed log2
packet, because the source orbits are different and the entire H is log4 Z.
Every mixed nonperiodic source orbit has I=0, extension isotropy0, H={0},
and a full real height line. These classifications cover EVERY point.

For the full clock kernel set R=s^2+t^2, W_0=||w||^2 and S=s^2+4t^2.
All are homogeneous in v. For n in Z, exact powers give

    ||A^(2n)v||^2=4^n R+W_0,
    ||A^(2n+1)v||^2=4^n S+W_0.

Thus k=0 gives all units. For k=2n!=0, the ENTIRE zero-clock locus is
W_0=2^n R, obtained by factoring
(2^n-1)(2^n R-W_0)=0. For k=2n+1, it is EXACTLY

    4^n S+W_0=2^(n+1/2)(R+W_0).                                   (7)

All points on these projective loci, including any lying on a coordinate
hyperplane, contribute their actual arrow to the kernel; no others do.
The lag kernel and its intersection remain units. Nonidentity zero-clock
arrows here need not be isotropy, which explains why they coexist with the
trivial extension isotropy established for all MAIN points.

## 4. Own S control — A_S=2 I_4

Now |det A_S|=16 and F_S is identity on ALL RP^3. Formula(2) gives J_k=1
for every k and every point; its own every-Borel IMAGE is m(E)=m(E).
Its full clock c_k=0, not a borrowed MAIN clock. Every point has least
source period1 and source isotropy Z. Extension isotropy remains Z,
H={0}, and each source point contributes a real height line. There is no
positive primitive physical packet and no nonperiodic source complement.
Every integer-labeled arrow survives although all point maps agree.
The clock kernel is the entire groupoid, the lag kernel is units and their
intersection is units. Repeated source loops have clock0, not positive time.

## 5. Own D control — A_D=diag(2,1,1,1)

Write v=(s,w), w in R^3, a=s^2, b=||w||^2. Here |det A_D|=2 and its
own density and clock, on ALL RP^3, are obtained from

    ||A_D^k v||^2=4^k a+b,
    c_k=2 log[(4^k a+b)/(a+b)]-k log2.                              (8)

The periodic set is EXACTLY the distinguished line e=[1,0,0,0] and the
complementary projective plane P={s=0}=RP^2; all are fixed. If s and w
are both nonzero, a projective return forces simultaneously its scalar
factor to be1 and2^k=1, so no nonzero k is possible. There are no other
periodic points or periods, and every mixed point is nonperiodic.

At e, J_A=1/8 and c_1=log8. Thus source I=Z, extension isotropy0,
H=(log8)Z, one primitive packet with L=log8 and multiplier8.
At EACH point of the ENTIRE RP^2 plane, J_A=2 and c_1=-log2. Hence
I=Z, extension isotropy0, H=(log2)Z and L=log2. These are continuum-many
distinct packets, not one packet obtained by choosing a plane representative.
Each mixed source orbit has trivial source/extension isotropy, H={0} and
one real height line. Equations(3),(8) give D's own full Borel transport.

For k!=0 put t=2^(k/2)>0, t!=1. Equation(5) is
(t^4-t)a+(1-t)b=0, hence EXACTLY b=t(t^2+t+1)a.
Together with all k=0 units these homogeneous loci give the whole clock
kernel, for positive AND negative k. Both a and b are then nonzero;
these are mixed-point arrows, not missed periodic isotropy. The lag
kernel and intersection are units. All incoming arrows and phases are
the full ones in§2, with D's own c_k, not MAIN's formula.

## 6. Own B control — A_B=diag(B_2,B_2)

Here B_2=[[0,2],[1,0]], |det A_B|=4 and A_B^2=2I_4. Thus F_B has order2
as a map, but the actual arrow group remains Z. Its two eigenspaces are

    E_+={(sqrt2 t,t,sqrt2 u,u):t,u in R},
    E_-={(-sqrt2 t,t,-sqrt2 u,u):t,u in R}.

The fixed set is EXACTLY P(E_+) union P(E_-), two disjoint full RP^1s.
Every other point has least period2. This exhausts RP^3: the nonperiodic
complement is empty. At each fixed point J_A=4/(sqrt2)^4=1, so c_1=0,
source isotropy Z, extension isotropy Z and H={0}. At each other point
J_(A^2)=1, so C=0 on its full period2, source isotropy2Z, extension
isotropy2Z and H={0}. There are no positive primitive physical packets.

Nevertheless individual step clocks are not everywhere zero. Write
v=(s_1,t_1,s_2,t_2), P=s_1^2+s_2^2, Q=t_1^2+t_2^2. Its OWN Jacobian is
J_A=4(P+Q)^2/(P+4Q)^2 and its step clock is

    c_1=2 log[(P+4Q)/(2(P+Q))].                                    (9)

For every even lag c_(2n)=0 at all points; for every odd lag c_(2n+1)=c_1,
including negative n, by the exact scalar identities for A_B powers.
Thus the COMPLETE clock kernel contains all even-lag arrows at all points
and exactly the odd-lag arrows on P=2Q. This quadric includes the fixed
sets but is not replaced by them. The lag kernel and intersection are units.
Formula(3) with this J gives B's own every-Borel transport, not invariance
of round volume for a single step. For a two-point source orbit the two
step clocks cancel, and the full height relation is h-c_1 between its two
phases. Every source orbit contributes an R of physical phases. Repetition
does not eliminate the retained2Z (or fixed-point Z) extension isotropy.

## 7. Self-contained dimensional comparison, not an imported RLA theorem

Formula(2) has exponent N, so it is genuinely dimension dependent.
For a rational invertible2-by-2 return matrix C acting on RP^1, an
irrational fixed projective line can have a rational nonunit positive
physical multiplier only if the following elementary obstruction fails.
Let Cv=lambda v. Its fixed-point Jacobian is |det C|/lambda^2.
If C is scalar this Jacobian is1. If C is nonscalar and lambda rational,
the one-dimensional kernel of C-lambda I has a rational basis, contrary
to the irrational line. Therefore lambda is quadratic irrational.
Rationality of exp(|log(lambda^2/|det C|)|) implies lambda^2 is rational.
Its conjugate is then -lambda, so det C=-lambda^2 and the ratio is1.
There is therefore NO rational multiplier>1 at such an irrational fixed
line in this one-dimensional rational-projective return setting.
This proof also applies to any rational first-return matrix, without
borrowing387 or394. It asserts only those explicit hypotheses.

For our small B_2 on RP^1, its irrational eigenlines have lambda^2=2 and
|det B_2|=2, hence Jacobian1. In MAIN on RP^3 the exponent is instead4,
while |det A|=2 and |lambda|^4=4, giving Jacobian1/2 and L=log2.
These are DIFFERENT ambient volume owners, so the MAIN calculation does
not contradict the proved one-dimensional restriction. It is not a
minimal-dimension theorem, universal higher-dimensional construction or
novelty claim. No extra candidate is admitted by this comparison.

## 8. External-control disposition and boundaries

MAIN supplies a genuine irrational eigenline with positive rational physical
multiplier2, but its full ledger has two such eigenline packets PLUS the
entire RP^1 continuum of log2 packets and continuum-many primitive log4
two-cycles. D retains its full RP^2 continuum as well as its log8 point.
S and B have no positive physical packets despite pervasive source periods.
These are conclusions for four separately owned full carriers, not a
cross-control synthesis of selected points and clocks.

Coefficient2 was assigned before analysis; no prime-symbolic admission or
endogenous arithmetic mechanism has appeared. All four objects remain
EXTERNAL CONTROLS. Stop any promotion to a main candidate or target credit.
No invariant flow measure, quotient manifold, symplectic lift, operator,
whole-program dimension theorem or new admissibility feedback is supplied.
External-owner T0/T1/T2 bookkeeping only; strong arithmetic naturalness
NOT ESTABLISHED; classical NOT APPLICABLE; formal UNASSIGNED;
T3 NOT AUDITED; Route B NOT INVOKED. Exact proofs, no scientific numerics,
external search, PDF, Git write or publication operation.

EOF — complete card-only raw; freeze and await separate PAPER UNLOCK.
