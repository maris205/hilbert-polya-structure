# Paper 7 figure package

The three figures read the frozen source lock and registered exact-symbolic
artifacts directly.  The scripts fail closed on a candidate-id, source-lock,
proof-contract, control, or evidence-boundary mismatch.  They do not access
the network, external prime tables, Riemann-zero data, or numerical orbit
matches.

From the Paper 7 directory, regenerate the figures with:

```bash
python -B figures/gen_fig1_boundary_map.py
python -B figures/gen_fig2_registered_ledger.py
python -B figures/gen_fig3_frobenius_filter.py
python -B figures/verify_figure_determinism.py
python -B figures/build_figure_manifest.py
```

Each figure has a PDF vector master, an editable SVG companion, and a 300 dpi
PNG review preview.  Shared typography and the colorblind-safe palette live in
`paper_plot_style.py`; manuscript snippets live in `latex_includes.tex`.
`figure_manifest.json`, `DETERMINISM_AUDIT.json`, and
`FIGURE_PROVENANCE.md` record the complete source/output hash chain.

