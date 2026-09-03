# HCS-C352: integer-kink Jackiw--Rebbi Dirac spectrum

This package proves one all-parameter theorem for the self-adjoint operators

\[
H_n=\begin{pmatrix}0&A_n^*\\A_n&0\end{pmatrix},\qquad
A_n=\frac d{dx}+n\tanh x,\qquad n\in\mathbb Z_{\ge 1}.
\]

The theorem closes self-adjointness, both supersymmetric scalar channels, the complete discrete Dirac spectrum, the unique chiral zero mode, threshold resonances, absence of threshold eigenvalues, and integer-height reflectionlessness.  The result is source-local: it makes no arithmetic-target or priority claim.

Primary artifacts:

- `paper/main.pdf`: the final manuscript.
- `THEOREM_PACKAGE.md`: theorem and proof dependency map.
- `results/c352_jackiw_rebbi_evidence.json`: exact finite certificate.
- `C352_RELEASE_MANIFEST.json`: 27-payload release ledger.
- `evaluations/route_a/HCS-C352/2026-09-03.yaml`: Route-A evaluation.

Run `python -B code/c352_release_manifest.py` for the complete no-write release audit.
