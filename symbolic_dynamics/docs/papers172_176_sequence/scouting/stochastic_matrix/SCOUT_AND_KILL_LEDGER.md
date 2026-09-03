# Exact scout and kill ledger

**Counting unit:** one genuinely different literal finite update or Markov
kernel, not a parameter value, theorem strengthening, or second encoding.  
**Executable census:** 23 rows = 18 fresh literals + 5 zero-addition historical
sentinels.  
**Decision vocabulary:** `SPIKE` means worthy of a theorem/owner gate, not
selected or novel; every external action remains `HOLD_EXTERNAL`.

## Fresh-literal accounting

The 18 counted handles are

```text
M02 M03 M04 M05 M06
S01 S02 S03 S04 S05 S06 A01
G01 G05 G02 G03 G04
R02
```

`M01`, `H01`, `R01`, `C01`, and `C02` are replayed only to catch entry-gate
regressions.  They are not counted.  Transferable-engine kills such as `M03`,
`S02`, `G02`, and `R02` remain different literal systems, but receive no
survival credit.

## Per-system exact pilots and decisions

| ID | Literal update/kernel | Exact pilot and early signal | Gate decision |
|---|---|---|---|
| `M01` | `X <- X+uv^T` on binary rectangular matrices, `u,v` uniform | Shapes through `3x3`; Fourier value `2^(r+c-rank B)` checked at every character; every endpoint through three steps; `3x3` rank census `1,49,294,168` and full 512-state support | **ZERO ADDITION / KILL.** Exact historical `RRO`; Delsarte's bilinear-forms scheme already owned the rank geometry. |
| `M02` | `X <- X+vv^T` on binary symmetric matrices | Every character and endpoint through `n=4,t=3`; at `n=4`, Walsh numerator histogram `{-8:35,-4:168,0:435,4:280,8:105,16:1}`, but only 576/1024 states at step three | **KILL DIRECT NEIGHBOUR.** Off-diagonal projection is the subset-inversion tournament walk now treated directly by Ai; diagonal augmentation leaves the same quadratic-form/Fourier engine and no independent axis. |
| `M03` | `X <- X+uv^T+vu^T` on alternating matrices | All characters through `n=5`; exact value `2^(2n-rank B)` and two-step endpoints; `n=5` alternating-rank census `1,155,868` | **KILL OWNER/ENGINE.** Alternating-bilinear-forms association scheme plus abelian Fourier inversion gives the whole package. |
| `M04` | XOR a uniform permutation matrix | `n=2,3,4`; increment-span dimensions `2,5,10`; complete Walsh histograms and Parseval.  At `n=4` the numerator assumes nine values from `-24` to `24` | **KILL COMPLEXITY.** Characters are permanents of sign matrices; the pilot exposes rather than removes the unclassified permanent-value problem. |
| `M05` | OR a uniform nonempty Boolean rectangle into a matrix | All states for `2x2,2x3,3x3`; exact diagonal numerators and four-step distributions.  From zero, `3x3` reaches 511/512 states after four events | **KILL TRANSFER.** Histories are ordered biclique/Boolean-rank covers, already owner-dense and too close to P171's clique-cover inverse engine. |
| `M06` | XOR the row-column cross indexed by uniform `(i,j)` | `n<=4`; exact Fourier histograms, Parseval, and span dimensions `0,2,4,6` | **KILL GENERIC LINEAR.** A translation walk on a `2n-2` dimensional cut/switching space; no second statistic survives Fourier reduction. |
| `S01` | `A <- A intersect f(A)`, fresh uniform endomap `f:[n]->[n]` | Every source/target and image-size mark exhaustively through `n=4`; closed formulas and size chains through `n=7`.  For every `n>=2`, `lambda_(n-1)=lambda_n` and nullities of `Q-lambda I,(Q-lambda I)^2` are `1,2` | **SPIKE 1 / OWNER-THIN.** Forced top Jordan block, all-time every-target law, absorption, and endpoint-conditioned image-size mark form a coherent package. |
| `S02` | `A <- A intersect pi(A)`, fresh uniform permutation | Exact fixed-target hypergeometric count through `n=7`; permutation/cycle-mark brute controls through `n=6`; absorbing sizes are `0,n` | **KILL P170 TRANSFER.** Hypergeometric overlap plus the same symmetric-group cycle marking used in P170; no new independent inverse axis. |
| `S03` | `A <- f^{-1}(A)`, fresh uniform endomap | Every source/target through `n=4`; count `a^b(n-a)^(n-b)`; size eigenvalues through `n=5` | **KILL DIRECT.** This is the neutral Wright--Fisher/binomial sampling chain in subset encoding. |
| `S04` | `A <- f(A)`, fresh uniform endomap | Every source/target through `n=4`; count `n^(n-a)b!S(a,b)`; exact size chains through `n=6` | **KILL DIRECT.** Classical random-map occupancy and the Zubkov--Serov image-composition program own the literal temporal core. |
| `S05` | `A <- A intersect f(A) intersect f^{-1}(A)` | All maps and states through `n=4`; relabelling-orbit kernel verified, with 14 distinct cardinality entries and support 15 at `n=4` | **KILL NO PACKAGE.** Correct symmetry reduction, but no uniform transition or independent mark emerged beyond coupled occupancy constraints. |
| `S06` | `A <- f(A) intersect f^{-1}(A)` | All maps/states through `n=4`; exact kernel depends on `(abs A,abs B,abs(A intersect B))`; 21 orbit entries and full 15-target support occur at `n=4` | **KILL NO PACKAGE.** Removing monotonicity produces a dense three-parameter kernel without a clean clock, spectrum, or inverse law. |
| `A01` | parity pushforward `A <- {y: abs(f^{-1}(y) intersect A) is odd}` | Every source/target and occupied-box mark through `n=5`; Krawtchouk formula checked exactly.  Weight parity is conserved and the finite chain is almost surely absorbed in size `0` or the uniform singleton class | **RESERVE / SPIKE 3.** Complete finite theorem package exists, but most of it is classical parity occupancy plus Krawtchouk inversion; retain only pending a strict owner-value gate. |
| `H01` | `pi <- pi meet ker(c)`, fresh uniform `q`-colouring | Every source/target and global-codeword mark for `q=2,n<=5,t<=3` and `q=3,n<=4,t<=2`; exact falling-factorial kernel and spectrum | **ZERO ADDITION / KILL.** Exact historical `RCR`, already killed against Krachun--Yakubovich, Pitman, and Brown. |
| `G01` | `U <- U intersect T(U)`, fresh uniform `T in End(F_q^n)` | Fixed-target/rank-mark formulas for `q=2,n<=6`, `q=3,5,n<=5`; all subspaces and matrices for `q=2,n<=3`; all exact-layer eigenvalues distinct | **RESERVE BEHIND G05.** Clean every-target diagonalizable chain, but finite-field rank plus P109/P162 machinery is heavy and the same-carrier `G05` has a sharper anomaly. |
| `G05` | `U <- U intersect T^{-1}(U)`, fresh uniform `T` | All fixed targets for `q=2,n<=3`; formulas/Jordan ranks for `q=2,n<=8`, `q=3,5,n<=7`.  Exact-state diagonals are `q^(-a(n-a))`; each complementary interior pair forms one `J_2` in the size quotient | **SPIKE 2 / COLLISION-RISK.** Strong complementary-dimension Jordan ladder and every-target quotient-leak law; must survive P109/P162/P168 and random-rank subtraction. |
| `G02` | `U <- T(U)`, fresh uniform linear map | Every target through `q=2,n<=3`; rank-retention law through `n=4` | **KILL DIRECT.** Random matrix rank and random-matrix-product image chain. |
| `G03` | `U <- U intersect ker(ell)`, fresh uniform linear functional | Every target and every `t<=n+2` through `n=4`; fixed codimension-`d` target has `2^((n-a)t) product_(i<d)(2^t-2^i)` histories | **KILL DIRECT/THIN.** It is the row-space/rank law of a random `t x a` matrix, with no residual beyond the standard Gaussian count. |
| `G04` | affine subspace `A <- T(A)+b`, fresh uniform affine map | Every affine target for `q=2,n<=3`; 3, 11, 51 carrier states and recurrent classes of 2, 4, 8 points | **KILL REPAINT.** Affine decoration of `G02`; translation erases location and leaves the same rank chain. |
| `R01` | row-support inclusion relation | All Boolean matrices through `n=4`; preorder image and transpose-on-preorders checked; image counts `1,4,29,355` | **ZERO ADDITION.** Literal P143, including its one/two-cycle mechanism. |
| `R02` | row-disjointness feedback `A <- not(AA^T)` in the Boolean semiring | Complete functional graphs through `n=3`; image sizes `2,5,18`, periods `1,2`, maximum tail `3` | **KILL P171 TRANSFER.** Complement of the Boolean Gram image; P171's graph-power and ordered-column fibres transfer after the complement splice. |
| `C01` | unital binary code `C <- span(C*C)` | Complete unital-code lattices through length 7; fixed census is `Bell(n)`.  The `RM(1,3)` control corrects the misleading small box with dimensions `4->7->8->8` | **ZERO ADDITION / KILL DIRECT.** Historical Schur-square closure; repeated powers and Hilbert regularity are directly owned. |
| `C02` | field-Gram feedback `A <- AA^T` over `F_2` | Complete functional graphs through `n=3`; periods reach 3 | **ZERO ADDITION / KILL.** Exact prior `R05` parity-Gram literal; also a semiring repaint of the now occupied P171 silhouette. |

## Funnel

```text
23 executable pilots
-5 exact historical literals
=18 fresh literal systems

18 fresh
  2 theorem spikes: S01, G05
  2 reserves: A01, G01
 14 kills
```

The reserve labels are intentionally conservative.  `A01` may collapse to
classical parity occupancy, and `G01` is dominated within this lane.  A bounded
owner-search non-hit cannot upgrade either.  `S01` and `G05` remain discovery
recommendations only; they are not assigned to P172--P176 here.
