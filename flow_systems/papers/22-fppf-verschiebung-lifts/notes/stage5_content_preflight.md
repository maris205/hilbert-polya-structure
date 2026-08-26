# Paper 22 Stage-5 content preflight

Date: **2026-08-26**  
Mode: **academic-paper / format-convert (Phase 7)**  
Citation decision: **retain current plainnat numeric style**  
Preflight result: **PASS; content confirmation required before final build**

## Accepted-input lock

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `e90dd88109d4e53d1f789808286c15cc917003cd38b69f49ddaff8661b9158ed` |
| `paper/references.bib` | `bd03813691db911316b18620ee4a1d212ac284fce7fb79af9f1b1cbc7ea71093` |
| `paper/paper.pdf` | `20e2d14f5a9e46b7d4f5eafac6669032c72fc69367fdf902e54440816a4a3f04` |
| Round-2 final integrity report | `d1636ec213ffa03be99aff791f075a6bf8bd894f73083a1fb40b3c965320ef44` |
| Stage-5 entry checkpoint | `6eae478c85a1aeff1f07218b131a9e2fa76ee526a1f2c243b4f7b11d4c87f959` |

The Stage-5 workspace copies of the source, bibliography, and content-proof PDF
have the same three hashes.  Therefore no scientific or declaration text has
changed at the formatting boundary.

## Formatter hard gate

- `\usepackage[numbers,sort&compress]{natbib}`: present.
- `\bibliographystyle{plainnat}`: present.
- Citation commands: 21; unique keys: 3; BibTeX entries: 3.
- Cited-but-missing keys: 0; bibliography orphans: 0; duplicate keys: 0.
- Undefined citations/references: 0.
- ARS `ref`/`anchor`/`block` markers: 0.
- `UNVERIFIED CITATION`, `HIGH-WARN`, `severity=HIGH-BLOCK`,
  `TERMINAL-BLOCK`, and `READ-LEDGER-INVALID` tokens: 0.
- Required declarations, AI-use disclosure, limitations, English abstract,
  Chinese abstract, keywords, author identity, affiliation, and contact:
  present.

Result: `FORMATTER_HARD_GATE=PASS` and `CURRENT_NUMERIC_PLAINNAT_LOCK=PASS`.

## Isolated LaTeX replay

An isolated temporary-directory replay completed via:

```text
LuaLaTeX -> BibTeX -> LuaLaTeX -> LuaLaTeX
```

The replay produced a 13-page A4 PDF with no fatal errors, unresolved
citations/references, overfull boxes, or missing glyphs.  The accepted and
replayed PDFs have byte-identical `pdftotext -layout` output with SHA-256
`5bdca519563858a0c084c2315f5f28d0132f0ad9b1459c07294953bfdab64c67`.
The PDF container hashes differ because the replay carries a new PDF creation
timestamp; this is not a content difference.

## Non-authoritative conversion check

Pandoc 2.9.2.1 is installed, but a temporary LaTeX-to-DOCX/Markdown trial did
not pass the content-preservation gate: it omitted or degraded theorem
environment labels, citation rendering, and several TeX math constructs.  The
configured output contract does not request DOCX.  Therefore no lossy DOCX is
promoted as an equivalent final paper.  LaTeX remains the authoritative source
and the final PDF will be compiled directly from it.

## Roadmap and authority preservation

Route A remains `NOT_TESTABLE`; Route B remains `ROUTE_B_NOT_TESTABLE`; Gates
A--E remain `NOT_REACHED`, with no gate credit.  Submission, public release,
Git action, external contact, venue-readiness claims, and Route advancement
remain outside Stage-5 authority.

## In-stage content confirmation

The scholar should review `stage5_finalization/content_proof.pdf` (or the
byte-identical `paper/paper.pdf`) and confirm that the content is correct.  On
confirmation, Stage 5 will compile and verify the final PDF and finish the
submission-package manifest without changing the accepted manuscript text.
