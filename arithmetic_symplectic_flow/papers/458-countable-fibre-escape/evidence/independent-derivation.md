# CFE01 — frozen card-only independent derivation

Candidate: ANG-AUDIT-20260924-CFE01. Paper458.
Reviewer: `/root/rcr01_independent_review`, 2026-09-24 UTC.
Status: RAW; freeze before author-manuscript access.

## 0. Input and execution boundary

The scientific input is only the original candidate card,95 lines,
FULL reread1–95/EOF after DISTINCT RAW RELEASE, SHA-256
`dbd87a7aa72060f50017529186d3a89026dde39686fa5e7894dea7f2b7a3d53f`.
Root reported its FULL read of the118-line CP1 PASS, whose SHA is
`2fb7ab068103c109df5e073658c2a807895de87231cf00d5d625d1befc3ced1e`.
No author paper, README, ledger, appended Outcome, helper or peer proof,
old scientific file or other current-batch card was read for this derivation.

The staged ARS original-mathematics adaptation and instruction receipts are
recorded at CP1. This is same-model/shared-root-history internal AI work,
NOT_CALIBRATED, not blind, human, external, cross-model or independent-error
validation. Card-disclosed informal design expectations and inherited
history are not preregistration. No scientific program, numerical census,
network, Git, PDF, operator/zero work or old-file edit is used below.

## 1. The lift owns its inverse IMAGE and clock

Write E_i=T(P_i), and let nu=mu times counting on Y=X times N_0.
The product is standard Borel and nu is sigma-finite. For each i,e,f put

    D_ief={(x,e): x in P_i, sigma(x,e)=f},
    A_ief={y in E_i: sigma(I_i y,e)=f}.

These sets are Borel. The countable collection D_ief is disjoint and covers
Y: each (x,e) has exactly one parent branch index and one output fibre f.
On D_ief, F is injective; its image is A_ief times {f}, and its inverse is
theta_ief(y,f)=(I_i y,e). This is an actual inverse on the whole actual image.
Empty pieces can be omitted. Noninjectivity between different pieces is
retained as different inverse branches, not erased by a chosen predecessor.

For any Borel B contained in A_ief times {f}, write
B=B_f times {f}. The parent IMAGE identity gives

    nu(theta_ief B)=mu(I_i B_f)
                  =integral_(B_f) J_i(y) dmu(y)
                  =integral_B J_i(y) dnu(y,f).

Thus each own inverse density is the prescribed J_i(y), at every point of
that branch image. No sum over other e or i enters this identity or its
logarithm. The all-point version includes measure-zero objects as frozen
data; the measure identity alone would not determine values there.
Consequently the lift's own outgoing clock is

    kappa_F(x,e)=kappa_T(x).

This is a signed Borel clock, not an assumed positive roof. F is total even
at objects with no predecessors; those objects are not terminals.

## 2. Ordered fibre transport and every incoming depth

Define maps on N_0 recursively by

    Q_0(x)(e)=e,
    Q_(n+1)(x)(e)=sigma(T^n x,Q_n(x)(e)).

Thus Q_n is the ordered composition along the ACTUAL base history, and

    F^n(x,e)=(T^n x,Q_n(x)(e)),
    Q_(m+n)(x)=Q_n(T^m x) composed with Q_m(x),
    S_n^F(x,e)=S_n^T(x).

All these expressions are Borel and hold pointwise for every n>=0.
The exact depth-n inverse set of (y,f) is

    {(x,e): x in T^(-n){y}, e in N_0, Q_n(x)(e)=f}.        (1)

The parent set T^(-n){y} is supplied by all actual inverse words of length n,
with all intermediate branch-domain guards. Every such word is injective on
its actual source itinerary. Its density is the product of its successive
J_i values, proved by repeated weighted substitution. To justify weighted
substitution from the assumed IMAGE identity, first use indicator functions,
then nonnegative simple functions and monotone approximation. Applying the
same argument to the lift pieces gives the identical product along x.

Conversely every point in (1) gives its actual parent itinerary and fibre
history, hence appears in that complete branch construction. The index set
is countable for each n; the inverse set may be countably infinite. No finite
cutoff, uniform predecessor bound or full-map injectivity is assumed. Formula
(1), for all n, retains all incoming depths and their actual multiplicity.

## 3. Both groupoids, cocycles, kernels and extension phases

For U=T or F, retain exactly the triples (z,k,w) having some witness
m,n>=0 with k=m-n and U^m z=U^n w. Distinct witnesses of the same triple
are identified; different integer lags remain different arrows.

If two witnesses have the same lag, one is a simultaneous nonnegative
advance of the other. Their common meeting state has the same subsequent
clock on both sides, so S_m(z)-S_n(w) is independent of the witness.
For composable arrows with witnesses (m,n) and (p,s), advance to the
common middle depth n+p. The composite has witness (m+p,s+n).
The identity S_(n+p)(w)=S_n(w)+S_p(U^n w)
                       =S_p(w)+S_n(U^p w)
then proves additivity of c. Inversion changes its sign; units have c=0.
In particular (Uz,-1,z) has clock -kappa_U(z), not plus kappa_U(z).

For F the complete arrow criterion is

    ((x,e),k,(y,f)) exists iff there are m,n>=0 with
    k=m-n, T^m x=T^n y, Q_m(x)(e)=Q_n(y)(f).              (2)
    c_F=S_m^T(x)-S_n^T(y).

Projection of (2) is a parent arrow (x,k,y), and c_F is its parent clock.
This projection need not provide every arrow between prescribed lift
endpoints. Equality of the transported fibre states is essential.
For either owner, the exact three kernels are all its actual arrows with,
respectively, k=0, c=0, or both. For F, (2) plus those equations is already
a full-history description, not only a core-level criterion.

The extension arrow acts by (w,h)->(z,h+c); physical translation adds an
arbitrary real t to every height. At a source object z the source isotropy
is G_z^z, its entire clock image is H_z=c(G_z^z), and extension isotropy is
the subgroup of G_z^z with clock0. Source isotropy is not identified with H.

For completeness, fix a reference object b in one source class and choose
an actual arrow b->z for each z, with clock B_z. For any arrow w->z, its
clock differs from B_z-B_w by an element of H_b; conversely composing with
isotropy realizes every such element. Extension orbits are therefore exactly

    (h-B_z) modulo H_b.                                  (3)

Changing the chosen arrows changes B_z by H_b only. Every real height is
present. Physical translation is transitive on R/H_b and has stabilizer
H_b. These are set-level statements; no measurable selector or quotient
regularity is claimed. Below H is either0 or a cyclic subgroup of R.
Only H=L Z with L>0 gives positive primitive L and all repetitions nL,
n>=1. H=0 gives real phases and no positive physical primitive, even when
nontrivial zero-clock source isotropy survives in the extension.

## 4. Complete parent classification and non-eventual lift classes

A total deterministic forward history either eventually repeats or never
repeats. If a source class contains an eventual cycle, every point of that
class enters that same cycle: its forward history meets one already doing
so. Otherwise all forward histories in the class never repeat.

In a non-eventual parent class, source isotropy is0. Indeed a nonzero-lag
self-arrow would give two equal iterates and hence an eventual cycle.
There is consequently a unique parent arrow between any ordered pair in
that class. Fix b and let d(x),B(x) be the lag and clock of b->x. Then
every pair arrow is

    (x,d(x)-d(y),y), c=B(x)-B(y),
    d(Tx)=d(x)-1, B(Tx)=B(x)-kappa_T(x).                  (4)

All three parent kernels are the equal-d, equal-B and joint relations.
Source/extension isotropy and H are0; every phase is h-B(x) in R.

Above this class, lift endpoints are related precisely by (2). Their only
possible lag is d(x)-d(y) and their clock, if an arrow exists, is B(x)-B(y).
Thus each actual lift class retains the corresponding restrictions of the
three relations in (4). Every one of its source/extension isotropy groups
and H is0, with phase h-B(x) in R. Fibre recurrence cannot manufacture
nonzero lag isotropy over a non-eventual parent. Formula (2) supplies the
full lift-class partition and all incoming merges, without assuming that
the fibre maps themselves are injective, recurrent or independent of x.

Now let a parent core have least period q, write v_j=T^j v_0 and let
C=S_q^T(v_0), with no restriction on its sign or whether it vanishes.
For every x in its complete basin, let n_x be first core-entry depth and
j_x its entry index. Put rho_j=(-j mod q) in {0,...,q-1} and define

    N_x=n_x+rho_(j_x), D_x=S_(N_x)^T(x).

Thus T^(N_x)x=v_0. It is harmless that this need not be first entry into
the core: it is the first specified arrival at the reference phase.
Advancing any two meeting histories far enough to phase v_0 proves that
the complete parent arrows in this basin are exactly

    k=N_x-N_y+q a, c=D_x-D_y+a C, a in Z.                (5)

Conversely any integer a is realized by sufficiently large nonnegative
numbers of additional q-step circuits on the two sides. Thus parent
source isotropy is q Z, H=C Z, and extension isotropy is0 for C nonzero
or q Z for C=0. The kernels are (5) with k=0, c=0, or both. All phases
are h-D_x modulo C Z, interpreted as real phases when C=0. The positive
primitive is abs C precisely when C is nonzero. Every incoming parent
tail is included in N_x and D_x, not replaced by its core representative.

## 5. Exact reduction over a parent core to a countable return graph

At v_0 define the actual return endomorphism

    Pi=Q_q(v_0): N_0->N_0.

For z=(x,e) above its full parent basin set a_z=Q_(N_x)(x)(e).
Then F^(N_x)z=(v_0,a_z). For w=(y,f), formula (2) is equivalent to

    there are u,v>=0 with Pi^u a_z=Pi^v a_w,
    k=N_x-N_y+q(u-v),
    c=D_x-D_y+(u-v)C.                                  (6)

To prove necessity, advance an actual meeting far enough that both paths
have passed their chosen N times and that their common base state is v_0.
The added times past those N values are multiples of q. Sufficiency is the
displayed common return state itself. The clock formula is valid because
each q-step return traverses the same parent core once, independently of
the fibre itinerary. Formula (6) includes arbitrarily deep parent tails
and all their ordered fibre transports, not just points above v_0.

Define a~b in N_0 iff Pi^u a=Pi^v b for some u,v>=0. This is an equivalence
relation (common further advances prove transitivity). The complete lift
classes over this parent basin are exactly its ~ classes pulled back by
z->a_z. Every such class occurs, since (v_0,a) realizes any a in N_0.
All incoming histories still have the more precise depth formula (1).

Each ~ class either contains one finite directed cycle, with all its
points eventually entering that cycle, or contains no repeat at all.
The assertion follows directly from determinism: any repeat is a cycle,
and meeting histories eventually share its future. The second alternative
cannot be removed merely because the fibre set is countable.

## 6. Finite return cycles, complete basins and phase invariance

Let O be a Pi cycle of least length d, enumerate it e_s=Pi^s e_0,
s=0,...,d-1. The orbit of (v_0,e_0) under F is a cycle of least length qd.
It returns after qd steps. Any return time must be a multiple of q because
the parent has least period q, and its quotient by q must be a return time
of e_0 under Pi. Therefore no smaller positive return exists.

Conversely every F-periodic point projects to a parent periodic point.
Advancing it to phase v_0 gives a Pi-periodic point. This establishes a
bijection between finite Pi cycles and F cores over the chosen parent core.
Different Pi cycles do not merge into one F core. The FULL basin of the
core corresponding to O is

    {z: a_z eventually enters O}
    = union_(n>=0) F^(-n){all qd points of that F core}.  (7)

The equality is both directions of the actual forward transport, so it
includes every parent incoming tail, all fibre predecessors, and all
core phases. It does not assume injectivity of transient fibre transport.

For an a in the Pi basin of O, let delta(a) be first entry depth and s(a)
the entered cycle index. Put eta(a)=delta(a)-s(a). The complete Pi lags
between a and b are eta(a)-eta(b)+d t, t in Z: necessity follows by
comparing sufficiently advanced cycle positions, and sufficiency by
advancing far enough to realize any such difference with nonnegative times.
For z=(x,e) in (7), define

    L_z=N_x+q eta(a_z), V_z=D_x+C eta(a_z).

Substitution in (6) gives every lift arrow in that basin:

    k=L_z-L_w+qd t,
    c=V_z-V_w+dC t, t in Z.                            (8)

The lag/clock/joint kernels are exactly (8) with k=0, c=0, or both.
In particular these formulas include zero-clock arrows between different
objects and the ineffective source isotropy when C=0. At EVERY object in
the basin, not only at the periodic core,

    source isotropy=qd Z, H=dC Z,
    extension isotropy=0 if C!=0, or qd Z if C=0.

Every extension phase is h-V_z modulo dC Z. If C!=0, this one full packet
has primitive d abs C and every repetition n d abs C. If C=0, the phase
is real and there is no positive primitive; source isotropy remains qd Z.
No division by q,d or an incoming depth is made to the entire group H.

Reference-phase changes preserve the finite-cycle accounting. To see this
without assuming transient bijectivity, let A be one step from phase j to
j+1 and B the remaining q-1 steps back. The return maps are Pi_j=BA and
Pi_(j+1)=AB. The identity A Pi_j=Pi_(j+1) A maps finite cycles forward.
On the union of finite cycles A is injective: A a=A b gives Pi_j a=Pi_j b,
and Pi_j is bijective on that periodic set. The image of a d-cycle has
least period d, since a shorter image period would, after applying B,
be a shorter period on the original cycle. Every target periodic point b
of period d has preimage B Pi_(j+1)^(d-1)b, itself periodic, under A.
Thus finite cycles correspond bijectively, with lengths unchanged.

The signed parent sum C is unchanged by cyclic reindexing; the qd lift
cycle and full basin are intrinsic to F. The packet, H and all phases
are therefore unchanged. No bijection of all transient or escaping fibre
states follows, and none is used. The argument also covers q=1, with B
the identity and the same periodic-set restriction.

## 7. Escaping return components are retained, with complete kernels

In an acyclic ~ class of Pi, every forward orbit never repeats. Fix one
a_* in the class. There is a unique integer b(a)=u-v for a meeting
Pi^u a=Pi^v a_*. If two different lags existed, advancing their witnesses
would give an eventual repeat, contrary to acyclicity. Accordingly all
Pi pair lags are b(a)-b(b), and b(Pi a)=b(a)-1.

For a lift point z=(x,e) whose a_z is in this class, put

    L_z=N_x+q b(a_z), V_z=D_x+C b(a_z).

Equation (6) becomes the unique-arrow formula

    k=L_z-L_w, c=V_z-V_w.                              (9)

Thus the three kernels are equal-L, equal-V and their intersection.
Source and extension isotropy and H are all0, even if the parent core has
nonzero C. Every real phase h-V_z remains. These are nonperiodic lift
source classes over an eventual parent class, with all objects and all
incoming histories retained through (1), (6) and the pullback partition.
They are not positive packets and are not omitted as irrelevant states.

Together §§4–7 cover every parent source class and every lift object.
They do not use the false inference that a countable functional graph
must eventually reach a cycle. They also require no measurable choice of
one reference per source class: all choices above merely express the
intrinsic classes and cocycle relations already defined by actual arrows.

## 8. Exact rational-parent benchmark criterion

Let Q denote a parent core, with least period q_Q and signed sum C_Q.
Choose one phase only for graph accounting; no global Borel selector is
claimed. Each finite cycle O of its actual return map Pi_Q contributes
one lift packet. For C_Q!=0 its positive primitive is

    len(O) abs C_Q = log(a_Q^(len(O))),
    a_Q=exp(abs C_Q).

There are no other positive packets, by the complete classification.
Assume the card's rational hypothesis: every a_Q for C_Q!=0 is rational>1.
For reduced a=A/B>1 and integer d>=1, if a^d is an ordinary prime p then
A^d=p B^d and coprimality forces B=1. Then A^d=p forces d=1 and A=p.
Conversely a=p and d=1 clearly gives primitive log p.

Consequently the card's three-clause benchmark holds if and only if:

1. There is at least one finite Pi_Q cycle with C_Q!=0.
2. For every Q with C_Q!=0, either Pi_Q has no finite cycles, or a_Q is an
   ordinary prime and EVERY finite Pi_Q cycle is a fixed point.
3. For each ordinary prime p, the set of pairs (Q,e) with C_Q!=0,
   a_Q=p and Pi_Q(e)=e has cardinality at most one.

Necessity follows by applying prime purity to each positive packet and
then counting distinct packets, not distinct lengths. Sufficiency follows
because (1) supplies a positive packet, (2) makes all such packets prime
with d=1, and (3) gives global multiplicity at most one. Parent cores with
C_Q=0 may have arbitrary finite cycles and escaping components: their
isotropy is retained but they contribute no positive primitive. All-prime
coverage would separately require the set in (3) to have cardinality one
for every prime. It is not part of the proved three-clause equivalence.

These are conditions on a GIVEN Borel lift, not a claim that arbitrary
independent graph prescriptions over all parent classes admit a Borel
realization. Finite nonempty fibres force a cycle by repetition among
finitely many iterates. N_0 does not: the allowed map e->e+1 has none.
Hence a nonprime parent multiplier can have a cycle-free return graph
without removing its objects, and finite-fibre conclusions needing a cycle
in every return graph do not extend on that premise. Escape alone also
does not ensure benchmark nonemptiness, as control A checks below.

For irrational a_Q the correct packet multiplier is still a_Q^d, but the
rational factorization implication is not available. No rational conclusion
above is asserted for that class. Even meeting these graph conditions is
not an endogenous arithmetic mechanism: sigma is freely chosen in this
audit, and naturalness remains OPEN.

## 9. Common parent of the three controls: full real doubling

Put lambda=log2. On X=R with Lebesgue measure, T(x)=2x is a total Borel
bijection with actual inverse y/2. For every Borel E,
Leb(E/2)=(1/2)Leb(E), so own J=1/2 at every point and kappa_T=lambda.
All depth-n predecessors are the singleton {y/2^n}; T^n x=2^n x.
The complete arrows are

    (2^(-k)y,k,y), k in Z, with c=k lambda.

All three kernels are units. At0 there is one fixed core, its complete
basin is {0}, source isotropy Z, H=lambda Z, extension isotropy0 and
phase h modulo lambda Z. Its one positive primitive is lambda, with all
positive integer repetitions. No nonzero real point enters that basin.

Every nonzero source class is {epsilon 2^n v:n in Z}, uniquely described
by epsilon in{+1,-1} and v in[1,2). Source/extension isotropy and H are0,
and the real phase is h+log(abs x). This includes both real half-lines
and every geometric iterate. These parent data are owned by this map and
are not a prime-arithmetic discovery from its prescribed coefficient2.

For each lifted control below, a branch at input sheet e has one fixed
target sheet f. Any Borel subset of that image has own inverse measure
Leb(E/2)=(1/2)Leb(E) in its source sheet. Thus EVERY inverse branch has
J_F=1/2, kappa_F=lambda, including the null states x=0. We enumerate all
such branches separately below; their densities are never summed before
taking the clock. All three product measures are the original Lebesgue
times counting on the entire R times N_0, with no selected fibre.

## 10. Control A: sigma(e)=e+1, complete escaping rays

F_A(x,e)=(2x,e+1). The source sheet e maps injectively onto the entire
sheet e+1, with inverse (y,e+1)->(y/2,e) and own density1/2. These are
all inverse branches. Sheet0 has no predecessors but remains a full set
of sources with infinite forward histories, not a terminal boundary.

    F_A^n(x,e)=(2^n x,e+n).
    F_A^(-n){(y,f)}={(y/2^n,f-n)} if f>=n, and empty otherwise.

The fibre meeting equation forces k=f-e; the base equation then gives
x=2^(e-f)y. Conversely these equations are realized by taking sufficiently
large nonnegative witness times. Thus complete arrows from(y,f) to(x,e) are

    k=f-e, x=2^(e-f)y, c=(f-e)lambda.                   (10)

The full source classes are indexed by xi=2^(-e)x in R:

    C_xi={(2^e xi,e):e in N_0}.

This includes xi=0 and both signs of xi. Every class is an injective ray
with its initial source at sheet0; all predecessors of a state are given
at exactly the allowed depths above. The lag, clock and joint kernels are
units, since zero k forces e=f and then x=y. Source/extension isotropy and
H are0 on EVERY class. All real phases are h+e lambda. On nonzero rays
one may instead use h+log(abs x), differing by the class constant log(abs xi).

At the parent fixed core, Pi(e)=e+1 has no finite cycles. There are no
positive lift packets or positive repetitions anywhere. Parent recurrence
has not been transferred to a hidden periodic fibre, nor has the escaping
zero ray been discarded. This fails benchmark nonemptiness, while proving
directly that countable return graphs need not contain a cycle.

## 11. Control B: sigma(e)=max(e-1,0), all collapsing histories

F_B(x,e)=(2x,(e-1)_+). Its complete one-step inverses at (y,f) are

    (y/2,0) and (y/2,1) if f=0;
    (y/2,f+1) if f>=1.

Each arises from its own entire source sheet and has density1/2 by the
every-Borel substitution above. The two inverse branches at target sheet0
must not be summed into a derivative1 and assigned clock0. The actual
branch clocks remain lambda, including at all zero-base states.

    F_B^n(x,e)=(2^n x,(e-n)_+).
    F_B^(-n){(y,f)}={(y/2^n,f+n)} if f>=1;
    F_B^(-n){(y,0)}={(y/2^n,e):0<=e<=n}.

Thus the fixed-depth inverse set over sheet0 has exactly n+1 points, not
countably infinitely many at a single fixed n. At base0, the union over
all depths is the countable set {(0,e):e in N_0}. At nonzero y, the same
formulas retain the differing geometric base predecessors at every depth.

For any two fibre indices, both can be made0 by sufficiently large witness
times while preserving any prescribed integer lag. The complete arrows are

    ((x,e),k,(y,f)) iff x=2^(-k)y,
    with arbitrary e,f in N_0 and c=k lambda.            (11)

Every parent-arrow witness can be advanced until its two fibre histories
have collapsed; this proves sufficiency, not merely a selected-zero-sheet
description. The lag, clock and joint kernels all equal

    {((x,e),0,(x,f)): x in R, e,f in N_0}.

They are full vertical pair relations, not only units. At nonzero base,
each source class is {epsilon 2^n v:n in Z} times N_0, with epsilon and
v as in §9. Source/extension isotropy and H are0, and every real phase is
h+log(abs x), independent of the fibre index. Every real nonzero state and
all its merging fibre histories are retained in this description.

At base0 there is ONE source class {(0,e):e in N_0}, with fixed core(0,0).
The first entry time from(0,e) is e. All its objects have source isotropy Z,
H=lambda Z and extension isotropy0, including those not themselves periodic.
Every extension phase is h modulo lambda Z; the first-entry expression
h-e lambda is equivalent. The entire class is one full positive packet,
primitive log2 with all repetitions n log2, n>=1.

The actual Pi has exactly one fixed point and every other state eventually
enters it. Hence this control meets the three-clause benchmark, but not
all-prime coverage. It is an EXTERNAL CONTROL with chosen coefficient2 and
chosen fibre dynamics, not an endogenous prime generator. Its positive
packet was not obtained by deleting any sheet or nonzero real state.

## 12. Control C: sigma(e)=e, countably many full packets

F_C(x,e)=(2x,e) is bijective, with actual inverse (y,f)->(y/2,f) on each
sheet and own every-Borel density1/2. At every depth,

    F_C^n(x,e)=(2^n x,e),
    F_C^(-n){(y,f)}={(y/2^n,f)}.

Complete arrows have x=2^(-k)y, e=f and c=k lambda. All three kernels
are units. For every nonzero parent geometric class and each fixed e,
there is one complete lift class at that sheet, with source/extension
isotropy and H equal0 and all real phases h+log(abs x).

Each (0,e) is its own fixed core and full source class; no nonzero or
other-sheet state enters it. At every one, source isotropy is Z,
H=lambda Z, extension isotropy0 and phase h modulo lambda Z. There is
one full primitive-log2 packet for EACH e in N_0, with all positive
integer repetitions. The set of distinct packets is countably infinite,
not a single packet merely because their primitive lengths coincide.
This violates multiplicity one, while remaining nonempty and prime-pure.

## 13. Scope disposition and freeze

The exact result is the complete countable return-graph classification,
including acyclic components and arbitrary incoming parent tails, together
with the stated necessary/sufficient rational benchmark conditions. The
three controls respectively test empty recurrence, one complete packet
with all collapsing states, and countably many identical-length packets.
They are separate full owners on their stated measures, not selected
sections of each other or components silently borrowed into a new object.

No classical symplectic suspension, natural prime-symbolic admission,
operator, trace or zeta is constructed. The conditional symbolic-memory
to full measured lift audit does not turn freely chosen sigma into an
endogenous arithmetic mechanism. Arithmetic T1 remains NOT PASSED;
classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.
Portfolio disposition: FORK after retaining this scoped transport/filter
result; a natural arithmetic source would require a new authorized contract.

Freeze this raw before author-file access. RAW READY sends only path, line
count and SHA, not the mathematical outcomes above. Any later discovered
error must be recorded separately, not silently rewritten after exposure.
Root FULL raw reading and a DISTINCT PAPER UNLOCK are required before
comparison with the four final author surfaces. No round460 is authorized.
