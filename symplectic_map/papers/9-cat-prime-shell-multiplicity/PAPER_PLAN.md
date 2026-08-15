# Paper Plan

## Frozen identity and release state

**Working title:** *A Multiplicity Audit for Prime-Torsion Euler Products of
the Cat Map*

**Article type:** low-novelty mathematical negative note / exact audit.

**One-sentence thesis:** classical prime-lattice orbit structure forces a
multiplicity exponent in the most direct prime-shell orbit product; fixed
nonzero scalar denominator weights cannot remove it, while the exact
fractional repair is shell-global, tautological, and non-prime-specific.

**Required terminal classification:**
`PRIME_SHELL_MULTIPLICITY_OBSTRUCTION_CERTIFIED /
A0_FAIL_GLOBAL_NORMALIZATION_ONLY / ROUTE_B_NOT_OPENED`.

**Novelty calibration:** **2.5--3/10**.  The note records and juxtaposes known
prime-lattice arithmetic with elementary product algebra.  It does not claim
a new finite-lattice orbit classification, dynamical zeta theory, transfer
determinant, prime-generating mechanism, or Riemann model.

> **Release gate:** the strict Paper-9 result package is closed and passed
> independent result-integrity review.  Its manifest has SHA-256
> `8ca12744638a47b6e4fa3239a60a19d79229d2b9596ae4fe4b2f66a399618f92`.
> This authorizes plan, citation, and figure assets under the frozen scope; it
> does not authorize a candidate rerun, a new prime/modulus scan, a
> centralizer computation, or manuscript drafting.

### Frozen inputs

| Role | Path | SHA-256 / state |
|---|---|---|
| source lock | `experiments/source_lock.json` | `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49` |
| proof source | `notes/PROOF_PACKAGE.md` | `47216ad4021d3476bfd0850ebec24c9ceafb5af8c0573214182fd2d0da7b2daa` |
| independent source review | `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `9509278ce55d908dba7d7cb4a809a335cc51d9364e8bfdfd1dc66be594775b8f` |
| exact registered result | `results/EXPERIMENT_RESULTS.json` | `448de06e92bd7ab4e5374e5d1f57413df45859cd3476ff14b2691b63ac364fab` |
| official result report | `experiments/OFFICIAL_EXPERIMENT_RESULTS.md` | `66bfefe9dcf5731cb89a0597deed5df322f9bc24f9fc3a592d4790a46d2a4dc0` |
| official validation report | `experiments/OFFICIAL_VALIDATION_REPORT.md` | `32a1758362f94372a83588de63e2b5df33a8f7e45e0646de53154a2ca1afaab4` |
| independent result review | `results/INDEPENDENT_RESULT_INTEGRITY.md` | `aa0c7db555f11920c7305be508f6cfff62375970e112e9f720111831da20b3bd` |
| strict result manifest | `results/result_manifest.json` | `PASS`; `8ca12744638a47b6e4fa3239a60a19d79229d2b9596ae4fe4b2f66a399618f92` |

The paper must not silently substitute later versions.  A changed theorem,
result, official report, or manifest requires a new claim--evidence and
asset-binding review.

## Scope and positioning

### In scope

1. A self-contained re-derivation of the prime-shell orbit classification for
   (A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)), with
   split, inert, binary, and ramified cases kept distinct.
2. The exact multiplicity formulas
   (m_p=(p+1)h_p) in the split case and
   (m_p=(p-1)h_p) in the inert case, together with the uniform odd-prime
   bound (m_p\ge p-1).
3. The binary boundary (m_2=1) and ramified profile at (p=5): two
   length-two cycles and two length-ten cycles.
4. A strict semantic separation between the point-potential/raw-return
   product and the externally assigned one-time orbit-label product.
5. The pure scalar denominator-degree obstruction, its zero-weight boundary,
   and the failure of equal weights beyond the first repetition.
6. The exact fractional shell identity and the reason it is global normalized
   counting rather than an ordinary local scalar potential.
7. The selector cost, safe global convergence bounds, and the explicit escape
   boundary for richer determinants and centralizer quotients.
8. A five-prime exact audit at (p\in\{2,3,5,7,11\}) as a
   development-seen implementation control only.

### Out of scope and explicit nonclaims

- No new prime-lattice or rational-lattice cycle classification.
- No numerical value of (s), no logarithm evaluation, no zero data, no
  prime scan, no composite-shell enumeration, and no candidate rerun.
- No exact abscissa, analytic continuation, functional equation, or statement
  in the gap (2<\operatorname{Re}s\le3).
- No prime-orbit or prime-zero correspondence and no Riemann hypothesis claim.
- No matrix-valued, numerator-bearing, alternating, transfer/Fredholm, or
  cohomological impossibility theorem.
- No claim that a canonical selector or centralizer quotient is impossible.
  The centralizer route is reserved for follow-up work and is not computed
  in the present audit.
- No Route B, quantization, spectral-landscape, Green-function, or
  Hilbert--P\'olya claim.

Use the verbs **record**, **re-derive**, **separate**, **audit**, and
**obstruct**.  Avoid “first,” “discover,” “new zeta function,” “prime-generating
cat map,” and “construct the Riemann dynamics.”

## Reader, format, and length

The intended reader works in arithmetic dynamics, smooth dynamics, or
mathematical physics and knows periodic-orbit products but may not know the
prime-lattice cat-map literature.  The target is a self-contained specialized
journal-style note; no venue is frozen.

Planned length: 10--12 pages of main text plus 3--5 pages of appendices.  The
split/inert proof, the (p=2,5) boundaries, and the raw-versus-label semantic
distinction remain in the main text.  Canonical cycle lists, audit provenance,
and mechanical ledger details may move to appendices.

## Claims--evidence matrix

| ID | Manuscript-level claim | Mathematical support | Exact audit support | Literature boundary | Status |
|---|---|---|---|---|---|
| C1 | For odd (p\ne5), every nonzero point has one common exact period; split shells have (m_p=(p+1)h_p), inert shells (m_p=(p-1)h_p). | Split diagonalization and inert (\mathbb F_{p^2}) multiplication in the frozen proof. | Fixed profiles at (p=3,7,11). | Gaspari 1994 is a direct collision; Baake--Neumärker--Roberts 2013 supplies close prime-power cycle formulas. | `CLASSICAL_REDERIVATION` |
| C2 | (p=2) has one three-cycle; (p=5) has two two-cycles and two ten-cycles; (p=2) is the unique one-orbit prime shell. | Cayley--Hamilton mod 2 and (A=-I+N), (N^2=0), rank (N=1) mod 5. | Exact rows at (p=2,5). | Appendix A.1 of Baake--Neumärker--Roberts 2013 is a direct boundary collision. | `CLASSICAL_REDERIVATION` |
| C3 | The point-potential factor is (Z_{\rm raw,p}=\prod_\gamma(1-p^{-s|\gamma|})^{-1}). | Fixed-point exponential grouped by primitive orbit and repeat. | Five exact raw factors, including the mixed (p=5) factor. | Artin--Mazur, Ruelle, Parry--Pollicott, Baake--Roberts--Weiss, and Chandra make the product formalism prior art. | `FORMAL_IDENTITY` |
| C4 | The distinct one-time label factor is (Z_{\rm lab,p}=(1-p^{-s})^{-m_p}), with repeat coefficient (m_p/r). | Direct logarithmic expansion. | Symbolic repeats (r=1,2,3). | The semantic separation, not the product itself, is the note's main audit contribution. | `FORMAL_IDENTITY` |
| C5 | For odd (p), fixed nonzero scalar coefficients independent of (z) cannot reduce the denominator degree from (m_p>1) to one. | Clear denominators and compare polynomial degrees. | Exact degree and zero-weight controls. | Elementary statement inside classical weighted-zeta formalism; it is not an operator theorem. | `PROVED_SCOPED` |
| C6 | Equal weights (w_\gamma=1/m_p) give power sums (m_p^{1-r}), so only (r=1) is repaired when (m_p>1). | Exact power-sum identity. | Rational controls for (r=1,2,3). | Elementary. | `FORMAL_IDENTITY` |
| C7 | Fractional exponents (|\gamma|/(p^2-1)) give one factor exactly but use the complete shell and extend symbolically to composite order (q). | Cycle partition and (J_2(q)) cardinality. | Exact prime weights; one proof-only symbolic (q) record, no scan. | Finite-permutation counting; not a prime-specific mechanism. | `A0_FAIL_GLOBAL_NORMALIZATION_ONLY` |
| C8 | The label logarithm diverges for real (1<s\le2), is not absolutely convergent for (1<\Re s\le2), and is absolutely convergent for (\Re s>3). | All-prime lower/upper bounds and comparison series. | None; finite rows cannot support global convergence. | Standard Euler-product analysis. | `PROOF_ONLY_SAFE_BOUNDS` |
| C9 | Selecting one orbit gives one factor only by adding symmetry breaking and discarding (m_p-1) cycles. | Definition and cycle count. | Selector-cost column at five locked primes. | No selector impossibility theorem. | `PROVED_CONSTRUCTION_COST` |
| X1 | A centralizer quotient may compress multiplicity. | Not investigated. | Zero centralizer computations. | Symmetry context in Baake--Neumärker--Roberts 2013. | `OUTSIDE_SCOPE_PAPER10` |
| X2 | Richer determinants may cancel multiplicity. | Requires a different construction and theorem. | No such computation. | Ruelle, Parry--Pollicott, and Chandra delimit the adjacent theory. | `OUTSIDE_SCOPE` |

## Core notation and theorem order

Use

\[
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
V_p=\mathbb F_p^2\setminus\{0\},\qquad
\Gamma_p=V_p/\langle A\rangle,
\]

and let (m_p=|\Gamma_p|).  A “raw return” always retains the primitive
orbit length (|\gamma|); an “orbit label” assigns (log p) once to an
already identified primitive orbit.  These must never be conflated.

Recommended logical order:

1. classify (A) over prime fields and count cycles;
2. isolate (p=2) and (p=5);
3. derive the raw-return and orbit-label products separately;
4. prove the scalar degree obstruction and repetition ledger;
5. identify fractional normalization and selector cost;
6. state safe global bounds and richer escape mechanisms;
7. report the frozen five-prime exact audit as corroboration only.

## Section-by-section outline

### Abstract (140--170 words)

State the classical multiplicity theorem, the two product semantics, the
scoped degree obstruction, and the global fractional repair.  Name the result
as a low-novelty negative audit.  End with the exact conclusion that Route A0
fails by global normalization only and Route B is not opened.  Do not cite
papers or claim analytic continuation in the abstract.

### 1. Introduction and bounded question (1.25 pages)

Ask whether one can obtain one Riemann-style local denominator from the
complete nonzero (p)-torsion shell of one fixed cat map.  Immediately
distinguish this diagnostic from the ordinary toral dynamical zeta function.
Place Gaspari 1994 and Baake--Neumärker--Roberts 2013 beside the orbit
classification, and Baake--Roberts--Weiss 2008 beside finite-lattice products.
State the qualitative low-novelty synthesis/audit positioning and the exact
nonclaims.  The 2.5--3/10 score remains an internal planning diagnostic.

### 2. Prime-shell arithmetic (2.25 pages)

For odd (p\ne5), treat split and inert characteristic-polynomial cases
separately.  Define (\tau_p) and (h_p), prove that every nonzero point has
period (\tau_p), and obtain

\[
m_p=(p+1)h_p\quad\text{(split)},\qquad
m_p=(p-1)h_p\quad\text{(inert)}.
\]

Then give the binary one-cycle proof and the ramified nilpotent calculation
at five.  Conclude that (p=2) is uniquely multiplicity-free and that every
odd prime has (m_p\ge p-1).  Figure 1 supports this section.

### 3. Two products that must not be identified (2.0 pages)

Derive

\[
Z_{\rm raw,p}(s)=\prod_{\gamma\in\Gamma_p}
 (1-p^{-s|\gamma|})^{-1}
\]

from the point potential and its repeated returns.  Separately define

\[
Z_{\rm lab,p}(s)=(1-p^{-s})^{-m_p}
\]

after assigning the shell label once per primitive orbit.  Display the
coefficient (m_p/r) for repetition (r), with the mixed (p=5) raw factor
as the semantic stress test.  Figure 2 supports this section.

### 4. Scalar obstruction and exact normalization boundary (2.25 pages)

Clear denominators in

\[
\prod_{\gamma}(1-w_\gamma z)^{-1}=(1-z)^{-1}.
\]

If every fixed scalar (w_\gamma\ne0), the left denominator has degree
(m_p); equality is impossible for odd (p).  If zeros are allowed, equality
forces the multiset ({1,0,\ldots,0}), hence discards all but one orbit.
Show that (w_\gamma=1/m_p) repairs only the first power sum.

Then prove

\[
\prod_{\gamma\in\Gamma_p}(1-p^{-s})^{-|\gamma|/(p^2-1)}
=(1-p^{-s})^{-1},
\]

label it `GLOBAL_NORMALIZED_COUNTING`, and give the symbolic (J_2(q))
extension without choosing or enumerating a composite (q).  Figure 3
supports this section.

### 5. Global bounds and escape boundary (1.0 page)

Use (m_p\ge p-1) and (m_p\le p^2-1) to state only the frozen safe bounds.
Leave (2<\Re s\le3) open.  Separate the scalar theorem from possible
matrix-valued factors, numerator/alternating cancellation, Fredholm or
cohomological determinants, enriched selectors, and centralizer quotients.
The centralizer is a live follow-up route, not a computation in the present
audit.

### 6. Exact audit and provenance (0.75 page)

Report one registered exact audit at exactly (p=2,3,5,7,11), 203 nonzero
points, 37 primitive cycles, dual exact engines, and all twelve controls.
State that the rows were development-seen and cannot prove an all-prime or
global analytic statement.  Report zero numerical (s/log) evaluations,
zero prime scans, zero composite scans, zero centralizer computations, and no
rerun.

### 7. Limitations and conclusion (0.75 page)

Reiterate the dominant prior-art collisions and the narrow surviving value:
a transparent semantic and mechanism failure record.  State the exact
terminal classification.  The next mathematical question is whether a
centralizer-enriched quotient can collapse multiplicity without merely
renaming a globally selected shell; do not answer it here.

### Appendices (3--5 pages)

- **Appendix A:** complete split/inert/binary/ramified proof.
- **Appendix B:** formal product and power-sum algebra, including zero weights.
- **Appendix C:** exact five-prime ledger and JSON field map.
- **Appendix D:** source/result/figure provenance and frozen hashes.

## Planned publication figures

Exactly three deterministic figures are authorized.  Each must be generated
from the manifest-bound JSON through a hash-checking data contract and emitted
as vector PDF, selectable-text SVG, and 300 dpi PNG.

### Figure 1: Fixed prime-shell profiles and multiplicity

**Message:** only (p=2) has one primitive orbit; (p=5) is the ramified
mixed-length boundary, while the odd controls already exhibit multiplicity.

**Layout:** (A) exact point-period bars by prime, split by orbit length; (B)
primitive-cycle profiles and (m_p) on a compact linear axis; (C)
boundary cards for (p=2) and (p=5), with the (p=11) eigenline/off-line
strata shown as a distinct split control.  Caption must call all five rows
development-seen controls and reserve the all-prime conclusion to the proof.

### Figure 2: Raw return versus one-time orbit label

**Message:** raw point returns retain (|\gamma|), while relabeling every
primitive orbit by (p) produces multiplicity (m_p) and repeat coefficient
(m_p/r).

**Layout:** (A) two nonidentical construction pipelines; (B) the ramified
(p=5) stress test; (C) an exact (p\)-by-(r) coefficient grid for
(r=1,2,3).  No numerical (s) or logarithm may be evaluated.

### Figure 3: Mechanism boundary

**Message:** scalar and equal-weight repairs fail for odd shells; fractional
counting succeeds only globally; a selector succeeds only by discarding
cycles; the centralizer route remains untested.

**Layout:** (A) a five-mechanism decision table for scalar, equal,
fractional, selector, and centralizer routes; (B) exact equal-weight power sums
at repetitions 1--3; (C) fractional weights and selector costs for the five
locked shells.  Status must be redundantly encoded by text, shape, and color.

## Citation and attribution plan

The bibliography contains exactly the eleven frozen primary records verified
in `notes/CITATION_VERIFICATION.md`.  Direct collision citations must appear
at the claim site, not only in a general related-work paragraph:

- Gaspari 1994 beside the common-period and orbit-decomposition theorem;
- Baake--Neumärker--Roberts 2013 beside the (p=2,5) cycle boundaries and
  the centralizer escape;
- Baake--Roberts--Weiss 2008 beside finite-lattice Euler products;
- Artin--Mazur, Ruelle, and Parry--Pollicott beside the primitive/repetition
  and weighted-product formalism;
- Tan--Li 2025 and Chandra 2026 only as contemporary collision/context, not
  as evidence for the present audit's theorem.

## Reproducibility and review gates

1. Figure loaders verify the frozen source, proof, raw-result, manifest,
   official-report, and result-review hashes before parsing data.
2. All figure values come from `results/EXPERIMENT_RESULTS.json` or from
   exact rational transformations of its fields.  No candidate module is
   imported or run.
3. Each of nine outputs is generated twice with fixed metadata,
   `PYTHONHASHSEED=0`, fixed SVG hash salt, a fixed source-date epoch, and
   bytecode writes disabled.  Both runs must be byte-identical.
4. PDF fonts must be embedded and no PDF/SVG may contain a raster object.
   SVG text must remain selectable; PNG fallbacks must report 300 dpi.
5. Original-resolution previews must pass human visual inspection for
   clipping, overlap, mathematical rendering, grayscale redundancy, and
   evidence-boundary wording.
6. After author-side freeze, a fresh independent reviewer must audit this
   plan, the citation ledger/BibTeX key set, all generators, input bindings,
   double-run hashes, rendering QA, captions, and visual semantics.
7. **Stop at that independent plan/figure gate.**  No manuscript may be
   drafted until a separate authorization follows an independent PASS.
