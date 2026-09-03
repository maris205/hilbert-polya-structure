# Hostile Review B — Minimum Inverse-Position Feedback

**Role:** independent Review B of the repaired live source; all theorem,
boundary, and fibre arguments were rederived from the literal map before the
author verifier was replayed.  
**Decision:** `MINOR_PACKAGING_REPAIR`.  
**Findings:** `0 Critical / 0 Major / 1 Minor`.  
**Theorem verdict:** `PROVABLE AS STATED`.  
**Lifecycle:** `HOLD_EXTERNAL`.

## Pinned repaired input

```text
500fdea81499204a92bd3b6e24c5f9fd7b758d29b5c5dcdbf60e5e3f8e861d73  main.tex
436404931cadf9818e01c18497196d1d6c02b94df7089abb906e126dc71f4266  references.bib
b32b14735d21a4354b7dfc242a98bb7a137d6ae1f5552fe0a4ea623500ad53b9  main.pdf
81bfa2ed4944f2750558f06cbb3a09d7081fc0361a0361f05f91869368faf379  main_round0_original.pdf
b7c10bd3738362397a97361ca3780c4f53c7297efbe3e1885175634b345b457b  verify_p167.py
1e7348f9eab389cffc14582b3cf26ebeec69cb72a6c77dbdb1fb204abd1e1a8c  verification_output.txt
```

The live repaired PDF is intentionally distinct from the preserved Round-0
PDF.  Extracted-text comparison shows exactly the two declared Review-A
changes: the lifecycle phrase is round-independent, and the
Flajolet--Odlyzko publication year is 1990 rather than 1989.  No theorem,
formula, proof, table entry, or credit boundary changed.

## Independent mathematical attack

Start with the literal identity-default selector

```text
M(f)(i) = min{j : f(j)=i} if i is present, and i otherwise.
```

The following derivation was performed independently of the author
verifier.

### First-image structure and component action

For distinct present symbols, their least occurrence positions are distinct.
Thus the off-diagonal values of every first image are injective.  In its
functional digraph each vertex has at most one incoming nonloop edge.  A
nonloop cycle therefore has no attached tree, while a loop can have only one
incoming chain.  The claimed cycle/loop-rooted-path decomposition is
complete.

For a path in root-to-leaf order `P=(p_0,...,p_{s-1})`, the word representing
the path contains `p_0` at positions `p_0,p_1`, contains `p_j` at position
`p_{j+1}` for `1<=j<=s-2`, and omits `p_{s-1}`.  Taking least positions gives
exactly the displayed dichotomy: reverse the whole path when `p_0>p_1`, or
fix `p_0` as a singleton and reverse the remainder when `p_0<p_1`.  A cycle
has one occurrence of each symbol and is sent to its inverse orientation.
All new values remain in the same labelled component, so components cannot
merge and a split cannot be undone.

### Recurrence and the two sharp clocks

A nonsingleton path is recurrent only if its first step reverses and the
reversed path also reverses.  These are precisely
`p_0>p_1` and `p_{s-1}>p_{s-2}`; the incompatible size-two boundary correctly
gives no recurrent path.

For a nonrecurrent path, a failed first inequality removes the root after one
step, whereas a satisfied first inequality followed by a failed final
inequality removes the old leaf after two steps and leaves the original
prefix.  Induction gives tail at most `2s-2`.  Equality forces the two-step
branch at every deletion and hence the unique decreasing order; conversely
that order realizes equality.

Every first image contains the coordinate value zero, since the symbol at
source position zero has first occurrence zero.  The unique full-label path
with tail `2n-2` is the decreasing path, whose coordinate values omit zero,
so it is not a first image.  Every other full path has integral tail at most
`2n-3`, and every smaller component has tail at most `2n-4`.  The source
`(1,2,...,n-1,1)` maps to the increasing full path of tail `2n-3`, yielding
both sharp maxima, including the `n=2` boundary.

### Recurrent census, fixed iterates, and zeta

On an `s`-set, directed cycles contribute `(s-1)!`.  Recurrent paths
contribute zero at `s=2`, two at `s=3`, and `s!/4` for `s>=4`: in the latter
range the two endpoint comparisons concern disjoint pairs, and swapping
either pair quarters all orders.  Together with the singleton boundary this
reproduces the stated `c_s`.  Labelled set assembly gives

```text
(1-x)^(-1) exp(x^3/3 + x^4/(4(1-x))).
```

Cycle inversion fixes only loops and two-cycles; a nonsingleton recurrent
path is exchanged with its distinct reversal.  Fixed states are therefore
exactly involutions.  Every other recurrent state lies on a two-orbit, so the
odd/even fixed-iterate counts and the two-factor zeta formula follow without
an additional dynamical assumption.

### Every-target fibre and Bell ceiling

For a target `g`, each off-diagonal coordinate forces a present symbol and
its first position.  Repeated forced positions make the fibre empty.  A fixed
coordinate may be absent or may open at itself, except when that position is
already occupied by another forced symbol.  After choosing the optional
fixed symbols, each unforced source position independently accepts exactly
the symbols whose forced first positions are earlier.  This proves every
factor and every zero case in `Phi_n(g)`, as well as its converse; the product
is an exact image-membership test, not just a necessary condition.

For a fixed target and a fixed kernel partition, a block with minimum `j`
has only one possible label: the unique off-diagonal `i` with `g(i)=j`, if it
exists, and otherwise `j`.  Hence at most one source occurs per set
partition.  Labelling every block by its minimum realizes all partitions
over the identity.  The Bell ceiling is therefore exact, with no need for a
uniqueness claim about the maximizing target.

No reversed inequality, missed size-one/two boundary, unsupported converse,
or hidden dependence on an arbitrary missing-symbol completion was found.

## Exact-control attacks

### Author control replay

One fresh process reran the unchanged paper-local verifier.  Its 9,831-byte
stdout matched `verification_output.txt` byte for byte and retained
`12,603,676` assertions:

```text
verifier SHA-256:  b7c10bd3738362397a97361ca3780c4f53c7297efbe3e1885175634b345b457b
transcript SHA-256: 1e7348f9eab389cffc14582b3cf26ebeec69cb72a6c77dbdb1fb204abd1e1a8c
decision: AUTHOR_ROUND0_PASS
```

### Reviewer-owned independent control

Review B also supplies a separate standard-library verifier at
`docs/papers167_171_sequence/reviews/p167_b/verify_review_b.py`.  It imports
no author or scouting module.  Two fresh processes matched each other and
the reviewer canonical transcript byte for byte:

```text
assertions: 1,670,407
verifier SHA-256:  d3d914b9de5eab4a3277fb952fcb7709603c505b0602f098a76b608461121a8d
canonical SHA-256: e3ee4873a81dc629357554470c45900ef1fe71a24e78997ad9c4206af660cac4
decision: REVIEW_B_INDEPENDENT_CONTROL_PASS
```

It exhausts the complete carrier, complete edge map, and every target fibre
for `1<=n<=6`; checks every point under positive iterates `1<=k<=4`; checks
every labelled path and canonical directed cycle through size nine; and
compares the connected recurrence with the displayed EGF through order 16.
The independently reconstructed full rows are:

| `n` | states | image | recurrent | fixed | full H | image H | max fibre |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| 2 | 4 | 3 | 2 | 2 | 2 | 1 | 2 |
| 3 | 27 | 14 | 8 | 4 | 4 | 3 | 5 |
| 4 | 256 | 84 | 38 | 10 | 6 | 5 | 15 |
| 5 | 3,125 | 612 | 220 | 26 | 8 | 7 | 52 |
| 6 | 46,656 | 5,220 | 1,540 | 76 | 10 | 9 | 203 |

For path sizes one through nine, the recurrent-path counts were
`1,0,2,6,30,180,1260,10080,90720`; the maximum tails were
`0,2,4,6,8,10,12,14,16`, always with the unique claimed maximizer.
Enumeration is used only as hostile falsification evidence; the uniform
proof verdict above is independent of these finite ranges.

## Review-A repair and source audit

Review A's sole finding is correctly implemented.  The Springer primary
record for DOI `10.1007/3-540-46885-4_34` cites the chapter as 1990 and gives
copyright 1990, while the proceedings title remains *EUROCRYPT '89*.
`references.bib` now uses `year={1990}`, and `SOURCE_VERIFICATION.md`
explicitly explains why the stable key still contains `1989`.

The other four bibliography records were rechecked on their DOI/publisher
surfaces.  The 2026 Annals of Combinatorics record explicitly identifies
restricted growth functions with unordered set partitions; the
transformation-semigroup records support the cited transversal/inverse
background; and the Artin--Mazur record supports the zeta terminology.  All
five bibliography entries are cited, and no placeholder or uncited record
remains.

The manuscript visibly assigns the transversal, inverse-matching,
first-occurrence/RGF, set-partition, functional-digraph, involution, Bell,
labelled-set, and zeta ingredients zero contribution credit.  The bounded
owner non-hit is not promoted to novelty, priority, or circulation
permission.  No source or ownership repair beyond Review A was found.

## Source-only build, PDF, and anonymity audit

Two Review-B cold directories began with only the repaired `main.tex` and
`references.bib`.  The explicit sequence `pdflatex`, `bibtex`, `pdflatex`,
`pdflatex` produced the same live PDF in both directories:

```text
cold build 1: b32b14735d21a4354b7dfc242a98bb7a137d6ae1f5552fe0a4ea623500ad53b9
cold build 2: b32b14735d21a4354b7dfc242a98bb7a137d6ae1f5552fe0a4ea623500ad53b9
live main.pdf: b32b14735d21a4354b7dfc242a98bb7a137d6ae1f5552fe0a4ea623500ad53b9
```

Both final cold logs and the retained Review-A settled log have zero
warnings, bad boxes, unresolved citations/references, rerun requests, or
fatal errors.  The live PDF has four A4 pages and 285,799 bytes.  All 21 font
rows are embedded, subsetted, and Unicode mapped.  It is unencrypted, has no
form or JavaScript, and has blank title, subject, keyword, author, creator,
and producer metadata fields.  Extracted text contains no email, filesystem
path, affiliation, acknowledgment, or unresolved marker.

All four pages were independently rendered at 144 dpi.  The title, theorem,
table, equations, proof endings, lifecycle line, and repaired bibliography
are legible; no clipping, collision, overflow, malformed glyph, or orphaned
heading was found.  The visible byline and running heads remain anonymous.

## Findings

### Critical

None.

### Major

None.

### Minor

**M1 — Live repaired artifact pointers and integrity manifest remain on the
Round-0 values.**  The repair workflow intentionally preserved
`main_round0_original.pdf` and deferred final packaging until Review B, as
the addendum in `BUILD.md` explains.  Nevertheless, the current `README.md`
still calls `main.pdf` the byte-identical Round-0 artifact and gives the old
`81bfa2...` rebuild hash; the historical `SELF_QA.md` makes the same pathname
comparison; and the unqualified `SHA256SUMS` now fails for eight changed
entries (`BUILD.md`, `SOURCE_VERIFICATION.md`, `main.aux`, `main.bbl`,
`main.log`, `main.pdf`, `main.tex`, and `references.bib`) while omitting the
review/repair additions.

This is a localized post-review packaging inconsistency, not a theorem,
source, PDF-build, or anonymity failure.  Finalization should distinguish the
immutable Round-0 copy from the repaired live artifact, replace the live PDF
bytes/hash with `285,799` and `b32b147...`, and regenerate a paper-local
manifest only after all review files are present.

## Recommendation

Accept the mathematics and the Review-A source repair without weakening or
changing any theorem.  Apply M1 as a documentation/integrity closeout,
preserve `main_round0_original.pdf` under its original hash, rerun the
paper-local checksum check, and then freeze the repaired artifact.  External
status remains `HOLD_EXTERNAL`; this review grants no posting or submission
permission.
