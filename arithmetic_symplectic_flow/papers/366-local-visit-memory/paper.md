# Local visit memory: a full Haar owner with retained histories and zero physical clock

**Paper:** 366-local-visit-memory. **Candidate:** ANG-20260921-LVM01.
**Date:** 2026-09-21. **Status:** ZERO HAAR CLOCK; FULL MEMORY PREVENTS RETURNS — STOP / FORK.
**Batch:** LONG-MEMORY-20260921-D, round 2/5. **Formal:** UNASSIGNED; **B:** NOT INVOKED.

## Abstract

We retain every oriented edge and profinite local visit counter. Routing depends on incoming edge and current
memory, and the full map has a unique actual inverse. Its countable branch
partition proves Haar preservation for every Borel set. Consequently every
prescribed cylinder IMAGE ratio is one at every point and every signed lag.
Full profinite visit retention also excludes every nonzero source period.
The owned height extension has no positive physical return. Three separate
controls receive their own inverse, measure and clock audits; finite memory
has an exact visit-count return criterion, without a global cycle census.
This negative result concerns the frozen clock, not all history-dependent arithmetic sources or filtering.

## 1. Identity, question and boundary

The [frozen card](candidate-card.md), including CP1 clarification, fixes the full object and clock version.

| Item | LVM01 owner | Scope |
| --- | --- | --- |
| Arithmetic source | Integer factor/divisor neighbor graph below | No prime labels |
| State and map | Actual incoming edge and every local counter; F below | No selected run |
| Measure | Edge counting times full product Haar | Not a fitted density |
| Clock | Prescribed forward cylinder IMAGE, then minus its logarithm | No graph-length roof |
| Extension and time | Full real-height extension; height translation | Quotient as a set |
| Primitive convention | Entire positive return group and its least generator | No projected return |
| Classical geometry / analysis | No symplectic suspension or analytic operator | NOT APPLICABLE / NOT AUDITED |

The question is whether this source owns nonzero arithmetic time. We prove global ownership, zero clock,
and no such packet. Strong naturalness remains OPEN. Routing uses the current
arithmetic position and its evolving local memory; neither an absolute-time
schedule nor a prime-dependent input is present. This does not establish an
escape from a Markov filtering obstruction or an intrinsic prime-selection law.

## 2. Exact carrier, graph and full inverse

Put V={2,3,...}, K=the profinite integers, and
\[
N(v)=\{av:2\le a\le v\}\cup
\{b\ge2:b\mid v,\ 2\le v/b\le b\}.
\tag{1}
\]
The first set has v-1 distinct members, all at least 2v; the second consists of proper divisors at most v/2.
Thus d(v)=|N(v)| is finite and
positive. If w=av is in the first set, v is in the second set for w;
the same implication reversed treats every second-set neighbor. Hence the
graph is undirected, without loops, and the deduplication gives a simple graph.
Let iota_v number N(v) increasingly by 0,...,d(v)-1.

Let E be the discrete set of all oriented neighbor pairs, R=K^V, and X=E times R with product topology and Borel structure. For
x=((u,v),rho), define
\[
i=\iota_v(u),\quad j=i+\rho_v\pmod{d(v)},\quad
w=\iota_v^{-1}(j),\qquad
F(x)=((v,w),\rho+\mathbf1_v).
\tag{2}
\]
For example N(3)={6,9}; incoming 6 routes to 6 or 9 according to the current counter parity, which each actual visit updates.
Given any target ((v,w),rho'), its proposed predecessor is
\[
\rho=\rho'-\mathbf1_v,\qquad
i=\iota_v(w)-(\rho_v\bmod d(v)),\qquad
u=\iota_v^{-1}(i).
\tag{3}
\]
The neighbor symmetry makes (u,v) an actual oriented edge. Substitution in
(2) returns the target; applying (3) after (2) recovers both i and every
memory coordinate. This proves both inverse identities and uniqueness on
ALL points, including arbitrary noninteger profinite counters. On each
fixed-edge residue piece the formulas are translations of one coordinate,
so both maps are continuous. F is a global homeomorphism. Every point has
exactly the full bilateral history (F^k x) for k in Z; there are no additional
preperiodic incoming histories and no missing boundary states.

## 3. Every-Borel IMAGE and the specified all-point version

Let m be normalized product Haar on R and mu=edge counting times m.
E is countable and every edge fiber has mass one, so mu is sigma-finite.
For u in N(v) and r in Z/d(v)Z define the complete branch
\[
B_{u,v,r}=\{((u,v),\rho):\rho_v\equiv r\pmod{d(v)}\}.
\]
With w=iota_v^{-1}(iota_v(u)+r), its exact image is
\[
D_{u,v,r}=\{((v,w),\rho'):\rho'_v\equiv r+1\pmod{d(v)}\}.
\tag{4}
\]
The complete B cylinders partition X.
For a target ((v,w),rho'), its residue r=rho'_v-1 and then
iota_v(u)=iota_v(w)-r are unique, so the D pieces also partition X.
Each branch translates rho_v by one and leaves every other coordinate
unchanged. Product Haar therefore gives, for EVERY Borel A contained in B,
mu(F A)=mu(A), not merely equality of the two cylinder masses.
Indeed finite-coordinate rectangles have that equality by translation
invariance, and uniqueness of their product measures extends it to all Borel
sets. Countable disjoint branch summation then proves
\[
\mu(F^k A)=\mu(A)\quad
\text{for every Borel }A\subset X\text{ and every }k\in\mathbb Z.
\tag{5}
\]
Negative k follow using the actual inverse; all images are Borel.

For the card's C_N(x), the edge is fixed and N-1 coordinates have specified
residues modulo N!, so mu(C_N(x))=(N!)^{-(N-1)}>0. Equation (5) applies
even if the image splits across many cylinders. Hence, for EVERY x,k,N,
\[
\frac{\mu(F^k C_N(x))}{\mu(C_N(x))}=1,\qquad J_k(x)=1.
\tag{6}
\]
The frozen limit exists in (0,infinity) everywhere and agrees with every-Borel
IMAGE. There is no almost-everywhere reassignment. Thus c(x,k)=-log J_k(x)=0
is the specified cocycle, with its additivity immediate on actual compositions.
The conditional mass 1/d(v) in (4) is shared by source and image; it is
not a full branch derivative and does not supply a log d(v) clock.

## 4. Full source returns, kernels and physical phases

Write F^j x=((u_j,v_j),rho^(j)). For n>0 put
\[
L_a(n;x)=\#\{0\le j<n:v_j=a\}.
\]
Only finitely many L_a are nonzero, their sum is n, and iterating (2) gives
rho_a^(n)=rho_a+L_a(n;x) in K for EVERY a. A positive integer L cannot
vanish in K: its residue modulo L+1 is nonzero. At least one L_a is
positive, so F^n x is never x. Invertibility excludes negative periods too.
Thus the ENTIRE source isotropy I_x={k:F^k x=x} is {0}, at every full state.
Token-edge closure or closure of finitely many residue observations is not
full-memory closure.

Use the actual action groupoid G with arrows (x,k):x->F^k x, retaining k.
The clock kernel ker c is ALL G; the lag kernel ker(k) consists exactly of
unit arrows, as does their intersection. The extension arrow is
(x,h)->(F^k x,h+c(x,k))=(F^k x,h); its isotropy is I_x={0}.
For every x, the full isotropy clock image H_x=c(I_x) is {0}.

More directly, the full orbit quotient as a SET is
\[
Y=(X\times\mathbb R)/G\ \cong\ (X/F)\times\mathbb R,\qquad
\phi^t([x],h)=([x],h+t).
\tag{7}
\]
Height is well-defined on every equivalence class. A return forces h+t=h,
so t=0: no stationary physical orbit, positive primitive or repetition exists.
All representatives of [x,h] are exactly (F^k x,h); all physical phases are
the full real line over that source orbit. No unvisited coordinate is deleted
or identified by a finite-difference rule. No quotient separation, smoothness,
invariant flow measure or Borel transversal is needed or claimed.

## 5. Three own controls

Each control uses its own graph, memory measure, map and branches. For the stated finite-positive-degree graphs,
formulas (2)--(4) can be checked afresh: the residue determines the unique
predecessor edge; translating the active memory gives the exact image residue.
The following own branch checks verify every-Borel IMAGE for EACH control, without transferring MAIN's recurrence.

**EDGE.** Vertices {0,1}, one edge, degree one at both ends, memory K^2; edge counting times Haar has total mass two.
The rule sends ((u,v),rho) to ((v,u),rho+1_v); its inverse subtracts at the
first target vertex and reverses the edge. Each entire edge fiber maps by
one Haar translation onto the other, proving every-Borel IMAGE one for all
signed iterates. C_N fixes both coordinates modulo N! and has mass
(N!)^-2, so its specified J_k is one at every point. Every positive
number of steps increments at least one retained K-coordinate positively;
the modulo L+1 argument gives I_x={0}, including token loops.

**LINE.** Vertices Z, neighbors v-1,v+1 with indices 0,1, memory K^Z.
At an incoming edge, r=rho_v mod 2 selects j=i+r. The inverse subtracts
one at the first target vertex and recovers i=j-r with r=(rho'_v-1) mod 2. Each source parity
cylinder maps by translation onto its exact target parity r+1; the two
incoming possibilities give disjoint exhaustive target pieces. Haar on K^Z
therefore gives every-Borel IMAGE one, and counting edges makes the measure
sigma-finite. Here mu(C_N)=(N!)^{-(2N+1)}, hence J_k=1 everywhere.
The same directly counted visits have finite support and total n for n
steps, so a positive retained counter change again gives I_x={0}.

**FINITE-MEMORY.** Use MAIN's graph and R_f=product_v Z/d(v)Z, with product
uniform measure. Formula (2) now adds one modulo d(v); (3) subtracts it
there. A source piece rho_v=r maps to the whole image piece rho'_v=r+1;
for every target residue and incoming target edge there is exactly one
predecessor. Translation preserves the finite uniform factor, including
d(v)=1. The disjoint branch argument proves every-Borel IMAGE one for all
signed iterates. Its measure is sigma-finite and
mu(C_N)=product_(2<=v<=N) d(v)^(-1)>0, so its own J_k=1 everywhere.
For its ACTUAL forward trajectory and n>0, the exact criterion is
\[
F_f^n x=x\quad\Longleftrightarrow\quad
(u_n,v_n)=(u_0,v_0)\quad\text{and}\quad
L_a(n;x)\equiv0\pmod{d(a)}\ \text{for EVERY }a.
\tag{8}
\]
This follows by iterating each memory update; conversely these conditions
restore every coordinate and the entire edge. Unvisited coordinates have
count zero and remain included. If no positive n satisfies (8), I_x={0};
otherwise its least satisfying n=q exists and I_x=qZ by the group law and
division with remainder. This does not classify which trajectories return.

For EACH control, its proved J makes c identically zero, ker c its whole
actual groupoid, and the retained-lag kernel precisely its unit arrows.
Its extension isotropy is its own I_x just stated, and H_x={0} at ALL
points, whether or not a finite-memory source returns. Formula (7) holds
with that control's own source orbit set and excludes every nonzero physical
time. All incoming representatives and real phases are retained; at a
period-q source, coincident endpoints still have distinct lag-k arrows.
No control supplies a prime packet to MAIN.

## 6. Gate assessment, collision and decision

| Gate | Evidence | Status / boundary |
| --- | --- | --- |
| T0 | Complete inverse, all-point histories, sigma-finite Haar owner | ESTABLISHED |
| T1 | Owned every-Borel IMAGE and prescribed J=1 | ZERO CLOCK; naturalness OPEN |
| T2 | Full source isotropy; physical height obstruction | NO POSITIVE PHYSICAL RETURNS |
| T3 | No operator, trace or determinant | NOT AUDITED |
| Classical A0/A1/A2; formal Route; B | No classical suspension or evaluation | NOT APPLICABLE; UNASSIGNED; NOT INVOKED |

The [329 card](../329-moving-divisibility-rotor/candidate-card.md), including its outcome, was read for the collision;
its paper and review were not read. That different owner uses binary flips
and biased product measure. Local memory and clock cancellation are not
claimed as new. All proofs above use LVM01's actual graph, counters and Haar
law; no 329 theorem is imported. The earlier 025/026/029/049 card-only scout
and the definition distinction from 365 establish no nonconjugacy or novelty.

**Decision: STOP / FORK.** The full source and its history-dependent routing
exist, but their frozen IMAGE clock is zero. Do not substitute finite memory,
a graph-length roof, selected histories or a new measure under this ID.
Measure preservation is not a claim of measure-theoretic conservativity or
Markov-filter escape. No finite-memory global census, target match or broader
impossibility theorem follows from this decisive gate.

## Reproducibility and disclosure

Inputs are exactly the [card](candidate-card.md); proofs cover all Borel sets, points and signed lags. No numerical
experiment, finite orbit search, external dataset or fitted parameter is used.
Root owns the separate claim/evidence records and review integration. This
author text does not preclaim their completion. AI-assisted internal work is
not external peer review or novelty certification; no venue criteria are bound.
