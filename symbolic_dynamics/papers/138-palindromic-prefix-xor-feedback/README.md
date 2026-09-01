# P138 — palindromic-prefix XOR feedback

Anonymous Stage-2 Round-0 package for the finite map

```text
P_n(x)_i = x_i xor 1{x_1...x_i is a palindrome}.
```

The manuscript proves complement equivariance, the unique recurrent two-cycle,
the sharp maximum transient `0,1,n-2`, and a complete target-by-target fibre
decoder.  Static palindrome algorithms and word combinatorics are explicitly
zero-credit background.

## Files

- `main.tex`, `references.bib` — anonymous manuscript and verified references
- `main.pdf`, `main_round0_original.pdf` — current and immutable Round-0 PDF
- `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`, `CLAIMS_EVIDENCE.md` — theorem and
  evidence control
- `code/verify.py`, `code/verification_output.txt` — dependency-free exact
  verifier and canonical transcript
- `BUILD.md` — reproduction and QA record

Run the verifier with `python code/verify.py`.  Run the four-stage build listed
in `BUILD.md`.  The package is `HOLD_EXTERNAL`; it is not authorized for public
posting or submission.
