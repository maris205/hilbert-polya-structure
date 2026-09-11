# Proof Package

## Claim

The following subtraction facts hold for the two literal entry mechanisms.

1. For arbitrary finite local update maps, the full-state predecessor count
   and its sharp global maximum are the formulas in Step 2.
2. If each local update is a single-cycle permutation, the local-memory map
   is conjugate to ordinary rotor routing on a finite directed multigraph
   whose parallel arcs remain distinguished. Under strong connectivity its
   recurrent classification is the source-owned unicycle classification.
3. The pointer-reversal map in Step 1 is a permutation on its entire finite
   carrier with the stated explicit inverse. All positive-iterate fibres have
   size one; its fixed-state count is $n^n$. It preserves the augmented
   undirected edge multiset and has the displayed reversing involution.

These claims certify removal of old or elementary mechanisms. They do not
assert a new candidate, an all-time period formula for the pointer map, or a
classification of every finite local-memory model.

## Status

PROVABLE AS STATED.

The claims are deliberately limited to the exact literals below. No earlier
candidate theorem is silently strengthened or repaired.

## Assumptions

For local memory, $V$ is finite and nonempty. At each vertex $v\in V$, the
finite set $S_v$ is nonempty, the update $U_v:S_v\to S_v$ is deterministic,
and the output $o_v:S_v\to V$ is fixed. If a prescribed directed support
graph $G$ is supplied, every $o_v(a)$ is an out-neighbour of $v$ in $G$.
There is no random choice, external scheduler or quotient of labels.

The conjugacy in Claim 2 additionally requires every $U_v$ to consist of one
cycle on $S_v$, including a singleton cycle. Its recurrent classification
additionally requires the constructed graph $H$ to be strongly connected.
The conjugacy and the full-state fibre formulas do not require this last
condition.

For pointer reversal, $V=[n]=\{0,\ldots,n-1\}$ and $n\geq1$. Every location
has one pointer field with value in $V$. Loops, repeated heads and equality
of the two location registers are allowed. No nil-stop is imposed.

## Notation

For a vector $s=(s_v)_{v\in V}$ and $a\in S_v$, write $s[v:=a]$ for the
vector obtained by replacing only coordinate $v$. The same notation applies
to functions $f:V\to V$.

The indicator of a condition $E$ is $\mathbf1_E$. The fibre of a self-map
$F$ at $z$ means the full set $F^{-1}(\{z\})$, unless a restricted domain is
explicitly named. A recurrent state of a finite deterministic map means a
periodic state, not a state which merely eventually enters a periodic orbit.

For an unordered pair of labels, $[a,b]$ denotes an undirected edge,
including a loop when $a=b$. Multiset addition is denoted by $\uplus$.

## Proof Strategy

Recover a predecessor directly from its last updated location. This yields
the local-memory count and pointer inverse without an experiment. Encode
cyclic local states as distinguished arcs to establish an exact conjugacy,
then apply the already-owned rotor theorem only with its hypotheses.

## Dependency Map

1. Step 2 uses only the literal local update and independent coordinates.
2. Step 3 uses the single-cycle hypothesis and the rotor definition. Only
   its final recurrent conclusion cites Holroyd et al., Lemma 3.4 and
   Theorem 3.8.
3. Step 4 uses the pointer literal and a two-sided inverse calculation.
4. Step 5 uses Step 4 plus direct counting and multiset cancellation.
5. Source priority and internal occupancy are separate evidence claims
   documented in SOURCES_AND_SUBTRACTION.md; the elementary calculations
   do not establish novelty or priority.

## Proof

### Step 1. Freeze both autonomous maps

The local-memory carrier and one tick are
$$
\mathcal X=V\times\prod_{v\in V}S_v,\qquad
T(x,s)=\bigl(o_x(U_x(s_x)),\,s[x:=U_x(s_x)]\bigr).
$$
Thus the memory at the current vertex is updated before the move, and all
other memories retain their old values. The assumptions make the output
belong to the same finite carrier.

The pointer carrier and one tick are
$$
\mathcal P_n=V\times V\times V^V,\qquad
R(u,v,f)=\bigl(v,f(v),f[v:=u]\bigr).
$$
The first register remembers the previous location and the second is the
current location. This tick reverses the current pointer toward the first
register and moves the two-register window forward using the old pointer.
All three output coordinates belong to the stated carrier, even when
locations coincide.

### Step 2. Full-state predecessor atlas for local memory

For $a\in S_v$, put
$$
c_v(a)=|\{b\in S_v:U_v(b)=a\}|.
$$
Fix a target $(y,t)\in\mathcal X$. Then
$$
|T^{-1}(y,t)|
=\sum_{v\in V}\mathbf1_{\{o_v(t_v)=y\}}\,c_v(t_v).
\tag{1}
$$

Indeed, if a predecessor has current vertex $v$, every coordinate other than
$v$ must equal the corresponding coordinate of $t$. Its old coordinate at
$v$ must be one of the $c_v(t_v)$ preimages of $t_v$ under $U_v$.
The outgoing location is then $o_v(t_v)$; it equals $y$ precisely under
the displayed indicator condition. Conversely, every such local preimage,
together with the forced other coordinates and current vertex $v$, gives
a predecessor. Different choices of $v$ are disjoint because the first
coordinate of the predecessor is different. This proves (1), including
targets with no predecessor.

For $v,y\in V$, define
$$
m_v(y)=
\max\bigl(\{c_v(a):a\in S_v,\ o_v(a)=y\}\cup\{0\}\bigr).
$$
The exact maximum over the entire carrier is
$$
\max_{(y,t)\in\mathcal X}|T^{-1}(y,t)|
=\max_{y\in V}\sum_{v\in V}m_v(y).
\tag{2}
$$
For fixed $y$, each summand in (1) is at most $m_v(y)$, proving the upper
bound. If $m_v(y)>0$, choose $t_v$ attaining that maximum. If $m_v(y)=0$,
every allowed $t_v$ makes the corresponding summand zero, so any choice
works. Nonemptiness of every $S_v$ makes all these choices possible,
independently for different vertices. They attain the sum for each fixed
$y$; finiteness and nonemptiness of $V$ let us choose a maximizing $y$.
This proves equality in (2).

Equations (1) and (2) are consequences of one-coordinate overwrite. Alone
they supply no recurrent geometry or nontrivial temporal theorem for a new
choice of local updates.

### Step 3. Exact rotor conjugacy and its limits

Assume each $U_v$ is a single-cycle permutation. Construct $H$ on vertex set
$V$ with one distinguished arc $e_{v,a}$ from $v$ to $o_v(a)$ for each
$a\in S_v$. Even if two outputs coincide, their arcs have different labels.
Give the arcs out of $v$ the cyclic successor
$$
e_{v,a}^{+}=e_{v,U_v(a)}.
$$
There is at least one outgoing arc at every vertex. Send $(x,s)$ to the
chip position $x$ and the rotor choice
$$
\rho(v)=e_{v,s_v}\qquad(v\in V).
$$
This correspondence is bijective: an arc out of $v$ has exactly one
distinguished state label $a$, so every rotor configuration recovers $s$.

Advancing the rotor at $x$ replaces $e_{x,s_x}$ with
$e_{x,U_x(s_x)}$. Moving along the new arc sends the chip to
$o_x(U_x(s_x))$. No other rotor changes. Therefore the bijection commutes
with the update $T$ and the rotor operation; this is a conjugacy on the
full carrier, not merely equality of a projected chip trajectory.

If $H$ is strongly connected, the cited rotor theorem applies: its
periodic chip-and-rotor states are exactly the configurations with one
directed rotor cycle and the chip on that cycle. Rotor routing restricts
to a permutation of these unicycles. These imported conclusions are
already covered by the original rotor source and the old C181 package.
[Holroyd et al., Definition 3.1, Lemma 3.4 and Theorem 3.8](https://arxiv.org/pdf/0801.3306).

Since $c_v(a)=1$ for permutations, (1) and (2) become
$$
|T^{-1}(y,t)|=|\{v\in V:o_v(t_v)=y\}|,
\qquad
\max_{(y,t)}|T^{-1}(y,t)|
=\max_{y\in V}|\{v\in V:y\in o_v(S_v)\}|.
\tag{3}
$$
The right side counts contributing source vertices, not incoming arcs:
parallel arcs do not create extra predecessors with the same source vertex
and target memory. The full-state fibre may exceed one even when the target
is a unicycle. The fibre under the restriction to unicycles is exactly one;
these two assertions concern different domains.

For completeness, arbitrary deterministic $U_v$ also fit the primary
hidden-memory update definition by assigning transition mass one to
$U_v(a)$ and jump mass one to $o_v(b)$ after the update to $b$.
The augmented last-exit coordinate is redundant on the invariant set
$$
\rho(v)=o_v(s_v)\quad(v\in V).
$$
The lift $(x,s)\mapsto(x,\rho=o(s),s)$ is bijective onto this set and
commutes with the deterministic update. This is a definition-level
embedding in Remark 2.1, not an application of subsequent stochastic
ergodicity theorems.
[Kaiser, Levine and Sava-Huss, Remark 2.1](https://arxiv.org/html/2412.13766v3).

Nothing here makes a noncyclic $U_v$ a rotor cyclic order on its entire
state set. No noncyclic-specific candidate with a fresh temporal theorem
is proposed in this desk.

### Step 4. Two-sided inverse for pointer reversal

For a target $(p,q,g)\in\mathcal P_n$, define
$$
I(p,q,g)=\bigl(g(p),p,g[p:=q]\bigr).
\tag{4}
$$
Apply $R$ to this state. The new first and second registers are $p$ and
$q$, since the old pointer at $p$ in $g[p:=q]$ is $q$. The new function is
$$
\bigl(g[p:=q]\bigr)[p:=g(p)]=g.
$$
Thus $R(I(p,q,g))=(p,q,g)$.

In the other direction, put $g=f[v:=u]$, $p=v$ and $q=f(v)$.
Then $g(p)=u$ and
$$
g[p:=q]=\bigl(f[v:=u]\bigr)[v:=f(v)]=f.
$$
Consequently $I(R(u,v,f))=(u,v,f)$. Equation (4) is a two-sided inverse.
No distinctness of $u$, $v$ and $f(v)$ was used.

The map is therefore a permutation of the finite nonempty set
$\mathcal P_n$. Every state lies on a periodic orbit from time zero, and
each positive iterate remains a bijection, so every positive-iterate
fibre has cardinality one.

### Step 5. Fixed states, edge invariant and reverser

Equality $R(u,v,f)=(u,v,f)$ forces $u=v$ from the first register and
$f(v)=v$ from the second. These two conditions also imply that the overwritten
pointer retains its old value, so they are sufficient. For each of the
$n$ choices of $v$, the other $n-1$ pointer values are free. Hence
$$
|\operatorname{Fix}(R)|=n\,n^{n-1}=n^n.
\tag{5}
$$
At $n=1$ the carrier has one state; (4) and (5) give that same fixed state.

Define the augmented undirected edge multiset
$$
\mathcal E(u,v,f)
=\left(\biguplus_{x\in V}\{[x,f(x)]\}\right)\uplus\{[u,v]\}.
\tag{6}
$$
Set $w=f(v)$. A tick removes the pointer edge $[v,w]$ and inserts
$[v,u]$, while the extra register edge changes from $[u,v]$ to $[v,w]$.
Since $[v,u]=[u,v]$, the total multiset is unchanged. This cancellation
uses multiset multiplicities, so it remains valid for loops and coinciding
edges.

Finally set
$$
J(u,v,f)=(v,u,f),\qquad
K(u,v,f)=\bigl(f(v),v,f[v:=u]\bigr).
$$
The map $J$ swaps registers twice to give the identity. The map $K$ keeps
$v$ fixed and swaps the first register with the pointer at $v$, so applying
it twice restores both values and every other coordinate. Thus
$J^2=K^2=\mathrm{id}$ and $R=J\circ K$. It follows that
$$
J\circ R\circ J=K\circ J=R^{-1}.
\tag{7}
$$
This gives a reversing involution; it does not assert that $R$ itself is
an involution.

All three claims follow. $\square$

## Corrections or Missing Assumptions

No correction to the stated claims is needed. Two tempting extensions were
explicitly excluded:

- The recurrent unicycle characterization needs strong connectivity for its
  converse. Only the rotor conjugacy and full-state fibre formula are used
  without that assumption.
- The in-place LISP source imposes list, finiteness, purity and isolation
  conditions and has a stop case. Its algorithm is not asserted to be the
  literal full autonomous carrier $\mathcal P_n$. Only the pointer-update
  kernel is attributed to that source.

## Open Risks

No unproved step remains in the displayed algebra. This is not a separate
independent review or a finite verification claim. The classification of
all exact pointer periods, or a nontrivial census by invariant graph, was
not attempted and is not credited as a surviving theorem axis. The results
do not prove global absence of a novel finite graph-memory system.

