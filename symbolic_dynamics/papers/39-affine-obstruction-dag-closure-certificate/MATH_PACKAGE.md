# Paper 39 mathematical architecture — SD-C41

## Executive verdict

Paper 39 can prove a rigorous closure theorem, but only relative to its
retrospective affine encoding, assembled from hashed Papers 35--38 artifacts
after their outcomes were known and frozen before the Paper-39 checker. The
theorem's source object is a typed obstruction DAG, not a fifth affine
mechanism.

The strict Route-A tuple is

```text
(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)
overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
affine_branch: CLOSE_ENTIRE_AFFINE_BRANCH
```

The realized registry decision is

```text
RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY
```

because the Session-4 preregistration/source lock independently froze six
non-affine candidates, `SD-C01`--`SD-C06`, before their own evaluation. This
is a governance handoff without ranking or selection. The code

```text
STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR
```

is retained as the conditional empty-registry fallback; its antecedent is
false in the hashed snapshot.

## 1. Canonical theorem

For $r\ge2$, let

$$
M_r=\langle u,v\mid vu=u^rv\rangle^+,
\qquad
G_r=\langle u,v\mid vuv^{-1}=u^r\rangle.
$$

The exact top-level repair alphabet has fourteen classes:
`affine_cayley_representation`, `finite_rank_local_system`, `character`,
`grading`, `quotient`, `induced_shift`, `first_return_map`,
`bass_serre_splitting`, `valuation_tree`, `boundary_model`, `modular_phase`,
`basepoint_damping`, `finite_total_weight_retrofit`, and `groupoid_trace`.
The finite instance universe has exactly sixteen stable tokens: six
theorem-covered frozen-family tokens, six explicit exit-only tokens, and one
tested plus one alternative-exit token for each of the two mixed classes.
Their exact IDs are listed in the source lock, derivation token table, and
`paper39_DAG_BRIDGE.json`; there is no catch-all instance token.

```text
AFFINE_CAYLEY_FROZEN_FAMILY
FINITE_RANK_LOCAL_SYSTEM_FROZEN_FAMILY
CHARACTER_FROZEN_FAMILY
GRADING_FROZEN_FAMILY
QUOTIENT_FROZEN_FAMILY
MODULAR_PHASE_FROZEN_FAMILY
INDUCED_SHIFT_EXIT
FIRST_RETURN_MAP_EXIT
VALUATION_TREE_EXIT
BOUNDARY_MODEL_EXIT
BASEPOINT_DAMPING_EXIT
FINITE_TOTAL_WEIGHT_RETROFIT_EXIT
FROZEN_ASCENDING_HNN_BASS_SERRE_SPLITTING
ALTERNATIVE_BASS_SERRE_SPLITTING_EXIT
FROZEN_TREE_LATTICE_GROUPOID_IMPORT
ALTERNATIVE_GROUPOID_CATEGORY_EXIT
```

Let $\mathcal P_{\rm fr}$ be the nonempty typed audit-provenance paths through
the seventeen internal transitions. If $p$ ends at $v$, its candidate datum is
typed only by the endpoint family $X_v(r)$. Define

$$
\mathfrak C_{\rm aff}(r)
=\coprod_{p\in\mathcal P_{\rm fr}}\{p\}\times X_{\operatorname{end}(p)}(r).
$$

The path records historical obligation flow, not cumulative mechanism
composition. The seventeen transitions refine positive affine Cayley sources,
formal inverse edges, Hashimoto reduction, quotient/Gibbs/Fock comparisons,
complete relation filling, scalar chain lift, ordinary/graded finite
coefficients, normal-closure saturation, and the Bass--Serre full tree
canonical for the frozen ascending-HNN splitting/presentation with its
canonical modular/tree-lattice/orbital/marker boundaries.

Define

$$
\operatorname{Good}(c)=I(c)\wedge R(c)\wedge S(c)
\wedge D(c)\wedge M(c)\wedge C(c),
$$

where the conjuncts respectively require intrinsic source, nonempty primitive
recurrence with repetitions, arithmetic selectivity, same-object determinant
ownership, marker compatibility, and frozen-control survival.

### Relative affine-branch closure theorem

$$
\boxed{
\forall r\ge2\;\forall c\in\mathfrak C_{\rm aff}(r),
\quad\neg\operatorname{Good}(c).}
$$

The balanced value $r=1$ is a boundary control, not part of the main
quantifier. It removes two individual obstructions—unequal relation length
and image nondiscreteness—but still has contractible filling, a nonproper
original tree action with infinite stabilizers, and a divergent orbital
ledger.

## 2. Typed closure graph

Terminology is frozen as follows.

- **Structural spine** means only the executable prototype's coarse realized
  lineage: exactly 6 nodes and 5 edges.
- **Expanded proof DAG** means the mathematical obstruction ledger: exactly
  22 nodes and 28 edges, of which 17 are internal transition tags, 5 are
  closure edges, 3 are token-associated contract-exit edges, 1 is an
  auxiliary non-domain firewall, and 2 are mutually exclusive governance
  guards.

The structural-spine IDs are

```text
nodes (6):
N35_OBJECT_FIREWALL
N36_CELLULAR_CANCELLATION
N37_COEFFICIENT_SATURATION
N38_TREE_ORBITAL_TRILEMMA
N39_AFFINE_BRANCH_CLOSED
N_REGISTRY_HANDOFF

edges (5):
E35_36, E36_37, E37_38, E38_CLOSE, E_CLOSE_REGISTRY
```

The expanded-proof-DAG IDs are

```text
nodes (22):
N00;
N35F, N35P, N35S, N35H, N35Q, N35D, N35B;
N36F, N36G;
N37O, N37D, N37N;
N38T, N38M, N38L, N38O, N38K;
NX, NC, NR, NS

edges (28):
E00a, E00b, E01, E02, E03, E04a, E04b,
E05, E06, E07, E08, E09, E10, E11, E12, E13, E14,
E15, E16, E17, E18, E19, E20, E21, E22, E23, E24, E25
```

The total many-to-one projection, with every node/edge ID retained alongside
explicit auditable fibers and the exact 14-class-to-17-transition coverage
relation, is machine-readable in `/tmp/paper39_DAG_BRIDGE.json`. “Retained”
describes the bridge artifact, not an injective or invertible projection. Its
principal node fibers are:

| Projection target | Expanded node fiber |
|---|---|
| `AUX_CONTRACT_ROOT` | `N00` |
| `N35_OBJECT_FIREWALL` | `N35F,N35P,N35S,N35H,N35Q,N35D,N35B` |
| `N36_CELLULAR_CANCELLATION` | `N36F,N36G` |
| `N37_COEFFICIENT_SATURATION` | `N37O,N37D,N37N` |
| `N38_TREE_ORBITAL_TRILEMMA` | `N38T,N38M,N38L,N38O,N38K` |
| `AUX_NONMEMBERSHIP_SINK` | `NX` |
| `N39_AFFINE_BRANCH_CLOSED` | `NC` |
| `N_REGISTRY_HANDOFF` | `NR` |
| `AUX_EMPTY_REGISTRY_FALLBACK` | `NS` |

The cross-spine expanded edges are
$E05\mapsto E35\_36$, $E07\mapsto E36\_37$,
$E10\mapsto E37\_38$, $E15$--$E19\mapsto E38\_CLOSE$, and
$E24\mapsto E\_CLOSE\_REGISTRY$. Internal refinements collapse at their
own coarse node but retain their expanded IDs. `E20,E21,E23` project to the
auxiliary contract-exit branch; `E22` projects separately to the auxiliary
non-domain firewall; inactive `E25` projects to the auxiliary
empty-registry fallback. Hence the 6/5 spine is a quotient view, never a
replacement for the 22/28 proof DAG.

`E22` retains the hashed Paper-37 future-search prohibition against trying an
unenumerated post-result matrix, character, fiber rank, representation,
automaton, or completion. It is not an exact $\mathcal A_{14}$ tag, not a
$\Sigma_{16}$ token, and not a witness in $\Gamma$ or $\chi$. Its explicit
historical path is stored separately under `non_domain_firewall_edges` in the
bridge. Thus it preserves boundary provenance without turning the pure
finite-rank/character/grading classes into mixed classes.

The projection also preserves reset strength. Expanded `E07` maps to coarse
`E36_37`, but only obligations and historical provenance carry. The coarse
edge must reset object, marker, operator owner, and determinant owner under
the Paper-37 source lock. Its unquotiented target and one-edge marker are
separately redeclared P37 fields, not equivalent transports from the P36
filled/control node. The exact constraint is machine-readable at
`projection_transfer_constraints.E36_37` in the bridge.

The structural spine is

```text
P35 object firewall
  -> P36 filling / clock non-descent
     -> P37 coefficient leakage-or-erasure
        -> P38 full-tree empty / non-Fredholm / orbital-generic fork
           -> CLOSE_ENTIRE_AFFINE_BRANCH
              -> RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY
```

The expanded obstruction branches are:

```text
P35 positive source
  |-- positive: strict height -> empty ledger
  |-- formal reverses: universal 2-step backtracks
  |-- Hashimoto: primitive generic relation polygon
  |-- finite quotient: added translation cycles
  `-- Gibbs/Fock: changed space, marker, and determinant

P36 complete relation fill
  |-- K_r contractible -> all recurrence erased
  |-- (r-1)deg(u)=0 -> unit marker does not descend
  |-- prequotient Tr(T^(r+3))>0 -> determinant does not descend
  `-- scalar (1,2,1) superlift -> generic total erasure

P37 finite coefficients
  |-- ordinary invertible: factor deletion would require nilpotence
  |-- direct graded: explicit mixed leakage -4r^4(r-1)
  `-- full normal closure: every closed factor erased, Z_gr=1

P38 tree of the frozen ascending-HNN splitting
  |-- literal full tree: empty primitive ledger
  |-- full-edge B: noncompact, not trace class
  |-- canonical modular weight: still noncompact
  |-- tree-lattice formula: hypotheses/category fail
  |-- orbital substitute: (1-z)/(1-rz) or r=1 divergence
  `-- tree marker: many-to-one collapse of the old clock
```

Every vertex and edge is fully typed in
`/tmp/paper39_DERIVATION_PACKAGE.md`. In particular, each record includes the
inherited obligation, source object, marker, operator/determinant owner,
exact obstruction, matched control, forbidden escape, and terminal code.

## 3. Four proof kernels

### 3.1 Object fork

On the positive affine source,

$$
U(b,k)=(b+r^k,k),\qquad V(b,k)=(b,k+1),
$$

so $b+k$ strictly increases and no positive cycle exists. Formal reverses
create $e\bar e$. Hashimoto reduction deletes immediate reversals but retains

$$
C_{r,x}=vu\bar v\bar u^r,
\qquad |C_{r,x}|=r+3.
$$

The word is primitive because the count of $v$ is one and therefore cannot be
divisible by a proper power exponent. The same relation phenomenon occurs in
matched non-arithmetic presentations.

### 3.2 Filling and clock

The relation cell identifies path lengths $2$ and $r+1$. In any torsion-free
abelian grading target,

$$
\deg v+\deg u=r\deg u+\deg v
\Longrightarrow (r-1)\deg u=0
\Longrightarrow \deg u=0.
$$

Complete filling makes $K_r$ contractible. Yet the prequotient trace-class
operator satisfies

$$
\operatorname{Tr}(T_{r,\theta}^{r+3})
\ge(r+3)\theta^{r(r+1)+4r+10}>0.
$$

Thus recurrence, marker, and determinant cannot all descend through the same
fill.

### 3.3 Finite coefficients

For finite $W$,

$$
\det(I-tW)=1
\iff \operatorname{Tr}(W^m)=0\ \forall m\ge1
\iff W\text{ is nilpotent}.
$$

Invertible parallel transport is not nilpotent. Grading permits direct factor
matching, but the frozen mixed word

$$
M_r=\bar u^rv\bar u^{r-1}vu\bar v^2
$$

has

$$
\operatorname{Tr}W_r(M_r)-\operatorname{Tr}W_{-r}(M_r)
=-4r^4(r-1)\ne0.
$$

At the composite baseline $r=4$, this is $-3072$. Requiring cancellation on
every mixed product covers every closed Cayley label and forces $Z_{\rm gr}=1$.

### 3.4 Tree of the frozen ascending-HNN splitting

A tree has no positive reduced closed path. The full-edge Hashimoto operator
is nevertheless nonzero and satisfies, on an infinite orthonormal family,

$$
\langle B\delta_{e_i},B\delta_{e_j}\rangle=0\quad(i\ne j),
\qquad \|B\delta_{e_i}\|^2=r.
$$

Hence $B$ is noncompact and not trace class. Canonical modular weights are
nonzero constants on the two step orientations and leave a constant-norm
orthogonal subfamily.

The changed positive-height conjugacy object has primitive counts

$$
P_r(1)=r-1,
\qquad
P_r(k)=\frac1k\sum_{d\mid k}\mu(d)r^{k/d}\quad(k>1),
$$

and therefore

$$
Z_{+,r}(z)=\frac{1-z}{1-rz}.
$$

This is the generic necklace law for all matched ascending index-$r$ controls,
not a selective full-tree determinant. At $r=1$, every positive height has
infinitely many conjugacy classes.

## 4. Exhaustiveness proof

Exhaustiveness is syntactic-semantic rather than universal.

1. Freeze the exact top-level alphabet $\mathcal A_{14}$ as data.
2. Use a set-valued relation $\Gamma$ to classify each class as a tested
   obstruction, a pure exit, or a tested canonical representative plus exits
   for alternative instances.
3. Enumerate exactly sixteen stable instance tokens: six obstructed, six
   exit-only, and two tested/exit pairs, with no catch-all token.
4. Refine the tested endpoint families into the seventeen internal edge tags
   $\mathcal T_{17}$ and map each tag to its unique edge head.
5. Treat a nonempty path only as audit provenance; type all candidate data at
   its endpoint and reset ownership across historical successor edges.
6. Prove endpoint-obstruction totality: every nonempty provenance path ends at
   one of the seventeen tested nodes, and every such node has a nonempty
   failed-`Good` coordinate set.
7. Make no claim about coordinatewise combinations or compound repairs.
8. Type `E22` separately as a historical non-domain firewall with empty token
   and class fibers; exclude it from all coverage and failed-`Good` claims.
9. Use the explicit 0--11 topological rank in the bridge; every one of the 28
   expanded edges strictly increases rank.

This proves three distinct finite statements: all fourteen class labels have
dispositions, all sixteen frozen instance tokens have tested-or-exit records,
and every endpoint state in the in-contract provenance domain falsifies at
least one conjunct of `Good`. Root damping and finite-total-weight retrofit
are exits, not targets of the undamped noncompactness theorem. Likewise, the
tree canonical for the frozen splitting and the frozen tree-lattice/groupoid
import do not refute unlisted alternative constructions. No unlisted idea or
compound repair is claimed impossible.

## 5. Sharp counterexamples to overclaiming

1. The directed cycle $C_m$ has a primitive orbit and
   $\det(I-zA)=1-z^m$. Universal symbolic emptiness/non-Fredholm is false.
2. The noninvertible nilpotent
   $N=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}$ has
   $\det(I-tN)=1$. Factor deletion is possible outside invertible transport.
3. Root-dependent summable damping can make a weighted infinite-tree operator
   trace class. Paper 38 excludes it because it is not the canonical modular
   cocycle.
4. Proper discrete finite-stabilizer tree actions may admit tree-lattice
   determinants. The frozen $BS(1,r)$ action does not meet those hypotheses.
5. The traceless invertible
   $J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}$ satisfies
   $\det(I-tJ)=1+t^2$, so first-trace cancellation is insufficient.
6. At $r=1$, marker descent and discrete action image coexist with
   contractible filling, nonproper original action, and orbital divergence.

## 6. Quantifier audit verdict

The exact conclusion is

$$
\forall r\ge2\;\forall c\in\mathfrak C_{\rm aff}(r),\quad
\neg\operatorname{Good}(c).
$$

It is derived by endpoint-obstruction totality: every nonempty provenance path
has one of the seventeen enumerated endpoints, and the explicit map $F$ assigns
that endpoint a nonempty set of failed `Good` coordinates. No graph-termination
claim is used.

The only live semantic ambiguity is that Paper 38 does not define “unspent
successor.” Under its literal historical-existence wording, the Session-4
source lock supplies six witnesses and the realized code is registry handoff.
Those witnesses are already evaluated, so they do not authorize Paper 40.

The proof also depends on the sealed validity of the predecessor theorems,
notably Paper 36's contractibility input. Paper 39 does not independently
re-prove external literature results. The matrix primitive regrouping is safe
near $z=0$ because a nonnegative scalar trace-class kernel dominates the
absolute cycle sum.

The six `Good` coordinates consolidate fields from the pre-existing Route-A
criterion (SHA-256
`29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a`)
and the P35--P38 source/Route locks. The fourteen-class/sixteen-token encoding
is retrospective: predecessor outcomes were known, and the encoding is frozen
only before the Paper-39 checker run.

The full audit is in `/tmp/paper39_QUANTIFIER_AUDIT.md`.

## 7. ARS Phase-1 methodology blueprint

- **Paradigm:** theorem-relative closure, never universal impossibility.
- **Data:** assemble the retrospective Paper-39 encoding from hashed
  predecessor artifacts and freeze it before the Paper-39 checker.
- **Graph:** type object, marker, operator, determinant category, and owner.
- **Coverage:** require a total fourteen-class relation, sixteen exact stable
  instance tokens, a single head for each of seventeen internal tags, and
  endpoint-typed audit-provenance paths; type any auxiliary historical
  firewall separately with empty class/token fibers.
- **Validity:** use matched generic controls and out-of-contract countermodels.
- **Freeze timing:** Paper 39 is a retrospective encoding built after the
  predecessor outcomes were known. Freeze its graph, tokens, route tuple,
  guards, and stop codes before the Paper-39 checker run; do not claim they
  were preregistered before Papers 35--38 failed.
- **Limitation:** closure gives no new mechanism and no successor ranking.

## 8. Paper 40 minimum obligation

Paper 40 may begin only after root/registry governance independently freezes a
new candidate-specific source lock after the Paper-39 seal. The lock must
specify a genuinely non-affine object, phase space, primitive/repetition
semantics, intrinsic marker, operator and function space, determinant category
and ownership theorem, controls, forbidden data, and stop rule. It must prove
that no coordinate is imported from a closed affine node or assembled from
different historical candidates.

Registry handoff alone is not `GO`. No historical candidate is selected or
ranked by Paper 39.

## 9. Package index

- `/tmp/paper39_SOURCE_LOCK.md` — retrospective encoding, source hashes, and
  decisions, frozen before the Paper-39 checker.
- `/tmp/paper39_DERIVATION_PACKAGE.md` — complete typed node and edge ledgers.
- `/tmp/paper39_DAG_BRIDGE.json` — exact 6/5-spine to 22/28-DAG projection.
- `/tmp/paper39_PROOF_PACKAGE.md` — rigorous theorem proof and open risks.
- `/tmp/paper39_QUANTIFIER_AUDIT.md` — quantifier-by-quantifier gap audit.
- `/tmp/paper39_ROUND2_CLUES.md` — successor and adversarial-review clues.
- `/tmp/paper39_route_a_evaluation.yaml` — strict meta-object Route card.
- `/tmp/paper39_PACKAGE_SHA256.txt` — byte-level SHA-256 ledger for this
  frozen `/tmp` bundle.
