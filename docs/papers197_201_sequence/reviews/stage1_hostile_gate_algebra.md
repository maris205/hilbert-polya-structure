# Stage-1 hostile gate: algebra, graph, matching, and word candidates

**Audit date:** 2026-09-05 UTC  
**Role:** process-separated hostile reader; none of the four candidate packages was authored in this process  
**Scope:** `GBE`, `SCT`, `CMM`, and `TCSD`, against the inspected P1--P196 paper and kill ledgers  
**External status:** `OWNER_AMBER / HOLD_EXTERNAL` for every surviving candidate  
**Novelty status:** not assessed; an internal noncollision is not novelty evidence

## Outcome first

| candidate | correctness result | decisive subtraction | Stage-1 verdict |
|---|---|---|---|
| `GBE`, synchronous graph Bellman envelope | The iterate, fixed-locus, sharp-height, and every-time fibre formulas rederive correctly on nonempty finite graphs. | The map is exactly repeated Bellman relaxation to the canonical greatest integer `1`-Lipschitz minorant.  The clock and inverse inclusion--exclusion are two readings of the same tropical minimum formula; fixed counts are generic graph-homomorphism counts. | **`KILL_CANONICAL_BELLMAN_CLOSURE`** |
| `SCT`, self-cardinality prefix toggle | The parity image, labelled one-step fibres, indegree distribution, two-cycle criterion, and even-period obstruction are correct.  P188 alone does not identify this map. | The identical literal update already occurs as killed scout `RC13/CPT`: “toggle the prefix `[|A|]`.”  A stronger analysis does not silently reopen an existing killed system. | **`KILL_LITERAL_REPEAT_RC13_CPT`** |
| `CMM`, odd-cycle monomer matching | The deficiency clock, single `n`-cycle, depth layers, triangular every-target fibre, unique fibre maximum, and image formula survive rederivation, including `n=3`. | P90/GCM share hard-core and alternating-interval language, but neither their literal maps nor their sufficient statistics prove the present package: P90 conserves rank and updates locally; GCM uses simultaneous path retile/defect migration.  CMM strictly raises matching rank and its inverse is a target-prefix interval choice. | **`SELECT_INTERNAL_AMBER`** |
| `TCSD`, ternary cyclic sign derivative | The recurrent core, inverse on the core, parity-sharp clock, de Bruijn depth/cycle formulas, comparison-walk fibres, image language, and Lucas maximum survive the attacks below. | Generic CA, run, transfer-matrix, SFT, Lucas, and Möbius machinery is zero credit.  The residual conjunction—three-valued sign derivative, fourth-root-of-shift core, sharp attraction, and equality-case-resolved inverse extremum—does not transfer from P90, P164, P187, P190, or P196. | **`SELECT_INTERNAL_AMBER`** |

The gate therefore returns

```text
SELECT 2: CMM, TCSD
RESERVE 0
KILL 2: GBE, SCT
EXTERNAL RELEASE: HOLD
```

These are internal portfolio decisions, not paper numbers or ownership
clearance.

## Gate standard

A correct formula is insufficient when the literal map is an existing scout,
a canonical closure, or a renamed standard algorithm.  For selection I
required both:

1. a temporal statistic not mechanically inherited from the nearest occupied
   system; and
2. a target-resolved inverse or counting theorem whose proof does not merely
   replay that same occupied statistic.

Static carrier counts, generic functional-graph terminology, transfer traces,
Möbius inversion, and bounded search non-hits receive no separation credit.

## 1. `GBE`: correct mathematics, fatal canonical closure

Let `G=(V,E)` be a nonempty finite simple graph and
`x in {0,...,h}^V`.  The proposed synchronous update is

```text
T(x)_v=min({x_v} union {x_u+1:u~v}).
```

### Cold rederivation

Min-plus multiplication gives, by induction,

```text
T^t(x)_v=min_{d(v,u)<=t}(x_u+d(v,u)).
```

At stabilization this is the metric lower envelope

```text
g_v=min_u(x_u+d(v,u)),
```

with the minimum restricted to the component of `v`.  Thus `T(x)=x` exactly
when adjacent heights differ by at most one.  For each `v`, stabilization
occurs as soon as the radius-`t` ball contains a minimizer of
`x_u+d(v,u)`; maximizing this least radius over `v` gives the point tail.
The global extremum is

```text
min(largest component diameter, max(0,h-1)).
```

The `h-1` rather than `h` boundary is correct: a putative minimizing source
at distance `h` ties the unchanged height-`h` value at the target, so it is
not needed to change or certify that coordinate.

For a target `y`, the lower bounds

```text
ell_u=max(0,max_{d(v,u)<=t}(y_v-d(v,u)))
```

are exactly the conditions that every candidate value in each minimum is at
least `y_v`.  Inclusion--exclusion over the events that the minimum at `v`
is strictly greater than `y_v` yields the displayed all-time fibre formula.
No sign or endpoint error was found, including `t=0`, isolated vertices, and
times beyond the component diameter.

### Why this is nevertheless killed

The terminal state is a canonical normal form: the greatest integer
`1`-Lipschitz function below `x`.  Bellman relaxation and the shortest-path
formula supply the entire forward theorem.  The inverse theorem then applies
ordinary inclusion--exclusion to the active minimizers of the same tropical
operator.  The purported third axis, counting fixed states, is the generic
homomorphism count into a reflexive path and is only explicitly tractable on
special graph families.

Consequently there is no nontransferable residual after the batch's
canonical-closure and standard-algorithm subtraction.  The fact that no
literal numbered-paper duplicate was located does not rescue a definition-
level Bellman owner.

### Frozen claim ceiling

`GBE` may remain in a negative ledger as a compact finite Bellman-envelope
example.  It must not be called a survivor, and the metric envelope, sharp
diameter/height bound, graph-homomorphism fixed locus, or generic tropical
fibre inclusion--exclusion must not be presented as separate contribution
axes.  If the empty graph is ever included, it also needs an explicit
diameter and empty-product convention; the reviewed verifier starts at
`|V|=1`.

## 2. `SCT`: separated from P188, but an exact killed-scout repeat

The proposed map is

```text
F_n(A)=A symmetric-difference [|A|],    A subseteq [n].
```

### Mathematical audit

For a target `B` and a proposed source size `k`, the source is forced to be
`A=B triangle [k]`.  The equality `|A|=k` is equivalent to

```text
|B intersect [k]|=|B|/2.
```

This proves the even-cardinality image and, for
`B={b_1<...<b_(2r)}` nonempty, the exact fibre
`b_(r+1)-b_r`; the empty target has the `n+1` prefix predecessors.  Fixing
the two middle positions also gives the stated indegree distribution, with
the unprinted summation range

```text
r <= i <= n-g-r+1.
```

For a two-cycle, comparing the two toggled prefixes forces both source sizes
to agree.  Hence `k` is even and exactly half of `[k]` is occupied, giving
the stated binomial census.  Coordinate `1` toggles at every nonzero state,
so every nontrivial period is even.  The `4`, `8`, and `16` examples are
valid existence witnesses only.

This is genuinely different from P188.  P188 uses
`A -> A intersect [|A|]`, is monotone and fixed-only, and is controlled by a
decreasing rank recursion.  `SCT` has parity image and long even cycles; the
P188 theorem package neither conjugates to nor proves it.

### Binding collision

The P187--P191 root-coordinator denominator already froze

```text
RC13 CPT | subsets A subseteq [n] | toggle the prefix [|A|]
```

in `scouting/root_coordinator/CANDIDATES.md`, and its kill ledger records

```text
RC13 CPT | KILL | rich finite cycles but no stable uniform theorem route
```

This is literal equality, not a shared carrier or proof-engine analogy.  The
new inverse and two-cycle formulas improve the diagnosis but do not create a
new system.  The current batch expressly excludes existing systems, so P188
separation cannot override the older exact hit.

### Frozen claim ceiling

The candidate must be labelled an enriched analysis of killed `RC13/CPT`, not
a fresh survivor.  No complete recurrence or period classification has been
proved: only evenness and three explicit periods are established.  Re-entry
would require an explicit central override of the literal-repeat rule plus a
new full-parameter recurrent theorem; neither is supplied here.

## 3. `CMM`: survives P90/GCM only under a narrow subtraction

For `n=2m+1`, let the carrier be matchings of the labelled cycle `C_n`, with
`e_i={i,i+1 mod n}`.  If at least three monomers remain, choose the least
labelled monomer `a`, then the next monomer `b` clockwise, and flip every edge
on the clockwise `a`--`b` arc.  With one monomer `a`, flip `e_a` and
`e_(a+1)`, moving it by `+2`.

### Cold rederivation and boundary attacks

Between consecutive monomers the matching is forced to alternate.  Flipping
the selected arc removes exactly its two endpoint monomers and adds one
matching edge.  Hence

```text
tau(M)=m-|M|,
```

and the empty matching is the unique state at maximum tail `m`.  On maximum
matchings the unique monomer moves by `+2`; since `gcd(2,2m+1)=1`, all `n`
maximum matchings form one `n`-cycle.

For a target `Y`, let `u` be its least monomer and `r=floor(u/2)`.  All
vertices below `u` are forced into exactly `r` consecutive dimers: from
`e_0` when `u` is even, or after the wrap dimer when `u` is odd.  A transient
predecessor is obtained uniquely by reversing one nonempty contiguous
interval of these dimers.  Therefore

```text
|F^(-1)(Y)|=r(r+1)/2 + 1_{|Y|=m}.
```

The indicator is the disjoint rotor predecessor.  This proof includes:

- `u=0,1`, where there is no transient predecessor;
- targets outside the image;
- maximum targets, which can have both transient and rotor predecessors;
- `n=3`, where `F_(n-3)=F_0=0`, the image has size three, and the maximum
  fibre is two.

Counting all image targets with `u>=2` by whether `e_0` is present or both
the wrap edge and `e_1` are present, then adding the two maximum targets with
monomer `0` or `1`, gives

```text
|Im(F)|=F_(n-1)+F_(n-3)+2=L_(n-2)+2.
```

An additional no-import inline reimplementation checked closure, every
target fibre, every point clock, and the single core cycle for odd
`3<=n<=17` in 23,116 assertions.  It reproduced

```text
n       3  5  7  9  11 13 15 17
maxfib  2  4  7 11  16 22 29 37.
```

### P90 and `GCM` subtraction

The matching word is hard-core and the maximum shell is alternating; those
facts are occupied and earn no credit.  They do not, however, transfer the
literal dynamics or its two retained proof axes.

- P90 Rule 184 is a translation-equivariant radius-one update preserving
  particle number.  CMM uses a global least-label scheduler and strictly
  raises matching rank off the core.
- Killed `GCM` simultaneously complements every uncovered interval of a path
  matching.  Its clock is migration of a leftmost bad edge and its arbitrary
  inverse is a regular-expression parser.  CMM flips one state-selected arc;
  its clock is deficiency and its target inverse is the finite set of
  intervals inside one forced labelled prefix.
- Recurrent data already prohibit a conjugacy: `GCM` has
  `2^floor(n/2)` recurrent path states arranged in two-cycles, while CMM has
  `n` recurrent states in one `n`-cycle.  More importantly, the GCM/P90
  defect-migration statistic does not prove either CMM's strict-rank temporal
  law or the target parameter `floor(u/2)`.

Thus the serious adjacency is real, but it is not the same dominant proof
engine.  The candidate survives the internal gate.

### Mandatory claim weakening

The selectable residual is only

```text
least-monomer/next-clockwise scheduler
 + odd-cycle rotor splice
 + every-target triangular interval atlas.
```

Assign zero standalone credit to Berge augmentation, the deficiency clock,
matching layer counts, Fibonacci/Lucas identities, hard-core encodings, and
rotation of maximum matchings.  Do not say that CMM introduces a new
augmenting-path method or a new traffic model.  Its current owner state must
remain amber: selection authorizes internal proof construction only, and a
source owning the literal scheduler or the displayed conjunction kills it.

## 4. `TCSD`: strongest survivor, with generic machinery removed

On `X_n={-1,0,1}^{Z/nZ}`, synchronously set

```text
D(x)_i=sgn(x_(i+1)-x_i),
```

and let `rho` be left rotation.  The tensor convention and sign orientation
in the reviewed contract and verifier agree.

### Core and temporal proof

Put

```text
K_n={x:D^4x=rho^2x}.
```

The relation is forward invariant because `D` commutes with `rho`, and on
`K_n`

```text
D^(-1)=rho^(-2)D^3.
```

Therefore `D` is bijective on `K_n`.  The local run argument proves global
attraction.  A zero-run in `D(x)` is one shorter than an equal-letter run of
`x`, while three consecutive `+` or three consecutive `-` outputs would
require a strict chain of four letters in a three-letter alphabet.  Hence,
for nonconstant `x`,

```text
R(Dx)<=max(R(x)-1,2).
```

The frozen local certificate now covers both cases actually used by the
all-size proof:

- 96 length-six words with no equal adjacent pair satisfy
  `delta^5(w)_0=delta(w_2w_3)_0`, so `R(x)=1` implies `D(x) in K_n`;
- 1,344 length-seven words with no constant triple satisfy
  `delta^6(w)_0=delta^2(w_2w_3w_4)_0`, so `R(x)<=2` implies
  `D^2(x) in K_n`.

Unfolded cyclic windows may repeat coordinates when `n<7`, but they are still
members of these exhaustively certified local classes.  Thus the proof does
not silently assume `n>=7`.

The one-exception trajectory

```text
a^(n-1)b -> 0^(n-2) s (-s) -> ...
```

ends at the full alternating core after `n-1` steps for even `n`, but at
`0 Alt_(n-1)(s) in K_n` after `n-2` steps for odd `n`.  Earlier states in
that displayed trajectory are outside `K_n`.  Together with the run bound,
this gives exactly

```text
H_1=1;
H_n=n-1 for even n;
H_n=n-2 for odd n>=3.
```

The small boundaries agree: at `n=1` all three letters map to zero; at `n=2`
the maximum tail is one; at `n=3` it is one.

### Depth, cycle, and inverse axes

The condition `tau(x)<=t` is the local equality

```text
D^(t+4)x=rho^2 D^t x.
```

The contract's de Bruijn matrix `A_t` therefore counts that set by
`tr(A_t^n)`, including `n<t+4` because closed de Bruijn walks correctly
encode repeated cyclic coordinates.  At `t=0`, an independent exact symbolic
check gives

```text
charpoly(A_0)
 = z^74 (z-1)(z^3-z^2-2z-1)(z^3+z^2+2z+1),
```

with 165 allowed edges.  This yields the stated order-seven recurrence for
`|K_n|`.  The `C_p` matrices similarly encode `D^p(x)=x`, and ordinary
Möbius inversion then gives exact-period and cycle counts.

For a labelled target `y`, the product of strict-lower, identity, and
strict-upper `3 x 3` matrices counts exactly the closed source words having
the prescribed comparisons.  Contracting equality edges shows that a target
is in the image iff it is all zero, or its strict-sign skeleton contains both
signs and no cyclic sign-run of length three.

For a strict skeleton of length `r`, direct matrix products give maximum
`L_r` for even `r`, uniquely at the two alternating sign phases, and
`F_(r-1)` for odd `r`; for odd `r>=3` equality means one doubled sign-run.
At `r=1` both one-sign products have trace zero and lie outside the image.
Comparing over the number of equality edges proves

```text
max_y |D^(-1)(y)|=L_(2 floor(n/2)).
```

For even `n>=4`, only the two alternating targets maximize.  For odd
`n>=5`, exactly one equality edge is present, giving `2n` maximizers.  The
exceptional ties are correct: at `n=2`, `00` joins the two alternating
targets; at `n=3`, `000` joins the six one-zero alternating targets.  A
separate strict-sign product attack through `r=16` reproduced the claimed
maxima and all equality-case counts.

### Internal collision decision

- There is an exact first-front projection to P164 at alphabet size three:
  `1{D(x)_i=0}=1{x_i=x_(i+1)}`.  This receives zero credit.  It is not a
  semiconjugacy of the iterated maps: replacing `+` and `-` by the same
  “unequal” bit loses whether adjacent nonzero comparison signs agree.  P164
  then follows a binary affine Rule-102 tail and has one recurrent point on
  its dyadic main family, whereas TCSD preserves both orientations, remains
  ternary and nonlinear, and has an extensive fourth-root-of-shift core.
- P196 reaches a shift core after one step.  Its implication inequalities and
  gap-product fibres do not give TCSD's long parity-sharp attraction or its
  comparison-walk fibre extremum.
- P90, P117, P187, and P190 occupy CA/run/difference/trace vocabulary, but
  their conserved traffic, run reversal, frozen positive peaks, and Brandt
  support erosion do not supply the TCSD local identities or core.

No inspected literal map, conjugacy, or sufficient-statistic factor reproduces
the retained conjunction.  `TCSD` therefore passes the internal gate.

### Mandatory claim weakening

The following are tools or corollaries, not standalone contributions:

- generic cellular-automaton and SFT language;
- de Bruijn traces and transfer-matrix products;
- Lucas/Fibonacci identities and Möbius inversion;
- the finite period sets observed for `n<=12`;
- the statement that periods divide `4n/gcd(n,2)`.

Do not claim that all divisors of the period bound occur, or that the listed
small period sets form a classified pattern.  The added fibre certificate
correctly exposes the rank-one `U^2/L^2` reduction, Fibonacci merge
inequality, equality cases, and the `r=1` zero-trace exception.  A frozen
paper should still print the coefficient indexing behind that reduction and
an exact characteristic-polynomial certificate rather than treating checked
recurrence instances as an all-`n` proof.  The local 96/1,344-window tables
are legitimate finite lemmas, not novelty evidence.

## Exact replay record

All four author-side programs were run afresh without modifying their source.
Finite replay is counterexample pressure only.

| candidate | reviewed exact scope | assertions | raw stdout SHA-256 | result |
|---|---|---:|---|---|
| `GBE` | all labelled simple graphs `|V|<=4`, `0<=h<=3`, all states and times through stabilization | 232,448 | `ee8420f918a84b212d14f969ea1a7bea211b4cdecff8b70807baf3ad15f2acf0` | PASS |
| `SCT` | all subsets through `n=18`; explicit period witnesses through `n=30` | 1,650,635 | `89fab9d538aa6bed1b48d89b22466bff8972f85b36ec0d070a6cf20da0fc9241` | PASS |
| `CMM` | all cycle matchings for odd `3<=n<=21`, plus lane controls | 2,508,857 | `5b4981797bb2dd1ca83a8bc0432c20af8352c2eee89870011895924448c33596` | PASS; byte-equal to lane `CANONICAL.txt` |
| `TCSD` | all `3^n` states through `n=12`, local certificates, fibres, core, tails, and lane controls | 3,238,990 | `2b47662aaeab35569a9720896846537c58e040a4b82b9197c4a8b698e7479132` | PASS; two fresh processes byte-identical |

The current principal input hashes are:

```text
b4e093c44b41a7a8a09c00d202c2bc9d45bc3f05f177d54958e65546552cedd4  scouting/root_graph_bellman/THEOREM_SPIKE.md
b11cb1f13d84ac3bf9892449ebb3e238382643dab4e160781f6521aca074fd83  scouting/root_graph_bellman/verify_scout.py
736fe6a1df12bee26f47d846a47e78319f7b41fdcfd37ad15415c21ca8ec0ff0  scouting/root_self_cardinality_toggle/THEOREM_SPIKE.md
71d4d7072961fc0b1675f332d766514b76baac1c231cbbc41580ece64ff0a594  scouting/root_self_cardinality_toggle/verify_scout.py
afaa5df4e2772c8fe1cb8dd119dcc7e7663c752bccd538183e660afc01966171  scouting/graph_matching_lane/CMM_THEOREM_CONTRACT.md
8f3d04b91e627f8f6e88e5bf899db76a3e85bfad44d137fcd589bb18d1218bc4  scouting/graph_matching_lane/COLLISION_FIREWALL.md
2718ee085a93dc6e5753b42090c4d4f403c3db51bca3f4c8f0b1f2c69a92a964  scouting/graph_matching_lane/verify_graph_matching_lane.py
f9e9343986a4602d8cd607ae1265a7457f2a5b8538dc6cbd5adf5919f39d34e0  scouting/word_poset_lane/TCSD_THEOREM_CONTRACT.md
f63c0cc9a5f69321f6f63666aef7374d61125ee8df9ec8bb833fe048c948395e  scouting/word_poset_lane/TCSD_LOCAL_CERTIFICATE.md
f74d17e5d7b767bf971de99a8d3f740333a77956a770a8b1eadc4fba36b71dc8  scouting/word_poset_lane/TCSD_FIBRE_CERTIFICATE.md
6d277b780ca925118d0a648148d106116e3145e1c3c2913bde8618aaf0407e42  scouting/word_poset_lane/COLLISION_FIREWALL.md
db0751ce25aff410db4cf5c1021df6dc65a51b1f44e05da85533bafeb2205522  scouting/word_poset_lane/verify_word_poset_lane.py
da265471b6c3567703f588157e5a2e871d8dd53b8f7a6789133e71351265cd1f  scouting/word_poset_lane/CANONICAL.txt
f63d594dea94d3b47bba208c4a9f138a2111d105b53e5dcd7c062f452ac9a5fe  scouting/word_poset_lane/REPLAY_LOG.md
```

Paths in this block are relative to `docs/papers197_201_sequence/`.

## Final gate statement

`CMM` and `TCSD` are internally selectable only under their narrow residual
contracts and remain `OWNER_AMBER / HOLD_EXTERNAL`.  `GBE` is a correct but
canonical Bellman closure, and `SCT` is the exact killed `RC13/CPT` map; neither
is a reserve.  No statement in this audit asserts novelty, priority, freedom
to operate, or authorization for external circulation.
