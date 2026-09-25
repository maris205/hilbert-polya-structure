# Reversal pairs nonzero density-clock packets

Candidate: ANG-AUDIT-20260923-RCP01. Paper414; session date2026-09-23.
Outcome: REVERSIBLE NONZERO CYCLE CLOCKS OCCUR IN DISTINCT EQUAL-PERIOD PAIRS — CONDITIONAL AUDIT / FORK
Status: exact conditional theorem and complete external controls, not a new
prime-lineage candidate. Classical NOT APPLICABLE; T3 NOT AUDITED;
formal Route UNASSIGNED; Route B NOT INVOKED.

## Abstract and boundary

A globally invertible smooth map F, reversed by a smooth involution R on the
same complete measured manifold, has opposite signed density-clock sums on
reversed periodic cycles. A self-reversed cycle therefore has zero sum.
Every nonzero sum belongs to two DISTINCT complete source packets having the
same least positive physical period. Thus this reversible class cannot meet
the simultaneous nonempty, ordinary-prime-only and unique-per-prime benchmark.
The conclusion concerns the prescribed full density clock, not an unstable
direction exponent or a manually chosen roof. It is not a no-go theorem for
partial, noninvertible, nonreversible, or differently clocked objects.

The [frozen card](candidate-card.md) supplies the exact class and three full
external controls. A plane stretch has zero AREA clock; the projective line
has two distinct log2 packets, one expanding and one contracting; a half-turn
circle retains a continuum of zero-clock period-two cores. All points,
inverse histories, integer lags and real heights remain throughout.

## 1. Same-object ledger and question

M is a second-countable smooth manifold without boundary, mu a fixed smooth
positive density. F and R are global C1 diffeomorphisms with R²=id and
RFR=F inverse. Let j_F,j_R be positive density Jacobians at EVERY point,
kappa=log j_F and rho=log j_R. There are no terminal points in this class.
The actual inverse has prescribed J(w)=1/j_F(F inverse w). In local charts,
the change-of-variables formula, with the fixed density on both sides, gives
mu(F inverse E)=integral_E J dmu for every Borel E; a countable chart
partition extends this to all E. Positivity and finiteness follow from the
invertible differential and positive density. This is the frozen differential
version, not a choice from an almost-everywhere equivalence class.

No prime source, positive roof, symplectic structure, Hamiltonian lift or
operator is supplied. The lineage use is a conditional test of a proposed
reversible realization of an ALREADY specified prime-symbolic source;
see the [prior-work interface](../../docs/prior_work/README.md). Generic
geometric controls below are EXTERNAL CONTROLS, never admitted candidates.

Necessary target: at least one positive packet, every least positive period
log p for an ordinary integer prime p, and at most one actual packet per p.
Coverage of all primes is an additional, stronger target. No target data are
used in the maps or clock. The theorem tests only the stated necessary target.

## 2. Complete invertible ledger

For k>=0 let S_k(z)=sum_{j=0}^{k-1} kappa(F^j z); S_0=0. For k<0 set
S_k(z)=-S_{-k}(F^k z). These equal log j_{F^k}(z) for all integer k.
The chain rule gives S_{k+l}(z)=S_k(z)+S_l(F^k z).

Every actual meeting triple is uniquely written
g=(z,k,w), w=F^k z, k in Z; source w, range z, c(g)=S_k(z).
Indeed cancellation of F^n from F^m z=F^n w gives this equation, and the
same chain identity gives S_m(z)-S_n(w)=S_{m-n}(z). Composition adds lags
and clocks, units have k=0, and inverse arrows negate c. ALL integers are
retained even when several lags have the same endpoints.

The lag kernel consists of units. The clock kernel consists of exactly the
triples with S_k(z)=0; its intersection with the lag kernel is the units.
A nonperiodic point has trivial source isotropy and H={0}. A least-q cycle
has source isotropy qZ and total C=S_q(z), independent of cycle phase.
Its entire H=CZ; the extension isotropy is zero if C!=0, qZ if C=0.
Only if C!=0 is there a least positive period L=abs(C), with repeats rL.
These conclusions use ALL isotropy, not one arbitrarily chosen return.

Global invertibility implies an eventually periodic point was periodic
already: apply F inverse to any finite entrance. A periodic source packet
is exactly its q-point cycle, with no strict preperiodic incoming. Other
source packets are the complete two-sided nonperiodic orbits.

For a reference b of a nonperiodic orbit, z=F^j b has the unique j in Z.
The arrow (b,j,z) goes TO b and takes h to h+S_j(b); this is the complete
height coordinate on the packet, a free real line. For a q-cycle reference
b use the same expression modulo CZ, with j any index of z. Changing j
by q changes it by C, so it is well-defined. When C=0 it is a real line,
retaining qZ ineffective isotropy; when C!=0 it is R/CZ, circumference |C|.
Every real height and every source orbit is included, with no convergence
or attracting-basin identification.

## 3. Reversal theorem, arrow sign and height lift

Define Psi(z,k,w)=(Rz,-k,Rw). Since R F^k=F^{-k} R this is an actual
groupoid involution. Differentiate F^{-k} R=R F^k at z, where w=F^k z:

S_{-k}(Rz)+rho(z)=rho(w)+S_k(z).

Consequently c(Psi g)=c(g)+rho(w)-rho(z). In particular reversing lag does
NOT simply negate the clock. The compatible lift on all height objects is
U(z,h)=(Rz,h-rho(z)). A source (w,h) and its target (z,h+c) transform to
heights h-rho(w) and h+c-rho(z), whose difference is exactly c(Psi g).
Also rho(Rz)+rho(z)=0 follows from R²=id; hence U²=id. U commutes with
height translation. This constructs a lift; no uniqueness assertion is needed.

For a least-q cycle gamma, Rgamma is a least-q cycle: a shorter return there
would reverse to a shorter return here. Taking k=q gives
S_{-q}(Rz)=S_q(z)=C; at the periodic point Rz the left side is -S_q(Rz).
Thus its positive-iterate signed sum is -C. If Rgamma=gamma, cyclic
invariance of the same sum gives C=-C, hence C=0. Equivalently R acts on
the q phases by j -> a-j modulo q for some a, not generally by a rotation.

If C!=0 the cycles gamma,Rgamma are distinct. They cannot lie in one source
packet: two distinct cycles of an invertible deterministic map never have
an actual meeting. Each has entire H=CZ=(-C)Z and least period |C|.
Neither a negative signed sum nor time-reversal identification deletes one
packet. U pairs packets but does not quotient by that pairing.

**Conditional obstruction.** If there is no nonzero-clock cycle, positive
nonemptiness fails. Otherwise select any one: if |C| is not log an ordinary
prime, support fails; if it is log p, the distinct reversed cycle supplies
a second packet at log p, so uniqueness fails. Thus every full owner in
this reversible class fails the joint necessary benchmark. This does not
assert existence of a cycle, nor arithmetic relevance of an arbitrary F.

## 4. Control A — full plane, volume rather than a chosen direction

M=R2, mu=dx dy, F(x,y)=(2x,y/2), R(x,y)=(y,x). Both are global and
RFR(x,y)=(x/2,2y)=F inverse(x,y). Own inverse (u/2,2v) has determinant1,
so its IMAGE J=1, kappa=0 at every point; rho=0 also. An expanding coordinate
with factor2 does not supply a log2 clock for the full area owner.

F^k(x,y)=(2^k x,2^{-k} y). The only periodic point is (0,0), least period1:
for k!=0 both fixed coordinate equations force zero. It has source and
extension isotropy Z, H=0, and a free real height line. No other point enters
it under the unique inverse. Every nonzero point is aperiodic, full source
orbit { (2^k x,2^{-k}y):k in Z }, isotropy zero and H=0. Clock kernel is
the entire groupoid, lag/intersection kernels units. Every packet has height
coordinate h since all S_k vanish. These formulas describe every point and
both unbounded directions, without an asymptotic-basin quotient.

## 5. Control B — both projective ends retained

M=RP1, theta modulo pi, mu=dtheta. In t=tan(theta), F(t)=2t and R(t)=1/t,
with both 0 and infinity retained and exchanged by R. In the second chart
u=1/t, F is u/2, so both maps are global smooth diffeomorphisms. R is the
round-length reflection theta -> pi/2-theta, rho=0, and RFR=F inverse.

In a finite t chart mu=dt/(1+t²); the own formulas are

j_F(t)=2(1+t²)/(1+4t²),
J(w)=2(1+w²)/(4+w²),
kappa(t)=log2+log(1+t²)-log(1+4t²).

At infinity the second chart gives j_F=1/2 and J=2. These are the smooth
all-point versions, and change of variables on both charts proves every-Borel
IMAGE. In particular kappa(0)=log2 and kappa(infinity)=-log2.

The complete periodic set is {0,infinity}, each fixed: for finite nonzero t,
2^k t=t is impossible at k>0. Each fixed point is its own entire source
packet, source isotropy Z, H=(log2)Z, extension isotropy zero and height
phase h modulo log2. Their repetitions are r log2 but they remain TWO
packets. All other points have no eventual entrance into either end.

For finite nonzero t and integer k,
S_k(t)=k log2+log(1+t²)-log(1+2^{2k}t²).
Their source orbit is {2^k t:k in Z}, H=0 and trivial source/extension
isotropy. Choose its unique reference b=s u, s=sign(t), 1<=u<2, t=2^j b.
The complete real phase is h+j log2+log(1+u²)-log(1+t²), by the arrow TO b.
These coordinates describe all nonperiodic packets, not merely their ends.

The lag kernel and intersection are units. Clock kernel includes units and,
for k!=0, precisely arrows (t,k,2^k t) with t=+/-2^{-k/2}; neither projective
end contributes a nonzero-lag clock-kernel arrow. Indeed setting a=2^k gives
a(1+t²)=1+a²t², or (a-1)(1-a t²)=0. Such zero-clock arrows between distinct
aperiodic points do NOT create nontrivial isotropy or positive H.

Thus the control fails UNIQUENESS, not prime support at its fixed cores.
Deleting the contracting end, identifying R-related points, or assigning
both ends one orbit would change the frozen owner.

## 6. Control C — zero clock with all period-two cores

M=R/(2pi Z), mu=length, F(theta)=theta+pi, R(theta)=-theta.
RFR=F inverse=F. The actual inverse is the same half-turn, with J=1,
kappa=rho=0 everywhere and every-Borel IMAGE from rotation invariance.
Every point has least period2, no fixed point, and source packet
{theta,theta+pi}. Incoming is exactly this same pair. Every source and
extension isotropy is 2Z, entire H=0; every packet is a free real height
line. Distinct unordered pairs give a continuum of packets, none positive.

All triples satisfy w=theta+k pi mod2pi, c=0. Clock kernel is all G,
lag/intersection kernels units. The reversal fixes precisely the two source
packets {0,pi} and {pi/2,3pi/2} and pairs the others: self-reversal requires
2theta=0 modulo pi. All signed sums remain zero, consistently with either case.

## 7. Gates, limitations and decision

T0: the conditional class and each control own their full inverse, density,
pointwise clock and actual groupoid. T1: no endogenous prime-symbolic source
is asserted; the prior-work arrow is a conditional application interface.
T2: the joint target is excluded for this reversible class under its stated
clock, while each control has a complete periodic and source/height ledger.
T3 NOT AUDITED; classical candidate fields NOT APPLICABLE; formal Route
UNASSIGNED; B NOT INVOKED. The theorem is not a Route verdict or RH claim.

Arithmetic shuffled labels are inapplicable without an arithmetic source.
The three full controls test volume ownership, paired positive packets and
zero-clock ineffective isotropy. No numerical cutoff/precision is used;
the exact formulas cover both charts, all points and all integer lags.
PROVES_TOO_MUCH is restricted by global reversibility and the full density
clock. Dropping either hypothesis is outside the theorem, not an evasion to
be ruled out here. Strong naturalness and an admitted arithmetic source remain
unestablished. No literature priority or global novelty claim is made.

Portfolio: CONDITIONAL AUDIT / FORK. Use this filter before proposing a
reversible completion with its full density clock; do not quotient paired
cores or substitute a one-direction exponent to rescue it. A new owner needs
a new card. No round415 is authorized by this batch.

## Evidence and AI assistance

Exact inputs are [card](candidate-card.md); claim map [ledger](claim-ledger.md),
navigation [README](README.md), [scope review](evidence/scope-review.md),
[frozen independent raw](evidence/independent-review-raw.md) and
[final comparison](evidence/independent-review.md). Proof method is symbolic
chain rule, integer-iterate equations and explicit coordinate changes above;
no scientific numerical program, external literature search, fitting or
target data were used. Mechanical commands/limits are recorded in the
[batch log](../410-euclidean-complex-feedback/batch-log.md).

AI assistance was used for definition design, exact derivation, manuscript
drafting and separate staged internal review. Root is the author; the reviewer
receives the frozen card before any manuscript unlock. Informal design
expectations and shared prior history are disclosed, not blind preregistration.
Same-model internal review is NOT_CALIBRATED, not human/external peer review;
artifact validation is not a proof certificate. Any recorded review correction
remains visible in its own evidence report.
