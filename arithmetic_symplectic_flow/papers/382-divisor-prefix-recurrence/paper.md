# Divisor-prefix recurrence: full transport and a composite primitive packet

Candidate ANG-20260922-DPR01; paper 382-divisor-prefix-recurrence.
Batch FULL-TRANSPORT-20260922-G, round 3/5; date 2026-09-22.
Outcome: `OWNED DIVISOR CLOCK; COMPOSITE PRIMITIVE PACKET — STOP / FORK`
T0/full chart-clock ownership established; fixed prime-time target fails.
Strong naturalness OPEN; T3 NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE;
formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

The full path source owns its probability, exhaustive inverse charts and
prescribed all-point IMAGE. Its signed cocycle and real-height orbit-SET
action retain every primitive state-edge necklace, incoming path and phase.
The precommitted three-step packet has ENTIRE return group (log8)Z,
distinct from the (log2)Z self-edge packet. Three own controls distinguish
an owned clock without returns from a wrong primitive.

## 1. Full arithmetic source and closure

The [55-line frozen card](candidate-card.md) fixes
S={(a,b):a,b>=1, gcd(a,b)=1}, D(a,b)={d>=1:d divides a+b}, and
\[
 (a,b)\xrightarrow{d}(b,(a+b)/d).                         \tag{1}
\]
Write W(a,b)=a+b and r(s)=|D(s)|. Each allowed quotient is positive.
Since gcd(b,a+b)=1, every divisor of a+b is coprime to b, proving closure.
There are finitely many outgoing edges, at least the distinct d=1 and d=a+b.
Hence no terminal paths occur. X is ALL infinite legal state-and-edge paths
from EVERY s in S, with its discrete-product Borel structure. T removes
the first edge and starting state; cylinders retain the complete starting pair.

For target (b,c), an incoming d must have source (dc-b,b). Positivity requires
dc>b, and gcd(dc-b,b)=gcd(d,b), because gcd(b,c)=1. Conversely these two
conditions put the source in S and give source sum dc, so d is legal and
its image is exactly (b,c). Thus ALL incoming branches are
\[
 d\ge1,\qquad dc>b,\qquad \gcd(d,b)=1.                    \tag{2}
\]
There are infinitely many, for example sufficiently large d=kb+1.
Each actual edge f:s->t supplies I_f:X_t->[f] by full prefix insertion,
with inverse T on [f]. The charts cover every actual predecessor; T is onto.

The lineage is divisibility/compositeness -> prefix-dependent legal divisor
choices -> sequential pair evolution. The full pair remains the history state.
This is a countable Markov realization, not a proved infinite-memory escape,
non-free-block mechanism, geometric lift or canonical arithmetic law.

## 2. Own probability, full support, atoms and stationarity

The normalizer C=sum_S 2^(-W(s)) obeys 1/4<=C<=1, by the (1,1) term
and the larger sum over all positive pairs. Set eta(s)=2^(-W(s))/C.
The uniform probabilities P_s(d)=1/r(s) and their consistent finite cylinders
construct the conditional path laws and mu=sum_s eta(s)P_s^path:
\[
 \mu([f_0\cdots f_{m-1}])
   =\frac{\eta(s_0)}{\prod_{i<m}r(s_i)}.                 \tag{3}
\]
This is a probability with full support: every nonempty cylinder is positive.
Because r(s)>=2, every length-m cylinder has mass at most eta(s_0)2^(-m).
Every path is null, including every periodic path; on this standard Borel
space mu is atomless. No typical-path restriction is used.

This frozen probability is NOT stationary. The incoming states of (1,1)
are (d-1,1), d>=2. Writing tau(d) for the number of positive divisors,
\[
 \mu(T^{-1}X_{(1,1)})=\frac1C\sum_{d\ge2}\frac{2^{-d}}{\tau(d)}
 <\frac1{2C}\sum_{d\ge2}2^{-d}
 =\frac1{4C}=\mu(X_{(1,1)}).                             \tag{4}
\]
Strictness uses tau(4)=3. This concerns mu, not every possible invariant probability on the graph.

## 3. Every-Borel IMAGE and the signed full-point clock

For each actual f:s->t, conditioning (3) on its first edge gives on cylinders,
and then on ALL Borel E subset X_t by uniqueness of finite measures,
\[
 \mu(I_fE)=j_f\mu(E),\qquad
 j_f=\frac{\eta(s)}{r(s)\eta(t)}
     =\frac{2^{W(t)-W(s)}}{r(s)}.                        \tag{5}
\]
This is the prescribed finite positive value at EVERY tail, including all
null paths, and equals every corresponding full-cylinder ratio.
Countability, positivity and the exhaustive incoming list imply
mu(E)=0 iff mu(T^(-1)E)=0. All inverse charts are Borel bijections.

For a path beginning at s with next state t,
\[
 \kappa=\log r(s)+(W(s)-W(t))\log2.                     \tag{6}
\]
For instance (1,2)--1-->(2,3) has kappa=-log2: this is the owned signed
IMAGE clock, not a positive classical roof or monotone source-step time.

## 4. Finite histories, descent and complete kernels

For any finite legal path u:s->r define its edge length |u|,
R(u)=product_(edge departures v)r(v), and
\[
 K(u)=2^{W(s)}R(u),\qquad
 D(u)=\frac{\eta(s)}{R(u)\eta(r)}
     =\frac{2^{W(r)}}{K(u)}.                            \tag{7}
\]
For an empty path R=1. Prefix insertion has every-Borel IMAGE D(u).
Replacing v by u, when both end at the same r, has IMAGE D(u)/D(v)
on every Borel subset of its complete domain [v].

Use exactly G={(z,m-n,y):T^m z=T^n y}, source y and range z, with equal
triples identified, and ell(z,k,y)=k. Let A_m(z)=sum_(i<m)kappa(T^i z).
For u=z|m and v=y|n,
\[
 c(z,m-n,y)=A_m(z)-A_n(y)=\log\frac{K(u)}{K(v)}.          \tag{8}
\]
The prefix-replacement IMAGE is exp(-c). Two representations of one triple
append the same number of common-tail edges, so their additional A-sums
cancel. This proves descent everywhere. Aligning tails proves cocycle
addition under composition; inverse arrows negate c.

The FULL kernels, including all transient histories, are
\[
 \ker c=\{(z,m-n,y):T^mz=T^ny,\ K(z|m)=K(y|n)\},
\]
\[
 \ker\ell=\{(z,0,y):T^Nz=T^Ny\text{ for some }N\ge0\},
\]
\[
 \ker c\cap\ker\ell=
 \{(z,0,y):T^Nz=T^Ny,\ K(z|N)=K(y|N)\text{ for some }N\ge0\}.
                                                               \tag{9}
\]
These are explicit integer-product tests in every presentation, not tests requiring an unknown cocycle.
The arrow (1,1)--1-->(1,2) has zero clock and nonzero lag.
Three self-edges at (1,1) and the three-step walk in Section 6 have equal
length, start, endpoint and R=8. Prefixing them to one common tail gives
distinct paths and a nonunit intersection-kernel arrow.

## 5. Entire isotropy, primitive necklaces and all phases

Source isotropy is nontrivial exactly when the full state-and-edge path is
eventually periodic. If its periodic tail has least period q, the ENTIRE
source isotropy is qZ: an equality T^m x=T^n x forces eventual period
|m-n|, and all multiples of q occur beyond the transient part.
Otherwise source isotropy is {0}. Incoming paths need not literally return.

The periodic core is a finite closed state-edge word
w=(s_0,d_0,...,s_(q-1),d_(q-1)), with (1) cyclically and s_q=s_0,
which is not a proper power. Cyclic rotations identify the same primitive
necklace; no endpoint-only quotient or simple-cycle restriction is made.
Every periodic tail gives such a word, and two primitive words give the
same tail-equivalence class iff they are cyclic rotations. This is an
exhaustive finite-word criterion, not a finite enumeration of cycles.

State weights telescope around w, giving
\[
 L(w)=\log R(w)=\sum_{i<q}\log r(s_i)>0,\qquad
 H_x=c(G_x^x)=L(w)\mathbb Z.                            \tag{10}
\]
At an incoming x, transient contributions cancel and c(x,kq,x)=kL(w).
For a noneventually-periodic x, H_x={0}. All three kernels in (9) have
trivial isotropy. In the entire extension with arrows
(y,h)->(z,h+c(z,k,y)), isotropy is therefore trivial at EVERY (x,h).

Keep all X times R. Height translation gives a complete real action on
the orbit SET; no smooth, Hausdorff or measure-preserving quotient is asserted.
Its stabilizer at [(x,h)] is exactly H_x. The complete source orbit is
O_x={u T^n x:n>=0, u any legal finite path ending at the start of T^n x}.
Nothing restricts incoming prefixes to a selected recurrent core.
Choose a in O_x and an arrow g:y->a. The phase of (y,h) is
h+c(g) modulo H_a. Choices differ by isotropy, and equal phases yield an
actual arrow after an isotropy correction. Thus the quotient over O_x is
exactly R/H_x. Each primitive necklace supplies ONE physical packet with
least positive time L(w), all phases R/L(w)Z and repeats jL(w), j>=1.
Aperiodic source classes have phase line R and no nonzero time returns.

## 6. Precommitted packets and the decisive target failure

At (1,1), d=2 is a self-edge with r=2. Its repeated path has q=1,
H=(log2)Z, and least physical time log2.
For w=((1,1),1,(1,2),3,(2,1),3), all three states have two divisors
available. Its distinct states give least source period EXACTLY 3.
Hence R(w)=8, ENTIRE H=(log8)Z, and least physical time log8.
This is not the third traversal of the self-edge packet: the infinite
state-edge tails are different primitive necklaces and never become equal.
The integer 8 is composite, so this wrong primitive stops target promotion.
More generally every q>=2 word has composite R(w); the only MAIN self-edge
solves a=b and d=2, hence a=b=1 by coprimality. There is no unexamined
length-one primitive that changes the interpretation of this counterexample.

The three source clock steps of w are 0, log2 and log4. Relative to its
first source phase, the three equal-height phase offsets are 0, 0 and log2
modulo log8. Coincident offsets do not create a smaller isotropy period.
For every incoming y=uT^n a, m=|u|, its phase is
h+A_n(a)-A_m(y) modulo H_a. This keeps all legal prefixes and all heights.

## 7. Three own controls, including boundary and atom differences

Each control constructs its OWN normalized eta=2^(-W)/C and uniform legal-
edge probabilities. Conditional cylinders reprove (3),(5),(7)-(9); no MAIN
transition law is inherited. The incoming lists below replace (2), with no
nonexistent predecessor added. Source isotropy and the complete orbit/phase
argument of Section 5 apply to these own paths.

**NO-DIVISION.** Only F(a,b)=(b,a+b) occurs on coprime pairs; C is the
same state sum, but each conditional path law is a point mass. Thus the
full probability is atomic, with mass eta(s) at the unique path from s,
and has full support. An incoming branch exists exactly for target (b,c)
with c>b: source (c-b,b), d=1. There are no other branches.
Its j=2^b, kappa=-b log2; every-Borel IMAGE remains valid.
No mass enters (1,1), so this law is not stationary.
F is injective and W(Fs)>W(s). It has no eventual periods anywhere.
If F^m s=F^n t, injectivity makes s,t comparable on one forward chain;
their W-values strictly order distinct states. With R(u)=1 and
K(u)=2^W(start(u)), (9) then makes clock, lag and intersection kernels
ALL unit-only. Source/extension isotropy and H are zero everywhere.
Each full source orbit has phase line R and no nonzero physical returns:
this is an OWNED clock without returns, not an undefined clock.

**END-DIVISORS.** Each state permits the distinct d=1 and d=a+b, so r=2.
The own full probability is atomless and full-support. Incoming branches
are exactly: d=1 from (c-b,b) when c>b; or, when c=1, from every (a,b)
with a>=1, gcd(a,b)=1, labelled d=a+b. Some states have no predecessors.
It is not stationary: mass entering (2,3) is eta(1,2)/2=1/(16C),
whereas eta(2,3)=1/(32C). Here K(u)=2^(W(start(u))+|u|);
ker c requires W(start(u))+|u|=W(start(v))+|v|, with (9) giving the
lag and intersection conditions. Every primitive closed word has L=q log2.
The self-edge and three-step word independently remain legal, with q=1,3
and entire H=(log2)Z,(log8)Z respectively. Extension isotropy is zero,
and every own incoming history and phase follows Section 5 with its own A.

**ALL-PAIRS.** All positive pairs are states, C=1; the own divisor law has
r(a,b)=tau(a+b)>=2, so its probability is atomless and full-support.
Incoming branches are EXACTLY d>=1 with dc>b, source (dc-b,b):
there is NO gcd condition. All targets have predecessors.
The strict calculation (4), with C=1, proves nonstationarity.
The own j and integer K are (5),(7); (9) gives all kernels.
Every primitive cyclic legal word has L=log product_i tau(W(s_i))>0,
so source isotropy is qZ, H=LZ and extension isotropy is trivial; all
aperiodic, incoming and phase data remain as in Section 5 for this graph.
The self-edge and three-step tests still have least times log2 and log8.
There are also self-edges d=2 at EVERY (a,a), with q=1 and
H=log(tau(2a)) Z: (2,2) gives log3 and (3,3) gives a wrong primitive log4.
Their full incoming sets and phase circles are retained, not transferred
to MAIN or merged merely because times agree.

## 8. Scope, decision and evidence

The same-object ledger remains intact: source, probability, inverse IMAGE,
signed cocycle and full packets belong to this law. T0/chart-clock ownership
is established; target promotion STOPS by the primitive log8 packet.
Strong naturalness OPEN; T3 NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED. No universal history no-go, positive classical
suspension, rescaling, bad-packet deletion or changed owner is claimed.

Data/method: exact proofs and [card](candidate-card.md), no scientific numerics or finite-cycle cutoff.
See [ledger](claim-ledger.md) and [overview](README.md). The author supplied
the scout and shares earlier authorship/history; no reviewer/raw or other new
main was read. ARS writing boundaries keep review root-owned; internal model
scrutiny is NOT_CALIBRATED, not external peer review, novelty or Route evidence.
AI: definition, derivation and drafting. Human subjects: N/A; human CRediT, funding and conflicts not supplied.

EOF — full recurrence transport and complete scoped STOP / FORK.
