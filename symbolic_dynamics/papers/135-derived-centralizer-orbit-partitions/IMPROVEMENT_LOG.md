# Paper improvement log — P135

## Round 0

The anonymous five-page note froze the wreath-product local rule, tagged
transient theorem, complete recurrent decoder and OGFs, and every-target
coefficient fibre.  The immutable `main_round0_original.pdf` and the
7,130,840-assertion paper-local verifier passed the initial gate under
`HOLD_EXTERNAL`.

## Round 1 — implementation of Hostile Review A

Review A returned critical 0 and major 0, with three minor repairs:

- `P135-A-m1`: equations (8)--(9) now explicitly use the empty-partition
  bookkeeping convention `f_0=1`, `c_0=0`.
- `P135-A-m2`: recurrent states and `tail(lambda)` are now defined before the
  main theorem, with tail equal to the least entrance time into a cycle.
- `P135-A-m3`: the claims and planning ledgers now point to equations (8)--(9),
  Theorem 4.1, and the actual unnumbered Section 4 proof.  The finite-control
  prose was moved before its table so the float can no longer splice the
  ownership paragraph.

These changes define boundaries and repair traceability/layout; they do not
enlarge the theorem contract or modify the verifier.  Fresh verifier stdout
matched the canonical transcript byte for byte.  An isolated four-stage build
reproduced `main.pdf`; it is byte-identical to `main_round1.pdf`, five A4
pages and 395,335 bytes, with SHA-256
`dbf3a7ff19d1ddd2bcde59b35287835ffa8dec3b4244c53e65e87fc14a2b1b94`.
The immutable round-zero hash remains
`7cd8a811a9d879e303c3d7a0b1bd6631aa24d9fc64704df62b4a369ce327505b`.
Page 5 was visually rechecked and the former table splice is gone.

## Round 2 — implementation of Hostile Review B

Round B independently passed the complete theorem package and every Round-A
repair, returning no critical or major finding.  Its sole minor,
`P135-B-m1`, observed that `CONTROL_RESULTS.md` left the historical Round-0
`main.tex` hash under an unqualified heading.  The ledger now labels that
block as immutable Round 0 and separately pins the current Round-1 source,
control files, `main.pdf`, and `main_round1.pdf`.  Fresh `sha256sum` checks
match every listed value.  This is a provenance-only repair: no manuscript,
formula, verifier, canonical transcript, bibliography, or PDF byte changed.
External status remains `HOLD_EXTERNAL`; no Git action was taken.

The independent closure addendum changed the final Round-B count to critical
0, major 0, minor 0 and `GO_INTERNAL / HOLD_EXTERNAL`.  `main_round2.pdf` is
the support-only sign-off copy, byte-identical to `main.pdf` and
`main_round1.pdf` with SHA-256
`dbf3a7ff19d1ddd2bcde59b35287835ffa8dec3b4244c53e65e87fc14a2b1b94`.
