# C02 hard residual: multipartite synchronous-mex fibres

**Status:** `PROVABLE AS STATED`  \
**Owner gate:** **PROMOTE**  \
**External status:** `HOLD_EXTERNAL`

## Target

Determine the exact one-step fibres, basin sizes, and transient layers of
synchronous open-neighbourhood mex on a complete multipartite graph
$K_{a_1,\ldots,a_k}$, retaining the labelled vertices and the full
part-size vector. The target is specifically the simultaneous finite map,
not Grundy colouring as an optimization or stabilization procedure.

The target survives and strengthens: the earlier loose graph-depth bound
$\tau\le3$ improves to the exact structural bound

\[
\boxed{\Phi^2(c)\text{ is recurrent for every initial colouring }c.}
\]

Thus the full labelled phase space has only depth layers $0,1,2$. The bound
is attained, for example, by six of the $27$ states of the canonical
$K_{1,2}$ system.

## Invariant object

The organizing object is the first-round part vector

\[
y(c)=(y_1(c),\ldots,y_k(c)),\qquad
y_i(c)=\operatorname{mex}c(V\setminus V_i),
\]

together with its exact fibre weight

\[
N_{\mathbf a,q}(y)
=\#\{c:V\to\{0,\ldots,q-1\}:y(c)=y\}.
\]

Every graph image is constant on each part, so all subsequent dynamics is
the quotient map

\[
T(y)_i=\operatorname{mex}\{y_j:j\ne i\}.
\]

Keeping the weights $N_{\mathbf a,q}(y)$ rather than replacing each part by
one unweighted coordinate is what preserves the information in
$(a_1,\ldots,a_k)$.

## Assumptions and notation

- $k\ge1$, every $a_i\ge1$, and the vertex parts $V_i$ are labelled with
  $|V_i|=a_i$.
- $n=\sum_i a_i$ and
  $\Delta=\max_i(n-a_i)=n-\min_i a_i$.
- The canonical palette is $C_{\Delta+1}=\{0,\ldots,\Delta\}$. The formulas
  are proved slightly more generally for
  $C_q=\{0,\ldots,q-1\}$ with $q\ge\Delta+1$. This is a closed extension
  because every open neighbourhood has at most $\Delta<q$ vertices.
- For $y\in C_q^k$, $N_{\mathbf a,q}(y)$ denotes the fibre above the
  part-monochromatic state represented by $y$.
- $s(a,d)=d!\,S(a,d)$ is the number of onto maps from an $a$-element
  labelled set to $d$ labelled colours; $s(a,0)=0$ for $a\ge1$.
- Empty products equal one. All powers with exponent zero use the
  combinatorial convention $u^0=1$, including $u=0$.

For $k=1$, every open neighbourhood is empty, $\Phi(c)=0^{a_1}$, and the
canonical palette has $q=1$. The general $q\ge1$ extension has one recurrent
state, $q^{a_1}-1$ depth-one states, and no depth-two state. The remaining
derivation includes this boundary where the notation permits it.

## Claim package

### Theorem A — inclusion-exclusion fibre formula

For every $y\in C_q^k$, define

\[
\mathcal R(y)=\{(i,r):1\le i\le k,\ 0\le r<y_i\}.
\]

For $J\subseteq\mathcal R(y)$ and a part $h$, put

\[
B_h(y,J)
=\{y_i:i\ne h\}
\cup
\{r:(i,r)\in J,\ i\ne h\}.
\]

Then

\[
\boxed{
N_{\mathbf a,q}(y)
=
\sum_{J\subseteq\mathcal R(y)}
(-1)^{|J|}
\prod_{h=1}^k
\bigl(q-|B_h(y,J)|\bigr)^{a_h}.
}
\tag{1}
\]

The union in $B_h$ is a set union, so repeated forbidden colours are counted
once. Formula (1) returns zero for an impossible target without a separate
feasibility test.

### Theorem B — support/EGF fibre formula

For a colour $r\in C_q$, let $\mathcal A_r(y)$ be the family of supports
$P\subseteq[k]$ satisfying

\[
\begin{aligned}
y_i=r&\Longrightarrow P\subseteq\{i\},\\
y_i>r&\Longrightarrow P\nsubseteq\{i\}.
\end{aligned}
\tag{2}
\]

Define

\[
G_r^y(x_1,\ldots,x_k)
=
\sum_{P\in\mathcal A_r(y)}
\prod_{i\in P}(e^{x_i}-1).
\]

Then

\[
\boxed{
N_{\mathbf a,q}(y)
=
\left(\prod_{i=1}^k a_i!\right)
[x_1^{a_1}\cdots x_k^{a_k}]
\prod_{r=0}^{q-1}G_r^y(x_1,\ldots,x_k).
}
\tag{3}
\]

Equivalently, with $P_r$ the support of colour $r$ and
$d_i=\#\{r:i\in P_r\}$,

\[
\boxed{
N_{\mathbf a,q}(y)
=
\sum_{\substack{P_r\in\mathcal A_r(y)\\0\le r<q}}
\prod_{i=1}^k s(a_i,d_i).
}
\tag{4}
\]

If $M=\max_i y_i$, every colour $r>M$ is unconstrained. Hence

\[
G_r^y=\prod_{i=1}^ke^{x_i}
=e^{x_1+\cdots+x_k}
\qquad(r>M),
\]

and (3) simplifies exactly to

\[
N_{\mathbf a,q}(y)
=
\left(\prod_i a_i!\right)[x^{\mathbf a}]
e^{(q-1-M)(x_1+\cdots+x_k)}
\prod_{r=0}^{M}G_r^y(x).
\tag{5}
\]

This is the precise palette reduction: high colours are not deleted or
identified; their entire contribution is the background exponential in
(5).

### Theorem C — two-round global collapse

Let $\mathcal R_k$ be the recurrent quotient states:

1. the $k!$ permutations of $0,\ldots,k-1$, which are fixed; and
2. for $0\le m\le k-2$ and an injection
   $\iota:\{0,\ldots,m-1\}\hookrightarrow[k]$, the pair

   \[
   x^-_{\iota,m}(i)=
   \begin{cases}
   r,&i=\iota(r),\\
   m,&i\notin\operatorname{im}\iota,
   \end{cases}
   \qquad
   x^+_{\iota,m}(i)=
   \begin{cases}
   r,&i=\iota(r),\\
   m+1,&i\notin\operatorname{im}\iota.
   \end{cases}
   \]

   The quotient map swaps $x^-_{\iota,m}$ and $x^+_{\iota,m}$.

For every labelled vertex colouring $c$,

\[
\boxed{T(y(c))\in\mathcal R_k.}
\tag{6}
\]

Consequently $\Phi^2(c)$ is recurrent and no original state has depth
greater than two.

### Corollary D — exact depth and basin laws

Let

\[
b_k=\sum_{m=0}^{k-2}\frac{k!}{(k-m)!},
\qquad
R_k=|\mathcal R_k|=k!+2b_k,
\]

where the sum is empty for $k=1$, and put

\[
S_{\mathbf a,q}
=\sum_{x\in\mathcal R_k}N_{\mathbf a,q}(x).
\]

The exact numbers of original labelled colourings at depths $0,1,2$ are

\[
\boxed{
D_0=R_k,\qquad
D_1=S_{\mathbf a,q}-R_k,\qquad
D_2=q^n-S_{\mathbf a,q}.
}
\tag{7}
\]

For $x\in\mathcal R_k$, define the two-step entrance mass

\[
H_x=\sum_{\substack{y\in C_q^k\\T(y)=x}}N_{\mathbf a,q}(y).
\tag{8}
\]

If $\mathcal O\subseteq\mathcal R_k$ is a fixed orbit or a 2-cycle, then

\[
\boxed{
\begin{aligned}
B_{\mathcal O}&=\sum_{x\in\mathcal O}H_x,\\
B_{\mathcal O,0}&=|\mathcal O|,\\
B_{\mathcal O,1}&=\sum_{x\in\mathcal O}N_{\mathbf a,q}(x)-|\mathcal O|,\\
B_{\mathcal O,2}&=
B_{\mathcal O}-\sum_{x\in\mathcal O}N_{\mathbf a,q}(x).
\end{aligned}}
\tag{9}
\]

Thus (1), (3), or (4), together with the finite preimage sets below, gives
every basin and every layer exactly.

## Derivation strategy and dependency map

1. A mex target is translated into absence of its own colour and presence of
   every lower colour outside the corresponding part.
2. Route I applies inclusion-exclusion to the lower-colour presence
   conditions; vertex choices then factor by parts.
3. Route II fixes the set of parts supporting each colour and counts labelled
   vertices by multivariate exponential generating functions, or
   equivalently by products of onto-function counts.
4. An image-shape lemma shows that a repeated first-round value can only be
   the maximum value.
5. A general identity for $T(y)$ then places $T(y)$ in the recurrent list,
   proving (6).
6. The recurrent-target fibres simplify to explicit products. Summing those
   products yields (7).
7. Exact descriptions of $T^{-1}(x)$ yield (8) and the basin layers (9).

No approximation enters this chain.

## Proof route I: bad-event inclusion-exclusion

Fix $y\in C_q^k$. The equality

\[
y_i=\operatorname{mex}c(V\setminus V_i)
\]

holds if and only if:

1. colour $y_i$ is absent from $V\setminus V_i$; and
2. for every $0\le r<y_i$, colour $r$ occurs at least once in
   $V\setminus V_i$.

Impose all conditions of type 1 as base restrictions. For
$(i,r)\in\mathcal R(y)$, let $E_{i,r}$ be the bad event that $r$ is absent
from $V\setminus V_i$. Inclusion-exclusion over a set
$J\subseteq\mathcal R(y)$ of bad events gives the sign $(-1)^{|J|}$.

Under the base restrictions and all events in $J$, a vertex in part $V_h$
cannot use:

- $y_i$ for any $i\ne h$; or
- $r$ whenever $(i,r)\in J$ and $i\ne h$.

The forbidden set is exactly $B_h(y,J)$. Every labelled vertex of $V_h$ can
therefore choose independently among $q-|B_h(y,J)|$ colours. Multiplication
over the parts and inclusion-exclusion over $J$ gives (1). This proves
Theorem A.

## Proof route II: colour supports and labelled species

For each colour $r$, let

\[
P_r=\{i:\text{colour }r\text{ occurs in }V_i\}.
\]

The target condition for $y_i$ says:

- if $y_i=r$, then $r$ occurs nowhere outside $V_i$, so
  $P_r\subseteq\{i\}$;
- if $y_i>r$, then $r$ occurs outside $V_i$, so
  $P_r\nsubseteq\{i\}$.

These are precisely the conditions defining $\mathcal A_r(y)$ in (2).

Fix all supports $(P_0,\ldots,P_{q-1})$. Part $V_i$ uses exactly
$d_i=\#\{r:i\in P_r\}$ named colours, each at least once. The number of
labelled colourings of that part is $s(a_i,d_i)$, independently of the other
parts. Summing the product over all admissible supports gives (4).

For the EGF form, one named colour used in part $V_i$ contributes
$e^{x_i}-1$, the EGF of a nonempty labelled subset. If its support is $P$,
its multivariate contribution is
$\prod_{i\in P}(e^{x_i}-1)$. Summing over admissible $P$ gives $G_r^y$;
multiplying over the named colours and extracting all $a_i$ labelled
vertices gives (3). This proves Theorem B by a route that never introduces
the bad events from Route I.

For $r>M=\max y_i$, neither implication in (2) imposes a restriction, so all
$2^k$ supports are allowed and

\[
\sum_{P\subseteq[k]}\prod_{i\in P}(e^{x_i}-1)
=\prod_i e^{x_i}.
\]

Multiplying this factor for all $q-1-M$ high colours proves (5).

## Image shape and proof of the two-round theorem

### Lemma 1 — only the maximum output can repeat

Assume $k\ge2$, $y=y(c)$, and $y_i=y_j=r$ for distinct $i,j$. The target
condition at $i$ says that $r$ is absent from $V\setminus V_i$, while the
condition at $j$ says that $r$ is absent from $V\setminus V_j$. These two
sets cover all vertices, so $r$ is globally absent.

If some $y_\ell>r$, the mex condition at $\ell$ would require $r$ to occur in
$V\setminus V_\ell$, a contradiction. Hence every repeated coordinate value
of a graph image is its maximum.

### Lemma 2 — quotient support reduction

For an arbitrary $y\in C_q^k$, let

\[
g=\operatorname{mex}\{y_1,\ldots,y_k\}.
\]

Then

\[
T(y)_i=
\begin{cases}
y_i,&y_i<g\text{ and }y_i\text{ occurs exactly once in }y,\\
g,&\text{otherwise}.
\end{cases}
\tag{10}
\]

If $y_i<g$, every colour below $g$ occurs in $y$. Removing coordinate $i$
removes the colour $y_i$ exactly when it was unique; in that case the new mex
is $y_i$. If it was not unique, all colours below $g$ remain and $g$ is still
absent, so the mex is $g$. If $y_i>g$, removing it does not affect any colour
at most $g$, and the mex is again $g$. This proves (10).

Equation (10) also proves that the displayed list $\mathcal R_k$ is the whole
recurrent quotient. Indeed, after one quotient step a state has some unique
values $U\subseteq\{0,\ldots,g-1\}$ and value $g$ in every other coordinate.
Let $m=\operatorname{mex}U$. If $m<g$, a second use of (10) preserves the
unique initial segment $0,\ldots,m-1$ and replaces every remaining coordinate
by $m$, producing a fixed permutation or a state $x^-_{\iota,m}$. If $m=g$,
the first quotient image already consists of $0,\ldots,g-1$ once each and
either zero or one further coordinate (a fixed permutation), or at least two
coordinates equal to $g$ (a state $x^-_{\iota,g}$). Hence every quotient
state enters the displayed list in at most two steps. The listed
permutations are fixed and each displayed pair is swapped, so a recurrent
state can be no other state.

### Completion of Theorem C

Let $M=\max y(c)$. If $g\le M$, Lemma 1 makes every
$0,\ldots,g-1$ unique. Equation (10) therefore produces one copy of each
$0,\ldots,g-1$ and fills every remaining coordinate by $g$. If one
coordinate remains, this is a fixed permutation; if at least two remain, it
is $x^-_{\iota,g}$.

If $g=M+1$, all values $0,\ldots,M$ occur. Lemma 1 makes
$0,\ldots,M-1$ unique. If $M$ is unique, $y$ is a permutation and fixed. If
$M$ repeats, (10) preserves $0,\ldots,M-1$ and changes all occurrences of
$M$ to $M+1$, producing $x^+_{\iota,M}$.

In every case $T(y(c))\in\mathcal R_k$. This proves (6).

Finally, every periodic graph colouring has a predecessor and therefore lies
in the image of $\Phi$; it is consequently part-monochromatic. Its part
vector must be recurrent under $T$. Conversely every state in
$\mathcal R_k$, expanded constantly over its parts, is recurrent under
$\Phi$. Thus the recurrent graph colourings are exactly the $R_k$ expanded
quotient states used in (7).

## Explicit recurrent-target fibres

The general formulas collapse to elementary products on every recurrent
target. These are useful both as theorem statements and as a nontrivial check
that the full vector $\mathbf a$ remains visible.

### Fixed permutation

Let $x$ be a permutation and let $i_r$ be the part with $x_{i_r}=r$. Put
$h=q-k\ge0$. Then

\[
\boxed{
N_{\mathbf a,q}(x)
=
\left[
\prod_{r=0}^{k-2}
\bigl((h+1)^{a_{i_r}}-h^{a_{i_r}}\bigr)
\right]
(h+1)^{a_{i_{k-1}}}.
}
\tag{11}
\]

Indeed, low colour $r$ can occur only in $V_{i_r}$. For $r<k-1$, some target
is larger than $r$, so that colour must occur in its allowed part. Colour
$k-1$ is optional in $V_{i_{k-1}}$. The $h$ colours
$k,\ldots,q-1$ are free.

### Lower state of a 2-cycle

For $x^-_{\iota,m}$, write $i_r=\iota(r)$,
$R=[k]\setminus\operatorname{im}\iota$, and
$A_R=\sum_{j\in R}a_j$. Put $v=q-m-1$. Then

\[
\boxed{
N_{\mathbf a,q}(x^-_{\iota,m})
=
\left[
\prod_{r=0}^{m-1}
\bigl((v+1)^{a_{i_r}}-v^{a_{i_r}}\bigr)
\right]v^{A_R}.
}
\tag{12}
\]

Each low colour $r$ is confined to and required in $V_{i_r}$. Because the
target value $m$ occurs in at least two parts, colour $m$ is absent globally.
The $v=q-m-1$ larger colours are otherwise free.

### Upper state of a 2-cycle

For $x^+_{\iota,m}$ use the same $R,A_R$ and put $u=q-m-2$. Define

\[
\begin{aligned}
L_1&=\prod_{r=0}^{m-1}
\left((u+2)^{a_{i_r}}-(u+1)^{a_{i_r}}\right),\\
L_0&=\prod_{r=0}^{m-1}
\left((u+1)^{a_{i_r}}-u^{a_{i_r}}\right),\\
Q&=(u+1)^{A_R},\\
Q_{\ge2}
&=Q-u^{A_R}
-\sum_{j\in R}
\left((u+1)^{a_j}-u^{a_j}\right)u^{A_R-a_j}.
\end{aligned}
\]

Then

\[
\boxed{
N_{\mathbf a,q}(x^+_{\iota,m})
=(L_1-L_0)Q+L_0Q_{\ge2}.
}
\tag{13}
\]

The repeated target $m+1$ makes colour $m+1$ globally absent. Colour $m$
must occur outside every part in $R$. If it occurs in a low part, all those
requirements are satisfied and the $R$-parts are arbitrary, giving
$(L_1-L_0)Q$. If it occurs in no low part, it must occur in at least two
different $R$-parts. The quantity $Q_{\ge2}$ subtracts the cases in which it
is absent or supported in exactly one $R$-part. This proves (13).

Equations (11)--(13), summed over the fixed permutations and the injections
$\iota$, give $S_{\mathbf a,q}$ in (7) without summing over all
$q^k$ potential first-round targets.

## Exact quotient preimages and basin formulas

Equation (10) also gives compact finite descriptions of every preimage used
in (8).

### Fixed point

For a fixed permutation $x$ with $x_{i_r}=r$,

\[
T^{-1}(x)
=
\left\{
y:
y_{i_r}=r\ (0\le r<k-1),\
y_{i_{k-1}}\in\{k-1,\ldots,q-1\}
\right\}.
\tag{14}
\]

### Lower 2-cycle state

\[
T^{-1}(x^-_{\iota,m})
=
\left\{
y:
y_{i_r}=r\ (0\le r<m),\
y_j\in\{m+1,\ldots,q-1\}\ (j\in R)
\right\}.
\tag{15}
\]

### Upper 2-cycle state

\[
\begin{aligned}
T^{-1}(x^+_{\iota,m})
=\{y:\;&y_{i_r}=r\ (0\le r<m),\\
&y_j\in\{m\}\cup\{m+2,\ldots,q-1\}\ (j\in R),\\
&\#\{j\in R:y_j=m\}\ge2\}.
\end{aligned}
\tag{16}
\]

Substitution of (14)--(16) into (8), with any of the two fibre formulas,
produces every $H_x$. Since Theorem C puts $\Phi^2(c)$ at exactly one
recurrent state, the $H_x$ partition the entire labelled phase space by the
second iterate. Summing over the one or two states in an orbit proves the
basin formula in (9).

For the depth layers inside that basin, a state has depth at most one exactly
when its first image is already in $\mathcal O$. Its number is
$\sum_{x\in\mathcal O}N_{\mathbf a,q}(x)$. Removing the
$|\mathcal O|$ recurrent states gives layer one; subtracting the depth-zero
and depth-one masses from the basin gives layer two. This proves all of (9)
and, after summing over the orbits, (7).

## Small asymmetric signal

For $K_{1,2}$, the canonical palette has $q=3$. The four recurrent quotient
states have one-step fibres

\[
N(0,0)=8,\qquad N(1,1)=3,\qquad
N(0,1)=4,\qquad N(1,0)=6.
\]

In particular the two fixed permutations have different fibres because the
part receiving the maximal low colour has a different size. The exact depth
profile is

\[
(D_0,D_1,D_2)=(4,17,6).
\]

The basin sizes are

\[
B_{\{(0,1)\}}=4,\qquad
B_{\{(1,0)\}}=10,\qquad
B_{\{(0,0),(1,1)\}}=13.
\]

They sum to $27=3^{1+2}$. This is the first compact signal that quotient
symmetry does not erase the original multipartite geometry.

## Exact verification

The unique deterministic standard-library verifier is
[comb_c02_multipartite_fibres.py](./comb_c02_multipartite_fibres.py).
It performs, independently:

1. brute-force enumeration of every labelled colouring;
2. evaluation of (1) for every target $y\in C_q^k$;
3. support enumeration weighted by onto counts, implementing (4);
4. evaluation of (11)--(13) on every recurrent target;
5. exhaustive verification of (14)--(16);
6. pointwise verification that every graph image enters $\mathcal R_k$ after
   one quotient step;
7. direct comparison of all global and per-basin depth counts with
   (7)--(9).

The test grid contains 15 cases, including the canonical systems
$K_{1,2,3}$ with $46{,}656$ labelled states and $K_{2,2,2}$ with
$15{,}625$ states, all targets for those systems, $k=1$, and enlarged
palettes above $\Delta+1$. There is no sampling and no random branch.

Fresh command:

    python3 docs/papers117_121_sequence/proof_spikes/comb_c02_multipartite_fibres.py

Fresh result:

    C02 MULTIPARTITE SYNCHRONOUS-MEX FIBRES
    parts=(1,) q=1 states=1 nonzero_fibres=1 recurrent_states=1 depths=(1, 0, 0) basins=1
    parts=(2,) q=1 states=1 nonzero_fibres=1 recurrent_states=1 depths=(1, 0, 0) basins=1
    parts=(2,) q=3 states=9 nonzero_fibres=1 recurrent_states=1 depths=(1, 8, 0) basins=1
    parts=(1, 1) q=2 states=4 nonzero_fibres=4 recurrent_states=4 depths=(4, 0, 0) basins=3
    parts=(1, 1) q=4 states=16 nonzero_fibres=4 recurrent_states=4 depths=(4, 12, 0) basins=3
    parts=(1, 2) q=3 states=27 nonzero_fibres=6 recurrent_states=4 depths=(4, 17, 6) basins=3
    parts=(1, 2) q=4 states=64 nonzero_fibres=6 recurrent_states=4 depths=(4, 52, 8) basins=3
    parts=(2, 2) q=3 states=81 nonzero_fibres=9 recurrent_states=4 depths=(4, 45, 32) basins=3
    parts=(2, 2) q=4 states=256 nonzero_fibres=9 recurrent_states=4 depths=(4, 192, 60) basins=3
    parts=(1, 1, 1) q=3 states=27 nonzero_fibres=17 recurrent_states=14 depths=(14, 10, 3) basins=10
    parts=(1, 1, 2) q=4 states=256 nonzero_fibres=32 recurrent_states=14 depths=(14, 181, 61) basins=10
    parts=(1, 2, 2) q=5 states=3125 nonzero_fibres=55 recurrent_states=14 depths=(14, 2304, 807) basins=10
    parts=(2, 2, 2) q=5 states=15625 nonzero_fibres=91 recurrent_states=14 depths=(14, 9660, 5951) basins=10
    parts=(1, 2, 3) q=6 states=46656 nonzero_fibres=85 recurrent_states=14 depths=(14, 34117, 12525) basins=10
    parts=(1, 1, 1, 1) q=4 states=256 nonzero_fibres=87 recurrent_states=58 depths=(58, 152, 46) basins=41
    K_(1,2)_q3 recurrent_fibres=00:8,11:3,01:4,10:6
    K_(1,2)_q3 basin_sizes=fixed01:4,fixed10:10,uniform_two_cycle:13
    assertions=201922

All **201,922 assertions** passed.

## Owner subtraction and promotion gate

Hedetniemi, Jacobs, and Srimani,
[*Linear time self-stabilizing colorings*](https://doi.org/10.1016/S0020-0190(03)00299-0)
(2003), directly own the local rule “replace a privileged vertex by the least
positive colour absent from its open neighbourhood,” up to the colour shift
from $1,2,\ldots$ to $0,1,\ldots$. They assume a serial central daemon and
prove convergence to a Grundy colouring. The mex rule, Grundy fixed points,
and serial convergence therefore receive zero credit.

The residual established here is disjoint from that theorem:

1. all vertices update simultaneously, so nontrivial 2-cycles are essential;
2. complete multipartite symmetry collapses the graph but leaves exact
   labelled fibre weights depending on every $a_i$;
3. the two independent formulas (1) and (3) count those fibres;
4. the graph image has the special repeated-maximum shape, forcing global
   two-round recurrence;
5. (7)--(9) give every transient layer and every orbit basin exactly; and
6. (11)--(13) are closed recurrent-target formulas, not merely an algorithm
   for evaluating the quotient.

This clears the hard residual gate. The recommendation is therefore
**PROMOTE C02**, with the paper claim restricted to this exact synchronous
multipartite conjunction and with the 2003 rule-level owner credited
prominently.

## Boundaries and non-claims

- The canonical paper phase uses $q=\Delta+1$. The $q\ge\Delta+1$ extension
  is exact and is stated only to expose how surplus colours enter the fibre
  formulas.
- The result does not cover arbitrary graphs, asynchronous schedules,
  closed-neighbourhood mex, or recolouring with conflict guards.
- Formula (1) is finite but exponential in $\sum_i y_i$; no polynomial-time
  evaluation claim is made.
- The basin entrance masses (8) are exact finite sums using the explicit
  preimage sets (14)--(16). They are not claimed to collapse to one uniform
  elementary product for arbitrary $\mathbf a$.
- Fixed-point/Grundy facts, the quotient zeta function after cycle
  classification, and generic distributed-colouring results receive zero
  novelty credit.
- The owner search remains bounded. `PROMOTE` means that the mathematical
  residual is now paper-sized relative to the located direct owner; it is
  not a public novelty or priority claim.

## Open risks

- A specialized synchronous-Grundy paper could still own the same
  multipartite fibre distribution under different terminology. External
  status must remain `HOLD_EXTERNAL` until the batch owner audit closes.
- A hostile referee may regard either (1) or (3) alone as routine. The viable
  contribution is their conjunction with the repeated-maximum image lemma,
  two-round theorem, explicit recurrent fibres, and exact basin layers.
- If a short paper cannot present both proof routes without crowding, Route I
  should prove the main formula and Route II should remain as an independent
  coefficient theorem or appendix proof; neither should be advertised as a
  generic colouring algorithm.
