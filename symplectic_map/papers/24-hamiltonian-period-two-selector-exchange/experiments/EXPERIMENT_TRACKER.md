# Paper 24 — Analytic Verification Tracker

## Current state

- Lifecycle: source-design author package only.
- Scientific experiments run: **zero**.
- Code, data, plots, numerical spectra, CAS certificates, and parameter
  sweeps: **absent**.
- Frozen family: $V_m=Aq_1^m q_2^2+Bq_1q_2^{2m}$ and
  $W_{m,s}=Cp_1^{s(2m+1)+1}+Dp_2^{sm+1}$.
- Frozen phase order: $F_{m,s}=T\circ S$.
- Frozen field/range: characteristic zero, integers $m\ge2$, $s\ge1$, and
  arbitrary nonzero $A,B,C,D$.
- Source lock, paper plan, manuscript, build, PDF, or release authority:
  **not granted**.

## Verification ledger

`AUTHOR-CLOSED` means that the source-design author supplied a symbolic
derivation. It is not an independent-review verdict.

| ID | Status | Evidence location | Residual reviewer attack |
|---|---|---|---|
| P01 gradients/supports | AUTHOR-CLOSED | Proof Steps 1--2 | differentiate every coordinate independently |
| P02 symplecticity/inverses | AUTHOR-CLOSED | Proof Step 1 | check block signs and subtraction inverses |
| P03 selector wall/matrices | AUTHOR-CLOSED | Proof Step 2 | recompute both row comparisons and the wall $r=2$ |
| P04 branch algebra | AUTHOR-CLOSED | Proof Step 3 | recompute $\ell_m(r)-1$ and $2-\ell_m(r)$ with corrected factors |
| P05 strict exchange | AUTHOR-CLOSED | Proof Step 3 | verify neither branch admits the wall as a theorem point |
| P06 base carry | AUTHOR-CLOSED | Proof Step 4 | separate base carry from selector choice |
| P07 later $S$ carry | AUTHOR-CLOSED | Proof Step 4 | preserve the phase indices and chamber split |
| P08 later $T$ carry | AUTHOR-CLOSED | Proof Step 4 | reject any hidden large-$s$ argument |
| P09 arbitrary nonzero coefficients | AUTHOR-CLOSED | Proof Step 5 | attack the top-homogeneous-part argument in a domain |
| P10 $q_1$ visibility | AUTHOR-CLOSED | Proof Step 6 | compare against all four final coordinates |
| P11 monodromy product | AUTHOR-CLOSED | Proof Step 7 | recompute $(B_mA_+)(B_mA_-)$ entry by entry |
| P12 spectrum/recurrence | AUTHOR-CLOSED | Proof Steps 7--8 | rederive trace, determinant, and initial values |
| P13 wall gaps | AUTHOR-CLOSED | Proof Step 8 | check the left-eigenvector identities and parity signs |
| P14 parity closed forms | AUTHOR-CLOSED | Proof Step 9 | verify the coefficients and integrality explanation |
| P15 structural lemma scope | AUTHOR-CLOSED | Proof Step 10 | reject any claim beyond the crossed-binomial / two-pure-power ansatz |
| P16 conditional period-$k$ scope | AUTHOR-CLOSED | Proof Step 11 | reject novelty inflation or missing hypotheses |

## Exact non-running record

No command, job, script, notebook, random seed, dataset, accelerator, timing,
or result file exists for Paper 24. The word “experiment” in these two
filenames is a repository convention and does not describe the evidence used
for the theorem.

## Failure actions

- Selector or branch failure: block the period-two exchange headline.
- Carry or no-cancellation failure: block the conversion from weighted support
  to actual polynomial degrees.
- Visibility failure: remove the scalar degree law until a visible functional
  is proved.
- Monodromy or spectral failure: remove the recurrence and exact
  $\lambda_1=sm(2m+1)$ conclusion.
- Structural-lemma overreach: narrow the paper back to the explicit family.
- Any request for code or computation: defer until separately authorized;
  computation cannot replace a theorem-critical hand proof.
