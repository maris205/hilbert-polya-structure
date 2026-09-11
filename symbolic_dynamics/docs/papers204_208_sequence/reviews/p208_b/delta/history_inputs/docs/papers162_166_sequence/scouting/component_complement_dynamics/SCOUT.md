# Component-complement dynamics (CCD): exact scout and strict gate

**Scout date:** 2026-09-03 UTC  
**Lifecycle:** `HOLD_EXTERNAL`  
**Decision:** **`KILL_TOO_ELEMENTARY_CLOSURE_COMPLEMENT_COMPOSITE`**  
**Mathematical audit:** `0` counterexamples; `257,729` assertions; two fresh
canonical replays byte-matched

## 1. Decision first

All requested formulas are correct.  For labelled simple graphs of order
`n>=2`, the empty and complete graphs form the unique two-cycle.  Every other
connected graph enters it after one step; every nonempty disconnected graph
enters after two.  The sharp height is therefore two for `n>=3`, while order
two has no transient states.  The first image consists of exactly the
complete multipartite graphs and has Bell size.  A prescribed multipartite
target has the product of connected-graph edge polynomials as its exact
fibre, and all later weighted fibres collapse to the connected/disconnected
split with parity exchanged.

This complete solvability is also the fatal value signal.  Let `L(G)` fill
every connected component into a clique.  Then

```text
C(G) = complement(L(G)).                                  (1.1)
```

The operator `L` is simply the equivalence/transitive closure of undirected
adjacency.  Hence CCD is a complement-after-closure composite.  The
closure/complement interaction is classical; the image is the elementary
complement of the cluster graphs; and each target fibre merely prescribes the
connected components, so its polynomial is the classical labelled SET of
connected graphs evaluated on fixed blocks.  No theorem survives subtraction
as an independent, owner-thin dynamical or inverse axis.

The internal gate is equally decisive.  P123 already occupies nontrivial
component/complement dynamics, and the portfolio explicitly excludes another
graph-component complement unless it has a genuinely different theorem
engine.  P118 and the current true-twin projection scout already occupy the
complete-multipartite/partition-image plus block-sensitive-fibre silhouette.
CCD is strictly simpler than each.  It is therefore killed rather than used
to fill a paper slot.

## 2. Literal definition and conventions

Let `G_n` be the `2^N` labelled simple graphs on `[n]`, where

```text
N = binom(n,2).
```

For `G in G_n`, let `pi(G)` be its connected-component partition.  If
`pi={B_1,...,B_k}`, write `K_pi` for the complete multipartite graph with
parts `B_i`: two vertices are adjacent exactly when they lie in different
blocks.  Define

```text
C(G) = K_(pi(G)).                                          (2.1)
```

Equivalently, complete each component of `G` into a clique and take the
simple-graph complement.  Let `E_n` and `K_n` denote the empty and complete
graphs.  A singleton graph is connected.  For `n>=2`, `E_n` is disconnected.

The transient depth of a state is its distance to the recurrent core.

## 3. Exact functional graph

### Theorem 3.1 — recurrent core and pointwise depth

For `n>=2`,

```text
C(E_n)=K_n,             C(K_n)=E_n.                        (3.1)
```

This two-cycle is the entire recurrent core.  More precisely:

1. if `G` is connected, then `C(G)=E_n`;
2. if `G` is disconnected and nonempty, then `C(G)` is connected and is
   neither `E_n` nor `K_n`;
3. consequently every connected `G` outside the core has depth one, and
   every disconnected nonempty `G` has depth two.

### Proof

If `G` is connected, `pi(G)` has one block, and the complete multipartite
graph with one part has no edges.  This proves item 1 and (3.1) for `K_n`.

If `G` is disconnected, its component partition has at least two blocks.
The graph `K_(pi(G))` is connected: vertices in different parts are adjacent,
while two vertices in one part have a path of length two through any other
part.  If `G` is nonempty, at least one component has two vertices, so the
corresponding part contains a missing edge in `K_(pi(G))`; hence the image is
not complete.  It is nonempty because there are at least two parts.  This
proves item 2.  A connected noncomplete graph maps next to `E_n`, after which
(3.1) forces the core alternation.  No state outside the displayed cycle can
recur.

### Boundaries and sharpness

- At `n=1`, `E_1=K_1`; it is a fixed point, not a two-cycle.
- At `n=2`, the only graphs are `E_2` and `K_2`; both are recurrent and the
  global height is zero.
- For every `n>=3`, a spanning path is connected noncomplete and has depth
  one.  The graph consisting of the edge `{1,2}` and `n-2` isolates is
  disconnected nonempty and has depth two.  Thus the height-two bound is
  sharp exactly from order three onward.

The labelled functional graph has one two-cycle for every `n>=2`.  All
connected noncomplete graphs point directly to `E_n`; every disconnected
nonempty graph points to a connected noncomplete complete multipartite graph,
which then points to `E_n`.

## 4. Exact depth edge polynomials

Define

```text
A_n(z)    = sum_(G in G_n) z^(e(G))
          = (1+z)^N,

Conn_n(z) = sum_(G in G_n connected) z^(e(G)),             (4.1)
```

with `Conn_1(z)=1`.  For `n>=2`, Theorem 3.1 gives the exact-depth
polynomials

```text
D_(n,0)(z) = 1 + z^N,
D_(n,1)(z) = Conn_n(z) - z^N,
D_(n,2)(z) = A_n(z) - Conn_n(z) - 1.                       (4.2)
```

The three terms are respectively:

- the empty/complete recurrent pair;
- connected graphs other than `K_n`; and
- disconnected graphs other than the empty graph.

They are disjoint and sum to `A_n(z)`.  At `n=2`, both positive-depth
polynomials vanish.  At `n=1`, formula (4.2) must not double-count
`E_1=K_1`; the corrected boundary is

```text
D_(1,0)(z)=1,              D_(1,1)=D_(1,2)=0.             (4.3)
```

The connected polynomial itself satisfies the classical distinguished-
vertex recurrence

```text
Conn_n(z)
 = A_n(z)
   - sum_(s=1)^(n-1) binom(n-1,s-1)
       Conn_s(z) A_(n-s)(z).                              (4.4)
```

Indeed, expose the component containing vertex `1`, choose its other `s-1`
labels, put a connected graph on them, and an arbitrary graph on the
remaining labels.  The verifier checks (4.4) coefficientwise through `n=6`.

## 5. Image and every-target weighted fibre

### Theorem 5.1 — exact image

```text
im(C) = {K_pi : pi is a set partition of [n]},             (5.1)
```

so

```text
|im(C)|=B_n.                                               (5.2)
```

Every image is complete multipartite by definition.  Conversely, for any
partition `pi`, the disjoint union of cliques on its blocks has component
partition `pi` and maps to `K_pi`.  Distinct partitions give distinct
multipartite graphs because nonadjacency recovers the parts.

Moreover,

```text
im(C^t)={E_n,K_n}                    for n>=2 and t>=2.     (5.3)
```

### Theorem 5.2 — all targets and all source edge counts

For a labelled target `H`, define

```text
Phi_H(z)=sum_(G:C(G)=H) z^(e(G)).                          (5.4)
```

If `H=K_pi` and the blocks of `pi` have sizes `s_1,...,s_k`, then

```text
Phi_(K_pi)(z) = product_(i=1)^k Conn_(s_i)(z).             (5.5)
```

If `H` is not complete multipartite, then

```text
Phi_H(z)=0.                                                (5.6)
```

### Proof

The equality `C(G)=K_pi` holds exactly when the connected-component
partition of `G` is `pi`.  Such a source has no edge between distinct blocks,
and the graph induced on every block must be connected.  Choices on the fixed
label blocks are independent, and edge counts add, proving the product.  The
image theorem proves (5.6).

Summing all fibres recovers the classical component exponential formula at
fixed label set:

```text
sum_(pi in Pi_n) product_(B in pi) Conn_(|B|)(z)=A_n(z).   (5.7)
```

### Extremal coefficients

The smallest number of edges in a source with component blocks of sizes
`s_i` is

```text
n-k = sum_i(s_i-1).                                       (5.8)
```

Let

```text
tau(1)=1,                 tau(s)=s^(s-2) for s>=2.         (5.9)
```

Cayley's labelled-tree count gives

```text
[z^(n-k)] Phi_(K_pi)(z) = product_i tau(s_i).             (5.10)
```

These are precisely the spanning forests whose prescribed components are
trees on the blocks of `pi`.

The largest source edge count is

```text
M_pi=sum_i binom(s_i,2),                                  (5.11)
```

and

```text
[z^(M_pi)] Phi_(K_pi)(z)=1.                               (5.12)
```

The unique maximizer is the disjoint union of cliques on the target parts.
Both extremes are direct consequences of the connected-factor product; they
are not separate inverse axes.

## 6. Complete time-t kernel and weighted fibres

The deterministic kernel from an individual source is fully explicit.  For
`n>=2`,

```text
C^0(G)=G,
C^1(G)=K_(pi(G)),

C^t(G) = K_n  if t>=2 and
                 [(G connected and t even) or
                  (G disconnected and t odd)],

C^t(G) = E_n  if t>=2 and
                 [(G connected and t odd) or
                  (G disconnected and t even)].           (6.1)
```

Here `E_n` counts as disconnected.  This includes both recurrent states.

For an all-source edge-weighted formulation, put

```text
Phi_(t,H)(z)=sum_(G:C^t(G)=H) z^(e(G)).                   (6.2)
```

At `t=0`,

```text
Phi_(0,H)(z)=z^(e(H)).                                    (6.3)
```

At `t=1`, equations (5.5)--(5.6) apply.  For all `t>=2`, the only supported
targets are `E_n,K_n`, and

```text
t even:
  Phi_(t,E_n)(z)=A_n(z)-Conn_n(z),
  Phi_(t,K_n)(z)=Conn_n(z);

t odd:
  Phi_(t,E_n)(z)=Conn_n(z),
  Phi_(t,K_n)(z)=A_n(z)-Conn_n(z).                         (6.4)
```

All other target fibres are zero.  Thus parity merely exchanges the connected
and disconnected source polynomials.  At `n=1`, the sole target is
`E_1=K_1` and its fibre polynomial is `1` at every time.

## 7. Independent exhaustive verifier

`verify_scout.py` uses only the Python standard library and imports no author
or repository code.  Graphs are independent bit masks; connected components
are constructed with a literal disjoint-set traversal.  The run exhausts all
labelled simple graphs through order six and checks:

- the component partition and literal complete-multipartite update;
- the unique recurrent core and exact pointwise depths;
- the `n=1`, `n=2`, and sharp `n>=3` boundaries;
- all three depth polynomials coefficientwise;
- exact image equality and Bell cardinality;
- every one-step target, including every zero fibre;
- the connected-polynomial product for every labelled partition target;
- minimum forest and maximum clique coefficients for every target;
- the fibre mass identity and connected-graph recurrence;
- every time-`t` weighted fibre through `t=6`; and
- the per-source connected/disconnected parity rule.

Frozen result:

```text
graphs_exhausted=33867
assertions=257729
STATUS PASS
```

Two fresh executions matched `CANONICAL.txt` byte for byte; source-only syntax
compilation passed.

```text
CANONICAL.txt sha256
ff8210ef6bc0c3e700e74fb676799b934122ffb67a9036412e9f09dc602dc631

verify_scout.py sha256
4218b080855f0caa57dfeedd63e464d72dcf1b5603dc3442344ef3110070d6e4
```

Finite enumeration is counterexample pressure, not proof, ownership, or
release authorization.

## 8. Owner/value subtraction

The detailed primary-source record is in `OWNER_SEARCH_LOG.md`.  The main
subtraction is:

| CCD component | owner-covered input | residual |
|---|---|---|
| `G ->` clique completion of components | transitive/equivalence closure of symmetric adjacency | zero credit |
| complement after closure and its iterates | Graham--Knuth--Motzkin closure/complement operator algebra | a very degenerate symmetric case |
| image as complete multipartite graphs | complement of cluster graphs; set partitions | Bell bijection, zero credit |
| prescribed target fibre | connected graphs placed independently on fixed component blocks | product of classical `Conn_s(z)` |
| depth census | connected versus disconnected partition of all graphs | subtraction of two classical polynomials |
| `t>=2` fibres | the same connected/disconnected split with parity | no new axis |

The bounded search did not locate a paper naming precisely the simple-graph
self-map (2.1) and printing all formulas (4.2), (5.5), and (6.4) together.
That non-hit is not novelty.  Graham--Knuth--Motzkin directly own the
underlying closure/complement composition; Gilbert owns connected labelled
graph enumeration by edge count; Prisner establishes iteration/image/fixed
points as standard graph-operator questions.  The residual is packaging, not
a paper-scale conjunction.

## 9. Internal collision gate

| occupied or killed item | comparison |
|---|---|
| P123 odd-component complementation | **Decisive.** P123 needed a parity-pruned component/co-component tree, sharp order-growing depth, and an all-depth EGF. CCD removes the scheduler and collapses to height two. The historical firewall explicitly excludes another graph-component complement. |
| P118 synchronous mex on complete multipartite graphs | Same complete-multipartite part structure, depth-at-most-two architecture, and part-size-sensitive exact fibres; P118 has a genuinely nontrivial quotient dynamics. |
| current true-twin projection scout | Even closer image/fibre silhouette: a graph is projected to a Bell-indexed cluster graph with a prescribed-partition edge polynomial. That candidate was already killed as a one-step classical decomposition. CCD merely complements the Bell-indexed output and adds one forced core alternation. |
| P80 cocktail-party majority | Only a broad two-cycle/zeta and complete-multipartite-family overlap; no literal transfer. It still removes value from a bare two-cycle census. |
| P127 parity-transpose digraphs | Different literal algebra, but its shallow collapse and codomain-wide fibres are materially richer. |
| P143 Boolean row residual | Different relation operator; it already has image characterization, `T^3=T`, Bell fixed objects, and a nontrivial quotient-poset fibre. |
| P145 vertex-push chains | Component data drive a random product spectrum and recovery theorem; no literal collision, but a much stronger component-sensitive second axis. |
| P158 cut-intersection collapse | Different stochastic update; its every-target fibre has a real resource obstruction and history geometry absent from CCD. |

The candidate is not conjugate to P80, P118, P127, P143, P145, or P158.
That cannot overcome the direct P123 policy collision and the absence of an
owner-resistant theorem axis.

## 10. Final gate

```text
FORMULAS_CORRECT YES
EXHAUSTIVE_REPLAY PASS_X2
EXACT_NAMED_WHOLE_PACKAGE_OWNER BOUNDED_NON_HIT
NON_HIT_USED_AS_NOVELTY NO
CLOSURE_COMPLEMENT_MECHANISM_DIRECTLY_OWNED YES
CONNECTED_GRAPH_FIBRE_ENGINE_DIRECTLY_OWNED YES
INTERNAL_COMPONENT_COMPLEMENT_EXCLUSION YES
INDEPENDENT_RESIDUAL_AXIS NO
GREEN_OWNER_THIN NO
DECISION KILL_TOO_ELEMENTARY_CLOSURE_COMPLEMENT_COMPOSITE
HOLD_EXTERNAL
```

Do not allocate CCD to P162--P166.  Preserve it only as a compact exact
negative control for future graph-operator scouting.
