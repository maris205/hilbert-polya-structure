# Checked deterministic results

This directory contains eleven CSV ledgers and `manifest.json`, with exactly
3,486 body rows. The manifest binds the active Paper-12 v4 content tuple, the
Phase-1/Phase-2 gates, the v4 final gate and status re-lock, all six control
implementation files, every artifact schema, row count, byte count, and
SHA-256 digest. It deliberately does not bind a concurrently drafted v4 proof.

The ledgers cover nerve/face/`d^2`, T0 factorization and its non-T0 falsifier,
finite `Z1/B1/H1` witnesses, marked isotropy periods, strict/scaled/unmarked
maps, quotient topology direction, the source-gated packet schema, label
neutrality, and explicit negatives. The added orbitwise ledger records exact
finite common-cycle `Z`-action cohomology, automorphisms, basepoint transport,
the diagonal/invariant calculation, nonzero coboundaries, zero-isotropy
potentials, mixed-length rejection, and wrong-`J`-direction rejection. Its
3,252 rows are schematic controls, not theorem proofs, source substitutes,
Route verdicts, or arithmetic-specific evidence.

`manifest.json` is generated mechanically. Do not edit it or a CSV by hand;
`--verify-only` fails closed on content, hash, row, schema, filename, lock,
gate, implementation, or manifest drift.
