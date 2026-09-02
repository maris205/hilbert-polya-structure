# P163 Hostile Review A — original report

**Review date:** 2026-09-03 UTC  
**Calibration:** `NOT_CALIBRATED`  
**Execution boundary:** role-separated internal cold read. The reviewer did
not author the Round-0 paper and wrote an independent literal-map checker.

## Verdict

**PASS — 0 Critical / 0 Major / 0 Minor.**

No change is requested. The parity kernels, mixed-rank clock, recurrent
support involution, central-slice deepest-shell equivalence, support-resolved
count, period split, `n=2` exception, and every-target inverse formula survive
fresh derivation and 356,948 independent assertions. A byte-identical Round-1
freeze is required so the no-change disposition remains explicit.

## Strongest counter-argument

The square of the map is an owned Johnson-graph neighbourhood expansion; the
powerset lift is a Boolean relation; and the inverse formula is ordinary
cover inclusion--exclusion. Those facts remove most of the apparent novelty.
If the manuscript stopped at its kernel, recurrence, or inverse statements,
the correct decision would be owner-thin rejection.

The surviving result is narrower: across the entire phase of `2^(2^n)` set
families, maximum tail is equivalent to a singleton central slice, with every
off-central atom free. The endpoint-support and eventual-period products then
resolve that complete extremal shell. This conclusion requires the even/odd
radius competition and its equality cases; it is not a Johnson ball-volume or
generic relation-power statement. The paper states this residual explicitly
and gives the classical machinery zero contribution credit.

## Independent theorem audit

| Interface | Fresh attack | Verdict |
|---|---|---|
| atomic square | Expanding two deletions/complements gives the original set or one exchange, exactly the closed neighbourhood in `J(n,k)`. | PASS |
| odd kernel | A rank `n-k+1` target has predecessors `bar(C) union {c}`; because every rank-`k` source meets `C`, the minimum Johnson distance is `|A intersect C|-1`. | PASS |
| union lift / silent atom | Literal iteration distributes over source atoms; the empty atom contributes only at time zero and is otherwise erased. | PASS |
| mixed-rank clock | Each occupied slice must fill at one common parity. Taking maxima within parity and then the earlier parity gives the printed `min(2e,2o+1)`; reversing these operations fails. | PASS |
| recurrent core | Inflation under the square and connectedness of each Johnson graph force every periodic slice to be empty or full. Rank support follows `phi`. | PASS |
| fixed counts / zeta | The number of `phi`-orbits is `ceil(n/2)` and every nonfixed recurrent support belongs to a strict two-cycle. | PASS |
| atomic depth census | The two singleton radii yield the printed depth; parity inversion gives one rank at every depth and the stated binomial count. | PASS |
| even deepest equality | In `J(2m,m)`, only a singleton slice has covering radius `m`, because a vertex has a unique antipode. | PASS |
| odd deepest equality | Attaining odd defect `m` forces one `(m+1)`-set to meet every source atom in all `m+1` points, hence the slice is a singleton. | PASS |
| support and period products | The central atom is chosen once, every other occupied layer is any nonempty family, and the silent atom is optional; imposing `R=phi(R)` factors over rank orbits. | PASS |
| every-target inverse | Selecting admissible atomic kernels and requiring their union to cover the target gives the inclusion--exclusion formula and image criterion in both directions. | PASS |
| stable fibre | At `t>=n-1`, every selected nonempty rank slice is saturated; the exact source support is `phi^t(R)`. | PASS |

## Mandatory boundary attacks

- `n=2`: all 12 nonrecurrent phase states are deepest and split `6/6` by
  eventual period; the central-slice condition selects only eight and is not
  asserted.
- `t=0`: the atomic formula is the identity, while the inverse proposition is
  correctly restricted to positive time.
- Empty family and silent-only family have tails zero and one, respectively.
  Both map to the empty target, explaining its positive-time fibre two.
- A target containing the empty atom has inverse count zero: the
  inclusion--exclusion terms cancel, and the union criterion cannot create the
  silent atom.
- Mixed ranks cannot merge because `phi` is a bijection on ranks.
- At and after `n-1`, only rank-union targets occur, with the correct parity in
  `phi^t(R)`.

## Independent exact evidence

The paper-local verifier was freshly replayed: 1,430,898 assertions,
`STATUS PASS`, canonical SHA-256
`21d2dc8e66580e7b78ef9c4bd2bda3eaa393757ee466497a62defb0f15700434`.

The reviewer checker at
`docs/papers162_166_sequence/reviews/p163_a/verify_p163_review_a.py` imports no
paper code. It reconstructs the literal map, compares all atomic kernels
through `n=9`, exhausts all phase states through `n=4`, independently builds
all inverse counts from optional atomic kernels, and sums the support/period
formulas through `n=12`. Two fresh replays matched its canonical transcript.

```text
reviewer verifier SHA-256:
2aa8eeb15f1c8bfcd8bbcc9a9eb5c370c75fffef5f1b78a4acfcef419a76b993
reviewer canonical SHA-256:
d5af4294cac10164d1b3bfa963d44bcabe25326ec65f6389a0fd8f8d8a67c180
assertions: 356,948
```

## Source, collision, and artifact audit

The bounded source screen correctly assigns the shadow/Johnson square to
Kruskal--Katona and Diego--Serra--Vena, and generic Boolean relation powers to
the cited relation literature. It found no direct primary statement of the
central singleton iff, full-phase deepest count, or support/period refinement.
This is a bounded non-hit, not a novelty, priority, or publication-clearance
claim.

P97, P110, P115, and P143 share broad union, deepest-shell, or Boolean-relation
vocabulary but do not transfer the simultaneous parity optimization or the
central equality condition. P162's stochastic affine-coset fibres and P164's
nonlinear-to-linear word interface do not collide with the literal system.

Two source-only cold builds were byte-identical to Round 0 at SHA-256
`899e7c6b24f3a6e99041d05410db75c1de152f4d98b2e90d10e4619927b216bf`.
The five-page A4 PDF has blank identifying metadata; 32/32 fonts are embedded,
subsetted, and Unicode mapped. No build/citation/reference/box warning or
identity leak was found. All five rasterized pages were inspected without
clipping, overlap, malformed mathematics, or bad glyphs.

## Findings

None.

Review A supports `ACCEPT_INTERNAL / HOLD_EXTERNAL`, subject to a different
reviewer completing Review B. No external posting, circulation, submission,
or author contact is authorized.
