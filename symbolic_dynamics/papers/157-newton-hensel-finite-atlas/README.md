# P157 — Newton–Hensel finite atlas

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

This anonymous AMS short note studies the standard idempotent-lifting cubic
`F_n(x)=3x^2-2x^3` only as a finite dynamical system modulo `2^n`.  Its
residual temporal and one-step inverse package is deliberately narrow:

- the exact parity-selected temporal clock and shell census;
- the normalized-unit image split between `v=1` and `v>=2`;
- the explicit `N=1`, `N=2`, and `N>=3` predecessor laws;
- every-target full fibres, endpoint fibres, and closed image size.

The literal polynomial, idempotent lifting, and quadratic improvement are
prior background and receive zero contribution credit.  Burban–Drozd is used
as a direct prior/foundation record, not as an origination attribution.

## Exact replay

~~~bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p157.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p157.py > /tmp/p157_replay.txt
cmp -s /tmp/p157_replay.txt verification_output.txt
sha256sum /tmp/p157_replay.txt
~~~

The frozen transcript contains 2,563,880 exact assertions, ends in PASS, and
has SHA-256
`f5f1884f809110ca8ec3a954af1783c774896708495d626f694bbfb23f7876f1`.

## Rebuild

~~~bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

`BUILD.md` records the immutable Round-0/Round-1 histories and current
Round-2 PDF, logs, page counts, checksums, and quality gates.
`main_round0_original.pdf` is the immutable pre-review freeze.

## Package map

- `main.tex`, `references.bib`: manuscript and verified direct prior record.
- `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`, `PROOF_PACKAGE.md`: story, scope,
  and expanded proof spine.
- `CLAIMS_EVIDENCE.md`, `CONTROL_RESULTS.md`: evidence mapping and exact lanes.
- `SOURCE_VERIFICATION.md`: direct-prior verification and subtraction.
- `verify_p157.py`, `verification_output.txt`: paper-local falsifier and frozen
  deterministic transcript.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`, `IMPROVEMENT_LOG.md`:
  independent findings and author-side dispositions.
- `BUILD.md`: reproducible Round-0/Round-1/Round-2 build record.

Internal Round-2 completion does not authorize posting, submission,
circulation, author contact, or any other external action.
