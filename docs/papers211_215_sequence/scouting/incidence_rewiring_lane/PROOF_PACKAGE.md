# SDS: recurrence boundary, not an admitted two-axis contract

## Claim and status

For the all-$n$ literal in INTAKE.md, the following claims are **PROVABLE AS
STATED**: every labelled vertex degree is nonincreasing; old connected
components never merge; the recurrent graphs are exactly disjoint unions
of components containing no degree-two vertex and isolated odd cycles;
their periods are explicit signed orders of $2$; and the entrance time
has the nonsharp bound below. An independent all-target inverse, global
fibre maximum and sharp all-size entrance bound are **NOT CURRENTLY
JUSTIFIED**. No finite enumeration is used in these proofs.

## Assumptions and notation

Graphs are finite, simple, undirected and labelled on $[n]$, with isolates
retained. Write $D=D(G)$, $C=[n]\setminus D$, $e(G)=|E(G)|$, and $c(G)$
for the number of connected components, with $c(\varnothing)=0$.
Let $p(G)$ be the number of path components in the induced graph $G[D]$;
an isolated vertex counts as a path. All other components of $G[D]$ are
cycles. Let $\tau(G)$ be the first entrance into a periodic orbit, with
time zero allowed. For odd $q\ge3$, define
$$
\rho(q)=\min\{r\ge1:2^r\equiv 1\text{ or }-1\pmod q\}.
$$
This exists because multiplication by $2$ permutes the nonzero invertible
residue classes modulo odd $q$; two powers coincide, giving a positive
power equal to $1$.

## Strategy and dependency map

1. Count possible output incidences at each old vertex.
2. Count old edges incident to $D$ and generated edges to force strict
   edge loss whenever $G[D]$ has a path component.
3. If no such path exists, the old degree-two vertices are isolated whole
   cycle components; all remaining components are already fixed.
4. Compute the literal action on a labelled cycle using cyclic indices.
5. Combine strict loss and the explicit isolated-cycle action. No external
   convergence theorem, source abstract or empirical pattern is a premise.

## 1. Coordinatewise degree loss and component refinement

Suppose first that $v\in C$. An output edge at $v$ is either an old edge
from $v$ to $C$, or is produced by one old neighbour $u\in D$: if
$N_G(u)=\{v,w\}$, the vertex $u$ supplies the single edge $vw$. Thus
$$
d_{F(G)}(v)\le |N_G(v)\cap C|+|N_G(v)\cap D|=d_G(v).
$$
Duplicates can only reduce this count. If $v\in D$, no edge of
$E(G[C])$ touches it. Each output edge at $v$ must come from an old
neighbour in $D$, and each such neighbour supplies one candidate edge.
Therefore
$$
d_{F(G)}(v)\le |N_G(v)\cap D|\le2=d_G(v).
$$
This includes isolated outputs and all coincidences of candidate edges.
Summing degrees proves $e(F(G))\le e(G)$.

Every output edge is either an old edge or joins the endpoints of an old
two-edge path. Its endpoints lie in one old connected component. Hence
the connected-component partition can only refine, and
$c(F(G))\ge c(G)$. This does not assert that all components necessarily
split at every update.

## 2. Strict loss outside the cycle/fixed decomposition

Every vertex of $G[D]$ has degree at most two. A finite connected graph
of maximum degree two is a path (including a singleton) or a cycle:
starting at a degree-at-most-one vertex traces all vertices of a connected
component without branching; if none exists, following successive unused
edges returns to its initial vertex and connectedness leaves no exterior
vertex. Consequently, writing $d=|D|$,
$$
|E(G[D])|=d-p(G).
$$
The number of old edges with at least one endpoint in $D$ is
$2d-|E(G[D])|$. There are at most $d$ distinct generated neighbour pairs.
It follows that
$$
e(F(G))\le e(G)-2d+|E(G[D])|+d=e(G)-p(G). \tag{1}
$$
Thus $p(G)>0$ forces at least one edge to disappear in the edge-count
sense, though particular new edges can be added.

If $p(G)=0$, every vertex of $D$ has its two neighbours in $D$. There are
no edges between $D$ and $C$, so the components in $D$ are whole isolated
cycle components of $G$. The components on $C$ contain no degree-two
vertex in $G$ and are unchanged by $F$. This property persists: the
cycle components evolve independently, and the fixed components cannot
create new edges to them. This is a permanent decomposition, not a
quotient that forgets an evolving decoration.

## 3. Literal labelled-cycle calculation

Let an isolated cycle have distinct labels $(v_0,\ldots,v_{l-1})$ in
cyclic order, $l\ge3$. Its neighbour-pair edges after one step are
$$
\{v_i,v_{i+2}\},\qquad i\in\mathbb Z/l\mathbb Z.
$$
For odd $l$, these form one cycle. At time $t$ the edge set is precisely
$\{\{v_i,v_{i+2^t}\}:i\in\mathbb Z/l\mathbb Z\}$. This follows
inductively because the two neighbours of $v_i$ at a current step $s$
are $v_{i-s},v_{i+s}$, whose new edge has step $2s$. No duplicate causes
a drop when $l$ is odd and $s$ is invertible modulo $l$.

Two invertible steps $s,s'$ specify the same labelled cycle edge set if
and only if $s'\equiv s$ or $-s\pmod l$: equality of the neighbours of
$v_0$ gives $\{v_s,v_{-s}\}=\{v_{s'},v_{-s'}\}$. Thus the exact period
of an odd cycle is $\rho(l)$, not necessarily the ordinary order of $2$.
In particular the triangle has period one.

If $l=4$, the output consists of the two opposite edges, a fixed matching.
If $l\ge6$ is even, one step splits the cycle into the two parity classes,
each carrying a cycle of length $l/2$. Distinct old connected components
cannot merge back. Write $l=2^a q$ with $q$ odd. For $q\ge3$, the exact
cycle entrance time is $a$; at that time there are $2^a$ odd $q$-cycles,
each of period $\rho(q)$. For $q=1$ one has $a\ge2$, the exact entrance
time is $a-1$, and the endpoint is a matching. Exactness follows because
before the stated time there is an even cycle: its next update either
splits its component or, at length four, drops its edge count. It cannot
already be periodic by the monotonicities proved above.

This action on isolated cycles is exactly the familiar two-step/open-
neighbourhood graph operation. Its power/root arithmetic is zero-credit
background, not a new period mechanism.

## 4. Complete recurrence and nonsharp entrance bound

If $G$ is recurrent, monotonicity of edge count forces equality throughout
its orbit. Equation (1) then implies $p(G)=0$. By Section 2, it is a
disjoint union of fixed degree-two-free components and isolated cycles.
An even cycle cannot be recurrent by Section 3. Therefore every cycle
component in $D$ is odd.

Conversely, a graph of this form is periodic: the first class of components
is fixed, and each odd cycle has finite period $\rho(l)$. Since the
components have disjoint fixed label sets, the exact graph period is the
least common multiple of their $\rho(l)$ values, taking the least common
multiple of an empty family to be one. Thus the claimed recurrent class
is an if-and-only-if statement, including $n=0,1,2$.

Let $s$ be the first time $p(F^s(G))=0$. Such a time exists: otherwise
(1) would force a nonnegative integer edge count to decrease forever.
Before that time, every update drops at least one edge, so $s\le e(G)$.
After time $s$ only the independent isolated cycles can be transient.
Define
$$
L(n)=\begin{cases}0,&0\le n\le3,\\
\lfloor\log_2 n\rfloor-1,&n\ge4.
\end{cases}
$$
Every cycle on at most $n$ vertices has entrance time at most $L(n)$:
for a power of two this is Section 3 directly; if $q\ge3$ and $a\ge1$,
then $2^{a+1}\le2^a q\le n$, which gives $a\le L(n)$.
Odd cycles have entrance zero. Therefore
$$
\tau(G)\le e(G)+L(n). \tag{2}
$$
The bound for isolated-cycle unions alone is sharp when $n\ge4$, by a
cycle of length $2^{\lfloor\log_2 n\rfloor}$ and the remaining isolates.
No sharpness is claimed for (2) on the whole carrier.

For comparison, the integer potential $e(G)+n-c(G)$ also strictly drops
at every nonrecurrent state: either $p>0$ and (1) applies, or an even
isolated cycle splits (or loses edges at length four). This supplies
another generic bound, not a second independent contribution.

## 5. Inverse boundary and disposition

The empty graph has itself as its unique predecessor. Indeed, a nonempty
graph with $D=\varnothing$ is fixed and nonempty; a graph with
$D\ne\varnothing$ generates at least one neighbour-pair edge. This
elementary fibre fact is not an independent inverse axis.

An arbitrary predecessor could be searched by choosing its old set $D$,
its path/cycle structure on $D$, its incident endpoints in $C$ and its
old graph on $C$, and then enforcing the target and degree constraints.
No target-local characterization, evaluated non-generic fibre formula,
sharp maximum or equality classification has been obtained by this
observation. Rephrasing that search as a finite sum would not close the
missing obligation. The cyclic part alone also reduces to ordinary
cycle-power roots and is not a residual inverse theorem.

Status: **NO_PROMOTION / ONE_LITERAL / ZERO_SCIENCE**. The recurrence
proof is useful negative evidence; its components are generic monotone
loss plus a known cycle operation. No pilot is warranted by an incomplete
second axis. These author proofs have not received independent review.

