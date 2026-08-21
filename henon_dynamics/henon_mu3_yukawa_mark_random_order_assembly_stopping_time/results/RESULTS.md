# C83 results

Canonical evidence SHA-256:
`4777695a3082a2cca1ee82cdced208f0bddf56431285774a51e7563c4cfdfea0`.

Package manifest: [C83_PREFREEZE_MANIFEST.json](../C83_PREFREEZE_MANIFEST.json).

The exact stopping counts are listed in the package README and canonical JSON.
They sum to `16! = 20922789888000`; the reduced probability at `T=3` is
`5/112`, and the exact expected stopping time is `36499/3960`.

All full-core subset sizes and pivotal-label pattern counts are retained in the
receipt, so the stopping distribution can be replayed without enumerating the
twenty-trillion permutations.
