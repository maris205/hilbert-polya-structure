# Build record — P130 round 2

## Manuscript build

Command sequence:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The round-two sequence was run once in the paper directory and independently
in a fresh isolated temporary directory initialized with only `main.tex` and
`references.bib`.  Both runs completed all four stages with exit status zero.
The isolated sources and settled PDF matched their local counterparts byte
for byte.  Result: **PASS**.

- PDF: 4 A4 pages, 346,056 bytes.
- `main.pdf`, `main_round2.pdf` and the isolated PDF are byte-identical,
  SHA-256:
  `c5a4fd3976a733c62a7f8f4e90b773cc6300970b9a25ac95b33f68a491f9c3fa`.
- Immutable `main_round0_original.pdf`: 342,739 bytes, SHA-256:
  `4d914ae6857739b11955dc9ec0db356e8bca5ae5cb67c1fd852ff3d4c2e796c9`.
- Immutable `main_round1.pdf`: 345,749 bytes, SHA-256:
  `6580b2822113677f5256d0dffcd95b8048e2c0fe6442d434e9fd4b28a1b9a0cb`.
- Round-two `main.tex` SHA-256:
  `70f020aa1b89353b94f76b781bee19e6c6fbc2d56824431d95090e3e4fcb033a`.
- Settled log/BLG scan: 0 errors, 0 warning hits, 0 undefined citations or
  references, 0 overfull/underfull boxes.
- Bibliography closure: 8/8 entries cited.
- Fonts: all 25 listed font records embedded, subsetted and Unicode-mapped.
- Metadata: title/author/subject/keywords blank; dates omitted; A4; rotation
  0; no form, JavaScript or encryption.
- Visual audit: all 4 rendered pages inspected; no clipping, collision,
  missing glyph, bad theorem break or anonymity leak.

## Exact control

- Fresh verifier/canonical comparison: **PASS**.
- Assertions: **735,609**.
- Scope: every state and target through seven chords, plus independent
  all-source reconstruction.
- Verifier SHA-256:
  `abd519009e877fa1fa98ece4e6cc290a5fb55bda47f07d4e79b9ccad43568a3d`.
- Fresh and canonical stdout SHA-256:
  `89b6142c21feac945f9d0dd362b5edf78aed78530596330be0c237e9088d60b4`.

## Review state

Hostile Review A's 2 MAJOR and 2 MINOR findings were repaired in round one.
Independent Hostile Review B returned 0 CRITICAL, 0 MAJOR and 2 MINOR
findings with `GO_INTERNAL`; round two closes both minors by qualifying the
Igusa statement at degree zero and correcting the literal P110 firewall.
The consolidated review and final QA record no open internal findings.
Internal status is `GO_INTERNAL`; external status remains `HOLD_EXTERNAL`.
