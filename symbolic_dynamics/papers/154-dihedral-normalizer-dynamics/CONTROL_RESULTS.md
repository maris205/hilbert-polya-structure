# Deterministic control results

Status: `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

Verifier: verify.py
Canonical transcript: CANONICAL.txt
Randomness: none
External packages: none

## Coverage

The paper-local replay audits 44 parameter boxes and four explicit
equal-signature pairs. Total assertions: 29,590.

For each box, every claimed subgroup is an element set. Every normalizer is
computed by ambient element conjugation before it is compared with the
coordinate formula. The resulting literal map drives all depth, fixed,
image, source-mass, and every-target fibre assertions.

Terminal profile:

    PROFILE_SHA256 6eed12ce0c63f2d20f734ac1fa67634ce445140372dfc53e779a389de023b782
    TOTAL boxes=44 iso_pairs=4 assertions=29590
    VERDICT PASS_EXACT_REPLAY

## Additional pressure

An independent rooted-component scan for n from 3 through 500 reported 442
graph classes and 442 signature classes, with no necessity or sufficiency
mismatch. The first collisions include 33/35, 51/55, 66/70, and 69/77.

## Limits

The verifier constructs the theorem carrier and checks uniqueness; subgroup
completeness is proved in the manuscript rather than by enumerating every
subset. The four isomorphism checks use the theorem-coded update, while base
boxes 33 and 35 separately use literal normalizers. Signature necessity is a
proof obligation, not a conclusion from bounded scans.

Hostile Review B cold-replayed the same 29,590 assertions and reproduced the
frozen transcript and five-page PDF. It returned
`ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor`. The subsequent Round-2
font-expansion build fix changes no control code, transcript, theorem, or
proof. The final five-command build has zero warnings and bad boxes; current
and Round-2 are byte-identical at SHA-256
`72b99fe5f4813434cccb3aef9f8a023d0e7ca471029ce9831b4228dfe8db90cd`.
