# P155 independent hostile review A

**Review date:** 2026-09-02 UTC.  
**Reviewer relation:** independent internal reader; did not author P155.  
**Protocol:** docs/papers152_156_sequence/HOSTILE_REVIEW_PROTOCOL.md.  
**External state:** HOLD_EXTERNAL. No manuscript content was sent to an
external model or service.

## Verdict

**REVISE — 0 Critical / 0 Major / 2 Minor.**

The reduced CME theorem package survives independent rederivation. The sharp
target threshold, all-rank sections, weighted fibres, and strict rank descent
are correct as stated. I found no direct owner of the owner-subtracted
residual, no verifier or build mismatch, no anonymity defect, and no hidden
promotion of the unproved power clock to theorem status.

Two local repairs remain. The deterministic scheduler needs an explicit
all-openers boundary branch rather than an undefined O_(m+1), and the finite
power-clock material must be moved into the Limitations paragraph exactly as
the freeze contract requires.

This is a raw review. I did not edit main.tex, the verifier, transcript, PDF,
or any author ledger.

## 1. Package and theorem-ceiling comparison

I read FINAL_THEOREM_CONTRACTS.md, CME_FREEZE_CONTRACT.md, the system
collision firewall, the replacement-2 scout and owner log, main.tex,
PROOF_PACKAGE.md, SELF_QA.md, every paper-local ledger, references.bib,
verify_p155.py, verification_output.txt, BUILD.md, FINAL_QA.md, the manifest,
and both Round-0 PDFs.

| Frozen interface | Manuscript interface | Hostile result |
|---|---|---|
| literal support-maxima map | equation (1) | PASS; static ingredients fully subtracted |
| rank equals cycle count; identities only recurrent | Theorem 1(3), Section 3 | PASS |
| exact threshold mu(sigma)=2m-rlmin(sigma) | Theorem 1(1), Section 2 | PASS |
| constructive section at the minimum and every larger rank | Lemma 2 and enlargement paragraph | PASS with one algorithm-boundary Minor |
| factorially weighted every-target fibres | Theorem 1(2), equation (4) | PASS |
| image census and minimum-rank unweighted fibre | Corollary 3 | PASS; direct consequences with classical distribution zero-credit |
| no sharp power clock or iterated-preimage optimum | abstract, Section 3, Limitations | no theorem overclaim; location repair required |

The note remains paper-sized only as the conjunction of the sharp
target-resolved image theorem and the independently complete fibre theorem.
Neither static endpoint vocabulary nor the recurrence clause carries the
paper by itself.

## 2. Independent theorem rederivation and proof attacks

### 2.1 Literal map and strict rank descent

One output letter is read from each disjoint-cycle support, so the output
rank is the number of source cycles. Equality with source rank n occurs if
and only if all n cycles are singletons, hence the source is id_n. Its support
maxima are 1,...,n, so it is fixed. Every other step strictly lowers positive
integer rank. Therefore no other state can lie on a directed cycle in the
finite cutoff, and the recurrent set is exactly the identities.

The example pi=(4,5,3,1,2) is consistent with functional notation: its
supports are {1,4}, {2,5}, {3}, and their maxima standardize to 231.

### 2.2 Necessity of the minimum source rank

Let a target position i correspond to support B_i. If B_i is a singleton,
then for every later support B_j,

~~~text
max B_j >= min B_j > min B_i = max B_i.
~~~

Thus sigma_i is a right-to-left minimum. If s supports are singleton, then
s<=rlmin(sigma), and all other supports have size at least two:

~~~text
n >= s+2(m-s)=2m-s >= 2m-rlmin(sigma).
~~~

Equality requires all and only right-to-left-minimum positions to be
singleton and every other block to have size two. This also validates the
minimum-rank fibre corollary.

### 2.3 Sufficiency and simultaneous endpoint events

Use opener order O_1<...<O_m and closer-value order K_1<...<K_m, pairing
O_i with K_(sigma_i). The greedy rule emits a simultaneous pair only when
the next opener is a right-to-left-minimum position and its paired closer is
the next closer. Otherwise it closes an available next closer before opening
another block.

For a right-to-left minimum of value v, every smaller value occurs at an
earlier position. Once all earlier openers are emitted, closer priority
therefore exhausts K_1,...,K_(v-1), so K_v and its opener become next
together. Conversely the rule declares no other simultaneous event. The word
has 2m-rlmin(sigma) events and respects both endpoint chains and every
opener-before-closer constraint. Consecutive integer event labels give the
minimum-rank supports with the required standardized maxima.

Splitting any simultaneous event into adjacent opener/closer events adds one
coordinate without changing either chain order. After all such events are
split, every block has a nonempty endpoint interval; arbitrary further
coordinates may be inserted inside one interval and later coordinates
renumbered. Choosing the increasing cyclic order on each support gives a
literal permutation. Hence every n>=mu(sigma) has a section.

The mathematical construction is complete. The pseudocode statement in
Lemma 2, however, says to consider O_(i+1) even after i=m. The intended closer
branch is forced and implemented correctly by the verifier, but the written
algorithm is not literally total. This is Finding m1.

### 2.4 Every-target fibres and equality cases

A source permutation has one unique ordered support partition. On a fixed
labelled block of size b there are exactly (b-1)! cyclic permutations, and
the cycle choices on disjoint blocks are independent. Conversely, any
ordered support family satisfying the target endpoint condition, together
with one cyclic order per block, reconstructs exactly one permutation mapped
to sigma. The disjoint sum in equation (4) therefore counts the complete
fibre, including the zero case.

At n=mu(sigma), every block size is one or two, so all weights are 0!=1 or
1!=1. The claimed equality with the number of support families follows.

### 2.5 Image census

The number of permutations in S_m with r right-to-left minima is the unsigned
first-kind Stirling number [m r]. Inserting the largest letter in the final
position creates one new right-to-left minimum; any of the other m-1
positions preserves the count. This gives the standard Stirling recurrence.
Combining r>=2m-n with 1<=r<=m proves the double sum in Corollary 3.

No division, empty-rank, or m=1 exception is hidden: every nonempty
permutation has at least one right-to-left minimum, so
m<=mu(sigma)<=2m-1.

## 3. Owner attack

### Direct and same-object ownership

The source ledger correctly subtracts:

- Chen--Deng--Du--Stanley--Yan for fixed block minima/maxima and
  crossing/nesting theory;
- Rubey--Stump for opener/closer/singleton endpoint configurations;
- Mongelli for cycles written and ordered by increasing minima; and
- Andrews--Egge--Gawronski--Littlejohn for prescribed cycle maxima.

These are direct owners of the static ingredients, not of contribution value.
The factor (b-1)! for cyclic orders on a fixed support and the unsigned
Stirling/right-to-left-minimum distribution are standard and also receive
zero credit.

### Residual and bounded non-hit

The residual is only the literal map-specific conjunction of the
target-dependent threshold with constructive all-rank sections and the
target-resolved weighted fibre sum. The manuscript does not claim that cycle
maxima, ordered cycles, endpoint scheduling, or factorial weights originate
here. The exact-map query non-hit is explicitly bounded and is not converted
to novelty, priority, ownership completeness, or clearance.

I found no internal evidence that the four checked primary sources state the
literal rank-changing map and this residual conjunction. A later direct
source would reopen the slot.

## 4. Portfolio-collision attack

- **P105:** P105 preserves rank and performs cycle-minimum arrow surgery,
  with a largest-cycle clock. P155 immediately forgets cyclic order, changes
  rank to the cycle count, and uses support endpoints.
- **P149:** both standardize variable-rank permutation data, which earns no
  separation credit. P149 selects endpoint peaks and uses alternating slots;
  P155 selects one maximum per disjoint-cycle support and uses
  right-to-left-minimum singleton capacity.
- **P156:** both have target sections and every-target fibres. P156 uses a
  weak-excedance selector, maximum-drop cost m+d, Ferrers matchings, and a
  Fibonacci inverse tower. P155 uses threshold 2m-rlmin and factorially
  weighted ordered support partitions; it freezes no inverse tower.
- **P152:** stochastic shared-edge triad flips, a marked Chebyshev transform,
  and a mean/parity inverse have no literal or proof-engine overlap.
- **P153:** factorial collapse on a fixed finite plane uses forced-coordinate
  fibres, not rank-changing standardized permutations.
- **P154:** subgroup-normalizer forests and arithmetic signature recovery
  share only generic rank/branch language.

The literal selector, obstruction, and fibre engine remain distinct. The
portfolio gate passes provided generic “rank-changing permutation with exact
fibres” language receives no independent credit; the manuscript respects
that boundary.

## 5. Independent exact replay

I cold-ran:

~~~bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p155.py
~~~

Fresh stdout matched verification_output.txt byte for byte and ended with:

~~~text
power_of_two_clock=NOT_CLAIMED
enumeration_role=COUNTEREXAMPLE_PRESSURE_ONLY
boxes=26
assertions=16473121
status=PASS
~~~

The run enumerates 4,037,913 literal permutation states through rank ten,
145,684 target/rank image cells, 46,233 independent endpoint-DP targets,
3,161 constructed section cells, and 53,218 target fibre cells through source
rank eight. The endpoint DP permits O, K, and S moves independently of the
closed threshold; restricted-growth words build the support side independently
of literal predecessor counts.

This computation does not prove the all-rank theorem, settle the excluded
power clock, complete the owner search, establish novelty or priority, or
authorize release. It is bounded exact counterexample pressure.

## 6. Source-only build, PDF, and anonymity

A fresh directory containing only main.tex and references.bib completed

~~~text
pdflatex -> bibtex -> pdflatex -> pdflatex
~~~

and reproduced the paper-local PDF byte for byte:

~~~text
pages=4, bytes=348083
SHA256=f1025e7a19e40eed7dc2608bdebad47ebed998345bc58d94aec6b27025c6b3c8
~~~

The current PDF and main_round0_original.pdf are byte-identical. The
paper-local manifest passes for all listed Round-0 files. The settled log has
no unresolved citation/reference, rerun request, build warning, overfull box,
underfull box, or duplicate label. All 28 reported font rows are embedded and
subsetted. The PDF is A4 and unencrypted, with blank identifying title,
author, subject, and keyword metadata and no form or JavaScript.

I rasterized and inspected all four pages. The ownership boundary, theorem,
greedy schedule, image/fibre corollaries, finite profile, recurrence proof,
declarations, and four references are legible and within bounds. I found no
clipping, overlap, blank page, corrupt glyph, unresolved marker, or visible
identity leak.

BUILD.md and FINAL_QA.md accurately record the Round-0 author freeze and do
not misrepresent SELF_QA.md as independent review.

## 7. Findings and required repairs

### m1 — Minor: greedy scheduler is not total at the all-openers boundary

**Evidence.** Lemma 2 begins every iteration by considering the next opener
O_(i+1) and next closer K_(j+1). When i=m<j is impossible, but
i=m and j<m is the normal final-closing phase. O_(m+1) is undefined, even
though the intended second move must apply because all closer owners are
open. The verifier guards i<m and therefore does not share the prose defect.

**Required repair.** State the boundary first: if i=m, emit K_(j+1) until all
closers are exhausted. Otherwise apply the three cases. Equivalently define
the simultaneous and opener cases only for i<m. Retain the proof that the
algorithm cannot stall.

### m2 — Minor: the power-clock profile appears outside the frozen location

**Evidence.** CME_FREEZE_CONTRACT.md permits the computationally supported
power-clock question only in the Limitations paragraph. The manuscript also
prints “maximum observed tail” as a row of Table 1 and devotes a separate
Section 3 paragraph/display to the sequence and power-of-two suggestion.
Every occurrence is carefully labelled non-theorem, so this is not a false
claim or Major theorem expansion, but it exceeds the frozen presentation
boundary.

**Required repair.** Remove the tail row from Table 1 and move the finite
sequence plus one-sentence open-question disclaimer into the existing
Limitations paragraph. Keep the title, abstract, theorem, image table, proof,
claim ledger, and conclusion free of any clock result; retain the transcript
sentinel power_of_two_clock=NOT_CLAIMED.

## 8. Decision

The mathematical, owner, portfolio, exact-control, build, visual, and
anonymity gates pass. Internal acceptance is withheld only until both Minor
items are repaired in source, documented in IMPROVEMENT_LOG.md, and compiled
as main_round1.pdf according to the protocol.

**Verdict: REVISE — 0 Critical / 0 Major / 2 Minor / HOLD_EXTERNAL.**
