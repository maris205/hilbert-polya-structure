# Hostile Review A — P181 first-descent prefix reversal

**Role:** independent algebra/combinatorics reviewer; author files read-only  
**Frozen author baseline:** `main.tex` SHA-256
`090a010f27688156432c863f1b30e2ccf2a44d8ab111a51771ac7b525713439d`  
**Original Round-0 decision:** `MINOR_REPAIR / THEOREM_ACCEPT / HOLD_EXTERNAL`  
**Round-1 delta disposition:** `ACCEPTED / HOLD_EXTERNAL`  
**Current open findings:** `0 Critical / 0 Major / 0 Minor`

## 1. Scope and independent method

I re-read the literal map, the complete five-part theorem and proofs, the
`n=2,3` proposition, author verifier/canonical, claims/evidence, narrative,
plan, source-owner ledger, bibliography, build/self-QA records, PDF metadata,
and the P117/P122/FDF/FAR collision boundary.  I did not compile or modify any
paper file.

The review verifier was written from scratch and imports no author or scout
code.  Its state is an integer factoradic rank rather than a tuple-keyed
permutation.  It builds a flat forward edge array, target-sorts the source
codes, finds the recurrent vertices by indegree peeling, and obtains tail
depths by reverse breadth-first propagation.  Thus it does not reuse the
author's permutation-generator/dictionary/incoming-set/per-orbit
organization.  It also derives and checks the full decreasing-run and fibre
histograms, and implements the Project Euler follower-to-front update as an
independent negative control.  Two fresh processes reproduce `CANONICAL.txt`
byte for byte.

## 2. Independent theorem re-derivation

Let the first descent of a nonidentity word be at position `d`, and reverse
positions `1,...,d+1`.  The first two output values are the reversed descent
pair `pi_(d+1)<pi_d`, so every nonfixed output begins with an ascent.  Conversely,
if `tau_1<tau_2`, then reversing its first two entries makes a source whose
first descent is at position one and which returns to `tau`.  This proves

```text
Im(F_n) = {tau: tau_1<tau_2},       |Im(F_n)|=n!/2   (n>=2).
```

If `tau_1<tau_2>tau_3`, its first descent is two, so the update is `rho_3`.
The partner again has a peak at position two, and a second `rho_3` returns;
distinct entries exclude a fixed point.  An ascent-starting, nonidentity
state that is not a peak starts with three increasing entries.  At its later
first descent `d>=3`, the first three output entries are
`tau_(d+1)<tau_d>tau_(d-1)`, hence it enters the peak core.  This proves the
identity-plus-peak recurrent set and excludes every longer cycle.

For an ascent target `tau`, reversing a prefix of length `k` gives

```text
tau_k,tau_(k-1),...,tau_2,tau_1,... .
```

Its first descent is exactly at `k-1` if and only if
`tau_2>tau_3>...>tau_k`.  Involutivity proves that these are all nonfixed
predecessors, and distinct `k` have distinct first entries.  The identity
contributes its fixed predecessor in addition to `rho_2(identity)`.  The
paper's every-target formula is therefore exact.

As a stronger counting check, if `r(tau)` is the decreasing-run length from
position two, then for `1<=k<=n-1`

```text
#{tau in Im(F_n): r(tau)>=k} = n! k/(k+1)!.
```

Indeed, among the first `k+1` values, position two must contain their maximum;
after choosing the value in position one, the remaining `k-1` values have a
forced decreasing order.  Consecutive differences give the exact run
histogram, and shifting the identity from fibre one to fibre two gives the
whole fibre histogram, including zero-fibre targets.  The independent boxes
verify these identities through `S_9`.

The nonrecurrent image states are exactly the ascent-starting words whose
first three values increase.  Each has run length one and hence the unique
predecessor `rho_2(tau)` outside the image.  This is a bijection from
`I_n\R_n` to depth-two states.  Counting the core, that set, and the remaining
states gives

```text
depth 0 = n!/3+1,   depth 1 = n!/2,   depth 2 = n!/6-1.
```

A run of length `n-1` forces `tau_2=n`; choosing `tau_1` in `[n-1]` forces
the rest in decreasing order.  Hence there are exactly `n-1` fibres of size
`n-1` for `n>=4`.  At `n=3`, the identity's extra fixed predecessor creates
the stated third maximizer.  The complete coded edge arrays are

```text
S_1: [0]
S_2: [0,0]
S_3: [0,3,0,1,1,3]
```

in lexicographic factoradic order, confirming the stated `n=2,3` atlases and
the omitted trivial `n=1` atlas.

## 3. Findings

### Critical

None.

### Major

None.  I found no counterexample to the image, recurrent-core, depth,
predecessor, or maximizer claims, and no hidden period or duplicate inverse.

### P181-A-m01 — The map includes `S_1`, but the smallest boundary is not stated

**Severity:** Minor.  **Locations:** `main.tex`, lines 64--78 and 278--299;
abstract and package documents describing the “exceptional `n=2,3`
atlases.”

The definition is meaningful at `n=1`: the sole word `1` has no descent and
is fixed.  Its image and recurrent set are `{1}`, its only tail has depth
zero, and its unique fibre has size one.  The theorem correctly starts at
`n>=3` and Proposition 2 correctly handles `n=2,3`, so no displayed formula
is false.  The issue is domain closure: no sentence either declares the
whole family to start at `n>=2` or records `F_1`, despite the author verifier
calling `n=1` an outside-contract boundary.

**Mandatory repair:** either declare `n>=2` before defining the family and
consistently label `n=1` outside the domain, or add the one-sentence `S_1`
atlas above and synchronize the plan/claims/self-QA boundary wording.  The
latter is cleaner and does not alter the main theorem.

## 4. First Sort, sources, and owner subtraction

The Project Euler negative control is accurate.  Problem 523 explicitly says
to scan adjacent pairs from the beginning and move the smaller member of the
first out-of-order pair to the front.  If the first descent is at position
one this equals a two-prefix reversal; if it is at `d>=2`, distinct entries
make

```text
(pi_(d+1),pi_1,...,pi_d) != (pi_(d+1),pi_d,...,pi_1).
```

The manuscript's `1324 -> 2134` versus `1324 -> 2314` witness is correct,
and the reviewer exhaustively checks equality exactly at the identity/first-
position boundary through `S_9`.  Calling First Sort a different rule rather
than a name for P181 is mandatory and is already done correctly.

The three bibliography records are real and used within their verified
scope.  Gates--Papadimitriou owns classical permutation prefix reversal and
pancake distance; Hurkens et al. owns prefix-reversal sorting on binary and
ternary strings; Pudwell--Smith selects the longest increasing prefix but
then performs cut-and-riffle procedures, including suffix-reversal variants,
not P181's whole-prefix reversal.  These operations, descent/peak counts, and
generic finite-map bookkeeping correctly receive zero contribution credit.

Internally, P122 is the closest same-carrier inverse-cut proof vocabulary but
reverses all even record blocks and is acyclic; P117 acts on cyclic binary
runs; FDF is the owner-killed follower-to-front rule; and FAR is explicitly
discarded as the value-complement conjugate.  These separations appear across
the manuscript and paper-local source ledger.  A fresh bounded literal search
found no direct owner of the full P181 conjunction, but that non-hit proves
nothing about novelty or priority.  `OWNER_AMBER / HOLD_EXTERNAL` is the
right ceiling and must remain.

## 5. Claims/evidence, anonymity, and artifacts

- The paper's all-parameter arguments support every frozen theorem claim;
  finite enumeration is correctly described only as falsification pressure.
- The author canonical replays and reports 6,273,063 assertions through
  `S_9`.  The independent review makes 17,364,060 assertions in the different
  factoradic/graph-peeling formulation.
- The 14-entry paper manifest passes 14/14.  `main.pdf` and
  `main_round0_original.pdf` are byte-identical, three A4 pages, SHA-256
  `1df6b41b097c29cc933123906fa1539a37c0944bd843d007204c07b2dc824ad0`.
- The settled log has no unresolved citation/reference, bad-box, or rerun
  warning.  The visible author is Anonymous; PDF title, author, subject,
  keywords, creator, and producer fields are blank.
- The no-figure decision is appropriate for this proof-only atlas.  No
  visual claim is missing.

## 6. Kill switches and disposition

Kill or withdraw if a direct/conjugate owner of the literal map and atlas is
found, if the action is silently changed from length `d+1`, if First Sort is
treated as the same update, or if the value-complement FAR copy is counted as
independent progress.  None of those conditions is active.  After the single
domain-boundary sentence is repaired, the theorem package is acceptable for
the next internal round, still under `HOLD_EXTERNAL`.

**Reviewer assertions:** 17,364,060.  **Canonical replay:** byte-identical in
two fresh processes.

## 7. Round-1 delta acceptance

I re-read the superseding live package at `main.tex` SHA-256
`95909031cae2c75f09399452a472597e72a1bf3a91d10cf4286df54e54e2fb82`
and `main.pdf` SHA-256
`57f62423e760c5a7f4f3add7bd94a559d99468acea3b05082afa5b28e1d24861`.
The initial response correctly added the `S_1` statement but briefly applied
the `rho_2` predecessor sentence to all three small cases.  The superseding
source removes that overreach: lines 278--280 state the complete singleton
atlas, while lines 296--301 prove `n=1` directly and invoke the two-prefix
predecessor only for `n=2,3`.

- **P181-A-m01 — CLOSED.**  The abstract now identifies the `n=1,2,3`
  atlases; Proposition 2 gives `1 -> 1`, singleton image and recurrent set,
  depth zero, and fibre one; the narrative, plan, claims ledger, and self-QA
  all record the same boundary.  The paper-local verifier replaces its old
  one-assertion outside-contract sentinel with eight explicit `S_1` checks
  and its canonical now reports 6,273,070 assertions and
  `boundaries=n1_n2_n3 PASS`.

The author control replayed byte-identically.  The independent factoradic /
indegree-peeling reviewer control was also run in two fresh processes; both
outputs are byte-identical with 17,364,060 assertions.  Its canonical status
has been normalized from the historical missing-boundary label to the proved
`boundary=n1_singleton_atlas PASS`; no mathematical check or assertion count
changed.

The paper's 16-entry manifest passes 16/16.  The live three-page PDF is
byte-identical to `main_round1.pdf` and distinct from the immutable Round-0
receipt.  Identifying PDF metadata remain blank, and the README, BUILD,
SELF_QA, and IMPROVEMENT_LOG accurately distinguish the two rounds.  The
First Sort and owner-subtraction boundaries are unchanged, with
`OWNER_AMBER / HOLD_EXTERNAL` preserved.

**Final Review-A delta verdict:** `0 Critical / 0 Major / 0 Minor open`.
Round 1 is accepted for the next internal stage only; this is not owner
clearance or authorization for external circulation.
