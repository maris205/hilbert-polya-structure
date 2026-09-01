# Build and QA record — P150

**Status: ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL.**

## Historical artifacts

- Engine: pdfTeX 1.40.22 / TeX Live 2022-dev; BibTeX 0.99d.
- Sequence: `pdflatex -> bibtex -> pdflatex -> pdflatex`.
- `main_round0_original.pdf`: first settled own-author artifact, 5 A4 pages,
  396,310 bytes, SHA-256
  `d94b53e9a1e496c766e8770e88f588053b7333e702b08177f0647578f90d274d`.
- `main_round1.pdf`: repaired post-Review-A artifact, byte-identical to current
  `main.pdf`.

## Accepted current artifact

- `main.pdf`: 5 A4 pages, 403,358 bytes.
- SHA-256:
  `26d0a73adb71b2e303ea637b5874939914cffd53f09a2230ded5775484c33dca`.
- Bibliography: 5/5 entries cited and resolved.
- Hone--Kouloukas metadata: version of record 57(3), 763--791 (2023), with
  online publication on 29 December 2022; source key, ledger, BibTeX year, and
  printed citation are consistent.
- Settled log: zero unresolved citations/references, rerun requests, build
  errors, bad boxes, or multiply defined labels.
- Fonts: all 29 reported font rows embedded and subsetted.
- PDF: version 1.5, A4, unencrypted, zero rotation, no form or JavaScript, and
  blank identifying title/author/subject/keyword metadata.
- Visual QA: independent Review B accepted all 5/5 pages with no clipping,
  overlap, broken glyph, malformed formula, unresolved marker, or illegible
  bibliography entry.

## Exact control

- Coverage: 31 odd finite fields and 110,095 state/target cells in each
  exhaustive enumeration role.
- Assertions: 2,144,131; `STATUS=PASS`.
- Fresh stdout is byte-identical to frozen `verification_output.txt`.
- Enumeration is exact falsification pressure, not a proof or ownership
  certificate.

## Reproducibility

- Volatile dates, trailer IDs, and pdfTeX source metadata are suppressed.
- Review B performed two isolated builds in separate temporary directories,
  each containing only `main.tex` and `references.bib` and using the frozen
  four-stage sequence.
- Both isolated PDFs are byte-identical to each other and to current
  `main.pdf` at the accepted digest above.

## Review and repair history

Hostile Review A returned **0 Critical / 0 Major / 2 Minor**. Both repairs are
present: the proof explicitly partitions nonfixed generic states into
five-element orbits and records `q=3`/characteristic-five boundaries; the
source ledger exposes replayable owner queries and subtracts Lyness (1942)
and Kanki (2013).

Hostile Review B returned **0 Critical / 0 Major / 1 Minor, REVISE**. It
accepted all substantive interfaces and found only that the old
`FINAL_QA.md` still presented round-zero provenance as current. The current
Markdown closure repairs that documentation defect; no review item remains
unresolved.

During this Markdown closure, root separately froze `main_round2.pdf`. A
read-only comparison confirms that it is 403,358 bytes and byte-identical to
current `main.pdf` at the accepted SHA-256. This closure did not create or
modify any PDF or `SHA256SUMS`. Internal acceptance does not authorize Git,
novelty/priority claims, posting, specialist contact, submission, or release.
External status remains `HOLD_EXTERNAL`.
