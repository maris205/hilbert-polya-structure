# Nested primorial periods force dense factor singularities on the packet-zeta boundary

**Paper ID:** `036-primorial-packet-zeta-boundary-audit`  
**Record ID:** `AFC-20260914-PZA01`  
**Date / status:** `2026-09-14; T3 LOCAL PRODUCT RETAINED; ANALYTIC PROMOTION STOPPED`  
**Route state:** `Broadened analytic audit only; Route B NOT INVOKED`

The 032 packet zeta is

```text
Z_P(s)=product_(k>=1)(1-exp(-s P_k))^(-1),     Re(s)>0.
```

Each factor has roots of its denominator at `s=2 pi i n/P_k`. Since the mesh
`2 pi/P_k` tends to zero, the union of these root sets is dense on the imaginary
axis. More strongly, if `s=2 pi i n/P_j`, then for every `k>=j`,
`P_k/P_j` is an integer and `exp(-sP_k)=1`. Thus infinitely many later factors
share the same boundary root.

This is an exact property of the same packet periods, not a numerical
observation. It does not prove a natural-boundary theorem or rule out every
possible continuation construction. It does prove that the local Euler product
cannot be promoted by rhetoric into a simple global divisor statement: any
extension must explicitly confront these dense, infinitely repeated factor
singularities. No such extension is present.

**Portfolio decision: stop analytic promotion.** Retain 032/035 as a local
broadened T3 chain. Do not develop target comparisons, quantization, or Route
language for this product unless a new same-object analytic construction is
specified and audited separately.

## Evidence index

- [Audit card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence](evidence/README.md)
