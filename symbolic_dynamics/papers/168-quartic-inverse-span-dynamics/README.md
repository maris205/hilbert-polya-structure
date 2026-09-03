# P168 — Quartic Inverse-Span Dynamics

**Status:** `ROUND2 DUAL-REVIEW FREEZE / GREEN_OWNER_THIN / HOLD_EXTERNAL`  
**Format:** anonymous `amsart` 10pt short theory note  
**Final no-change PDF:** 5 A4 pages, 322,829 bytes

## Result

On the complete `F_p`-subspace lattice of `F_{p^4}`, the literal update

```text
J(A)=span_Fp{a^(-1): 0 != a in A},   J(0)=0
```

has an exactly determined functional graph.  After assigning the published
patched-inversion classification and inverse-line geometry zero contribution
credit, the frozen note derives:

- the sharp maximum-tail jump: two steps at `p=2`, one step at every odd
  prime;
- the complete recurrent set, fixed/two-cycle census, depth enumerator,
  image stabilization, and finite-map zeta function;
- every target's fibre at every positive time, including the binary anomaly
  in which the 30 non-subfield planes map two-to-one onto 15 hyperplanes;
- the complete component graph: one full-field basin and otherwise bare
  recurrent cycles.

The theorem is deliberately owner-thin.  The bounded source non-hit has no
positive novelty or priority force, and the artifact remains
`HOLD_EXTERNAL`.

## Core artifacts

- `main.tex` — complete anonymous manuscript.
- `main.pdf` — settled canonical Round-2 PDF.
- `main_round0_original.pdf` — byte-identical Round-0 freeze.
- `main_round1.pdf` — byte-identical no-change post-Review-A freeze.
- `main_round2.pdf` — byte-identical final dual-review freeze.
- `references.bib` — six cited, primary-source-verified records.
- `verify_p168.py` — standalone standard-library exact verifier.
- `verification_output.txt` — frozen verifier stdout.
- `PAPER_PLAN.md` — claim-aligned short-note plan.
- `NARRATIVE_REPORT.md` — temporal/inverse narrative and ownership boundary.
- `CLAIMS_EVIDENCE.md` — frozen claim/evidence ledger.
- `SOURCE_VERIFICATION.md` — primary-source metadata and subtraction record.
- `BUILD.md` — replay, build, PDF, and hash ledger.
- `SELF_QA.md` — mathematical, source, executable, anonymity, and visual QA.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md` — two independent hostile
  review records.
- `IMPROVEMENT_LOG.md` — explicit no-change review closeout.
- `SHA256SUMS` — paper-local integrity manifest.

The independent pre-paper hostile gate fixed the theorem ceiling; it was not
a manuscript review.  Review A and Review B both returned
`PROVABLE AS STATED / 0 Critical / 0 Major / 0 Minor`.  Review B used two
separately implemented finite-field controls totalling 1,567,354 assertions.
No review changed the manuscript, bibliography, author verifier, theorem
ceiling, PDF, ownership decision, or lifecycle.

## Reproduce the verifier

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p168.py > replay.txt
cmp replay.txt verification_output.txt
sha256sum verify_p168.py verification_output.txt
```

Expected terminal rows and hashes:

```text
PASS total_checks=32754
decision=AUTHOR_ROUND0_PASS
external_status=HOLD_EXTERNAL_OWNER_THIN
verifier SHA-256: c3c40bfc0e92c19fe3a6fe6b7b924c7d0cb6f2a518f6478363701ae4bab1f6f1
transcript SHA-256: 8c0b77d99e976e9666ae658f4af7525ccf185f927948e660e3323a0f6f7f3d74
```

## Rebuild the PDF

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The settled PDF SHA-256 is
`846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e`.
Review B repeated two source-only cold builds and matched this artifact byte
for byte.  Round 0, Round 1, Round 2, and the live canonical all retain the
same hash.
