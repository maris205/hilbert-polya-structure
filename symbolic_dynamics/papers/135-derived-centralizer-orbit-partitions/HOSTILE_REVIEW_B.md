# P135 hostile review — Round B

**Manuscript:** *Derived-Centralizer Orbit Partitions: Tagged Transients,
Recurrent Types, and Exact Fibres*  
**Review date:** 2026-09-01 UTC  
**Reviewer role:** second independent reviewer; no participation in the draft
or in Round-A review  
**Calibration:** `NOT_CALIBRATED`; `criteria_binding_unavailable`, so this
report makes no venue-fit claim  
**External status:** `HOLD_EXTERNAL`  
**Verdict:** **`REPAIR`** — every Round-A mathematical/boundary/layout repair
and the full theorem package pass, but one stale unlabelled pinned source hash
still breaks Round-1 traceability.

Severity summary: **CRITICAL 0; MAJOR 0; MINOR 1**.

## 1. Frozen Round-B snapshot

I reviewed the repaired package without modifying `main.tex`, bibliography,
code, canonical output, or any PDF.  The reviewed hashes are:

| artifact | SHA-256 |
|---|---|
| `main.tex` | `cd8ea8a0d077b9619adf8b8d7e172757a5262d2f24a9060c98c92f0ad87ae149` |
| `references.bib` | `515faec4ab071ecf7c68bf65c5bb721867eeea912ef30a57c7b41f9e4402baae` |
| `code/verify.py` | `26b87846c87dd671f709f90e9945f5724b3f6deac959f2619a73078721f0313a` |
| `code/verification_output.txt` | `be50b73c6c3c17c6378d141bc6c594388512241b8acb9b6e7b877b470070ba90` |
| `main.pdf` | `dbf3a7ff19d1ddd2bcde59b35287835ffa8dec3b4244c53e65e87fc14a2b1b94` |
| `main_round0_original.pdf` | `7cd8a811a9d879e303c3d7a0b1bd6631aa24d9fc64704df62b4a369ce327505b` |
| `main_round1.pdf` | `dbf3a7ff19d1ddd2bcde59b35287835ffa8dec3b4244c53e65e87fc14a2b1b94` |

Fresh raw execution of `code/verify.py` matched the canonical stdout byte for
byte (`cmp=0`).  It again reported 7,130,840 exact assertions over all
540,634 partitions through weight 45, every 28,628 target through weight 30,
118,634 reachable tagged states, 56,961 two-clean pairs, and 18 literal
wreath-product cases.  It uses exact Python integers/tuples, no sampling, and
no floating point.

A fresh isolated four-stage build from only `main.tex` and
`references.bib` produced a PDF byte-identical to both `main.pdf` and
`main_round1.pdf`.  The artifact has five A4 pages and 395,335 bytes.  The
settled build has no undefined reference/citation, bad box, or actionable
warning.  All 31 font rows are embedded, subsetted, and Unicode-mapped.  The
PDF is unencrypted; Title/Subject/Keywords/Author metadata fields are blank,
and the visible byline is `Anonymous`.

I rasterized and inspected all five pages.  No clipping, overlap, malformed
glyph, bad link box, or bibliography defect is visible.  On page 5 the final
ownership/control paragraph now finishes before Table 1, so the Round-A
float splice is gone.  The table is fully inside the text block and its rows,
caption, and references remain legible.  Extracted text is searchable and
contains no leaked tool/debug tokens.

## 2. Closure of Round-A findings

| Round-A item | repaired state | Round-B result |
|---|---|---|
| `P135-A-m1`, undefined `f_0,c_0` | Theorem 1.1(iv) states `f_0=1,c_0=0` by the empty-partition convention before equations (8)--(9). | closed |
| `P135-A-m2`, undefined `tail`/recurrent | Lines preceding the theorem define recurrent as lying on a directed cycle and tail as the least `t>=0` entering recurrence, with recurrent tail zero. | closed |
| `P135-A-m3`, false GF locator | Both ledgers now point to equations (8)--(9), Theorem 4.1, and the unnumbered Section 4 generating-function proof. | closed |
| `P135-A-m3`, page-5 float splice | Ownership/control prose precedes Table 1; full-page visual inspection confirms separation and legibility. | closed |

The `main_round0_original.pdf` hash remains immutable, while `main.pdf` and
`main_round1.pdf` are byte-identical.  The source/PDF differences are
consistent with the documented boundary and layout repairs.  No Round-A
finding remains open.

## 3. Independent hostile reconstruction

### 3.1 Derived wreath factor and local orbit law

For multiplicity `m` at cycle length `j`, the centralizer factor is
`C_j^m semidirect S_m`.  Coordinate sum on the base and sign on the top put
the commutator inside `B_0 semidirect A_m`.  Commuting a base coordinate with
a transposition generates every coordinate difference and hence `B_0`;
commutators of the top copy generate `A_m` for `m>=3`, and the top derived
group is trivial for `m=2`.  For `m=1` the factor is abelian.

On natural points this yields exactly `1^j` for `m=1`, two orbits `j^2` for
`m=2`, and one orbit `jm` for `m>=3`.  The delicate thresholds survive:
`A_3` is transitive on three blocks, `j=1` merely makes within-block motion
vacuous, and `m=2` has base transitivity inside but no top block merger.
Derived subgroups commute with the finite direct product over occupied
lengths, whose actions have disjoint supports, so collecting local outputs is
valid.

### 3.2 Reachable tags, crossings, and two-clean normal form

A reachable tag is always represented either by one whole part of its mass
or by that many tagged singletons.  A split changes only representation; a
multiplicity-two step preserves tags; a merge takes the union of distinct
tags and exactly preserves total mass.  Current tags therefore partition the
atomic tags, and their number drops precisely at a crossing merge.

The reachability restriction closes the strongest apparent counterexample
to the two-clean lemma.  After the first clean transition, non-singleton
pieces are distinct-size dimers plus at most one whole oscillator.  If the
next transition is clean, a singleton sector of size at least three must be
copies of one split tag, leaving at most one split oscillator; a smaller
sector is the residue `e<=2`.  An unpaired `H_2` exists only at time zero and
cannot be recreated, so it cannot supply a delayed residue beside an
oscillator.  Same-size dimer exclusions prevent a hidden merger on either
adjacent transition.  The remaining whole/split pieces swap phase and return
after two updates.

### 3.3 Tail and recurrence boundary

There are initially `ell(lambda)` tags and hence at most
`ell(lambda)-1` crossing transitions.  Before recurrence, every disjoint
pair of transitions must contain a crossing; otherwise its intermediate
reachable tagged state is already periodic with period dividing two.  A tail
exceeding `2 ell(lambda)` would therefore force `ell(lambda)` crossings, a
contradiction.  The result is the advertised safe, explicitly nonsharp bound
`tail(lambda) <= 2 ell(lambda) <= 2n`.

The repaired definition handles all boundaries: fixed points and both phases
of a strict two-cycle have tail zero, while `tail` is the least entrance time
and not a first-repeat convention.  The proof needs no empirical assumption
about the observed maximum tail six.

### 3.4 Complete recurrent classes and OGFs

On a recurrent uncoloured orbit, the lifted tag partition can coarsen only
finitely often.  After enough laps it stabilizes, so every adjacent pair is
clean and the normal form applies at every phase.  Projection gives exactly
the four disjoint classes: base dimers plus residue `e<=2`, one oscillator,
two equal opposite-phase oscillators, or two unequal opposite-phase
oscillators.  Direct substitution gives the converse and the stated exact
periods.  The requirement that dimer set `D` avoid oscillator amplitudes is
both necessary and present.

The fixed-point OGF has a base term `(1+q+q^2)D(q)` and the equal-amplitude
term `sum q^(2a)D_{a}(q)`.  Strict cycles have the one-oscillator term
`sum q^aD_a(q)` and the unordered unequal-amplitude term
`sum_{a<b}q^(a+b)D_{a,b}(q)`.  The four recurrent types neither overlap nor
double count, and recurrent points are consequently `f_n+2c_n`.  The
repaired `f_0=1,c_0=0` matches the constant terms exactly.

### 3.5 Every-target fibre

For each source multiplicity `m_j`, the mutually exclusive cases
`0,1,2,m>=3` contribute the four local terms in the displayed product.
Source multiplicities at different sizes are independent.  Extracting
`z^n` fixes total source weight, and extracting the complete target monomial
counts each source multiplicity vector exactly once.  Terms above weight
`n` cannot survive the `z^n` extraction.  An out-of-image target has
coefficient zero without an extra domain condition.

I specifically attacked the thresholds `m=1,2,3`, `j=1`, a lone unpaired
part of size two, equal versus unequal oscillator amplitudes, oscillator/
dimer size collisions, `n=0` formal coefficients, and targets outside the
image.  None supplies a theorem counterexample.

## 4. Code-to-paper consistency

The verifier's map uses the same three multiplicity thresholds as equation
(2).  Its recurrent recognizer matches the four source templates; its OGF
coefficients distinguish fixed points from strict cycles exactly as the
paper does; its fibre expansion checks every target rather than only image
targets.  The tagged tests are restricted to reachable lifts, matching the
hypothesis of the two-clean lemma.  Literal group enumeration independently
tests derived closures and natural-point orbits at the small wreath
thresholds.  All headline counts in the paper and canonical transcript
match the fresh replay.

## 5. Citations, ownership, and contribution boundary

The bibliography metadata and citation roles are coherent.  Britnell--Wildon
is used for orbit-partition/permutation-group context, Skuratovskii for
existing wreath-commutator material, Eliahou--Erickson for a neighbouring
multiplicity-description iteration, and Baalbaki et al. for a different
weight-preserving partition dynamics.  Every bibliography entry is cited;
none is asked to prove the manuscript's tagged classification or fibre law.

I cross-checked the title/author/year/venue-or-arXiv identifiers against the
primary records for
[Britnell--Wildon](https://doi.org/10.1515/jgt-2013-0029),
[Skuratovskii](https://arxiv.org/abs/1812.10481),
[Eliahou--Erickson](https://doi.org/10.1016/j.disc.2012.11.014), and
[Baalbaki et al.](https://doi.org/10.1007/s11139-023-00791-5).  The local
records and the manuscript's deliberately limited attribution roles agree.

The owner subtraction is conservative: centralizer decomposition, generic
wreath commutators, orbit-partition language, multiplicity dynamics, and
formal coefficient extraction receive zero contribution credit.  The
residual package is explicitly limited to this literal map's reachable tag
theorem, recurrent atlas/OGFs, and all-target fibre.  Internal comparisons
with P113/P123/P105/P110 distinguish mechanisms rather than claiming
novelty.  The bounded non-hit is correctly not promoted to priority evidence.

## 6. Findings

### Critical

None.

### Major

None.

### Minor

#### `P135-B-m1` — unlabelled `CONTROL_RESULTS.md` hash block pins obsolete Round-0 `main.tex`

The current repaired source has SHA-256
`cd8ea8a0d077b9619adf8b8d7e172757a5262d2f24a9060c98c92f0ad87ae149`.
The unqualified section headed `## Pinned hashes` in `CONTROL_RESULTS.md`
instead lists
`386b0cbca5cf812599687df39e3db43ee0edb47cb500f7718742b9badf0cb273`
for `main.tex`, which is the Round-0 source hash.  The block does label the
PDF path `main_round0_original.pdf`, but it does not label the source hash as
historical and supplies no current Round-1 source/PDF pin.  A reader following
the purported current control record therefore obtains a failed source hash
despite the genuinely reproducible build.

**Evidence anchor:** `CONTROL_RESULTS.md`, unqualified `Pinned hashes` block;
fresh `sha256sum main.tex`; compare the correct Round-1 hashes in
`IMPROVEMENT_LOG.md` and `BUILD_REPORT.md`.  
**Severity:** Minor — traceability/support defect only; the theorem, verifier,
and PDF are unaffected.  
**Confidence:** 5/5 — direct hash comparison.

**Required repair:** either:

1. relabel the existing block explicitly as the immutable Round-0 snapshot
   and add a separate Round-1 block containing the current `main.tex`,
   `main.pdf`, and `main_round1.pdf` hashes; or
2. update the unqualified block to the current source/PDF pins while keeping
   separately labelled immutable Round-0 hashes.

Do not rebuild or alter `main.tex`, code, or PDFs for this support-only fix.
After editing the ledger, re-run the hash comparisons once.

## 7. Verdict

**Round-B verdict: `REPAIR / HOLD_EXTERNAL`.**  Critical 0, Major 0, Minor 1.
All mathematics, verifier alignment, anonymity, font/metadata checks, and
page-5 presentation pass.  Only `P135-B-m1` prevents `GO_INTERNAL`; it is a
single ledger repair and requires no theorem, code, or PDF change.  The
external-release hold remains mandatory.

## Closure addendum — 2026-09-01 UTC

I independently rechecked the support-only repair of `P135-B-m1` after the
Round-B report above.  `CONTROL_RESULTS.md` now has two unambiguous sections:
`Immutable Round-0 pinned hashes` and `Current Round-1 pinned hashes`.  The
former explicitly says that the `386b...` `main.tex` pin is historical and
produced the immutable Round-0 PDF; it no longer purports to identify the
current source.

A fresh `sha256sum -c` over every entry in the current Round-1 block returned
`OK`.  Direct hashes were:

```text
cd8ea8a0d077b9619adf8b8d7e172757a5262d2f24a9060c98c92f0ad87ae149  main.tex
515faec4ab071ecf7c68bf65c5bb721867eeea912ef30a57c7b41f9e4402baae  references.bib
26b87846c87dd671f709f90e9945f5724b3f6deac959f2619a73078721f0313a  code/verify.py
be50b73c6c3c17c6378d141bc6c594388512241b8acb9b6e7b877b470070ba90  code/verification_output.txt
dbf3a7ff19d1ddd2bcde59b35287835ffa8dec3b4244c53e65e87fc14a2b1b94  main.pdf
dbf3a7ff19d1ddd2bcde59b35287835ffa8dec3b4244c53e65e87fc14a2b1b94  main_round1.pdf
```

Fresh byte comparison of `main.pdf` and `main_round1.pdf` also returned
`cmp=0`.  The immutable `main_round0_original.pdf` remains distinct at
SHA-256
`7cd8a811a9d879e303c3d7a0b1bd6631aa24d9fc64704df62b4a369ce327505b`.
No manuscript, bibliography, verifier, canonical transcript, or PDF change
was required or made in this closure review.

**Closure:** `P135-B-m1` is closed.  Final severities are **CRITICAL 0;
MAJOR 0; MINOR 0**.  This dated addendum supersedes the pre-repair disposition
above.  **Final verdict: `GO_INTERNAL / HOLD_EXTERNAL`.**
