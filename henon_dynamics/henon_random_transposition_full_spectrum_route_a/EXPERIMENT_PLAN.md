# C183 exact validation plan

## Claims under test

1. Central convolution diagonalizes on every irreducible \(S_n\)-sector indexed by \(\lambda\vdash n\).
2. The eigenvalue is
   \[
   \beta_\lambda=\frac1n+\frac1{n^2}\sum_i\bigl(\lambda_i^2-(2i-1)\lambda_i\bigr)
   \]
   with regular multiplicity \(d_\lambda^2\).
3. Hook dimensions close the regular representation: \(\sum_{\lambda\vdash n}d_\lambda^2=n!\).
4. The determinant, trace, identity-return probability, exact \(L^2\) density distance, bottom eigenvalue, and spectral gap follow from the same spectral ledger.
5. On frozen \(S_n\), \(P_n\) is not a deterministic map or permutation Koopman operator, and the determinant is not an unweighted Artin--Mazur determinant.
6. The changed weighted path space has a canonical primitive-cycle product for \(\det(I-zP_n)^{-1}\), but that different owner does not repair A0 or A1.

## Independent paths

- The producer builds partitions, hook dimensions, characters, eigenvalues, collected factors, moments, and exact return counts for \(2\le n\le11\), \(0\le k\le8\).
- The checker reimplements every combinatorial formula, verifies every factor string and metadata cutoff, and directly enumerates ordered-pair transition words for \(2\le n\le7\), \(0\le k\le6\).
- The checker also enumerates the primitive binary path cycles through length eight for \(P_2\) and recovers the first nine coefficients of \(\det(I-zP_2)^{-1}=1/(1-z)\).
- SymPy reconstructs rational sector formulas, determinant degrees, and trace/return identities without importing producer code.
- Replay regenerates the evidence byte for byte.
- Fifty-seven repaired-hash mutations and one stale-hash mutation attack source locks, source year and registry, cutoffs, partitions, characters, traces, every determinant-factor string contract, owner boundaries, Route-A qualifications, scope, and citation metadata.

Finite rows are regression sentinels. The all-\(n\) conclusions rest on the proof in `THEOREM_PACKAGE.md` and the manuscript.
