# Paper plan — P158 cut-intersection collapse

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`  
**Form:** anonymous `amsart` probability/combinatorics short note, 4–6 pages.

## One-sentence contribution

Complementary history words simultaneously resolve every-time absorption and
every-labelled-target fibres for repeated fair cut intersections of `K_n`.

## Claims–evidence architecture

| Claim | Deductive support | Exact pressure | Placement |
|---|---|---|---|
| `uv` survives iff histories are complementary | literal intersection identity | every enumerated history | §2 |
| absorption CDF and first hits | one-sided pair occupancy | empty fibres; temporal monotonicity | theorem, §2 |
| exact target fibre | pair injection, orientation, residual occupancy | every labelled graph including zeros | theorem, §3 |
| corrected image boundary | consumed-pair no-reuse argument | `n=5,t=2` explicit nonimage | theorem remark, §3 |
| labelled image EGF | proved component classification | independent species count | §3 |
| tail and mean convergence | one-edge survival plus union bound | finite tail inequalities | §2 |

## Section plan

1. **The process and theorem.** Freeze labels, fair independence, time
   convention, `R`, `A_R`, and boundary values.  Subtract the three source
   neighbourhoods.  State the absorption and every-target axes together.
2. **Complement histories and absorption.** Prove the pathwise encoding and
   the `(2e^x-1)^R` occupancy count.  Derive CDF, first hits, tail, almost-sure
   absorption, and the exact mean series.
3. **The labelled fibre atlas.** Prove component necessity, pair injection,
   orientation, isolate avoidance, converse decoding, and the image EGF.
4. **Exact controls and scope.** Report the frozen boxes and 77,530 assertions,
   including the independent literal-update/complement-history comparison;
   retain limitations, declarations, and `HOLD_EXTERNAL`.

## Mandatory visible boundaries

- `A_0(0)=1`, `A_0(z>0)=0`, and `A_R(0)=1`.
- Positive image iff `r<=R` and (`z=0` or `r<R`).
- `n=5,t=2`: two disjoint edges plus one isolate have fibre zero.
- The verifier is counterexample pressure, never proof or source clearance.
- The source non-hit is bounded and never phrased as novelty or priority.

## Round boundary

Review-A repair preserved this theorem boundary and Review B accepted it with
zero findings.  Any later revision must preserve the same boundary.
