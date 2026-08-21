# C96 compile report

Two isolated deterministic two-pass `pdflatex` builds under `SOURCE_DATE_EPOCH=0`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, and `LC_ALL=C` used a fixed trailer ID and produced byte-identical two-page PDFs.  All fonts are embedded; the final log has no unresolved references, overfull boxes, underfull boxes, or warnings.

PDF SHA-256: `9222c35bd7d0d8c097ffadf47eeb086e735adbfccd98bff142143087c4626e18`.
