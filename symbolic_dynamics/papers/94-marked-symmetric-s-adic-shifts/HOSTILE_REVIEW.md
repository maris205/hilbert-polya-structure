# Internal hostile review — P94

Audit date: 2026-08-28 UTC  
Disposition: **internal GO after repair / external HOLD**

The authoring stage was followed by two internal audit passes. Round 1 was a
line-by-line closure review by the primary agent of the already repaired
package. No standalone verbatim Round-1 report was retained, so the Round-1
section below is a closure ledger reconstructed from the recorded handoff and
the resolved manuscript; it is not presented as a quotation or as an
independent referee report. Round 2 was a separate, strictly read-only hostile
review by the stochastic scout, followed by a bounded integrating pass that
adopted one wording clarification and created this record. None of these
passes is external peer review.

## Authoring-stage repairs entering Round 1

Two bare `quad` TeX tokens had already been repaired before the retained
Round-1 state. More importantly, the contribution boundary had been rewritten
to subtract the direct prior mechanisms:

1. general recognizability for sequences of morphisms;
2. general tower and inverse-limit descriptions of invariant measures;
3. the Ferenczi--Fisher--Talet symmetric-adic reciprocal-sum criterion; and
4. the Arbulú--Durand--Espinoza constant-length criterion and nearby
   reciprocal-sum/two-measure examples.

The manuscript therefore does not claim that the summability transition,
incidence-cone mechanism, or general measure-transfer framework is new. Its
residual theorem record is confined to the frozen marked morphisms, their
elementary word-level recognizability, the explicit physical bias/frequency
interval, and the two closed product specializations.

## Round 1 — primary-agent closure ledger

The primary agent rederived the corrected theorem chain rather than relying
only on the incidence matrices.

- The words `0^(a+1)1` and `01^(a+1)` contain no internal `10`; every image
  boundary contributes exactly one `10`. The marker residue fixes the
  constant-length phase, and the two distinct cut blocks fix the preimage
  letters.
- Positivity places every lower-level supertile type in both next-level
  types. This gives uniform recurrence. A period would have to preserve every
  unique cut residue and hence be divisible by all supertile heights, proving
  aperiodicity.
- The marked bases give two clopen towers. Their normalized weights satisfy
  the displayed compatibility equation in the recorded direction.
- Compatible weights construct cylinder frequencies; boundary errors tend to
  zero. Conversely, tower decomposition recovers all cylinder values and
  then the marked base weights, giving the affine bijection.
- Diagonalizing the normalized incidence matrices gives the bias contraction
  `rho_n=a_n/(a_n+2)`, the inverse-limit interval `[-R,R]`, and the physical
  zero-frequency interval of radius `R/2`.
- The infinite-product test and both specializations `a_n=n` and `a_n=n^2`
  were recomputed with the stated constants.

At that checkpoint the registered control passed **90,509 assertions**, and
the four-stage LaTeX build completed successfully. Round 1 found no remaining
theorem defect in the repaired state.

## Round 2 — independent reattack

The second reviewer independently attacked all points named in the review
contract: marker existence, centered desubstitution, minimality,
aperiodicity, clopen towers, measure surjectivity and injectivity, the bias
inverse limit including the `R=0` tail, the summability criterion, both closed
constants, the owner boundary, and the evidence/build claims.

No mathematical correction was required. One nonblocking presentation issue
was found in the abstract: after distinguishing the bias radius from the
symbol-frequency radius, the phrase "finite radius" was momentarily
ambiguous. The integrating pass replaced it with the precise phrase
"finite-prefix bias radius" and displayed

```text
R_N = 2/((N+1)(N+2)).
```

This is a notation clarification only; it does not change the theorem.

## Round 2 derivation ledger

- **Existence and uniqueness of desubstitution.** Centered windows in higher
  supertiles give two-sided preimage windows whose lengths tend to infinity.
  After fixing the phase modulo `a_m+2`, compactness gives a tail-language
  preimage. The complete `10` marker class fixes the phase, and the two image
  words decode uniquely.
- **Clopen nested towers.** For each fixed level, iterated marker decoding
  uses a finite window. The cut phase and type are therefore locally
  constant, so the bases are clopen; unique cutting makes their floors a
  partition, and composition gives refinement.
- **Minimality and aperiodicity.** Every level-`(n+1)` supertile contains the
  chosen level-`n` supertile, so allowed words have gaps at most twice the
  next height. If `T^p x=x`, unique level-`n` cuts imply `h_n` divides `p` for
  all `n`, impossible because `h_n >= 3^(n-1)`.
- **Measure construction.** Internal occurrences in a level-`(n+1)`
  supertile contribute exactly `Gamma_n(u)` by compatibility. The remaining
  boundary contribution is at most
  `(a_n+1)(|u|-1)/h_(n+1) <= (|u|-1)/h_n`. The geometric growth of `h_n`
  gives convergence, and endpoint errors of at most `1/h_n` give both
  cylinder-consistency identities and invariance.
- **Injectivity and surjectivity.** Decomposing a cylinder over the two towers
  leaves boundary-floor mass at most `(|u|-1)/h_n`, so tower weights determine
  the measure. Counting marked level-`n` bases inside higher supertiles gives
  the prescribed compatible weights; high-supertile endpoints have vanishing
  density.
- **Bias interval.** With `b_n=p_0^(n)-p_1^(n)`, compatibility is
  `b_n=rho_n b_(n+1)`. If `R>0`, every `t` in `[-R,R]` has the unique lift
  `b_n=t/R_(n-1)`. If `R=0`, every fixed tail product is
  `lim_N R_N/R_(n-1)=0`, forcing every `b_n` to vanish.
- **Summability and constants.** For `y_n=2/(a_n+2)`, the inequalities
  `y_n <= -log(1-y_n) <= 3y_n`, together with comparison of
  `1/(a_n+2)` and `1/a_n`, give the exact transition. Telescoping gives
  `R_N=2/((N+1)(N+2))` for `a_n=n`; Euler's sinh product gives
  `pi*sqrt(2)/sinh(pi*sqrt(2))` for `a_n=n^2`. The conversion from bias to
  physical frequency contributes the stated factor `1/2`.

## Final control and build replay

After the wording repair, the registered script again reported:

```text
marked symmetric S-adic exact control: PASS
assertions=90509
literal_marker_words=2286
cyclic_phase_words=2286
incidence_bias_cases=28050
inverse_limit_cases=170
```

The production replay

```text
pdflatex -> bibtex -> pdflatex -> pdflatex
```

completed with **7 pages** and **352,417 bytes**. The final log has no
undefined citation or reference, no overfull or underfull box, and no rerun
warning. All PDF fonts are embedded subsets with Unicode maps.

## Literature boundary and residual risk

Ferenczi--Fisher--Talet (2009), DOI
`10.1007/s11854-009-0027-y`, directly owns the symmetric-adic criterion.
Arbulú--Durand--Espinoza (2024), DOI `10.3934/dcds.2024052`, supplies a general
constant-length unique-ergodicity criterion, explicitly records the FFT
symmetric-matrix result, and includes nearby two-letter reciprocal-sum and
two-measure behavior. The manuscript positively cites and subtracts both.

- **Mathematics:** low risk after two derivations, literal marker checks,
  exact matrix/inverse-limit arithmetic, and the final build replay.
- **Scope:** low risk inside the frozen marked family because the general
  mechanisms and direct criterion owners are expressly excluded.
- **Literature/priority:** medium risk. A bounded search did not locate the
  exact combined marked package, but search absence is not a novelty proof.
- **Verdict:** **GO** for internal Stage 2 theorem use; **HOLD** for public
  posting, submission, author contact, specialist-clearance language, or any
  priority claim.
