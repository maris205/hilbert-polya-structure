# Figure Plan

Status: no publication figure is required. The immutable Round-0 manuscript
was three pages; the accepted Review-A repair compiles cleanly as the current
four-page theorem note. The central relationships remain clearer as formulas
than as graphics.

## Mandatory visuals

None.

The local identity

\[
(a,b),(a,c)\mapsto(a,c),(b,c)
\]

already exposes the rightward scheduler mechanism. The sharp witness and reverse-admissibility criterion are similarly compact. Adding a state graph or histogram would risk giving finite evidence visual prominence comparable to the proved results.

## Optional expansion-only visual

If a later round needs one explanatory figure, use a single black-and-white local scheduler schematic:

- left panel: the first collided pair ((a,b),(a,c)), with equal lower endpoints highlighted;
- middle arrow: the right Hurwitz move (H_i);
- right panel: ((a,c),(b,c)), showing that the new second lower endpoint is (>a);
- footer: "all comparisons left of (i) are unchanged; the next execution index is (>i)."

This would support Section 2 only. It must not depict the history-set conjecture as a theorem.

Suggested technical specification: vector PDF/SVG, one-column width, grayscale-safe, no decorative colour, transposition endpoints typeset with the same notation as the manuscript, and accessible alt text describing the algebraic replacement.

## Computational diagnostics

The (n\le8) depth histograms and the (n=9) mask counts belong in canonical text transcripts, not in the paper figure set. If plotted for internal debugging, label every such plot:

> finite exact evidence for Conjecture 5.1; not an all-(n) theorem and not novelty evidence.

No figure should be generated until the owner gate moves beyond `OWNER_RED_AMBER/HOLD_EXTERNAL` or a specific internal review requires it.
