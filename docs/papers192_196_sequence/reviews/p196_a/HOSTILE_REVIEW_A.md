# P196 hostile Review A

**Reviewer relation:** process-separated internal Reviewer A; did not author
P196 and did not import or reuse its verifier.  
**Frozen input:** Round-0 sources, author controls, and identical frozen PDF are
pinned in `PINNED_INPUTS.sha256`.  
**Decision:** `ACCEPTED_NO_CHANGE` (`0 Critical / 0 Major / 0 Minor`).  
**Mathematical decision:** `PROVABLE_AS_STATED`.  
**External state:** `OWNER_AMBER / HOLD_EXTERNAL`.

## Outcome first

The full theorem package survived an independent hostile reconstruction.  The
literal map was evaluated on every word for `2 <= q <= 5` and `1 <= m <= 7`,
covering 123,032 transitions and every labelled target fibre.  The observed
image is exactly the claimed cyclic descent language, and the map on that
language is exactly left rotation.  Direct orbit tests agree with every
fixed-iterate and least-period formula.

The reviewer did not accept the manuscript's row-operation sketch as the only
support for the characteristic polynomial.  The identity was rederived by a
rank-one determinant lemma, and a separate executable control computed the
full determinant by the Leibniz formula through `q=8`.  The target gap factor
was independently obtained by counting weak chains with a terminal cutoff and
was also checked by direct enumeration, including `d=1`.  The degenerate
cyclic length `m=1` was checked separately: the core consists only of the
all-top word and its fibre consists of the `q` constant words.

No source, owner, build, or presentation defect crossed the finding threshold.
This is an internal mathematical and production acceptance only.  It is not a
novelty, priority, completeness, or freedom-to-operate statement.

## Hostile mathematical attacks

- **Image orientation:** the forward implication was reconstructed from
  `y_(i+1)<M`, not inferred from finite data.  It forces
  `x_(i+1)>x_(i+2)` and hence `y_i>y_(i+1)`.  Conversely, applying `T` to a
  legal target gives left shift, and shift invariance supplies the explicit
  preimage `S^{-1}y`.
- **Tail convention:** periodic points must lie in the image.  The image is a
  permuted core, so legal states have depth zero and all other states depth
  one.  This was tested with first-entry time, not number of distinct states
  visited.
- **Fixed state boundary:** a shift-fixed core word is constant, while a
  constant core word must be all top.  Thus the fixed-state count is one for
  every allowed `q,m`, including `m=1`.
- **Spectrum:** closed walks in the independently built adjacency matrix count
  the core.  Words fixed by `S^r` reduce to closed words of length
  `gcd(m,r)`.  Direct iterate tests through `r=2m` and direct least-period
  classification agree with trace and Möbius inversion.
- **Characteristic polynomial:** a rank-one update calculation gives
  `lambda^q-(lambda+1)^(q-1)` without the author's row operations.  A second,
  algorithmically different Leibniz determinant check and the resulting trace
  recurrence agree through `q=8`.
- **Fibre orientation:** incoming arrows were accumulated from the literal
  map before the formula was evaluated.  Targets outside the language have
  fibre zero; the all-top target has exactly `q` constant sources; every other
  fibre is the claimed product over cyclic gaps.
- **Gap endpoints:** the direct weak-chain control checks all
  `2 <= q <= 7`, all nontop `a,b`, and `1 <= d <= 7`.  At `d=1` the factor is
  exactly the legal strict-descent indicator.  A single-nontop-site gap of
  length `m` is included, so the cyclic wrap does not duplicate or omit a
  variable.
- **All-time fibres and mass:** `T^t=S^(t-1)T` follows after the first image
  hit; rotating the target gives the asserted inverse formula.  Summing all
  independently accumulated indegrees gives `q^m` in every box.

## Verifier and build record

```text
author replay: PASS, byte-equal to its frozen canonical transcript
reviewer replay 1: PASS, byte-equal
reviewer replay 2: PASS, byte-equal
reviewer boxes: 28
reviewer transitions/targets: 123,032 / 123,032
reviewer assertions: 370,380
reviewer digest: f382efcbf3d3bcf0886753db89f27b174817d6351c49cb5547a174268b482122
cold PDF builds: two, byte-identical
cold/frozen PDF SHA-256: bb0ee2d7e155bd515a250fe1c84146fcea3d2586b903fd5a71ecedb1a3d34948
```

All three pages were rasterized and inspected.  Fonts are embedded,
subsetted, and Unicode mapped.  No warning, bad box, unresolved reference or
citation, clipping, overlap, missing glyph, broken display, or unintended
blank page was found.

The accepted delta is empty.  The owner and release gates remain exactly
`OWNER_AMBER / HOLD_EXTERNAL`.
