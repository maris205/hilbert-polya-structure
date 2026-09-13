# Paper 21 Deterministic R0 Repair-Build Authorization

Date: 2026-08-22 UTC

The final proof-first repair source has passed two genuinely fresh,
independent, read-only source reviews:

- R1: `INDEPENDENT_PAPER_SOURCE_R1_R0_REPAIR_REVIEW.md`, SHA-256
  `07114e0da0eb41ed827f86064186639ffed49c2be2db97bf3e016d7390fface0`,
  terminal `PAPER_SOURCE_R1_R0_REPAIR_PASS`.
- R2: `INDEPENDENT_PAPER_SOURCE_R2_R0_REPAIR_REVIEW.md`, SHA-256
  `3b606a9481811d795dd7fe5ebb16bf280898f56748e61045f8b802de0b063a3a`,
  terminal `PAPER_SOURCE_R2_R0_REPAIR_PASS`.

The only authorized build input is:

| File | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 84,917 | 1,990 | `34074c5965086d79145bf2b273398c4c17fdc264b6f5e3555fd1b9a2bd27c7b2` |
| `paper/math_commands.tex` | 981 | 33 | `05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a` |
| `paper/references.bib` | 675 | 19 | `4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8` |

Exactly two new independent temporary roots must each receive only these three
files and run, with fixed date/locale/timezone variables:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Acceptance is conjunctive: all stable outputs agree byte for byte; the source
trio remains unchanged; the substantive body through the conclusion occupies
24--29 pages; there is no fatal, undefined citation/reference, unresolved
marker, or overfull box; anonymous metadata and public scope are correct; and
all fonts are embedded, subsetted, and Unicode mapped. Underfull boxes may be
reported but are not independently fatal.

Only build-generated local artifacts and one canonical R0 receipt may be
persisted after PASS. Failure writes a blocker record and reopens no authority
by implication. Source editing, CAS/numerical/scientific execution, figures,
release, submission, upload, external messaging, and identity disclosure
remain unauthorized.

`BUILD_AUTHORIZATION_R0_REPAIR`
