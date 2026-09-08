# C420 — complete cusp scattering commutativity

**Status: two full-manuscript reviews passed; final same-input builds and
all-page visual checks completed. Local final PDF published below.**
The coordinator's [formal-evaluation closure](../../EVALUATION_ADJUDICATION.md)
records A4_FORMAL_HINT for genuine classical source scattering, with all
target flags false. Exact batch sealing and synchronization are reported
separately in the [external release receipt](../../../RELEASE_C419_C423.md).

Title: *When do the cusp scattering matrices of Gamma_0(N) commute?*

The article instantiates the admitted AS2 contract only. It classifies
every level for which the complete weight-zero, trivial-character cusp
scattering family is pairwise commuting in fixed width-one cusp
coordinates at all regular complex parameters. Both directions, both
obstructions, the imprimitive-square scalar factors, the all-exponent
principal basis and the elementary level criterion are proved in the
article, relative to explicitly attributed classical analytic inputs.

## Read and review

- Current final PDF: [main.pdf](main.pdf) — 18 pages, 428401 bytes.
  It is byte-identical to both fresh final builds and the revised PDF
  that received the second full-manuscript PASS.
- Master LaTeX: [paper/main.tex](paper/main.tex); modular proof sections:
  [paper/sections/](paper/sections/).
- Claim/dependency map: [PAPER_PLAN.md](PAPER_PLAN.md).
- Actual source access and verified metadata:
  [BIBLIOGRAPHY_VERIFICATION.md](BIBLIOGRAPHY_VERIFICATION.md).
- Final build pair, source freeze, hashes, diagnostics and all-page receipt:
  [FINAL_BUILD_REPORT.md](FINAL_BUILD_REPORT.md).
- Complete manuscript reviews:
  [round 1](../../manuscript_reviews/round1/C420_REVIEW.md) and
  [round 2](../../manuscript_reviews/round2/C420_REVIEW.md).
- Item-by-item revision response: [REVISION_ROUND1.md](REVISION_ROUND1.md).
- Preserved baseline build history: [COMPILE_REPORT.md](COMPILE_REPORT.md).

The current final PDF has SHA256
`9753a3262ce775b5c289a0870bf4694066cb778c1cd10ada267d4ac5f5e74512`.
The source manifest shared by `round1`, `final1` and `final2` has SHA256
`ba887f152fc9fe7ca9e69cf74f14a96332bcf04c998f6352786358a65acc147e`.
All 13 production TeX/Bib inputs match this manifest and both final source
snapshots. No production source changed during the final-build task.

## Build without overwriting an earlier receipt

First copy this paper directory outside the sealed batch; never add a new
build to the sealed original. From that copy, run `bash build.sh UNIQUE_LABEL`, using a fresh
alphanumeric/underscore/hyphen label. The script rejects an existing
build directory, snapshots the manuscript sources, records their hashes
and the environment, and preserves the actual latexmk output. It needs
the local LaTeX packages used in `paper/main.tex`, latexmk, BibTeX and
Poppler's PDF inspection tools. The recorded tool versions are in each
build's `environment.txt`.

The preserved build history is `baseline`, `baseline_polished`, `round1`,
`final1` and `final2`. The first two have different inputs and were never
counted as a same-input pair or as manuscript reviews. After round 1 of
full-manuscript review, two optional presentation edits were made and
actually compiled as `round1`. Round 2 reread the complete revised article
and requested no further source change.

The actual fresh `final1` and `final2` builds each exited zero after normal
latexmk convergence. Their PDF, BibTeX output and extracted text compare
byte-for-byte equal. Every one of the 18 pages from each final build was
opened and checked; both sets of page images are retained in their
respective `pages/` directories. Final logs have no actual warning,
error, undefined-reference/citation or overfull/underfull box. All 27 font
rows are embedded, subset, Unicode-mapped Type 1 fonts.

No old build or receipt was deleted or overwritten. The pre-final README
is preserved as [README_before_final.md](README_before_final.md). Its
baseline status is historical, not the status of the current final PDF.

## Scope and remaining gates

Seven bibliography entries are cited, with classical ownership and access
limits disclosed in the text. The article does not claim a new scattering
formula, a new Dirichlet functional equation, a full reading of inaccessible
sources, worldwide priority, a Hilbert–Polya construction or human peer
review. No numerical experiment is used as a theorem premise. No old
mathematical diagnostic was rerun during manuscript preparation.

The coordinator accepted both complete manuscript reviews and the final
production gate. The local checks do not constitute human peer review,
venue acceptance, external publication or worldwide-priority certification.
Formal evaluation has its separate completed record linked above. This
coordinator navigation update does not change any production source or PDF.
The [exact final-build handoff README](README_final_build_handoff.md) retains
the bytes whose hash is quoted by the build report; its pending-evaluation
language describes that earlier handoff. Later changes to production inputs
require renewed build and review checks.
