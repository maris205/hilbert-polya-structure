# Experiment plan

## Claim-driven checks

1. Reconstruct \(\beta_n\) exactly from reciprocal cyclotomic polynomials for
   \(3\le n\le72\).
2. Check the identity
   \(\log\beta_n=\varphi(n)\log L/2+\varepsilon_n\) to 70 decimal digits.
3. Bound \(C_L\) using 32 explicit terms and a rigorous geometric tail.
4. Evaluate \(\tau^2Z(\tau)\) at
   \(\tau=0.2,0.1,0.05,0.025,0.0125\).
5. Evaluate normalized Laplace transforms at \(s=1/2,1,2\).
6. Measure the mass retained by the fixed prefix \(3\le n\le20\).

## Adversarial controls

- omit the factor \(1/2\) in the packet main term;
- normalize by \(\tau\) instead of \(\tau^2\);
- replace Gamma\((2,1)\) by an exponential law;
- promote scalar mass convergence to tagged-vector convergence;
- promote a one-orbit result to an all-orbit result;
- mutate dependency hashes or the theorem ledger.

## Acceptance

- Producer and independent checker agree.
- All dependency locks match.
- Exact packet formula error is below \(10^{-70}\).
- All tests pass with Python bytecode disabled.
- Numerical rows are labelled as finite certificates, not proofs of the
  asymptotic statements.
