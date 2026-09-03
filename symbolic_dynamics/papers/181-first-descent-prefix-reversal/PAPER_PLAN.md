# Paper plan — P181

**Working title:** First-Descent Prefix Reversal Has a Depth-Two Functional
Graph  
**Format:** anonymous deterministic `amsart` short theory note  
**Target length:** 4–5 A4 pages including references  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

## One-sentence contribution

The autonomous prefix reversal ending immediately after the first descent
has an exact half-image, an identity-plus-two-cycle recurrent core, a complete
depth census, and a target-local inverse atlas controlled by one decreasing
run.

## Claims–evidence matrix

| ID | Frozen claim | Proof evidence | Author-side exact pressure | Manuscript location |
|---|---|---|---|---|
| C1 | `Im(F)=I_n={tau:tau_1<tau_2}` and `|I_n|=n!/2` | every reversal output starts with the reversed descent pair; two-prefix reversal supplies a predecessor to every target in `I_n`; first-coordinate swap pairs the two comparison classes | construct the full image through `S_9` | Theorem 1(i), §2 |
| C2 | recurrent states are the identity plus all position-two peaks; peaks form `n!/6` two-cycles | a peak triggers `rho_3` and maps to a peak partner; every other image state maps to a peak | full orbit coordinates and partner checks | Theorem 1(ii), §2 |
| C3 | tail census is `(n!/3+1,n!/2,n!/6-1)` with maximum tail two | count peaks; identify depth-two states bijectively with nonrecurrent image states; subtract | literal tails for every state through `S_9` | Theorem 1(iii), §3 |
| C4 | every target fibre is the family `rho_k(tau)`, `2<=k<=r(tau)+1`, plus the fixed identity predecessor when applicable | translate the source first-descent inequalities under an involutive prefix reversal | full incoming sets, not just sizes, through `S_9` | Theorem 1(iv), §3 |
| C5 | for `n>=4`, maximum fibre is `n-1` at exactly `n-1` targets with `tau_2=n` and decreasing suffix from position two | the run is at most `n-1`; equality forces the largest value into position two; choose `tau_1` and force the rest | maximum and complete maximizing set through `S_9` | Theorem 1(v), §4 |
| B1 | at `n=1`, the sole state is fixed with singleton image/core, depth zero, and fibre one | direct one-state calculation | complete literal box | Proposition 2 |
| B2 | at `n=2`, image/recurrent/tails/fibres are `{12}`, `{12}`, `(1,1)`, and maximum two at `12` | direct two-state calculation | complete literal box | Proposition 2 |
| B3 | at `n=3`, image has three states, all recurrent image states, tails `(3,3,0)`, and all image targets have fibre two | specialize the theorem and account for the identity's extra predecessor | complete six-state calculation | Proposition 2 |

## Section and page budget

| Part | Purpose | Budget |
|---|---|---:|
| Abstract and title | literal rule, depth two, half-image, inverse run | 0.25 page |
| 1. Rule, background, and theorem | define `rho_k`, first descent, owner boundary, and full five-part result | 1.25 pages |
| 2. Image and recurrent core | prove the half-image and all cycles | 0.85 page |
| 3. Fibres and tail census | prove the inverse lemma, depth-two bijection, and census | 1.05 pages |
| 4. Maximizers and small boundaries | prove sharp maximum; freeze `n=1,2,3` separately | 0.65 page |
| 5. Controls and status | executable scope, collisions, owner ceiling | 0.35 page |
| References | three verified journal sources only | 0.40 page |

## Author-round obligations

- Use the prefix length `d(pi)+1`; do not accidentally reverse only through
  the left member of the descent.
- Distinguish P181 from Project Euler First Sort, which moves the follower to
  the front and agrees only when the first descent occurs at position one.
- Prove the complete predecessor *set*, not only its cardinality.
- Separate recurrence (tail zero) from the image, and count depth one only
  after the depth-two bijection is established.
- State `n=1`, `n=2`, and `n=3` explicitly; do not force the `n>=4` maximizer formula
  onto the identity at small size.
- Assign generic prefix reversal, pancake sorting, descent statistics,
  longest-increasing-prefix selection, and finite-map bookkeeping zero
  contribution credit.
- Keep `OWNER_AMBER / HOLD_EXTERNAL` visible.  Never call a bounded non-hit a
  novelty result.

Review A later requested the `S_1` boundary closure; that exact one-state
atlas is now included without changing the `n>=3` theorem package.  Review A
accepted the repaired package with no open finding, and process-separated
Review B independently accepted the full theorem package.  Round 2 therefore
closes at `0 Critical / 0 Major / 0 Minor` open while retaining
`OWNER_AMBER / HOLD_EXTERNAL`.
