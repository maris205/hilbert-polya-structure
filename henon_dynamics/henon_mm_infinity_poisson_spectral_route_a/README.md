# HCS-C233 — M/M/∞ Poisson–Charlier semigroup atlas

This paper treats the infinite-server immigration–death chain

\[
 Qf(n)=\lambda[f(n+1)-f(n)]+\mu n[f(n-1)-f(n)],\qquad n\in\mathbb N_0.
\]

For positive rates it closes the exact Poisson invariant law, the
binomial-survivor plus Poisson-immigration transition kernel, the complete
Charlier eigenbasis and sharp gap `mu`.  The positive-time semigroup is
trace-class on `L2(Poisson)` with an explicit source Fredholm product; pure
death, pure birth, zero-rate and long-time faces are kept separate.  The
stochastic semigroup is not relabeled as a primitive-orbit zeta.

Route-A is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall
`ROUTE_A_REJECTED`, with scope `NO_BAD_EULER_OR_ROOT_NUMBER` and Route B false.

Reproduce:

```bash
python -B code/c233_mminf_producer.py
python -B code/c233_mminf_checker.py
python -B code/c233_mminf_sympy_crosscheck.py
python -B code/c233_mminf_replay.py
python -B code/c233_mminf_mutation.py
python -B code/c233_release_manifest.py
```

The paper is [paper/main.pdf](paper/main.pdf); evidence is
`results/c233_mminf_evidence.json` and the release ledger is
`C233_RELEASE_MANIFEST.json`.
