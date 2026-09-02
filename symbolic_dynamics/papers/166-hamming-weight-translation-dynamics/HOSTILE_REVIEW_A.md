# Hostile Review A — Hamming-Weight Translation Dynamics

**Role:** independent Review A; no author code was imported.  
**Frozen input:** anonymous Round 0.  
**Decision:** `ACCEPT`.  
**Findings:** `0 Critical / 0 Major / 0 minor`.  
**Lifecycle:** `HOLD_EXTERNAL`.

## Scope and pinned artifact

The review starts from the literal map

\[
T_n(x)=x+\operatorname{wt}(x)\mathbf 1
\quad\text{on }(\mathbb Z/n\mathbb Z)^n,\qquad n\ge2,
\]

where the weight is the integer number of nonzero coordinates.  The pinned
`main.tex`, `references.bib`, and `main_round0_original.pdf` have SHA-256
values

```
a709e1b8dc6f50059cf85c8a2c922455b7812b24f4e38ebab88c77123f279ce8  main.tex
fcd2132a399ed5d21d75035aaadc234cce79dc4040613a9c5cc54ca9c896c500  references.bib
f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c  main_round0_original.pdf
```

The canonical `main.pdf` has the same PDF hash.  No author file was modified
during this review except for adding this review report.

## Mathematical assessment

The diagonal phase reduction is exact.  For a target `y`, write
`X_j=y-j\mathbf1`, let `m_j` count the coordinates of `y` equal to `j`, and
put `g_m(j)=j+m_j` modulo `n`.  The diagonal action is free and
`T_n^t(X_j)=X_{g_m^t(j)}`.  This proves the stated target-local all-time
preimage oracle, including `t=0`.

Independent derivation also confirms:

- the positive-mass exhaustion argument for all nontrivial cycles;
- `P_{n,1}=1+(n-1)^n` and
  `P_{n,k}=k!\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}` for
  `2\le k\le n`, with the ensuing recurrent and zeta censuses;
- the exact-depth formula
  \[
  D_{n,d}=d!\sum_{s=d}^{n-1}\binom ns
  \left\{\begin{matrix}s\\d\end{matrix}\right\}(n-d-1)^{n-s},
  \]
  the sharp depth cap `n-2`, and the last-shell total
  `(n-1)n!/2` for `n\ge3`;
- the special binary boundary: `T_2` is a permutation and has depth zero;
- the arbitrary-target one-step fibre formula, including the distinct
  integer-weight-zero and integer-weight-`n` branches;
- the marked fibre enumerator, its all-zero correction, and the maximum
  fibre `1+h_n`, where
  `h_n=\lfloor(\sqrt{8n+1}-1)/2\rfloor`, including the triangular-remainder
  construction and equality characterization.

The proofs use only modular arithmetic and labelled occupancy, so composite
`n` introduces no unmentioned field assumption.  The endpoint-zero,
`d=n-1`, `t=0`, sharp-last-shell, and triangular remainder boundaries all
survived explicit attack.

## Findings

### Critical

None.

### Major

None.

### Minor

None.

## Independent computational controls

A standalone reviewer verifier, written without importing the author or
Gate-A code, exhausts the literal functional graphs for `2\le n\le7`, every
target and time through `n=6`, a deterministic 7,000-target extension at
`n=7`, all weak occupancy profiles through `n=11`, the marked enumerator
through `n=30`, triangular-remainder boundaries through `n=256`, and all
one-zero/one-two last-shell placements through `n=64`.

The frozen transcript reports `11,795,304` assertions and `PASS`.  Two fresh
process-separated executions are byte-identical to it.  Reviewer verifier
and transcript hashes are, respectively,

```
2f717ff4cd557e353b94826c85238cff19497d622f4d498b1b549cdc786be4ef
bee2274c898591173b9fdda41b728f627c7dc30faedbf2eea70efee967ecf46d
```

## Ownership and portfolio collision

The bounded owner audit subtracts the exact binary parity-complement map,
classical siteswap/permutation language, occupancy and parking language,
Hamming terminology, Stirling/Fubini identities, and generic finite-map
zeta conversion.  No searched source directly owned the retained `n\ge3`
conjunction of labelled HWT phase dynamics, the complete transient and
last-shell census, and the target-resolved inverse atlas.  This bounded
non-hit is not a novelty or priority claim and remains reopenable.

The P1–P165 audit found no literal duplicate, conjugacy, or proof transfer.
P138 is the closest numerical/theorem silhouette (`n-2` depth and a target
decoder), but its prefix-palindrome XOR update, complement phase, and
sequential inverse mechanism are structurally different.  P128 shares only
translation vocabulary; its mechanism is polynomial-factor erosion.

## Build, PDF, and anonymity QA

Two source-only cold builds, each seeded solely by the pinned source and
bibliography, settled to byte-identical 294,007-byte PDFs with SHA-256
`f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c`.
Both equal the frozen Round-0 PDF.  Final LaTeX and BibTeX scans contain zero
warnings, errors, undefined references, rerun requests, or bad boxes.

The PDF has four A4 pages, blank standard metadata, no encryption, form,
JavaScript, metadata stream, or raster image.  All 24 font rows are embedded,
subsetted, and Unicode mapped.  Extracted text is anonymous, contains the
visible `HOLD_EXTERNAL` lifecycle token, and contains no editing marker or
local path.  All four pages were inspected independently at 144 dpi; no
clipping, overlap, malformed formula, or visual defect was found.

## Recommendation

Accept Round 0 for the next internal pipeline stage without a mathematical,
source, or build repair.  External circulation remains prohibited while the
artifact is marked `HOLD_EXTERNAL`.

Full reviewer evidence is frozen under
`docs/papers162_166_sequence/reviews/p166_a/`.
