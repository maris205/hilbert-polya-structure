# P139 owner-repair log — Round 3

**Date:** 2026-09-01 UTC  
**Trigger:** `docs/papers137_141_sequence/phase1/FINAL_OWNER_AUDIT.md`  
**External status:** `HOLD_EXTERNAL`

## Defect closed

The pre-repair manuscript foregrounded the equivalence

```text
Lyndon-factor starts = left-to-right strict new minima among suffixes
```

as if it helped thicken the residual theorem package.  That static statement
is pre-owned.  Its inverse-suffix-array formulation is Theorem 2.2 of Mantaci,
Restivo, Rosone, and Sciortino.  The ordered-tail comparison used in the local
proof is classical CFL machinery and is likewise unavailable as residual
credit.

## Exact controlling citation

Sabrina Mantaci, Antonio Restivo, Giovanna Rosone, and Marinella Sciortino,
“Suffix Array and Lyndon Factorization of a Text,” *Journal of Discrete
Algorithms* **28** (2014), 2--8, DOI
`10.1016/j.jda.2014.06.001`.

Verification closure:

1. The official Elsevier/ScienceDirect record at
   `https://www.sciencedirect.com/science/article/pii/S157086671400032X`
   confirms the complete metadata and DOI.
2. The accepted manuscript in the University of Pisa institutional repository
   at
   `https://arpi.unipi.it/retrieve/handle/11568/728487/440835/MRRS_JDA_2014_postPrint.pdf`
   gives Theorem 2.2: the left-to-right minima of the suffix permutation are
   the starting positions of the Lyndon factors.
3. The formal STACS 2021 proceedings paper “Finding an Optimal Alphabet
   Ordering for Lyndon Factorization Is Hard” explicitly restates the result
   as its Lemma 8 and attributes it to Mantaci et al., Theorem 2.2.

## Textual repair

- `references.bib`: added the exact four-author journal entry and DOI.
- `main.tex` abstract: removed the suffix-record theorem from the advertised
  result list and declared static suffix-array characterizations zero credit.
- `main.tex` introduction: cited Mantaci et al. Theorem 2.2 at the owner gate
  and enumerated only the surviving residual.
- `main.tex` Section 2: renamed as an owned static interface; labelled the
  proposition “owned input” and the retained proof “Reproduced background
  proof”; labelled ordered-tail comparison static zero-credit machinery.
- `main.tex` limitations: interpreted the independent mask equality only as an
  integration check and repeated the narrowed residual boundary.
- `README.md`, `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`, and
  `CLAIMS_EVIDENCE.md`: removed the static theorem from residual claims and
  synchronized the exact owner citation and zero-credit treatment.
- `BUILD.md`: replaced the Round-0-only record with the Round-3 citation,
  preservation, replay, reproducibility, and QA record.

No batch document, hostile-review file, verifier file, or historical PDF was
edited.  No Git operation was performed.

## Surviving residual contract

Only the following remain in the paper's residual package:

1. the iterated Lyndon-factor-start mask dynamics and its unique recurrent
   state `1^n`;
2. the sharp depth `n` theorem with the unique alternating deepest state;
3. the target-wise ordered-Lyndon fibre atlas, including its matrix form and
   special target cells after subtracting the classical Lyndon census and
   generic matrix multiplication.

The static suffix-record theorem, its ordered-tail proof machinery, CFL
factorization, Duval algorithms, Lyndon-array/tree infrastructure, binary
Lyndon census, Möbius inversion, and matrix multiplication receive zero
contribution credit.

## Frozen invariants and repaired artifact

```text
code/verify.py
01d10e3ffde5cfe675665e0cdfb1d2fc5e411c864ef83a82e93ca3d7d23e6b75

code/verification_output.txt
801b82a729adff63f35dc92306ad1044444d2cd0fc89b603306064fd7f6ec0fe

main_round0_original.pdf
main_round1.pdf
main_round2.pdf
3d41d36820b33b2b4f9215dd55d8b9d620d7c39ae0f65c5512426c8d7b79acf0

main.pdf
main_round3.pdf
3c4b474a05290223a1ea70a050cab1b7b46043b0ca3c67f88327d9f71ceb76e3
```

The verifier replay remains byte-identical, the isolated repaired build is
byte-identical to `main.pdf`, and `main_round3.pdf` is frozen read-only at mode
`0444`.  This repair is an internal ownership correction only; it grants no
novelty, priority, posting, submission, or release clearance.
