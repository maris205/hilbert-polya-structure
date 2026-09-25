# 377 — Raw-card independent derivation

Owner `ANG-20260922-PCS01`: full measured source/real clock owned;
**STOP promotion: an intrinsic primitive time lies strictly between log2 and log3.**

## 1. Inputs, method and exposure

Only scientific input read: `candidate-card.md`, all 81 lines through EOF;
SHA256 `de295c4060e55678d98ac8239a110588ad278c0a07a09b713f45aa81c0d2a8e6`.
Root released mathematics after reading CP1. No main manuscript, peer/scout,
375+ paper or other new scientific material was read. Earlier shared-history
source/clock reasoning is retained: this is not blind/model-independent review.
ARS instructions retained; internal **NOT_CALIBRATED**, not external peer review.
Served model identity/effective reasoning setting are not independently known.
Exact symbolic constructions and integral bounds only; no numerical experiment,
auxiliary agent, external source, network, Git, PDF or model change.

## 2. Four separate graph-law constructions and full measure

The following lemma is proved for each of the four OWN graphs, not by importing
MAIN's transitions. Write U_s=sum_(n in A(s))rho(n), with each graph's legal A.
Since rho(n)=1/(n-1)-1/n, sum_(n>=2)rho(n)=1. At e, U_e=Z_e=1.
At nonempty states Z_s=1+U_s, with 0<=U_s<=1. For MAIN, the integers
1+k product_(n in s)n are legal for every k>=1, so U_s>0 at every finite s.
TOP-ONLY has the same argument using just the top entry; OFF allows all n.
DEPTH-ONE has U_(n)=0 and a compulsory pop. Thus every graph has outgoing
edges and positive finite Z; every stated transition is positive and sums to one.
At level h, the sum of products of rho over legal stacks is at most 1.
Consequently 3/4<=B=sum_s b(s)<=sum_(h>=0)2^(-h-1)=1; levels 0,1 give 3/4.
Every eta(s)>0 and sum eta=1. Selecting the initial state with law eta, and
each subsequent enumerated edge by a fresh uniform variable and its cumulative
P_s probabilities, constructs the full Borel path probability. Its cylinders are

    mu([alpha])=eta(s_0) product_(i=0 to m-1)P_(s_i)(f_i)

for every finite legal path alpha:s_0->...->s_m, including m=0.
All cylinders have positive mass; hence support is the ENTIRE declared X.
Every infinite path from a finite stack has infinitely many pushes: otherwise
its remaining finite height permits only finitely many pops. Each push has
probability <=1/2 (at e by rho<=1/2, elsewhere because Z>=1).
Thus nested cylinder probabilities tend to zero and EVERY individual path is
nonatomic, including every periodic and infinite-push path. None is removed.
This argument uses the frozen finite-initial-stack hypothesis; it does not
settle any infinite-initial-stack carrier or assign that boundary a measure.

The law is in fact not stationary: eta((n))=eta(e)rho(n)/2 gives

    mu(T^(-1)X_e)=eta(e) sum_(n>=2)rho(n)/(2 Z_(n)) <= eta(e)/2 < eta(e).

This does not obstruct the requested nonsingular chart owner.

## 3. Every predecessor and every-Borel full-point IMAGE

At t!=e there is exactly one incoming push, parent(t)->t with its actual
last integer. There is no incoming push at e. At EVERY t, incoming pops
are precisely tn->t for every n in its OWN A(t). DEPTH-ONE nonempty states
have none of these pops; all other stated predecessors remain. This exhausts
edges entering t, so every shift preimage is obtained by one such insertion.
Each I_f:X_t->[f] is a homeomorphism onto its cylinder, inverse T|_[f];
these cylinders partition X. Every state has a predecessor, so T is onto.
For E Borel in X_t, the Markov construction directly gives

    mu(I_f E)=eta(s)P_s(f) P_t^path(E)
             =[eta(s)P_s(f)/eta(t)] mu(E),       f:s->t.

The identity holds first on cylinders and then for every Borel set by finite
measure uniqueness. Its declared constant J_f is positive finite at EVERY y,
including all null paths. Since eta(sn)/eta(s)=rho(n)/2, its exact values are

    J_(push n:s->sn)=2/Z_s,       J_(pop:sn->s)=rho(n)/(2 Z_sn).
    kappa_push=log(Z_s/2),       kappa_pop=log(2 Z_sn/rho(n)).

In particular the root push clock is -log2. The clock is not a positive roof.
All chart measures are mutually absolutely continuous with their domains;
countably many such charts also give nonsingularity of the full shift relation.

## 4. All actual histories, cocycle and complete kernels

For alpha:s->t write p(alpha)=product P(f), M(alpha)=eta(s)p(alpha) and
C(alpha)=-log[eta(s)p(alpha)/eta(t)]. The empty path is allowed.
For an actual triple gamma=(z,m-n,y), let alpha=z|m:s->t and beta=y|n:r->t.
The common infinite tail includes its full starting stack t. Prefix replacement
beta w ->alpha w, on the ENTIRE beta cylinder, has every-Borel IMAGE

    J_gamma=M(alpha)/M(beta),
    c(gamma)=log[M(beta)/M(alpha)]=A_m(z)-A_n(y).

Any two witnesses of the SAME triple differ by a common number of future
steps; appending their shared tail multiplies both M's by the same positive
factor. Hence these formulas descend pointwise, including on periodic paths.
Reversing the arrow reverses c; composing after a common-tail refinement
multiplies IMAGE ratios, so c adds. No free-history or endpoint quotient is used.
These are exact FULL kernel tests on all triples, not only their isotropy:

    ker c: M(alpha)=M(beta);   ker ell: m=n;
    ker c intersect ker ell: m=n AND M(alpha)=M(beta).

The mass equality is an explicit finite-product test using the OWN weights:
M(alpha)=B^(-1)2^(-|s|-1)(product_(n in s)rho(n))
times (product over pushes in alpha of rho(label))/(product over its edges of Z_origin).
Changing witnesses cannot change either test. The common B cancels within one
owner; this does not identify its law with another owner's law. All labels stay.

## 5. All isotropy, positive cycles, incoming and physical phases

Unequal suffix equality of a full state-edge path is equivalent to eventual
periodicity. Its least eventual edge period q gives ENTIRE source isotropy qZ:
every equality difference is a multiple of q, and every multiple occurs beyond
the transient prefix. A non-eventually-periodic path has source isotropy {0}.
Returning only to a stack vertex is NOT returning to the same infinite path.
For any nonempty closed state-edge walk delta of length q, put

    L(delta)=-log product_(f in delta)P_origin(f)
            =sum_(f in delta)log Z_origin(f)
              +sum_(push n in delta)log[n(n-1)].

All eta factors telescope. Closed height balance gives equally many pushes
and pops, with at least one push. Thus q is even and, because each push has
probability <=1/2 and every pop <=1, L(delta)>0 (indeed >=(q/2)log2).
This proves positive cycle time despite signed local steps, for all four owners.
If delta is the least eventual word, c sends rq to r L(delta); therefore
H_x=L(delta)Z is the ENTIRE return group and extension isotropy is trivial.
For aperiodic tails, H_x={0} and extension isotropy is likewise trivial.

Keep ALL X times R, with (y,h)->(z,h+c(gamma)). All incoming at a are exactly
x=alpha T^n a, for every n>=0 and every finite legal path alpha ending at
the starting stack of T^n a; every such prefix's starting stack is permitted.
For any actual gamma:x->a, the complete phase is h+c(gamma) modulo H_a.
Two arrow choices differ by exactly H_a. Equality of phase is equivalent to
extension equivalence, so this source orbit contributes the SET R/H_a.
Height translation descends; its entire stabilizer is H_a. No global Borel
selector, Hausdorff quotient or invariant physical-flow probability is asserted.
For a periodic reference a with least word delta, x=alpha T^j a has phase
h-C(alpha)+A_j(a) mod L(delta). For an aperiodic reference the same expression
is real and witness-independent. All incoming histories and all heights remain.

## 6. Complete primitive packet classification

Take ALL finite nonempty closed state-edge walks in the OWN graph, including
those never reaching e. Keep those not proper powers, modulo cyclic rotation
of the FULL state-edge word. Each gives exactly one physical packet of least
time L(delta); its r repetitions have times r L(delta), not new primitives.
Conversely a nonzero physical return requires source isotropy and hence an
eventual primitive closed word of precisely this kind. Two eventual periodic
tails share a source orbit exactly when their primitive words are rotations.
Thus the list is complete, preserving packet multiplicity even when costs
coincide. No push/pop word is cancelled or merged merely for returning to the
same endpoint, and no arbitrary non-root starting stack is dropped.

## 7. MAIN's precommitted full packet: exact wrong primitive

Let a repeat e->(2)->e. The two distinct states force least source period 2,
so its ENTIRE isotropy is 2Z, not a selected loop. At (2), legal pushes are
all odd n>=3. Using rho(n)=integral_0^1 x^(n-2)(1-x)dx and nonnegative sums,

    U_(2)=sum_(odd n>=3)rho(n)=integral_0^1 x/(1+x)dx=1-log2.
    Z_(2)=2-log2,   L(a)=log[Z_e Z_(2)/rho(2)]=log(4-2log2).

The strict integral bounds 1/2<integral_0^1 dx/(1+x)=log2<1 imply
2<4-2log2<3. Therefore log2<L(a)<log3, not log of any prime.
The whole H is L(a)Z, so there is no smaller hidden physical generator.
Extension isotropy is trivial. All incoming are alpha T^j a, j=0,1, with
every legal alpha ending at that core state, and every real height.
Both source phases remain: relative to a, phases of (a,h) and (Ta,h) are
h and h-log2 modulo L(a), because A_1(a)=-log2. The general incoming phase
is h-C(alpha)+A_j(a). All repetitions are rL(a) on this same packet.
This violates the frozen primitive-time target and stops MAIN promotion.

## 8. Three complete independently owned controls

ARITHMETIC-OFF: S is every finite integer stack, A(s)={n>=2}; thus U_s=1,
Z_e=1, Z_s=2 otherwise. Summing each unrestricted level gives B=1 and eta=b.
Its OWN P,mu,J and signed clock follow from these values, with full support
and no atoms by section 2. Incoming lists, all-arrow mass-product kernels,
entire isotropy, extension, phases and ALL primitive closed walks are exactly
sections 3–6 evaluated with this OWN S,Z,eta; this specifies every field.
For e->2->e the least source period is 2 and L=log4, hence H=log4 Z,
extension isotropy zero, both phases h,h-log2 mod log4 and all incoming
prefixes retained. Log4 is a wrong primitive, not two repetitions of log2.

TOP-ONLY: S contains all adjacent-coprime stacks, A(e) all integers and
A(s)={n:gcd(n,top(s))=1} otherwise. Its OWN U_s is that exact convergent
rho sum, Z_s=1+U_s off e, B=sum over THESE stacks b(s), eta=b/B.
The bounds and probability construction apply anew, not with MAIN's B or law.
Every actual predecessor, IMAGE, mass-product kernel/intersection, entire
isotropy, phase and primitive walk is given by sections 3–6 on this graph.
At (2) its own U is the odd sum 1-log2, so its full e->2->e packet has
least time log(4-2log2), entire H that time times Z, trivial extension isotropy,
both phases h,h-log2 and every legal TOP-ONLY incoming prefix. Agreement at
this one word does not identify its deeper admissibility or packet ledger.

DEPTH-ONE: A(e) all integers, A((n)) empty; Z_e=Z_(n)=1. Direct summation
gives B=3/4, eta(e)=2/3 and eta((n))=rho(n)/3. OWN root push P=rho(n),
leaf pop P=1; J_push=2, J_pop=rho(n)/2. Its full law remains nonatomic
because infinitely many pushes are forced. Its predecessors and ALL kernels
are the explicit section 3–4 tests with these values; source/extension isotropy,
H and all phases follow from section 5. There are no direct leaf-to-leaf graph
edges; all composite history arrows between leaf-starting paths remain.
Every primitive closed walk corresponds to a primitive cyclic integer word
(n_1,...,n_r), with source period 2r and least time sum_i log[n_i(n_i-1)].
All its root/leaf rotations and incoming alternating histories remain; words
with equal costs remain distinct packets. The e->2->e and e->3->e packets
have ENTIRE H=(log2)Z and (log6)Z respectively, least source period 2 and
trivial extension isotropy. Both retain phases h,h-log2 modulo their OWN time,
every legal incoming prefix and all repetitions. The first prime-looking
packet does not rescue this control's log6 primitive or MAIN's wrong time.

## 9. Closure

All four full finite-initial-stack owners and every required field are covered;
no infinite initial stack, selected endpoint quotient or positive classical
roof was introduced. MAIN stops at its intrinsic wrong primitive. The own-law
and finite-history conclusions do not establish canonical arithmetic naturalness.
Strong naturalness OPEN; T3 NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED. No extra architecture or sixth round is opened.
EOF — raw-card derivation complete; freeze pending root read and manuscript unlock.
