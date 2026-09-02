# P163 — Complemented-Shadow Dynamics

Anonymous internal theorem draft for the set-family map

```text
S_n(F) = { complement(A without {a}) : A in F, a in A }.
```

**Gate:** `GREEN_REENTRY_AFTER_CONTRACT_STRENGTHENING`  
**Lifecycle:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`

## Artifact map

- `main.tex` and `references.bib` — manuscript source and verified owner
  references.
- `main.pdf` — settled anonymous Round-2 PDF.
- `main_round0_original.pdf`, `main_round1.pdf`, `main_round2.pdf` —
  byte-identical lifecycle freezes.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md` — process-separated hostile
  reviews, each returning `0 Critical / 0 Major / 0 minor`.
- `PAPER_PLAN.md` — theorem, proof, boundary, and build architecture.
- `CLAIMS_EVIDENCE.md` — claim-to-proof and claim-to-control ledger.
- `NARRATIVE_REPORT.md` — mathematical progression and owner ceiling.
- `code/verify.py` — independent standard-library exact verifier.
- `code/CANONICAL.txt` — frozen deterministic transcript.
- `BUILD.md` — replay, cold-build, PDF, font, log, and anonymity record.
- `FINAL_QA.md` — final verifier, review, build, PDF, and lifecycle closure.

## Exact control

```bash
python3 code/verify.py
cmp code/CANONICAL.txt <(python3 code/verify.py)
```

The verifier does not import the scout or re-entry-gate code.  Its finite
checks are counterexample pressure rather than a proof or an ownership test.

## Paper build

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Both hostile reviews independently rederived and falsified the complete
contract.  Review B added 1,041,401 independent assertions, a fresh owner
and internal-collision audit, and two source-only cold builds.  Since neither
review requested a repair, all three lifecycle PDFs are byte-identical.

The internally accepted artifact is not cleared for posting, submission,
circulation, or author contact.
