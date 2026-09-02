# Test report

All mandatory lanes pass:

- producer: `C317_PRODUCER_PASS`, 7,720 leaves;
- independent checker: 8,490 checks;
- SymPy cross-check: 483 identities;
- byte replay: evidence SHA-256 `51943f98667f9b121c386d4b92584ea1cdbafa88937430891f17078aff0a125a`;
- hostile mutation suite: 40/40 rejected, plus optimized-Python rejection.

The release gate also performs two clean deterministic builds per revision round, warning scanning, round-token checks, font embedding/subsetting checks, rasterization, exact file-ledger validation, and self-excluded manifest verification.
