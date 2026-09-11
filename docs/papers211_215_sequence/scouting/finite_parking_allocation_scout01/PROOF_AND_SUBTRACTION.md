# Elementary parkization: exact deductions and occupied mechanism

## Claim and status

**PROVABLE AS STATED** under the exact $n,M\ge1$ carrier and update in
[INTAKE.md](INTAKE.md). All recurrent points are fixed; the hitting time,
full labelled basin coordinates, every one-step inverse, basin census and
complete maximum-fibre equality cases below are proved.

**NO_PROMOTION_SOURCE_OCCUPIED_GAP_DELETION.** These deductions do not give
two residual research mechanisms. This is one literature-defined literal,
not a new map invention, admission, experiment or manuscript verdict.

Main author: /root/round211_finite_matching_scout. Child
parking_primary_screen checked the deductions without code and supplied
the useful explicit indegree formulation and its strict nonfixed bound.
Both roles are author-side mathematical assistance; no independent paper
review is claimed.

## Assumptions, notation and strategy

Positions of a word remain labelled. Sorting is a proof device, not a
different state space or an additional sorting step in $T$. Tied values
remain tied under every update. Let $b=w^{\uparrow}$ and put
$$C_i=\max\bigl(0,\max_{1\le r\le i}(b_r-r)\bigr),
\qquad z_i=b_i-C_i. \tag{1}$$
Write $h(w)$ for the first fixed-point time. The terminal labelled word
will be denoted by $u$, with sorted entries $z$.

Dependency map: the first deficient rank identifies an unchanged prefix
and a decreased suffix; this proves the clock and invariance of $z$.
Record maxima in (1) then identify constant-shift blocks and a bijection.
The bijection turns $T$ into first-positive gap deletion. All inverse and
enumeration formulas are derived inside those same coordinates.

## 1. Literal closure and exact time

If $d=d(w)\le n$, then $b_i\le i$ for $i<d$ and $b_d\ge d+1$.
Thus precisely the first $d-1$ sorted entries are at most $d$; all remaining
entries exceed $d$. The sorted updated word is
$$b'_i=\begin{cases}b_i,&i<d,\\b_i-1,&i\ge d.\end{cases} \tag{2}$$
For $d>1$, $b_{d-1}\le d-1$ while $b_d-1\ge d$, so (2) is still sorted
and does not merge unequal adjacent values across the cut. Decreased
values stay positive and never exceed $M$, proving finite-carrier closure.

Let $H_0(w)=\max(0,\max_i(b_i-i))$. If $H_0(w)>0$, every positive
deficiency occurs in the suffix of (2), so
$$H_0(Tw)=H_0(w)-1.$$ 
If $H_0(w)=0$, the word is a parking function and is fixed by definition.
It follows by induction that
$$h(w)=\max\bigl(0,\max_i(b_i-i)\bigr). \tag{3}$$
There are no other recurrent points. Since $b_i\le M$, the largest time
on $X_{n,M}$ is $M-1$. For $M>1$, equality requires $i=1,b_1=M$, hence
every entry is $M$; this word attains equality. At $M=1$ the carrier is a
singleton, and the same word is its only, depth-zero, state.

## 2. A direct full-coordinate derivation

The sequence $C_i$ is nonnegative and nondecreasing. Equation (1) gives
$z_i\le i$. Also $C_i\le b_i-1$, because $b_r\le b_i$ and $r\ge1$,
so $z_i\ge1$. To check that $z$ is sorted, consider $i>1$. If
$C_i=C_{i-1}$, subtraction preserves $b_{i-1}\le b_i$. If
$C_i>C_{i-1}$, then $C_i=b_i-i$ and $z_i=i>z_{i-1}$.
Thus $z$ is a parking function.

When (2) applies, $C_i=0$ for $i<d$ and $C_i\ge1$ for $i\ge d$.
Taking the prefix maxima again gives
$$C'_i=\begin{cases}0,&i<d,\\C_i-1,&i\ge d.\end{cases}$$
Therefore $z'_i=b'_i-C'_i=z_i$ at every rank. Ties of $b$ have equal
$C_i$: inside a run of equal $b_i$, the new value $b_i-i$ strictly
decreases and cannot set a new prefix record. We may consequently put
$z_i$ back at the original positions without a tie-breaking ambiguity.
The resulting labelled $u$ is invariant and, by (3), is exactly the
terminal word $\mathrm{Park}(w)$.

For a fixed parking word $u$, cut its sorted word $z$ immediately before
every rank $s$ with $z_s=s$, except that rank $1$ starts the first block.
Let the resulting starts be $1=s_1<\cdots<s_k$, and put $s_{k+1}=n+1$.
These are its prime blocks. Values in block $j$ range from $s_j$ to at
most $s_{j+1}-1$; their sets of original positions are well-defined.

A strict increase of $C_i$ forces $z_i=i$. Hence $C_i$ is constant on
each such block. Call that value $c_j$. We have
$$w_a=u_a+c_j\quad(a\text{ in block }j),
\qquad 0\le c_1\le\cdots\le c_k. \tag{4}$$

Conversely, start with any labelled parking $u$ and any nondecreasing
nonnegative integers $c_1,\ldots,c_k$, and define $w$ by (4).
Block values remain in their original order. For a rank $i$ in block $j$,
all earlier $b_r-r$ are at most $c_j$; at its block start
$b_{s_j}-s_j=c_j$. Consequently the prefix maximum in (1) is exactly
$c_j$ throughout that block, and (1) returns $u$. This proves both
surjectivity and uniqueness of (4), including labelled positions.

Let $m=\max_a u_a$. Since later blocks have larger values and shifts,
$$\max_a w_a=m+c_k.$$ 
The finite alphabet condition is therefore precisely $c_k\le M-m$.
For $c_0=0$, define
$$\delta_j=c_j-c_{j-1},\quad H=M-m,\quad
S=\sum_{j=1}^k\delta_j=c_k.$$ 
The basin of $u$ in $X_{n,M}$ is bijective with
$$\Delta_{k,H}=\{\delta\in\mathbb Z_{\ge0}^{k}:\sum_j\delta_j\le H\}. \tag{5}$$
Only parking words with $m\le M$ occur, so $H\ge0$.

## 3. The entire dynamics in these coordinates

If $\delta\ne0$, let $r=\min\{j:\delta_j>0\}$. Then $c_j=0$ for
$j<r$ and $c_r>0$. All ranks before $s_r$ remain a feasible parking
prefix, while $w^{\uparrow}_{s_r}=s_r+c_r>s_r$. Thus $d(w)=s_r$.
The literal step decreases exactly blocks $r,\ldots,k$, equivalently
$$\delta\longmapsto\delta-e_r. \tag{6}$$
At $\delta=0$ it is the identity. This is a full basinwise conjugacy,
not merely a factor, matching census or an eventual approximation.
The invariant label $u$ is unchanged, and every state of the full carrier
occurs in exactly one basin (5). The time is $S$; all periods are one.

By counting nonnegative gap allocations, the exact basin size and its
depth layers are
$$|\mathrm{Park}^{-1}(u)\cap X_{n,M}|=\binom{H+k}{k},\qquad
|\{w:\mathrm{Park}(w)=u,\ h(w)=t\}|=\binom{t+k-1}{k-1}
\quad(0\le t\le H). \tag{7}$$
For the first count, append a slack coordinate $H-S$ and count weak
compositions of $H$ into $k+1$ parts. The second count is the weak
composition count for $S=t$. Since $n\ge1$, we have $k\ge1$; at $t=0$
the second expression is one, including $k=1$.

## 4. Every one-step inverse and all extremizers

Let a target have coordinates $(u,\delta)$ in (5). If $\delta\ne0$,
let $r$ be its first positive index. Its nonfixed predecessors are exactly
$$\delta+e_j,\qquad 1\le j\le r,\quad S+1\le H. \tag{8}$$
Indeed, a predecessor must decrease its first positive coordinate; if that
coordinate were after $r$, the target's earlier positive coordinate would
already have been positive. Conversely each vector in (8) has first
positive coordinate $j$ and is mapped to $\delta$ by (6). Distinct $j$
give distinct sources, which also proves that none are missed.
For $\delta=0$, the predecessor set is zero itself and all $e_j$ allowed
by $H\ge1$. In particular
$$|T^{-1}(u,\delta)|=
\begin{cases}
1+k\,\mathbf1_{\{H\ge1\}},&\delta=0,\\
r\,\mathbf1_{\{S<H\}},&\delta\ne0.
\end{cases} \tag{9}$$
There is no overcount from separate basins: $\mathrm{Park}(Tw)=
\mathrm{Park}(w)$ was proved above. An immediate image description is
$$T(X_{n,M})=\{w\in X_{n,M}:\max w<M\}\ \cup
(\mathrm{PF}_n\cap X_{n,M}). \tag{10}$$

Every block start is a distinct integer value between $1$ and $m$, so
$k\le\min(n,m)$. A fixed target with nonfixed predecessors has
$m\le M-1$, and (9) bounds its fibre by $1+\min(n,M-1)$.
A nonfixed target with a predecessor has $S\ge1$ and $m+S<M$, hence
$m\le M-2$ and its fibre is at most $\min(n,M-2)$.
If $M=1$, there is just the fixed singleton. These bounds and the following
constructions prove
$$\max_{w\in X_{n,M}}|T^{-1}(w)|=\min(M,n+1). \tag{11}$$

For $M\ge n+1$, equality requires a fixed target and $k=n$.
Every rank must then start a block, so its sorted word is $(1,2,\ldots,n)$.
Every permutation of this word has $H\ge1$ and attains $n+1$; these are
all equality targets.

For $2\le M\le n$, equality requires a fixed target with
$m=k=M-1$. Its $k$ distinct block-start values must be all of
$1,\ldots,M-1$, so its first $M-1$ sorted ranks have those values in
order. Every remaining entry is at least and at most $M-1$.
Thus all and only permutations of
$$\bigl(1,2,\ldots,M-2,
\underbrace{M-1,\ldots,M-1}_{n-M+2}\bigr) \tag{12}$$
attain equality. Conversely (12) has exactly $M-1$ blocks and $H=1$,
so (9) gives its fibre as $M$. At $M=1$ the unique target is the unique
extremizer. At $n=1,M\ge2$, the first regime gives the target $(1)$
with exactly two sources, so the one-letter boundary is included. ∎

## 5. Precise source subtraction, not a renamed contribution

The elementary update is already in Novelli–Thibon's
[parkization definition, §2, equation (6)](https://arxiv.org/pdf/math/0411387).
Segovia's [2025 v1, Lemma 25 and Propositions 26/29](https://arxiv.org/html/2502.07926v1#S3)
already supplies the blockwise monotone shifts, their bijective encoding
by inserted empty columns, and deletion of those columns under parkization.
No published formula for the finite-cap extremizers is asserted here.

The direct deductions above identify the precise consequence for this
bounded literal: (6) merely removes one unit from the first occupied gap.
Equations (3), (7), (9) and (11) all arise from the same existing coordinate
model and elementary weak-composition counting. The longer clock obtained
by exposing one recursive step does not free an independent inverse axis.
In particular, fixed-point counting, a sharp bound, and a solved extremum
are not automatically separate contributions when a single known decoder
delivers all of them.

This is not claimed literally equal to old circular parking displacement,
mass-driven cyclic allocation or Fibonacci fission. Those different maps
remain excluded on their actual definitions. Nor is (6) proposed as a
fresh queue/allocation system: it is the explicit mechanism that closes
this one attempted word rule.

## Open risks and decision boundary

The formulas are deductive, not tested by a pilot or independent verifier.
No global first-publication claim is made for any displayed specialization.
The exact owner/model subtraction suffices for this negative desk; a broad
unsearched statement that no related work exists is neither needed nor
supported. No pilot preparation, candidate admission, reserve or manuscript
number follows. Historical source texts and accepted packages are unchanged.
