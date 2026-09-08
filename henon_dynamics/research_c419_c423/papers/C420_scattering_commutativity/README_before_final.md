# C420 — complete cusp scattering commutativity

**Status: complete, author-checked manuscript baseline; independent
full-manuscript review and release gates pending.**

Title: *When do the cusp scattering matrices of Gamma_0(N) commute?*

The article instantiates the admitted AS2 contract only. It classifies
every level for which the complete weight-zero, trivial-character cusp
scattering family is pairwise commuting in fixed width-one cusp
coordinates at all regular complex parameters. Both directions, both
obstructions, the imprimitive-square scalar factors, the all-exponent
principal basis and the elementary level criterion are proved in the
article, relative to explicitly attributed classical analytic inputs.

## Read and review

- Current PDF: [builds/baseline_polished/main.pdf](builds/baseline_polished/main.pdf)
  — 18 pages, 428469 bytes, author visually checked on every page.
- Master LaTeX: [paper/main.tex](paper/main.tex); modular proof sections:
  [paper/sections/](paper/sections/).
- Claim/dependency map: [PAPER_PLAN.md](PAPER_PLAN.md).
- Actual source access and verified metadata:
  [BIBLIOGRAPHY_VERIFICATION.md](BIBLIOGRAPHY_VERIFICATION.md).
- Build history, hashes, warnings and visual receipt:
  [COMPILE_REPORT.md](COMPILE_REPORT.md).

The review PDF has SHA256
`08967fffb8542a60bdedc4142f2efd7149d26fb9057276bb6ab27fbcce5f10ff`.
Its input-manifest hash is
`9d94846bd6fe52a6a9c30e5a7385bd369c3aa8a767e5cd85a5a404a7d1003994`.
The current 13 TeX/Bib source files were verified against that manifest.

## Build without overwriting an earlier receipt

From this directory, run `bash build.sh UNIQUE_LABEL`, using a fresh
alphanumeric/underscore/hyphen label. The script rejects an existing
build directory, snapshots the manuscript sources, records their hashes
and the environment, and preserves the actual latexmk output. It needs
the local LaTeX packages used in `paper/main.tex`, latexmk, BibTeX and
Poppler's PDF inspection tools. The recorded tool versions are in each
build's `environment.txt`.

Two actual builds have been made: `baseline` and `baseline_polished`.
They have different inputs because two typesetting issues were repaired
between them. They are **not** a same-input reproducibility pair or two
independent manuscript review rounds. Both artifacts and source snapshots
are retained. The polished build's final log has no warning, overfull,
underfull, undefined-reference or error match.

## Scope and remaining gates

Seven bibliography entries are cited, with classical ownership and access
limits disclosed in the text. The article does not claim a new scattering
formula, a new Dirichlet functional equation, a full reading of inaccessible
sources, worldwide priority, a Hilbert–Polya construction or human peer
review. No numerical experiment is used as a theorem premise. No old
mathematical diagnostic was rerun during manuscript preparation.

Pending coordinator-routed work: two actual independent full-manuscript
review/fix/recompile rounds, final source freeze and two-directory
same-input PDF reproducibility, final whole-batch/release checks and any
formal evaluation. No review outcome or release authorization is assigned
by this author handoff.
