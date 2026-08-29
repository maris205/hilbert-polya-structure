# P111 final QA

QA date: 2026-08-29 UTC

## Verdict

**Internal Stage 2 package: mechanical PASS. External release: HOLD.**

Two independent nonauthor reviews reconstructed the complete theorem tree.
The retained repairs add the P93 update-rule firewall and subtract the direct
Takács/Janson ownership of the fair binary lattice-path/random-word inversion
specialization. No unresolved critical or mathematical major defect remains.

## Exact-control gate

- command: `python3 code/verify.py`;
- exit status: 0; stored stdout: byte-for-byte match;
- exact assertions: **421,285**;
- all 131,071 binary words through length 16, with literal matrix products,
  independent word-area scans, Gaussian slices, exact biased moments,
  covariance/decomposition checks, endpoints, extrema, and pressure bounds;
- exact integer and rational arithmetic only; no sampling.

## Build and bibliography gate

- sequence: pdfLaTeX, BibTeX, pdfLaTeX, pdfLaTeX; all stages exited 0;
- deterministic extra pdfLaTeX pass reproduced the PDF SHA-256;
- LaTeX/package warnings, undefined citations/references, multiply-defined
  labels, overfull/underfull boxes, errors, and rerun requests: **0**;
- bibliography: 6 cited keys, 6 resolved entries, 0 missing, 0 uncited.

## PDF gate

- artifact: `main.pdf`;
- SHA-256: `b8e12c56d072ef7e3fa7fe6c478256f6fbeb6da2dc37126453e079174c5c4476`;
- 7 A4 pages; 316,032 bytes; PDF 1.5; rotation 0;
- encryption, JavaScript, and forms: absent;
- visible author: Anonymous; PDF Author metadata: empty;
- fonts: 21/21 embedded, subsetted, and Unicode-mapped;
- searchable layout text: 25,570 bytes, 397 lines; sentinel scan: clean.

## Visual gate and release boundary

All seven pages were freshly rendered and inspected. The exact normal form,
Gaussian-binomial law, two moment routes, SLLN/CLT proof, norm-exponent
boundary, positive/negative pressure arguments, owner firewall, conclusion,
and six references are legible and uncropped. No overlap, malformed display,
unintended blank page, broken citation, or stray `qquad` token remains.

`SHA256SUMS` covers and verifies the final evidence package. Classical
inversion laws and fair-word limits receive no novelty credit; specialist
direct-owner review of the residual arbitrary-bias conjunction remains open.
External posting, submission, contact, venue choice, and novelty or priority
language remain **HOLD**.
