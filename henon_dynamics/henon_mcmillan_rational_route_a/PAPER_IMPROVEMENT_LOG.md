# Paper improvement log

No numerical reviewer scores are asserted.

## Round 0 — algebraic baseline

The baseline manuscript stated the rational inverse, first integral, valid
fixed locus, real two-cycle, and local monodromy.  It was mathematically
correct but compressed the denominator-clearing issue into prose.

## Round 1 — domain and pole audit

The revision exposed the raw second-iterate resultant, separated the
\((x^2+1)^2\) pole factor, and added a domain-status table.  It now states why
\(x=\pm i\) are not complex periodic points and reports the nonzero
denominators for every certified orbit row.

## Round 2 — ownership and control audit

The final revision added the fixed-origin control polynomial
\(z^2+4z+1\), contrasted it with the two-step cycle polynomial
\((1+z)^2\), and explicitly denied transfer/Fredholm ownership.  The Route-A
verdict was narrowed to `A1_PARTIAL_CERTIFIED`, `A2_FAIL`,
`A3_NOT_ADDRESSED`, `A4_FAIL`.

## Format audit

The final source is built twice in isolated temporary directories with
`SOURCE_DATE_EPOCH=0` and `TZ=UTC`.  The two hashes must agree; all fonts must
be embedded; the final log must contain no undefined reference, undefined
citation, overfull box, or underfull box warning.
