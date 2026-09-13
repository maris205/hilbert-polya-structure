# Proof-Validation Tracker

## Tracker scope

This tracker records source-design obligations actually discharged in the
ten-file proof package. It records no computational run, empirical result,
CAS output, parameter scan, manuscript action, or downstream authorization.
The current lifecycle state is **AUTHOR PACKAGE PREPARED; INDEPENDENT
SOURCE-DESIGN REVIEW NOT YET AUTHORIZED BY THIS FILE**.

## Design obligations

| ID | Obligation | Design status | Evidence location |
|---|---|---|---|
| D-01 | Exact support-row Sylvester factorization | DISCHARGED IN DESIGN | PROOF_PACKAGE, Proof Step 1 |
| D-02 | Lower-bound-only unit multiplicity wording | DISCHARGED IN DESIGN | PROOF_PACKAGE, Step 1; CLAIMS_EVIDENCE_MATRIX C-01 |
| D-03 | Every-$d$ parameter existence in noncircular order | DISCHARGED IN DESIGN | PROOF_PACKAGE, Step 2 |
| D-04 | Symplecticity and literal gradient rows | DISCHARGED IN DESIGN | PROOF_PACKAGE, Step 3 |
| D-05 | Broad ratio-cone selector and strict invariance | DISCHARGED IN DESIGN | PROOF_PACKAGE, Steps 4--5 |
| D-06 | Fine visibility chamber and seed entry | DISCHARGED IN DESIGN | PROOF_PACKAGE, Step 6 |
| D-07 | Both temporal carries and cross-phase domination | DISCHARGED IN DESIGN | PROOF_PACKAGE, Step 7 |
| D-08 | Positive-semiring top-form survival | DISCHARGED IN DESIGN | PROOF_PACKAGE, Step 7 |
| D-09 | Exact $q_1$-visible ordinary-degree identity | DISCHARGED IN DESIGN | PROOF_PACKAGE, Steps 6--7 |
| D-10 | Characteristic-polynomial formula | DISCHARGED IN DESIGN | PROOF_PACKAGE, Step 8 |
| D-11 | Modulo-$p$ reduction and full binomial criterion | DISCHARGED IN DESIGN | PROOF_PACKAGE, Step 9 |
| D-12 | Explicit $d=2$ and $4\mid d$ boundary audit | DISCHARGED IN DESIGN | PROOF_PACKAGE, Step 9 and Boundary Cases |
| D-13 | Exact Perron algebraic degree and dynamical-degree limit | DISCHARGED IN DESIGN | PROOF_PACKAGE, Step 10 |
| D-14 | Reachability, observability, Hankel rank, and minimal scalar order | DISCHARGED IN DESIGN | PROOF_PACKAGE, Step 11 |
| D-15 | Sharpness for each constructed rank $r=d\ge2$ | DISCHARGED IN DESIGN | PROOF_PACKAGE, Step 12 |
| D-16 | Local Papers 22--24 subtraction | DISCHARGED IN DESIGN | NOVELTY_ASSESSMENT; REVIEW_SUMMARY |
| D-17 | Bounded primary-source claim boundaries | DISCHARGED IN DESIGN | CITATION_VERIFICATION; NOVELTY_ASSESSMENT |
| D-18 | Mandatory anti-claims propagated across design | DISCHARGED IN DESIGN | all proposal and evidence files |
| D-19 | 22--30-page article and lemma budget | DISCHARGED IN DESIGN | FINAL_PROPOSAL |
| D-20 | Claim-specific falsifiers and dependency order | DISCHARGED IN DESIGN | EXPERIMENT_PLAN; CLAIMS_EVIDENCE_MATRIX |

“Discharged in design” means that the author supplied a complete symbolic
derivation or scope statement. It is not an independent PASS and is not a
publication claim.

## Boundary checks recorded

- $d=1$ is excluded by the theorem.
- At $d=2$, the selected prime is odd and a generator is a nonsquare.
- If $4\mid d$, then $p\equiv1\pmod4$ follows from
  $p\equiv1\pmod d$.
- The seed lies on permitted equal-coordinate walls of the fine chamber but
  satisfies its strict upper-ratio and weighted inequalities.
- Visibility is unique only after a positive complete iterate.
- The support-rank factor may contain additional unit roots in general.
- The sharp family covers nontrivial ranks $r=d\ge2$ and makes no rank-zero
  or rank-one sharpness claim.
- Characteristic zero is used for nonvanishing positive integer
  coefficients.

## Objects deliberately not created or executed

| Object or action | State | Reason |
|---|---|---|
| Code or script | NOT CREATED | No computation is evidence for this theorem. |
| Numerical or CAS certificate | NOT RUN | Explicitly outside authorization and unnecessary. |
| Dataset or result table | NOT CREATED | No empirical question exists. |
| Manuscript, TeX, or BibTeX | NOT CREATED | Source-design gate only. |
| Figure | NOT CREATED | Source-design gate only. |
| Independent source-design review | NOT CREATED BY AUTHOR | Must be separately authorized and independent. |
| Source/publication lock | NOT CREATED | Depends on later gates. |
| Build or PDF | NOT RUN / NOT CREATED | Depends on later gates. |
| README or registry mutation | NOT PERFORMED | Outside this gate. |
| Release or external effect | NOT PERFORMED | Outside this gate. |

## STOP conditions

The next actor must stop with no source or build mutation if rederivation
finds any of the following:

1. the broad and fine cones cannot both be justified as stated;
2. a carry comparison omits an old coordinate;
3. positivity is insufficient to prevent a selected top-form loss;
4. the modular binomial fails at $d=2$ or when $4\mid d$;
5. the Hankel matrix is not forced to have rank $d$;
6. sharpness requires an exact unit-multiplicity claim;
7. a citation is asked to support a stronger proposition than its frozen
   verification boundary;
8. any first, only, unprecedented, or priority claim is introduced;
9. verification would require computation, network access, or an object not
   explicitly authorized by the next gate.

## Handoff

The author stops after inventory verification. A distinct reviewer may
accept or block this package only under separate governance authorization.
This tracker itself grants no permission to edit these files, add a review,
open a manuscript, or perform any external action.
