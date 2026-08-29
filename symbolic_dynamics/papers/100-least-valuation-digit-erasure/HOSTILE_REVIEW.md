# Internal hostile review — P100

Audit date: 2026-08-29 UTC.
Disposition after repair: **internal GO / external HOLD**.

Round 1 was the primary author's independent proof/control audit. Round 2
was a read-only cross-review by the completed P97 reviewer. The second pass
found a direct binary owner that materially narrowed the contribution. This
ledger is internal adversarial review, not external peer review.

## Round 1 — proof and control attack

The first pass reconstructed the no-borrow digit rule, derived the complete
depth polynomial both by digit factorization and inclusion–exclusion, and
checked the moments, local-limit normalization, fixed data, and parameter
recovery. It also made the standard-representative section explicit, so the
map is not misdescribed as a representative-independent ring operation.

Implemented first-pass repairs included:

1. the unimodality proof was expanded from a verbal convolution claim to a
   moving-window difference argument;
2. the arithmetic erasure implementation was rewritten to preserve the
   original representative visibly before subtracting the selected place;
3. the control report was anchored to five exhaustive lanes and exact
   rational moments.

The repaired run passed **46,319,420 exact assertions**.

## Round 2 — direct owner and endpoint attack

Initial verdict:

- **CRITICAL:** 0.
- **MAJOR:** 1 ownership/scope issue, not a mathematical error.
- **MINOR:** 3.

### Major owner finding and repair

At $p=2$,
\[
E_{2,r}(x)=x-2^{v_2(x)}=x\mathbin{\&}(x-1),
\]
which is Peter Wegner's 1960 rightmost-one clearing step; its absorption time
is binary popcount. The first draft had not cited this direct specialization
and described the normal form too broadly as a residual contribution.

The final manuscript now cites Wegner's original Communications of the ACM
paper (DOI **10.1145/367236.367286**), expressly declines the binary
bit-clearing/popcount identity, and narrows the residual contribution to the
general-prime standard-representative family, full transient polynomial,
parameter recovery, and periodic-blindness synthesis. The bounded-search
sentence now concerns only that combined package and grants no priority.

### Minor findings and repairs

1. The unimodality induction now includes the $r=1$ base case, defines
   $C_r=(p-1)r/2$, and proves the required centre-distance inequality for
   integer and half-integer centres.
2. The control prose now describes what the code actually does: an
   exhaustive arithmetic-orbit histogram cross-checked against convolution
   and inclusion–exclusion. It records the exact assertion total.
3. The Artin–Mazur identity is explicitly placed in $\mathbb Q[[z]]$.

The reviewer then performed a read-only closure check and returned **PASS**:
all four reported findings were closed, all four citations resolved, the
PDF was newer than the source, and the final log was clean.

## Final risk and verdict

- **Mathematics:** low after exact orbit enumeration and independent
  rederivation.
- **Scope:** low after the binary owner subtraction.
- **Literature/priority:** medium for equivalent general-base algorithms or
  finite-dynamics packaging under different terminology.
- **Verdict:** GO for internal Route-A use; external posting, submission,
  contact, and absolute priority language remain HOLD.
