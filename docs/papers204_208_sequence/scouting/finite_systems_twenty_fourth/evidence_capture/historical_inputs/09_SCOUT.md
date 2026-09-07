# Word/permutation/combinatorial breadth scout — P162–P166

**Date:** 2026-09-02 UTC  
**Portfolio boundary audited:** P1–P161 plus the live P162–P166 scout lanes  
**External status:** `HOLD_EXTERNAL`  
**Outcome:** `EMPTY_POOL`  
**Literal systems exact-tested:** 18

## Bottom line

No system in this lane clears both gates: (i) a clean all-parameter temporal
theorem and (ii) an independent every-target fibre/image/extremal theorem,
after direct owners and internal proof-engine transfer are subtracted.

The two strongest raw signals were `DAE` (Dyck area-sequence erosion) and
`LCD` (Lehmer-coordinate countdown).  Both have exact iterates, sharp global
height, complete images, and every-target weighted fibres.  They are still
**killed**, not reserved:

- their temporal engine is coordinatewise truncation;
- their paper silhouette is exactly the P160 `RCS` silhouette: truncation
  iterate, maximum-coordinate clock, sharp family height, image criterion,
  and every-target inverse generating function;
- `LCD` also meets the same-batch killed Lucas digit truncation (`AA04/LDT`),
  and a 2026 Lehmer-iteration preprint creates a serious topical owner risk;
- `DAE` adds a non-product transfer matrix, but this does not replace the
  occupied truncation engine.  Its Dyck carrier also forces subtraction of
  P144's Catalan/Dyck interfaces.

Thus this directory records two useful **near-miss theorem contracts**, but
zero survivors and no paper recommendation.

## Historical firewall actually applied

The audit started from the P1–P156 occupancy table and the P157–P161 kill
ledger.  In particular, this scout did not admit generic selectors or
standardized subword extractors, generic reversal/closure/refinement,
comparator sorting, or cosmetic instances of these occupied engines:

- P134 whole-array border recomputation;
- P139 Lyndon-factor-start feedback;
- P147 adjacent-run consolidation;
- P149 endpoint-peak extraction;
- P155 cycle-maximum extraction;
- P156 weak-excedance extraction.

Previously killed pop-stack, pancake, parking-delete-first-one, singleton
erasure, leftmost-`10` bubbling, square deletion, composition subtraction,
primitive-Dyck cutting, and tree-suppression candidates were not re-entered.
Named classical maps below are negative controls, not attempted renamings.

## Eighteen-system exact decision ledger

| ID | literal finite system | exact small signal | all-parameter theorem spine attempted | owner/internal collision | decision |
|---|---|---|---|---|---|
| `LCD` | encode `pi in S_n` by its Lehmer digits `c_i`; replace every digit by `(c_i-1)_+`; decode | at `n=8`, image sizes `40320,5040,720,120,24,6,2,1`; at `t=2` fibre range `6..1458` | `c_i(t)=(c_i-t)_+`; clock `max c_i`; image `(n-t)!`; exact inversion-weighted every-target product | P160 RCS truncation silhouette; same-batch `AA04/LDT`; Allagan–Gao–Testart 2026 topical collision | **`KILL_P160_COORDINATE_TRUNCATION`** |
| `LHF` | Lehmer digits `c_i -> floor(c_i/2)` and decode | `n=8` image sizes `40320,576,16,1` | `c_i(t)=floor(c_i/2^t)`; logarithmic clock; interval-product fibres | cosmetic coordinate-code variant of `LCD`; same P160/LDT engine | `KILL_DUPLICATE_COORDINATE_CODE` |
| `DAE` | Dyck area sequence `a=(0,a_2,...,a_n)` with `a_{i+1}<=a_i+1`; set `a_i -> (a_i-1)_+` | at `n=9`, images `4862,1430,429,132,42,14,5,2,1`; sharp height `8` | `a_i(t)=(a_i-t)_+`; clock `max a_i`; time-`t` image `(UD)^t D_{n-t}` of size `C_{n-t}`; every-target area-GF by a finite transfer matrix | exact P160 truncation/clock/fibre silhouette; P144 owns Dyck/Catalan interfaces | **`KILL_P160_PROOF_ENGINE`** |
| `MHE` | Motzkin height profile `h_0=h_n=0`, adjacent difference at most one; set `h_i -> (h_i-1)_+` | length 10 images through `t=5`: `2188,323,51,9,2,1` | exact truncation, maximum-height clock, every-target weighted walk DP | same proof as `DAE`, hence also P160 truncation transfer | `KILL_DUPLICATE_HEIGHT_EROSION` |
| `SST` | West/Knuth deterministic stack-sort, recursively `S(L n R)=S(L)S(R)n` | on `S_8`, image 1780, fibre range `2..1430`; sharp tail 7 with 720 maximizers | universal `n-1` sorting bound is clean; arbitrary target fibres are the difficult classical fertility problem | direct, heavily developed stack-sorting owner; adjacency to previously killed pop-stack lane | `KILL_DIRECT_OWNER` |
| `DUC` | cyclic absolute-difference map on `{0,1,2}^5` | image 91; two 15-cycles plus zero fixed point; maximum tail 4; fibres `2,3,4,8` | eventual periodicity follows from bounded maximum, but no sharp uniform period/tail/fibre atlas emerged | classical Ducci sequence and period literature directly owns the system | `KILL_DIRECT_OWNER_UNSTABLE` |
| `PHM` | a length-4 word over `Z/4Z` maps to its four letter-counts modulo 4 | image 32; three fixed points; maximum tail 3; fibre sizes `4,6,12,24` | no clean all-parameter functional graph law across `(q,n)` | Parikh-vector transform is classical; small signature is irregular and theorem-thin | `KILL_NO_SPINE` |
| `VVT` | a balanced binary bridge rotates after its first global prefix minimum | semilength 5: Catalan image 42; idempotent; fibre sizes `2,4,6,8,10` | cycle lemma gives image and periodicity-sensitive rotation fibres, but only one-step normalization | Vervaat/cycle-lemma canonicalization is direct; repeats a previously killed rotation-normalizer silhouette | `KILL_DIRECT_OWNER_IDEMPOTENT` |
| `ROW` | rowmotion on order ideals of `[2] x [3]` | 10 ideals split into two 5-cycles; singleton fibres | on `[r] x [s]`, period `r+s`; inverse axis is trivial because the map is bijective | classical rowmotion/toggle-group theorem | `KILL_DIRECT_OWNER_THIN_FIBRES` |
| `CPD` | for a permutation word, output the permutation `x -> cyclic predecessor of x` | `n=7`: first image 720 with uniform fibre 7; eventual cycles have lengths `1,7,14,35,49`; max tail 9 | first image is exactly all `n`-cycles, but iteration becomes `f -> f r f^{-1}` and no clean all-`n` clock/fibre theorem emerged | first step is the last column of the Burrows–Wheeler rotation matrix for distinct letters | `KILL_BWT_OWNER_AND_NO_SPINE` |
| `FTF` | write a permutation in canonical cycle form, erase parentheses (Foata fundamental transformation) | on `S_7`, bijective with 21 fixed points and cycle lengths up to 963 | no monotone clock; fibres singleton; cycle spectrum is already highly irregular | direct Foata owner | `KILL_DIRECT_OWNER_BIJECTION` |
| `LXS` | cyclic lexicographic successor on `S_n` | `S_7` is one cycle of length 5040 | exact period `n!`, but no independent target axis | standard enumeration algorithm; dynamics is tautological | `KILL_TAUTOLOGICAL_CYCLE` |
| `PIN` | permutation inversion `pi -> pi^{-1}` | on `S_7`, 232 fixed points and 2404 two-cycles | exact involution; every fibre singleton | classical group involution; below the two-axis threshold | `KILL_THIN_INVOLUTION` |
| `ITS` | left-to-right sweep of legal vertex toggles on independent sets of path `P_n` | `P_8`: 55 states in cycles of lengths `3,9,13,13,17` | bijective Coxeter-element dynamics; singleton fibres | Joseph–Roby directly study this literal path independent-set toggle system and its orbit structure | `KILL_DIRECT_OWNER` |
| `PFN` | for `w in {0,...,n}^n`, take the unique uniform residue shift that is a parking function | `n=4`: image 125, every fibre 5, and idempotence | image `(n+1)^(n-1)` and uniform fibre `n+1`; temporal part stops after one step | Pollak circular parking proof directly supplies the orbit representative and count | `KILL_DIRECT_OWNER_IDEMPOTENT` |
| `BRG` | successor in binary-reflected Gray order on `{0,1}^n` | at `n=8`, one cycle of length 256 | exact period `2^n`; every fibre singleton | classical Gray enumeration; tautological schedule | `KILL_TAUTOLOGICAL_CYCLE` |
| `SPR` | Schützenberger promotion on standard tableaux of rectangular shape `2 x 3` | five tableaux split into a 2-cycle and a 3-cycle | rectangular promotion has a classical finite-order theory; fibres singleton | direct jeu-de-taquin/promotion owner | `KILL_DIRECT_OWNER_BIJECTION` |
| `RKC` | RSK-insert a permutation and output the bottom-to-top row word of its insertion tableau | on `S_7`, idempotent image 232; fibre sizes `1,6,14,15,20,21,35` | image is one canonical word per SYT; fibre is the number of recording tableaux of the shape; temporal depth one | direct RSK/Knuth-class canonicalization and only a one-step retraction | `KILL_DIRECT_OWNER_SHALLOW` |

The two coordinate-code entries and the two height-profile entries were kept
as explicit mutation controls.  Even if each such pair is conservatively
counted as one mechanism rather than two systems, the scout still contains
16 mutually different literal mechanisms, exceeding the requested breadth.

## Focused near-miss contract A — `DAE` (killed)

Let `A_n` be the area sequences of Dyck paths of semilength `n`:

```text
a_1=0,  0 <= a_(i+1) <= a_i+1.
```

Define `E(a)_i=(a_i-1)_+`.  For every `t>=0`,

```text
E^t(a)_i=(a_i-t)_+,
tau(a)=max_i a_i,
max_(a in A_n) tau(a)=n-1.
```

The time-`t` image for `0<=t<=n-1` is exactly the set of area sequences
whose first `t+1` entries are zero.  In path language these are

```text
(UD)^t D,  where D is any Dyck path of semilength n-t.
```

Hence the image has cardinality

```text
C_(n-t) = 1/(n-t+1) binom(2(n-t),n-t),
```

and for `t>=n-1` the image is the single zigzag path.

For an arbitrary target `b`, set, in one-based indexing,

```text
S_i(b,t) = {b_i+t}                    if b_i>0,
           {0,...,min(t,i-1)}         if b_i=0.
```

Its complete area-weighted fibre is

```text
F_(b,t)(q)
 = sum q^(a_1+...+a_n),
```

where the sum is over `a_1=0`, `a_i in S_i(b,t)`, and
`a_(i+1)<=a_i+1`.  This is an explicit finite transfer product: at step `i`
use matrix entry

```text
K_i(x,y)=1[y in S_(i+1)(b,t)] 1[y<=x+1] q^y.
```

The fibre is nonempty exactly for the stated time-`t` image.  A constructive
witness takes `a_i=i-1` through `i=t+1`, then takes `a_i=t` at later zero
target coordinates and `a_i=b_i+t` at positive target coordinates.

This contract has two real theorem axes, including every target and all
boundaries.  It is nevertheless `KILL_P160_PROOF_ENGINE`: P160 already turns
literal coordinate truncation into the same clock/image/every-target paper
architecture.  Replacing independent Ferrers boundaries by an adjacency
transfer matrix is insufficient proof-engine separation.

## Focused near-miss contract B — `LCD` (killed)

For `pi in S_n`, let `c_i(pi)` be its standard right-inversion Lehmer digit,
so `0<=c_i<=d_i=n-i`.  Define `L(pi)` by decoding
`(c_i(pi)-1)_+`.  Then

```text
c_i(L^t(pi))=(c_i(pi)-t)_+,
tau(pi)=max_i c_i(pi),
max_(pi in S_n) tau(pi)=n-1.
```

For `0<=t<=n-1`,

```text
|image(L^t)|=(n-t)!.
```

A target with digits `b_i` lies in the image exactly when every positive
digit satisfies `b_i+t<=d_i`.  Its full inversion-weighted source polynomial
is

```text
prod_(b_i>0) q^(b_i+t)
prod_(b_i=0) (1+q+...+q^min(t,d_i)).
```

Consequently its ordinary fibre size is

```text
prod_(b_i=0) (min(t,d_i)+1).
```

At time `t`, the minimum supported fibre is `(t+1)!`; the maximum is
`t! (t+1)^(n-t)`, attained by the identity.  At `t=0` both are one; at
`t=n-1` both are `n!`.

This is exact but receives no reserve: it is an especially transparent
coordinate-box version of P160's truncation engine, and its literature label
is now unusually dangerous because Allagan–Gao–Testart (arXiv:2608.24476)
study a different iteration explicitly titled *Iterating the Lehmer code*.
Their operator is not this countdown map, but the topical collision plus the
internal proof transfer makes the gate decisively negative.

## Exact evidence

The verifier is self-contained and imports no paper or prior scout code.  It
exhausts all permutations in `S_8` for both Lehmer maps, all 4,862 Dyck area
sequences of semilength nine, all 2,188 Motzkin profiles of length ten, all
permutations in `S_8` for stack-sort tails, and the complete finite carriers
declared for the remaining controls.  It checks every reached target fibre,
not sampled targets, for `LCD`, `LHF`, `DAE`, and `MHE`.

Run:

```text
python3 docs/papers162_166_sequence/scouting/word_combinatorial/verify_scout.py
```

The canonical run contains **832,353 assertions** and ends in `STATUS PASS`.
Two fresh runs had byte-identical stdout SHA-256
`070f169017be376d2bf028f1345e408629cefbc8addbc65257e3b1fe4acf0b6b`.
Enumeration is falsification pressure, not proof and not an owner-absence
claim.

## Final gate

`EMPTY_POOL / HOLD_EXTERNAL`.

The ranked near misses are `DAE > LCD`, but neither exceeds the live P160 RCS
package after proof-engine subtraction.  No paper should be started from this
lane without a new literal mechanism and a fresh owner gate.
