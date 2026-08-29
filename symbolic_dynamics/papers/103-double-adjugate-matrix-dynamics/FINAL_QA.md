# P103 final QA

QA date: 2026-08-29 UTC

## Verdict

**Internal Stage 2 package: mechanical PASS after evidence strengthening.
External release: HOLD.**

The final tree incorporates the nonauthor review repairs: direct Cremona
attribution, an explicit `I_0` time convention, internal firewalls, and 850
new noncircular image-staircase/iterate assertions.

## Exact-control gate

- command: `python3 code/verify_double_adjugate.py`;
- exit status: 0; stored stdout: byte-for-byte match;
- final exact assertions: **141,190** (author freeze 140,340, audit delta
  +850);
- exhaustive literal-minor spaces: `M_3(F_2)`, `M_3(F_3)`, `M_4(F_2)`;
- independent scalar-line stabilization lanes: `t_*=0,1,2,4,1`;
- final line: `double-adjugate exact controls: PASS`.

## Build and bibliography gate

- sequence: pdfLaTeX, BibTeX, pdfLaTeX, pdfLaTeX; all stages exited 0;
- LaTeX/package warnings, undefined citations/references, multiply-defined
  labels, overfull/underfull boxes, errors, and rerun requests: **0**;
- bibliography: 4 cited keys, 4 resolved entries, 0 missing, 0 uncited.

## PDF gate

- artifact: `main.pdf`;
- SHA-256: `c2f31e00a677cffed632f381717ded6a7628d2ba84e1b375acab2b87340c619a`;
- 4 A4 pages; 296,320 bytes; PDF 1.5; rotation 0;
- encryption, JavaScript, and forms: absent;
- visible author: Anonymous; PDF Author metadata: empty;
- fonts: 23/23 embedded, subsetted, and Unicode-mapped;
- searchable layout text: 13,815 bytes; sentinel scan: clean.

## Visual gate and release boundary

All four pages were rendered and inspected.  The double-adjugate identity,
boxed iterate/fixed/image/depth formulas, alternating and third-period
signals, new `I_0` convention, `t_*=0,1,2,4,1` control disclosure, collision
firewalls, and four references are legible and uncropped.  No overlap,
malformed display, accidental blank page, or orphaned heading was found.

`SHA256SUMS` covers all final sources, controls, stored output, evidence and
review ledgers, this QA, and the PDF, and verifies entry by entry.  Classical
Jacobi/Cremona and scalar-power owners are subtracted; specialist priority
review remains open.  External circulation and priority language remain
**HOLD**.
