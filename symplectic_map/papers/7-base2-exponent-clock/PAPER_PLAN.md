# Paper Plan

Planning date: 2026-08-14.  This is an outline, not a manuscript or a result
report.  It is bound to source-lock v2,
`205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1`.
The outline has been reconciled after the one authorized registered run and
the independent result-integrity audit.  Its finite-result cells are bound to
`results/EXPERIMENT_RESULTS.json` SHA-256
`847564ffb9e69aee2018dfa179490fafa81b733ad58231dab9202b82623f3ce6`
and manifest SHA-256
`6d9407408437954f52b4a1cb7f0caa50ca00bd22be9cf9a348a1bbb60c9a87e8`.

## Paper identity

- **Safe title:** *Exact 2-Adic Valuation of Higher-Period Multipliers for a
  Frozen PCF Quadratic*.
- **Article type:** a short, theorem-led arithmetic-dynamics note with a
  source-locked exact audit as a bounded implementation-falsification
  appendix.  It is not a prime-orbit, spectral, or
  computational-discovery paper.
- **Target readership:** arithmetic and non-Archimedean dynamics researchers,
  with enough local-field detail for a complex dynamicist to verify the proof.
- **Venue posture:** arithmetic-dynamics/dynamical-systems journal, venue not
  yet locked.  Plan for roughly 10--12 main-text pages plus proof/audit
  appendices; do not force a conference template before venue selection.

### One-sentence contribution

For the frozen type-\((3,1)\) PCF quadratic
\(g(z)=z^2-u\), \(u^3-2u^2+2u-2=0\), every exact
period-\(n\ge2\) multiplier lies exactly on the 2-adic boundary
\(w(\Lambda)=n w(2)\), while a Frobenius--Hensel norm description and a
two-coefficient residue obstruction isolate, but do not resolve, the remaining
rational equality \(\Lambda=\pm2^n\) for \(n\ge4\).

### Required nonclaim sentence

The paper does **not** exclude \(\Lambda=\pm2^n\) in all periods, does not
decide \(|\Lambda|=2^n\) without rationality, and makes no claim about prime
orbits, zeta zeros, quantization, or a general rigidity theorem for PCF
quadratics.

## Narrative spine

**What.**  The inherited global derivative-content theorem says only that a
rational period-\(n\) multiplier is in \(2^n\mathbb Z\).  At the frozen
parameter, local dynamics at the unique place over two sharpens this to
\(2^n\) times an odd integer.

**Why.**  The exact target left open by the preceding project paper is not
ordinary divisibility but equality at the boundary: \(\Lambda=\pm2^n\).
Conflating that arithmetic predicate with complex modulus or characteristic
exponent would invalidate the question.

**So what.**  A standard contraction argument settles the valuation in every
period, and the local Hensel model then explains the unresolved residue as a
norm-one problem over Frobenius orbits.  The mod-2 expansion proves equality
impossible at periods two and three and simultaneously exhibits why this
first obstruction cannot settle period four or higher.

The introduction should state all three paragraphs, the main theorem, and the
open equality boundary before discussing computations or project genealogy.

## Claims--evidence matrix

| ID | Claim allowed in the paper | Evidence and proof location | Status/gate |
|---|---|---|---|
| C1 | Over a complete non-Archimedean field of characteristic zero and residue characteristic two, if \(f(z)=z^2+c\) and \(0<|c|<1\), every exact \(n\ge2\) cycle consists of units and has multiplier norm \(|2|^n\). | Escape for \(|z|>1\); invariance and strict contraction in the open unit disk; chain rule.  Give the complete proof in Section 3. | `PROVED`; label the technique standard and claim no priority. |
| C2 | For the frozen cubic and every cycle-field place \(w\mid2\), \(w(\Lambda_C)=n w(2)\). | The cubic is 2-Eisenstein, so the completion is a totally ramified cubic with \(u\) a uniformizer; apply C1.  Section 4. | `PROVED`; this is the core frozen corollary. |
| C3 | If \(\Lambda_C\in\mathbb Q\), then \(\Lambda_C=2^n m\) with \(m\) odd. | A periodic point is integral over \(\mathcal O_K\); hence \(B_C=\Lambda_C/2^n\) is an algebraic integer.  Rationality makes \(B_C\in\mathbb Z\), and C2 makes it a 2-adic unit.  Section 4. | `PROVED`; restate this two-line integrality argument so the note is self-contained. |
| C4 | Exact local cycles are unique Hensel lifts of Frobenius cycles, and \(B_C\) is their unramified norm. | \(g^n(X)-X\equiv X^{2^n}-X\pmod u\), simple roots, Hensel uniqueness, and \(\sigma(z_\alpha)=g(z_\alpha)\).  Section 5. | `PROVED`; distinguish exact Frobenius degree from formal period. |
| C5 | \(B_C=\pm1\) forces two residue coefficients to vanish; this excludes exact periods two and three, but the filter is insufficient starting at period four. | Expansion \(z_\alpha\equiv\alpha+u+u^2\pmod2\); norm expansion; degree-2/3 irreducibles; degree-4 reciprocal witness pair.  Section 6. | `PROVED`; the degree-4 witness passes only the necessary filter and is not an equality cycle. |
| C6 | A rational base-2 equality appearing after repeating an orbit already has primitive \(B_C=\pm1\). | \(B_C\in K_u\) and the only roots of unity in this totally ramified odd-degree local field are \(\pm1\).  Section 6 or Appendix A. | `PROVED`; do not relabel a repeated return as exact period \(nr\). |
| C7 | The cycle-polynomial identity and its values at the frozen postcritical points are necessary equality conditions. | \(P_C(g(X))=(-1)^nP_C(X)P_C(-X)\), followed by substitutions at \(0,\pm u,a\).  Section 6. | `PROVED`; do not infer \(P_C\in K[X]\) for a single cycle. |
| C8 | The registered finite ledger excludes \(B_C=\pm1\) in the frozen exact-set records for periods 2--7 and exercises the implementation with sign, target, and formal-period controls. | `results/EXPERIMENT_RESULTS.json`: exact degrees \(2,6,12,30,54,126\), cycle counts \(1,2,3,6,9,18\), twelve zero-degree target gcds, twelve agreeing nonzero resultant norms; V4 deployment review, 38-test JUnit, strict manifest, and independent result-integrity audit.  Section 7 and Appendix B. | `SUPPORTED AS DEVELOPMENT-SEEN REPRODUCTION ONLY`; no blind, prospective, confirmatory, or all-period language. |
| C9 | \(B_C\ne\pm1\) for every \(n\ge4\). | No proof or registered finite computation can establish this. | `OPEN`; never state as a result or implication. |
| C10 | \(\chi_C=\log2\), or merely \(|\Lambda_C|=2^n\), is excluded. | The local theorem is 2-adic, not an Archimedean modulus theorem. | `OUTSIDE`; preserve the rational/modulus/exponent separation. |

## Planned abstract logic

Use a five-sentence abstract, written only after the theorem sections are
stable:

1. State the exact arithmetic question and the frozen PCF map.
2. State C1 and the frozen valuation corollary C2--C3.
3. State the Frobenius--Hensel norm model C4.
4. State the two-coefficient obstruction, its exact \(n=2,3\) consequence,
   and its degree-four insufficiency.
5. End with the explicit all-period open boundary; mention the passed finite
   ledger only as a development-seen implementation-falsification record.

No prime-distribution or zeta motivation belongs in the abstract.

## Section-by-section outline

### 1. Introduction: the boundary left by divisibility (1.25--1.5 pages)

- Define \(\Lambda_C=2^nB_C\) and state the arithmetic equality
  \(B_C=\pm1\).
- Present the main frozen corollary and the unresolved equality in the first
  page.
- Give the contribution list as C2--C5, not as a claim of novelty for C1.
- State the rational/modulus/characteristic-exponent separations verbatim.
- Preview Figure 1.

### 2. Frozen object, genealogy, and nearby results (1.25--1.5 pages)

- Verify the type-\((3,1)\) critical orbit
  \(0\mapsto-u\mapsto a\mapsto-a\mapsto-a\).
- Explain that the parameter is inherited unchanged from Batch-01 Paper 2;
  no parameter search or prime/zero data enter this note.
- Cite standard arithmetic-dynamics definitions and exact/formal period
  distinctions \cite{silverman2007arithmetic,morton1994rational}.
- Position the local theorem against the PCF/non-Archimedean literature
  \cite{benedettoetal2014attracting,hutz2009good,riveraletelier2026critical}.
- Keep current good-reduction work as context only
  \cite{rajagopalzhang2025uniform}; it is not a premise of the proof.

### 3. A local sharp-boundary lemma (1--1.25 pages)

- State C1 at the correct level of generality.
- Give the three-step proof: escape, strict contraction, chain rule.
- Add a remark that the power map shows sharpness of the numerical boundary.
- Add Rivera--Letelier's strict-threshold theorem as an independent
  contemporary comparison, not as the primary proof or historical input.

### 4. The frozen 2-adic valuation theorem (1.25--1.5 pages)

- Prove 2-Eisenstein irreducibility, uniqueness of the place over two, and
  \(2=u^3/(u^2-u+1)\).
- Apply C1 at every extension place to prove C2.
- Give the self-contained integrality step proving C3.
- State explicitly that odd normalized quotient does not imply
  \(B_C\ne\pm1\).

### 5. Frobenius cycles and the norm coordinate (1.5--2 pages)

- Construct the unramified degree-\(n\) extension and Hensel lifts.
- Prove exact dynamical period equals exact Frobenius degree.
- Prove \(\sigma(z_\alpha)=g(z_\alpha)\) by uniqueness.
- Identify \(B_C=N_{K_{u,n}/K_u}(z_\alpha)\).
- Use Figure 3 to keep the field, residue, norm, and coefficient-gate levels
  distinct.

### 6. What equality would force (1.75--2 pages)

- Derive \(z_\alpha\equiv\alpha+u+u^2\pmod2\).
- Compute the two norm coefficients and prove the \(n=2,3\) exclusion.
- Present the degree-four reciprocal witness as failure of sufficiency, not as
  an equality hit.
- State the cycle-polynomial identity and special-value conditions.
- Close the repetition loophole carefully through local roots of unity.
- End the section with a boxed `OPEN FOR n >= 4` statement.

### 7. Registered finite exact audit (1--1.25 pages)

- Report the completed V4-reviewed registered run: exact-period set degrees
  and cycle counts, all twelve zero-degree gcds, all twelve agreeing nonzero
  target-resultant norms, controls, and machine-readable hashes.
- Label periods 2--7 as development-seen reproduction/implementation
  falsification.  Do not call them blind, prospective, or theorem evidence.
- Use Figure 2 for the compact ledger.  Put exact polynomials and large norm
  factorizations in Appendix B rather than consuming main-text space.
- State that the registered candidate used exact symbolic arithmetic, no
  numerical candidate runs, and no post-null extension.

### 8. Discussion and open boundary (0.75--1 page)

- Explain why the mod-2 filter stops at degree four.
- Separate rational equality, Archimedean modulus, and characteristic
  exponent one final time.
- List plausible next steps as questions: higher \(u\)-adic coefficients,
  norm-one unit structure, and Galois constraints on single-cycle
  polynomials.
- Do not suggest that a finite null ledger proves the all-period statement.

### Appendices

- **Appendix A:** detailed local-field and root-of-unity lemmas if referees
  need them.
- **Appendix B:** exact-period construction, formal-period pollution control,
  and registered certificate tables.
- **Appendix C:** provenance table linking every displayed finite datum to a
  JSON record and hash.

## Related-work comparison table planned for Section 2

| Literature axis | Closest references | What they supply | What this note still has to prove itself |
|---|---|---|---|
| Non-Archimedean attracting cycles and PCF maps | \cite{benedettoetal2014attracting,riveraletelier2026critical} | Critical-point criteria and the sharp strict multiplier threshold. | Equality at the threshold for this frozen map and its exact valuation. |
| Good reduction and periods | \cite{hutz2009good,rajagopalzhang2025uniform} | Relations/bounds for periods under reduction. | The unique Hensel lift, norm identity, and equality filter for this cubic. |
| Dynatomic and multiplier formalisms | \cite{morton1994rational,buffgauthier2015quadratic,murakami2024arithmetic} | Formal-period machinery, parameter-space multiplier loci, and multiplier-polynomial arithmetic. | Exact least-period semantics and the frozen local certificate. |
| Multiplier and exponent spectra | \cite{jixiezhang2026space} | Standard exponent semantics and global span/rigidity context. | One specified rational equality; no consequence is imported from global span. |
| Misiurewicz arithmetic and dynamical units | \cite{benedettogoksel2023part1,benedettogoksel2024part2} | Arithmetic of parameter polynomials and certain associated multipliers. | Arbitrary primitive cycles of the fixed type-\((3,1)\) map. |
| Project genealogy | \cite{wang2026prime} plus the local Batch-01 Paper-2 artifact | Motivation and the frozen candidate; Paper 2 supplies the preceding divisibility boundary. | Every Paper-7 theorem is proved or restated self-contained; no prime/zero data or empirical claim is inherited. |

## Three figures

All three figures are generated reproducibly from frozen JSON/theorem fields;
no candidate number, target decision, or control outcome is hand-entered into
the plotting scripts.  PDF is the manuscript source, SVG is the editable
vector companion, and PNG is a review preview.

### Figure 1 (hero): exact boundary, residual equality, and semantic split

- **Question answered:** What is proved at every period, and what remains
  open?
- **Layout:** a left-to-right theorem chain: local hypotheses
  \(\to\) unit cycle \(\to\) \(w(\Lambda)=nw(2)\) \(\to\) rational
  \(2^n\times\) odd; then a three-way branch to rational
  \(\Lambda=\pm2^n\) (`OPEN_FOR_N_GE_4`), modulus-only (`NOT_DECIDED`), and
  characteristic-exponent equality (`NOT_DECIDED`).
- **JSON contract:**
  `experiments/source_lock.json:{parameter,definitions,frozen_theorem_claims,
  open_claims_and_nonclaims}` plus
  `results/EXPERIMENT_RESULTS.json:{pre_execution_gates.proof_contract,
  all_period_equality_status}`.  The script fails closed unless both candidate
  ids and the frozen source-lock hash agree.
- **Caption obligation:** state residue characteristic two, \(n\ge2\), and
  rationality explicitly; say that the local lemma is standard.

### Figure 2: registered exact-set and two-target ledger

- **Question answered:** What did the sole registered run check, and how large
  were the exact-period sets?
- **Layout:** exact-set degree and exact-cycle count versus \(n=2,\ldots,7\)
  in the upper panel; a two-row target-certificate raster for \(B_n=+1\) and
  \(B_n=-1\) in the lower panel.  Every cell encodes zero gcd degree, nonzero
  field norm, and dual-engine agreement; the full panel is visibly labeled
  `DEVELOPMENT-SEEN REPRODUCTION`.
- **JSON contract:** `results/EXPERIMENT_RESULTS.json:{period_records,
  classification,development_seen_periods,new_blind_periods}`.  Periods,
  degrees, counts, signs, and decisions are all read from the records.
- **Caption obligation:** say that finite absence through period seven does
  not close the all-period claim.

### Figure 3: Frobenius--Hensel norm and the first coefficient obstruction

- **Question answered:** Why does the valuation theorem reduce equality to a
  norm-one condition, why are periods two and three excluded, and why does the
  first residue filter stop at degree four?
- **Layout:** the upper chain follows exact Frobenius degree to unique Hensel
  lift to \(B_C=N(z_\alpha)\), then to the necessary gate
  \(e_{n-1}=e_{n-2}=0\).  The lower matrix reads the degree-2, degree-3, and
  degree-4 irreducible ledgers, marking the first two obstructed and the
  degree-four witness as “filter passes; equality not proved.”  A compact
  footer reports the passed power-map, Chebyshev sign-path, negative-target,
  and formal-period-pollution controls.
- **JSON contract:**
  `results/EXPERIMENT_RESULTS.json:{pre_execution_gates.proof_contract.records.
  frobenius_hensel_norm,pre_execution_gates.controls}` plus source-lock claims
  `T4`--`T5`.  The script fails if the proof contract or controls did not pass.
- **Caption obligation:** identify the degree-four witness as a counterexample
  to sufficiency only, not an equality cycle.

## Citation placement and chronology controls

- Cite Rivera--Letelier in Sections 2--3 as a 2026 independent comparison and
  second proof check.  The elementary contraction proof must appear first and
  remain logically complete without that paper.
- Cite Ji--Xie--Zhang for terminology and global spectrum context only.  Do
  not infer a value-specific statement from their span theorem.
- Cite the two Benedetto--Goksel papers for neighboring Misiurewicz-unit
  arithmetic, with an explicit warning that their associated multipliers are
  not arbitrary primitive cycles here.
- Cite Wang's 2026 article only for external author/project genealogy.  Do not
  treat its latest claims, tables, prime data, or zero-related discussion as
  assumptions, validation, or evidence.
- The internal Batch-01 Paper-2 artifact has no public DOI/arXiv identifier and
  therefore is recorded in the provenance note rather than fabricated as an
  external BibTeX citation.

## Writing and release gates

1. Draft Sections 3--6 from the audited proof package before the introduction.
2. Check every theorem hypothesis against source-lock v2 and preserve exact
   versus formal period throughout.
3. Draft Sections 1--2 only after the claim--evidence matrix is unchanged.
4. Bind Section 7 and Figure 2 to the official result/manifest hashes and
   preserve the development-seen label in prose and caption.
5. Run a dedicated mathematical review of the eventual manuscript; that
   review is deliberately outside this planning task.
6. Before release, revalidate every DOI/arXiv record and either publish the
   Batch-01 predecessor with a stable identifier or retain it solely as a
   transparent local genealogy note.
