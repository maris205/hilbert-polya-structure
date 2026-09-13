# Paper 23 — Analytic Verification Tracker

## Current state

- Lifecycle: source-design author package only.
- Scientific experiments run: **zero**.
- Code, data, plots, numerical spectra, CAS certificates, and parameter
  sweeps: **absent**.
- Frozen signs: both shears use addition.
- Frozen phase order: $F_g=T_g^+\circ S_g^+$.
- Frozen field/range: characteristic zero and integer $g\ge10$.
- Proof cone used in this package: the explicit sufficient ratio cone in
  `notes/PROOF_PACKAGE.md`.
- Source lock, paper plan, manuscript, build, PDF, or release authority:
  **not granted**.

## Verification ledger

`AUTHOR-CLOSED` means that the source-design author supplied a symbolic
derivation.  It is not an independent-review verdict.

| ID | Status | Evidence location | Residual reviewer attack |
|---|---|---|---|
| P01 gradients/supports | AUTHOR-CLOSED | Proof Steps 1--2 | differentiate every row independently |
| P02 symplecticity/inverses | AUTHOR-CLOSED | Proof Step 1 | verify block signs and Hessian symmetry |
| P03 phase matrices/order | AUTHOR-CLOSED | Proof Step 2 | recompute $B_gA_g$, not $A_gB_g$ |
| P04 four selectors | AUTHOR-CLOSED | Proof Step 3 | recompute both $T$ gaps at $A_gu$ |
| P05 seed/$g=9$ boundary | AUTHOR-CLOSED | Proof Steps 3 and 10 | verify margins $(1,0,-2,5)$ at $g=9$ |
| P06 all cone faces | AUTHOR-CLOSED | Proof Step 4 | attack every numerator and strictness sign |
| P07 two carries | AUTHOR-CLOSED | Proof Step 5 | preserve phase indices in the induction |
| P08 no cancellation | AUTHOR-CLOSED | Proof Step 5 | check positive-semiring and characteristic-zero use |
| P09 $q_4$ visibility | AUTHOR-CLOSED | Proof Step 6 | compare against all seven other coordinates |
| P10 characteristic polynomial | AUTHOR-CLOSED | Proof Step 7 | sum the written principal-minor ledger |
| P11 mod-five irreducibility | AUTHOR-CLOSED | Proof Step 8 | repeat root and quadratic-factor exclusions |
| P12 support-profile scope | AUTHOR-CLOSED | Proof Step 9 | reject novelty/classification inflation |

## Exact non-running record

No command, job, script, notebook, random seed, dataset, accelerator, timing,
or result file exists for Paper 23.  The word “experiment” in these two
filenames is a repository convention and does not describe the evidence used
for the theorem.

## Failure actions

- Selector or cone failure: block exact recurrence and quartic headline.
- Carry or cancellation failure: block the conversion from weighted support
  to actual degrees.
- Visibility failure: remove the scalar recurrence and dynamical-degree
  conclusion until a fixed visible functional is proved.
- Characteristic-polynomial or modular failure: remove the quartic Perron
  subfamily.
- Citation collision: narrow positioning; do not assert priority.
- Any request for code or computation: defer until separately authorized;
  computation cannot replace a theorem-critical hand proof.
