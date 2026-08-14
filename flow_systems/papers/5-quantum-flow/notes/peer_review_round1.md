# Paper 5 independent peer review — Round 1 and final gate

**Manuscript:** *The Canonical Koopman Lift Is Too Large: Dense Rational
Spectrum for a Frobenius Suspension*  
**Review date:** 2026-08-13  
**Review mode:** independent adversarial mathematical, Route, source, artifact,
and release review  
**Final recommendation:** **ACCEPT**  
**Confidence:** **5/5**  
**Issue count:** **0 critical / 0 major / 0 residual required minor**

## 1. Submission lock

- `paper/manuscript.tex` SHA-256:
  `3616a52872510f9b8ddb355b8f35b437ba0956dc592342757f5c64f5214c8f4a`.
- `paper/manuscript.pdf` and `paper/paper.pdf` SHA-256:
  `767eb1d2764d4276392d77e61d772caa94bd985b530d75cb16b195ab7082413d`.
- The two PDFs are byte-identical; the release has 14 letter-size pages.
- `results/koopman_spectral_manifest.json` SHA-256:
  `af9746cd5a5684ecbd7c92fdbbbf661ad6ad6acd00577c8ce5aa938421bf0344`.
- Route-A Stage-5 YAML SHA-256:
  `db55fad0bb5ccb4fa0ee35472f77a046e2cd78d1efba133be0907e8944489f04`.

## 2. Mathematical verdict

The core theorem chain passes independent checking.

1. The countable Hilbert direct sum, invariant weighted measures, Koopman
   action, periodic boundary conditions, and maximal graph-summability domain
   are explicit. The map
   $W_wf=(\sqrt{w_x}f_x)_x$ is unitary for every family of finite, strictly
   positive component weights and maps the full generator domains onto one
   another.
2. Circle Fourier transform identifies each component generator with real
   multiplication by $2\pi n/L_x$ on periodic $H^1$. The countable
   orthogonal-sum theorem therefore proves self-adjointness on the displayed
   global domain. The sign check agrees with
   $U_tf=f(u-t)=e^{-itA_w}f$, and finite-component trigonometric polynomials
   form a graph-norm core.
3. The elementary closed-point argument proves that a component exists in
   every degree. Taking the union of the degree-$d$ Fourier lattices gives
   
   \[
   \sigma_{\rm p}(A_w)=\frac{2\pi}{\log2}\mathbb Q.
   \]
   For $q=a/b$, degrees $kb$ and modes $ka$ give infinitely many
   orthogonal witnesses for the same eigenvalue. Thus every **point
   eigenvalue**, including zero, has countably infinite multiplicity; the
   manuscript does not incorrectly extend this eigenvalue statement to
   irrational spectral points.
4. Closure of the component spectra gives $\sigma(A_w)=\mathbb R$. Exact
   orthogonal eigenvectors at rational points and singular Weyl sequences
   approaching irrational points prove
   $\sigma_{\rm ess}(A_w)=\mathbb R$ and
   $\sigma_{\rm disc}(A_w)=\varnothing$. The text correctly distinguishes a
   complete pure-point eigenbasis/atomic vector spectral measures from the
   operator-set decomposition in which irrational reals lie in continuous
   spectrum.
5. Infinite-multiplicity eigenspaces directly prove noncompact resolvent,
   infinite rank for every positive-width interval projection, and failure of
   trace class for $e^{-tA_w^2}$, $e^{-t|A_w|}$, and
   $(1+A_w^2)^{-s/2}$. Repeating the argument at a nonzero rational
   eigenvalue proves that deletion of the kernel repairs none of these
   failures. The manuscript properly avoids treating the unbounded
   $e^{-tA_w}$ as a heat operator.

The determinant conclusion is also correctly scoped. It excludes the ordinary
trace-class Fredholm and compact-resolvent spectral-zeta mechanisms for the
frozen generator; it does not claim that every possible relative, compressed,
or renormalized determinant is impossible. The orbit Hasse--Weil product,
Deligne's finite-dimensional cohomological Frobenius determinant, and the
Koopman/Stone generator remain in separate operator ledgers.

## 3. Strongest counter-argument and adjudication

The strongest attempted repair is that the spectral pathology might be an
artifact of infinite total mass, component normalization, or the invariant
zero modes. It is not. Positive component reweighting is explicitly unitarily
equivalent to the canonical model, including summable probability weights;
retaining only one closed point per degree still realizes every rational
frequency infinitely often; and after deleting all zero modes, every fixed
nonzero rational frequency still has an infinite-dimensional eigenspace. A
finite-degree cutoff can have compact resolvent, but it is a different object
and no cutoff-removal or determinant-renormalization theorem is supplied.

Accordingly, the B3 obstruction is intrinsic to the frozen uncoupled Koopman
candidate. It is not a no-go theorem for every Frobenius-inspired operator,
coupled model, compression, or new quantization scheme, and the manuscript
states this boundary clearly.

## 4. Route-A and limited Route-B audit

The Stage-5 YAML parses and supports
`A4_UNITARY_OR_SCATTERING_CANDIDATE — PROVED`, while explicitly withholding
`A4_NATURAL_QUANTIZATION` and `A4_ROUTE_B_READY`. Its overall
`ROUTE_A_SUCCESS_ROUTE_B_NOT_READY` is confined to the native finite-field
positive control; the earlier rejection against the Riemann target remains
unchanged.

The project-lead exception authorizes exactly the early B1--B3 audit. The
supported scoped verdict is:

```text
B1_COMPLETE_OPERATOR_DEFINITION — PROVED
B2_SELF_ADJOINT — PROVED
B3_FAIL — PROVED
overall: ROUTE_B_REJECTED at Gate C
hilbert_polya_claim_allowed: false
```

B4 and B5 receive no evaluator verdict. In the manifest,
`limited_route_b` contains only `b1`, `b2`, `b3`, scope, overall status, and
the Hilbert--Pólya permission flag; `b4_b5_invoked` is `false`. The manuscript
and notes use “not invoked” only as a scope annotation. No invented B4/B5 enum
or synthetic full Route-B serialization was found.

## 5. Required minor revisions — closed before final lock

1. The probability-measure condition is now stated correctly as
   $\sum_xw_xL_x=1$, and the ambiguous phrase “strictly positive finite
   family” was replaced across the release surfaces by “family of finite,
   strictly positive component weights.” **Addressed.**
2. `research_protocol.md` now quantifies the local-rank theorem over intervals
   of positive width and explicitly records that an irrational singleton has
   zero spectral projection. **Addressed.**

The final manuscript also names $a\mapsto a^2$ as the square-map Frobenius
convention and explains that inversion reverses finite cycles without changing
degree, suspension length, or the spectral calculation. No required action
remains.

## 6. Citation and source-claim verdict

All ten bibliography entries are cited, the BibTeX log is clean, and their
identities agree with the source matrix. The five acquired authoritative PDFs
match the recorded hashes. Direct inspection of the extracted sources confirms
the load-bearing locators: Teschl Theorem 2.23 for self-adjoint orthogonal sums
and spectral closure; Teschl Theorems 5.1--5.2 for the Stone convention;
Niederreiter--Xing Theorem 1.3.6 for irreducible counts; Deligne equation
(1.5.4) for the graded cohomological determinant; and Bornemann Sections 2--3
for the ordinary trace-class determinant boundary.

No cited source is asked to prove the candidate-specific dense spectrum,
multiplicity, Weyl-sequence, compactness, or heat results; those are derived in
the manuscript. Historical Koopman, Stone, and Kostant citations are not used
to infer a physical quantization or Hilbert--Pólya realization. **Citation
verdict: PASS.**

## 7. Reproduction and release checks

- `./experiments/reproduce.sh`: **8/8 tests passed**; rerunning it left every
  generated artifact hash unchanged.
- Closed-point positivity/fixed-point reconstruction, signed rational-frequency
  witnesses, nonzero kernel-deletion control, and the weighted-unitary
  regression all pass. The finite controls are correctly presented as
  regressions, not proofs of the infinite theorems.
- The manifest records no target-zero data, no fitted parameters, and no B4/B5
  invocation.
- A clean independent XeLaTeX/BibTeX/XeLaTeX/XeLaTeX build succeeds at 14
  pages with no unresolved citation/reference, missing character, overfull box,
  or compilation error. Five underfull-box notices are confined to narrow table
  cells and do not remove or clip content.
- `pdfinfo` and `pdftotext` succeed. All 14 pages were rasterized, and
  representative theorem, ledger/figure, Route/control, and bibliography pages
  were visually inspected without finding clipping, overlap, or missing
  glyphs. Status-token adjacency is clean.
- The ARS PDF parser preflight remains **UNAVAILABLE** solely because `pypdf`
  is not installed; this was not promoted to a pass. The manuscript uses stable
  theorem/section/equation locators rather than uncertified reader-page anchors.

## 8. Final adjudication

No critical, major, or residual required minor issue remains. The paper proves
a complete and natural self-adjoint Koopman lift, then correctly uses its exact
dense, infinitely degenerate essential spectrum as a disqualifying B3 result.
It neither mistakes pure-point spectral measures for compact-resolvent discrete
spectrum nor imports the orbit/cohomological determinant into the Koopman
ledger. The scoped Route verdicts, citations, deterministic artifacts, and
release PDF are consistent with the proved claims.

**FINAL GATE: ACCEPT.**

## 9. Metadata-only release re-lock addendum

After the final mathematical gate, the Koopman 1931 bibliography title was
corrected from singular “Transformation” to the source-accurate plural
“Transformations.” This is a metadata-only change.

- `paper/manuscript.tex` is unchanged at SHA-256
  `3616a52872510f9b8ddb355b8f35b437ba0956dc592342757f5c64f5214c8f4a`.
- The corrected `paper/references.bib` SHA-256 is
  `e020001bf9a2273bd58ff5454dc24d61d58627ed1940950dde685c63303bbc46`.
- The byte-identical `paper/manuscript.pdf` and `paper/paper.pdf` are re-locked
  at SHA-256
  `802ad1a1169be166d5a82da2e0247a92e6c848113303c7d70818bbdfd90acef5`.
- The release remains 14 pages. The bibliography pages were re-rendered and
  visually checked; `pdftotext` and the status-adjacency scan remain clean.

No theorem, formula, Route verdict, artifact, citation-to-claim mapping, or
layout conclusion changed. The final **ACCEPT** recommendation remains in
force; this addendum supersedes only the earlier Paper-5 PDF and bibliography
hashes.
