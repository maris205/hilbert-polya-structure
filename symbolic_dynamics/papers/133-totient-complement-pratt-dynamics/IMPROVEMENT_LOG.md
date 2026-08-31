# Paper improvement log — P133

## Round 0

The anonymous three-page note froze the support conjugacy, source-phase
decoder, exact recurrent census, nonsharp `h+1` entry bound, and every-target
inclusion--exclusion fibre formula.  Its paper-local verifier and immutable
`main_round0_original.pdf` passed the initial reproducibility gate under
`HOLD_EXTERNAL`.

## Round 1 — implementation of Hostile Review A

Review A found no critical or major issue and one minor package-integrity
issue (`P133-A-m1`): the planning and claims ledgers cited theorem numbers
that do not exist in the manuscript.  Both ledgers now point to the actual
proof objects:

- Proposition 2.1 for the arithmetic support conjugacy;
- equations (6)--(7), Lemma 3.1, and the completeness/census paragraphs after
  Proposition 3.3 for the source-phase recurrent decoder;
- Lemma 3.2 and Proposition 3.3 for the two-step erasure and entry bound; and
- Theorem 1.1(iv) plus Section 4 for every-target fibres.

No theorem, formula, bibliography entry, verifier, canonical output, or PDF
source changed.  Round 1 is therefore a support-only traceability repair.
Fresh verifier stdout matched the canonical transcript byte for byte, and an
isolated four-stage build reproduced the reviewed PDF.  `main.pdf`,
`main_round0_original.pdf`, and `main_round1.pdf` are byte-identical, three
A4 pages and 346,509 bytes, with SHA-256
`bbb869d485230bc0165bbe49ff43929de61700c1e0acc960a541b64b23651d7b`.
Round B independently reconstructed the support conjugacy, source-phase
decoder, simultaneous `h+1` entrance, recurrent census, and every-target
fibre formula.  It returned critical 0, major 0, minor 0 and
`GO_INTERNAL / HOLD_EXTERNAL`.  No Git action was taken.

`main_round2.pdf` is the review sign-off copy.  It is byte-identical to
`main.pdf`, `main_round1.pdf`, and `main_round0_original.pdf`, with SHA-256
`bbb869d485230bc0165bbe49ff43929de61700c1e0acc960a541b64b23651d7b`.
