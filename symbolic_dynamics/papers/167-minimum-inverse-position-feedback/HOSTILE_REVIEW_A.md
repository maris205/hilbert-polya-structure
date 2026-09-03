# Hostile Review A — Minimum Inverse-Position Feedback

**Role:** coordinator-side independent Review A; the proof was rederived from
the literal definition before consulting the author verifier.  
**Frozen input:** anonymous Round 0.  
**Decision:** `MINOR_REPAIR`.  
**Findings:** `0 Critical / 0 Major / 1 Minor`.  
**Lifecycle:** `HOLD_EXTERNAL`.

## Pinned Round-0 artifact

```text
01d2bded0a4457e95f677543227a213dc07057d8e1b8273786e5f7aa3f8606e4  main.tex
4286e4273768a76d295904a91caa1384cfcb11c6fc9157afe9fe8ddd3140a2b6  references.bib
81bfa2ed4944f2750558f06cbb3a09d7081fc0361a0361f05f91869368faf379  main_round0_original.pdf
b7c10bd3738362397a97361ca3780c4f53c7297efbe3e1885175634b345b457b  verify_p167.py
1e7348f9eab389cffc14582b3cf26ebeec69cb72a6c77dbdb1fb204abd1e1a8c  verification_output.txt
```

The frozen PDF and the then-current `main.pdf` were byte-identical.  The
review did not modify the Round-0 PDF.

## Independent mathematical attack

Starting from

\[
 (\mathcal M_n f)(i)=\min f^{-1}(i)
\]

for a present symbol and the identity value `i` for an absent symbol, the
following claims were rederived.

- Distinct present symbols have distinct first positions.  Consequently a
  first image has indegree at most one away from loops, hence consists only
  of directed cycles and loop-rooted paths.  Directly listing occurrences on
  a path gives exactly the stated reverse-or-split rule; no component can
  merge under a later update.
- The path clock recurrence is complete: an ascending root comparison costs
  one step and deletes the root, while a descending root comparison on a
  nonrecurrent path costs two steps and deletes the old leaf.  This proves
  the `2s-2` ceiling and its unique decreasing-order equality case.
- Every first image contains value zero, excluding the unique full-label
  decreasing path.  The displayed source
  `(1,2,...,n-1,1)` maps to the increasing path and realizes the two sharp
  carrier clocks `2n-2` and `2n-3`, including `n=2`.
- The recurrent connected census separates cycles from paths.  For
  `s>=4`, the two endpoint inequalities occupy disjoint position pairs and
  independently quarter the `s!` orders.  The special `s=1,2,3` values and
  the labelled-set exponential generating function follow.
- Cycle inversion and path reversal leave only singleton loops and
  two-cycles fixed.  Thus fixed states are involutions, every recurrent
  period divides two, and the odd/even fixed-iterate and zeta formulas are
  valid.
- In the fibre formula, off-diagonal target coordinates force distinct
  first positions; a diagonal coordinate is either absent or first opened at
  itself.  Once these choices are made, every unforced source position may
  independently use exactly the already-opened symbols.  This proves the
  product for every target, including unsupported targets.
- For a fixed kernel partition of a source, the target determines each block
  label uniquely.  There is therefore at most one source per partition; all
  partitions occur over the identity target by minimum-block labelling.  The
  Bell ceiling is exact without requiring uniqueness of the maximizer.

No missing boundary, reversed inequality, unsupported converse, or theorem
overstatement was found.  In particular, the first-image off-diagonal
injection is used only as a necessary structural condition; the fibre
formula supplies the exact support test.

## Findings

### Critical

None.

### Major

None.

### Minor

**M1 — Proceedings publication year.**  The Round-0 BibTeX entry for
Flajolet--Odlyzko records `year = {1989}`.  `EUROCRYPT '89` is the conference
designation, but the Springer chapter metadata for DOI
`10.1007/3-540-46885-4_34` records publication in 1990 in LNCS 434.  Change
the bibliographic year to 1990 and make the source-verification ledger
explicit about the conference/publication-year distinction.  This is a
metadata-only repair and does not touch a mathematical claim.

## Exact-control replay

A fresh process ran the frozen standard-library verifier and was compared
byte for byte with `verification_output.txt`.  The comparison returned zero.
The replay retains the author hashes above and reports `12,603,676` exact
assertions.  The proof assessment does not infer the uniform theorem from
this bounded enumeration; the replay is a hostile falsification control.

## Ownership and scope

The manuscript correctly assigns zero contribution credit to least kernel
transversals, first-occurrence/RGF encodings, functional-digraph language,
Bell and involution numbers, labelled-set calculus, and the Artin--Mazur
conversion.  The bounded literal-owner non-hit supports only the internal
`GREEN_OWNER_THIN` routing label.  It does not establish novelty, priority,
or clearance to circulate.

## Recommendation

Apply M1, rebuild from clean sources, and retain this review with the frozen
Round-0 PDF.  Subject to that repair, the theorem package is suitable for
Review B.  External status remains `HOLD_EXTERNAL`.
