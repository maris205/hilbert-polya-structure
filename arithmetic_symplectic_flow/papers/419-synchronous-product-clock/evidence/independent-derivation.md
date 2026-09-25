# SPC01 — card-only independent derivation

Candidate: `ANG-AUDIT-20260923-SPC01`; Paper419; session2026-09-23.
Scope: frozen synchronous full-product class and the three complete controls.
This is independent derivation from the card, NOT external peer verification.

## 1. Input, method and exposure

- candidate-card.md original88-line prefix SHA256 e03e09a6a4a99c3b0adfc514ad760a7ba8a37fd88aa626177b7335730bca1828.
- evidence/scope-review.md SHA256 06544a7d88e55ffdca24ffe3a4b57cb153da0ae600276704831a8f4a7955b4e1 — 86 frozen lines.
- After root's complete CP1 read and explicit raw release, I reread precisely
  card1–88 and verified its prefix hash. No later outcome, manuscript, README,
  ledger, peer answer,413 result or other new scientific input was accessed.
- Retained ARS/router/workflow/DA/runtime instructions govern the staged
  process. Earlier shared history and the card's informal design expectations
  are disclosed exposure, not evidence for the result. NOT_CALIBRATED; not
  blind, sealed, cross-model, human or external peer review. Effective served
  model identity/settings have not been independently attested.
- Method: measure identities, exact meeting equations, integer congruences
  and symbolic coordinate formulas. No scientific code, numerical search,
  outside source, auxiliary agent, Git mutation or external action was used.
  This file is my only write; I have not edited the scope report or card.

## 2. Full product branches and every-Borel IMAGE

Write Y_ai=T_a(P_ai). These are Borel branch images, with the actual Borel
isomorphisms I_ai:Y_ai->P_ai prescribed in the card. The product partition
consists of ALL P_1i times P_2j; it is countable, disjoint and covers X.
Its actual image is Y_1i times Y_2j, and its inverse is I_1i times I_2j.
Overlapping target images do not identify distinct source branches.

For a fixed branch put nu_a(E)=mu_a(I_ai E). This is the transport of the
restricted source measure, hence a measure; the assumption identifies it
on every Borel E with q_ai mu_a restricted to Y_ai. Both are sigma-finite:
one can cover the target by sets where mu_a is finite and q_ai is bounded.
On rectangles E_1 times E_2 the product inverse-image measure equals
nu_1(E_1)nu_2(E_2). Tonelli identifies this with integration of q_1i q_2j
against mu_1 times mu_2. Sigma-finite uniqueness on rectangles therefore
gives, for EVERY Borel E in Y_1i times Y_2j,

    mu((I_1i times I_2j) E) = integral_E q_1i(y_1)q_2j(y_2) dmu(y).   (1)

This includes sets of infinite measure. For example, countable finite-measure
rectangles with bounded q's provide the sigma-finite cover needed for the
uniqueness argument; no finite-total-measure or probability hypothesis is used.
The version is the prescribed pointwise product, positive and finite on its
entire branch image, not a newly chosen a.e. equivalent density. Therefore

    kappa(x_1,x_2)=kappa_1(x_1)+kappa_2(x_2),
    S_n(x_1,x_2)=S^1_n(x_1)+S^2_n(x_2),  n>=0.                    (2)

All values at periodic null points remain fixed. There is no extra constant,
roof, time normalization, branch discard or stationarity assumption.
The full N-step incoming set is T_1^(-N){y_1} times T_2^(-N){y_2}; each
factor is the union of all legal length-N inverse-branch compositions.
Their actual domains, not formal branch words alone, determine admissibility.

## 3. Actual same-lag groupoid and entire kernels

For a single total deterministic map, two presentations of (z,k,w) have
(m',n')=(m+r,n+r) after possibly exchanging their order. Since the earlier
meeting is actual and future iterates exist, the appended clock sums cancel.
Thus S_m(z)-S_n(w) depends only on the actual triple. For composable meetings
(m,n) from w to z and (p,q) from v to w, append p steps to the first and
n to the second. Their middle clock sums are both S_(n+p)(w), so their
sum is the clock on the meeting (m+p,n+q) from v to z. This proves descent,
additivity, the zero unit value and sign change under arrow inversion.
No branch-path isotropy is retained beyond the card's actual triples.

A product arrow gives parent arrows with the SAME integer k. Conversely,
let parent witnesses (m_a,n_a) have m_a-n_a=k. Set n=max(n_1,n_2) and
m=n+k. Append n-n_a steps to the a-th meeting; then both witnesses are
(m,n). Totality is precisely what licenses these extra forward steps.
Consequently, as actual groupoids and with their endpoint conventions,

    G = { (g_1,g_2) in G_1 times G_2 : lag(g_1)=lag(g_2) },
    c(g_1,g_2)=c_1(g_1)+c_2(g_2).                               (3)

The unrestricted Cartesian product of arrows is wrong. Formula (3) includes
every source branch and all common-lag witnesses, not a selected subgroupoid.
The groupoid and clock are Borel: use the countable Borel meeting relations,
and, if a formula is needed, select their first witness in a fixed countable
ordering; descent makes the resulting value independent of that ordering.

Let M_a be the parent lag kernel and K_a its clock kernel. Entire product
kernels, including arrows with distinct endpoints, are exactly

    M = { (g_1,g_2) : lag(g_1)=lag(g_2)=0 } = M_1 times M_2,
    K = { (g_1,g_2) in G : c_1(g_1)+c_2(g_2)=0 },
    K intersect M = { (g_1,g_2) in M : c_1(g_1)+c_2(g_2)=0 }.    (4)

M need not consist only of units for a noninjective parent. K need not be
K_1 times K_2: opposite nonzero parent values can cancel. At fixed equal
endpoints lag0 is the actual unit, not a hidden additional isotropy arrow.
Equations (3)–(4), with the prescribed sums, describe every clock value and
kernel arrow; no return-only or almost-everywhere replacement is used.

## 4. Complete source components, including nonperiodic parents

For parent points x,y define the full available-lag set

    L_a(x,y)={ k : (x,k,y) belongs to G_a }.

It is empty for distinct parent source components. A parent source component
is either the whole eventual basin of one finite cycle, or consists entirely
of non-eventually-periodic points. Indeed sharing a finite future meeting
preserves eventual periodicity and, in that case, the final cycle.

If a point enters a least-p cycle, its ENTIRE source isotropy is pZ: after
entry, equality of two future states requires their index difference to be
a multiple of p, and every such multiple has a sufficiently late witness.
Its clock on np is nC, where C is the signed cycle sum; transient sums cancel.
If a point is not eventually periodic, a nonzero isotropy lag would itself
give two unequal times with the same future state, a contradiction. Its
source isotropy is therefore0. Composing two arrows with the same endpoints
shows that nonempty L_a(x,y) is a coset of this isotropy subgroup. Thus it
is a coset of pZ in a periodic basin, and a singleton in a nonperiodic one.

For ALL product points z,w,

    L(z,w)=L_1(z_1,w_1) intersect L_2(z_2,w_2).                 (5)

Nonempty intersection is exactly source equivalence. In particular, merely
belonging to the same two parent components does not automatically suffice.
The following explicit split exhausts the Cartesian product of every pair
of parent source components, including all their incoming branches.

Periodic parent phases: number a least-p cycle b_0,...,b_(p-1) with
T b_i=b_(i+1). If T^e x=b_i, put v(x)=i-e mod p. This is independent of
the chosen entry time, satisfies v(Tx)=v(x)+1, and gives

    L_a(x,y)=v(y)-v(x)+pZ.                                    (6)

For a nonperiodic parent component choose a reference b and define d(x)
as the unique lag of an arrow (b,d(x),x). Then d(Tx)=d(x)+1, d(b)=0,
and L_a(x,y)={d(y)-d(x)}. No inverse surjectivity is assumed: forward
iterates of b already show that every nonnegative value of d occurs.
References here are packet-local; no global measurable transversal is claimed.

(i) Both parent components are periodic basins, of core periods p,q. Put
g=gcd(p,q), ell=lcm(p,q). By (5)–(6) and the integer congruence criterion,
their product splits into exactly g full source components labelled

    delta=v_2(x_2)-v_1(x_1) mod g.                             (7)

Every label occurs on the full Cartesian core. No finite incoming history
can merge two labels, since both phases advance by one at each step.

(ii) The first parent is a period-p basin and the second a nonperiodic
component. The complete split has exactly p components, labelled
delta=v_1(x_1)-d_2(x_2) mod p. Equality of this label is precisely the
congruence requiring the unique second-parent lag to be legal in the first.
All labels occur by choosing core phases in the first parent. If instead
the second parent is a period-q basin, labels are v_2-d_1 modulo q.

(iii) Both parents are nonperiodic components. Their complete split is
delta=d_2(x_2)-d_1(x_1) in Z. Equality is precisely equality of the two
unique lags. Every integer label occurs by taking sufficiently far forward
iterates of the two references. There are exactly countably many source
components for this particular pair of parent components, not one component.

Cases (ii) and (iii) have trivial source isotropy, hence H=0, despite any
nonzero arrow clocks. These splits and (5) cover all product source points;
no eventual-periodic assumption is imposed on the full owner.

## 5. Complete cycle ledger, incoming, height and signed boundary

Fix parent cycles gamma_1,gamma_2 with lengths p,q and signed sums C_1,C_2.
On their full pq-point Cartesian core, synchronous advance adds (1,1) to
the two cyclic indices. A return requires divisibility by BOTH p and q,
so its least length is ell. It follows that exactly pq/ell=g cycles occur,
precisely the labels (7). The signed sum on EVERY such product cycle is

    D=(ell/p) C_1+(ell/q) C_2=(q/g) C_1+(p/g) C_2.             (8)

Each coordinate traverses an integral number of its entire cycles, so this
does not depend on core phase or relative label. A product point is eventually
periodic if and only if both coordinates are; different entry times can be
advanced to their maximum because both maps are total. The full incoming
basin of each product core is exactly the corresponding label set (7), not
the unrestricted Cartesian basin and not just a selected section.

At EVERY point of any such full basin, including strict preperiodic points,

    source isotropy = ell Z,
    c(z,n ell,z)=nD (n in Z),       ENTIRE H_z=D Z,
    extension isotropy = { n ell : nD=0 }.                    (9)

The same source group also follows by intersecting pZ and qZ in (3).
For a common entry time N, both parent isotropy clocks cancel their initial
transients and give (8), proving the clock assertion even off the core.
If D!=0 there are exactly g positive packets from this pair of parent
cycles, each with primitive |D| and repetitions r|D|, r=1,2,... . If D=0
there are still g source packets and ell Z ineffective isotropy, but no
positive period from any of them. Taking absolute values BEFORE summing
is invalid. Neither negative D nor equal periods delete or identify packets.
In particular H is D Z, not the possibly larger group H_1+H_2.

The full extension consists of all objects (z,h), h in R, and arrows
(w,h)->(z,h+c(g)) for EVERY actual g=(z,k,w). There is ONE real height,
not a product of two parent height quotients. For a reference b in any source
component and an arrow a_z=(b,k,z), its complete phase is

    [h+c(a_z)] in R/H_b.                                    (10)

Different choices of a_z differ by isotropy and change this by an element
of H_b. Composition proves invariance, and an equal phase conversely gives
an actual extension arrow after adding the corresponding isotropy clock.
Every class occurs since all (b,h) exist. This classifies ALL extension
orbits; no smooth global orbit quotient or global Borel selector is implied.
Height translation acts by [u]->[u+t], with entire physical stabilizer H_b.
Extension isotropy in (9) is distinct from this physical time stabilizer.
For H=0 the phase is a free real line, even if source isotropy is nonzero.

An explicit incoming formula supplements (10). Choose the product core
reference b of the appropriate label, a common entry N for z, and
0<=j<ell with T^j b=T^N z. The arrow (b,j-N,z) is TO b and its clock is
S_j(b)-S_N(z). Thus the full phase is

    [h+S_j(b)-S_N(z)] modulo D Z.                             (11)

Changing N or j changes the value only by D Z. This also works when D=0,
where it is an actual real number and transient clock offsets still matter.
For the nonperiodic components of section4, (10) is a real phase and
extension isotropy is trivial. Formula (5) specifies every allowed incoming
point and (3) gives its exact clock; no partial or terminating owner is used.

## 6. Scoped integer-multiplier obstruction

Suppose an actual pair of parent cycles has A=exp(C_1), B=exp(C_2), with
A and B integers at least2. Their full Cartesian core is present, and (8)
gives D>0 and

    exp(D)=A^(q/g) B^(p/g).                                  (12)

Both exponents are positive integers and both factors exceed1. Their product
is a composite integer, so D is not log of an ordinary prime. Each of the
g actual packets therefore violates the prime-support requirement. One
eligible pair already obstructs the necessary target for the full product,
irrespective of other cycles. If g>1 multiplicity is also retained; even
g=1 cannot cure the composite primitive. No all-prime coverage argument is
needed for this obstruction, and no diagonal restriction is allowed.

This is conditional on existence of such a pair, not a theorem that every
full product has one. With no positive packet the separate nonemptiness
condition fails, but arbitrary mixed signs or rational multipliers are not
excluded by (12). In particular D=0 can occur by exact cancellation, and
D with prime exponential can occur outside the integer-positive hypothesis.
The controls below check both boundaries using their own complete owners.

## 7. Control A — full plane with expanding factors2 and3

The own global inverse is (u,v)->(u/2,v/3), with density derivative1/6
at EVERY point. Change of variables proves every-Borel inverse IMAGE for
Lebesgue area. Thus kappa=L_A=log6 on the entire plane. Equivalently the
two prescribed parent inverse densities are1/2 and1/3; their clocks add.
For every integer r,

    F_A^r(x,y)=(2^r x,3^r y),
    G_A={ (z,r,F_A^r z) },      c_A=r L_A.                    (13)

Since F_A is invertible, the formula includes all actual arrows and inverse
histories. M_A=K_A=K_A intersect M_A=units. The origin is the ONLY periodic
point: at a nonzero return r both fixed-coordinate equations force x=y=0.
It is fixed, has source isotropy Z, entire H=L_A Z and extension isotropy0.
Its sole physical packet has primitive log6 and repeats n log6. Its entire
source component is {0}; invertibility leaves no strict preperiodic entrance.

Every other point is aperiodic, with source/extension isotropy0 and H=0.
Its entire source orbit is {F_A^n z:n in Z}; its extended orbit through
(z,h) is { (F_A^n z,h-n L_A):n in Z }. This formula also applies at0,
where heights differing by L_A are identified and phase is h modulo L_A.

Explicit references cover ALL nonzero points. If x!=0, set
n=floor(log_2|x|), b=(2^(-n)x,3^(-n)y); then z=F_A^n b and
1<=|b_x|<2. If x=0,y!=0, set n=floor(log_3|y|), b=(0,3^(-n)y),
again z=F_A^n b with 1<=|b_y|<3. These unique references give the free
real phase h+n L_A by the arrow (b,n,z) TO b. Both axes and all signs
remain. The complete positive ledger has one composite primitive log6,
so prime support fails. A is an external ownership/control example only.

## 8. Control B — full two-sheet product and signed cancellation

The own inverse is (u,j,v,k)->(u/2,j-1,2v,k-1), with sheet indices
modulo2. It permutes all four sheets, and its continuous derivative has
absolute determinant1. Summing the Lebesgue change-of-variables identity
over the four target sheets proves every-Borel IMAGE for the OWN full
Lebesgue/counting measure. The all-point inverse density is1, kappa=0.
The two parent clocks are +log2 and -log2, not two positive logs.

For every integer r, including negative integers,

    F_B^r(x,j,y,k)=(2^r x,j+r,2^(-r)y,k+r),
    G_B={ (z,r,F_B^r z) },      c_B=0.                        (14)

Hence K_B=G_B, M_B=units and their intersection is units. The retained
integer lag is not reduced modulo2 even on an origin-sheet cycle.
Periodicity forces x=y=0 and an even return r. Thus the full periodic set
is exactly the FOUR origin-sheet states, all of least period2. It splits
into the TWO cycles labelled delta=k-j modulo2:

    delta=0: {(0,0,0,0),(0,1,0,1)},
    delta=1: {(0,0,0,1),(0,1,0,0)}.                          (15)

Each is its full source component, has source AND extension isotropy2Z,
entire H=0, and a free real phase h. Every non-origin point is aperiodic,
with both isotropies0 and H=0. All its inverse histories are exactly its
full two-sided orbit (14); no additional point can enter either finite cycle.
For every point the full extended orbit is { (F_B^n z,h):n in Z }.

For completeness, if x!=0 normalize with n=floor(log_2|x|) and b=F_B^(-n)z;
this retains both sheet indices shifted by -n and gives 1<=|b_x|<2.
If x=0,y!=0, let m=floor(log_2|y|) and b=F_B^m z, with 1<=|b_y|<2.
These are unique representatives of their full nonperiodic source orbits;
phase is h in either case. At the two origin cycles use b_delta=(0,0,0,delta).
Every origin-sheet state is a forward phase of exactly one such reference,
and h is still unrestricted. No sheet, half-cycle or real height is removed.

The parent origin cycles have p=q=2 and signed sums +2log2,-2log2.
Formula (8) gives g=2, ell=2 and D=0, consistently with the entire ledger.
The negative second sum lies outside (12). Replacing signed sums by their
absolute values, or adding only the parents' unsigned clock groups, would
give a false positive period. The true positive ledger is empty, so the
necessary target fails nonemptiness while both zero-clock cores remain.

## 9. Control C — a mixed-sign product with exactly one prime packet

The own inverse is (u,v)->(u/6,2v), with all-point density derivative1/3.
Lebesgue change of variables proves every-Borel IMAGE on the whole plane.
The prescribed clock is L_C=log3; its parent clocks are log6 and -log2.
For every integer r,

    F_C^r(x,y)=(6^r x,2^(-r)y),
    G_C={ (z,r,F_C^r z) },      c_C=r L_C.                    (16)

All kernels M_C,K_C and their intersection are units. Only the origin is
periodic, and it is fixed; both coordinate equations at a nonzero return
force zero. Its source isotropy is Z, extension isotropy0, entire H=L_C Z,
phase h modulo L_C and positive primitive log3, with repetitions n log3.
It is its whole source component with no strict preperiodic incoming.
Every nonzero point is aperiodic, has source/extension isotropy0 and H=0.
The full source and extension orbits are, respectively,

    {F_C^n z:n in Z},       {(F_C^n z,h-n L_C):n in Z}.         (17)

If x!=0 take n=floor(log_6|x|), b=F_C^(-n)z=(6^(-n)x,2^n y),
with 1<=|b_x|<6. Its free real phase is h+n L_C via (b,n,z) TO b.
If x=0,y!=0 take m=floor(log_2|y|), b=F_C^m z=(0,2^(-m)y),
with 1<=|b_y|<2; now z=F_C^(-m)b and the phase is h-m L_C.
This includes all signs and axes, all real heights and every inverse iterate.

The parents have p=q=1, C_1=log6 and C_2=-log2, so D=log3 as required.
The full positive ledger therefore satisfies the stated NECESSARY nonempty,
prime-only and at-most-one-per-prime benchmark, but covers only the prime3.
It does not provide all-prime coverage, endogenous arithmetic, naturalness
or admission as a main candidate. It is an EXTERNAL CONTROL demonstrating
why the integer-positive gate cannot be extended to arbitrary mixed signs.

## 10. Closure, limits and freeze hold

The full branch IMAGE and pointwise clock, actual same-lag arrows, kernels,
all source-component splits, incoming basins, source/extension isotropy,
entire H, phases and cycle multiplicities are derived above. No witness-only
census or numerical approximation stands in for an infinite claim. Opposite
signs and zero D are retained; no extra source or phase quotient is introduced.

The integer-positive cycle-pair hypothesis gives a decisive scoped STOP/FORK
against the necessary prime support. The unrestricted synchronous-product
class is NOT universally excluded: C shows the boundary of that statement.
No missing arithmetic parent is supplied by any control. Strong naturalness
and arithmetic adequacy remain unestablished; classical fields NOT APPLICABLE,
T3 NOT AUDITED, formal Route UNASSIGNED, Route B NOT INVOKED. No operator,
RH, novelty, literature-priority or external verification claim is made.

Freeze this raw record after complete readback; preserve the card and CP1.
HOLD for root's full raw read and separate PAPER UNLOCK before any author
surface is accessed. No further scientific round or round420 is authorized.

EOF — card-only raw derivation; shared-history internal NOT_CALIBRATED.
