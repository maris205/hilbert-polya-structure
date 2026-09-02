# Hostile Review A — P165 Low-Weight Support Shortening

**Frozen artifact reviewed:** Round0 `main.pdf`  
**Pinned PDF SHA-256:** `f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a`  
**Independent verdict:** **ACCEPT_INTERNAL**  
**Severity:** **0 Critical / 0 Major / 0 minor**  
**Lifecycle:** **HOLD_EXTERNAL**

## 1. Independence and scope

I did not author P165 and did not use the paper-local author verifier.  The
Round0 manuscript, bibliography, PDFs, and author evidence were pinned
before review in
`docs/papers162_166_sequence/reviews/p165_a/PINNED_INPUTS.sha256`.  The
reviewer program was implemented independently from the literal padded
shortening definition and theorem statement; it neither imports nor calls
the author program.

The review re-derived strict descent, distance doubling, recurrence, the
sharp height, the every-time nonzero-target image criterion, both inverse
lower bounds, the simultaneous-equality iff classification, and its exact
prime-power count.  It separately attacked `D=0`, `t=0`, `n=0`, nonzero
full-support targets, post-cap times, and the strict-versus-weak cutoff.  It
also audited the one-step hitting-set owner, the complete P1--P164 internal
occupancy, two fresh deterministic replays, two source-only cold builds,
and every PDF page/font/metadata/log surface.

## 2. Mathematical verdict by theorem part

| part | verdict | independent hostile result |
|---|---|---|
| A: descent, doubling, recurrence, height | **PASS** | A minimum word is purged, so every nonzero transition is proper.  A nonzero survivor below `2d(C)` would be both supported on and zero on `U(C)`.  Successive purge supports are disjoint and have sizes at least `1,2,4,...`, giving the upper bound; disjoint full-support lines on dyadic blocks attain it. |
| B: every-time nonzero image | **PASS** | Necessity follows from repeated doubling and the disjoint zero-coordinate budget.  If `d(D)>=2^t` and `z(D)>=2^t-1`, adjoining full-support lines on zero-coordinate blocks of sizes `2^i` makes the lines disappear in exact order; the strict threshold protects the next line and the target. |
| C1: inverse lower bounds | **PASS** | The `t` proper inclusions force codimension at least `t`; the disjoint purge supports lie in `Supp(C)\Supp(D)` and force at least `2^t-1` new support coordinates. |
| C2: simultaneous equality iff | **PASS** | Equality of the two totals forces codimension one and `|U_i|=d_i=2^i` at every step.  A minimum word then has support exactly `U_i`, and the restriction kernel splits off its full-support line.  Recursion gives precisely the claimed direct sum; the image construction proves the converse. |
| C3: exact prime-power count | **PASS** | Ordered labelled dyadic blocks contribute the factorial quotient.  An `m`-block supports `(q-1)^(m-1)` full-support lines, so the product is `(q-1)^(2^t-1-t)`.  The argument is field-theoretic, not prime-only, and the independent F4 audit passes. |

The full derivation is frozen in
`docs/papers162_166_sequence/reviews/p165_a/PROOF_REDERIVATION.md`.

## 3. Boundary and counterexample pressure

### `D=0`

The manuscript correctly excludes zero from the nonzero-target atlas.  Its
complete fibre is `{C:tau(C)<=t}`.  On the exact-depth slice `tau(C)=t`, the
same stepwise budget gives minimum dimension `t` and minimum support
`2^t-1`; simultaneous minimizers have the same dyadic-line form and the
same count with `z(D)` replaced by `n`.  Enumeration confirms both the full
zero-fibre identity and this narrower extremal statement.

### `t=0`

`T^0` is the identity.  Every nonzero target satisfies the criterion, the
two lower bounds are zero, its sole simultaneous extremizer is itself, and
the empty-product formula is one.  For the zero target the fibre is `{0}`,
consistent with `tau(C)<=0`.

### `n=0`, full support, and post-cap time

At `n=0` zero is the only code and the height is zero.  A nonzero
full-support target has `z(D)=0` and therefore no positive-time source.  If
`2^t-1>n`, the positive image is empty although zero remains.  These
statements are all explicit in the manuscript and independently verified.

### Strict cutoff

The strict `<2d(C)` is essential.  In the direct sum of a full-support line
on one coordinate and one on two disjoint coordinates, the strict map
removes only the first line at the first step; the weak `<=2d(C)` variant
also purges the second block.  The reviewer verifier contains this dedicated
sentinel for every audited field and every `n>=3`.

## 4. Findings and executable repairs

### Critical

None.

### Major

None.

### minor

None.

No author-source patch is recommended in Review A.

## 5. Independent exact verification

Reviewer evidence is under
`docs/papers162_166_sequence/reviews/p165_a/`:

- independent verifier `verify_review_a.py` SHA-256:
  `f6399e25007c147f78f83799f825c14fb19419b1ad4a0467ea17618ea592e27f`;
- frozen `CANONICAL.txt` SHA-256:
  `66de01f2399047e6a32d9b22d508be9eab56fd14b62b3e766991d0b28d5b25e7`;
- fresh replay 1 SHA-256:
  `66de01f2399047e6a32d9b22d508be9eab56fd14b62b3e766991d0b28d5b25e7`;
- fresh replay 2 SHA-256:
  `66de01f2399047e6a32d9b22d508be9eab56fd14b62b3e766991d0b28d5b25e7`.

Both fresh outputs are byte-identical to each other and to the canonical
transcript.  The verifier executes **1,574,098 assertions** over **32,805
distinct labelled linear codes**:

- every binary code for `0<=n<=7`;
- every ternary code for `0<=n<=4`;
- every code over the genuine nonprime field
  `F4=F2[x]/(x^2+x+1)` for `0<=n<=3`.

The F4 arithmetic is implemented locally and checked against the field
axioms, including `x^2=x+1` and `x(x+1)=1`.  Codes are generated once from
unique reduced-row-echelon matrices.  The test compares every literal map
and orbit, every time image and target criterion, both lower bounds, all
**43,357** observed simultaneous-equality sources, their recovered dyadic
blocks/lines, the entire actual-versus-constructed extremizer sets, and the
closed count formula.  It also checks Gaussian subspace totals, sharp
heights, exact-depth zero-target minimizers, full-support holes, time zero,
the empty ambient space, the post-cap image, and the strict-cutoff sentinel.

Reproduction command:

```bash
python3 docs/papers162_166_sequence/reviews/p165_a/verify_review_a.py
```

## 6. Owner and internal-collision verdict

Jibril et al. directly own the neighboring one-step low-weight hitting-set
shortening principle.  Taking their generalized protected weight range
through `2d-1` contains the one-step distance-doubling route.  Grassl and
White own nearby low-weight-support special puncturing.  P165 exposes these
sources and gives the entire one-step mechanism zero contribution credit.

The bounded primary search did not locate an owner for the residual
conjunction: autonomous recomputation, the sharp dyadic clock, every-time
nonzero-target reachability, and the simultaneous extremal inverse
classification/count.  This is an owner-thin non-hit, not a novelty or
priority claim.

P109 is the closest internal carrier/proof-shape neighbor, but it iterates a
fixed nilpotent linear operator and uses Gaussian incidence fibres.  P137's
rank-feedback p-group budget is additive/triangular on unordered types.
P164 evolves individual q-ary words through a cellular equality front and
uses affine-code fibres.  None supplies P165's state-dependent
minimum-distance support kernel, multiplicative distance clock, joint
distance/zero-capacity image condition, or dyadic equality-source
classification.  Inspection of the remaining P1--P164 occupancy found no
literal duplicate or proof-engine transfer.  Full receipts and the
subtraction boundary are in
`docs/papers162_166_sequence/reviews/p165_a/OWNER_AUDIT.md`.

## 7. Source-only builds and artifact QA

Two fresh directories received only `main.tex` and `references.bib`.  Both
completed `pdflatex -> bibtex -> pdflatex -> pdflatex`, and the settled logs,
bibliographies, and PDFs agree byte for byte.  Both PDFs also equal the
frozen Round0 artifact:

```text
pages:                 4 (A4)
bytes:                 288,837
PDF SHA-256:           f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a
fonts:                 23/23 embedded, subsetted, Unicode mapped
settled warnings:      0
BibTeX warnings:       0
```

All four pages were rendered at 150 dpi and inspected individually.  No
clipping, overlap, missing glyph, broken formula/link/reference, anomalous
page break, or orphaned heading was found.  Page 4's white area is the
natural end after the three references.  Metadata title/author/subject/
keywords/creator/producer fields are empty; the visible author is
`Anonymous`, and extracted text reveals no affiliation, email, ORCID,
acknowledgement, funding source, or draft token.  `HOLD_EXTERNAL` is the
intended visible lifecycle marker.  Detailed receipts are in
`docs/papers162_166_sequence/reviews/p165_a/BUILD_QA.md`.

## 8. Final recommendation

**ACCEPT_INTERNAL — 0C / 0M / 0m.**  The theorem package, all stated
boundaries, exact nonprime prime-power count, owner subtraction, source
build, and artifact QA survive independent Hostile Review A without a
requested repair.  This is not permission to post or submit: keep the paper
anonymous and maintain **HOLD_EXTERNAL** pending the remaining review and
central lifecycle gates.
