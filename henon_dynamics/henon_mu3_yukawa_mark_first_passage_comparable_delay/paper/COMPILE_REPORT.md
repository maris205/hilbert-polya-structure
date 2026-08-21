# C95 compile report

Two isolated deterministic two-pass `pdflatex` builds under `SOURCE_DATE_EPOCH=0`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, and `LC_ALL=C` used a fixed trailer ID and produced byte-identical two-page PDFs.  All fonts are embedded; the final log has no unresolved references, overfull boxes, underfull boxes, or warnings.

PDF SHA-256: `60caec178a32d3d33d459cd0103c922fb5e967d25e06830fcd4011705ac3698c`.
