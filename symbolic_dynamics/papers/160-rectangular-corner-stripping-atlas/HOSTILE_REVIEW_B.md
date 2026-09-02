# P160 independent Hostile Review B

**Date:** 2026-09-02  
**Frozen object:** `main_round1.pdf`  
**Frozen SHA-256:**
`3bbbb6f3243171d612f86a17cd88b58f56bc5ec80c3533dc30464343931def03`  
**Verdict:** **ACCEPT** at the internal mathematical/reproducibility gate  
**External status:** **HOLD_EXTERNAL**  
**Finding count:** **Critical 0 / Major 0 / Minor 0**

This is an independent reconstruction from `main.tex`, the frozen theorem
contract, and `main_round1.pdf`.  It does not rely on an earlier review's
verifier or argument.  Review-B evidence and the new standard-library
verifier are under
`docs/papers157_161_sequence/reviews/p160_rcs_b/`.

## 1. Result in one paragraph

All stated theorem components survive hostile re-derivation: the iterate is
literal coordinate translation; the point clock and sharp capped height
follow from one moving corner cell; the empty fibre has the stated finite
slice series; every nonempty target has the stated forced monomial and two
independent bounded-partition factors; and the repaired support witness
`gamma=(d)` is legal for every value in the paper's claimed range.  Transpose
conjugates `(a,b)` to `(b,a)`, and the three one-step thresholds recover the
ordered pair exactly.  An independent 11,287,366-assertion audit passes twice
with byte-identical output.  Two source-only cold builds reproduce the frozen
PDF byte for byte, and settled log, font, visual, anonymity, and citation QA
all pass.  The classical records own substantial static input, but the paper
subtracts it explicitly.  No P113 proof-engine transfer was found.  The owner
search is bounded, so acceptance does not lift `HOLD_EXTERNAL`.

## 2. Independent mathematical reconstruction

### 2.1 Iterates, clock, and sharp height

One application of `T_(a,b)` retains precisely the cells with `i>a` and
`j>b`, translating `(i,j)` to `(i-a,j-b)`.  After `t` applications the
retained coordinates are therefore `i>at`, `j>bt`, giving

```text
T_(a,b)^t(lambda)=(lambda_(at+1)-bt,lambda_(at+2)-bt,...)_+.
```

The remainder is nonempty precisely when its prospective northwest cell was
present:

```text
T^t(lambda) != empty
iff lambda_(at+1) >= bt+1
iff (at+1,bt+1) belongs to lambda.
```

Taking the first failure gives

```text
tau_(a,b)(lambda)=min{t>=0:lambda_(at+1)<=bt}.
```

Survival at rank `t` forces the rectangle
`[1,at+1] x [1,bt+1]`, of area `(at+1)(bt+1)`.  That rectangle itself is a
witness whenever its area is at most the cap.  Consequently

```text
H_(a,b)(N)=min{t>=0:(at+1)(bt+1)>N}.
```

This also handles `N=0`: the minimum is `t=0`.  Every nonempty partition
loses at least `(1,1)` in one update, so the empty partition is the only
recurrent state.

### 2.2 Empty fibre

Write `h=at`, `w=bt`.  Absorption by rank `t` is
`lambda_(h+1)<=w`.  Slice by `k=lambda_(h+1)`.

- If `k=0`, the partition has at most `h` rows and contributes
  `1/(q;q)_h`.
- If `1<=k<=w`, remove the forced `k x (h+1)` rectangle.  The excess in the
  first `h` rows is a partition with at most `h` parts, while the lower
  remainder has largest part at most `k`.

The slices are disjoint and reversible, giving exactly

```text
E_(h,w)(q)=1/(q;q)_h * sum_(k=0)^w q^(k(h+1))/(q;q)_k.
```

This proof remains valid at the artificial boundaries `h=0` or `w=0`.  In
particular, `E_(0,0)=1`, as required by the identity map at `t=0`.

### 2.3 Every nonempty target fibre

Fix nonempty `mu=(mu_1,...,mu_r)`.  A source of the rank-`t` crop has the
forced middle block

```text
lambda_(h+j)=mu_j+w,  1<=j<=r,
lambda_(h+r+1)<=w.
```

Each of the first `h` rows has baseline `mu_1+w`; its excesses give an
arbitrary partition `gamma` with at most `h` parts.  The rows below the
middle block give an independent partition `beta` whose largest part is at
most `w`.  Padding `gamma` by zeros reconstructs exactly one source from each
pair `(gamma,beta)`.  Its forced weight is

```text
M_(h,w)(mu)=|mu|+h(mu_1+w)+w ell(mu),
```

so the fibre series is

```text
q^M_(h,w)(mu) / ((q;q)_h (q;q)_w).
```

The empty target cannot be substituted into this expression; its separate
line above is necessary.  The displayed convolution formula for fixed source
weight follows by reading the coefficient in the two independent factors.
For the worked `(h,w)=(4,2)` example, direct coefficient calculation gives
`1,2,5,9,17`, exactly as printed.

### 2.4 Support, caps, and the repaired witness

The every-weight claim is explicitly restricted to `t>=1`.  Since the paper
fixes `a,b>=1`, this implies `h=at>=1` (and also `w>=1`).  For an excess
degree `d`:

```text
d=0: gamma=empty, beta=empty;
d>0: gamma=(d), beta=empty.
```

The partition `(d)` has one part, hence at most every legal `h`; unlike a
column `(1^d)`, it has no length problem.  Its reconstructed top rows are

```text
(mu_1+w+d, mu_1+w, ..., mu_1+w),
```

which join weakly decreasingly to the forced middle block.  The result crops
to `mu` and has weight `M_(h,w)(mu)+d`.  Therefore every weight at or above
the threshold occurs, none below it can occur, and under a cap

```text
mu is in Image(T^t | P_(<=N)) iff M_(at,bt)(mu)<=N.
```

The boundary repair is complete:

- `h=1` is legal because `(d)` has length one;
- `d=0` is handled by the empty partition, not `(0)`;
- at `t=0`, `h=w=0` and the fibre is correctly stated to be the singleton
  source `mu` at exact weight;
- in the artificial, unclaimed boundary `h=0<w`, the correct every-degree
  witness would be `beta=(1^d)`, not `gamma=(d)`.  The paper does not cross
  this boundary with its support assertion.

### 2.5 Mass identity, duality, and recovery

The empty and nonempty fibres partition all sources, so their formal sum is
the ordinary partition series.  Coefficientwise local finiteness is immediate
from `M_(h,w)(mu)>=|mu|`; the mass identity is sound.

Transposing retained cell coordinates swaps deleted rows and columns:

```text
T_(a,b)(lambda)'=T_(b,a)(lambda').
```

For one step, substituting the three targets into `M_(a,b)` gives

```text
m((1))   =1+a(1+b)+b=(a+1)(b+1),
m((2))   =2+a(2+b)+b=m((1))+a+1,
m((1,1)) =2+a(1+b)+2b=m((1))+b+1.
```

Hence the printed differences recover `a` and `b` in the correct order.  The
transpose symmetry therefore does not collapse ordered identifiability when
row and column probes remain labelled.

## 3. Independent exact audit

The new verifier `verify_p160_review_b.py` imports only Python's standard
library and independently generates every partition through weight 28.  It
does not import the author verifier or any earlier-review verifier.  Coverage
includes `t=0`, `t=1,...,5`, asymmetric `(a,b)`, artificial `h=0` and `w=0`
boundaries, literal targets and sources, cap images, source-support intervals,
the repaired witness, empty fibres, all nonempty fibre coefficients,
decode/rebuild bijections, clocks, sharp heights, conjugation, mass, and
recovery.

```text
partitions enumerated                           18,460
partition-engine assertions                     73,840
iterate/clock/height/conjugation assertions   2,068,432
fibre and boundary assertions                 8,602,762
support/cap/witness assertions                    6,726
t=0/recovery/mass assertions                    535,606
TOTAL                                        11,287,366
result                                               PASS
```

Two fresh executions produced byte-identical stdout:

```text
b6034231aa620d0de80a56bfcda69f8ddfe047e343498896426699252b918b8a
```

The verifier source SHA-256 is
`589a737b8371e46aba51caabbb431fb00b4ab9531fc4bd48805eb2cc62adeea9`.
The retained run files and detailed section ledger are in the Review-B
evidence directory.

## 4. Owner/source subtraction

The source check supports the paper's conservative subtraction:

- **Barnes--Savage (1995):** the official EJC text explicitly deletes the
  first row and first column in its recurrence and states the Durfee
  decrement.  The paper correctly gives zero credit to that one-step square
  crop.  <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v2i1r11>
- **Gordon--Houten (1968):** own the static `m`-Durfee rectangle, the largest
  `(m+j) x j` rectangle, as explicitly attributed by Chen--Ji--Zang.  This is
  static rectangle ownership, not evidence for the residual temporal atlas.
  <https://doi.org/10.1016/S0021-9800(68)80089-4>
- **Andrews (1971):** the official record and subsequent primary literature
  support generalized maximal rectangles with prescribed rational
  base-to-height ratio.  The manuscript subtracts this static rational-slope
  viewpoint.  <https://doi.org/10.1112/jlms/s2-3.3.563>
- **Chen--Ji--Zang (2015):** Section 3 defines the `m`-Durfee rectangle symbol
  from the right and lower boundary partitions and records the
  area-plus-boundary weight decomposition.  The manuscript correctly gives
  the symbol, decomposition, and product factors zero credit.
  <https://arxiv.org/abs/1305.2116>

The source language is accurate as a collective subtraction: Gordon--Houten
cover additive `m`-rectangles, Andrews covers ratio rectangles, and
Chen--Ji--Zang expose the static two-boundary symbol.  Bounded exact-operation
searches did not identify an owner of the combined fixed-crop all-time
iterate, arbitrary-target fibre atlas, empty branch, exact cap support, and
ordered recovery.  This negative result is not priority evidence; the
manuscript itself says so.  No owner/source red flag requiring revision was
found, while `HOLD_EXTERNAL` remains mandatory.

## 5. P113 collision attack

The collision does not survive comparison of carriers, updates, or proof
engines.

| Axis | P113 principal-hook dynamics | P160 RCS |
|---|---|---|
| Carrier | partitions of one fixed weight `n` | all partitions of weight at most `N` |
| Update | regroup principal diagonal hooks; weight preserving | delete fixed rows/columns; strictly weight decreasing |
| Clock engine | exact adjacent-gap increment | moving rectangular survival cell |
| Sharp extremum | `floor(n/2)` via a two-row witness | first failure of `(at+1)(bt+1)<=N` via a rectangle |
| Fibre engine | owned Frobenius-coordinate one-step product | all-time top/middle/bottom target decomposition |
| Conjugation | diagonal-hook data unchanged, with timing exception | conjugacy swaps `(a,b)` and `(b,a)` |
| Identification | none of P160's ordered probes | three target thresholds recover ordered `(a,b)` |

The shared words “partition”, “Ferrers”, “fibre”, “clock”, “conjugation”, and
“absorbing” are interface-level overlap.  P160 imports no adjacent-gap
identity, hook regrouping, Frobenius fibre, fixed-weight layer transport, or
P113 depth witness.  No occupied internal proof transfer or theorem collision
was found.

## 6. Build, PDF, font, anonymity, citation, and log QA

Two clean temporary directories received only `main.tex` and
`references.bib`; each ran one `pdflatex`, one `bibtex`, and two settling
`pdflatex` passes.  Both rebuilt PDFs are byte-identical to each other and to
the frozen PDF, all with SHA-256
`3bbbb6f3243171d612f86a17cd88b58f56bc5ec80c3533dc30464343931def03`.

- Both final TeX logs contain zero warnings, unresolved references/citations,
  bad boxes, or errors; both BibTeX logs are clean.
- The PDF is four A4 pages.  All four 144-dpi page renders were visually
  inspected: no clipping, overlap, bad break, broken glyph, or table/margin
  failure.
- All 22 font records are embedded, subset, and Unicode-mapped.
- PDF title, subject, keywords, and author metadata are blank; the visible
  byline is `ANONYMOUS`.
- Extracted text contains no placeholder, email, personal acknowledgement,
  funding statement, or accidental author identity.  Bibliographic names are
  expected.
- All five bibliography entries are cited and rendered; no unresolved marker
  remains.

## 7. Findings and executable repairs

### Critical: 0

No false theorem, invalid boundary, corrupt artifact, or owner collision.

### Major: 0

No gap in an advertised proof axis, no failed cold build, no missing source
subtraction, and no P113 engine transfer.

### Minor: 0

No localized statement, typography, citation, anonymity, or log defect.

### Required repairs

None.  There is no executable author repair attached to an empty finding
list.

As a regression guard rather than a repair: if a future version extends the
every-weight assertion to artificial `h=0<w`, it must use
`beta=(1^d)` (or another bounded-part witness), not `gamma=(d)`.  The frozen
Round-1 text does not make that extension.

## 8. Final disposition

**ACCEPT** the frozen Round-1 object for the internal P160 gate with
**Critical 0 / Major 0 / Minor 0**.  Keep **HOLD_EXTERNAL** unchanged: this
review verifies mathematics, internal non-collision, source subtraction, and
artifact integrity, but a bounded owner search cannot establish novelty,
priority, or safety for dissemination.
