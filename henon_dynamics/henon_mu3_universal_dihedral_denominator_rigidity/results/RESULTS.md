# HCS-C54 exact results

Status: **full-project release freeze complete**.

The exact producer and independent checker establish the following certificate
claims.

- For every `n >= 2`, the full projective **monomial** stabilizer of the
  cubic--quadric ideal is `Dih(C_(3n))`, of order `6n`.  This does not classify
  nonmonomial projective automorphisms.
- C53 semilinear transport gives a nonconstant finite étale rational group
  form of geometric rank `6n` with exactly two rational geometric points.
  The Reynolds denominator `6n` and the quadratic-transfer denominator `2`
  remain separate.
- For every packet-admissible row, an actual rational compatible realization
  matching the prescribed good split-prime trace/factor exists exactly when
  `n | 4`, hence only at `n=2,4`.  Packet admissibility means actual pure
  compatible realizations, not semisimplicity.  The proof fixes one
  coefficient prime and passes to semisimplifications before applying
  Chebotarev--Brauer--Nesbitt; C53 does not certify semisimplicity.
- At `n=3`, the exact `Dih(C9)` Cayley--Jacobian and Fermat characters leave no
  nonzero common central source-isotypic sector on which the factor `4/3` is
  integral on both pure rails.
- The nonzero virtual class `1-chi_(K/Q)` is split-invisible, restricts to zero,
  and has rank zero.  It changes neither a `K`-rail rank nor a source-isotypic
  multiplicity.  Rational split primes have absolute density `1/2`; the
  counterpacket hypothesis is relative density one within those split primes,
  which lifts to density one among degree-one primes of `K`.  Here `K0_ss`
  means classes of fixed-coefficient-prime, finite-dimensional continuous
  semisimple `ell`-adic realizations arising from the compatible systems in
  scope and unramified outside one common finite set, not arbitrary Galois
  representations.

Exact control totals:

- universal group rows `n=2..64`: 63;
- independent phase brute force: `n=2,3,4`;
- rational-form fixed-point parity rows `n=2..256`: 255;
- denominator mutation scan `n=2..512`: 511;
- `n=3` Cayley relation images: 126;
- `n=3` Cayley group-law monomial tests: 8,748;
- nontrivial projective scalar-lift descriptor tests: 972;
- semantic gates: 36/36;
- scalar-leaf inventory: 1,078 total = 198 strict semantic + 876 exact-derived
  + 4 chronology-only nonsemantic hashes;
- unit tests: 93/93, including all-digest-rebound semantic sweeps and rollback
  after each of the four release-promotion moves.

Frozen source provenance:

- C53 certificate SHA-256:
  `f4325a5987933e2acf81656389d46701d82d38912c546d1e5996123f617f6e79`;
- C53 implementation commit:
  `0a7f0fdb8290eab4aa92ed5ade432401c40c22cf`;
- C53 provenance commit:
  `9d509d3b3826b7bfbdb38ed9fe4dac9297f5dbdf`.
- committed C53 Route SHA-256:
  `ae508e6e41523559f014f6fbcd0c4c199229f221fe6ac915a75cd27b02e73719`;
- parsed C53 independent-check SHA-256:
  `0d38643ded626c2a5e1536c8a4df9c56ae98c4fda01e1d15660996ea8c495e67`;
- parsed C53 code/results-manifest SHA-256:
  `b62f353d119d6c8565f513dad771a047a5e6343411d08ad2e91562fe84923480`.

Current payload SHA-256:
`f068d5e11ea8e6245e04bd3a30e77140267f835c4e07412ce2009c7fb04ceae1`.

Explicitly excluded are all-`n` smoothness/motives/packets, a full PGL
automorphism classification, a global or inert fractional Euler root,
uniqueness of rational extension from split traces, automorphy, continuation,
functional equation, RH, and any fixed-Frobenius-prime theorem input.

The machine passport remains `RELEASE_CANDIDATE`.
`results/CODE_RESULTS_HASHES.sha256` is the persistent, directly replayable
11-entry code/results inventory; it excludes both manifest files.  The
44-entry full-project manifest includes that scoped manifest together with the
frozen documentation, manuscript and PDF, byte-identical root and archived
Route-A records, code, and results.  The default runner reconstructs both JSON
artifacts in a temporary directory, compares them byte-for-byte with the frozen
copies, and verifies both manifests without modifying stable bytes.
