# P178 improvement log

## Round 0 → Round 1

Hostile Review A independently reconstructed the difference flag, anchored
lift, image/fibre atlas, rooted clock, and complete Jordan inventory.  It also
used `GF(4)` as a positive scope guard, confirming that the theorem's
prime-field quantifier must not be widened.  No Critical or Major issue was
found.

The sole Minor concerned evidence provenance: the author-created verifier was
called “independent.”  `README.md`, `BUILD.md`, `SELF_QA.md`, `PAPER_PLAN.md`,
and the verifier docstring now call it a paper-local author-side control.
No theorem formula or manuscript source changed.  Consequently Round 1 is a
deliberate byte-identical PDF freeze with SHA-256
`b637423674d7ec40f0e1e316a60f92b1dc5cc3d30061c8cbd444c8aaab5e76ce`.

## Round 1 → Round 2

Reviewer A accepted the provenance repair after two 53,524-assertion replays;
Reviewer B independently reproduced 36,899 assertions and closed the same
wording boundary.  Both report zero open findings.  Since the repair was
documentation-only, Round 0, Round 1, and Round 2 PDFs are intentionally
byte-identical.  Two final source-only cold builds and 3/3 visual pages pass.
External status remains `OWNER_THIN / HOLD_EXTERNAL`.
