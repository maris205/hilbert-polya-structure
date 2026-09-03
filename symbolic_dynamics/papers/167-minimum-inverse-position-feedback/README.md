# P167 — Minimum Inverse-Position Feedback

**Status:** `ROUND2 DUAL-REVIEW FREEZE / GREEN_OWNER_THIN / HOLD_EXTERNAL`  
**Format:** anonymous `amsart` 10pt short theory note  
**Final repaired PDF:** 4 A4 pages, 285,799 bytes

## Result

For `X_n=[n]^[n]`, the literal feedback map sends coordinate `i` to the
least position carrying symbol `i`, and sends an absent `i` to `i` itself.
The frozen theorem gives:

- cycle inversion and endpoint-controlled path reversal/splitting;
- sharp carrier height `2n-2` and first-image height `2n-3` for `n>=2`;
- the connected recurrent census, labelled EGF, involution fixed counts,
  all positive-iterate counts, and the finite-map zeta function;
- an exact product/sum for the fibre of every target, including zero fibres;
- maximum fibre `B_n`, attained by the identity;
- explicit complete boundary rows for `n=1,2,3`.

The theorem is deliberately owner-thin.  Least kernel transversals,
first-occurrence/set-partition encodings, functional-graph language,
labelled component calculus, involution and Bell numbers, and zeta
conversion are all background.  The bounded owner non-hit grants no
external lifecycle permission.

## Core artifacts

- `main.tex` — complete anonymous manuscript.
- `main.pdf` — settled canonical Round-2 PDF after both hostile reviews.
- `main_round0_original.pdf` — immutable author Round-0 freeze.
- `main_round1.pdf` — immutable post-Review-A repair freeze.
- `main_round2.pdf` — byte-identical final dual-review freeze.
- `references.bib` — five cited, primary-source-verified background records.
- `verify_p167.py` — standalone standard-library verifier.
- `verification_output.txt` — byte-identical frozen verifier stdout.
- `PAPER_PLAN.md` — claim-aligned short-note plan.
- `NARRATIVE_REPORT.md` — temporal/inverse narrative and risk boundary.
- `CLAIMS_EVIDENCE.md` — frozen claim/evidence ledger.
- `SOURCE_VERIFICATION.md` — primary-source metadata and subtraction record.
- `BUILD.md` — replay, build, PDF, and hash ledger.
- `SELF_QA.md` — author-side mathematical, source, anonymity, and visual QA.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md` — two independent hostile
  review records.
- `IMPROVEMENT_LOG.md` — exact repair and closeout record.
- `SHA256SUMS` — paper-local integrity manifest.

The independent pre-paper hostile candidate gate froze the contract before
drafting and is not relabelled as either manuscript review.  Review A found
one bibliographic-year repair; Review B accepted every theorem and found one
packaging inconsistency, now closed.  Neither review changed a theorem,
formula, proof, verifier, claim ceiling, or lifecycle decision.

## Reproduce the verifier

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p167.py > replay.txt
cmp replay.txt verification_output.txt
sha256sum verify_p167.py verification_output.txt
```

Expected result:

```text
decision: AUTHOR_ROUND0_PASS
assertions: 12,603,676
verifier SHA-256: b7c10bd3738362397a97361ca3780c4f53c7297efbe3e1885175634b345b457b
transcript SHA-256: 1e7348f9eab389cffc14582b3cf26ebeec69cb72a6c77dbdb1fb204abd1e1a8c
```

## Rebuild the PDF

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final settled PDF SHA-256 is
`b32b14735d21a4354b7dfc242a98bb7a137d6ae1f5552fe0a4ea623500ad53b9`.
Two Review-B source-only cold builds matched this artifact byte for byte.
The immutable Round-0 PDF retains SHA-256
`81bfa2ed4944f2750558f06cbb3a09d7081fc0361a0361f05f91869368faf379`.
