# Independent GM candidate gate

Date: 2026-09-05 UTC. Reviewer: batch197_fifth_scout.

## Verdict

**MATH_VALID / KILL_VALUE_FOR_THIS_BATCH / HOLD_EXTERNAL.**

The three displayed GM claims survive independent reconstruction: the local
degree deadline, every-degree sharpness, and the unique maximum one-step
fibre. I found no mathematical counterexample or theorem-threatening gap.
This is nevertheless not an admission: after the old-rule/serial-cover
subtraction, the only plausible new temporal residual is the sharp deadline
package, while the proposed inverse axis transfers directly from elementary
incidence-mex forbidden-palette counting already used inside P118.

This verdict does **not** assert that the exact degree deadline was stated in
the 2003 paper. A per-node move count is not a bound on the wall-clock index
of the last move. The additional no-delay induction must not be falsely
attributed to that source merely because the double-cover adapter exists.

## Scope and independence

I was not an author of GM_PROOF_PACKAGE.md and did not edit it or the author
verifier. I read its complete statement and proofs, independently rebuilt
the arguments, read P118's actual map and fibre proof, and inspected the full
five-page primary 2003 article. I wrote an independent verifier using no
author-code imports. The only current writes for this task are in GM_GATE/.
No manuscript review A/B, paper freeze, or paper-level acceptance is claimed.
Any future substantive repair to which I contribute must be disclosed before
assigning a later manuscript reviewer role.

Reviewed candidate input SHA-256:

```text
c23868e2390fff81fdcf5a9dec1e13894b1379675547b6a6b840cfb6e9f40c56  ../GM_PROOF_PACKAGE.md
```

The main correctness finding is no required mathematical repair. For the
empty graph, interpret maximum degree as zero, as the author verifier does.
This convention does not affect the result or value decision.

## 1. Independent mathematical reconstruction

### Temporal part

If $c_t(v)=k$, every neighbor of $v$ excludes $k$ from its next mex, because
the edge can be read in reverse. Thus $k$ is absent around $v$ at time
$t+1$, proving $c_{t+2}(v)\leq k$.

For a strict drop to $l<k$ at time $t+2$, with $t\geq1$, the previous mex
condition at time $t$ supplies a neighbor $u$ with $c_{t-1}(u)=l$.
The new mex condition says $c_{t+1}(u)\ne l$. The established two-step
inequality forces $c_{t+1}(u)<l$. This is the required strict-drop witness
one time earlier, with a strictly smaller colour. At time zero a strict
drop begins above zero. Induction therefore yields $k\geq t+1$.
For $t\geq1$, $k\leq\deg(v)$, so the displayed local deadline follows.
Every periodic orbit must have equality in the two-step inequalities,
giving periods dividing two. Neither directed graphs nor time-zero degree
bounds were smuggled into the argument.

### Sharpness part

The author's graph has $d+2+\binom{d+1}{3}$ vertices and maximum degree $d$.
In the simultaneous orbit formula an anchor of colour $j$ sees its lower
clique colours and an extra chain colour at least $j+1$, so it stays fixed.
At $v_k$, $k\geq2$, the anchors force all colours below $k-1$, and only the
left chain neighbor determines whether the mex is $k-1$ or $k$. The right
neighbor cannot alter either alternative. At the base, the $u,w$ pattern
starts the alternating drop at $v_1$ at time two. The formula propagates
that signal by one chain position per round.

In particular the final chain vertex has different colours at times $d-1$
and $d+1$, while the universal deadline gives equality from time $d$.
Thus the entrance time is exactly $d$. The stated edge example handles
$d=1$; the nonempty edgeless and empty graphs have entrance maxima one and
zero respectively. The proof is simultaneous induction, not an assumption
that anchors stay fixed followed by a circular use of that assumption.

### Inverse part

The forbidden-palette upper bound is correct and the all-zero target
attains it. If equality held at a different target, all used source
vertices would have a single forbidden colour. At a nonzero target
coordinate, assigning its inputs nonzero colours outside those singletons
produces an allowed assignment with missing zero, a contradiction. The
$q\geq3$ hypothesis is necessary for this step. The binary edge is an
actual boundary counterexample to a uniqueness claim without it.

## 2. Primary-source subtraction and exact double-cover adapter

Primary source inspected: Stephen T. Hedetniemi, David P. Jacobs and
Pradip K. Srimani, *Linear time self-stabilizing colorings*, Information
Processing Letters 87 (2003), 251--255,
[DOI 10.1016/S0020-0190(03)00299-0](https://doi.org/10.1016/S0020-0190(03)00299-0).
Page 252 explicitly specifies serial moves. Algorithm 2.1 uses the same mex
value after shifting colours by one. Page 253, Lemmas 4--6 establish
persistent properness, at most one initial increasing move, and a per-node
move bound; Theorem 1 bounds total moves by $n+2m$. These are prior inputs,
not synchronous-round statements.

Here is the reviewer's exact adapter, rather than an analogy. Let the
bipartite double cover of $G$ have vertices $(v,0),(v,1)$ and edges
$(v,0)(u,1)$ whenever $uv\in E(G)$. Start the two parts at $(c_0,c_1)$,
where $c_1=F(c_0)$. This is a proper coloring of the cover: across an edge,
$c_1(u)$ cannot equal $c_0(v)$. Updating all of part zero gives $c_2$;
updating all of part one gives $c_3$; alternating continues the original
Jacobi orbit, split by parity.

Each part is independent, so one whole-part update can be executed in any
serial vertex order without changing its result. A no-op can be skipped,
matching the guard in Algorithm 2.1. At a proper cover state, the old colour
of a vertex is an available choice, so its mex never increases. Each move
preserves properness. After both parts have been refreshed, all local
colours obey the degree bound even when the original palette allowed
larger colours. Finite descending palettes then force eventual stability
of the cover under the alternating fair schedule. A stable cover pair
$(a,b)$ satisfies $F(a)=b$ and $F(b)=a$. Consequently the generic
eventual-period-two mechanism is inherited through this adapter.

The sharp $\Delta$ deadline needs more. A bounded number of changes of a
coordinate alone permits those changes to occur late, triggered by other
coordinates. The candidate's earlier-time/lower-colour witness rules out
that delay. This induction is mathematically sound but is not literally
Lemmas 4--6 or the stated $n+2m$ total-move bound. The bounded source search
did not settle an exact owner of the full sharp deadline, and a non-hit is
not novelty evidence. No exaggerated direct-owner kill is used here.

## 3. Why the inverse axis does not survive mechanism subtraction

Read P118's actual Section 3.1, including the absence constraints, the
forbidden sets $B_h(y,J)$ and the product over independent source vertices
in its inclusion--exclusion proof. The current forbidden-palette product
is the same elementary counting step before imposing lower-colour presence.
Changing multipartite complements to arbitrary input sets does not create
a different inverse mechanism.

The following stronger statement makes the transfer explicit. Let $U$ be
any finite source-coordinate set, $W$ any finite target-coordinate set,
and choose arbitrary sets $S_v\subseteq U$ for $v\in W$. Define
$$M(c)(v)=\operatorname{mex}\{c(u):u\in S_v\}$$
with $q\geq\max\{3,1+\max_v|S_v|\}$, interpreting the maximum over no
target coordinates as zero. Let $s$ count source coordinates appearing in
none of the $S_v$. Then, over all targets, the largest fibre of $M$ is
$$q^s(q-1)^{|U|-s},$$
uniquely at the all-zero target. There is no undirectedness, common vertex
set, symmetry, graph geometry, or dynamical assumption in this statement.

Proof of this review comparison: at source $u$ define
$B_u(y)=\{y(v):u\in S_v\}$. Its palette must avoid $B_u(y)$, giving
$|M^{-1}(y)|\leq\prod_u(q-|B_u(y)|)\leq q^s(q-1)^{|U|-s}$.
At zero, exactly the used coordinates must avoid zero, so equality holds.
If any used coordinate has two forbidden values, its upper bound is strict.
Otherwise all used coordinates have a forbidden singleton. For any nonzero
target $y(v)$, an empty $S_v$ is impossible; if $S_v$ is nonempty, choose
at every $u\in S_v$ a positive colour outside its forbidden singleton,
which is possible because $q\geq3$. Extend using any allowed colours.
This assignment meets every absence condition but has mex zero at $v$.
Hence equality fails at every nonzero target. The empty target-coordinate
set has only one target and is included. This proves the comparison.

This generalization is evidence that GM's inverse result is a generic
local-mex palette envelope, not a proposed new replacement candidate. It
does not invalidate the formula. It removes it as the materially different,
nontransferable inverse contribution required by this batch's gate.

## 4. Claims matrix after subtraction

| Claim | Correctness | Contribution ceiling |
|---|---|---|
| Same local mex rule on arbitrary undirected graphs | Valid | Classical local correction; P118 already uses the same synchronous rule on a restricted class |
| Two-step descent and eventual periods dividing two | Valid | Proper-cover/serial mex mechanism through the explicit adapter; zero standalone engine credit |
| Local degree deadline and every-degree sharpness | Valid | Plausible temporal residual; do not assert source absence or pretend per-node move bounds are time bounds |
| Unique maximum fibre $q^s(q-1)^{n-s}$ | Valid | Generic incidence-mex forbidden-palette argument, transferring the P118 absence-counting skeleton |
| Two surviving materially separate new axes | Not established | Fails current admission gate |

P118's two-round clock on complete multipartite graphs does not by itself
prove GM's degree clock on all graphs. Conversely, broadening the same
literal rule's graph carrier is not enough to pass the occupied-mechanism
gate. Even granting the full sharp deadline as a surviving temporal axis,
the inverse result leaves this candidate below the required two-axis bar.

## 5. Independent checks and remaining obligations

verify_gate.py exhausts all 76 labelled simple graphs through four vertices,
with two admissible palettes each, totaling 34,867 graph/palette/source
instances. It uses an orbit-until-repeat detector, tests every local
deadline, and serializes the exact cover adapter. It separately exhausts
531 arbitrary directed/looped incidence systems through three coordinates,
20,228 sources, confirming that the inverse mechanism extends beyond graphs.
The symbolic sharp-graph construction is checked at every time through
$2d+5$ for $2\leq d\leq16$. The degree-one and binary uniqueness boundary
are included.

Two real fresh subprocesses produced byte-identical raw stdout, with empty
stderr and return codes zero. Each made 3,804,852 assertions. CANONICAL.json
is the actual raw output, 2799 bytes, SHA-256
`37ad2ae57e682f81b21ff7af1562af6bfed4e64601fa34c1eb9ee5dc3b747d4e`.
The incidence checks are mechanism-falsification pressure, not a proof of
originality. The mathematical deductions above, not enumeration, support
the correctness and value findings.

No author repair is requested to make a false theorem true. Admission would
require a genuinely nontransferable additional structural/inverse result;
increasing the exhaustive cutoffs or adding generic inclusion--exclusion
is not a remedy. No such new work was authorized or performed by this gate.
The current candidate should be closed without assigning a paper seat.
