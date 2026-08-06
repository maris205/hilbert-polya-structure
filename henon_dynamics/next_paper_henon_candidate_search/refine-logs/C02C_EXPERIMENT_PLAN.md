# C02C claim-driven experiment plan

Date: 2026-08-06  
Protocol: `../code/C02C_FINITE_WINDOW_PROTOCOL.md`
Status: **complete; C1--C8 pass; effective specialization retained with
novelty delta unconfirmed**

## Claims and falsifiers

| ID | Claim | Evidence route | Falsifier |
|---|---|---|---|
| C1 | Full frozen endpoint disks define unique holomorphic finite-window solutions. | Analytic contraction plus exhaustive short-window boundary regression. | Any admissible sampled endpoint leaves its disk or fails to converge. |
| C2 | Endpoint derivatives satisfy the frozen one-sided Neumann-path envelopes. | Analytic proof plus implicit derivatives for every center-endpoint word through \(N=8\). | Ratio exceeds one beyond tolerance. |
| C3 | Two-coordinate chronological gluing equals direct union solving. | Frozen nonpalindromic complex-endpoint case. | Direct/glued discrepancy exceeds tolerance. |
| C4 | Continuants recover chronological monodromy and the periodic matching/Hill determinant. | Every admissible cyclic word through \(N=8\), including \(N=1,2\). | Any determinant or entry identity fails. |
| C5 | Complex \(q\) gives the exact separated projective child disks. | Rational inversion formula plus adversarial boundary points. | Pole clearance, containment, tangency, or separation fails. |
| C6 | Ordered projective dynamics loses remote endpoint memory at the proved rate. | Chain-rule derivatives compared with the frozen envelope. | Any derivative exceeds its bound. |
| C7 | Scalar averaging and reversed chronology destroy the frozen test case. | Expected-fail controls. | Either altered object agrees within tolerance. |
| C8 | The checker rejects incomplete or tampered artifacts. | In-memory truncation and mutation controls. | Any tampered artifact validates. |

## Execution order

1. Compile producer and checker.
2. Run producer with the frozen protocol.
3. Run independent checker.
4. Run checker against an explicitly truncated temporary producer run if a
   CLI hook is available; otherwise use the mandated in-memory controls.
5. Inspect all non-finite values and worst-case rows.
6. Update Route-A and paper/infrastructure decision only after checks pass.

## Resource estimate

CPU-only.  Exhaustive sign enumeration ends at length eight and is expected
to finish in well under one minute on a single modern CPU core.  No GPU,
cluster, target data, or network service is required.

## Interpretation rule

Passing C1--C8 certifies implementation consistency with the analytic
derivation.  It does not establish novelty, nuclearity, a Fredholm operator,
or any Hilbert--Pólya statement.
