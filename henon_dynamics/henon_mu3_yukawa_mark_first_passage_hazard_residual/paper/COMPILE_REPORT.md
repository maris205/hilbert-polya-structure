# Compilation report

The paper was compiled twice in separate temporary directories with
`SOURCE_DATE_EPOCH=0` and `TZ=UTC`.  Each isolated `latexmk -pdf` build ran
the required two `pdflatex` passes.
The resulting PDFs were byte-identical:

```text
c9678e7a39c3ae4aeaff56ce20f809cd2bd894bae4ca98cf5164cd18c2dddf54
```

Both builds produced a 308,680-byte, two-page PDF.  The logs contain no
undefined-reference, undefined-citation, `Overfull`, `Underfull`, fatal, or
emergency-stop diagnostics.  All fonts are embedded and the extracted text
contains no `[VERIFY]`, `[?]`, or `??` marker.
