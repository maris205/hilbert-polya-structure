# Paper artifacts

- `main_round0_original.pdf`: complete classical clean-return and flux-integrality paper.
- `main_round1.pdf`: adds the Bochner Landau ladder, exact multiplicity, holonomy rigidity, and finite magnetic translations.
- `main_round2.pdf`: adds heat/zeta/determinant, both least revival times, boundary atlas, and Route-A closure.
- `main.pdf`: byte-identical to round 2.
- `main_round0.tex`, `main_round1.tex`, and `main_round2.tex`: minimal buildable wrappers that freeze the intended revision round before loading `main.tex`.

The release gate compiles every wrapper twice in fresh directories, requires strictly increasing page counts, and audits warnings, fonts, text extraction, rasterization, and round-specific content.
Each round has its own non-leaking English abstract, independently written Chinese abstract, and five to seven English and Chinese keywords. Chinese text uses the embedded `Droid Sans Fallback` font.
