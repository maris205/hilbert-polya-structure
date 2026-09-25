# Scope card — ASFS-SCOUT-20260914-49

| Field | State |
| --- | --- |
| Source object | ECPP certificate chain (n_i, curve data, group-order data, q_i, point) | source-backed external control |
| Arithmetic mechanism | a certificate step proves n_i prime conditional on a smaller prime q_i | target-driven verification |
| Local carrier | elliptic-curve group arithmetic modulo the supplied n_i | changes with certificate step |
| Progress/recursion | n_(i+1) = q_i with q_i < n_i in the certificate chain | strictly descending |
| Local cycles | finite group point addition/multiplication may be periodic for fixed frozen data | local control only |
| Prime-symbolic lineage | none from the prior sieve symbol, sequential deformation, or Hénon lift | EXTERNAL CONTROL |
| Fixed symplectic base / roof / suspension | NOT SUPPLIED | no P0 admission |
| Closed-orbit / repetition ledger | no one action across all certificate steps | NOT TESTABLE |
| Route state | no A0--A2 evaluation; Route B NOT INVOKED | frozen scope |
