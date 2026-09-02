# P161 Hostile Review B — fresh independent report

**Review date:** 2026-09-02 UTC  
**Calibration:** `NOT_CALIBRATED`  
**Criteria binding:** `criteria_binding_unavailable`; this review makes no
venue-fit or external-novelty claim.  
**Execution boundary:** fresh reviewer, independent of authoring and Hostile
Review A.  The author manuscript and author-side ledgers were read but not
edited.  This report and the two reviewer-owned artifacts under
`docs/papers157_161_sequence/reviews/p161_b/` are the only writes.

## Verdict

**ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor — HOLD_EXTERNAL.**

The Round-1 theorem agrees exactly with the frozen ORT contract.  Independent
derivation confirms the anisotropic carrier, the counts `T,R,Q`, the exact
four-window core, the oriented singular depths `2/1/1`, every
`0/1/(1+2R)` one-step fibre, the one-step and stable images, the depth CDF,
the zeta factorization, and the `p=3` empty-core boundary.  Three executable
lanes survive double cold replay, including a new Review-B implementation
that imports neither author nor Review-A code and adds normalized exhaustive
checks at `p=11,19`.

Review A's sole microtype finding is closed.  The current source explicitly
disables font expansion while retaining protrusion (`main.tex:11`); the
settled retained log and both source-only cold builds contain zero selected
warning, bad-box, undefined-reference, or rerun lines.  The Round-1 PDF is a
deterministic four-page A4 artifact with all fonts embedded, subsetted, and
Unicode mapped.  No mathematical repair is requested.

This verdict authorizes only an internal Round-2 freeze.  It does not
authorize posting, circulation, submission, author contact, a novelty or
priority claim, or any other external action.

## Strongest counter-argument and claim ceiling

The strongest objection is significance rather than correctness.  Once the
classical orthocentric quartet is granted, the nonright four-cycle is already
forced.  Once `H=A,B,C` is recognized as the three oriented right-angle
conditions, the singular depths are short substitutions into the chosen
sliding-window convention.  The reverse law also uses the same quartet once:
the first two target coordinates force the only candidate source
`(H(A,B,C),A,B)`.  A reader can therefore view the atlas as exact but
elementary bookkeeping around a classical geometric identity.

The paper survives this objection because it makes the narrow ceiling
explicit before the theorem (`main.tex:34-64`), in the subtraction table
(`main.tex:139-165`), and again in the claim-ceiling paragraph
(`main.tex:250-266`).  It assigns zero contribution credit to the
orthocenter, orthocentric quartet, finite-field metric setting, periodic
four-window mechanism, elementary counts, and generic zeta conversion.  The
retained object is only the anisotropic sink totalization together with the
orientation-resolved singular, fibre, and image conjunction.  That is enough
for a precise internal short note, but not enough to relax `HOLD_EXTERNAL`.

## Frozen-contract audit

| Contract interface | Fresh derivation / attack | Result |
|---|---|---|
| Carrier and sink | For a noncollinear `(A,B,C)`, the coefficient vectors `B-C` and `A-C` in the two altitude equations are independent.  The standard dot pairing is nondegenerate, so the orthocenter exists uniquely.  The sink is one additional fixed state. | PASS; `main.tex:66-83` matches the contract literally. |
| Anisotropy | For prime `p=3 mod 4`, a nonzero solution of `x^2+y^2=0` would make `-1` a square.  Thus every nonzero vector has a distinct one-dimensional perpendicular line. | PASS; the restriction is essential and printed at `main.tex:169-176`. |
| Counts `T,R,Q` | Translate `A` arbitrarily, then choose the ordered independent pair `(B-A,C-A)`: `T=p^2(p^2-1)(p^2-p)`.  At a specified right vertex choose a nonzero first side and one of `p-1` nonzero perpendicular second sides: `R=p^2(p^2-1)(p-1)`.  Two right slots would force a nonzero isotropic side, so `Q=T-3R`. | PASS. |
| Exact four windows | Altitude symmetry gives `H(B,C,H(A,B,C))=A`.  In a nonright triangle `H` is not a vertex.  If `H` lay on any side, its two relevant altitude equations would force the corresponding right-angle equality; hence every three-point quartet window is noncollinear.  Returns at times one, two, or three force repeated ordered vertices. | PASS: exact period four, not merely period dividing four. |
| Oriented depths | Right at the first slot gives `H=A` and `(A,B,C)->(B,C,A)->dagger`; the rotation is right at its third slot.  Right at the second or third slot gives `H=B` or `H=C`, so the proposed next triple already repeats a coordinate. | PASS: strict depths `2/1/1`, and `R>0` makes height two sharp. |
| Triangle fibres | A nonsink predecessor of `(A,B,C)` must be `(D,A,B)`.  Mutual orthocentricity forces `D=H(A,B,C)`.  The candidate repeats a vertex exactly for target slots one and two and is valid for slot three and for nonright targets. | PASS: target fibres `0,0,1,1`. |
| Sink fibre | If `H` lies on `BC`, write `H=B+lambda(C-B)`.  The altitude at `B` shows either `lambda=0` (right at `B`) or the triangle is right at `C`, in which case uniqueness gives `H=C`.  Thus exactly source slots two and three degenerate.  Add the sink's self-predecessor. | PASS: `1+2R`; no hidden interior point of `BC` is omitted. |
| Image tower | Positive triangle fibres are precisely the nonright and right-at-third targets.  The latter map to the sink, while the nonright locus is permuted. | PASS: `#im F=1+T-2R`, `F^2(X)={dagger}+nonright`, and stability for all `t>=2`. |
| Depth CDF | Recurrent states are the sink plus `Q` nonright states; the depth-one shell has `2R` states and the depth-two shell has `R`. | PASS: `1+Q`, `1+T-R`, `1+T`. |
| Zeta | The recurrent graph has one fixed cycle and `Q/4` cycles of exact length four. | PASS: `(1-z)^(-1)(1-z^4)^(-Q/4)`. |
| Boundary `p=3` | Direct substitution gives `T=432`, `R=144`, `Q=0`.  The first image is the sink plus the 144 right-at-third targets; the stable image is the sink alone. | PASS: image sizes `145/1`, sink fibre `289`, and a 144-state depth-two shell. |

No claim leaks to isotropic primes, prime powers, other quadratic forms,
higher dimensions, perturbed centers, or a priority statement.  The theorem
therefore stays at the frozen ceiling.

## Independent coordinate derivation

Translate a triangle so that `A=0`, and put `u=B-A`, `v=C-A`.  Writing its
orthocenter as `h`, the two displayed altitude equations reduce to

```text
h dot (u-v) = 0,
h dot v     = u dot v.
```

Because `det(u,v)` is nonzero, this two-row system has one solution.  If
`a=u dot u`, `b=v dot v`, and `c=u dot v`, the three vertex equalities are

```text
h=0  iff c=0,       (right at A)
h=u  iff a=c,       (right at B)
h=v  iff b=c.       (right at C)
```

An overlap of two equalities makes `u`, `v`, or `u-v` a nonzero isotropic
vector, which anisotropy excludes.  This supplies a coordinate-level check
that there is no fourth equality or singular stratum.

For a nonright target, applying the same altitude predicates to the four
points proves

```text
(A,B,C) -> (B,C,H) -> (C,H,A) -> (H,A,B) -> (A,B,C).
```

For a right target, the equality table gives the directed `2/1/1` collapse
without an orbit-count argument.  Reversing a target forces
`(H(A,B,C),A,B)` before any counting is performed; its validity table is
exactly `0,0,1,1`.  The fibre mass check closes:

```text
(1+2R) + R + Q = 1+T.
```

Thus every state and every target is accounted for once, including the sink.

## Exact-control audit

### Author lane

The paper-local verifier was run twice in fresh Python processes with
bytecode disabled.  Both outputs are byte-identical to
`verification_output.txt`:

```text
assertions:          1,317,843
status:              PASS
transcript SHA-256:  26846bfd5cb94d397605f7f4dbf19b22bb29081fe43156e8e45c5ea2839f045c
verifier SHA-256:    0c5ac6d3303e19142569517f77e1ee1c9792e092e7dc7e309b80bb7c3f81330d
```

### Review-A lane

Review A's predicate-scan implementation was also replayed twice and matched
its canonical transcript byte for byte:

```text
assertions:          1,767,768
status:              PASS
transcript SHA-256:  3b9b0dd75b1311cc26c40d07becd9ffdc13b10d53daf14c01f501f680a4111d3
verifier SHA-256:    a56c97c9426d587e7c16b9dd526687813580e897783fd035efec7929693cfd72
```

### Fresh Review-B lane

`docs/papers157_161_sequence/reviews/p161_b/verify_p161_review_b.py`
imports no author or Review-A code.  It uses translation equivariance to
enumerate ordered affine bases, independently solves the two altitude rows,
checks every normalized target reverse candidate and literal forward window
at `p=3,7,11,19`, and checks translation equivariance exhaustively at
`p=3,7`.  The `p=5` negative lane finds eight nonzero null vectors and only
64 normalized right-at-first triangles versus the anisotropic prediction 96.
Two runs match `CANONICAL.txt` byte for byte:

```text
assertions:          6,262,521
status:              PASS
transcript SHA-256:  c42b7e380549062c6415b567a6694f0da5bb218f1e84048e3fba9099b370b9ad
verifier SHA-256:    33d81c531b65c6b5ed877bfc6f1f3c0f2ae5567e4ea366350fdd90fdda0b850b
```

The additional exact signatures are:

```text
p=11: T=1,597,200, R=145,200, Q=1,161,600,
      image1=1,306,801, stable=1,161,601, sink fibre=290,401
p=19: T=44,446,320, R=2,339,280, Q=37,428,480,
      image1=39,767,761, stable=37,428,481, sink fibre=4,678,561
```

All three programs are bounded exact falsifiers.  They do not establish the
universal quantifier or source ownership; the symbolic proof does that first
job, and the source audit only bounds the second.

## Review-A repair audit

Review A found a reproducibility mismatch caused by pdfTeX font expansion.
Round 1 changes the microtype configuration to
`protrusion=true,expansion=false` (`main.tex:11`).  Fresh checks give:

- the retained Round-1 settled log: zero selected warnings, bad boxes,
  undefined citations/references, and rerun requests;
- each of two source-only cold settled logs: the same zero result;
- `main.pdf` and `main_round1.pdf`: byte-identical;
- both source-only cold PDFs and the current PDF: byte-identical;
- an extra settling pass in each cold build: byte-identical;
- current/Round-1 PDF: 4 A4 pages, 304,462 bytes, SHA-256
  `1fcf260e266257c04d0f47aa90a6d47821eefa22834bd32d60fc4a1451d7f214`;
- immutable Round-0 PDF: 4 A4 pages, 305,817 bytes, SHA-256
  `b0e241883509857362f59688b6ea18422959b07862681cabe13bedfe0d1f79c0`.

A raw Round-0/Round-1 text diff shows only line wrapping, interword spacing,
and discretionary hyphenation caused by the changed microtype layout.  After
removing whitespace and ASCII line-break hyphens, the extracted character
streams are byte-identical.  The theorem values, bibliography, author
verifier code, frozen transcript, and all independent exact signatures also
remain unchanged.  I therefore confirm that the repair is build-only and
does not alter the mathematical content.

## Source and ownership audit

The three retained sources support the stated subtraction boundary:

- Kocik and Solecki's author manuscript,
  [*Disentangling a Triangle*](https://fmw.math.uni.wroc.pl/sites/default/files/upload_attach/triangle.pdf),
  explicitly states that each of the four points consisting of a triangle's
  vertices and orthocenter is the orthocenter of the other three.  The
  manuscript correctly gives that quartet zero contribution credit.
- Wildberger's primary manuscript,
  [*Neuberg Cubics over Finite Fields*](https://arxiv.org/abs/0806.2495),
  defines affine metrical geometry over odd finite fields, discusses null
  lines and perpendicularity, gives coordinate orthocenter formulas, and
  states the four-point symmetry.  The finite-field setting and quartet are
  therefore correctly subtracted.
- Guy's primary arXiv record,
  [*The Triangle*](https://arxiv.org/abs/1910.03379), treats the triangle as
  an orthocentric quadrangle, but the advertised iteration reflects a point
  in the triangle edges, uses the resulting Steiner line, and moves to new
  circumcircle points.  It is not the deterministic window `(B,C,H)` and
  supplies no sink-fibre or stable-image atlas.

These primary-source checks validate attribution and distinction only.  The
bounded non-hit for the full residual conjunction is not novelty, priority,
ownership-completeness, or release clearance.  The amber owner gate therefore
remains an external hold rather than a paper defect.

## Cold PDF, source, and anonymity audit

Two fresh directories containing only `main.tex` and `references.bib` were
built by `pdflatex -> bibtex -> pdflatex -> pdflatex`, followed by one extra
settling pass.  Both PDFs match the current Round-1 artifact byte for byte.

```text
pages / stock:      4 / A4
bytes:              304,462
PDF SHA-256:        1fcf260e266257c04d0f47aa90a6d47821eefa22834bd32d60fc4a1451d7f214
encryption:         none
metadata fields:    title/author/subject/keywords blank
fonts:              21/21 embedded, subsetted, Unicode mapped
selected warnings:  0 in both settled cold logs
```

All four pages were rasterized at 144 dpi and inspected individually.  The
title, abstract, theorem, subtraction table, displayed formulae, proofs,
declarations, links, and references are legible.  There is no clipping,
overlap, margin excursion, malformed glyph, or missing page content.  Page 4
is intentionally sparse because it contains only the three-item bibliography;
the complete paper still meets its declared 4–6 page short-note target.

Source and extracted-text scans find no `[VERIFY]` marker, unresolved
citation/reference token, email, local filesystem path, affiliation,
acknowledgment, or hidden identity.  `Anonymous` is the only manuscript
author label, and the identifying PDF metadata fields are blank.  `qpdf` is
not installed, so no qpdf-specific structural check is claimed; `pdfinfo`,
`pdffonts`, `pdftotext`, and raster inspection all pass.

## Findings

### Critical

None.

### Major

None.

### Minor

None.

## Final disposition

Hostile Review B supports **`ACCEPT_INTERNAL`**.  The author may freeze the
unchanged Round-1 mathematics as the Round-2 internal artifact and update
author-side status ledgers accordingly.  P161 remains **`HOLD_EXTERNAL`**:
no posting, submission, circulation, author contact, novelty/priority claim,
or external release is authorized by this review.
