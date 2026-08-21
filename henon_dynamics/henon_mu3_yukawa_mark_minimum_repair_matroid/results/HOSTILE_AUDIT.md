# C84 hostile mutation audit

The checker rejected `18/18` canonical but semantically corrupted receipts.
The mutations target schema, status, scope, C79 authority, ambient/effective
group orders, the rank and basis formulas, mask and exchange-obligation counts,
template and graph counts, line-graph diameter, an all-deleted basis mask, the
C76 equality flag, a per-basis degree, and the main matroid claim.

No mutation was accepted.  The checker has no permissive or warning-only path.
