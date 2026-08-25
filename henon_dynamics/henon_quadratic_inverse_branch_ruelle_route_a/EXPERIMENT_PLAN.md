# C141 exact experiment plan

## Claim-driven tests

1. Generate \(F^n(z)-z\), \(1\le n\le6\), exactly by integer polynomial composition.
2. In \(\mathbb Q[z]/(F^n-z)\), invert \(\Lambda_n(\Lambda_n-1)\). The trace of multiplication by this inverse is \(\operatorname{Tr}\mathcal L_2^n\).
3. Apply the Fredholm Newton recurrence to obtain coefficients through \(u^6\).
4. Independently reconstruct the quotient algebra by polynomial extended Euclid; do not import the producer.
5. Cross-check with SymPy polynomial inversion for all six periods and resultant logarithmic derivatives for periods one through three.
6. Verify the exact \(m=0,1\) controls, rooted/primitive counts, byte replay, and semantic mutation rejection.
7. Compile the short theorem paper twice in isolated fixed-epoch directories, audit fonts/warnings/text, and visually inspect every page.

## Acceptance conditions

- Producer, full independent checker, SymPy cross-check, byte replay, and mutation suite all exit zero.
- All six recorded period polynomials and traces are exact.
- The checker rejects 36 repaired-hash semantic mutations and one stale-hash mutation.
- The paper distinguishes the entire determinant from the \(|u|<4\) raw product.
- Exactly 27 payload files are content-addressed by a self-excluded manifest.

## Negative control

The same \(\mathbb D_4\) construction for \(z^2-2\) must be rejected because its inverse branch point lies inside the disk.
