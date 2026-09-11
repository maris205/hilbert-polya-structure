# P197--P201 replacement breadth and kill ledger

**Scope:** replacement search after the GBE/SCT gate.  **External state:**
`HOLD_EXTERNAL`.  **Counting rule:** one frozen literal update is one tested
system; parameter boxes do not inflate the denominator.  Old killed/reserved
systems, including LSPO, blocker duality, and component complementation, are
not counted.

The dependency-free verifier tests **nine new literal maps** and makes more
than 1.5 million exact assertions.  Only LZK is promoted from this directory.
LFAS is a mathematically closed reserve below the paper threshold.  PZK is
not a second recommendation because it shares LZK's Kempe primitive.  The
other six maps are killed aggressively.

## Exact ledger

| ID | finite carrier and frozen deterministic update | exact signal | decision |
|---|---|---|---|
| `LZK` | Proper `q`-colourings of labelled `K_{r,s}`.  If no vertex has colour `0`, hold.  Otherwise choose the least-labelled zero and interchange `0,1` on its bichromatic Kempe component. | `(q,r,s)=(3,3,4)`: `66` states, image `54`, recurrent `44`, max tail `4`, max fibre `5`; `(4,3,4)`: `924/714/568/4/5`; `(5,3,4)`: `7100/5198/4154/4/5`.  Exact support-side dichotomy, sharp `#zero` clock, full fixed/two-cycle/depth census, and every-time binomial target fibres. | **`PROMOTE_THEOREM_SPIKE / OWNER_AMBER / HOLD_EXTERNAL`.**  Kempe moves and chromatic/onto counts are zero credit.  The residual is the deterministic scheduler + opposite-side recurrent core + all-time labelled fibre atlas. |
| `PZK` | Proper edge-colourings of a path, encoded by adjacent-unequal words.  At the leftmost zero, swap `0,1` on its maximal bichromatic edge path; hold if zero is absent. | `q=3,n=10`: `1536` states, image `1152`, recurrent `1024`, max tail `5`, max fibre `6`; `q=4,n=10`: `78732/52488/39878/5/6`.  The invariant separator skeleton gives tail `ceil(n/2)` and only periods `1,2`. | **`KILL_BATCH_DUPLICATE_BEHIND_LZK`.**  The run-skeleton proof is different, but this is a second least-zero Kempe system in the same batch.  It cannot provide the requested independent survivor. |
| `LFAS` | Binary `r x s` matrices.  Complement the lexicographically least alternating `2 x 2` rectangle; hold if none exists. | `4x4`: `65536` states, image `47114`, fixed `6902`, max observed tail `4`, max fibre `9`, periods `1,2`.  Row/column margins are invariant; selector indices descend; fixed points have the lonesum Stirling census; every target has an exact admissible-rectangle fibre atlas. | **`RESERVE_AMBER / NOT SELECTED`.**  This is not sorting or closure, but the switch is the standard contingency-table `2`-switch and the current all-size tail bound is not sharp. |
| `LFCTR` | Labelled tournaments.  Reverse all three arcs of the lexicographically first directed triangle; hold if none exists. | At `n=6`: `32768` states, image `22704`, fixed `720`, max observed tail `4`, max fibre `4`; only periods `1,2`.  Scores are invariant and the selector decreases. | **`KILL_DIRECT_MOVE_OWNER / P112_COLLISION`.**  The same cyclic-triangle reversal move is already killed as `G09 CTR`, and P112's tournament/cycle-reversal surface is occupied.  Determinising the schedule does not reopen it. |
| `BDC` | Labelled simple graphs.  Delete every bridge simultaneously. | At `n=5`: `1024` states, image=fixed `314`, max fibre `291`.  It is idempotent; the fibre over a bridgeless target is a weighted labelled-forest count on its connected components. | **`KILL_CANONICAL_PRUNING`.**  The inverse formula is clean, but the literal map is one-step bridge-core extraction and its entire clock is the pruning definition. |
| `GMP` | Matchings of `K_n`.  If at least two monomers remain, join the two least labels; otherwise hold. | At `n=10`: `9496` states, image `3328`, sharp tail `5`, max fibre `6`.  Tail is `floor(#monomers/2)` and the target fibre counts matched edges lying before the first target monomer. | **`KILL_GREEDY_AUGMENTATION / CMM_CLUSTER`.**  This is the trivial complete-graph precursor of the selected odd-cycle matching candidate; deficiency and inverse-edge choice are inherited greedy augmentation. |
| `SCR` | Oriented simple graphs.  Reverse every arc internal to every strongly connected component, simultaneously; cross-component arcs hold. | At `n=5`: `59049` states; `29281` fixed DAGs and `14884` two-cycles.  The SCC partition is invariant and the map is an involution. | **`KILL_COMPONENTWISE_ACTION`.**  SCC decomposition makes the whole system a transparent product involution with singleton fibres. |
| `HCI` | `k`-uniform hypergraphs.  Retain precisely those current hyperedges meeting every other current hyperedge in at most one vertex. | For `3`-graphs on five vertices: `1024` states, image=fixed `26`, max fibre `959`.  Target fibres count vertex subsets of a conflict graph having no selected isolate. | **`KILL_CANONICAL_PRUNING`.**  It is a one-round projection to linear hypergraphs; the conflict-graph fibre is static reconstruction, not an independent temporal axis. |
| `OCI` | Permutations.  Simultaneously invert every odd-length disjoint cycle; even cycles hold. | At `n=8`: `40320` states, `17984` fixed and `11168` strict two-cycles.  Fixed EGF is `exp(x)/sqrt(1-x^2)`. | **`KILL_COMPONENTWISE_ACTION`.**  Cycle length is invariant and conditional inversion supplies the whole theorem before iteration begins. |

## Funnel

```text
9 genuinely new literal updates tested here
  1 theorem spike: LZK
  1 independent mathematical reserve below threshold: LFAS
  1 same-cluster kill behind LZK: PZK
  6 direct-owner, pruning, augmentation, or action kills
```

The separately delegated Stirling-permutation replacement, FOSP, is not
counted in this nine-system denominator and is not duplicated here.  Its
independent package supplies the batch's second survivor if its proof and
owner gates remain intact.

## Strongest contract and non-contract

- [`LZK_THEOREM_CONTRACT.md`](LZK_THEOREM_CONTRACT.md) freezes all admissible
  claims, including `q=2`, `t=0`, and ordered-versus-unordered cycle counts.
- [`LFAS_RESERVE_CONTRACT.md`](LFAS_RESERVE_CONTRACT.md) records the exact
  theorem already available and the missing sharp-tail requirement.  It must
  not be cited as a selected candidate.
- LSPO is excluded rather than silently dropped; its binding hostile
  disposition is recorded in [`LSPO_HOSTILE_DISPOSITION.md`](LSPO_HOSTILE_DISPOSITION.md).

