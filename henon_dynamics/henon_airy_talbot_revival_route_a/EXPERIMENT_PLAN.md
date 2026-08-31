# Experiment and proof plan

## Analytic contract

1. Diagonalize the periodic Airy generator in the Fourier basis and prove the
   strongly continuous unitary group.
2. Use the mode `n=1` to prove that `2*pi` is the least full-space period.
3. At `t=2*pi*p/q`, prove cubic phase periodicity modulo `q` and invert its
   finite Fourier transform into `q` spatial translations.
4. Prove Parseval, exact strobe order, the prime-valuation fixed-mode stride,
   and the finite-support gcd period law.
5. Separate rational from irrational fixed subspaces and prove the
   noncompact/non-trace-class boundary.

## Executable contract

- Enumerate every reduced `(p,q)` with `q<=96` and hash the exact cubic phase
  vector independently.
- Reconstruct all cubic DFT coefficients for `q<=18` at 90 decimal digits and
  check inverse DFT and Parseval.
- Verify `q|n^3` against the valuation stride in a symmetric 1,025-mode
  window and on independent out-of-window sentinels.
- Prove polynomial and prime-valuation identities with SymPy, require clean
  byte replay, and reject repaired-hash semantic mutations.
- Compile three substantively different paper rounds twice in fresh trees at
  `SOURCE_DATE_EPOCH=1788048000`, with embedded fonts and no final warning or
  layout defect.

Finite computation checks conventions.  It does not replace the all-modulus
or Hilbert-space proof.
