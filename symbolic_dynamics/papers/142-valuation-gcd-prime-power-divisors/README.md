# P142 — Valuation--GCD dynamics on prime-power divisors

Status: **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**.

This anonymous mathematical short note studies, for an odd prime `p` and
`e>=2`, the literal finite self-map

```text
d -> gcd(p^e, d^2 + p^e/d)
```

on the divisors of `p^e`.  It proves the exact exponent rule
`a -> min(2a,e-a)`, the complete recurrent set and fixed-iterate counts, the
pointwise entry-time law and unique sharp deepest divisor, the temporal
polynomial, and the image and fibre over every target.  The characteristic-two
equal-valuation failure is displayed explicitly.

General valuation algebra, finite-map and zeta bookkeeping,
piecewise-monotone interval dynamics, and finite/discretized tent maps receive
zero contribution credit.  A bounded direct-owner non-hit is not novelty,
priority, or ownership evidence.  The arithmetic lift remains subject to a
cosmetic-encoding kill condition.

## Package map

- `main.tex`, `references.bib`: anonymous `amsart` source and three-source
  verified bibliography.
- `main.pdf`: current five-page A4 reviewed build.
- `main_round0_original.pdf`: immutable pre-review Round-0 build.
- `main_round1.pdf`, `main_round2.pdf`: frozen reviewed builds.
- `verify_p142.py`, `verification_output.txt`: focused exact verifier and
  canonical stdout.
- `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`: theorem narrative, architecture,
  no-figure decision, and release gate.
- `CLAIMS_EVIDENCE.md`: claim--proof--control ledger.
- `SOURCE_VERIFICATION.md`: claim-level verification of the three primary
  background sources already present in the scout.
- `CONTROL_RESULTS.md`: exact coverage and selected frozen profiles.
- `BUILD.md`: reproducible build and artifact audit.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`, `IMPROVEMENT_LOG.md`: two
  independent review records and repair closure.

## Reproduce the exact control

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p142.py
cmp -s verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 verify_p142.py)
```

The frozen run contains 319,074 exact assertions and ends with
`STATUS=PASS`.  It uses exact integers without sampling, floating point,
network access, a computer algebra system, or third-party packages.

## Compile

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The settled build has zero warnings, zero bad boxes, and zero undefined
citations or references.  All fonts are embedded and the identifying PDF
metadata fields are blank.

No novelty, priority, authorship, posting, specialist contact, submission, or
external-release decision is made.  External status remains `HOLD_EXTERNAL`.
