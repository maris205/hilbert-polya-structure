# P111 — Positive Heisenberg Word-Area Cocycles

Status: **FINAL QA PASS / INTERNAL FREEZE / EXTERNAL HOLD**.

Choose

```text
X = I + E_12 with probability p,
Y = I + E_23 with probability 1-p,
M_n = A_n ... A_1.
```

The central coordinate of this positive Heisenberg product is the number
`C_n` of `Y`-before-`X` pairs in the chronological word. The paper combines
the exact finite-word law with an independent centered-pair expansion.

## Theorem package

- Exact finite-time normal form
  `M_n = H(J_n,n-J_n,C_n)` under the stated left-product convention.
- Conditional Gaussian-binomial area polynomial and the full biased PGF
  `E[z^C_n] = sum_j p^j(1-p)^(n-j) [n choose j]_z`.
- Exact mean and variance for every `p in [0,1]`, with two independent
  derivations of the variance.
- For `0<p<1`, `C_n/n^2 -> p(1-p)/2` almost surely and
  `(C_n-E C_n)/n^(3/2)` converges to a centered Gaussian with variance
  `p(1-p)(3p^2-3p+1)/3`.
- Every fixed matrix norm has logarithmic polynomial exponent two for
  `0<p<1`, but exponent one at the deterministic endpoints.
- The `n^2`-scale annealed area pressure equals `theta/4` for positive
  tilt in the interior and zero for nonpositive tilt; the pathwise value is
  `theta p(1-p)/2`, giving a strict gap for every nonzero tilt.

Gaussian-binomial inversion laws are expressly treated as owned background.
Takács's uniform lattice-path area results and Janson's uniform random-word
inversion moments, limit theorems, and Hoeffding decomposition directly own
the fair binary specialization; general random-word subsequence methods and
random walks on Heisenberg/unitriangular groups are also subtracted. The
residual scope is only the arbitrary-bias conjunction, polynomial exponent
boundary, and quadratic pressure kink for the displayed positive pair. This
scope statement is not a novelty or priority claim.
Internally it is separated at update-rule level from P70's finite-quotient
weighted shifts, P93's symbolic push--pop stack maps, P99's deterministic
integer-sublattice shear, and P104's contracting monomial cocycle.

## Exact control

From this directory, run:

```text
python3 code/verify.py
```

The standard-library verifier uses exact integer and `Fraction` arithmetic,
with no sampling, floating point, network access, or external package. The
fresh author run passed **421,285 assertions**; exact stdout is stored in
`code/verify.out`. See `CONTROL_RESULTS.md` for coverage and evidence
limits.

## Build

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

See `BUILD.md` for the author, review, and final production records.

## Files

- `main.tex`, `references.bib`, `main.pdf` — anonymous short paper
- `code/verify.py`, `code/verify.out` — exact verifier and stored fresh run
- `PROOF_ROUTES.md` — primitive-data separation between the two proof lanes
- `CLAIMS_EVIDENCE.md`, `CONTROL_RESULTS.md` — traceability and controls
- `BUILD.md` — author, review, and final production record
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`, `HOSTILE_REVIEW.md` —
  independent audits and their consolidated decision
- `FINAL_QA.md`, `SHA256SUMS` — frozen mechanical gate and package seal

Public posting, submission, specialist contact, and any novelty or priority
language remain **HOLD**.
