# Paper 27 Stage 4-prime response to reviewers

## REV-03 — resolved

The two order routines are now described as separately implemented at the
high-level search-strategy layer and explicitly shared at the low-level
`scalar_sign` and matrix-multiplication kernel. The existing `-I` localization
note, direct test, receipt, and read-only replay are bound into the revision
evidence package. This fixture remains shared-kernel branch coverage: it adds
no owner, independent arithmetic implementation, canonical result, or Route
credit.

Applied locations: `B0040/B0108`, `B0041/B0109`, and `B0042/B0110`.

Result: **RESOLVED**. All 10/10 registered surfaces remain byte-exact once;
the isolated test suite passes 8/8 and the canonical verifier passes without
refreshing results.
