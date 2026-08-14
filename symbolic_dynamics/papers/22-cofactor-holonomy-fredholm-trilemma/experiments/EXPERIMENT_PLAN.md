# SD-C24 exact experiment plan

Candidate: `SD-C24`  
Primary family: Symbolic Dynamics  
Status: frozen theorem-audit protocol

## Objective

Audit the cofactor-holonomy construction on the frozen successor-divisor
shift. The experiment tests exact algebraic identities, sharp analytic
classifications, and matched obstruction controls. It does not fit parameters,
score Riemann zeros, or use atom data to build the graph.

## Frozen source

- Vertices: integers `n >= 2`.
- Edge: `n -> d` exactly when `d >= 2` divides `n+1`.
- Cofactor: `q(n,d)=(n+1)/d`.
- Operator: column-source `L_(s,u)` with weight `(nd)^(-s) q^(-u)`.
- Primitive equivalence: directed rotation only; no reflection quotient.
- Post-freeze atom fixtures: `2,3,5,7`, used only in evaluation.

## Exact audits

1. Inspect all source edges through `n=4096` and certify the quotient identity.
2. Enumerate simple cycles by sparse DFS at `N=12,20,30`; verify telescoping,
   `Q>=2`, `Q=2 iff C_k`, and the atomic `C_(k,p)` classifications.
3. Enumerate rooted closed words through `r=8` at the certified cutoff `2r-1`;
   record every rotation, primitive temporal root, and repetition.
4. Compute group-algebra traces by sparse dynamic programming through `r=10`
   at exact integer `s=1,2`; verify neutral coefficient zero and atomic formulas.
5. Recover finite group coefficients by alias-free discrete Fourier inversion.
6. Verify the integer gauge identity exactly and unitary gauge similarity
   numerically on finite prefixes.
7. Diagnose the two boundaries of the sharp trace-class region on eight
   parameter points and seven cutoffs. Finite prefixes are illustrations only.
8. Cross-check four finite determinants against Newton trace coefficients.
9. Audit pure-cofactor nondecay, endpoint factorial damping, scalar phase
   blindness, and the neutral group-trace determinant one.
10. Run six arbitrary positive inventories and one transported-presentation
    control; require unchanged `Q=2` support and zero selection margin.

## Evidence policy

Integers and rational weights are exact. Floating calculations are limited to
unitary phases, Fourier inversion, and diagnostic prefixes with explicit error
thresholds. Infinite-dimensional assertions come from proofs in the frozen
derivation package, never from cutoff trends. Target-zero metrics are marked
`not applicable; no_target_zero_evaluation`.

## Acceptance gates

- all 26 tests pass;
- every exact mismatch count is zero;
- the Route-A tuple is
  `(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_WEAK,
  A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)`;
- Route B stays locked;
- the integrity audit passes with pending two-stage provenance;
- two full clean runs have identical SHA-256 ledger hashes;
- no cache directory remains in the project artifact tree.

Run from the paper directory:

```bash
python experiments/run_sdc24_exact_suite.py --verify-byte-determinism
```
