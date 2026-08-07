# Exact-​$U_c$ polar boundary trace

Stage ID: `P4-LOGISTIC-UC-POLAR-BOUNDARY-TRACE`

This stage closes the local trace obligation left by the half-open partition
audit. For the unique boundary periodic point

\[
P=-\pi/2,
\qquad
\alpha_0=U_c^2/4,
\]

the exact left weighted-composition traces are

\[
\operatorname{Tr}T_{s,L}
=\frac{\alpha_0^s}{1-\alpha_0},
\qquad
\operatorname{Tr}_P T_{s,L}^n
=\frac{\alpha_0^{ns}}{1-\alpha_0^n}.
\]

There is no half-weight or doubled/matching factor. Although `P` is a real
endpoint, it lies inside the frozen complex stadium and belongs only to the
left component.

The certificate verifies exact endpoint identities and 100-digit Taylor tails
for powers 1--4, `s=0,1/2,1,2+i`, and cutoffs 4--64. No prime or zero data is
used.

## Reproduction

```bash
python3 src/boundary_trace_audit.py --quiet \
  --output results/boundary_trace_certificate.json
python3 -m unittest -v tests/test_boundary_trace.py
```

## Claim boundary

This is a theorem-level local result, but not a Route-A determinant pass.
Nuclearity of the full two-component matching-space family, a complete trace
formula, Fredholm determinant, target divisor, Route B, Hilbert--Pólya, and RH
remain open.

The next smallest task is full matching-space nuclearity, before any Fredholm
zero calculation.
