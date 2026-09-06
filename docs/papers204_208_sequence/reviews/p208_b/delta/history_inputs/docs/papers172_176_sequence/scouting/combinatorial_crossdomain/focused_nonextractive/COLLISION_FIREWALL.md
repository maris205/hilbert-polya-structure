# Collision firewall — non-extractive permutation/word/matching lane

**Portfolio boundary:** P1--P171.  **Lifecycle:** `HOLD_EXTERNAL`.

## FCR exact comparison

| axis | FCR | P166 / HWT |
|---|---|---|
| literal carrier | binary words, coordinate positions labelled cyclically | words in `(Z/nZ)^n`, alphabet translated diagonally |
| literal update | rotate coordinates by multiplicity of the current first bit | add current nonzero-coordinate count to every symbol |
| invariant orbit | coordinate-rotation necklace | free diagonal alphabet-translation orbit |
| reduced phase | `j -> j+a_j`, `a_j in {k,n-k}` | `j -> j+c_j`, `c` a weak composition of `n` |
| decisive constraint | `a` is a two-height profile; its sum is generally not `n` | `sum c_j=n` |
| forward proof | orient `gcd(k,d)` disjoint `+/-k` Cayley cycles | mass exhaustion around a phase cycle |
| recurrence | possibly many nontrivial components per necklace | at most one nontrivial cycle per diagonal orbit |
| periods | `1`, `2`, proper divisors of `n` | every `1,...,n` |
| target inverse | two first-bit-labelled inverse rotations; fibres `0/1/2` | histogram-selected diagonal translates; growing sharp fibre |
| fixed census | primitive fixed-density word Möbius sum | Stirling/support census |

The common reduced phase form, ordinary cyclic actions, generic functional
graphs, the number `n-2`, and indicator-style inverse prose are **zero
credit**.  The constrained Cayley-component theorem, its multiple-component
period inventory, and the exact two-branch fibre law are the only residual.
This supports `AMBER_INTERNAL_NEAR_P166`, not green.

## Other nearest occupied mechanisms

| current handle | closest owner | firewall decision |
|---|---|---|
| `A01_VIS` | score/rank feedback neighbourhood including P112; stable standardisation is also a current-batch killed control | literal differs, but no sharp clock or every-target atlas was proved; `KILL_UNCLOSED_CLOCK_SCORE_RERANK` |
| `A02_NPR`, `A03_SPR`, `A05_CTR`, `A06_SDR` | P137/global score feedback and the current adjacent-sum reranker | rich spectra alone do not separate a theorem; `KILL_NO_SPINE` |
| `A04_IGR` | P112 tournament score refinement and degree-defined reranking controls | direct score-profile silhouette, irregular tail; `KILL_SCORE_RERANK_NEAR_P112` |
| `B01_FFR` | canonical alphabet renaming/inventory maps | depth-one retraction; `KILL_CANONICALISER_THIN` |
| `B02_RSS`, `B03_LRS` | P117 run dynamics, P147 run consolidation, and composition sorting | run/composition engine is occupied; `KILL_RUN_ENGINE` |
| `B04_FCR` | Høyer--Špalek Hamming-weight rotation branches; P166 phase map; P117 carrier | only constrained residual retained; `AMBER_INTERNAL_NEAR_P166` |
| `B05_BGS`, `B06_OLS` | stable word sorting/canonicalisation | distinct literals (explicitly checked), but both are depth-one retractions; `KILL_RETRACTION_THIN` |
| `C01_MOC` | P169 successor transfer restricted to pair partitions, with direction reversed | exact mechanism transfer; `KILL_INTERNAL_P169_PAIR_SLICE` |
| `C02_SOC`, `C03_LEW` | canonical matching rewiring and matching-action neighbourhood | irregular spectra/no inverse theorem; `KILL_NO_SPINE` |
| `C04_ESR`, `C05_EDR`, `C06_CDR` | score-based canonical relabelling, close in architecture to P112 | retraction or small irregular core, no parameter theorem; `KILL_MATCHING_RERANK_THIN` |

## Required kill switch

FCR is killed without further balancing if any of the following is found:

1. a direct owner states rotation by the multiplicity of the first symbol and
   any one of the component, clock, or fibre theorems;
2. a literal embedding/conjugacy into P166, rather than the shared quotient
   architecture documented above;
3. a derivation of FCR's multiple-component/proper-divisor theorem directly
   from P166's mass-exhaustion theorem with no new constrained argument; or
4. the independent verifier fails outside its current exact box.

No search non-hit weakens this switch.
