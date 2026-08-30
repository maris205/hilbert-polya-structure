# P125 improvement log

Status: **ROUND-TWO POST-REVIEW REPAIR COMPLETE / EXTERNAL HOLD**.

This pass implements exactly the two MINOR items in `HOSTILE_REVIEW_A.md`.
No theorem statement, count formula, owner ceiling, bibliography entry, or
release status was changed.

## MINOR A1 — directed-cycle canonicalization

Review issue: `code/verify.py` treated both rotations and reflections of a
cycle-decoration word as identical, although a functional graph has an
oriented cycle and directed-cycle isomorphism preserves that orientation.

Repair:

- `canonical_cycle` now minimizes over cyclic rotations only;
- reflection candidates were removed;
- a three-position asymmetric decoration is compared with its reversal by a
  dedicated assertion, so a future reintroduction of reflection fails the
  verifier immediately;
- the README, claims map, control record, narrative, plan, and manuscript
  control section now state the rotation-only convention explicitly.

Fresh result:

```text
ASSERTIONS 27405887
PASS
```

The fresh transcript is byte-identical to `code/verification_output.txt`.
Every original state, fibre, image, orbit, cycle, and component assertion
still passes; the assertion total increased by exactly one for the new
orientation sentinel.

## MINOR A2 — matrix-word auditability

Review issue: the proof of Theorem 2.2 compressed the pointwise period
calculation into a sentence about multiplying matrix words.

Repair: the proof now displays

```text
A0^2 = I,  A1^3 = I,
A1 A0 = [[1,0],[1,1]],
A0 A1 = [[1,1],[0,1]],
```

notes that both two-step products square to the identity, and gives an
eight-row table.  For each value of the invariant polar bit and each starting
quadratic-bit pair, the table records either the controlling word and its
fixed-pair equation or the exact landing type.  It explicitly derives the
only shortenings `x=y`, `x=0`, and `y=0`, and explains why the `c=1` fixed
possibilities are inadmissible.

Proof status: **PROVABLE AS STATED**.  The theorem and all boundary cases are
unchanged.

## Build and freeze

An isolated directory containing only `main.tex` and `references.bib` was
built by `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.  All stages exited zero;
the final stage has zero errors, undefined references/citations, box warnings,
or rerun requests.  The resulting PDF has 5 A4 pages and 367,956 bytes.  All
five pages were rendered and visually checked; the new table is fully visible
and no clipping, overlap, malformed formula, or unresolved marker appears.
Anonymous metadata and full font embedding were retained.

Freeze hashes:

```text
main.pdf / main_round1.pdf   8dd8ecf6ba49912b5984b5755e8b240cfd97be0d5931e944925e5253469f6d50
main_round0_original.pdf     e9f190aed3d2ac1ec337c7d9133f77d2e17c64f8b18070e74587c6c8397d4368
main.tex                     505a1dd841a5e09c1ab8124634f037d1959d8b6b5812f785752a72c088ceceb9
references.bib               138ccfc9deec2c31fc8fad76c7046b2f3ce6c3b34e2dba3f60f8cd64a39c3017
code/verify.py               57d9770d3054d28e06ab54bf6faab57140b61dd24f3d6e7f4c7c5d70d55ba96c
code/verification_output.txt 484d8734adfd36a5e562a206fc833fa13eb5240f3ebc36c67ad3c02e2b54ceb0
```

At the round-one freeze, `main_round0_original.pdf` was not overwritten and
Review B had not yet been created.  External release remained **HOLD**.

## MINOR B1 — Yang--Baxter notation

Review B confirmed every theorem and both Review-A repairs, with no critical
or major finding.  Its sole minor noted that Remark 2.3 used the letter `R`
in the quantum Yang--Baxter display without defining it.  The remark now says
explicitly `Put R=Phi` before that display.  The two computed sides and the
failure conclusion are unchanged.  This phrase-only repair is frozen in
`main_round2.pdf`; external status remains HOLD.
