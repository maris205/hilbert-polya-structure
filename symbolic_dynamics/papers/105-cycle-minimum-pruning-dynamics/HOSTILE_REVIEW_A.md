# Cross-hostile review A — P105

Date: 2026-08-29 UTC.  Reviewer role: independent of the P105 author.

Verdict: **internal GO / external HOLD**.  There is no mathematical
CRITICAL or MAJOR finding.  The iterate normal form, transient census, and
one-step fibre theorem survive reconstruction, including `n=1,2,3` and the
transposition branch.  A specialist direct-owner search remains a
release-only MAJOR gate.

## Scope and method

The review reconstructed the labelled map from predecessor/successor arrows,
then separately attacked:

1. the exact iterate and absorption-depth quantifiers;
2. the unique recurrent point, all iterate-fixed counts, M\"obius ledger, and
   formal zeta;
3. the restricted-cycle EGF and the independent cycle-containing-1
   recurrence;
4. the threshold matching, cyclic insertion multiplicity, and unmatched
   involution factor in every one-step fibre; and
5. owner subtraction, the P100 collision boundary, control independence, and
   the compiled artifact.

## Hostile findings

### CRITICAL

None.

### MAJOR

No mathematical or reproducibility defect.

One **release-only owner gate** remains.  Classical permutation-cycle
enumeration, longest-cycle laws, deletion-consistent structures, and
Artin--Mazur zeta are correctly attributed.  The bounded search did not find
the same simultaneous labelled surgery or its inverse-fibre formula, but it
is not an exhaustive owner certificate.  The existing HOLD language is the
correct treatment, so no source repair was needed.

### MINOR

None requiring repair.

## Formula-by-formula reconstruction

- Each original cycle loses exactly its next-smallest surviving label per
  step, with cyclic order inherited.  A length-`ell` cycle therefore finishes
  after `ell-1` steps, and parallel processing makes the total depth
  `L(pi)-1`.  This includes `n=1` and the single transposition at `n=2`.
- Away from the identity, at least one new fixed label is created and no fixed
  label is destroyed.  Hence no nonidentity state can be periodic; every
  iterate has one fixed point and the zeta is exactly `(1-z)^(-1)`.
- `tau<=t` is equivalent to all cycle lengths being at most `t+1`.  Adjacent
  subtraction yields the layer formula.  Exposing the cycle containing label
  1 gives the stated coefficient `(n-1)!/(n-j)!`, independently of the EGF.
- Depth `n-1` consists of all `n`-cycles.  For `n>=3`, depth `n-2` consists of
  one `(n-1)`-cycle and a singleton, giving `n(n-2)!`; the excluded `n=2`
  endpoint is necessary and is stated.
- For a nontrivial output cycle `B_i`, its source minimum must be a distinct
  fixed output label below `min(B_i)`.  Ordering the thresholds makes all
  earlier selections eligible for every later cycle, hence the exact factor
  `e_i-i+1`.  Inserting the selected minimum into a directed edge gives
  `|B_i|` choices.  Every unmatched fixed label is either a source singleton
  or belongs to a source transposition, which is exactly an involution on the
  unmatched set.  These choices are bijective and nonoverlapping.
- P100 erases valuation digits on changing arithmetic coordinates.  P105
  preserves `[n]`, operates in parallel on permutation cycles, and has a
  threshold-matching inverse graph; the systems and proof engines do not
  collide.

## Reproducibility and PDF gate

- Fresh exact control: **PASS**, 17,219,241 assertions.
- Stored stdout comparison: byte-for-byte **PASS**.
- Literal range: every state of `S_1` through `S_9`, 409,113 permutations.
- Fibre formula checked at all 409,113 output states; recurrence extended
  through `n=50`; temporal M\"obius/zeta ledger checked through period 60.
- Four stages: **PASS** (`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`).
- PDF: 5 A4 pages, 331,181 bytes, PDF 1.5.
- Final log: zero undefined citations/references, package warnings,
  multiply-defined labels, or over/underfull boxes.
- Fonts: 24/24 embedded, subsetted, and Unicode-mapped.
- All five rendered pages visually inspected: **PASS**.

## Actual repairs

None.  The current source, bibliography, and evidence ledgers already match
the proved theorem scope.  This review adds only the independent audit
ledger.

## Residual risk

The exact labelled pruning rule or fibre formula could have a direct owner
outside the bounded search.  This is an external-release question, not a
mathematical defect.  Public posting, submission, contact, novelty, and
priority language remain **HOLD**.

## Post-A chronology note

Review B subsequently corrected only the semantics of the control counter:
the 1,981,326 quantity is repeated trajectory-step evaluations, not distinct
functional-graph edges.  That wording repair changed neither a theorem nor
the 17,219,241 assertion total.  It regenerated the current PDF at 331,334
bytes; the A-pass value 331,181 bytes above is a historical checkpoint.  See
`HOSTILE_REVIEW_B.md` for the final cross-hostile metrics.
