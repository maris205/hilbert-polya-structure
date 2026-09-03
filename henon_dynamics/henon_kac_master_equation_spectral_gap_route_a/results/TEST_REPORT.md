# Test report

All mandatory lanes pass:

- producer: `C322_PRODUCER_PASS`, 21,003 audited leaves;
- independent checker: 10,161 checks and 6,540 exact form cells;
- SymPy cross-check: 71 identities;
- byte replay: evidence SHA-256 `a9ca2cf48318051caf1dfcb35901184ebcd07c6263f9f94498d32f184f49d4c5`;
- hostile mutation suite: 51/51 rejected, plus optimized-Python rejection.

The release gate additionally performs two fresh LuaLaTeX builds for every manuscript round, warning/control-character scans, revision-token checks, font embedding/subsetting checks, page rasterization, exact 27-file payload validation, and self-excluded manifest verification.
