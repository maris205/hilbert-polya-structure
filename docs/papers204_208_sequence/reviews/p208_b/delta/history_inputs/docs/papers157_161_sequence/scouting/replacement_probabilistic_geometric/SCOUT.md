# Replacement probabilistic/geometric breadth scout

**Intake:** P157--P161 Route-A Stage 1  
**Date:** 2026-09-02 UTC  
**Decision:** `EMPTY_POOL / HOLD_EXTERNAL`

This lane tested sixteen genuinely different finite configuration dynamics.
All printed small cases were exhaustively checked with exact integer or
`Fraction` arithmetic.  Enumeration is counterexample pressure only: it proves
neither an all-parameter statement nor novelty.  After the P1--P156 firewall,
hard exclusions, and direct-owner subtraction, **no candidate remains eligible
for focused development**.  Consequently no paper number, theorem package, or
TeX draft is assigned.

## Concise kill ledger

| ID | literal carrier and update | exact small-case signature | possible temporal theorem / independent second axis | closest occupied or direct collision | gate |
|---|---|---|---|---|---|
| `PBL` | A rooted boundary arc with an ordered set of surviving vertices; choose uniformly a nonempty proper contiguous block and delete it, stopping at one vertex. | At size 7, `E T=2798/945`; endpoint survival `12844/42525`. | The clock PGF is `2z/D_n product_(r=2)^(n-1)(1+z(r+1)/D_r)`, `D_r=(r-1)(r+2)/2`; a labelled terminal-survivor law is the second axis. | Explicit generic-random-deletion exclusion; P146 polygon deletion is nearest. | `KILL_GENERIC_DELETION_P146` |
| `RTF` | Triangulations of a convex `n`-gon with marked vertex 0; uniformly flip a diagonal when the replacement diagonal is incident with 0. | For `n=8`, depth layers are `1,5,14,28,42,42`; maximum checked history count 8. | The clock is exactly `n-3-d_0(T)` and layers are a Catalan ballot triangle; reduction histories are the second axis. | The fan-flip argument is classical, and its tree/hook proof transfers from P146. | `KILL_TREE_HOOK_P146` |
| `LDL` | Triangulations of a fixed convex point set; uniformly flip a currently illegal edge to its locally Delaunay diagonal. | Generic convex hexagon: 14 states, one sink, maximum mean `103/24`. | A random-legalization clock law and path census would be required; the pilot yielded only instance-specific recurrences. | Lawson's flip algorithm is the literal owner. | `KILL_DIRECT_LAWSON` |
| `DPF` | Domino tilings of `2 x n`; choose one of the `n-1` plaquettes uniformly, rotate two parallel dominoes if possible, otherwise hold. | `2 x 9`: 55 states, active-slot range 3--8, one connected symmetric kernel. | Spectral/mixing time versus component and stationary census. | Direct domino-flip Markov chain; earlier tiling/Glauber scouts. | `KILL_DIRECT_TILING_GLAUBER` |
| `KCI` | Proper colourings of `C_n`; choose a vertex and colour pair, and swap that pair on the selected bichromatic component (or hold). | `C_6`, 3 colours: 66 states in one orbit. | Exact mixing/spectrum versus Kempe-class census. | For three colours this scheduler is the WSK Kempe-component chain. | `KILL_DIRECT_WSK_KEMPE` |
| `LCW` | Labelled simple graphs; choose a vertex uniformly and complement the graph induced by its neighbourhood. | `n=5`: 1,024 graphs, 93 orbits, largest orbit 132. | Walk spectrum versus complete orbit/component census. | Classical local complementation; P117 C01 and P145 occupy the internal interface. | `KILL_LOCAL_COMPLEMENT_P117_P145` |
| `TSW` | Binary `n x n` tables with fixed margins; choose two rows and columns and toggle an alternating `2 x 2` minor, otherwise hold. | `4 x 4`, margins 2: 90 states, active-slot range 12--16, connected symmetric kernel. | Mixing/spectrum versus fibre-component census. | The move is the standard contingency-table Markov-basis switch. | `KILL_DIRECT_MARKOV_BASIS` |
| `MBE` | Spanning trees of a distinctly weighted complete graph; uniformly add a non-tree edge and remove a heavier edge on its fundamental cycle. | `K_5`: 125 trees, unique terminal MST, largest clock support 16. | Exact absorption PGF versus reduction-history/basin census; no stable all-`n` formula emerged. | Permanent generic matroid-basis exclusion and P62--P81/P146 forest machinery. | `KILL_HISTORICAL_MATROID_BASIS` |
| `BCD` | Signed permutations in `B_n`; uniformly apply a right simple descent until the identity. | `B_4`: 384 states; longest clock 16 and 24,024 histories. | Clock equals Coxeter length; histories are reduced decompositions. | Both axes are standard weak-order/Coxeter data and generic reduced-word machinery. | `KILL_DIRECT_COXETER_DESCENT` |
| `VMD` | Sorted positive Markoff triples; apply the unique sum-decreasing Vieta mutation. | Levels 0--8: `1,1,1,2,4,8,16,32,64`. | Exact depth versus parent/child component census. | This is the classical Markoff tree itself. | `KILL_DIRECT_MARKOFF_TREE` |
| `ACD` | Sorted integral Descartes quadruples in the packing rooted at `(-1,2,2,3)`; apply the unique sum-decreasing Descartes reflection. | Levels 0--6: `1,2,5,14,41,122,365` (550 states total). | Exact depth versus branch/level census. | Descartes reflections and their orbit are the Apollonian group. | `KILL_DIRECT_APOLLONIAN_GROUP` |
| `FCR` | Words over `a,A,b,B`; uniformly delete an adjacent inverse pair until freely reduced. | Length 8 reduced-length census `{0:2092,2:11496,4:21816,6:21384,8:8748}`; maximum histories 105. | Clock `(n-|red(w)|)/2` versus every-normal-form histories/fibres. | Generic deletion; exact proof engine already appears in earlier free-reduction scouts (`R05/W01`) and P90. | `KILL_FREE_NORMAL_FORM_DELETION` |
| `PCR` | Arbitrary `q`-colourings of `C_n`; choose a monochromatic edge, an endpoint, and a different colour uniformly; proper colourings absorb. | From `00000` at `q=3`, absorption CDF at times 1--8 ends at `321583/331776`. | An all-`n,q` clock law and target distribution were sought; the fractions show no clean closure and no second theorem survived. | Owner-crowded random recolouring/repair programme; P62--P81 and P139/P141 are nearby. | `KILL_OWNER_CROWDED_WEAK_CLOCK` |
| `ZIG` | Binary cycles; uniformly flip an isolated spin whose two neighbours agree, stopping when none exists. | Absorbing counts through `n=10` end at 122; alternating length 10 has clock masses `4:71/105, 5:34/105`. | Energy drops by two; joint terminal-wall/clock law is the second axis. | Literal collision with the earlier `R06` pilot, plus the one-dimensional Glauber mechanism. | `KILL_PRIOR_R06_GLAUBER_MECHANISM` |
| `MTG` | Monotone triangles with bottom row `1,...,n`; choose a non-bottom site and resample uniformly from its legal interlacing interval. | Order 4: 42 states, connected symmetric kernel, hold range `19/36..3/4`. | Spectral/mixing law versus ASM/triangle census. | Generic single-site heat bath plus classical ASM enumeration; bounded search found no residual exact scheduler theorem. | `KILL_GENERIC_HEATBATH_STATIC_ASM` |
| `BKM` | Two centres on the path `0,...,n-1`; assign vertices to the nearest centre (left tie), then replace each centre by the lower median of its cluster. | `P_16`: 120 starts, 2 fixed states, maximum depth 3, largest basin 64. | An all-`n` transient/basin formula is possible but shallow; basin fibres would be the second axis. | Classical Lloyd-style `k`-medians alternating minimization; no paper-thick stochastic law. | `KILL_CLASSICAL_K_MEDIANS_THIN` |

## Gate rationale

`PBL` and `RTF` were the strongest formula-bearing controls.  `PBL` has a real
product-form clock and endpoint product, but the governing task explicitly
forbids generic random deletion.  `RTF` has a sharp deterministic clock and
Catalan layers, but the fan-increasing flip is classical and the history proof
is exactly the triangulation/tree/hook interface already charged to P146.

The five reversible fixed-slot chains (`DPF`, `KCI`, `LCW`, `TSW`, `MTG`) have
clean component or stationary signatures but no residual sharp temporal law.
The remaining descents are either literal classical algorithms/groups or lose
the second theorem axis.  Promoting any row would therefore violate the
problem anchor rather than fill one of P157--P161.

## Exact evidence

Run:

```text
PYTHONDONTWRITEBYTECODE=1 python3 verify_replacement_scout.py
```

The frozen run reports **16 systems and 206,089 assertions**.  The canonical
transcript is `CANONICAL.txt`.  The verifier is deterministic, standard-library
only, and leaves no bytecode when invoked as above.

