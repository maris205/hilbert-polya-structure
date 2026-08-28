# P86 — Finite-Field Adjacent-Product Processes

Status: internal freeze after hostile audit; external release **HOLD**.

Let `(U_i)` be iid uniform on the finite field `F_q`, and set
`Y_i = U_i U_{i+1}`.  This short paper gives an exact theorem package for
the resulting stationary symbolic process.

The main results are:

- the support is exactly the mixing two-step SFT forbidding `a 0 b` with
  `a,b != 0`;
- its word complexity satisfies a cubic recurrence and its topological
  entropy is the logarithm of an explicit Perron root;
- two `2 x 2` matrices count every cylinder fiber;
- the process is reversible, one-dependent, and strongly mixing, yet is not
  Markov of any finite order;
- generalized-Fibonacci ratios give the exact next-symbol law after every
  zero-run context;
- an explicit exponentially convergent series gives the measure entropy,
  which is strictly below the support entropy.

All theorems hold for every prime power `q >= 2`.  The control script checks
prime fields `F_2`, `F_3`, `F_5` and the nonprime field `F_4`.

## Build

From this directory, run the reproducible four-stage build:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

The expected artifact is `main.pdf`.

## Exact controls

Run:

    python3 code/verify_adjacent_product.py

The program uses only the Python standard library and exits nonzero on any
failed identity.

## Ownership scope

The paper positively cites Aaronson--Gilat--Keane--de Valk for the general
one-dependent/block-factor landscape, Blackwell for entropy of functions of
finite-state Markov chains, Rissanen and Buhlmann--Wyner for variable-memory
contexts, and Parry for the intrinsic Markov measure.  Its residual contribution is the
finite-field adjacent-product calculation.  A bounded search found no direct
primary owner for the combined formula package; the draft makes no absolute
novelty or priority claim.

## Files

- `main.tex` — complete amsart manuscript and proofs
- `references.bib` — cited, source-verified bibliography
- `code/verify_adjacent_product.py` — deterministic exact controls
- `CLAIMS_EVIDENCE.md` — theorem-to-proof/control map
- `CONTROL_RESULTS.md` — recorded control output
- `BUILD.md` — build instructions and artifact metadata
- `FINAL_QA.md` — release checklist
- `HOSTILE_REVIEW.md` — independent adversarial proof and ownership audit
- `main.pdf` — compiled manuscript
