# Paper improvement log — P132

## Round-0 provenance

The immutable `main_round0_original.pdf` records the first anonymous build.
Its bibliography parsed the second author's suffix incorrectly.  Before
Review A, the BibTeX author field was corrected, yielding a distinct current
PDF while leaving the mathematical body unchanged.  Review A records both
hashes; the divergence is not treated as a theorem repair.

## Round 1 — implementation of Hostile Review A

Review A returned no critical or major finding and four mandatory minor
repairs:

- `A132-1`: removed the stray commas from the exponents in the fixed-language
  theorem, so the displayed words are literally `0^(n-2r)` and `1^(n-2r)`;
- `A132-2`: restored the missing backslash in the constant-fibre display's
  spacing command;
- `A132-3`: replaced “complete finite dynamics” in the abstract by the exact
  delivered scope—recurrent set, sharp global stabilization, and target-wise
  one-step fibres; and
- `A132-4`: retained the immutable round-zero PDF and documented the pre-review
  bibliography-only delta instead of conflating the artifacts.

No theorem formula, verifier, canonical output, or contribution ceiling was
enlarged.  The fresh replay passed byte for byte; the repository and isolated
four-stage builds agreed; the repaired locations were inspected; and
`main_round1.pdf` was frozen at SHA-256
`dcfd7eddb0cb85a197f0ae875af97fd353f50070317ca4ec6f8de0ad5a74527e`.
External status remains `HOLD_EXTERNAL`; no Git action was taken.

## Round 2 — implementation of Hostile Review B

Round B independently reconstructed the complete theorem package and returned
no critical or major finding.  Its sole minor, `B132-1`, found that the
Round-0 PDF hash in `BUILD.md` had been transcribed incorrectly.  The ledger
now records the fresh digest
`f6329905059f20811380dcfe1163d9cd908a592e428a358ec1f9461d55140679`,
which agrees with Review A and the preserved artifact.  No source, theorem,
verifier, bibliography, canonical stdout, or PDF byte changed.

The original reviewer independently rehashed the artifact, replayed the
verifier, and closed `B132-1`.  Final Round-B severity is critical 0, major 0,
minor 0 with `GO_INTERNAL / HOLD_EXTERNAL`.  `main_round2.pdf` is the
support-only sign-off copy, byte-identical to `main.pdf` and
`main_round1.pdf` at SHA-256
`dcfd7eddb0cb85a197f0ae875af97fd353f50070317ca4ec6f8de0ad5a74527e`.
