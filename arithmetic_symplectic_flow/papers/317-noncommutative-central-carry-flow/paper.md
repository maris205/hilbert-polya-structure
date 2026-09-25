# Noncommutative central carry: an owned fourth-power clock excluding prime primitives

Candidate ID: `ANG-20260920-CCF01`.
Status: `OWNED CENTRAL-CARRY CLOCK; PRIME TIMES EXCLUDED — STOP / FORK`.
Date: 2026-09-20. Exact Markdown research record, not a publication.

## Abstract

On all signed real triples we audit a state-read integer-cell
quotient with a noncommutative central borrow, anisotropic dilation and
polynomial feedback. Complete inverse branches and ordinary three-volume supply
the same object's all-point IMAGE clock. The ONLY fixed point
is the origin and its time group is zero. More
decisively, every actual positive primitive at ANY source period would
have least time 4log N for an integer N>=2,
not log of a prime. This is a universal time
obstruction, not proof that positive higher periods exist or do
not exist. Those remain OPEN. Separately owned controls exhibit a
genuine primitive log16 packet and three log16 fixed packets, while
a unit-dilation control has globally zero time. All finite predecessors,
null cuts and source/extension isotropy remain. No formal Route
coordinate, classical symplectic realization or operator is asserted.

## 1. Frozen source and precise symbolic lineage

The [original card](candidate-card.md), first 197 lines, SHA-256
`301ff3423c91673e6baae9e2287579059465b7b46eaee5e2a97a0cd7c5af1054`,
freezes X=R^3, ordinary Borel structure and Lebesgue volume.
Define

    (a,b,c)*(r,s,t)=(a+r,b+s,c+t+a*s),
    delta_m(a,b,c)=(m*a,m*b,m^2*c).

Direct substitution verifies associativity, the identity (0,0,0), inverse
(-a,-b,-c+ab), and the multiplication-preserving dilation. These are
the defined laws, not permission to add ambient group arrows.
At each actual g=(x,y,z) write

    A=floor x, B=floor y, r=x-A, s=y-B,
    C=floor(z-A*s), t=z-A*s-C,
    gamma=(A,B,C), f=(r,s,t) in [0,1)^3.       (1)

Thus g=gamma*f, uniquely, including every signed floor and cut.
Its cell D_gamma has the three half-open inequalities in the card.
With m=1+|C|, define nonnegative residues and integer quotients

    A=m*a+j1, B=m*b+j2, 0<=j1,j2<m,
    C=j1*m*b+m^2*c+j3, 0<=j3<m^2,
    d=(j1,j2,j3), eta=(a,b,c).                 (2)

Then gamma=d*delta_m(eta) by the actual multiplication law.
For F(x,y,z)=(y,z,x+yz), its displayed inverse is
F_inverse(u,v,w)=(w-uv,u,v). The total autonomous map is

    T(g)=F(delta_m^(-1)(d^(-1)*g)).              (3)

All next digits come from its new REAL coordinates. Every
state, axis and cut is retained; m=1 at C=0
uses the same formula, with zero digits. No terminal,
reset, infinity, root fibre, atom or independent scale is added.

The actually used digit j1 satisfies m|A iff j1=0.
On the ENTIRE cell gamma=(n,0,d0-1), n,d0>=1,
m=d0 and the observable is d0|n, with proper-divisor
symbols at 1<d0<n. No cell is deleted on this
test. The lineage is divisor-symbolic readout -> current remainders ->
noncommutative quotient/borrow -> real feedback. Factor sets are at
most derived read-only observables, not input tables or time selectors.
Multiplication, m, dilation powers, F and measure remain DECLARED
DESIGN; stronger naturalness OPEN. There is no claimed Logistic/Henon
conjugacy or classical symplectic lift. See the [source record](evidence/scout-record.md)
for exact access and the separate pending frontier.

## 2. Complete inverse/image, including infinite incoming branches

For every integer gamma and its own m,d, the actual
inverse is

    theta_gamma(u,v,w)=d*delta_m(w-uv,u,v)
       =(j1+m*(w-uv), j2+m*u, j3+m^2*v+j1*m*u). (4)

Its entire domain E_gamma is exactly theta_gamma(u,v,w) in
D_gamma. Necessity follows by undoing each factor of (3);
sufficiency follows because that cell test recovers the very digits
used in (4). Different gamma have disjoint source cells,
so different branches meeting a target give distinct predecessors. The
exact image is the union of ALL E_gamma, not a
chosen branch or finite integer box.

An explicit complete target-wise enumeration sharpens this description. For
a target w0=(u,v,w), put

    p=w-u*v, a=floor p, rho=p-a,
    b=floor u, sigma=u-b,
    c=floor(v-a*sigma), tau=v-a*sigma-c.          (5)

For each integer m>=1 require

    rho<1/m, sigma<1/m, tau<1/m^2.              (6)

Let S_1={0} and S_m={-(m-1),m-1} for m>=2.
For ALL j1,j2=0,...,m-1 and C in S_m, set

    j3=C-m^2*c-j1*m*b,
    A=m*a+j1, B=m*b+j2.                        (7)

Keep precisely 0<=j3<m^2 and output (4). Equations (5)–(7)
enumerate EVERY predecessor and none twice. To prove this, (4)
gives fractional source x=m*rho and y=m*sigma. Their floor
digits are consistent exactly under the first two tests in (6).
Subtracting A times the fractional source y from its z gives

    j3+j1*m*b+m^2*(v-a*sigma),

so central-digit consistency is exactly the third test and (7).
Finally C in S_m is precisely m=1+|C|. The
singleton S_1 prevents duplicate enumeration of C=0. This yields
an exact countable formula for image/multiplicity, without truncation.

Every NONINTEGER target has only finitely many predecessors: unless u,v,w
are all integers, at least one of rho,sigma,tau is
positive, and (6) bounds m; all remaining digit choices
are finite. Integer targets need not have finite multiplicity. At
origin, the complete immediate predecessor set is

    {(A,B,C) in Z^3:C>=0, 0<=A<=C, 0<=B<=C}. (8)

Indeed theta_gamma(0)=d is integer, hence its actual cell
must have gamma=d; then C=j3>=0 and m=C+1.
Conversely every listed triple has quotient zero and maps to
origin. This is countably infinite, with all branches retained.
The map is not onto: target (0,1,0) has a=b=0,
c=1, rho=sigma=tau=0, and (7) would require
j3=C-m^2<0 for every C in S_m. It is
a total countable-to-one Borel map, not globally finite-to-one.
No continuity, etale or Hausdorff structure is inferred.

## 3. Actual volume clock and the global time obstruction

In (4), left multiplication by d is affine triangular with
determinant 1; F_inverse has determinant 1; delta_m has determinant
m*m*m^2=m^4. Thus on EVERY actual inverse branch

    J_gamma=m^4,
    mu(theta_gamma E)=integral_E m^4 dmu,
    kappa(g)=-4 log m(g).                        (9)

This is change of variables for the actual polynomial bijection,
restricted to its actual domain. The frozen analytic formula supplies
the same finite positive density on every retained null cut/axis.
A.e. uniqueness alone would not prescribe those values; no atom
ratio, branch count or log-prime roof supplies (9).

For a k-step history put Q_k(z)=product_(0<=i<k)m(T^i z),
with Q_0=1. The full retained-lag arrow (z,k-l,w),
source w and range z, has actual branch-pair IMAGE and clock

    J_g=Q_k(z)^4/Q_l(w)^4,
    c(g)=-4log Q_k(z)+4log Q_l(w).               (10)

Common extensions append identical future factors and cancel. Two presentations
of the same triple have a common extension, so (10)
is pointwise independent of presentation; synchronized middle histories prove
composition. All actual finite branch pairs are retained, not ambient
group translations or free digit words. This gives the countable
Borel groupoid and its extension on ALL X x R_h,
with arrows (w,h)->(z,h+c) and translation h->h+time.
An actual forward arrow has lag -1 and time +4log m.

For ANY eventually periodic state z, let P>=1 be the
least source period of its actual eventual cycle and set

    N=product_(i=0,...,P-1) m(on that cycle).     (11)

For a total deterministic map the source isotropy is exactly PZ:
nonzero equality of two iterates is equivalent to eventual periodicity,
and the differences are precisely multiples of the least cycle length.
Finite entry prefixes cancel in loops. Hence its ENTIRE time
image and extension kernel are

    N=1: H_z={0}, extension kernel=PZ;
    N>=2: H_z=(4log N)Z, extension kernel={0}.  (12)

At a state not eventually periodic all three groups are trivial.
Thus any actual positive primitive must have least time

    L=4log N=log(N^4), N an integer >=2.        (13)

N^4 is composite and cannot be a prime. Nor may
one divide the clock by four, discard three traversals, or
merge different packets: (12) is the FULL group of this
frozen owner. Every positive repeated time is log(N^(4r)),
r>=1, of the same actual packet. This excludes prime
primitive times at EVERY source period, not only fixed points.

Crucially, (11)–(13) are conditional on an actual cycle: they
do NOT prove a positive cycle exists. Its possible N-values,
positive higher-period existence and a complete source cycle census remain
OPEN / UNCLASSIFIED. No finite orbit data or absence argument
has been substituted for this universal algebraic time obstruction.

## 4. Complete main fixed locus: only the zero-time origin

At a putative fixed state use its OWN (1)–(2).
Because delta_m^(-1)(d^(-1)g)=eta*delta_m^(-1)f, its three
coordinates before F are

    a+r/m, b+s/m, c+a*s/m+t/m^2.               (14)

Fixedness gives x=b+s/m. Since 0<=s/m<1, this
forces A=b, r=s/m, hence

    0<=r<1/m, B=m*A+j2, s=m*r,
    y=m*A+j2+m*r=c+a*r+t/m^2,
    z=a+r/m+x*y.                               (15)

For m=1, C=0 and digits vanish, so T=F at
that point. A fixed point of F has x=y=z and
x=x+x^2, forcing origin, which is indeed fixed.

Suppose m>=2. Then C=+(m-1) or -(m-1). The
following cases exhaust ALL integer A, with no diagonal restriction.

If A>=1, then a<=A/m and
c=floor((C-j1*m*A)/m^2)<=0. Equation (15) gives
y<(A+1)/m^2, whereas y>=m*A, impossible.

If A<=-2, then c>=-1 and a=floor(A/m)>=
(A-m+1)/m. Since a<0 and r<1/m,

    y>-1+(A-m+1)/m^2, while y<m*(A+1).

The first bound exceeds the second: their difference is at
least m-1-(m+1)/m^2>0 for m>=2, obtained at A=-2.
This is again impossible, without truncating negative integer cells.

If A=0, then a=j1=0, and c is 0
or -1 according to the sign of C. Since y>=0,
c=-1 is impossible. Then y=t/m^2<1/m^2 forces
j2=0. From (15), 0<=z=r/m+r*y<1/m^2+1/m^3<1.
As A=0, this forces C=floor z=0, contradiction.

If A=-1, then a=-1,j1=m-1 and c=0 for
B's quotient b=A=-1 and either allowed sign of C.
Thus -1/m<y=-r+t/m^2<1/m^2. But B=-m+j2<=-1,
so y=B+m*r<0; necessarily B=-1 and j2=m-1.
Now -1+m*r=-r+t/m^2 forces r>=1/(m+1).
Using the third equation of (15) and s=m*r,

    z-A*s=r*(m*r-1+1/m).

For 1/(m+1)<=r<1/m this is strictly positive and
strictly less than 1/m^2, hence C=0, contradiction.

Therefore origin is the ONLY main fixed point. Its source
isotropy is Z, H=0 and extension isotropy Z. Its complete
basin is B_0=union_(d>=0)T^(-d){0}, enumerated with ALL
branches (4), including the infinite direct set (8). Every
predecessor is an integer triple, because (4) maps integer targets
to integer sources; no noninteger finite tail is silently selected.
We do not claim a simpler complete list of B_0.

For z in B_0 let d(z) be first hit and S(z)
its kappa prefix sum. All integer lags between two points
of B_0 occur, and (10) gives c=S(z)-S(w), since
the core clock is zero. The complete height invariant is
h-S(z), with residual source/extension Z at each object.
Thus this fixed-basin quotient has free real translation and no
positive primitive, despite genuine source recurrence and infinitely many predecessors.

## 5. COMMUTATOR-OFF — one positive fixed packet survives

This control uses ordinary cubes, C=floor z and digits
A=m*a+j1, B=m*b+j2, C=m^2*c+j3. Its own
map is F(delta_m^(-1)(g-d)), inverse

    (j1+m*(w-uv), j2+m*u, j3+m^2*v),          (16)

on exactly the inverse's original cube. For a complete target
enumeration use a=floor(w-uv), b=floor u, c=floor v
and their fractional parts rho,sigma,tau. Conditions (6) apply,
with C in S_m, j3=C-m^2*c in [0,m^2),
and ALL j1,j2 in [0,m). This is its OWN
exact union image and every predecessor, not the main central
test. For c=0, m=1 already gives an image point;
for c=-1 the allowed m start at 2. Other c
give no predecessors. Noninteger targets have bounded m, while e.g.
origin has countably infinitely many predecessors. No cutoff is imposed.

Each inverse (16) has determinant m^4, so its OWN
kappa=-4log m and whole-period formula (12)–(13) follow
on its OWN histories. In particular they do not establish
an equality of main/control packet identities or return sets.

For fixed points, m=1 again gives only origin. If m>=2,
fixedness gives x=b+s/m, A=b, r=s/m and

    B=m*A+j2, y=B+m*r=c+t/m^2,
    z=a+r/m+x*y, c=floor(C/m^2).               (17)

If C=m-1, c=0, so y<1/m^2 forces B=A=j2=0;
then z>=0 and z<1, contradicting C>0. If C=-(m-1),
c=-1 and y=-1+t/m^2 forces B=-1,A=-1,j2=m-1,
a=-1,j1=m-1 and r=t/m^3. Substituting gives

    z=-t/m^2-r*(1-1/m)+r*t/m^2.

For 0<t<1 it lies strictly between -1 and 0;
t=0 would give C=0 and is inadmissible here. Hence
C=-1 and m=2. Since t=8r and z=-1+t,
the remaining equation is

    4r^2-21r+2=0, 0<r<1/8.

Exactly one root qualifies:

    r_*=(21-sqrt409)/8,
    z_*=(x,y,z)=(-1+r_*,-1+2r_*,-1+8r_*).      (18)

The exact bounds 20<sqrt409<21 verify all these half-open
cell inequalities. Thus ALL control fixed points are origin and
z_*, not just a numerical example. The latter has source
Z, ENTIRE H=(4log2)Z=(log16)Z and extension kernel zero.
Its full actual inverse basin contributes ONE positive primitive packet,
not a repetition of another core. Origin's basin has H0
and source/extension Z. Other source cycles remain UNCLASSIFIED.

## 6. FEEDBACK-OFF — full zero region and three positive cores

Keep the main cells/digits/multiplication, replacing F by identity.
Its OWN inverse is d*delta_m(u,v,w), on that point
belonging to D_gamma. The exhaustive target enumeration (5)–(7)
now uses p=u, the second horizontal coordinate v and
the central coordinate w, rather than F_inverse of the target.
This follows by solving this inverse's cell tests directly. Its
Jacobian is m^4 by the actual triangular/dilation factors; its
own clock and all-period obstruction are again (9), (12)–(13).

The entire region U={g:C(g)=0} is fixed, because m=1
and all digits vanish. It is retained in full, with
H=0 and source/extension Z at every fixed point, not
one representative chosen from a continuum.

For m>=2, fixedness of the first coordinate says
A-a=-(1-1/m)r. Its right side is in (-1,0]
and its left side integer, so r=0 and A=a.
Hence (m-1)A+j1=0, giving A=0 or -1. The
second coordinate similarly gives s=0 and B=0 or -1.
The central equation then forces t=0,C=c, leaving

    (m^2-1)C+j3+j1*m*B=0.                     (19)

For C=m-1, the left side is at least
(m-1)(m^2-m-1)>0, impossible. For C=-(m-1), its
maximum is -(m^2-1)(m-2), so equality requires m=2,
j3=3 and j1*m*B=0. Precisely THREE fixed points remain:

    (0,0,-1), (0,-1,-1), (-1,0,-1).            (20)

All satisfy their actual cells/digits and (19); (-1,-1,-1)
does not. Each has source Z, ENTIRE H=log16 Z
and extension kernel zero. Their complete finite inverse basins cannot
merge because their actual fixed futures differ. They are three
different positive primitive packets, not three phases of one packet.
Every fixed point in U also keeps all its incoming branches.
No classification of higher control cycles is claimed.

## 7. UNIT-DILATION and full-basin control ownership

UNIT-DILATION has m=1 everywhere, zero digits and action F
on the entire R^3. Its exact global inverse F_inverse
has determinant 1, so its OWN kappa=c=0 globally.
ALL time stabilizers H are zero. Its only fixed point
is origin, with source/extension Z; its unique inverse is
origin itself, so that fixed basin has no other points.
Higher source periods remain UNCLASSIFIED; zero time is not a
claim that all source isotropy vanishes. Extension isotropy equals source
isotropy wherever the latter occurs.

For each fixed core f in the first two controls, the
FULL basin means the union of all legal finite predecessors
under that control's exhaustive inverse domains, with no selected word
or depth cutoff. If d(z) is least entry depth,
S(z) its own kappa prefix and a=kappa(f), all
integer lags occur and

    c(z,ell,w)=S(z)-S(w)+(ell-d(z)+d(w))*a.     (21)

For a nonzero, the complete phase is h-S(z) modulo
|a|, one packet per fixed core, with H=aZ and
trivial extension kernel. For a=0 the phase is the
real number h-S(z), H0 and source/extension Z remain.
No equal clock or coordinate value across different controls identifies
their sources. These are their OWN actual basins and prefix sums.

## 8. Gate synthesis, limits and portfolio decision

T0 and the owned part of T1 are established: the
entire noncommutative cell transport, real arithmetic readout, inverse/image and
volume clock have one frozen owner. Stronger arithmetic naturalness remains
OPEN; the dilation degree and pointwise version are declared designs.

The main's complete fixed locus is only a zero-time core.
Positive higher-period existence remains OPEN. Independently, the all-period
time theorem excludes ANY log-prime primitive, so the T2
prime-time target fails without waiting for a cycle census. The
changed controls supply genuine log16 positive primitives, demonstrating why
source recurrence and correct prime primitive time must remain separate.

Null axes/cuts use the frozen analytic version, not a.e.
uniqueness. The quotient is only Borel/set-level, and a phase
circle is not a claimed embedded geometric orbit. No global
continuity, etale structure, Hausdorff quotient, classical symplectic base or
positive-roof mapping torus has been established. Dividing the clock by
four would change the owner; it is not a normalization
licensed by this audit. No universal central-carry impossibility follows for
other clocks or architectures.

Portfolio STOP / FORK. Preserve the source, complete fixed/control
results and global prime-time negative; do not extend this stopped
object into T3. T3 NOT SUPPLIED / NOT PURSUED;
classical A0/A1/A2 NOT APPLICABLE; formal coordinates UNASSIGNED;
B NOT INVOKED. No operator, trace, zeta or RH claim.

See [ledger](claim-ledger.md), [evidence](evidence/README.md) and
[internal review](evidence/independent-review.md) for exact scope and all
three ARS checkpoints. Review is inherited-model/shared-history internal AI,
NOT_CALIBRATED, not external peer review or formal proof. No
scientific numerics, prime tables, empirical cutoff or external campaign.
Positive 304 and old packages unchanged; 241/242 paused;
goal active. Markdown only; no publication, upload or Git commit.
