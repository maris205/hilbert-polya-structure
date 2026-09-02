# Exact results — C297

The canonical receipt has SHA-256
`5d3bba21dd63e89f0183427a111b663f20ef6da5fb65e2ffdf186c137e42273a`
and self-excluding payload SHA-256
`f8ec6fa154f636efef854236327e71f7e6e870a8e84d2cbee609f9e6ddcdeeaa`.

The complete exact regression rectangle contains 168 parameter cells:

| phase | cells |
|---|---:|
| unbroken | 64 |
| exceptional | 16 |
| broken | 88 |

Eight additional cells close the Hermitian axis, both exceptional sheets,
the uncoupled and zero-generator limits, eigenrays, the zero vector, and the
vector/projective period convention.

Independent validation produced 6,475 checker assertions and 516 SymPy
checks.  Two fresh producer paths were byte-identical to the archived
85,343-byte evidence file.  All 52 hostile mutations were rejected.  The
obstruction identifier `HEN-O281` is independently locked in evidence and
evaluation.
