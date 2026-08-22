# C104 compile report

Two isolated builds of `main.tex` were run with
`SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1`; the PDFs were byte-identical.

* pages: 2, US Letter (`612 x 792 pt`)
* PDF SHA-256: `b9d3a478e211cfe4856485c96e0045de0c95240354e3163768ddf09f57761efb`
* fonts: all listed fonts embedded and subsetted (`pdffonts`)
* layout: no overfull/underfull boxes and no unresolved-reference warnings

The first-pass `rerunfilecheck` notice is absent after the second isolated
build. The checked PDF is `paper/main.pdf`.
