# Paper artifacts

`main.tex` is revision-conditional. Round 0 closes the exact image; round 1 adds the regular torus and the initial-phase coset form of every linear-flow closure; round 2 adds unshifted GT branching labels and quantization count, evidence, sources, boundaries, and the Route-A firewall. `main.pdf` must be byte-identical to `main_round2.pdf`.

All stored PDFs are built twice from separate fresh directories with `SOURCE_DATE_EPOCH=1788480000` and LuaLaTeX.
