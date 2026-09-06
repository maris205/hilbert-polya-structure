# Alternate P160 replacement scout and kill ledger

**Date:** 2026-09-02 UTC  
**Portfolio boundary:** P1--P156, retired BST, and the frozen P157/P158/P159/P161 systems  
**External state:** `HOLD_EXTERNAL`  
**Outcome:** `NO_BETTER_THAN_RCS`

This was an independent alternate lane.  It did not edit the primary RCS
files.  Eighteen genuinely different literal systems were implemented and
probed exactly.  The best near-survivor, `CSD`, has correct theorem-level
structure, but it does not beat rectangular-corner stripping (`RCS`) after
owner subtraction.  It is therefore an amber reserve, not a replacement.

## Exact-probe ledger

The probes were deliberately small exhaustive programs, not random samples.
They were run ephemerally so this directory contains only the requested scout
and contract documents.

| handle | lane and literal update | exact signal | decision and decisive reason |
|---|---|---|---|
| `CSD` | set families; take the lower shadow and complement every resulting set | exhaustive `n=2,3,4`; at `n=4`, image sizes at times `1,2,3` are `576,64,16`, with `16` recurrent states, `4` fixed states, and height `3`; 461,409 formula assertions, transcript digest `d9e1176c6911f59a48aacaf8ebc71b6ea87a9dae238c2f567aae617ec6c8375b` | **`ALT_RANK_1_AMBER / NO_BETTER_THAN_RCS`**; exact clock, recurrence, and every-target fibres survive, but the square is the standard Johnson closed-ball operator and the fibre engine is generic covering inclusion--exclusion |
| `USH` | arbitrary set families; ordinary lower shadow | `n=4`: 65,536 states, 576 first images, tail histogram `0:1,1:1,2:30,3:2016,4:30720,5:32768`; 461,038 all-time fibre/image assertions, digest `8c5bb3bc399e838d66b9431ae0cb0c26c9f4f85fb91f0a4f64f6a20a72f3ab7e` | `KILL_DIRECT_OPERATOR_OWNER`; iterated shadow is already a standard formalized operator, leaving only one generic cover-count axis |
| `MEP` | labelled finite posets on subsets of `[n]`; delete every maximal element | `n=4`: 318 states, 99 first images, height histogram `0:1,1:15,2:146,3:132,4:24`; 516 inverse/clock assertions, digest `b68c317b4f9815cdc9435427629df8ee7ef9df547f92b84252e28362f1d43e03` | `KILL_MAXIMAL_LAYER_OWNER`; maximal-layer peeling and height are direct prior objects, so only the ideal-lattice one-step fibre remains |
| `CDW` | positive-integer words/compositions; decrement all letters and erase zeros | weight cap 8: 256 states, 34 first images, sharp height 8; complete tail and fibre histograms checked | `KILL_DIRECT_1_REDUCTION/P126`; Bender--Canfield explicitly use this one-reduction and its inverse parsing, while the remaining composition engine is occupied |
| `LBD` | set partitions; delete the block containing the largest label and standardize | ranks 6 and 7: 203 and 877 states; tails equal block count; rank-7 histogram `1:1,2:63,3:301,4:350,5:140,6:21,7:1` | `KILL_PARTITION_DELETION_OWNER/P126`; Stirling insertion supplies the whole inverse and partition deletion is an established random-partition interface |
| `UPQ` | binary languages; a suffix survives iff both one-letter predecessors occur | height-3 leaf row: all 16 targets; fibre values `1,3,9,27,81` with multiplicities `1,4,6,4,1` | `KILL_GENERIC_CYLINDER_GATE/P63/P88`; independent-block Boolean reduction has no second nontransferable engine |
| `ICL` | set families; adjoin all pairwise intersections each round | on `2^[3]`: 256 inputs, 122 terminal closure systems, tail histogram `0:122,1:132,2:2` | `KILL_GENERIC_CLOSURE`; the logarithmic generator-arity clock is a standard closure computation and the inverse did not factor |
| `SFP` | simplicial complexes; delete every facet in parallel | on four vertices: 168 complexes, 29 first images, sharp tail 5 | `KILL_GENERIC_POSET_PEEL`; forward time is just reverse rank and target fibres become set-cover counts |
| `LNK` | simplicial complexes; take the link of the largest vertex | on four vertices: 20 targets; fibre values range from 1 to 20 | `KILL_COORDINATE_RESTRICTION`; tagged dimension gives a forced clock and the inverse is arbitrary complex extension |
| `F2B` | uniform simplicial chains; take mod-2 boundary support | 3-chains on five vertices map onto 64 two-boundaries, each with fibre 16 | `KILL_DIRECT_HOMOLOGY`; `boundary^2=0` and the rank/nullity fibre are classical and collide with occupied linear engines |
| `LEC` | simplicial complexes; perform the lexicographically first elementary collapse | on four vertices: 168 complexes, 32 terminal cores, tails through 8 | `KILL_DIRECT_DISCRETE_MORSE/UNSTABLE`; the rule is owner-heavy and no all-parameter clock emerged |
| `PID` | binary words; strip equal endpoints until the first mismatch | length 8 depth histogram `0:128,1:64,2:32,3:16,4:16` | `KILL_P138/P149`; palindrome radius plus endpoint extraction is already occupied |
| `FIP` | functional digraphs; delete all zero-indegree vertices in parallel | on five labels: 3,125 maps, tails `0:120,1:1185,2:1160,3:540,4:120` | `KILL_GENERIC_GRAPH_PRUNING`; standard cyclic-core peeling, too close to the permanent pruning exclusion |
| `MOORE` | complete binary DFAs; one simultaneous Myhill--Nerode partition refinement | three states: 5,832 automata, tails `0:2808,1:3024` | `KILL_DIRECT_ALGORITHM_OWNER`; classical DFA minimization and shallow at this rank |
| `MDT` | monomer--domino interval tilings; delete the two endpoint tiles | length 11: 144 tilings, tails `3:6,4:91,5:46,6:1` | `KILL_ENDPOINT_EXTRACTION/P149`; Fibonacci enumeration is the only second input |
| `P4E` | square-grid subsets; parallel four-neighbour morphological erosion | `3x3`: 512 states, only two first images, tails `0:1,1:495,2:16` | `KILL_MORPHOLOGICAL_OWNER/THIN_IMAGE`; no target-resolved second axis |
| `ZRC` | binary matrices; delete all-zero rows and columns | `3x3`: 512 matrices, 328 canonical trimmed forms, 265 full-support fixed inputs | `KILL_IDEMPOTENT_SUPPORT_TRIM`; one-step canonicalization only |
| `GIP` | order ideals of a `3x3` grid; delete all maximal cells | 20 ideals, tail histogram `0:1,1:1,2:3,3:9,4:5,5:1` | `KILL_RCS/PARTITION_PEEL`; a one-parameter Ferrers layer shadow of the stronger RCS system |

## Early owner subtraction on the strongest three

1. **CSD.** Kruskal (1963) and Katona (1968) own the lower-shadow
   foundations.  More decisively, Diego--Serra--Vena, *Graphs and
   Combinatorics* 34 (2018), DOI
   `10.1007/s00373-018-1923-7`, state
   `B(S)=nabla(Delta(S))=Delta(nabla(S))` for the Johnson closed ball.
   That is exactly the even two-step kernel of CSD.  The bounded search did
   not find the mixed-rank finite dynamics or target-resolved inverse census,
   but owner absence is not claimed.
2. **MEP.** The maximal-layer literature recursively defines a layer by
   removing all preceding maximal layers and identifies their number with
   poset height.  Order ideals are also standard.  The exact inverse
   `sum_{A subset Max(Q)}(-1)^|A| J(Q-A)^d` was not located, but after the
   forward owner is removed it is only one surviving axis.
3. **CDW.** Bender--Canfield, *Locally Restricted Compositions I*, EJC 12
   (2005), DOI `10.37236/1954`, explicitly subtract one from every part,
   parse the zero/nonzero regions, and reconstruct by adding one.  This is a
   direct mechanism hit, not merely adjacent terminology.

## RCS comparison and red-flag audit

| criterion | alternate `CSD` | primary `RCS` |
|---|---|---|
| carrier/update | arbitrary Boolean set families; complemented lower shadow | integer partitions; delete `a` rows and `b` columns |
| recurrent core | `2^n` full-rank unions, fixed points and strict 2-cycles | unique empty recurrent state |
| sharp clock | `n-1`, refined by two Johnson covering radii | exact rectangle test and capped height `min{t:(at+1)(bt+1)>N}` |
| every-target inverse | exact, but exponential target-cover inclusion--exclusion | factored coefficient formula `q^M/((q;q)_{at}(q;q)_{bt})` plus the empty-target series |
| owner exposure | high: `CSD^2` is the directly documented Johnson ball | standard Durfee/bounded-partition pieces are prior, but no direct owner of the two-parameter dynamic atlas was found |
| internal collision risk | moderate: generic relation-image/Boolean-lattice machinery near P97/P143 | low: two-boundary Ferrers factorization differs from P126/P148 |

The alternate does **not** exceed RCS.  The RCS formulas were also checked
structurally: its nonempty-target baseline weight and two independent
boundary-partition factors are consistent, and its empty-target exception is
necessary.  The focused search found standard Durfee rectangle and bounded
partition decompositions, but no direct owner of the literal two-parameter
iteration, all-time every-target atlas, or three-threshold recovery.  Thus
this scout found **no RCS mathematical, owner, or internal-collision red
flag**.

## Final decision

`NO_BETTER_THAN_RCS / KEEP_CSD_AMBER_ONLY / HOLD_EXTERNAL`.

If RCS later fails a hostile owner gate, CSD is the only candidate here worth
a dedicated owner audit.  None of the other seventeen systems should be
silently promoted.
