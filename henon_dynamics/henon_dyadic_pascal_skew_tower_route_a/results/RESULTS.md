# C166 results

- All-parameter theorem: `Fix(T^n)` is the whole `q^d`-state space exactly
  when `2^(r+floor(log_2 d))` divides `n`, and is empty otherwise.
- Every state has that exact least period; primitive cycles number `q^d/M`.
- `zeta_T(z)=(1-z^M)^(-q^d/M)` and the finite Koopman determinant is its
  reciprocal.
- Substitution `t -> -t/(1+t)` is an involutive source reversor.
- Canonical evidence SHA-256:
  `3272e01ce32f4d58f609ebfc76dba60584636bc8225970c01e6659af2ae4aaca`.
- Regression ledger: 90 parameter rows, 25,200 coefficient-clock cases,
  27,788 direct state-period cases, and 90 reversor matrix rows.

These exact finite rows validate implementations; the theorem proof is
independent of their cutoffs.
