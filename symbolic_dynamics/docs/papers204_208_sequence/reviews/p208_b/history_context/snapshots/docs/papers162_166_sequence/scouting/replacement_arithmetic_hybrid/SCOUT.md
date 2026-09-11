# Arithmetic--combinatorial hybrid replacement scout — P162--P166

**Freeze date:** 2026-09-03 UTC  
**Portfolio boundary:** P1--P161 plus visible P162--P166 scout/kill ledgers  
**External state:** **HOLD_EXTERNAL**  
**Decision:** **EMPTY_POOL**; 24 literal systems tested, 24 killed, no paper
allocation

## 1. Outcome and evidence rule

This lane tests 24 genuinely different finite deterministic updates in four
carrier families:

1. ordered factorizations, arithmetically labelled set partitions, and
   factor-bracketing trees (`AH01`--`AH06`);
2. nonlinear or state-gated finite-module maps (`AH07`--`AH14`);
3. bounded primitive rational pairs and continuant-labelled compositions
   (`AH15`--`AH20`); and
4. residue-labelled graphs, hypergraphs, and matchings (`AH21`--`AH24`).

They are not parameter changes of a single map.  The frozen standard-library
verifier enumerates each displayed box, checks closure pointwise, computes the
full functional-graph signature, and makes **7,863 exact assertions**.  A
second run was byte-identical.  The script and transcript are
`verify_scout.py` and `CANONICAL.txt` in this directory.

Enumeration here is counterexample pressure, not proof of an untested
all-parameter statement.  A bounded owner-search miss means only
`NO_DIRECT_HIT_FOUND_BOUNDED`; it never means novelty, priority, freedom to
operate, or permission to circulate.

The required exclusions were applied before ranking.  Derivative--GCD,
squarefree-extraction/valuation erasure, divisor--GCD maps, generic power or
fixed-linear maps, Schur/LDU, QRT/Lyness, inventory maps, CPE, BQC, RTI, and
all already occupied P1--P161 mechanisms receive no candidate credit.  One
initial formula duplicated the same-batch `NL14/BSP` map exactly and was
removed before this 24-system frozen registry.

The only map with a clean unbounded all-parameter clock is `AH15`, but its
nonabsorbing target fibres are all zero or one and its update is literally one
left-child ray in the Calkin--Wilf tree with a denominator cap.  Thus its two
advertised axes are one unipotent-ray calculation, and direct ownership plus
the P131/SBW collision is decisive.  No other candidate has both a sharp
uniform temporal theorem and an independent target-fibre/image or recovery
axis.  The pool is therefore honestly empty.

## 2. Signature convention

For each representative finite box:

- `S` is the number of states and `I` the one-step image size;
- `F` is the fixed-point count and `H` the largest tail before a cycle;
- `C=l:c,...` records the number `c` of distinct cycles of length `l`; and
- `B=d:m,...` says that `m` targets have one-step indegree `d`, including
  zero-indegree targets.

These signatures are intentionally stronger than a few sample trajectories:
they expose every cycle, every tail, and every one-step fibre in the displayed
box.

## 3. Exact 24-system kill ledger

| ID | literal carrier and deterministic update | frozen exact signal | strongest prospective spine | decisive reason / verdict |
|---|---|---|---|---|
| `AH01/PTF` | Triples `(a,b,c)` of positive integers (ones allowed) with product `N`.  Simultaneously move one least prime factor from a coordinate to its cyclic successor exactly when that prime does not already divide the successor. | `N=60`: `S/I/F/H=54/24/0/5`, `C=6:1`, `B=0:30,1:6,2:6,3:12`. | Product is invariant and the update is a prime-support transport. | Even the first mixed-prime box has a nontrivial 6-cycle and five transient layers; cycle type depends on the incidence of prime supports, with no all-parameter clock or inverse atlas.  It also transfers the occupied finite transport/partition machinery. **`KILL_IRREGULAR_ARITHMETIC_TRANSPORT`.** |
| `AH02/CPF` | On the same ordered-factor carrier, fuse the first adjacent pair of factors greater than one whose gcd is one, replacing `(a,b)` by `(ab,1)`. | `N=60,k=3`: `54/21/21/1`, `C=1:21`; fibre sizes reach 7. | Product and left-to-right priority give a terminating rewrite. | With a fixed slot left behind, the tested update is only one fusion; with compaction it becomes the already excluded run/block consolidation engine.  No independent axis remains. **`KILL_ONE_MERGE_OR_P147`.** |
| `AH03/MSP` | Set partitions of `{1,...,n}`.  For each block `B`, let `p` be the least prime divisor of `sum(B)` and split `B` into its residue classes modulo `p`; do this simultaneously. | `n=5`: `52/9/8/2`, `C=1:8`; largest fibre 19. | Refinement is monotone and reaches an arithmetically stable partition. | It is a partition refinement closure with height two already at the first nontrivial box; the fibre tree is exactly the P126/permanent-refinement silhouette. **`KILL_PARTITION_REFINEMENT_ENGINE`.** |
| `AH04/PMC` | Set partitions of `{1,...,n}`.  Label a block by the product of its elements modulo `m`; merge all blocks with the same label. | `(n,m)=(5,5)`: `52/42/42/1`, `C=1:42`; largest fibre 5. | Fixed partitions have distinct block-product labels. | The update is an idempotent coalescence/closure.  Arithmetic labels do not create temporal depth or a logically independent inverse theorem. **`KILL_LABELLED_CLOSURE`.** |
| `AH05/ATR` | Full binary bracketings of the fixed leaf word `(2,3,5,7,11)`.  Perform the first preorder rotation `((A,B),C)->(A,(B,C))` for which `prod(A)+prod(B)+prod(C)=0 mod 5`. | `14/6/6/1`, `C=1:6`, `B=0:8,2:4,3:2`. | Tamari rank forces termination. | The temporal engine is literally a gated Tamari rotation and is shallower than P144. **`KILL_DIRECT_TAMARI_INTERNAL`.** |
| `AH06/RSF` | All ordered full binary trees with leaves `{2,3,5,7}`.  Recursively swap the two children of every subtree whose leaf-product is a quadratic nonresidue modulo 11. | `120/120/24/0`, `C=1:24,2:48`, all fibres one. | Subtree products freeze the simultaneous swap rule, so the map is an involution. | This is only an invariant-gated permutation action; there are no nontrivial fibres or clock. **`KILL_ACTION_ONLY`.** |
| `AH07/MVI` | `F_p^3`, with `T(x,y,z)=(x,y,xy-z)`. | `p=5`: `125/125/25/0`, `C=1:25,2:50`, all fibres one. | Exact involution and fixed hyperplanes. | This is the standard Vieta involution on Markoff-type cubics, directly owned in the finite-field Markoff literature. **`KILL_DIRECT_VIETA_OWNER`.** |
| `AH08/HCM` | `F_p^3`, with cyclic Vieta update `T(x,y,z)=(y,z,yz-x)`. | `p=5`: bijective on 125 states with cycle lengths `1,2,3,4,6,7,10,12,21,30`. | A polynomial automorphism preserving Markoff-type level sets. | The dense cycle spectrum is not a sharp uniform clock; Markoff automorphism orbits over finite fields are a direct research object. **`KILL_DIRECT_MARKOFF_ACTION`.** |
| `AH09/UGT` | `(Z/6Z)^2`.  If `x` is a unit send `(x,y)` to `(x,y+x)`; else if `y` is a unit send it to `(x+y,y)`; otherwise fix it. | `36/32/16/3`, `C=1:16,6:2`, `B=0:4,1:28,2:4`. | Unit/nonunit strata are invariant enough to describe this particular modulus. | The mixed tails and 6-cycles change with the unit structure of the modulus.  Any classification is a piecewise transvection action, while fibres are at most two. **`KILL_GATED_ACTION_THIN`.** |
| `AH10/DGM` | `2x2` matrices over `F_3`.  If the determinant is nonzero swap the two columns; if it is zero add column one to column two. | `81/81/9/0`, `C=1:9,2:24,3:8`, all fibres one. | Determinant is preserved, freezing an invertible column operation on each stratum. | Pure state-gated `GL_2` action: periods yes, inverse/target fibres no. **`KILL_MATRIX_ACTION_ONLY`.** |
| `AH11/QHN` | `F_p^2`, with quadratic Hénon map `T(x,y)=(y,y^2-x)`. | `p=5`: `25/25/2/0`, cycles of lengths `1,3,9,11`, all fibres one. | Polynomial inverse is immediate. | A bijective Hénon-type polynomial map has no fibre axis, and finite-field polynomial automorphism cycles are owner-dense. **`KILL_HENON_ACTION_ONLY`.** |
| `AH12/SPC` | `F_p^2`, with symmetric sum--product compression `T(x,y)=(x+y+xy,xy)`. | `p=5`: `25/15/5/2`, `C=1:5,2:2,3:1`; 10 targets have two sources. | One-step fibres are the roots of `X^2-(u-v)X+v`. | The discriminant gives a static `0/1/2` fibre law, but cycle data already vary at `p=3,5,7`; this is the previously rejected Vieta/unordered-root quotient engine, not a temporal theorem. **`KILL_STATIC_DISCRIMINANT_ONLY`.** |
| `AH13/FUN` | `(Z/6Z)^3`.  Normalize by multiplying by the inverse of the first unit coordinate; if no coordinate is a unit, send the vector to zero. | `216/77/77/1`, `C=1:77`, with one fibre of size 64. | Fixed normalized vectors and their source counts can be enumerated. | This is a one-step projective normalization/closure; the exceptional zero fibre does not supply a second theorem. **`KILL_NORMALIZATION_CLOSURE`.** |
| `AH14/TPC` | `F_3^3`, with `T(x,y,z)=(x,xy,xyz)`. | `27/15/7/1`, `C=1:7,2:2,4:1`, largest fibre 9. | The first coordinate freezes a triangular multiplicative action. | After freezing `x`, later dynamics are scalar power/action data.  This is explicitly below the generic monomial/triangular threshold. **`KILL_TRIANGULAR_POWER_REDUCTION`.** |
| `AH15/FCD` | Primitive positive pairs `(p,q)` with `p+q<=Q`, plus `dagger`; send `(p,q)` to `(p,p+q)` while the new pair stays under the cap, and otherwise to `dagger`. | `Q=9`: `28/14/1/8`, unique recurrent sink; `B=0:14,1:13,15:1`. | Exact iterate, sharp height `Q-1`, every clock shell, every-time image, and sink fibre. | Every nonsink target has at most one source; all formulas are the same Calkin--Wilf left-ray inequality.  The literal step is directly owned and P131/current `SBW` already occupy its decoder. **`KILL_DIRECT_CALKIN_WILF_THIN`.** |
| `AH16/FFL` | Reduced `p/q in (0,1)` with `q<=Q`; set `T(p,q)=(min(p,q-p),q)`. | `Q=10`: `31/16/16/1`, `B=0:15,1:1,2:15`. | Fixed points are precisely the fractions at most `1/2`; other fibres pair complements. | A one-step fold under the involution `p<->q-p`, hence a generic retraction with no temporal mass. **`KILL_INVOLUTION_FOLD_CLOSURE`.** |
| `AH17/MIF` | Same Farey carrier; send `(p,q)` to `(p^(-1) mod q,q)`. | `31/31/19/0`, `C=1:19,2:6`, all fibres one. | Exact fixed points solve `p^2=1 mod q`. | Pure arithmetic involution.  Counting roots of unity modulo `q` is static classical arithmetic and there is no fibre or clock axis. **`KILL_MODULAR_INVOLUTION_ONLY`.** |
| `AH18/CTR` | Positive compositions `w=(a_1,...,a_k)` of `N`.  Let `r=tr(prod_i [[a_i,1],[1,0]]) mod k` and rotate `w` left by `r`. | `N=8`: bijective on 128 compositions; 32 fixed points and cycles of lengths `2,3,4,5,6`. | Trace is invariant under cyclic permutation, so each orbit is a fixed rotation with period `k/gcd(k,r)`. | Exact period formula, but all fibres are singletons and the update is an invariant-frozen action. **`KILL_CONTINUANT_ACTION_ONLY`.** |
| `AH19/CTG` | Same composition carrier.  Reverse `w` iff its continuant-matrix trace is `0 mod 3`, otherwise fix it. | `N=8`: `128/128/88/0`, with 20 two-cycles. | Symmetry of the continuant matrices makes trace reversal-invariant. | Only a gated involution with singleton fibres; no independent theorem axis. **`KILL_CONTINUANT_INVOLUTION_ONLY`.** |
| `AH20/FMM` | Triples `(x,y,z)` of Farey fractions of order `Q`.  Replace the middle term by the reduced mediant of `x,z` when its denominator is at most `Q`; otherwise leave the triple fixed. | `Q=5`: `1331/561/561/1`; 77 image targets have fibre 11 and 484 have fibre 1. | The endpoint pair freezes a unique normalized middle term. | An idempotent endpoint-conditioned normalization.  The large fibres are only “forget the old middle coordinate.” **`KILL_MEDIANT_NORMALIZATION`.** |
| `AH21/EAI` | Simple graphs on `Z/5Z`.  Send each edge `{u,v}` to `{u+v,u-v}` modulo 5, discard loops, and take the union of image edges. | `1024/128/4/1`, with cycles of lengths `1,2,3,4,6,12`; nonzero fibres `1,3,9,27`. | The edge substitution itself can be diagonalized as a finite relation map. | This is exactly a direct-image system on a finite relation, a permanent P97/generic-relation-power exclusion. **`KILL_RELATION_DIRECT_IMAGE`.** |
| `AH22/CSC` | Simple graphs on `Z/5Z`.  Compute connected components, label each by its vertex sum modulo 5, merge equal-label components, and output cliques on the merged classes. | `1024/30/30/1`; the largest fixed-target fibre is 775. | Fixed points are residue-labelled cluster graphs. | One-step component closure followed by clique completion; P123 and the generic graph-closure ban are decisive. **`KILL_COMPONENT_CLOSURE`.** |
| `AH23/HPS` | 3-uniform hypergraphs on `Z/5Z`.  Map each edge `{a,b,c}` to the distinct triple of pair sums `{a+b,b+c,c+a}`, discarding degenerate images, and take the union. | Bijective on 1024 states; `C=1:16,2:24,4:240`. | The edge map is a permutation of the ten triples, so the entire hypergraph action is its Boolean lift. | Pure induced permutation action with singleton fibres; no inverse or extremal axis beyond cycle inventory. **`KILL_BOOLEAN_LIFT_ACTION`.** |
| `AH24/DMR` | Perfect matchings of `{0,...,5}`.  Rank edges by determinant label `j-i mod 7`; split each ranked edge into its smaller and larger endpoint and cyclically rematch the two endpoint lists. | `15/10/0/3`, with two 2-cycles and one 3-cycle; fibre sizes `0,1,2,3`. | A small nonlinear functional graph exists. | There is no natural all-`n` closure of the smaller/larger endpoint rule, and already at six vertices there is neither absorption nor a stable period law.  The current matching/Hurwitz scout also occupies the nearest action interface. **`KILL_FIXED_SIZE_MATCHING_GADGET`.** |

## 4. Exact theorem ceiling for the strongest near miss `AH15/FCD`

Fix `Q>=2` and let

```text
X_Q = {(p,q) in Z_(>0)^2 : gcd(p,q)=1, p+q<=Q} union {dagger}.
```

Set `T(dagger)=dagger` and

```text
T(p,q) = (p,p+q)   if 2p+q<=Q,
         dagger     otherwise.
```

The complete nonabsorbed iterate is

```text
T^t(p,q)=(p,q+tp)  iff p+q+tp<=Q.
```

Consequently the first hitting time of `dagger` is

```text
h_Q(p,q)=floor((Q-p-q)/p)+1,
```

and the sharp global height is `Q-1`, attained by `(1,1)`.  The exact shell
at time `j` is the primitive lattice strip

```text
{(p,q): gcd(p,q)=1, p+q<=Q,
          jp+q<=Q<(j+1)p+q}.
```

For every `t>=0`, a nonsink target `(r,s)` has the complete fibre law

```text
|(T^t)^(-1)(r,s)| = 1  if s-tr>=1,
                     0  otherwise,
```

with the unique source `(r,s-tr)`.  The sink fibre is

```text
|(T^t)^(-1)(dagger)|
 = 1 + #{(p,q): gcd(p,q)=1, p+q<=Q, h_Q(p,q)<=t}.
```

These formulas are correct and the verifier checks the pointwise hitting-time
formula at `Q=9`, including `(1,1)`, the last admissible layer, and the sink.
They nevertheless form only one theorem axis: all clock shells, image
conditions, and fibres are restatements of the single inequality
`p+q+tp<=Q`.  Nonsink inverse multiplicity never exceeds one; `Q` is recovered
tautologically as height plus one; and changing the cap supplies no logically
independent deformation.

Most importantly, `(p,q)->(p,p+q)` is exactly the left-child move in the
Calkin--Wilf rational tree.  Capping that standard ray and adjoining a sink
does not create a new proof engine.  The same-batch `SBW` scout has already
killed the two-branch stochastic version on direct Calkin--Wilf/P131 grounds.
Thus `AH15` is a theorem-complete **negative control**, not an amber reserve.

## 5. Collision firewall

| candidate block | closest occupied or current neighbour | subtraction result |
|---|---|---|
| `AH01`--`AH04` | P126 composition refinement, P129 pile coalescence, P142 divisor valuations, P147 run consolidation | Prime labels change the trigger, but the surviving arguments are transport, split, merge, or closure.  Those engines receive zero credit. |
| `AH05`--`AH06` | P144 Dyck/Tamari reassociation and the current adaptive-action lane | `AH05` is literally a gated Tamari rotation; `AH06` is an invariant-frozen involution. |
| `AH07`--`AH12` | P125 quadratic shear, P150 Lyness, current nonlinear-algebra Vieta controls | Markoff/Vieta/Henon actions are externally owner-dense; `AH12` leaves only a discriminant fibre after its temporal failure. |
| `AH13`--`AH14` | P100 erasure/normalization, P115 finite-linear components, P153 finite-plane polynomial collapse | One-step normalization or a triangular scalar-action reduction is not a new system package. |
| `AH15`--`AH20` | P131 Euclidean quotient rotation; current `SBW`; permanent action/retraction ban | The left-child ray is direct Calkin--Wilf, folds/mediants are closures, and continuant trace only freezes permutation actions. |
| `AH21`--`AH23` | P97 relation direct images, P123 component complementation, P143 Boolean residuals | Arithmetic edge labels do not change the direct-image, component-closure, or Boolean-lift proof engines. |
| `AH24` | current matching/Hurwitz scout | A single 15-state gadget has no all-parameter theorem spine and cannot be padded into a family. |

No derivative--GCD/PDG/SFE, valuation or digit erasure, generic fixed linear or
power map, Schur/LDU, QRT/Lyness, divisor--GCD, inventory, CPE, BQC, or RTI
candidate is being held silently.  They were exclusions, not part of the 24.

## 6. Freeze decision

- **Screened/tested literal systems:** 24.
- **Survivors:** 0.
- **Kills:** 24.
- **Best negative control:** `AH15/FCD`, killed by a direct Calkin--Wilf step
  and failure of the independent-axis requirement.
- **Paper allocation:** none.
- **Re-entry rule:** a new lane must change the literal mechanism, not enlarge
  one of these boxes or relabel a standard ray/action/closure.
- **External status:** **HOLD_EXTERNAL**.

