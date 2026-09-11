# True-twin projection on labelled simple graphs — strict exact scout

**Decision: `KILL_DIRECT_COPOINT_SPECIES_AND_INTERNAL_TWIN_QUOTIENT`.**

The proposed formula is correct, including its partition-lattice direction,
signs, block-internal exponent, and all small boundaries.  The candidate is
nevertheless below the batch threshold.  Gessel and Li's point-determining
graph paper already identifies co-point-determining graphs as exactly the
graphs with distinct closed neighborhoods and proves the species identity

```text
G = Q o K_+,
```

which says that every graph is uniquely a co-point-determining graph with a
nonempty clique substituted at each vertex.  That is precisely the static
decomposition underlying every fibre here.  Encoding the true-twin partition
as a cluster graph makes the operation literally idempotent, but does not add
a temporal axis.  The edge-weighted, prescribed-block-size Möbius polynomial
is a valid multivariate refinement; after subtraction it is one compact
enumerative corollary, not two independent theorem axes.

The system remains **`HOLD_EXTERNAL`**.  No paper allocation or theorem
contract is frozen.

## 1. Literal map

Let `G` be a labelled simple graph on `[n]`.  Write `N_G[v]` for the closed
neighborhood of `v`, and let

```text
u ~_G v  iff  N_G[u]=N_G[v].
```

This is equality of sets, hence an equivalence relation.  Define `tau(G)` on
the same labelled vertex set by joining two distinct vertices exactly when
they lie in the same equivalence class.  Thus `tau(G)` is the cluster graph
whose clique components are the true-twin classes of `G`.

The empty graph at `n=0` is included as a useful algebraic boundary.  Omitting
it changes no positive-rank statement.

## 2. Cold dynamics

### Proposition 2.1 — image, fixed locus, and idempotence

Every true-twin class is a clique.  Indeed, if `u!=v` and
`N_G[u]=N_G[v]`, then `u in N_G[u]=N_G[v]`, so `uv` is an edge.  Equality of
closed neighborhoods also makes adjacency between two distinct classes
uniform.

For a cluster graph with component partition `pi`, every vertex in a block
has that whole block as its closed neighborhood, while different blocks give
different sets.  Therefore

```text
tau^2=tau,
im(tau)=Fix(tau)={cluster graphs on [n]}.
```

The image and fixed count are the Bell number `B_n`.  Every nonfixed graph has
depth one, so the global height is one for `n>=3` and zero for `n<=2` (all
graphs on at most two vertices are cluster graphs).  There are no nontrivial
periodic or higher-depth states.

## 3. Every-target edge-weighted fibre

Fix a target cluster graph with partition

```text
pi={B_1,...,B_k},   s_i=|B_i|>0.
```

Define

```text
Phi_pi(z)=sum_{G:tau(G)=pi} z^{e(G)}.                    (3.1)
```

Here `tau(G)=pi` abbreviates equality with the cluster graph encoded by `pi`.

### 3.1 Quotient derivation

If all vertices of `B_i` have one closed neighborhood, then `B_i` is a
clique.  Uniform external adjacency gives, for every pair `i<j`, either all
`s_i s_j` cross edges or none.  Hence `G` is the clique blow-up of a unique
simple graph `H` on `[k]`.

Two target blocks merge into one true-twin class of `G` exactly when their
vertices in `H` have equal closed neighborhoods.  Consequently

```text
tau(G)=pi  iff  H is co-point-determining
                 (all N_H[i] are distinct).             (3.2)
```

This gives the equivalent positive formula

```text
Phi_pi(z)
 = z^{sum_i binom(s_i,2)}
   sum_{H co-point-determining on [k]}
       z^{sum_{ij in E(H)} s_i s_j}.                     (3.3)
```

Formula (3.3) proves coefficient positivity but uses the already-owned
co-point species directly.

### 3.2 Partition-lattice Möbius derivation

Order `Part([k])` by refinement and let `0hat` be the singleton partition.
For `Gamma in Part([k])`, put

```text
S_C=sum_{i in C}s_i,
mu(0hat,Gamma)=product_{C in Gamma}(-1)^{|C|-1}(|C|-1)!.
```

Let `A_Gamma` be the family of graphs for which all original target blocks
indexed by one part `C` are contained in a common true-twin class.  Such a
part forces their union to be a clique; distinct parts have an arbitrary
all-or-nothing complete join.  Therefore its edge enumerator is

```text
F(Gamma)
 = z^{sum_C binom(S_C,2)}
   product_{C<D}(1+z^{S_C S_D}).                         (3.4)
```

If `Rho` is the true-twin partition induced on `[k]`, then `A_Gamma` is the
event `Gamma<=Rho`.  Thus

```text
F(Gamma)=sum_{Rho>=Gamma} Exact(Rho).
```

Möbius inversion at `0hat` has exactly the proposed orientation and gives

```text
Phi_pi(z)
 = sum_{Gamma in Part([k])}
     mu(0hat,Gamma)
     z^{sum_C binom(S_C,2)}
     product_{C<D}(1+z^{S_C S_D}).                       (3.5)
```

No sign correction or global prefactor is missing.  In particular, the
internal edges of the original `B_i` are already included in every
`binom(S_C,2)` term.

## 4. Boundary checks and consequences

- `n=0`, `k=0`: the empty partition contributes `Phi=1`.
- `k=1`: `Phi=z^{binom(n,2)}`; only the complete graph maps to the one-block
  target.
- `k=2`: the joined quotient has two true twins and cancels under inversion,
  leaving `Phi=z^{binom(s_1,2)+binom(s_2,2)}`.
- For sizes `(2,1,1)`, the only admissible quotient graphs are the empty graph
  and the three labelled two-edge paths, giving
  `Phi=z+2z^4+z^5`.

Let `q_k` be the number of labelled co-point-determining graphs on `[k]`.
Evaluating (3.5) at one yields

```text
q_k=sum_{Gamma in Part([k])}
      mu(0hat,Gamma) 2^{binom(|Gamma|,2)},                (4.1)
```

so every target with `k` blocks has the same unweighted fibre size.  The
first values from the independent verifier are

```text
q_0,...,q_7 = 1,1,1,4,32,588,21476,1551368.
```

This also gives the standard mass identity

```text
sum_{k=0}^n S(n,k)q_k = 2^{binom(n,2)}.                  (4.2)
```

The minimum exponent of `Phi_pi` is

```text
v_pi=sum_i binom(s_i,2),
```

with coefficient one, because the empty quotient is co-point-determining and
any quotient edge adds positive weight.  Hence `n+2v_pi=sum_i s_i^2` is
recoverable from the polynomial.  Also `Phi_pi(1)=q_k` recovers `k` for
`k>=3`: adjoining an isolated labelled vertex injects the `k`-vertex class
into the `(k+1)`-vertex class, and the path `P_{k+1}` shows strictness for
`k>=2`.  The sole collision `q_1=q_2=1` is separated by the valuation when
`n>=2`, because the one-block valuation is `binom(n,2)` and every two-block
valuation is smaller.

These recovery observations are correct, but both are read directly from the
same fibre polynomial.  They do not create an independent structural axis.

## 5. Exact executable evidence

`verify_scout.py` uses only the Python standard library and three separately
implemented routes:

1. **Literal route:** for every one of the **2,131,020** labelled simple
   graphs across `0<=n<=7`, construct all closed-neighborhood bitsets, form
   their equality partition, and accumulate the original edge count in the
   corresponding target fibre.
2. **Möbius route:** independently evaluate (3.5) using generated set
   partitions and the explicit partition-lattice Möbius function.
3. **Quotient route:** enumerate every graph on the `k` target blocks, retain
   exactly those with distinct closed neighborhoods, and lift quotient edges
   with weights `s_i s_j` as in (3.3).

For every labelled target partition through `n=7`, the three polynomials are
identical coefficient by coefficient.  The verifier also checks all Bell
image/fixed counts, idempotence for every target, positivity, fibre mass,
valuation, the size-independent total, the displayed boundary polynomials,
and quotient counts.  The frozen run contains **9,367 explicit assertions**;
the millions of graph visits are aggregated before equality assertions rather
than inflating the counter once per loop iteration.

## 6. External subtraction

The decisive source is Ira M. Gessel and Ji Li, “Enumeration of
Point-Determining Graphs,” *Journal of Combinatorial Theory, Series A* 118
(2011), 591--612, DOI
[10.1016/j.jcta.2010.03.009](https://doi.org/10.1016/j.jcta.2010.03.009).
Their Theorem 2.2 defines co-point-determining graphs by distinct closed
neighborhoods and proves `G=Q o K_+`.
[Primary preprint/full text](https://arxiv.org/abs/0705.0042)

This source receives full credit for:

- the canonical true-twin clique partition;
- the co-point-determining quotient;
- unique clique substitution/blow-up of every graph;
- enumeration of the quotient class; and
- the unweighted fact that a prescribed `k`-block fibre has size `q_k`.

Generic twin modules, graph substitution, and quotient language are also
standard within modular decomposition; see Habib and Paul,
“A survey of the algorithmic aspects of modular decomposition,” *Computer
Science Review* 4 (2010), 41--59, DOI
[10.1016/j.cosrev.2010.01.001](https://doi.org/10.1016/j.cosrev.2010.01.001).
Partition-lattice Möbius inversion and its product formula are classical; see
Rota, “On the foundations of combinatorial theory I,” 1964, DOI
[10.1007/BF00531932](https://doi.org/10.1007/BF00531932).

No inspected primary text was found that prints (3.5) verbatim with arbitrary
prescribed clique sizes and original-edge variable `z`.  This is a bounded
non-hit, not novelty or priority evidence.  Because (3.5) follows in one
inversion step from the directly owned unique substitution, its residual
credit is too small.

## 7. Internal and same-batch collision audit

The requested controls give the following result:

- **P118:** different mex dynamics on a fixed complete multipartite graph,
  but labelled block-size-sensitive fibre formulas are already occupied.
- **P127:** different looped-digraph matrix map, yet idempotent projection and
  codomain-wide exact fibres are occupied.
- **P143:** strong architecture collision: a Boolean-relation map into a
  quotient preorder, followed by an inclusion--exclusion every-target fibre.
- **P152:** only broad graph-dynamics proximity; its stochastic triad kernel
  and absorption mechanism do not transfer.

Two earlier internal kills are even more decisive:

- The P112--P116 breadth scout's `C9` already killed weighted open/closed twin
  quotienting as directly owned by twin reduction and modular decomposition.
- The P157--P161 breadth scout's `GQT` independently killed equal-neighborhood
  quotienting as `KILL_DIRECT_TWIN_QUOTIENT`, explicitly citing the earlier
  `C9` result.

Within the current batch, outdegree-residue clustering already projects
labelled digraphs to cluster graphs and derives block-size-sensitive
every-target fibre spectra.  Its literal statistic differs, but it removes any
claim that “cluster projection plus block-size fibre” supplies portfolio
separation.

## 8. Strict gate

The strongest possible residual package is:

```text
one-step idempotent encoding
+ prescribed-size edge-weight refinement of G=Q o K_+
+ two easy statistics read from that polynomial.
```

The temporal axis is vacuous, the image/fixed/Bell result is immediate, the
unweighted fibre is directly owned, and both recovery statements are
corollaries of the same weighted inversion.  This does not meet the demand for
two independent theorem axes.  Extending the polynomial with another marker
would refine the same owner rather than create a new mechanism.

**Final verdict: `KILL_DIRECT_COPOINT_SPECIES_AND_INTERNAL_TWIN_QUOTIENT`.**
Keep the exact negative result and verifier; do not allocate a paper number.

