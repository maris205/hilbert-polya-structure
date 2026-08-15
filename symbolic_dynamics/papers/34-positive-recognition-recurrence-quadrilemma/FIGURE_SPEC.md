# Figure specification — Paper 34 / SD-C36

All figures are source TikZ compiled inside the paper. No external image,
raster plot, target-zero data, or decorative artwork is permitted.

## Figure 1 — recognition-to-recurrence quadrilemma

One central source box branches to four paths:

1. shared recurrent SCC -> mixed primitive root -> ledger failure;
2. terminal recognition -> cyclic pruning -> determinant sees only support;
3. private visible cycles -> logarithmic length -> whole operator noncompact;
4. first return -> trace-class diagonal -> marker changes from `z^ell` to `z`.

Use blue for frozen inputs, amber for ownership transitions, and red for stop
outcomes. The caption must state that the four branches are exhaustive only in
the frozen positive compiler class.

## Figure 2 — connector repair

The left panel shows the preregistered strict normal form: two private cycles
and two shortest connector paths whose interiors avoid both cycles, crossed
out because it need not exist. The right panel shows arbitrary SCC paths
between arbitrary attachment vertices and the mixed closed word
`gamma_a alpha gamma_c beta`, whose primitive root retains both cycle edge
supports.

The figure must not suggest that a one-way connector is recurrent.

## Figure 3 — clock and marker firewall

The upper row displays a private cycle of length `ell`, total roof `log N(a)`,
and one edge whose roof is at most the average. A sequence of such edges feeds
the weak-null noncompactness criterion. The lower row compares the raw factor
`1-z^ell N(a)^(-s)` with the induced factor `1-zN(a)^(-s)` and highlights that
they agree only after `z=1`.

## Visual audit

- A4 margins and body font must remain readable at 100% zoom.
- No node label may overlap an edge, filled region, or another label.
- Figures must work in grayscale and use line style as well as color.
- Captions are self-contained; figures contain no decorative title.
- `pdfimages -list` must report no raster images in the final PDF.
