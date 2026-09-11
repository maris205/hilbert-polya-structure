# Replacement breadth scout — adaptive finite maps

**Date:** 2026-09-02 UTC  
**Scope:** state-dependent actions, endofunctions/partial functions, adaptive
automata, and nonlinear maps with a frozen invariant  
**Portfolio boundary:** P1–P161 plus all earlier P162–P166 scout lanes  
**External state:** `HOLD_EXTERNAL`  
**Literal systems exact-tested:** 26  
**Survivors:** one amber candidate (`AQN`), no paper allocation

## Outcome first

Twenty-six genuinely different finite maps were implemented.  The pool was
not padded with parameter changes: it contains word quotients, raw word
actions, subset and partition actions, graph relabellings, permutation and
endofunction conjugations, partial functions, coordinate involutions, matrix
actions, endofunction summaries, transformation-semigroup schedulers,
synchronizing-subset policies, nonlinear feedback registers, and a
state-switched cellular map.

Only `AQN`, adaptive quotient-normalized rotation, survives as
`SELECT_AMBER_SPECIALIST_OWNER_GATE`.  It has all three requested axes:

1. an exact iterate, depth-one-to-cycle theorem, pointwise period, all-period
   fixed counts and Möbius cycle census;
2. an all-time every-target image test and target-dependent zero-weight fibre
   polynomial; and
3. exact recovery of `(q,n,c)` from the labelled atlas when `q` is odd and
   `n>=3`.

The recurrent action is an ordinary cyclic rotation only **after** passing to
cyclic differences and conditioning on the nonlinear invariant.  All
ordinary necklace, single-parity-check-code, Burnside/Möbius, and
data-dependent-rotation facts are therefore zero credit.  The proposed
residual is the integrated noninvertible map and its complete decorated-cycle
atlas.  Because that residual is elementary and may be judged an engineered
semidirect quotient, the status is amber, not green and not a novelty claim.

The other 25 systems are killed.  Fifteen are invertible state-dependent
actions with singleton fibres; four endofunction summaries have irregular
small signatures and no all-parameter spine; the six automaton/feedback maps
are directly owner-heavy or unstable.  None is a hidden reserve.

## Historical and current-batch firewall

The scout excludes coordinate truncation, digit/valuation erasure, graph or
tree pruning/core peeling, selectors followed by standardization, generic
fixed linear maps/powers, generic closure, and generic random group walks.
It does not re-enter any P134/P139/P147/P149/P155/P156 word or permutation
engine.  The following current-batch mechanisms were also removed before
ranking:

- `RFW` reciprocal Fibonacci windows and `CNG` cyclic GCD erosion;
- `USP` recursive Schur complementation and all arithmetic digit systems;
- `BQC` block quotient/coalescence and its set/hypergraph lifts;
- the killed word-coordinate truncation maps `LCD/DAE`; and
- all stochastic rank/Fourier/record/product transfers.

## Twenty-six-system exact decision ledger

| ID | literal update | exact small signal | all-parameter spine attempted | owner/internal gate | decision |
|---|---|---|---|---|---|
| `AQN` | for `w in F_q^n`, let `k` be the number of nonzero cyclic differences and set `T_c(w)=R^(ck)w-w_0 1` | `(q,n,c)=(3,6,1)`: 729 states, 243 recurrent image states; point periods `1^23,2^40,3^120,6^60`; change census `0^1,2^30,3^40,4^90,5^60,6^22` | exact iterate; depth at most one; uniform decorated cycles; every-time target fibres and zero-weight polynomial; fixed/cycle formula; marked recovery of `c` | standard necklaces/SPC enumerators/data-dependent rotations subtracted; no exact map hit; nearest P98/P99/P96 actions do not supply the noninvertible target atlas | **`SELECT_AMBER_SPECIALIST_OWNER_GATE`** |
| `HWR` | binary word rotates by its Hamming weight | `n=9`: cycles `1^8,3^54,9^38` | weight freezes the rotation; point period is word rotation period divided by its gcd with the weight | Hamming-weight-controlled rotations appear directly in quantum circuits and cryptographic data-dependent rotations; singleton fibres | `KILL_DIRECT_ACTION_OWNER_THIN` |
| `DCR` | `q`-ary word rotates by its number of unequal cyclic adjacencies | `q=3,n=6`: cycles `1^69,2^60,3^120,6^30` | change count is invariant and freezes one rotation | exactly the recurrent action inside `AQN`, without the quotient/fibre axis | `KILL_AQN_ACTION_ONLY` |
| `DAR` | rotate by cyclic-change count when even; reflect-then-rotate when odd | `q=3,n=6`: cycles `1^69,2^150,3^120` | invariant splits rotation strata and reflection involutions | dihedral necklace action only; singleton fibres | `KILL_DIHEDRAL_ACTION_ONLY` |
| `CCR` | rotate a word by its number of distinct colours | `q=3,n=6`: cycles `1^15,2^267,3^60` | colour count freezes the rotation | fixed-content necklace/Burnside calculation; singleton fibres | `KILL_NECKLACE_ACTION_ONLY` |
| `SVT` | translate `S subset Z_n` by `|S|` | `n=9`: cycles `1^8,3^54,9^38` | cardinality freezes a cyclic action | identical action spectrum to Hamming-weight rotation and adjacent to P96 circle subsets | `KILL_P96_ACTION_TRANSFER` |
| `BRT` | cyclically relabel a set partition by its block count | `n=6`: 203 states; cycles `1^15,2^40,3^32,6^2` | block count freezes label rotation | Burnside on partitions; P135 partition interfaces; singleton fibres | `KILL_PARTITION_ACTION_ONLY` |
| `EGR` | cyclically relabel a graph by its edge count modulo `n` | `n=6`: 32,768 states; cycles `1^5546,2^2688,3^3698,6^1792` | edge count freezes vertex rotation | graph relabelling/Burnside only; no inverse axis | `KILL_GRAPH_ACTION_ONLY` |
| `PFC` | conjugate a permutation by the label cycle raised to its fixed-point count | `S_7`: 1,855 fixed states and 455 seven-cycles | conjugation preserves fixed-point count | finite group conjugation action; P154 normalizer/centralizer neighbourhood; singleton fibres | `KILL_GROUP_ACTION_ONLY` |
| `EIC` | conjugate an endofunction by a label rotation raised to its image size | `n=5`: 120 fixed states and 601 five-cycles | image rank is conjugacy invariant | functional-digraph relabelling only; singleton fibres | `KILL_ENDOFUNCTION_ACTION_ONLY` |
| `PDR` | rotate a partial binary word by its number of undefined coordinates | `n=7`: 2,187 states; cycles `1^129,7^294` | defect freezes domain rotation | partial-word necklace action; no target fibres | `KILL_PARTIAL_ACTION_ONLY` |
| `PCR` | conjugate a partial permutation by the label cycle raised to its defect | `n=5`: 1,546 states; cycles `1^121,5^285` | defect freezes inverse-semigroup conjugation | symmetric inverse-semigroup action; singleton fibres | `KILL_PARTIAL_PERMUTATION_ACTION_ONLY` |
| `ISR` | invert every nonzero `F_5` letter, then rotate by support size | `q=5,n=5`: cycles `1^33,2^496,5^42,10^189` | support freezes commuting inversion and rotation actions | coordinate involution plus necklace action; singleton fibres | `KILL_PRODUCT_ACTION_ONLY` |
| `WCR` | complement a binary word, then rotate by its old weight | `n=9`: 256 two-cycles | exact identity `T^2=id` | thin involution; complement/rotation group action | `KILL_INVOLUTION_ONLY` |
| `MRR` | rotate rows by binary matrix rank and columns by rank plus one | `3x3`: two fixed matrices and 170 three-cycles | rank freezes a row-column permutation | generic rank statistic plus coordinate permutation; singleton fibres | `KILL_RANK_ACTION_ONLY` |
| `CLT` | translate every colour by the number of colours used | `q=4,n=6`: cycles `1^1560,2^186,4^541` | colour count freezes alphabet translation | colour relabelling action only | `KILL_ALPHABET_ACTION_ONLY` |
| `IDH` | endofunction maps to its indegree histogram modulo `n` | `n=5`: image 122, two fixed points, maximum tail 4; fibre sizes `5..120` | no stable formula across `n`; inventory-like iteration | inventory/counting-sequence literature directly adjacent; irregular signatures | `KILL_INVENTORY_OWNER_NO_SPINE` |
| `PIS` | target `i` receives the sum modulo `n` of labels in `f^{-1}(i)` | `n=5`: image 281; 43 fixed points, 83 two-cycles; maximum tail 3 | no monotone invariant or parameter-uniform period law | nonlinear incidence summary, but only raw finite spectrum | `KILL_NO_SPINE` |
| `OCL` | replace each value by the eventual cycle length of that starting vertex, modulo `n` | `n=5`: image 60; one fixed point; maximum tail 3; maximum fibre 1296 | first step is a functional-graph statistic; later iteration is representation-dependent | a canonical summary/retraction with no independent target theorem | `KILL_FUNCTIONAL_GRAPH_SUMMARY_THIN` |
| `BAS` | replace each vertex by the size modulo `n` of its weak functional-graph component | `n=5`: image 42; five fixed points; maximum tail 3; maximum fibre 1569 | no all-`n` temporal law survived | component-size summary; P135 component/partition interface | `KILL_COMPONENT_SUMMARY_NO_SPINE` |
| `RAC` | left-compose an endofunction by a rotation when its rank is odd and by a one-point reset when rank is even | `n=5`: image 2045, maximum tail 1; cycles `1^420,5^325`; fibres `1,2,3,7,31` | rank can drop once, then a permutation action freezes | transformation-semigroup/rank decomposition; one-step transient and no clean every-target formula | `KILL_SEMIGROUP_ACTION_THIN` |
| `CNY` | on a nonempty subset of a Černý automaton, apply reset if it lowers rank, otherwise rotate | `n=9`: image 447; maximum tail 13; cycles `3^1,9^8` | attractive long tail, but no uniform synchronization: 75 recurrent states | Černý/reset-word and greedy synchronization literature directly controls the mechanism | `KILL_DIRECT_AUTOMATA_OWNER` |
| `PAS` | on a nonempty automaton subset, choose rotation at odd rank and one-point reset at even rank | `n=9`: image 383, tail at most one; cycles `1^128,3^1,9^28` | parity freezes or drops rank once | artificial scheduler over standard transformation generators; thin | `KILL_ADAPTIVE_SCHEDULER_THIN` |
| `MFS` | shift a binary register and append its global majority bit | `n=10`: image 638, only two fixed points, sharp observed tail 10 | small data suggest convergence to constant states, but proof is a global-majority shift theorem and collides with occupied majority systems | global majority and feedback-register owners; P132 proximity | `KILL_MAJORITY_INTERNAL_OWNER` |
| `NFS` | shift a binary register and append NAND of the two endpoint bits | `n=10`: image 768; two 11-cycles; maximum tail 19 | nontrivial but parameter pattern not proved; fibres only one or two | literal nonlinear feedback shift register, a mature cycle-structure subject | `KILL_NLFSR_OWNER_NO_SPINE` |
| `ACA` | on a binary cycle, use neighbour-OR when global weight is odd and neighbour-AND when it is even | `n=9`: image 206, 2 fixed points, 39 two-cycles, maximum tail 3; fibre values up to 37 | parity is not invariant and the signature changes irregularly with `n` | state-switched cellular automaton; P82/P90 and generic CA literature | `KILL_CA_INTERNAL_UNSTABLE` |

## Frozen theorem contract for `AQN`

### Literal carrier and update

Let `q` be a prime, `n>=1`, `c in Z/nZ`, and
`X_(q,n)=F_q^n`.  Write `R` for left cyclic rotation.  Define the cyclic
difference word and its support size by

```text
Delta(w)_i = w_(i+1)-w_i,
k(w)       = |{i:Delta(w)_i != 0}|.
```

The proposed map is

```text
T_c(w) = R^(c k(w)) w - w_0 1.
```

This is nonlinear because the rotation exponent depends on the state and is
noninvertible because all global alphabet translates have the same image.

### Contract A — iterate, recurrent image and point periods

Put `s=c k(w)` in `Z/nZ`.  Cyclic differences remove the additive
normalization, so

```text
Delta(T_c(w))=R^s Delta(w),
k(T_c(w))=k(w).
```

For every `t>=1`,

```text
T_c^t(w)=R^(ts)w-w_((t-1)s) 1.                 (A1)
```

The recurrent set equals the one-step image

```text
Y_(q,n,c)={y:y_(-c k(y))=0},
|Y_(q,n,c)|=q^(n-1).                           (A2)
```

Every state outside `Y` has depth exactly one; every state in `Y` is
recurrent.  If `p(Delta y)` is the least positive rotational period of the
difference word, then

```text
per_T(y)=p(Delta y)/gcd(p(Delta y),c k(y)).     (A3)
```

Thus the complete functional graph consists of permutation cycles, each of
whose vertices has exactly `q-1` additional depth-one leaves.

### Contract B — all-time target fibres and a target-dependent weight atlas

For every `t>=1`, a target has a source precisely when it satisfies (A2).
For a supported target `y`, all sources are

```text
w^(a)_i = y_(i-t c k(y)) + a,     a in F_q.    (B1)
```

Hence every supported target has exactly `q` time-`t` sources.  This uniform
number does not exhaust the inverse information.  If
`N_a(y)=|{i:y_i=a}|`, the source zero-count polynomial is

```text
sum_(T_c^t(w)=y) z^(N_0(w))
   = sum_(a in F_q) z^(N_a(y)).                 (B2)
```

It is target-dependent, valid at every positive time, and determines the
unordered composition of every target word.  At `t=0`, the fibre is the
singleton target and (B1)–(B2) are not applied.

### Contract C — change strata, fixed counts and all cycles

The difference map identifies additive-translation classes of words with
the single-parity-check code

```text
D_(q,n)={d in F_q^n:sum_i d_i=0}.
```

The exact number of recurrent states in change stratum `k` is

```text
A_(q,n)(k)=binom(n,k)
 ((q-1)^k+(q-1)(-1)^k)/q.                     (C1)
```

For `ell>=1`, put

```text
g_k=gcd(n,ell c k),   r_k=n/g_k.
```

Terms with `r_k` not dividing `k` are zero.  If `s_k=k/r_k`, define

```text
B_k(ell)=binom(g_k,s_k)(q-1)^s_k,
             if q divides r_k,
          =binom(g_k,s_k)
             ((q-1)^s_k+(q-1)(-1)^s_k)/q,
             otherwise.
```

Then

```text
Fix(T_c^ell | Y)=sum_(k=0)^n B_k(ell).         (C2)
```

Möbius inversion gives the number of cycles of exact length `m`:

```text
C_m=(1/m) sum_(d|m) mu(m/d) Fix(T_c^d | Y).   (C3)
```

This is not inferred from enumeration; it follows by decomposing the
position permutation `R^(ell c k)` into `g_k` cycles and imposing the
zero-sum condition on their repeated values.

### Contract D — parameter recovery and decisive boundaries

The positive indegree in the functional graph is `q`; the recurrent-set size
then gives

```text
n=1+log_q |Y|.
```

For odd `q` and `n>=3`, the labelled image atlas also recovers `c`.  Use a
target with exactly two changes and a unique zero, and another with exactly
three changes and a unique zero.  If their admitted zero positions are
`z_2,z_3`, (A2) gives

```text
z_2=-2c,  z_3=-3c,  hence c=z_2-z_3 mod n.    (D1)
```

The verifier constructs such targets for every `c`, all tested odd primes,
and every `n>=3` in its range.

Mandatory edges are explicit:

- `n=1`: every one-letter word maps to zero, which is the unique recurrent
  state with fibre `q`;
- `c=0`: the map is the one-step normalization `w -> w-w_0 1`, so all of
  `Y={y:y_0=0}` is fixed;
- `k=0`: only constant words occur, and all map to zero;
- `q=2`: Contracts A–C remain valid, while the two/three-change recovery in
  D is deliberately not claimed.

### Collision ceiling

Ordinary cyclic rotations, necklaces, Burnside/Möbius inversion, the
single-parity-check weight enumerator, Hamming-weight/data-dependent
rotations, and generic finite functional-graph terminology are all
zero-credit inputs.  The candidate may claim only their conjunction for the
literal nonlinear map, including the target hyperplane selected by the
state's own change count, the uniform decorated-cycle graph, the weighted
all-time inverse atlas, and marked parameter recovery.

Closest internal comparisons:

- P98 is a fixed equal-block-sum finite-field operator with repeated-root
  linear algebra; `AQN` is not a fixed linear map and its noninvertible part
  is an additive-orbit quotient.
- P99 is a bijective unipotent action on sublattices; it has no transient
  leaves or target-fibre hyperplanes.
- P96 acts on finite subsets of a circle by expansion; it neither uses word
  differences nor adaptive rotation strata.
- P139 selects Lyndon factor starts; `AQN` selects no coordinates or
  subwords and performs no standardization.
- Current `RFW`, `CNG`, `USP`, and `BQC` use respectively singular rational,
  lattice erosion, Schur complement, and quotient/coalescence engines.

This separation is plausible but not final.  A specialist may still judge
the package a routine disjoint union of necklace actions after quotienting;
that is the exact reason for the amber gate.

## Executable evidence

Run:

```text
python3 docs/papers162_166_sequence/scouting/replacement_adaptive_maps/verify_scout.py
```

The self-contained verifier imports no earlier implementation.  It checks all
states for 21 `(q,n)` AQN carriers and four distinct `c` boundaries per
carrier (with degeneracies deduplicated), including every target, all tested
positive times, weighted fibres, invariant strata, fixed counts, point
periods, and recovery witnesses.  It then computes complete functional graphs
for the other 25 literal systems.

The frozen run contains **393,864 assertions** and ends in `STATUS PASS`.
Exact enumeration is falsification pressure, not proof and not evidence of
owner absence.

## Final gate

```text
AQN  SELECT_AMBER_SPECIALIST_OWNER_GATE
all other systems  KILL
HOLD_EXTERNAL
```

No paper should be drafted from `AQN` until an independent hostile proof
review and a specialist combinatorics-on-words/coding owner search accept the
residual theorem conjunction.
