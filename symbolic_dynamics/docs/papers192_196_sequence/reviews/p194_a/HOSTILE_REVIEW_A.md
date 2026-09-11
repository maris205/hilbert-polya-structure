# P194 hostile Review A

**Reviewer relation:** process-separated internal Reviewer A; did not author
P194 and did not import, execute, or reuse its verifier while constructing the
reviewer control.  The frozen author verifier was replayed only after the
independent control passed.  
**Frozen input:** the original Round-0 source/PDF record and the current
post-Review-B source-repair package are distinguished below; all current live
inputs, both preserved four-page snapshots, and the five-page current PDF are
pinned in `PINNED_INPUTS.sha256`.  
**Decision:** `ORIGINAL_A_ACCEPTED_NO_CHANGE +
POST_B_REPAIR_ACCEPTED_NONREGRESSION` (`0 Critical / 0 Major / 0 Minor`).  
**Mathematical decision:** `PROVABLE_AS_STATED`.  
**External state:** `OWNER_AMBER / HOLD_EXTERNAL`.

## Outcome first

The stated theorem package survived an independent reconstruction.  The
reviewer built the complete functional graph for every word in the 30 boxes
`1 <= k <= 5`, `1 <= n <= 6`, including an alphabet size absent from the
author's complete grid.  All 26,214 literal transitions and all 26,214
labelled target fibres agree with the theorem.  Every component has the
claimed ballot sink, pointwise energy clock, reverse-RSK shape, Schur depth
polynomial, and Aitken multiplicity.  No nontrivial cycle or excess fibre was
found.

The implementation was intentionally orthogonal to the author control.  It
locates `e_i` by strict prefix-balance record minima, locates `f_i` by a
right-to-left scan, recovers RSK shape from Greene multi-chain invariants,
computes Schur specializations by Jacobi--Trudi determinants, and computes
`f^lambda` by the Aitken determinant.  It contains no import from the paper
directory.

The convention attack is decisive rather than cosmetic.  Under the frozen
signature, `e_1(21)=11`.  Ordinary left-to-right RSK changes shape from
`(1,1)` to `(2)`, whereas RSK of the reversed words gives `(2)` before and
after.  Thus the reversal in the manuscript is necessary and correctly
oriented.

No source, owner-boundary, build, or presentation defect crossed the finding
threshold.  This is only an internal mathematical and production acceptance.
It is not a novelty, priority, completeness, independence, or
freedom-to-operate conclusion.

## Post-Review-B source-repair nonregression

Review B located Defant--Williams' crystal pop-stack dynamics, a source missed
by the original bounded Review-A search.  The author-side repair is accepted.
The exact Round-0-to-current source delta consists of three prose changes in
`main.tex`--an abstract subtraction, one nearest-owner comparison paragraph,
and a closing zero-credit sentence--plus the single
`DefantWilliams2022` bibliography record.  It does not alter the literal map,
any proof, theorem statement, equation, example, finite-control claim, or
verifier.

The six proposition/theorem/corollary environments extracted from the old and
current sources are byte-identical, with common SHA-256
`50b8063105affc11fda5ebde3fd8c1cc4cc3951b40ce37b210d34e1b9d43955d`.
The same 16 equation labels occur in the same order.  The author verifier and
canonical output retain hashes
`ba0945a66d47ce074ba5cff9838777edebc640fe7fffa828eee6013bf9ee054c`
and
`969d07b598949b7ad14e8e032d7b294f320b09e0bbc05e656efb72282f7673ec`;
two fresh author replays remain byte-identical.  Reviewer A's independent code
and canonical output likewise retain hashes
`0f5a94796da5e39fda40de72a60659126380d23055080b47b513cd38816bc763`
and
`4e579cb9e2552fe5703e9d0e2ad5f462e8b822c0751a2531d024f901abeb1881`,
and two fresh replays still report `0/0/0`.

The added comparison is accurate and conservative.  Defant--Williams define
one pop step by fixing the starting vertex's full descent-colour set and taking
the unique source of its connected component in the corresponding restricted
crystal.  P194 instead takes exactly one edge of the least currently available
colour and recomputes availability after every edge.  The paper explicitly
gives the entire pop-stack dynamical surface zero contribution credit, limits
the retained object to the exact scheduler/clock/targetwise-atlas conjunction,
and makes no novelty claim.

## Hostile mathematical attacks

- **Signature and ballot orientation:** unmatched minuses were reconstructed
  as strict prefix-balance record lows.  Their absence is exactly the prefix
  ballot condition.  Mutual inversion of every available `e_i/f_i` edge was
  checked separately.
- **Tensor convention:** the explicit `21 -> 11` witness falsifies ordinary
  RSK invariance and confirms reverse-word RSK invariance.  Shape preservation
  was then checked on every edge and component in the complete grid.
- **Clock and recurrence:** each effective step lowers letter sum by one and
  remains in one component.  Direct orbit reconstruction found only fixed
  recurrence and verified `tau(w)=E(w)-b(shape(w))` at every state.
- **Sharp tail:** every complete box has maximum `n(k-1)` and unique deepest
  state `k^n`.  The `n=1` orbit of every letter was separately checked through
  `k=12`; the `k=1` carrier was separately checked through `n=12`.
- **Schur normalization:** Jacobi--Trudi output was shifted by
  `n(lambda)=sum_(r>=1)(r-1)lambda_r`, then cross-multiplied against the
  manuscript's hook-content product.  This catches either a missing `q^n` or
  a missing principal-specialization shift.
- **`q=1` limit:** every factor has positive numerator exponent when
  `ell(lambda)<=k`; the factorwise limit is `(k+ct(x))/h(x)`.  All 109 allowed
  shape/alphabet cases in the complete grid agree with the polynomial value,
  and the global mass is exactly `k^n`.
- **Fixed and involution census:** permutations through `S_8` were recognized
  as involutions without RSK inversion.  Greene shape height also agreed with
  a direct longest-decreasing-subsequence computation.  Shape counts equal
  Aitken `f^lambda`, bounded-height sums agree, and `k>=n` gives the telephone
  numbers.
- **Every-target atlas:** actual incoming sets were accumulated before the
  formula was evaluated.  Empty fibres, highest self-sources, each admissible
  `f_i(y)`, distinct colours, the bound, and total fibre mass all agree.
- **Stable threshold:** a full fibre must contain the self-source and all
  `k-1` colour candidates, forcing a highest target with strictly decreasing
  padded content and hence size at least `binom(k,2)`.  Staircase witnesses
  were checked literally for `1 <= k <= 10` and four boundary/surplus values.
  The complete grid also checks nonattainment below the threshold.  For
  `k=5`, the complete grid stops at `n=6<10`, so its largest fibre is four;
  the separate length-10 staircase check realizes fibre five.

## Exact evidence record

```text
author replay 1: PASS, byte-equal
author replay 2: PASS, byte-equal
reviewer replay 1: PASS, byte-equal
reviewer replay 2: PASS, byte-equal
reviewer boxes: 30
reviewer states/transitions/targets: 26,214 / 26,214 / 26,214
reviewer components/fixed states: 366 / 366
reviewer assertions: 1,202,599
reviewer control digest: 75f58e8352bf97f6d02178cc37cc2cf194a2ac7ee84a9f1b00a33b313e12cb43
reviewer canonical SHA-256: 4e579cb9e2552fe5703e9d0e2ad5f462e8b822c0751a2531d024f901abeb1881
cold PDF builds: two, byte-identical to both frozen PDFs
cold/frozen PDF SHA-256: 9f1b67680b4c915e5bd60d01730095d5d06817368244d83ecfc84d39a86bf207
post-B cold PDF builds: two, byte-identical to current main.pdf
current PDF: 5 pages / 372,121 bytes
current PDF SHA-256: 682eeced97037b899f91dc2b93afaaf514b6dcbf8f95d1225ddb87f4cce6203b
Round-0/Round-1 preserved PDF SHA-256: 9f1b67680b4c915e5bd60d01730095d5d06817368244d83ecfc84d39a86bf207
```

All four original pages and all five current pages were rasterized and
inspected individually.  All 27
font rows are embedded, subsetted, and Unicode mapped.  No warning, bad box,
unresolved citation/reference, clipping, overlap, missing glyph, malformed
display, unintended blank page, attachment, form, JavaScript, or identifying
PDF metadata was found.

The original Review-A requested delta remains empty.  The later source-only
repair has passed exact nonregression and requires no further change.  The
owner and release gates remain exactly `OWNER_AMBER / HOLD_EXTERNAL`.
