# P197 Review A replay receipt

2026-09-05 UTC. From the workspace root, two fresh processes ran:

`python3 docs/papers197_201_sequence/reviews/p197_a/verify_independent.py`

Both exited zero. Full stdout was collected independently, compared byte
for byte, and saved unchanged as `CANONICAL.txt`. Each run contains
4,814,623 assertions, 797,160 sources and 797,160 targets. The two jobs
were launched in separate operating-system processes; no stochastic seeds
or timing values enter the transcript.

| Item | SHA-256 |
|---|---|
| independent verifier | `86c1c1fc554d2180c14955c0920feea083ede00045a0d494b534dc99e494f50a` |
| complete stdout / canonical | `56cf9e85128085117465b1c365f70a223ced365d37b5f2726364832fa748970b` |

A separate fresh execution of the frozen author verifier was compared
directly with its frozen canonical bytes and matched:
`54d09ba740900f49fdd045c9aae3b3fbe4f0cf2bc6cbbee3fe92f7f98a77d5d1`.
Its 3,998,247 assertions are author reproduction, not reviewer assertions.

All 18 frozen/relevant input hashes were checked from the workspace root
with `sha256sum -c docs/papers197_201_sequence/reviews/p197_a/PINNED_INPUTS.sha256`.
All 12 generated-QA hashes were checked from the `qa/` directory.
The top-level non-self manifest also pins that QA manifest.

No author module is imported. Python standard-library dynamics are combined
with SymPy 1.14.0 only for exact Berkowitz characteristic coefficients and
integer Möbius values. Two matching finite runs do not prove all-size
theorems; the independent deductive audit is in `PROOF_REDERIVATION.md`.
