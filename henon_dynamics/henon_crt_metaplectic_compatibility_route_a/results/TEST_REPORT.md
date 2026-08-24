# Test report — HCS-C136

All tests were run from the repository root with Python 3 on 2026-08-24.

| command | result |
|---|---|
| `python3 .../code/c136_crt_metaplectic_producer.py` | PASS; deterministic evidence generated |
| `python3 .../code/c136_crt_metaplectic_checker.py` | PASS; 1,131,414 enumerated exact cases plus closed schema |
| `python3 .../code/c136_sympy_crosscheck.py` | PASS; 96,449 exact checks |
| `python3 .../code/c136_replay.py` | PASS; byte-identical replay |
| `python3 .../code/c136_mutation.py` | PASS; 83 repaired-hash semantic plus one stale-hash mutation rejected |

The exact evidence SHA-256 is
`5b3f4a6494c8f4559a99b520247c1b83f1504884a31aaeb1fcdc3c153bbac47b`.
Its internal canonical payload SHA-256 is
`10aecc0620400102eb0776794dd43d587d87ff2adeb2c10c1309c3504ebaddc7`.

## Independence

The checker does not import the producer.  It independently reconstructs the
CRT idempotents, every case ledger, the antiunitary involution/reversal/Weyl
swap and CRT identities, all constants, controls, route fields, and closed
dictionaries.  The symbolic cross-check uses SymPy modular and
cyclotomic arithmetic rather than the producer's ledger implementation.

## Mutation semantics

Semantic mutations alter phase conventions, inverse coefficients, Weyl
exponents, operator identities, ledger hashes/counts, bracketing receipts,
antiunitary headlines and ledgers, the fixed-ordered-leaf boundary, negative
controls, progress claims, scope flags, and Route-A fields.  The
payload checksum is repaired before validation, so rejection cannot be
credited to stale bytes.  One additional mutation deliberately keeps the old
checksum and verifies the checksum gate.

## PDF gate

The final four-page PDF has SHA-256
`ab83e92b78e5857946d501c579bc3d53ca233ea5d32bf1c1865506ce776a460d`.
Two fresh isolated fixed-epoch builds are byte-identical.  Every font is
embedded and subset; the final log has no warning, bad box, undefined
reference/citation, or multiply-defined label.
