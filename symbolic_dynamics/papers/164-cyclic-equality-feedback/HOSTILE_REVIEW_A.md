# Hostile Review A — P164 Cyclic Equality-Feedback Dynamics

**Frozen artifact reviewed:** `main.pdf`  
**Pinned PDF SHA-256:** `db26e57e610577cdff03c348fa3ce794165e3268393350d7d2f55b14e98070ae`  
**Independent verdict:** **REVISE_MINOR**  
**Severity:** **0 Critical / 0 Major / 2 minor**  
**Lifecycle:** **HOLD_EXTERNAL**

## 1. Review independence and scope

I did not participate in the author verification.  Before reviewing the
claims, I pinned the manuscript, bibliography, PDF, and author evidence
hashes in
`docs/papers162_166_sequence/reviews/p164_a/PINNED_INPUTS.sha256`.  The
reviewer verifier was written from the literal map and theorem statements; it
does not import, call, or copy the author verifier.

The review independently re-derived Theorem 1(A)--(D), attacked all stated
parameter boundaries `q>=3` and dyadic `n>=4`, checked the excluded `n=2`
support-repair boundary, audited the direct owners and P1--P161 collisions,
performed two deterministic verifier replays, performed two source-only cold
builds, and inspected every PDF page, font row, metadata field, citation, and
final build warning.

## 2. Mathematical verdict by theorem part

| part | independent result | hostile boundary result |
|---|---|---|
| A: iterates, recurrence, clock, shells | **PASS** | `T_q^t(w)=1+D^(t-1)c(w)` and the one-block dyadic kernel flag re-derive correctly.  The final shell formula is correct and strictly positive, but the proof omits the elementary inequality establishing `>0`. |
| B: images and arbitrary-target fibres | **PASS** | Time-one holes are exactly complements of units.  For every `1<=j<=n`, including `j=n`, the all-one vector lies in `ker D^j`; a unit plus that vector has weight `n-1>=3`.  The proof is correct but should spell out this endpoint.  At `n=2` the repair fails exactly as the paper says. |
| C: time-two spectrum | **PASS** | `im D` is the even-weight hyperplane and each solvable syndrome has one complementary solution pair.  The formula and the `binom(n,r)` / half-central class counts are correct at all endpoints. |
| D: midpoint spectrum | **PASS** | `D^(n/2)=I+S^(n/2)`, the image is exactly `(u,u)`, the pair-factor enumerator is correct, and the formula and `binom(n/2,h)` class counts hold for `h=0` and `h=n/2`. |

The complete derivation, including the explicit positivity inequality and the
cap-time image repair, is frozen in
`docs/papers162_166_sequence/reviews/p164_a/PROOF_REDERIVATION.md`.

## 3. Targeted hostile attacks

### 3.1 Last-shell strict positivity

The value in equation (7) is correct.  Put `x=q-1>=2`.  Its direct expansion
is

```text
L = ((x+1)^n-(x-1)^n)/2 - x2^(n-1)
  >= x(n x^(n-2)-2^(n-1))
  >= x2^(n-2)(n-2) > 0,
```

for `n>=4`.  The manuscript currently jumps from the exact formula to “It is
positive”; this is repairable without changing the theorem.

### 3.2 Image feasibility at the nilpotent cap

For positive tail time, `j=min(t-1,n)` satisfies `1<=j<=n`.  Since `D1=0`,
the all-one vector belongs to `ker D^j` for every such `j`, including `j=n`.
If a syndrome coset is represented by the forbidden unit `e_i`, then
`e_i+1` is in the same coset and has weight `n-1>=3`, so Lemma 2 makes it a
feasible change mask.  At `j=n`, this proves feasibility in the sole terminal
coset; it does not silently assume `j<n`.  The verifier checks every `j` at
`n=4,8,16` and isolates the genuine `n=2` failure.

### 3.3 Parameter classes versus numerical collisions

The manuscript's wording is correct: parts (C) and (D) count parameter
classes, and equal numerical fibre values must be merged.  Independent
enumeration finds precisely the following collisions over the audited
spectra:

- `(n,q)=(4,4)`: parameters `1,2` collide in both the time-two and midpoint
  formulas;
- `(n,q)=(8,3)`: parameters `3,4` collide in both formulas.

Thus the example after Theorem 1 is valid, and the general merge instruction
also covers midpoint collisions.  No theorem change is needed.  Adding the
midpoint `(4,4)` example would be useful but is not a finding.

## 4. Findings and executable repairs

### Critical

None.

### Major

None.

### minor m1 — the proof of sharpness does not display the inequality

**Location:** `main.tex`, proof of Theorem 1(A), currently lines 195--203.

The strict inequality in equation (7) is true, but “It is positive for
`q>=3,n>=4`” leaves the only sharpness inequality unproved on the page.

**Executable repair:** after the last-shell expression, set `x=q-1` and add

```tex
Expanding the odd part and using $x=q-1\ge2$ gives
\[
 L\ge x\bigl(nx^{n-2}-2^{n-1}\bigr)
   \ge x2^{n-2}(n-2)>0,
\]
```

where `L` denotes the displayed last-shell quantity.  No statement, equation
number, or downstream proof changes.

### minor m2 — the all-one coset repair should quantify the cap endpoint

**Location:** `main.tex`, proof of Theorem 1(B), currently lines 208--213.

The argument is mathematically recoverable as written, but it does not
explicitly say why the all-one vector is in every relevant kernel, why the
complemented unit is feasible, or why this remains valid when `j=n`.  These
are precisely the boundary facts on which the claimed full image rests.

**Executable repair:** replace the compressed repair sentence with

```tex
Here $1\le j\le n$ and $D\one=0$, hence
$\one\in\ker D^j$, including when $j=n$.  If a chosen representative is a
unit $e_i$, then $e_i+\one$ has the same $D^j$-image and weight
$n-1\ge3$; Lemma~\ref{lem:chi} therefore makes it a feasible change mask.
Every affine class consequently contains a feasible representative.
```

This also makes the later `n=2` exclusion visibly necessary.  No theorem
formula changes.

## 5. Independent exact verification

Reviewer artifacts are under
`docs/papers162_166_sequence/reviews/p164_a/`:

- `verify_review.py` SHA-256:
  `51f1ac4357b922edb32807133645cd6f5c0de426744882d64b0316848e5eda72`;
- `CANONICAL.txt` SHA-256:
  `5ad48573820c14d20f881dd131eb0b7551024b239fb6eb6868ec003c749e830e`;
- replay 1 SHA-256:
  `5ad48573820c14d20f881dd131eb0b7551024b239fb6eb6868ec003c749e830e`;
- replay 2 SHA-256:
  `5ad48573820c14d20f881dd131eb0b7551024b239fb6eb6868ec003c749e830e`.

The two fresh outputs are byte-identical to each other and to the canonical
transcript.  The verifier executes **950,659 assertions**.  It starts from
the literal q-ary map and checks:

- 74,355 words in six boxes `(4,3),(4,4),(4,5),(4,6),(8,3),(8,4)`;
- every literal orbit through the cap, the iterate identity, every depth,
  shell, positive-time image, and binary target fibre;
- time-zero full image and singleton fibres;
- kernel/image flags and every unit repair for all `j` at `n=4,8,16`, with a
  dedicated `j=n` assertion and the excluded `n=2` counter-boundary;
- explicit last-shell lower bounds;
- both evaluated spectra at `n=4,8,16`, `q=3,4,5,7`, including endpoints,
  mass conservation, and numerical-collision aggregation.

Reproduction command:

```bash
python3 docs/papers162_166_sequence/reviews/p164_a/verify_review.py
```

## 6. Owner, citation, and internal-collision verdict

The owner firewall is accurate and unusually explicit:

- Martin--Odlyzko--Wolfram and Kim own the general algebraic and direct
  periodic Rule-102 matrix-power lanes;
- Zhao--Li--Yang--Fu--Shum owns the substantially more general homogeneous
  repeated-root cyclic-code weight-distribution lane;
- Bolognesi--Ciancia owns equality-pattern cellular automata in a different
  nominal carrier;
- the cycle chromatic polynomial and finite Fourier inversion are correctly
  assigned zero contribution credit.

P98 is the closest internal proof-engine collision and already occupies the
repeated-root linear-shift lane.  P164 survives only on its stated residual:
the finite-q nonlinear front, exceptional support holes, q-weighted affine
pullbacks, and the two evaluated target spectra.  P63, P117, and P138 have
different literal maps and theorem engines.  No direct full-system owner or
P1--P161 literal duplicate was located in the bounded audit.  This is an
**owner-thin pass**, not a novelty or priority claim.

All four citations resolve, the bibliographic details agree with the primary
sources inspected, and BibTeX reports zero warnings.  The separate audit is
`docs/papers162_166_sequence/reviews/p164_a/OWNER_AUDIT.md`.

## 7. Source-only builds and PDF QA

Two fresh directories received only `main.tex` and `references.bib`.  Both
completed `pdflatex -> bibtex -> pdflatex -> pdflatex`; their final logs and
PDFs are byte-identical.  Each output is also byte-identical to the frozen
paper PDF:

```text
pages:       4 (A4)
bytes:       300,597
PDF SHA-256: db26e57e610577cdff03c348fa3ce794165e3268393350d7d2f55b14e98070ae
fonts:       23/23 embedded, subsetted, Unicode mapped
final warnings/errors: 0
```

All four pages were rendered and inspected individually.  There is no
clipping, overlap, missing glyph, orphaned heading, or broken reference.  Page
4's white area is the natural end after reference 4.  PDF title, author,
subject, and keyword metadata are blank; the visible author is `Anonymous`,
and no affiliation, email, ORCID, acknowledgement, or institution is exposed.
Full receipts are in
`docs/papers162_166_sequence/reviews/p164_a/BUILD_QA.md`.

## 8. Final recommendation

**REVISE_MINOR — 0C / 0M / 2m.**  Theorem 1(A)--(D), all stated boundary
conditions, both target spectra, and the owner-subtracted residual package
survive independent hostile review.  Apply the two local proof-expansion
patches above, rebuild, and send the revised artifact to the next review
round.  Until those changes are reviewed, maintain **HOLD_EXTERNAL** and do
not post, circulate, or submit the manuscript.
