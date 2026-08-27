# HCS-C207 — full-exponent Barenblatt similarity atlas

This theorem package classifies the centered, nonnegative, integrable
first-kind similarity profiles whose `F^m` is locally absolutely continuous
and whose zero-flux profile identity holds almost everywhere, for

\[
u_t=(u^m)_{xx},\qquad x\in\mathbb R,\quad m>0,
\]

at prescribed mass `M>0`.  It treats the compact-support (`m>1`), Gaussian
(`m=1`), and algebraic-tail (`0<m<1`) regimes in one normalization, including
exact Beta-function masses and all absolute moments, the sharp fast-diffusion
moment boundary, pressure/free-boundary data, and the stated finite-energy
rescaled dissipation law.

The all-parameter statements are proved symbolically in
`THEOREM_PACKAGE.md` and `paper/main.tex`.  The finite ledger is an exact,
deterministic convention audit; it is not an interpolation proof.  It uses
100 working decimal digits and stores 82 significant digits in each
nonzero decimal certificate field.

Run from this directory:

```bash
python3 code/c207_barenblatt_producer.py
python3 code/c207_barenblatt_checker.py
python3 code/c207_barenblatt_sympy_crosscheck.py
python3 code/c207_barenblatt_replay.py
python3 code/c207_barenblatt_mutation.py
python3 code/c207_release_manifest.py
```

The release contains 27 manifest-tracked payload files plus the self-excluded
manifest.  Scope is frozen to `NO_BAD_EULER_OR_ROOT_NUMBER`; Route A is
rejected and Route B is not invoked.
