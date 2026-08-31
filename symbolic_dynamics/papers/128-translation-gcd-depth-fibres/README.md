# P128: translation--GCD depth fibres

Anonymous internal short-paper package for
`T(f)=gcd(f(x),f(x+1))` on monic `F_q[x]`, `q=p^a`.

## Current snapshot

- frozen state: **round2 / GO_INTERNAL**, with external release on hold;
- manuscript: 4 pages, anonymous `amsart`;
- lead result: exact all-depth formal orbit Euler product;
- second result: unit-fibre OGF plus every exact/capped invariant-target
  fibre;
- verifier: 180,453 exact assertions, including 50 literal truncated-matrix
  coefficient comparisons, over 17,523 monic states in explicit F4/F8/F9
  models;
- build: isolated `pdflatex -> bibtex -> pdflatex -> pdflatex`, status 0 at
  every stage, no warnings or bad boxes;
- external state: **HOLD_EXTERNAL**.

## Files

- `main.tex`, `references.bib`: anonymous source and primary-source
  bibliography;
- `main.pdf`: current working PDF;
- `main_round0_original.pdf`: immutable pre-review snapshot;
- `main_round1.pdf`: current post-Review-A snapshot;
- `main_round2.pdf`: support-only post-Review-B sign-off, byte-identical to
  round 1;
- `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`, `CLAIMS_EVIDENCE.md`: frozen claim
  architecture and evidence map;
- `code/verify.py`, `code/verification_output.txt`: independent
  extension-field falsifier and canonical stdout;
- `CONTROL_RESULTS.md`, `BUILD.md`: reproducibility records;
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`, `HOSTILE_REVIEW.md`, and
  `IMPROVEMENT_LOG.md`: two independent reviews, consolidated verdict, and
  exact repair map;
- `FINAL_QA.md`, `SHA256SUMS`: terminal paper-local audit and integrity
  manifest for the frozen round-two package.

## Reproduce the verifier

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | cmp -s - code/verification_output.txt
```

Expected terminus:

```text
TOTAL_ASSERTIONS=180453
scope_sentinel=finite extension-field enumeration is falsification evidence, never proof
credit_sentinel=old window/clock/fixed/depth results remain zero credit
release_sentinel=bounded owner non-hit is not novelty or priority; external HOLD
```

## Credit and collision firewall

The literal map, sliding window, order-`p` clock, invariant ring, fixed
counts, and old finite depth tables are zero credit.  Garefalakis/Reis own
the translation-fixed irreducible theory and Reis owns the displayed
`b_(pm)` formula.  P110 owns the order-dual semilattice orbit-fold mechanism
internally.  The surviving contribution is only the all-depth formal orbit
Euler product and target-refined unit fibres.  `Q^(-1)(1)` is a **unit fibre**, not a
monoid kernel; `Q` is not multiplicative.

No posting, submission, priority statement, or external novelty claim is
authorized.
