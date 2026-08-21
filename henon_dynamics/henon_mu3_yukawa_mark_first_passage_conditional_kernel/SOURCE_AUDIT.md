# C98 source audit

| Source | Role | SHA-256 |
|---|---|---|
| C88 evidence | marginal PMFs, survival boundaries, packed support hits | `4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b` |
| C88 manifest | frozen C88 package ledger | `aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5` |
| C90 evidence | 400 joint-survival arrays | `c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978` |
| C90 manifest | frozen C90 package ledger | `4233c3b8e60a09729ce1befdb68e28566bde87042fef3059f8ff98cac6ebb737` |

Both canonical JSON inputs and both manifests are hash-checked before any
calculation.  The producer and checker use separate implementations.  The
checker additionally tests every equal-threshold C90 survival cell directly
from intersections of C88 nonhit support bitsets and factorial completion.

The literal firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.  No arithmetic/local
data, Euler factors, root numbers, automorphy, full Burnside ring/table of
marks, or Hilbert--Polya operator enters the source contract.
