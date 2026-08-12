# Proof Package — Bisimulation and Clock Obstructions

## Claim

Three scoped claims are proved.

1. A strong forward-bisimulation quotient of a **finite** directed acyclic
   graph is acyclic.
2. A quotient of a level-graded graph is acyclic whenever the quotient
   equivalence preserves a class label that is injective in the level. For
   the wheel recursion, the exact next multiplier $q_{k+1}$ is such a label.
3. A finite-alphabet, fixed-finite-window decoder cannot recover the unbounded
   exact wheel clock $(q_k)$.

## Status

**PROVABLE AS STATED**

## Assumptions

- A directed graph is acyclic when it has no directed cycle of positive
  length.
- In Claim 1 the graph $G=(V,E)$ is finite.
- An equivalence relation $\sim$ is a strong forward bisimulation when, for
  every $v\sim w$:
  - if $vEv'$, there is $w'$ with $wEw'$ and $v'\sim w'$;
  - if $wEw'$, there is $v'$ with $vEv'$ and $v'\sim w'$.
- The quotient has an edge $[v]\to[v']$ exactly when some representatives
  $u\in[v]$ and $u'\in[v']$ satisfy $uEu'$.
- In Claim 2, $V=\bigsqcup_{k\ge0}V_k$, every edge goes from $V_k$ to
  $V_{k+1}$, and a label $\lambda$ is constant on each $V_k$ with pairwise
  distinct values across levels. The equivalence respects $\lambda$.
- In Claim 3 the alphabet and decoder window are finite, and the decoder is a
  single fixed function rather than a cutoff-dependent table.

## Notation

- $[v]$ is the $\sim$-equivalence class of $v$.
- $G/{\sim}$ is the quotient graph.
- For the wheel graph, $V_k$ is level $k$ and
  $\lambda(v)=q_{k+1}$ for $v\in V_k$.
- $A^W$ denotes the set of patterns on a fixed finite window $W$ over an
  alphabet $A$.

## Proof Strategy

Claim 1 is proved by contradiction: a quotient cycle can be lifted, one edge
at a time, through the bisimulation to an infinite path in the original
finite DAG. Claim 2 constructs a well-defined quotient grading. Claim 3 is
the finite-image principle for a function on a finite domain.

## Dependency Map

1. Claim 1 uses finiteness, acyclicity, and the successor-matching half of
   strong forward bisimulation.
2. Claim 2 uses only strict level growth and label preservation; it does not
   depend on Claim 1 or on graph finiteness.
3. The wheel corollary to Claim 2 uses the proved fact that consecutive
   multipliers $q_{k+1}$ are pairwise distinct primes.
4. Claim 3 uses finiteness of both $A$ and $W$, plus unboundedness of the
   prime sequence.

## Proof

### Step 1 — a finite-DAG strong-bisimulation quotient is acyclic

Assume for contradiction that $G/{\sim}$ contains a directed cycle

$$
C_0\longrightarrow C_1\longrightarrow\cdots\longrightarrow C_{m-1}
\longrightarrow C_m=C_0,
\qquad m\ge1.
$$

For each $i\in\{0,\ldots,m-1\}$, the definition of a quotient edge supplies
representatives $a_i\in C_i$ and $b_{i+1}\in C_{i+1}$ with
$a_iEb_{i+1}$, where indices are read modulo $m$.

Choose any $v_0\in C_0$. Suppose $v_j\in C_i$, with
$i\equiv j\pmod m$, has been chosen. Since $v_j\sim a_i$ and
$a_iEb_{i+1}$, the successor-matching condition supplies a vertex
$v_{j+1}$ such that

$$
v_jEv_{j+1}
\quad\text{and}\quad
v_{j+1}\sim b_{i+1}.
$$

Thus $v_{j+1}\in C_{i+1}$. Induction constructs an infinite directed path
$v_0Ev_1Ev_2E\cdots$ in $G$.

A finite directed acyclic graph has no infinite directed path: an infinite
sequence of vertices in finite $V$ repeats a vertex, and the segment between
two repetitions is a directed cycle. This contradicts acyclicity of $G$.
Therefore $G/{\sim}$ is acyclic.

### Step 2 — a level-injective class label preserves acyclicity

Because the values of $\lambda$ are pairwise distinct across levels and
$\sim$ respects $\lambda$, every equivalence class is contained in one
level $V_k$. Define

$$
\bar k([v])=k\quad\text{when }v\in V_k.
$$

This is well-defined. If $[v]\to[w]$ is a quotient edge, there are
representatives $v'\in[v]$ and $w'\in[w]$ with $v'Ew'$. Strict level
growth gives

$$
\bar k([w])=\bar k([v])+1.
$$

Along a directed path of positive length, $\bar k$ therefore increases
strictly. Such a path cannot return to its initial class, so the quotient is
acyclic. No finiteness assumption is used in this step.

For the wheel recursion, $q_{k+1}$ is the $(k+1)$-st rational prime and is
therefore different at every level. A quotient that requires the exact
multiplier to be a state-class label, or requires a state-only decoder to
return one exact multiplier for the entire class, satisfies the hypotheses
with $\lambda(v)=q_{k+1}$. It cannot merge levels or create a cycle.

### Step 3 — a finite local decoder cannot recover the exact unbounded clock

Let $A$ be finite and $W$ be a fixed finite window. Then $A^W$ is finite. Any
fixed decoder

$$
d:A^W\longrightarrow\mathbb N
$$

has finite image. The wheel multipliers are all rational primes and hence
form an unbounded, infinite set. Therefore no such $d$ can output every exact
multiplier $q_k$. An exact recoding must instead use a countable alphabet,
unbounded memory, or a decoder whose domain contains additional unbounded
data.

All three claims follow. $\square$

## Corrections or Missing Assumptions

- Claim 1 is false without finiteness. The one-way infinite path
  $0\to1\to2\to\cdots$ is acyclic, while identifying all vertices is a
  strong-bisimulation quotient with one self-loop.
- Claim 2 applies only when $q_{k+1}$ is constant on quotient classes. It
  does not cover an edge decoder or a path-window decoder that can distinguish
  representatives of one state class.
- A one-way simulation, bounded-radius observational equivalence, or arbitrary
  graph homomorphic image need not be a strong bisimulation and is not covered
  by Claim 1.
- Finite-cutoff bisimulation partitions have terminal-boundary effects. Their
  apparent stability cannot define an infinite quotient without a separate
  consistency theorem.

## Open Risks

- A countable-alphabet or infinite-memory factor may evade Claim 3; it must be
  defined before numerical testing.
- If periodic words occur only in the closure of a recoded image, the project
  must prove how their arithmetic clock is inherited rather than assigning it
  afterward.
- A coarse quotient can manufacture mixed primitive words by concatenating
  transitions from incompatible representatives. Its path-lifting and
  prime-power ledger remain separate obligations.
