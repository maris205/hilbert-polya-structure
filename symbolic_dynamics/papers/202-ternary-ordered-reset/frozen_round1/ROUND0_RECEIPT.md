# P202 immutable Round0 receipt

2026-09-05 UTC. ROUND0_FROZEN / REVIEW_A_PENDING / OWNER_AMBER /
HOLD_EXTERNAL. This is the author baseline only, not accepted paper A/B.
Allocation authority: docs/papers197_201_sequence/OR_ROOT_ADJUDICATION.md.

| Input | SHA-256 |
|---|---|
| main.tex | bcb24151784b52a27d846dd564ab6a0b438381e617575e6064c698f69683fa1a |
| references.bib | 56077d3271a58dc9ca3d22b4710c1790a52fbb242d1587da9a443b6455ad2fb0 |
| code/verify.py | 42c79767025b5da710aaccd8be170df964a14a65427470dd814cf3ce4081b850 |
| code/CANONICAL.txt | a971574926784fa43f27df88b58979ba6724a11c6070a3484c7641ea56fd6446 |
| main.pdf and main_round0_original.pdf | e1ca5021ff1ac74cff118d0d571fa0f3f74db32cc8b6ba5e7cd557fb69d88f8a |

The frozen copies reside at frozen_round0/ with their own nonself manifest.
They include the complete main source, bibliography, PDF, code/canonical,
run transcripts and author companions. Do not overwrite them during later
reviews or revisions. The top-level manifest covers the complete package,
including cold-build logs, source metadata, PDF metadata and page images.

Two fresh paper-local author processes each passed 3,962,690 assertions,
with code/RUN1.txt, RUN2.txt and CANONICAL.txt byte-identical. They cover
all 797,160 states n=1..12, every full source set, recurrent/action/time
tests, 7,280 parking configurations and sharp witnesses n=3..150.
The verifier is adapted from this writer's prior Stage1 checker; these
new executions are explicitly author checks, not independent paper review.

Two physically separate source-only cold builds, starting with only main.tex
and references.bib, each executed pdfLaTeX/BibTeX/pdfLaTeX/pdfLaTeX and
produced exactly the same PDF bytes as main. All commands exited zero;
the final logs and bibliography logs have no warnings. The PDF has four
A4 pages, 312,997 bytes, and 25 embedded/subset/Unicode font entries.
All four rendered pages were actually viewed and found readable, without
clipping, overlaps, missing glyphs or unresolved citations. Metadata is
anonymous/empty. ARS structural preflight is UNAVAILABLE because pypdf is
missing; successful Poppler/visual checks do not erase that advisory.

Five primary DOI records were freshly fetched and saved. The actual
full-text read scopes and the preprint/published metadata distinction are
documented in SOURCE_VERIFICATION.md. Parking, traffic branches, moving
frames, local coding and adjacency enumeration receive zero generic-method
credit. External owner search and missing P51--P56 remain limitations.

No independent manuscript findings census or delta is claimed. Review A
and B must be performed by agents other than this writer or the original
OR candidate author, using the frozen versions and new process evidence.
