# Local isolation of positive periodic packets

Candidate: ANG-AUDIT-20260923-LPI01. Paper439; session2026-09-23.
Outcome: LOCAL POSITIVE-PERIOD ISOLATION FILTER ESTABLISHED; NO ARITHMETIC ADMISSION

## Abstract and scope

For the frozen partial deterministic germ/density owner, continuity of an
actual q-return and its accumulated clock gives a local necessary condition
for ordinary-prime support with unique packets: every nonzero-clock q-fixed
point must be isolated among q-fixed points in that regular window. Compact
nonzero-clock return sets are finite. No commuting action, manifold structure
of the return set or injective family parameter is required. Three full-plane
controls separate varying positive families, zero-clock families and an
isolated nonhyperbolic positive core. This is a conditional screening theorem,
not arithmetic admission, a periodic-existence result or universal failure.

## 1. Same owner, inverse IMAGE and actual histories

Use exactly the [card](candidate-card.md): full manifold X, fixed positive
continuous density mu, deterministic T on its Borel legal domain and a
countable partition with assigned local C1 diffeomorphism germs f_i.
In density coordinates mu=rho(x)dx the own inverse at y=f_i(x) has
J_i(y)=rho(x)/(rho(y)|det Df_i(x)|). Thus
kappa(x)=log|det Df_i(x)|+log rho(Tx)-log rho(x).
This is finite and pointwise, including an owned null/face point. Local
change of variables gives mu(theta(E))=integral_E J_i dmu for EVERY Borel E
in an inverse patch. Countably refine patches, using disjoint restrictions,
to obtain the same law on a whole actual inverse domain. All actual inverse
points are retained; no assembled-map injectivity or smoothness is inferred.
Terminals have no kappa step, but have units and all actual incoming.

Let S_m(z) be its own legal clock sum. For a meeting arrow
g=(z,m-n,w), T^m z=T^n w, set c(g)=S_m(z)-S_n(w).
Two representatives with the same lag have indices shifted by the same
integer; their extra common-tail sums cancel. Composition is obtained by
extending the earlier of the two meetings to the later legal meeting along
the shared middle history; the sums telescope. Hence c is well defined and
additive, without extending a terminal illegally. Source is w, range z;
the forward arrow(Tz,-1,z) has clock -kappa(z).
The three full kernels are respectively actual arrows satisfying
m=n; S_m(z)=S_n(w); and BOTH. These are exact unrestricted conditions,
not assertions that a noninvertible owner's zero-lag kernel consists of units.
The full height extension sends(w,h) to(z,h+c(g)). Physical time translates
h on its orbit SET; neither a nice quotient nor a global Borel selector is used.

Every source orbit either eventually meets a least-d cycle or does not.
Indeed nonzero loop lag gives equality of two unequal legal iterates and
therefore an actual eventual cycle; the converse provides all multiples of d.
For a least-d core with signed sum C, source isotropy=dZ and its ENTIRE
clock image H=CZ, for ALL incoming ancestors, not merely core points.
Extension isotropy is0 if C!=0, and dZ if C=0. If no eventual cycle,
source/extension isotropy and H are0, even when different histories merge.
Thus only |C| is a positive primitive; repetitions are r|C|,r>=1.
Choose a base a for a single source orbit and any arrow g_z:a->z with
b_z=c(g_z). The complete phase is h-b_z modulo H_a. Different choices
change it by H_a. This describes every real height and all incoming; H0
gives a free real phase. No equal-clock identification of different source
orbits is allowed. The inverse recursion takes EVERY actual inverse at each
finite depth, not a depth or branch cutoff.

## 2. The local isolation theorem

Fix q>=1 and the card's open regular q-window U: q legal iterates on U,
T^q and S_q continuous there. Write Z={x in U:T^q x=x}.
A fixed-itinerary open neighborhood of continuous germs is sufficient,
because all partial compositions and kappa are continuous there. Piecewise
smoothness across a jumping itinerary boundary is NOT sufficient by itself.

Assume the full owner satisfies the necessary prime-packet benchmark.
For x in Z let d(x)|q be its least source period. Then
S_q(x)=(q/d(x))C(x). At nonzero-clock x the benchmark implies
S_q(x) belongs A_q={epsilon(q/d)log p:d|q,epsilon=+1 or -1,p prime}.
A_q has only finitely many values in every bounded real interval: finitely
many d and signs, and an upper bound on log p bounds the integer p.
It excludes0 and is locally discrete. We use this elementary bound, not a
prime table, external prime roof or hypothesis about prime distribution.

Theorem. If x in Z has S_q(x)!=0, x is isolated in Z.
Proof. Continuity gives a neighborhood on which S_q is nonzero and near
S_q(x). Choose the clock interval small enough that its intersection with
A_q is just S_q(x). For z in Z there, S_q(z)=S_q(x). If their primitives
are log p and log r with least periods d and e, the equality in absolute
value gives e log p=d log r, hence p^e=r^d. Unique prime factorization
implies p=r and then e=d. By unique-packet hypothesis their core is the
SAME finite source cycle. Distinct cycles cannot merge under deterministic
forward evolution, and a periodic point in its eventual basin is on that
core. Shrink the neighborhood to exclude the other finitely many core
points. Only x remains. This proves isolation, not hyperbolicity.

Corollary. Every compact K subset Z on which S_q never vanishes is finite.
Each point has an isolating open neighborhood as above; these neighborhoods
cover K, and a finite subcover consists of singletons in K. No uniform
isolation radius on all X or over unbounded q has been proved.

Corollary. A continuous nonconstant map gamma:I->Z from an interval, with
S_q(gamma(t))!=0 everywhere, contradicts the benchmark. Its image is connected
but lies in a discrete subspace by the theorem, hence must be a singleton.
No injectivity of gamma or ambient continuous group action is assumed.
This conclusion is local to the regular window and nonzero-clock family;
it is not a theorem about zero-clock strata or discontinuous branch faces.
Failure means at least support or uniqueness fails, not that either specified
failure individually follows without more information. Nonemptiness is a
separate benchmark clause and does not enter the local implication.

## 3. Complete control A: varying fixed-family clock

A is full R2,Lebesgue,T(x,y)=(a(y)x,y), a(y)=2+y^2.
Inverse(X,Y)=(X/a(Y),Y), full determinant J=1/a(Y); the off-diagonal
derivative does not change this triangular determinant. The inverse is
smooth globally, so all-point and every-Borel IMAGE hold. kappa=log a(y).
All signed iterates T^k(x,y)=(a(y)^k x,y), k in Z, are actual. Consequently
G consists exactly of(z,k,T^k z) and c=k log a(y). Lag, clock and joint
kernels are units. Every x=0 is fixed, and no x!=0 is periodic or eventually
periodic; bijectivity prevents outside incoming into a fixed core.
At(0,y), source isotropy=Z,H=log a(y)Z,extension isotropy0, phase
h mod log a(y); each different y is a different complete packet.
For x!=0, source/extension isotropy and H are0. Its whole orbit consists
of the displayed signed iterates, with invariant phase h+log|x|. A full set
of source-orbit labels is(y,sign x,u),1<=u<a(y), where |x|=a(y)^n u.
Every inverse is unique, so these exhaust all incoming and all states.
The fixed line is a nonconstant positive family. Its y=0 primitive is log2;
y=+1,-1 give TWO distinct log3 packets, and y=+sqrt2,-sqrt2 give log4.
Both support and uniqueness therefore fail on this same full owner.

## 4. Complete control B: zero-clock family boundary

B is full R2,Lebesgue,T(x,y)=(x,y+x^2), inverse(X,Y)=(X,Y-X^2).
The full inverse determinant is1, so IMAGE holds globally, kappa=0,c=0.
T^k(x,y)=(x,y+kx^2) for all signed k. Hence G=(z,k,T^k z), its lag
and joint kernels are units and its clock kernel is ALL G.
The line x=0 consists of fixed singleton cores; source AND extension
isotropy areZ there. For x!=0 the complete signed orbit is nonperiodic,
with both isotropies0; it is labeled by x and y mod x^2, retaining every
point and the unique full inverse chain. ENTIRE H is0 everywhere, including
the fixed line. All height phases are h itself, with free physical R motion.
Thus a nonisolated zero-clock return family does not contradict the theorem;
the full positive ledger is empty. Ineffective fixed isotropy is not deleted.

## 5. Complete control C: isolated is not nondegenerate

C is full R2,Lebesgue,T(x,y)=(2x,f(y)), f(y)=y+y^3.
f is a strictly increasing smooth bijection with derivative1+3y^2>0.
Its inverse psi is the unique real root of s+s^3=Y. The FULL inverse is
(X/2,psi(Y)), with J=1/[2(1+3psi(Y)^2)], establishing own global IMAGE.
kappa(x,y)=log2+log(1+3y^2)>=log2 at every point.
Define f^k for all integers via psi; then T^k(x,y)=(2^k x,f^k(y)).
For k in Z put S_k=k log2+log (f^k)'(y), with S_0=0. The chain rule
gives the signed sums, including negative k. Full G=(z,k,T^k z),c=S_k(z).
For k>0 S_k>=k log2; for k<0 S_k<=k log2<0. All three kernels are units.
Only(0,0) is periodic: x!=0 cannot return, and nonzero y moves strictly
away from0 forward, never changing sign. Its singleton basin has sourceZ,
H=log2 Z,extension0,phase h mod log2. Every other state has both isotropies
and H0; all incoming are its unique negative iterates, not omitted branches.

For completeness phases can be explicitly anchored. If y!=0, its signed
orbit has a UNIQUE representative a=(u,epsilon v),1<=v<2, because f(1)=2
and f^n(v) increases from0 to infinity as n runs through Z (in absolute value).
Every state in that orbit is T^n a, and phase h+S_n(a) is invariant.
If y=0,x!=0 use the unique anchor a=(epsilon u,0),1<=u<2 and the same
formula (here S_n=n log2). These choices exhaust all real phases; they do
not select a smaller carrier. The origin has derivative diag(2,1), so its
fixed point is isolated but nonhyperbolic and det(DT-I)=0. The benchmark's
necessary nonempty/prime-only/unique clauses hold with just one log2 packet;
all-prime coverage and endogenous arithmetic are absent. Isolation is not
a sufficient arithmetic criterion or a nonsingular fixed-equation test.

## 6. Decision, lineage and reproducibility

The filter tests the prime-symbolic-to-geometric realization arrow when a
full geometric return family is retained. It has no arithmetic source and
does not import429's commuting-action theorem. The complete A/B/C controls
are external boundary tests, not main candidates or sources of Route credit.
Methods were exact germ change of variables, legal-history cancellation,
cycle arithmetic, elementary local discreteness and explicit signed iterates.
Inputs are the frozen card and declared controls, with no scientific code,
cutoff, approximate precision, prime/zero tables or source campaign.
Author's definition-stage reasoning and complete389/429card outcome exposure
are disclosed in the card. This draft was written before reading the frozen
raw review. Separate same-model shared-history review is NOT_CALIBRATED,
not blind/cross-model/human/external verification.
Portfolio: retain the conditional filter and FORK search; no candidate advance.
Same-object ledgers remain intact separately. Classical NOT APPLICABLE;
arithmetic T1 NOT PASSED; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.
No440, Hamiltonian/quantum operator or publication work follows this paper.
[Claims](claim-ledger.md) · [Overview](README.md) · [CP1](evidence/scope-review.md)
· [Raw](evidence/independent-derivation.md) · [Final review](evidence/independent-review.md).
