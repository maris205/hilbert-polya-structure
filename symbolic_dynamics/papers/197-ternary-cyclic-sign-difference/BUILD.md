# P197 deterministic build

From this paper directory, set SOURCE_DATE_EPOCH=1704067200,
FORCE_SOURCE_DATE=1, TZ=UTC and LC_ALL=C for the complete build. Run
pdflatex -interaction=nonstopmode -halt-on-error main.tex, then bibtex main,
then pdflatex twice with the same options. Only main.tex and references.bib
are required source inputs. Volatile PDF metadata is suppressed in source.

Verifier: `PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py`.
Compare complete stdout byte for byte with code/CANONICAL.txt. Use shell
pipefail when piping to cmp, so a producer failure cannot be masked.

Final physical source-only cold builds and all-page visual QA will occur
after the two accepted manuscript reviews, not be inferred from this
author development build. Python standard library only is needed for the
verifier. Existing system pdflatex/BibTeX provide the PDF toolchain.
