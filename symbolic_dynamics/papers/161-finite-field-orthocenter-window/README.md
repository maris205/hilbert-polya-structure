# P161 — finite-field orthocenter sliding window

**Status:** `ROUND-2 / REVIEW B ACCEPTED / HOLD_EXTERNAL`.

This anonymous AMS short note totalizes the orthocenter window on ordered
triangles over `F_p^2`, `p=3 mod 4`, by a sink.  Its narrow residual is:

- the three orientation-sensitive right-angle depths;
- the complete `0/1/(1+2R)` target-fibre law;
- the one-step and stable images;
- the `p=3` empty periodic-core but height-two boundary.

The orthocenter, orthocentric quartet, finite-field metrical triangle
geometry, elementary right-triangle counts, and period-four mechanism receive
zero contribution credit.

## Exact replay

~~~bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p161.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p161.py > /tmp/p161_replay.txt
cmp -s /tmp/p161_replay.txt verification_output.txt
sha256sum /tmp/p161_replay.txt
~~~

The frozen transcript contains 1,317,843 assertions, ends in PASS, and has
SHA-256
`26846bfd5cb94d397605f7f4dbf19b22bb29081fe43156e8e45c5ea2839f045c`.

## Rebuild

~~~bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

`BUILD.md` records the immutable Round-0 freeze, repaired Round-1 artifact,
and byte-identical Round-2 acceptance freeze, together with logs, page counts,
checksums, and warning gates.  `main_round0_original.pdf` is the immutable
pre-review freeze.

## Package map

- `main.tex`, `references.bib`: manuscript and three verified source records.
- `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`, `PROOF_PACKAGE.md`: claim
  architecture, readable account, and expanded proof spine.
- `CLAIMS_EVIDENCE.md`, `CONTROL_RESULTS.md`: evidence map and exact lanes.
- `SOURCE_VERIFICATION.md`: source distinction and zero-credit subtraction.
- `verify_p161.py`, `verification_output.txt`: paper-local exact falsifier and
  frozen transcript.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`, `IMPROVEMENT_LOG.md`: two
  independent reviews and author-side dispositions.
- `BUILD.md`: reproducible Round-0/Round-1/Round-2 build record.

Internal Round-2 acceptance does not authorize posting, submission,
circulation, author contact, or any other external action.
