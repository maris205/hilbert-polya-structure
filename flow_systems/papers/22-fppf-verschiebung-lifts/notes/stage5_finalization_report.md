# Stage 5 finalization report

Project: `22-fppf-verschiebung-lifts`  
Stage: `5 — FINALIZE`  
Mode: `format-convert` with LaTeX as the authoritative source  
Date: `2026-08-26`  
Verdict: **PASS — final paper produced; FULL checkpoint pending**

## 1. Author decisions and immutable inputs

The scholar entered Stage 5 with the exact retained citation profile
`natbib[numbers,sort&compress] + plainnat`, then supplied the distinct in-stage
confirmation `内容确认`. The confirmation receipt is
`stage5_content_confirmation_20260826.md`, SHA-256
`a911f03772cba87b9e6e70a5573da9e87dcc609ce6a1eff18abe6471c8da7aa1`.

No scientific-content edit was authorized or made. The final package retains:

| Artifact | SHA-256 | Result |
|---|---|---|
| `paper/manuscript.tex` | `e90dd88109d4e53d1f789808286c15cc917003cd38b69f49ddaff8661b9158ed` | exact Stage-4.5 accepted source |
| `paper/references.bib` | `bd03813691db911316b18620ee4a1d212ac284fce7fb79af9f1b1cbc7ea71093` | exact verified bibliography |
| `stage5_finalization/content_proof.pdf` | `20e2d14f5a9e46b7d4f5eafac6669032c72fc69367fdf902e54440816a4a3f04` | retained confirmation proof |
| `paper/paper.pdf` | `e030259bb34c6d92af8fd53af80dce0e43200133c9bbdc91efb4f54e8f6c761a` | reproducible Stage-5 final PDF |

The package copy and authoritative `paper/` copy of each source and final PDF
are byte-identical.

## 2. Reproducible compilation

The accepted source and bibliography were compiled in two independent
temporary directories using LuaLaTeX -> BibTeX -> LuaLaTeX -> LuaLaTeX with:

```text
SOURCE_DATE_EPOCH=1787702400
FORCE_SOURCE_DATE=1
TZ=UTC
LuaTeX input wrapper:
\pdfvariable suppressoptionalinfo 512\relax\input{manuscript.tex}
```

The first diagnostic double-build, before the LuaTeX optional-info control was
added, produced identical page content but different random trailer IDs. Those
outputs were not promoted. Suppressing only optional-info bit 512 removed that
non-content source of nondeterminism without changing `manuscript.tex`.

The two final builds produced the identical SHA-256
`e030259bb34c6d92af8fd53af80dce0e43200133c9bbdc91efb4f54e8f6c761a`.
The final PDF and accepted content proof produced the identical
`pdftotext -layout` SHA-256
`5bdca519563858a0c084c2315f5f28d0132f0ad9b1459c07294953bfdab64c67`.
This establishes content equivalence while retaining the accepted proof as a
separate provenance artifact.

## 3. Content and citation checks

- Body length remains the independently reproduced Stage-2 value of 4,586
  words, inside the configured 4,500--5,500 band.
- English abstract: present.
- Chinese abstract: present.
- Keywords and MSC 2020: present.
- Numbered sections: seven, unchanged.
- Declarations: data/materials, ethics, author contributions, funding,
  competing interests, AI-use disclosure, and limitations all present.
- Citation commands: 21.
- Unique citation keys: 3.
- BibTeX entries: 3.
- Cited-but-missing keys: 0.
- Uncited BibTeX entries: 0.
- Duplicate BibTeX keys: 0.
- PDF/BibTeX mapping: `Deninger2025Rational -> [1]`,
  `DeningerMellit2019 -> [2]`, `StacksProject -> [3]`.

The formatter hard-gate scan found no ARS marker, unverified-citation marker,
high/block token, terminal token, `TODO`, `TBD`, `FIXME`, citation placeholder,
author-confirmation placeholder, or material-gap token in the final source and
bibliography.

## 4. PDF and render checks

- Pages: 13.
- Page size: A4 (`595.276 x 841.89 pt`).
- PDF version: 1.5.
- Final file size: 152,288 bytes.
- Fonts: 9/9 embedded, subsetted, and equipped with Unicode mappings.
- All 13 pages rendered and were visually inspected: no clipping, overlap,
  blank-page defect, broken equation, missing reference, or unreadable Chinese
  text was observed.
- Undefined citations: 0.
- Undefined references: 0.
- Overfull boxes: 0.
- Output `Missing character:` diagnostics: 0.
- Fatal errors / emergency stops: 0.

Nonblocking log information consists of two underfull Chinese-abstract lines,
one `lualatex-math` compatibility warning, two `unicode-math` command-override
warnings, and `microtype` configuration information. BibTeX reports
`warning$ -- 0`.

## 5. Submission-package verifier

The ARS verifier was run with the explicitly resolved `advisory` policy and a
freshness replay.

- Package fingerprint:
  `ae88ba5618ee5879542b02173e9db72562d0fcd96bddd98096f69d622abd4ac9`.
- Freshness: `fresh (policy=advisory)`.
- A1--A7: `NOT-APPLICABLE`; no anonymized variant and no declared
  double-blind review.
- B1--B5: `NOT-CHECKED`; no venue profile was declared, so venue limits were
  not guessed.
- C1: `PASS`; all 3 in-text citation keys occur in the BibTeX list.
- C2: `PASS`; all 3 BibTeX entries are cited.
- Terminal tokens: none (`TERMINAL-BLOCK`, `VERIFICATION-INCOMPLETE`, and
  `STALE-REPORT` absent).

This is a completed general-paper package, not a venue-compliance or
submission-readiness certificate.

## 6. Advisory and Route boundaries

- #660 remains exactly `HEURISTIC-ADVISORY / UNMEASURED / not_checked /
  SNAPSHOT_NOT_PROVIDED`; it is not a clean certificate.
- #672 remains exactly
  `ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE`; no carrier exists and it is
  not an agreement or clean result.
- Route A remains `NOT_TESTABLE`, with no tuple and no Gate A--E credit.
- Route B remains `ROUTE_B_NOT_TESTABLE`, with no invocation/entry authority,
  no tuple, no Hilbert--Pólya claim, and no Gate A--E credit.

The governing Route files retain their exact Stage-4.5 hashes:

- `skills/route-a-evaluator.md`:
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`;
- `skills/route-b-evaluator.md`:
  `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

## 7. Output-format decision and authority boundary

LaTeX, BibTeX, PDF, and Markdown audit sidecars are the configured outputs.
DOCX was not configured, and the installed Pandoc conversion loses theorem
labels, citation rendering, mathematical structure, and preamble semantics; no
lossy derivative is represented as content-equivalent. No cover letter was
generated because no venue was declared.

No submission, public release, Git action, external contact,
corresponding-author designation, venue-readiness claim, or Route advancement
was performed. Stage 6 remains optional and has not been entered.
