# R105 — Gauge, Residual, and Reproducibility Audit

## Design

Recompute the \(a=1.02,n=1\), \(h=0.03\), 180-level spectra for

- \(B=0\), symmetric gauge;
- \(B=1\), symmetric gauge;
- \(B=1\), Landau gauge;
- \(B=-1\), symmetric gauge.

Use a deterministic Lanczos initial vector and retain maximum relative
eigen-residual and orthogonality defect before discarding eigenvectors.

## Gates

- maximum relative residual below \(10^{-8}\);
- maximum eigenvector orthogonality defect below \(10^{-8}\);
- \(B=1\) symmetric/Landau spectra agree to relative \(10^{-10}\);
- \(B=1\) and \(B=-1\) spectra agree to relative \(10^{-10}\);
- rerun spectra agree with the archived R100 arrays to relative \(10^{-10}\).

The source hashes and deterministic-initial-vector flag are saved.
