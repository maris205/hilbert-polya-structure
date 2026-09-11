# Nonlinear-algebra replacement breadth scout — P162–P166

**Lane:** `replacement_nonlinear_algebra`  
**Freeze:** 2026-09-02  
**External state:** **HOLD_EXTERNAL**  
**Decision:** **EMPTY_POOL**; twenty-four kills and no paper allocation

## 1. Scope and evidence rule

This is a fresh replacement pass after the earlier arithmetic/algebra and
geometry/group pools failed their specialist thresholds.  It exact-tests 24
literal self-maps, six in each of four mechanism families:

1. class-two/extraspecial commutator windows;
2. nilpotent-semigroup recurrence windows;
3. nonlinear finite-ring or finite-algebra maps; and
4. rank-changing module/configuration maps.

The deterministic control is `verify_scout.py`; `CANONICAL.txt` is its frozen
stdout.  Exact enumeration is counterexample pressure only.  It neither proves
the proposed all-parameter reductions nor certifies ownership.  A bounded
search miss below means only `NO_DIRECT_HIT_FOUND_BOUNDED`; it is not novelty,
priority, freedom to operate, or permission to circulate.

The intake exclusions were applied before ranking.  No candidate is promoted
by a generic linear or group power map, Fibonacci toral conjugacy, Schur/LDU
factorization, valuation truncation, QRT/Lyness dynamics, or the proof engines
of P108/P119/P125/P150/P154/P157.  A candidate that reduces to one of those
engines is killed rather than relabelled.

## 2. Exact ledger

In the signatures below, `S/I/F/H` are state count, one-step image size, fixed
count, and maximum tail; `C` is the cycle histogram by length.  The entries are
representative boxes from the frozen transcript.

| ID | literal carrier and update | representative exact signature | strongest all-parameter signal | inverse and third-axis test | collision / decision |
|---|---|---|---|---|---|
| `NL01/SCW` | On `H_p^2`, `T(x,y)=(y,[x,y])`. | `p=3: S/I/F/H=729/75/1/3`, `C={1:1}`. | In every class-two group, `T^3=(e,e)`; on generalized Heisenberg groups the middle layer is the alternating-form value. | Every target `(g,c)` has `0`, `|G|`, or `p^(2d)` sources according as `c` and the projection of `g` meet the elementary bilinear criterion.  No independent deformation survives. | Mandatory candidate.  Constant-depth bilinear bookkeeping; P70/P111/P119/P135 and direct commutator-word fibres consume it. **`KILL_WORD_MAP_OWNER_THIN`.** |
| `NL02/PCW` | On `H_p^2`, `T(x,y)=(xy,[x,y])`. | `p=3: 729/75/27/2`, `C={1:27}`. | The commutator is central, so the second iterate lies in the fixed stratum `(g,e)`. | Fibres again reduce to one alternating linear equation after fixing the product.  The only extra statistic is the fixed copy of `H_p`. | Same class-two word-map engine as `NL01`, still shallower. **`KILL_DOMINATED_COMMUTATOR`.** |
| `NL03/CTW` | On `H_p^3`, replace a triple by the three pairwise commutators. | `p=3: 19683/27/1/2`, `C={1:1}`. | The first image is central and the second is the identity triple. | Image/fibres are the value distribution of three alternating bilinear forms with a shared input triple.  No third axis. | P119 commutator machinery plus direct commutator-word fibre ownership. **`KILL_CENTRAL_DEPTH_TWO`.** |
| `NL04/DCW` | On `H_p^3`, `T(x,y,z)=(y,z,[x,z])`. | `p=3: 19683/2025/1/4`, `C={1:1}`. | Successive shifts move the central commutator out in exactly four steps. | Reverse layers are repeated linear equations against one alternating form; the sharp clock is merely window length. | Same carrier/window silhouette as P111/P119 with no new axis. **`KILL_SHIFT_REGISTER_THIN`.** |
| `NL05/CAP` | On `H_p^3`, `T(x,y,z)=(xy,yz,[x,z])`. | `p=3: 19683/2025/27/2`, `C={1:27,3:234}`. | Modulo the centre the update is the finite-linear recurrence `(u,v,w)->(u+v,v+w,0)`; the central coordinate is a bilinear cocycle. | Fibres can be stratified by the rank of that quotient recurrence, but identifiability transfers from its linear quotient. | Exactly the forbidden P119/P137 pattern: linear quotient plus commutator bookkeeping. **`KILL_INTERNAL_ENGINE`.** |
| `NL06/CCC` | On `H_p^3`, each output is a product of two consecutive pairwise commutators. | `p=3: 19683/27/1/2`, `C={1:1}`. | Central image, then identity. | Simultaneous fibre counts are a rank census for three dependent alternating equations; no temporal depth remains. | Dominated by `NL03` and the same direct owner. **`KILL_CENTRAL_DEPTH_TWO`.** |
| `NL07/TWC` | Let `S_(q,h)={0} union A^[1,h]` be the free semigroup truncated to zero above length `h`; on `S_(q,h)^2`, `T(u,v)=(uv,vu)`. | `q=2,h=4: 961/61/1/3`, `C={1:1}`; nonzero indegrees include `1,2,3`, and sink indegree `893`. | Nonzero iterates are the two complementary Thue–Morse block words; their common length at time `t>=1` is `2^(t-1)(|u|+|v|)`.  Thus zero is the only recurrent state, the sharp height is `1+floor(log_2 h)`, and every depth shell is an explicit weighted length sum. | Every time-`t` target fibre is an exact finite parsing sum against the two complementary block patterns, including the zero and mixed-zero branches.  Independently, for `h>=3` the largest nonzero one-step fibre is `h-1`, attained exactly by the `q` targets `(a^h,a^h)`. | Fici–Romana–Sciortino–Urbina explicitly identify every morphism `(uv,vu)` as composition with the Thue–Morse morphism.  That consumes the full iterate skeleton; after subtracting it, only an artificial cap, parsing, and a same-axis cut extremum remain. **`KILL_DIRECT_THUE_MORSE_ACTION_OWNER`.** |
| `NL08/SSW` | On the same truncated free semigroup, `T(u,v)=(uvu,vuv)`. | `q=2,h=4: 961/21/1/2`, `C={1:1}`. | Lengths evolve by `[[2,1],[1,2]]` until overflow. | Reverse equations are overlap/sandwich word equations; no cleaner every-target atlas than `NL07` emerged. | Dominated by `NL07` after word-equation subtraction. **`KILL_DOMINATED_WORD_WINDOW`.** |
| `NL09/TCW` | On triples of truncated words, `T(u,v,w)=(uv,vw,wu)`. | `q=2,h=3: 3375/189/1/2`, `C={1:1}`. | Lengths follow a cyclic `I+S` recurrence before simultaneous or partial overflow. | Fibres are coupled word equations and the partial-overflow boundary destroys a uniform target law. | Generic linear recurrence on lengths plus word equations; no third axis. **`KILL_WEAK_INVERSE_AXIS`.** |
| `NL10/PAC` | In the nilpotent path semigroup of a directed chain, `T(x,y)=(xy,y)`. | chain size `5`: `121/21/11/2`, `C={1:11}`. | Since no nonzero path squares, `T^2(x,y)=(0,y)` whenever the first product survives, and that state is fixed. | Fibres are merely counts of factorizations of a path through an intermediate vertex. | Definition-level path factorization and constant depth. **`KILL_PATH_FACTORISATION`.** |
| `NL11/UTW` | For strictly upper `3x3` binary matrices, `T(A,B)=(AB,(AB)A)`. | `64/2/1/2`, `C={1:1}`. | Every triple product is zero and every product lies in the one-dimensional top-right annihilator. | Image and fibres are one bilinear scalar equation. | P109/P119 and the earlier P122–P126 `AB/BA` scout make the collision decisive. **`KILL_MATRIX_WORD_SHALLOW`.** |
| `NL12/DTW` | For order-decreasing transformations of `[n]`, `T(f,g)=(fgf,gf)`. | `n=5: 576/8/1/2`, `C={1:1}`. | Coordinates are positive words in `f,g`; any word of length at least `n-1` is the zero transformation, giving a logarithmic word-length bound. | Factorization fibres in a transformation semigroup have no closed all-target law here, and the bound is not a separate structural theorem. | Generic nilpotent transformation-semigroup word evaluation. **`KILL_GENERIC_WORD_NILPOTENCE`.** |
| `NL13/DSS` | On `F_p^2`, `T(a,b)=(a,ab)` (scalar action on the square-zero direction). | `p=5: 25/21/9/1`, `C={1:9,2:2,4:2}`. | `T^t(a,b)=(a,a^t b)`; periods are multiplicative orders and only the `a=0` line has tails. | For `t>=1`, `(c,d)` has one source if `c!=0`, `p` sources at `(0,0)`, and zero on the rest of the zero line.  Recovering `p` from the exceptional fibre is tautological. | Generic cyclic scalar action and finite-linear fibres after freezing `a`; too thin. **`KILL_SKEW_PRODUCT_THIN`.** |
| `NL14/BSP` | On `F_p^2`, `T(x,y)=(xy,x(1-y))`. | `p=3: 9/7/1/5`; `p=5: 25/21/1/7`, with new 2- and 3-cycles. | The sum of the two outputs is `x`, yielding the second-order recurrence `x_(t+1)=x_t(x_(t-1)-x_t)`, but the prime boxes have no stable period law. | One-step fibres are exact: `p` at zero, one off the line `u+v=0`, and zero at nonzero points of that line. | A first-fibre formula without an all-parameter temporal theorem is below threshold. **`KILL_UNSTABLE_POLYNOMIAL_DYNAMICS`.** |
| `NL15/MDQ` | On `F_p^2`, `T(x,y)=(xy,x-y)`. | heights for `p=3,5,7` are `3,6,6`; cycle types vary. | No uniform temporal reduction survived the prime scan. | A target `(u,v)` has `1+chi(v^2+4u)` sources.  This is the unordered-root/Vieta quotient under a linear sign swap. | Static discriminant fibres collide with the P122–P126 Vieta-fold scout and P125; temporal axis is weak. **`KILL_VIETA_QUOTIENT`.** |
| `NL16/DFM` | On `M_2(F_p)`, `T(A)=A+det(A)I`. | `p=2: 16/12/10/1`; `p=3: 81/54/33/2`. | Trace and determinant obey a closed two-scalar polynomial update, but the resulting period split is characteristic-sensitive and shallow in the tested boxes. | Matrix fibres reduce through trace/determinant strata; no independent rank or deformation theorem appeared. | Determinant/adjugate engine is occupied by P103; polynomial remainder is weak. **`KILL_P103_RECOMBINATION`.** |
| `NL17/PQC` | Fix `E=diag(1,0)` and set `T(A)=EA(I-E)AE=(a_12 a_21)E`. | `p=5: 625/5/1/2`, `C={1:1}`. | The image is a scalar line annihilated by the next iterate. | A nonzero scalar target has `p^2(p-1)` sources, zero has `p^2(2p-1)`, and all other targets are empty. | One Peirce multiplication plus one hyperbola count. **`KILL_EXACT_BUT_SHALLOW`.** |
| `NL18/MSQ` | With `N=E_12`, set `T(A)=ANA` on `M_2(F_p)`. | `p=3: 81/12/10/2`, `C={1:10}`. | If `c=A_21`, then `T^2(A)=c^2T(A)`; subsequent motion is a scalar power map on a rank-one image. | First fibres are polynomial rank-one equations, but later fibres transfer to the forbidden scalar-power engine. | Generic power map after one sandwich; matrix-word owner density. **`KILL_POWER_MAP_REDUCTION`.** |
| `NL19/UCS` | Unital binary codes `C<=F_2^n`, `T(C)=span(C*C)` under coordinatewise product. | `n=4: 16/15/15/1`, one nonfixed source. | `T^t(C)=C^[2^t]` is increasing and stabilizes at the algebra generated by `C`; fixed points are coordinate subalgebras/partition algebras. | Target fibres ask for generating subspaces of a prescribed coordinate algebra; extremal growth is code-power data. | Randriambololona and Falk–Heninger–Rudow directly own products, repeated powers, growth, and stability. **`KILL_DIRECT_SCHUR_POWER_OWNER`.** |
| `NL20/TPS` | All subspaces of `F_2[x]/(x^3)`, `T(U)=span(UU)`. | `16/6/4/2`, `C={1:4}`. | Nilpotence and the scalar projection force a two-step classification in this three-dimensional algebra. | Fibres are a finite subspace-product table with no scalable third axis. | P107/P109/P124 and generic algebra-generation/subspace-square machinery. **`KILL_SMALL_ALGEBRA_TABLE`.** |
| `NL21/LDS` | All subspaces of the three-dimensional Heisenberg Lie algebra, `T(U)=[U,U]`. | `16/2/1/2`, `C={1:1}`. | The derived image lies in the centre and the second derived subspace is zero. | Fibres only distinguish abelian subspaces from the rest. | Lie version of the already killed class-two commutator collapse. **`KILL_SAME_BILINEAR_ENGINE`.** |
| `NL22/EWS` | All subspaces of the two-generator exterior algebra, `T(U)=span(U wedge U)`. | `67/14/13/2`, `C={1:13}`. | Degree doubling supplies a nilpotent bound away from the scalar component; small rank has only two transient layers. | Product-subspace fibres are nonuniform but no all-rank atlas emerged. | Internal exterior-square scouts (P132–P136 and P147–P151) plus generic subspace powers. **`KILL_INTERNAL_EXTERIOR_ENGINE`.** |
| `NL23/SLC` | Pairs of subspaces of `F_2^3`, `T(U,W)=(U+W,U cap W)`. | `256/66/66/1`, `C={1:66}`. | Lattice absorption law gives `T^2=T`. | Fibres are subspace-lattice comparator counts. | Permanent comparator/closure exclusion. **`KILL_LATTICE_COMPARATOR`.** |
| `NL24/TSH` | Subspaces `U<=M_2(F_2)`; replace `U` by `L(U) tensor R(U)`, using column and row supports. | `67/17/17/1`, with one fibre of size `51`. | This is an extensive idempotent hull: `T^2=T`. | Every fixed target is a rectangular tensor subspace; its fibre is a support-realization count. | Generic closure operator plus P109-style support/rank machinery. **`KILL_TENSOR_HULL_CLOSURE`.** |

## 3. Near-miss theorem ceiling and decisive kill for `NL07/TWC`

Fix an alphabet `A` of size `q>=2` and `h>=1`.  Give `0` absorbing
multiplication and concatenate two nonzero words only when the result has
length at most `h`.  Put

`T(u,v)=(uv,vu)`.

Let `theta(0)=01`, `theta(1)=10`, and substitute the word `u` for `0` and
`v` for `1`.  If `u,v` are nonzero and `s=|u|+|v|`, then for every `t>=1`
with `2^(t-1)s<=h`, the two coordinates of `T^t(u,v)` are obtained from
`theta^t(0)` and `theta^t(1)`.  Otherwise both coordinates are zero.  This
immediately gives the exact temporal census

`#{x : tail(x)>t} = sum_(s=2)^(floor(h/2^(t-1))) (s-1) q^s`  for `t>=1`,

with the empty sum interpreted as zero.  The zero pair is the unique recurrent
state and the sharp height is `1+floor(log_2 h)`.

For the independent inverse axis, fix a nonzero target `(A,B)` and time
`t>=1`.  Its fibre is empty unless `|A|=|B|` and `2^(t-1)` divides that common
length.  Put `s=|A|/2^(t-1)`.  For each split `s=a+b`, `a,b>=1`, parse `A`
according to `theta^t(0)` using blocks of lengths `a,b`, and parse `B`
according to `theta^t(1)`.  That split contributes one precisely when all
zero-blocks agree on one word `u`, all one-blocks agree on one word `v`, and
the two parsings recover the same pair.  Summing these indicators is the
complete time-`t` fibre.  Mixed-zero targets have empty fibre, while

`#(T^t)^(-1)(0,0) = |S_(q,h)|^2 - sum_(s=2)^(floor(h/2^(t-1))) (s-1)q^s`.

Finally, for `h>=3`, a nonzero one-step fibre has size at most `h-1`.  Equality
forces all `h-1` cyclic cuts of one length-`h` word to agree, hence that word is
constant.  Therefore equality occurs exactly for the `q` targets
`(a^h,a^h)`.  (`h=1,2` must remain explicit boundary cases.)

This is the largest honest theorem ceiling at scout stage, but it does not
survive ownership subtraction.  Fici, Romana, Sciortino, and Urbina prove in
their 2025 primary paper on morphisms that a binary morphism of the form
`mu=(uv,vu)` is exactly `psi compose tau`, where `tau=(01,10)` is the
Thue–Morse morphism.  Hence our update is right-composition by `tau`, and the
entire iterate formula is that established morphism action.  The cap converts
the already-owned exponential length growth into a sink clock.  The remaining
target parsing and maximal-cut statements share one word-factorization axis;
they do not supply two independent residual theorem axes.  The correct verdict
is **`KILL_DIRECT_THUE_MORSE_ACTION_OWNER`**, not amber.

## 4. P1–P161 collision firewall

| candidate block | closest occupied/internal systems | decisive comparison |
|---|---|---|
| `NL01`–`NL06`, `NL21` | P70 weighted Heisenberg nullities; P111 Heisenberg area; P119 regular Engel unitriangular dynamics; P135 centralizer partitions; P137 rank-feedback `p`-groups | The new windows centralize in one step or have a finite-linear quotient with a bilinear cocycle.  They add no owner-thin axis after commutator fibres are subtracted. |
| `NL07`–`NL12` | P30 free-monoid incidence; P86 adjacent-product process; P117 cyclic words; P134 border arrays; P139 Lyndon feedback; P122–P126 algebraic scout `C12=(AB,BA)` | `NL08`–`NL12` are shallow or dominated.  `NL07` is not a literal occupied paper map, but externally it is right-composition by the Thue–Morse morphism; the overflow sink does not restore a paper-scale residual. |
| `NL13`–`NL15` | P108 Fibonacci absorption; P121 product-plus-one; P125 quadratic shear; P150 Lyness; P122–P126 Vieta-fold scout | `NL13` is a scalar skew product; `NL14` has no period theorem; `NL15` is a static Vieta quotient.  None may re-enter through a renamed quadratic map. |
| `NL16`–`NL18` | P102 group-algebra norm; P103 double adjugate; P119 matrix commutators; prior `AB/BA` scouts | Determinant/Peirce/sandwich reduction leaves depth at most two or a scalar power map. |
| `NL19`–`NL24` | P107 annihilator-power ideals; P109 nilpotent-image subspaces; P124 cross-colon ideals; P143 Boolean row residual; prior exterior-square scouts | Schur powers are directly owned; the remaining maps are product closures, derived subspaces, comparators, or tensor hulls and fail the non-closure intake rule. |
| whole lane | P154 normalizers; P157 Hensel cubic | No subgroup-normalizer, valuation-lifting, or prime-power truncation mechanism is used. |

The literal directory-name roster through P161 was inspected, and targeted
full-text searches were made for `commutator`, `Heisenberg`, `AB/BA`, word
products, annihilators, module ranks, and subspace products.  The exact
`NL07` update string was not found locally.  This is a bounded internal
noncollision result, not an external novelty statement.

## 5. Freeze decision

- **Focused survivors:** none; **`EMPTY_POOL`**.
- **Killed:** `NL01`–`NL24`.
- **Selected papers:** none.
- **Next permitted action:** change mechanism family.  Do not reopen `NL07`
  by presenting Thue–Morse right-composition as a new recurrence.
- **External status:** **HOLD_EXTERNAL**.
