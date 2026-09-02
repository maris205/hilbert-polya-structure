# P152 independent hostile review A

**Review date:** 2026-09-02 UTC.  
**Reviewer relation:** independent internal reader; did not author P152.  
**Protocol:** `docs/papers152_156_sequence/HOSTILE_REVIEW_PROTOCOL.md`.  
**External state:** `HOLD_EXTERNAL`.  The manuscript was not sent to an
external model, reviewer, or review service.  Primary-source records were
consulted only for the owner audit.

## Verdict

**REVISE — 0 Critical / 0 Major / 2 Minor.**

The complete owner-subtracted theorem package survives independent
rederivation.  The physical sign process really has the stated reflected
count quotient; the Chebyshev elimination, all exceptional parameters, mean
and extrema, spine parity, exact two-statistic inverse, and private-block
tail certificate are correct.  I found no direct source for the special-book
law conjunction, no portfolio collision, no build or transcript mismatch,
and no anonymity leak.

Two artifact-level repairs remain.  The Round-0 manifest covers only six core
files rather than the complete stable package, and the largest verifier lane
does not actually pressure the infeasible half of the inverse iff or the
probabilistic part of the absorption certificate.  Neither issue creates a
mathematical counterexample, but both must be made exact before internal
acceptance.

This is a raw review.  I did not edit `main.tex`, the verifier, bibliography,
transcript, PDF, or any author ledger.

## 1. Package and theorem-ceiling comparison

I read `BTB_FREEZE_CONTRACT.md`, `main.tex`, `references.bib`, every
paper-local planning/evidence/source/control/build record, the proof package,
`verify_p152.py`, the frozen transcript, the manifest, and both Round-0 PDFs.

| Frozen interface | Manuscript interface | Hostile result |
|---|---|---|
| owned `p=1/3` local-triad kernel on `B(3,r)=K_{1,1,r}` with the active clock | Section 1 and ownership table | PASS; kernel, clock relation, XOR dual, carrier, and static classes are explicitly zero-credit |
| strong count lumping `k -> k-1` with mass `2/3`, `k -> r-k` with mass `1/3` | Theorem 1(i), Section 2 | PASS, including coincident targets |
| joint `(T,J)` transform and Chebyshev-rational solution | Theorem 1(ii), Section 3 | PASS as a reduced rational identity |
| mandatory `r=1`, `r=2`, and `z=0` continuations | equation (6) and its proof | PASS; no illegal invocation of `U_{-2}` and the `r=2` removable factor is cancelled |
| quadratic mean and sharp count extrema | Theorem 1(iii), Section 4 | PASS for both parities of `r` and the `r=1` equality case |
| spine parity plus exact feasible-image inverse from `(m,q)` | Theorem 1(iv), Section 4 | PASS in both iff directions, including `q=1/2` and both one-statistic collisions |
| book-specific private-block exponential tail | Theorem 1(v), Section 2 | PASS, including `n=0` |
| no arbitrary-graph, friendship-carrier, noisy-inverse, or full-sign recovery claim | theorem aftermath and Limitations | PASS; no ceiling overrun |

The note remains paper-sized only as the complete conjunction led by the
marked transform and the exact coarse inverse.  Strong lumping, the generic
Bellman equation, or the mean alone would be owner-compressed and would not
carry the paper.  The manuscript respects that ceiling.

## 2. Independent theorem rederivation and proof attacks

### 2.1 Physical signs, full-state quotient, and clock convention

Let the common-spine sign bit be `s` and the two private sign bits on page
`i` be `a_i,b_i`.  Its imbalance bit is

```text
x_i = s xor a_i xor b_i.
```

Flipping either private edge toggles only `x_i`; since the page selected for
an update is active, this changes the count from `k` to `k-1`.  Flipping the
spine toggles every `x_i`, hence changes the count to `r-k`.  The page choice
does not alter either target, and the physical-edge choice gives masses
`2/3` and `1/3`.  These probabilities are identical for every sign
configuration in a count fibre, so this is strong lumpability of the full
sign chain rather than only a weak statement about a chosen representative.

When `k-1=r-k`, the private and spine events remain distinct physical
updates but enter the same quotient cell; adding their masses is therefore
mandatory and correct.  For `r=2,k=1` this produces the stated spine
self-loop.

At `p=1/3`, the Antal--Krapivsky--Redner rule selects every edge of an
imbalanced triad with probability `1/3`.  Conditioning the 2005 all-triad
clock on a non-no-op epoch chooses uniformly among currently imbalanced
pages, while the 2006/Istrate formulation directly uses that active clock.
Thus the manuscript does not silently transfer an all-triad hitting time to
the embedded chain.

As a check independent of `verify_p152.py`, I enumerated actual spine and
private sign bits for every state through `r=6` and every legal active-page/
physical-edge update.  All **92,844** full-sign transitions gave exactly the
two quotient targets above.

### 2.2 Marked Bellman system and every division

With a factor `z` for every active epoch and a factor `u` only for a spine
flip, first-step conditioning gives

```text
F_k = z[(2/3)F_(k-1) + (u/3)F_(r-k)],   F_0=1.
```

For `1<=k<r`, the equation at `r-k` can be solved for
`F_(r-k-1)` using division by `2z`; the proof explicitly works first in the
rational-function field with `z != 0`.  Substitution at `k+1` eliminates the
reflected term without division by `u` and yields

```text
F_(k+1) - 2 xi F_k + F_(k-1) = 0,
2 xi = [9+z^2(4-u^2)]/(6z).
```

The initial condition `F_0=1` gives
`F_k=U_(k-1)(xi)F_1-U_(k-2)(xi)`, including `k=1` because
`U_0=1,U_-1=0`.  The terminal equation
`F_r=(2z/3)F_(r-1)+zu/3` gives the displayed quotient for `F_1`.
No step divides by `u`, so `u=0` is regular.

The probability-transform domain is also correctly separated from the
formal identity.  Almost-sure absorption gives convergence for
`|z|<1,|u|<=1`; zeros of a displayed denominator are read through the
reduced rational function/Bellman continuation, not by pointwise division.

### 2.3 Exceptional parameters

- `r=1`: every edge choice absorbs in one active epoch, with two unmarked
  private choices and one marked spine choice, so
  `F_1=z(2+u)/3`.  The general quotient is not used.
- `r=2`: at `k=1`, the Bellman equation is
  `F_1=z(2/3+(u/3)F_1)`, hence `F_1=2z/(3-zu)`.  The unreduced Chebyshev form
  has the factor `3+zu` on both sides and the manuscript cancels it before
  evaluation.
- `z=0`: `xi` is undefined, but the Bellman system gives `F_0=1` and
  `F_k=0` for every `k>0`.
- `u=-1,0,1`: no derivation divides by `u`; `u=-1` specializes to the parity
  transform and `u=1` to the ordinary hitting-time transform.

No missing equality or singular parameter was found.

### 2.4 Mean, extrema, and equality cases

The tail certificate below makes the mean finite, so differentiating or
first-step conditioning is legitimate.  Eliminating reflected terms from

```text
m_0=0,
m_k=1+(2/3)m_(k-1)+(1/3)m_(r-k)
```

gives the constant second difference `-1`.  Together with
`m_r=1+(2/3)m_(r-1)`, the unique solution is

```text
m_k = k(r+2-k)/2.
```

This quadratic is strictly concave.  On `1<=k<=r`, its two endpoints have
values `(r+1)/2` and `r`, so for `r>1` the minimum is uniquely `k=1`.
The vertex is `(r+2)/2`; the nearest admissible integer(s) give exactly the
even/odd maximum formulas.  For `r=1`, the only nonabsorbing state has mean
one and is correctly declared both extremizers.

### 2.5 Parity and the inverse iff

Writing `h_k=E_k[(-1)^J]`, private flips preserve the sign and spine flips
negate it, giving

```text
h_0=1,
h_k=(2/3)h_(k-1)-(1/3)h_(r-k).
```

The affine solution `(r+2-2k)/(r+2)` satisfies the system.  Iteration to
`T wedge n`, followed by almost-sure absorption and bounded convergence,
establishes uniqueness as an expectation.  Therefore
`q=P(J odd)=k/(r+2)`.

For the forward inverse direction, put `R_0=r+2`.  Then

```text
m=k(R_0-k)/2,
q(1-q)=k(R_0-k)/R_0^2,
2m/[q(1-q)]=R_0^2.
```

The principal square root is the integer `R_0>=3`, and `qR_0=k` lies in
`[1,R_0-2]`.  Conversely, if the stated integer conditions hold, setting
`r=R-2,k=qR` makes a legal nonabsorbing state and substitution recovers both
input observations.  This also proves uniqueness, not merely a reconstruction
formula.  The central value `q=1/2` has no zero denominator and is regular.
The printed `q`-only and `m`-only examples are exact collisions.

### 2.6 Private blocks and the tail quantifier

At every active epoch the private/spine type is an independent Bernoulli
choice with private probability `2/3`, regardless of the current count.  A
run of `r` private types lowers the positive count at every performed update
and therefore absorbs within the block.  Conditional on survival to a block
boundary, that event has probability `(2/3)^r`.  The Markov property gives

```text
P_k(T>nr) <= [1-(2/3)^r]^n
```

for every integer `n>=0`; at `n=0` both sides equal one.  The bound is
book-specific and is not promoted to a generic convergence theorem.

## 3. Owner attack

### Direct ownership

The subtraction is appropriately severe.

- Antal--Krapivsky--Redner directly own local triad dynamics and the
  `p=1/3` equiprobable-edge kernel: [2005 primary manuscript](https://arxiv.org/abs/cond-mat/0506476)
  and [2006 primary manuscript](https://arxiv.org/abs/physics/0605183).
- Istrate directly owns the same general-graph kernel and its triadic-dual/
  XOR hypergraph representation.  Definition 4 of the
  [primary manuscript](https://arxiv.org/abs/0811.0381) explicitly turns a
  physical edge into the hyperedge of all incident triangles and permits two
  self-loops at a triangle.
- On the triangular book, that dual is exactly one `r`-vertex hyperedge for
  the spine plus two self-loops at each page.  Thus the literal construction,
  kernel, Boolean representation, and generic recurrence/absorption program
  receive no contribution credit.
- Sehrawat--Bhattacharjya directly own the signed-book carrier and its static
  switching classes.  No carrier or static-class contribution is retained.

### Nearby ownership and standard tools

Istrate--Bonchis--Marin own the generic hypergraph particle-system, drift,
and WalkSAT setting.  Bellman/resolvent rationality, Chebyshev identities,
quadratic concavity, finite-chain tail iteration, and algebraic inversion are
standard and correctly assigned zero independent credit.

### Residual and bounded non-hit

I repeated the exact/alias query families in the source ledger, including
`book graph triad dynamics`, `K_{1,1,r} social balance`, `shared-edge
triangles`, `one large hyperedge two self-loops`, `Chebyshev absorption`,
`spine flip`, `friendship`, and `windmill`.  The checked primary texts locate
the direct kernel and dual owners but do not print the special-book marked
transform/inverse conjunction.

That result is only a bounded non-hit.  It does not establish novelty,
priority, ownership completeness, or clearance.  P152 remains
**owner-thin**: a later source for the triangular-book law, or for the
equivalent one-large-hyperedge/two-loop process, reopens the paper immediately.

## 4. Portfolio-collision attack

- **P136 and killed S09:** the shared-edge triangular carrier is literal
  overlap, but P136/S09 delete a chosen edge and inherit a sunflower
  transversal law.  P152 never deletes an edge; a spine sign flip reflects
  `k` to `r-k`.  No endpoint/transversal proof transfers.
- **P145:** both quotient binary edge data, but P145 is a stationary
  vertex-push group walk with folded-hypercube Fourier factors.  P152 is an
  active-page absorbing chain with a reflected Bellman recurrence.
- **P138:** XOR notation is common and therefore zero-credit.  P138 is a
  deterministic length-preserving prefix-feedback map; P152 is stochastic
  and absorbing on a fixed signed graph.
- **P151:** this is the closest theorem silhouette because both have marked
  first-passage transforms and inverse boundaries.  P151 uses unequal-arm
  continuants and labelled-leaf tomography.  P152 is separated only by the
  spine-marked Chebyshev reflection law plus the parity/mean feasible inverse;
  the manuscript leads with exactly those objects.
- **P153--P156:** factorial collapse on a finite plane, subgroup-normalizer
  forests, and the two rank-varying permutation extractors have no literal
  carrier or proof-engine collision with P152.

The portfolio gate passes.  It would fail if the paper were reduced to a
generic mean/absorption calculation or if XOR notation were presented as
separation value.

## 5. Independent exact replay and assertion semantics

I cold-ran, in a fresh process,

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p152.py
```

Fresh stdout matched `verification_output.txt` byte for byte.  The transcript
SHA-256 is

```text
07a907a470143337248905b56a630672ba976ff6806b05c4458e20b2f7695da5
```

and the run ended with

```text
assertions=191278
arithmetic=integer_and_Fraction_only
PASS
```

The script enumerates every nonzero imbalance mask through `r=9`, solves
independent rational Bellman systems at four exact `(z,u)` points through
`r=20`, checks all three small boundaries, solves mean/parity systems through
`r=60`, and evaluates every valid `(r,k)` through `r=300`.  My separate
full-sign audit described above adds 92,844 physical-edge checks without
importing the paper verifier.

Finite computation does **not** prove the all-`r` rational identity, the
almost-sure/probabilistic block iteration, the inverse iff for arbitrary exact
candidate pairs, owner completeness, novelty, or external clearance.  The
symbolic proof carries those claims.  Finding m2 below concerns the precision
with which the frozen lane advertises its narrower checks, not the theorem.

## 6. Source-only build, PDF, and anonymity

A fresh temporary directory containing only `main.tex` and `references.bib`
completed

```text
pdflatex -> bibtex -> pdflatex -> pdflatex
```

and reproduced the current PDF byte for byte:

```text
pages=5, bytes=338268
SHA256=f2c2476df00d223fdacaf8fb28954d5f620b10611087c3ff35b16ea158f17e57
```

The current PDF and `main_round0_original.pdf` are byte-identical.  The
settled source-only log has no unresolved citation/reference, rerun request,
build warning, overfull box, underfull box, or duplicate label.  All 25 font
rows are embedded and subsetted.  The PDF is A4 and unencrypted; title,
author, subject, and keyword metadata are blank, with no volatile date,
form, or JavaScript.

I rasterized and inspected all five pages.  The ownership table, theorem,
exception display, Chebyshev proof, inverse collision examples, verifier
table, declarations, and references are legible and within bounds.  No
clipping, overlap, corrupt glyph, unresolved marker, or identifying author
information is visible.  `Anonymous` is the only displayed author identity,
and the explicit `HOLD_EXTERNAL` statement is present.

## 7. Findings and required repairs

### m1 — Minor: `SHA256SUMS` is only a core-file manifest

**Evidence.**  The current manifest has six entries: the two PDFs,
`main.tex`, `references.bib`, `verify_p152.py`, and
`verification_output.txt`.  It omits the stable author package
(`BUILD.md`, `CLAIMS_EVIDENCE.md`, `CONTROL_RESULTS.md`, `FINAL_QA.md`,
`NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `PROOF_PACKAGE.md`, `README.md`, and
`SOURCE_VERIFICATION.md`).  This differs from the complete stable-file
manifests already used by P153--P156 and cannot satisfy the protocol's final
artifact invariant after the review/improvement rounds.

**Required repair.**  At author Round 1, regenerate `SHA256SUMS` after all
review dispositions and build artifacts are frozen.  Exclude the manifest
itself, include every other retained paper-local file required by the final
protocol (including reviews, improvement log, and historical round PDFs),
and record a cold `sha256sum -c SHA256SUMS` pass in the QA ledger.  Do not
overwrite the Round-0 PDF.

### m2 — Minor: the largest verifier lane does not test the full advertised
inverse/certificate boundary

**Evidence.**  `verify_inverse_and_absorption()` ranges only over genuine
states `(r,k)`.  It checks that their computed square is `(r+2)^2`, that
`q(r+2)=k`, and that a deterministic counter decremented at most `r` times
reaches zero.  It does not generate infeasible exact `(m,q)` candidates and
compare rejection with the theorem's iff criterion; it does not assert the
two printed one-statistic collisions; and it does not check the exact
probability `(2/3)^r` or a bounded instance of the block-tail inequality.
Nevertheless, **180,600** assertions are grouped under “inverse/absorption
certificate,” which can be read more broadly than the code's pressure.

**Required repair.**  Either narrow the lane label and all ledgers to
“valid-state inverse identities and deterministic private-block clearing,”
or add independent bounded negative-candidate tests, explicit assertions for
both scalar collisions, and exact-Fraction block-probability/tail checks.
Keep the statement that none of these finite tests proves the iff or the
all-parameter tail theorem.

## 8. Required Round-1 disposition

Record both items in `IMPROVEMENT_LOG.md`, implement the evidence/manifest
repairs without broadening any theorem or ownership language, rebuild from a
source-only copy, preserve `main_round0_original.pdf`, and freeze
`main_round1.pdf`.  P152 remains `HOLD_EXTERNAL`; this review does not claim
novelty, priority, submission readiness, or release clearance.
