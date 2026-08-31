# Hostile Review B — P127 odd-outdegree transpose dynamics

**Role:** second independent nonauthor reviewer  
**Review date:** 2026-08-31 UTC  
**Object reviewed:** repaired round1 package in
`papers/127-parity-transpose-looped-digraphs/`  
**External status:** **HOLD_EXTERNAL**

## Verdict

**GO_INTERNAL.**  I independently reconstructed the update, quotient,
factor-product route, codomain-wide fibres, temporal classification, margin
count, and component formulas from the round1 manuscript.  I found no false
statement, missing quantifier, or unclosed boundary.  In particular, the
singular factor now has an exact kernel/image proof, the even factor has the
correct identity/transvection split, and `L_c A L_r^T` independently yields
both the second and fourth iterates.  The full codomain law includes
zero-fibre targets, and the `n=1` degeneration is correct.

The internal P102/P103/P125 firewall is sufficient and mathematically
accurate.  Chen--Ren 2026 is cited as a static transpose-action neighbor,
the Koch--Pardal--dos Santos preprint has a visible locator, and the former
bare `qquad` is absent from both source and rendered quotient display.
Fresh control, isolated build, every-page visual inspection, fonts, and
anonymous metadata all pass.

This is an internal theorem/package decision only.  The literature audit is
bounded, so novelty, priority, posting, submission, and external circulation
remain **HOLD_EXTERNAL**.

## Severity summary

| severity | count | disposition |
|---|---:|---|
| CRITICAL | 0 | no counterexample or invalid theorem |
| MAJOR | 0 | every round1 re-entry condition is closed |
| MINOR | 0 | no manuscript or artifact repair required |

## 1. Independent reconstruction of the algebra

### 1.1 Literal update and quotient

For `A in M_n(F_2)`, put

```text
r=A1,  c=A^T1,  tau=1^T A1,
Phi(A)=A^T+rr^T.
```

The graph wording is literal: transpose reverses every ordered arc, and
`rr^T` toggles all ordered pairs, including loops, whose two vertices have
odd pre-update outdegree.  The correction has rank zero for `r=0` and rank
one otherwise, so “rank-at-most-one” is exact.

For `B=Phi(A)`, direct multiplication gives

```text
r(B)=c+tau r,
c(B)=r+tau r=(1+tau)r,
tau(B)=1^T(c+tau r)=tau+tau^2=0.
```

Thus every image has even total parity.  On
`H_n={A:tau(A)=0}`, the margin pair swaps.  The source and rendered PDF both
show the third equality as `tau(B)=0`; there is no bare `qquad` token.

### 1.2 Temporal classification

On `H_n`, a second literal update gives

```text
Phi^2(A)=A+rr^T+cc^T.
```

Because `1^T r=1^T c=0`, the correction has zero row and column margins.
Applying the same two-step identity again adds it a second time, so
`Phi^4(A)=A`.  The fibre theorem below supplies `H_n subset im(Phi)`, while
the quotient gives the reverse inclusion.  Hence `H_n` is both the image and
the complete recurrent set; every odd-total state enters it at exact depth
one.

If `r!=c`, then `rr^T!=cc^T` because the diagonal of `vv^T` is `v` over
`F_2`.  Such a state is not fixed by the second iterate and therefore has
exact period four.  If `r=c`, the second iterate is the identity and the
period is one or two.  No temporal case is omitted.

### 1.3 Full codomain fibre law

For a prescribed target `B`, a proposed preimage with row margin `r` must be

```text
A=B^T+rr^T,
r=c(B)+(1^T r)r.
```

If `r` has even weight, the equation forces `r=c(B)` and is consistent
exactly when `tau(B)=0`; this gives one even solution.  If `r` has odd
weight, the two copies of `r` cancel and consistency is exactly `c(B)=0`;
then all `2^(n-1)` odd vectors work.  Therefore

```text
0                         if tau(B)=1,
1                         if tau(B)=0 and c(B)!=0,
2^(n-1)+1                 if tau(B)=0 and c(B)=0.
```

This is genuinely codomain-wide, not an image-only statement.  Targets with
`c(B)=0` have all columns even, so there are
`(2^(n-1))^n=2^(n(n-1))` large-fibre targets.  The global mass check is

```text
2^(n(n-1))(2^(n-1)+1)
 + (2^(n^2-1)-2^(n(n-1))) = 2^(n^2).
```

### 1.4 The `n=1` boundary

The two literal states satisfy

```text
Phi([0])=[0],  Phi([1])=[0].
```

Thus `[0]` has the large fibre of size two, `[1]` has zero preimages, and
there is no unit fibre.  The recurrent set is `{[0]}`; `[0]` is fixed and
`[1]` has exact depth one.  The formulas give

```text
F_1=1,  C_(2,1)=0,  C_(4,1)=0,
zeta=(1-z)^(-1).
```

The singular factor boundary also works: for `r=[1]`, `L_r=[0]` has rank
zero, kernel `<r>`, and image `1^perp={0}`.  The manuscript separately
declares the unique `n=0` state fixed and correctly restricts the displayed
closed formulas to `n>=1`.

## 2. Factor-product re-entry

Set `L_r=I+r1^T`.  Since `1^T A^T=r^T`,

```text
Phi(A)=L_r A^T.
```

Direct multiplication and the matrix determinant lemma give

```text
L_r^2=I+tau r1^T,
1^T L_r=(1+tau)1^T,
det(L_r)=1+tau.
```

### Even branch

When `tau=0`, `L_r^2=I`.  If `r=0`, then `L_r=I`; if `r!=0`, then
`L_r-I=r1^T` has rank one and `1^T r=0`, so `L_r` is a nontrivial
involutory transvection.  The round1 wording “the identity when `r=0` and an
involutory transvection otherwise” is exact, including `n=1`.

### Odd branch

When `tau=1`, `L_r^2=L_r` and

```text
L_r x=0  <=>  x=r(1^T x).
```

Here `r!=0` and `L_r r=0`; the displayed equivalence gives
`ker(L_r)=<r>` rather than merely an inclusion.  Rank--nullity yields rank
`n-1`.  Since `1^T L_r=0`, its image lies in `1^perp`, which also has
dimension `n-1`; hence `im(L_r)=1^perp`.  This fully proves the stated
idempotent projection.

### Independent temporal route

For even `tau`, let `B=L_r A^T`.  Multiplication of this product and its
transpose by `1` gives row/column margins `c,r` without citing the temporal
theorem.  Therefore

```text
Phi^2(A)=L_c B^T=L_c A L_r^T.
```

Expanding produces

```text
A + c(1^T A) + (A1)r^T + c(1^T A1)r^T
= A + cc^T + rr^T,
```

because the mixed term is `c tau r^T=0`.  The correction has zero margins,
so the same factor-product calculation adds it once more, proving
`Phi^4(A)=A` in characteristic two.  This is now a genuine second route,
not a restatement of the quotient proof.

## 3. Component formulas

For feasible row/column margins `(u,v)`, an arbitrary
`(n-1)x(n-1)` core uniquely forces the last row and column, and the
bottom-right requirements coincide exactly when `1^T u=1^T v`.  Thus every
feasible pair has `2^((n-1)^2)` matrices, including `n=1`.

A fixed point satisfies `A+A^T=rr^T`.  The left diagonal is zero, so `r=0`;
then a symmetric zero-row-sum matrix is determined freely by its
`n(n-1)/2` off-diagonal entries.  Hence

```text
F_n=2^(n(n-1)/2).
```

The states with period dividing two are exactly those with equal even
margins, numbering
`2^(n-1) 2^((n-1)^2)=2^(n(n-1))`.  Removing fixed points and dividing by two
gives `C_(2,n)`; the remaining recurrent points have exact period four, so
dividing by four gives `C_(4,n)`.  The odd half-space consists exactly of
the `2^(n^2-1)` depth-one states.  The zeta product correctly uses cycle
counts, not periodic-point counts.

## 4. Internal and external firewall audit

### P102

P102 iterates the involutive norm `a -> aa*` on a split cyclic group algebra
over a finite field.  Its Fourier blocks synchronize and square, and its
depth depends on the 2-adic part of `q-1`.  P127 instead acts on all binary
square matrices by transpose plus a recomputed row-parity outer product;
its quotient is the feasible margin space and its tail is at most one.  The
carriers, literal updates, quotients, and temporal laws differ.  P102 is
named and receives zero credit in the manuscript.

### P103

P103 uses `A -> adj(adj A)=det(A)^(d-2) A` for `d>=3` over `F_q`: singular
rank strata collapse to zero and invertible projective lines carry scalar
power maps.  P127 uses neither determinant nor adjugation, and its odd-total
half-space maps onto a large recurrent hyperplane rather than a single
singular basin.  P103 is named and receives zero credit.  Generic matrix,
power-map, component, and zeta packaging is also subtracted.

### P125

P125 acts on pairs in a nonsingular quadratic space.  Its engine is the
quadratic/polar three-bit quotient; it has a genuine depth-two layer and
period-three states (as well as other periods).  P127 acts on the full
`n^2`-dimensional matrix carrier, has the `(2n-1)`-dimensional feasible
row/column-margin quotient, exact maximum tail one, and recurrent periods
only `1,2,4`.  These carrier, quotient, tail, and period invariants rule out
conjugacy.  All four distinctions and the zero-credit generic packaging are
visible in round1.

### Chen--Ren and Koch--Pardal--dos Santos

Chen and Ren study modular invariant rings for group actions
`M -> g M g^T` on full `2x2` matrix spaces, not this state-dependent
iteration.  Round1 cites the published 2026 paper, gives the correct authors,
venue, volume, article number, and DOI, and assigns the interface zero
credit.  Primary record checked 2026-08-31:
[DOI 10.1016/j.ffa.2026.102824](https://doi.org/10.1016/j.ffa.2026.102824).

The Koch--Pardal--dos Santos static subgraph-complementation neighbor is
cited and zero-credited.  Because `plainnat` does not render its `eprint`
field, round1 also prints the visible locator
[arXiv:2502.15675](https://arxiv.org/abs/2502.15675).  The title and authors
match the primary record checked 2026-08-31.

The bounded search did not identify the literal P127 update.  This non-hit
cannot establish novelty or priority, and the manuscript says so.

## 5. Fresh exact control

I reran the deterministic paper-local verifier from the repaired snapshot
and compared fresh stdout byte-for-byte with the canonical transcript.
Result: `cmp=0`.

```text
n=1 states=2 image=1 zero/unit/large targets=1/0/1
    large fibre=2 fixed=1 C2=0 C4=0
n=2 states=16 image=8 zero/unit/large targets=8/4/4
    large fibre=3 fixed=2 C2=1 C4=1
n=3 states=512 image=256 zero/unit/large targets=256/192/64
    large fibre=5 fixed=8 C2=28 C4=48
n=4 states=65536 image=32768 zero/unit/large targets=32768/28672/4096
    large fibre=9 fixed=64 C2=2016 C4=7168
ASSERTIONS=1271047
STATUS=PASS
```

The verifier exhausts every domain and codomain matrix for `1<=n<=4`; it
checks the literal and factored updates, quotient, second/fourth iterates,
exact depth and period, all zero/unit/large fibres, margin counts, and the
component census.  This remains finite falsification evidence only.

Review-run hashes:

```text
58ea6c04eb35a43d1805128584a2c4c61f34e237dbccf6ab32bfd793a17692f8  code/verify.py
53ec418b88941cad406b24cca6837818a36e69ed3ebb0194219b4c09fbea67b1  code/verification_output.txt
53ec418b88941cad406b24cca6837818a36e69ed3ebb0194219b4c09fbea67b1  fresh stdout
```

## 6. Isolated build and PDF QA

I copied only `main.tex` and `references.bib` into a fresh temporary
directory and ran

```text
pdflatex -> bibtex -> pdflatex -> pdflatex.
```

Every stage returned status zero.  The settled log and BibTeX transcript have
no errors, warnings, undefined citation/reference, rerun request, or
overfull/underfull box.  The isolated PDF is byte-identical to the working
and round1 PDFs:

```text
ede8031b5c8fb5bf4e91de83977ccb41690df236c5f700d89469c2e293e971ea  main.tex
30fce2e9337ef4742394ae1023fc90cc5c7cd54e22274be3636df8b74699ceb0  references.bib
107d6baa4063d747799f26710bc1de0bc0eb8a7460509e9d8beafe570f760f0d  isolated main.pdf
107d6baa4063d747799f26710bc1de0bc0eb8a7460509e9d8beafe570f760f0d  main.pdf
107d6baa4063d747799f26710bc1de0bc0eb8a7460509e9d8beafe570f760f0d  main_round1.pdf
```

The immutable round0 PDF remains separately preserved at
`9ba5ea88ead104331d4bfbde46479e1ad17fb23553c593595b116406d40cb8bf`
(325,507 bytes); round1 is 328,070 bytes.

`pdfinfo` reports 3 A4 pages, rotation zero, no encryption, forms,
JavaScript, custom metadata, or metadata stream.  Title, Subject, Keywords,
and Author metadata are blank.  All 26 `pdffonts` rows are embedded,
subsetted, and Unicode-mapped.  I rasterized and inspected all three pages:
there is no clipping, collision, blank page, missing glyph, malformed
equation, unreadable reference, or anonymity leak.  The quotient display is
clean, both new references are visible, and the only displayed author is
“Anonymous.”

## 7. Final disposition and claim ceiling

The admissible internal claim ceiling is unchanged:

1. the literal binary square-matrix update and exact margin quotient;
2. image/recurrent hyperplane, exact depth, second/fourth iterates, and
   periods `1,2,4`;
3. the complete codomain fibre trichotomy;
4. prescribed-margin, fixed, two-cycle, four-cycle, depth-one, and fixed-`n`
   zeta formulas; and
5. the independent transvection/projection factor-product route.

Static local, loop, pivot, and subgraph complementation; transpose group
actions; outer-product and transvection algebra; binary-margin counts;
generic quotient/fibre/component/zeta templates; P102/P103/P125 mechanisms;
and any novelty or priority claim remain outside the contribution ceiling.

**Decision: GO_INTERNAL / HOLD_EXTERNAL.  No round1 repair is required by
Review B.**
