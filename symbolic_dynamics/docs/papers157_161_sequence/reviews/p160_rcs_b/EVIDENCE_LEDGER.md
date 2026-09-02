# P160 RCS — independent Review-B evidence ledger

## Frozen object

- PDF: `papers/160-rectangular-corner-stripping-atlas/main_round1.pdf`
- SHA-256: `3bbbb6f3243171d612f86a17cd88b58f56bc5ec80c3533dc30464343931def03`
- Size: 294,530 bytes
- Format: PDF 1.5, four A4 pages, unencrypted.
- Reviewed mathematical sources: `main.tex`, the frozen replacement theorem
  contract, and the frozen PDF.  The independent verifier below imports no
  author or earlier-review code.

## Independent exact verifier

Program: `verify_p160_review_b.py`

SHA-256:

```text
589a737b8371e46aba51caabbb431fb00b4ab9531fc4bd48805eb2cc62adeea9
```

It independently generates all 18,460 partitions of weights 0 through 28
and performs 11,287,366 exact assertions:

```text
partition_engine                              73,840
iterates_clocks_heights_conjugation        2,068,432
fibres_empty_branch_artificial_boundaries  8,602,762
support_caps_repaired_witness                  6,726
t_zero_recovery_mass                          535,606
TOTAL                                      11,287,366
```

Coverage includes:

- literal repeated updates versus the closed iterate for `t=0,...,5`;
- asymmetric ordered pairs `(1,2),(2,1),(1,3),(3,1),(2,3),(3,2)` as well as
  symmetric controls;
- literal entry clocks, survival cells, cap heights, and sharp rectangular
  witnesses for every cap through 28;
- conjugation with the parameter order swapped;
- nonempty target fibres for every target partition through weight 28 and
  every source weight through 28;
- the empty fibre separately;
- artificial `(h,w)` boundaries `(0,0),(0,1),(0,4),(1,0),(4,0)`, plus nine
  two-sided pairs;
- a direct decode/rebuild test of the top-excess/forced-middle/bottom
  bijection for every enumerated nonempty fibre source;
- caps, exact support intervals, the repaired `gamma=(d), beta=empty`
  witnesses, the identity-time singleton fibre, all three recovery probes,
  and the coefficientwise mass identity.

Two clean executions are byte-for-byte identical:

```text
b6034231aa620d0de80a56bfcda69f8ddfe047e343498896426699252b918b8a  VERIFIER_RUN_1.txt
b6034231aa620d0de80a56bfcda69f8ddfe047e343498896426699252b918b8a  VERIFIER_RUN_2.txt
```

Both end in `assertions=11287366` and `result=PASS`.

## Boundary finding for the repaired witness

For the theorem's support assertion, `a,b>=1` and `t>=1`, hence
`h=at>=1`.  Given excess `d`:

- `d=0`: take `gamma=empty`, `beta=empty`;
- `d>0`: take the one-part partition `gamma=(d)` and `beta=empty`.

The length of `(d)` is one, so it is at most every legal `h`; its part size is
unrestricted.  After zero padding, the reconstructed top block is

```text
(mu_1+w+d, mu_1+w, ..., mu_1+w),
```

followed by `(mu_1+w,...,mu_r+w)`.  It is a partition, has weight
`M_(h,w)(mu)+d`, and crops to `mu`.  Thus the repair is valid at `h=1`, at
`d=0`, for asymmetric parameters, and for every genuine `t>=1` boundary.

The artificial boundary check is also informative but is not a paper claim:
when `h=0<w`, `gamma=(d)` is unavailable and every degree is instead supplied
by `beta=(1^d)`; when `h=w=0`, only degree zero occurs.  The manuscript
correctly restricts the every-weight sentence to `t>=1` and treats `t=0` as
an exact-weight singleton.

## Source-only cold builds

Two fresh temporary directories received only `main.tex` and
`references.bib`.  Each ran

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Both output PDFs are byte-identical to each other and to the frozen PDF:

```text
3bbbb6f3243171d612f86a17cd88b58f56bc5ec80c3533dc30464343931def03
```

The two final-pass logs are byte-identical (SHA-256
`53f1e914743cc9ec116ca5fc85ba009babc93de3c14924b9a502e767f0b2bf3f`)
and contain no LaTeX/package warning, undefined reference, undefined
citation, overfull box, underfull box, or TeX error.  The two BibTeX logs are
byte-identical (SHA-256
`7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9`)
and contain no diagnostic.  The retained logs are in this directory.

## PDF, font, anonymity, citation, and visual QA

- `pdfinfo`: blank title, subject, keywords, and author metadata; no custom
  metadata, JavaScript, forms, or encryption.
- `pdffonts`: 22 font records, all embedded, subset, and Unicode-mapped.
- `pdftotext`: clean extraction (241 lines, 2,159 words); no `??`, TODO,
  FIXME, draft marker, email, personal acknowledgement, funding statement,
  or named manuscript author.  Names occurring in the reference list are
  bibliographic and expected.
- The visible byline is `ANONYMOUS`.
- All five bibliography records are cited; the settled PDF has no unresolved
  citation marker.
- All four pages were rendered independently at 144 dpi and inspected.  No
  clipping, overlap, orphaned display, illegible table cell, broken glyph,
  excessive whitespace, or margin excursion was observed.

## Owner/source subtraction

The following are treated as positive owner hits and receive zero credit:

1. **Barnes--Savage (1995).**  The official EJC paper defines the map used in
   its recurrence by deleting the first row and first column, and states that
   the Durfee size falls by one.  This owns the literal one-step `(1,1)` crop
   and its Durfee decrement, not an all-time arbitrary-target atlas.
   Official record/PDF:
   <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v2i1r11>.
2. **Gordon--Houten (1968).**  The source record is *Notes on Plane
   Partitions II*, JCT 4(1), 81--99, DOI
   <https://doi.org/10.1016/S0021-9800(68)80089-4>.  Chen--Ji--Zang explicitly
   attribute to it the largest `(m+j) x j` Durfee rectangle.  This is static
   rectangle ownership.
3. **Andrews (1971).**  The official record is *Generalizations of the Durfee
   Square*, JLMS s2-3(3), 563--570, DOI
   <https://doi.org/10.1112/jlms/s2-3.3.563>.  Later primary research quoting
   Andrews' construction records maximal rectangles of base-to-height ratio
   `r:s`; this supports the manuscript's rational-slope subtraction rather
   than an RCS residual claim.  The official full text is access-controlled,
   so the result was not used to infer absence of a temporal theorem.
4. **Chen--Ji--Zang (2015).**  Section 3 defines the `m`-Durfee rectangle
   symbol using the partitions of columns to the right and rows below the
   rectangle and gives total weight as rectangle area plus the two boundary
   weights.  This owns the static two-boundary decomposition.  Author copy:
   <https://arxiv.org/abs/1305.2116>; journal DOI
   <https://doi.org/10.1016/j.aim.2014.10.017>.

Exact-phrase and operation searches for iteration of a fixed `(a,b)` crop,
all-time fibres over arbitrary targets, cap thresholds, and recovery did not
produce a direct owner.  This is only a bounded negative search.  It does not
support novelty or priority, and external dissemination remains on hold.

## P113 collision attack

P113 acts on `P(n)` by **weight-preserving principal-diagonal-hook
regrouping**.  Its retained proof engine is an adjacent-gap increment leading
to depth `floor(n/2)`; its one-step image/fibre product is explicitly owned
background.  P160 acts on `P_(<=N)` by a **strictly weight-decreasing
coordinate crop**.  Its engine is additive cell-coordinate translation,
rectangular survival, and a top/middle/bottom inverse decomposition.

The possible similarities—integer partitions, Ferrers diagrams, an absorbing
state, a sharp finite clock, fibres, and conjugation—are generic interfaces.
No P113 adjacent-gap identity, diagonal-hook regrouping, Frobenius-coordinate
fibre, fixed-weight transport, or depth witness is used in P160.  Conversely,
P160's moving rectangular corner, arbitrary-time target fibre, cap support,
and ordered three-probe recovery are absent from P113.  No internal proof
transfer or occupied theorem collision was found.

## Disposition

`Critical 0 / Major 0 / Minor 0`.

Mathematical/reproducibility verdict: `ACCEPT`.

Dissemination status: `HOLD_EXTERNAL` because the owner search is bounded and
the residual is deliberately narrow.
