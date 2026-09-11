# Open finite-algebra lane for P166: idea and kill ledger

**Frozen decision:** `KILL_ALL`  
**Lifecycle:** `HOLD_EXTERNAL`  
**Scope:** finite algebra, codes, matrices, permutations, and finite-field
configurations; independent of the P158 lane.  This is a scouting record, not
a novelty, priority, freedom-to-operate, or publication claim.

## Intake firewall

Before literal enumeration, the lane was compared against P1--P164 and the
current P162--P166 kill records.  In particular, the following mechanisms were
treated as unavailable:

- P97 sumset/subspace product growth; P99/P125 triangular linear or quadratic
  shears; P100 digit/valuation erasure; P102 involution-norm collapse to a power
  map; P103 adjugate matrix dynamics; P107/P109 ideal and subspace powers;
- P115 Cartier/Frobenius-linear coordinate deletion; P119 unitriangular word
  maps; P124 colon operations; P128 translation--gcd reduction; P135
  centralizers; P137 finite-group split series; P150 totalized rational maps;
  P154 normalizers; P155/P156 permutation extraction; P157 Newton--Hensel;
- the current Schur-power, adjacent-minor, LDU, reciprocal-gcd, group-word,
  cyclic-code-power, row/column support, closure/core, direct-image, Jordan,
  semilattice, and state-normalized-rotation kills.

The hard rule was stronger than literal nonidentity: a new carrier with an old
proof engine was killed.

## Broad desk screen

The table records the actual proposal before the three small-box promotions.
Rows marked `DESK_KILL` were not allowed to consume a deep-test slot.

| ID | literal proposal | earliest obstruction | disposition |
|---|---|---|---|
| `C01` | binary code `C -> span(C*C)` | literal Schur powers and algebra closure | `DESK_KILL_DIRECT_OWNER` |
| `C02` | `C -> C cap C^perp` | idempotent hull/radical extraction | `DESK_KILL_ONE_STEP` |
| `C03` | quadratic-extension code `C -> C+C^q` | Galois closure, an idempotent join | `DESK_KILL_SEMILATTICE` |
| `C04` | puncture all zero or proportional columns, then repeat | matroid simplification finishes in one pass | `DESK_KILL_ONE_STEP` |
| `C05` | alternate trace code and subfield subcode | Delsarte/Galois operations; carrier mismatch | `DESK_KILL_CLASSICAL` |
| `C06/SCD` | `C -> I(C)^perp`, with `I` the Galois interior over `F_(q^2)/F_q` | exact fibres looked nontrivial; promoted | `DEEP_3` |
| `M01` | `A -> adj(A)` or double adjugate | P103 literal family | `DESK_KILL_P103` |
| `M02` | `A -> A^T A` on square matrices | Gram projection followed by powering/rank data | `DESK_KILL_GRAM` |
| `M03` | `(A,B) -> (AB,BA)` | killed Thue--Morse/group-word engine | `DESK_KILL_WORD_MAP` |
| `M04` | `A -> A + A^2` on binary upper triangular matrices | nonuniform fibres and a double-log period anomaly; promoted | `DEEP_1` |
| `M05` | `A -> A^D` or `AA^D` | Drazin inverse / spectral projection | `DESK_KILL_CLASSICAL` |
| `M06` | replace `A` by the induced map on its stable image | Fitting/Jordan filtration | `DESK_KILL_LINEAR_JORDAN` |
| `M07` | simultaneous adjacent `2x2` minors | Dodgson/condensation and the permanent adjacent-minor kill | `DESK_KILL_DIRECT_OWNER` |
| `P01` | recursively delete permutation records | direct recursive-record-filtering owner already in the P102--P106 ledger | `DESK_KILL_DIRECT_OWNER` |
| `P02` | delete cycle extrema and standardize | P105/P155 | `DESK_KILL_INTERNAL` |
| `P03` | halve every Lehmer digit and decode | P100 digit erosion in factorial coordinates | `DESK_KILL_COSMETIC` |
| `P04` | RSK shape/recording-tableau feedback | classical insertion/jeu-de-taquin engine | `DESK_KILL_CLASSICAL` |
| `P05/RTCD` | `pi -> pi^{-1} w_0 pi w_0` | strong matching/period anomaly; promoted | `DEEP_2` |
| `F01` | `U -> U+U^q` for subspaces of an extension field | Frobenius-orbit closure | `DESK_KILL_SEMILATTICE` |
| `F02` | span of inverses of nonzero points in a subspace | reciprocal-linear-space owner density; no temporal law in small hand cases | `DESK_KILL_NO_SPINE` |
| `F03` | normalize an ordered projective frame by its first independent subframe | one-step quotient by `PGL` | `DESK_KILL_ONE_STEP` |
| `F04` | cyclic secant/intersection update on projective polygons | pentagram-map literature; fibres generically singleton | `DESK_KILL_DIRECT_DYNAMICS` |
| `F05` | finite-field Chebyshev or Redei rational iteration | conjugate/semiconjugate power-map functional graphs | `DESK_KILL_DIRECT_OWNER` |
| `A01` | `f -> gcd(f,f')` on bounded-degree polynomials | squarefree decomposition; prior derivative--gcd kill | `DESK_KILL_CLASSICAL` |
| `A02` | `f -> f(x+f(0))-f(f(0))` | state-normalized translation becomes a one-step slice | `DESK_KILL_ONE_STEP` |
| `A03` | annihilator/colon alternation in a finite local algebra | P107/P124 | `DESK_KILL_INTERNAL` |
| `A04` | `g -> g^{-1}theta(g)` for an involution of a finite group | RTCD is the strongest concrete instance | `PROMOTE_ONLY_AS_RTCD` |

No decorated weighting was used to rescue a killed row.

## Literal small-box screen

All signatures below come from `verify_scout.py`, from definitions rather than
the displayed formulas.

| candidate | boxes | states in largest box | image | recurrent | max tail | decisive anomaly |
|---|---:|---:|---:|---:|---:|---|
| `UTAS` | upper triangular `F_2` matrices, `1<=n<=5` | 32,768 | 1,024 | 1,024 | 1 | core periods `1,2,4` at `n=5`; 16 distinct first-fibre sizes |
| `RTCD` | `S_n`, `1<=n<=8` | 40,320 | 105 | 33 | 3 | exact matching-coset image; `-2` power dynamics |
| `SCD` | all `F_4`-linear codes of length `1<=n<=4` | 529 | 67 | 67 | 1 | fibres by target dimension `1,1,3,15,183` |

The signals were mathematically real.  They nevertheless fail the value gate
for separate reasons recorded in `SCOUT.md`.

## Final gate

| candidate | temporal axis | inverse/image/census axis | fatal gate |
|---|---|---|---|
| `UTAS` | exact core period from nilpotency index | fibre equals commuting-idempotent count; sharp zero/regular extremes | arbitrary-target count is not closed; tail one; square-zero/idempotent strata already owned; P102-style power core |
| `RTCD` | exact pointwise depth, fixed sequence, cycles | exact image, uniform first fibres, matching partition census | P102 proof-engine collision plus classical Cartan embedding and matching double-coset machinery |
| `SCD` | `T^3=T`, duality periods one/two | closed every-target `q`-Mobius fibre | forbidden one-step Galois-interior projection followed by classical duality |

Therefore there is **no P166 theorem contract from this lane**.  The strongest
candidate (`RTCD`) is deliberately not marked amber or reserve: the P102
collision is structural, not cosmetic.

**Final state: `KILL_ALL / HOLD_EXTERNAL`.**
