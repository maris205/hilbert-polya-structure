# P164 build ledger

## Round 0 freeze

The anonymous manuscript was built with:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

- output: `main_round0_original.pdf`
- pages: 4, A4
- PDF SHA-256: `db26e57e610577cdff03c348fa3ce794165e3268393350d7d2f55b14e98070ae`
- final log: no warnings, undefined references/citations, bad boxes, or errors
- fonts: all embedded, subsetted, and Unicode mapped
- title/author/subject/keywords metadata: empty
- paper author line: `Anonymous`
- release sentinel: `HOLD_EXTERNAL`

Round-1 and Round-2 entries are appended only after process-separated
reviews and repairs.

## Round 1 freeze

Hostile Review A requested two proof-completeness repairs: an explicit lower
bound proving strict positivity of the last shell, and an explicit
all-one-vector repair covering the endpoint `j=n`.  Both were implemented
without changing any stated formula.

- output: `main_round1.pdf`
- pages: 4, A4
- bytes: 301,337
- source SHA-256:
  `6a589c778137cb6e039f7a01710e7264686c6952321f0494ee3c992bfcda4218`
- PDF SHA-256:
  `b1fb98834db37564a50869c1fd637ceb78a5565104fb1dbb096dbd9a6b9c2f26`
- Round-0 PDF retained unchanged at its pinned hash
- settled `pdflatex -> bibtex -> pdflatex -> pdflatex` logs: zero warnings
- fonts: 23/23 embedded, subsetted, and Unicode mapped
- identifying PDF metadata: blank
- author and Review-A canonical replays: byte-identical, 1,154,387 and
  950,659 assertions respectively
- release sentinel: `HOLD_EXTERNAL`

## Round 2 freeze

An independent Hostile Review B returned
`ACCEPT — 0 Critical / 0 Major / 0 minor`.  It rederived the literal map,
dyadic repeated-root law, mask multiplicities, every-time image and affine
target enumerator, both evaluated target spectra, and all repaired endpoint
cases.

```text
independent assertions: 7,718,087
verifier SHA-256: b4a591e4f9a69c31debf00753ae443efde5445a06508ddc9b5e8e0ee79b47c31
canonical SHA-256: 843ded22172b6ea0abe5b3fd29243b0a6c66b8a412c9795112763cfcf1072007
fresh byte-identical replays: 3/3
output: main_round2.pdf
pages: 4, A4
bytes: 301,337
PDF SHA-256: b1fb98834db37564a50869c1fd637ceb78a5565104fb1dbb096dbd9a6b9c2f26
Round-1/current/Round-2 byte match: YES
```

Both source-only cold builds matched the current PDF.  Settled warning,
undefined-reference, rerun, and bad-box counts are zero; all 23 fonts are
embedded, subsetted, and Unicode mapped; metadata, anonymity, the visible
`HOLD_EXTERNAL` sentinel, and all four 144-dpi page renders pass.  No Round-2
repair was needed.  This is the internally accepted artifact; batch Git sync
remains pending.
