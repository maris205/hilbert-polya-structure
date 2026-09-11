# P188 source-only build and PDF QA

## Frozen object

- Reviewed PDF: `papers/188-self-cardinality-truncation/main_round0_original.pdf`
- SHA-256: `10b881a6200e075ed66514e8f4f8873c433383c8118c6037ad1ecd1d5bcb8bc3`
- Source SHA-256: `f08712d1b1e43f707c1254ebf791724727e9387a5e0794dae3b5c40d4874ab39`

## Two source-only cold builds

Two fresh temporary directories outside the paper tree received only
`main.tex` and `references.bib`.  Each used
`SOURCE_DATE_EPOCH=1704067200`, `TZ=UTC`, and the documented sequence:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Both PDFs had SHA-256
`10b881a6200e075ed66514e8f4f8873c433383c8118c6037ad1ecd1d5bcb8bc3`.
Thus each is byte-identical to the frozen Round-0 PDF and to the other cold
build.  Each final log had zero LaTeX/package warnings, zero overfull boxes,
zero underfull boxes, and zero undefined references/citations.  Their
extracted-text SHA-256 was
`e5c0a659cbabc1ceebac21f74e47b0f2b64116d23411fcd0ab01655f3e57cfa5`.

The builds were diagnostic only; no output was copied into the paper tree.

## Structural PDF checks

| check | result |
|---|---|
| pages | 4 |
| page geometry | every page `595.276 x 841.89 pt` (A4), rotation 0 |
| encryption | no |
| JavaScript | no; no `/JavaScript`, `/JS`, `/Launch`, `/EmbeddedFile`, or `/Encrypt` action token found |
| form | none |
| metadata stream / custom metadata | none / no |
| title, author, subject, keywords, creator, producer | all empty |
| fonts | 23 rows; every row embedded, subset, and Unicode-mapped |
| citation keys versus bibliography keys | exact set equality, 2 versus 2 |

The source is anonymous and contains no affiliation, acknowledgement,
funding, email, or identity marker.  No identity is exposed in PDF metadata.

## Visual inspection

All four pages were inspected at rendered resolution.  The dense nested-chain
formula remains legible, display limits do not collide with text, theorem and
proof breaks are coherent, proof-end boxes are visible, hyperlinks do not
cover glyphs, and the references on page four have no clipping or overlap.
No blank-content page, orphaned heading, or margin escape was found.

Build/PDF verdict: `PASS`.  These checks do not prove the mathematics and do
not alter `OWNER_AMBER / HOLD_EXTERNAL`.
