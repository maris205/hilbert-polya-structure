# Paper 10 Figure QA

**Disposition:** `PASS`  
**Inspection basis:** final 300 dpi PNGs viewed at original resolution plus
mechanical inspection of the corresponding PDF and SVG files.  
**Inspected:** 2026-08-15 UTC.

## Inventory and determinism

- Exactly three figure stems and exactly nine rendered outputs are present.
- Two complete generation runs are byte-identical for all nine outputs;
  `DETERMINISM_AUDIT.json` has SHA-256
  `e3f51a1985f6d00a7655db882cbbccddcfa712f710e210af19b9d15c8485567e`.
- Every generator loads the same strict, hash-locked data contract but is an
  independent per-figure script.
- No bytecode cache, candidate import/execution, random draw, external data
  load, new modulus target, or numerical $s$, $q^{-s}$, or logarithm
  evaluation occurs in the final build.

## Mechanical publication checks

| Stem | PDF | SVG | PNG |
|---|---|---|---|
| `fig1_quotient_layers` | one page, 518.4 x 345.6 pt; 3 embedded/subset/Unicode CID TrueType fonts; 0 Type-3; 0 raster objects | XML PASS; 51 selectable text nodes; 0 image nodes | 2160 x 1440 RGBA; 299.9994 dpi |
| `fig2_nine_modulus_ledger` | one page, 518.4 x 367.2 pt; 3 embedded/subset/Unicode CID TrueType fonts; 0 Type-3; 0 raster objects | XML PASS; 107 selectable text nodes; 0 image nodes | 2160 x 1530 RGBA; 299.9994 dpi |
| `fig3_clock_semantics` | one page, 518.4 x 352.8 pt; 3 embedded/subset/Unicode CID TrueType fonts; 0 Type-3; 0 raster objects | XML PASS; 49 selectable text nodes; 0 image nodes | 2160 x 1470 RGBA; 299.9994 dpi |

All PDFs and SVGs are vector-only.  SVG text remains selectable.  The PNG
metadata meets the 300 dpi tolerance used by the manifest builder.

## Original-resolution visual inspection

| Check | Figure 1 | Figure 2 | Figure 3 |
|---|---|---|---|
| Text and math legible | PASS | PASS | PASS |
| No clipped title, axis, label, caption line, or callout | PASS | PASS | PASS |
| No unintended text/marker overlap | PASS | PASS | PASS |
| Panel sequence and semantic arrows unambiguous | PASS | PASS | PASS |
| Prime/composite boundary visible without color alone | PASS: text/hatch/border | PASS: order, dashed divider, shade | PASS: labels/hatch/border |
| Scientific status redundant beyond hue | PASS: labels and hatches | PASS: bars/markers/hatching and exact annotations | PASS: shapes, arrows, labels, hatches |
| Outside-scope boundary explicit | PASS | not the purpose of this ledger | PASS |

Figure-specific inspection:

- **Figure 1:** the shell, cyclic locus, centralizer, $A$-orbit layer, full
  quotient, symplectic quotient, and reversor layer are visually distinct.
  The $q=5,11$ discard callout does not imply a general finite-data theorem.
  The information-retention ledger is fully visible.  Its reversor row says
  both that $d$ and $-d$ may be paired and that the noncyclic complement is
  not mixed with $\mathrm{CV}_q$; it does not claim that split noncyclic
  orbits can never merge.  The outside-scope note remains visible.
- **Figure 2:** the nine moduli remain in frozen registered order; all exact
  annotations are readable.  The five quotient rows are fully visible,
  prime/composite separation is explicit, and composite reversor cells are
  visibly `n/a` rather than zero.
- **Figure 3:** source-period bars and the native quotient-period-one line
  are distinct.  The arrows separate intrinsic identity dynamics from the
  external $q$ label.  Prime and composite cards both display one class;
  the live enriched boundary is readable and is not presented as tested.

## Evidence and semantic checks

- The exact nine-row values match the frozen ledger and satisfy
  $|\mathrm{CV}_q|=|C_q|$, $|E_q|=|\mathrm{CV}_q|+\text{discard}$,
  $|\mathrm{CV}_q/C_q|=1$,
  $|\mathrm{CV}_q/C_q^1|=|\operatorname{im}N_q|$, and
  $|C_q/\langle A\rangle|\operatorname{ord}_q(A)=|C_q|$ for every displayed
  modulus.
- Both quotient transitions are certified identity maps at all nine
  controls; the all-$q$ conclusion is attributed to the proof package.
- Figure 3 uses $q^{-s}$ and $\log q$ only as typeset symbols.  No numerical
  value of either expression appears.
- Captions in `latex_includes.tex` preserve finite-versus-proof authority,
  local-versus-global scope, and the untested enriched-quotient boundary.
- The Okabe--Ito palette is color-vision-safe, while all claim-bearing
  distinctions also use text, geometry, markers, borders, or hatching.

**Final figure QA verdict: PASS.**
