# HCS-C168: rank-three phase law for a four-symbol open Walsh map

This package proves an all-register-length theorem for the natural gate

```text
A=F4^* diag(1,0,1,1),       C_k=B_k^k=A^(tensor k).
```

The one-site characteristic polynomial factors exactly as
`x(x-1)(x^2+i x/2-1/2)`.  Consequently the nonzero secular degree is `3^k`,
the zero generalized eigenspace has dimension `4^k-3^k`, and the surviving
phases form a three-step multiplicative walk.  Its fixed nonzero Fourier
modes contract strictly, yielding weak Haar convergence.  Centered log
modulus and phase converge jointly to a Gaussian--Haar product law.

The same-clock hole-zero control has phases `{1,-1,-i}` and converges in
total variation to the uniform law on `<i>`, with bound
`(3/2)3^(-k)`.  A hole-reflection/antiunitary identity is retained only as a
finite-dimensional control; no self-adjoint limit is claimed.

## Reproduce

```bash
python code/c168_rank_three_producer.py
python code/c168_rank_three_checker.py
python code/c168_sympy_crosscheck.py
python code/c168_replay.py
python code/c168_mutation.py
```

The finite ledgers are sentinels, not proofs.  The written all-`k` arguments
are in `THEOREM_PACKAGE.md` and `paper/main.pdf`.  The literal scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is not authorized.
