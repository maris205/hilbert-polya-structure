# Initial build record — P143

- Engine: pdfTeX 1.40.22 / LaTeX2e 2021-11-15.
- Sequence: `pdflatex -> bibtex -> pdflatex -> pdflatex`.
- Result: success, 3 A4 pages, 331,522 bytes.
- Bibliography: 4/4 entries cited and resolved.
- References/citations: no unresolved entries after settling.
- Fonts: 25/25 rows embedded, subsetted, and Unicode-mapped.
- PDF: version 1.5, unencrypted.
- Exact control: 265,050 assertions, all passed.
- Round-0 SHA-256: `2cc73cb1f9cb0c673f86fc7a869cd8937b6aa0aa80a6a9d5a07fd50682567b6f`.
- Initial warning retained for review: one 1.82649pt overfull vertical page box; no horizontal overflow.
- External status: `HOLD_EXTERNAL`.

## Repaired round-1 build

- Review input: HOSTILE_REVIEW_A.md, verdict REVISE.
- Corrected Katona--Nagy DOI: 10.1007/s11083-014-9342-8.
- Bibliography: 5/5 entries cited and resolved; printed identifiers audited.
- Result: success, 4 A4 pages, 334,898 bytes.
- Current SHA-256: 240aac151d3f077854d1ceb8de1ed53f510f0c27cdde662314cd1fbadfb07efe.
- Frozen artifact: main_round1.pdf, byte-identical to the current PDF.
- Isolated build from only main.tex and references.bib: byte-identical.
- Main verifier: 265,050 assertions and canonical stdout comparison pass.
- Independent embedding verifier: 13,238,845 assertions and canonical stdout
  comparison pass.
- Settled citations/references and bad boxes: zero warnings.
- Round-0 remains immutable at its previously recorded hash.

## Accepted round-2 freeze

- Hostile review B: `ACCEPT`, with 0 critical, 0 major, and 0 minor findings.
- Canonical main control: 265,050 assertions, transcript byte match.
- Independent embedding control: 13,238,845 assertions, transcript byte
  match.
- Source-only isolated build: byte-identical to current `main.pdf`.
- Current PDF: 4 A4 pages; 25/25 font rows embedded, subsetted, and
  Unicode-mapped; all pages visually accepted.
- Frozen artifact: `main_round2.pdf`, byte-identical to `main.pdf` and
  `main_round1.pdf`.
- External status remains `HOLD_EXTERNAL`.
