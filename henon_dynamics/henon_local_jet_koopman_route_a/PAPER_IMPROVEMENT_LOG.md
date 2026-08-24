# Paper improvement log — C114

No external reviewer or numerical review score is claimed.  Two internal,
evidence-led revision passes were applied.

## Round 0 — baseline

The baseline draft defined the local quotient, listed the total dimension,
and stated the finite determinant factorization.  It did not yet explain why
composition descends to the quotient or distinguish nonlinear entries from
the linearized control.

## Round 1 — proof and convention repair

- added the maximal-ideal argument proving that pullback is well defined;
- fixed and printed the column-image matrix convention and basis order;
- added the five associated-graded blocks with exact traces, determinants,
  and eigenvalues;
- replaced a bare spectral assertion by the filtration proof from the
  linearization eigenvalues \(1\) and \(1/2\).

The resulting PDF is preserved as `paper/main_round1.pdf`.

## Round 2 — nonlinear and boundary repair

- added the 11-entry nonlinear-control comparison and nilpotence index four;
- added the closed trace-power formula and its eight-value evidence prefix;
- stated explicitly that \(\det(I-zK)\) is an ordinary finite determinant,
  not a global Fredholm determinant;
- added independent-checker, replay, hostile-mutation, deterministic-build,
  and font-embedding provenance;
- tightened all global-spectrum, analytic, arithmetic, and Route-B nonclaims.

The final PDF is `paper/main.pdf` and is preserved byte-for-byte as
`paper/main_round2.pdf`.
