# Internal hostile-review protocol — P167–P171

**External state:** `HOLD_EXTERNAL`.  Manuscripts, source packages, and
review material must not be transmitted to an external model, author, or
specialist.  Candidate gates and scouting dossiers do not replace either of
the two manuscript reviews.

## Round and role separation

Each paper begins with an immutable author-side `main_round0_original.pdf`.
Review A is an independent cold theorem/source/artifact attack.  Any accepted
repair is rebuilt and frozen as `main_round1.pdf`; a no-change decision is
recorded by a byte-identical copy.  Review B is performed by a different
internal reader after Review A and may not be authored by the paper's
construction agent.  Its accepted artifact is frozen as `main_round2.pdf`.

Across the two reviews, every paper must receive both:

1. a line-by-line deductive rederivation from the literal update, including
   inverse directions and sharpness witnesses; and
2. at least one separately implemented exact verifier whose carrier and
   internal representation are not imported from the author verifier.

Both reviewers also replay the author transcript when practical.  Finite
enumeration remains counterexample pressure, never a substitute for the
uniform proof.

## Required contents and severity

Each retained `HOSTILE_REVIEW_A.md` and `HOSTILE_REVIEW_B.md` must state the
pinned input, verdict, Critical/Major/Minor counts, theorem disposition,
owner subtraction, boundary attacks, executable evidence, source-only build
results, PDF/anonymity/integrity results, and external lifecycle.

- **Critical:** false central theorem, direct owner eliminating the residual,
  irreproducible evidence, or anonymity/integrity failure.
- **Major:** proof gap, theorem-ceiling violation, missing decisive boundary,
  materially misleading provenance, or paper-scale failure after owner
  subtraction.
- **Minor:** local clarity, source currency, attribution metadata, verifier
  coverage, artifact provenance, or noncentral presentation defect.

Every finding is closed in `IMPROVEMENT_LOG.md` before Round 2.  No unresolved
Critical, Major, or Minor finding is compatible with internal acceptance.

## Paper-specific mandatory attacks

- **P167 / MIP:** equivalence of inverse-position and component surgery;
  identity default for absent values; cycle inversion; path reversal and
  splitting; exact full-carrier and first-image clocks; recurrent EGF and
  iterate-fixed census; every-target fibre reconstruction and Bell maximum,
  including empty image, loops, and repeated functional-graph attachments.
- **P168 / QIS:** basis-free well-definedness under scalar representatives;
  inverse-line geometry in `F_(p^4)`; all plane ranks at `p=2` and odd `p`;
  hyperplane-to-field step; exact height convention; Gaussian-binomial
  carrier counts; every positive-time fibre, especially the exceptional
  two-to-one `p=2` plane-to-hyperplane branch; and the Kolomeec--Bykov owner
  boundary.
- **P169 / STF:** restricted-growth-word equivalence; canonical block order
  through cyclic wrap; load-smoothing and labelled-height cones; dense and
  sparse terminal regimes; exact sharp tail on every `k`-block stratum;
  least periods rather than dividing periods; trace-product fibre
  reconstruction, singleton deletion, multiplicities, and the interlacing
  nonuniform-fibre witness.
- **P170 / RPS:** interpretation of independent fresh permutations at each
  epoch; endpoint-history inclusion--exclusion; impossible `n-1` endpoint
  from the full source; containment eigenbasis; absorption CDF, PGF, and
  moments; cycle-marked history polynomial; sharp minimum and maximum marked
  degrees; conditional cycle expectation; and the explicit `n=1,2,3`
  asymptotic boundaries, with the two-scale claim beginning only at `n>=4`.
- **P171 / BGM:** transpose and Boolean-semiring orientation; the
  post-first-image exponent `2^(t-1)`; loop padding and the `D<=1` clock;
  partial-equivalence fixed classification and `B_(n+1)` census; path-
  incidence sharpness at `n=1,2`; all-target ordered-column
  inclusion--exclusion; empty/repeated columns; loop atoms; clique-cover
  image iff; the looped `K_(2,3)` obstruction; and direct subtraction of
  Boolean-power, graph-intersection, and symmetric-factorization owners.

## Build and artifact attack

Each review checks two fresh directories populated only with `main.tex` and
`references.bib`, using the declared
`pdflatex / bibtex / pdflatex / pdflatex` sequence.  Settled logs must have no
genuine warning, bad box, unresolved reference/citation, rerun request, or
fatal diagnostic.  Every page is inspected after rasterization.  Font rows
must be embedded, subsetted, and Unicode mapped; identifying metadata fields
must be blank; bylines must be anonymous; and there must be no encryption,
form, JavaScript, attachment, identifying path, or release language.

## Final artifact invariant

At closure, `main.pdf` and `main_round2.pdf` are byte-identical.  Round-0,
Round-1, and Round-2 PDFs remain preserved.  Each paper-local `SHA256SUMS`
excludes itself and covers every other retained local file.  The batch
canonical-PDF manifest covers exactly P167–P171 and passes 5/5.  Internal
acceptance never authorizes posting, circulation, contact, priority language,
or submission.
