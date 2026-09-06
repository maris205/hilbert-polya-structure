# Root local proof contributions to FTH — no global admission claim

2026-09-06 UTC. Root read the actual nineteenth-lane [literal intake](finite_systems_nineteenth/INTAKE.md),
not a scientific output. These observations were sent to its author during
the bounded proof attempt. The author reports convergent component/fixed
tests written earlier; chronology and shared authorship must remain explicit.
No numerical producer or enlarged box is introduced here.

## Claim, assumptions and status

Let $f:[n]\to[n]$, with $[n]=\{0,\ldots,n-1\}$, including $n=0$.
For each nonempty fibre $f^{-1}(v)=\{i_1<\cdots<i_k\}$ define $g=T(f)$ by
$g(i_r)=i_{r+1}$ for $r<k$ and $g(i_k)=v$.
Every domain element lies in precisely one fibre, so the rule is total.

The following local statements are **PROVABLE AS STATED**. A complete
temporal/recurrent theorem, sharp clock and value clearance remain
**NOT CURRENTLY JUSTIFIED** by this note. These are not paper admission,
an independent review, or assertions of global novelty.

Write $d_f(j)=|f^{-1}(j)|$ and $I(f)=\operatorname{im}f$.
The proof strategy is to classify the two possible incoming-arrow types.
That classification yields the image and branch identities; separate fibre
inspection gives the fixed-state criterion and connectivity statement.

## 1. Exact indegree and image identity

For every $j\in[n]$,

$$d_{T(f)}(j)=\mathbf1_{j\in I(f)}+
\mathbf1_{j\ne\min f^{-1}(f(j))}.$$

Proof. For every nonempty old target fibre $f^{-1}(j)$, exactly one retained
arrow enters $j$, namely the arrow from its maximum. This accounts for the
first indicator. An inserted sibling arrow enters $j$ exactly when $j$ is
not the minimum of its own old fibre; its source is then the unique preceding
member in that fibre's increasing order. This gives the second indicator.
These source vertices cannot coincide. If the preceding sibling $i<j$
were also the retained source entering $j$, then $f(i)=j$ and
$f(i)=f(j)$, so $f(j)=j$. But $j$ would then lie in $f^{-1}(j)$ and be
larger than its alleged maximum $i$, a contradiction. The rule has no other
arrow types, proving the formula.

Consequently every state after one step has indegrees at most two, and

$$I(T(f))=I(f)\cup\{j:j\ne\min f^{-1}(f(j))\}.$$

In particular the image increases by inclusion, and a vertex with positive
old indegree cannot acquire zero indegree. These conclusions hold for every
step, not merely in a numerical box. All statements are vacuous for $n=0$.

## 2. Exact fixed-state criterion

$T(f)=f$ if and only if each nonempty fibre has size at most two and every
two-member fibre is $f^{-1}(v)=\{i,v\}$ with $i<v$ (hence $f(v)=v$).

Proof. In a fibre $\{i_1<\cdots<i_k\}$, equality of old and new arrows at
every nonlast member requires $i_{r+1}=v$ for every $r<k$. If $k\ge3$ this
would equate two distinct consecutive members to $v$. If $k=2$ the sole
requirement is $i_2=v$, yielding the stated condition; it is also sufficient,
because the last arrow already ends at $v$. Singleton fibres are unchanged.
This proves both directions, including the empty function.

This criterion alone does not prove that every orbit reaches a fixed state.

## 3. Weak connected components and backward arrows

Ignoring directions and loops, $f$ and $T(f)$ have exactly the same weak
connected-component vertex sets.

Proof. Each new sibling edge joins two vertices sharing an old target and
therefore stays in one old component. Retained edges do too, so no old
components merge. Conversely, for each old arrow $i_r\to v$, the new graph
contains the walk $i_r,i_{r+1},\ldots,i_k,v$. If $v$ is itself a fibre member,
this may repeat a vertex, but it still connects $i_r$ to $v$. Every old
connection persists as a walk, so an old component cannot split.

Let $B(f)=\{(i,f(i)):f(i)\le i\}$. Then $B(T(f))\subseteq B(f)$.
Every inserted sibling arrow has larger head than tail, and all other
arrows are retained old arrows. Thus an arrow in $B(T(f))$ must have been
retained from $B(f)$. No claim of strict decrease at every nonfixed step
follows.

## 4. Branch transport after the first step

Suppose all old indegrees are at most two, as is guaranteed after one step.
Each old branch target $v$ with $f^{-1}(v)=\{i<j\}$ creates a new branch
at $j$ if $d_f(j)>0$, and no new branch if $d_f(j)=0$. These are all new
branches, and different old branches give different candidate vertices $j$.

Proof. The second indicator in §1 is one precisely at the larger member
$j$ of a two-member fibre. Its sum with the first indicator equals two
exactly when $j\in I(f)$. A vertex $j$ belongs to one fibre only, so two
old branch targets cannot choose the same $j$. This proves the description.

Calling this a branch-transport rule is just terminology for the identity.
It does not show that a transported branch terminates or provide a clock.

## Open proof and source obligations

Image growth and backward-arrow loss may both stall. This note contains
no Lyapunov function strict at every nonfixed step, no exclusion of a
nontrivial recurrent component, and no all-size sharp witness. The nineteenth
author's separate increasing-path-cover inverse attempt is not proved or
adopted by this note. Exact graph-linearization/traversal literature and
historical FSP/PR adapters still require scrutiny before any value decision.
Root is a mathematical contributor if these deductions are used and cannot
independently review a resulting FTH paper. HOLD_EXTERNAL.
