# Hostile Review A — P174

**Reviewer:** independent coordinator-side rederivation (not the manuscript
author)  
**Round reviewed:** author Round 0  
**Verdict:** `PROVABLE AS STATED / AMBER GATE UNCHANGED`  
**Findings:** 0 Critical, 0 Major, 0 Minor  
**Lifecycle:** `PROVISIONAL_AMBER / HOLD_EXTERNAL`

## Hostile questions and outcomes

### HR-A1 — Is the two-stage tower merely inferred from examples?

No.  The pivot is the unique source point mapped to infinity, and infinity
is the unique source point mapped to zero.  These two forced-point facts give
`im M subseteq Z` and `M(Z) subseteq Y`.  Pivot-zero inversion supplies the
reverse containments, so `im M=Z`, `im M^2=Y`, and `M^4=M^2` hold uniformly.

### HR-A2 — Can a state be assigned the wrong depth because it lands on a
different inversion cycle?

No.  Every point of `Y` is already periodic under the involution, every
point of `Z\Y` first enters `Y`, and every point outside `Z` first enters
`Z\Y`.  The three strata are disjoint and exhaustive.  The binomial depth
counts and the sharp depth-two claim follow exactly.

### HR-A3 — Does the inverse count omit modular wraparound or double-count a
parent under two pivots?

No.  For proposed pivot `a`, the inverse source is forced.  Its other finite
representatives are `a+y^(-1) mod p`; the condition that none wraps below
`a` is precisely `a < p-max(y^(-1))`.  Hence valid pivots are the initial
interval `0,...,h(T)-1`.  Different valid pivots cannot give the same parent
because each is the parent's least finite point.

### HR-A4 — Are the fibre histogram and unique maximum consistent at all
boundaries?

Yes.  Relabelling nonzero target points by inversion reduces the count at
fibre size `q` to `binom(p-q,k-2)`, with the usual zero convention.  At
`q=p-k+2` this equals one, proving uniqueness.  The independent control
checks the complete `p=2,k=2` graph and every allowed box through `p=13`.

### HR-A5 — Is the owner boundary overstated?

No positive novelty claim is made.  Fixed Möbius dynamics, `PGL(2)` subset
actions, inversion, binomial enumeration, P96/P168, and generic adaptive
normalization are all explicitly subtracted.  The artificial coordinate
order and shallow clock remain reasons for amber status.  A later general
adaptive-section owner is still an active kill switch.

## Independent computational receipt

The separately written bit-mask verifier is at
`docs/papers172_176_sequence/reviews/p174_review_a/verify_review_a.py`.  It
imports no author or scouting code and exhausts 35 complete `(p,k)` boxes for
`p=2,3,5,7,11,13`:

```text
STATES 20765
ASSERTIONS 161536
RESULT PASS
```

It reconstructs every edge, the first and second images, depth and fixed
censuses, `M^4=M^2`, every forced inverse source and pivot interval, the
full fibre histogram, mass identity, and unique maximum.  The canonical
transcript and verifier are covered by `MANIFEST.sha256`.

## Required action

No manuscript repair is required by Review A.  Preserve the Round-0 PDF as
the Round-1 no-change baseline, retain the amber kill switch, and proceed to
an independently implemented Review B.
