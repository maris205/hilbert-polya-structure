# Improvement log

## Round 0 — proof-contract manuscript

- Defined the fixed-cut synchronous map without unrooted/canonical language.
- Implemented the independent gate's required four-step sibling inverse:
  forward localization, converse section construction, connected decoration
  and mutual inversion.
- Added the exact pointwise fibre product and strict unique-max proof.
- Made `n=0`, the virtual root and the formal-OGF boundary explicit.
- Corrected the uncrossing attribution to Thomas Lam.
- Zero-credited Igusa parallel parts, Alman--Lian--Tran A111088,
  Flajolet--Noy, Nabergall, Acan, Callan, Kreweras and Lam individually.
- Added a paper-local verifier that independently rebuilds every source
  through seven chords: 735,609 assertions, canonical byte comparison PASS.
- Built and froze `main_round0_original.pdf` (4 pages).

At the round-zero freeze, Independent Review A and Review B were pending.
External status was `HOLD_EXTERNAL`.

## Round 1 — Hostile Review A repair

- Replaced the ambiguous comparable-parent sentence in Theorem 2.1, Step 1:
  if `p_i` lies strictly inside a distinct `p_j`, then `p_i` is a strict
  intermediate container between `x_j` and its alleged immediate parent
  `p_j`.
- Replaced the false uniform-gap sentence in Step 2 by the exact two-case
  lemma.  A selected child's descendant interval is a gap of `B_Q`; an
  unselected child's closed support is a strict subinterval of one gap.
- Made endpoint coverage/disjointness explicit and closed the leaf-to-root
  induction across distinct child intervals and again at the virtual root;
  no partition blocks merge or alternate across nesting levels.
- Identified every matching sibling list as an exact specialization of
  Igusa's parallel sets (Definition 1.7) and zero-credited the compatible
  merge criterion (Proposition 1.8), rather than calling the relation merely
  “close.”
- Added the Alman--Lian--Tran all-size identification and theorem locators:
  Theorem 4.1.6, Remark 4.1.7, Theorem 4.1.8 and Theorem 4.2.1.
- Synchronized the claim, narrative, plan, build and README records with the
  actual repairs.  The verifier and bibliography remain unchanged.
- Fresh canonical comparison passed with 735,609 assertions.  An isolated
  four-stage build produced the byte-identical `main.pdf` and
  `main_round1.pdf` (4 A4 pages); the settled warning, bibliography, font,
  metadata and all-page visual checks passed.

Review A is repaired in source; Review B is still pending.  External status
remains `HOLD_EXTERNAL`.

## Round 2 — Hostile Review B closure

- Preserved Review B's independent disposition: 0 CRITICAL, 0 MAJOR and
  2 MINOR findings, with `GO_INTERNAL / HOLD_EXTERNAL`.
- Closed B1 by restricting the exact Igusa parallel-set specialization to
  nonempty immediate-sibling lists, including a nonempty top-level list.  A
  degree-zero child list is now explicitly only the singleton `A_0=1`
  bookkeeping factor and is not identified with a parallel set.
- Closed B2 by describing P110 literally as cyclic partition shift--join
  dynamics, while retaining the narrower shared chord witness only as a
  firewall observation.
- Synchronized the README, claim table, narrative, plan, control and build
  records without changing the verifier, canonical transcript or references.
- Fresh canonical comparison passed with **735,609 assertions**.  Both the
  local and isolated four-stage builds passed; the isolated directory began
  with only `main.tex` and `references.bib`, and its settled PDF is
  byte-identical to local `main.pdf` and `main_round2.pdf`.
- Inspected all four rendered pages.  The settled log, bibliography, font,
  metadata, attachment and anonymity checks passed.

The round-two source has SHA-256
`70f020aa1b89353b94f76b781bee19e6c6fbc2d56824431d95090e3e4fcb033a`.
The 4-page, 346,056-byte round-two PDF has SHA-256
`c5a4fd3976a733c62a7f8f4e90b773cc6300970b9a25ac95b33f68a491f9c3fa`.
All internal review findings are closed: `GO_INTERNAL`.  External status
remains `HOLD_EXTERNAL`.
