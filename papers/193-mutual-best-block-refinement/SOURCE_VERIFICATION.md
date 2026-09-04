# Source and collision verification — P193 Round 0

**Checked:** 2026-09-04 UTC  
**Status:** `PASS_INTERNAL / OWNER_AMBER / HOLD_EXTERNAL`  
**External search:** bounded owner extension performed in hostile Review A.

## Bibliography scope

| key | record used | manuscript scope | excluded inference |
|---|---|---|---|
| `GaleShapley1962` | Gale and Shapley, *College Admissions and the Stability of Marriage*, *American Mathematical Monthly* 69(1), 9–15 (1962), DOI `10.2307/2312726` | stable matching and blocking-pair vocabulary only | the mutual-best scheduler, permutation map, block normal form, or any P193 theorem |
| `SchipperZhang2025` | Burkhard C. Schipper and Tina Danting Zhang, *Matching, Unanticipated Experiences, Divorce, Flirting, Rematching, Etc*, arXiv:2504.01280 (2025) | mutual optimal blocking-pair terminology and a decentralized stochastic one-pair process | P193's fixed common orders, simultaneous all-pair permutation update, direct-sum clock, or fibre product |
| `Bona2012` | Miklós Bóna, *Combinatorics of Permutations*, 2nd ed., CRC Press (2012), DOI `10.1201/b12210` | standard permutation/direct-sum background | P193's update or enumeration |
| `Stanley2011EC1` | Richard P. Stanley, *Enumerative Combinatorics*, vol. 1, 2nd ed., Cambridge University Press (2011), DOI `10.1017/CBO9781139058520` | standard enumerative permutation background | P193's dynamic or inverse theorem |

These are background citations.  No source is cited as an owner or proof of a
P193 result.  The exact citation-key set in `main.tex` equals the exact
bibliography-key set.

Round 0 reused stable bibliographic metadata and inspected the local paper
history.  Review A then ran the reserved query family and found
Schipper--Zhang's closest matching-process terminology.  Its process selects
one blocking pair stochastically in a changing-awareness model; P193 computes
and exchanges all mutual choices synchronously under fixed common orders.
This distinction prevents a literal-map collision but supplies no novelty,
priority, completeness, or freedom-to-operate inference.

## Matching wrapper subtraction

Under common master orders, a matching represented by `pi` has a blocking
pair exactly at an inversion `i<j` with `pi_i>pi_j`.  If each man chooses the
lowest-labelled blocking woman and each woman chooses the lowest-labelled
blocking man, mutual choices obey the two displayed nomination conditions in
the paper.  Swapping the two partners is the literal permutation exchange.

This equivalence is included only as motivation.  Stable matching, common
master lists, inversions as blocking pairs, preference vocabulary, and
sequential or stochastic mutual-best blocking-pair dynamics earn zero
contribution credit.  The manuscript's definition and every proof are stated
directly on permutations.

## Internal history subtraction

| paper | proximity | strict literal difference |
|---|---|---|
| P105, cycle-minimum pruning | same carrier, unique identity absorber, maximum tail `n-1`, `(n-1)!` deepest states, exact fibres | P105 removes the minimum from each nontrivial functional cycle and fixes it; its clock is longest-cycle length minus one. P193 uses one-line direct-sum blocks and exchanges rather than deleting cycle entries. On `3412`, P105 gives `1234`, while P193 gives `1432`. |
| P122, even record-block reversal | same carrier, adaptive blocks, sharp `n-1` scale, inverse analysis | P122 cuts at left-to-right maxima and reverses even record blocks. P193 cuts at direct-sum boundaries and swaps first/minimum in every nontrivial block; it has no parity selector or reversal. |
| P155, cycle-maximum extraction | cycle and extremal-value vocabulary, target fibres | P155 extracts cycle maxima and standardizes to a generally lower-rank permutation. P193 is rank preserving and does not read functional cycles. |
| P156, weak-excedance extraction | same broad permutation/fibre surface | P156 retains weak-excedance letters and standardizes, changing rank. P193 exchanges entries in place and preserves all labels and positions. |
| P181, first-descent prefix reversal | same carrier, descent/inversion trigger, exact functional graph and fibres | P181 selects one first descent and reverses one prefix; P193 simultaneously swaps first/minimum in every sum-indecomposable block. P181 has nontrivial two-cycles and tail at most two; P193 has strict component refinement, one absorber, and tail up to `n-1`. On `132`, the maps give `231` and `123`, respectively. |

The comparisons establish that P193 is not a literal repeat of these local
systems.  They do not establish external ownership, novelty, or independence
from an uninspected conjugate.

## Bounded owner queries executed at Review A

The following terms were screened in the process-separated source audit:

```text
"sum-indecomposable permutation" "first minimum" swap
"connected permutation" parallel selection sort
permutation component decomposition sorting operator
simultaneous mutual best blocking pairs common master list
parallel swap earliest inversion minimum value
```

The query found Schipper--Zhang as recorded above, but no source was identified
that transfers P193's simultaneous literal map together with its recursive
clock and target product.  This bounded non-hit is not clearance.  A direct
owner or such a conjugacy would require withdrawal or substantial
repositioning.

Final gate: `OWNER_AMBER / HOLD_EXTERNAL / NOVELTY_CLAIM_NOT_AUTHORIZED`.
