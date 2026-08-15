# Author Post-Run Provenance Repair (Not Independent)

Date: 2026-08-14 UTC.

This record documents a post-run validator repair.  It is author-written and
cannot satisfy the independent execution review or the independent post-run
analyzer review.

## Immutable registered execution

The registered exact audit was executed exactly once and completed before
this repair.  It was not rerun.  The following artifacts are immutable and
were not modified by this repair:

| Artifact | SHA-256 |
|---|---|
| `results/CODE_REVIEW.md` | `0fe0a5ba625cbbb88bd6ed6a8ff61389a916fd300127a244981fa4643ffa25a6` |
| `results/PRE_EXECUTION_AUDIT.json` | `850cb7cd8eb3ca63dd4e54757e569a66e01f190db0980c8d9682f4931d711883` |
| `results/registered_run.claim.json` | `14b06403bd5a23b533138ccec4962d74910e6e0242abfcf7ac5fe6b3a947a0ee` |
| `results/EXPERIMENT_RESULTS.json` | `0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0` |
| `results/registered_run.json` | `b3a40e9db554ffdc9fe14b654d84f8e918f26fdb47025eb301337b3ecd5fa192` |

Their execution code-tree binding is
`b4441fb68ac42ab1649ee62037fb7cdf741aa9c09a0b0d5cffc4003697caa059`.

## Repaired ambiguity

The original post-run manifest validator compared the raw result's embedded
`pre_execution_gates` against a newly collected live preflight.  That was
incorrect after `results/pytest.xml` was deliberately refreshed following
the registered run: the claim-bound pre-run JUnit hash is
`81ffc571c773cfa9a69f157559fdaa3611f55c748908c20183e4eae3f3420aa1`,
whereas the passing post-run JUnit hash is
`2a0844152eea6d9184d374a6e33c3c4be72fce8deb60296c77650027104348cc`.
The scientific result and every claim/terminal link remained unchanged.

The repaired validator uses two explicit, noninterchangeable code-tree roles:

1. the immutable execution tree, whose result gates must equal the gates in
   the claim-bound immutable pre-execution audit; and
2. the post-run analyzer tree, which may only validate existing artifacts and
   has no authority to execute or rerun the candidate.

It separately validates the current source/upstream hashes, the post-run
execution-tree JUnit, a new analyzer-tree JUnit, and a fresh independent
analyzer authority bound to both tree hashes.  The final manifest schema
records both trees and both JUnit roles.  Missing, stale, malformed, or
ambiguous evidence fails closed.

No source-locked mathematical claim, determinant, factorization, finite-field
profile, exception set, raw result, registered lifecycle artifact, or
execution review was changed.
