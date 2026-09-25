# Full factor-history transport exists, but its first packet has the wrong time

Paper380; candidate `ANG-20260922-FAH01`; 2026-09-22.
Outcome: `OWNED FULL-POINT FACTOR CLOCK; WRONG PRIMITIVE — STOP / FORK`
Exact theorem/negative target result. Classical A0/A1/A2 NOT APPLICABLE;
formal UNASSIGNED; Route B NOT INVOKED; T3 NOT AUDITED. Naturalness OPEN.

## Abstract and question

On the full parity-coprime history source, an infinite factor-allocation
mixture admits a normalized, strictly positive, everywhere specified IMAGE
derivative for every actual predecessor. This differs from375's finite
alphabet mixture and does not repair that stopped object. The law is nonatomic,
stationary and full-support. Nevertheless, the complete physical packet of
(23)^infinity has least time strictly between log2 and log3. The clock owner
exists; its fixed-normalization prime-time target fails. The proof classifies
all source and physical packets and preserves every null point and incoming
history. Three controls have their own full laws and clocks. No canonical
arithmetic origin, continuous derivative, smooth quotient or Route pass follows.

## 1. Identity, definitions and provenance

The [frozen card](candidate-card.md) owns A={2,3,...}, the full source
X={x:gcd(x_i,x_j)=1 for every odd j-i}, its left shift T, and all
I_a:E_a->X, I_a y=ay, E_a={y:gcd(a,y_(2j))=1 for every j}.
X and E_a are closed countable intersections in the discrete-product space;
they are Borel, not presumed open domains of an étale action. T(X) subset X.
Every actual inverse has this form. A finite prefix u of length m is legal
exactly when its own opposite-parity letters are coprime and
gcd(u_i,y_j)=1 whenever m+j-i is odd. These are all cross-boundary tests.
L(y)={a:y in E_a} contains all positive
powers of y_1, so it is infinite and T is onto. No carrier is trimmed.

| Field | This owner |
| --- | --- |
| Arithmetic lineage | Common-divisor witnesses -> odd-distance symbolic exclusion -> factor-allocation law |
| Probability | Fair independent irreducible colors, integrated out, as below |
| All-point version | j_a(y)=rho(a)/Z(y), Z(y)=sum_(a in L(y))rho(a) |
| Arrows | All equal-tail triples with integer lag retained |
| Physical realization | Full real-height extension and its orbit SET, not a manifold claim |
| Classical symplectic map / roof | NOT APPLICABLE; no borrowed map or roof |
| Operator / determinant | NOT CONSTRUCTED; T3 NOT AUDITED |
| Controls | Fixed allocation; arithmetic-off; explicit allocation coordinates |

Let P be the irreducibles of integer multiplication. Unique prime factorization
is used as elementary integer arithmetic, not an input table or prime-time law.
Theta={0,1}^P with fair product probability lambda; remove its two constant
points solely to define component probabilities (lambda-null). For a
nonconstant theta, S_i consists of integers whose factors all have color i;
rho(a)=1/[a(a-1)], Z_i=sum_(a in S_i)rho(a)>0. Each S_i contains infinitely
many powers of at least one factor. nu_theta is the independent law on even
sites rho/Z_0 on S_0, odd sites rho/Z_1 on S_1. Set mu=int nu_theta dlambda.
The integer labels, their divisor structure and this explicit prior are inputs.
The fair prior/rho are designed, not proved endogenous or uniquely natural.
No log-prime roof, target spectrum, per-prime weights or tuning is introduced.

## 2. Probability and support

sum_(a>=2)rho(a)=sum(1/(a-1)-1/a)=1. Membership a in S_i depends on finitely
many factor coordinates; Z_i is a pointwise limit of Borel partial sums.
All finite cylinder component probabilities are measurable. The consistent
independent finite-dimensional probabilities therefore define nu_theta and
the integrated probability mu; all components give X mass1 by cross-coprimality.
T_*nu_theta=nu_(1-theta), so complement invariance of lambda proves T_*mu=mu.

Any nonempty relative cylinder fixes finitely many letters with cross-parity
coprimality. Their factor sets on opposite parities are disjoint; prescribing
their colors gives a positive-lambda finite-coordinate event. On that event
the component cylinder probability is positive. Thus mu has full support on
the entire X, including cylinders around histories with zero singleton mass.
Each S_i has at least two letters with positive probabilities, so each parity's
maximum one-letter mass is at most1-delta_theta for some delta_theta>0.
Independent draws imply every singleton has nu_theta mass0; integration shows
mu has no singleton atoms. In this countably coordinate-separated Borel
space, any positive Borel atom must lie almost entirely in a unique cell at
each coordinate; intersecting those cells gives a singleton of that mass.
Thus mu is nonatomic. No finite-alphabet restriction is hidden here.

## 3. Every-Borel transport and the declared full-point version

For every theta, almost surely every letter of S_0 appears on even sites and
every letter of S_1 on odd sites: omission of a fixed positive-probability
letter has probability lim_N(1-p)^N=0, and there are countably many letters.
Call this Borel event Q_theta. On Q_theta, the legal predecessor set is
EXACTLY S_1(theta): every color0 irreducible itself appears on an even site;
any integer using it is forbidden, while every color1-only integer is legal.
Consequently Z(y)=Z_1(theta) for nu_theta-almost every y. Q_theta is used to
prove an integral identity, never to replace the declared full carrier.

For ANY Borel D subset E_a, product independence, then the change theta->1-theta,
give

    mu(I_a D)
      = integral 1_(a in S_1(theta)) rho(a)/Z_1(theta) nu_theta(D) dlambda
      = integral_D rho(a)/Z(y) dmu(y).

The second equality uses Q_theta and the actual domain D subset E_a. It is
an identity for every Borel D, including null/exceptional sets, not merely
a formula for typical singleton paths. At EVERY y, L(y) is infinite,
0<Z(y)<=1, and 0<rho(a)/Z(y)<1 for every legal a. Hence the frozen j is
finite, Borel, strictly positive and sum_(a in L(y))j_a(y)=1 everywhere.
In particular all actual branch image measures and their source restrictions
have the same null sets. The version at exceptional points is an explicit
part of this owner; IMAGE alone does not assert its uniqueness or continuity.

For any legal finite prefix u=(u_0,...,u_(m-1)), put
J_u(y)=product_(i<m) j_(u_i)(u_(i+1)...u_(m-1)y).
Iterating the preceding every-Borel formula and the change-of-variables
identity for nonnegative simple functions proves
mu(I_u D)=int_D J_u dmu for every Borel legal D. This proves full finite
history transport, including all intermediate legal domains; J_empty=1.

## 4. Complete retained-lag and physical ledger

Write kappa(x)=-log j_(x_0)(Tx)>0 and A_m(x)=sum_(i<m)kappa(T^i x), A_0=0.
For G={(z,m-n,y):T^m z=T^n y}, source y and range z, define
c(z,m-n,y)=A_m(z)-A_n(y). Two witnesses for the SAME integer lag differ
by adding/removing equal tail lengths; the added sums on the common tail
cancel. Thus c descends to equal triples. Extending the two common tails
to a common witness proves the composition law c(gh)=c(g)+c(h).

The ratio of two finite-prefix identities also gives IMAGE exp(-c) for
every actual branch-pair replacement on every Borel part of its domain.
Every incoming arrow at y is obtained by choosing n>=0 and every prefix u
of length m with z=u T^n y in X; its lag is m-n and clock A_m(z)-A_n(y).
Different witnesses of an equal triple are not additional arrows. This is
also an exhaustive source-orbit description, with no chosen initial phase.
The lag kernel is precisely these triples with m=n; the clock kernel is
precisely those with A_m(z)=A_n(y); their intersection satisfies BOTH tests.
These are exact finite-sum membership rules on every admissible history,
not just typical formulas. Extension arrows are

    (y,h) -> (z,h+c(g)), for ALL real h and ALL g in G.

Source isotropy is zero unless y is eventually periodic; for eventual least
symbolic period l it is the ENTIRE lZ. Indeed a nonzero isotropy lag is
exactly an equality of two shifted tails, and least tail period divides all
such lags. A periodic word cannot have odd l: its repeated equal letter at
distance l would have gcd>1. For even l, admissibility is exactly that all
even-position letters are coprime to all odd-position letters; there is no
same-parity restriction. This gives every admissible primitive necklace.

For such a least word w, let R_0,R_1 be the products of its even/odd letters,
and Z[R]=sum_(gcd(a,R)=1,a>=2)rho(a). At a periodic phase the entire legal
predecessor set is determined by the opposite parity product, giving

    L(w)=log( (Z[R_0] Z[R_1])^(l/2) / product_(i<l)rho(w_i) ) > 0.

Thus c on full source isotropy sends rl to rL(w), and for every incoming
eventually periodic tail its full H is L(w)Z. There is no extra generator
from a finite prehistory: conjugation cancels its clock. For non-eventual
points H={0}. Extension isotropy is ker(c|Iso)=0 in both cases.
The real-height fiber over a whole source orbit is R/H; all heights are
retained. It is one translation circle/primitive packet for each primitive
necklace, or one nonclosed translation line for a non-eventual source orbit.
Traversing a word r times is repetition at rL, not a new primitive packet.
This set-level classification does not assert a Hausdorff smooth quotient.

## 5. First primitive and exact STOP

The word23 is legal of least source period2. Set beta=Z[2]=1-log2 and
gamma=Z[3]=1-sum_(k>=1)1/[3k(3k-1)]. Its whole H is L_23 Z, where
L_23=log(12 beta gamma), not an arbitrarily selected subgroup.
Here are exact bounds, without a finite experimental scan:

- beta > 1/6+1/20+1/42+1/72 = 641/2520 > 1/4.
- For k>=2, 1/[3k(3k-1)] < 1/[6k(k-1)]. Summing the telescoping upper
  bound and adding the k=1 term gives gamma>2/3.
- Integrating a geometric series gives log2=2 sum_(n>=0)
  1/[(2n+1)3^(2n+1)] > 2/3+2/81=56/81; hence beta<25/81.
- The k=1,2 terms in the removed gamma sum give gamma<1-1/6-1/30=4/5.

Therefore 2 < 12 beta gamma < 80/27 < 3, so log2<L_23<log3.
There is no integer prime strictly between2 and3. The full original owner
therefore fails its necessary prime-time target. No larger period table,
time-unit rescaling, deletion of this null periodic orbit or new version is
used to rescue it. This is STOP for FAH01, not a universal no-go for all laws.

## 6. Three complete own controls

The constructions below each prove their own product/mixed law and branch
identity by independence. Their positive j values supply finite-history
products, cocycle descent, all kernels and height phases exactly by section4's
argument, applied to THEIR sources and normalizers, not imported MAIN values.

**FIXED-ALLOCATION.** Let U={2^k:k>=1}, V={odd a>=3}, alpha=sum_U rho,
beta=sum_V rho. Full source is the union of the two alternating U,V product
spaces; phase is determined by the first letter. mu is the equal mixture of
the two normalized product probabilities. It is stationary, nonatomic and
full-support on this declared carrier. For a tail starting in V, all legal
predecessors are U, with own j_a=rho(a)/alpha; for a U-tail use V,beta.
All source periods are even primitive alternating words; all incoming
prefixes alternate and all packets have L=log((alpha beta)^(l/2)/prod rho).
Entire H=LZ, extension isotropy0, and kernels use the corresponding finite
products; non-eventual histories have H0. For23, L=log(12 alpha beta).
The first three U terms give alpha>3/5. The bound rho(2^k)<=2/4^k,
strict for k>=2, gives alpha<2/3.
The above log-series upper bound, replacing 1/(2n+1) by1/3 for n>=1,
gives log2<2/3+1/36=25/36, hence beta>11/36. Together with beta<25/81,
2<11/5<12 alpha beta<200/81<3. Its own wrong primitive also stops.

**OFF.** Full A^N0, iid rho. Every prefix is legal and j_a=rho(a), verified
on all Borel sets by product independence, then prescribed everywhere.
All primitive necklaces occur, with L=log product_i w_i(w_i-1)>0;
all incoming prefixes, retained lag, kernel equalities, H=LZ and free
extension follow as above with these own products. The constant3 packet
has entire H=(log6)Z, a wrong primitive; constant2 separately has log2.
This probability is stationary, nonatomic, full-support. No control credit
is transferred from that one successful prime-time packet.

**EXPLICIT-ALLOCATION.** Full carrier consists of EVERY nonconstant theta
and every alternating compatible x. S(theta,x)=(1-theta,Tx), law
dlambda(theta)dnu_theta(x); both null allocations and null paths remain.
The law is stationary; nonempty relative cylinders constrain finitely many
colors and letters and have positive measure. It is nonatomic. All actual
inverses send(theta,y) to(1-theta,ay), a in S_1(theta); independently
conditioning this mixture gives every-Borel j_a=rho(a)/Z_1(theta) on its
WHOLE domain. The same finite-history and positive-clock construction works.
Every incoming prefix carries the forced complement parity of theta.
Full isotropy requires even lag AND eventual periodicity of x; the intrinsic
symbol period is already even because the two alphabets are disjoint.
Primitive packets are all compatible(theta,w) modulo cyclic rotation WITH
the corresponding theta complement. L=log((Z_0 Z_1)^(l/2)/prod rho), H=LZ;
other histories have H0, extension isotropy0, and kernels are full product
equalities with this theta ownership. Uncountably many theta compatible with
23 give distinct packets up to the finite phase equivalence; equal times
across all those packets are NOT claimed. The allocation coloring only2
as0 and every other irreducible as1 is retained although prior-null; its
23 packet has exactly the FIXED-ALLOCATION time just computed, a wrong time.
This control cannot be turned into MAIN by secretly selecting a theta.

## 7. Gates, limits and reproducibility

T0 full Borel source/probability/transport owner ESTABLISHED. T1 its actual
all-point normalized IMAGE clock ESTABLISHED, strong naturalness OPEN.
T2 full packet ledger ESTABLISHED; fixed prime-time target STOP. T3 NOT
AUDITED; classical NOT APPLICABLE, formal UNASSIGNED, B NOT INVOKED.
No smooth/Hamiltonian/quantum owner, spectral divisor or determinant supplied.
This is a new law/version on375's old source, not old credit transferred.

The proof uses exact countable products/sums and elementary inequalities;
no scientific numerics, parameter search, truncation experiment or external
priority claim. Inputs and normalization are the frozen card. Reproduce by
the derivations in sections2–6. Evidence: [claim ledger](claim-ledger.md),
[scope review](evidence/scope-review.md), [separate derivation](evidence/independent-proof.md),
[final internal review](evidence/review.md), [batch record](batch-log.md).
ARS CP1 preceded proof; raw must freeze before manuscript unlock and CP2/CP3.
Shared-history internal model review is NOT_CALIBRATED, not external peer review.
Portfolio STOP this candidate; FORK a fresh architecture/contract only after
the five-round summary and user confirmation. No sixth round is initiated.
