# A complete symplectic compute–uncompute conveyor has no closed orbit

**Paper ID:** 159-reversible-sieve-conveyor  
**Candidate ID:** ASFS-20260915-RSC01  
**Date:** 2026-09-15  
**Status:** STOP — COMPLETE REVERSIBLE SOURCE CONVEYOR; NO INTRINSIC CLOSED ORBITS.  
**Evidence class:** exact construction and scoped negative theorem.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

An explicit autonomous symplectic map performs ordered proper-divisor tests,
undoes them, and advances through successive integer inputs on its positive
tail. A prime-independent negative tail makes its entire state space
reversible. Every discrete phase carries a full real register plane, and the
unit suspension is complete. We give a global inverse and an explicit
componentwise symplectic coordinate change under which the full map becomes
integer translation times an identity map. Thus no state, calibrated or
otherwise, is periodic. A separately closed finite compute–uncompute control
has the opposite defect: each register plane returns identically, producing
continuum primitive packets independently of primality. This realizes the
existing monotone-frontier obstruction on a concrete full geometric carrier;
it does not assert a new universal no-go theorem. The source computation is
retained, but this owner stops before a nonempty closed-orbit or analytic chain.

## 1. Question, lineage and collision boundary

Can a genuinely chronological source replace the parallel fixed-n geometry
in the [156 portfolio](../156-multi-round-source-trace-frontier/paper.md)
without obtaining recurrence from an unrelated object?

The [prior-work lineage](../../docs/prior_work/README.md) motivates the exact
arrow tested here:

\[
\text{prime/composite divisor symbols}
\longrightarrow\text{ordered source evolution}
\longrightarrow\text{area-preserving register transport}.
\]

The carrier below is two-dimensional on each connected component. It is
neither a zero-dimensional symbolic relabelling nor a disk thickening whose
centres are selected after the fact. It is also not asserted to be conjugate
to a historical Logistic or Hénon system. Its limited geometric contribution
is a full smooth conservative realization of the specified divisor evolution.

The relevant earlier collisions are narrow and acknowledged:

| Earlier record | Already established | What this contract additionally specifies |
| --- | --- | --- |
| [018](../018-monotone-sieve-clock-obstruction/paper.md) | A strictly increasing integer frontier excludes periodic points | An exact reversible full symplectic carrier, its derived height, and a complete suspension |
| [025](../025-sadic-sieve-automaton-screen/paper.md) | The operational growing-stage source does not recur | Concrete forward and backward register rules, including a defined negative tail |
| [053](../053-realtime-sieve-ca-nonrecurrence/paper.md) and [054](../054-prime-time-observation-nonrecurrence/paper.md) | The particular trajectory carrying a prime-time observation cannot close | Classification of every geometric state, not merely a designated arithmetic trajectory |
| [011](../011-reversible-sieve-simulation-control/paper.md) | Universal programmability does not establish special arithmetic geometry | No universality theorem is used; the fixed test rule is explicit, and its arbitrariness control is still adverse |

These are source and collision references, not transferred theorem credit.
The recurrence proof below is supplied in full and is elementary. No new
general impossibility theorem or literature novelty is asserted.

## 2. Frozen candidate and same-object ledger

The [version-1 card](candidate-card.md) was created before this audit.
For each j in Z put

\[
n_j=2+|j|,\qquad L_j=2n_j-2=2|j|+2,
\qquad E=\{(j,k):0\le k<L_j\}.
\]

The successor S increments k, except that the final phase goes to (j+1,0).
The full ordered block sequence is therefore

\[
\ldots,5,4,3,\underbrace{2}_{j=0},3,4,5,\ldots.
\]

Only the positive tail beginning at j=0 enumerates 2,3,4,... in forward
chronological order. The negative tail is a fixed symmetric computational
completion independent of primes, not a claim about pre-existing backwards
sieve history. Removing it would destroy the stated global inverse.

For n=n_j define

\[
w(j,k)=
\begin{cases}
1_{\{k+2\mid n\}},&0\le k\le n-3,\\
0,&k=n-2,\\
-1_{\{2n-2-k\mid n\}},&n-1\le k\le2n-4,\\
0,&k=2n-3.
\end{cases}                                                     \tag{1}
\]

The forward tests visit d=2,...,n−1. The reverse tests visit d=n−1,...,2.
There is one top pause and one block connector. Empty intervals cause no
test, so n=2 has only its two zero-increment phases. The rule invokes integer
divisibility directly; it does not read a prime table or factorization oracle.

The actual map and geometry are

\[
M=\bigsqcup_{(j,k)\in E}\mathbb R^2_{q,p},\qquad
\omega|_{(j,k)}=dq\wedge dp,\qquad
F(j,k,q,p)=\bigl(S(j,k),q+w(j,k),p\bigr).                         \tag{2}
\]

Every real q and p in every component belongs to M. Its smooth structure is
the usual countable disjoint-union structure. No phase, zero section or
calibration level is removed. The area measure is the sum of the ordinary
componentwise area measures; finite total volume is not claimed.

| Owned item | Exact definition and scope |
| --- | --- |
| Map and parameters | (1)–(2), no adjustable parameters and all integer blocks |
| Roof and flow | tau=1, X=(M×[0,1])/((x,1)~(Fx,0)), real time translation through the gluing |
| Source and observable | Proper-divisor increments along each actual forward scan; clean output or within-block displacement as defined in Section 3 |
| Periodic convention | Every intrinsic positive-period point of F, modulo its cyclic phase; suspension times computed with the same unit roof |
| Analytic owner | NOT ADVANCED: no transfer operator, zeta, determinant or trace is proposed |
| Later owner | Hamiltonian/contact/quantum DEFERRED; X has dimension three, not a symplectic-manifold claim |

## 3. What the source really computes

Write

\[
a(n)=\sum_{d=2}^{n-1}1_{\{d\mid n\}}.
\]

For n≥2, a(n)=0 exactly when n is prime, directly by the definition of
primality. Starting from (j,0,q_0,p_0), after its n−2 forward test steps the
actual state has phase k=n−2 and q=q_0+a(n). After the pause and reverse
tests, its q coordinate again equals q_0, and the connector enters the next
block without changing it.

Thus the top displacement q_top−q_entry is a(n) for every initial register
offset. On the explicitly calibrated source path q_entry=0, the top output
is zero exactly for prime inputs. All positive-tail integers are visited in
order on that same trajectory; there is no independently frozen n parameter
along it. A block consumes 2(n−2) divisor tests and two overhead steps, so its
physical duration is exactly 2n−2 under the frozen roof, not log n.

This is a finite deterministic trial-divisor computation, not a special
prime-generation complexity claim. The calibrated point observation must
not be asserted for arbitrary states: for a composite n with a(n)>0,
choosing q_entry=−a(n) makes q_top=0 as well. The displacement observation
avoids this offset ambiguity, but is a block observation, not a claim that
all full states have a pointwise prime indicator. None of these calibrations
is used to restrict the periodic ledger.

## 4. Exact full-state proofs

### Proposition 1. Global invertibility and symplecticity

The discrete predecessor is

\[
P(j,k)=
\begin{cases}
(j,k-1),&k>0,\\
(j-1,L_{j-1}-1),&k=0.
\end{cases}
\]

Consequently the global inverse of (2) is

\[
F^{-1}(j,k,q,p)=\bigl(P(j,k),q-w(P(j,k)),p\bigr).                \tag{3}
\]

Substituting (3) on either side of (2) yields the identity, including block
boundaries and j=0. On every connected component w is a fixed real constant,
so d(q+w) wedge dp=dq wedge dp. Both maps are smooth componentwise and
F is a global C-infinity symplectomorphism. This proof applies to all
real register states, not only integer or clean values.

### Proposition 2. A global translation coordinate

Define

\[
H(j)=
\begin{cases}
j(j+1),&j\ge0,\\
j(3-j),&j\le0,
\end{cases}
\qquad h(j,k)=H(j)+k.                                         \tag{4}
\]

Both formulas give H(0)=0. Direct subtraction yields
H(j+1)−H(j)=L_j for all j. The integer intervals
[H(j),H(j)+L_j−1] are therefore adjacent, disjoint, and exhaust Z because
H(j) tends to opposite infinities at the two ends. Hence h:E→Z is a
bijection, and

\[
h(S(j,k))=h(j,k)+1.                                           \tag{5}
\]

Let

\[
C(j,k)=\sum_{i=0}^{k-1}w(j,i),\qquad C(j,0)=0.                \tag{6}
\]

The total sum of w over each block is zero because its forward and reverse
lists exactly cancel. It follows at every phase, including the connector,
that

\[
C(S(j,k))-C(j,k)=w(j,k).                                      \tag{7}
\]

The componentwise affine change of coordinates

\[
\Psi(j,k,q,p)=\bigl(h(j,k),Q=q-C(j,k),P=p\bigr)               \tag{8}
\]

is a global diffeomorphism to Z×R² and preserves the symplectic form on each
component. Its inverse recovers the unique (j,k) from h and sets q=Q+C(j,k).
Equations (5) and (7) give the exact conjugacy

\[
\Psi F\Psi^{-1}(h,Q,P)=(h+1,Q,P).                             \tag{9}
\]

The witness increments are therefore an explicit additive coboundary on
the whole carrier. This coordinate change is not a selection of a centre
or a periodic subset. The prime computation remains visible in the original
register observable, but supplies no different full orbit geometry here.

### Corollary 3. No periodic state and a complete aperiodic flow

For every state x and every positive integer m, (9) increases its h
coordinate by m, so F^m x is never x. This classifies the full periodic
ledger: it is empty on all of M, including arbitrary q,p and both tails.

There is also a direct global description of the frozen suspension:

\[
\widehat\Psi([j,k,q,p,t])
=\bigl(q-C(j,k),p,h(j,k)+t\bigr)\in\mathbb R^2\times\mathbb R,
\quad 0\le t\le1.                                            \tag{10}
\]

At a glued endpoint (7) makes the first coordinate agree and (5) makes
the last coordinate agree. Thus (10) is well-defined. Every real last
coordinate has a unique integer-plus-unit-interval representative up to
this gluing; together with (8), this proves that (10) is a global smooth
coordinate identification of the suspension. In these coordinates its flow
is (Q,P,u)→(Q,P,u+t) for every real t. It is complete in both directions
and has no closed orbit of any positive real time.

No separate compactness assumption or local numerical orbit search is
needed. This is a concrete application of the mechanism already isolated
in 018, with exact full geometric ownership rather than a newly claimed
general obstruction.

## 5. Controls and the finite-closing trap

### Control A: exact integer and endpoint checks

The n=2 and n=3 blocks have no positive divisor witness. The n=4 block has
the explicit increment list (1,0,0,0,−1,0): its top output is one on a clean
register, but its total output is zero. These direct cases test empty ranges,
top-pause indexing and a genuine composite without constituting the global
proof. The negative-tail boundary j=−1→0 uses n=3→2 and satisfies (3)–(5).

### Control B: arbitrary offsets and retained geometry

Every initial q,p is included in Propositions 1–2. For n=4, q_entry=−1
makes q_top=0 although the input is composite. This refutes a full-state
pointwise primality claim from q_top alone. It does not alter the exact
displacement calculation or create a periodic orbit. Selecting the clean
q_entry=0 source path would not turn it into a symplectic periodic carrier.

### Control C: finite closed whole blocks are a different owner

Take any finite nonempty ordered list of whole blocks and redirect its
last connector to the first phase, retaining all real q,p. Denote its total
number of phases by L. This changes the phase map and is a control only,
not a modification of RSC01. Each full block has zero increment sum, so
the closed map G obeys

\[
G^L=\operatorname{id}
\quad\text{on its entire phase/register carrier}.
\]

The phase permutation is one cycle of length L; therefore no smaller
positive iterate returns a state. Every point has least period exactly L.
After cyclic identification, each orbit has a unique representative at the
first phase, and these representatives are parametrized by all of R².
Thus there is a continuum of primitive unit-roof closed orbits, each of
length L, with ordinary repeated times rL.

For a single block this holds for every integer n, including composites,
with L=2n−2. For one closed conveyor through n=2,...,N, it holds with
L=N(N−1); its cycles visit all those inputs, not a prime-only subset.
The full continuum cannot be removed by selecting a clean register or a
phase centre. This is the concrete cancellation failure of the proposed
compute–uncompute return construction.

### Control D: zero and nonarithmetic paired tests

Set every test to zero without changing the phase successor. The full
map is still aperiodic, now with C=0. More generally replace each forward
integer witness table by any fixed integer table and undo that table in
reverse order. Its block sum is again zero, and (4)–(9) apply with its new C.
The finite closed controls again return every real state.

These are changed maps, not inherited owner results. They establish the
PROVES_TOO_MUCH limitation of this architecture: invertibility, aperiodicity
and the return cancellation do not distinguish divisibility from arbitrary
paired data. The original prime observable is genuinely computed by (1),
but that fact alone does not produce privileged prime orbit geometry.

## 6. Gate assessment and limitations

| Obligation | Exact finding | Status / boundary |
| --- | --- | --- |
| P0 geometry and unit completeness | Explicit inverse, componentwise symplecticity and complete suspension | ESTABLISHED for this full owner |
| Prime-symbolic lineage | Ordered proper-divisor computation on the actual trajectory | Operational source ESTABLISHED; no privileged arithmetic geometry claim |
| A0 prime-orbit/target-clock relation | No closed orbit exists, and block runtime is 2n−2 | NOT ESTABLISHED; source positivity is not full A0 credit |
| A1 full intrinsic ledger | Empty on all states, not just the calibrated source | Scoped FAIL for the proposed nonempty prime-packet chain |
| A2 operator/trace/zeta | None proposed after the decisive recurrence result | NOT ADVANCED |
| Formal Route A | No formal evaluation performed | UNASSIGNED |
| Route B | No authorized ready same-object entry | NOT INVOKED |

The base has countably many connected components, although its unit
suspension has the global coordinates (10). It is a deliberately explicit
register transport, not an assertion of a compact or chaotic arithmetic
system. It supplies no finite-dimensional universal-computation theorem,
no source conjugacy to historical Logistic/Hénon dynamics, no exact log p
periods, no Fredholm or spectral result, and no claim about all possible
reversible sieve realizations. Failure here does not exclude a differently
defined recurrent arithmetic carrier.

## 7. Conclusion and decision

**STOP** RSC01 as a proposed prime closed-orbit source. Genuine forward
input chronology and reversible conservative geometry coexist, but the
entire object is a translation and has no intrinsic periodic orbit. Closing
the computation is a different object and cancels its arithmetic displacement,
leaving a continuum of cycles for prime and composite tests alike.

The next breadth decision is **FORK** only if a new source-return mechanism
can be specified that is neither an advancing input height nor an exact
compute–uncompute loop. It must retain the complete state space and derive
its own multiplicity and clock. No finite closing, clock, operator or
favourable subset is transferred into this stopped owner.

## Evidence and disclosure

The [claim ledger](claim-ledger.md) separates construction, negative results,
controls and nonclaims; the [evidence index](evidence/README.md) records the
proof method and file checks. All formulas and proofs are present here;
there is no unpublished dataset, numerical cutoff argument or target data.
The bounded ARS claim–evidence–counterargument discipline is used, without
claiming a full publication pipeline or human peer review. This is an
AI-assisted internal research record, with no human-subject data. External
funding, human authorship and conflicts are not asserted by this record.
