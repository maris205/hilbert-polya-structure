# HCS-C84 research question

For each deletion set `D` in the frozen sixteen-label model, do all minimum
restoration witnesses form the bases of an explicit matroid on `D`?  If so,
which unlabeled basis-exchange graphs occur, how many deletion sets realize
each type, and how does the all-deleted family compare with C76's 25
full-core-minimal triples?

The proposed answer is the direct sum of:

1. deleted labels irrelevant to a minimum repair, as loops;
2. `S9`, when deleted, as a coloop;
3. the rank `max(0,t(D)-2)` truncation of the partition matroid on the fully
   deleted direction blocks.

Success requires an independent reconstruction of the C75 point-set closure,
direct minimum-witness enumeration for all `65536` deletion sets, maskwise
basis-exchange verification, exact recovery of C79's ten `(rho,W)` cells, and
exact equality of the `D=L` bases with the C76 orbit expansion.

This is a finite named-support question only.  Scope firewall:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
