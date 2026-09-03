# Historical and cross-lane collision firewall

**Verdict:** all candidates killed; `HOLD_EXTERNAL` remains mandatory.

The exact directory-title inventory has 171 lines because P96 has two
historical directories.  It covers numbered directories P1--P50 and P57--P176.
P51--P56 are absent from `papers/`; their recovered sequence-record titles are
listed in `TITLE_COLLISION_INVENTORY.md`.  The full historical seeds remain
authoritative; title separation by itself never earns survival credit.

## High-pressure comparisons

| candidate | nearest occupied mechanism | exact comparison | result |
|---|---|---|---|
| `MCJ` | P105 cycle-minimum pruning | P105 simultaneously removes the minimum of each nontrivial cycle and absorbs at the identity with longest-cycle depth.  `MCJ` serially joins an outside cycle to the 0-cycle and absorbs at all long cycles with cycle-count depth. | Literal not equal, but cycle/minimum/descent/fibre silhouette is already heavily occupied. |
| `MCJ` | P122 even record-block reversal | P122 already owns target-local admissible record cuts, a sharp permutation clock, and a record automaton.  `MCJ` reduces further to independent lower-record cuts and `(1+u)^r`. | **Fatal proof-engine transfer.** |
| `MCJ` | P155 cycle-maximum extraction | P155 is rank-changing and uses ordered supports; `MCJ` stays in one `S_n`.  Both organize inverse data by ordered cycles and record endpoints. | Adds owner pressure; no separation credit. |
| `MCJ` | P176 first-frequency rotation | P176 is binary pointed-necklace phase dynamics with signed Cayley components and `0/1/2` fibres.  `MCJ` has neither rotation nor necklace phase. | No literal collision, but this noncollision cannot rescue the Foata kill. |
| `IAC` | P91/P102/P154 | Two iterates are conjugation by the fixed long cycle, and odd fixed powers are permutation-root counts. | **Fatal reusable inversion/dihedral/root engine.** |
| `PMX` | P118 and P132 | P118 owns synchronous mex dynamics; P132 owns recomputed prefix feedback. | **Fatal recombination.** |
| `NOG` | P110/P167 and set-partition scouts | The update forgets labels and is injective only at the equality-partition level; labelled fibres are falling factorials. | Static quotient encoder, not an independent dynamic mechanism. |
| `TAN` | P117/P138/P164/P176 cyclic-word band | It is not first-frequency rotation, run reversal, prefix XOR, or equality feedback.  Nevertheless it is a textbook nonsingular NFSR differing from pure rotation on one cycle-join class. | Direct external owner density kills before internal allocation. |
| `CRP` | P77 digit towers and P174 canonicalization | Its image tower is exactly stable radix passes; the bit rotation merely schedules the next digit. | Algorithm rename, no residual. |
| `CSS` | P174 and sibling `SMP` | All temporal and fibre statements follow from greedily replacing a noncanonical support label by a missing canonical one. | Canonical selection-sort engine, killed. |
| `FDF` | sibling `FDR` | Both trigger at the first descent, but `FDR` reverses a prefix and has tail at most two, whereas `FDF` moves only the descent follower to front and has exponential sharp depth. | Literal/mechanism separation exists, but exact Project Euler ownership is independently fatal. |

## P176 exclusion

No candidate uses a state-dependent rotation amount determined by a symbol
frequency, pointed necklaces, signed `+/-k` Cayley walks, proper-divisor period
inventory, or the P176 two-branch predecessor mechanism.  `TAN` uses ordinary
word rotation only on its unmodified bulk states and was killed as an NFSR
cycle join; it receives no credit for cyclic-word behaviour.

## Frozen inputs

Selected source hashes at the audit point:

```text
bbcfd687ebf99c7b37b389c6dd8067f51db561399c7aa89d33cb819ad047b80e  docs/papers177_181_sequence/HISTORICAL_COLLISION_SEED.md
e9f0328ea00ba78316ab41d44f86844a22f20a97b818fbbf637d1fad3289c912  docs/papers172_176_sequence/HISTORICAL_COLLISION_SEED.md
8bf14d50abf29591dcc55686863c8775c34b88a44edd4e0e8af428ddf304ab98  papers/105-cycle-minimum-pruning-dynamics/main.tex
e443cc734b226a5c4d9a598369fc0f8fc42dc6b17ec5973815b9163c0896c576  papers/122-even-record-block-reversal/main.tex
11d9defc5f014d5c5b5cba3db860da214169dcdcb07cdf55595563a59cdb81ee  papers/155-cycle-maximum-extraction/main.tex
500fdea81499204a92bd3b6e24c5f9fd7b758d29b5c5dcdbf60e5e3f8e861d73  papers/167-minimum-inverse-position-feedback/main.tex
ff1f7d45c7ac7146a06f737a7187a9cedd451591ab9cbffeccf2d35eadc5874a  papers/176-first-frequency-rotation/main.tex
```

