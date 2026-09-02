# Compile report

Engine: LuaLaTeX, two passes per build, `SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`.

Each revision was compiled in two isolated fresh directories.  Both builds of each round were byte-identical to the corresponding archive.  Settled logs were warning-free: no LaTeX/package warning, overfull or underfull box, undefined reference, missing character, or rerun request.  All font rows were embedded and subset.

| round | pages | font rows | SHA-256 |
|---|---:|---:|---|
| 0 original | 3 | 23 | `7c3d1df6a841187f8a0e65ad73f5d4d850d1d3a0b4921beb21590960ea2ba4d6` |
| 1 | 3 | 23 | `42927de3b7740dd44e340c0b43c5796bf952efc0477dc052987378b2aefeef88` |
| 2 | 4 | 25 | `88ce6ad9ad23e0cebea986cf9305bc6b258c5816170120e656c334b0b38aed9e` |

The three hashes are distinct and `main.pdf` equals round 2 byte-for-byte.  Text extraction confirms the critical defective/not-stable language, all four point/sign/eigenvalue rank checks, the resonance-safe linear boundary, the 65/65 strict-JSON/strict-YAML hostile lane, Route-A scope, corrected Gascheau--Routh source ownership, and declarations.  Visual inspection found no clipping, overlap, blank page, or unreadable mathematical text.
