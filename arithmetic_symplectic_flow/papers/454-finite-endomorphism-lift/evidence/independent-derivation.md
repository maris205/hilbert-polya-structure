# FEL01 — independent full-endomorphism derivation

Candidate: ANG-AUDIT-20260924-FEL01.
Batch: TRANSPORT-PACKET-20260924-U; Paper454, round5/5; no455.
Reviewer: pcr01_independent_review. Date: 2026-09-24 UTC.

## 0. Scientific input and review boundary

The scientific input is the frozen card and its CP1 coverage clarification:
original96 lines SHA256
`20748816cab93b86a339ea13addb8a7fcae879c6ec8c81ced496c122f82e909e`;
complete105-line pre-release card SHA256
`ad4f00a8a77b8d65df65c866e758c9161a588176eb37e7a8ae118b9b3cd90a19`.
In particular the disjoint Borel P_i cover all X. Root reported its complete
CP1 read before the separate RAW RELEASE. No author manuscript, package
README, ledger, Outcome, peer result, helper result or old proof is read.
Prior summary exposure and inherited history are disclosed in CP1; no prior
theorem is used as a proof here. This is separate-author same-model internal
work, NOT_CALIBRATED, not blind, human, external or cross-model verification.

All deductions are exact from the card. There is no scientific code,
numerical census, external search, Git mutation, PDF or publication work.
The class is a conditional lift audit, not an endogenous prime candidate.

## 1. Complete actual lift inverse and its own IMAGE

For each base piece P_i and endomorphism tau:E->E, let

    P_(i,tau)=P_i intersect {x:sigma(x)=tau}.

These Borel sets partition X because End(E) is finite and the P_i form the
complete base partition. For each e in E, the lifted source piece is
P_(i,tau) x {e}. Its image is T(P_(i,tau)) x {tau(e)}, and its actual inverse is

    theta_(i,tau,e)(y,tau(e))=(I_i(y),e),
    y in T(P_i), sigma(I_i(y))=tau.

The image condition is Borel: it is tested by the given Borel I_i on T(P_i).
Both inverse identities follow from T I_i y=y and I_i T x=x on that base
piece. The source sheet is part of the branch identity. If several source
sheets have the same tau(e), each supplies an actual inverse branch; their
target images may coincide and none is discarded. If no source sheet maps
to a target sheet, there is no one-step inverse there, but the forward F
remains total at that target state. No terminal is thereby created.

Write nu=mu x counting. On one of these actual inverse images, every Borel
set has the form A x {tau(e)}, with A a Borel subset of T(P_(i,tau)). Then

    nu(theta(A x {tau(e)}))=mu(I_i(A))
       =integral_A J_i(y) dmu(y)
       =integral_(A x {tau(e)}) J_i(y) dnu(y,tau(e)).

This proves the lifted every-Borel IMAGE identity from its own measure.
The prescribed all-point version J_lift(y,tau(e))=J_i(y) is positive finite
and Borel on the branch, including null points. There is no division or
multiplication by the number of preimage sheets in a branch's IMAGE factor.
Summing measures of several inverse images is a different operation from
choosing the actual inverse germ of one source. The null-point version is
frozen data, not a uniquely inferred consequence of an a.e. identity.

For each actual source, this independent IMAGE construction yields

    kappa_F(x,e)=-log J_lift(F(x,e))=kappa_T(x).

Every sheet, including a transient or no-incoming sheet, has this own
next-step clock because F is total. Signed and zero clocks are retained.

## 2. Iterates, every inverse depth and exact lifted arrows

Define the transported fibre maps

    Sigma_0(x)=id_E,
    Sigma_n(x)=sigma(T^(n-1)x) composed ... composed sigma(x),  n>=1.

They obey Sigma_(m+n)(x)=Sigma_n(T^m x) composed Sigma_m(x), and

    F^n(x,e)=(T^n x,Sigma_n(x)e).

The complete depth-n predecessor set of (y,f) is exactly

    {(x,e): T^n x=y, Sigma_n(x)e=f},

using all actual base inverse branches and all e in E. Finite histories
are all such compatible branch choices; infinite histories retain every
compatible sequence of finite prefixes. No extra sheet-word multiplicity
is attached to a state or arrow: one initial state has one deterministic
forward history. Different witnesses of the same lag triple remain one arrow.

For U=T and U=F separately, form G_U={(z,m-n,w):U^m z=U^n w}, m,n>=0.
Define S_n^U(z) as the own clock sum, S_0=0, and c_U=S_m^U(z)-S_n^U(w).
Two witnesses for one triple differ by the same integer in both indices.
Extending to the larger witness adds the identical common-tail sum on both
sides, proving descent. For composable witnesses, align the two middle
depths at their maximum; the common middle sums cancel. Thus c_U is
additive, changes sign on inverse arrows, and has forward-arrow value

    c_U(Uz,-1,z)=-kappa_U(z).

Since S_n^F(x,e)=S_n^T(x), the full lifted arrow condition is

    ((x,e),m-n,(y,f)) belongs to G_F
    iff T^m x=T^n y AND Sigma_m(x)e=Sigma_n(y)f
    for some m,n>=0,

and its clock is S_m^T(x)-S_n^T(y). Projection defines a groupoid
homomorphism pi_G:G_F->G_T retaining lag and clock. It is not presumed to
lift every parent arrow for every pair of source and target sheets.

More explicitly, fix a parent arrow witness T^m x=T^n y=z. Put
a=Sigma_m(x)e and b=Sigma_n(y)f. A lift with that same lag exists exactly
when Sigma_j(z)a=Sigma_j(z)b for some j>=0. Sufficiency extends the witness
by j. Necessity follows by extending any lifted witness to a common later
depth with the given parent witness; totality permits the extension. Thus
future fibre merging is retained even when equality fails at the first
chosen parent witness. No inverse permutation is assumed.

For each U its complete kernels are

    ker lag_U = {(z,0,w): U^n z=U^n w for some n>=0},
    ker c_U = {(z,m-n,w): U^m z=U^n w, S_m^U(z)=S_n^U(w)},
    ker(lag,c)_U = ker lag_U intersect ker c_U.

For F these equations include all fibre-merging arrows, and
ker c_F=pi_G^(-1)(ker c_T), with analogous identities for lag and the joint
kernel on the actual lifted arrow set. The pullback statement introduces
no nonexistent fibre arrows. In particular two sheets over the same x
that eventually merge produce a lag-zero, clock-zero nonunit arrow.

## 3. Whole source packets, isotropy and all real phases

Let Inv_U(A) contain every actual one-step predecessor of every point of A.
The entire source packet of w for either owner is

    union_(n>=0) union_(m>=0) Inv_U^m({U^n w}).

This is both necessary and sufficient for a common forward iterate and
retains all inverse depths. A source with a nonzero-lag loop is eventually
periodic, because two distinct forward times agree. Conversely, if its
tail reaches a least-L cycle with signed sum C_*, its source isotropy is
exactly L Z and the isotropy character is r L -> r C_*.
No other lags can occur once the eventual cycle has least period L, and
every multiple occurs by extending a witness after reaching that core.

The full height extension has arrows (w,h)->(z,h+c_U(z,k,w)). Height
translation by t preserves the extension orbit of (w,h) exactly when a
source isotropy arrow at w has clock t. Consequently the ENTIRE stabilizer is

    H_w=C_* Z                       for an eventual least-L core,
    H_w={0}                         for a non-eventual source.

If C_*!=0, the extension isotropy is zero and the positive primitive is
|C_*|, with positive integer repeats. If C_*=0, extension isotropy remains
L Z but there is no positive physical return. Non-eventual sources have
both isotropies zero. Incoming states cannot shorten H: the character just
computed includes every possible source loop at every point in the packet.

For a cyclic component choose ordered core a_0,...,a_(L-1), put
K_j=S_j^U(a_0), K_0=0, K_L=C_*. For each z in its full incoming basin let
d_z be first entry depth and j_z its core entry phase. Set

    l_z=d_z-j_z,       b_z=S_d_z^U(z)-K_j_z.

Then all component arrows, including all incoming states, are

    (z,l_z-l_w+r L,w),       c_U=b_z-b_w+r C_*,       r in Z.

Necessity follows by comparing the common eventual cycle phases; sufficiency
follows by taking large enough forward depths with the specified difference.
All restricted lag, clock and joint kernels are the respective equalities
l_z-l_w+r L=0, b_z-b_w+r C_*=0, or both. Every real phase is

    h-b_z modulo C_* Z.

For C_*=0 this is a real value, and entry-clock differences need not vanish.
A zero cycle sum does not imply the entire component cocycle is zero.

For each non-eventual component choose a set-level reference a and its
unique arrow g_z:a->z. Two different lags between fixed points would force
an eventual cycle, so this arrow and its clock are unique as a triple.
The complete real phase is h-c_U(g_z). No measurable global selector or
regular orbit-quotient topology is asserted in either construction.

## 4. Complete finite functional graph over a parent core

Fix a parent least-q core x_0,...,x_(q-1), with x_j=T^j x_0 and signed
C=S_q^T(x_0). Let a_j=sigma(x_j) and

    P=a_(q-1) composed ... composed a_0:E->E.

Every finite endomorphism graph has at least one directed cycle, and each
vertex reaches exactly one such cycle after finitely many iterates. This
follows by the first repeated vertex in its forward sequence and determinism.
Let the cycles of P be O_1,...,O_s, with respective lengths r_1,...,r_s;
all remaining vertices, if any, are transient. No injectivity is required.

Each O_i gives one actual lifted periodic core: start at (x_0,e) for e in
O_i and iterate F. A return to this state must occur at a multiple of q
because the parent has least period q. At time q n its sheet is P^n e,
so its least lifted source period is exactly q r_i. Two points of O_i
lie on this same lifted cycle, not two different packets.

The lifted core has exactly r_i points over each parent phase. Distinct
cycle vertices cannot merge during a partial traversal: if their images
after j steps agreed, completing the q steps would give equal images
under P, impossible on P's cyclic set, where P is a permutation.
Thus there are q r_i distinct states on the lifted core, with no hidden
shorter cycle or omitted periodic sheet.

Conversely every lifted periodic core projects to a parent periodic core.
Its intersection with the x_0 fibre consists of periodic vertices of P,
and one P-cycle generates the whole lifted orbit. This proves coverage and
converse. Distinct P-cycles cannot be joined by any full incoming packet:
a deterministic point cannot eventually reach two different periodic cores.

The cycle sum is exactly r_i C, because the own lifted clock equals the
parent step clock at every phase and the orbit traverses the parent q-core
r_i times. Therefore on the entire corresponding lifted basin,

    source isotropy = q r_i Z,
    entire H = r_i C Z,
    extension isotropy = q r_i Z if C=0, and zero otherwise,
    positive primitive = r_i |C| if C!=0, and none if C=0.

The general all-arrow, kernel and real-phase formulas of Section3 apply
with L=q r_i and C_*=r_i C. All positive integer repeats remain. A transient
sheet does not divide the source period, change H, create a second core,
or contribute an extra sheet-word multiplicity. It remains an actual state
and can create nonunit merging arrows, which those formulas retain.

## 5. Full incoming assignment, including parent preperiods

Let (x,e) project to the entire incoming packet of the chosen parent core.
Let t be the parent's first arrival depth and x_j its entry phase:
T^t x=x_j. Its actually transported sheet there is e_j=Sigma_t(x)e.
To align with x_0, take h_j=0 if j=0 and h_j=q-j otherwise; define H_0=id
and H_j=a_(q-1) composed ... composed a_j for j>0. The aligned sheet is

    u=H_j(e_j),       F^(t+h_j)(x,e)=(x_0,u).

Iterate the ENTIRE finite graph of P starting at u. If it enters O_i after
l return iterations, then F^(t+h_j+q l)(x,e) is on the corresponding lifted
core. This is a valid arrival time, not necessarily the first lift-core
entry: entry at another parent phase may have occurred earlier. The first
actual lift entry used in Section3 is obtained from its finite forward path.

This assigns every (x,e) over the parent's full incoming packet to exactly
one O_i. Explicitly the i-th lifted basin is

    {(x,e): x eventually reaches the parent core and
             H_j Sigma_t(x)e belongs to the P-basin of O_i},

with t,j determined by the actual first parent arrival. It is equivalently
the union of all unrestricted inverse depths of that lifted core, using
every base inverse and every matching source sheet from Section1.
Hence the assignment includes all parent inverse trees and every finite
fibre transient, including sheets with no immediate predecessor.

If a parent class is non-eventual, none of its lifts can be eventually
periodic: projecting a lifted eventual cycle would give a parent cycle.
The full relation and every incoming history there are still the exact
equations of Sections2–3, with all merging kernels retained. Each lifted
component has source/extension isotropy zero, H={0}, and every real phase
h-c(g_z). No positive packet can appear over such a parent component.
Its lift need not be represented by a selected sheet over one parent anchor;
no unproved description of its component count or sheet bijections is used.

## 6. Reference-phase invariance without full-graph conjugacy

For 1<=j<q write R_j=a_(j-1)...a_0 and L_j=a_(q-1)...a_j, in the indicated
composition order. The return endomorphism at x_j is P_j=R_j L_j while
P=L_j R_j. Thus

    R_j P=P_j R_j,       L_j P_j=P L_j.

Let Per(P) denote its cyclic vertices. R_j maps Per(P) to Per(P_j).
It is injective there: if R_j u=R_j v with u,v cyclic, applying L_j gives
P u=P v, and P is injective on Per(P). It is surjective there: for cyclic
w of P_j, choose its cyclic predecessor w_- with P_j w_-=w. Then
u=L_j w_- is cyclic for P and R_j u=w. Hence R_j is a bijective conjugacy
of the CYCLIC restrictions, preserving all cycle lengths and their count.
This is proved on the periodic subsets, not assumed on the entire E.

Transient assignment is compatible without a transient bijection. If u
eventually enters O_i under P, then R_j u eventually enters R_j O_i under
P_j by the intertwining equation. Conversely one can transport from phase
j back to phase zero with L_j before assigning its eventual cycle.
These assignments describe the same actual lifted core and full packet.
Cycle sum C is invariant under cyclic parent phase shift, and r_i is
preserved, so q r_i, r_i C, entire H and packet multiplicities are invariant.

The actual forward phase arrow from (x_0,e) to (x_j,R_j e) has lag -j and
clock -S_j^T(x_0). Changing a fibre-cycle representative by l parent returns
adds the actual shift -l C. Such changes translate the real phase coordinate;
they do not rescale its physical stabilizer or delete phases.

Full functional graphs genuinely need not be bijectively conjugate. As a
finite algebraic witness within the class, on E={0,1,2} take

    a=(0,0,1),       b=(0,1,1),
    b a=(0,0,1),     a b=(0,0,0),

where tuples list values at 0,1,2. One composition has a length-two
transient chain 2->1->0; the other is a star with 1,2->0. Their indegree
multisets differ, so their full graphs cannot be conjugate by a bijection.
Both have the same one-vertex cyclic restriction. This is a witness for
the scope of the phase statement, not a new prime candidate or a replacement
for any of the three frozen full controls.

## 7. Exact primitive multiplicities and the rational-parent criterion

Index distinct parent periodic cores/full periodic packets by O. Let their
least periods and signed sums be q_O,C_O. Let n_(O,r) be the number of
length-r cycles of the complete return endomorphism at any parent phase.
Section6 makes this number phase-independent. It obeys

    sum_r r n_(O,r) <= D,       sum_r n_(O,r) >= 1.

Strict inequality in the first expression corresponds to transient vertices;
such vertices are not lost states. The complete positive primitive ledger
of the lift, with packet multiplicity, is exactly the multiset

    { r |C_O|, repeated n_(O,r) times : C_O!=0, r>=1 }.

There are no additional positive packets over zero-clock or non-eventual
parent classes. Distinct O or distinct return cycles give distinct lifted
packets even when the displayed lengths agree. Thus positive nonemptiness
is equivalent for parent and lift, while purity and uniqueness require
inspection of these full multiplicities, not just one return-map orbit.

Now impose the frozen rational hypothesis a_O=exp(|C_O|) in Q, a_O>1,
for each C_O!=0. If a_O^r is an ordinary prime p, write a_O=u/v in lowest
positive integer terms. The equality u^r=p v^r and coprimality force v=1;
then u^r=p forces r=1 and u=p. Conversely r=1 and a_O=p plainly suffice.
This exact elementary argument does not apply to irrational a_O.

Therefore lift PRIME PURITY is equivalent to both of the following:

1. Every nonzero parent multiplier a_O is an ordinary prime.
2. Every directed cycle of every such return endomorphism has length one.

Zero-clock parent endomorphisms are unrestricted by positive prime purity.
Every finite endomorphism has a cycle, so a wrong nonzero parent multiplier
cannot simply be hidden in transient sheets of a full finite lift.

Under purity, the number of lifted packets with prime primitive log p is

    N_p = sum_(O:a_O=p) n_(O,1).

This is a sum over distinct parent packets, not over phase representatives;
it may be infinite. The exact uniqueness condition is N_p<=1 for every p.
Since each relevant graph has at least one cycle, the combined necessary
benchmark (nonempty, prime-only, at most one packet per prime) is equivalent
to the parent satisfying that same benchmark AND, for every C_O!=0, its
return graph having exactly one cycle and that cycle being a fixed vertex.
All other D-1 vertices may be transient to that vertex; D>=2 itself is not
an obstruction in the endomorphism class. Zero-clock graphs remain unrestricted.

When these conditions hold, the set of prime names in the parent and lift
is identical. All-prime coverage is still an extra condition, equivalent
between them in this regime, not a consequence of purity or uniqueness.
Outside the rational hypothesis the exact multiset formula still holds,
but the reduction to fixed cycles and prime parent multipliers is not
claimed. None of these conditional criteria supplies arithmetic naturalness,
a prime source, an analytic operator or Route credit.

## 8. Base control: the complete real doubling owner

Put a=log 2. The base T(x)=2x has inverse I(y)=y/2 on all R, with all-point
J=1/2 and every-Borel IMAGE for dx. Thus kappa_T=a. For every k in Z,
T^k x=2^k x, and the complete base arrows are

    (2^(-k)w,k,w),      c_T=k a,      w in R, k in Z.

Lag, clock and joint kernels are units. The only periodic point is 0,
with least period one and singleton full incoming packet; there source
isotropy is Z, entire H=a Z, extension isotropy zero, phases h modulo a,
and primitive a with all positive integer repeats.

Each nonzero complete source packet has unique labels epsilon in {+1,-1}
and r in [1,2), with states x_n=epsilon 2^n r, n in Z. It has source and
extension isotropy zero, H={0}, and complete real phase h+n a. All positive
and negative real states and all signed inverse depths are included.
There are no terminals and no other eventual cores.

## 9. Control A: identity sheets, with both full packets retained

F_A(x,e)=(2x,e) on R x {0,1}. Each source-sheet branch has inverse
(y,f)->(y/2,f), on all real y in the matching target sheet. Its product-
measure all-point IMAGE factor is 1/2 and kappa_A=a. All signed iterates
are (2^n x,e), n in Z. The complete arrows are

    ((2^(-k)w,f),k,(w,f)),       c_A=k a.

All three kernels are units. The states (0,0) and (0,1) are separate
fixed cores, each with singleton full incoming packet, source isotropy Z,
H=a Z, extension isotropy zero and phases h modulo a. Each contributes
primitive log 2 and all repeats. These are two distinct full packets of
the same prime length, so uniqueness fails; they cannot be merged by
choosing a preferred sheet or by identifying equal clocks.

For every nonzero parent packet epsilon,r and each fixed e, the lifted
packet is {(x_n,e):n in Z}. Its source/extension isotropy are zero, H={0},
and complete phase is h+n a. Its unique two-sided history keeps its sheet.
These formulas cover the full lift; there are no other cycles or incoming
branches, because the map is globally bijective and the parent nonzero
coordinates never return periodically or reach zero.

## 10. Control B: swap sheets and the actual two-step primitive

F_B(x,e)=(2x,e+1 modulo 2) is a bijection. Its inverse is
(y,f)->(y/2,f+1 modulo 2), with its own branch J=1/2 and kappa_B=a.
For all signed n, F_B^n(x,e)=(2^n x,e+n modulo 2), and all arrows are

    ((2^(-k)w,f+k modulo 2),k,(w,f)),       c_B=k a.

Again lag, clock and joint kernels are units. The whole zero-coordinate
packet consists of the two-state cycle (0,0)<->(0,1), with no other incoming
states. Its least source period is two, source isotropy 2 Z, entire H=2a Z,
extension isotropy zero, primitive 2a=log 4, and all positive integer repeats.
At sheet e the complete phase is h+e a modulo 2a. This is not a log-2
packet whose doubled traversal was accidentally called primitive: there
is no source loop of odd lag, and its entire clock subgroup is 2a Z.

For each nonzero parent packet epsilon,r, there are two full lifted packets
indexed by ell in {0,1}, with states

    (x_n,ell+n modulo 2),       n in Z.

The invariant sheet label is ell=e-n modulo 2. Each has all its positive
and negative histories, source/extension isotropy zero, H={0}, and complete
real phase h+n a. No additional periodic or eventually periodic states
occur. The one positive packet has nonprime primitive log 4, so purity fails.

## 11. Control C: collapse, merging kernels and every transient sheet

F_C(x,e)=(2x,0), total on both sheets. At every target (y,0) there are exactly
two actual inverse branches, (y/2,0) and (y/2,1); at (y,1) there is none.
Each branch separately has all-point J=1/2 and every-Borel IMAGE for
Lebesgue x counting. The sum of two preimage measures is not a substitute
branch Jacobian. Thus kappa_C=a at EVERY source in both sheets, including
(0,1), which has an outgoing step even though it has no predecessor.

The exact iterates are F_C^0(x,e)=(x,e) and

    F_C^n(x,e)=(2^n x,0),       n>=1.

For each n>=1 the full depth-n inverse set of (y,0) is
{(y/2^n,0),(y/2^n,1)}, whereas (y,1) has no inverse of positive depth.
There are not 2^n different source states or branch-word copies. An inverse
history that reaches a sheet-1 source cannot extend farther backward;
every infinite backward history ending in sheet0 stays on sheet0 throughout.
All finite sheet-1 branches remain present.

Because witnesses can be taken with both depths at least one, the ENTIRE
groupoid is

    {((z,e),k,(w,f)): w=2^k z, e,f in {0,1}, k in Z},
    c_C=k a.

At nonzero coordinates a related pair has a unique k. At zero, all k occur
for every pair of sheets. All three kernels coincide and are exactly

    {((x,e),0,(x,f)): x in R, e,f in {0,1}}.

For e!=f these are nonunit merging arrows, witnessed already after one
forward step. Having no one-step map predecessor is not the same as having
no incoming groupoid arrow through a common future. This distinction is
essential at sheet1 and no point is removed.

The only periodic core is the fixed point (0,0). The state (0,1) is not
fixed: it reaches that core in one step. Together they form the ENTIRE
zero-coordinate source packet, since no nonzero base point reaches zero.
Both states have source isotropy Z, entire H=a Z and extension isotropy
zero. In particular the transient (0,1) has nonzero source isotropy via
equal later forward times; it must not be assigned the isotropy of a
non-eventual state. Its phase can be taken as h modulo a in both sheets,
since their lag-zero merging arrow has zero clock. There is exactly one
positive packet, primitive log 2, with every positive integer repeat.

For every nonzero parent packet epsilon,r, its ENTIRE lift is one source
packet consisting of both (x_n,0) and (x_n,1), n in Z. Sheet0 forms the
bi-infinite forward chain; each sheet1 state has no predecessor and maps
to the next sheet0 state. All those finite incoming branches and all
sheet0 two-sided histories are retained. Arrows from (x_j,f) to (x_i,e)
have lag j-i and clock (j-i)a, for all e,f. Both isotropies and H are zero,
and the complete phase is h+n a at (x_n,e), independent of e. Zero-lag
merging identifies the equal-height sheet copies within this full packet.

Control C therefore meets the necessary nonempty/prime-pure/prime-unique
benchmark with one log-2 packet. It does not cover all primes and supplies
no endogenous arithmetic source. It exhibits the genuinely endomorphic
possibility allowed by Section7: one fixed cyclic vertex and a retained
transient vertex, rather than an omitted sheet or a permutation inverse.

## 12. Scope and raw conclusion

The full endomorphism lift owns its all-point inverse IMAGE and clock;
its full finite functional graphs, including transients, determine every
lifted cycle and incoming assignment over a parent periodic packet. The
least lifted periods are q r, cycle sums r C, entire stabilizers r C Z,
with exact kernel and real-phase descriptions on every full component.
No positive packet appears over a non-eventual or zero-clock parent class.
Phase invariance holds by a proved conjugacy of cyclic restrictions, not
by a false bijection of whole functional graphs.

Under the explicit rational-parent hypothesis, the combined necessary
prime benchmark is exactly the parent's benchmark plus one fixed return-
graph cycle per nonzero parent packet, all remaining fibre vertices allowed
to be transient. All three frozen controls have been completely treated,
including nonzero real points, null zero strata and merging sheets.

These are conditional structural results, not an admitted arithmetic
carrier or an extension of the rational theorem to irrational parents.
Strong naturalness and PROVES_TOO_MUCH remain OPEN. Classical N/A;
arithmetic T1 NOT PASSED; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.
No new candidate, other research round or later Route action is authorized.

After full self-read this is the pre-manuscript immutable raw checkpoint.
Any subsequent scientific correction requires an explicit erratum, not
rewriting after author exposure. Await root's full raw read and a distinct
PAPER UNLOCK; no author surface may be opened before it.
