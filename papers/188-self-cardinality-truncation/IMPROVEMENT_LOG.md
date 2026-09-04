# Improvement log — P188

## Pre-freeze repairs

1. Added the `n=0` carrier and all small-boundary statements.
2. Distinguished the exact pointwise clock from the scalar rank sequence.
3. Strengthened the one-step formula to an iff image criterion, exact image
   count, empty-target count, and total mass check.
4. Lifted the inverse result from time one to every time using nested rank
   chains and interval-capacity binomial factors.

Round 0 was frozen after two verifier replays and deterministic PDF mechanics
passed.

## Hostile Review A and Round 1

The process-separated reviewer used a `frozenset` carrier and a backward
interval-capacity construction rather than the author implementation. It
reopened the endpoint/basin proof, unique depth extremizer, one-step image,
largest fibre, and the all-time every-target chain formula through post-height
times. Its 8,193,247 exact assertions returned
`Critical 0 / Major 0 / Minor 0`, `PROVABLE_AS_STATED`, and
`ACCEPTED_NO_CHANGE`.

No source repair was requested. `main_round1.pdf` is an intentional
byte-identical receipt of Round 0, with SHA-256
`10b881a6200e075ed66514e8f4f8873c433383c8118c6037ad1ecd1d5bcb8bc3`.

## Hostile Review B and Round 2

Review B rebuilt the dynamics from target profiles `(b,M(B))` and difference
variables `d_j=k_j-k_{j+1}`, avoiding both the author's direct chain
enumeration and Review A's backward interval-capacity program. Its 57,622
exact assertions reopened the all-time chain formula, unique deepest state,
every-target fibres, Fibonacci image law, and largest-fibre census, and
returned `Critical 0 / Major 0 / Minor 0`.

No source or PDF change was requested. `main_round2.pdf` is therefore
byte-identical to Round 0 and Round 1, with SHA-256
`10b881a6200e075ed66514e8f4f8873c433383c8118c6037ad1ecd1d5bcb8bc3`.
Terminal QA later confirmed two source-only cold builds, both reviewer-package
replays, final manifests, and PDF mechanics. `OWNER_AMBER / HOLD_EXTERNAL`
remains binding.
