# FOSP independent Stage-1 replay receipt

Date: 2026-09-05 UTC. Reviewer: `/root/batch197_fosp_gate`.

Implementation SHA-256:
`12cc0ddb6db24a365625ce6630eda4e9b904915652b3a156b9f100c9125efaad`.

Canonical stdout SHA-256:
`baade2cc4fb29d31fb0a5b2d5560de283959e901faeb1a44b3c69fc2fe43de06`.

The initial complete run was executed directly and its observed output was
saved as `CANONICAL.txt`. Two further fresh Python processes were captured
and compared byte-for-byte with the canonical. Both returned exit code zero:

```
frozen canonical replay 1: PASS
stdout_sha256=baade2cc4fb29d31fb0a5b2d5560de283959e901faeb1a44b3c69fc2fe43de06
frozen canonical replay 2: PASS
stdout_sha256=baade2cc4fb29d31fb0a5b2d5560de283959e901faeb1a44b3c69fc2fe43de06
```

Each process used `python3 -B verify_independent.py` at its default maximum
n=7. The implementation imports standard-library modules only and imports
none of the author code. The root can reproduce the canonical with that
command from this directory.

Per-run scope: all 146,600 ordered increasing trees across n=0,...,7;
1,496,779 assertions. Repeated executions are reproducibility checks, not
additional independent theorem axes or additional validated subclasses.
The author's separate 71,614,800-count n<=8 transcript is an input record;
this receipt does not claim to have replayed that author implementation.
