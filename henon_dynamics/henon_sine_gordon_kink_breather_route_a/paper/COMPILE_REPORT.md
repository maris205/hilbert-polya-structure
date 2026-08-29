# C236 compile report

Build contract: LuaLaTeX (LuaHBTeX 1.14.0), fixed
`SOURCE_DATE_EPOCH=1787875200`, two settled passes in each of two independent
fresh directories per revision.  Settled logs are scanned for warnings,
overfull/underfull boxes, undefined references, missing citations, duplicate
destinations, missing characters, and errors.  Final pages are visually
checked; all listed fonts must be embedded and subset.

| artifact | pages | SHA-256 |
|---|---:|---|
| `main_round0_original.pdf` | 2 | `145fab0cad6ae89cfdcf35135f443e5fd43f90034344f9693ab1ce6a5491606e` |
| `main_round1.pdf` | 2 | `567930a8bbccd9b2dc5bb4a2bb4d88985f178b54c14396260b9bf901fe1f672d` |
| `main_round2.pdf` | 2 | `46f0872ba2230fd24fe41761f0946a2d0f623d8d987c768fdcc233ddc047ad53` |
| `main.pdf` | 2 | `46f0872ba2230fd24fe41761f0946a2d0f623d8d987c768fdcc233ddc047ad53` |

The three round hashes are distinct and `main.pdf` is byte-identical to
`main_round2.pdf`.  All six fresh builds had two settled passes and clean
warning/reference scans; final fonts are embedded and subset.  The final
declaration block follows the references without an artificial blank page.
