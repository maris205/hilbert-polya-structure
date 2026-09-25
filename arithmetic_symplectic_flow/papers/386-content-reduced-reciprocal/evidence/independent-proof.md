# Card-only independent proof — ANG-20260922-CRR01

2026-09-22; batch `GEOMETRIC-RETURN-20260922-H`, round 2/5.
Verdict: `STOP — OWNED POSITIVE PRIMITIVE WITH NONINTEGER MULTIPLIER`.
Internal shared-history evidence: `NOT_CALIBRATED`, not external peer review.

## 0. Input, release and scope

The original card was fully read before CP1, and its sole target-specification
gap was reported without mathematical derivation. Root preserved those bytes,
appended the target clarification before releasing mathematics, and explicitly
authorized the raw proof once that clarification passed review. I reread the
whole 66-line card through EOF, verified both hashes, and appended the PASS
disposition to scope before starting mathematics.

candidate-card.md — 66 lines — SHA256 61ed514128aa4a7660a8f60c30cab978bbd35fccd8d0d64f35689cf60af5f781
candidate-card.md (original lines 1–55) — SHA256 172fe27af715c5a2acecd55abdd4c5953518628b2712b93eee01f0c80207891a
scope-review.md — 75 lines — SHA256 922902ed3dab4ee7b2e4917e7b19c03d4101690796a405634115ec4295aed1fb

This card is the sole scientific input. No main/peer/scout, other scientific
package, web source, numerical experiment, auxiliary agent or model change was
used. Prior project history and evidence authorship are shared. Current raw
derivation is separated from the unread main, not blind or cross-model review.
ARS instructions were previously fully read as disclosed in scope and retained.
The decisive fixed-packet result was sent to root before writing this report.
The necessary target is every positive MAIN primitive L=log p, p an ordinary
integer prime. Coverage, multiplicity and sufficiency are outside this first
test. Controls are independent diagnostics. No other-cycle census follows.

## 1. Four full owners, branches and boundaries

For each owner take its own Y=N_(>=1) x [0,1], counting x Lebesgue measure mu,
and the given Borel structure. Let U={(n,x):x>0}; T is undefined on x=0.
For n>=1 and a>=n define the disjoint source interval

    B_(n,a)={n} x (n/(a+1), n/a].

These intervals partition U. Indeed a=floor(n/x) iff a<=n/x<a+1, which is
equivalent to that interval, and x<=1 implies a>=n. For d=gcd(n,a), use

    MAIN: (R,S)=(a/d,d); D: (a,1); H: (n,d); Q: (a/d,1).

Each has positive integer R,S. On B_(n,a), T(n,x)=(R,(n/x-a)/S) belongs to
{R} x [0,1/S), a subset of the full Y. The actual inverse chart is exactly

    E_(n,a)={R} x [0,1/S),
    theta_(n,a)(R,y)=(n,n/(a+S y)).

This is precisely the frozen proposed domain: a>=n makes 0<x<=1 automatic,
and S>=1 makes S y<1 imply y<=1. On it, n/x=a+S y has floor a; the gcd is
the same d and the target root is the prescribed R. Thus T theta=id and
theta T=id on the displayed domains. These identities and the partition
prove completeness, not merely a list of possible inverses. Distinct labels
cannot create duplicate one-step arrows: the source determines n and then a.

The upper source endpoint n/a is included and maps to (R,0); the excluded
lower endpoint n/(a+1) belongs to the next digit branch. The point (n,1)
belongs to a=n and maps to (1,0) in MAIN/Q and to (n,0) in D/H. Every (r,1)
has no incoming one-step arrow, since all image coordinates are <1, but its
own legal outgoing step is retained. Every (r,0) is a retained terminal.
These are boundaries of the actual partial map, not deleted or absorbing loops.

For a target (r,y), the following are ALL incoming source points; conditions
and actual points, not branch labels, are the enumeration. Every line also
requires 0<=y<1; at y=1 there are none. Put C_r={q:1<=q<=r, gcd(q,r)=1}.

    MAIN: (d q, q/(r+y)), q in C_r, d>=1, d y<1;
    D:    (n, n/(r+y)), 1<=n<=r;
    H:    (r, r/(a+gcd(r,a)y)), a>=r, gcd(r,a)y<1;
    Q:    (d q, d q/(d r+y)), q in C_r, d>=1.

For MAIN/Q, writing a=d r and n=d q is equivalent to gcd(n,a)=d precisely
when gcd(q,r)=1; a>=n becomes q<=r. Conversely these parameters reproduce the
required branch, proving exhaustion. D fixes a=r and H fixes n=r. Outputs
are distinct: in MAIN x determines q then n determines d; in Q equal n,x
determine a=n/x-y and hence d,q; D has distinct roots, and H has distinct
source branch intervals. Thus no invisible arrow multiplicities are inserted.

In particular ALL direct terminal predecessors are

    MAIN/Q at (r,0): (d q,q/r), q in C_r, d>=1;
    D at (r,0): (n,n/r), 1<=n<=r;
    H at (r,0): (r,r/a), a>=r.

Their further finite predecessors are obtained by iterating the full lists,
deduplicating actual points/arrows. No terminal-root fibre is identified with
another merely because their clock values agree.

## 2. Same-measure every-Borel IMAGE and all-point versions

Each inverse chart is a decreasing smooth rational bijection between its
half-open intervals, with positive absolute derivative

    J_(n,a)(R,y)=n S/(a+S y)^2.

It is finite, strictly positive and continuous on its entire domain. At y=0
the same rational derivative gives the one-sided branch value; no free null
parameter is added. Change of variables for this one-dimensional bijection,
with counting weight one on both root fibres, gives for EVERY Borel E subset
E_(n,a): mu(theta E)=integral_E J dmu. Endpoints are included in both sets and
have measure zero; the stated identity is an exact Borel identity, not a
conull deletion of points. Equivalently one can extend interval identities
by finite-measure uniqueness. Each nonempty relatively open subset of the
half-open domain has positive mu measure. Hence any continuous IMAGE version
equal a.e. to this J must equal it everywhere: its difference cannot be
nonzero on an open neighbourhood of any point. Uniqueness is ONLY among
continuous branch versions, not all measurable versions or across digit cuts.
The countable partition also proves nonsingularity of the partial transport;
mu is sigma-finite, and no invariant probability or invariant flow measure is
asserted. All four owners use their own branch parameters and the same frozen
counting-times-Lebesgue prescription, not a borrowed measure.

At a source (n,x) in a legal branch the local clock simplifies to

    J_(theta_z)(Tz)=S x^2/n,       kappa(n,x)=log[n/(S x^2)].

Here S<=n in all four owners: MAIN/H have S=gcd(n,a), D/Q have S=1.
Thus kappa>=0, and it is strictly positive whenever x<1. A zero clock in
MAIN/H occurs exactly at x=1; in D/Q it occurs exactly at (1,1).
All such zero-clock edges lead to terminals, not loops. There is no clock
for a nonexistent step from x=0. A classical positive-roof suspension has
not been defined by these formulas.

## 3. Actual partial-history groupoid and full kernel formulas

Let U_m consist of points allowing m forward steps, with U_0=Y; the last
iterate may be terminal. All these domains and iterates are Borel. For
z in U_m, write (n_i,x_i)=T^i z for i<m and S_i for its actual branch scale.
The empty product is one. Define

    D_m(z)=product_(i<m) S_i x_i^2/n_i,
    A_m(z)=-log D_m(z).

Finite compositions of the inverse charts have IMAGE density D_m at the
corresponding source point; composition uses the usual pulled-back product,
not a formal product at unrelated endpoints. Repeated change of variables
proves every-Borel finite-history IMAGE, including histories ending at a
terminal. No infinite derivative product is used.

For an actual arrow g=(z,m-l,w) with T^m z=T^l w, the full clock is

    c(g)=log[D_l(w)/D_m(z)].

Two presentations of the same triple have both indices shifted by the same
integer. Passing to the larger pair is legal by its witness, and multiplies
both D's by the identical common-tail product. Hence c descends. To compose
(z,m-l,w) and (w,p-q,v), align at the larger of l,p. The longer legal history
of w guarantees that the corresponding common tail can be extended on the
other side, even with terminals present. Finite-product cancellation proves
addition; inverses negate c. This constructs the full retained-lag Borel
groupoid; its source/range fibres are countable by the countable inverse atlas.

For every actual triple, not just isotropy, the complete finite-history tests
are ker c iff D_m(z)=D_l(w), ker lag iff m=l, and their intersection iff both.
These retain every legal witness, root, endpoint and null point. The groupoid
acts by (w,t)->(z,t+c(g)); the real height action descends to its orbit SET.
No smooth, Hausdorff or regular coarse quotient is inferred.

All incoming source points at z are obtained by taking each legal forward
iterate T^m z and every finite inverse history of length l ending there.
The actual incoming arrow is (z,m-l,w), with source height t-c(g) for a target
height t. This is both necessary and sufficient by the shared-tail definition.
Terminal source orbits consist of all finite histories ending at that same
terminal. There are no positive-length terminal self-iterates and no terminal
source isotropy; all their physical phases are R with zero stabilizer.

## 4. Conditional classification for the remaining full owner

If the forward history terminates or is infinite but not eventually periodic,
source isotropy is trivial: unequal shared-tail indices would create a cycle
and legal indefinite repetition. If an actual history eventually enters a
cycle of least period d>=1, its entire source isotropy is dZ. Indeed a nonzero
isotropy lag is exactly an eventual period, and the set of such lags is a
subgroup of Z with least positive generator d. No other source cases occur.

Every point on a cycle has 0<x<1: x=0 has no successor and x=1 immediately
reaches a terminal. Hence every cycle edge has strictly positive kappa. Let
L be the finite sum over one least-period cycle. Cancelling the common stem
proves c(kd)=kL, L>0, for the entire isotropy, not merely for one witness.
Thus H_z is {0} in the first case and LZ in the second. The full extension
fixed-object isotropy is the clock-zero part of source isotropy and is trivial
in every case. All phases over a source orbit are R/H_z, with coordinate
changes determined by actual incoming arrows. A positive primitive is the
least positive generator L; same-packet repetitions are kL, k>=1. Equal-time
packets and different roots are not identified by this statement.
This is conditional on actual eventual periodicity, not a census or a claim
that the fixed point below exhausts other periodic cycles.

## 5. Entire prescribed fixed set and the decisive physical primitive

At n=1,a=1 all four owners have gcd=1 and R=S=1. The full source branch is
x in (1/2,1], and a fixed point must satisfy x=1/x-1, or x^2+x-1=0.
Its only allowed solution is alpha=(sqrt(5)-1)/2; the second root is negative.
The inequalities 2<sqrt(5)<3 give 1/2<alpha<1, so it belongs to the branch.
Neither endpoint supplies another fixed point. Thus the ENTIRE fixed-point
set in the specified sector is {z*=(1,alpha)} for each own owner.

At z*, J=1/(1+alpha)^2=alpha^2, using alpha(1+alpha)=1. Since every iterate
equals z*, source isotropy is exactly Z and the clock on every lag k is kL,

    H_(z*)=L Z,   L=-log(alpha^2)=log[(3+sqrt(5))/2]>0.

Consequently this is an owned physical primitive, not an unchecked return or
a multiple of an unexamined shorter period. Its multiplier lies strictly
between 2 and 3, so it is not an integer and hence not an ordinary prime.
The MAIN necessary target fails. Each control independently has the same
fixed-sector failure because its own branch, derivative and full H coincide
there. No change of scale, deletion of root one or extra sieve is permitted.

## 6. ALL ancestors, arrows and phases of the tested packet

MAIN: putting r=1,y=alpha in its complete inverse list forces q=1 and
d alpha<1. Since alpha>1/2, d=1 is the only possibility, producing z* again.
Thus every finite ancestor is z* and its complete source orbit is a singleton.
D: its inverse list at r=1 also has only n=1 and produces z*. The same
singleton conclusion follows for its own source orbit, not by identification
with MAIN. Both owners still retain all arrows k in Z and all real heights.

H: root is held, so all ancestors have root 1. Its complete source orbit is
all points (1,f_(a_1) ... f_(a_j)(alpha)), j>=0, a_i>=1, where
f_a(y)=1/(a+y). All finite compositions are taken and actual repeated points
are deduplicated; in particular f_1(alpha)=alpha does not create new states.
The inverse list proves both inclusions, without omitting longer histories.

Q: start E_0={z*} and recursively take E_(j+1) to be E_j together with

    {(d q,d q/(d r+y)) : (r,y) in E_j, q in C_r, d>=1}.

Its complete source orbit is union_j E_j, deduplicated as actual points.
Every point in this construction has 0<y<1, so every displayed inverse is
legal. The exhaustive inverse formula proves conversely that every finite
ancestor is included. Already the direct predecessors (d,d/(d+alpha)), d>=1,
show why replacing this owner by the singleton MAIN fibre would be incorrect.

For each of these four own orbits and each y in it, let h_y be the least
nonnegative hitting time of z* and beta_y=A_(h_y)(y)-h_y L. These are finite
and beta_(z*)=0. For ANY two points z,w in that orbit and ANY k in Z, an actual
arrow (z,k,w) exists by taking both histories sufficiently far past their
hitting times. Every such arrow has exactly

    c(z,k,w)=kL+beta_z-beta_w.

This is the complete packet arrow and clock ledger. In particular all incoming
arrows to (z*,t) from y have heights t-kL+beta_y, k in Z. Source isotropy at
every ancestor is Z, H=LZ, and extension isotropy is trivial. The full phase
coordinate is t-beta_y modulo L; changing the incoming arrow changes it by
an integer multiple of L only. Each owner therefore has one complete tested
packet with all phases R/LZ and repetitions kL. No countable ancestor/null set
has been discarded, and no assertion identifies packets from different owners.

## 7. Lineage, own controls and bounded stop

For the frozen lineage subfamily n=D, x=D/(N+rho), 1<D<N and 0<=rho<1,
the actual digit is N and d=gcd(D,N). MAIN evolves to (N/d,rho/d), whereas
D, H and Q evolve respectively to (N,rho), (D,rho/d), and (N/d,rho).
Thus divisibility enters the actual next root/remainder; it is not an external
prime label. This exact feedback does not establish strong naturalness.

Sections 1–4 give EACH own control its full carrier, inverse atlas, terminal
boundary, same-measure IMAGE, all-point continuous branch versions, legal
history cocycle, kernels and conditional full isotropy/phase description.
Sections 5–6 separately finish the entire prescribed fixed set and its full
incoming packet for each. They are not a partial control based only on a
shared numerical clock. No additional periodic cycle was sought or classified.
The fixed-sector obstruction already occurs where content is one; this
negative control observation cannot justify excluding that retained sector.

Portfolio STOP. Same-object ownership and an actual branch-Jacobian clock are
proved, but the necessary MAIN log-prime condition fails. Strong naturalness
remains OPEN; no sufficiency, prime coverage or multiplicity audit is claimed.
T3 NOT AUDITED; classical fields NOT APPLICABLE; formal UNASSIGNED; B NOT
INVOKED. No empirical, novelty, quantum, zero, operator or publication result
is asserted. This card-only raw report freezes here pending root's full read
and explicit manuscript unlock; scope and candidate bytes remain unchanged.
