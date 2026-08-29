# C234 compile report

Build contract: LuaLaTeX (LuaHBTeX 1.14.0), fixed
`SOURCE_DATE_EPOCH=1787875200`, two settled passes in each of two independent
fresh directories per revision.  Settled logs are scanned for warnings,
overfull/underfull boxes, undefined references, missing citations, duplicate
destinations, missing characters and errors.  Final pages are visually
checked; all listed fonts must be embedded and subset.

| artifact | pages | SHA-256 |
|---|---:|---|
| `main_round0_original.pdf` | 2 | `a3d268b97e461928e664e56d58c83ca29a00f1ed7d7d412c51b77880b696f330` |
| `main_round1.pdf` | 3 | `aa65259c6dd93b643734c1de4e63db0d95086e28c43251953e7b9433f8994b6c` |
| `main_round2.pdf` | 2 | `7d2ef519da3d2eaa3e2097457861b074920a229f44d6aa29db6cfd0dc45b3afa` |
| `main.pdf` | 2 | `7d2ef519da3d2eaa3e2097457861b074920a229f44d6aa29db6cfd0dc45b3afa` |

The three round hashes are distinct and `main.pdf` is byte-identical to
`main_round2.pdf`.  The revised round-2 source records the field-by-field
boundary audit (186 checker assertions; 37/37 hostile rejections) and the
corrected Lakshmanan DOI `10.1098/rsta.2010.0319`.  Both independent fresh
round-2 builds had two settled passes and clean warning/reference scans;
final fonts are embedded and subset.  The final declaration block follows
the references without an artificial blank page.

Integrity note: `main_round0_original.pdf` and `main_round1.pdf` are retained
as archival, superseded revision evidence.  Their historical reference line
predates the DOI/issue correction and must not be used as the release
citation.  The authoritative `main_round2.pdf`/`main.pdf` contains the
verified `369(1939)` issue and DOI `10.1098/rsta.2010.0319`.
