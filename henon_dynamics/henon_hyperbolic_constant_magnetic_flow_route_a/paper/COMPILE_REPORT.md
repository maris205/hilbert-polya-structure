# Compile report

Engine: LuaLaTeX, two passes per build, `SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`.

Each revision was compiled in two isolated fresh directories.  Both builds of each round were byte-identical to the corresponding archive.  The settled second-pass logs were warning-free: no LaTeX/package warning, overfull or underfull box, undefined reference, missing character, or rerun request.  All `pdffonts` rows were embedded and subset.

| round | pages | font rows | SHA-256 |
|---|---:|---:|---|
| 0 original | 2 | 23 | `989ee3a527d893e2ba2e8f0a7d17ab82629a3225b5c4fec1cb6ecadd1a1b64b4` |
| 1 | 3 | 23 | `f63494f71de5b93efa02aed2b4a53785b47abba082adc25eb2bd26ef857a9f35` |
| 2 | 4 | 24 | `c3361619fe4d967223415894bd712a772989827a0ebc2de5b0fd98872b328cd1` |

`main.pdf` is byte-identical to round 2.  Text extraction contains the theorem, critical nilpotency, evidence nonclaim, Route-A tuple/scope literal, owner DOI tokens, and declarations.  Visual inspection found no clipping, collision, blank page, or unreadable type.
