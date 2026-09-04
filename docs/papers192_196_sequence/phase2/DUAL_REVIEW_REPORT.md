# Route A — dual hostile-review report for P192–P196

Status: `BOTH REVIEWS ACCEPTED FOR 5/5 PAPERS / ZERO OPEN FINDINGS /
HOLD_EXTERNAL`.

## Canonical evidence totals

| paper | author assertions | Review-A assertions/checks | Review-B assertions | combined |
|---:|---:|---:|---:|---:|
| P192 | 1,962,920 | 305,104 | 4,606,117 | 6,874,141 |
| P193 | 7,985,745 | 917,785 | 1,170,066 | 10,073,596 |
| P194 | 618,419 | 1,202,599 | 16,194,669 | 18,015,687 |
| P195 | 4,328,312 | 6,551,607 | 9,390,311 | 20,270,230 |
| P196 | 492,356 | 370,380 | 421,266 | 1,284,002 |
| **total** | **15,387,752** | **9,347,475** | **31,782,429** | **56,517,656** |

These are deterministic assertion/check counters disclosed by the frozen
canonical transcripts. They are useful regression and counterexample
pressure, not independent statistical samples and not a substitute for the
deductive proofs. P192's separate `n=9` C++ stream is an additional finite
conjecture check and is not folded into the author assertion total above.

## Acceptance and finding lifecycle

| paper | Review A | Review B | historical findings across A+B | open findings |
|---:|---|---|---|---|
| P192 | `ACCEPTED_REPAIR` | `ACCEPTED_NO_CHANGE` | 0 Critical / 1 Major / 3 Minor, all resolved | 0 / 0 / 0 |
| P193 | `ACCEPTED_REPAIR` | `ACCEPTED_NO_CHANGE` | 0 Critical / 1 Major / 0 Minor, all resolved | 0 / 0 / 0 |
| P194 | original `ACCEPTED_NO_CHANGE`; post-B repair `ACCEPTED_NONREGRESSION` | `ACCEPTED_REPAIR` | 0 Critical / 1 Major / 0 Minor, all resolved | 0 / 0 / 0 |
| P195 | `ACCEPTED_REPAIR` | `ACCEPTED_NO_CHANGE` | 0 Critical / 1 Major / 1 Minor, all resolved | 0 / 0 / 0 |
| P196 | `ACCEPTED_NO_CHANGE` | `ACCEPTED_NO_CHANGE` | none | 0 / 0 / 0 |
| **batch** | **5/5 accepted** | **5/5 accepted** | **0 Critical / 4 Major / 4 Minor, all resolved** | **0 / 0 / 0** |

Historical findings are retained as provenance. They are not silently erased,
but they are also not counted as current defects after same-reviewer repair
acceptance. The only finding first raised in Review B was P194-B1. Review B
accepted the Defant–Williams citation/zero-credit repair, after which the
original Reviewer A completed an independent nonregression acceptance.

## Three-route theorem agreement

### P192 — first-collision Hurwitz dynamics

The author orbit carrier, Review A's Cartesian factor-sequence and circular
parking reconstruction, and Review B's residual-cycle splitting and
parking-content DP agree on the product orientation, the `n=2` boundary,
strictly increasing executed indices, sharp tail `n-2`, fixed count, every
labelled target fibre, and the unique fibre maximizer. Campion Loth–Rattan's
conditional Hurwitz-string construction is cited and zero-credit.

The history-set product, binomial depth distribution, and general
unique-deepest statement remain conjectures. Finite agreement through `n=9`
does not move them into the proved package.

### P193 — mutual-best block refinement

The literal permutation/block implementation, Review A's direct
reconstruction and expanded recurrences, and Review B's cut-bit/interval
grouping route agree that active nominations are exactly block-first/block-
minimum pairs and are updated simultaneously. They also agree on strict
direct-sum refinement, the identity absorber, pointwise recursive height,
maximum tail `n-1`, `(n-1)!` deepest sources, the depth-OGF recurrences, image
criterion `sigma_1=1`, every-target fibre product, and the unique maximum
`2^(n-1)` at the identity. Schipper–Zhang's stochastic sequential mutual-best
process is cited, subtracted, and zero-credit.

### P194 — least-colour raising on type-A crystal words

The author signature/RSK/component computation, Review A's prefix-minimum,
Greene, Jacobi–Trudi, and Aitken reconstruction, and Review B's sign-rewrite,
growth-diagram, Gelfand–Tsetlin, cyclotomic, Young-poset, and matching routes
agree on highest-word sinks, the exact weight clock, global tail `n(k-1)`
uniquely at `k^n`, component and global Schur depth polynomials, bounded-height
involution fixed census, every-target predecessor atlas, fibre bound `k`, and
the full-fibre threshold `n >= binom(k,2)`.

Review B's Defant–Williams finding caused a source-only repair. The repaired
text assigns existing crystal pop-stack dynamics, convergence, and sharp
orbit results zero credit and explains the macrostep/one-edge distinction.
No P194 theorem or control changed, and Review A's post-repair nonregression
recheck passed.

### P195 — odd-side least-neighbour tree walk

The author Prüfer/tree computation, Review A's reconstructed trees and
predecessor bins, and Review B's rerooted oriented-edge size arrays and
rational EGF route agree on fixed recurrence for odd `n`, reciprocal
two-cycles for even `n`, sharp tail `floor((n-1)/2)`, recurrent EGFs,
every-target local fibres, and sharp maxima `(n+1)/2` for odd `n` and `n-1`
for even `n`. All routes retain the counterexample showing that one connected
`H` component can contain multiple mutual edges; no uniqueness-per-component
claim survives. P123/P159's parity/tail/zeta/species/fibre silhouette is
explicitly subtracted.

### P196 — cyclic Gödel implication

The author tuple/transfer computation, Review A's weak-chain fibres and
determinant/Leibniz route, and Review B's packed-radix relation-matrix and
Faddeev–LeVerrier route agree on the exact one-step core, rotation on the
core, depths `0/1`, the unique fixed point, trace/Möbius cycle counts,
characteristic polynomial `lambda^q-(lambda+1)^(q-1)`, and the labelled
gap-factorized fibre formula. The rejected q-bonacci characteristic form is
not part of the paper.

## Process and release conclusion

For each paper, the author verifier, Reviewer A, and Reviewer B use distinct
implementations and materially different representations recorded in
`reviews/PROCESS_SEPARATION_LEDGER.md`. Each review has its own proof
rederivation, source/owner audit, delta, input pins, build/PDF QA, canonical
transcript, and non-self manifest; Review B additionally records two explicit
fresh-process byte-identical replays.

Dual acceptance certifies this internal review process only. It does not
certify novelty, priority, owner-search completeness, independence from an
unqueried conjugate, freedom to operate, or external-release readiness. P192
remains `OWNER_RED_AMBER / HOLD_EXTERNAL`; P193–P196 remain
`OWNER_AMBER / HOLD_EXTERNAL`.
