# Improvement log

External state: `HOLD_EXTERNAL`.

## Round 0 -> Round 1

Hostile Review A returned `REVISE — 0 Critical / 0 Major / 2 Minor`.

| Finding | Implemented repair | Closure evidence |
|---|---|---|
| m1: the fibre theorem omitted `n<m`, `n=m`, and empty-product boundaries | Made the theorem piecewise for every `n>=1`; set the `n<m` fibre to zero; defined the empty product as one; proved the same-rank fibre is one only for `id_m`; quantified the finite carrier by `N>=1` | `main.tex`, setup, Theorem 1(ii), and fibre proof |
| m1 executable closure | Added independent `n<m` and `n=m` boundary lanes to the verifier and exposed their cell counts in stdout | `verify_p156.py`, regenerated transcript, and synchronized evidence ledgers |
| m2: no explicit manuscript-level external-status declaration | Added the house External Status paragraph with literal `HOLD_EXTERNAL` and explicit posting/submission/circulation/contact boundary | `main.tex`, final declarations |

No withdrawn clock claim or global multi-step optimum was revived. Round-1
execution evidence is recorded after cold replay and source-only builds.

## Round-1 execution evidence

- A scrubbed-process replay completed 3,689,489 assertions, including 316,646
  `n<m` and 46,233 `n=m` boundary cells, and produced stdout byte-identical
  to `verification_output.txt`; transcript SHA-256 is
  `5c78864527c5781da43f79f8b2b667f9d915fd13fadaea09abe6a7c49f76f53e`.
- Two independent source-only four-command builds were mutually and
  canonically byte-identical. Settled logs contained no warning, bad box,
  unresolved item, or rerun request.
- All four pages were rasterized and inspected; the piecewise fibre theorem,
  same-rank proof, and External Status line are legible. Metadata, A4,
  anonymity, encryption/forms/JavaScript, and font checks passed.
- `main_round1.pdf` and `main.pdf` are byte-identical at SHA-256
  `7e222ce483cc755d4bb732f14ecf94d92ea13c505eba91212150308bebcc7979`
  (336,311 bytes). Round 0 remains unchanged.

## Round 1 -> Round 2

Hostile Review B returned `REVISE — 0 Critical / 0 Major / 1 Minor` after an
independent theorem rederivation, verifier replay, source-only build, and
four-page visual audit.

| Finding | Implemented repair | Closure evidence |
|---|---|---|
| m1: `BUILD.md` and `FINAL_QA.md` retained the Round-0 count of 26 font rows, while the Round-1/current PDF has 27 | Corrected both current ledgers to 27 and recorded that every row is embedded, subsetted, and Unicode-enabled | independent `pdffonts` checks in `HOSTILE_REVIEW_B.md`; corrected `BUILD.md` and `FINAL_QA.md` |

The finding was documentation-only.  No theorem, proof, bibliography,
manuscript source, verifier, frozen transcript, or PDF changed.  The canonical
Round-2 `main.pdf`/`main_round2.pdf` remains 4 A4 pages and 336,311 bytes at
SHA-256
`7e222ce483cc755d4bb732f14ecf94d92ea13c505eba91212150308bebcc7979`.
`main_round1.pdf` preserves the identical Review-A repair PDF, while Round 0
remains at
`ee5cedd089d9d837839f9fc715aae9530e19fc4f414dfcbef77ad0adfafa256c`.
All Review-A and Review-B findings are closed: 0 unresolved Critical, 0 Major,
and 0 Minor.  Status is `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.
