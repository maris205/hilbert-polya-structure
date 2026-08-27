# Paper improvement log

No external reviewer, reviewer score, or independent error process is claimed.
The two revisions are internal theorem/scope audits bound to executable bytes.

| round | substantive content |
|---|---|
| 0 | Frozen Fourier sign; full characteristic formula; composition; exact, sharp sector norm, attainment boundary, and scale. |
| 1 | Added inviscid mixing, all parameter boundaries, periodic-state classification, reversor, and non-trace-class proof. |
| 2 | Added checker/SymPy/replay/mutation closure, explicit 100-working/82-serialized precision contract, source ownership, Route-A tuple, declarations, and claim firewall. |

Round 1 specifically checked the direction `eta -> eta+a k t` and the
composition evaluation point. Round 2 checked that norm one in the `k=0`
sector is not confused with a nonzero periodic eigenvector, and that the
noncompact channel is not assigned a Fredholm determinant.

The release audit also removed an ambiguous norm-attainment phrase.
The final statement distinguishes sharp operator-norm equality from existence
of a maximizing `L2` vector: nonattainment for `nu*t>0`, unitary attainment for
`nu*t=0`.

The final internal audit also replaced the ambiguous “100 decimal digits”
label by two testable fields: 100 working decimal digits and 82 serialized
significant digits.
