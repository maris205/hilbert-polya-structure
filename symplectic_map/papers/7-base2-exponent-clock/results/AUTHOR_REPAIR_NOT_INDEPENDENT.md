# Round-1 author repair record (not independent authority)

Date: 2026-08-14 UTC

This record documents the author's repair and safe self-check of the three
Round-1 deployment blockers.  It is **not** an independent review, is not a
`DEPLOYMENT_PASS`, and grants no authority to execute the registered P4
candidate.

## Frozen bindings after repair

- Source-lock v2 SHA-256:
  `205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1`.
- Repaired reviewed-tree SHA-256:
  `8716715b9449e2943bfbe1e0566c61d2271260cada2f23c6aa70c6b44d4e5b37`.
- Historical Round-1 `FAIL` review SHA-256:
  `c9768c8ecf6b9f066621e687dd8dcf0c01de6adc193cf8da1c0d5894752431f5`.
- Safe JUnit SHA-256:
  `767c8bb51d32958dc14ce8ea5f3e6cfa0e40150ae42349598fbb90b44d411865`.

The reviewed-tree digest binds the exact executable allowlist, `pyproject.toml`,
and the frozen source lock, experiment plan, proof package, and source-lock
audit.  Mutable project narrative and tracker files are intentionally outside
that deployment digest.

## Repairs made

1. The scanner and tree/binding layer now uses a closed file and directory
   allowlist, rejects symlinks, special files, bytecode and caches, tracks
   import/assignment/tuple/subscript/bound-method aliases, rejects dynamic and
   higher-order forbidden callables, and reads/hashes through held componentwise
   `openat`-style dirfd chains.  Parent-directory replacement is detected and
   fails closed.  The three direct wrappers install their reviewed code root
   without external `PYTHONPATH` and disable bytecode before project imports.
2. Algebraic target resultants are converted into the exact coefficient domain
   before zero comparison.  Synthetic `QQ(u)` hit and miss fixtures now make
   gcd, resultant, rational field norm, and hit classification agree, including
   the halt-side lifecycle path.
3. Preflight, result, period, target, polynomial, field-element, claim, terminal,
   registry, JUnit, and result-tree evidence now have exact nonvacuous schemas.
   Polynomial expressions are reconstructed from their basis coefficients;
   leading coefficients, variable, monicity, and the no-hit gcd certificate are
   checked.  The registered run is claimed durably with exclusive creation
   before candidate construction, every lower-level candidate entry revalidates
   live P0--P3 and the claim, and success, hit, and interruption are immutable
   terminal states.  The authority parser requires the exact historical V1
   `FAIL` binding plus one fresh canonical V2 authority.

## Safe self-check only

- Python source parse/compile check: 23 files passed.
- Safe tests: 34 passed, 0 failed, 0 errors, 0 skipped.
- Closed-world executable scanner: passed with 0 findings.
- Safe preflight: passed with status
  `READY_FOR_INDEPENDENT_PRE_EXECUTION_REVIEW`.
- Registered candidate runs: 0.
- Registered candidate periods executed: none.
- P4, prime-table data, Riemann-zero data, floating orbit matching, and network
  access: not invoked.

A fresh independent Round-2 reviewer must inspect the repaired tree and, only
if warranted, append one canonical `BASE2_CLOCK_CODE_REVIEW_V2` authority line
bound to the repaired tree and source-lock hashes.  Until then the deployment
gate remains locked.
