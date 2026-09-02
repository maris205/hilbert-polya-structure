# P154 independent hostile review B

**Review date:** 2026-09-02 UTC.  
**Reviewer relation:** independent internal reader; did not author P154 and
did not perform P154 Hostile Review A.  
**Protocol:** `docs/papers152_156_sequence/HOSTILE_REVIEW_PROTOCOL.md`.  
**External state:** `HOLD_EXTERNAL`. No manuscript content was sent to an
external model, reviewer, or service.

## Verdict

**ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor.**

The repaired Round-1 package stays within the owner-subtracted GDN theorem
ceiling. A fresh derivation found no counterexample or missing exceptional
case in the iterated forest, positive-time target fibres, iff graph signature,
or the 33/35 commuting bijection. All three Review-A findings are closed in
the source and artifacts, not merely marked closed. The cold verifier replay,
source-only five-command build, PDF inspection, historical hashes, and
pre-review manifest all pass.

This is the raw Review-B report. I did not edit any author file, verifier,
transcript, PDF, ledger, or manifest. The author still has to freeze
`main_round2.pdf` and regenerate the final all-file manifest required by the
protocol; that mechanical closure does not reopen this zero-finding verdict.

## 1. Cold package and theorem-ceiling audit

I started from `FINAL_THEOREM_CONTRACTS.md`, `GDN_FREEZE_CONTRACT.md`, the
focused and independent GDN audits, the owner and collision ledgers, and the
Round-1 package. I then read `main.tex`, `references.bib`, `verify.py`, both
transcripts, every paper-local Markdown ledger, Review A, the improvement log,
the retained build artifacts, and both historical PDFs. I did not use Review
A's mathematical derivation as a substitute for the fresh derivation below.

| Frozen interface | Round-1 evidence anchor | Review-B result |
|---|---|---|
| owned carrier and one-step normalizer, zero credit | `main.tex` (1)--(2), lines 69--109; owner table, lines 352--362 | PASS; visible credited input rather than residual value |
| exact iterates and full binary forest | (3)--(4), lines 112--131; lift atlas (10) | PASS for all carrier states, including `a=0` |
| all positive-time images and every-target fibres | (5)--(7), lines 132--151 and Section 3 | PASS, with zero targets and stabilized times included |
| iff signature `(v2(n),sigma(odd(n)),tau(n))` | (8), (13), lines 153--157 and 291--312 | PASS in both directions, including `m=1` |
| explicit 33/35 collision and all common two-power lifts | (14), lines 314--330 | PASS; literal 52-state commuting bijection independently checked |
| owner subtraction and portfolio separation | Section 5, lines 346--386 | PASS; bounded non-hit is not promoted to novelty evidence |

The manuscript does not claim group isomorphism or subgroup-lattice
isomorphism. It classifies only the unlabelled directed functional graph of
the normalizer self-map. The zeta formula remains explicitly generic
bookkeeping and is not used to inflate the paper's residual contribution.

## 2. Independent rederivation and exceptional-parameter attack

### 2.1 Carrier and one-step rule

Let `C=<r>`. A subgroup contained in `C` is uniquely `R_d=<r^d>` for a
divisor `d|n`. If a subgroup is not contained in `C`, its intersection with
`C` is a unique `R_d`; choosing one reflection `r^j s` shows that its second
coset is exactly `R_d r^j s`, with `j` unique modulo `d`. Thus the carrier has
`tau(n)+sum_{d|n}d=tau(n)+sigma(n)` distinct states.

Every `R_d` is normal. For `H_{d,j}`, conjugation by a rotation gives

```text
r^u (r^j s) r^{-u} = r^(j+2u) s,
```

so a normalizing rotation satisfies `d|2u`. A normalizing reflection satisfies
the companion congruence `d|2(u-j)`. The two normalizing cosets therefore form

```text
H_{d/gcd(d,2), j mod (d/gcd(d,2))}.
```

This covers `d=1` and involves no unsafe division. It confirms the credited
one-step bridge but supplies it no contribution credit.

### 2.2 Iteration, forest, images, and fibres

Write `n=2^a m`, with `m` odd, and `d=2^k e`. Each update removes exactly one
factor of two until level zero, proving for every `t>=0`

```text
N^t(H_{2^k e,j})
 = H_{2^max(k-t,0)e, j mod 2^max(k-t,0)e}.
```

For a fixed root residue `(e,j_0)`, its level-`k` vertices are precisely

```text
H_{2^k e, j_0 + ell e},       0 <= ell < 2^k.
```

Reduction modulo `2^(k-1)e` is two-to-one. Hence each of the `sigma(m)` roots
carries a full binary inverse tree of height `a`. Independently, every one of
the `tau(n)` rotation states is a source leaf entering `H_{1,0}` in one step.
This yields the claimed depth polynomial without merging rotation leaves with
the binary levels.

At time `t>=1`, the surviving target levels are exactly
`0,...,max(a-t,0)`, which gives

```text
|im N^t| = sigma(m)(2^(max(a-t,0)+1)-1).
```

A positive-level target at level `k` has sources only at level `k+t`. If that
level exists, its residue has exactly `2^t` lifts; otherwise the fibre is
empty. A root receives levels `0,...,min(t,a)`, giving the geometric mass
`2^(min(t,a)+1)-1`; all rotations add `tau(n)` only at `(e,j)=(1,0)`. No
positive iterate lands on a rotation. Summing the pointwise fibres gives
`sigma(n)+tau(n)` for every `t>=1`, including times after stabilization.

### 2.3 Signature necessity, including `a=0/1` and `m=1`

An unlabelled directed graph isomorphism preserves loops, so the number of
fixed vertices recovers `sigma(m)`. Let `L` be the maximum transient tail.
When `L>=2`, rotation leaves cannot create that length, and `a=L`.

When `L=1`, only `a=0` and `a=1` are possible. For either value, `n>=3`
forces the relevant odd part to exceed one, so a nondistinguished fixed root
exists. If `a=0`, such a root has no nonfixed predecessor. If `a=1`, every
root has exactly two binary level-one predecessors. This graph-internal test
separates the two cases.

When `m=1`, the restriction `n>=3` forces `a>=2`, so the maximum tail already
recovers `a`; no nonexistent second root is used. After `a` and `sigma(m)` are
known, the total vertex count recovers

```text
tau(n) = |V| - sigma(m)(2^(a+1)-1).
```

This is exactly the mandatory one-root repair. Conversely, equal signatures
permit a level-preserving match of the distinguished roots, the other roots,
all binary positions, and all extra rotation leaves. The matching commutes
with the update, so necessity and sufficiency are both closed.

Fresh literal boundary calculations, implemented without importing the
project verifier, returned

```text
n=3  states=6  fixed=4  depths={0:4,1:2}
n=4  states=10 fixed=1  depths={0:1,1:5,2:4}
n=6  states=16 fixed=4  depths={0:4,1:12}
n=8  states=19 fixed=1  depths={0:1,1:6,2:4,3:8}.
```

Thus the cold boundary set simultaneously pressures `a=0`, `a=1`, and the
single-root cases `m=1` at heights two and three.

### 2.4 The 33/35 commuting bijection

Both odd parameters have `sigma=48` and `tau=4`, so all 48 dihedral vertices
are fixed. Matching `H_{1,0}` to itself and the other 47 dihedral states
lexicographically commutes automatically. The four rotation leaves are
matched as

```text
R_1 -> R_1,  R_3 -> R_5,  R_11 -> R_7,  R_33 -> R_35.
```

Every one maps to the distinguished root. A separate literal-normalizer
calculation, sharing no code with `verify.py`, checked a 52-element domain, a
52-element codomain, injectivity, surjectivity, and all 52 commuting-square
equalities. For common lifts, `v2=b`, both odd-part divisor sums remain 48,
and both divisor counts are `4(b+1)`; signature sufficiency supplies the
lifted conjugacies.

## 3. Review-A closure audit

| Review-A item | Source-level closure | Independent closure test |
|---|---|---|
| m1: implicit domains in (3) and (6) | `main.tex` lines 116--117 now state `t>=0`, `0<=k<=a`, `e|m`, `0<=j<2^k e`; lines 137--146 state `t>=1`, `1<=k<=a`, and the full target domain | theorem and proof were reread under `a=0`, `a=1`, `k=a`, `k+t=a`, and `k+t>a`; no dangling carrier value remains |
| m2: unresolved direct-owner name metadata | `SOURCE_VERIFICATION.md` lines 20--35 retains the article-printed `Hader Baqer Shelash` and records `Hayder` and contact-address surname `Ameen` as variants; `references.bib` uses the printed form | rendered reference [4] matches the chosen form; direct one-step ownership remains zero credit |
| m3: build stopped before settled references | `BUILD.md` lines 8--12 now contains pdflatex, BibTeX, and three final pdflatex passes; lines 21--24 explain the fifth command | a new source-only directory completed exactly those five commands; the final log has no rerun request or warning and the PDF is canonical |

`IMPROVEMENT_LOG.md` records the same concrete dispositions, and the actual
source/artifact checks agree with it. No Review-A repair caused a theorem,
layout, ownership, or reproducibility regression.

## 4. Owner subtraction and portfolio attack

The residual remains owner-thin but honest.

- Cavior and Conrad own the complete subgroup coordinates and counts.
- Frenkel and Shelash--Ahmad--Obaid own equivalent complete odd/even
  normalizer cases. The manuscript places this rule before the contribution
  boundary.
- Shelash--Ashrafi owns nearby two-adic normalizer-length intuition, not the
  pointwise all-subgroup functional graph.
- Divisor sums, binary-tree counting, finite-map zeta bookkeeping, and graph
  matching are standard tools and receive no independent value.
- The bounded source non-hit is described only as a non-certificate.

After those deductions, the retained conjunction is still the full iterated
forest, every positive-time target fibre, the iff unlabelled-graph signature,
and the arithmetic order collision. It does not collapse into P142's
divisor-only reserve, P153's factorial arms into a field cycle, P152's
stochastic reflected chain, or P155/P156's rank-changing permutation maps.
The literal carrier, update, inverse obstruction, and temporal proof engine
remain distinct.

## 5. Cold verifier replay and assertion semantics

I ran, in a fresh scrubbed process,

```bash
env -i PATH=/usr/bin:/bin PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
  /usr/bin/python3 verify.py
```

Fresh stdout was byte-identical to both `CANONICAL.txt` and
`verification_output.txt`. Its SHA-256 was
`25ab2e157715ddce077402e8f9383a7d52c261401d6579035eb43e8e945e9219`,
and it ended with

```text
PROFILE_SHA256 6eed12ce0c63f2d20f734ac1fa67634ce445140372dfc53e779a389de023b782
TOTAL boxes=44 iso_pairs=4 assertions=29590
VERDICT PASS_EXACT_REPLAY
```

The 29,590 assertions materially check literal element-set uniqueness,
ambient-conjugation normalizers, depths, fixed roots, all audited images,
source mass, and every target fibre through `a+3`. They are bounded
falsification pressure. They do not enumerate every subset to prove subgroup
completeness, establish an all-parameter theorem, prove signature necessity,
establish ownership or novelty, or authorize release. The four pair checks in
the project verifier use the theorem-coded update; the independent literal
33/35 calculation above separately closes the advertised base commuting map.

## 6. Source-only build, PDF, and rendered-page inspection

A new temporary directory containing only `main.tex` and `references.bib`
completed the documented five commands. Its PDF was byte-identical to both
`main.pdf` and `main_round1.pdf`:

```text
pages=5
bytes=375182
SHA256=aafab23ed519a68e3d03df44999aa8dc525db0f3e2a860abb67825e556fd839b
```

The settled log contains no LaTeX/package warning, undefined citation or
reference, rerun request, overfull box, or underfull box. Text extraction has
no unresolved marker, workspace path, email, affiliation, ORCID,
acknowledgement, or corresponding-author residue.

`pdfinfo` reports A4, five pages, unencrypted, no forms, no JavaScript, blank
title/author/subject/keyword metadata, and no creation or modification dates.
All 26 font rows are embedded, subsetted, and Unicode mapped. There are no
raster image objects hidden in the PDF.

I rasterized all five cold-build pages at 160 dpi and inspected each one:

1. title, anonymous author, abstract, theorem carrier, equations (1)--(4),
   and the newly explicit iterate domains are legible and in bounds;
2. fibre domains (5)--(7), signature (8), dependency display, and forest
   derivation are complete with no collision or clipping;
3. all-time fibre example, zeta disclaimer, signature necessity, repaired
   total-vertex formula, and 33/35 map are visually intact;
4. sharpness paragraph, owner-firewall table, replay transcript, release
   status, and the start of the references are aligned and readable;
5. references [3]--[5], including the repaired direct-owner citation, are
   complete, uncut, and free of corrupt glyphs.

## 7. Historical and manifest integrity

Before this Review-B file was created, `SHA256SUMS` listed exactly every one
of the 23 other paper-local files and no nonexistent file; all 23 entries
passed `sha256sum -c`. The frozen PDF state was

```text
main_round0_original.pdf
  45901bc68e404cd387c48c848b87ce98d24ead5d60c9ec52b7d584fcb34e60f3
main_round1.pdf = main.pdf
  aafab23ed519a68e3d03df44999aa8dc525db0f3e2a860abb67825e556fd839b
```

The Round-0 digest is unchanged from the author freeze. Round 1 is
byte-identical to the current paper. As required by the workflow, adding this
raw report now makes the Round-1 manifest intentionally incomplete; the
author must add Review B and the Round-2 freeze when regenerating the final
manifest. I did not edit the manifest.

## 8. Findings and required repairs

No Critical, Major, or Minor finding survived the fresh falsification pass.
There is no mathematical, ownership, reproducibility, anonymity, or rendered
artifact repair request from Review B.

The only remaining actions are protocol mechanics owned by the author:
freeze `main_round2.pdf` byte-identically to `main.pdf`, record the zero-finding
Round-B disposition, update final QA status, and regenerate the all-file
manifest. Those actions are not Review-B defects.

## 9. Decision

The P154 theorem contract, all three Review-A repairs, literal replay,
source-only reconstruction, visual artifact, owner subtraction, and portfolio
firewall pass a fresh independent cold read.

**Final Review-B verdict: ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor /
HOLD_EXTERNAL.**

This internal verdict does not authorize novelty, priority, posting,
circulation, specialist contact, submission, or any other external action.
