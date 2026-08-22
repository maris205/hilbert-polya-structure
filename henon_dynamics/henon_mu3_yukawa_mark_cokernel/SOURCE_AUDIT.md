# C66 source audit

The producer binds the following frozen inputs:

| input | SHA-256 |
|---|---|
| C64 `results/c64_mark_evidence.json` | `7c4673e46f2b97ac03d4e331c762a47286058c36ea243fb20fc39543dd699212` |
| C64 `C64_PREFREEZE_MANIFEST.json` | `eb1d6a55cb81ccfc9b3041879cb913367a514f5c4cba50872d8b286c0ac095b6` |
| C65 `results/c65_defect_evidence.json` | `ebdd80fd2292225b98248aacd6b21bafab2987bdccb801c22c10adef7e7b4e4c` |

The C64 matrix hash is
`4e57d980e774e14709d60feac0fff5af831b6496409d248f398a8a3e2796c307`.
Schema IDs, prefreeze statuses, and `NO_BAD_EULER_OR_ROOT_NUMBER` are checked
before any Smith computation.  C65 is used only for its already certified
compatibility values `(2,8)`, `(2,2,8)`, and relative `Z/2`.

## Bounded novelty audit

Smith normal form and primary decomposition are standard procedures. The
bounded contribution is the exact invariant-factor computation for this frozen
16-by-16 mark embedding, together with its source-bound compatibility check
against C65. No general classification or priority claim is made.
