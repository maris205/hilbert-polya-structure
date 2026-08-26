# HCS-C183 — random-transposition full spectrum

This package resolves the lazy random-transposition Markov operator on every symmetric group \(S_n\). Its all-size theorem gives the complete partition-indexed spectrum and multiplicities, finite determinant, trace and exact return formulas, \(L^2\) density distance, spectral gap \(2/n\), bottom eigenvalue \(-1+2/n\), and reversibility.

The owner boundary is exact. On frozen \(S_n\), \(P_n\) is neither a single-valued deterministic map nor a permutation Koopman operator, and \(\det(I-zP_n)\) is not an unweighted Artin--Mazur determinant there. After changing to the weighted directed-edge path space, its reciprocal does have the canonical primitive-cycle product

\[
\det(I-zP_n)^{-1}=\prod_{[\gamma]\ \mathrm{primitive}}
(1-w(\gamma)z^{|\gamma|})^{-1}.
\]

That lift changes the phase space and dynamical object. It does not repair A0, and A1 remains `FAIL` because the frozen source has no primitive orbit carrying an A0 arithmetic payload.

## Run

```bash
python3 code/c183_random_transposition_producer.py
python3 code/c183_random_transposition_checker.py
python3 code/c183_sympy_crosscheck.py
python3 code/c183_replay.py
python3 code/c183_mutation.py
python3 code/c183_release_manifest.py
```

The final paper is `paper/main.pdf`. The strict Route-A tuple is `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`; overall `ROUTE_A_REJECTED`; Route B false. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
