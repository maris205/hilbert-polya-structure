# Figure Specification — SD-C27

## Global style

- Source format: pure TikZ, included directly in LaTeX.
- Output: vector PDF through the manuscript build.
- Palette: formal blue for definitions, green for the genuine graded escape,
  amber for ownership changes, red for failure/collapse, gray for context.
- Accessibility: every color-coded result also carries a text label and
  distinct border style; no conclusion depends on color alone.
- Typography: manuscript font, minimum effective size 8 pt after scaling.
- No title inside a figure; captions are self-contained.
- All arrows show mathematical implication or object change, never merely
  decoration.

## Figure 1 — Local escape, global collapse

**File:** `figures/lefschetz_collapse.tex`  
**Role:** hero figure in the Introduction  
**Width:** full text width, landscape flow

### Composition

1. Left source box: logarithmic code \(c(n)\), affine branch
   \(\phi_n(z)=a_n+q_nz\), and \(q_n=2^{-\ell(n)}\).
2. Upper red local branch: ordinary zero-form trace
   \(w^r/(1-q^r)\), with scalar and ordinary tensor repair marked `FAIL`.
3. Central green box: canonical de Rham pair
   \(P_N\to P_{N-1}dz\) and
   \(\operatorname{Str}W^r=w^r\).
4. A prominent firewall tag: `graded ratio, not ordinary block determinant`.
5. Right fork:
   - shared disk: \(1-z\sum_jw_j\), mixed necklaces survive;
   - disjoint disks: \(\prod_j(1-zw_j)\), atom-loop collapse.
6. Bottom conclusion rail: genuine A2 repair; A1/A3/A4 fail.

### Caption

A logarithmic code branch carries the ordinary stability factor
\((1-q^r)^{-1}\).  Scalar and ordinary tensor repairs fail, whereas the
canonical zero-/one-form supertrace supplies \(1-q^r\) at every power.  The
successful graded determinant then retracts to cohomology: one shared
constant state retains mixed necklaces, while one constant per disjoint disk
is exactly an atom-loop inventory.

### Visual checks

- the two right-hand outcomes must not look like alternative formulas for
  one object;
- the graded/ordinary warning must remain legible at 100% PDF view;
- branch arrows must terminate outside node text;
- no equation may cross a box boundary.

## Figure 2 — Assembly and marker ownership

**File:** `figures/assembly_marker_firewall.tex`  
**Role:** summary figure in the marker/ceiling section  
**Width:** 0.96 text width

### Composition

Use a two-by-two grid:

| | Shared recurrence | Disjoint recurrence |
|---|---|---|
| Digit time | \(1-\sum_nu^{\ell(n)}n^{-s}\); mixed words | \(\prod_n(1-u^{\ell(n)}n^{-s})\); listed components |
| Return time | \(1-z\sum_nn^{-s}\); induced full shift | \(\prod_n(1-zn^{-s})\); induced atom loops |

Draw vertical arrows labelled `induce / declare whole codeword one return`.
Draw horizontal arrows labelled `separate recurrent components`.  The four
cells are four objects; no arrow is labelled equality.  Add a bottom
firewall: exterior grading cancels stability, not code duration or mixed
branch content.

### Caption

Two independent choices determine the ledger.  Shared recurrence permits
all mixed return necklaces, while disjoint recurrence removes them by
component separation.  Return time assigns one \(z\) per completed code;
digit time retains \(u^{\ell(n)}\).  Neither exterior cancellation nor the
specialization \(u=1\) identifies these dynamical objects.

## Reproducibility

Both figures are theorem diagrams and use no empirical data.  Their labels
must match the frozen formulas in `SOURCE_LOCK.md`, and both are compiled and
visually checked as part of the final paper build.
