# Paper plan and claim--evidence map

## Working title

**Open Modular Scattering Under Trace Closure**

Subtitle: **Endpoint Coboundaries, Selberg Loops, and Commuting Squarefree
Cusp Channels**

## One-sentence contribution

We prove that the modular denominator becomes an algebraic coboundary when
rational endpoints are retained, that full-boundary automorphy-period support
contains only signed Selberg lengths, and that standard squarefree multi-cusp
scattering matrices form a simultaneously diagonalizable family, while
explicitly identifying the off-diagonal structures outside the obstruction.

## Paper type

Theory plus exact reproducibility note.  The article uses a conventional
mathematics layout rather than an ML conference template.  Proofs remain in
the main manuscript; machine-schema details go to the appendix.

## Claims--evidence matrix

| claim | evidence | status | section |
|---|---|---|---|
| Unoriented open scattering has the displayed two-term Dirichlet--Laplace series | coefficient classification, Euler products, \(q\le2000\) audit | classical corollary / positive control | \(\S2\) |
| Double cosets do not compose canonically | exact representative witness | proved | \(\S3\) |
| Every displayed rational-endpoint projective-section cocycle is an algebraic coboundary | primitive integral section | proved; no analytic conjugacy claimed | \(\S3\) |
| Positive reversal-even sojourn time is not a real groupoid 1-cocycle | inversion identity | proved | \(\S3\) |
| Full-boundary nonzero loop periods are signed Selberg lengths | real fixed-point classification and eigenvalues | proved | \(\S4\) |
| Squarefree scattering is tensor-factorized and has a fixed Walsh eigenbasis | classical source formula plus exact reconstruction | classical input / proved corollary | \(\S5\) |
| Frozen bare products at distinct spectral parameters are permutation-invariant | analytic commutator theorem and 80-digit matrices | proved; conditional modeling diagnostic | \(\S5\) |
| Projector-resolved amplitudes retain assignment/path information | frozen \(\Gamma_0(6)\) witness | finite positive signal only; not intrinsic chronology | \(\S6\) |
| Standard eigenchannels retain the shifted zeta quotient divisor | local-factor zero/pole lines | proved, scoped | \(\S7\) |
| A Hilbert--P\'olya operator follows | none | not claimed | \(\S7\) |

## Section structure

1. Introduction: open arithmetic versus diagonal trace closure; state the
   dichotomy and scope on page one.
2. Open scattering positive control: geometric count, explicit series, and
   why it is not an Euler product over closed primitive orbits.
3. Rational endpoint groupoid: failed double-coset composition, automorphy
   cocycle, primitive gauge, and coboundary theorem.
4. Boundary loops: rational parabolics, quadratic hyperbolics, signed Selberg
   periods, and the ordinary-trace consequence.
5. Squarefree multi-cusp scattering: tensor blocks, Walsh characters,
   determinant, functional equation, and exact product permutation invariance.
6. What remains open: endpoint-projector amplitudes and the explicit
   \(\Gamma_0(6)\) assignment/path-sensitivity witness.
7. Divisor and Route-A evaluation.
8. Reproducibility, limitations, and conclusion.
9. Appendix: proofs, coefficient Euler factors, and result schema.

## Main tables

| ID | content | source |
|---|---|---|
| Table 1 | open off-diagonal data versus cusp-only trace versus full-boundary trace | theorem synthesis |
| Table 2 | object-wise Route-A A1--A4 decision | frozen evaluation YAML |

No decorative figure is needed.  A compact theorem-flow diagram may be added
only if it makes the three closures easier to distinguish than Table 1.

## Citation plan

- Introduction/geometric setup: Guillemin; Ji--Zworski and their correction;
  Pujahari--Satpathy.
- Groupoid/cocycle context: Nekrashevych; Mayer; Pohl--Wabnitz.
- Multi-cusp formulas: Huxley/Hejhal through verified published formulae;
  Young; Cakoni--Chanillo; Levitin--Strohmaier.
- Off-diagonal boundary: Kloosterman--Selberg and current modular-symbol
  twists, cited only to delimit novelty.

## Reviewer red lines

- Do not call the open series a new zeta theory.
- Do not claim every endpoint or matrix cocycle is excluded.
- Do not infer that a fixed basis change itself destroys information.
- Attribute order blindness to the frozen commuting scattering algebra.
- State that projectors can leave that algebra and restore assignment/path
  sensitivity, not a source-derived chronology.
- State that the rational coboundary is algebraic/set-theoretic and does not
  imply bounded analytic transfer-operator conjugacy.
- Do not identify resonances with a discrete self-adjoint point spectrum.
