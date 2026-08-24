# Exact experiment plan — HCS-C136

## Purpose

The computation is a theorem receipt, not a numerical phase comparison.  It
must detect missing inverse scalings, half-phase sign errors, wrong Weyl
conventions, false antiunitary identities, and over-broad coherence claims
using integers only.

## Frozen certificates

Two-factor levels:

`(3,5), (3,7), (3,11), (3,13), (5,7), (5,9), (5,11), (7,9)`.

Three-factor levels:

`(3,5,7), (3,5,11), (3,7,11), (5,7,9)`.

The generalized global characters `c=1,2` are used in every triple receipt.
A four-factor arithmetic sentinel uses `(3,5,7,11)` with left, right, and
balanced parenthesizations for the same ordered leaves.  No permutation receipt
is used or claimed.  Single-level antiunitary sentinels exhaust every unit
character at levels `3,5,9,15`.

## Exact tests

For each pair `L=MN`:

1. reconstruct the CRT idempotents and inverse coefficients;
2. exhaust all `L^2` Fourier kernel congruences;
3. exhaust all `L` chirp diagonal congruences;
4. exhaust all `L^2` unitary kernel congruences;
5. exhaust all `L^3` Weyl-on-basis phase and output-shift cases;
6. verify the real CRT basis permutation intertwines coefficientwise
   conjugation and exhaust the `c=1,2` antiunitary CRT kernels.

The frozen totals are:

- 13,520 Fourier kernel cases;
- 306 chirp diagonal cases;
- 13,520 unitary kernel cases;
- 658,314 Weyl basis-action cases;
- 306 conjugation-basis cases;
- 27,040 antiunitary CRT kernel cases.

For each triple and both characters, exhaust every unitary kernel entry after
direct, left-bracket, and right-bracket character reconstruction.  This adds
381,672 kernel cases.  The four-factor sentinel adds six exact bracketing
comparisons.

For every unit character at the antiunitary sentinel levels, exhaust the
Fourier orthogonality matrix for `Theta^2`, the kernel reduction proving
`Theta U Theta^(-1)=U^(-1)`, and every Weyl basis action proving the coordinate
swap.  These add 2,404, 2,404, and 31,928 cases, respectively.

## Independent paths

- The producer streams case hashes and writes the evidence object.
- The checker independently reconstructs all 1,131,414 enumerated cases and
  closes every schema field without importing the producer.
- The SymPy/congruence path verifies CRT idempotents, all pair kernel and
  antiunitary congruences, multi-factor coefficients, and cyclotomic negative
  controls.
- Replay regenerates the JSON in a temporary directory and compares bytes.
- The mutation suite repairs the payload hash after each semantic change, then
  tests one separate stale-hash mutation.  Its repaired cases explicitly attack
  every antiunitary headline and the fixed-ordered-leaf boundary.

## Negative controls

- `(3,5)` with `a=b=1` must fail even up to a scalar;
- `(5,7)` with raw residues instead of inverses gives exponent `4`, not `1`,
  modulo 35;
- `(3,9)` is rejected before CRT because the factors are not coprime;
- level 4 is rejected only for the unchanged odd half-phase convention.

No randomness, fitting, floating point, external data, or network access is
permitted.
