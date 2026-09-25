# Continuous symmetries, density clocks and full packet multiplicity

Paper429; candidate ANG-AUDIT-20260923-CSM01;2026-09-23.
Outcome: CONTINUOUS-SYMMETRY MULTIPLICITY FILTER ESTABLISHED; FIXED-LOCUS EXCEPTION RETAINED — CONDITIONAL FILTER / FORK

## Abstract and exact owner

A continuous real-parameter symmetry of a full diffeomorphism need not
preserve the density clock on every arrow. Its geometric density correction
does, however, preserve entire isotropy clocks and signed cycle sums. Every
positive periodic core moved by the symmetry belongs to a continuum of
distinct equal-primitive packets. Hence a unique-prime-packet ledger would
have to place every positive core in the symmetry's pointwise fixed locus.
This is a conditional filter, not a universal no-go. Three complete planar
controls retain that exception and a noninvariant all-arrow clock kernel.

The frozen [card](candidate-card.md) fixes a full second-countable smooth M,
positive smooth density mu, global C1 diffeomorphism F and real action alpha_t
by C1 diffeomorphisms commuting with F. Both alpha and its spatial derivative
are jointly continuous; no differentiability in t is needed. No point or
stratum is removed, no quotient by alpha is made and no mu invariance assumed.
The carrier is broadened ANG, not a classical symplectic suspension. Its own
Jacobian, actual inverse, clock, groupoid and height extension are kept together.
No arithmetic candidate, prime source, operator, determinant or trace is supplied.

## 1. All-point inverse IMAGE and actual groupoid

Write j_F(x)>0 for the differential density Jacobian, and j_t(x)>0 for
alpha_t. These are prescribed continuous values at EVERY point. The sole
inverse branch satisfies J(y)=1/j_F(F^-1 y), and change of variables gives
mu(F^-1 E)=integral_E J dmu for every Borel E, allowing infinite integrals.
The smooth positive density is sigma-finite by a countable relatively compact
chart cover. There is no arbitrary modification at a null periodic point.
Set kappa=log j_F and rho_t=log j_t. All are finite; kappa may be signed/zero.

For k in Z extend S_k by S_0=0 and S_(-k)(x)=-S_k(F^-k x), k>0.
The chain rule gives S_(k+l)(x)=S_k(x)+S_l(F^k x) for all integers.
Because F is bijective the complete retained-lag groupoid is

    G={(z,k,F^k z): z in M,k in Z},   c(z,k,F^k z)=S_k(z).

Indeed F^m z=F^n w implies w=F^(m-n)z, and the chain rule reduces the
witness difference to S_(m-n)(z). Thus all presentations agree and c adds
on composition. Source is w=F^k z, range z. Forward (Fz,-1,z) has clock
-kappa(z). Differential chain rules also give the corresponding Borel
branch-pair IMAGE law. All arrow sets are countable unions of Borel graphs.
The extension retains ALL M x R: (w,h)->(z,h+c); height translation
commutes with every arrow. Only a set-level orbit space is asserted.

The lag kernel and its intersection with the clock kernel are the units.
The entire clock kernel consists precisely of these actual arrows with
S_k(z)=0; it need not contain only units. Source orbits are whole F^Z orbits.
If a core has least source period q and signed sum C=S_q(b), its source
isotropy is qZ, entire H=CZ; extension isotropy is0 if C!=0 and qZ if C=0.
Only C!=0 gives primitive L=abs(C), with repeats kL,k>=1. An aperiodic
source orbit has source/extension isotropy0 and H=0. A bijection has no
extra preperiodic tails entering a finite core: F^-1 permutes that core.

For a reference b in any ONE orbit, z=F^n b has phase

    h+S_n(b) modulo H.

Changing n by a source period adds a multiple of C, so this is well-defined.
For H0 it is a full real line; otherwise every point of R/LZ is retained.
No global measurable choice of b is needed or claimed. Source packets are
never identified merely because their L values agree.

## 2. Symmetry transport, including the nonpreserving density

Differentiate alpha_t F=F alpha_t using the fixed density:

    j_F(alpha_t x) j_t(x)=j_t(Fx) j_F(x).
    kappa(alpha_t x)=kappa(x)+rho_t(Fx)-rho_t(x).

Telescoping holds for all integer k. Therefore the actual arrow automorphism

    Phi_t(z,k,w)=(alpha_t z,k,alpha_t w)

satisfies c(Phi_t g)=c(g)+rho_t(w)-rho_t(z). In particular integer lag is
unchanged, but the whole clock kernel is NOT generally invariant. Its
transported arrows have clock0 precisely when c(g)=rho_t(z)-rho_t(w).
For isotropy z=w the correction cancels, preserving entire H and zero-clock
isotropy, not just one chosen loop. The full height lift is

    (x,h) -> (alpha_t x,h-rho_t(x)).

An extension arrow maps to an extension arrow by the displayed correction.
The density chain rule rho_(s+t)(x)=rho_s(alpha_t x)+rho_t(x) proves these
lifts form a real action. Joint continuity of the spatial derivatives suffices
for continuity of rho and the lift; no generating vector field is assumed.
This lift commutes with physical height translation, not rescales time.
All incoming/orbit arrows and every phase transport bijectively. Relative to
the moved reference alpha_t b, the phase changes only by -rho_t(b).

Commutation preserves least source period q, and telescoping around the
cycle gives S_q(alpha_t b)=C. Thus its signed sum, entire H, primitive,
repetition law and source/extension isotropy remain the same.

## 3. Connected-symmetry multiplicity theorem and its exception

For a finite periodic core O set K_O={t:alpha_t O=O}. It is a subgroup.
It is closed: if t_n in K_O converge to t, continuity puts alpha_t x in the
closed finite O for every x in O; injectivity implies alpha_t O=O.
A closed subgroup of R is R,{0},or aZ for a>0. For completeness: if its
positive elements have infimum0, integer multiples approximate every real
number and closedness gives R. Otherwise that infimum is a positive attained
minimum a, and division with remainder proves the group is aZ; if there are
no positive elements the subgroup is0.

If K_O=R, each continuous curve t->alpha_t x takes values in the finite
set O and hence is constant. Thus EVERY point of O is fixed by EVERY alpha_t.
Conversely pointwise fixation gives K_O=R. In every other case R/K_O has
continuum cardinality (use any short interval if K_O=aZ). Its cosets label
exactly the different cycles alpha_t O. Different periodic cores cannot be
the same source orbit of a bijection, so these are distinct full packets.
The preceding clock identity assigns the SAME signed C and entire H to all.

Consequently, if C!=0 and O is not pointwise fixed by the action, there are
continuum many equal-positive-primitive packets. A nonempty prime-only ledger
with at most one packet per prime can therefore contain positive cores ONLY
inside Fix(alpha)={x:alpha_t x=x for all t}. This is necessary, not sufficient:
wrong times, duplicates within that locus and missing primes remain possible.
If Fix(alpha) is empty, either no positive core exists (empty ledger) or a
positive core forces duplicate packets. No existence theorem is assumed.
For C=0 the same source multiplicity statement gives H0, not positive periods.
Discrete, partial/noninvertible and noncommuting actions are outside this proof.

## 4. Complete external controls

### A — a whole translation family of log2 fixed packets

Full R2, Lebesgue area, F(x,y)=(2x,y), alpha_t(x,y)=(x,y+t).
F^-1(x,y)=(x/2,y), inverse IMAGE1/2, kappa=log2, rho_t=0.
For every integer k, F^k(x,y)=(2^k x,y), c=k log2. All kernels are units.
All periodic cores are the fixed points (0,y), y in R: each full basin is
that singleton, source isotropy Z, extension isotropy0, entire H=(log2)Z,
all circle phases h mod log2, integer repetitions. They are distinct packets,
not one axis packet. Translation moves them transitively, K_O=0.
For x!=0 the entire orbit is {(2^n x,y):n in Z}, with isotropy0,H0 and free
phase h+log abs(x). No other points or incoming remain to enumerate.
Every-Borel IMAGE is the linear change of variables, on the full plane.

### B — the pointwise-fixed exception cannot be discarded

Full R2, Lebesgue area, F(x,y)=(2x,3y/2), alpha_t=e^t times(x,y).
Inverse(x/2,2y/3) owns IMAGE1/3; kappa=log3. Symmetry j_t=e^(2t),
rho_t=2t, so its height lift subtracts2t. The sole periodic core is the
origin: every other point has a nonzero coordinate multiplied by a factor
greater than1 under each positive iterate, precluding any period.
Origin is pointwise fixed by alpha, K_O=R, source isotropyZ, extension0,
entireH=(log3)Z and all phases h mod log3. Its full basin is the singleton.
This is ONE primitive log3 packet, not a continuum. All other orbits are
{(2^n x,(3/2)^n y):n in Z}, aperiodic, H0, isotropy0. Their reference phase
is h+n log3 at F^n b. All kernels are units since c=k log3.
Although the origin core is fixed, its phase changes by -2t under the symmetry;
the symmetry stabilizer of a phase is((log3)/2)Z, not the whole R. This does
not add a source packet or change its physical translation stabilizer(log3)Z.
This full control meets the necessary nonempty/prime/unique conditions;
it misses every prime other than3 and supplies no arithmetic source.

### C — changed density, same return groups, different arrow kernel

Full R2, mu=e^(xy) dxdy, F(x,y)=(2x,y), alpha_t(x,y)=(x,y+t).
Inverse IMAGE J(u,v)=(1/2) exp(-uv/2), hence

    kappa(x,y)=log2+xy; rho_t(x,y)=tx;
    S_k(x,y)=k log2+(2^k-1)xy, all k in Z.

These are all-point smooth differential values, and the weighted change of
variables proves every-Borel IMAGE; local finiteness gives sigma-finiteness.
The complete source orbits and periodic cores equal A's, as actual maps do.
Each fixed (0,y) still has entireH=(log2)Z, sourceZ/extension0, allcirclephases;
all x!=0 orbits have source/extension0,H0, free phase h+log abs(x)+xy.
The full clock kernel is exactly the arrows with
k log2+(2^k-1)xy=0; lag/joint kernels remain units. This includes nonunits:
at z=(1,-log2), k=1, w=Fz, the clock is0. Its alpha_t-image clock equals
t, so for t!=0 it leaves the kernel. No failure of isotropy-clock transport
is involved, because this arrow is not isotropy. The lift subtracts tx and
preserves the displayed free phase. No density from A is silently reused.

## 5. Scope, adverse controls and decision

This filter addresses the prime-symbolic -> geometric realization arrow only
when a separately specified realization has a continuous commuting action.
It is not itself an endogenous arithmetic mechanism. A/C show that a full
continuous fixed family cannot be reduced to a chosen centre; B prevents an
overbroad symmetry no-go. C distinguishes invariant cycle clocks from the
noninvariant whole clock kernel. Arithmetic shuffled labels are inapplicable
without a source; no arbitrary-data encoding or PROVES_TOO_MUCH universal
claim is made. Exact whole-owner identities replace numerical cutoffs.

T0/clock transport and conditional T2 multiplicity are established in the
frozen class. Arithmetic T1 NOT PASSED; strong naturalness NOT ESTABLISHED;
T3 NOT AUDITED; classical NOT APPLICABLE; formal Route UNASSIGNED;
Route B NOT INVOKED. Portfolio CONDITIONAL FILTER / FORK. No continuous
quotient, new candidate admission or rescue of any stopped object follows.
The next use is only to test a newly frozen same-owner realization's actual
symmetry and fixed locus; absence of that hypothesis gives no verdict.

All results are exact algebra/analysis, no scientific numerical or literature
run, new operator, prime/zero table, external roof, Git/PDF/publication action.
The elementary subgroup and density identities are proved here, not priority
claims. Root used AI for design, derivation and drafting; a separate same-model
shared-history AI reviewer supplies scope/raw/final checks, NOT_CALIBRATED,
not blind, external peer, cross-model or human verification. Root drafted this
paper before reading that raw derivation. No author helper was used.

[Claims](claim-ledger.md) · [Overview](README.md) · [Scope](evidence/scope-review.md)
· [Independent raw](evidence/independent-derivation.md)
· [Final internal review](evidence/independent-review.md)
· [Batch record](../425-divisor-remainder-companion/batch-log.md).
