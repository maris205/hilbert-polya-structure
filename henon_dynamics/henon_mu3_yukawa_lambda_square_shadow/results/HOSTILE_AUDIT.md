# C62 hostile audit

## Findings

1. The lambda identities are algebraic character identities and are not used
   as a substitute for orbit-isomorphism testing.
2. The complete atlas stores element sets, so stabilizer, core, normalizer,
   and degree checks are independently replayable.
3. The fixed-field dictionary uses ambient subgroup conjugacy with an explicit
   order-equality guard. A proper-subgroup inclusion cannot be mistaken for
   conjugacy.
4. Multiple subgroup orders split into distinct type labels; therefore the
   dictionary cannot be reconstructed from order alone.
5. Marker noncollision is described only as a formal orbit-labeling result.
   The manuscript does not claim an arithmetic resolvent, discriminant,
   different, local field, Euler factor, or root number.

## Residual limitations

The package remains a finite-group prefreeze result. External novelty
citations and any future arithmetic/local computation are outside this release
and require a new source-bound gate. The literal scope control is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
