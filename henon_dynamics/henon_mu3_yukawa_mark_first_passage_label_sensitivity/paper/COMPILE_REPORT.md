# C92 compile report

Two isolated deterministic two-pass `pdflatex` builds under
`SOURCE_DATE_EPOCH=0`, `TZ=UTC`, and `LC_ALL=C` produced byte-identical
one-page PDFs.  The fixed trailer ID removes environment-specific PDF IDs.
The final log has no undefined references, citations, overfull, or underfull
boxes; fonts are embedded.

PDF SHA-256:
`960f7c5869ed49a40f21cf22dd5eb2c1a14b652b982ce0ee69407454406b4a95`.
