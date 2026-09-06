# C401 paper plan: exact Frobenius–Hénon equalizers

Date: 2026-09-05. Parent authority: `../BATCH_PLAN.md`.
Type: mathematical research article, no assigned journal and no page quota.
Language: English mathematical manuscript; anonymous human-author block.
Internal series identifier: C401, explicitly not a journal designation.

## One-sentence contribution

For every generalized Hénon map over a finite field, every nonresonant pair
of Hénon and Frobenius clocks has exactly `max(d^n q^r, q^(2r))` distinct
geometric equalizer points, with a coefficient-uniform calculation of both
boundary multiplicities and the exact short-twist defect.

Working title: **Exact Frobenius–Hénon equalizers and their boundary defects**.
Alternative titles considered: “Two-clock intersection counts for Hénon maps
over finite fields”; “Boundary multiplicities in Frobenius-twisted Hénon
dynamics”. The selected title names both the object and the calculation,
without claiming a new general trace formula.

## Frozen inputs and claim/evidence map

The original contract, producer, results, and proof review remain unchanged.
All proofs are included in the main text, not outsourced to the contract.

| Claim | Proof evidence and required assumptions | Body location |
|---|---|---|
| Exact nonresonant geometric max-law | Degree induction, graph classes, Jacobian, two completed local rings; `d>=2`, `a!=0`, `d^n!=q^r` | Main theorem in §1; full proof in §§3–4 |
| All pairs when d is not a p-power | Prime-factor argument applied to the max-law | Corollary in §1, full proof in §4 |
| Exact short-twist defect and first/eventual threshold | Max-law and classical compactly supported cohomology of affine space | §5 |
| Fixed-n slice formula and transcendence when d^n>q | Finite defect polynomial; elementary exponential-growth contradiction to an algebraic equation | §5 |
| No all-r finite-dimensional invertible-Frobenius weighted trace for a defective slice | Cayley–Hamilton with nonzero recurrence constant and backward induction; no commutation assumption | §5 |
| Rational zeta of the genuine diagonal system | Coefficient-field commutation and main theorem for `(km,sm)` | §6 |
| Resonance is excluded for a real nonlinear reason | Hand elimination to `x^6-x` in characteristic three, derivative `-1` | §6 |

The complete recorded 47 nonresonant Gröbner checks and one resonant negative
control are illustrative exact checks, not proof of the quantified theorem.
They will be described once in the reproducibility paragraph, without a rerun,
new experiment, performance plot, or census-based novelty claim.

## Section structure and argument blueprint

There are seven numbered sections plus one abstract file. Length is determined
by the complete argument rather than a word or page target.

0. **Abstract.** State the equalizer and max-law with all clocks and nonresonance;
   identify boundary lengths `Q min(D,Q)` and `1`; distinguish slice and
   diagonal zetas; flag a genuine resonant counterexample. No references.
1. **Introduction and main theorem.** Define `q=p^e`, algebraic closure, the
   exact map, actual power morphism and both positive clocks before the
   theorem. Give main theorem, all-clock corollary and the two concrete
   deliverables (exact boundary count and resulting clock distinction).
2. **Classical trace results and the question addressed here.** Credit Fujiwara
   and Varshavsky for eventual trace agreement, Shuddhodan for twisted
   étaleness, torus example and threshold-growth motivation. Cite the inspected
   v2 locators explicitly. Explain the limited Hénon increment without a
   universal negative or global priority claim. Classical Chow and cohomology
   inputs are identified as such.
3. **Iterate geometry and projective graph classes.** Prove forward and inverse
   degree induction, uniqueness of the opposite base points and graph-chart
   assertions. Compute every coefficient of both graph classes and their
   intersection product. State that properness will be proved locally.
4. **Affine reduction and the two boundary lengths.** Prove affine finiteness
   and reducedness for all clocks; locate both boundary intersections; prove
   the non-zero-divisor filtration and `Q min(D,Q)` length; prove inverse-chart
   transversality. Verify properness and multiplicity/length identification,
   then subtract and prove the all-clock corollary.
5. **The exact trace threshold and fixed-time slices.** Define the compact
   cohomological trace using proper pullback and the actual Frobenius morphism.
   Derive its value from classical affine-space cohomology with a short
   specialization argument. Prove threshold and defect, slice rationality or
   transcendence, and the finite-dimensional trace obstruction in full.
6. **Diagonal iteration and the resonant boundary.** Prove the single-map
   iterate identity, point counts and rational Artin–Mazur zeta. Compare with
   its cohomological determinant. Prove the nonlinear characteristic-three
   counterexample and identify the failed unit argument at equality.
7. **Scope and reproducibility.** State which arithmetic/periodic/resonant
   questions are outside scope; explain the already-saved exact evidence.
   Include truthful data, ethics, author-contribution, funding/conflict and
   AI-assistance disclosures without inventing human authors or attestations.

## Figure and citation plan

No figure is needed: the relevant geometry and clock relations are short
exact formulas, and no new visual/experimental claim is authorized.

The manuscript uses a standard `article` class and numeric mathematical
citations via `amsplain`. Bibliography contains only cited entries.

- Shuddhodan (2019), DOI `10.1112/S0010437X19007188`; exact content locators
  refer explicitly to arXiv:1803.06461v2, Lemma 2.6, Proposition 2.10,
  Definition 2.12/Lemma 2.14, Example 3.6 and the paragraph immediately after
  it. No unverified “Remark 3.7” label.
- Varshavsky (2007), DOI `10.1007/s00039-007-0596-9`; author v2 §2.2 and
  Theorem 2.3.2 for high-Frobenius contraction and trace context.
- Fujiwara (1997), DOI `10.1007/s002220050129`; original ownership is
  explicitly attributed through the inspected Shuddhodan and Varshavsky
  accounts, not through a falsely claimed full-text read.
- The Stacks Project, tags `0FEZ` and `0B01`, especially Lemma 43.16.1,
  for the classical intersection framework and local length interpretation.
- Milne, *Lectures on Étale Cohomology*, v2.21 (2013), Example 16.3,
  §22 and Theorem 24.1, for affine-space cohomology and duality. Exact
  bibliography is supplied in the author PDF; cite theorem/section locators.
- Dwork (1960), DOI `10.2307/2372974`, for the classical fixed-variety
  rationality setting, not as an input to the equalizer proof. Publisher DOI
  metadata is retrieved; original proof is not claimed inspected.

Detailed access and metadata notes will be in `paper/SOURCE_VERIFICATION.md`.
No human-read marks, venue-fit certificate or external-review claim is made.

## Review findings adopted and writing boundaries

The frozen independent proof review has no blocking mathematical finding.
A-M1 is adopted by saying **finite morphism degree** for `Q^2`, explicitly
distinguishing it from geometric fiber cardinality. A-M2 is adopted through
the exact threshold-paragraph locator above. Neither changes a theorem.

`paper-plan`, `paper-write`, `paper-compile`, proof-writer and the applicable
ARS writing/source discipline are used within the assigned mathematical
drafting scope. The user-authorized current-team model, absence of page/ML
quotas, existing frozen plan and explicit direct drafting assignment override
older model/API examples and redundant planning checkpoints. This is not an
ARS full-pipeline run or a simulated multi-panel review. No new scientific
claim, target Euler factor, root number, automorphy, target zero correspondence,
or Hilbert–Pólya realization is authorized.

## Handoff gate

Write modular TeX and verified BibTeX; actually compile in a fresh `mktemp`
directory; inspect logs, text and fonts; save the initial PDF and genuine
receipt. Then freeze all TeX/BibTeX and report every local build-input hash.
The coordinator owns independent manuscript review, final two-empty-directory
builds, all-page final QA, formal evaluation, release metadata and Git.
