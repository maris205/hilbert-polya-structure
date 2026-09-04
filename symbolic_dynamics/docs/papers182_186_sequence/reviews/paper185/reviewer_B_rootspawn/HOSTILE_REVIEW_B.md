# Hostile Review B — P185 prefix-diversity delay

**Reviewer process:** `/root/reviewer_b_p185_p186`, process-separated from the
P185 author and P185 Review A  
**Review date:** 2026-09-03 UTC  
**Frozen input:** immutable Round 1  
**Decision:** `ACCEPT_ROUND1_FOR_COORDINATOR_GATE`  
**External lifecycle:** `HOLD_EXTERNAL`

## Bottom line

The Round-1 theorem package is provable as stated.  I found zero Critical,
Major, and Minor defects after reopening the all-time delay law, all clock and
image ranges, every-target products, empty-product and stabilized boundaries,
the `n=1,2,3` carriers, deepest-set descriptions, repaired wording, sources,
ownership language, and artifact state.

This review authorizes only the next internal coordinator gate.  It does not
authorize circulation or submission, and it does not convert a bounded owner
search non-hit into novelty, priority, completeness, freedom-to-operate, or
validated-subclass evidence.  P185 remains `OWNER_AMBER / HOLD_EXTERNAL`.

This is process separation, not a claim of statistically independent error
processes.  The author, Review A, and Review B share the theorem contract and
Python runtime even though their state representations are different.

## Frozen binding and read-only discipline

No file under `papers/185-prefix-diversity-delay/` was edited.  This review
binds the following objects:

| frozen object | SHA-256 |
|---|---|
| `main.tex` | `e17e073a15d839a3178bc5ed922227bd24cea41d4c6ceff4e6066090651da6f6` |
| `main_round1.pdf` | `fcd6257debd3a3e8744571a390296fe02566cc6655957011778400582bea03c3` |

The live `main.pdf` is byte-identical to Round 1.  The immutable Round-0 PDF
still has SHA-256
`45a2ce36879d17dafb42fd4a08c2afbc6213c8c140ffdee145f4e27f4c8a9129`.
The four-row Review-A manifest passes.  Review A's delta record binds the same
Round-1 hashes and closes its one historical Minor finding.

The paper-local fifteen-row manifest remains intentionally Round-0-bound at
this intermediate stage: thirteen rows pass, while only the repaired
`main.tex` and rebuilt live `main.pdf` rows retain their Round-0 hashes.  This
is not a mathematical finding against the frozen Round-1 object, but it is an
explicit terminal-QA obligation.  The coordinator must regenerate the final
paper manifest after Round 2; external release remains blocked if that does
not occur.

## Reviewer-owned representation

The verifier imports neither earlier verifier and uses neither of their state
spaces:

- the author enumerates all labelled words in `[n]^n`;
- Review A enumerates equality partitions as weighted restricted-growth
  strings;
- Review B enumerates only the binary rise/flat automaton of the first image
  `d=P_n(w)` and attaches exact transition weights.

For `n>=2`, a path has `d_0=0`, `d_1=1`, and `n-2` free binary increments.
If the current distinct-letter count before source position `q` is `d_q`, a
rise has multiplicity `n-d_q` and a flat has multiplicity `d_q`.  The first
and last source letters contribute `n^2`.  Hence each binary path represents

\[
 n^2\prod_{q=1}^{n-2}
 \bigl((n-d_q)\mathbf 1_{\Delta d_q=1}
       +d_q\mathbf 1_{\Delta d_q=0}\bigr)
\]

labelled words.  The weights sum to `n^n` in every exhaustive box.  The
all-rise aggregate is handled without losing the exceptional identity word:
one unit is placed at depth zero and its remaining weight at depth one.

This representation is smaller than both prior state spaces and does not
store equality blocks or letter labels.  A separate transfer recurrence by
the current number of seen letters checks total mass through `n=80`.

## Exact audit coverage

The reviewer control exhausts all weighted novelty paths for `1<=n<=18`,
literal feedback on each path through `t=n+3`, all image targets, every
positive target fibre, the zero-fibre complement by exact image-set equality,
and all clock strata.  It makes **3,677,711 exact assertions**.  At `n=18`,
only 65,536 paths represent all `18^18` labelled words, and all 65,536
time-one targets are checked individually.

Two fresh processes reproduced `CANONICAL.txt` byte for byte.  Each transcript
has SHA-256
`6331595b010aadf421f33d8e6a22deb06303da84131cb1ac792153527afb9ca0`.

## Hostile theorem audit

### 1. All-time delay normal form

For any zero-one-rise path `d`, its prefix through `d_{i-1}` contains every
integer from zero through `d_{i-1}`.  Literal feedback on the path therefore
satisfies

\[
 Q(d)_0=0,\qquad Q(d)_i=d_{i-1}+1.
\]

Repeated application inserts one identity coordinate and shifts the retained
path.  The control compares this literal set-based feedback with the displayed
formula for every weighted path and every `1<=t<=n+3`.  It explicitly reaches
the `r>=n` branch rather than stopping at the transient range.

**Verdict:** survives.

### 2. Images, recurrence, and the pointwise clock

At time `t`, exactly the final `n-t-1` increments remain free when
`1<=t<=n-1`, giving the manuscript's identity prefix and
`2^(n-t-1)` images.  Direct set equality between literal weighted endpoints
and the independently constructed path language holds at every tested time;
therefore every other carrier target has zero predecessors.

The first flat at source position `q` makes the exact positive entrance time
`n-q`.  If no visible flat occurs, the aggregate reaches the identity in one
step; separating the literal identity word gives depth zero exactly once.
This recovers the manuscript's longest-distinct-prefix clock without orbit
peeling.  All states reach the identity, so there is no nonfixed recurrent
state.

For `n>=3`, maximum depth occurs exactly when the first decision is flat.  At
that point only `w_0` has been seen, so flatness is exactly `w_1=w_0`; the
remaining letters are arbitrary.  The control recovers `n^(n-1)` such words.
It separately obtains one state of depth zero for `n=1`, and three depth-one
nonidentity words for `n=2`.

**Verdict:** survives.

### 3. Depth CDF and its ranges

Entrance by time `t` is equivalent to the first `n-t` source letters being
distinct.  The weighted path census agrees at each `1<=t<=n-1` with

\[
 (n)_{n-t}n^t.
\]

It also agrees target-by-target with the fibre of the identity.  The repaired
abstract now carries the transient range and never applies this expression to
a negative falling-factorial index.  At `t=0`, only the identity word has
depth zero; at and after `t=n-1`, the CDF is the full carrier `n^n`.

**Verdict:** survives.

### 4. Every-target products and all boundary times

A time-`t` target fixes precisely the visible novelty decisions
`q=1,...,n-t-1`.  The first letter contributes `n`; summing each of the `t`
unseen source coordinates over “fresh” and “old” choices contributes `n^t`.
This gives the exact leading factor `n^(t+1)` and the displayed local product.
The weighted automaton constructs predecessor counts before invoking the
claimed product, then compares every reachable target individually.

The endpoint audit is explicit:

- `t=0`: the identity relation has the full `n^n` image and unit fibres;
- `t=1`: every visible rise/flat factor is exercised;
- `t=n-1`: the product is empty and the identity fibre is `n^n`;
- `t=n,n+3`: the same single target and full fibre persist;
- `n=1`: time zero and stabilization coincide on the one-state carrier;
- `n=2,3`: all exceptional deepest-set statements and empty products are
  checked directly.

Fibre mass is `n^n` at every tested time.  No division by average image size
is used.

**Verdict:** survives.

## Source and owner-language audit

Both bibliography keys resolve and are used only for subtracted background.
The [Mansour--Vajnovszki ScienceDirect record](https://www.sciencedirect.com/science/article/abs/pii/S0020019013001427)
supports statistic-restricted growth words and Gray-code generation, while the
[Wachs ScienceDirect record](https://www.sciencedirect.com/science/article/pii/0097316594901171)
supports the classical restricted-growth/set-partition interface.  Neither is
cited as a proof of the autonomous feedback theorem.

Review B reran four bounded exact-phrase/structural web queries:

1. `"prefix-diversity" iteration fibre word dynamics`;
2. `"prefix diversity" "dynamical system" word`;
3. `"strict prefix" "number of distinct" iteration word`;
4. `map word "distinct letters" prefix iterate finite dynamics`.

The returned items concerned unrelated automata, language prefix diversity,
and other symbolic maps; no literal or equivalent owner was identified.  This
is a bounded public-web non-hit only.  It is not a professional database or
citation-chain search, and it supplies no novelty, priority, completeness, or
freedom-to-operate conclusion.

The manuscript explicitly subtracts restricted-growth vocabulary,
first-occurrence patterns, prefix statistics, falling factorials, and generic
finite-map bookkeeping.  It retains `OWNER_AMBER`, calls the owner search
bounded, and states that the non-hit is neither novelty nor priority evidence.

**Verdict:** sources and lifecycle wording survive; `HOLD_EXTERNAL` retained.

## Artifact and declaration audit

The frozen Round-1 PDF is 273,283 bytes, three A4 pages, unencrypted, and has
no JavaScript.  All 22 font rows are embedded and subset.  Its metadata title
and author fields are blank.  Text extraction finds both owner/hold notices,
data availability, ethics, and AI-use declarations.  The current LaTeX and
BibTeX logs contain no undefined references/citations, warning diagnostics, or
bad boxes.

The source is anonymous, contains the repaired `t=0`, `t=n-1`, and
post-height wording, and makes no claim that finite verification proves an
all-parameter theorem.

## Findings ledger

### Critical findings (0)

None.

### Major findings (0)

None.

### Minor findings (0)

None.

No manuscript repair is requested.  A byte-identical Round-2 receipt is
acceptable.  Any content change for another reason reopens every proof,
source, artifact, and reproducibility gate.

## Residual risks that are not findings

1. Finite automaton checks are bounded falsification pressure, not a proof of
   the all-`n,t` claims; the written induction carries those quantifiers.
2. Process separation and representation diversity do not establish
   statistically independent errors.
3. The paper-local manifest must be regenerated at terminal QA after the
   staged Round-1 repair.
4. Ownership remains amber pending a deeper database and citation-chain
   search.

## Reproduction

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers182_186_sequence/reviews/paper185/reviewer_B_rootspawn/verify_review_b_p185.py
```

The byte-for-byte expected transcript is `CANONICAL.txt`.  `SHA256SUMS`
binds the report, delta template, verifier, and canonical transcript while
deliberately excluding itself.

