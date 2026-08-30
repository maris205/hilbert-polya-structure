# Improvement log — P124

Status: **ROUND2 GO_INTERNAL / EXTERNAL HOLD**.

## Review A to round 1

Review A returned `GO_INTERNAL` with zero critical, zero major, and two minor
support-package findings.

1. Corrected the sharp-depth proof anchor from the nonexistent Theorem 3.3
   to Theorem 3.2, and the layer/terminal-ballot anchor from the nonexistent
   Corollary 5.2 to Theorem 5.1.
2. Added the explicit P107/P104 internal collision firewall.  P107 is an
   annihilator-power map in CRT valuation coordinates; P104 is a random
   contraction cocycle.  Neither supplies the crossed-colon, sourced-diagonal,
   first-trace basin, or contact-transfer mechanism of P124.  Generic ideal,
   monomial, toggle, cycle, and depth language receives zero credit.

No theorem, proof, verifier, bibliography, or `main.tex` line changed.
`main_round0_original.pdf`, `main_round1.pdf`, and current `main.pdf` were
therefore intentionally byte-identical for Review B.

## Review B to round 2

Independent nonauthor Review B returned `GO_INTERNAL` with
`0 CRITICAL / 0 MAJOR / 0 MINOR`.  It confirmed:

1. both Review-A repairs at their corrected theorem anchors;
2. the explicit P107/P104 internal collision firewall and zero-credit owner
   subtraction;
3. every theorem, proof equation, and boundary case;
4. fresh byte-identical canonical outputs from the independent verifier lanes,
   totaling `1,735,656` assertions;
5. a fresh isolated four-stage build reproducing the five-page PDF exactly;
6. clean visual pages, embedded/subsetted/Unicode fonts, resolved references,
   and anonymous metadata.

Round 2 performs mechanical support closure only.  It adds the consolidated
`HOSTILE_REVIEW.md`, `FINAL_QA.md`, `main_round2.pdf`, and `SHA256SUMS` and
updates support statuses to `ROUND2 GO_INTERNAL / EXTERNAL HOLD`.  It does not
change `main.tex`, `references.bib`, either verifier, either canonical
transcript, or the contents of any pre-existing PDF.  Round 0, round 1,
current, and round 2 are byte-identical at 293,617 bytes with SHA-256
`3dd3316a0abbc504a65c6214bc52d4a439a4e16f8290ca655b7fcece2b501f81`.
