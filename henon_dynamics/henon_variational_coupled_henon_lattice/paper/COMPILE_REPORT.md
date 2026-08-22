# C106 paper compile report

* Engine: `pdflatex` via `latexmk`, `-interaction=nonstopmode -halt-on-error`.
* Output: `main.pdf`, 2 pages, letter size.
* PDF SHA-256: `73eccfff0ada7eafe1a96caac809faad1a70845bb719f2d558a76634ce9a0d2f`.
* Fonts: embedded Type 1 Latin Modern and AMS symbols (`pdffonts` audit PASS).
* Determinism: two isolated `SOURCE_DATE_EPOCH=0` builds were byte-identical; both produced the hash above.
* Layout: no overfull/underfull boxes in the final two-pass build; first-pass rerun notices are normal LaTeX auxiliary-file behavior.

The PDF deliberately reports the formal A1-weak/A2-fail (operator-owner-open qualification) boundary and does not use the finite monodromy polynomial as a Fredholm claim.
