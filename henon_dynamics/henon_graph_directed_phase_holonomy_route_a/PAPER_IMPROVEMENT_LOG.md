# C129 paper improvement log

No external reviewer, score, novelty estimate, or acceptance prediction was
used. The two rounds below are internal claim/evidence and presentation audits,
each followed by deterministic recompilation.

## Round 0

Artifact: `paper/main_round0_original.pdf`

SHA-256: `be2fad2716ec5be544202d0b7e889151b6c1b06ff7a203856826fd1e3b1493e9`

The initial manuscript states the frozen character, all-order trace and
Fredholm formulas, and the exact control pair. Its principal weakness is that
the group-ring mechanism separating primitive-character evaluation from the
trivial character is too implicit.

## Round 1

Artifact: `paper/main_round1.pdf`

SHA-256: `f0ea2c28381c18438d925707916c535e16701e2d2bd452883407288ddd3142b3`

The revision adds `Q[Z/5]`, its augmentation, and its cyclotomic quotient as
distinct maps. This prevents the invalid operation of setting a primitive root
equal to one inside the cyclotomic quotient and makes the exact C124
degeneration auditable.

## Round 2

Artifacts: `paper/main_round2.pdf`, `paper/main.pdf`

SHA-256: `c3e4fc5b46116583dea7f1dff2c084e0ea348adff269b4484f3579d36e86ae35`

The final revision sharpens the interpretation boundary: sensitivity is only
to the frozen translation residues and branch assignment, not to complete
geometry. It also states why the phase gives `A4_FORMAL_HINT` rather than a
unitary-quantization pass, and labels the finite period-eight ledger as replay
rather than theorem cutoff.  The release audit additionally fixes the
operator, all-order trace formula, positive control, complete progress record,
and related key schemas in the independent checker; the manuscript now reports
the resulting 71 assertions and 35 registered repaired-hash mutations.

All versions are two pages. Two fresh fixed-epoch builds are byte-identical to
the checked-in final PDF; every font is embedded; the final logs contain no
warning, overfull or underfull box, or undefined reference. Both rendered pages
were inspected without clipping, collision, truncation, or broken mathematics.
