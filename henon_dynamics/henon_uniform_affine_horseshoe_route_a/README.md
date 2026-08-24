# C127 — Uniform affine Hénon horseshoe over a parameter rectangle

This package proves a parameter-uniform theorem for a two-strip affine
horseshoe rather than checking a few nearby parameter values.  For

\[
(\lambda,\mu)\in[3,4]\times[1/5,1/3],
\]

the model has uniform strip separation, exact full two-shift coding, one
periodic point for every based binary word, and an exact trace-class
stability-mode operator whose traces equal the all-period fixed-point sums.

## Explicit progress over the prior gate

Earlier Hénon-track packages supplied individual parameter witnesses or
finite word prefixes.  C127 closes the stronger **uniform-parameter gate**:
all geometric, coding, trace-class, determinant, zero-free-domain, and
Lipschitz estimates hold on one explicit two-dimensional parameter rectangle.

## Reproduce

```bash
python3 code/c127_uniform_horseshoe_producer.py
python3 code/c127_uniform_horseshoe_checker.py
python3 code/c127_sympy_crosscheck.py
python3 code/c127_replay.py
python3 code/c127_mutation.py
```

The final paper is `paper/main.pdf`.  The package remains behind the
`NO_BAD_EULER_OR_ROOT_NUMBER` firewall: it contains no target spectral table,
Euler-factor claim, root number, automorphy claim, or Hilbert--Pólya claim.

Strict Route-A tuple:
`(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`; Route B is not authorized.
