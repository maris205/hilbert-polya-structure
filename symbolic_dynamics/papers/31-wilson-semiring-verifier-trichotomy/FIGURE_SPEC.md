# Figure specification — Paper 31 / SD-C33

All figures are native vector TikZ.  They encode theorem dependencies,
markers, and ownership boundaries.  They contain no raster content, target
zeros, sampled ordinates, prime tables, or fitted magnitudes.

## Figure 1 — bare escape and matched-clone firewall

**File:** `figures/semiring_clone_boundary.tex`

The left column contains the finite-full-shift semiring with alphabet sum and
product.  The upper right branch shows Paper 30's bare monomial UFD clone:
multiplication transports, but ordinary addition produces the explicit barred
identity \(x_2=2\).  The lower right branch shows the matched formal labels
\(y_n\) with transported \(\oplus_Y,\otimes_Y\).  A double arrow records the
source isomorphism and an equality box records identical Wilson path, cycle,
roof, and marker ledgers.

**Claim:** addition genuinely defeats the old bare clone but cannot defeat an
isomorphic matched semiring presentation.

## Figure 2 — Wilson cycle and marker ownership

**File:** `figures/wilson_cycle_marker.tex`

A representative recurrent block is drawn as a cycle from
\(v_{p,1}\) through \(v_{p,p-1}\).  The center records graph length \(p-1\)
and total roof \(\log p\).  One lane maps the raw cycle to
\(1-z^{p-1}p^{-s}\); a second lane contracts first return to one marked base
and gives \(1-zp^{-s}\).  Equality at \(z=1\) is shown separately from the
barred free-marker equality.

**Claim:** the entropy weight survives first return, while the graph-step time
does not.

## Figure 3 — ownership trichotomy

**File:** `figures/verifier_trichotomy.tex`

The source-natural Wilson recurrence feeds three lanes:

1. the matched semiring clone copies all data;
2. the transient trace-class verifier loses its DAG under pruning and leaves
   the prime diagonal;
3. the recurrent exact-clock verifier retains raw graph time but is
   noncompact because one edge weight tends to one.

The first-return repair branches from lane 3 and is labeled “honest determinant
of changed time.”  The bottom decision box prints
`CLOSE_TERMINAL_SEMIRING_VERIFIER_BRANCH`.

**Claim:** every available repair loses either selectivity, computation, or
same-object Fredholm ownership.

## Accessibility and layout

- The palette uses blue, green, amber, and red only redundantly with labels,
  border shapes, and line styles.
- Solid double arrows mean isomorphism/equality; dashed arrows mean a changed
  object or diagnostic comparison; barred arrows mean a failed implication.
- Every figure remains understandable in grayscale.
- Font size is at least `\small` at full-text width.
- Captions are self-contained and state both the positive inference and its
  limit.
- No decorative title is placed inside a figure.
- The PDF audit must show zero raster-image objects.
