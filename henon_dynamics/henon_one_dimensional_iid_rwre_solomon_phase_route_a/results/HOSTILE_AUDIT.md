# Hostile audit

## Mathematical attacks

- Replacing the direction condition by a first-moment condition is rejected.
- Promoting every transient chamber to nonzero speed is rejected.
- Interchanging \(\rho\) and \(\rho^{-1}\) changes the reflected chamber and
  is rejected.
- Treating annealing as resampling the environment on every visit is rejected.
- Claiming that finite enumeration proves the infinite-time theorem is rejected.

## Artifact attacks

The checker rejects repaired-hash changes to IDs, date, source commit, scope,
evaluator authority, model assumptions, theorem contract, collision boundary,
nonclaims, sources, Route-A tuple, Route-B lock, every exact ledger, and row
digests.  A repaired-hash source mutation specifically rejects the unrelated
`arXiv:math/0503089` in place of Zeitouni's Springer DOI.  It also rejects
missing, duplicate, truncated, or extended coordinate sets.

Strict parsing rejects duplicate and nonfinite JSON, JSON with a non-object
root, YAML anchors and aliases, merge keys, non-string keys, implicit dates,
unknown fields, type changes, and a non-object YAML root.  Raw and semantic YAML
hashes are independently bound into the evidence.

## Scope result

All forbidden flags remain false.  The package contains no target arithmetic
local data, target Euler factor, root number, automorphy assertion, target
functional equation or divisor, target-zero match, Hilbert--P\'olya operator,
or Route-B invocation.
