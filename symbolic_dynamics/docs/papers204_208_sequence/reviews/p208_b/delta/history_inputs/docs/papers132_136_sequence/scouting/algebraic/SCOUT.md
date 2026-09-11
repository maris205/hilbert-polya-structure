# Algebraic/arithmetic breadth scout for the P132--P136 round

Status: **SCOUT ONLY / NO PAPER NUMBER / NO GIT / HOLD EXTERNAL**  
Owner-search date: **2026-08-31 UTC**  
Mechanical status: **PASS; 27 literal systems; 531,206 exact assertions**

## 1. Outcome first

This lane locked exactly 27 pairwise literal-different finite maps before
theorem fitting.  It found one plausible proof-spike candidate, one
theorem-complete but heavily owned reserve, and one complete functional graph
whose main period theorem is directly owned.

| rank | handle | theorem-scale signal | honest recommendation |
|---:|---|---|---|
| 1 | `A02` | A squarefree divisor map becomes a triangular Boolean network on the Pratt divisibility DAG.  The proposed all-prime-set package has no fixed points, only two-cycles, `2^s` recurrent states from `s` source phases, a Pratt-height transient bound, and an every-target inclusion--exclusion fibre formula. | **CONDITIONAL PROOF SPIKE.**  This is the only lane candidate whose literal map was not located in the bounded owner search.  Kill it if the arithmetic lift is judged cosmetic after the Boolean reduction. |
| 2 | `M01` | On at-most-three-generator abelian `p`-group types, `G -> Lambda^2 G` is accidentally closed: `W^3=W^2`, all fixed points, the image, and every one-step and terminal fibre have closed formulas. | **RESERVE / OWNER HEAVY.**  The invariant-factor transformation is explicitly classical; a specialist must decide whether the dynamical packaging has any independent value. |
| 3 | `M02` | Syzygy on indecomposable modules over a self-injective cyclic Nakayama algebra has a complete functional graph: one fixed zero, projective leaves, explicit nonprojective periods, cycle counts, fixed iterates, and zeta product. | **DIRECT-OWNER CONTROL, NOT A CLEAN PROMOTION.**  Marks's Lemma 5.12 already owns the exact two period cases; almost everything remaining is immediate packaging. |

`P01` (derivative-remainder descent) remains a proof-burden reserve, but it is
not promoted above these three: the pilot has no all-degree fibre law and its
Euclidean-polynomial silhouette is too close to P128/P131.  No claim in this
ledger is a novelty or priority claim.

## 2. Protocol, counting, and reproducibility

An assertion is one deterministic equality or carrier-membership check in
`verify_algebraic_scout.py`.  All arithmetic is exact and the script uses only
the Python standard library.  The 531,204 per-system checks below plus two
global scope/uniqueness checks give the frozen total 531,206.

| family | systems | assertions |
|---|---:|---:|
| squarefree divisor arithmetic | 5 | 6,627 |
| abelian-group/Nakayama module functors | 5 | 26,658 |
| polynomial transforms | 5 | 337,836 |
| linear, bilinear, and code transforms | 5 | 10,926 |
| group/cluster controls | 5 | 24,848 |
| local/residue-ring controls | 2 | 124,309 |
| **per-system subtotal** | **27** | **531,204** |
| global sentinels | -- | 2 |
| **total** | **27** | **531,206** |

The frozen transcript is `CANONICAL.txt`.  A fresh run is compared without a
persistent scratch output by

```bash
python docs/papers132_136_sequence/scouting/algebraic/verify_algebraic_scout.py
cmp docs/papers132_136_sequence/scouting/algebraic/CANONICAL.txt \
  <(python docs/papers132_136_sequence/scouting/algebraic/verify_algebraic_scout.py)
```

Enumeration is a falsification device, not a proof.  In particular, the
all-parameter statements in Section 4 are theorem contracts/proof routes,
not consequences of the finite boxes by themselves.

## 3. Literal catalogue and disposition

The observable in every row is the functional-graph statistic named in the
pilot column: fixed/recurrent counts, maximum tail/period, image/fibres, or
depth layers.  Full parameter profiles are preserved in `CANONICAL.txt`.

### 3.1 Squarefree divisor arithmetic

| handle | carrier and literal map | exact pilot and signal | disposition |
|---|---|---|---|
| `A01` | For squarefree `n`, divisors `d|n`; `d -> gcd(n,phi(d))`. | Three prime sets of sizes 5, 6, 7; 224 states; **2,801** assertions.  Support is the Pratt-edge image and absorption depth is the longest selected prime-chain length plus one. | **FAMILY CONTROL.**  The Pratt DAG itself owns the clock; weaker than `A02`. |
| `A02` | Same carrier; `d -> gcd(n,(n/d)phi(d))`. | 224 states; **1,132** assertions.  Profiles `(sources,recurrent,max tail,image,max fibre)` are `(1,2,3,8,10)`, `(2,4,4,17,8)`, `(4,16,2,25,8)`; every target fibre was checked against the formula in Section 4.1. | **LEAD.**  Exact literal owner not found; Pratt-tree and Boolean-network machinery receive zero credit. |
| `A03` | Same carrier; `d -> gcd(n,phi(n/d))`. | 224 states; **902** assertions.  Unique fixed divisor in each box; maximum tails 4, 4, 2. | **RESERVE SIBLING.**  Same arithmetic DAG as `A02`, but a weaker unique-attractor package. |
| `A04` | Same carrier; `d -> gcd(n,sigma(d))`. | 224 states; **896** assertions.  `q+1` support relations give periods at most two and four recurrent states in each box. | **KILL OWNER.**  After support encoding this is exactly a disjunctive relation-image map. |
| `A05` | Same carrier; `d -> gcd(n,J_2(d))`. | 224 states; **896** assertions.  The `q^2-1` relation is denser but again has only the same short Boolean-image dynamics. | **KILL SIBLING.**  Only the edge predicate changed from `A04`. |

### 3.2 Module functors

| handle | carrier and literal map | exact pilot and signal | disposition |
|---|---|---|---|
| `M01` | Isomorphism types of abelian `p`-groups with exponent at most `p^e` and generator rank at most three; `G -> Lambda^2 G`. | `1<=e<=12`; 1,819 types; **3,764** assertions.  State count `C(e+3,3)`, fixed count `e+1`, image count `C(e+2,2)`, depth at most two, and all fibres verified. | **RESERVE OWNER HEAVY.**  The structural type formula is classical, so the dynamics may be only a short corollary. |
| `M02` | Zero plus indecomposables `M(i,l)` of `A_{n,e}=kQ_n/J^e`, where `Q_n` is the oriented `n`-cycle; syzygy `Omega`. | All `2<=n<=10`, `2<=e<=9`; 2,448 states; **11,376** assertions.  Projectives alone have tail one; every nonprojective period matches the gcd formulas in Section 4.3. | **LEAD OWNER HEAVY / CONTROL.**  Direct period owner located. |
| `M03` | Same indecomposable carrier plus zero; `M -> rad M`. | 2,448 states; **2,448** assertions.  Exact absorption time is composition length. | **KILL OWNER.**  This is the Loewy radical filtration. |
| `M04` | Same carrier; `M -> M/soc M`. | 2,448 states; **2,448** assertions.  Exact length clock with stationary top label. | **KILL SIBLING.**  Dual Loewy erosion adds no second theorem. |
| `M05` | Nonprojective indecomposables of cyclic self-injective Nakayama algebras; Auslander--Reiten translate `tau`. | 2,156 states; **6,622** assertions.  Each length stratum is a vertex-rotation cycle. | **KILL OWNER.**  The update is the standard AR-quiver rotation. |

### 3.3 Polynomial transforms

| handle | carrier and literal map | exact pilot and signal | disposition |
|---|---|---|---|
| `P01` | Zero plus monic `f in F_p[x]` of bounded degree; `f -> monic(f mod f')`, fixing derivative-zero states. | `(p,D)=(2,8),(3,7),(5,6),(7,5)`; 42,934 states; **257,494** assertions.  Strict degree descent and tails 1, 2, 3, 3 expose characteristic-`p` terminal strata. | **RESERVE PROOF BURDEN.**  No all-degree fibre theorem; derivative Euclidean/subresultant ownership and P128/P131 adjacency remain. |
| `P02` | Fixed-degree monic polynomials; classical Graeffe transform (root squaring). | 1,796 states; **7,191** assertions.  Mixed tails/periods outside characteristic two; every binary polynomial is fixed. | **KILL DIRECT OWNER.**  Graeffe iteration is the literal classical operation. |
| `P03` | Monic degree `m`, `p` not dividing `m`; translate by the unique shift killing the `x^(m-1)` coefficient. | 17,646 states; **70,599** assertions.  A uniform `p`-to-one idempotent retraction onto depressed polynomials. | **KILL THIN.**  Tschirnhaus centering is classical and stops in one step. |
| `P04` | Tangent-to-identity series modulo `x^(D+1)` over `F_p`; compositional inverse. | 270 states; **1,353** assertions.  Exact fixed/two-cycle counts in three finite Nottingham quotients. | **KILL OWNER.**  Reversion is involutive by definition. |
| `P05` | Projective binary forms; substitute `(X,Y)->(X+Y,X)`. | 397 states; **1,199** assertions.  Periods track the projective order of one Fibonacci matrix. | **KILL OWNER.**  A standard `PGL_2` representation action. |

### 3.4 Linear, bilinear, and code transforms

| handle | carrier and literal map | exact pilot and signal | disposition |
|---|---|---|---|
| `L01` | Subspaces of `F_2^d`, `d=3,4`; `U -> A(U^perp)` for the fixed upper-unitriangular Jordan block `A`. | 83 states; **336** assertions.  The square is `U -> AA^(-T)U`; maximum periods 8 and 10 and no fixed points. | **RESERVE OWNER HEAVY.**  Twisted polarities/asymmetry own the reduction and no all-`d` census emerged. |
| `L02` | `GL_2(F_2)`, `GL_2(F_3)`, `GL_2(F_5)`, `GL_3(F_2)`; `A -> A^(-T)A`. | 702 states; **2,808** assertions.  Mixed tails 2--3 and periods 1--12. | **KILL NO SPINE.**  Mature cosquare theory plus no uniform pilot law. |
| `L03` | Invertible `2x2` matrices over odd `F_p` with `I+/-A` invertible; `A -> (I-A)(I+A)^(-1)`. | 1,712 states; **6,851** assertions.  Closed-domain involution and fixed counts 6, 20, 58 for `p=3,5,7`. | **KILL OWNER/THIN.**  Classical Cayley involution. |
| `L04` | Disjoint union of binary linear codes of lengths 0 through 4; dualize, then puncture the last coordinate. | 91 states; **364** assertions.  Ambient length is the exact absorption time. | **KILL MECHANICAL.**  Ordinary duality plus shrinking ambient space. |
| `L05` | Subspaces of `F_2^d`, `d=3,4`; `U -> U intersect rho(U)` for cyclic coordinate rotation. | 83 states; **567** assertions.  `T^t(U)=intersection_(j=0)^t rho^j(U)` and the endpoint is the largest cyclic-code core in `U`. | **KILL CLOSURE.**  Generic invariant-core intersection. |

### 3.5 Group/cluster and local-ring controls

| handle | carrier and literal map | exact pilot and signal | disposition |
|---|---|---|---|
| `G01` | `F_p^3`; `(x,y,z)->(y,z,yz-x)`. | `p=3,5,7,11`; 1,826 states; **9,134** assertions.  Markoff--Fricke cubic preserved; maximum periods 12, 30, 48, 102. | **KILL DIRECT OWNER.**  Literal Fricke trace-map dynamics is mature. |
| `G02` | `F_p^3`; `(x,y,z)->(x,y,xy-z)`. | 1,826 states; **5,482** assertions.  Involution with `p^2` fixed states. | **KILL DIRECT OWNER.**  A single Vieta move. |
| `G03` | `(Z/mZ)^3`; sweep the adjacent pairs by `R(x,y)=(y,2y-x)`. | `3<=m<=10`; 3,016 states; **9,072** assertions.  Bijective braid sweep, maximum period six and exactly `m` fixed triples. | **KILL OWNER.**  Alexander-quandle/Burau linear braid action. |
| `G04` | `P^1(F_p)`; `x -> 1/(1-x)` with the usual infinity conventions. | Eight primes through 19; 85 states; **340** assertions.  Order three; fixed-point anomaly governed by discriminant `-3`. | **KILL OWNER.**  One order-three `PGL_2` element. |
| `G05` | `F_p^2`; area-preserving Henon map `(x,y)->(y,y^2+1-x)`. | `p=3,5,7,11`; 204 states; **820** assertions.  Polynomial permutation with long but nonuniform cycles. | **KILL OWNER / NO SPINE.**  Finite-field Henon dynamics is crowded and the pilot has no uniform census. |
| `R01` | `Z/2^e Z`; `x -> x^2(3-2x)`. | `2<=e<=13`; 16,380 states; **123,064** assertions.  Parity selects 0 or 1 and the 2-adic defect valuation doubles, giving every depth layer. | **KILL INTERNAL.**  Newton/Hensel error squaring was already rejected near P100. |
| `R02` | `Z/p^e Z`; `x -> x^2+x+1`. | Five prime-power boxes; 415 states; **1,245** assertions.  Tails/periods vary discontinuously with ramification. | **KILL GENERIC.**  No clean invariant, fibre theorem, or stable spectrum. |

## 4. Focused theorem contracts and proof routes

### 4.1 `A02`: totient-complement dynamics on a Pratt DAG

Let `P` be a finite nonempty set of distinct primes, let
`n=product_(p in P) p`, and identify `d|n` with
`S(d)={p in P:p|d}`.  Put a directed edge `q -> p` exactly when
`p | q-1`, and define

```text
F_n(d) = gcd(n,(n/d) phi(d)).
```

Squarefreeness gives the exact support rule

```text
F(S) = (P \ S) union N(S),
N(S) = {p in P : q -> p for some q in S}.
```

Equivalently, for the support bit `x_p`,

```text
x'_p = not x_p  OR  OR_(q -> p) x_q.                 (4.1)
```

Because `q -> p` implies `q>p`, the non-self interaction graph is a DAG.
Let `s` be its number of sources (vertices with no incoming edge), and let
`h` be its maximum directed-path length in edges.  The proposed temporal
theorem is:

1. there is no fixed state;
2. every recurrent state has exact period two;
3. there are `2^s` recurrent states and hence `2^(s-1)` two-cycles; and
4. every orbit enters recurrence by time at most `h+1`.

The source bits toggle freely.  Once their phases are fixed, process vertices
topologically.  If the two successive OR-inputs at a nonsource are `(u,v)`,
they cannot both be zero on a recurrent trajectory, and

```text
y = not x OR u,       x = not y OR v
```

has a unique phase pair.  This gives the recurrent census.  A second
topological induction on consecutive phase pairs is the intended proof of the
`h+1` transient bound.  The verifier deliberately checks a bound, not
sharpness: the three observed maximum tails are 3, 4, 2.

There is also an exact all-target one-step fibre formula.  For a target support
`B`, set `Z=P\B` and

```text
Par(U) = {q in P : q -> p for some p in U}.
```

Then inclusion--exclusion over the forbidden target-one events gives

```text
|F^(-1)(B)| =
  sum over T subseteq B with (Z union T) intersect Par(Z union T)=empty
    (-1)^|T| 2^(|P|-|Z union T|-|Par(Z union T)|).   (4.2)
```

Indeed, target zeros force `Z` to be one in the source state and `Par(Z)` to
be zero.  For `p in B`, the only bad source pattern is `x_p=1` with every
parent zero.  Intersecting a set `T` of bad events forces `Z union T` to one
and `Par(Z union T)` to zero, producing (4.2).  Formula (4.2) was checked for
every target in all three boxes, not only for image targets.

The proof route is therefore arithmetic support factorization -> triangular
phase induction -> target-wise inclusion--exclusion.  An independent control
route is the literal integer computation versus the bit-DAG computation at
every state, which is included in the verifier.

**Zero-credit boundary.**  Ford--Konyagin--Luca own prime chains
`p_j | p_(j+1)-1` and Pratt-tree height; generic synchronous Boolean networks,
signed interaction graphs, source vertices, and feedback arguments are also
background.  The only possible residual is the conjunction of the literal
arithmetic self-map with the complete temporal and target-fibre package.

### 4.2 `M01`: exterior-square dynamics in generator rank at most three

Encode

```text
G = direct_sum_i Z/p^(a_i)Z
```

by a partition `lambda=(a_1>=...>=a_r>=1)`, with `r<=3` and `a_1<=e`.
The exterior-square type map is

```text
W(lambda) = sort_desc {min(a_i,a_j): i<j}.
```

Thus

```text
W(())=(),  W((a))=(),  W((a,b))=(b),
W((a,b,c))=(b,c,c).                                  (4.3)
```

The rank-three closure is the special accident `C(3,2)=3`; it already fails
as a bounded-rank self-map in rank four.  Formula (4.3) gives the complete
candidate theorem immediately:

- `|X_e|=C(e+3,3)` and `|im W|=C(e+2,2)`;
- `W^3=W^2`, with fixed types `()` and `(c,c,c)`, `1<=c<=e`;
- the one-step fibre of `()` is `e+1`;
- the one-step fibre of `(b)` is `e-b+1`;
- the one-step fibre of `(u,v,v)` is `e-u+1` for `u>=v>=1`, and every other
  target fibre is zero;
- the terminal fibre of `()` under `W^2` is
  `1+e+C(e+1,2)`; and
- the terminal fibre of `(c,c,c)` is `C(e-c+2,2)`.

The proof is a direct count of partitions after applying (4.3), and the
verifier checks all formulas for `1<=e<=12`.  This is theorem-ready
mathematically, but not value-cleared.

**Zero-credit boundary.**  Frei--Loughran--Newton, Lemma 6.5, explicitly give
the invariant-factor formula for `Lambda^2 G`; that formula and the
classification of finite abelian groups receive zero credit.  No exact
iteration hit appeared in the bounded search, but `W^3=W^2` and the displayed
fibres are elementary consequences of the owned formula.  Absence of a search
hit is not enough to promote this reserve.

### 4.3 `M02`: syzygy functional graph for cyclic self-injective Nakayama algebras

Let `Q_n` be the oriented cycle `i -> i+1 (mod n)` and
`A_{n,e}=kQ_n/J^e`.  Write `M(i,l)` for the indecomposable of top `S_i` and
length `l`, and adjoin the zero module.  With this convention,

```text
Omega(0)=0,
Omega(M(i,e))=0,
Omega(M(i,l))=M(i+l,e-l)       for 1<=l<e,            (4.4)
Omega^2(M(i,l))=M(i+e,l).
```

Put `g=gcd(n,e)`, `a=floor((e-1)/2)`, and `L=2n/g`.  For every nonmidlength
`l` (`2l != e`), the exact period is `L`.  If `e` is even and `l=e/2`, put
`g_0=gcd(n,e/2)` and `L_0=n/g_0`; the exact period is `L_0`.  Consequently the
complete graph consists of:

- one fixed zero with the `n` projectives as one-step leaves;
- for each of the `a` unordered length pairs `{l,e-l}`, exactly `g` cycles of
  length `L`; and
- when `e` is even, `g_0` midlength cycles of length `L_0`.

Every nonprojective target has indegree one, every projective target has
indegree zero, and zero has indegree `n+1`.  The fixed-iterate count is

```text
Fix(Omega^t) = 1 + 2na [L divides t]
                 + [e even] n [L_0 divides t],        (4.5)
```

and the Artin--Mazur zeta function of the finite map is

```text
zeta(z) = (1-z)^(-1) (1-z^L)^(-ag)
          * (1-z^L_0)^(-g_0)  if e is even,           (4.6)
```

with the last factor omitted for odd `e`.  Formula (4.4) follows from the
minimal projective cover; the rest is rotation orbit counting.

**Zero-credit boundary.**  Marks's Lemma 5.12 states the same two exact
periodicity conditions, while Dugas proves the broader periodicity of
self-injective algebras of finite representation type.  Thus (4.4), both
period cases, and general periodicity are not residual claims.  Equations
(4.5)--(4.6), the projective leaves, and the indegree census are immediate
finite-map assembly.  This candidate is useful as a completeness control but
should not receive a paper slot without a specialist identifying a genuinely
new module-theoretic output.

## 5. Primary-owner search and bounded conclusions

Only primary papers or official publisher/preprint records are used for the
technical ownership conclusions below.  Exact-query non-hits are recorded as
bounded observations, never as novelty certificates.

### 5.1 `A02`

Queries included `"gcd(n,(n/d) phi(d))" dynamics divisors`,
`"gcd(n" "phi(d)" divisors iteration`, `"(n/d)phi(d)" gcd divisors`, and
`"triangular Boolean network" periodic points`.  No result stated the literal
map or formulas (4.1)--(4.2).

- Kevin Ford, Sergei Konyagin, and Florian Luca,
  [*Prime Chains and Pratt Trees*](https://doi.org/10.1007/s00039-010-0089-0),
  GAFA 20 (2010), 1231--1258
  ([author preprint](https://arxiv.org/abs/0904.0473)), own the prime-chain
  relation and Pratt-tree height.  They do not study the present divisor
  self-map in the material screened.
- Julio Aracena, Luis Cabrera-Crot, and Lilian Salinas,
  [*Finding the fixed points of a Boolean network from a positive feedback
  vertex set*](https://doi.org/10.1093/bioinformatics/btaa922),
  Bioinformatics 37 (2021), 1148--1155, supply current primary background for
  signed Boolean interaction graphs, sources, acyclic propagation, and
  feedback arguments.  Their results are not the source-phase two-cycle or
  target-fibre theorem above.

Conclusion: **literal owner not located in this bounded search; owner status
remains open**.  Pratt and Boolean machinery must be visibly subtracted.

### 5.2 `M01`

Queries included `"iterate" "exterior square" "finite abelian" group`,
`"exterior square" "finite abelian p-group" invariant factors`, and quoted
searches for the cyclic-gcd direct-sum formula.  No iteration paper was found.

- Christopher Frei, Daniel Loughran, and Rachel Newton,
  [*The Hasse norm principle for abelian
  extensions*](https://arxiv.org/abs/1508.02518), American Journal of
  Mathematics 140 (2018), 1639--1685,
  [DOI 10.1353/ajm.2018.0048](https://doi.org/10.1353/ajm.2018.0048),
  explicitly prove in Lemma 6.5 that if
  `G=direct_sum_j Z/n_j Z` with `n_(j+1)|n_j`, then
  `Lambda^2 G` has `(j-1)` copies of `Z/n_j Z`.  This directly owns (4.3)'s
  structural input.

Conclusion: **no direct iteration hit, but severe owner compression**.  The
remaining census is an elementary bounded-rank corollary, so this is not a
clean novelty lead.

### 5.3 `M02`

Queries included `syzygy self-injective Nakayama Omega indecomposable module
formula`, `"Lemma 5.12" "self-injective Nakayama"`, and quoted searches for
the two periodicity cases.

- Frederik Marks,
  [*Universal localisations and tilting modules for finite dimensional
  algebras*](https://arxiv.org/abs/1307.6496), Journal of Pure and Applied
  Algebra 219 (2015), 3053--3088,
  [DOI 10.1016/j.jpaa.2014.10.003](https://doi.org/10.1016/j.jpaa.2014.10.003),
  Lemma 5.12, directly states the nonmidlength even-period condition
  `(z/2)e=0 mod n` and the midlength condition `z(e/2)=0 mod n`.
- Alex Dugas,
  [*Periodic resolutions and self-injective algebras of finite
  type*](https://arxiv.org/abs/0808.1311), Journal of Pure and Applied Algebra
  214 (2010), 990--1000,
  [DOI 10.1016/j.jpaa.2009.09.012](https://doi.org/10.1016/j.jpaa.2009.09.012),
  proves the broader finite-representation-type periodicity theorem.

Conclusion: **direct owner collision** for the central period theorem.  The
finite-map zeta and leaf attachment do not by themselves clear the value gate.

## 6. P1--P131 collision firewall

The intake comparison used the on-disk portfolio and prior scout ledgers.  In
particular, P099 occupies unipotent shear on integer sublattices, P103 double
adjugation, P107 annihilator/power ideal dynamics, P109 nilpotent image
dynamics on subspace lattices, P115 Cartier coefficient dynamics, P119 Engel
commutator dynamics, P124 cross-colon monomial ideals, P125 a quadratic-state
shear, P127 parity/transpose looped-digraph dynamics, P128 polynomial
translate--gcd dynamics, and P131 Euclidean quotient queues.

- `A02` is not P084's Ramanujan/Cayley-shift spectral arithmetic, nor the
  stochastic proper-residue gcd/totient descent killed in the P122--P126
  round.  Its carrier is the divisor lattice of one fixed squarefree `n`, its
  update is deterministic, and its separating invariant is the negative-self
  triangular Pratt network with source-controlled two-cycles.
- `M01` and `M02` use functor iteration on isomorphism types, not P109's
  nilpotent linear image filtration.  This literal separation does not repair
  their external owner problems.
- `P01` is separated literally from P128 and P131, but all three use
  polynomial gcd/Euclidean structure.  Without an all-degree inverse/fibre
  theorem, that adjacency is fatal at this stage.
- `L01`--`L05` are not P127's parity-matrix update, but their strongest laws
  collapse to classical polarity, Cayley, duality, or invariant-core
  operations.
- `R01` is explicitly killed by the prior Newton/Hensel error-squaring
  mechanism rather than recycled as a new local-ring system.

Literal distinctness is only the first firewall.  Generic finite-map census,
Boolean-network propagation, partition counting, gcd rotation, and standard
functor identities receive zero contribution credit.

## 7. Devil's-advocate checkpoint and handoff

The hostile reading is deliberately asymmetric:

1. `A02` may still be only a pleasant arithmetic encoding of a simple
   triangular Boolean network.  It deserves one proof/value spike because
   the every-target fibre formula and source-phase recurrence coexist in one
   literal arithmetic map, not because an owner search missed it.
2. `M01` is mathematically complete but almost embarrassingly close to a
   three-line corollary of a known invariant-factor formula.  Do not spend a
   paper slot without specialist validation of residual value.
3. `M02` has a direct owner for its central theorem and should normally be
   killed.  Its role here is to show that a visually rich functional graph is
   not enough after source subtraction.
4. `P01` should not displace a cleaner system until an all-degree theorem
   explains the characteristic-`p` depth layers and target fibres.

Accordingly, this lane hands the batch selector **one conditional lead
(`A02`), one owner-heavy reserve (`M01`), and one direct-owner completeness
control (`M02`)**.  It assigns no paper number and authorizes no external
release, posting, contact, submission, novelty claim, or priority claim.

## 8. AI-assistance disclosure and limitations

The system definitions, exact code, algebraic reductions, proof sketches, and
source triage were prepared with AI assistance.  Every finite assertion is
deterministically reproducible from the checked-in script.  The literature
search was bounded by the stated queries and accessible primary records; it
is not an exhaustive MathSciNet/zbMATH/specialist review.  The promoted
formulae still require an independent human proof audit and specialist owner
subtraction before any manuscript freeze.
