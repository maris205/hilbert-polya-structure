# P184 hostile Review A

## Verdict

`PROVABLE AS STATED / ZERO FINDINGS / HOLD_EXTERNAL`

The frozen Round-0 theorem package survives this review.  No paper-directory
file was edited.  This is a process-separated review, not a claim of an
independent error process: the manuscript was authored in the cross-domain
author process identified by the coordinator, whereas this report and control
were produced in `/root/reviewer_a_p183_p184`.

## Frozen input binding

| object | SHA-256 | audit result |
|---|---|---|
| `papers/184-co-gcd-translation-prime-powers/main.tex` | `6f11630dfbb68ff3ac30e652130497b3c473a45869c968fb0679136ba2b8b44a` | read only |
| `papers/184-co-gcd-translation-prime-powers/main_round0_original.pdf` | `991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab` | 4 pages; unencrypted; no JavaScript |

The paper-local `SHA256SUMS` verified every listed Round-0 object.  The live
`main.pdf` was byte-identical to `main_round0_original.pdf` at review time.
The abstract's 109,478 author assertions agree with both the manuscript and
the paper-local canonical output.  No undefined citation/reference or
overfull-box diagnostic was found in the frozen build log.

## Reviewer-owned representation and exact control

The reviewer does not import the author verifier.  For a target `y`, it solves
the predecessor congruence

`x + p^(a-v) = y (mod p^a)`

separately for every candidate valuation `v`, retaining the unique residue
only when its actual valuation is `v`.  It independently constructs the full
functional graph, extracts every tail and canonical cycle, and compares those
objects to the valuation formulas.  This route directly attacks the inverse
problem instead of accepting the author's fibre derivation.

The replay covers 39 prime-power carriers:

- `p=2`, `a=1,...,12`;
- `p=3`, `a=1,...,8`;
- `p=5`, `a=1,...,6`;
- `p=7`, `a=1,...,5`;
- `p=11,13`, `a=1,...,4`.

It records 521,367 successful assertions over every state and target of these
carriers.  A second replay must match `CANONICAL.txt` byte for byte.

## Hostile claim audit

### Low, high, zero, and middle strata

Writing a nonzero state as `p^v u`, the two summands have valuations `v` and
`a-v`.  If `2v<a`, division by `p^v` gives unit-coordinate translation by
`p^(a-2v)` modulo `p^(a-v)`, whose exact order is `p^v`; `v=0` correctly makes
this increment zero modulo `p^a`.  If `2v>a`, factoring gives complementary
valuation `a-v`, so the tail is exactly one and the eventual period is
`p^(a-v)`.  The convention `v_p(0)=a` is used only after separately checking
`0->1`, avoiding an invalid factorization at zero.

For `a=2h`, the middle unit coordinate is exactly `u->u+1 mod p^h`.  The least
positive step reaching a multiple of `p` is
`r=p-(u mod p) in {1,...,p-1}`.  At step `r` the state has valuation `h+s`,
including the endpoint `u+r=p^h` where the residue is zero and `s=h`; one more
step reaches low valuation `h-s`.  This verifies tail `r+1`, period
`p^(h-s)`, and the index convention behind depths `2,...,p`.  For `p=2`,
`r=1` for every middle unit and the maximum tail is exactly two.

### Cycle and tail censuses

Each low valuation-`v` stratum has `(p-1)p^(a-v-1)` states and cycle length
`p^v`, so it contains `(p-1)p^(a-2v-1)` cycles.  Direct cycle extraction agrees
on all 39 carriers.  The low population is the complement of the multiples of
`p^ceil(a/2)`, giving `p^a-p^floor(a/2)` recurrent states.

For odd `a=2h+1`, all `p^h` high states, including zero, have tail one.  For
even `a=2h`, the strict-high population is `p^(h-1)` at depth one, while each
nonzero residue class of `u mod p` occurs `p^(h-1)` times in the middle layer;
therefore every depth `2,...,p` also has population `p^(h-1)`.  These counts
sum to the full carrier in every boundary case, including `a=1` and `a=2`.

### Direct fibres, empty/double sets, and image defect

Valuation-class congruence solving produces at most one candidate per `v` and
agrees target-by-target with brute reverse adjacency.  Low restrictions are
bijective.  Each strict-high source of valuation `a-w` injects into
`p^w(1+p^(a-2w)u)`, while the zero source supplies the separate double target
`1`; valuation and quotient recover `w,u`.  Thus the displayed `D` is exactly
the double-target set and no fibre exceeds two.

When `a` is odd, precisely high targets are missed.  When `a=2h`, the middle
target coordinate `z` lacks a unit predecessor `z-1` exactly when
`z=1 mod p`, giving the displayed `Z`.  The exact solver confirms `D` and `Z`
are disjoint and each has size `p^floor((a-1)/2)`, the remaining fibre count is
`p^a-2d`, total predecessor mass is `p^a`, and the image size is `p^a-d`.

## Wording, citation, owner, and source-control audit

The statement consistently uses canonical representatives, explicitly fixes
`gcd(0,N)` and `v_p(0)`, quantifies `p` as prime and `a>=1`, and distinguishes
tail entrance time from eventual period.  The strict inequalities and the
even equality layer do not overlap.  No composite-modulus or Chinese-remainder
extension is implied.

Citation metadata and contexts agree with primary records.  Xu--Zou is used
only for linear dynamics over finite rings, Anashin--Khrennikov for broad
algebraic and p-adic dynamics, and Konyagin et al. for generic finite
functional-graph background.  These records are confirmed by the
[Xu--Zou arXiv/publisher record](https://arxiv.org/abs/0810.3164), the
[Anashin--Khrennikov publisher record](https://www.degruyterbrill.com/document/doi/10.1515/9783110203011/html),
and the [Konyagin et al. arXiv record](https://arxiv.org/abs/1307.2718).
None supports, and the manuscript does not attribute to it, the literal
co-gcd translation or the stated atlas.

The owner-search language is appropriately bounded: it explicitly denies
that a search non-hit is a novelty certificate, promises withdrawal on a
literal/equivalent owner, and keeps `HOLD_EXTERNAL`.  The internal P128/P142/
P166 subtraction is labelled as internal proof-transfer control, not external
priority evidence.

## Finding ledger

- Critical: **0**.
- Major: **0**.
- Minor: **0**.

No repair is requested.  A byte-identical Round-1 receipt is acceptable.  Any
content change not required by this review reopens all theorem, source, and
reproducibility gates and must be recorded in the delta acceptance file.

## Replay

From the repository root:

```bash
python3 docs/papers182_186_sequence/reviews/paper184/reviewer_A_rootspawn/verify_review_a_p184.py
```

Acceptance requires exit code zero and stdout exactly equal to
`CANONICAL.txt`.  The review-package `SHA256SUMS` is non-self-referential.
