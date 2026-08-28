# Hostile audit

The mutation harness uses a temporary copy of the evidence and never edits the canonical receipt.  It injects semantic changes into source/evaluator/scope locks, \(\mu,q,p,E,L,A\), eccentricity and residuals, conic labels, period/action/scattering/collision fields, Levi–Civita fields, fixed-set dimension, route tuple, attribution, and summary counts.  Each modified payload is rehashed before invoking the independent checker, so a passing hash alone cannot hide a semantic mutation.

It also injects an unknown root key and one stale-hash mutation.  The release result is 24 repaired-hash rejections, 1 stale-hash rejection, 25 total, with the unknown-key case included.  No mutation is accepted.
