# Improvement log — P187

## Pre-freeze repairs

1. Split lengths one and two from the exponent-height formula.
2. Replaced ambiguous `C_1/C_2` graph language with an explicit cyclic
   zero--one support polynomial.
3. Added all-target mass conservation and the `N=1` empty-product boundary.

Round 0 was frozen after the verifier, bibliography, build log, and PDF
mechanics passed.

## Hostile Review A and Round 1

The process-separated reviewer independently reconstructed exponent dynamics,
cyclic support counts, target traces, all short-cycle conventions, and fibre
mass. Its 1,444,819 exact assertions returned
`Critical 0 / Major 0 / Minor 0`, `PROVABLE_AS_STATED`, and
`ACCEPTED_NO_CHANGE`.

No manuscript delta was requested. `main_round1.pdf` is therefore an
intentional byte-identical copy of the accepted Round-0 PDF, with SHA-256
`399ee1fd64a569ef3076e1049a5151e5b4b07d03d2c1592f84c5b2a811fbb8a1`.
Review B and terminal QA remain required; `HOLD_EXTERNAL` remains active.
