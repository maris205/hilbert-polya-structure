# PST01 — card-only independent derivation

Candidate: ANG-AUDIT-20260924-PST01. Paper453.
Reviewer: `/root/rcr01_independent_review`, 2026-09-24 UTC.
Input: original 91-line card, SHA-256
`9cbd785bb07b7461a3fcb94a51b4ae17068176567678143689b9844a375d1326`.
Root separately released raw work after its full CP1 read. No author
paper, README, ledger, appended Outcome, peer/helper proof or old proof
was read. The inherited shared history includes a total-stride overview;
the results below are rederived for the frozen partial class, not imported
as an old proof lock. Same-model internal AI work remains NOT_CALIBRATED,
not blind, human, external or cross-model validation. No numerical code,
network, Git, PDF, old-file edit or operator work is used.

## 1. Actual refinement and all-point IMAGE

Write D_i for the parent's countable disjoint injective source pieces,
E_i=T(D_i), and theta_i:E_i->D_i for their actual Borel inverses.
The given every-Borel IMAGE identity also gives the weighted identity

    integral_{theta_i(B)} h(x) dmu(x)
      =integral_B h(theta_i(y)) J_i(y) dmu(y)

for every nonnegative Borel h, first for indicators, then simple functions
and monotone limits. This derivation uses the frozen IMAGE identity, not
an inferred derivative or another measure.

For a length-r word i=(i_0,...,i_{r-1}), define its ACTUAL source piece
by requiring T^j x in D_{i_j} for every 0<=j<r. These pieces are Borel,
disjoint and exhaust D_r. T^r is injective on each, by successively
inverting its r prescribed branches. Its inverse Theta_i is the legal
composition theta_{i_0} ... theta_{i_{r-1}}, restricted to targets for
which every intermediate reconstructed point has the prescribed branch.
The final target is not required to admit another parent step.

If y_r=y, y_j=theta_{i_j}(y_{j+1}) for j=r-1,...,0, then

    J_Theta(y)=product_{j=0}^{r-1} J_{i_j}(y_{j+1}).

Repeated weighted substitution proves the every-Borel IMAGE identity
for this composition. Each factor is the prescribed positive finite
all-point value, so the product is specified at every actual point,
including every null point. No almost-everywhere reassignment occurs.
Each actual source has exactly its own itinerary, and all words and all
admitted roots are retained. Countability is preserved under finite
refinement; no selected sheet or inverse is substituted.

Thus the sampled owner has, for every legal R step and every legal
sampled history,

    kappa_R(x)=S^T_r(x), S^R_m(x)=S^T_{rm}(x),
    Pre_R^m(y)=Pre_T^{rm}(y).

All these equalities use genuinely legal parent steps. Objects outside
D_r remain in X as sampled terminals; no identity evolution is added.
Their units are lag-zero units, not artificial loops of every integer lag.

## 2. Full groupoids and the exact embedding image

For either owner U, two witnesses for the same triple (z,k,w) differ
by equal increments of the meeting exponents. The common added legal
tail contributes the same sum on both sides and cancels. Therefore
c_U=S^U_m(z)-S^U_n(w) descends to equal triples. For composition, align
the two middle exponents at their maximum; the longer given middle
history supplies the legal extra tail on the matching other side.
The middle sums cancel, proving additivity without continuing a terminal.
The forward arrow (Uz,-1,z) has clock -kappa_U(z).

For each U the complete source class is

    O_U(w)=union_{n>=0, U^n w legal} union_{m>=0} Pre_U^m(U^n w).

Every actual branch at every depth is included. Its complete kernels are

    K_lag(U)={(z,0,w):U^m z=U^m w legally for some m},
    K_c(U)={(z,m-n,w):U^m z=U^n w legally,
                         S^U_m(z)=S^U_n(w)},
    K_joint(U)=K_lag(U) intersect K_c(U).

Clock equality alone does not create an arrow. These definitions are
further resolved on every type of source class below.

The map Phi:G_R->G_T given by (z,k,w)->(z,rk,w) is an injective
groupoid homomorphism, the identity on objects. A sampled witness m,n
gives parent witnesses rm,rn. Clock compatibility is EXACT:

    c_T(Phi(g))=c_R(g).

Consequently the image of each sampled lag, clock or joint kernel is
the intersection of Phi(G_R) with the corresponding parent kernel.
The associated height-extension embedding keeps h unchanged. It is
not a global time rescaling.

Here is the exact legal-witness image criterion. A parent arrow
(z,l,w) is in Phi(G_R) if and only if l is divisible by r AND it has
some legal parent witness m,n for which the common meeting point
y=T^m z=T^n w admits delta further parent steps, where

    delta is the integer in {0,...,r-1} with m+delta=0 modulo r.

Since m-n=l is divisible by r, the same delta aligns n. Padding that
LEGAL tail gives witnesses divisible by r, and hence a sampled arrow.
Conversely any sampled witness supplies such a parent witness with
delta=0. The quantifier is "some witness", not "every witness";
an unnecessarily late witness can lie too near a terminal.

There is also a canonical equivalent test. For a fixed actual parent
triple let (m_0,n_0) be its minimal meeting witness, obtained by minimizing
n among its witnesses; m is then fixed by the lag. Every other witness
is (m_0+t,n_0+t) for some t>=0 along the common trajectory, and exactly
the legal such t occur. Let h_T(y) be the number of legal future parent
steps from y, with infinity allowed. Then

    (z,l,w) in Phi(G_R)
      iff l in r Z and h_T(T^{m_0}z)>=(-m_0 modulo r).

The least nonnegative residue on the right is essential. This criterion
does not assume that every parent arrow of divisible lag can be padded.

## 3. Every parent terminal-ending class

For a point with finite parent lifetime put d_z=h_T(z),
t_z=T^{d_z}z, and A_z=S^T_{d_z}(z). The endpoint t_z is terminal.
The parent classes are exactly

    B_t={z:t_z=t}, for each parent terminal t.

Two points meet if and only if they have the same final terminal.
Inside B_t there is precisely one arrow between each ordered pair:

    (z,d_z-d_w,w), with c_T=A_z-A_w.

Indeed at any legal common meeting y, d_z=m+h_T(y) and
d_w=n+h_T(y). Conversely the terminal itself supplies the witness.
Hence parent lag, clock and joint kernels impose respectively equal
d values, equal A values, and both. There is no nonzero-lag isotropy.
Parent source and extension isotropy and whole H are zero. The complete
real height phase is h-A_z, normalized to h at the terminal t.

For the sampled owner define

    n_z=floor(d_z/r), s_z=d_z-r n_z,
    b_z=T^{r n_z}z.

This is the last ACTUALLY sampled object, with parent depth s_z<r.
It is a sampled terminal even when it still has unsampled parent steps.
The sampled lifetime is n_z. The complete decomposition of B_t is

    B_t = disjoint union_{b in B_t, d_b<r} B^R_b,
    B^R_b={z:b_z=b}=union_{k>=0}Pre_T^{rk}(b).

Each such b occurs as its own sampled endpoint. This class label is
an actual object, not just its depth residue. Distinct branches at the
same residual depth may give different b and therefore different classes.
This accounts for finite merging before a parent terminal.

On B^R_b the sampled accumulated clock to its terminal is

    A^R_z=S^T_{r n_z}(z)=A_z-A_b.

There is exactly one sampled arrow between each pair in this class,
with k=n_z-n_w=(d_z-d_w)/r and c_R=A_z-A_w. Its lag, clock and joint
kernels impose respectively equal d, equal A, and both, within B^R_b.
Source and extension isotropy and H are all zero. The full real phase
is h-A^R_z=h-A_z+A_b. Every incoming branch and depth is present.

Thus on a terminal-ending parent class the divisible-lag condition
only asserts equal depth residues; the EXACT image additionally needs
b_z=b_w. When this fails, objects have not been removed: it is the
parent merging arrow that is absent from the sampled groupoid.

## 4. Infinite, non-eventual parent classes

If a point has an infinite legal parent future, so does every point
of its parent source class. Every common meeting then has arbitrarily
long legal future, so the criterion in Section2 reduces on this invariant
part to parent lag divisible by r. This reduction is proved here, not
assumed for the full partial map.

For an infinite non-eventual parent class choose an anchor a. Parent
isotropy is zero: unequal matching times would force an eventual cycle.
For every z in its class there is therefore a unique parent arrow
a->z. Write its lag l_z and clock B_z, with l_a=B_a=0. All parent
arrows w->z have lag l_z-l_w and clock B_z-B_w. The parent lag,
clock and joint kernels require equal l, equal B, and both.

The sampled classes are exactly the r residue classes

    l_z modulo r.

Every residue occurs, since z=T^j a, 0<=j<r, has l_z=-j; these
points are distinct in a non-eventual class. On one residue class all
sampled arrows have k=(l_z-l_w)/r and c_R=B_z-B_w. Their kernels
impose equal l, equal B within the residue class, and both. All parent
lag-zero merging arrows survive, by legal padding on the infinite tail.
This retains branching rather than replacing the class by one orbit path.

Both source and extension isotropy and whole H are zero. For both
owners h-B_z is a complete real phase, with the sampled residue label
retained separately. Changing a class anchor adds only a constant to
that class coordinate. No global measurable selector or nice quotient
is assumed. The complete inverse/meeting unions in Section2 supply
all points and inverse depths, including all coalescing histories.

## 5. Every eventual parent core and its full sampled basins

Let a_j=T^j a_0, 0<=j<q, be a parent core of least period q. Put
A_j=S^T_j(a_0), C=S^T_q(a_0), ell=C/q. C may be positive, negative
or zero. For any point z in its complete parent basin, let d_z be its
first core arrival and e_z its entry index. Define

    chi_z=e_z-d_z,
    beta_z=S^T_{d_z}(z)-A_{e_z}+chi_z ell.

The exact parent arrows between basin points are all integers l with
l=chi_w-chi_z modulo q, and their clocks are

    c_T(z,l,w)=l ell+beta_z-beta_w.

To see necessity, advance a meeting to the core and compare its two
phase indices. Conversely every congruent lag is realized by sufficiently
large nonnegative meeting exponents on that infinite core. Cancelling
the common core phase in the clock sums gives the displayed formula.
Parent kernels impose l=0, the displayed clock equal to zero, or both,
always with the congruence. Source isotropy is q Z and ENTIRE H=C Z.
Extension isotropy is zero for C!=0 and q Z for C=0. A complete phase
is h-S^T_{d_z}(z)+A_{e_z} modulo C Z, where modulo zero means R.

Put g=gcd(q,r), q'=q/g and u=r/g. The sampled map advances the core
index by r modulo q. It therefore has exactly g distinct cores, indexed
by eta in {0,...,g-1}, each of least sampled period q'. Every sampled
core traversal consists of r q'=u q actual parent steps, so its own
SIGNED clock is u C, the same on all g cores.

The full parent basin splits into exactly these g sampled classes:

    chi_z=eta modulo g.

Indeed late sampled times r m reach core indices e_z+r m-d_z, which
have that residue. Conversely, for two points with equal residue,
r k=chi_w-chi_z modulo q has an integer solution. Legal padding on
the eventual core then gives the sampled arrow. Equivalently the class
is union_{m>=0}Pre_T^{rm}(O_eta), with every actual inverse retained.
Thus intermediate parent objects are assigned to sampled basins rather
than dropped or manually identified.

Within such a sampled class the complete arrows and clocks are

    r k=chi_w-chi_z modulo q,
    c_R(z,k,w)=r k ell+beta_z-beta_w.

The lag, clock and joint kernels impose k=0, this clock zero, and both,
with the displayed congruence. In particular equality modulo g alone
does not suffice to assert a lag-zero arrow. Source isotropy is q' Z;
the clock of its lag q' generator is u C. Hence ENTIRE H_R=u C Z,
and extension isotropy is zero if C!=0 and q' Z if C=0.
For C!=0 each of the g distinct packets has primitive u|C| and all
positive integer repetitions. Equal lengths do not merge those packets.
For C=0 none has a positive physical primitive, but its nontrivial
source and extension isotropy remains in the ledger.

An explicit sampled phase keeps all entry clocks, including overshoot
past the first parent core arrival. Choose the eta-core anchor a_eta,
write b_t=a_{eta+r t modulo q}, 0<=t<q', and let
K_t=S^T_{rt}(a_eta). For z in that sampled class define

    D_z=ceil(d_z/r),
    e'_z=e_z+r D_z-d_z modulo q,
    t_z uniquely by eta+r t_z=e'_z modulo q, 0<=t_z<q'.

This is its first SAMPLED core arrival. The full phase is

    h-S^T_{r D_z}(z)+K_{t_z} modulo u C Z.

For C=0 it is an ordinary real phase. This is not a parent phase
divided by r or by a source period. The general anchor description
h minus an actual arrow clock, modulo the whole H, gives the same
set-level coordinate. Physical height translation stabilizes exactly
H: a shift returns to the same extension orbit precisely when supplied
by an isotropy arrow. No regular quotient has been assumed.

Finally, a periodic R point is periodic for T, since R^m x=x implies
T^{rm}x=x legally. Thus the above lists ALL sampled periodic cores:
no terminal or non-eventual source creates an additional sampled cycle.
The terminal, infinite non-eventual and eventual cases exhaust X and
all histories, clocks, kernels and phases of both owners.

## 6. Rational-parent conditional obstruction and its exact limit

Assume the frozen rational-parent condition: for every parent core with
C!=0, a=exp(|C|) is rational and greater than one. If there is no such
core, Section5 shows the sampled owner has no positive primitive, and
the nonempty-positive benchmark fails.

Otherwise take any such core and use g,q',u from Section5. If g>=2,
its g distinct sampled packets have the same positive primitive. If
that length is not log of a prime, prime purity fails; if it is, prime
uniqueness fails. If g=1, then u=r>=2 and the sampled exponential
primitive is a^r. It cannot be an ordinary prime: writing a=v/w in
lowest positive integer terms, a^r=p implies w=1 by coprimality and
then v^r=p, impossible for r>=2 and v>1.

Thus the simultaneous nonempty, prime-pure, prime-unique benchmark
fails for the sampled owner in this stated rational-parent subclass.
Zero-clock cores are not treated as positive packets. No prime table,
fitted roof, target-zero comparison or operator is used. The argument
does not cover an irrational exp(|C|); Control C below demonstrates
why that hypothesis cannot be silently removed. All-prime coverage
is a separate obligation even for a control satisfying the smaller
three-part benchmark.

## 7. Control A — scalar doubling and its actual square

Parent T(x)=2x and sample R(x)=4x are global diffeomorphisms of the
whole real line, with inverse IMAGE densities 1/2 and 1/4 at EVERY
target and every Borel set. Their own step clocks are log2 and log4.
More generally for either scalar a=2 or4, every integer iterate is
U^n x=a^n x, and all arrows are

    (a^{-k}w,k,w), k in Z, with c_U=k log a.

Lag, clock and joint kernels are units. The only periodic point is 0,
whose entire basin is {0} by bijectivity. Its source isotropy is Z,
H=log a Z, extension isotropy zero, and phase h modulo log a.
Its one positive primitive is log a, with all positive integer repeats.

All nonzero source classes have unique anchors epsilon v, epsilon in
{+1,-1}, 1<=v<a, and states epsilon a^n v for all integers n. They
have zero source/extension isotropy and H, and complete real phase
h+log|x|. For a parent anchor v in[1,2), its class splits under R
according to parity of n, with sample anchors v and2v in[1,4).
This accounts for every nonzero history and sampled class.

The embedding image is exactly parent even-lag arrows; there is no
extra terminal loss. The parent fixed primitive is log2, while the
sample fixed primitive is log4, a composite-integer logarithm. There
is no time renormalization identifying these two whole stabilizers.

## 8. Control B — two sheets and retained prime multiplicity

Let a=sqrt2 and lambda_0=log a. The parent map
T(x,j)=(a x,j+1 modulo2) has total inverse (X/a,j-1 modulo2).
For Lebesgue times counting measure its every-point IMAGE factor is
1/a: permutation of the counting sheet contributes no extra factor2.
The sample R(x,j)=(2x,j) has inverse(X/2,j), IMAGE factor1/2 and
step clock log2=2lambda_0. Every-Borel identities hold separately on
the two measurable sheets and then by their disjoint union.

For every integer n,

    T^n(x,j)=(a^n x,j+n modulo2),
    R^n(x,j)=(2^n x,j).

The parent source-oriented arrows have ranges (a^{-k}x,j-k) and clock
k lambda_0. Sample arrows have ranges(2^{-k}x,j) and clock k log2.
Both owners' lag, clock and joint kernels are units.

At x=0 the parent has ONE least-two core {(0,0),(0,1)}, with no
other incoming points. Source isotropy is2Z, entire H=log2 Z,
extension isotropy zero. With anchor(0,0), its phases are h on sheet0
and h+lambda_0 on sheet1, modulo log2. Its primitive is log2.
The sample has TWO separate fixed cores, one on each sheet, each
with singleton basin, source isotropy Z, H=log2 Z, extension isotropy
zero, and phase h modulo log2. Each has primitive log2 and ordinary
integer repeats. Their multiplicity is two, not a divided clock or
one merged packet. This is the g=2 case of the general formula.

For x!=0, parent source anchors are (epsilon v,J), 1<=v<a, with
states (epsilon a^n v,J+n modulo2). These are all non-eventual classes.
Each splits into two sampled classes according to n modulo2. Globally
the sampled anchors are (epsilon v,j), 1<=v<2, on each fixed sheet.
All such classes have zero source/extension isotropy and H; their
complete real phase for either owner is h+log|x|. Every inverse depth
is included by the all-integer iterate formulas. The embedding image
is precisely the parent even-lag arrows, with no terminal-boundary loss.
The parent core has rational exp(|C|)=2; the sampled failure is prime
uniqueness, not a false claim that these fixed primitives became log4.

## 9. Control C — the irrational-parent boundary

For parent a=sqrt5 and sample a=5, each owner is the whole-line scalar
diffeomorphism U(x)=a x, with inverse IMAGE factor1/a and own clock
log a. All arrows, kernels, source anchors and phases have the exact
scalar formulas of Section7, now with these specified values of a.
This is a direct application of those explicit formulas, not a change
of carrier or measure: U^n x=a^n x at every point and integer n.

Only0 is periodic, with singleton full basin, source isotropy Z,
H=log a Z, extension isotropy zero and phase h modulo log a.
All nonzero anchors epsilon v, 1<=v<a, describe all non-eventual
classes, with zero isotropy/H and real phase h+log|x|. Parent classes
split by parity into sample classes with anchors v and sqrt5*v in[1,5).
The embedding image is exactly parent even-lag arrows.

The parent primitive is log sqrt5, whose exponential is irrational;
the sampled primitive is log5, with exactly one positive packet and
all positive integer repetitions. Thus the sample meets nonempty
positive, prime-pure and prime-unique data for this control, but not
all-prime coverage. It supplies no endogenous arithmetic source.
The rational-parent hypothesis fails precisely where it should:
sqrt5 cannot be rational, since a coprime fraction squared to5 would
force both numerator and denominator to be divisible by5. Hence this
is a boundary control, not a counterexample to Section6 and not a
license for a universal no-go over irrational parent multipliers.

## 10. Control D — complete terminal merging and strict image loss

The parent legal sources are exactly (-1,0) union(0,1), with
T(x)=x^2+2. Every legal image is in(2,3), hence terminal. The two
actual inverse branches are

    theta_+(y)=sqrt(y-2), theta_-(y)=-sqrt(y-2), 2<y<3,
    J_+(y)=J_-(y)=1/[2sqrt(y-2)].

Each is a C1 inverse diffeomorphism on its actual open interval, so
the every-Borel IMAGE identity holds, with the displayed geometric
value at every point. Parent kappa(x)=log(2|x|) on the legal sources.
The excluded critical point0 is terminal and is not added to a branch.
The targets2 and3 have no inverse because their formal roots are
excluded boundary sources. All these boundary objects remain in X.
No next-step test is imposed on y in(2,3), despite its terminal status.

There is NO source with two legal parent steps. Thus D_2 is empty:
the sampled map has the same full real carrier and measure, but no
transitions or inverse branches. Every object is a sampled terminal,
each source class is a singleton, and G_R is precisely the unit
groupoid. All three sampled kernels are units, source and extension
isotropy and H are zero, and the full phase is the real coordinate h.
There is no positive primitive or repetition ledger. This does not
add an identity step at a sampled terminal.

For the parent, every b in(2,3) has the complete three-point class

    C_b={b,+u,-u}, u=sqrt(b-2) in(0,1).

All other objects outside the legal source intervals and(2,3) are
isolated parent terminals. Put d(b)=0,d(+u)=d(-u)=1 and
A(b)=0,A(+u)=A(-u)=K=log(2u). Every parent arrow in C_b is exactly

    (z,d(z)-d(w),w), c_T=A(z)-A(w), z,w in C_b.

This lists all nine ordered-pair arrows: three units; the two
coalescing arrows(+u,0,-u) and(-u,0,+u), always of clock zero;
the two arrows(plus/minus u,1,b) of clock K; and their inverses of
lag-1 and clock-K. No other parent lag occurs. The lag kernel has
the three units and the two coalescing arrows. For u!=1/2, the clock
kernel equals that lag kernel. For u=1/2, b=9/4 and K=0, the clock
kernel is all nine arrows. The joint kernel always equals the lag
kernel. This retains nonisotropy zero-clock arrows and signed step
clocks, rather than interpreting them as periodic source loops.

Every parent source and extension isotropy and H is zero. A complete
real parent phase is h at b and h-K at either incoming source.
Isolated terminal phases are h. No parent class is periodic or has
an infinite forward history. The three-point classes and isolated
terminals therefore exhaust the full parent ledger and all inverse
depths; there are no positive physical primitives.

Each C_b splits into THREE sampled singleton classes, even though
r=2. The two incoming points share parent depth residue1 but have
different last sampled endpoints, namely themselves. This proves why
depth residue alone is insufficient in the terminal classification.
In particular (+u,0,-u) is a parent arrow of lag divisible by2 and
clock zero, but it is not in Phi(G_R). Its minimal parent witness is
m=n=1, meeting at terminal b; alignment would require one further
parent step, which is illegal. Thus Phi(G_R) is strictly smaller than
the parent's divisible-lag subgroupoid. The failure is a missing
merging arrow, not a removed point or an artificially selected quotient.

## 11. Scope and immutable raw handoff

The refined IMAGE clock, embedding and exact image, all three history
types, and all four complete controls have been derived from the card.
The terminal boundary is explicit; infinite-tail padding is justified
only where an infinite legal tail exists. Zero-clock source isotropy,
all incoming points, nonunit coalescence, whole H and real phases are
retained. No signed clock is turned into a positive roof by definition.

The rational-parent obstruction is conditional and has the specified
irrational boundary. The control meeting a limited prime benchmark is
still external and does not establish all-prime coverage or an arithmetic
source. The lineage audit concerns finite symbolic batching against
actual partial evolution, not a generic arithmetic admission theorem.
Classical N/A; arithmetic T1 NOT PASSED; T3 NOT AUDITED;
formal UNASSIGNED; B NOT INVOKED. No455 work was begun.

Only this raw evidence file was written. The RAW READY notification
will contain receipt only, no scientific outcomes. Stop pending root's
FULL raw read and a DISTINCT PAPER UNLOCK. These raw bytes remain
immutable after manuscript exposure; any later correction requires an
explicit erratum rather than silently rewriting the derivation.
