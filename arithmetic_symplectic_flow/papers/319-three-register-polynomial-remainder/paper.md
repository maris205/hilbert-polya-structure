# Three-register polynomial remainder feedback: a composite fixed primitive

Paper ID: `319-three-register-polynomial-remainder`.
Candidate ID: `ANG-20260920-PRF01`. Date: 2026-09-20.
Status: `OWNED POLYNOMIAL CLOCK; COMPOSITE FIXED PRIMITIVE — STOP / FORK`.
Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## Abstract

On the entire signed real three-space, a current integer polynomial
quotient participates in the actual real register update. We prove complete
inverse branches, exact target-wise predecessor enumeration and the owned Lebesgue
IMAGE. Its full-point clock is log(1+3x^2), without an inserted
prime logarithm. The complete fixed locus is origin and the diagonal
cores (sqrt(n^2+1),sqrt(n^2+1),sqrt(n^2+1)), n>=1. Their
full actual finite basins retain source isotropy Z; the positive cores
have entire time group log(3n^2+4)Z and trivial extension kernel.
The preselected n=2 cell therefore supplies a genuine primitive log16,
not a repetition of another packet. This violates the prime-only target
and stops the candidate. Three controls own their separate images/clocks;
one retains the same wrong-time fixed cores, one has only origin
fixed, and the linearized control has globally zero time. All higher
source-cycle classifications remain UNCLASSIFIED. No formal Route result follows.

## 1. Identity, lineage and source freeze

| Field | This frozen owner |
| --- | --- |
| Carrier / category | X=R^3, ordinary Borel structure and Lebesgue volume |
| Source | Total current-cell polynomial quotient/remainder feedback below |
| Arithmetic input | Current floors and nonnegative integer Euclidean residue |
| Clock | Actual inverse IMAGE, including a declared analytic full-point version |
| Packet / repetition | Full retained-lag groupoid and X x R extension |
| Classical base / roof / mapping torus | NOT APPLICABLE |
| Controls | DIVISION-OFF, POLYNOMIAL-OFF, THIRD-NUMERATOR-OFF |
| Operator / trace / determinant | NOT SUPPLIED / NOT PURSUED |

The [original card](candidate-card.md), 165 lines, was frozen before
these results, SHA-256
`8f7138b4f3478df3072c6fcf87f20620fcf72c7662505ec149fec042ed461d09`.
Root read the entire [318 frontier](../318-polynomial-quotient-remainder-register/evidence/scout-record.md),
199 lines, SHA-256
`7c7dcb9609bfa92d79e56c392211369becd73a441a66a9ae2a65752133bf5e6c`.
The [source record](evidence/scout-record.md) preserves actual author access;
the [review](evidence/independent-review.md) distinguishes raw and manuscript exposure.

Write h(t)=t^3+t, A=floor(x), B=floor(y), C=floor(z),
N=h(A)+C. If B!=0, define the nonnegative residue R=N mod |B|
and q=(N-R)/B. If B=0, set q=0 and R=N, an
explicit totalization design rather than ordinary division. The full update is

    T(x,y,z)=(y,z,h(x)+z-q*y).                         (1)

It is Borel and total, since each integer cell has a fixed finite
q and every real expression exists. All negative cells, cuts, axes,
zero/unit branches and nondivisible states remain. No terminal, reset or
infinity point; every step reads new real registers. At integer states
(1) is exactly (A,B,C)->(B,C,N-qB), hence carries the
actual residue R, including the declared B=0 case.

At full cells (A,B,C)=(0,d,n), d,n>=1, N=n;
R=0 iff d|n, with proper-divisor symbols 1<d<n. The
lineage is divisor-symbolic observation -> current quotient/remainder constraint ->
quotient in actual continuous feedback -> the next arithmetic input. This
is a declared deformation, not an unrelated space decorated with primes.
Cubic interpolation, the third-register term, zero-divisor convention and volume
remain design choices. Stronger naturalness, conservative/symplectic realization and
Logistic/Henon conjugacy are not established. No prime/factor/zero table.

## 2. The exact inverse owner and full predecessor ledger

### 2.1 The real root and cell branches

Define sigma by the card's explicit real Cardano expression. If its
two cube-root terms are p,r, then p^3+r^3=a and
pr=-1/3. Thus (p+r)^3=a-(p+r), proving h(sigma(a))=a.
Since h'(x)=1+3x^2>0 and h tends to the corresponding
infinities, it is a global increasing bijection. Its inverse sigma is
smooth everywhere, with sigma'(a)=1/(1+3sigma(a)^2)>0. No
branch choice or critical-point removal is hidden in the formula.

On D_gamma=[A,A+1) x [B,B+1) x [C,C+1), q=q_gamma.
For target (u,v,w), the exact inverse and full domain are

    theta_gamma(u,v,w)=(sigma(w-v+q_gamma*u),u,v),
    E_gamma={A<=sigma(w-v+q_gamma*u)<A+1,
             B<=u<B+1, C<=v<C+1}.                  (2)

Substitution in (1) proves both inverse identities and T(D_gamma)=E_gamma.
Each branch is a restriction of a global smooth bijection; E_gamma
keeps every actual half-open boundary. Different source cells are disjoint,
so duplicate indices cannot create extra copies of one predecessor.

For ANY target set B=floor(u), C=floor(v). Enumerate every A in Z,
compute its own q_A from h(A)+C and B, and retain exactly

    h(A)<=w-v+q_A*u<h(A+1).                          (3)

Each retained A contributes the distinct point in (2); no other
predecessor is possible. This is an exact full image/predecessor criterion,
not a cutoff, numerical root list or presumption of surjectivity.

### 2.2 Multiplicity, cuts and failure of onto

The same proof will be used with epsilon=0 for the THIRD-NUMERATOR-OFF
control, replacing N by h(A)+epsilon*C and w-v by w-epsilon*v.
This paragraph's main owner has epsilon=1; each control substitution below
is explicitly its own rule. Write u=B+beta, v=C+gamma0,
with beta,gamma0 in [0,1), and set Delta_A=h(A+1)-h(A)=3A^2+3A+2.

If B=0, q_A=0 for every A; exactly one predecessor exists,
(sigma(w-epsilon*v),u,v). If B!=0 and beta>0, the inverse
test is 0<=a_A-h(A)<Delta_A, where

    a_A-h(A)=(beta/B)*h(A)+w-epsilon*v
               +(u/B)*(epsilon*C-R_A).              (4)

The last terms are uniformly bounded over A because 0<=R_A<|B|.
The nonzero cubic leading term in (4) dominates Delta_A=O(A^2)
in both tails: on one tail it is eventually negative, and on
the other it eventually exceeds Delta_A. Therefore only finitely many A
can be admitted. This is an exact finiteness proof, not a
claim that every such target has a predecessor; (3) decides that.

If B!=0 and beta=0, the test instead is

    0<=w-epsilon*gamma0-R_A<Delta_A.                  (5)

R_A depends only on A modulo m=|B|. Let r_min be the
minimum of (h(a)+epsilon*C) mod m over a=0,...,m-1.
The target is in the image iff w-epsilon*gamma0>=r_min.
Necessity follows from (5); sufficiency follows by choosing the minimizing
residue class and taking |A| large so Delta_A exceeds the fixed
nonnegative difference. Every nonempty integer-u fibre with B!=0 is
therefore countably infinite, not a finite multiplicity assumed from cell geometry.

In particular (1,0,-1) is missing from the main image, while
(1,0,0) has exactly the predecessors (A,1,0), A in Z.
Origin has the unique predecessor origin, by the B=0 formula.
All these targets remain source objects: (1) is total even when
a target has no incoming branch. No conull deletion removes these distinctions.

## 3. Own IMAGE, full-point clock and retained lags

On a main cell the forward derivative and inverse density are

    D T=[[0,1,0],[0,0,1],[1+3x^2,-q,1]],
    det D T=1+3x^2,
    J_theta(u,v,w)=1/(1+3sigma(w-v+q*u)^2).          (6)

Change of variables for the global smooth branch, restricted to its actual
domain, gives mu(theta E)=integral_E J_theta dmu for EVERY Borel
E subset E_gamma. This strictly positive finite density is the actual
three-dimensional IMAGE, not cell mass, branch count, runtime or a chosen roof.
The analytic branch formula specifies its FULL-POINT version on retained
cuts and axes. Lebesgue-a.e. data do not make those null values
unique; no atom or domain extension is asserted.

Thus at the actual source

    kappa(x,y,z)=log(1+3x^2)>=0.                    (7)

For a legal length-k history let D_k(z)=product_(0<=i<k)(1+3x_i^2),
D_0=1. Its inverse branch has IMAGE 1/D_k(z). A finite
branch pair with T^k z=T^l w, mapping w to z, has
IMAGE D_l(w)/D_k(z), including the prescribed full-point version.
Define only the actual retained-lag groupoid and clock

    G={(z,k-l,w):T^k z=T^l w, k,l>=0}, source w, range z,
    c(z,k-l,w)=log D_k(z)-log D_l(w).                (8)

It has the inherited Borel structure in X x Z x X; equal
triples are one arrow. Longer presentations of the same lag append an
identical common future, whose factors cancel. Composition aligns the two
middle histories at their longer length, yielding the cocycle law. These
are pointwise statements, not a.e. identities on a deleted subsystem.
The actual forward arrow (Tz,-1,z) has clock -kappa(z), whereas
the inverse arrow has +kappa(z). Keep ALL X x R_h, arrows
(w,h)->(z,h+c), and full translation in h. Only a Borel/set
quotient is claimed; no smooth/etale/Hausdorff or invariant-volume-times-dh claim.

For any actual eventual least-period-P cycle, source isotropy is PZ.
Let L=sum_cycle log(1+3x_i^2). Its entire H is LZ and
extension kernel is zero when L>0; if L=0, H={0} and
kernel PZ. A non-eventual state has all three groups zero.
The coordinate shift in (1) implies a cycle with L=0 has
all three registers zero, so its core is origin. This conditional
time rule does not supply or classify higher cycles.

## 4. Complete main fixed locus and decisive prime-target failure

A fixed state must have x=y=z=t. Put n=floor(t).
If n=0 then q=0 and its remaining equation is h(t)=0,
giving only t=0. If n!=0, N=n^3+2n is divisible by
n, so R=0 and q=n^2+2 under the SAME signed rule.
The fixed equation is h(t)=q*t, or

    t*(t^2-n^2-1)=0.                               (9)

Since t=0 cannot have n!=0, t=+/-sqrt(n^2+1). For n>=1,
the positive root lies strictly between n and n+1; the negative
root does not. For n<=-1, the negative root is strictly less
than n, while the positive root is outside the negative cell. Thus
the ENTIRE signed fixed locus is

    g_0=(0,0,0),
    g_n=(t_n,t_n,t_n), t_n=sqrt(n^2+1), n=1,2,... . (10)

All fixed states are diagonal as a consequence of the full equations,
not a selected carrier. The preselected three cells contain respectively
g_0, g_1 and g_2; the same short equation also closes every
other fixed cell. No higher-period census was used.

The fixed-source lag group is Z, and its clock generator is

    a_0=0; a_n=log(3n^2+4)>0 for n>=1.              (11)

Hence g_1 has primitive log7, while g_2 has primitive log16.
The latter is already a least positive return of its OWN full
packet: every loop has integer lag and clock integer*a_2. It is
not a chosen long repetition of a hypothetical log2 packet. Since
16 is composite, this positive fixed primitive violates the prime-only
target and gives STOP / FORK. The log7 fixed packet does not
erase it. No time normalization, prime sieve or state deletion is permitted.

## 5. Full fixed basins, phases and repetition ownership

For each fixed g_n define its complete basin by the exact inverse
branches, with no depth or index cutoff,

    B_n=union_(d>=0) T^(-d){g_n}.                   (12)

Equations (2)–(5), recursively applied at every target, enumerate ALL
members and retain actual overlaps as single states. Each level is
countable, so B_n is countable, but no finite basin census is
assumed. Distinct basins cannot meet, since one forward orbit cannot
eventually equal two different fixed points. Conversely two states in one
basin do share a future; its full actual-tail class is exactly B_n.

For z in B_n let d_z be the first entry depth and
S_z=sum_(0<=i<d_z)kappa(T^i z). For ANY two such states,
all retained lags ell in Z occur, and the exact clock is

    c(z,ell,w)=S_z-S_w+(ell-d_z+d_w)*a_n.            (13)

Indeed extend both entry histories along the fixed core until their
length difference is ell; the nonnegative extra lengths can realize every
integer difference. Formula (13) also proves source isotropy Z at
every basin state, ENTIRE H=a_n Z, and extension kernel0 for
n>=1. Full phase is h-S_z modulo a_n. All positive
repetitions r*a_n are of the SAME B_n packet; identical times
could not merge different basins. Origin has only itself as immediate
predecessor, hence B_0={g_0}, H0, source/extension Z and real
phase h. No extra branch words or erased incoming points alter these groups.

Thus the composite primitive is a complete-owner obstruction, not a diagonal
witness with unknown incoming identifications. Other eventual periodic packets
and all higher source cycles remain UNCLASSIFIED; they cannot remove this
already established fixed packet.

## 6. Controls, each with its OWN source and clock

### 6.1 DIVISION-OFF

T_0=(y,z,h(x)+z) has the global inverse (sigma(w-v),u,v),
without an integer-label multiplicity. It is a smooth bijection of X.
Its OWN determinant is 1+3x^2, inverse IMAGE its reciprocal and
kappa_0=log(1+3x^2), with global analytic boundary version. The finite
history/lag construction uses this source. Fixedness gives x=y=z=t and
h(t)=0, so only origin is fixed. Its unique predecessor is itself;
source/extension Z, H0, phase h. Higher source periods remain UNCLASSIFIED;
any nonzero periodic core would have L>0 by the coordinate-shift
argument, a conditional assertion only. This control supplies no main orbit.

### 6.2 POLYNOMIAL-OFF

Now N=A+C, own q,R with the same B=0 rule, and
T_lin=(y,z,x+z-q*y). Its actual branch inverse is
(w-v+q_A*u,u,v), with full domain A<=w-v+q_A*u<A+1
and B=floor(u), C=floor(v). This already enumerates every predecessor.
Its OWN forward determinant and inverse IMAGE are 1, so kappa_lin=0
globally and every retained-lag clock is zero. Source cycles are not
thereby erased: extension isotropy equals source isotropy.

For clarity its entire image/multiplicity can be resolved explicitly. If
B=0 there is exactly one inverse (w-v,u,v). If B!=0,
put m=|B|, beta=u-B, gamma0=v-C, delta=w-gamma0. Every
integer input numerator can be written A+C=B*q+R with 0<=R<m;
the exact cell test becomes

    0<=delta+q*beta-R<1.                            (14)

If beta>0, enumerate ALL integers q with 0<=delta+q*beta<m,
and set R=floor(delta+q*beta), A=B*q+R-C. They give all
distinct predecessors, finitely many and at least one because the allowed
q interval has length m/beta>1. If beta=0, a predecessor
exists iff 0<=delta<m; then R=floor(delta), every q in Z
is admitted, and the predecessors are countably infinite. This includes
all half-open endpoints and negative divisors. It is not globally onto:
(1,0,-1) is missing, whereas (1,0,0) has infinitely many predecessors.

For ALL fixed states x=y=z=t, n=floor(t). If n=0 then
q=0 and 2t=t gives t=0. If n!=0, q=2 and the
third output is 0, incompatible with nonzero-cell fixedness. Thus only
origin is fixed, with unique predecessor by B=0, full fixed basin
singleton, source/extension Z, H0 and phase h. Higher source cycles
remain UNCLASSIFIED despite the global zero time-group theorem.

### 6.3 THIRD-NUMERATOR-OFF

This source uses N=h(A), its own q,R, and
T_nc=(y,z,h(x)-q*y). Its OWN inverse is
(sigma(w+q_A*u),u,v) on its actual cell-membership domain. Formulae
(3)–(5) with epsilon=0 give its full image and exact
predecessor enumeration: B=0 unique, noninteger u outside that strip
finite, and integer u=B!=0 either absent or countably infinite by
w>=min_(a mod |B|)(h(a) mod |B|). The same missing/infinite
examples and unique origin inverse follow under THIS rule, not the main one.
Its OWN forward derivative has bottom-right entry 0 and determinant
1+3x^2, giving own inverse IMAGE and kappa_nc=log(1+3x^2).

At a fixed point x=y=z=t, n=floor(t). For n=0, q=0,
and h(t)=t implies t=0. For n!=0, h(n) is divisible
by n, so q=n^2+1. Fixedness is h(t)-q*t=t, again
t^2=n^2+1 after the impossible t=0 case. The same signed
floor comparison proves its COMPLETE fixed locus is exactly (10).
The owned clocks at these cores are exactly (11), including its
own primitive log16 at n=2. Its complete basins use its OWN
inverse branches at every depth; formula (13) holds with its own
entry depths and prefixes. Distinct fixed basins remain disjoint, full
phases and extension kernels unchanged in form, not borrowed in membership.
Higher source periods remain UNCLASSIFIED. Removing the third numerator term
does not repair the composite fixed primitive on this different owner.

## 7. Gate assessment, limits and decision

| Audit | Result for ANG-20260920-PRF01 | Limit |
| --- | --- | --- |
| T0 carrier / actual source / inverse | ESTABLISHED on entire X | Not onto or globally finite-to-one |
| T1 owned arithmetic / volume clock | ESTABLISHED within declared design | Stronger naturalness OPEN |
| T2 prime primitive target | FAILS at genuine fixed primitive log16 | Higher-cycle census not required or supplied |
| T3 trace / zeta / operator | NOT SUPPLIED / NOT PURSUED | No borrowed analytic owner |
| Classical A0/A1/A2 | NOT APPLICABLE | No symplectic base or roof asserted |
| Formal Route / Route B | UNASSIGNED / NOT INVOKED | No formal evaluation |

Portfolio STOP / FORK. The decisive reason is the complete positive
fixed packet of least log16, not lack of a prime example or
failure to classify all periods. The same-object ledger is intact: current
polynomial arithmetic, actual feedback, complete inverse histories, own volume
clock and full retained-lag packet give this result on ONE frozen owner.
The PROVES_TOO_MUCH control retains the same composite family after removal
of the third numerator term; it is not a rescue or main theorem transfer.

All proofs are exact; no scientific numerics, coefficient/cell cutoff, sampled
seeds, prime data or external literature were used. The first three cells
were preselected, and the global fixed classification was closed by the
same short equation, not inferred from those three cells. No all-period
source census, canonical arithmetic mechanism, invariant measure, smooth quotient,
RH or Hilbert--Polya construction is claimed. Internal ARS three-checkpoint
review is NOT_CALIBRATED, not external peer review or independent-error evidence.

Evidence: [card](candidate-card.md), [ledger](claim-ledger.md),
[inputs/checks](evidence/README.md), [review](evidence/independent-review.md),
[source/frontier](evidence/scout-record.md), [package](README.md).
Positive 304 and older packages unchanged; 241/242 paused; goal active.
Markdown only, no PDF/LaTeX, publication/upload, Git staging or commit.
