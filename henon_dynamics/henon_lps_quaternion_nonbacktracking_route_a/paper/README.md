# Paper artifacts

- `main_round0_original.pdf`: arithmetic graph and chamber theorem.
- `main_round1.pdf`: adds exact primitive nonbacktracking dynamics.
- `main_round2.pdf`: adds the spectral circle, density, evidence and route
  closure.
- `main_round0.tex`, `main_round1.tex`, `main_round2.tex`: frozen build
  wrappers for the corresponding artifacts.
- `main.pdf`: byte-identical to round 2.

All PDFs are rebuilt twice in fresh directories with LuaLaTeX and a fixed
source epoch.  The release gate requires distinct round hashes, warning-free
logs, embedded subset fonts, clean extracted text, and successful rasterization.
Every round has an English abstract and an independently written Chinese
abstract, each with 5--7 language-matched keywords; the wrapper gate also
forbids conclusions and evidence that belong only to later rounds.
