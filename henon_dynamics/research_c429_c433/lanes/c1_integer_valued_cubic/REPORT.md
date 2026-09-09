# C1 — full integer-valued cubic rational-period question

## Frozen question and stopping rule

For every $P\in\operatorname{Int}(\mathbb Z)$ of degree exactly three and each $\epsilon\in\{1,-1\}$, let

$$F_{P,\epsilon}(x,y)=(y,P(y)-\epsilon x),\qquad (x,y)\in\mathbb Q^2.$$

One tick is one application of this displayed map. The observable is the ordinary least period. Determine whether there is an absolute integer $N$ such that every rational periodic point of every map in this full coefficient class has least period at most $N$. A proof must give an explicit coefficient-independent bound; a disproof must give a proved family with unbounded least periods. A finite coefficient scan, an arbitrary restricted Newton subfamily, a parameter-dependent terminating algorithm, or a normalization failure does not close this question.

This is the frozen **C1-UB3** question. Neither the two signs nor auxiliary denominator claims are independent paper contracts. No claim is made that a family-level period list holds for every individual polynomial. Root owns admission.

## Current status

**NOT CURRENTLY JUSTIFIED.** The all-coefficient uniform bound is not proved or refuted. Denominator and normalization feasibility are now settled by the auxiliary [proof package](PROOF_PACKAGE.md): finite denominator control is available for every input, but universal transport of all rational periodic points into an integral-coefficient integer-point problem is false. No mathematical program, old certificate, census, or PDF build has been run in this lane.

## Immediate source subtraction

- C424, `papers/C424_integer_valued_quadratic/sections/1_introduction.tex`, `2_normalization.tex`, and `3_integrality.tex`, proves the degree-two conservative full $\operatorname{Int}(\mathbb Z)$ atlas by two rational affine normal forms. Its denominator and maximum-coordinate methods are imported mechanisms, not new here.
- C417, `continuation_c414_c418_round2/papers/C417_integral_cubic/sections/1_introduction.tex` and `3_global_secant.tex`, proves the monic integral conservative cubic classification, including rational-point integrality, at most three coordinate symbols per cycle, and the sharp eleven-point bound. That coefficient/sign branch is already owned.
- C428, `papers/C428_integer_period_spectrum/sections/01_theorem_sources.tex`, proves the family-union integer-period spectra for arbitrary-degree $\mathbb Z[t]$ maps with both signs. Its domain is $\mathbb Z^2$, not all rational points; its coefficient ring is not $\operatorname{Int}(\mathbb Z)$. The source explicitly explains that those distinctions are essential.
- GR5, `continuation_round5/arithmetic/PROOF_PACKAGE.md`, already classifies all affine regular-good-reduction models of one Hénon factor over number fields, including the leading-coefficient valuation condition. The squareclass/good-model discussion here does not supersede or extend that full classification. Our pointwise derivative-trace example addresses a proposed transport into any integral polynomial map at an integral point, without requiring the target model to retain degree on reduction.

All C424/C428 paths above are relative to `henon_dynamics/research_c424_c428/`; the C417 path is relative to `henon_dynamics/`.

## Feasibility checkpoint

Write uniquely $P(t)=A\binom t3+B\binom t2+Ct+D$, with $A,B,C,D\in\mathbb Z$ and $A\ne0$. A valuation maximum proves that every rational periodic coordinate belongs to $A^{-1}\mathbb Z$. The coefficient-dependent lattice does not itself give a uniform period bound.

Under a diagonal affine change $u=\lambda x+\mu$, the cubic leading coefficient $a=A/6$ changes to $a/\lambda^2$. Direct comparison of first components proves that **every** rational affine conjugacy between standard-form Hénon maps has this common-scale/common-translation shape. Thus its rational squareclass survives: unlike the quadratic case, finitely many fixed leading coefficients cannot represent the entire class by rational affine conjugacy. This is a method boundary, not a disproof of C1-UB3.

More decisively, for every integer $q\ge2$ and either sign,

$$P_{q,\epsilon}(t)=qt^3-t^2+(1+\epsilon)t\in\mathbb Z[t]$$

has the rational fixed point $z_q=(1/q,1/q)$ with derivative trace $1+\epsilon+1/q$. Trace is invariant under every conjugacy regular with invertible derivative at the fixed point, whereas an integral polynomial map at an integer point has integral derivative trace. Therefore **no such conjugacy can put this point in an integral target lattice**, even after a number-field extension. This does not say the original polynomial lacks integral coefficients; it already has them. It says that rational periodic points cannot all be moved into an integer-point problem while retaining integral target coefficients.

## Primary-source check

Local collisions were checked first. The following primary texts were actually accessed through web search/open on 2026-09-09; no external model received a manuscript or repository content.

| Primary source | Accessed portion and established content | Subtraction and boundary |
| --- | --- | --- |
| Kim, Krieger, Postolache, Szeto, *Hénon maps with many rational periodic points*, arXiv:2412.01668v2 | [Versioned abstract](https://arxiv.org/abs/2412.01668v2) and [full HTML, §§2.2, 4.1, 5–5.1](https://arxiv.org/html/2412.01668v2). Explicit integer-valued odd-degree family; local escape and integrality; growing-degree long cycles. | The cubic $s_3(t)=(t^3-7t)/6$ and escape method are source-owned. The proved growing-degree long-cycle theorem does not imply unbounded periods at fixed degree three. The shifted tables in §5.1 are identified there as experimental, not proofs. |
| Ingram, *Canonical heights for Hénon maps*, PLMS 108 (2014), 780–808 | [Primary preprint HTML](https://arxiv.org/html/1111.3609), introduction, Lemmas 2.1–2.2, and opening §3. [Published DOI](https://doi.org/10.1112/plms/pdt026). | General local escape, height context, and affine normalization are imported methods. Monic normalization there permits algebraic coordinate changes; it does not make every original rational cubic a monic integral map over $\mathbb Q$. Bounds involving bad places are not an absolute all-coefficient C1-UB3 bound. |
| Julia Xénelkis de Hénon, *Hénon maps: a list of open problems*, Arnold Math. J. 10 (2024), 585–620, §11 by P. Ingram | [Journal-hosted HTML](https://armj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html), §11 uniform boundedness discussion and Conjectures 2–4. | C1-UB3 is a restricted fixed-degree arithmetic boundedness question, not a solution to the general number-field conjecture. The determinant-negative rational quadratic conjecture is not our cubic question. |

The arXiv HTML display for the Kim et al. item carries an internal date different from the version record; the bibliographic identifier is explicitly the v2 record, rather than a claim of a newly published journal version. The displayed formulas, definitions and stated theorem ranges are what were used. Targeted Pezda primary-page fetches timed out/failed; this lane does not claim a fresh full-text Pezda verification. Its integer-domain boundary was checked directly in C428's actual statement. No exhaustive literature-priority certification is asserted.

## Reusable interfaces

| Interface | Exact output | Potential consumer and compatibility requirement |
| --- | --- | --- |
| Theorem F, Steps 1–3 | All rational periodic coordinates lie in $A^{-1}\mathbb Z$, with refined prime exponents and an explicit coefficient-dependent real box. | Rational-orbit search or congruence analysis may use this finite domain for a fixed input. It must retain the dependence on $A$ and must not apply an integral-coefficient theorem to the transformed rational polynomial. |
| Theorem F, Step 4 | All affine conjugacies between standard single-factor maps are common scalar/translation changes; cubic leading squareclass survives. | Good-model and composition lanes may use it only when source and target are both these standard single-factor forms. General affine-good-model statements remain GR5-owned. |
| Theorem O, Step 5 | A periodic multiplier characteristic polynomial must be integral if a regular conjugacy sends the orbit into an integral polynomial map at integral points; $P_{q,\epsilon}$ violates this at a fixed point. | B3/B4 or normalization proposals can use it to falsify an asserted integral image of the marked orbit. It does not prohibit integral coefficients in the original coordinates, where the marked point is nonintegral. |

The source-owned cubic $s_3$ has the exact ten-cycle

$$(0,2,-1,-1,2,0,-2,1,1,-2),$$

checked symbolically by its five polynomial values and ten distinct adjacent pairs in the supplement. It already invalidates an unchanged transfer of C428's positive-sign spectrum to integer-valued cubics. Scaling this known family gives rational ten-cycles with unbounded denominators; the period stays ten. This is an explicit separation witness, not a new all-coefficient spectrum or unbounded-period family.

## Exact remaining gap and recommendation

The missing step is a coefficient-independent restriction on primitive rational cyclic words satisfying the cubic recurrence, despite arbitrarily fine denominator lattices and unbounded leading squareclasses. C417/C428 require integral secant/divided-difference constraints unavailable after the necessary rational scaling. A replacement must recover an equally strong discrete restriction or produce genuine unbounded periods; it cannot merely enumerate the box in Theorem F.

**Recommendation: retain C1-UB3 as unresolved; retain the proved obstruction and denominator interface as auxiliary; do not admit a paper from this lane on present evidence.** The full question was not narrowed to a fixed leading Newton coefficient, a few coefficient tuples, or integer points. A normalization method was refuted, not the uniform boundedness claim. The elementary auxiliary package should not occupy a C429–C433 slot by itself.

Execution record: zero new mathematical executions, zero old certificate reruns, zero PDF builds, zero external LLM uploads, zero shared-file/Git/config/evaluator edits. Only this lane's two Markdown files were written. Final internal proof review, if desired, remains the coordinator's allocation; no independent-review status is claimed.
