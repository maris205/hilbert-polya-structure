# Paper 28 Stage-5 content preflight

Date: **2026-08-31**  
Mode: **academic-paper / format-convert (Phase 7)**  
Citation decision: **retain current natbib numeric + plainnat style**  
Status: **PASS; Stage 5 remains in progress awaiting one content confirmation**

## Accepted-input lock

| Artifact | SHA-256 |
|---|---|
| Batch Round-9 Stage-4.5 Round-2 input lock | `bcfc097598a062fa91176aebb76be41a28eda7699c4a39ccaaaf2426194b8b30` |
| Accepted `notes/stage4_prime_revision_round1.tex` | `126783db66949396f7b3b494e06f55e4deedcc9f443f29e6477e6254676d472e` |
| Accepted `paper/references.bib` | `95728b0a7120e5df341a364ff77f65f5c1d4628d55a6e584e2de7d747d8ca63e` |
| Accepted Stage-4.5 content proof | `253d10080331076a14d658afc423a72b2f687eadcfb68c6e482cec03aabae382` |
| Stage-4.5 machine integrity report | `29c2808742e5af9456a01cc56e40b2c443b70d4e65578563eb90098532b16659` |
| Stage-4.5 final integrity report | `9ce7de406d5f28e6a5efcfa1320c653296d2b7f639ed278507e78e1deafd6fa7` |
| Stage-5 input manifest | `8fb6e0646c9b9eb4bb7643363548f723c3daf4e019df617c2b4c657e6f88e18f` |

The Stage-4.5 verdict is `PASS`.  The #660 phrase-list carrier records
`not_checked / SNAPSHOT_NOT_PROVIDED`, and the #672 diagnostic records
`ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE`; both bind the same accepted
draft and are nonblocking orchestrator-owned carriers.  This formatter
preflight neither created nor altered them.

## Marker-only source conversion

The accepted draft contained 127 HTML comments, all of them standalone ARS
block markers.  A byte-preserving filter removed only lines matching
`^[ \t]*<!--block:B[0-9]{4}-->[ \t]*$`:

- input: 52,917 bytes and 1,168 lines;
- output: 50,504 bytes and 1,041 lines;
- removed: 127 lines and 2,413 bytes;
- remaining HTML comments or ARS markers: 0;
- reconstruction of the output by filtering the accepted bytes: exact match.

The stripped source is `stage5_finalization/manuscript.tex`, SHA-256
`14ad8eeaa7cdd55bc889adc250630a7b18a9e20e316d4fb6becddb9e05922d22`.
No manuscript-content line was rewritten.

## Formatter, citation, and declaration gates

- `\usepackage[numbers,sort&compress]{natbib}`: present.
- `\bibliographystyle{plainnat}`: present.
- Citation commands: 9; citation-key occurrences: 9; unique keys: 6.
- BibTeX entries: 6; cited-but-missing keys: 0; bibliography orphans: 0;
  duplicate keys: 0.
- Undefined citations/references after the four-step replay: 0/0.
- Formatter refusal tokens, `<!--ref:...-->`, `<!--anchor:none:...-->`,
  unresolved `HIGH-WARN`, `severity=HIGH-BLOCK`, `TERMINAL-BLOCK`, and
  `READ-LEDGER-INVALID`: 0.
- Required-content gate: 16/16 present — title; author identity; affiliation;
  contact; English abstract; Traditional-Chinese abstract; both keyword sets;
  Limitations; Declarations; Funding; Conflict of interest; CRediT author
  statement; Data and code availability; Ethics statement; and AI-Assisted
  Research Disclosure.
- `references.bib` is byte-identical to the accepted bibliography.
- `content_proof.pdf` is byte-identical to the accepted Stage-4.5 preview.

Results: `FORMATTER_HARD_GATE=PASS`, `CITATION_BIB_GATE=PASS`,
`DECLARATION_GATE=PASS`, and `CURRENT_NUMERIC_PLAINNAT_LOCK=PASS`.

## Isolated LaTeX replay

An isolated preflight workspace ran, in order:

```text
LuaLaTeX -> BibTeX -> LuaLaTeX -> LuaLaTeX
```

with `SOURCE_DATE_EPOCH=1788134400`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, and
`-interaction=nonstopmode -halt-on-error`.  The replay produced a 14-page A4
PDF, SHA-256
`603969c3eb9143350192b3707115b3b7c8f4d578d9a5a87f5bad128ce1038d9a`.
The final build log has SHA-256
`8e9150df809ad2a34f2a7531b4e4eea4bcedb1d2862203797050ce7469933cac`.

Fatal errors, unresolved citations, unresolved references, overfull boxes,
missing characters/glyphs, and BibTeX warnings were all zero.  The temporary
replay PDF is verification evidence only and is not promoted or retained as
the final paper.

## PDF text equivalence

`pdftotext -layout` over both the copied content proof and the isolated replay
produced 51,436-byte text streams with identical SHA-256
`2e7c021043d9d5e00e561bcc134a047df00f957d39b91bf48fd856f74861f1ff`.
Therefore the accepted proof and the marker-stripped replay are text-equivalent
under the recorded extractor.  PDF container hashes are not used as the
content-equivalence criterion.

## Pandoc lossiness diagnostic

Pandoc 2.9.2.1 parsed the LaTeX source without a runtime error.  It retained
30/30 headings and 9/9 citation nodes, but the conversion is not
content-equivalent:

- the final `\bibliography{references}` command is not represented in the
  Markdown output;
- the literal `\path{results/round8_control_finite_ball_certificate.json}` is
  dropped, leaving the sentence's artifact-path slot blank;
- six theorem-style environments and the 26-label/34-cross-reference system
  are weakened into generic inline labels, spans, and links rather than the
  LaTeX theorem/cross-reference structure.

The Pandoc conversion therefore receives `LOSSINESS_GATE=FAIL_EXPECTED` and is
diagnostic only.  No DOCX or Pandoc-derived manuscript is delivered or claimed
equivalent.  LaTeX remains the authoritative format.

## Scientific and route boundary

The scientific result, declarations, subtype, canonical source, bibliography,
and result tree are unchanged.  Route A receives no new gate credit; A2 is not
evaluated.  Route B is not invoked.  The 19 recorded model instances remain
non-independent diagnostic/calibration instances.  This preflight PASS is a
formatting result, not scientific validation, venue readiness, or Route
promotion.

## One required in-stage confirmation

The scholar should review
`stage5_finalization/content_proof.pdf`.  One explicit confirmation that its
content is correct is required before the final PDF is built.  Until then,
`stage5_finalization/paper.pdf` must remain absent and Stage 5 remains
`in_progress`.
