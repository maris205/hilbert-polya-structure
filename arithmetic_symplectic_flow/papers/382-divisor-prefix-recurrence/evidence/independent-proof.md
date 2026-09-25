# 382 — Card-only independent derivation

Owner `ANG-20260922-DPR01`: full measured path/clock owner established;
**STOP target promotion: a primitive three-edge packet has least time log8.**

## 1. Input, authorization and method

- `candidate-card.md` — full 55 lines; SHA256 `c55f333215cbe53168f367db11f4fd24b315ee6ad4909b5545f51160ee6d6e7e`.

Root explicitly released mathematics after its full CP1 read. No manuscript,
peer/raw answer, scout, other new card/package or external source was read.
ARS instructions and prior shared-history source/clock familiarity are retained;
this is raw-card-separated, not blind/model-independent/external peer review.
Internal **NOT_CALIBRATED**; served model identity/effective reasoning setting
are not independently known. Exact constructions and finite identities only;
no numerical search, auxiliary agent, network, Git, PDF or model change.

## 2. MAIN closure and the complete inverse atlas

Write q(a,b)=a+b and tau(k)=the number of positive divisors of k.
If gcd(a,b)=1 and c=(a+b)/d with d dividing a+b, then c divides a+b;
therefore gcd(b,c)=1. Every frozen edge stays in S, with no discarded divisor.
Its outdegree is N(a,b)=tau(a+b), finite and >=2 because a+b>=2.
Taking d=1 forever constructs an infinite legal continuation from EVERY state.

For target (b,c) in S, the edge equation forces its source to be (dc-b,b).
It is positive exactly when dc>b. Since gcd(b,c)=1,

    gcd(dc-b,b)=gcd(dc,b)=gcd(d,b).

Thus d>=1, dc>b and gcd(d,b)=1 are necessary AND sufficient; d then divides
the source sum dc automatically. These are ALL labelled incoming edges.
Infinitely many exist at each target: choose d=1+kb sufficiently large.
For each such f:s->t, insertion I_f:X_t->[f] is a homeomorphism with inverse
T restricted to [f]. These cylinders exhaust the domain of T; every target
has a predecessor, so MAIN's T is onto. Full initial states and edge labels
are part of path equality, not auxiliary data later quotiented away.

## 3. Own probability, support, atoms and nonstationarity

For the coprime state set, 1/4<=C=sum_S 2^(-q(s))<=1, since (1,1) is present
and sum over ALL positive pairs is (sum_(a>=1)2^(-a))^2=1.
Hence eta(s)=2^(-q(s))/C is positive at every state and sums to one.
Selecting the initial state with law eta and choosing each enumerated outgoing
edge uniformly defines a Borel Markov path probability on the FULL carrier.
For a finite legal history u:s_0->...->s_m, including the empty history,

    Q(u)=product_(i<m)N(s_i),    mu([u])=eta(s_0)/Q(u).

Consistent cylinder probabilities define the conditional laws and their initial
mixture. Every cylinder is positive, so the support is all X. Since every
N(s_i)>=2, each path's length-m cylinder has mass <=eta(s_0)2^(-m).
All singleton paths, including every periodic and unbounded path, are null;
on this standard Borel path space the law is atomless. No null path is removed.

The frozen probability is NOT stationary. All predecessors of (1,1) are
(d-1,1) with label d>=2. Therefore

    mu(T^(-1)X_(1,1))=(1/C)sum_(d>=2)2^(-d)/tau(d)
                     <(1/(2C))sum_(d>=2)2^(-d)=1/(4C)=mu(X_(1,1)).

Strictness holds because tau(d)>=2 and tau(4)=3. This uses the entire
predecessor set, not a selected recurrent class or an invariant-law assumption.

## 4. Every-Borel full-point IMAGE, finite histories and full kernels

For EVERY Borel E subset X_t, conditional path factorization yields

    mu(I_f E)=eta(s)P_s(f)P_t^path(E)
             =[eta(s)/(N(s)eta(t))]mu(E),       f:s->t.

The identity on cylinders extends to all Borel sets by finite-measure uniqueness.
The frozen version is the constant j_f=2^(q(t)-q(s))/N(s), positive finite at
EVERY tail, including null ones, and is the exact ratio of full image cylinders.
For an outgoing divisor d and c=(a+b)/d,

    j_f=2^(c-a)/tau(a+b),    kappa_f=log tau(a+b)+(a-c)log2.

For example d=1 at (1,2) has kappa=-log2, whereas the (1,1) self-edge has
kappa=log2. The local clock is not a positive classical suspension roof.
Each actual inverse chart is nonsingular. In MAIN, the exhaustive positive
incoming charts also imply mu(E)=0 iff mu(T^(-1)E)=0.

For u:s->r set K(u)=2^(q(s))Q(u). The insertion density and summed clock are

    D(u)=eta(s)/(Q(u)eta(r))=2^(q(r))/K(u),
    C(u)=-log D(u)=log Q(u)+(q(s)-q(r))log2.

For gamma=(z,m-n,y), u=z|m and v=y|n have the SAME complete endpoint r.
On the ENTIRE v cylinder, replacement v w->u w has every-Borel IMAGE

    D(u)/D(v)=K(v)/K(u),     c(gamma)=log[K(u)/K(v)]=A_m(z)-A_n(y).

Appending a common tail multiplies both Q products by the same factor, so
these formulas do not depend on the witness m,n. Tail refinement proves
composition adds c; reversing the actual triple negates c. No free-word or
endpoint-only identification is made. The exact full kernel criteria are

    ker c: K(z|m)=K(y|n) with T^m z=T^n y;
    ker ell: (z,0,y) with T^N z=T^N y for some N>=0;
    intersection: T^N z=T^N y AND K(z|N)=K(y|N).

K is an explicit positive integer, including the initial-state weight factor.
These are necessary/sufficient tests on ALL arrows, not just isotropy or one
return word, and hold in every presentation. All actual lag labels remain.

## 5. Complete source/physical ledgers and primitive words

Every source orbit is precisely

    O_a={u T^n a:n>=0, u any finite legal path ending at start(T^n a)}.

This retains every compatible initial state and incoming prefix. A nonzero
source isotropy lag occurs exactly for an eventually periodic FULL state-edge
path. If its least eventual edge period is l, all equality differences are
multiples of l and every multiple occurs beyond the transient prefix. Thus
ENTIRE source isotropy is lZ; for every other path it is {0}.

For a primitive closed state-edge word w=(s_i,f_i) of length l, cancellation
of the endpoint q terms gives

    L(w)=sum_(i<l)log N(s_i)=log product_(i<l)N(s_i)>=l log2>0.

Consequently c(x,kl,x)=kL(w) even with an arbitrary finite transient prefix.
The ENTIRE clock image is H_x=L(w)Z, and the full real extension has trivial
isotropy. At aperiodic paths H_x={0} and extension isotropy is also trivial.
These statements apply to MAIN and the two branching controls below; the
deterministic NO-DIVISION case is proved separately, not forced into N>=2.

Keep all X times R and arrows (y,h)->(z,h+c). For any reference a in a source
orbit and actual g:y->a, phase h+c(g) modulo H_a is complete: choices differ
by exactly H_a, and equal phases supply a connecting arrow after an isotropy
correction. The quotient over that orbit is the SET R/H_a; height translation
is a complete R-action with entire stabilizer H_a. No quotient topology,
smoothness, invariant physical-flow measure or positive-roof structure is inferred.
For a core a and y=u T^j a, its phase is h-C(u)+A_j(a) modulo L(w).
For an aperiodic reference the same formula (with any n) is real and independent
of the witness. Every height and incoming path is retained, not a chosen section.

ALL primitive closed state-edge necklaces, modulo cyclic rotation, give exactly
one physical packet each, of least time L(w). Proper powers are only repetitions,
with times kL(w). Distinct primitive necklaces cannot share an eventual tail;
equal numerical times do not merge packets. Conversely every positive return
requires source isotropy, so this exhausts all packets, including those not
based at (1,1). Return of a finite pair alone is not full-path isotropy.

## 6. Both precommitted MAIN tests, with full return groups

The d=2 self-edge at (1,1) has N=2, least source period 1 and kappa=log2.
Its whole source isotropy is Z, H=(log2)Z and extension isotropy is trivial.
Every legal prefix ending at (1,1), followed by its constant core, is incoming;
relative phase is h-C(u) modulo log2, with all heights and repetitions retained.

The second frozen word visits (1,1),(1,2),(2,1) with labels 1,3,3.
All three transitions are legal and the distinct full states force least
source period 3. Their outdegrees are tau(2),tau(3),tau(3)=2,2,2, so

    L=log8,     entire source isotropy=3Z,     ENTIRE H=(log8)Z.

The three local clock values are 0, log2 and 2log2; their sum is log8.
Relative to the (1,1) phase a, the three source phases have offsets
A_0(a)=0, A_1(a)=0 and A_2(a)=log2 modulo log8. All incoming are
u T^j a, j=0,1,2, with every legal u ending at that core state, and phase
h-C(u)+A_j(a). All starting states can reach (1,1) by two maximal-divisor
steps (a,b)->(b,1)->(1,1), so every initial state occurs among incoming paths.
This does not say all paths enter the core: always-d=1 paths have strictly
increasing pair sums and are aperiodic. All other legal incoming histories remain.
Its repetitions are k log8 and extension isotropy is trivial.
This is one primitive packet of wrong least time, not three copies or a
repetition of the distinct self-edge packet. The two infinite core words are
not tail-equivalent even though their finite graph vertex (1,1) is shared.
Since 8 is composite, the frozen primitive prime-time target fails.

## 7. NO-DIVISION — full deterministic, atomic, nonreturning owner

Here S is independently the coprime set, N(s)=1 and F(a,b)=(b,a+b).
Closure follows from gcd(b,a+b)=1. Its only possible predecessor of (b,c)
is (c-b,b), present exactly when c>b. T is not onto; initial components
with c<=b remain in the full carrier. Each s owns exactly one infinite path,
so the independently normalized eta yields a purely atomic law of mass eta(s)
on that path, with full support. This is not inherited atomlessness from MAIN.
It is not stationary: X_(1,1) has positive mass and no predecessor.
Every actual chart has j=2^b on the edge from (a,b), and kappa=-b log2.
All every-Borel/finite-history formulas above apply with Q=1 and K=2^(q(start)).

F is injective and q(Fs)=q(s)+b>q(s). Its partial inverse decreases the
positive integer sum, so every backward chain ends at a unique r=(a,b) with
b<=a. Each entire source orbit is the ray {F^j r:j>=0}. If y has index i
and z index j on that ray, the unique arrow has lag i-j and clock
(q(z)-q(y))log2. Strict growth of q on the ray proves clock kernel, lag kernel
and their intersection are ALL just units. Source and extension isotropy are
trivial, H={0}, and every full source orbit has real phase h-q(s)log2.
Every ray state is retained in this groupoid incoming/orbit ledger, including
later states beyond the finite literal-predecessor chain. There are NO directed
closed walks, no eventually periodic paths and no positive physical packets.
This is a defined full clock with source nonreturn, NOT an undefined clock.

## 8. END-DIVISORS — independently rebuilt binary branching owner

The own coprime state set and weights give its own C and eta (numerically the
same initial distribution because that set and formula are unchanged). Both
legal labels 1 and a+b are distinct; N(s)=2 at every state. The two maps
are (a,b)->(b,a+b) and (a,b)->(b,1), so closure is exact. Own path probabilities
use 1/2 per edge; all cylinders are positive and all singletons null.
At target (b,c), ALL incoming edges are exactly these two disjoint cases:

    c>b: source (c-b,b), label 1;
    c=1: source (d-b,b), label d>b with gcd(d,b)=1.

No other target has a predecessor: the maximal-divisor equation d=dc forces
c=1. For example (3,2) remains a positive-mass initial component with no
predecessor, so T is not onto and the law is not stationary. Local charts
nevertheless have valid own positive j=2^(q(t)-q(s)-1) at every tail and
every-Borel IMAGE. MAIN's global two-way shift null-set equivalence is NOT
asserted here or for NO-DIVISION; their individual chart laws remain nonsingular.
The finite-history invariant is explicitly K(u)=2^(q(start(u))+|u|).
Thus ker c has q(start z)+m=q(start y)+n on actual triples; lag kernel
has m=n, and intersection also requires equal starting sums.
The full source, incoming, isotropy, extension and phase construction in section 5
applies with this OWN graph and L(w)=|w|log2 to EVERY primitive closed necklace.
Its d=2 self-packet has entire H=log2 Z, and its distinct primitive 1,3,3
packet has entire H=log8 Z. All source phases/incoming and repetitions remain
with the phase formula above. It too fails the target, without repairing MAIN.

## 9. ALL-PAIRS — no coprime condition may be imported

Here S is ALL positive pairs, C=1 exactly, eta=2^(-a-b), N(s)=tau(a+b).
Every allowed divisor gives a positive target, so closure needs no gcd test.
At arbitrary (b,c), the COMPLETE inverse list is (dc-b,b), label d>=1 with
dc>b, with NO restriction on gcd(d,b) or gcd(b,c). This proves sufficiency
and necessity anew and makes T onto. All labels, including noncoprime ones,
remain in the carrier. Own cylinder probabilities construct the full-support
atomless law; the strict calculation at X_(1,1) in section 3 applies with
C=1 and proves nonstationarity for this law too.
Own j, integer K, full clock/lag kernels/intersection and every-Borel IMAGE
are exactly section 4 with this larger S and its OWN eta/transition law.
Every primitive closed state-edge necklace has least L=log product tau(q(s)),
entire source isotropy |w|Z, H=LZ, trivial extension isotropy and ALL incoming,
phases and repetitions from section 5. Aperiodic paths instead have H={0}.
In particular EVERY n>=1 gives a distinct d=2 self-packet at (n,n), source
period 1 and H=log(tau(2n)) Z. Coincident divisor counts do not identify these
different constant tails. At n=3 this is a primitive log4 packet, already wrong;
the original three-edge word also independently retains its primitive log8.
No control time, null path or source label is transferred into MAIN.

## 10. Closure and claim boundary

Every frozen MAIN obligation and all three own-control ledgers are established
or explicitly classified as source nonreturn. None of these four clocks is
undefined. MAIN's full owner survives, but target promotion stops on log8.
No rescaling, exceptional-path removal, endpoint identification or chosen
recurrent subgraph repairs this ID. Countable Markov state ownership remains
explicit; prefix dependence is not a proved escape from graph-word splicing,
free-block mechanisms or all Markov models. Strong naturalness remains OPEN.
Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED; T3 NOT AUDITED.
Only this raw proof was written; no main-paper unlock or further route is assumed.
EOF — freeze for root's complete read; manuscript remains locked pending release.
