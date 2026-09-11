# Focused idea ledger — non-extractive permutation/word/matching dynamics

**Scope:** 18 genuinely different finite autonomous maps.  No deletion,
pruning, coordinate extraction, or parity-linear update is used.  The three
within-carrier families have all 45 pairwise literal differences witnessed by
exact states in `breadth2.py`.

**Exact boxes:** every permutation in `S_n`, `2<=n<=8`; every binary word
through length 10 and ternary word through length 7; every labelled perfect
matching with at most six edges.  Enumeration is falsification evidence, not
proof or novelty evidence.

| handle | carrier and literal update | earliest exact progress/signal | decision |
|---|---|---|---|
| `A01_VIS` | `S_n`; replace `pi_i` by its stable rank among `pi_j+j` | `Inv(F(pi))` is a strict subset of `Inv(pi)` off identity, proving unique identity recurrence; identity fibre is exactly `2^(n-1)`.  `S_8`: image 4,451, tail 5, max fibre 128.  Sharp clock/other target fibres remain open. | `KILL_UNCLOSED_CLOCK_SCORE_RERANK` |
| `A02_NPR` | `S_n`; stable-rank cyclic neighbour products `pi_i pi_(i+1)` | one recurrent `2n`-cycle for every tested `3<=n<=8`; `S_8` tail 13 and max fibre 33.  This repeats the attractive-but-branching adjacent-score silhouette without an atlas. | `KILL_ASR_LIKE_NO_ATLAS` |
| `A03_SPR` | `S_n`; stable-rank `value + position(successor value)` | `S_8` already has periods `1,2,3,4,5,6,9,10,12,15,26` and tail 96.  Exact richness falsifies a compact period conjecture. | `KILL_CHAOTIC_SCORE_RERANK` |
| `A04_IGR` | `S_n`; replace each position by the stable rank of its inversion-graph degree | only fixed points and two-cycles through `S_8`, where tail is 12 and max fibre 574; however fixed/tail sequences do not close and degree-score reranking approaches P112. | `KILL_SCORE_RERANK_NEAR_P112` |
| `A05_CTR` | `S_n`; stable-rank the range of each cyclic length-three window | `S_8` has periods `15,16,19,63`, tail 112, and no fixed state; small data destroy any uniform short-period claim. | `KILL_CHAOTIC_SCORE_RERANK` |
| `A06_SDR` | `S_n`; stable-rank the positional distance from each value to its cyclic successor value | `S_8` has periods `1,2,3,8,33`, tail 40, image 3,117, max fibre 184.  No monotone statistic or target grammar emerged. | `KILL_NO_SPINE` |
| `B01_FFR` | fixed-length `q`-ary words; globally rename letters by `(frequency, first occurrence, old label)` | depth-one retraction; at `q=3,n=7` it has 365 fixed images and maximum fibre 6.  Exact canonicalization, no temporal axis. | `KILL_CANONICALISER_THIN` |
| `B02_RSS` | fixed-length words; sort maximal linear runs by `(length, letter, old position)` | converges in every exact box; binary `n=10` has 31 fixed states, tail 4, max fibre 84.  Sorting run compositions is owner-heavy and no independent fibre closed. | `KILL_RUN_SORT_ENGINE` |
| `B03_LRS` | fixed-length words; exchange the leftmost longest run with its cyclic successor run | binary `n=10` has fixed/two-periodic core and tail 7; ternary `n=7` already has periods `1,2,6,10` and tail 9.  This is an occupied run/composition mechanism with no general atlas. | `KILL_RUN_ENGINE` |
| `B04_FCR` | binary words; rotate by the global multiplicity of the current first bit | proved pointed-necklace `+/-k` component decomposition, complete period inventory, sharp tail `n-2`, exactly two deepest states, every-target `0/1/2` fibres, and fixed-point Möbius census; independently exhaustive through `n=18`. | **`AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL`** |
| `B05_BGS` | fixed-length words; order positions by `(current letter, cyclic next letter, position)` and read the letters | primary key makes the output the globally sorted content word, hence a depth-one retraction.  Binary `n=10`: 11 images, max fibre 252. | `KILL_SORT_RETRACTION` |
| `B06_OLS` | fixed-length words; order positions by `(occurrence number of its letter, letter, position)` | occurrence layers give a distinct depth-one canonicalizer; explicit witness differs from `B05`.  Ternary `n=7`: 36 images and max fibre 210. | `KILL_RETRACTION_THIN` |
| `C01_MOC` | perfect matchings; orient edges low/high, sort by lows, pair low `i` to high `i+1` cyclically | at six edges: tail 5, 120 six-cycles, recurrent count 720, image 3,840, max fibre 5.  RGF encoding proves it is reverse-direction P169 successor transfer restricted to pair partitions. | `KILL_INTERNAL_P169_PAIR_SLICE` |
| `C02_SOC` | perfect matchings; perform the same cyclic low/high cross after sorting edges by `(sum,length,endpoints)` | six edges: periods `2,4,6`, tail 26, image 2,305, max fibre 32.  Edge order changes under iteration and no clock/inverse closes. | `KILL_NO_SPINE` |
| `C03_LEW` | perfect matchings; length-sort edges, list lows forward and highs backward, pair consecutive endpoints | apart from the one-edge boundary, only two-cycles are recurrent in the tested range; six edges have tail 8 and max fibre 52 with no stable formula. | `KILL_MATCHING_REWIRE_THIN` |
| `C04_ESR` | perfect matchings; relabel vertices stably by endpoint sum | exact depth-one retraction; at six edges the image/fixed set has 32 matchings and max fibre 3,736. | `KILL_SCORE_RETRACTION` |
| `C05_EDR` | perfect matchings; relabel vertices stably by edge length | converges to 11 fixed states at six edges, with tail 3, image 57, max fibre 3,871.  Short reranking without an inverse grammar. | `KILL_MATCHING_RERANK_THIN` |
| `C06_CDR` | perfect matchings; relabel by `(crossing degree, lower/upper endpoint side)` | six edges produce 16 fixed states plus periods 2 and 3, tail 5, image 375, max fibre 458.  Exact irregularity replaces, rather than supports, a parameter theorem. | `KILL_MATCHING_RERANK_NO_SPINE` |

## Decision count

```text
18 distinct literal systems
17 KILL
1 AMBER_INTERNAL_NEAR_P166
0 GREEN
HOLD_EXTERNAL
```

The sole amber entry is not an allocation.  Its strict kill switch and all
zero-credit overlap are recorded in `COLLISION_FIREWALL.md` and
`OWNER_SEARCH_LOG.md`.
