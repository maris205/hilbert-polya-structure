# P161 Hostile Review A — original report

**Review date:** 2026-09-02 UTC  
**Calibration:** `NOT_CALIBRATED`  
**Criteria binding:** `criteria_binding_unavailable`; no venue-fit claim is
made.  
**Execution boundary:** one reviewer-owned adversarial cold read, not a claim
of independent error processes.  No pre-existing P161 author file was
modified; this report and the reviewer artifacts under
`docs/papers157_161_sequence/reviews/p161_a/` are the only writes.

## Verdict

**REVISE — 0 Critical / 0 Major / 1 Minor.**

The theorem survives unchanged.  A predicate-search implementation independent
of the author code confirms the nondegenerate carrier, four-window identity,
the oriented depth split `2/1/1`, every `0/1/(1+2R)` fibre, the full image
tower, and the exceptional prime `p=3`.  The direct-owner and portfolio gates
also survive after the classical orthocentric quartet and finite-field metric
geometry are assigned zero contribution credit.

The sole defect is reproducibility documentation: every settled build emits a
real pdfTeX font-expansion warning, while `BUILD.md` describes the build as
warning-clean.  This is a build-only repair; it does not call for a theorem,
proof, verifier, transcript, or source-boundary change.

## Strongest counter-argument

After the classical orthocentric-system identity is subtracted, a skeptical
reader can argue that almost the whole temporal theorem is forced bookkeeping.
The equality `H=A`, `H=B`, or `H=C` is exactly the corresponding right-angle
condition.  Sliding the window then visibly sends the first-coordinate class
through one cyclic rotation before degeneracy and sends the other two classes
straight to the sink.  On the complement, the already-owned mutual-
orthocenter identity supplies the four-cycle.  The inverse theorem uses that
same identity once more: a target `(A,B,C)` has only the possible predecessor
`(H(A,B,C),A,B)`, whose validity is decided by whether a coordinate repeats.
Thus the depth, fibre, and image formulas are all short consequences of one
classical geometry fact plus the chosen sink convention; they should not be
marketed as a new orthocentric recurrence or new finite-field geometry.

This objection limits significance but does not falsify the stated narrow
note.  The manuscript makes the subtraction before the theorem, repeats it in
Table 1 and the conclusion, and retains only the orientation-sensitive
singular completion and codomain-wide atlas.  Those statements are exact,
complete for the declared carrier, and not found in the bounded direct-owner
screen.  The claim ceiling is therefore defensible as an elementary finite-
dynamics residual, provided the zero-credit language remains intact.

## Claim-by-claim theorem-ceiling audit

| Frozen interface | Independent attack | Ceiling / manuscript result |
|---|---|---|
| Carrier and totalization | For a noncollinear triple, the two opposite-side coefficient vectors are independent; the nondegenerate dot pairing gives exactly one altitude intersection.  The sink is an additional fixed state, not a triangle. | PASS; equations (1)–(2) match the frozen carrier literally. |
| `T`, `R`, and disjoint right strata | Translation leaves `p^2` basepoints; an ordered affine basis gives `(p^2-1)(p^2-p)` choices.  Anisotropy makes every nonzero vector independent of its perpendicular line.  Two right coordinates would force a nonzero isotropic side. | PASS: `T=p^2(p^2-1)(p^2-p)`, `R=p^2(p^2-1)(p-1)`, and `Q=T-3R`. |
| Classical four-window core | Predicate-solving the altitudes gives `H(B,C,H(A,B,C))=A`; for a nonright triangle all four points are distinct and every three-point window is noncollinear.  Ordered returns at times one, two, or three force repeated original vertices. | PASS, exact period four.  Correctly assigned zero contribution credit. |
| Three oriented singular depths | `H=A` yields `(A,B,C)->(B,C,A)->dagger`, and the rotated state is right at coordinate three.  `H=B` or `H=C` makes the first proposed window repeat a coordinate. | PASS: depths are exactly `2/1/1`, with a genuinely attained height two. |
| Depth CDF and zeta | Recurrent states are the sink and the `Q` four-cycle states; the two depth-one classes contain `2R` states and the depth-two class contains `R`.  Direct fixed-iterate counts through time eight agree with one fixed cycle plus `Q/4` four-cycles. | PASS: `1+Q`, `1+T-R`, `1+T` and `(1-z)^(-1)(1-z^4)^(-Q/4)`. |
| Triangle-target fibres | Any nonsink source of `(A,B,C)` must be `(D,A,B)`; mutual orthocentricity forces `D=H(A,B,C)`.  This candidate is invalid exactly for target right slots one and two and valid for slot three and nonright targets. | PASS: fibre sizes `0,0,1,1` on the four target classes. |
| Sink fibre | Literal graph construction shows that the proposed window is degenerate exactly for source right slots two and three.  Adding the sink itself gives `1+2R`. | PASS; no orbit-count division is used. |
| One-step and stable images | The support of the positive target fibres is `dagger` plus nonright targets plus right-at-three targets.  The last class maps to the sink, while the nonright core is permuted. | PASS: sizes `1+T-2R` and `1+Q`, with stabilization for every `t>=2`. |
| Boundary prime `p=3` | Exhaustion gives `T=432`, three disjoint right classes of size `144`, and no nonright triangle.  The first image is the sink plus the 144 right-at-three targets; the second image is the singleton sink. | PASS: image sizes `145/1`, sink fibre `289`, and a nonempty depth-two shell of size `144`. |

No manuscript claim exceeds the frozen theorem contract.  In particular, the
text does not extend to isotropic primes, prime powers, arbitrary quadratic
forms, higher dimensions, other centers, or an external novelty/priority
claim.

## Independent derivation and proof attacks

### 1. Nondegenerate carrier and equality cases

Write `u=B-A` and `v=C-A`.  Noncollinearity is `det(u,v)!=0`.  If `H=A+h`,
the two displayed altitude equations are equivalent to

```text
h dot (u-v)=0,
(h-u) dot v=0.
```

Thus `h dot u=h dot v=u dot v`.  The two linear functionals have independent
coefficient vectors, so there is exactly one `h`.  Moreover `H=A` if and only
if `u dot v=0`, and cyclic relabelling gives the two other equality cases.
These equivalences rule out an unmentioned fourth singular stratum.

The use of anisotropy is legitimate at every point where division or
independence is needed.  For a prime `p=3 mod 4`, `-1` is not a square, so
`x^2+y^2=0` has only the zero solution.  The proof divides by `y` only in the
explicit branch `y!=0`; there is no division by a possibly null side or by
two.  The smallest allowed prime is handled separately rather than hidden in
an asymptotic argument.

### 2. Four windows and all three directed right layers

Subtracting the first two altitude relations produces the third.  Re-reading
the same three perpendicularities for `(B,C,H)` makes `A` its unique
orthocenter.  Cyclic repetition gives

```text
(A,B,C) -> (B,C,H) -> (C,H,A) -> (H,A,B) -> (A,B,C).
```

For a nonright source, `H` cannot coincide with a vertex.  If, for example,
`H=A+lambda(B-A)` lay on `AB`, the first and third altitude equations give
`(lambda-1)(B-A) dot (B-A)=0`; anisotropy forces `lambda=1`, hence `H=B`, a
right case.  Relabelling excludes every other collinear triple.  All four
windows therefore lie in the carrier, and an ordered return before time four
would repeat two of `A,B,C`.

For a right angle at the first listed vertex, `H=A` and the first window is
the valid rotation `(B,C,A)`, whose right angle is now at the third position;
the following window repeats `A`.  At the second or third listed vertex, the
very first proposed window repeats `B` or `C`.  Hence the three depths are
strictly `2/1/1`, not merely upper bounds.

### 3. Every-target inverse and image tower

The first two coordinates of a target fix the last two coordinates of every
nonsink source.  Orthocentric symmetry then fixes its remaining coordinate,
so there is at most one triangle source.  The candidate

```text
(H(A,B,C),A,B)
```

repeats a vertex for target right slots one and two; it is the valid cyclic
rotation for target slot three and a valid quartet window for a nonright
target.  Directly counting the actual graph indegrees gives zero or one in
exactly these cases.  A source reaches the sink precisely in right slots two
and three, so the sink fibre is `1+2R` after its fixed self-predecessor is
included.  Fibre mass is

```text
(1+2R) + R + Q = 1+T,
```

which closes the carrier.  At time zero the image is the full carrier; at
time one it is the positive-fibre support; at time two the transient
right-at-three layer is gone; and from then on the sink is fixed and the
nonright locus is permuted.  There is no omitted `t=0`, `t=1`, or eventual-
stability boundary.

### 4. Isotropic negative control

The scope restriction is material.  Over `F_5`, the standard dot product has
eight nonzero null vectors.  Full enumeration finds 1,600 triangles right at
a fixed coordinate, rather than the anisotropic formula 2,400.  The paper
does not leak its formulas into this regime.

## Exact-control and artifact audit

The author verifier was run twice in fresh Python processes with bytecode
disabled.  Both outputs are byte-identical to `verification_output.txt`:

```text
assertions:          1,317,843
status:              PASS
transcript SHA-256:  26846bfd5cb94d397605f7f4dbf19b22bb29081fe43156e8e45c5ea2839f045c
verifier SHA-256:    0c5ac6d3303e19142569517f77e1ee1c9792e092e7dc7e309b80bb7c3f81330d
```

The independently written reviewer verifier is
`docs/papers157_161_sequence/reviews/p161_a/verify_p161_review_a.py`.  It
imports and calls no author code, finds each orthocenter by scanning all field
points against the altitude predicates rather than using the author's matrix
formula, and constructs literal indegree and image sets.  It exhausts all
states and targets at `p=3,7`, checks fixed iterates through time eight, and
adds the `p=5` scope control.  Two cold runs match `CANONICAL.txt` byte for
byte:

```text
assertions:             1,767,768
status:                 PASS
canonical SHA-256:      3b9b0dd75b1311cc26c40d07becd9ffdc13b10d53daf14c01f501f680a4111d3
reviewer-code SHA-256:  a56c97c9426d587e7c16b9dd526687813580e897783fd035efec7929693cfd72
```

These computations are bounded counterexample pressure.  They do not prove
the all-prime theorem, source ownership, novelty, priority, or release
readiness; the symbolic arguments above carry the universal quantifier.

## Source and ownership audit

### Direct classical ownership, fully subtracted

- Kocik and Solecki's author manuscript, [*Disentangling a
  Triangle*](https://fmw.math.uni.wroc.pl/sites/default/files/upload_attach/triangle.pdf),
  states that the three vertices and orthocenter form a quartet in which each
  point is the orthocenter of the other three.  This directly owns the
  classical mutual-orthocenter mechanism.
- Wildberger's primary record and manuscript, [*Neuberg Cubics over Finite
  Fields*](https://arxiv.org/abs/0806.2495), set up affine metrical geometry
  over odd finite fields, give altitude and orthocenter constructions, and
  explicitly state the four-point symmetry.  Thus even the finite-field
  version of the quartet is background, not merely its Euclidean analogue.
- Right-angle counting, anisotropy of the standard form for `p=3 mod 4`, and
  the finite-map cycle-to-zeta conversion are standard tools.  The manuscript
  assigns them no contribution credit.

The abstract, opening paragraph, subtraction table, controls section,
`SOURCE_VERIFICATION.md`, and frozen contract consistently enforce this
ceiling.  No sentence claims the orthocenter, quartet, finite-field setting,
or four-periodic core as the retained advance.

### Guy comparison

Guy's primary arXiv manuscript, [*The
Triangle*](https://arxiv.org/abs/1910.03379), does two relevant but distinct
things.  Its quadration viewpoint grants equal status to the four points of an
orthocentric quadrangle, which is part of the classical zero-credit core.  Its
actual “trisequence,” however, starts from a point on a circumcircle, reflects
that point in three edges to obtain a Steiner line, and iterates to new
circumcircle points; Guy describes three followers per point.  It is not the
deterministic ordered-triangle window `(A,B,C)->(B,C,H)`, has no degeneracy
sink, and gives none of the target-fibre or stable-image formulas.  The
manuscript's distinction is accurate.

### Nearby sources and bounded non-hit

The finite-field right-angle literature, for example Michael Bennett's
[*Occurrence of Right Angles in Vector Spaces Over Finite
Fields*](https://arxiv.org/abs/1511.08942), studies extremal occurrence in
subsets and explicitly notes the isotropic `q=1 mod 4` boundary.  It does not
define the orthocenter window or its functional graph.  Searches under
`orthocenter/orthocentre map`, `triangle BCH iteration`, `orthocentric
quadrangle dynamics`, `finite-field orthocenter`, `reverse window`, and
`singular/degenerate totalization` located the classical quartet and unrelated
triangle-center iterations, but no direct owner of the retained conjunction.
This remains a terminology-bounded non-hit, not novelty or priority clearance.

## Portfolio-collision audit through P160

| Closest occupied note | Shared surface | Why the proof engine does not transfer |
|---|---|---|
| P81 | orthogonality vocabulary | P81 is an infinite spherical relation shift whose engine is bridge geometry and scale entropy, not a finite affine triangle map. |
| P146 | triangles | P146 is stochastic convex-polygon ear deletion with rooted-tree hook counts; it has no center map, sink, or reverse window. |
| P150 | finite-field singular totalization and target fibres | P150 uses a zero-totalized Lyness rational map on affine pairs and denominator strata.  Its inverse equation and height-three exceptional tree do not yield P161's quartet or right-angle layers. |
| P153 | finite-plane collapse and inverse fibres | P153 uses a triangular polynomial and factorial products for all-time fibres.  No orthogonality or four-point symmetry is present. |
| P160 | ordered triples, finite geometry, shallow fibres | P160 is a characteristic-two projective Steiner-quasigroup map with a pair-sum inverse family and fixed/three-cycle strata.  P161 uses an odd-characteristic anisotropic metric and a unique orthocenter reverse window. |

A repository-wide literal scan found `orthocenter`, `orthocentre`, and
`orthocentric` in no P1–P160 manuscript.  The carrier, update, recurrent
period, singular layers, and inverse equation therefore do not mechanically
reuse an occupied theorem, despite generic overlap in fibres and finite-map
bookkeeping.

## Cold PDF and anonymity audit

Two fresh directories containing only `main.tex` and `references.bib` were
built by `pdflatex -> bibtex -> pdflatex -> pdflatex`; an additional settling
pass left the first build byte-identical.  Both cold PDFs, `main.pdf`, and
`main_round0_original.pdf` are identical:

```text
pages / stock:  4 / A4
bytes:          305,817
PDF SHA-256:    b0e241883509857362f59688b6ea18422959b07862681cabe13bedfe0d1f79c0
encryption:     none
metadata:       title/author/subject/keywords blank
fonts:          21/21 embedded, subsetted, Unicode-mapped
```

All four pages were rasterized at 144 dpi and inspected.  The theorem, source
table, formulas, declarations, links, and references are legible, with no
clipping, overlap, bad glyph, or margin excursion.  Text/source scans found no
personal name, email, local path, affiliation, acknowledgments, or other
identity leak beyond cited authors; `Anonymous` is the only manuscript author
label.  Citations and cross-references settle, BibTeX reports zero warnings,
and there are no overfull/underfull boxes or rerun requests in the settled
pass.

The build is not warning-free: every settled cold pass and the retained
author `main.log` emit the same pdfTeX font-expansion warning described below.

## Findings

### Critical

None.

### Major

None.

### Minor

#### M1 — Retained and cold builds contain an undisclosed font-expansion warning

- **Evidence anchor:** log: `main.log:642`, `build_pdflatex_1.log:88`,
  `build_pdflatex_2.log:88`, and `build_pdflatex_3.log:88` each emit
  `pdfTeX warning (font expansion): font should be expanded before its first
  use`; `BUILD.md:38-42` presents the final build checks without disclosing it.
- **Confidence:** 5/5 — reproduced in two source-only builds and present in
  every retained author pdflatex log.
- **Impact:** the PDF is readable and deterministic, so this is not a theorem
  or integrity failure.  It is a real discrepancy in the Round-0 build record
  and prevents a clean internal freeze.
- **Minimum repair:** load microtype with protrusion retained and expansion
  disabled, for example
  `\usepackage[protrusion=true,expansion=false]{microtype}`; rebuild the
  Round-1 PDF, preserve `main_round0_original.pdf`, replace the retained build
  logs, and update `BUILD.md` with the actual warning-free result and new
  bytes/SHA.  Do not change mathematical content or the frozen transcripts.

## Required repair and Review-B target

1. Apply the build-only microtype repair and regenerate a warning-free Round-1
   package while preserving the Round-0 PDF.
2. Update the build ledger honestly; leave all theorem, proof, source,
   verifier, and transcript claims unchanged.
3. Review B should cold-rederive the three oriented layers and all fibres,
   replay both verification lanes, build from a source-only copy, confirm the
   current/Round-1 byte identity and warning-free settled log, and inspect all
   four pages again.

After M1 is closed, Review A supports `ACCEPT_INTERNAL / HOLD_EXTERNAL`,
subject to a fresh independent Review B.  This report does not authorize
posting, circulation, author contact, submission, or any other external
action.
