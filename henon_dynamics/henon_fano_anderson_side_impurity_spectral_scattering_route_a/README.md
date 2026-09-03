# HCS-C345 / HEN-O329 — Fano--Anderson side impurity

This package owns the infinite one-dimensional nearest-neighbour chain with a
single discrete state side-coupled at the origin.  For every `J>0`, real
`epsilon`, and nonzero real `g`, it proves the full spectral type, the two
physical-sheet bound states, the impurity spectral measure, and the exact
one-channel scattering law including the Fano transmission zero.

The spectral-measure proof fixes the resolvent sign convention explicitly:
`G_dd=<d,(z-H)^(-1)d>` is anti-Herglotz and `-G_dd` is Herglotz.  Uniform
open-band boundary limits, Stone inversion, exterior pole classification, and
zero band-edge atom limits jointly exclude a singular-continuous remainder.

The proof is infinite-volume and branch-safe.  The squared secular quartic is
used only with its physical sign constraints; finite chains are regression
objects and never evidence for the infinite-volume spectral theorem.

## Release objects

- `THEOREM_PACKAGE.md`: theorem, proof dependencies, boundary atlas.
- `results/c345_fano_anderson_evidence.json`: canonical exact receipt.
- `code/c345_fano_anderson_checker.py`: independent strict checker.
- `paper/main.pdf`: final round-two manuscript.
- `C345_RELEASE_MANIFEST.json`: self-excluding 27-payload ledger.

The fixed scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.  Route A is rejected with
tuple `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` and Route B
is not invoked.
