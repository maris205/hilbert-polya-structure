# P209 B — independent deductive and source review

Reviewer `/root/p209_b_reviewer`, 2026-09-07 UTC. Status:
**PROVABLE AS STATED** for the three frozen manuscript theorems, at the
unchanged narrow internal note ceiling. This is manuscript Review B, not
candidate-gate reuse. All source paths below are relative to the physically
pinned `papers/209-ordered-fibre-threading/frozen_round1/` unless stated.

## Exact claim, assumptions and proof dependency map

The state space is every function $f:[n]\to[n]$, with $[n]=\{0,\ldots,n-1\}$,
including the unique empty function. At each epoch every old fibre
$\{i_1<\cdots<i_k\}=f^{-1}(v)$ is simultaneously threaded by
$Tf(i_j)=i_{j+1}$ for $j<k$ and $Tf(i_k)=v$. Labels are retained, loops
permitted, and fibres are never recomputed during a step.

Theorem 1 claims precisely the recurrent cycle/unbranched-feeding-path
carrier with each final noncycle label below every label on its cycle,
attachment rotation and attached-cycle LCM least period. Theorem 2 is the
all-target bijection from admissible increasing-arrow selections to one-step
predecessors. Theorem 3 is the unique cyclic-successor maximum $2^{n-1}$ for
$n\ge1$, with $n=0$ separate. There is no sharp entrance clock or all-time
inverse claim. The third theorem belongs to the inverse axis, not a third
independent mechanism.

B's dependency map is: literal arrow substitution -> monotone full vertex
reachability -> frozen reachability on recurrent orbits -> sibling-on-cycle
necessity -> complete path carrier -> explicit attachment rotation and exact
period. Separately: local continuation/terminal port capacities -> triangular
source reconstruction -> bijection -> independent product bound/equality.
No finite experiment or outside convergence theorem is a premise.

## 1. Monotone reachability proof of full recurrent necessity

For a vertex map $f$, let $R_f$ be its reflexive reachability relation:
$(u,v)\in R_f$ if $f^r(u)=v$ for some integer $r\ge0$. Every old edge
$i_j\to v$ is replaced by the directed walk
$i_j\to i_{j+1}\to\cdots\to i_k\to v$. It is a positive-length walk even
when $v$ occurs earlier in that fibre; simplicity is not required.
Concatenating replacement walks proves $R_f\subseteq R_{Tf}$.

Suppose $T^p f=f$. Applying these inclusions around the $p$-cycle yields
$R_f=R_{Tf}=\cdots=R_{T^{p-1}f}$. This freezes a labelled binary relation,
not just a rank or an unlabelled graph. At any epoch take consecutive
distinct siblings $u<v$ with $f(u)=f(v)=w$. The new edge $u\to v$ lies in
$R_{Tf}=R_f$. Because $u\ne v$, old reachability from $u$ to $v$ uses at
least one edge, so $w$ reaches $v$ in the old graph. Together with
$v\to w$ this places $v$ on an old vertex cycle. The special case $v=w$
is an old self-loop and is covered without pretending the numerical head
changed. Thus every member of any fibre after its first lies on a cycle.

A fibre has at most one cyclic member. Indeed, a cyclic vertex maps to the
next vertex on its own cycle, and that cycle has exactly one cyclic
predecessor at each vertex; another cycle cannot feed into it. Hence a fibre
has size at most two. A double fibre has a smaller noncyclic member and a
larger cyclic member. In particular, every noncycle vertex has indegree at
most one, and every cycle vertex has at most one extra noncycle predecessor.
All noncycle vertices eventually reach a cycle because the carrier is finite;
tracing their predecessors backwards, indegree at most one and absence of
noncycle cycles partition them into disjoint unbranched feeding paths.
The doubled-fibre bound gives at most one path at each cycle vertex.

Every cycle predecessor is maximal in its fibre, so its arrow is retained.
An internal-path target has a singleton fibre, so its incoming path arrow
is retained too. If final path vertex $a$ currently points to $c$ and $p$
is the fixed cycle predecessor of $c$, the fibre is $(a,p)$; therefore
$Tf(a)=p$. At every epoch the necessary double-fibre order gives $a<p$.
Iterating the same conclusion visits every predecessor label of the fixed
cycle. Hence $a<\min C$. This proves necessity without using the author's
frozen-height/head-height argument. Reflexive reachability here is used as
a monotone global relation, not A's positive-walk SCC carrier classifier.

The structural conclusion also proves preservation of the cycle order at
all recurrent epochs, so no hidden relabelling or component permutation
has entered the argument. For general states, component vertex sets are
preserved: each new edge stays inside an old component, while the old-edge
replacement walks keep each old component connected. This familiar
path-substitution primitive is credited background.

## 2. Sufficiency and exact period

Assume the stated cycle/path carrier and $a<\min C$ at every path end.
Each occupied cycle target has precisely the two incoming labels $a<p$;
the literal rule preserves the cycle predecessor arrow and moves the
path-end attachment to $p$. Every internal arrow is unchanged. Distinct
attachments remain distinct because cycle-predecessor is a bijection, and
the label inequalities persist. Thus this carrier is invariant and every
configuration returns after a common multiple of its attached cycle lengths.

For an attached cycle of length $\ell$, choose one particular labelled
final vertex $a$. Its image visits all $\ell$ distinct cycle vertices in
order before first return. Therefore the component's least return time is
exactly $\ell$, even if its unlabelled attachment pattern is symmetric.
A pure cycle has only singleton fibres and is fixed by $T$, not rotated
as a whole-function state. The components act independently on disjoint
preserved label sets. Consequently the least global return is the LCM of
exactly the attached cycle lengths. A loop contributes one and the empty
LCM is one; both the empty function and the singleton function are fixed.

B's checker constructs this expected carrier from all choices of cyclic
core, all permutations on that core, and all ordered path slots for the
remaining labels; it does not classify the input graph by stripping or
SCCs. Actual recurrence is instead obtained from the stable image of the
entire $T$-state map. The latter is exactly its recurrent set: at stability
the finite restriction is surjective and hence bijective, whereas an orbit
outside the stable image cannot be periodic. Direct first-return paths then
measure actual least periods. These are supplementary finite checks.

## 3. Independent inverse proof through local ports

Fix a target $g$. For each target value $v$, its incoming arrows
$i\to v$ are assigned one of two typed ports: continuation $C$ or terminal
$D$. Each port has capacity one. Continuation is permitted only for $i<v$.
Terminal has no order restriction. Choices at different values $v$ are
independent. For a global valid port assignment define a source by descending
substitution, from $i=n-1$ down to $0$:

$$f(i)=\begin{cases} f(g(i)),&i\text{ has type }C,\\
g(i),&i\text{ has type }D.\end{cases}$$

The continuation case is triangular, since $g(i)>i$ has already been
assigned. Iterating continuation reaches a terminal in finitely many
steps. No two continuation chains merge: a merge would use one continuation
port twice. Thus these chains are disjoint increasing paths, with isolated
vertices allowed. Distinct chains terminate at distinct terminal arrows,
and terminal-port capacity says their terminal $g$-values are distinct.
Substitution gives a common source value precisely along each chain, with
different values on different chains. Threading these source fibres restores
each continuation arrow and each terminal arrow, so $Tf=g$.

Conversely any genuine predecessor assigns type $C$ to every nonmaximal
member of an old fibre, and $D$ to its maximum. Consecutive old fibre
members increase, no two continuation arrows have the same head, and the
terminal arrows retain distinct fibre values. Hence the local port rules
hold and substitution recovers that predecessor. This proves all-target
surjectivity, including unsupported targets.

For injectivity, from the reconstructed source and fixed target recover
the type at $i$: it is $C$ exactly when $i<g(i)$ and $f(i)=f(g(i))$.
The forward implication follows from substitution. If $i$ were terminal
while both conditions held, it would have a larger same-fibre member
$g(i)$, contradicting its being the fibre maximum. Thus assignments are
uniquely recoverable. Equivalently the nonmaximal positions of the source
recover the manuscript's selected set. The example $f=g=(1,1)$ has type
$C$ at 0 despite no numerical change; type is not a change mask.

This proves exactly the manuscript decoder after identifying $C$-typed
positions with its selected set. Theorem 2's two distinctness conditions
are the two port capacities. It does not use the recurrent classification.
For $n=0$, the empty product of local choices is one and substitution
produces the unique empty predecessor.

## 4. Reviewer-only local product check and original extremum

This paragraph is B's verification route, not an addition to the manuscript
contract or a novelty claim. Put $A_v=\{i:g(i)=v\}$. The number $c_v$ of
local port assignments is zero if $|A_v|>2$, or if at least two arrivals
are nonascending ($i\ge v$). In the other cases: $c_v=1$ for an empty
arrival set; $c_v=2$ for a nonempty arrival set all of whose labels are
less than $v$; and $c_v=1$ when exactly one arrival is nonascending.
These statements follow by placing up to two arrows into two capacity-one
ports, with the nonascending arrow forced terminal. Independence and the
bijection above give $|T^{-1}(g)|=\prod_v c_v$. Every positive fibre is
therefore a power of two. This elementary factorization receives no extra
contribution axis.

For $n\ge1$, $c_0$ cannot be two, so the product is at most $2^{n-1}$.
Equality forces $c_v=2$ for each $v\ge1$ and $c_0=1$. Thus every positive
target $v$ has at least one incoming arrow, all strictly ascending. The
largest source label $n-1$ must map to zero because it cannot supply any
positive target. At least $n-1$ arrows are already needed for the positive
targets; only $n$ source arrows exist. Hence zero has exactly one arrival
and every positive target also has exactly one. The target map is a
permutation with all lower labels ascending. Successively filling target 1,
then 2, and so on forces $g(0)=1,g(1)=2,\ldots,g(n-2)=n-1$, leaving
$g(n-1)=0$. Conversely this cyclic-successor map has one ascending arrival
at every positive target and one terminal arrival at zero, so its product
is $2^{n-1}$. The $n=1$ and empty cases give one. This independently
recovers Theorem 3 and excludes any missing equality family.

## 5. Hostile attack on the actual author and A proofs

After code/design commitment, I read the complete author PROOF_PACKAGE.md,
all manuscript TeX, author verify.py, A's full SOURCE_AND_PROOF/REPORT,
verify.py, replay/build records and actual accepted delta/current census.
The frozen-height proof in the manuscript is valid: it first proves every
$I_r(f)\subseteq I_r(Tf)$ by taking the final $r$ arrows of a replacement
walk, then uses periodicity to freeze labelled sets and hence vertex
heights. A finite-height arrow raises height strictly; only infinite-height
arrows can give equality. Using that single frozen height function, head
heights along a periodic source coordinate cannot strictly drop. The
next-sibling/cycle implication thus also holds when the next sibling equals
the old head. It is not an invalid comparison of changing height functions.

Other attempted objections fail for stated reasons: internal feeding-path
labels need not increase; only final labels are constrained. Distinct
attachments cannot collide under a permutation of cycle targets. The LCM
is exact because a fixed final label must return, not merely an unlabelled
shape. Selected-head distinctness alone would permit different inverse
paths to merge as old fibres; endpoint-value distinctness prevents exactly
that defect. Both decoder conditions are essential. Empty and singleton
cases are explicit. The unique maximum proof does not assume equality of
fibre size with the unconstrained Boolean count unless equality in both
bounds has actually been established.

I found no mathematical or evidence-based reason to request manuscript
changes. This conclusion remains revisable on a concrete counterexample
or a complete applicable owner adapter; numerical agreement is not proof.

## 6. Primary bodies and bounded source subtraction

I directly read the following saved primary bodies in complete indicated
sections, not snippets or the author/A summaries. The physical copies are
part of all 2,004 INPUT_PINS. Line locators refer to saved extracted text,
not certified PDF-page anchors; no source-PDF visual-reading claim is made.

| Bibliography record and actual read | Exact subtraction and scope |
|---|---|
| Onus–Richa–Scheideler, `source_context/workspace/docs/papers204_208_sequence/scouting/finite_systems_nineteenth/public_sources/linearization-ALENEX07.txt`, lines 1–470; 241–350 was reread after a combined tool-output truncation | Complete model, Algorithm 1, §2 convergence proof and §3 memory variant; start of §4 only. Connected undirected graph, separate left/right phases and add-wins conflict convention. Ordered star-to-chain rewiring and old-edge walk substitution are prior primitives. The sorted-list theorem is not the full directed-endofunction recurrence theorem here. |
| Cramer–Fuhrmann, same directory `isprp_correctness_2005.txt`, lines 1–595 | Complete §4 and §§5.1–5.3 plus model/conclusions opening. Every pointer repair replaces successor $c$ by $b$ in the clockwise interval from $a$ to $c$; flooding also only shortens. The final sign in Lemma 7's displayed inequality contradicts its preceding cases; I use only those explicit rules/cases for the nonincrease test, not an imported correctness theorem. |
| Shaker–Reeves, `source_context/workspace/docs/papers204_208_sequence/scouting/FTH_GATE/public_sources/rn_TR2005_25.txt`, lines 1–414 | Complete §4/Figure 3 and §5.1, with model; only opening §5.2. Action a1 minimizes successor distance over a set containing the existing successor; actions a2–a7 do not replace successor slot zero. Bootstrap/neighbour arrays/messages remain part of their state. The acyclic functional-graph subcase in their convergence discussion is not needed as a premise here. |
| Aradhya–Scheideler v1, same directory `tree_path_selected_sections.txt`, all 259 lines | Complete selected §1.3, §3.4, Algorithms 10–13 and Appendix B. Rooted undirected trees carry depth-parity labels; the sequential transformation uses parent/sibling/grandchild cases. Distributed operation adds advice, supervisor and message/timer state. Sibling rewiring and tree-to-path construction are prior; repeated threading on arbitrary cyclic endofunctions is not that literal input/output specification. Apparent $u/v$ pseudocode typos are not silently repaired into premises. |

For both ring comparisons, the loop-free literal witness
$(1,2,1)\mapsto(2,2,1)\mapsto(1,2,1)$ raises vertex 0's clockwise distance
from 1 to 2 in its first step. It cannot be a literal successor-shortening
step or a batch consisting exclusively of such steps on the same labelled
pointer state. This does not exclude all conjugacies, projections,
unfair schedules or enlarged states. The tree input mismatch likewise
defeats the stated literal adapter, not every abstract construction.

All four bibliography metadata records were independently opened live:
[SIAM](https://epubs.siam.org/doi/10.1137/1.9781611972870.10),
[KIT](https://publikationen.bibliothek.kit.edu/1000003169),
[NCSU original](https://techrep.csc.ncsu.edu/2005/TR-2005-25.pdf), and
[versioned arXiv](https://arxiv.org/abs/2504.02448v1).
PRIMARY_METADATA_WEB.json preserves the complete second actual tool return;
the first equivalent four-page opening was not separately archived and is
not mislabelled as that saved call. SIAM's 2007 proceedings date, pages and
DOI agree (its 2013 online date is not substituted). KIT confirms 2005-5
and DOI, and the primary first page confirms the authors/date. NCSU's
departmental original confirms title/authors/institution; the exact report
identifier/year are bound by its official dated report URL. ArXiv confirms
version 1 of 3 April 2025. No latest-version claim is made. All citations
are attribution/comparison, not hidden proof premises. No broad new owner
search or reading of every linked work is claimed.

## 7. Internal originals and exact collision tests

All paths in this table start at frozen `source_context/workspace/`.

| Original read directly | Checked literal adapter and residual |
|---|---|
| `docs/papers172_176_sequence/scouting/fresh_geometry_automata/SCOUT_AND_KILL_LEDGER.md`, full file, D03/FSP | FSP closes each fibre to its minimum and forgets its destination, sending permutations to identity. P209 retains old destination and fixes every permutation. Same-kernel inputs $(0,0)$ and $(1,1)$ yield $(1,0)$ and $(1,1)$ with distinct next kernels. Neither P209 nor its next kernel is determined by the old kernel alone. |
| `docs/papers177_181_sequence/scouting/combinatorial_lane/SCOUT_AND_KILL_LEDGER.md`, lines 1–50, C05/NOG and context | Cyclic next-equal distances encode only equality partitions; retained absolute destination labels prevent that sufficient-statistic adapter. No full older-lane theorem audit is claimed. |
| `docs/papers204_208_sequence/scouting/combinatorial_second/PROOF_NOTES.md`, lines 1–70, complete PR section | PR reverses or retains old unordered edges. P209 $(2,2,2)\mapsto(1,2,2)$ creates $\{0,1\}$, absent before. This rejects the literal edge-preserving adapter, not every factor. |
| `papers/167-minimum-inverse-position-feedback/main.tex`, lines 1–255 | Exact rule and complete first-image component/recurrent proof: missing values default to their own coordinate; paths reverse or split and cycles invert. Whole-function recurrent periods divide two. P209 $(1,2,3,1)$ has period three by Theorem 1, excluding a full same-carrier conjugacy. No rereview of all P167 inverse arguments. |
| `docs/papers162_166_sequence/scouting/degree_feedback_jump/SCOUT.md`, lines 1–130 | DFJ stays on each old forward orbit and squares permutations. P209's all-2 example moves 0 to 1 outside old orbit $\{0,2\}$ and fixes permutations. Pointer-power and its root-counting mechanism are not relabelled as P209. |
| `papers/169-successor-transfer-set-partitions/main.tex`, lines 1–462 | Full literal, temporal and five-state inverse arguments in this range: only final repeated RGF occurrences move to the next block label. P209 changes nonfinal positions to absolute next positions, retaining the final value. Its $00\mapsto10$ leaves the RGF carrier. Load rotation, partition encoding and transfer-matrix bookkeeping are credited, not an accepted adapter to this literal map. |
| `docs/papers172_176_sequence/scouting/combinatorial_crossdomain/focused_nonextractive/IDEA_LEDGER.md`, full file, C01/MOC | MOC is a directional matching restriction of P169, not destination-sensitive threading. Generic rotation gives no extra P209 novelty credit. |

The strongest value objection is that the inverse is elementary local
path bookkeeping and the recurrent action is ordinary rotation once the
carrier is known. Those primitives receive zero separate credit, as do
the local port product and generic monotone-relation reasoning in this
review. What survives the checked literal subtractions is the exact
all-endofunction necessary-and-sufficient recurrent carrier coupled with
the independently derived target-complete inverse and unique equality
case. This supports only the assigned modest internal theorem-note contract.
It is not a broad novelty, priority, owner-nonexistence, venue-fit or expert
endorsement finding. Historical gaps and original failed evidence remain;
all OWNER_AMBER / HOLD_EXTERNAL limits continue.
