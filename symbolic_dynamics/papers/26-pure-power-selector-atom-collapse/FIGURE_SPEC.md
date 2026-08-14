# Figure Specification — SD-C28

All figures are pure vector TikZ, colorblind-safe, legible in grayscale, and
self-contained at single-column width.  No data-derived raster plot is used.

## Palette

- formal blue `#2A5D7A`: exact constructions and theorems;
- green `#2F6F4E`: honest positive analytic statements;
- amber `#9A6700`: scope firewalls and convention changes;
- red `#A63D40`: rejected route gates and counterexamples;
- gray `#E9ECEF`: trace-invisible or dormant structure.

Color is redundant with shape, border style, and text labels.

## Figure 1 — Selector-to-atom collapse

**File:** `figures/selector_atom_collapse.tex`  
**Placement:** Introduction  
**Width:** `0.98\textwidth`

Left: a shared renewal word enters two exact selector routes.  The upper route
computes reduced support and applies the exterior Euler coefficient, marked
“exact, word-indexed.”  The lower route uses stationary projectors, marked
“exact, one line/color.”  Both point to the observable algebra `C^m`; a final
arrow through the inherited de Rham cancellation ends at
`product_n(1-z u^ell(n)n^-s)` and a disjoint-block icon.  A red footer states
“selector solved; arithmetic source selection not solved.”

Caption must distinguish the nonstationary orbitwise rule from the stationary
projector and explain that their common determinant survivor is atom indexed.

## Figure 2 — Visibility layers

**File:** `figures/character_visibility_layers.tex`  
**Placement:** Character-rigidity section  
**Width:** `0.92\textwidth`

Four horizontal layers:

1. one net color simple per label — visible to word traces and determinant;
2. dormant zero-action sector — visible only at the empty word;
3. matched even/odd semisimple sector — cancels in supertraces;
4. radical extensions — may connect matrices but are trace invisible.

A right-hand visibility column uses solid/empty markers, not color alone.
The caption states that semisimplification is classified while literal
operator splitting is not.

## Figure 3 — Wordwise versus aggregate

**File:** `figures/wordwise_aggregate_firewall.tex`  
**Placement:** Determinant section  
**Width:** `0.90\textwidth`

Top: two oriented necklaces `0→1→2→0` and `0→2→1→0`, labelled `+1` and `-1`.
Middle: abelianization maps both to `x_0x_1x_2`, where they cancel.  Bottom:
two decision boxes say “aggregate pencil: passes” and “wordwise selector:
fails.”  The diagram visually enforces the order: audit words first, commute
variables second.

## Accessibility and build audit

- minimum node text approximately 8.5 pt at final size;
- no text placed over arrows;
- arrowheads and dash patterns remain distinct in grayscale;
- equations use manuscript macros where possible;
- captions explain every abbreviation and logical role;
- no internal figure title duplicates the caption;
- inspect rendered pages at 130–150 dpi for overlap, clipping, and contrast;
- keep all TikZ sources directly input by the corresponding section.

The independent experiment integrator owns numerical result artifacts; these
three theoretical figures do not read or rewrite any result file.

