# Test report

All mandatory lanes pass:

- producer: `C321_PRODUCER_PASS`, 16,380 audited leaves;
- independent checker: 2,722 checks and all 40,320 weighted parent histories;
- SymPy cross-check: 38 identities;
- byte replay: evidence SHA-256 `4e42cf081790f86a225ab728c81f89fef196e5ce67214f96c57ef0b6cf5e832e`;
- hostile mutation suite: 41/41 rejected, plus optimized-Python rejection.

The final release gate additionally performs two clean builds of each of three manuscript rounds, warning/control-character scans, revision-token checks, embedded-subset-font inspection, page rasterization, exact file-ledger closure, and self-excluded manifest verification.
