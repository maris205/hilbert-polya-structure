# Cross-family scout — 28 exact finite systems

## Scope and integrity

`cross_family_scout.py` exhaustively evaluates 28 literal maps on algebra,
binary-word, graph, permutation, partition, chord-matching, and endofunction
state spaces.  The canonical run contains 2,328,763 assertions.  These finite
computations are falsification evidence only: no extrapolated statement is a
theorem until a separate proof route is written.

## Permanent ledger

| ID | literal system | observed signal | disposition |
|---|---|---|---|
| X01 | `x F_2[x]/(x^N)`, `f -> f+f^2` | bijective; periods `1,2,4` through `N=12`; fixed strata jump at double powers | **conditional promote**: exact Frobenius-filtration census has a short proof, but generic finite-linear theory is zero credit |
| X02 | same ideal, `f -> x+f^2` | unique fixed attractor, height `4` | kill: affine translate of nilpotent Frobenius |
| X03 | same ideal, `f -> f^2` | unique fixed attractor, height `4` | kill: bare nilpotent Frobenius |
| X04 | cyclic words, `w -> w xor shift(w)` | long arithmetic period set | kill: standard additive cellular automaton / circulant linear map |
| X05 | cyclic words, `w -> w and shift(w)` | fixed-only recurrence, height `n-1` | kill: elementary erosion |
| X06 | cyclic words, `w -> w or shift(w)` | dual of X05 | kill: complement conjugate of X05 |
| X07 | cyclic radius-one majority | only periods `1,2` in scope | kill: classical elementary CA carrier and heavy owner burden |
| X08 | flip iff neighbours disagree | periods through `31`, tails at most two | kill: linear CA in disguise |
| X09 | graph of odd common-neighbour pairs | periods `1,2`, nontrivial tails | reserve only: exact matrix description exists, but collides with the P127 parity-matrix portfolio |
| X10 | toggle odd-common-neighbour pairs | periods `1,2,4` | reserve only: same P127 collision, and breadth does not isolate a clean invariant |
| X11 | complete every component | idempotent | kill: closure operator |
| X12 | complement inside each component | period two with short merger tail | kill: component closure followed by an involution |
| X13 | toggle induced graph on odd-degree vertices | idempotent | kill: one-step projection |
| X14 | switch the cut of vertices in an odd number of `K_4`s | nearly involutive | kill: switching involution plus shallow transient; no theorem-sized anomaly |
| X15 | permutation inversion | involution | kill: classical |
| X16 | reverse-complement conjugation | involution | kill: classical symmetry |
| X17 | permutation squaring | arithmetic periods and nontrivial fibres | kill: classical power map |
| X18 | reverse maximal excedance-position runs | idempotent | kill: local sorting projection |
| X19 | reverse maximal parity-agreement runs | idempotent | kill: local sorting projection |
| X20 | cyclic shift of set partitions | pure rotation | kill: group action |
| X21 | meet with cyclic shift | fixed-only, height up to six | kill: generic lattice contraction |
| X22 | join with reflection | idempotent | kill: generic closure |
| X23 | merge blocks with consecutive minima | idempotent | kill: one-step local closure |
| X24 | reflect ground-set order | involution | kill: group action |
| X25 | Bulgarian solitaire | rich small periods and long tails | kill: heavily owned classical system |
| X26 | delete every Ferrers corner | deterministic descent | kill: rank erosion with no hidden recurrent structure |
| X27 | delete all adjacent chords, then standardize | strict termination; depth through seven | kill by portfolio: same chord-matching carrier and deletion geometry as P130 |
| X28 | restrict an endofunction to its image, then standardize | exact depth equals maximal tree-to-cycle distance | kill by portfolio and ownership: classical functional-graph pruning, overlapping P114 |

## X01 proof spike

Let `q=p^a`, `I_N=x F_q[x]/(x^N)`, let `F(f)=f^p`, and put
`T=1+F` on the additive group.  Since `F` is nilpotent, `T` is a
permutation.  If `t=p^r m` with `p` not dividing `m`, then in characteristic
`p`

```text
T^t-1 = F^(p^r) U(F),                  U(0)=m != 0.
```

Thus `U(F)` is invertible and

```text
Fix(T^t)=ker F^(p^r),
|Fix(T^t)|=q^((N-1)-floor((N-1)/p^(p^r))).
```

Consequently all exact periods are powers of `p`; the points of exact period
`p^r` are the difference of two consecutive fixed strata, and division by
`p^r` gives the exact cycle census.  The order is the least `p^R` satisfying
`p^(p^R)>=N`.  This route is elementary and auditable, but it is not yet a
novelty claim.

## Direct-owner control for X01

The closest primary literature located in the first pass concerns the general
dynamics of finite linear systems and linearized/additive polynomials, rather
than this exact truncated-ideal census:

- R. A. Hernández-Toledo, *Linear finite dynamical systems*, Communications
  in Algebra 33 (2005), 2977–2989;
- S. D. Cohen and D. Hachenberger, *The dynamics of linearized polynomials*,
  Proc. Edinburgh Math. Soc. 43 (2000), DOI
  `10.1017/S0013091500020733`;
- L. Reis, *Iterating additive polynomials over finite fields*, Proc.
  Edinburgh Math. Soc. 68 (2025), DOI `10.1017/S0013091525000173`.

All general linear-cycle and additive-polynomial machinery is assigned zero
credit.  A search non-hit is not novelty or priority evidence.  X01 remains
`HOLD_EXTERNAL` and may enter the five only if the batch owner/value gate
finds that the explicit filtration census adds enough standalone value.

## Recommendation

Carry X01 as at most one root-lane finalist.  Do not promote X09, X10, X27, or
X28 unless another lane fails and a genuinely different theorem invariant is
found.  This leaves four slots for distinct carriers and proof engines from
the other three lanes.
