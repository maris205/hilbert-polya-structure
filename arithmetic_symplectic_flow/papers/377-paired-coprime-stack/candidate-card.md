# Frozen card — paired hard coprime stack paths

Candidate `ANG-20260922-PCS01`; batch `HARD-NONLOCAL-20260922-F`, round3/5.
Date2026-09-22. Status `FROZEN; FULL STACK PATH MEASURE/CLOCK OPEN`.

## 1. Entire arithmetic stack carrier

rho(n)=1/[n(n-1)],n>=2. S contains the empty stack e and ALL finite ordered
stacks s=(n_1,...,n_h) with pairwise gcd(n_i,n_j)=1 for i!=j.
A(s)={n>=2:gcd(n,n_i)=1 for EVERY current stack entry}.
Edges are push n:s->sn for n in A(s), and pop:s->parent(s) if s!=e.
Labels include the actual matched integer; no unmatched or empty pop.
X is ALL infinite directed edge paths with their full initial state s in S,
with disjoint-state/product topology and Borel structure. Keep infinite push,
never-returning paths, all legal depths, all null periodic paths and phases.
Initial stacks are FINITE by this freeze; infinite initial stacks are not an
implicitly solved boundary. T deletes the first edge and its starting state.
Only actual path shifts and legal prefix insertions generate the relation.
Lineage: common-divisor witnesses -> hard admissibility against all still
unclosed entries -> matched nesting and return. This is a stated deformation,
not a geometric lift or an escape from its own countable-state Markov graph.

## 2. Own path law and actual full-point IMAGE

Z_s=1_(s!=e)+sum_(n in A(s))rho(n).
P_s(push n)=rho(n)/Z_s; P_s(pop)=1/Z_s when s!=e.
b(s)=2^(-|s|-1)product_(n in s)rho(n), B=sum_(s in S)b(s), eta(s)=b(s)/B.
Construct mu=sum_s eta(s)P_s^path on ALL X, proving normalization,
full support and actual atom status. Do NOT assume stationarity; the contract
needs nonsingular inverse charts, not an invariant probability assertion.
For every actual edge f:s->t, I_f:X_t->[f] inserts f and its starting state.
Prove ALL predecessor charts, including incoming pushes and pops at EVERY t.
Freeze J_f(y)=eta(s)P_s(f)/eta(t), y in X_t. Require EVERY-Borel IMAGE
mu(I_f E)=integral_E J_f dmu for all E subset X_t, with all-point positivity
and finiteness. This is an owned full-cylinder ratio, not a supplied roof.

## 3. Clock, full returns and decisive test

For x starting with f, kappa(x)=-log J_f(Tx); local values MAY be signed.
No positive classical roof or monotone step-time is presumed. A_m sums kappa.
G={ALL actual(z,m-n,y):T^m z=T^n y}, source y range z; equal triples only.
Prove all finite-history IMAGE, descent/cocycle, FULL clock/lag kernels and
intersection, entire source/extension isotropy and physical H. Retain ALL
X times R with arrows(y,h)->(z,h+c),c=A_m(z)-A_n(y), and physical height
translation on orbit SET. Prove full incoming/phase and primitive closed-walk
classification/repetition; no root-only orbit selection or endpoint quotient.
Precommitted full packet: the path repeatedly e->(2)->e, with ALL legal
incoming histories and both source phases. Derive least source period and
ENTIRE H, comparing the least positive time with log2 and log3 by exact
series/integral inequalities. Target least log p, at most one per prime in
fixed normalization. Wrong primitive stops promotion; finish own controls.

## 4. Three own control definitions

ARITHMETIC-OFF: ALL finite stacks of integers>=2, push any integer, exact pop.
TOP-ONLY: ALL finite stacks with only adjacent entries coprime; push checks
only top, all integers allowed at empty; exact matching pop remains.
DEPTH-ONE: states e and(n),n>=2; empty may push any n, nonempty only pops.
Each reconstructs its OWN legal push sets, Z_s,P_s,b,B,eta,mu and full path
source by the SAME displayed recipes, and its own J/chart clock. No measure
or transition is inherited after changing the graph. Each retains every legal
infinite path, all starts/null cycles, all kernels,isotropy,H,incoming,phases.
Test the full e->2->e packet separately for each; DEPTH-ONE also e->3->e.
State the complete primitive closed-walk formula, without a finite census.
A control's prime-looking word may not be transferred to MAIN.

## 5. Scope and provenance

Definition scout supplied this tuple without theorem/clock calculation, based
on prior370/372 authorship and old shared history. It read current AGENTS,
plan and overview1–160, not375+papers or peers. Root freezes its exact law
before audit, privately anticipating graph-word splicing may remain despite
unbounded stack memory. No nonconjugacy, novelty or canonical-law claim.
Root/scout know that keeping the full stack is a countable Markov realization;
do not market unbounded state size as escape from all Markov obstructions.
ARS CP1 before math, separate raw before manuscript unlock, CP2/CP3; internal
shared-history NOT_CALIBRATED. Strong naturalness OPEN; T3 NOT AUDITED;
classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
Markdown only; no scientific numerics, external/Git actions or sixth round.

EOF — full finite-initial-stack path owner and actual signed chart clock frozen.

## Outcome — 2026-09-22

Candidate ANG-20260922-PCS01.
Status: OWNED STACK CLOCK; WRONG PRIMITIVE TIME — STOP / FORK.
The preceding 81 lines remain the unchanged pre-audit freeze; this outcome
records the [main proof](paper.md), not a change of carrier or law.

The entire finite-initial-stack countable Markov path source owns its
full-support, atomless probability, exhaustive inverse charts and all-point,
every-Borel IMAGE. This probability is not shift invariant. Its signed local
clock descends to the full retained-lag groupoid and real-height orbit SET;
it is not a positive classical suspension. All kernels, source/extension
isotropy, primitive closed walks, incoming histories and phases are retained.
For the whole e->(2)->e packet, least source period is 2 and
H=L Z, L=log(4-2 log2), with log2<L<log3. This is a wrong least positive
time, not merely a repetition: fixed prime-time target promotion stops.

Own-law controls give log4 (ARITHMETIC-OFF), the same between-prime time
(TOP-ONLY), and log2 plus a separate primitive log6 packet (DEPTH-ONE).
No control result is transferred to MAIN. Strong naturalness OPEN;
T3 NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED;
B NOT INVOKED. Infinite initial stacks remain outside this finite-initial
owner. No all-Markov or all-memory no-go, novelty or geometric lift follows.
Method: exact cylinder identities, finite-product kernel criteria and an
exact series/integral bound; no scientific numerics or finite cycle census.
See [overview](README.md) and [claim ledger](claim-ledger.md) for scope.
