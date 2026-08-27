# C197 test report

## Executable gates

- Producer: exact rational evidence generated successfully.
- Independent checker: projector/reflection reconstruction passed.
- SymPy: symbolic block, modulus, determinant and every evidence row passed.
- Replay: canonical evidence reproduced byte for byte.
- Mutation: all repaired-hash semantic attacks and the stale-hash attack were
  rejected.

Exact command outputs and counts are re-run before manifest closure; release
hashes are recorded in `C197_RELEASE_MANIFEST.json`.

## PDF gates

The release requires three content-distinct revision PDFs, `main.pdf` equal to
round 2, two fresh fixed-epoch builds with identical SHA-256, embedded fonts,
extractable text, a clean log without bad boxes/reference warnings, and visual
inspection of every rendered page.

## Interpretation

Finite rational blocks are regression tests.  They are not used to infer the
all-subspace decomposition or global optimality theorem.
