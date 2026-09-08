# Inversion-rank replacement scout — frozen owner kill

**Frozen verdict (2026-08-31 UTC): no promotion from this lane.**  The primary
map S01 is not merely close to prior work: it is exactly the operator of
Allagan--Gao--Testart, arXiv:2608.24476v1, submitted 2026-08-25.  That preprint
already owns the literal update, Catalan fixed points, finite stabilization, the
sharp `n-2` bound, and the identical extremal family.  S01 is therefore **KILL**.
The other twenty counted maps either collapse to standard encodings/algorithms or
show only cosmetic finite signals.  S07 and S16 are retained as controls but are
not counted.

The relative same-carrier decision is also frozen: the root Morris--Pratt
border-array reserve survives and S01 does not.  This says only that the root map
is literally different from the direct owner found here; it is **not** a novelty
certificate for the border-array map.

## Scope and exact pilot

The carrier is

\[
E_n=\{e=(e_0,\ldots,e_{n-1}):0\le e_i\le i\},\qquad |E_n|=n!.
\]

The verifier exhausts S01 through `n=8`, all 23 listed maps through `n=7`, and
the S01 sharp family through `n=12`.  It checks closure, complete functional
graphs, fixed points, image sizes, tails, periods, coordinate monotonicity,
no-pause behavior, and an independently generated noncrossing-partition model.
The frozen run has **793,652 assertions**.  The full audit census has SHA-256
`fc2320357944180847fe4c8c2a34b475f93d27b0c9aa4c4fd87f78fc7acd829a`.

- Verifier: `verify_inversion_rank.py`
- Exact stdout: `CANONICAL.txt`
- Counted literal systems: 21 = S01 plus 20 alternatives
- Non-counted controls: S07 (inequality dual) and S16 (proved identical to S14)
- Pairwise firewall: every counted map has a different truth table on `E_6`
- Promoted candidates: 0

## S01 / PR1: strict earlier-rank iteration

Define

\[
R(e)_i=\#\{j<i:e_j<e_i\}.
\]

### Independent rediscovery, retained only as an audit

The exact census is

| `n` | states | image | fixed | max tail | max period |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 0 | 1 |
| 2 | 2 | 2 | 2 | 0 | 1 |
| 3 | 6 | 5 | 5 | 1 | 1 |
| 4 | 24 | 15 | 14 | 2 | 1 |
| 5 | 120 | 53 | 42 | 3 | 1 |
| 6 | 720 | 217 | 132 | 4 | 1 |
| 7 | 5,040 | 1,014 | 429 | 5 | 1 |
| 8 | 40,320 | 5,335 | 1,430 | 6 | 1 |

The following all-parameter argument was obtained independently, but every
dynamical statement in it is zero-credit after the direct-owner hit.

1. **Inflation.**  If `e_i=k`, then `e_j<=j<k` for every `j<k`; hence the first
   `k` coordinates are all strictly below `k`, and `R(e)_i>=e_i`.

2. **No pause.**  Suppose coordinate `i` has value `k` and does not move in one
   round.  The number of earlier coordinates below `k` is then exactly `k`.
   Earlier coordinates can only increase, so that count can only decrease; the
   inflation bound forces it always to remain at least `k`.  It therefore remains
   exactly `k`, and this coordinate can never move later.

3. **Convergence and clock.**  A zero coordinate is fixed immediately.  Every
   positive coordinate strictly increases in each active round and is at most
   `i`, so the entire state is fixed by round `n-2`.  Thus every recurrent state
   is fixed and there are no nontrivial cycles.

4. **Sharpness.**  For `n>=2`,
   \[
   w_n=(0,1,2,\ldots,n-3,0,1)
   \]
   has final-coordinate trajectory `1,2,...,n-1` while its prefix is fixed.
   Its tail is exactly `n-2`.

5. **Endpoint class.**  If `pi` is a noncrossing partition of `[n]`, let
   `c_i=min(B_i)-1`, where `B_i` is the block containing `i`.  Then `R(c)=c`:
   the `min(B_i)-1` positions preceding the block minimum have lower labels, and
   a further lower label between the minimum and `i` would make a crossing.
   Conversely, in a fixed inversion sequence the first occurrence of a value
   `v` must be position `v+1`; a later first occurrence would supply either an
   extra value below `v` or an earlier copy of `v`.  Equal values therefore form
   blocks whose label is their minimum minus one.  A crossing would put an extra
   smaller block label after the relevant block minimum, contradicting the fixed
   equation.  Hence the fixed set is exactly the minimum-block codes of
   noncrossing partitions and has size `C_n`.

The verifier checks the last equivalence against an independent restricted-growth
generation of all set partitions through `n=8`.  This minimum-block description
is an alternative realization of the already-owned Catalan fixed set, not enough
for a new dynamics paper.  No clean non-iterative formula for the target
`R^(n-2)(e)` and no all-target fibre theorem emerged.

### Exact direct owner: terminal collision

[Allagan, Gao, and Testart, *Iterating the Lehmer code on inversion sequences:
Catalan fixed points and finite stabilization*, arXiv:2608.24476v1
(2026-08-25)](https://arxiv.org/abs/2608.24476) gives, verbatim in mathematical
content:

- the same operator `Theta(sigma)_i=#{j<i:sigma_j<sigma_i}` (Definition 2.3);
- its iteration on inversion sequences;
- a fixed-point characterization by `101` avoidance plus saturation, Catalan
  enumeration, and an explicit Dyck-path bijection;
- stabilization of every inversion sequence in at most `n-2` rounds;
- the identical sharp family `(0,1,2,...,n-3,0,1)` and its coordinate-by-coordinate
  trajectory;
- a one-step stabilization characterization by simultaneous `101`/`201`
  avoidance.

This is an exact literal-and-theorem collision, not a synonymous background
match.  The correct decision is unconditional **KILL**, even though the preprint
was only six days old at the time of this audit.

### Fishburn image signal: explicitly not a rescue

The image sizes

\[
1,2,5,15,53,217,1014,5335
\]

match the Fishburn numbers A022493 through `n=8`.  They do **not** show that
`Im(R)` is the ordinary ascent-sequence class: already

\[
(0,0,1)\stackrel R\longmapsto(0,0,2),
\]

and `(0,0,2)` violates the ordinary ascent bound.

There is also a strong owner-adjacent factorization.  Reverse-stably standardize
`e` by ranking the pairs `(e_i,-i)` and call the resulting permutation `rho(e)`.
For the positive-convention max-hat bijection `H` from inversion sequences to
permutations,

\[
R(e)_i+1=H^{-1}(\rho(e))_i.
\]

Indeed, an earlier position has lower rank under `rho(e)` exactly when its value
is strictly lower; earlier ties are deliberately ranked later.  The Burge
transpose of the word `e` is `rho(e)^{-1}`.  Thus the observed Fishburn sequence
sits immediately inside the existing standardization/max-hat/Burge framework.
We did not obtain a clean all-`n` image characterization or fibre formula, and
the numerical match is recorded as a finite signal only.  Even a later proof of
that single-step count would not recover the already-owned iteration package.

## Twenty-three-map audit

For each row, the finite assertion is the exact `(image, fixed, max tail, max
period)` census on all 5,040 states of `E_7`.  Complete censuses for every
`n=1,...,7` are in `CANONICAL.txt`.  “KILL” means stop: no parameter fitting or
cosmetic inequality variant was pursued after the first clear explanation.

| ID | Literal update | Exact assertion / early signal at `n=7` | Gate |
|---|---|---|---|
| S01 | strict earlier rank `#{j<i:e_j<e_i}` | `(1014,429,5,1)`; Catalan fixed, sharp `n-2` | **KILL — exact arXiv:2608.24476 owner** |
| S02 | first position carrying the current value | `(877,877,1,1)`; Bell idempotent image | KILL — standard minimum-block set-partition code |
| S03 | rank values by order of first appearance | `(877,877,1,1)`; Bell idempotent image | KILL — standard restricted-growth relabeling |
| S04 | number of prior equal entries | `(232,0,1,2)`; immediate 2-cycle behavior | KILL — occurrence counter toggle, no fixed geometry |
| S05 | number of distinct prior values strictly lower | `(999,877,3,1)`; Bell fixed set | KILL — support compression; no clean depth/image theorem |
| S06 | cumulative prefix descents | `(22,1,2,1)` | KILL — tiny cumulative-statistic closure |
| S07 | cumulative prefix ascents | `(64,64,1,1)` | **CONTROL, not counted** — inequality dual of S06 |
| S08 | cumulative strict records | `(64,64,1,1)`; `2^(n-1)` idempotent image | KILL — record-indicator encoding |
| S09 | prefix distinct count minus one | `(64,64,1,1)`; `2^(n-1)` idempotent image | KILL — support-size indicator encoding |
| S10 | root of `i` in the parent map `i -> e_i` | `(877,877,1,1)`; Bell idempotent image | KILL — ordinary rooted-forest component closure |
| S11 | depth of `i` in that parent map | `(877,0,9,8)`; cycles appear early | KILL — generic depth re-encoding, no stable theorem package |
| S12 | grandparent jump `e_i -> e_(e_i)` | `(1487,877,3,1)`; Bell fixed set | KILL — standard pointer jumping / path compression |
| S13 | number of earlier vertices in the same root component | `(232,0,3,2)` | KILL — S10 followed by S04-type occurrence counting |
| S14 | decode permutation, reverse its right Lehmer code | `(5040,48,0,2)`; bijective involution | KILL — standard reverse-complement symmetry |
| S15 | decode, invert the permutation, re-encode | `(5040,232,0,2)` | KILL — ordinary permutation inverse; fixed count is involutions |
| S16 | decode, reverse-complement, re-encode | `(5040,48,0,2)` | **CONTROL, not counted** — exactly identical to S14 |
| S17 | decode, square the permutation, re-encode | `(1890,1,2,4)` | KILL — group power map; generic cycle census |
| S18 | decode, stack-sort, re-encode | `(326,1,6,1)`; tail `n-1` | KILL — classical stack-sorting operator |
| S19 | decode, pop-stack-sort, re-encode | `(1653,1,6,1)`; tail `n-1` | KILL — classical pop-stack sorting |
| S20 | LIS-ending layer of the decoded permutation | `(877,0,4,2)`; Bell-sized image | KILL — patience/LIS layer recoding, no new inverse geometry |
| S21 | index of the preceding equal entry (zero if absent) | `(203,0,2,2)`; Bell `B_(n-1)` image | KILL — standard set-partition predecessor arcs |
| S22 | gap since the preceding equal entry minus one | `(203,1,6,1)`; Bell `B_(n-1)` image | KILL — recency encoding with cosmetic long tail |
| S23 | mex of the strict prefix | `(57,1,6,1)` | KILL — deterministic mex skeleton, no fibre/recurrent census |

The controls matter methodologically.  S07 prevents a descent/ascent sign change
from being counted as a new literal system.  S14 and S16 look different at the
code level but the verifier proves equality on the whole tested carrier; the
identity also follows from the definitions, so S16 is excluded from the count.

## Owner and value gate

The owner search was run on 2026-08-31 over the literal formula and the phrases
“earlier smaller”, “left-to-right Lehmer code”, “rank of an inversion sequence”,
“standardization”, “stabilization”, “Catalan fixed points”, and the max-hat/Burge
synonyms.  Primary-source conclusions:

1. **Direct owner.**  Allagan--Gao--Testart is a complete hit on S01 and its core
   theorem package.  No novelty inference remains available.
2. **Max-hat owner.**  [Cerbai, Claesson, and Sagan, *Modified difference ascent
   sequences and Fishburn structures*](https://arxiv.org/html/2406.12610)
   extends hat maps to inversion sequences and proves that max-hat bijects
   inversion sequences with permutations (Section 5.1).  This owns the principal
   code-conversion background used in the factorization above.
3. **Fixed-hat owner.**  [Cerbai, Claesson, and Sagan, *Self-modified difference
   ascent sequences*](https://arxiv.org/abs/2408.06959) studies fixed points of a
   different hat operator.  It is not the literal S01 owner, but makes generic
   “self-modified inversion/ascent sequence” positioning zero-credit.
4. **Fishburn/ascent owner.**  [Bousquet-Mélou, Claesson, Dukes, and Kitaev,
   *(2+2)-free posets, ascent sequences and pattern avoiding permutations*](https://arxiv.org/abs/0806.0666)
   owns ascent sequences and the Fishburn framework.  The Fishburn count cannot
   be presented as a new enumeration without a new literal-class theorem.
5. **Burge owner.**  [Cerbai and Claesson, *Transport of patterns by Burge
   transpose*](https://arxiv.org/abs/2005.07950) owns the reverse-stable sorting
   machinery on Cayley words and its Fishburn transport.
6. **Noncrossing/RGF background.**  [Lin and Fu, *On 1212-Avoiding Restricted
   Growth Functions*](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v24i1p53)
   records the standard natural bijection between noncrossing partitions and
   `1212`-avoiding RGFs.  Our minimum-block code is a different presentation, but
   it does not create a new dynamical result after the exact S01 owner.

The sequence label A022493 was used only to identify the finite image counts; an
OEIS match is not treated as theorem ownership or proof.

## Portfolio collision firewall

- **P105:** its carrier is permutations and its mechanism is cycle-minimum
  pruning.  S14--S19 enter permutation-code territory and were killed rather
  than repackaged as a new inversion-sequence lane.
- **P110:** it already uses a partition normal form and a sharp `n-2` clock.
  S01's noncrossing endpoint and clock silhouette would need stronger literal
  novelty even without the direct owner.
- **P117:** odd-run reversal is literally separate; no useful theorem is imported
  from its binary run structure.
- **P122:** record-block reversal already owns a sharp-depth/image/fibre package.
  S01 has no all-target fibres and its image class remains unresolved here.
- **P126:** balanced composition refinement already owns kernel/image/every-fibre
  packaging.  None of the rank maps here supplies a comparable inverse theorem.
- **P131:** the Euclidean quotient queue already has a sharp linear clock.  A
  bare `n-2` extremal time is therefore zero portfolio value even before owner
  checking.

## Direct same-carrier pairwise verdict

The root border-array candidate has, in the root audit, explicit `n-1` two-cycles,
sharp maximum tail `2n-4`, and two unique maximum fibres of size `(n-1)!`, checked
over 409,113 states with 868,745 assertions.  S01 has the conceptually attractive
noncrossing/Catalan endpoint class and a clean coordinate Lyapunov argument, but
those exact dynamics and its sharp witness are already owned.

**Selection: root Morris--Pratt border-array reserve > S01.  Do not retain both.**
The reason is decisive literal ownership, not a claim that an owner search failed
for the root map.  The border-array reserve must still pass its own owner gate;
it merely remains the only same-carrier option after this lane's direct hit.

## Frozen handoff

- S01 / PR1: **KILL (exact direct owner)**
- S02--S06, S08--S15, S17--S23: **KILL**
- S07, S16: **non-counted controls**
- Candidate promotions: **none**
- Recommended portfolio action: retain the root border-array map as the sole
  same-carrier reserve, subject to its independent owner/value gate
- No paper number assigned; no Git operation performed
