# Post-collision combinatorial replacement scout

**Date:** 2026-09-02 UTC  
**Trigger:** both LCP and PAE failed the focused collision gate  
**Systems:** 12 genuinely different finite dynamics  
**Forbidden families avoided at intake:** selector/extraction maps, tree
pruning/contraction, partition refinement, and random deletion  
**External state:** `HOLD_EXTERNAL`  
**Allocation:** no paper number and no manuscript

## Outcome

All twelve alternatives are killed.  This is a useful negative result rather
than a failed quota: every weak or owned signal is stopped at Stage 1.

The strongest raw signal was `TLS`, a cyclic Temperley--Lieb sweep on
noncrossing matchings.  It has a complete theorem package---one-step retraction,
a rotation core, and an every-target fibre law.  It still fails the portfolio
gate because its fibre is exactly P144's primitive-Dyck-component fibre after a
fixed rotation, while its remaining core is the classical link-pattern
rotation under owned Temperley--Lieb generators.  `DFG` has an attractive
linear maximum-period pattern but is exactly the path-independent-set Coxeter
toggle dynamics already studied by Joseph--Roby.  The other ten are direct
actions, arbitrary schedulers, classical symmetries, or have no second exact
axis.

```text
paper-sized survivors = 0
strongest killed theorem = TLS
next combinatorial action = leave TL/toggle/Dyck-fibre/classical-transform
                            territory rather than refine these systems
```

Exact replay is in `verify_replacement_scout.py`; its frozen stdout is
`REPLACEMENT_CANONICAL.txt`.

## Decision ledger

| rank | handle | carrier | literal update | exact signal | verdict |
|---:|---|---|---|---|---|
| 1 | `TLS` | noncrossing perfect matchings | apply cyclic TL generators `e_0,e_1,...,e_(2n-1)` | image `Cat_(n-1)`, rotation core, target indegree `1+returns` | `KILL_P130_P144_TRANSFER` |
| 2 | `DFG` | domino tilings of a `2 x n` rectangle | flip all even faces, then all odd faces | bijective; observed max period `3n-10` for `n>=5` through 20 | `KILL_DIRECT_OWNER` |
| 3 | `MVT` | Markoff triples over `F_p` | `(x,y,z)->(y,z,3yz-x)` | rich prime-dependent cycle spectra | `KILL_DIRECT_VIETA_ACTION` |
| 4 | `HWT` | reduced transposition factorizations of an `n`-cycle | full Hurwitz braid sweep | `n^(n-2)` states; max periods `n(n-1)` at `n=4,5,6` | `KILL_DIRECT_HURWITZ` |
| 5 | `NFR` | ordered pairs in a finite group | `(x,y)->(y,xy)` | nonabelian periods `1,3,8,18` on `S_1,...,S_4` | `KILL_NIELSEN_ACTION` |
| 6 | `RAC` | fixed-width ternary words | reverse digits, add with carry modulo `3^n` | exact image pattern; erratic tails and periods | `KILL_NO_SECOND_AXIS` |
| 7 | `CRW` | reduced words of the longest permutation | leftmost lex-decreasing Coxeter relation | fixed counts `1,1,3,20`; max tails `0,1,4,12` | `KILL_SCHEDULER_AND_WORD_GRAPH` |
| 8 | `BWT` | permutations as distinct-letter words | pure Burrows--Wheeler last column | uniform cyclic fibre `n`; irregular iterates | `KILL_DIRECT_MAP` |
| 9 | `PPR` | plane partitions / ideals of three-chain boxes | rowmotion | small-box periods equal displayed rank sum | `KILL_DIRECT_ROWMOTION` |
| 10 | `LPS` | Latin squares | swap row and symbol coordinates | involution; fixed counts `1,2,6,96` through order four | `KILL_PARASTROPHE_SYMMETRY` |
| 11 | `FPG` | incident point--line flags in `PG(2,q)` | standard polarity `(P,L)->(L,P)` | involution; `q+1` absolute fixed flags | `KILL_POLARITY_SYMMETRY` |
| 12 | `PTR` | convex-polygon triangulations | rotate all vertex labels once | Catalan carrier and classical rotation periods | `KILL_GROUP_ACTION_P146_CARRIER` |

## 1. `TLS`: cyclic Temperley--Lieb boundary sweep

- **Carrier.** Noncrossing perfect matchings of `0,...,2n-1` around a circle.
  Its size is `Cat_n`.
- **Local update.** The generator `e_i` pairs `i` with `i+1` modulo `2n`.
  If they were paired to `a,b`, reconnect `a` with `b`; if already paired,
  do nothing.  Apply `e_0,e_1,...,e_(2n-1)` sequentially.
- **Exact signature.** For `n=1,...,9`, state counts are
  `1,2,5,14,42,132,429,1430,4862`; image counts are
  `1,1,2,5,14,42,132,429,1430`; maximum target fibres are
  `1,2,...,9`.  Maximum recurrent periods are
  `1,1,1,3,4,5,6,7,8`.

### Candidate sharp theorem

The image is exactly the matchings containing the boundary arc
`{0,2n-1}`.  Delete this arc and subtract one from the other labels.  On that
image, one further sweep is rotation by `-2` on the resulting noncrossing
matching of `2n-2` points.  Hence every state enters the recurrent core in at
most one step, and the core cycle census is the rotation census on
`NC_2(n-1)`.

**Proof sketch.** The final generator forces the boundary arc, so the image is
contained in the stated set.  Starting with that arc, successively applying
`e_0,e_1,...` propagates the exposed boundary strand two sites around the
circle; induction on the generator index shows that after the last generator
the outer arc is restored and every interior endpoint has moved by `-2`.
Rotation is bijective, so every boundary-arc state already has a predecessor
inside the set, proving equality of the image.

### Independent fibre theorem---and the fatal collision

For a target `U` in the image, delete its boundary arc, rotate the interior
matching by `+1`, write the corresponding Dyck word as a concatenation of `r`
primitive components, and then

```text
|TLS^(-1)(U)|=r+1.
```

In reverse sweep order, noncrossing forces the moving strand through the
interior of a primitive component; branching is possible only at a return to
height zero.  The `r` returns plus the option not to enter a component give the
`r+1` mutually exclusive predecessors.  Conversely each cut between primitive
components reconstructs one predecessor, so there is no overcount.

Putting `k=n-1`, the number of targets of indegree `r+1` is

```text
r/k binom(2k-r-1,k-1),       1<=r<=k,
```

because a Dyck word with `r` components is a sequence of `r` primitive Dyck
words.  Thus the unique maximum fibre is `n`.

This theorem is not a residual.  P144 proves the same `r+1` target fibre, the
same primitive-component cut inverse, the same ballot distribution, and the
same unique maximum.  P130 already occupies a retraction from matchings to a
noncrossing core with target-local fibres.  After those subtractions, the only
remaining axis is a word in classical cyclic Temperley--Lieb generators acting
as classical rotation.  **Verdict: `KILL_P130_P144_TRANSFER`.**

## 2. `DFG`: checkerboard domino face gyration

- **Carrier.** Domino tilings of a `2 x n` rectangle, encoded by independent
  sets of the path on `n-1` possible horizontal `2 x 2` blocks.
- **Update.** Toggle all legal even-starting blocks simultaneously, then all
  legal odd-starting blocks.  Each half-step is an involution.
- **Signature.** Maximum periods for widths `1,...,20` are
  `1,2,3,3,5,8,11,14,17,20,23,26,29,32,35,38,41,44,47,50`; hence
  `3n-10` from width five through the tested frontier.
- **Candidate theorem.** Classify every orbit and prove the sharp maximum,
  with a second homomesy/cycle-index axis.
- **Collision.** Under the independent-set encoding, this is exactly a
  Coxeter element in the toggle group of a path.  Joseph--Roby directly study
  that system, including nontrivial orbit sizes and homomesy.  Relabeling it as
  domino faces contributes nothing.  **Verdict: `KILL_DIRECT_OWNER`.**

## 3. `MVT`: Markoff--Vieta rotor over finite fields

- **Carrier.** Solutions of `x^2+y^2+z^2=3xyz` in `F_p^3`.
- **Update.** `(x,y,z)->(y,z,3yz-x)`.
- **Signature.** At primes `3,5,7,11,13,17,19`, carrier sizes are
  `9,41,29,89,209,341,305` and maximum periods are
  `6,30,15,18,78,138,120`.
- **Candidate theorem.** Resolve the cycle lengths of this fixed Vieta word,
  refined by exceptional/generating-pair strata; an independent axis would be
  an exact component or largest-orbit theorem.
- **Collision.** The rule is a coordinate cycle composed with a standard
  Vieta involution.  Markoff-surface modular-group actions, their finite-field
  orbits, and the Nielsen interpretation are direct literature objects; even
  the large-orbit questions remain active.  A deterministic word in those
  generators is not a fresh local system without a new solved invariant.
  **Verdict: `KILL_DIRECT_VIETA_ACTION`.**

## 4. `HWT`: Hurwitz sweep on reduced transposition factorizations

- **Carrier.** Length `n-1` transposition factorizations of a fixed `n`-cycle.
- **Update.** Apply the Hurwitz moves at adjacent positions from left to right.
- **Signature.** For `n=2,...,6`, state counts are
  `1,3,16,125,1296=n^(n-2)` and maximum periods are `1,3,12,20,30`.
- **Candidate theorem.** A full sweep to the power `n-1` is simultaneous
  conjugation by the product cycle, so its order divides `n(n-1)`; prove
  attainment and the exact cycle census.
- **Second axis.** Refine cycles by the associated labelled tree/factorization
  statistic.
- **Collision.** The carrier, local moves, transitivity, and Coxeter-element
  factorization count all belong directly to Hurwitz-action theory.  The power
  identity is the standard full-twist identity.  **Verdict:
  `KILL_DIRECT_HURWITZ`.**

## 5. `NFR`: Nielsen--Fibonacci group-pair dynamics

- **Carrier.** `G x G` for a finite group `G`.
- **Update.** `(x,y)->(y,xy)`, a bijection induced by a free-group Nielsen
  automorphism.
- **Signature.** On `S_1,S_2,S_3,S_4` the state counts are
  `1,4,36,576` and maximum periods are `1,3,8,18`.
- **Candidate theorem.** In the abelian case the Fibonacci matrix controls all
  periods; in the nonabelian case refine the census by the commutator class,
  which is preserved up to inversion/conjugacy.
- **Second axis.** Exact orbit counts on a family of finite groups.
- **Collision.** The map is literally evaluation of a named Nielsen
  automorphism.  Abelian results reduce to generic finite linear dynamics and
  the nonabelian experiment has no closed second theorem.  **Verdict:
  `KILL_NIELSEN_ACTION`.**

## 6. `RAC`: ternary reverse-and-add carry transducer

- **Carrier.** Width-`n` ternary words, interpreted modulo `3^n` with leading
  zeros retained.
- **Update.** Add the digit reversal to the word, including ordinary carries,
  and reduce modulo `3^n`.
- **Signature.** For widths `1,...,8`, image sizes are
  `3,5,15,25,75,125,375,625`; maximum tails are
  `0,1,7,6,28,17,25,42`; maximum periods are
  `2,4,8,18,12,27,27,19`.
- **Candidate theorem.** The image pattern suggests
  `5^(n/2)` for even width and `3*5^((n-1)/2)` for odd width, approachable by a
  carry automaton.
- **Second axis.** No temporal or target-resolved law survives the pilot: both
  tails and periods are irregular, and generic finite-state spectra are
  excluded.  **Verdict: `KILL_NO_SECOND_AXIS`.**

## 7. `CRW`: oriented Coxeter-relation descent on reduced words

- **Carrier.** Reduced words of the longest element `w_0 in S_n`.
- **Update.** Find the leftmost commuting or long-braid relation whose
  application lexicographically lowers the word, and apply the lexicographically
  least such move; otherwise fix the word.
- **Signature.** For degrees `2,...,5`, state counts are `1,2,16,768`, fixed
  counts `1,1,3,20`, and maximum tails `0,1,4,12`.
- **Candidate theorem.** Classify local normal forms and the sharp greedy
  distance, with target basin sizes as a second axis.
- **Collision.** Matsumoto connectivity, reduced-word commutation/braid graphs,
  and their diameters are directly studied.  The chosen orientation creates
  multiple local sinks and the residual is an arbitrary scheduler on an owned
  word graph, precisely the kind of scheduling-only result rejected elsewhere
  in the portfolio.  **Verdict: `KILL_SCHEDULER_AND_WORD_GRAPH`.**

## 8. `BWT`: pure Burrows--Wheeler iteration

- **Carrier.** Permutations of `0,...,n-1`, viewed as distinct-letter words.
- **Update.** Sort all cyclic rotations lexicographically and take the last
  column.
- **Signature.** Image sizes through rank eight are
  `1,1,2,6,24,120,720,5040=(n-1)!`; every nonempty fibre has size `n`.
  Maximum tails are `0,1,2,2,3,3,9,54`, while maximum periods are
  `1,1,1,4,5,33,49,16`.
- **Candidate theorem.** The one-step quotient is exact because BWT is constant
  on the `n` cyclic rotations and reconstructs their necklace.
- **Second axis.** Iteration is already irregular by rank seven and no sharp
  law emerged.  The literal transform is directly Burrows--Wheeler, so the
  uniform fibre is definitional background.  **Verdict: `KILL_DIRECT_MAP`.**

## 9. `PPR`: plane-partition rowmotion

- **Carrier.** Order ideals of `[a] x [b] x [c]`, equivalently plane
  partitions in an `a x b x c` box.
- **Update.** Take the ideal generated by the minimal elements of the
  complement.
- **Signature.** Boxes
  `(2,2,1),(2,2,2),(2,2,3),(2,2,4),(2,3,2),(3,3,1)` have
  `6,20,50,105,50,20` states and maximum periods `4,5,6,7,6,6`.
- **Candidate theorem.** Periodicity/cyclic sieving and homomesy on box
  families.
- **Collision.** This is exactly rowmotion on plane partitions, a central
  dynamical-algebraic-combinatorics object with direct promotion, toggle, and
  cyclic-sieving literature.  **Verdict: `KILL_DIRECT_ROWMOTION`.**

## 10. `LPS`: Latin-square parastrophe

- **Carrier.** All Latin squares of order `n`.
- **Update.** In each triple `(row,column,symbol)`, swap row and symbol.
- **Signature.** Orders `1,...,4` have `1,2,12,576` states and
  `1,2,6,96` fixed states.
- **Candidate theorem.** Enumerate fixed squares, equivalently columnwise
  involutive quasigroup tables.
- **Second axis.** The map is an involution with fibre one, leaving no temporal
  axis independent of the fixed census.
- **Collision.** Parastrophes are the classical coordinate `S_3` symmetry of
  Latin squares.  **Verdict: `KILL_PARASTROPHE_SYMMETRY`.**

## 11. `FPG`: finite projective flag polarity

- **Carrier.** Incident point--line flags of `PG(2,q)`, representing both
  points and lines by normalized triples and using the standard dot-product
  polarity.
- **Update.** `(P,L)->(L,P)`.
- **Signature.** At `q=2,3,5`, state counts are `21,52,186` and fixed counts
  `3,4,6=q+1`.
- **Candidate theorem.** The fixed flags are the absolute points of the
  nondegenerate conic.
- **Second axis.** None: it is a classical involutive duality with unit fibres.
  It also meets the portfolio's existing polarity vocabulary.  **Verdict:
  `KILL_POLARITY_SYMMETRY`.**

## 12. `PTR`: rotation of polygon triangulations

- **Carrier.** Triangulations of a convex `m`-gon.
- **Update.** Add one modulo `m` to every vertex label.
- **Signature.** For `m=3,...,12`, state counts are
  `1,2,5,14,42,132,429,1430,4862,16796`; maximum periods are
  `1,2,5,6,7,8,9,10,11,12`.
- **Candidate theorem.** Burnside/cyclic-sieving formulas give every cycle
  count.
- **Second axis.** Fibre one and zero transient leave only the classical group
  action.  P146 already uses the same triangulation carrier, albeit with random
  ear deletion.  **Verdict: `KILL_GROUP_ACTION_P146_CARRIER`.**

## Collision receipt for the twelve replacements

None is a disguised selector, tree prune, partition refinement, or random
deletion.  They span link patterns, domino tilings, finite cubic surfaces,
group factorizations, group pairs, carry words, Coxeter words, transform words,
plane partitions, Latin squares, projective flags, and polygon triangulations.
Their kills are therefore substantive and system-specific rather than a claim
that the twelve are cosmetic variants of one mechanism.

## Reproduction and release boundary

Run

```bash
python -B docs/papers157_161_sequence/phase1/combinatorial_gate/verify_replacement_scout.py
```

The verifier checks 12 isolated literal lanes, including closure, the exact TLS
image/rotation/fibre laws, and all displayed finite signatures.  Enumeration
does not prove owner absence.  No paper is numbered, no manuscript is drafted,
and all external state remains `HOLD_EXTERNAL`.
