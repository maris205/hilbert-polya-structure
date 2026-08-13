# Independent Manuscript Review — Round 1

**Manuscript:** *Rational Periodic Multiplier Moduli under Good Reduction: A Hénon Certificate and Exact Audit*  
**Review date:** 2026-08-14  
**Review mode:** independent mathematical-domain, methodology, evidence-integrity, and devil's-advocate review  
**Reviewed snapshot:** `paper/manuscript.tex` SHA-256
`ea6ed18de3a35b02e34882ff4e647f4e4eeec0fe33e8e285511d40d44c6eb10d`; `paper/paper_pre_review.pdf`
SHA-256 `450eae555f09faf7071efbd476f34c570b288166a067d81ddbeac9e6c225010f`

## Verdict

`PASS_WITH_MINORS`

**Overall score:** **8.5/10** as a narrowly positioned arithmetic-dynamics
certificate note.  There are **no major or critical defects**.  The all-period
theorem is correct under the stated hypotheses, the frozen specialization is
valid, and the manuscript consistently distinguishes that proof from the
finite $n\leq 3$ software audit.  Three minor repairs should be made before the
final integrity pass: expose two standard but currently compressed ring/place
implications in the main-text proof, correct two bibliography-ledger metadata
inconsistencies, and remove one control character from the integrity report.

The mathematical novelty is modest rather than deep: the ingredients are
standard good-reduction and algebraic-unit arguments.  The manuscript already
states this limitation and markets the result as a transparent certificate,
not as multiplier rigidity.  That positioning is honest and adequate for the
intended note; a venue requiring a major new theorem would instead call for
merging this result into a broader obstruction paper.

## Scores

| Dimension | Score | Assessment |
|---|---:|---|
| Mathematical correctness | 9.3/10 | The projective finiteness, non-Archimedean maximum, unit-monodromy, and conjugation-stable support arguments close correctly. |
| Claim/evidence alignment | 9.6/10 | All-period claims come from proof; the $n\leq3$ ledger is repeatedly and correctly labeled an implementation audit. |
| Exact-computation rigor | 9.4/10 | Exact-period separation, reciprocal polynomials, rational-root checks, exact modulus classification, and controls agree with the frozen JSON. |
| Reproducibility/integrity | 9.5/10 | The result manifest, tests, deterministic build, citation-key closure, and figure provenance all revalidated. |
| Scope discipline | 9.7/10 | The manuscript expressly excludes approximate/irrational moduli, universal symplectic claims, target-zero claims, and finite-to-infinite extrapolation. |
| Exposition | 8.6/10 | Clear and unusually careful; two standard algebraic implications should be stated explicitly in the manuscript rather than left to the proof package. |
| Standalone novelty/significance | 5.0/10 | Useful packaging and a clean frozen certificate, but the proof mechanism is elementary and plausibly folklore-level. |

## Mathematical audit

### 1. Algebraicity of every finite periodic orbit — PASS

For a period-$n$ point of a composition of $m$ Hénon factors, the manuscript
correctly expands the orbit into a cyclic sequence of $N=mn$ first
coordinates satisfying

$$
p_{i_j}(z_j)-z_{j+1}-z_{j-1}=0.
$$

After homogenizing each equation to its own degree, setting the common
homogenizing coordinate to zero leaves $Z_j^{d_{i_j}}=0$ for every $j$.
Thus there is no projective point at infinity.  A positive-dimensional
projective component cannot be disjoint from a hyperplane; equivalently, a
projective variety contained in the affine chart would be both proper and
affine and hence zero-dimensional.  The cyclic solution scheme therefore has
finite support, and its coordinates are algebraic over $K$.  This correctly
establishes algebraicity before any valuation argument.

### 2. Cyclic non-Archimedean maximum — PASS

At a finite place outside $S$, monicity and integral coefficients give

$$
|p_{i_j}(z_j)|_w=|z_j|_w^{d_{i_j}}
$$

whenever $|z_j|_w>1$.  Choosing a coordinate with maximal absolute value
$M>1$ yields $M^{d_{i_j}}>M$, while the recurrence bounds the same quantity
by $M$.  This contradiction is valid for all degrees $d_{i_j}\geq2$ and all
factor compositions in the stated class.  Together with algebraicity and the
valuation criterion, it proves $S$-integrality of every periodic coordinate.

### 3. Integral $\mathrm{SL}_2$ monodromy and algebraic units — PASS

At an $S$-integral orbit, every $p_i'(z_j)$ is $S$-integral and each derivative
factor has determinant one.  Hence the return monodromy lies in
$\mathrm{SL}_2(\overline R)$ and has characteristic polynomial

$$
T^2-\operatorname{tr}(M_P)T+1.
$$

Both roots are integral, and determinant one identifies the second root with
$\lambda^{-1}$; therefore $\lambda$ and $\lambda^{-1}$ are in the integral
closure and $\lambda$ is a unit.  The logic is correct.  Minor M1 below asks
only that the main text state the transitivity-of-integrality step explicitly.

### 4. Rational modulus and conjugation-stable support — PASS

The repaired Galois-closure argument is correct.  Taking a finite Galois
$M/\mathbb Q$ containing all relevant algebraic numbers and taking **all**
places above the rational bad-prime set $S_{\mathbb Q}$ makes the place set
stable under $\operatorname{Gal}(M/\mathbb Q)$.  Therefore both $\lambda$ and
its chosen complex conjugate $\bar\lambda$ are $T$-units.  If
$|\lambda|=q\in\mathbb Q_{>0}$, then

$$
q^2=\lambda\bar\lambda
$$

is a rational $T$-unit, so $v_\ell(q)=0$ for every
$\ell\notin S_{\mathbb Q}$.  This proves the claimed rational-prime support.
The manuscript correctly does **not** identify $\bar\lambda$ with
$\lambda^{-1}$; conjugation and reciprocal pairing are used for different
purposes.

### 5. Frozen specialization — PASS

$P(U)=U^3-2U^2+2U-2$ is monic, so the chosen root $u$ is an algebraic integer.
Moreover $P'(U)=3U^2-4U+2$ has discriminant $-8$, so the real root is unique.
For $H_u(X,Y)=(X^2-u-Y,X)$ the finite bad set is empty and determinant is one.
The general theorem therefore gives

$$
|\lambda|\in\mathbb Q_{>0}\Longrightarrow |\lambda|=1
$$

at every period.  Exclusion of exact rational-prime modulus follows without
assuming $\lambda\in\mathbb Q$.

### 6. Sharp and boundary controls — PASS

For $a=-15/16$ and $r=5/4$, the identity $a=r^2-2r$ makes $(r,r)$ fixed, and

$$
L^2-\frac52L+1=(L-2)(L-1/2).
$$

Thus the predeclared bad prime $2$ is exactly realized.  The
$J_{a,\delta}$ control has determinant $\delta$; at $(a,\delta)=(0,2)$ its
polynomial $L^2+2$ has nonunit roots, correctly showing why determinant data
must be tracked.  The cat-map control correctly demonstrates that irrational
algebraic-unit instability is outside the rational-support conclusion.

## Computation and evidence audit

The manuscript's finite claims match the frozen artifacts:

- exact point/cycle counts are $(2,2)$, $(2,1)$, and $(6,2)$ for periods
  $1,2,3$, giving ten exact points on five cycles;
- the three trace and multiplier eliminants in Table 2 match
  `results/candidate_multiplier_audit.json` and
  `results/exact_period_ledger.json`;
- the rational-root theorem is applied only after norming to $\mathbb Q$, and
  exact substitution rejects $L=\pm1$ through the cutoff;
- the exact modulus engine distinguishes rational $M$ from rational
  $q=\sqrt M$ and does not promote display approximations;
- in the selected real embedding, one elliptic fixed cycle has exact modulus
  $1$, while the other four cycles have irrational algebraic-unit moduli;
- all 15 registered runs pass, with controls executed before candidate
  periods, and the formal route classification is A0 failure by theorem.

The evidence hierarchy is stated correctly in the abstract, Sections 5--7,
and Appendix A.  Nothing in the manuscript uses the finite ledger to infer an
all-period result.

## Reproducibility checks performed during this review

- `PYTHONPATH=code pytest -q` — **39 passed**.
- `paper/build.sh` — clean 11-page letter-size PDF; no LaTeX warning, undefined
  citation/reference, overfull box, or underfull box found in the final log.
- The rebuilt `paper/manuscript.pdf` remained byte-identical to the pre-review
  snapshot at SHA-256
  `450eae555f09faf7071efbd476f34c570b288166a067d81ddbeac9e6c225010f`.
- `results/final_result_manifest.json` — **41/41** declared paths, byte sizes,
  and SHA-256 hashes match.
- Citation-key closure — **12/12**, with zero missing and zero unused BibTeX
  keys.
- `paper/FIGURE_PACKAGE.json` — all frozen-input, generator, and nine figure
  output hashes match.
- All 11 rendered PDF pages were visually inspected; equations, tables,
  figures, captions, links, and page boundaries are legible.
- Review activity accessed bibliographic metadata only.  No prime table,
  Riemann-zero data, or other forbidden target data was accessed.

## Strengths

1. **The theorem/experiment boundary is exemplary.**  The abstract explicitly
   says that the finite ledger audits software rather than proving the
   all-period result, and this distinction survives through the conclusion and
   appendices.  **Evidence anchor:** `text: manuscript abstract and lines
   399--453, 605--609`.
2. **The conjugation subtlety is handled correctly.**  Passing to all places
   above $S_{\mathbb Q}$ repairs the non-Galois $(K,S)$ problem, and the text
   explicitly separates complex conjugation from reciprocal eigenvalues.
   **Evidence anchor:** `equation: manuscript Lemma 3.5 and equation (6)`.
3. **The controls test real theorem boundaries.**  The denominator-$2$ control
   is a sharp positive support example, while the nonunit determinant and cat
   map prevent overgeneralization.  **Evidence anchor:** `equation:
   manuscript equation (9) and Section 5.2`.
4. **The negative outcome is reported without inflation.**  Geometry passes,
   A0 fails by theorem, and downstream prime/zero/zeta stages remain closed.
   **Evidence anchor:** `text: manuscript Section 6 and
   results/negative_result_ledger.json`.
5. **Novelty is positioned honestly.**  The manuscript calls the proof
   elementary and compares it with deeper height and multiplier-rigidity work
   without claiming priority.  **Evidence anchor:** `text: manuscript Sections
   2 and 7; notes/NOVELTY_AUDIT.md`.

## Required minor revisions

### M1. Make two compressed algebraic implications explicit in the manuscript

**Severity:** Minor  
**Confidence:** 5/5 — direct algebraic-number-theory proof audit  
**Evidence anchor:** `text: manuscript lines 297--308 and 317--332`

The conclusions in Lemmas 3.4 and 3.5 are correct, and the fuller proof
package states the missing details.  The paper itself, however, jumps from a
characteristic polynomial in $\overline R[T]$ to “both eigenvalues are
integral over $R$,” and then from the $\overline R$-unit statement to
$\lambda\in\mathcal O_{M,T}^{\times}$.  A specialist can reconstruct both
steps, but two sentences would make the main-text proof fully standalone.

**Executable repair:** after the characteristic polynomial in Lemma 3.4, add
that each root is integral over $\overline R$, that $\overline R$ is integral
over $R$, and hence transitivity makes each root integral over $R$.  In Lemma
3.5, add that a place of $M$ outside $T$ lies over a rational prime outside
$S_{\mathbb Q}$, so its restriction to $K$ lies outside $S$; applying the
integrality statement to both $\lambda$ and $\lambda^{-1}$ gives valuation
zero there.

### M2. Reconcile the two bibliographic metadata inconsistencies

**Severity:** Minor  
**Confidence:** 5/5 — checked against DOI/publisher records  
**Evidence anchor:** `text: paper/references.bib lines 12--20;
notes/NOVELTY_AUDIT.md prior-work entries 2 and 5`

The Silverman entry is rendered as *Mathematische Zeitschrift* **215(1)**,
237--250, while the correct issue is **215(2)** (DOI
[10.1007/BF02571713](https://doi.org/10.1007/BF02571713)); the novelty audit
already has 215(2).  Conversely, the Kawaguchi novelty-audit entry ends at
page **1251**, while the publisher PDF and the BibTeX/citation ledger give
**1225--1252**.

**Executable repair:** change `number = {1}` to `number = {2}` for
`silverman_1994`; make the citation-verification ledger include the same issue
number; change the Kawaguchi page range in `notes/NOVELTY_AUDIT.md` to
`1225--1252`; then rebuild the PDF and refresh every retrospective paper hash
that depends on `references.bib`, the PDF, or the citation ledger.  The source
lock and official result JSON must remain unchanged.

### M3. Remove a stray control character from the integrity report

**Severity:** Minor  
**Confidence:** 5/5 — byte-level scan  
**Evidence anchor:** `text: paper/INTEGRITY_PRE_REVIEW.md line 28`

The phrase intended to display $\bar\lambda$ contains byte `0x08` before
`ar\lambda`.  It does not affect the manuscript PDF or theorem, but it makes
the integrity artifact non-clean text.

**Executable repair:** replace the corrupted token with literal Markdown math
`$\bar\lambda$`, rerun a control-character scan over text artifacts, and
refresh any retrospective integrity hash that is meant to cover this report.

## Major or critical issues

None.

## Devil's-advocate stress test

The strongest objection is not correctness but contribution size: a skeptical
reader can compress the theorem to “good reduction makes periodic points
integral; determinant-one integral monodromy has unit eigenvalues; conjugation
then restricts a rational modulus.”  That objection is valid as a novelty
assessment, but it does not invalidate the result.  The manuscript already
absorbs it by using “certificate” language, explicitly conceding the
elementary mechanism, supplying a source-locked nonlinear case and a sharp
support control, and making no historical-first claim.  No stronger
counterexample survives the stated hypotheses: the $a=-15/16$ example lies
at the declared bad prime, the $\delta=2$ example violates determinant one,
and the cat map has irrational rather than rational modulus.

## Final recommendation

Implement M1--M3, rebuild deterministically, update only the affected
retrospective paper/integrity indexes, and perform a short Round 2 verification
against this exact manuscript snapshot.  No new experiment, higher-period
search, theorem weakening, or route reopening is required.
