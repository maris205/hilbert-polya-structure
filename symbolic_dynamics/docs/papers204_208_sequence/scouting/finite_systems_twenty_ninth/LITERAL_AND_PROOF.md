# MCC: minimum-card carousel — deductive rejection

Status: **PROVABLE AS STATED / KILL_LITERAL_P169_INVARIANT_RESTRICTION**.
One literal definition, no scientific execution and no pilot box. This is
an author proof for a rejected scout, not an independent gate or paper.

## Carrier, update and assumptions

Fix integers $1\le k\le n$. A state is an ordered partition
$B=(B_0,\ldots,B_{k-1})$ of $[n]=\{1,\ldots,n\}$ into nonempty blocks.
Positions are fixed named sites in $\mathbb Z/k\mathbb Z$, not canonically
reordered by the current block minima. Write $m_i=\min B_i$ and set

$$F(B)_i=(B_i\setminus\{m_i\})\cup\{m_{i-1}\}.$$

Every $m_i$ is selected from the **old snapshot**. Distinct blocks give
distinct sent labels, every label appears once after the update, and every
site receives a label. Thus the carrier is finite and invariant. At $k=1$
the removal and return cancel and there is only one state. Empty carriers
$k=0$ and $k>n$ are outside this literal; they are not silently repaired.

## Claims and dependency map

1. The full labelled map is conjugate to a compatible stack of old
   directed-cycle unit-service queues, not just factored by total loads.
2. The recurrent locus consists exactly of states in which labels
   $1,\ldots,k$ lie in distinct blocks. Each such state has exact period
   $k$. There are $k!\,k^{n-k}$ recurrent states and
   $(k-1)!\,k^{n-k}$ cycles.
3. The maximum entrance time is zero if $n=k$ or $k=1$, and $k-1$ if
   $n>k>1$.
4. Every target has a complete one-step inverse parametrization by its
   selected incoming labels, with explicit necessary-and-sufficient
   inequalities and no multiplicity in the parametrization for $k>1$.

Claim 1 follows directly from prefix counting and difference decoding.
The queue max-plus identity proves the mass-$k$ smoothing bound; this and
Claim 1 give Claims 2–3. Claim 4 is a separate direct reconstruction.
The queue identity and smoothing mechanism are already explicitly present
in the captured P169 original and receive zero credit. No claim depends on
an experiment, an uninspected source theorem, P208/P209, or scout 28.

## 1. Full-stack conjugacy

For $0\le r\le n$ define $z_i^{(r)}=|B_i\cap[r]|$, with $[0]=\varnothing$.
The stack satisfies

$$z^{(0)}=0,\qquad z^{(r)}-z^{(r-1)}=e_{j_r},\qquad
z_i^{(n)}\ge1,$$

where $e_j$ is the unit vector at site $j$. Conversely these conditions
recover the state uniquely: place label $r$ at the unique site $j_r$.
Thus this encoding is a bijection onto the stated compatible-stack carrier.

Site $i$ sends a label at most $r$ if and only if $z_i^{(r)}>0$: its sent
label is its minimum. Therefore, for **every** $r$,

$$z_i^{(r)}(F(B))=Q(z^{(r)}(B))_i,
\qquad Q(z)_i=z_i-\mathbf1_{\{z_i>0\}}+
                         \mathbf1_{\{z_{i-1}>0\}}. \tag{1}$$

The same map $Q$ acts separately on every level; compatibility is invariant
because the left side is the stack of the well-defined state $F(B)$.
The inverse decoding recovers $F(B)$ and every later iterate, so (1) is a
full-state conjugacy to a restricted product, not a lossy count projection.
An intrinsic labelled presentation does not change this deduction.

## 2. The already-owned queue bound, proved in the exact needed scope

For a nonnegative integer load vector $z$ on the $k$-cycle with mass $k$,
choose a lift $H_i$ on $\mathbb Z$ satisfying
$H_i-H_{i-1}=z_i$ and $H_{i+k}=H_i+k$. Equation (1) is equivalent to

$$H_i(t+1)=\max\{H_i(t)-1,H_{i-1}(t)\}.$$

Indeed this equals $H_i(t)-\mathbf1_{\{z_i(t)>0\}}$ because $z_i(t)$
is a nonnegative integer. Taking adjacent differences gives (1). Induction
expands the two alternatives at each step to

$$H_i(t)=\max_{0\le r\le t}\bigl(H_{i-r}(0)-t+r\bigr).$$

Put $X_r=H_{i-r}(0)+r$. Adjacent differences yield

$$z_i(t)=1+\max_{0\le r\le t}X_r-
                    \max_{1\le r\le t+1}X_r. \tag{2}$$

If $z_i(t)=0$, the second maximum exceeds the first by one. Its maximizing
index cannot be in their common range $1,\ldots,t$, hence is $t+1$.
Consequently $X_{t+1}\ge X_0+1$, implying

$$\sum_{r=0}^{t}z_{i-r}(0)=H_i(0)-H_{i-t-1}(0)\le t.$$

At $t=k-1$ this contradicts the mass $k$ in a full cycle. Every load is
therefore positive at time $k-1$, and conservation of mass makes every
load exactly one. This vector is fixed. This proof is precisely the
classical unit-service/max-plus queue mechanism already used in P169;
it is reproduced to make the subtraction checkable, not claimed new.

## 3. Recurrent locus, counts and exact clock

Apply the mass-$k$ bound to $z^{(k)}$. By time $k-1$, each site has exactly
one label in $[k]$. From then on this is always its minimum, so every label
in $[k]$ moves one site clockwise on every step and all labels above $k$
remain stationary. The state returns after $k$ steps. Label 1 changes its
site on every step, so no positive time less than $k$ returns the state
(including the special value $k=1$, where the period is one).

Conversely, if $B$ is recurrent, its factor $z^{(k)}$ is recurrent.
Every such factor reaches the all-ones fixed state by the preceding bound,
so a recurrent factor must already be all ones. This proves both directions
of the recurrent-locus claim. Assigning the first $k$ labels bijectively
to $k$ sites gives $k!$ choices; each other label has $k$ unconstrained
choices. Every site is already nonempty. Division by the exact orbit
length $k$ gives the cycle count.

When $n=k$, every state has one label per site, so every state is recurrent.
When $k=1$, the single state is fixed. Suppose $n>k>1$. Use

$$B_0=\{1,2\},\quad B_1=\{k+1,\ldots,n\},\quad
B_i=\{i+1\}\ (2\le i\le k-1).$$

Its $[k]$-loads are $z_0=2$, $z_1=0$, and one elsewhere. Under $Q$, as
long as the hole is not at $k-1$, the double load stays at site 0 and the
hole moves one site clockwise; this follows by evaluating (1) at the
hole, its successor and site 0. At time $k-2$ the hole is at $k-1$; the
next update gives all ones. For $k=2$ the initial hole is already at
$k-1$ and the same last step applies. The recurrent characterization shows
that the entrance time is exactly $k-1$. Together with the upper bound,
this proves the sharp maximum.

## 4. Full-target inverse reconstruction

Fix a target $C=(C_0,\ldots,C_{k-1})$ and suppose $k>1$. Choose one label
$a_i\in C_{i+1}$ for each $i$, interpreted as the label sent from old site
$i$. Put $\min\varnothing=+\infty$. The admissibility conditions are

$$a_i<\min(C_i\setminus\{a_{i-1}\})\qquad\text{for all }i. \tag{3}$$

For each admissible choice define

$$B_i=(C_i\setminus\{a_{i-1}\})\cup\{a_i\}. \tag{4}$$

The selected labels lie in different target blocks and are therefore
distinct. Each selected incoming label is removed exactly once and
reinserted at the preceding site; every unselected label stays. Thus (4)
is an ordered partition of $[n]$. Each block contains its selected $a_i$,
so it is nonempty. Because $k>1$, $a_i\notin C_i$; condition (3) says
precisely that $a_i$ is the minimum of (4). Sending those minima produces
the target $C$, proving sufficiency.

For necessity, take any preimage $B$ and set $a_i=\min B_i$. Its sent
label lands in $C_{i+1}$, undoing all sends gives (4), and minimality gives
(3). Finally, (4) determines a unique source and its minima recover the
selected vector $a$, so different admissible vectors cannot encode the
same source. Hence

$$|F^{-1}(C)|=
\#\{(a_i)\in\prod_i C_{i+1}:\text{(3) holds for every }i\}.$$

This is an exact local-label decoder on every labelled target, not a
brute-force scan of all ordered partitions or a formal matrix-product
claim. It supplies no asserted extremal classification or novelty. When
$k=1$, the carrier and fibre are singletons; using the selected-label
parametrization there would overcount and is explicitly disallowed.

## Disposition and risks

The statements are deductively proved at all stated parameters, but the
time axis is completely conjugate to a compatible stack of the old queue
rule. Its period, clock and recurrent enumeration cannot satisfy the
new-mechanism conjunction. The separate inverse decoder does not rescue
admission. **NO_PROMOTION; no pilot justified.**

The source search is bounded. No direct worldwide priority statement is
made for this exact card presentation or for the decoder, and no claimed
full-target extremizer is offered. Neither another total mass cutoff nor
a variant send-min/send-max scheduler reopens this lane. Ordinary counting
and full-stack encoding are not independent papers.

## Stronger subsequent collision: literal P169 invariant restriction

The preceding full-stack argument already suffices to reject MCC. A
stronger literal collision follows directly from the captured P169 update.
P169 uses partitions of $\{0,\ldots,N-1\}$ canonically ordered by block
minimum and sends the maximum of every nonsingleton block to its successor.
Set $N=n+k$ and embed the MCC state by

$$E(B)_i=\{i\}\cup\{n+k-j:j\in B_i\},\qquad 0\le i<k.$$

The label ranges $\{0,\ldots,k-1\}$ and $\{k,\ldots,n+k-1\}$ are
disjoint. The former labels are one fixed sentinel in each block. Each
block has at least one moving label, so its minimum is its sentinel $i$,
its size is at least two, and its maximum is $n+k-\min B_i$. The blocks
are therefore in P169's canonical minimum order, and every block donates.
P169 never moves a sentinel. Every block loses one moving label and receives
one, keeping its positive number of moving labels. The embedding image is
forward invariant and the actual maps satisfy

$$\mathcal T_{\rm P169}\circ E=E\circ F.$$

Deleting the sentinels and reversing the moving label map is an inverse
on the image, so $E$ is a conjugacy to that restriction. This is an explicit
old-map embedding, not merely similar vocabulary or a total-load factor.
MCC's apparent intrinsic multi-state carrier is thus already an old literal
under anchored relabelling. The old P169 target-fibre reconstruction also
uses the same selected-donor deletion/insertion skeleton. Restricting its
source set to $E(\mathcal X_{n,k})$ gives MCC fibres; no equality with the
**unrestricted** P169 fibre is asserted. Both this literal collision and
the independent full-stack mechanism are retained. **NO_PROMOTION** is
unconditional and does not depend on clearing a worldwide exact-title hit.
