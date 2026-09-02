# P166 — Hamming-weight translation dynamics

Status: **Round 2 internal accept / Reviews A and B accepted 0C-0M-0m /
`HOLD_EXTERNAL`**.

The literal system is

```text
H_n = (Z/nZ)^n,       T_n(x) = x + wt(x) 1,       n >= 2,
```

where `wt(x)` is the integer number of nonzero coordinates before the
translation is reduced modulo `n`.

## Main outcome

Diagonal translation gives an exact `n`-phase model
`g_m(j)=j+m_j`.  From it the paper proves two independent axes:

1. complete recurrent and transient dynamics: nontrivial-cycle mass
   exhaustion, all exact periods, zeta function, every exact depth, sharp
   maximum `n-2`, and the last shell;
2. every-target one-step inversion: an exact fibre formula, a marked EGF,
   the image size, and the sharp maximum fibre.

The every-time formula is deliberately scoped as a target-local `n`-phase
oracle.  It is not presented as a closed global all-time fibre census.

## Artifact map

- `main.tex`, `references.bib`: anonymous self-contained manuscript.
- `main.pdf`: canonical four-page PDF, unchanged from Round 0.
- `main_round0_original.pdf`: frozen byte-identical Round-0 copy.
- `main_round1.pdf`: no-change Review-A freeze, byte-identical to Round 0.
- `main_round2.pdf`: no-change Review-B freeze, byte-identical to all prior PDFs.
- `PAPER_PLAN.md`: claim-first paper architecture.
- `NARRATIVE_REPORT.md`: problem, mechanism, results, and scope narrative.
- `CLAIMS_EVIDENCE.md`: theorem-to-proof-to-control traceability.
- `CONTROL_RESULTS.md`: exact executable evidence.
- `SOURCE_VERIFICATION.md`: bounded source audit and metadata checks.
- `SELF_QA.md`, `BUILD.md`, `PAPER_BUILD_STATUS.md`: author QA and build
  provenance.
- `FINAL_QA.md`: final verifier, review, build, PDF, and lifecycle closure.
- `IMPROVEMENT_LOG.md`: both review decisions and no-change transitions.
- `code/verify.py`, `code/CANONICAL.txt`: deterministic standard-library
  verifier and its frozen transcript.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The verifier transcript must match `code/CANONICAL.txt` byte for byte.
Independent Hostile Reviews A and B both returned zero findings.  Review A
reported 11,795,304 assertions; Review B reported 14,005,344 assertions and
`ACCEPT_INTERNAL`.  Neither review required a source, proof, bibliography,
verifier, or PDF repair.  This directory is not externally cleared:
**`HOLD_EXTERNAL`**.
