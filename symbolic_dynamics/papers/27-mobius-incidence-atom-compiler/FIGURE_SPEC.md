# Figure Specification — Paper27 / SD-C29

All figures are native TikZ, vector-only, colorblind-aware, and legible after
grayscale conversion. Formal constructions use blue, proved passes green,
scope warnings amber, and route stops red.

## Figure 1 — Source-derived atom compiler and collapse

**Purpose:** show the whole argument in one left-to-right pipeline.

Nodes:

1. fixed divisibility grammar;
2. covers of \(1\), derived internally;
3. \(q_n=\zeta\varepsilon_n\mu\);
4. exact monochromatic atom words;
5. honest de Rham graded ratio;
6. atom Euler product.

A lower red return arrow from the compiler to coordinate projectors states
finite unitriangular conjugacy and countable bounded similarity for
\(\eta>1\). Footer labels: A1 pass, A2 honest, A3/A4 fail.

**Caption obligation:** source derivation is positive; determinant-equivalence
is the no-go.

## Figure 2 — Oblique/coordinate similarity firewall

**Purpose:** separate real off-diagonal incidence geometry from its
trace-invisible cyclic character.

Left panel: coordinate idempotents \(\varepsilon_n\).
Center: unitriangular zeta change of basis.
Right: oblique \(q_n\) with shared range geometry.
Bottom invariant band:

\[
\operatorname{Tr}Q^r=\sum_nb_n^r,\qquad
\det(I-zQ)=\prod_n(1-zb_n).
\]

Include a dashed line noting that adjoint Gram products are not covered by
this ordinary cyclic invariant.

## Figure 3 — Analytic domains and barrier

**Purpose:** prevent scope inflation.

Use three nested horizontal bands:

- \(\eta>1/2\): individual atom idempotents are rank-one trace class;
- \(\eta>1\): global zeta/Möbius similarity is bounded;
- \(\operatorname{Re}s>1+2\log_2|u|\): marked transfer and both de Rham
  degrees are trace class.

Mark the \(u=1\) vertical stop at \(\operatorname{Re}s=1\). Label the region
left of it “scalar continuation does not continue this operator.”

## Table specifications

### Literature boundary

Columns: classical ingredient; primary source; Paper27-safe use.

### Exact controls

Columns: control; expected outcome; ownership lesson.

### Route table

Columns: gate; status; analytic reason. Use green only for A0–A2 and red for
A3–A4. The overall rejected decision must be visually adjacent.

## Visual audit checklist

- no arrowhead enters node text;
- no line crosses an equation;
- figure fits the text width without raster scaling;
- red/green meaning remains readable through labels;
- marker exponent is \(r\ell(p)\);
- ordinary determinant and graded ratio labels are distinct;
- no route tuple is split across pages;
- no footer label is clipped.
