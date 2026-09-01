# Improvement log — P150

**Status: ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL.**

## Baseline

The round-zero package proved a complete functional-graph classification for

```text
L(x,y)=(y,(1+y)inv0(x)),  inv0(0)=0,
```

on the affine plane over every odd finite field.  It contained the five
strata, sharp tail polynomial, complete cycle/zeta census, every-target fibre
law, and distinguished in-tree.  The own-author proof, verifier, build, and
visual checks passed, but the source ledger and two proof-boundary explanations
still required independent hostile-review hardening.

Historical round zero is preserved as `main_round0_original.pdf`: 5 pages,
396,310 bytes, SHA-256
`d94b53e9a1e496c766e8770e88f588053b7333e702b08177f0647578f90d274d`.

## Hostile Review A

**Verdict:** ACCEPT WITH MINOR REPAIRS — 0 Critical / 0 Major / 2 Minor.

1. **Owner-ledger replayability.**  Exact query families and candidate
   exclusions were needed, together with explicit primary-source subtraction
   of Lyness (1942) and Kanki (2013).
2. **Orbit integrality and boundaries.**  The proof needed to say that
   nonfixed generic states partition into five-element orbits and to expose
   the `q=3` and characteristic-five boundary cases.

Review A found no false theorem, missing graph branch, build failure, or
direct same-object owner.  External status remained `HOLD_EXTERNAL`.

## Implemented round-one repair set

- Added seven replayable owner-query families with databases/lanes,
  candidates, and exclusion reasons.
- Added and verified the Lyness 1942 primary record for the rational
  five-cycle; assigned the classical rational core zero credit.
- Added and verified Kanki 2013 for the distinct extended-state/
  almost-good-reduction treatment; expressly distinguished it from
  `inv0(0)=0`.
- Replaced bare division by five with the literal partition of nonfixed
  generic states into disjoint five-element `L`-orbits.
- Added the `q=3` empty-generic boundary and the characteristic-five
  double-root boundary, including the `q=5` census.
- Rebuilt with 5/5 primary references cited and resolved.

The repair changed no theorem statement.  It produced the current
5-page, 403,358-byte artifact, frozen as `main_round1.pdf` and byte-identical
to `main.pdf`, with SHA-256
`26d0a73adb71b2e303ea637b5874939914cffd53f09a2230ded5775484c33dca`.

## Hostile Review B

**Score:** 0 Critical / 0 Major / 1 Minor — **REVISE**.

Review B independently closed both Review-A items.  It rederived all theorem
interfaces and boundary cases, replayed the owner search, cold-ran 2,144,131
exact assertions to a byte-identical transcript, produced two byte-identical
isolated source-only builds, and visually accepted all 5/5 pages.

Its sole finding was a provenance defect in `FINAL_QA.md`: that Markdown file
still presented the round-zero size/hash, three-reference count, and absence
of hostile reviews as the current package state.  The underlying current PDF,
proof, sources, verifier, transcript, and build evidence were already correct.

## Implemented post-B closure

- Recast `FINAL_QA.md` as the current round-2 internal QA record while
  preserving round-zero values explicitly as historical provenance.
- Recorded 5/5 references, both hostile reviews, both isolated builds, and
  5/5-page visual acceptance.
- Added `HOSTILE_REVIEW.md` to consolidate A, B, repairs, and the final credit
  ceiling without altering the original review records.
- Unified `README.md`, `NARRATIVE_REPORT.md`, `CLAIMS_EVIDENCE.md`,
  `PAPER_PLAN.md`, `BUILD.md`, and `FINAL_QA.md` under the status
  `ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL`.

This closure is Markdown-only.  It does not modify `main.tex`,
`references.bib`, `verify_p150.py`, `verification_output.txt`, any PDF, or
`SHA256SUMS`.

## Final claims subtraction

Zero credit is assigned to the classical Lyness recurrence and five-cycle,
QRT/cluster/integrability interpretations, generic finite-field rational-map
methods, projective denominator conventions, Kanki's distinct regularisation,
and generic functional-graph/zeta bookkeeping.

Only this conjunction survives for internal scoring:

```text
literal inv0(0)=0 all-affine five-stratum scheduler
+ exact tail/cycle/zeta classification
+ every-target 0/1/q fibre and image law
+ complete singular in-tree.
```

The owner search is bounded and non-certifying.  Its non-hits prove neither
novelty nor release freedom.

## Round-2 internal freeze record

- Current accepted `main.pdf`: 5 A4 pages, 403,358 bytes.
- SHA-256:
  `26d0a73adb71b2e303ea637b5874939914cffd53f09a2230ded5775484c33dca`.
- Exact control: 2,144,131 assertions, canonical byte-identical PASS replay.
- Bibliography: 5/5 cited and resolved.
- Reproducibility: two isolated source-only builds byte-identical to current
  `main.pdf`.
- Visual QA: 5/5 pages accepted.
- `main_round2.pdf`: separately frozen by root during this closure; a
  read-only comparison confirms 403,358 bytes and byte identity with current
  `main.pdf` at the accepted digest; not created or modified here.

Internal review is accepted.  No statement in this log authorizes Git,
external posting, specialist contact, submission, novelty/priority claims, or
release; status remains `HOLD_EXTERNAL`.
