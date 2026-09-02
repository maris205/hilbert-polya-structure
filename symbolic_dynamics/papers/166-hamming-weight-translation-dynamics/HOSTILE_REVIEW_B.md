# Hostile Review B — Hamming-Weight Translation Dynamics

**Role:** fresh independent Review B, begun from the literal map rather than
the author or Review-A proof/verifier.  
**Frozen input:** anonymous Round 1 (`main.tex`, `references.bib`,
`main_round1.pdf`).  
**Decision:** `ACCEPT_INTERNAL`.  
**Findings:** `0 Critical / 0 Major / 0 minor`.  
**Lifecycle:** `HOLD_EXTERNAL`.

## Frozen object

```text
a709e1b8dc6f50059cf85c8a2c922455b7812b24f4e38ebab88c77123f279ce8  main.tex
fcd2132a399ed5d21d75035aaadc234cce79dc4040613a9c5cc54ca9c896c500  references.bib
f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c  main_round1.pdf
```

`main.pdf` is byte-identical to the frozen Round-1 PDF.  Review B did not
modify an author source, bibliography, verifier, PDF, or build ledger.

## Mathematical verdict

The exact diagonal phase reduction is correct.  If `m_j` is the multiplicity
of residue `j` in a target `y` and `X_j=y-j1`, then `X_j` has weight
`n-m_j`, whence

\[
T_n(X_j)=X_{j+m_j},\qquad
|(T_n^t)^{-1}(y)|=\#\{j:g_m^t(j)=0\}.
\]

This remains valid at `t=0`.  On a nontrivial phase cycle the positive
increments sum to a positive multiple of `n` bounded by the total occupancy
mass `n`, so they sum to exactly `n`; this proves support exhaustion and the
clockwise-gap description.  Independent labelled-composition summation then
recovers

\[
P_{n,1}=1+(n-1)^n,
\qquad P_{n,k}=k!S(n,k)\quad(2\le k\le n),
\]

the recurrent count, fixed-iterate divisor sums, and the zeta product.

For exact depth `d`, anchoring each literal state at phase zero gives an
ordered positive increment composition of total `s<n`, one forced empty
endpoint, and `n-d-1` available residual bins.  This directly yields

\[
D_{n,d}=d!\sum_{s=d}^{n-1}{n\choose s}S(s,d)
(n-d-1)^{n-s}.
\]

This independent count resolves the possible anchor-factor hazard: in the
equivalent phase-pair argument the `n` lifted starting phases and the `n`
representations of every literal state cancel exactly.  The strict no-wrap
bound gives maximum depth `n-2`.  At the last shell it forces one zero, one
two, and all remaining entries one, with exactly the stated exceptional
second phase; the count `(n-1)n!/2` follows.

For a target `y`, any source is `y-k1`.  Separating the congruent shifts from
integer weights zero and `n` gives exactly

\[
|T_n^{-1}(y)|=1_{y=0}+1_{m_0=0}
+\sum_{k=1}^{n-1}1_{m_k=n-k}.
\]

This separation confirms the all-zero correction.  Direct exponential
marking recovers the displayed EGF.  The sum of `h` distinct prescribed
positive counts is at least `1+...+h`, proving the upper bound for the
maximum fibre; the paper's remainder construction realizes it in both the
triangular and nontriangular cases.

Focused attacks on `n=2`, `n=3`, `d=n-2`, `t=0`, all-zero targets, composite
`n=4,6`, the exact anchor factor, and the triangular boundary produced no
counterexample or omitted case.

## Findings

### Critical

None.

### Major

None.

### Minor

None.

## Independent computation

A new standard-library verifier imports no author, Gate-A, or Review-A code.
It exhausts every literal state through `n=7`, every target and multiple times
through `n=6`, every weak occupancy profile through `n=10`, and larger
last-shell and triangular-boundary controls.  Its frozen transcript reports
`14,005,344` assertions and `PASS`.

```text
verifier SHA-256: bd00021b6e802fd1fac7654697df826f7d1b0890051910010e5531d2cd06c5cd
canonical SHA-256: cca342885005ce13989fcd93e8f224b92eae2d13a87856b19cbef9880d7df689
fresh byte-identical process replays: 2/2
```

The author verifier was additionally replayed twice as a regression control;
both runs matched its `17,017,929`-assertion canonical transcript byte for
byte.

## Ownership and portfolio collision

Fresh bounded searches subtract Hamming terminology, the exact binary
boundary, siteswap landing permutations and gap vectors, occupancy/parking
language, mapping parking, ordered-Bell parking connections, Stirling and
multinomial identities, and finite-map zeta conversion.  Siteswap directly
owns the recurrent `j+a_j` permutation slice, but not the literal Hamming-
weight map, its transient shells, or its target inverse atlas.  Mapping and
unit-interval parking likewise own neighbouring language/enumeration, not the
retained dynamical conjunction.  No direct owner was found; this bounded
non-hit is not a novelty or priority claim.

P128 shares translation/depth/fibre vocabulary but uses polynomial-factor
erosion and an Euler-product engine.  P137 shares state-dependent feedback,
triangular numbers, and fibres but uses partition splitting.  P138 is the
closest silhouette because it also has depth `n-2` and target inverse data;
its prefix-palindrome XOR rule, complement normalization, forced zero-prefix
growth, and sequential decoder do not transfer the present occupancy/mass-
exhaustion proofs.  No literal, conjugacy, or two-axis proof-engine collision
was found across P1--P165.

## Build and artifact QA

Two distinct fresh directories, each initially containing only the pinned
source and bibliography, completed the full PDFLaTeX/BibTeX build.  Both
settled PDFs are 294,007 bytes, have SHA-256
`f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c`,
and match Round 1 byte for byte.  Both settled logs have zero genuine
warnings, errors, undefined citations/references, rerun requests, or bad
boxes.

The PDF has four A4 pages, blank standard metadata, no metadata stream,
encryption, form, or JavaScript.  All 24 font rows are embedded, subsetted,
and Unicode mapped; all 6 references are visible.  Extracted text is
anonymous and contains no personal or workspace residue.  The lifecycle
token `HOLD_EXTERNAL` is visibly present.  Independent 144-dpi inspection of
all four pages found no clipping, overlap, missing glyph, malformed display,
or other visual defect.

## Recommendation

Accept Round 1 for the next internal pipeline stage with no repair request.
The ownership conclusion is deliberately bounded and external circulation
remains prohibited under `HOLD_EXTERNAL`.

Full Review-B evidence is frozen under
`docs/papers162_166_sequence/reviews/p166_b/`.
