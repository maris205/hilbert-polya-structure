# Paper 25 Stage-5 content preflight

Date: **2026-08-31**  
Mode: **academic-paper / format-convert (Phase 7)**  
Citation profile: **retain `natbib[numbers,sort&compress] + plainnat`**  
Result: **PASS for content review; Stage 5 remains in progress**

## Frozen inputs and mechanical transformation

| Artifact | SHA-256 |
|---|---|
| Accepted TeX `notes/stage4_revision_round1.tex` | `39a643c05b4820b782e45a5ec240caa7223ad444229e8a89bdcc98791ce23835` |
| Accepted derived BibTeX `notes/stage4_5_references_corrected_round1.bib` | `a0bf0cd2f022f1b5dcc0bffdd1b28d135cef7c287f77c2a46e514480e2b3b5ab` |
| Accepted preview `notes/stage4_5_round2_preview.pdf` | `34c5351403f81c22a16b8de0fa4e9011b0b3b5a5b7be6c321a25d47e4724fe65` |
| Stage-5 TeX `stage5_finalization/manuscript.tex` | `9c7782ebf6a90f0e33ab86f2e77d7ce78ecfb2ad0ddb9413e4829cfe33f776e1` |
| Stage-5 BibTeX `stage5_finalization/references.bib` | `a0bf0cd2f022f1b5dcc0bffdd1b28d135cef7c287f77c2a46e514480e2b3b5ab` |
| Content proof `stage5_finalization/content_proof.pdf` | `34c5351403f81c22a16b8de0fa4e9011b0b3b5a5b7be6c321a25d47e4724fe65` |

The accepted source contains 116 standalone block-marker lines plus four
`ref` and four paired `anchor` comments. Block-line deletion alone yields
`08afbcb432b2f2105130abd5f608ee09149db07ecc19dfcad1f8e91c146e56e7`,
exactly the Stage-4.5 preview receipt's derived-source hash. Removing the eight
inline comments then yields the Stage-5 hash above. A mechanical comparison
confirms that the two hashes differ only by those eight comment deletions and
that every non-marker byte is preserved. The bibliography and content proof
pass byte-for-byte `cmp` against their accepted inputs.

## Citation, bibliography, and formatter hard gate

- Citation commands: **13**; unique citation keys: **8**.
- BibTeX entries: **8**; duplicate keys: **0**.
- Cited-but-missing keys: **0**; bibliography orphans: **0**.
- Numeric `natbib` declaration: **1**; `plainnat` declaration: **1**.
- ARS `ref`/`anchor`/`block` markers in the Stage-5 source: **0**.
- `UNVERIFIED CITATION`, `HIGH-WARN`, `severity=HIGH-BLOCK`,
  `TERMINAL-BLOCK`, `READ-LEDGER-INVALID`, and `anchor:none`: **0**.
- `TODO`, `TBD`, `FIXME`, citation-needed, or author-confirmation placeholder
  tokens inside the manuscript/bibliography: **0**.
- English and Traditional-Chinese abstracts, keywords, limitations, author
  identity, affiliation, email, Funding, Conflict of Interest, Author
  contributions, Data and code availability, Ethics, and AI-Assisted Research
  Disclosure are present.

Result: **formatter refusal-token scan PASS; citation/BibTeX closure PASS**.

## Isolated LaTeX replay and content equivalence

An isolated temporary-directory build ran:

```text
LuaLaTeX -> BibTeX -> LuaLaTeX -> LuaLaTeX
```

All four commands exited `0`. The replay produced a 13-page A4 PDF with no
fatal error, unresolved final-pass citation/reference, overfull box, or missing
character diagnostic. Ten underfull-box diagnostics are retained as
nonblocking layout information. The transient replay PDF had SHA-256
`3bbaf7a2f71173d512f62d6235f1d96f23930daf7a1cb5d6e9305b267ede57b0`;
it was not retained or promoted as a final paper.

`pdftotext -layout` output from the replay and the accepted content proof is
byte-identical, with SHA-256
`60aedb5e593ad6971ed37cda6206e2eab0aefc5653064f10f516f9208408b185`.
Thus removal of the eight inline provenance comments causes no rendered-text
change. This verifies rendered-text preservation for the recorded toolchain;
it is not a PDF byte-reproducibility or scientific-correctness certificate.

## Pandoc lossiness check

Pandoc 2.9.2.1 is installed. Citation-aware LaTeX-to-DOCX conversion cannot run
in this environment: `--citeproc` is unsupported (exit `6`), while the legacy
bibliography path exits `83` because `pandoc-citeproc` is absent. A separate raw
LaTeX-to-DOCX/round-trip diagnostic exits successfully but emits **39 math
conversion warnings** and loses the authoritative `natbib`/`plainnat` profile,
all six `\newtheorem` declarations, theorem-family environment tags,
10 `\cref` calls, 13 `\citep` calls, and the BibTeX linkage.

The diagnostic DOCX and round-trip files were temporary and were not retained.
No DOCX is promoted as content-equivalent; LaTeX remains authoritative.

## Route and authority boundary

The typed symbolic tuple remains
`(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)` for the
unit-roof calibrator only; the physical-flow tuple remains `UNASSIGNED`; Route
B remains `UNINVOKED`. Stage-5 formatting gives no route or gate credit and
changes no scientific result. The batch facts remain positive arithmetic A2
`0/5`, Route-B invocations `0/5`, and 19 model instances as structured stress
tests rather than independent samples.

## Next required action

The scholar should inspect `stage5_finalization/content_proof.pdf` and provide
one explicit content confirmation. No final `paper.pdf` exists at this point.
