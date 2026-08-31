# P135 hostile review — Round A

**Manuscript:** *Derived-Centralizer Orbit Partitions: Tagged Transients,
Recurrent Types, and Exact Fibres*  
**Review date:** 2026-08-31 UTC  
**Reviewer role:** independent hostile reviewer; no participation in the
round-0 draft  
**Calibration:** `NOT_CALIBRATED`; `criteria_binding_unavailable`, so this
report makes no venue-fit claim  
**External status:** `HOLD_EXTERNAL`  
**Verdict:** **`REPAIR`** — the wreath rule, tagged theorem, recurrent atlas,
generating functions, and fibre coefficient survive; three boundary/
traceability repairs are required before Round B.

Severity summary: **CRITICAL 0; MAJOR 0; MINOR 3**.

## 1. Frozen snapshot and reproducibility

I reviewed the complete round-0 source, bibliography, paper-local verifier,
canonical stdout, narrative/evidence files, build record, settled LaTeX
artifacts, and all five PDF pages.  I did not modify the manuscript,
bibliography, verifier, canonical transcript, or PDF.

| artifact | SHA-256 at review |
|---|---|
| `main.tex` | `386b0cbca5cf812599687df39e3db43ee0edb47cb500f7718742b9badf0cb273` |
| `references.bib` | `515faec4ab071ecf7c68bf65c5bb721867eeea912ef30a57c7b41f9e4402baae` |
| `code/verify.py` | `26b87846c87dd671f709f90e9945f5724b3f6deac959f2619a73078721f0313a` |
| `code/verification_output.txt` | `be50b73c6c3c17c6378d141bc6c594388512241b8acb9b6e7b877b470070ba90` |
| `main.pdf` | `7cd8a811a9d879e303c3d7a0b1bd6631aa24d9fc64704df62b4a369ce327505b` |
| `main_round0_original.pdf` | `7cd8a811a9d879e303c3d7a0b1bd6631aa24d9fc64704df62b4a369ce327505b` |

Fresh replay of `code/verify.py` matched the frozen stdout byte for byte
(`cmp=0`) in 21 seconds and reported 7,130,840 exact assertions.  The tested
surfaces include every partition through weight 45, every target through
weight 30, literal derived groups in 18 wreath cases, and every reachable
tagged state through weight 30.

I also ran a separate implementation that did not import the paper code.  It
exhausted all 1,596 partitions and target cells through weight 18, constructed
the recurrent classes from the four displayed templates rather than from a
recognizer, compared every literal fibre with an independent multiplicity
product, and followed 3,377 reachable tagged states through weight 16.  All
1,791 two-clean pairs returned after two steps.  The run made 22,731 exact
assertions and ended `STATUS=PASS`; its maximum observed tail was four.

A fresh four-stage isolated build from only `main.tex` and
`references.bib` produced a PDF byte-identical to the frozen artifact.  It
has five A4 pages and 394,566 bytes.  The settled log has no actionable
warning, undefined citation/reference, or bad box.  All 31 font rows are
embedded, subsetted, and Unicode-mapped; metadata fields are blank and the
visible author is `Anonymous`.  Extracted text is searchable.  Visual
inspection of all five pages found no clipping, collision, bad glyph, or
malformed formula.  The control table at the top of page 5 interrupts the
last ownership paragraph; this is readable and only an editorial risk.

## 2. Hostile reconstruction of the theorem

### 2.1 Wreath-product local rule — survives every threshold

For the `m` cycles of length `j`, the centralizer factor is
`C_j^m semidirect S_m`.  The coordinate-sum and sign maps put the derived
group inside `B_0 semidirect A_m`.  Commuting a base coordinate with a
transposition gives all coordinate differences and hence all of `B_0`;
top commutators give `A_m` for `m>=3` and the trivial group for `m=2`.
Thus the displayed derived subgroup is correct.

On natural points, `B_0` is transitive inside each block whenever `m>=2`.
For `m=2` there is no top motion, leaving two `j`-orbits; for `m>=3`,
`A_m` is block-transitive, including `A_3`, leaving one `jm`-orbit.  The
boundaries `m=1`, `m=2`, and `j=1` all agree with

\[
 j^m\mapsto 1^j,\quad j^2,\quad jm.
\]

The direct-product passage to all occupied cycle lengths is valid because
the factors act on disjoint point sets.

### 2.2 Whole/split tags and the crossing potential — survive

A current tag is a block of the initial-tag partition.  It is represented
either once as a whole part of its mass or by that many singleton copies.
For a merge at size `j>=2`, every participating tag is a distinct whole tag
of mass `j`; at size one, each split tag occurs exactly its mass many times.
Therefore the merged output has exactly the mass of the tag union.  Splits
and multiplicity-two preservation do not alter the tag partition, while a
merge of at least two distinct tags strictly coarsens it.  The asserted
potential is consequently well-defined and monotone on all reachable lifts.

Reachability is used correctly in the two-clean normal form.  After one
clean step, non-singleton parts are dimers plus at most one whole oscillator.
Cleanliness of the next step forces a singleton sector of size at least
three to be one split tag, hence there is at most one split oscillator.
An unpaired `H_2` cannot be created after time zero, which blocks the only
delayed two-singleton residue that could coexist with an oscillator.  The
same-size-dimer exclusions prevent a hidden crossing in either adjacent
transition.  The remaining pieces therefore swap whole/split phases and
return after two steps.

### 2.3 Period and nonsharp tail boundary — survives

There are initially `ell(lambda)` tags and at most `ell(lambda)-1` crossing
transitions.  If two consecutive transitions are clean, their intermediate
reachable state lies on a tagged, hence uncoloured, cycle of period at most
two.  Before the recurrent part, every disjoint pair of transitions must
therefore contain a crossing.  This proves the advertised safe bound

\[
              \operatorname{tail}(\lambda)\le 2\ell(\lambda)\le2n.
\]

The proof could squeeze an off-by-one improvement, but the manuscript
explicitly declines a sharp-clock claim; the weaker displayed inequality is
valid.  The observed maximum tail six through weight 45 is correctly kept
as falsification evidence and is not promoted into an all-weight statement.

### 2.4 Recurrent classes and ordinary generating functions — survive

Along a recurrent uncoloured orbit, the lifted tag partition can coarsen
only finitely many times.  Once it stabilizes, every consecutive pair is
clean, so the normal form applies at every phase.  Projection gives exactly:

- fixed dimers plus a residue `1^e`, `e=0,1,2`;
- one whole/split oscillator of amplitude `a>=3`;
- two opposite-phase oscillators, fixed when their amplitudes agree and a
  strict two-cycle when they differ.

The exclusion of dimers at oscillator amplitudes is necessary and present.
Direct substitution proves the converse.  The dimer product
`D(q)=product_(j>=2)(1+q^(2j))`, the residue factor, and the exclusions in
`D_A` then give the two displayed generating functions without overlap or
double counting.  In particular, unequal amplitudes are counted once by
`a<b`.

### 2.5 Every-target coefficient — survives

For each source multiplicity `m_j`, the four mutually exclusive choices
contribute

\[
 1,\qquad z^j x_1^j,\qquad z^{2j}x_j^2,\qquad z^{jm}x_{jm}\ (m\ge3).
\]

Multiplicities at distinct sizes are independent coordinates of a source
partition.  The `z^n` extraction fixes source weight and the target monomial
records the complete output multiplicity vector.  Consequently every source
is counted exactly once and an out-of-image target has coefficient zero.
The terms of weight greater than `n` that remain in individual finite
factors are harmless because `[z^n]` removes them.

## 3. Critical and Major findings

**None.**  I found no counterexample or proof break in the local group rule,
tag invariant, two-clean lemma, recurrent classification, OGF transfer, or
all-target coefficient formula.

## 4. Minor findings

### `P135-A-m1` — `f_0` and `c_0` are used without a boundary convention

The theorem is stated for `n>=1`, but equations (8)--(9) sum from `n>=0`.
Their right-hand sides have constant terms `1` and `0`, respectively, while
`f_0` and `c_0` have not been defined.

**Evidence anchor:** equation: Theorem 1.1(iv), equations (8)--(9), lower
summation limits and constant terms.  
**Severity:** Minor.  
**Confidence:** 5/5 — formal-series boundary check.

**Required repair:** either state immediately before (8) that, for the
generating functions, `f_0=1` and `c_0=0` by the empty-partition convention,
or start both sums at one and subtract the fixed-series constant term.  Do
not silently leave the coefficient undefined.

### `P135-A-m2` — `tail(lambda)` is never defined

The theorem and proof use `tail(lambda)`, but the manuscript does not state
whether this is the least entrance time to the recurrent set, the
preperiod length in a first-repeat convention, or something else.  The
proof clearly intends the first meaning.

**Evidence anchor:** absence: Section 1 before equation (3) — expected a
definition of `tail`; checked the abstract, theorem preamble, Section 3, and
notation declarations.  
**Severity:** Minor.  
**Confidence:** 5/5 — complete source search.

**Required repair:** define `tail(lambda)` as the least `t>=0` for which
`T^t(lambda)` is recurrent.  State that recurrent means lying on a directed
cycle of this finite self-map.  This also makes the zero-tail fixed and
two-cycle boundary explicit.

### `P135-A-m3` — one evidence locator and one page break need editorial repair

`CLAIMS_EVIDENCE.md` and `PAPER_PLAN.md` call the generating-function proof
“Corollary 4.2,” but no such corollary exists in the frozen source; it is an
unnumbered proof following Theorem 4.1.  Separately, Table 1 floats to the
top of page 5 between the two parts of the final ownership/control
paragraph.  Neither issue affects a formula, but the former breaks claim
traceability and the latter makes the final scope paragraph look
accidentally spliced.

**Evidence anchor:** absence: Section 4 and the two evidence ledgers —
expected a `Corollary 4.2` declaration; checked theorem declarations and
the generating-function proof.  
**Severity:** Minor.  
**Confidence:** 5/5 — source/PDF comparison.

**Required repair:** point C5 and the plan matrix to “equations (8)--(9),
Theorem 4.1, and the unnumbered generating-function proof in Section 4,” or
promote that proof to an actual corollary.  Then keep Table 1 with its
introducing control paragraph or move it after that paragraph; rebuild and
inspect page 5.

## 5. Scope and owner boundary

The manuscript correctly removes contribution credit for the centralizer
decomposition, generic wreath commutator structure, orbit-partition
language, generic multiplicity dynamics, and formal coefficient extraction.
The internal P113/P123/P105/P110 firewalls are carrier- and mechanism-level
distinctions rather than novelty evidence.  This Round-A review did not
perform a new unbounded novelty search; the bounded owner non-hit remains a
non-hit only.  `HOLD_EXTERNAL` must remain in force.

## 6. Round-A repair checklist

- [ ] Define the `n=0` generating-function convention.
- [ ] Define `tail` and `recurrent` before Theorem 1.1.
- [ ] Repair the C5/plan proof locator.
- [ ] Keep Table 1 with its introducing paragraph and visually recheck page
  5 after the rebuild.
- [ ] Fresh raw verifier replay remains `cmp=0`.
- [ ] Preserve `Anonymous` and `HOLD_EXTERNAL`.

**Round-A disposition:** the mathematical gate passes.  P135 needs only the
listed boundary and editorial repairs before Round B; no theorem or verifier
reconstruction is indicated.
