# Claims and evidence

| Claim | Proof/evidence |
|---|---|
| Length-`n` block space is a connected manifold of dimension `n(d-2)+1` | `main.tex`, Proposition 2.1 |
| Every pair of symbols admits a bridge of every length at least two | `main.tex`, Lemma 3.1 |
| The relation shift is mixing and has dense periodic points with one-symbol closing | `main.tex`, Theorem 3.2 |
| Equatorial-band covers give the upper scale-entropy exponent | `main.tex`, Lemma 4.1 |
| Homogeneous Markov small balls give the matching lower exponent | `main.tex`, Theorem 4.2 |
| Scale entropy is `(d-2) log(1/epsilon)+O_d(1)` and metric mean dimension is `d-2` | `main.tex`, Theorem 4.2 |
| The normalized Funk chain is unique in the stated homogeneous Markov class and has the recorded spectral gaps | `main.tex`, Proposition 5.1 |
| Bridge, Jacobian-rank, and Funk-spectrum implementations agree | `code/verify_orthogonality_shift.py`; counts in `CONTROL_RESULTS.md` |

Friedland's relation entropy, compact-type metric mean-dimension framework,
and the Funk spectrum are cited inputs.  The residual contribution is the
specific orthogonality-shift gluing and exact scale coefficient.  External
release remains on hold.
