# Stage 4 projective-sign localization

Status: **PASS**

The Stage-4 side test exercises the literal `-I` branch at every one of the
eight registered moduli. Both the sequential-order and group-bound routines
return projective order one with terminal sign `-1`. The same run replays the
five Round-2 tests and verifies the existing 24-row canonical directory
without regenerating or refreshing it.

This is a kernel fixture, not a new owner. All 24 registered owner rows end at
`+I`. That population-level absence is forced by the current setup: every
modulus is divisible by 3 and every registered matrix is in `Gamma(3)`, so an
owner power is `I` modulo 3 and cannot simultaneously be `-I` modulo the
registered modulus. No hyperbolic `-I` owner is claimed or added.

The two order routines remain partially dependent. They use different search
strategies, but both call the same projective `scalar_sign` function and both
ultimately use the same matrix-multiplication primitive. The Stage-4 test
makes that shared-kernel limitation explicit; it is not evidence of an
independently implemented arithmetic kernel.

The canonical Round-2 result tree stayed byte-identical at
`04d212196398835e0a07cf699fb2b30f06164827697af8270c0c4b8475c07413`
under the receipt's stated tree-hash procedure. Route-A state is unchanged and
Route B was not invoked.
