# HOSTILE REVIEW B — P150

## Verdict

**REVISE — 0 Critical, 0 Major, 1 Minor.**

The mathematical package survives independent rederivation.  The two issues in
`HOSTILE_REVIEW_A.md` are genuinely closed: the five-cycle quotient is now
justified by an explicit orbit partition (including the characteristic-five
case), and the small-field boundary at (q=3) is treated correctly; the source
boundary now expressly subtracts both Lyness's 1942 rational recurrence and
Kanki's 2013 finite-field regularisation framework, with a replayable search
ledger.  The verifier cold-replays byte-for-byte, two isolated source-only
builds reproduce the frozen PDF exactly, and all five pages pass visual
inspection.

The sole required repair is package metadata: `FINAL_QA.md` still describes
the pre-repair round-zero artifact as the current final artifact.  This does
not affect any theorem, proof, source boundary, verifier result, or PDF, but it
must be corrected or unambiguously labelled historical before release.

External status remains **HOLD_EXTERNAL**.

## Scope and independence

I did not author P150 or its Review A.  I read the complete current package,
rederived every theorem interface from the literal update rule, cold-replayed
the verifier and frozen transcript, inspected the primary-source records and
claim subtraction, built twice from isolated copies of the source pair, and
visually inspected every page of the resulting five-page paper.  This review
does not treat a bounded literature search as a novelty certificate.

## Disposition of Review A findings

| Review A item | Review B test | Disposition |
|---|---|---|
| Minor: the five-cycle count needed an orbit-partition proof, plus explicit (q=3) and characteristic-five treatment | Re-derived the generic identity (L^5=\mathrm{id}), the fixed-point set, and the partition of all remaining generic points into disjoint five-element orbits; checked (q=3), (q=5), and general characteristic five | **CLOSED** |
| Minor: the owner ledger needed replayable queries and direct subtraction of Lyness (1942) and Kanki (2013) | Inspected the official Cambridge record/preview for Lyness and the official SIGMA/arXiv full text for Kanki; replayed every listed query family and checked the candidate/exclusion table | **CLOSED** |

## Required repair

### Minor 1 — `FINAL_QA.md` is stale after the Review-A repair

`FINAL_QA.md` still says that the final manuscript is 396,310 bytes with SHA-256
`d94b...`, that current `main.pdf` is byte-identical to the round-zero PDF, that
the bibliography has three entries, and that no hostile-review file exists.
Those statements now describe the historical round-zero snapshot, not the
current package.  The current PDF is 403,358 bytes with SHA-256
`26d0a73adb71b2e303ea637b5874939914cffd53f09a2230ded5775484c33dca`, the
bibliography has five entries, and `HOSTILE_REVIEW_A.md` exists.  The current
values elsewhere in the package and in `SHA256SUMS` are correct.

**Required repair:** either (a) relabel `FINAL_QA.md` prominently as the
historical round-zero author QA snapshot and remove language that calls its
artifact values current, or (b) update it to the round-one artifact, five-entry
bibliography, and actual review state.  Preserve the historical record rather
than silently rewriting it if the file is meant to be an audit snapshot.

## Independent theorem audit

### 1. Literal rule and five-stratum partition

For odd (q), the paper studies

\[
 L(x,y)=\bigl(y,(1+y)\operatorname{inv}_0(x)\bigr),
 \qquad \operatorname{inv}_0(0)=0.
\]

The five stated sets form a genuine disjoint partition.  After removing the
axes, test successively (y=-1), (x=-1), and (1+x+y=0).  These give,
respectively, the parameterised strata (E_1,E_3,E_2); if none holds, then all
five factors in

\[
 xy(1+x)(1+y)(1+x+y)
\]

are nonzero, so the point lies in (G).  The parameterisations are injective
with sizes

\[
 |G|=(q-2)(q-3),\quad |A|=2q-1,\quad
 |E_1|=q-1,\quad |E_2|=|E_3|=q-2,
\]

and these sum to (q^2).  The formula remains valid at the boundary (q=3),
where (G) is empty.

### 2. Generic five-period law

On (G), direct substitution is legal at every step and gives

\[
\begin{aligned}
(x,y)&\mapsto \left(y,\frac{1+y}{x}\right)
\mapsto \left(\frac{1+y}{x},\frac{1+x+y}{xy}\right)\\
&\mapsto \left(\frac{1+x+y}{xy},\frac{1+x}{y}\right)
\mapsto \left(\frac{1+x}{y},x\right)
\mapsto (x,y).
\end{aligned}
\]

The defining five nonzero factors of (G) certify every displayed
denominator and numerator needed to stay in the rational regime.  Thus
(L^5=\mathrm{id}) on (G).  Since five is prime, every generic orbit has
period one or five.

A fixed point is either ((0,0)), which is on the axes, or ((a,a)) with
(a^2-a-1=0).  Such a root is neither (0) nor (-1), and
(1+2a\ne0): the contrary substitution (a=-1/2) would give
(a^2-a-1=-1/4\ne0) in odd characteristic.  Hence all (r_q) nonzero roots
are generic fixed points.  Removing them from (G), the remaining points are
literally partitioned into disjoint five-element (L)-orbits.  This proves,
without a separate congruence assumption, both

\[
5\mid\bigl((q-2)(q-3)-r_q\bigr)
\]

and the stated number of five-cycles.

In characteristic five, (X^2-X-1) has discriminant zero and one distinct
root, so (r_q=1); the same orbit partition still applies.  At (q=5), for
example, the six generic points consist of that fixed point and one
five-cycle.  At (q=3), (G=\varnothing), (r_q=0), and the five-cycle count
is zero.  No division-by-five argument fails in either case.

### 3. Axes, exceptional tails, and exact depth

The axis dynamics are

\[
L(0,a)=(a,0),\qquad L(a,0)=(0,a^{-1})\quad(a\ne0),
\]

with ((0,0)) fixed.  Inversion has precisely the two fixed elements
(a=\pm1) over an odd field.  Consequently the nonzero axes contain two
two-cycles, and the remaining (q-3) parameters pair under inversion to give
((q-3)/2) four-cycles.

The exceptional strata satisfy the strict chain

\[
E_3\longrightarrow E_2\longrightarrow E_1
\longrightarrow(-1,0)\in A.
\]

Because the five strata are disjoint and (G\cup A) is recurrent, these are
exact—not merely upper—tail depths three, two, and one.  Therefore

\[
\sum_{v\in\mathbb F_q^2}z^{\tau(v)}
=(q^2-3q+5)+(q-1)z+(q-2)z^2+(q-2)z^3.
\]

The (q=3) case still has (|E_3|=1), so the maximal depth three is attained.

### 4. Cycle census and zeta function

Combining the generic and axis analyses yields exactly

\[
c_1=1+r_q,\qquad c_2=2,\qquad
c_4=\frac{q-3}{2},\qquad
c_5=\frac{(q-2)(q-3)-r_q}{5},
\]

with no other cycle lengths.  Substituting these counts into the standard
finite functional-graph Euler product

\[
\zeta_L(t)=\prod_{m\ge1}(1-t^m)^{-c_m}
\]

reproduces the manuscript's zeta formula.  The verifier's fixed-iterate
counts through (n=20) independently exercise the same census.

### 5. Every-target fibre law, image, and complete in-tree

For a target ((u,v)), every predecessor must have (y=u), and its first
coordinate (x) must solve

\[
(1+u)\operatorname{inv}_0(x)=v.
\]

If ((u,v)=(-1,0)), every (x\in\mathbb F_q) works, giving fibre size (q).
If (u=-1) and (v\ne0), none works.  If (u\ne-1), exactly one works:
(x=0) when (v=0), and (x=(1+u)/v) otherwise.  Thus the fibre law,
image size (q(q-1)+1), and unique maximal fibre are all exact.

The full component of the unique (q)-fibre target also checks out.  The
target ((-1,0)) lies on the two-cycle with ((0,-1)).  Among its (q)
predecessors, ((0,-1)) is the cycle predecessor, ((-1,-1)) is a leaf, and
each ((a,-1)) for (a\ne0,-1) heads a unique chain

\[
(-1,-1-a)\longrightarrow(-1-a,a)\longrightarrow(a,-1)
\longrightarrow(-1,0).
\]

The first vertex in each such chain and the isolated leaf have empty fibres;
the fibre theorem rules out any omitted branch.  Hence the asserted in-tree
is complete, not just an exhibited subgraph.

## Primary-source and ownership audit

### Lyness (1942)

The [official Cambridge journal record](https://www.cambridge.org/core/journals/mathematical-gazette/article/1581-cycles/53291B598D44F2F40CA5C793391EF272)
confirms *The Mathematical Gazette* 26(268), page 62, DOI
`10.2307/3606036`.  The publisher-hosted first-page preview explicitly gives
the five-cycle recurrence

\[
u_{n+1}u_{n-1}-a^2=a u_n.
\]

At (a=1), this is exactly the non-singular rational recurrence underlying
the manuscript.  The paper therefore correctly assigns zero credit for that
rational five-period core.  Lyness does not supply the finite-field
zero-totalisation, exceptional scheduler, fibre law, or functional-graph
census claimed here.

### Kanki (2013)

The [official SIGMA article page](https://sigma-journal.com/2013/056/) and
[author-posted arXiv full text](https://arxiv.org/abs/1209.1715) confirm
M. Kanki, *Integrability of Discrete Equations Modulo a Prime*, SIGMA 9
(2013), 056, DOI `10.3842/SIGMA.2013.056`.  The article addresses division by
zero over finite fields through extension/reduction of the state space,
including blow-ups and (p)-adic reduction/almost-good reduction.  It does
not impose the manuscript's literal convention
(operatorname{inv}_0(0)=0).  The manuscript correctly subtracts Kanki's
finite-field singularity-regularisation framework while retaining only the
claims that depend on this different, explicitly totalised map.

### Search ledger and surviving conjunction

I replayed the seven query families recorded in `SOURCE_VERIFICATION.md`
across the listed publisher/DOI, arXiv/author, SIGMA, and citation-trail lanes.
The ledger supplies exact queries, access date, candidates, and explicit
exclusion reasons, so it is reproducible.  The remaining claim conjunction is
narrow and properly stated: the literal zero-totalised Lyness update over all
odd finite fields, its five-stratum scheduler, exact tails and cycle census,
zeta function, every-target fibre law, and the complete maximal-fibre in-tree.
No searched primary source owned that conjunction.  This is a bounded non-hit,
not proof of global novelty; the manuscript and ledger preserve that
limitation.

The remaining primary-reference metadata also agrees with the cited official
records: Hone--Kouloukas (2023), DOI `10.1007/s10801-022-01203-5`; Hone (2020),
DOI `10.1145/3373207.3404044`; and Jogia--Roberts--Vivaldi (2006), DOI
`10.1088/0305-4470/39/5/008`.

## Computational audit

I cold-ran

```text
PYTHONDONTWRITEBYTECODE=1 python3 verify_p150.py
```

and compared stdout byte-for-byte with `verification_output.txt`; the
comparison passed.  The frozen transcript covers all 25 odd prime fields
through 101 and the extension fields
(mathbb F_9,mathbb F_{25},mathbb F_{27},mathbb F_{49},mathbb F_{121},mathbb F_{125}).
It reports 110,095 state/target cells per relevant exhaustive layer,
2,144,131 assertions, and `STATUS=PASS`.

The verifier checks irreducibility for the extension-field models, field
arithmetic and inverses, unique stratum assignment and exact stratum sizes,
literal orbit tails and periods, all five generic iterates, exceptional arrows,
the root count (r_q), cycle census and divisibility, fixed-iterate shadows
through (n=20), every target fibre, image size, maximal fibre, and all
predecessor sets in the distinguished component.  These are direct exhaustive
tests of the theorem interfaces rather than spot examples.  `sha256sum -c
SHA256SUMS` also passes for every frozen artifact listed there.

## Build and visual audit

I performed two independent source-only builds in separate temporary
directories, copying only `main.tex` and `references.bib` and running the full
`pdflatex`/`bibtex`/`pdflatex`/`pdflatex` sequence.  Both outputs are
byte-identical to each other and to current `main.pdf`:

| Artifact | Pages | Bytes | SHA-256 |
|---|---:|---:|---|
| isolated build 1 | 5 | 403,358 | `26d0a73adb71b2e303ea637b5874939914cffd53f09a2230ded5775484c33dca` |
| isolated build 2 | 5 | 403,358 | `26d0a73adb71b2e303ea637b5874939914cffd53f09a2230ded5775484c33dca` |
| current `main.pdf` | 5 | 403,358 | `26d0a73adb71b2e303ea637b5874939914cffd53f09a2230ded5775484c33dca` |

The expected frozen size and digest therefore match exactly.  The logs contain
no unresolved citation/reference, rerun request, overfull/underfull box, or
duplicate-label warning.  All fonts are embedded and subsetted; the PDF is
unencrypted, contains no forms or JavaScript, and has blank identifying
metadata.

I rendered and inspected all five pages.  There is no clipping, overlap,
missing or broken glyph, malformed display, illegible bibliography, or bad
cross-reference.  The theorem and partition begin cleanly on pages 1--2,
axes/tails/cycles remain readable on pages 3--4, and the controls,
declarations, and five-entry bibliography are complete on page 5.

## Release decision

There is no mathematical, computational, build, visual, or direct-owner
obstacle in the current manuscript.  Review A's two requested repairs are
closed.  Release remains **HOLD_EXTERNAL** solely pending the one Minor package
consistency repair to `FINAL_QA.md` and confirmation that the repaired metadata
has been re-frozen.
