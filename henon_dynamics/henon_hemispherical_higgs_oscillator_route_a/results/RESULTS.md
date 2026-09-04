# Exact results

## Canonical evidence

- File SHA-256:
  `bddd07106ff003318555efe931b12ba10e3938669df23e97770a7f2327c342b5`
- Inner payload SHA-256:
  `07b934a1cb331ae27a52f0b764422d0844a4435a6860114f97c0ad033f858918`
- Bytes: 7,013,177

## Verified scale

| object | exact count |
|---|---:|
| positive-coupling classical cells | 2,048 |
| state labels through N=128 | 8,385 |
| quantum level rows | 129 |
| rational revival controls | 256 |
| irrational revival controls | 256 |
| boundary rows | 6 |

The classical grid is the full Cartesian product of four values of `R^2`,
four positive couplings, eight positive radial actions, eight positive angular
momenta, and two signs. Every row recovers the input action from the energy,
checks the turning discriminant, and verifies the exact 2:1 frequency lock.

The state ledger directly counts every admissible pair `(n_r,m)` satisfying
`N=2*n_r+|m|`; its 8,385 rows give multiplicity `N+1` at each of 129 levels.
This direct count, rather than a prose degeneracy statement in the historical
separation source, is the multiplicity certificate.

For each rational case, the least revival multiplier follows from the reduced
fraction `3+2*nu=a/b`, and the first-level exponent is independently certified
even, so the global phase is one. Every irrational control has nonsquare
radicand and no identity revival.

## Section commitments

- classical rows:
  `7f01972972389d7b653202f8697379166357372c092207002572a9d93feae560`
- quantum state rows:
  `0dda39584c9b42ec0e4c67395d2f27dd14ad64eeb0e981f58a5702a871ad2e61`
- quantum level rows:
  `55d3cb0bbc98ab4bfffebb6aa604549a5f7149973834409a709161cecd20608a`
- rational revival rows:
  `ca42727f2918b326cbb43df5261d3d946d293475213d22365b39e6f85914a684`
- irrational revival rows:
  `dd5b4e4a99a44d0686b618814689263f91a707400b18d9cffc2ab83e281bd16a`
- boundary rows:
  `ca72ce2e16f794513bab6db1c5656aa064aaa20f1cc70435541a07b169315d7a`

Finite enumeration is a regression receipt. The action formula, boundary
atlas, Jacobi spectrum, and revival equivalence are proved for their complete
parameter domains in the theorem package and paper.
