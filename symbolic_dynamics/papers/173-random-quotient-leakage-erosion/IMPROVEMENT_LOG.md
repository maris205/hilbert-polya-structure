# Improvement log — P173

## Author Round 0

- PDF: 3 pages, SHA-256
  `d876f022bdc1e04ec57b0f9438db78b1f84abb1691c61dbd78d53083df48d359`.
- Author verifier: 13,279 assertions, `RESULT PASS`, but its Jordan loop did
  not yet include the degenerate `n=0` inventory.

## Hostile Review A and Round 1

Review A returned `0 Critical / 2 Major / 2 Minor`; the quotient-kernel
fibre, every-time lift, spectrum, transient Jordan ladder, and absorption
core survived its independent 36,390-assertion RREF/annihilator control.

- `P173-A-M01` repaired: the abstract, theorem, proof, boundaries, QA, and
  author verifier now state one `J_1(1)` at `n=0`; for `n>=1`, the constant
  right vector and full-dimension indicator prove two semisimple endpoint
  blocks.
- `P173-A-M02` repaired: Fulman--Goldstein owns the uniform rectangular law;
  Balakin is accurately limited to sparse/nonuniform background;
  Goldman--Rota owns Gaussian enumeration; fixed-kernel symmetry and the
  ambient lift are zero-credit standard steps.
- `P173-A-m01` repaired: the visible `q^{,n-a}` typo is `q^{n-a}`.
- `P173-A-m02` repaired: P109, P162, P165, and P168 have a four-row
  carrier/engine/nontransfer firewall.
- The repaired author verifier passes 13,307 assertions.
- Round-1 PDF: 4 pages, 304,997 bytes, SHA-256
  `1a66075c7d64ae943cbbd42503b81964ea7fabe85e2ee7515001a052aa5cce22`.

Review A subsequently accepted all four repairs by a read-only delta audit;
the 13,307 author and 36,390 reviewer assertions replay byte-identically.

## Hostile Review B, Round 2, and final closeout

Review B returned `0 Critical / 2 Major / 1 Minor`; all mathematical claims
survived 9,995,101 independent projective-incidence assertions.

- `P173-B-MAJ-01` implemented: Evans's dimension precursor and Van Peski's
  labelled square-kernel/fixed-target injection chain are cited and assigned
  zero credit.  Their `a -> a` codomain is distinguished from P173's fixed-
  ambient `a -> n-a` schedule and complementary resonance.
- `P173-B-MAJ-02` implemented: P172 is reciprocally subtracted across the
  package; the shared fresh-map/nesting/quotient/labelled/Jordan/absorption
  shell earns zero separation credit.
- `P173-B-MIN-01` implemented: the all-time proof now uses an unconditional
  measure-preserving conjugation bijection of complete histories, including
  zero-mass layers.

Round-2 PDF: 4 pages, 333,340 bytes, SHA-256
`01235b8279d922b0d120f869f32ef8be1ee6aea105dafbc5ea25155be1ef039c`.
Reviewer B subsequently accepted all three repairs by a read-only delta
audit, leaving `0 Critical / 0 Major / 0 Minor` open.

Two independent temporary directories, each initially containing only
`main.tex` and `references.bib`, reproduced that PDF byte for byte; all eight
command logs are preserved as `final_cold_a_*` and `final_cold_b_*`.  Fresh
author, Review-A, and Review-B replays matched their canonical transcripts at
13,307, 36,390, and 9,995,101 assertions.  Font, anonymity, visible-hold,
four-page, marker, and metadata QA passed.  The 53-entry non-self
`SHA256SUMS` verifies.  Final status is
`DUAL_REVIEW_CLOSED / SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL`.
