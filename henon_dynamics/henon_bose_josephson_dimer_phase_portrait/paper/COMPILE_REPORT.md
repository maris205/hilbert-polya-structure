# C243 compile report

- Engine: LuaLaTeX, two passes for each of revisions 0, 1 and 2.
- Fixed environment: `SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`,
  `TZ=UTC`, `LC_ALL=C`.
- Artifacts: `main_round0_original.pdf`, `main_round1.pdf`,
  `main_round2.pdf`; final `main.pdf` equals round 2 byte-for-byte.
- Checks: PDF pages, embedded fonts, extracted-text coverage, references,
  undefined-reference/citation scan, and absence of build sidecars.
- Warnings: first passes may emit the normal rerun notice; final passes have
  no undefined references, missing citations, overfull boxes, or font warnings.

The final text includes the quartic/elliptic-period formulas, small-amplitude
limits, sech homoclinic, connected-level/separatrix distinction, the
\(\Lambda=1\) isolated critical point, and the \(\Lambda=2\) Bloch-pole
boundary.

Final PDF SHA-256 values (after the coordinate-command typography repair):

| artifact | SHA-256 |
|---|---|
| `main_round0_original.pdf` | `1bf4177428793dbd135b56cbcf54a2360add09c45ea25bf9ba2a928a246ffbcb` |
| `main_round1.pdf` | `d85fac19fd24ad3826177cf9329d4978d8f7f5f9efeec0ef7c63f8a7033b5b8c` |
| `main_round2.pdf` / `main.pdf` | `f83a93ceff68654d276ee330051c427b1283965856c03a1734678c160cf2bc2b` |

Each revision was rebuilt in two independent temporary trees; the paired
outputs were byte-identical and the settled logs were warning-free.
