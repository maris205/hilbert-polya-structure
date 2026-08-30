# Consolidated hostile-review verdict — P122

Status: **GO_INTERNAL / EXTERNAL HOLD**.

Reviewer A reconstructed the full clock, fibre inverse, DP, Boolean image
state and weighted transfer.  No theorem counterexample was found, but the
round-zero paper received `STOP/REWRITE` for four material defects: incorrect
live Huang metadata and incomplete source control; an underdefined five-bit
invariant; absent P105/P117/P120 collision subtraction; and no auditable
fibre/bit example.

The round-one rewrite corrected all four items.  Reviewer B independently
reconstructed the repaired proof, checked all five coordinate invariants,
exhausted record words through length 16 with 983,045 additional state
assertions, verified the worked target, audited the current primary records,
and reran both the 1,637,027-assertion paper verifier and an isolated build.
The re-entry decision was `GO_INTERNAL`, with critical 0 and major 0.

The sole nonblocking wording minor was repaired in round two by making the
abstract's external-HOLD status match the body and support package.  This did
not change any theorem, equation, code, reference or evidence boundary.
Novelty, priority and all external circulation remain **HOLD**.
