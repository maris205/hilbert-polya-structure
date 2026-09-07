# C414 author manuscript handoff

Status: **COMPLETE_AUTHOR_DRAFT; NONAUTHOR_MANUSCRIPT_REVIEW_PENDING**.
This is an authored article, not an independent manuscript review,
final deterministic release or formal Route A evaluation.

## Draft completeness

The new draft consists of `main.tex`, seven included sections,
`references.bib`, `CITATION_AUDIT.md` and the actual nine-page
`main.pdf`. It implements the frozen C414 section/claim plan.
The complete accepted height proof, full nonauthor review including
source-fix closure, source audit and finite diagnostic receipt were
read before drafting; no frozen file or mathematical test was changed.

All eight proof steps are typeset: two-sided escape, unique valley
partition, canonical limits and properness, exact edge/turn counts,
positive series and fundamental parallelogram, normal convergence,
fully aggregated simple/double poles, meromorphic boundary and
real-B counting with the floor retained in the exponent. At the
double-pole step the proof explicitly writes b_j = alpha*j + rho_j,
with rho periodic, to justify that the remainder contributes at most
a simple pole. This spells out the accepted central-cone argument,
not a new parameter claim.

The author read the complete extracted nine-page PDF text and the
source paragraphs against the claim matrix. The reverse outline runs
from the all-orbit counting question through the valley and analytic
work to the real-height count; no standalone secondary contract or
orphan section was added. All four bib entries are cited, and the
actual source access limits are stated in the introduction/audit.
An `rg` scan found no TODO/FIXME/XXX/[VERIFY] marker in TeX or Bib
(exit 1 = no matches).

## One actual author build

From this directory, one successful invocation, exit 0:

```sh
env SOURCE_DATE_EPOCH=1788652800 FORCE_SOURCE_DATE=1 latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build_author main.tex
```

Latexmk resolved normal first-pass references with its own TeX/BibTeX
passes. No source repair was needed to obtain a clean final log.
The resulting PDF was copied without replacing an existing file to
`main.pdf`: nine pages, 355639 bytes. Actual environment is latexmk
4.76; pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian);
BibTeX 0.99d. The final TeX/BibTeX log scan has no Warning, undefined,
Overfull or Underfull matches, only the selected PDF-output line.
`pdffonts` reports 21 fonts, all embedded, subset, Unicode-mapped,
no Type 3 fonts. Full text extraction succeeded.

| Handoff artifact | SHA256 |
|---|---|
| main.tex | `1944b5a5b8275c8ce296bb59499a5ff5b84295b67d522c8081087a4746cc17b6` |
| references.bib | `f39b2c2588908287103bb78dd40b57195799d35f1f3bcbb9fccf2b5ec0cd7fb8` |
| main.pdf | `23f41109cd6fa6f3c5f4eb209f1274ed4a45c77dd4ab34d3257dcd0d245267fe` |
| build_author/main.log | `114a4e6dea89d9789e9f188c202ec056afc4297075933454e49863517d4b7518` |
| build_author/main.bbl | `7a460a44d7f53890bd0392afab6d9dd91cee5bd2f2c7073981e1c3bd8ef788a2` |
| build_author/main.blg | `4e9a2d7ee63ee7f17e7dcef91eaf4d2a34d968a973c50975ea7fe0b66a6aa385` |

The author has not claimed a final visual or fresh double-build PASS.
Those checks, independent manuscript review and its affected fixes,
the pinned evaluation, exact release sealing and Git integration remain
separate gates. The height series supplies no target Euler factor,
root number, automorphy or target zero/divisor correspondence.
