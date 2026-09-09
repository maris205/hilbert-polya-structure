# C2 — Fixed-word integral Hénon compositions

2026-09-09 UTC. Disposition: **original boundedness alternative already settled by classical prior work; no new paper-level contract**. No mathematical program or old certificate was run.

## 1. Frozen question and decisive answer

Fix any word length $r\ge1$, any exact factor degrees $d_0,\ldots,d_{r-1}\ge2$, and any ordered Jacobian signs $a_0,\ldots,a_{r-1}\in\{1,-1\}$. Let every coefficient of every $p_i\in\mathbb Z[t]$, $\deg p_i=d_i$, vary without a height restriction. Set

$$
H_i(x,y)=(y,p_i(y)-a_i x),\qquad
W=H_{r-1}\circ\cdots\circ H_0.
$$

The domain is $\mathbb Z^2$ and one full application of $W$ is one native tick. The observable is the least positive $n$ for which $W^n(P)=P$, not an intermediate-factor return and not an unlabelled scalar-word period.

The original question asks whether there is an all-coefficient bound on $n$ for each fixed $r$, or whether some genuinely fixed $r$, degrees and signs admit primitive periods tending to infinity. The answer is stronger than the first alternative:

$$
n\in\mathcal P:=\{1,2,3,4,6,8,9,12,16,18,24\},
$$

uniformly over **all** word lengths, factor degrees, signs and coefficients. This is an immediate application of T. Pezda, *On cycles and orbits of polynomial mappings $\mathbb Z^2\mapsto\mathbb Z^2$*, Acta Mathematica et Informatica Universitatis Ostraviensis 10(1) (2002), 95–102, Theorem 2.1. Its definition on printed p.95 explicitly requires coordinate polynomials with coefficients in the ring, and its theorem on printed p.96 determines the period union for every such planar map. See the [primary journal record](https://dml.cz/handle/10338.dmlcz/120574) and [original article](https://dml.cz/bitstream/handle/10338.dmlcz/120574/ActaOstrav_10-2002-1_10.pdf).

Composition keeps both coordinate polynomials in $\mathbb Z[x,y]$, so $W$ itself meets the theorem's hypotheses. No factor clock is introduced in this deduction. Pezda does not require invertibility, fixed degree, monicity or good reduction. The exact applicability proof is in [PROOF_SUPPLEMENT.md](PROOF_SUPPLEMENT.md), Section 1.

Consequently an unbounded primitive-period family in the stated domain is impossible, even if the return-word length is allowed to grow. This is not a new theorem of this lane, and it cannot be admitted as a new C-series paper. The lack of a sharper composition classification must not be described as a gap in uniform boundedness.

## 2. Source subtraction and actual local reading

| Source actually inspected | Existing result or mechanism | Consequence for C2 |
| --- | --- | --- |
| C428, `papers/C428_integer_period_spectrum/sections/01_theorem_sources.tex`, Sections 2–6, and `SOURCE_AUDIT.md` | Single-factor all-degree spectra: $\{1,2,3,4,6\}$ for sign $+1$ and $\{1,2,3,4,6,8\}$ for sign $-1$. Secant/interpolation reduction and the two finite certificates establish the stronger exclusions. The paper itself expressly subtracts Pezda's uniform boundedness. | Its uniform-bound extension is already owned by the cited classical theorem; its sharper spectrum is not a theorem about arbitrary compositions. The frozen certificate statements and proof structure were read, not re-executed. |
| C425, `papers/C425_fricke_return/sections/01_introduction.tex`, `02_phase_lift.tex`, `04_height_forcing.tex`, `05_line_exhaustion.tex` | Fixed three-factor Fricke return, all ordered integral forcing, phase lift, global-maximum entry, finite-state propagation and periodic-line exhaustion. Bounds depend on forcing, uniformly in the invariant level. | The phase/native-clock discipline transfers. The low-coordinate forcing mechanism is specific to the multiplicative third-order recurrence; it is not a general Hénon-composition bound or a replacement for missing phasewise rigidity. |
| C428 frozen `continuation_round6/arithmetic/SOURCE_AUDIT.md` and targeted IH6 review/source passages | Existing local collision checks already record Pezda and distinguish $\mathbb Z[t]$ from integer-valued rational polynomials. | No claim that this lane discovered a new boundedness mechanism. |
| Targeted repository search for Hénon compositions, integer periods, fixed words and Pezda | Relevant hits include C428, C417 source ownership, C425 and unrelated analytic/spectral composition mechanisms. | No exact all-word sharp-spectrum theorem was identified in the inspected hits. Search absence is not a worldwide novelty result. |

All local paths in this table are relative to `henon_dynamics/research_c424_c428/` unless an earlier C417 source is explicitly mentioned. Earlier packages were read-only. The C428 main result is accepted as the sealed prior result, not reopened as a new proof task.

## 3. Honest surviving sharper question and transfer gap

A **different, stronger** question would ask for the exact period union of compositions at fixed word length and ordered signs/degrees, or whether the C428 sign-dependent exclusions survive after replacing the single sign by $\det DW=\prod_i a_i$. This lane has not proved or refuted that statement and does not silently substitute it for the original boundedness question. Pezda only reduces the extra exclusions to a finite list of possible lengths; it does not supply the required realizability or Hénon-specific exclusions.

The single-factor secant argument has a precise phase-dependent generalization. If $E_i$ is the input-coordinate support at phase $i$, with diameter $D_i$, then the output interval for $p_i(E_i)$ has length

$$
C_i=D_{i-1}+D_{i+1}.
$$

For $D_i>0$, the integral secant remainder satisfies

$$
|q_i|D_i\le C_i,\qquad
|h_i(t)|\,t(D_i-t)\le C_i.
$$

Thus C428's bound by $2D_i$ is available at a maximal-diameter phase, but not automatically at every phase. Moreover, the distinct polynomials $h_i$ have no cross-phase integer-value congruence. A complete proof of sharp-spectrum persistence would need an additional phase-coupling argument or an independently complete classification; reusing C428's one-support graph does not provide it. The precise lemma and derivation appear in [PROOF_SUPPLEMENT.md](PROOF_SUPPLEMENT.md), Section 3.

Support diameters can be arbitrarily unequal even for two monic quadratic positive-Jacobian factors. For every integer $M\ge1$, take

$$
p_0(t)=t^2+M,\qquad p_1(t)=t(t-M),\qquad a_0=a_1=1.
$$

Then the native word $W=H_1\circ H_0$ exchanges $(0,0)$ and $(M,0)$, while the two input supports are $E_0=\{0\}$ and $E_1=\{0,M\}$. This is a counterexample to silently identifying all phase supports/diameters, **not** a period-spectrum counterexample, a new period family or a paper increment. Its proof is four direct substitutions, not a numerical run.

One honest necessary condition also survives: if every phase polynomial restricts to an integral affine function on its own orbit input support, the entire native orbit is an orbit of an affine integral planar automorphism. Its native period lies in $\{1,2,3,4,6\}$ when $\prod_i a_i=1$, and in $\{1,2\}$ when $\prod_i a_i=-1$. Therefore any candidate exceptional composition period must involve a genuinely nonaffine phase restriction. This is elementary affine linear algebra, not a new admission.

## 4. Primary-source verification and limits

The primary Pezda record was opened in the browser. The original PDF was read through a read-only `curl` to `pdftotext` pipe without saving or modifying any PDF. Actual accessed portions: cover, definitions and Theorems 2.1–2.2 on printed pp.95–96, auxiliary statements beginning p.96, and selected later proof text including the end of Section 4. OCR defects in some formulas were not silently repaired into a purported independent verification of the whole proof. The theorem statement and ring/period definition are legible. This lane relies on the published theorem and proves its applicability; it does not claim to have reproved Pezda.

Targeted web queries were:

1. `"polynomial automorphisms" "integer" "periods" Pezda`
2. `"Hénon" "compositions" "integer" "periodic"`
3. `"polynomial automorphisms" "24" "period"`
4. `site:arxiv.org integral polynomial automorphisms cycles periods Z2`
5. `"integral polynomial automorphisms" "cycles"`
6. `"Hénon" "integer coefficients" "composition" periods`
7. `"Pezda" "automorphisms" cycles`

These did not identify a directly applicable sharper fixed-word integral spectrum theorem. Secondary aggregators and unrelated complex-dynamics results were not used as proof sources. A targeted arXiv web search was used as the source-discovery fallback; no arXiv client, paid API, external model or manuscript upload was used.

The open-problems collection's accessible primary Section 11 was also encountered in the targeted search, distinguishing rational coefficient/rational point questions from the present integral family. Its rational-period conjectures are not settled here. Neither a polynomial that merely takes integer values on $\mathbb Z$ nor a rational-coordinate cycle automatically satisfies Pezda's hypotheses; changing to those objects would change C2's coefficient/domain quantifiers.

## 5. Handoff and execution boundary

Reusable interfaces sent promptly to the coordinator: (i) Pezda's universal native planar bound, with exact hypotheses and primary locator; (ii) phase-labelled return conversion and phasewise secant coupling, as documented in the supplement. No computation is needed to decide the assigned bound/unboundedness alternative. A new census would not add an independent theorem and was not requested.

Files created: this report and one proof supplement, only in the assigned C2 lane. No old code/build runs, new mathematical census, old/shared-file changes, Git writes, evaluator writes, manuscript numbers, PDFs, live configuration changes or external LLM/API uploads. The proof-writing and Hénon batch skills enforce the distinction between the proved imported bound, proved auxiliary lemmas and the unproved stronger spectrum question. No Route-A arithmetic or target spectral grade is claimed; `NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.
