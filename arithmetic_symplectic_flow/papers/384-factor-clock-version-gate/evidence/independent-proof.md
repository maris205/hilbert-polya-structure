# FVG01 — independent full factor-clock regularity audit

Candidate `ANG-AUDIT-20260922-FVG01`; `FULL-TRANSPORT-20260922-G`, round5/5.
2026-09-22; reviewer `/root/nonlocal_source_review`.
Inputs: complete384card55lines and380card70lines only, following root's
explicit mathematical release after CP1. Input receipts:

384 candidate-card.md SHA256 e97733825ca454eb8a1d1fa51203001d8a5c4854aebb45cc3862ab4d0530f0b2
380 candidate-card.md SHA256 b5fda99de6457de81fcc6338c4e6ba9102b92402c815e3a8902e8365f5ba753b

No380 result,384 manuscript, peer proof or current batch log was read.
Separate derivation here remains internal shared-history `NOT_CALIBRATED`,
not blind, cross-model or external peer review. No external lookup, numerical
experiment, Git operation or target-dependent choice is used.

## 1. Reconstructing the conditional owner from its card

Let A={2,3,...}; P its multiplicatively irreducible integers. Write supp(a)
for a's finite irreducible-factor set. Let X contain EVERY one-sided history
whose even-position entries are coprime to every odd-position entry.
This is a closed subspace of A^N0; left shift T is continuous and total.
ALL one-step inverse domains are E_a={y:gcd(a,y_(2j))=1 for every j>=0}.
For a word u of length m, its complete domain E_u consists of tails y in X
such that opposite-parity entries of u are coprime and
gcd(u_i,y_j)=1 whenever 0<=i<m,j>=0 and m+j-i is odd.
These tests are necessary and sufficient, including every cross-boundary
interaction. Prefix insertion is a homeomorphism from its closed Borel domain
onto its cylinder intersection with X. No surjectivity or etale claim is used.

Put rho(a)=1/[a(a-1)], so sum_(a>=2)rho(a)=1 by telescoping.
For each nonconstant theta in {0,1}^P, S_i(theta) is all a>=2 with
supp(a) contained in theta^(-1)(i). Let Z_i=sum_(a in S_i)rho(a).
Both Z_i are positive and finite; each S_i contains p and p^2 for some p.
The product law nu_theta has independent even coordinates rho/Z_0 on S_0
and odd coordinates rho/Z_1 on S_1. All its histories lie in X.
The fair factor-coordinate prior is denoted pi; the constant allocations
have pi-measure zero, since there are infinitely many irreducibles.
Their infinitude follows by factoring one plus any proposed finite product.
No source histories are deleted when those two latent null allocations are
omitted in the mixture mu=integral nu_theta d pi(theta).

Membership in S_i is a finite-coordinate condition on theta, and Z_i is a
countable sum of measurable nonnegative terms. Thus cylinder probabilities
and the product probability kernel are measurable, so mu is a probability.
T_*nu_theta=nu_(1-theta), and pi is color-flip invariant, hence T_*mu=mu.
Every nonempty source cylinder has positive mu: assign the finitely many
factors in its even/odd symbols to their respective colors. Admissibility
makes these assignments consistent, their prior probability is positive,
and each resulting component assigns positive probability to the cylinder.
Thus mu has full source support. It has no atoms: in each component an even
coordinate law has at least two positive atoms, hence maximal atom at most
1-delta_theta<1 for some delta_theta>0. Independent even coordinates give
nu_theta({x})=0 for every x; integrating gives mu({x})=0.

For nu_theta-almost every y, every symbol of S_0 appears among its even
coordinates and every symbol of S_1 among its odd coordinates. Each such
event has probability one by independent positive-probability trials, and
there are countably many symbols. In particular the union of factor sets
seen in even entries is theta^(-1)(0). Therefore, almost surely in that
component, L(y)={a:y in E_a}=S_1(theta) and Z(y)=Z_1(theta).
On EVERY y in X, including exceptions, y_1 and all its powers lie in L(y).
Consequently 0<Z(y)=sum_(a in L(y))rho(a)<=1, L(y) is infinite, and
j_a(y)=rho(a)/Z(y) lies strictly between0 and1 on E_a, with sum_(a in L)j_a=1.
All these functions are Borel. No typical set replaces the full carrier.

For Borel D subset E_a, the product decomposition at its first coordinate is

    nu_(1-theta)(I_a D)
      =1_(a in S_1(theta)) rho(a)/Z_1(theta) * nu_theta(D).             (1)

When a has a color0 factor, nu_theta(E_a)=0, because typical even histories
contain that factor. Otherwise E_a has full nu_theta measure. Integrating(1),
using color-flip symmetry and the typical-tail identity above, proves

    mu(I_a D)=integral_D j_a(y) d mu(y)                                (2)

for EVERY Borel D subset E_a. This is a fresh proof of the required premise,
not an imported380 outcome. It proves measurable positive versions exist.

## 2. No IMAGE version can be continuous at the frozen probe

Let y*=(3,2)^infinity in E_2. Suppose g is ANY finite IMAGE density for I_2
on E_2. Equation(2) and equality of integrals on all Borel subsets imply
g=j_2 mu-almost everywhere on E_2. For example the sets where g-j_2 exceeds
any positive rational must be null, and likewise for j_2-g.

We construct positive-measure sequences approaching y*, not single latent
allocations of prior probability zero. Fix M=40. Let C_0 be the allocation
event with theta(2)=1 and every other irreducible p<=M colored0. Let C_1
instead color2 and5 by1 and every other irreducible p<=M by0. Both events
have positive prior probability, and both color3 by0; all their allocations
are nonconstant. Define finite sums

    B_0=sum_(2<=a<=M, supp(a) subset {2}) rho(a),
    B_1=sum_(2<=a<=M, supp(a) subset {2,5}) rho(a).

For theta in C_i, B_i<=Z_1(theta)<=B_i+1/M, since
sum_(a>M)rho(a)=1/M. Moreover B_1-B_0>=rho(5)=1/20>1/40.
These are exact rational inequalities, not a sampled cutoff inference.
In particular B_0+1/40<B_1, separating the two complete component families.

Let U_N be the relative neighborhood in E_2 fixing the first N coordinates
to those of y*. For every theta in C_i its product probability is positive:
the prefix uses only3 on even sites and2 on odd sites, and E_2 is conull
in that component. The typical factor-recovery event is also conull.
It follows by integration that, for EVERY N, the Borel sets

    A_i,N={y in U_N:B_i<=Z(y)<=B_i+1/40}

have positive mu. Remove g's null disagreement set; both sets still have
points. On A_0,N the value of g is at least rho(2)/(B_0+1/40); on A_1,N it
is at most rho(2)/B_1. Their separation delta is strictly positive and
independent of N. Choosing one point from each remaining set for every N
gives two sequences converging to y* in the inherited E_2 topology, with
g-values separated by at least delta. Continuity at y* is impossible.

Thus NO finite strictly positive IMAGE version is continuous on E_2; indeed
none can be continuous even at y*. This is stronger than discontinuity of
the displayed j. It does NOT contradict the measurable version proved in§1.
No a.e. equivalence was converted into equality on a selected null point.

## 3. Entire modification class and every-Borel versions

Let x*=(2,3)^infinity and O its ENTIRE eventual-tail G-class in X.
It consists exactly of all legal finite prefixes attached to either phase
of that periodic tail. There are countably many finite words, so O is
countable; equivalently it is the union over m,n of {x:T^m x=T^n x*}, hence
Borel. The atomlessness established in§1 gives mu(O)=0.
O is saturated for the actual equal-tail relation, not just T-invariant;
inserting ANY admissible prefix or taking a tail stays in the same class.

a_0(y)=min L(y) is well defined and Borel. For fixed t>0 define on O

    D_t(y)=Z(y)+(t-1)rho(a_0(y)),
    j_a^t(y)=rho(a)t^(1_(a=a_0(y)))/D_t(y),                            (3)

and let j_a^t=j_a outside O. Since L(y) is infinite, D_t is a positive
sum over infinitely many positive terms. Every j_a^t on E_a is strictly
between0 and1, and their sum over ALL legal branches is1 at EVERY point.
Borelness follows from the Borel least-symbol function and O. The versions
agree mu-a.e.; equation(2) therefore holds for j_a^t on EVERY Borel subset
of every E_a. No null source, prefix or boundary point is removed.

For each t separately define kappa_t(x)=-log j_(x_0)^t(Tx)>0 and
A_m^t(x)=sum_(0<=i<m)kappa_t(T^i x), with A_0^t=0. For a legal word u,

    J_u^t(xi)=product_(0<=i<|u|) j_(u_i)^t(u_(i+1)...u_(|u|-1)xi)
             =exp(-A_(|u|)^t(u xi)).                                 (4)

Induction in the every-Borel IMAGE identity proves
mu(I_u D)=integral_D J_u^t d mu for every Borel D subset E_u. This is
full finite-history transport, not a typical-tail approximation.

## 4. Full groupoid, kernels, isotropy, incoming and phases for EACH t

The actual source groupoid is G={(z,m-n,y):T^m z=T^n y}. Equal triples
alone are identified. Every arrow is (u xi,|u|-|v|,v xi) on E_u intersect E_v.
Define c_t=A_m^t(z)-A_n^t(y)=log(J_v^t(xi)/J_u^t(xi)). Different witnesses
for the same triple differ by common padding of the shift exponents; the
equal terminal histories contribute identical added sums. Thus c_t descends
and is additive. Each fixed t owns its own cocycle, not a versionless c.

The complete kernels, including their intersection, are precisely

    ker c_t={ (u xi,|u|-|v|,v xi):J_u^t(xi)=J_v^t(xi) },
    ker lag={ (z,0,y):T^m z=T^m y for some m },
    ker c_t intersect ker lag: both the product equality and |u|=|v|.  (5)

Here ALL legal words/tails are quantified; no inverse chart is discarded.
For fixed y, all outgoing arrows are (u T^n y,|u|-n,y), with T^n y in E_u.
All incoming arrows are their inverses, and their endpoints give the entire
source orbit. These formulas include arbitrarily long preperiods.

No source point can have an odd eventual period, since that repeats a
symbol at an odd separation and contradicts coprimality. Its entire source
isotropy is{0} when it is not eventually periodic, otherwise l Z, where l
is the least eventual word period and is even. For an even cyclic word w,
admissibility is EXACTLY gcd(product_(i even)w_i,product_(i odd)w_i)=1.
Primitive words are those not a proper power, modulo cyclic rotation;
neither reversal nor equal clock values merge distinct primitive necklaces.
Every legal eventual prefix is included via E_u. Distinct necklaces cannot
merge, since equal shifted periodic tails force cyclic equality of cores.

For such a primitive w let C_t(w)=sum_(0<=i<l)kappa_t(T^i w^infinity)>0.
At EVERY point in its eventual class, c_t on source isotropy sends r*l to
r*C_t(w): a prefix cancels in A_(N+l)-A_N. Therefore the full height extension
on X times R has trivial fixed-object isotropy everywhere. Its height-action
stabilizer is H_x=C_t(w) Z on that entire class, and H_x={0} on aperiodic
classes. This follows directly by composing any return to an isotropy arrow.
No representative-only H calculation replaces the full class calculation.

For an arrow g from a reference x to z, the phase of(z,h) is
h-c_t(g) modulo H_x. All incoming arrows and all heights are retained;
changing g changes this expression by an element of H_x. Over each source
orbit the orbit SET of the height extension is thus R/H_x. Periodic classes
give one primitive physical circle per primitive necklace, with least time
C_t(w) and rth repetition r*C_t(w); nonperiodic classes give real lines.
No Hausdorff/manifold or finite-dimensional symplectic conclusion is made.

For an explicit base formula, write F_even(w),F_odd(w) for unions of factors
in its respective parity positions, and Q(F)=sum_(supp(a) disjoint F)rho(a).
Then

    C_1(w)=(l/2)log[Q(F_even(w))Q(F_odd(w))]-sum_i log rho(w_i).         (6)

This is the exact full-point recipe, not a latent component denominator.
For every necklace except23, its entire class lies outside O, so C_t(w)=C_1(w)
and its full clock agrees with the base. Within O, all transient clocks
remain defined by(3)–(4), while the isotropy/packet time is calculated next.

## 5. Whole23 packet and the three frozen parameter controls

Put Z_2=sum_(a>=2,2 does not divide a)rho(a) and
Z_3=sum_(a>=2,3 does not divide a)rho(a). At (3,2)^infinity, L excludes
multiples of3 and a_0=2; at (2,3)^infinity, L consists of odd integers>=3
and a_0=3. Define A=2 Z_3-1>0 and B=6 Z_2-1>0; strictness follows because
the respective legal sets contain more than just their least symbol.
The two actual branch values and the WHOLE primitive-packet time are

    j_2^t((3,2)^infinity)=t/(t+A),
    j_3^t((2,3)^infinity)=t/(t+B),
    C_t(23)=log[(1+A/t)(1+B/t)].                                     (7)

Source least period remains2 on the core, and source isotropy is2 Z at
every point of O. Extension isotropy is trivial, H=C_t(23) Z on ALL O,
and phase is h-c_t(g) modulo C_t(23); all admissible prefixes are included.
The rth packet repetition has time r*C_t(23), never a new primitive packet.

BASE t=1: C_1=log[(1+A)(1+B)]=log(12 Z_2 Z_3).
DECREASE t=1/2: C_(1/2)=log[(1+2A)(1+2B)]>C_1.
INCREASE t=2: C_2=log[(1+A/2)(1+B/2)]<C_1.
Thus decreasing the parameter increases this packet's time; the labels name
the parameter, not the time. Each control's remaining source, every-Borel
transport, kernels, other packets and phases are given separately by its
fixed value in(3)–(6), not silently inherited from a versionless clock.

Equation(7) is strictly decreasing in t>0, tending to infinity as t tends
to0 and to0 as t tends to infinity. This establishes positive-time freedom
on this one precommitted null packet; no t is chosen for a target log p.
For different t the cocycles even differ on isotropy, so their difference
cannot be a mere height coboundary, which vanishes at every isotropy arrow.
They are genuinely distinct full-point clock owners with the same source,
probability and every-Borel IMAGE property. None is declared canonical.

## 6. Bounded disposition and controls against overreach

STOP the continuous-version requirement: even arbitrary IMAGE versions
cannot be continuous at the frozen point. Do NOT stop measurable existence:
§§1,3 prove positive every-Borel versions on the whole source. The full-source
clock is not identified by the measure law alone, as the three untuned
controls already give different primitive times on one entire null class.
This does not retroactively edit380, identify a preferred version, prove a
prime-target result, or resolve other proposed regularity requirements.
All conclusions are exact proofs from the two cards; M=40 is an analytic
tail bound in the regularity proof, not a scientific scan or fitted parameter.
Strong naturalness OPEN; classical NOT APPLICABLE; T3 NOT AUDITED; formal
UNASSIGNED; B NOT INVOKED. No sixth round begins after this audit.

EOF — raw proof frozen before manuscript access; await explicit PAPER UNLOCK.
