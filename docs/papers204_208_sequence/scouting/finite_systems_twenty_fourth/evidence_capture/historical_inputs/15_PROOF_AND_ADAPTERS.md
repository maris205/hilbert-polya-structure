# Desk proof package and exact subtraction adapters

Author/contributor: `eighteenth_finite_scout`, 2026-09-06 UTC.
Status: **PROVABLE AS STATED for the subtraction statements below**.
Fresh admissible two-axis conjunction: **NOT CURRENTLY JUSTIFIED**.
This is not an independent candidate or manuscript review.

## Claim and assumptions

The six literal comparisons are exactly D1--D6 in [INTAKE.md](INTAKE.md).
No numerical experiment is used in any proof. A named algorithm and its
static inverse do not acquire new value by treating one invocation as a
time step. D1 is the classical double-reversal minimization theorem, with
the complete-DFA convention checked directly below. All empty cases follow the
intake conventions. The requested research claim is not that these familiar
facts are new, but that they fail the present admission gate after subtraction.

## Notation and dependency map

For a set family $\mathcal K$, $\min\mathcal K$ denotes its
inclusion-minimal members, and $\uparrow\mathcal K$ all sets containing at
least one member. For words, $\varepsilon$ is empty and $\operatorname{red}$
is free reduction. A fibre is an exact set of source states, not a list of
insertion descriptions counted with multiplicity.

1. D1: reversal subset separation plus unique canonically labelled minimum
   gives a retraction; language equality gives its complete kernel.
2. D2: the explicit block key gives strict refinement and the bounded-word
   behavioural equivalence; the old A01 adapter is literal identity.
3. D3: elementary transversal separation gives double blocker; redundant
   supersets give the complete inverse and extremum.
4. D4: a tagged bipartite nonincidence graph gives a literal bijective
   conjugacy to P106, not merely a quotient or resemblance.
5. D5: a quotient section gives idempotence; dependence-poset extensions give
   exactly the old static trace fibre.
6. D6: the cancellation diamond and length induction give normal-form
   uniqueness; pair count gives all forward time, independently of priority.

## 1. D1 is Brzozowski canonicalization, not an iterative extension

Let $L(\mathcal A)$ be the accepted language. The classical double-reversal
theorem, in the complete-DFA convention, says that reachable
determinization after two reversals yields the minimum DFA of
$L(\mathcal A)$. Empty reachable subsets are retained to represent a dead
state when necessary. Thus the output has no more states than $\mathcal A$.
The accessible carrier is closed under D1. An empty alphabet leaves only
one reachable state and causes no exception.

Here is a direct check of that convention. For any accessible deterministic
$\mathcal B$ with initial state $i$, distinct subset states $P,Q$ of
$D(R(\mathcal B))$ are distinguishable: choose
$p\in P\mathbin\triangle Q$ and a word $u$ with $\delta(i,u)=p$.
In the reversed automaton, reading $u$ backwards from a subset reaches
the sole final state $i$ iff the subset contains $p$. Thus the two subset
states accept different suffixes. They are all reachable by construction,
so the resulting DFA is minimal. Indeed, reachable states accepting
different suffix languages cannot be identified in any deterministic
recognizer of the same language. Apply this argument first to $\mathcal A$
and then to the accessible deterministic $D(R(\mathcal A))$. Reversal
reverses the accepted language, so the second minimum recognizes
$L(\mathcal A)$. Retaining the empty subset changes no distinguishing
argument and supplies the required dead state. The minimum cannot exceed
$\mathcal A$'s size because $\mathcal A$ is itself a recognizer.

The minimum DFA of a regular language is unique up to initial-state,
transition and final-state preserving isomorphism. Ordered breadth-first
labelling removes that isomorphism freedom. Writing $M(L)$ for this unique
representative, the literal D1 map is

$$T(\mathcal A)=M(L(\mathcal A)).$$

It preserves language. Consequently $T^2=T$, and

$$T(\mathcal A)=T(\mathcal B)\iff L(\mathcal A)=L(\mathcal B).$$

The recurrent states are precisely these minimum representatives, and the
predecessors of one are all bounded presentations of the same language.
That is a canonical-section kernel, not a separate temporal mechanism.
No numerical count of those presentations is claimed.

The old P122--126 replacement A02 is **not** D1: its parity-gated language
reversal is a different literal. It supplies historical owner pressure only.
D1's decisive exclusion is the direct named minimization theorem, not a
false claim of conjugacy to A02.

## 2. D2 is exactly old A01, including arbitrary initial partitions

Write $E$ for the equivalence relation of $\Pi$, and $E_t$ for that of
$T^t(\Pi)$. The literal key gives

$$pE_{t+1}q\iff pE_tq,\quad c(p)=c(q),\quad
\delta(p,a)E_t\delta(q,a)\text{ for every }a\in\Sigma.$$

For every integer $t\ge0$, induction on $t$ gives the exact expression

$$pE_tq\iff
\begin{cases}
\delta(p,w)E\delta(q,w)&\text{for all }|w|\le t,\\
c(\delta(p,w))=c(\delta(q,w))&\text{for all }|w|<t.
\end{cases}$$

At $t=0$ the first line is $pEq$ and the second has no words. For the
induction step, the old-equivalence conjunct retains the empty word and
all previous constraints; the successor conjunct prepends each letter and
therefore supplies precisely all new words of the claimed lengths. The
colour conjunct supplies the empty word in the second line.

Every nonfixed step increases block count. Hence the depth from $\Pi$ is
at most $|Q|-|\Pi|$. A fixed partition is exactly a right-invariant
equivalence refining both the initial partition and the colour partition.
Any such equivalence refines every $E_t$ by the displayed formula, so the
terminal one is the greatest such relation. No strict periodic cycle is
possible. For $Q=\varnothing$ the unique partition is fixed and the bound is
zero; for empty $\Sigma$ one step merely intersects with the colour kernel.

Replacing blocks by their integer names preserves equality of keys, so the
identity on partitions intertwines D2 with A01 in the original
`docs/papers122_126_sequence/scouting/replacement/SCOUT.md`. This is exact
literal duplication. The later MOORE negative scout confirms prior failed
intake, not an independent theorem. P126's composition splitting is only a
related refinement mechanism; no conjugacy to P126 is asserted.

## 3. D3: complete blocker fibres do not restore the consumed clock

Let $E=[n]$ and let $b(\mathcal H)$ denote all inclusion-minimal sets
meeting every member of $\mathcal H$. Our conventions give
$b(\varnothing)=\{\varnothing\}$ and
$b(\{\varnothing\})=\varnothing$.

### 3.1 Double blocker and the entire temporal statement

Put $\mathcal K=\min\mathcal H$. Every member of $\mathcal H$ contains a
member of $\mathcal K$, so a set hits $\mathcal H$ iff it hits
$\mathcal K$. Thus $b(\mathcal H)=b(\mathcal K)$.

For a clutter $\mathcal K$ and any $S\subseteq E$,

$$S\text{ hits every member of }b(\mathcal K)
\iff S\in\uparrow\mathcal K.$$

For the backward implication, choose $K\in\mathcal K$ contained in $S$;
every transversal meets $K$. For the forward implication by contraposition,
if $S$ contains no $K\in\mathcal K$, the complement $E\setminus S$ meets
every such $K$ and, by finiteness, contains a minimal transversal disjoint
from $S$. This reasoning includes the two empty clutters under the stated
conventions. Taking minimal sets gives $b^2(\mathcal K)=\mathcal K$.
Therefore

$$b^2(\mathcal H)=\min\mathcal H,\qquad b^3=b.$$

The periodic states are exactly clutters, and each has period one or two.
A nonclutter has depth exactly one. At $n=0$ both families are clutters;
at $n\ge1$ a nonclutter exists, so the global depth is one. This is exactly
the old HBN map and its blocker-normalization proof, without relabelling.

### 3.2 Every target and sharp maximum, entirely static

A nonclutter target has no predecessor. For a clutter target $\mathcal C$,
put $\mathcal K=b(\mathcal C)$. Double blocker gives

$$b(\mathcal H)=\mathcal C
\iff\min\mathcal H=\mathcal K
\iff\mathcal K\subseteq\mathcal H\subseteq\uparrow\mathcal K.$$

For the final equivalence, minimal members must be included, and every
other member must contain one. Conversely these two containments prevent
any added set from becoming a new minimal member. All sets in
$\uparrow\mathcal K\setminus\mathcal K$ are independently optional. Hence

$$|b^{-1}(\mathcal C)|=2^{|\uparrow b(\mathcal C)|-|b(\mathcal C)|}.$$

For $n\ge1$, $\mathcal C=\varnothing$ has
$\mathcal K=\{\varnothing\}$, giving the fibre $2^{2^n-1}$. If
$\mathcal K=\varnothing$, the exponent is zero. If $\mathcal K$ is
nonempty and differs from $\{\varnothing\}$, then its upward closure omits
$\varnothing$, so its exponent is at most $2^n-2$. Thus the empty target is
the **unique** maximum for $n\ge1$. At $n=0$ the two singleton fibres tie.

The inverse and extremum are useful explicit deductions, but consist only
of choosing redundant supersets over the classical minimal core. They do
not form a new second axis for the exact old HBN system.

## 4. D4 is exactly P106 on a bipartite graph

Make disjoint tagged copies of $X$ and $Y$. Define the simple bipartite graph
$G$ by $xy\in E(G)$ iff $(x,y)\notin I$, with no edges within a side.
The map $h(A,B)=A\sqcup B$ is a bijection from $2^X\times2^Y$ to
$2^{X\sqcup Y}$.

For $x\in X$, membership in the P106 output $F_G(h(A,B))$ means that $x$
has no neighbour in $B$. By construction this is equivalent to
$(x,b)\in I$ for every $b\in B$, which is $x\in B'$. The corresponding
calculation for $y\in Y$ gives $y\in A'$. Therefore

$$F_G\circ h=h\circ T.$$

This is a literal conjugacy for every context, including empty sides, not a
restriction to symmetric incidence. It transfers the entire P106
bipartite functional graph and all fibre questions. In particular the
polarity identities give $T^3=T$ and depth at most one.

One may write the static inverse as

$$T^{-1}(C,D)=\{A\subseteq X:A'=D\}\times
\{B\subseteq Y:B'=C\}.$$

For example, inclusion-exclusion gives

$$|\{A\subseteq X:A'=D\}|=
\sum_{S\subseteq Y\setminus D}(-1)^{|S|}2^{|(D\cup S)'|}.$$

To justify this expression, restrict first to $A\subseteq D'$ so all of
$D$ is common. For each $y\notin D$, exclude the event $A\subseteq y'$;
an intersection of the events indexed by $S$ has exactly
$2^{|(D\cup S)'|}$ subsets. This finite inclusion-exclusion also handles
unrealizable $D$ by yielding zero. It is old static incidence counting and
does not evade the exact conjugacy.

## 5. D5 is a trace quotient section with static heap fibres

Let $q:\Sigma^n\to\mathcal T_n$ be the quotient by the equivalence relation
generated by the allowed adjacent commutations. Since each class is finite
and nonempty, its least word defines a section $s$ with $q\circ s=1$.
The literal map is $T=s\circ q$. It follows directly that
$T^2=sqsq=sq=T$, and $T(u)=T(v)$ iff $q(u)=q(v)$.

For completeness, label each occurrence of a letter by its ordinal among
that letter's occurrences. Given a word $w$, order two occurrences whenever
the first is earlier in $w$ and their letters are dependent (not in $J$),
then take transitive closure. This is an acyclic dependence poset. Swapping
adjacent independent letters preserves it. Conversely, two linear
extensions of a finite poset can be connected by adjacent swaps of
incomparable elements: move the first element of the desired extension
leftward through the present one; every crossed element is incomparable,
and induct on the remaining suffix. In this poset incomparable occurrences
have independent labels. Hence the words of the trace are exactly its
linear-extension readings.

Repeated equal labels cause no overcount: since $J$ is irreflexive, all
occurrences of any one label form a chain. The $k$th occurrence in a reading
must therefore be the tagged $k$th occurrence. The reading determines its
extension uniquely. Thus a normal target's fibre is the number of linear
extensions of its dependence poset; a nonnormal target has no predecessor.
The $n=0$ empty word is fixed and has one predecessor.

This is the explicit Cartier--Foata/heap equivalence, followed by choosing
a representative. No identity with old CRP radix sorting is asserted.
CRP and the old RSK retraction are mechanism-level warnings: static
canonical-section fibres were already insufficient for a seat. D5 has no
new temporal axis even if a particular poset's extension count is difficult.

## 6. D6 changes a free-reduction schedule only

An elementary cancellation deletes $aa^{-1}$. Any two cancellations from
one word have the following diamond. Disjoint pairs can both be deleted in
either order with the same resulting word. Overlapping pairs form
$aa^{-1}a$, and either deletion leaves the same letter $a$. Thus the two
one-step outputs coincide or have a common one-step descendant.

Every cancellation lowers length by two. Strong induction on length proves
unique terminal reduction: for two first steps, use the diamond and apply
the induction hypothesis to the shorter first-step outputs and their
common descendant. Both terminal words must coincide. A word already
reduced is the induction base. Consequently the leftmost schedule reaches
$\operatorname{red}(w)$, as does the old parallel PFR schedule.

Since D6 deletes exactly one pair at each nonfixed step, its exact clock is

$$\tau(w)=\frac{|w|-|\operatorname{red}(w)|}{2}.$$

Its maximum over words of length at most $N$ is $\lfloor N/2\rfloor$,
attained by $(aa^{-1})^{\lfloor N/2\rfloor}$; this includes $N=0,1$.
Every reduced word is fixed and no other recurrent state exists.

For a target word $v$ of length $m$, the complete one-step predecessor set
is obtained as follows. Include $v$ itself exactly when it is reduced.
If $m+2\le N$, for every gap and every letter $a$ insert $aa^{-1}$, retain
the resulting source exactly when its leftmost cancelling pair is the
inserted pair, and take a **set union** of retained sources. This is an iff:
any nonfixed predecessor determines its deleted pair and gap, and each
retained insertion is deleted back to $v$. Duplicated insertion
descriptions are not counted twice. This is the elementary cancellation/
insertion relation from free-group rewriting, merely priority-filtered.
No closed sharp one-step maximum is claimed.

The endpoint map $w\mapsto\operatorname{red}(w)$ is identical to the old
PFR endpoint. D6 and PFR are not claimed conjugate as one-step maps: their
clocks differ. The time change supplies only a generic count of deletions,
and the endpoint fibres are the same old normal-form classes. This cannot
reopen the permanent free-reduction failure.

## Corrections, value gaps, and final disposition

No computational conjecture is promoted. D1's direct convention check is a
rederivation of the classical theorem, not a novel theorem. D2 has
no new extremal inverse result. D5 has no new nontrivial time axis. D6 has
no sharp one-step inverse extremum. D3 and D4 have completely explicit
adapters and no unconsumed temporal contribution. A static hard counting
problem does not repair any of these failures.

**NO_FRESH_SLATE / SIX COMPARISON GROUPS / ZERO_EXECUTED / NO_PROMOTION.**
No paper number, reserve, independent review or P208 conclusion follows.
