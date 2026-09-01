# P139 — Lyndon-factor-start feedback

Anonymous Stage-2 Round-3 owner-repaired package for the map that replaces a
binary word by the start mask of its nonincreasing Chen--Fox--Lyndon factors.

Mantaci--Restivo--Rosone--Sciortino, *Journal of Discrete Algorithms* 28
(2014), 2--8, DOI `10.1016/j.jda.2014.06.001`, own the static equivalence
between Lyndon-factor starts and left-to-right suffix-rank minima.  The paper
imports that equivalence and the ordered-tail comparison with explicit zero
credit.  Its residual package is only the iterated start-mask dynamics, the
sharp depth `n` with a unique alternating source, and the target-wise
ordered-Lyndon fibre atlas.

## Files

- `main.tex`, `references.bib` — anonymous manuscript and verified references
- `main.pdf`, `main_round3.pdf` — identical current owner-repaired rendering
- `main_round0_original.pdf`, `main_round1.pdf`, `main_round2.pdf` — preserved
  pre-repair historical renderings
- `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`, `CLAIMS_EVIDENCE.md` — theorem and
  evidence control
- `code/verify.py`, `code/verification_output.txt` — dependency-free exact
  verifier and canonical transcript
- `BUILD.md` — reproduction and QA record
- `OWNER_REPAIR_LOG.md` — exact owner defect, citation closure, mutations, and
  historical-artifact invariants

Run the verifier with `python code/verify.py`.  Run the four-stage build listed
in `BUILD.md`.  The package remains `HOLD_EXTERNAL`; it is not authorized for
public posting, submission, priority, or specialist contact.
