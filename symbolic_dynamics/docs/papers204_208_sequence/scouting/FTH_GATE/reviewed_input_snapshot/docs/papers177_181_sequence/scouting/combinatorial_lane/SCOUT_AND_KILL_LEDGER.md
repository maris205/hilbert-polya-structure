# Scout and kill ledger

**Lifecycle:** `CLOSED_NO_RECOMMENDATION / HOLD_EXTERNAL`  
**Counting unit:** one literal map, never one parameter choice.

| ID | carrier and literal update | exact pilot and early signal | decision |
|---|---|---|---|
| `C01 / MCJ` | `S_n` in functional notation.  Let `C_0(pi)` be the cycle containing 0.  If it is not spanning, put `a=min([n] minus C_0(pi))` and swap the two outgoing values `pi(0),pi(a)`; spanning cycles are fixed. | Exhaustive `n<=9`.  Depth is `cyc(pi)-1`; all `n`-cycles are fixed; every-time every-target fibres are record-cut binomials; terminal basin polynomial is `(1+u)^r`; depth layers and basin-size strata are unsigned Stirling numbers. | **KILL_FOATA_STAR_TRANSPOSITION_THIN.**  Correct but not a new proof engine after Foata/star-transposition zero credit; direct internal proximity to P105, P122, and P155. |
| `C02 / IAC` | `S_n`; with fixed long cycle `c=(0 1 ... n-1)`, set `T(pi)=pi^{-1} c`. | Exhaustive `n<=8`.  `T^2(pi)=c^{-1}pi c`, all periods divide `2n`, and fixed powers reduce to centralizers or square roots of powers of `c`; Möbius inversion gives the full cycle census. | **KILL_PERMUTATION_ROOT_ENGINE.**  Singleton fibres and a full theorem are present, but permutation-root enumeration is directly owned and the dihedral/inversion architecture is occupied by P91/P102/P154. |
| `C03 / CTC` | `S_n`; `T(pi)=pi^{-1}c pi`. | Exhaustive `n<=8`.  The first image is exactly the set of long cycles and each such target has fibre `n`; later periods and tails already branch irregularly (`n=8` has maximum tail 54). | **KILL_NO_UNIFORM_TEMPORAL_SPINE.**  Conjugacy-orbit front end is standard and the recurrent core supplies no independent closed axis. |
| `C04 / PMX` | words in `[q]^n`; the `i`th output is the least alphabet symbol absent from the first `i` input positions, totalized to 0 after the prefix contains all symbols. | Exhaustive `(q,n)=(2,1..10),(3,1..8),(4,1..6)`.  Audited recurrence is only period two, with tail at most three; image and maximum fibre are recorded canonically. | **KILL_PREFIX_MEX_TRANSFER.**  It is a prefix transducer assembled from the already occupied P118 mex and P132 prefix-feedback mechanisms, with no new structural inverse axis. |
| `C05 / NOG` | words in `[n]^n`; output coordinate `i` is the cyclic distance modulo `n` to the next occurrence of the same letter. | Exhaustive `n<=6` (46,656 states at the top box).  The map factors injectively through equality partitions: image size is the Bell number, and a code with `k` blocks has labelled fibre `(n)_k`; temporal cores have only small irregular periods. | **KILL_STATIC_PARTITION_ENCODER.**  The labelled-fibre theorem is exactly a kernel-partition count; iteration adds no comparable second axis and lies near P167/set-partition occupancy. |
| `C06 / TAN` | binary words; `(x_0,...,x_{n-1}) -> (x_1,...,x_{n-1},x_0 xor product_{i>0}x_i)`. | Exhaustive `2<=n<=16`.  States with at least two zeros undergo ordinary rotation; the all-one and one-zero states form one `(n+1)`-cycle.  The remaining cycle inventory is the primitive binary-necklace inventory with one length-`n` cycle removed. | **KILL_DIRECT_NFSR_CYCLE_JOINING.**  The literal is a nonsingular nonlinear feedback shift register, and its entire theorem is one elementary cycle join on the pure circulating register. |
| `C07 / CRP` | permutations of the `2^m` binary `m`-bit labels; stably sort by the current least significant bit, then rotate every label's bits one place right. | Exhaustive `m<=3` (40,320 permutations).  At time `t<=m`, image size is `((2^m/2^t)!)^(2^t)` and every nonempty time-`t` fibre is uniform; `T^m` is the identity ordering and the clock `m` is sharp. | **KILL_STANDARD_RADIX_CANONICALIZER.**  The exact tower is simply stable least-significant-digit radix sorting with a rotating coordinate convention. |
| `C08 / DCS` | pairs `(a,b)` of endomaps of `[n]`; simultaneously swap row entries `a(i),b(i)` exactly where the old square commutes, `a(b(i))=b(a(i))`, and the row entries differ. | Exhaustive `n<=4` (65,536 automata at `n=4`).  Periods already include 1, 2, 4, and 6, with branching fibres and no monotone statistic. | **KILL_ARTIFICIAL_NO_SPINE.**  The local commuting-square trigger does not produce a scalable decomposition or inverse grammar. |
| `C09 / CSS` | `S_n`; let `C` be the support of the 0-cycle and `k=abs(C)`.  Unless `C={0,...,k-1}`, conjugate by `(min([k] minus C), max(C minus [k]))`. | Exhaustive `n<=9`.  Depth is `abs(C minus [k])`, sharp `floor((n-1)/2)`; fixed targets of stratum `k` have basin polynomial `sum_r binom(k-1,r)binom(n-k,r)u^r`. | **KILL_CANONICAL_SELECTION.**  The update is selection-sort canonicalization of a support set; its proof is the occupied adaptive-normalization/labelled-subset engine near P174 and the sibling `SMP` scout. |
| `C10 / FDF` | one-line `S_n`; at the first descent `pi_i>pi_{i+1}`, remove `pi_{i+1}` and insert it at the front; fix the increasing permutation. | Exhaustive `n<=8`.  Unique recurrence at the identity; sharp clock `2^(n-1)-1`, unique deepest state `n,1,2,...,n-1`; target-local insertion fibres and global positive-fibre counts `n!/(k+1)!`. | **KILL_EXACT_EXTERNAL_OWNER.**  This is verbatim Project Euler's **First Sort** algorithm in Problems 523 and 524. |

## Funnel

```text
10 genuinely different literal maps
  2 theorem-complete mathematical spikes, both killed by decisive gates
  4 direct-owner or exact proof-transfer kills
  4 irregular, static, canonicalizer, or no-second-axis kills
  0 reserves
  0 promotions
```

The two theorem closures are retained only as falsification/provenance records.
They are not candidate papers.

