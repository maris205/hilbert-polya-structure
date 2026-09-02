# P155 independent hostile review B

**Review date:** 2026-09-02 UTC.  
**Reviewer relation:** independent internal algebraic-style reader; did not
author P155 and did not perform its Review A.  
**Protocol:** `docs/papers152_156_sequence/HOSTILE_REVIEW_PROTOCOL.md`.  
**External state:** `HOLD_EXTERNAL`.  No manuscript content was transmitted
to an external model, service, or specialist.

## Verdict

**ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor.**

Starting cold from the reduced CME freeze contract and the Round-1 package, I
independently rederived the sharp threshold, the total greedy schedule, the
all-rank sections, the weighted fibres, and strict rank loss.  All statements
remain within the frozen theorem ceiling.  Both Review-A findings are repaired
in the source rather than merely marked closed: the scheduler now handles the
all-openers boundary explicitly, and the finite power-clock profile occurs
only inside the Limitations paragraph.  The transcript retains the required
`power_of_two_clock=NOT_CLAIMED` sentinel.

A fresh-process verifier replay completed 16,473,121 exact assertions and was
byte-identical to the frozen transcript.  A cold directory containing only
`main.tex` and `references.bib` reproduced the current/Round-1 PDF byte for
byte.  All four rendered pages, metadata, fonts, text, and settled logs pass.
This is internal acceptance only and does not authorize novelty, priority,
posting, circulation, specialist contact, submission, or release.

## 1. Cold package and theorem-ceiling audit

I read the hostile-review protocol, `FINAL_THEOREM_CONTRACTS.md`,
`CME_FREEZE_CONTRACT.md`, the historical-occupancy and system-collision
firewalls, the CME owner-search record, `HOSTILE_REVIEW_A.md`,
`IMPROVEMENT_LOG.md`, `main.tex`, `references.bib`, the complete paper-local
proof/claim/source/control/QA package, `verify_p155.py`, the frozen transcript,
the manifest, and the Round-0 and Round-1 PDFs.

| Frozen interface | Round-1 realization | Cold result |
|---|---|---|
| literal cycle-support maximum map | equation (1) | PASS; carrier and ordering agree exactly |
| strict rank loss and identity-only recurrence | Theorem 1(3) and Section 3 | PASS |
| `mu(sigma)=2m-rlmin(sigma)` | equation (2), Theorem 1(1), Section 2 | PASS |
| deterministic minimum and every-larger-rank sections | Lemma 2 and its enlargement argument | PASS, including `i=m` boundary |
| complete weighted target fibres | equation (4), Theorem 1(2) | PASS |
| Stirling image census and minimum-rank unweighted fibre | Corollary 3 | PASS as zero-credit consequences |
| no solved absorption clock or iterated-preimage optimum | abstract and Limitations | PASS; finite profile confined to Limitations |

The contribution remains the owner-subtracted conjunction of the exact target
threshold, constructive all-rank inverse sections, and target-resolved
weighted fibres.  Static endpoint language, ordered-cycle conventions,
right-to-left-minimum/Stirling statistics, and fixed-support cyclic-order
counts receive no independent contribution credit.

## 2. Independent rederivation and exceptional-parameter attack

### 2.1 Rank and recurrence

For a source `pi in S_n`, one output entry is read from each disjoint-cycle
support.  Thus `|C(pi)|` is the number of cycles of `pi`, at most `n`.
Equality holds exactly when every cycle is a singleton, hence exactly when
`pi=id_n`.  In that case the ordered maxima are `1,...,n`, so `id_n` is fixed.
Every nonidentity step strictly decreases positive integer rank.  A periodic
orbit cannot contain a strict decrease, so the recurrent states on every
finite cutoff are precisely the identities.

This also checks the cross-rank equality issue: a tuple in another symmetric
group cannot equal the source, and no rank can increase along an orbit.

### 2.2 Necessity of `2m-rlmin(sigma)`

Let `B_i` be a singleton support.  Since supports are ordered by increasing
minimum, every later support satisfies

```text
max B_j >= min B_j > min B_i = max B_i.
```

Therefore target position `i` is a right-to-left minimum.  If `s` supports
are singleton and `r=rlmin(sigma)`, then `s<=r`; every other support contains
at least two coordinates.  Consequently

```text
n >= s + 2(m-s) = 2m-s >= 2m-r.
```

At equality, necessarily `s=r`, every right-to-left-minimum block is a
singleton, and every other block has size two.  This equality analysis is
also exactly what the minimum-rank fibre corollary needs.

### 2.3 Total greedy scheduler, including `i=m`

Use the two strict chains `O_1<...<O_m` and `K_1<...<K_m`, pairing `O_i`
with `K_(sigma_i)`.  At a state `(i,j)` counting emitted openers and closers:

1. if `i=m`, every remaining closer owner is already open, so emit
   `K_(j+1)`; this forced branch is defined until `j=m`;
2. otherwise, if the next opener is a right-to-left-minimum position and is
   paired to the next closer, emit the pair simultaneously;
3. otherwise, if the next closer's owner is open, emit that closer;
4. otherwise emit the next opener.

When `i<m`, one cannot have `j=m`: emitting all `m` closers would require all
`m` distinct owners to have opened.  Hence every symbol referenced by the
ordinary three cases is defined.  If the next opener has target value `v` and
is a right-to-left minimum, every value below `v` lies to its left.  Those
owners are already open, and closer priority exhausts
`K_1,...,K_(v-1)` before the opener can be emitted.  `K_v` cannot have been
emitted because its owner is this unopened block.  Thus the simultaneous case
is reached.  No other position is declared simultaneous.

Exactly `rlmin(sigma)` pairs are identified among `2m` formal endpoints, so
the schedule length is `2m-rlmin(sigma)`.  Successive integer event labels
respect both chains and every opener-before-closer constraint, giving a
minimum-rank ordered support family whose maxima standardize to `sigma`.

### 2.4 Every-rank sections

Splitting a simultaneous event into the adjacent ordered pair `O_i,K_(sigma_i)`
adds one coordinate while preserving both endpoint-chain orders.  This covers
each rank up to the fully split `2m`-event word.  Once all pairs are split,
any further event can be assigned as an interior coordinate of one open
support; inserting and relabelling later events changes neither its minimum
nor maximum nor either global endpoint order.  Placing the increasing
canonical cycle on each support turns the support family into a literal
permutation.  Hence a deterministic source exists for every
`n>=2m-rlmin(sigma)`.

### 2.5 Weighted fibres

Every source has a unique cycle-support partition, and ordering its blocks by
minimum is unique.  A fixed labelled block of size `b` supports exactly
`(b-1)!` cycles: fix one anchor and linearly order the remaining elements
around it.  Choices on disjoint blocks are independent.  Conversely, an
ordered support family in `P_n(sigma)` together with one cycle on each block
reconstructs one and only one source mapped to `sigma`.  The disjoint union of
these classes gives

```text
|C_n^(-1)(sigma)| =
  sum_((B_1,...,B_m) in P_n(sigma)) prod_i (|B_i|-1)!.
```

The empty support-family sum is zero below the image threshold.  At the
minimum rank, all block sizes are one or two, so every weight is `0!` or `1!`
and equals one.

### 2.6 Census and hard boundaries

Permutations in `S_m` with `r` right-to-left minima are counted by the
unsigned first-kind Stirling number `[m r]`.  The target condition is
`2m-r<=n`, giving the stated double sum with
`r>=max(1,2m-n)`.

The exceptional cases all close:

- `m=1`, `sigma=1`: `r=1`, `mu=1`; the minimum schedule is one simultaneous
  event, and the rank-`n` fibre is the `(n-1)!` set of `n`-cycles;
- `sigma=id_m`: all `m` positions are right-to-left minima, `mu=m`, and the
  minimum section consists of singleton supports;
- `sigma=m...(2)1`: only the last position is a right-to-left minimum,
  `mu=2m-1`, attaining the largest target threshold;
- `n=m`: only the identity target of rank `m` can occur, consistently with
  strict rank loss for every nonidentity source;
- all claims concern positive ranks, so no empty-permutation or `0!`
  convention beyond singleton block weights is hidden.

## 3. Review-A repair verification

### A-m1: all-openers scheduler boundary — closed

The Round-1 Lemma 2 proof now starts with the loop condition
`i<m or j<m`, treats `i=m` by emitting `K_(j+1)`, and invokes the ordinary
three cases only when the next opener and closer both exist.  The proof also
states why `j<m` whenever `i<m`.  This is the required source-level repair;
the verifier's pre-existing guard agrees with it.

### A-m2: power-clock placement — closed

The Round-1 table contains only exact image sizes.  There is no tail row, no
separate clock display in the dynamics section, and no conclusion promoting a
clock.  The finite sequence

```text
0,1,2,2,3,3,3,3,4,4
```

appears only inside `Limitations`, immediately labelled an open computational
observation with no all-parameter bound, pointwise clock, or global
iterated-preimage minimum-rank theorem.  The abstract says only that no sharp
absorption clock is claimed.  The exact transcript retains
`power_of_two_clock=NOT_CLAIMED`.

A text diff from Round 0 to Round 1 shows only these two substantive repairs
plus their induced page reflow.  The original PDF remains preserved at its
frozen hash.

## 4. Owner and portfolio falsification

### 4.1 Owner subtraction

The package correctly assigns zero credit to the closest static inputs:

- Chen--Deng--Du--Stanley--Yan: block minima/maxima and fixed-endpoint
  crossing/nesting theory;
- Rubey--Stump: opener/closer/singleton/transient configurations;
- Mongelli: cycles written and ordered by increasing minima;
- Andrews--Egge--Gawronski--Littlejohn: prescribed cycle-maxima sets;
- standard inputs: `(b-1)!` cyclic orders, right-to-left-minimum Stirling
  distribution, standardization, and generic finite-map rank descent.

The bounded literal-map non-hit is explicitly not converted into novelty,
priority, ownership completeness, or freedom to release.  The residual claim
surface is therefore owner-thin rather than owner-blind.

### 4.2 Portfolio collision

- P105 changes arrows while preserving rank and has a largest-cycle pruning
  clock; P155 discards cyclic order, changes rank to cycle count, and solves a
  support-endpoint inverse problem.
- P149 uses local endpoint peaks and alternating-slot fibres; P155 uses whole
  disjoint-cycle supports, right-to-left-minimum singleton capacity, and
  factorial support weights.
- P156 uses weak-excedance positions, the `m+d` obstruction, Ferrers
  completions, and a Fibonacci inverse ray; P155 uses `2m-rlmin`, ordered
  support partitions, and freezes no inverse tower.
- P152--P154 use respectively stochastic triad flips, finite-field factorial
  collapse, and dihedral subgroup normalizers.  Their literal carriers and
  proof engines do not transfer to CME.

Generic phrases such as variable-rank permutation map, exact fibre, or
functional graph receive no separation credit.  The literal selector,
obstruction statistic, section, and fibre engine still distinguish P155.

## 5. Fresh exact-control replay

I ran the verifier in a fresh scrubbed process with bytecode disabled.  Fresh
stdout was byte-identical to `verification_output.txt`, whose SHA-256 is

```text
b398a0cade8b64cdab92ee6c638e7607f3310cf9e304a52e8df07ca7d57e410c
```

and whose terminal records are

```text
ordered_support_terms=5295
power_of_two_clock=NOT_CLAIMED
enumeration_role=COUNTEREXAMPLE_PRESSURE_ONLY
boxes=26
assertions=16473121
status=PASS
```

The replay covers 4,037,913 literal states through rank ten, 145,684
target/rank image cells, 46,233 independently optimized endpoint targets,
3,161 constructive section cells, and 53,218 every-target fibre cells through
source rank eight.  The endpoint dynamic program permits opener, closer, and
simultaneous moves independently of the closed formula; the support-fibre
side uses restricted-growth words independently of literal predecessor
counts.

This finite execution does not prove the all-parameter theorem, solve the
excluded clock, complete the owner search, establish novelty or priority, or
authorize external action.

## 6. Cold build, integrity, and rendered PDF

A fresh temporary directory contained only `main.tex` and `references.bib`
before running

```text
pdflatex -> bibtex -> pdflatex -> pdflatex.
```

The cold PDF is byte-identical to both `main.pdf` and `main_round1.pdf`:

```text
pages=4
bytes=345390
SHA256=54fb1fb0a2519950d3b5725ea5e02c09eb89de13048bf7a97c62d41a9f99ebd1
```

The preserved author-freeze PDF remains

```text
main_round0_original.pdf
SHA256=f1025e7a19e40eed7dc2608bdebad47ebed998345bc58d94aec6b27025c6b3c8
```

Immediately before this Review-B report was created, `SHA256SUMS` listed
every other paper-local file, excluded itself, and passed `sha256sum -c` with
no missing or extra pre-review artifact.  `main.pdf` and `main_round1.pdf`
were byte-identical.  The new review report is intentionally left for the
author's final Round-2 manifest regeneration, since this reviewer is not
permitted to edit author files.

The settled cold log has no unresolved citation/reference, rerun request,
build error, BibTeX warning, overfull/underfull box, or multiply defined
label.  All 28 reported font rows are embedded and subsetted with Unicode
maps.  PDF inspection reports A4, version 1.5, unencrypted, no metadata
stream, no embedded files, no form, no JavaScript, and blank title, author,
subject, and keyword fields.  Text extraction reveals no path, email, date,
acknowledgement, or personal identity; the visible author is `Anonymous`.

I rasterized and inspected all four pages at 144 dpi.  The title/abstract,
main theorem, complete repaired scheduler, image census/table, fibre and
recurrence proofs, Limitations/declarations, and all four references are
legible and within the page.  There is no clipping, overlap, blank accidental
page, corrupt glyph, unresolved marker, bad line break, or identity leak.

## 7. Findings and final decision

No unresolved Critical, Major, or Minor issue remains.  The mathematical
claims, owner subtraction, portfolio separation, exact-control provenance,
Round-1 repair history, source-only reproducibility, anonymity, and rendered
artifact all meet the internal protocol.

**Final verdict: ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor /
HOLD_EXTERNAL.**

