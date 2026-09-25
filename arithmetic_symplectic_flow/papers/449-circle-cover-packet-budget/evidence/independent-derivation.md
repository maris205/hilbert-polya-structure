# CPB01 — card-only independent derivation

Candidate: ANG-AUDIT-20260924-CPB01. Paper449.
Reviewer: `/root/rcr01_independent_review`, 2026-09-24 UTC.
Input: original 92-line card, SHA-256
`7463fb44ea9e5231e2559dcd182a469fd4abc7a6a75a6d2ae6086541be49913c`.
Root separately released raw work after its full CP1 read. The C1 inverse
germ clarification is retained: the general class does not assume C-infinity.
No author paper, package README, claim ledger, helper or peer proof was read.
This is same-model shared-history internal AI derivation, NOT_CALIBRATED,
not blind, human, external or cross-model verification. No scientific
numerics, network, citation campaign or external theorem is used below.

## 1. The entire expanding-circle owner

Write pi:R->R/Z. The frozen translation law makes u(x)=f(x)-Nx periodic
and bounded. Therefore f(x) tends to the corresponding infinity at both
ends of R. Since f' >= lambda >1, f is strictly increasing and onto R.
It has a C1 global inverse g with g'(y)=1/f'(g(y)), and

    g(y+N)=g(y)+1, f'(x+1)=f'(x).

For any lift y of a circle target, all its actual preimages are

    pi(g(y+j)), j=0,...,N-1.

Every integer j is equivalent to one of these modulo N. If two displayed
points differ by an integer a, applying f gives j_1-j_2=N a, forcing
a=0 and j_1=j_2. Thus there are exactly N distinct predecessors at EVERY
target, including the target at a chosen cut. No point is terminal.

Near each such predecessor choose real source/target intervals short
enough that pi is injective and f maps the source diffeomorphically to
the target lift. The associated inverse is the appropriate restriction
of g(y+j). Its density for normalized flat circle length is

    J_theta(pi(y))=g'(y+j)=1/f'(g(y+j)).

Changing chart lifts adds integer constants to the coordinates and does
not change this derivative. Changing the real representative of a fixed
actual source uses f'(x+1)=f'(x). Different actual predecessors need not
have equal derivatives: no branch average is used. For every Borel B in
the injective target chart, ordinary one-dimensional substitution gives
mu(theta(B))=integral_B J_theta dmu. Covering a branch restriction by
countably many such charts and disjointifying gives the same identity
on any Borel restriction. This includes null points and sets. The actual
local germ, not an almost-everywhere density representative, fixes J.

Consequently the single own clock is

    kappa(pi(x))=log f'(x),
    S_m(pi(x))=log (f^{circ m})'(x).

These are well-defined at every point. By compactness of a fundamental
interval let M=max f'(x)<infinity. Then log lambda<=kappa<=log M,
and for m>=1, m log lambda<=S_m<=m log M. This is a derivative clock;
it is not a roof set to log N from the covering degree.

Let f_m=f^{circ m}, with f_0 identity. It is a global increasing C1
diffeomorphism of R, f_m(x+1)=f_m(x)+N^m, and f_m'>=lambda^m.
Every depth-m predecessor of pi(y) is exactly

    Pre^m(pi(y))={pi(f_m^{-1}(y+j)):0<=j<N^m}.

The same lift argument proves these N^m predecessors distinct and
exhaustive. Union over all depths retains every inverse history, with
actual point duplicates identified only when they really coincide.

## 2. Exact all-period source count, proved directly

For q>=1 put h_q(x)=f_q(x)-x. It is strictly increasing because
h_q'>=lambda^q-1>0, and

    h_q(x+1)=h_q(x)+(N^q-1).

The equation F^q(pi(x))=pi(x) is precisely h_q(x) in Z. On [0,1),
h_q has image [h_q(0),h_q(0)+N^q-1). A half-open interval of integer
length L contains exactly L integers, even when either endpoint is an
integer. Strict monotonicity gives one point for each integer. Hence

    A_q := #Fix(F^q)=N^q-1, for EVERY q>=1.

The half-open source convention identifies the same circle endpoint
once; it does not remove the endpoint point or either of its local germs.
No numerical root search, trace formula or symbolic completeness premise
has been used in this count.

Let P_q be the number of source points of least period q. A point fixed
by F^q has a least period d dividing q, by division with remainder in its
actual finite orbit. Thus A_q=sum_{d|q}P_d. Define mu(1)=1 and, for n>1,

    mu(n)=-sum_{d|n, d<n}mu(d).

This finite recursion is well-defined and proves
sum_{d|n}mu(d)=1 if n=1, and zero otherwise. Rearranging finite divisor
sums now proves the inversion, rather than assuming it:

    sum_{d|q}mu(q/d) A_d
      =sum_{e|q} P_e sum_{d:e|d|q}mu(q/d)=P_q.

The exact number B_q of least-q source cycles is therefore

    P_q=sum_{d|q}mu(q/d)(N^d-1),
    B_q=(1/q) sum_{d|q}mu(q/d)(N^d-1).

Each actual least-q cycle contains exactly q distinct points. This
proves the division by q is a cycle count, not a division of its clock.
In particular B_1=N-1. For q>1, the constant terms cancel, so
B_q=(1/q)sum_{d|q}mu(q/d)N^d.

There is an actual least-q cycle for every q, not only a formal positive
word count. Indeed for q>=2 every proper divisor d is at most r=floor(q/2),
and

    P_q=A_q-sum_{d|q,d<q}P_d
       >=N^q-1-sum_{j=1}^r(N^j-1)>0.

For the last inequality, sum_{j=1}^r N^j <=N^{r+1}-N<=N^q-2.
The q=1 case follows from N-1>0. This argument uses the already proved
actual fixed-point count, not an independent symbolic realization claim.

## 3. Full groupoid, incoming classes and whole clock groups

An actual arrow (z,k,w), from w to z, has witnesses m,n>=0 with
F^m z=F^n w and k=m-n. If another witness has the same lag, both
exponents change by the same integer; the added common tail has equal
clock and cancels. Thus c=S_m(z)-S_n(w) is well-defined. To compose,
align the two middle exponents at their maximum. The now identical
middle history cancels, proving additivity. The forward arrow
(Fz,-1,z) has clock -kappa(z). Equal endpoint triples with different
lags remain different arrows.

All actual source histories are described exactly by

    O(w)=union_{n>=0} union_{m>=0} Pre^m(F^n w),

using the complete finite-depth formula in Section1. This is a countable
set, with no finite-depth restriction. The following kernel descriptions
are complete membership tests inside this actual G:

    K_lag={(z,0,w):F^m z=F^m w for some m>=0},
    K_c={(z,m-n,w):F^m z=F^n w and (f_m)'(z)=(f_n)'(w)},
    K_joint=K_lag intersect K_c.

Derivative evaluation uses any real representatives; it is periodic and
therefore well-defined. The displayed K_c is the union over all m,n,
not a test at one selected witness. For K_joint one may take m=n.
Different inverse branches can produce nonunit lag-zero arrows. For a
variable derivative no assertion that c is a function only of the lag,
or that the three kernels coincide, is made.

If a source is not eventually periodic, two unequal times cannot meet
on its own trajectory. Its source isotropy is zero, and H is zero. If
it eventually enters a least-q core a_e=F^e a_0, write

    C=sum_{e=0}^{q-1}kappa(a_e)=log (f_q)'(a_0)>0.

Its source isotropy is exactly q Z; the lag r q loop has clock r C.
Every return-time difference is of this form, and the entry sums cancel.
Consequently the ENTIRE H is C Z at every incoming point, the extension
isotropy is zero, and the primitive physical length is C. All positive
repetitions are r C for positive integers r. In particular the lower
bound C>=q log lambda prevents a zero-clock periodic core in this class.

Two distinct deterministic finite cycles cannot merge under unrestricted
incoming arrows. A forward meeting of points on those cycles makes their
cycles identical. Every eventual class is therefore the full basin of
exactly one actual core. Thus B_q is also the number of full source
packets whose eventual core has least source period q.

For a core O of q points its full basin is union_m Pre^m(O). The sets
are nested, have cardinality q N^m, and exhaust all incoming histories.
The first-arrival layer of depth m>=1 has q(N^m-N^{m-1}) points.
These are countably infinite basins, not merely their finite cores.

For explicit complete phases and kernels on such a basin, put
A_e=S_e(a_0), ell=C/q. If z first reaches a_{e_z} at depth d_z, set

    chi_z=e_z-d_z,
    beta_z=S_{d_z}(z)-A_{e_z}+chi_z ell.

All arrows between z,w in the basin are exactly those integers k with
k congruent chi_w-chi_z modulo q, and their clock is

    c(z,k,w)=k ell+beta_z-beta_w.

The congruence follows by matching sufficiently late core phases. The
clock formula follows by expanding both sums to that meeting phase;
it remains correct when individual core step clocks differ. Lag, clock
and joint kernels impose respectively k=0, the displayed clock equal
to zero, and both. The extension orbit phase is

    h-S_{d_z}(z)+A_{e_z} modulo C Z.

For a non-eventual class choose a source anchor a, and one arrow a->z
with clock b_z for each z in its class. There is only one possible
clock between these endpoints, since a second would differ by isotropy.
Its full extension phase is h-b_z in R. More generally this anchor
description is h-b_z modulo H. It is a set-level description only:
no global measurable selector or nice orbit space is asserted. Physical
height translation has stabilizer exactly H, by the isotropy-arrow
criterion, and all real heights are included.

The counts B_q alone neither evaluate the derivative product C nor
attach a prime label to a packet. Source repetition replaces (q,C)
by (r q,r C); it is not a prime-power law unless an independent
same-owner argument has first supplied a primitive log p. Degree and
source count must not replace that argument.

## 4. Complete linear controls, common formula for N=2 and N=3

Take f(x)=Nx, with N separately equal to 2 or 3. Each full circle owner
has the complete inverse set pi((y+j)/N), j=0,...,N-1, and every-point
inverse IMAGE density 1/N. Hence kappa=ell=log N is DERIVED from the
inverse, not inserted. Every-Borel identities include every cut endpoint.

All histories and arrows are exactly

    Pre^m(pi(y))={pi((y+j)/N^m):0<=j<N^m},
    (z,m-n,w) whenever N^m z-N^n w is an integer.

Here z,w may be any real representatives. The complete source class is
the union of these inverses of all forward iterates N^n w. For every
arrow c=(m-n)ell=k ell. Thus all three kernels are the SAME full
lag-zero equivalence relation,

    {(z,0,w):z-w belongs Z[1/N] modulo Z}.

This is not the unit groupoid: all distinct points coalescing at equal
depth remain in the kernel. No nonzero-lag arrow has zero clock.

The exact fixed points of F^q are

    pi(j/(N^q-1)), j=0,...,N^q-2.

The exact least-period point and packet counts are P_q and B_q from
Section2. Equivalently remove all points belonging to the proper-divisor
fixed sets. Every q has B_q>0. Each least-q core gives one full incoming
packet with source isotropy q Z, H=q ell Z, extension isotropy zero,
primitive q ell=log(N^q), and positive integer repetitions.

A circle point is eventually periodic exactly when it is rational.
For necessity, equality N^m x=N^n x modulo one, m>n, makes x rational.
For sufficiency, multiplication by N acts on a finite residue set for
any rational denominator. More precisely for these prime bases write
the reduced denominator as b=N^d b_0, gcd(b_0,N)=1. Then d is the
least preperiod, and the eventual period is the multiplicative order
of N modulo b_0, taking order one when b_0=1. On the coprime part,
the numerator is invertible, so the least return criterion is exactly
N^q=1 modulo b_0. This classifies every rational eventual history.

For each actual rational core choose a_0 and enumerate a_e=F^e a_0.
The full basin is the exact union of all displayed inverse sets of its
q core points. For a basin point with first entry depth d_z and phase
e_z, all arrows satisfy k congruent (e_w-d_w)-(e_z-d_z) modulo q.
Their clock is k ell, and the complete phase is

    h+(e_z-d_z)ell modulo q ell Z.

All irrational points are non-eventual. Their classes are the complete
inverse/forward meeting unions above, with source and extension isotropy
and H zero. Fixing one irrational anchor a, the lag k_z of an arrow
a->z is unique: two such lags would yield nonzero isotropy. The full
phase is h-k_z ell in R. Different endpoints at the same lag may still
have nonunit kernel arrows. These descriptions cover all circle points,
all inverse depths, and every real extension phase.

For A, N=2: B_1=1, with the sole fixed point 0 and primitive log2.
B_2=(4-2)/2=1 supplies an ACTUAL least-two primitive log4 packet.
All periods q>=2 have composite primitive log(2^q). Prime-only support
therefore fails; the log4 packet is not renamed a repeat of the log2
packet because their full source packets are different.

For B, N=3: B_1=2, the distinct fixed points 0 and 1/2, each with
primitive log3 and disjoint full incoming classes. This already fails
uniqueness per prime. Also B_2=(9-3)/2=3, and all q>=2 have composite
primitive log(3^q), so prime-only support fails separately. No selection
of one fixed point, inverse sheet or phase can repair the full ledger.

## 5. Digit words and actual endpoints for the linear controls

For digits a_j in {0,...,N-1}, the map

    pi_N((a_j)_{j>=1}) = pi(sum_{j>=1} a_j N^{-j})

satisfies F pi_N=pi_N shift. A word of length q repeated indefinitely
represents pi(A/(N^q-1)), where A is the integer with those q digits,
0<=A<=N^q-1. All N^q words occur, but A=0 and A=N^q-1 represent the
same circle endpoint. All other displayed values are different modulo
one. This is exactly the difference between N^q fixed digit sequences
and N^q-1 actual fixed circle points.

No other purely periodic expansion can coincide with a different one:
the reduced denominator of a nonzero purely periodic value is coprime
to N, whereas a finite base-N expansion has denominator a power of N.
The usual two-expansion ambiguity occurs when a finite expansion ends
in zeros and the alternative decreases its last nonzero digit and ends
in digits N-1. These values belong to the eventual basin of the actual
endpoint, and are retained by the actual inverse formulas. At the circle
endpoint the two constant sequences all-zero and all-(N-1) are identified.

Except for these two least-one sequences, least symbolic period agrees
with least circle period. Thus for q>1 primitive digit necklaces and
actual least-q cycles have the same count; for q=1, N constant words
give N-1 actual fixed packets. Cyclic rotations represent core phases,
not different full packets. This explicit quotient is a comparator
calculation, not a license to replace the circle's measure or clock by
a selected symbolic model or to claim prime-symbolic admissibility.

## 6. Nonlinear control C: own clock and the entire fixed basin

Now f(x)=2x+sin(2 pi x)/(4 pi). It obeys f(x+1)=f(x)+2 and

    f'(x)=2+(1/2)cos(2 pi x) in [3/2,5/2].

It satisfies the conditional hypotheses on the WHOLE circle. Its global
inverse g is the unique real solution of the displayed strictly increasing
equation. All actual predecessors are pi(g(y)) and pi(g(y+1)), with
their all-point inverse germs and IMAGE factors

    J_j(pi(y))=1/[2+(1/2)cos(2 pi g(y+j))].

The chart/endpoint arguments of Section1 apply without dropping any
point. Its own clock is kappa(pi(x))=log[2+(1/2)cos(2 pi x)], not log2.
All source fixed counts, least-period counts and packet counts from
Section2 hold with N=2 because the hypotheses were just checked.
This does not evaluate higher-period derivative products.

The fixed displacement is

    h_1(x)=x+sin(2 pi x)/(4 pi),
    h_1'(x)=1+(1/2)cos(2 pi x)>=1/2.

It maps [0,1) strictly increasingly onto [0,1), so its only integer
value there is h_1(0)=0. Thus 0 is the UNIQUE global fixed point.
Its full signed clock is C_0=log(5/2)>0. Source isotropy is Z,
the ENTIRE H is C_0 Z, extension isotropy is zero, and its primitive
physical length is log(5/2), not log2. It is not the logarithm of an
ordinary prime, since 5/2 is not an integer.

The entire fixed-core basin is exactly

    B_0=union_{m>=0}{pi(f_m^{-1}(j)):0<=j<2^m}.

Here f_m(0)=0 and f_m(1)=2^m, so all representatives are in [0,1).
The depth-m set has 2^m points and contains every earlier depth;
the first-arrival layer of depth m>=1 has 2^{m-1} points. In particular
the full basin is not the singleton fixed point. There is no prescribed
finite depth cutoff or selection of one incoming branch.

For every z in B_0 let d_z be its first arrival and set

    beta_z=S_{d_z}(z)-d_z C_0,
    S_{d_z}(z)=sum_{j=0}^{d_z-1}log[2+(1/2)cos(2 pi F^j z)].

Between every pair z,w in B_0 there is an actual arrow for EVERY integer
k, with c=k C_0+beta_z-beta_w. Thus the full lag kernel comprises all
k=0 pairs; the full clock kernel is the exact equation
k C_0=beta_w-beta_z; and the joint kernel has k=0 and equal beta values.
Source isotropy is Z, H=C_0 Z and extension isotropy zero at every
incoming point. All real phases are

    h-S_{d_z}(z) modulo C_0 Z.

These formulas retain possible nonunit zero-clock arrows and do not
replace the basin by its core. All positive physical repetitions are
the positive integer multiples of C_0.

Outside this fixed basin, Section1's two-sheet inverse formulas and
Section3's full meeting unions, derivative-product kernel tests and
general phase formulas continue to describe EVERY actual history.
Other eventual cores have the exact source counts already proved, and
their H is their own derivative-product clock times Z. No higher-period
clock value or prime-purity census for C is claimed. Non-eventual classes
have H and source isotropy zero with the full real anchor phase. No point
or phase outside B_0 is discarded by limiting the explicit clock audit
to the frozen fixed-core obligation.

The single actual fixed primitive already defeats prime-only support
for C. A and C have the same degree and ALL the same source-period
counts, yet their fixed clocks differ and only A's fixed clock is prime.
Thus degree and periodic word count alone do not decide prime clocks.
This conclusion does not require a higher-period clock computation for C.

## 7. Scope, ownership and immutable raw handoff

The conditional source-period packet budget is exact for every q.
It counts full packets because every actual finite cycle has its own
unrestricted incoming class and different cycles cannot coalesce. It does
not assign prime labels to the derivative-clock products, prove arithmetic
admission, or give a universal impossibility theorem for expanding covers.
The three controls retain their own full measures, every inverse, kernel
and phase conventions. Their failures are scoped negative controls, not
an accumulated positive arithmetic result.

The lineage under test is the proposed full-cover geometric realization
of symbolic admissibility; the complete digit shift is only a comparator.
No prime-symbolic pruning mechanism was invented. Classical NOT APPLICABLE;
arithmetic T1 NOT PASSED; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.
No operator, trace, zeta, Riemann zeros, per-prime parameter, scientific
numerical census, Git mutation, PDF, publication or old-file edit occurred.

Only this raw evidence file was written. Stop after its freeze and notify
root with receipt only, without mathematical results. A DISTINCT PAPER
UNLOCK is required before reading the four author surfaces. This raw
derivation remains immutable after manuscript exposure; any later correction
must be explicitly recorded rather than silently rewriting these bytes.
