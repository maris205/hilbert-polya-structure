# Hostile Review A — P127 odd-outdegree transpose dynamics

**Role:** first independent nonauthor manuscript reviewer  
**Review date:** 2026-08-31 UTC  
**Object reviewed:** frozen round0 package in
`papers/127-parity-transpose-looped-digraphs/`  
**External status:** **HOLD_EXTERNAL**

## Verdict

**GO_IF_REPAIRED / round0 is not yet signable.**  I found no counterexample
to the quotient law, temporal classification, codomain-wide fibre
trichotomy, or component formulas.  The all-`n` mathematical spine is sound,
and the `n=1` degeneracy is handled correctly.  However, two mandatory gate
repairs are not actually closed in the manuscript:

1. the advertised factorisation “second route” stops at a restatement of the
   update, contains a proof gap in its kernel/image assertion, and does not
   independently rederive a temporal conclusion; and
2. the external/internal owner firewall is weaker than the frozen contract:
   P102/P103/P125 are not named in the manuscript, the P125 separation is not
   itemized, and the already identified Chen--Ren 2026 transpose-action
   neighbor is absent from the bibliography.

There is also one visible LaTeX defect in the central quotient display.
These are repairable without changing the claim ceiling.  Until they are
repaired and rechecked, the disposition is **STOP for internal sign-off** and
**HOLD_EXTERNAL**.

## Severity summary

| severity | count | disposition |
|---|---:|---|
| CRITICAL | 0 | no theorem counterexample found |
| MAJOR | 2 | factorisation route; owner/P125 firewall |
| MINOR | 2 | malformed quotient display; support/bibliography locator consistency |

## 1. Independent reconstruction

I reconstructed the statements from the literal map, not from the verifier.
Let

```text
r=A1,  c=A^T1,  tau=1^T A1,  Phi(A)=A^T+rr^T
```

on `M_n(F_2)`, `n>=1`.

### 1.1 Rank wording and graph translation

The correction `rr^T` has rank zero when `r=0` and rank one otherwise, so
“rank-at-most-one” is the exact term.  The manuscript uses that wording in
the definition.  Its graph description is also literal: `rr^T` toggles all
ordered pairs, loops included, whose two endpoints have odd current
outdegree, after transposition reverses every arc.

One boundary wording remains inaccurate: the abstract calls the even-case
left factor an “involutory transvection.”  When `r=0` it is the identity, not
a nontrivial transvection.  The precise phrase is **“the identity or an
involutory transvection.”**

### 1.2 Margin quotient

For `B=Phi(A)`, direct multiplication gives

```text
r(B)=c+tau r,
c(B)=r+tau r=(1+tau)r,
tau(B)=1^T c+tau 1^T r=tau+tau^2=0.
```

Thus every image has even total parity.  On the even hyperplane `H_n`, the
margin pair swaps.  This proves the displayed quotient law exactly.

For `A in H_n`, a second step gives

```text
Phi^2(A)=A+rr^T+cc^T.
```

The added matrix has zero row and column margins, so repeating the same two
steps cancels it and `Phi^4(A)=A`.  If `r!=c`, then `rr^T!=cc^T` because the
diagonal of `vv^T` is `v`; hence the period is exactly four.  If `r=c`, the
period divides two.  Once surjectivity onto `H_n` is supplied by the fibre
theorem, `H_n` is exactly the recurrent set and every odd-total state has
exact entrance depth one.  The forward reference from Theorem 2.2 to
Theorem 3.1 is logically harmless.

### 1.3 Complete fibre trichotomy

For an arbitrary codomain target `B`, a proposed preimage with row margin
`r` must be

```text
A=B^T+rr^T,
r=c(B)+(1^T r)r.
```

The second equation has exactly the following solutions.

- If `r` has even weight, then `r=c(B)`; consistency requires
  `tau(B)=0`, and this gives one even solution.
- If `r` has odd weight, cancellation forces `c(B)=0`; then every one of the
  `2^(n-1)` odd vectors works.
- A target with `tau(B)=1` has neither kind of solution.

Therefore

```text
0                         if tau(B)=1,
1                         if tau(B)=0 and c(B)!=0,
2^(n-1)+1                 if tau(B)=0 and c(B)=0.
```

The manuscript states and proves this **codomain-wide** law correctly.  The
large-target count is also correct: `c(B)=0` means every one of the `n`
columns has even parity, giving
`(2^(n-1))^n=2^(n(n-1))` targets.  As a global consistency check,

```text
2^(n(n-1))(2^(n-1)+1)
 + (2^(n^2-1)-2^(n(n-1))) = 2^(n^2),
```

so the fibre masses recover the full domain.

### 1.4 The `n=1` boundary

The two literal states are

```text
Phi([0])=[0],   Phi([1])=[0].
```

Thus target `[0]` has the large fibre of size `2`, target `[1]` has the zero
fibre, and there is no unit-size fibre at `n=1`.  The component formulas give

```text
F_1=1,  C_(2,1)=0,  C_(4,1)=0,
depth-one states=1,  zeta=(1-z)^(-1).
```

All agree with the manuscript and canonical output.  The separate empty
`n=0` convention is also correctly excluded from the half-hyperplane
formulas.

### 1.5 Prescribed margins, fixed points, and cycles

The `(n-1)x(n-1)` free-core proof gives `2^((n-1)^2)` matrices for each
feasible pair `(u,v)` with equal total parity, including `n=1`.  Hence the
number of recurrent matrices with equal even margins is

```text
2^(n-1) 2^((n-1)^2)=2^(n(n-1)).
```

A fixed point satisfies `A+A^T=rr^T`; the zero diagonal on the left forces
`r=0`.  A symmetric zero-row-sum matrix is uniquely determined by its
`n(n-1)/2` off-diagonal entries, so

```text
F_n=2^(n(n-1)/2),
C_(2,n)=(2^(n(n-1))-F_n)/2,
C_(4,n)=(2^(n^2-1)-2^(n(n-1)))/4.
```

The zeta product uses cycle counts rather than periodic-point counts and is
therefore correctly

```text
(1-z)^(-F_n) (1-z^2)^(-C_(2,n)) (1-z^4)^(-C_(4,n)).
```

## 2. MAJOR findings and required repairs

### M1. The factorisation is not yet a closed second route

The identity

```text
Phi(A)=(I+r1^T)A^T
```

is correct.  With `L_r=I+r1^T`, one has

```text
L_r^2=I+tau r1^T.
```

However, Proposition 3.2 currently does not prove everything it states.  In
the odd case it notes `L_r r=0` and `im(L_r) subset 1^perp`, then concludes
that the rank is `n-1`.  Those two inclusions alone show only
`nullity>=1` and `rank<=n-1`; equality still needs an argument.  The minimal
repair is the one-line implication

```text
L_r x=0  =>  x=r(1^T x),
```

which gives `ker L_r=<r>` (and `r!=0` because `tau=1`), followed by
rank--nullity and hence `im L_r=1^perp`.

More importantly, the proposition merely rewrites the definition and
classifies `L_r`; the following sentence says it “independently explains”
the collapse, but no core temporal identity is actually derived by this
route.  This does not meet the frozen requirement for a genuinely second
factorisation proof.

**Required repair:** after closing the kernel/image proof, use the factors to
rederive at least one central all-`n` conclusion without citing the margin
proof.  A compact sufficient route is:

```text
1^T L_r=(1+tau)1^T,       det(L_r)=1+tau,
```

so the odd factor is the projection onto `1^perp` and the even factor is
invertible/self-inverse; then, for `tau=0`, write

```text
Phi^2(A)=L_c A L_r^T
        =(I+c1^T)A(I+1r^T)
        =A+cc^T+rr^T
```

and recover the fourth iterate from this product route.  Explicitly connect
the later fixed-space calculation to this route or give its short
factorised analogue.  Also change “involutory transvection” to “identity or
involutory transvection.”  No new claim is needed.

### M2. The mandatory owner/internal firewall is incomplete in the paper

The prose names three earlier mechanisms only descriptively (“an involution
norm, double adjugation, and a quadratic F2-state shear”).  The frozen plan
says P102/P103/P125 receive **explicit** zero credit, and the hostile gate
requires a point-by-point P125 firewall.  The PDF never prints those
identifiers and never records the carrier/quotient distinction.  This is a
support-to-manuscript mismatch, not merely a stylistic preference.

**Required internal repair:** name P102, P103, and P125 in the manuscript.
For P125 state the actual obstruction to conjugacy and template subtraction:

- P125 acts on pairs in a nonsingular quadratic space; P127 acts on all
  `n x n` binary matrices.
- P125 has transients of depth two and period three; P127 has depth at most
  one and recurrent periods only `1,2,4`.
- P125 uses a quadratic/polar three-bit quotient; P127 uses the
  `(2n-1)`-dimensional feasible row/column-margin quotient.
- Generic quotient/fibre/component/zeta packaging receives zero credit.

The external bibliography also omits a primary neighbor already identified
by the owner gate: Yin Chen and Shan Ren, *Modular matrix invariants under
some transpose actions*, **Finite Fields and Their Applications 113 (2026),
102824**, DOI
[10.1016/j.ffa.2026.102824](https://doi.org/10.1016/j.ffa.2026.102824).
It studies modular invariant rings under transpose actions, not this literal
state-dependent finite map, but its transpose-action interface must be cited
and zero-credited.  The bounded search still supplies no direct literal-map
owner; that non-hit is not novelty clearance.

The local/pivot/loop/subgraph-complementation sources currently cited are
appropriate adjacent primary sources and are already assigned zero credit.
Retain that subtraction.  Give the Koch--Pardal--dos Santos preprint a
visible locator in the PDF (for example
`https://arxiv.org/abs/2502.15675`); its current BibTeX `eprint` field is not
rendered by `plainnat`.

## 3. MINOR findings

### m1. Central quotient display has a visible literal typo

Source line 110 contains a bare `qquad` before `tau(B)=0`, rather than
`\qquad`.  Page 1 and `pdftotext` therefore visibly print

```text
c(B)=(1+tau)r, qquad tau(B)=0.
```

Repair the missing backslash and inspect the rebuilt page.

### m2. Support claims presently overstate closure

`PAPER_PLAN.md` describes the P102/P103/P125 subtraction as explicit and the
factorisation as an independent second route, while the current PDF does not
yet satisfy either description.  After the manuscript repairs, update the
improvement/build evidence to map those exact paragraphs and record fresh
source/PDF hashes.  Do not mark the gate items closed solely in support files.

## 4. Mechanical and visual evidence

### Fresh exact verifier

I reran the paper-local verifier and compared fresh stdout byte-for-byte with
the canonical transcript.  Result: `cmp=0`.

```text
n=1: states=2, image=1, zero/unit/large targets=1/0/1,
     large fibre=2, fixed=1, C2=0, C4=0
n=2: states=16, image=8, zero/unit/large targets=8/4/4,
     large fibre=3, fixed=2, C2=1, C4=1
n=3: states=512, image=256, fixed=8, C2=28, C4=48
n=4: states=65536, image=32768, fixed=64, C2=2016, C4=7168
ASSERTIONS=1271047
STATUS=PASS
```

Pinned hashes from the review run:

```text
58ea6c04eb35a43d1805128584a2c4c61f34e237dbccf6ab32bfd793a17692f8  code/verify.py
53ec418b88941cad406b24cca6837818a36e69ed3ebb0194219b4c09fbea67b1  code/verification_output.txt
53ec418b88941cad406b24cca6837818a36e69ed3ebb0194219b4c09fbea67b1  fresh stdout
```

### Isolated build

I copied only `main.tex` and `references.bib` into a fresh temporary
directory and ran

```text
pdflatex -> bibtex -> pdflatex -> pdflatex.
```

All four stages returned status `0`.  The final log had no warning,
overfull/underfull box, undefined citation/reference, or rerun request.  The
isolated PDF was byte-identical to both `main.pdf` and
`main_round0_original.pdf`:

```text
13608e8ae2dde7521a97c0c6b5548504831fa84da2fcf1b3797f58a06c70c2ea  main.tex
b46d0556c8884600a39be818f8c122e3db9afd045520890fc56a1f3667df2b31  references.bib
9ba5ea88ead104331d4bfbde46479e1ad17fb23553c593595b116406d40cb8bf  main.pdf
9ba5ea88ead104331d4bfbde46479e1ad17fb23553c593595b116406d40cb8bf  main_round0_original.pdf
```

`pdfinfo` reports 3 A4 pages and blank Title, Subject, Keywords, and Author
metadata.  Every font is embedded.  I rasterized and inspected all three
pages: there is no clipping, collision, or unreadable bibliography.  The
bare-`qquad` defect above is the only visible typesetting error found.

## 5. Re-entry test and claim ceiling

The allowed claim ceiling remains unchanged:

1. the literal map and exact margin quotient for `n>=1`;
2. the even hyperplane as image and complete recurrent set, with odd states
   at exact depth one;
3. the second/fourth-iterate identities and periods `1,2,4`;
4. the full codomain fibre trichotomy;
5. fixed, two-cycle, four-cycle, depth-one, and fixed-`n` zeta formulas.

No generic rank-one dynamics, transpose action, complementation operation,
binary-margin count, quotient/fibre/zeta template, general-field extension,
novelty, or priority claim is allowed.

**GO_INTERNAL on re-entry only if all of the following are visible in the
rebuilt manuscript/PDF:**

- the factor kernel/image proof is complete and the factorisation route
  independently rederives a temporal identity;
- the identity/transvection boundary is exact;
- P102/P103/P125 are explicitly itemized, with the P125 carrier, temporal,
  and quotient separation;
- Chen--Ren 2026 is cited and zero-credited, and the 2025 preprint has a
  visible locator;
- the `qquad` defect is gone;
- the unchanged verifier has a fresh canonical match, and an isolated
  four-stage build plus all-page visual audit passes.

Until that re-entry succeeds: **STOP / HOLD_EXTERNAL**.
