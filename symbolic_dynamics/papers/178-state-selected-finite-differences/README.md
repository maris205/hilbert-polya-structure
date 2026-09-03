# P178 — State-Selected Finite Differences

Anonymous AMS short note, Round 2 dual-review freeze.

## Status

- Scientific gate: `OWNER_THIN`.
- External lifecycle: `HOLD_EXTERNAL`.
- Hostile Reviews A/B: theorem package passed, provenance-only Minors closed,
  zero open findings.
- Figure: N/A; the proof-only no-figure phase is complete.
- Novelty, priority, release, circulation, and submission: not authorized.

## Literal system

For a prime \(p\), the carrier is every function
\(f:\mathbb F_p\to\mathbb F_p\), with

\[
T_p(f)(x)=f(x+f(0))-f(x).
\]

The paper proves the exact image at every time, every target fibre, the
sharp rooted functional graph, all depth shells, and every Jordan block of
the complex deterministic transition operator. The main inverse mechanism
is a unique backward integration after the selected direction is anchored
by the value at zero.

## Artifact package

- `main.tex` — anonymous deterministic `amsart` source.
- `references.bib` — only cited, primary-verified owner records.
- `main.pdf` — settled live Round-2/final PDF.
- `main_round0_original.pdf` — frozen byte-identical Round-0 copy.
- `main_round1.pdf` — immutable no-mathematics-change Round-1 copy.
- `main_round2.pdf` — byte-identical final dual-review receipt.
- `NARRATIVE_REPORT.md` — result story and scope.
- `PAPER_PLAN.md` — claims–evidence matrix, section plan, and page budget.
- `FIGURE_PLAN.md` — completed no-figure decision.
- `CLAIMS_EVIDENCE.md` — theorem dependency and evidence ledger.
- `SOURCE_VERIFICATION.md` — primary-source and internal owner subtraction.
- `verify_p178.py` — paper-local author-side standard-library exact verifier.
- `verification_output.txt` — canonical deterministic transcript.
- `BUILD.md` — reproducible build and artifact measurements.
- `SELF_QA.md` — mathematical, source, computation, anonymity, and visual QA.
- `IMPROVEMENT_LOG.md` — review finding and exact response.
- `FINAL_QA.md` — final two-review, cold-build, and PDF gate.

## Reproduce exact controls

From this directory:

~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 verify_p178.py
cmp -s verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 verify_p178.py)
~~~

The frozen run reports 44,689 assertions, 3,156 literal arrows, and
`RESULT=PASS`.

## Reproduce the paper

~~~sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

Exact toolchain, logs, page count, PDF inspection, and hashes are recorded
in `BUILD.md`.

## Ownership boundary

Fixed finite differences, augmentation-ideal nilpotence, affine kernel
fibres, fixed linear finite dynamics, and generic rank-to-Jordan conversion
receive zero contribution credit. A05 and P164 are explicitly subtracted.
Only the repeated state-selected direction, observable direction word, and
unique anchored lift remain as the paper's narrow conjunction. Bounded
search nonhits do not establish novelty; the package stays
`HOLD_EXTERNAL`.
