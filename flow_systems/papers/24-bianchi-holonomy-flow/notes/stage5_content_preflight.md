# Paper 24 Stage-5 content preflight

Date: **2026-08-31**  
Mode: **academic-paper / format-convert (Phase 7)**  
Citation profile: **retain `natbib[numbers,sort&compress] + plainnat`**  
Result: **PASS for content review; Stage 5 remains in progress**

## Frozen inputs and mechanical transformation

| Artifact | SHA-256 |
|---|---|
| Accepted TeX `notes/stage4_prime_revision_round2.tex` | `79735d058d965a35de10cc0b3655e0b1db5217bde00e02d2d48b7564cd841afc` |
| Accepted BibTeX `paper/references.bib` | `11e7dd42f07ecf22744f5d9c829d13a22212e0d43cb2591c0e9dfd66bde86d87` |
| Accepted preview `notes/stage4_5_round2_preview.pdf` | `7422198864a2c980c2033ab1851e4ef03886a4633cc644bb4fcef7b33576eaea` |
| Stage-5 TeX `stage5_finalization/manuscript.tex` | `153e80d360b35c25cac8f0ad2fc1cea14ba43afed07ce7fbb59b9f48c7baeb4e` |
| Stage-5 BibTeX `stage5_finalization/references.bib` | `11e7dd42f07ecf22744f5d9c829d13a22212e0d43cb2591c0e9dfd66bde86d87` |
| Content proof `stage5_finalization/content_proof.pdf` | `7422198864a2c980c2033ab1851e4ef03886a4633cc644bb4fcef7b33576eaea` |

The accepted source contains 121 standalone block-marker lines and no
`ref`/`anchor` markers. Deleting those 121 lines reproduces the Stage-4.5
receipt's marker-stripped source hash exactly. A line-sequence comparison
confirms that every non-marker line is byte-preserved. The bibliography and
content proof pass byte-for-byte `cmp` against their accepted inputs.

## Citation, bibliography, and formatter hard gate

- Citation commands: **9**; unique citation keys: **7**.
- BibTeX entries: **7**; duplicate keys: **0**.
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

All four commands exited `0`. The replay produced a 15-page A4 PDF with no
fatal error, unresolved final-pass citation/reference, overfull box, or missing
character diagnostic. The transient replay PDF had SHA-256
`0fc0b178a82e3e6bbc122b0ee12906e0aded9bc5cfe20bdb14fb1af77ee7133f`;
it was not retained or promoted as a final paper.

`pdftotext -layout` output from the replay and the accepted content proof is
byte-identical, with SHA-256
`f72efc209a139b7eb586b4db5b5b2ab9f8850d4728931c6c9f0882359c073931`.
This verifies rendered-text preservation for the recorded toolchain; it is not
a PDF byte-reproducibility or scientific-correctness certificate.

## Pandoc lossiness check

Pandoc 2.9.2.1 is installed. Citation-aware LaTeX-to-DOCX conversion cannot run
in this environment: `--citeproc` is unsupported (exit `6`), while the legacy
bibliography path exits `83` because `pandoc-citeproc` is absent. A separate raw
LaTeX-to-DOCX/round-trip diagnostic exits successfully but emits **14 math
conversion warnings** and loses the authoritative `natbib`/`plainnat` profile,
all six `\newtheorem` declarations, theorem-family environment tags,
11 `\cref` calls, nine `\citep` calls, and the BibTeX linkage.

The diagnostic DOCX and round-trip files were temporary and were not retained.
No DOCX is promoted as content-equivalent; LaTeX remains authoritative.

## Route and authority boundary

The paper tuple remains
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`; the physical
flow remains `UNASSIGNED`; Route B remains `UNINVOKED`. Stage-5 formatting gives
no route or gate credit and changes no scientific result. The batch facts
remain positive arithmetic A2 `0/5`, Route-B invocations `0/5`, and 19 model
instances as structured stress tests rather than independent samples.

## Next required action

The scholar should inspect `stage5_finalization/content_proof.pdf` and provide
one explicit content confirmation. No final `paper.pdf` exists at this point.
