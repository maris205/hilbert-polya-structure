# Hostile Review B — Successor Transfer on Set Partitions

**Role:** independent Review B of the repaired live source; the literal map,
all temporal statements, and the every-target fibre formula were rederived
before the author verifier was replayed.  
**Decision:** `MINOR_PACKAGING_REPAIR`.  
**Findings:** `0 Critical / 0 Major / 1 Minor`.  
**Theorem verdict:** `PROVABLE AS STATED`.  
**Lifecycle:** `HOLD_EXTERNAL`.

## Pinned repaired input

```text
0344686ca5f9334f7dd72aaced7cd81b3380c55a5365f534696a47d9a93c3cbb  main.tex
2ac478c62aee40ba723aca350782df7a9c8fbc37429abb419f010a2e4845430e  references.bib
419e91685b4a663fb8ab711abca28517436a2477a92184add424575d8bac77d3  main.pdf
df03b864b47ae963c467831ba7f5b47231663f1e369facf21eee1d468b17c9c2  main_round0_original.pdf
e4566e997ec656f3eaa41fa4f23953773222293cf23189ebd6c7d9a64aab950b  verify_p169.py
e59891873e682c0a271a28197e681f6ba813f394f4104140b02d5eb4e5ce258f  verification_output.txt
```

The repaired PDF is intentionally distinct from the preserved author
Round-0 PDF.  A layout-preserving extracted-text comparison found exactly
the two declared Review-A changes: the lifecycle line now says “anonymous
internal manuscript,” and Ji--Li--Wang is now the 2025 *Annals of
Combinatorics* article rather than an arXiv-only entry.  No theorem, formula,
proof, matrix, example, or ownership subtraction changed.

## Independent mathematical attack

### Canonical block order and the restricted-growth rule

Every donating block retains its minimum because it removes only its maximum,
and every singleton retains its sole element.  For a linear adjacent pair
`i,i+1`, every element entering output block `i+1` is either retained from
the old block `i+1` or is the old maximum of block `i`; either kind is
strictly larger than the old minimum of block `i`.  The new block `i`
contains that old minimum.  Hence adjacent output minima remain strictly
increasing.  The donation `k-1 -> 0` enters the first block and imposes no
false last-to-first order comparison.

In a restricted-growth word, the maximum of a nonsingleton block is exactly
the last occurrence of its repeated letter.  Thus the literal simultaneous
block update is precisely

```text
increment modulo k the final occurrence of every repeated letter.
```

The donating letter retains its first occurrence.  A newly earlier first
occurrence of `i+1` is still later than the first `i`, and wrap to zero is
harmless.  This proves both equivalence with the block rule and preservation
of the same `k`-letter restricted-growth carrier.

### Max-plus cone and load smoothing

Writing `z_i=|B_i|-1` gives directly

```text
z_i(t+1) = z_i(t) - 1[z_i(t)>0] + 1[z_(i-1)(t)>0].
```

For a periodic height lift with `H_i-H_(i-1)=z_i` and
`H_(i+k)=H_i+m`, the update is

```text
H_i(t+1)=max(H_i(t)-1,H_(i-1)(t)),
H_i(t)=max_{0<=r<=t}(H_(i-r)(0)-(t-r)).
```

Setting `X_r=H_(i-r)(0)+r`, the two adjacent maxima share precisely
`X_1,...,X_t`.  Therefore a zero at time `t` can only be created by the new
right endpoint and forces the backward cone sum to be at most `t`; a value at
least two can only be sustained by the old left endpoint and forces that cone
sum to be at least `t+2`.  The inequality directions in the paper are thus
correct.  At `t=m-1` the latter is impossible when `m<=k`; at `t=k-1` the
former is impossible when `m>=k`.  Binary loads rotate, positive loads are
fixed, and both terminal regimes are forward invariant.

### Sparse/dense windows, recurrence, exact counts, and the sharp clock

In the dense case, reverse the final `k` positions.  The first reversed
occurrence of every colour in the window advances, so its occupancy vector
obeys the same queue rule with total mass `k`.  It becomes all ones within
`k-1` further steps, exactly making the final word a permutation.  In the
sparse case every full-word multiplicity is one or two.  Prefix occupancies
belong to `{0,1,2}` with total `k`; each excess represented by a two moves
clockwise through ones to the first unmatched hole.  Cyclic-order pairing of
equally many excesses and holes proves the claimed `k-1` ceiling.  The
restricted-growth condition then forces the first permutation to be
`01...(k-1)`.  Both labelled window forms are invariant.

A periodic point must already be in the forward-invariant smoothed regime
and then in the appropriate invariant window.  Conversely, every displayed
dense or sparse form is preserved and its nonempty final word is incremented
componentwise modulo `k`.  No positive shift smaller than `k` fixes a
coordinate, so every nontrivial recurrent state has exact period `k`.  The
counts are consequently

```text
dense:  k! S(n-k,k),
sparse: (k)_(n-k),
```

with the two descriptions agreeing as `k!` when `n=2k`.  The fixed strata
`k=1` and `k=n`, and the `n=1,2` boundaries, also agree with the theorem.

The word `0^(m+1)12...(k-1)` realizes both phase ceilings.  Its printed load
trajectory prevents smoothing before `min(m,k)-1`.  In the sparse range the
prefix particle/hole trajectory needs exactly `k-1` more steps; in the dense
range the explicit suffix trajectory first becomes a permutation at that
same time.  Hence the stratum maximum is exactly
`min(n-2,2k-2)`, and choosing `k=n-1` gives the global `n-2` clock.

### Five-state trace, singleton rows, wrap, and interlacing

For a fixed target `C`, a predecessor supplies a cyclic token `x_i`: the
donated maximum lying in `C_(i+1)`, or absence when source block `i` was an
inactive singleton.  Reconstruction is forced by

```text
B_i = (C_i minus x_(i-1)) union x_i.
```

After deleting the incoming token, an absent outgoing token is admissible
exactly when the remainder has size one.  A present outgoing token is
admissible exactly when the remainder is nonempty and the selected label is
strictly larger than its maximum.  Deletion type affects only size, minimum,
and maximum; all interior deletions have the same retained extrema.  The five
states `(absent, sole, minimum, maximum, interior)` therefore retain all
future data, while the threshold entry counts the exact number of outgoing
labels within a type.

For `i<k-1`, the `K_i` factor is precisely the comparison of adjacent
retained source minima.  At `i=k-1` it must be one: the matrix trace closes
the donation token from the last block into `C_0` but canonical order has no
last-to-first minimum comparison.  Each contributing labelled trace path
constructs one source and each source recovers its unique path, proving the
formula including zero fibres.  Deleting the sole element of a singleton
correctly zeros its present-token row; the all-singleton target instead has
the unique all-absent path.

The reviewer reconstruction gives

```text
T^(-1)(025|134) = {023|145, 024|135},
T^(-1)(035|124) = {034|125}.
```

Its independently generated matrices are exactly the four printed matrices,
with traces two and one.  Thus the row/column orientation is correct and the
claimed interior-label interlacing really survives after the common ordered
size/minimum/maximum data are fixed.

No reversed cone inequality, missing recurrence converse, premature sharp
witness, period divisor, state-orientation error, singleton exception, or
wrap condition was found.

## Exact-control attacks

### Author control replay

One fresh standard-library process reran the unchanged paper-local verifier.
Its 1,785-byte stdout matched `verification_output.txt` byte for byte:

```text
assertions: 1,217,025
verifier SHA-256:  e4566e997ec656f3eaa41fa4f23953773222293cf23189ebd6c7d9a64aab950b
transcript SHA-256: e59891873e682c0a271a28197e681f6ba813f394f4104140b02d5eb4e5ce258f
decision: AUTHOR_ROUND0_PASS
```

### Reviewer-owned independent control

Review B supplies a separate standard-library verifier at
`docs/papers167_171_sequence/reviews/p169_b/verify_review_b.py`.  It imports
no author or scouting code and generates the carrier directly as canonical
tuples of blocks; its restricted-growth implementation is a separately
computed coordinate view.  Two fresh processes matched each other and the
reviewer canonical transcript byte for byte:

```text
assertions: 8,698,292
verifier SHA-256:  f0c6c7832138a88e3abb340c8491e2b64005f4c71918ce4241ea9b5582811dcc
canonical SHA-256: 5ff755c5d6148a98f2494c6fef5d3ade8e671fc12cb1bdba6268d6611578a133
decision: REVIEW_B_INDEPENDENT_CONTROL_PASS
```

The independent control exhausts every carrier and edge through `n=9`,
checks complete fibres three ways through `n=8` (literal source map,
five-state trace, and direct cyclic-token reconstruction), checks 203,481
max-plus load vectors, and follows the sharp family over all 1,711
nontrivial strata through `n=60`.  It also freezes the four interlacing
matrices and a wrap witness on which adding the false cyclic order comparison
changes the correct fibre one to zero.

| `n` | states | image | max fibre | global H | exact-period census |
|---:|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 1 | 0 | `1:1` |
| 2 | 2 | 2 | 1 | 0 | `1:2` |
| 3 | 5 | 4 | 2 | 1 | `1:2, 2:2` |
| 4 | 15 | 9 | 3 | 2 | `1:2, 2:2, 3:3` |
| 5 | 52 | 28 | 6 | 3 | `1:2, 2:6, 3:6, 4:4` |
| 6 | 203 | 95 | 8 | 4 | `1:2, 2:14, 3:6, 4:12, 5:5` |
| 7 | 877 | 359 | 16 | 5 | `1:2, 2:30, 3:36, 4:24, 5:20, 6:6` |
| 8 | 4,140 | 1,499 | 22 | 6 | `1:2, 2:62, 3:150, 4:24, 5:60, 6:30, 7:7` |
| 9 | 21,147 | 6,780 | — | 7 | `1:2, 2:126, 3:540, 4:240, 5:120, 6:120, 7:42, 8:8` |

Here `H` is the maximum tail.  Enumeration is hostile falsification
evidence; the all-parameter verdict above follows from the independent
derivation rather than extrapolation from these ranges.

## Review-A repair, source, and ownership audit

The Review-A source repair is correct.  DOI content negotiation resolves
`10.1007/s00026-025-00760-3` to David Ji, Michael Li, and Daniel Wang,
“Periods and Atomic Firing Sequences of Parallel Chip-Firing Games on
Directed Graphs,” *Annals of Combinatorics* 29(4), 1155--1175 (2025).  The
primary arXiv record `2407.15889` has the same title and authors and remains
valid auxiliary metadata.  The repaired bibliography and rendered reference
match those data.

The other journal DOI records and the two primary arXiv surfaces were
independently resolved.  The Wachs, Joseph--Propp--Roby, Brandt,
Schützenberger, Striker--Williams, Takahashi--Satsuma, and Choi--Gan--Li--Zhu
titles, authors, venues, dates, volumes, and pages agree with the source
ledger.  The known machine-record truncation of Brandt's terminal page is
already disclosed rather than silently propagated.  All eight bibliography
entries are cited and no placeholder remains.

The manuscript explicitly assigns restricted-growth encoding and whirling,
the full directed-cycle chip-firing/load mechanism, solitaire,
promotion/rowmotion, box--ball dynamics, set-partition stack sorting,
Stirling enumeration, and generic matrix algebra zero contribution credit.
The bounded literal-owner non-hit is not used for novelty, priority, or
release permission.  No additional source or ownership repair was found.

## Source-only build, PDF, and anonymity audit

Two Review-B cold directories began with only repaired `main.tex` and
`references.bib`.  The explicit sequence `pdflatex`, `bibtex`, `pdflatex`,
`pdflatex` produced the live PDF byte for byte in both directories:

```text
cold build 1: 419e91685b4a663fb8ab711abca28517436a2477a92184add424575d8bac77d3
cold build 2: 419e91685b4a663fb8ab711abca28517436a2477a92184add424575d8bac77d3
live main.pdf: 419e91685b4a663fb8ab711abca28517436a2477a92184add424575d8bac77d3
```

Both final cold logs and all retained Review-A settled logs have zero actual
warnings, bad boxes, unresolved citations/references, rerun requests, or
fatal errors.  The live PDF has five A4 pages and 392,380 bytes.  All 28 font
rows are embedded, subsetted, and Unicode mapped.  It is unencrypted, has no
form, JavaScript, attachment, custom metadata, or metadata stream, and has
blank title, subject, keywords, author, creator, and producer fields.
Extracted text contains no email, filesystem path, affiliation,
acknowledgment, review marker, or unresolved token.

All five pages were independently rendered at 144 dpi.  The theorem split,
max-plus cones, sharp trajectories, two five-state tables, boxed entry rule,
four numerical matrices, predecessor lists, lifecycle line, and repaired
bibliography are legible.  No clipping, collision, overflow, malformed
glyph, or orphan page was found.  The visible byline and running heads remain
anonymous.

## Findings

### Critical

None.

### Major

None.

### Minor

**M1 — The repaired live artifact has not yet received its post-review
documentation and integrity closeout.**  `BUILD.md` explicitly says this
step was deferred until Review B, so the condition is workflow-local rather
than evidence of a faulty build.  Nevertheless, the current unqualified
`SHA256SUMS` fails on ten repaired or regenerated entries:
`BUILD.md`, `PAPER_PLAN.md`, `SOURCE_VERIFICATION.md`, `main.aux`, `main.bbl`,
`main.blg`, `main.log`, `main.pdf`, `main.tex`, and `references.bib`.  It also
omits the Review-A additions.  Separately, `README.md` still calls live
`main.pdf` the canonical Round-0 PDF, gives its old 392,917-byte / `df03b...`
hash, and says the directory contains no review artifact; the historical
`SELF_QA.md` still compares that live pathname byte-for-byte with the
preserved Round-0 copy.

This is one localized packaging inconsistency, not a theorem, source,
build-reproducibility, PDF, or anonymity failure.  Finalization should retain
`main_round0_original.pdf` at `df03b...`, identify the repaired live PDF as
392,380 bytes / `419e91...`, update the live pointers, and regenerate the
manifest only after the Review-B report is present.

## Recommendation

Accept every theorem and the Review-A source repair without weakening or
changing the manuscript.  Apply M1 as a documentation/integrity closeout,
preserve the immutable Round-0 PDF, require a clean paper-local checksum
replay, and then freeze the repaired artifact.  External status remains
`HOLD_EXTERNAL`; this review grants no posting or submission permission.
