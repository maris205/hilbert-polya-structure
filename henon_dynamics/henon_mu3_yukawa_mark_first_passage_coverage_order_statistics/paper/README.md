# C96 paper

Compile `main.tex` with deterministic environment variables `SOURCE_DATE_EPOCH=0`, `TZ=UTC`, and `LC_ALL=C`, using two `pdflatex` passes.  The fixed trailer ID makes repeated isolated builds byte-identical.
