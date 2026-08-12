# HCS-C32 Phase-3 results

Decision:

`GOOD_PRIME_MORSE_LOCAL_HILL_INFORMATION_GATE=STOP_THEOREM_EXACT_COLLISION`

## Exact registered scan

The scan contains 16 primes and five clock lengths, hence 80 registered cells.
It enumerates primitive marked Hénon states and groups them into cyclic orbit
classes only after the exact return-time test.

Under the frozen collision criterion, exactly one registered cell contains a
collision:

| (p) | (n) | fixed states of (H_6^n) | primitive states | primitive Morse states | collision groups |
|---:|---:|---:|---:|---:|---:|
| 61 | 5 | 15 | 15 | 15 | 1 |

No other registered cell has a collision group.  This is a finite-window
census, not an extrapolation beyond (p\le61,n\le5).

## Decisive orbit pair

\[
z_A=(12,12,40,27,40),
\qquad
z_B=(33,58,36,36,58).
\]

Both are primitive period-five cycles, both have action value (45), and both
have zero critical residuals.  Their exact data are:

| Orbit | (det D^2\Phi_5) | quadratic character | (det(I-DH_6^5)) |
|---|---:|---:|---:|
| (z_A) | 44 | -1 | 44 |
| (z_B) | 7 | -1 | 7 |

The determinant ratio is

\[
44/7=15=25^2\pmod {61}.
\]

The released certificate contains an explicit matrix
(C\in\operatorname{GL}_5(\mathbb F_{61})) with

\[
\det C=22,
\qquad
C^{\mathsf T}D^2\Phi_5(z_A)C=D^2\Phi_5(z_B).
\]

The two henselian Morse function germs are therefore isomorphic, while their
full Hill determinant values differ.

## Theorem implication

For odd characteristic, the Morse-local quadratic Fourier factor is

\[
\psi_r(tc)\chi_r(t)^n\chi_r(\det B)\chi_r(2)^{-n}
G(\chi_r,\psi_r)^n.
\]

The explicit congruence is stronger than equality of this formula: it gives a
change-of-variables identity over every finite extension of
(mathbb F_{61}).  The henselian Morse lemma and functoriality of local
vanishing cycles then imply isomorphic local representations.

Thus the standard unframed good-prime Morse-local factor cannot recover the
full Hill value universally.

## Scope

The result does not prove equality of global Artin--Schreier cohomology.  It
does not remove infinity, degenerate critical points, parameter monodromy, bad
primes, or externally framed local theories.

## Reproducibility record

At release generation:

- certificate SHA-256:
  `c9fe783768ed993df37cdee3ef624e11cb771f69f1b25eb9f9862618e7f170fa`;
- certificate canonical payload SHA-256:
  `e8fb7c1a03c3e600e129bf7ff26598a62db6110ddc9e1b996da9e95b87d2a4d7`;
- independent-check SHA-256:
  `da8b655a7533eae5d863a82f482b64fd81733839323f324a6a0f3a21555f4110`;
- checker result: 14 passed, 0 failed, 0 errors;
- test suite: 22 tests, required to pass in the final runner;
- full artifact inventory: frozen separately in `ARTIFACT_HASHES.sha256`.

The witness was discovered before protocol freeze.  This disclosure is part
of the payload and is mutation-tested.

