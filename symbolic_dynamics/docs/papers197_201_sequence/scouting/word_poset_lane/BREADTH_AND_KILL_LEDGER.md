# Word, poset, lattice, tableau, and composition breadth ledger

Status: one theorem-ready spike, one reserve, ten kills.  This ledger makes no
novelty, priority, authorship, venue, or external-release claim.  All entries
are deterministic self-maps with frozen boundary conventions.

## Ranked candidates

| rank / ID | literal self-map | exact early signal | theorem route | disposition |
|---|---|---|---|---|
| 1 / `C01_TCSD` | On `{-1,0,1}^{Z/nZ}`, set `D(x)_i=sgn(x_(i+1)-x_i)`. | Complete `n<=12`; at `n=12`: `531441/103681/9621` states/image/recurrent, max tail 11, periods `1,2,3,8,12,24`, max fibre 322. | Recurrent core `D^4=rho^2`; parity-sharp clock; exact depth traces; exact cycle traces; every-target 3x3 trace; Lucas fibre extremum. | **`PROMOTE_SPIKE / OWNER_AMBER / HOLD_EXTERNAL`.** Only recommendation. |
| 2 / `C02_ZAD` | On chain words `{0,...,M}^{Z/mZ}`, apply Zadeh implication `T_i=max(M-x_i,min(x_i,x_(i+1)))`. | `M=3,m=5`: `1024/242/22`, depth `0:22,1:162,2:360,3:240,4:160,5:80`, max fibre 18.  For `M=2,3` and `3<=m<=8`, max tail is exactly `m`. | Centered absolute values obey cyclic min erosion; recurrent signs are independent sets and rotate.  `R_(M,m)=ceil(M/2)L_m+1_(M even)`; `Fix(T^t)=ceil(M/2)L_gcd(m,t)+1_(M even)`; every target has an `(M+1)`-matrix trace. | **`RESERVE_OWNER_RED_AMBER / HOLD_EXTERNAL`.** Strong mathematics, but same cyclic-chain/implication neighborhood as P196 and transfer syntax near P187. |
| 3 / `C03_PDM` | On positive compositions, simultaneously delete every cut between `a_i>a_(i+1)`; equivalently sum each maximal strict descending run. | `N=16`: `32768/10747/231`, max tail 14, unique deepest `(2,1^14)`, max fibre 37. | Fixed count `p(N)`; sharp `N-2`; every target is a chain of strictly decreasing refinements with endpoint inequalities. | **`KILL_SORTING_COALESCENCE`.** Parallel adjacent-violator sorting plus P147/P191 proof-shell transfer. |
| 4 / `C04_LPC` | On positive compositions, delete the cut after every old strict interior local peak `a_(i-1)<a_i>a_(i+1)`. | `N=18`: `131072/54100/9167`, max tail 15, unique deepest `(1,2,1^15)`, max fibre 26. | Monotone cut loss; local-peak-free fixed words; refinement CSP. | **`KILL_P191_CLOCK_EXTREMIZER`.** Its `N-3` clock and unique deepest state reproduce P191's temporal spine, with a weaker inverse. |
| 5 / `C05_TDS` | Across all SYT of size `n`, find the least consecutive values in incomparable cells that are inverted in row-reading order and swap them; fix if none. | `n=10`: 9,496 states, image 6,408, fixed 42, max tail 22, max fibre 5. | Inversion potential on linear extensions; predecessor swaps. | **`KILL_STANDARD_SORTING`.** A deterministic 0-Hecke/bubble-sort path on linear extensions. |
| 6 / `C06_FHN` | On ideals of the fence `1<2>3<4>...`, take Heyting pseudocomplement `not I={x:down(x) intersect I=empty}`. | `n=20`: 17,711 states, image=recurrent 1,024, tail 1, period 2, unique max fibre 1,024. | General identity `not^3=not`; Fibonacci ideal count. | **`KILL_STANDARD_CLOSURE`.** Double-negation closure supplies the whole dynamics. |
| 7 / `C07_SHI` | On cyclic words of ideals of a bottom-plus-`r`-leaves poset, apply Heyting implication coordinatewise: `T_i=A_i=>A_(i+1)`. | `r=3,m=4`: 6,561 states, image=recurrent 453, tail 1, cycles `1:1,2:14,4:106`, max fibre 99. | Exact identity `T^2=rho T`; local implication matrices. | **`KILL_P196_ARCHITECTURE`.** One-step core followed by shift, on an implication alphabet. |
| 8 / `C08_HMR` | On two ideals of the same star Heyting lattice, set `T(A,B)=(A meet B,A=>B)`. | `r=4`: 289 states, image 83, fixed 17, tail 2, max fibre 17. | `T^2(A,B)=(A meet B,top)`. | **`KILL_CANONICAL_LATTICE_SPLIT`.** The displayed normal form is the entire shallow result. |
| 9 / `C09_BES` | For `R=(F_2)^r`, map `(x_1,...,x_k)` to its full elementary-symmetric tuple `(e_1,...,e_k)`. | `k=5,r=2`: 1,024 states, image 36, fixed 9, depth `0:9,1:247,2:768`, max fibre 100. | Each atom of `R` reduces to `w -> (binom(w,j) mod 2)_j`; the next weight is `2^popcount(w)-1`. | **`KILL_VIETA_NORMAL_FORM_COMPRESSION`.** Coordinatewise canonical invariant extraction, tail at most two. |
| 10 / `C10_KDI` | On `{0,...,M}^{Z/mZ}`, apply Kleene--Dienes implication `T_i=max(M-x_i,x_(i+1))`. | `M=3,m=5`: 1,024 states, image=recurrent 197, tail 1, cycles `1:2,5:39`, max fibre 10. | Exact identity `T^2=rho T`. | **`KILL_EXACT_P196_SILHOUETTE`.** Different truth table, same one-step-core/rotation theorem. |
| 11 / `C11_SLI` | On labelled strict posets, declare `x<_{T(P)}y` iff the strict principal lower set of `x` is a proper subset of that of `y`. | `n=5`: 4,231 states, image 601, recurrent 541, max tail 2, max fibre 31. | Inclusion profiles and Boolean-row supports. | **`KILL_P143_RESTRICTION`.** This is the poset restriction of the occupied row-support inclusion/closure engine. |
| 12 / `C12_BCE` | On partitions in an `r x M` box, erode one column `E(lambda)_i=max(lambda_i-1,0)`, then take box complement `T=C E`. | `r=M=5`: 252 states, image=recurrent 126, tail 1, periods 1 and 2, max fibre 6. | Each reversed coordinate uses `f(0)=M`, `f(a)=M-a+1` for `a>0`; after one step `f` is an involution. | **`KILL_COORDINATE_INVOLUTION`.** Complement plus elementary erosion, no independent axis. |

The recommendation count is one, below the permitted maximum two.  `C02_ZAD`
is deliberately a reserve rather than a second recommendation.

## Compact exact tables

### TCSD

Entries are `(image,recurrent,max tail,max fibre)`.

```text
n=4  (43,27,3,7)        n=8  (2203,459,7,47)
n=5  (121,41,3,7)       n=9  (5773,949,7,47)
n=6  (321,93,5,18)      n=10 (15123,2093,9,123)
n=7  (841,225,5,18)     n=11 (39601,4533,9,123)
                            n=12 (103681,9621,11,322)
```

The data killed the tempting false conjecture `max tail=n-1 for all n`; odd
lengths have `n-2`.

### Zadeh implication

Entries are `(recurrent,max tail,max fibre)` for `m=3,...,8`.

```text
M=2: (5,3,4),(8,4,7),(12,5,11),(19,6,18),(30,7,29),(48,8,47)
M=3: (8,3,5),(14,4,10),(22,5,18),(36,6,31),(58,7,52),(94,8,100)
```

The jump to 100 at `(M,m)=(3,8)` is retained as an active counterexample to
simple extrapolations of the maximum-fibre sequence.

### Composition descent coalescence

At `N=16` the complete depth histogram is

```text
0:231,1:2374,2:6845,3:9095,4:6883,5:3946,6:1903,7:858,
8:378,9:155,10:63,11:24,12:9,13:3,14:1.
```

This is mathematically coherent evidence, but it does not survive the
sorting/closure gate.

## Pre-denominator collision kills

These attractive maps were tested or reconstructed but are not counted among
the twelve ranked candidates because a prior literal map, conjugacy, or
direct lift was found.

| proposed map | exact collision | disposition |
|---|---|---|
| Full words `w in [n]^n` mapped to strict earlier/suffix inversion ranks | After one step this is exactly historical inversion-sequence `S01`; Allagan--Gao--Testart is recorded there as direct owner. | `KILL_DIRECT_OWNER_LIFT` |
| Full words mapped to the number of distinct smaller earlier letters | One-step lift of historical `S05`, already killed as support compression. | `KILL_DIRECT_SCOUT_REPEAT` |
| Replace each binary run by its run-length parity | Literal historical `W04`. | `KILL_LITERAL_REPEAT` |
| Motzkin summit flattening `U H^r D -> H^(r+2)` in parallel | Historical Dyck/Motzkin coordinate-erosion and parallel-peak exclusion beside P144/P160. | `KILL_INTERNAL_EROSION` |
| Composition histogram/Ferrers conjugation | Same Ferrers-quotient engine as historical D18 and P189; partitions enter a conjugation 1/2-cycle after one step. | `KILL_FERRERS_CANONICALIZATION` |
| Double every composition cut modulo `N` and delete collisions | Finite-subset decimation/necklace-expansion factor already occupied near P96. | `KILL_DIRECT_SUBSET_ACTION` |
| Ordered set partitions with every nonsingleton box sending its least label to the next fixed box | Label reversal plus forgetting box names gives the cyclic token-transfer engine of P169; counts are exactly a `k!` lift of P169. | `KILL_LABELLED_LIFT_P169` |
| Strict poset relational squaring `R -> R o R` | Literal historical `C12_RPE/A02_PSE`. | `KILL_LITERAL_REPEAT` |
| Binary-projective Steiner cyclic product words | The length-three instance is the retired P160 literal map and the family uses the same quasigroup-product engine. | `KILL_RETIRED_LITERAL_FAMILY` |

## Verification

`verify_word_poset_lane.py` is standard-library-only and independently
constructs every map in this ledger.  It makes 3,238,990 exact assertions.
Two fresh processes were byte-identical with output SHA-256
`2b47662aaeab35569a9720896846537c58e040a4b82b9197c4a8b698e7479132`.
