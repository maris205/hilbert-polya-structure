# Test report

All mandatory lanes pass:

- producer: `C316_PRODUCER_PASS`, 14,914 leaves;
- independent checker: 10,315 checks;
- SymPy cross-check: 105 identities;
- byte replay: evidence SHA-256 `3b0004c830c2579e234a5263a3a76c7a65272e5b45f7de74165af94538dccd64`;
- hostile mutation suite: 39/39 rejected, plus optimized-Python rejection.

The final release gate additionally performs two clean builds of each of three manuscript rounds, warning scanning, text-token checks, font embedding/subsetting checks, page rasterization, exact file-ledger validation, and self-excluded manifest verification.
