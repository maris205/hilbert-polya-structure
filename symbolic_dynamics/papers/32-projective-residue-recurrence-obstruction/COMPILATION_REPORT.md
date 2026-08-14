# Compilation report — Paper 32 / SD-C34

Status: **SUCCESS**

Build date: 2026-08-15 UTC
Manuscript: *Projective Residue Recurrence in Symbolic Dynamics: Universal
Modular Cycles and Cusp-Diamond Obstructions*

## Clean build

`latexmk` is not installed in the environment, so the documented fallback was
used from an empty temporary output directory:

    pdflatex → bibtex → pdflatex × 3

Only the final `main.pdf` was copied into the authority directory.  The final
directory retains no `main.aux`, `main.bbl`, `main.blg`, `main.log`,
`main.out`, or compilation transcript.

## Output

| Check | Result |
|---|---|
| PDF | `main.pdf` |
| pages | 18 |
| page geometry | A4, 595.276 × 841.890 pt |
| file size | 446,283 bytes |
| PDF version | 1.5 |
| title metadata | correct |
| author metadata | Anonymous Authors |
| fonts | 26/26 embedded and subset |
| raster images | 0 |
| vector figures | 3/3 pure TikZ |

The conclusion begins on page 14, references on page 15, Appendix A on page
16, and Appendix B on page 17.  Visual inspection covered the title/abstract,
all three diagrams, the Fredholm proof, the canonical census table,
bibliography, provenance hashes, and final decision ledger.  No clipping,
overlap, illegible label, or malformed page was found.

## Log and source audit

- TeX errors: 0.
- Undefined citations: 0.
- Undefined cross-references: 0.
- Overfull boxes: 0.
- Noncritical underfull boxes: 1 (`badness 1221`, the long theorem heading for
  Proposition 7.2); no text is lost or displaced.
- Stale rerun warnings after the fourth TeX pass: 0.
- Section modules included/present: 13/13.
- Figure inputs included/present: 3/3.
- Bibliography entries cited/present: 8/8, with no orphan or missing key.
- Draft markers (`TODO`, `FIXME`, `TBD`, `PLACEHOLDER`, `??`, `[?]`): 0.
- Text-tree hygiene: 71/71 files have exactly one terminal LF, no trailing
  whitespace, no CRLF, and no NUL byte.
- Route tuple in the PDF:
  `(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL,
  A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)`.
- Overall verdict: `ROUTE_A_REJECTED`; Route B: `LOCKED`.
- Branch decision:
  `CLOSE_EUCLIDEAN_PROJECTIVE_RESIDUE_RECURRENCE_BRANCH`.

The exact audit was synchronized after the canonical integration freeze:
4,819,026/4,819,026 independent checks pass; 13/13 deterministic assertions
pass; two fresh runs reproduce 16/16 primary artifacts byte-identically; and
the final-tree integrity audit reports `PASS`.

## Final fingerprints

| Artifact | SHA-256 |
|---|---|
| `main.pdf` | `199237c7d49b1e748cb5902c24087b2d8d1924773ad9a995d97c2d7aa41d6146` |
| `main.tex` | `b6ed5125f9ed6fe5c87e877afed0139fbff33d34dc5751ead7e78fcdc3c9378d` |
| `math_commands.tex` | `2711ba0b430d87fe3f43a8b036f8aa89575dec59b989215dd738c1c5feb6aaf6` |
| `references.bib` | `973e3d480f053ceca537c6935c1ccfbe7ff7bd1e3098d2455f8bf81809627307` |
| `SOURCE_LOCK.md` | `b16c081bd1685e8fe9ea1bb63d2045ada813092ed9975f9f43b5545f9607df0d` |
| `EXPERIMENT_REPORT.md` | `acafeb77e0c8a8272ae92dab7fdacc26fde11d73050506eda35423095ce06ce6` |
| Route-A v0.2 YAML | `304a0084773c0896d29acbb19c0101fb2273bbe16519c9ae8363e3e6aba51530` |
| canonical code/result ledger | `689a73a593f1791e6b2f49836b50cc2a11e5ddb1b91c46053af7aaa495ae4b8f` |

## Review boundary

No peer-review or LLM review loop was run, per the explicit project
instruction.  The checks above are deterministic compilation, citation,
artifact, typography, and visual-QA checks only.
