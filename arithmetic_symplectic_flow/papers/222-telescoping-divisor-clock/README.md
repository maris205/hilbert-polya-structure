# 222 — Telescoping divisor-clock offset stop

**Candidate:** ASFS-20260918-TDC01  
**Status:** STOP — TELESCOPING ROOF HAS THE OFFSET log 2; NO PRIME-LOG CLOCK.

The full all-integer Hénon-form symplectic map has a complete prime-only
periodic ledger and a complete positive-roof suspension. But the frozen phase
scan begins at \(d=2\), so its universal roof telescopes to
\[
T_p=\sum_{d=2}^{p-1}\log\frac{d+1}{d}=\log(p/2)\quad(p\ge3),
\]
not \(\log p\). The \(p=2\) sentinel separately has length \(\log2\).
The initial incorrect normalization was caught by readback audit and is
preserved as a scoped negative finding, without changing the object.

There is exactly one primitive flow packet per prime, with repetitions
\(rT_p\), but the actual scalar product is not the prime Euler product.
All surviving monodromies are unipotent and have vanishing nondegenerate
trace denominators. No operator or formal Route credit is claimed.

The closest timing idea already occurs in
[160](../160-source-geometric-return-clock/README.md), which includes an
initialization phase and explicitly stops promotion on source-clock
naturalness. Neither its extra phase nor its exact clock is borrowed.

- [Full paper and exact audit](paper.md)
- [Frozen candidate card and appended stop](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence and verification record](evidence/README.md)

**Portfolio:** stop / fork on the exact clock. Route coordinates remain
UNASSIGNED; Route B NOT INVOKED.
