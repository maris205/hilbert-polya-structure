# C83 results

Canonical evidence SHA-256:
`033f42f0eea2518f7cb269dd465d82d4871a729d2b93679fcd9f3af38cf9ca28`.

Package manifest: [C83_PREFREEZE_MANIFEST.json](../C83_PREFREEZE_MANIFEST.json).

The exact stopping counts are listed in the package README and canonical JSON.
They sum to `16! = 20922789888000`; the reduced probability at `T=3` is
`5/112`, and the exact expected stopping time is `36499/3960`.

All full-core subset sizes and pivotal-label pattern counts are retained in the
receipt, so the stopping distribution can be replayed without enumerating the
twenty-trillion permutations.
