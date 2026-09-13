# Combined candidate brief: exact directional degree series

Date: 2026-09-05. Candidate `coefficient_cancellation_directional_degree_v1`.
This is a bounded content outline for the still-open Paper29 selection
gate, not a manuscript, project, scientific/publication lock or PASS.
It introduces no additional mathematical claims and does not modify the
three author proofs. Batch07 remains 2/5 accepted.

## 1. One technical question, not four independent headlines

For the single fixed-support family
$$
V(x,y)=x^4/4+x^2y,\qquad W_\delta(p,z)=p^3/3+\delta z^7/7,
\qquad \delta\in\mathbb C^*,
$$
determine the ordinary total degrees of every positive and negative iterate
in the displayed affine coordinates, including every coefficient
cancellation and its subsequent recovery.

Working title: **Coefficient cancellation and exact directional degree
series for a polynomial symplectic family**.

One-sentence contribution: a nonzero error layer closes an exact
cancellation/restart induction for this two-gradient-shear family, giving
its all-parameter forward and backward degree series and real resonance
parameters with arbitrarily many strictly expanding subdominant modes.

The mathematical payoff is an explicit solvable test family in which
leading-rate information misses an unbounded collection of growing
lower-order recurrence modes. This is a restricted structural example,
not a new general degree-growth theory, intrinsic conjugacy invariant,
or solution of an open dynamical-degree conjecture.

## 2. Inputs and claim-to-proof map

The author inputs are:

- [Forward proof](PAPER29_BOUNDARY_VIABILITY_20260905.md), SHA256
  `98e0046e80fb9ab971a5d6fe5ba8ba5f1c771c5fdc2875ed5ed8a2a23fdd8bd6`.
- [Complex parameter proof V2](PAPER29_CANCELLATION_PARAMETER_PROOF_V2_20260905.md),
  SHA256 `d571c60b88d16f45f7630449a47bb416a7e3d00f7ebb6e105f54c8deb5034d5e`.
- [Inverse and real proof V1](PAPER29_CANCELLATION_INVERSE_REAL_PROOF_V1_20260905.md),
  SHA256 `cf37a355038239be7b86f0914eb7aa6dea3cbdef8198456cf4abf2b24d6c65ef`.

The map is $F_\delta(x,y,p,z)=(X,Y,P,Z)$, with
$$
P=p+x^3+2xy,\quad Z=z+x^2,\quad X=x+P^2,\quad Y=y+\delta Z^6.
$$
For a nonzero parameter $\epsilon$, let $m(\epsilon)$ be the first hit
of $-1/2$ by $r_0=0$, $r_{j+1}=\epsilon/(1+2r_j)^4$, or infinity
when there is no hit. Set $L(\epsilon)=m(\epsilon)+2$ in the finite case.

| Claim block | Exact evidence | Logical role |
| --- | --- | --- |
| Forward series for every $\delta$ | Forward proof §§1–7 | Core error-layer induction and its scalar output |
| Existence of every complex first-hit time, and multiplicity-weighted counts | Parameter V2 §§1–5 | Completes the parameter quantifier; not a new general critical-orbit method |
| Backward series for every $\delta$ | Inverse/real V1 §§1–4 | New actual seed and output observable using the same induction; not a second method |
| Canonical real branch for every hit time | Inverse/real V1 §§5–6 | Real realization and directional corollary; not all-real-root classification |
| Minimal recurrence and strictly growing residual | Forward §§6–7 and inverse §4 | Consequences of explicit series and pole noncancellation, not independent headline theorems |

In the finite-hit case the respective series are
$$
D^+_\delta(t)=\frac{1+6t-40t^{L(\delta)}}
 {(1-6t)(1-16t^{L(\delta)})},\qquad
D^-_\delta(t)=\frac{1+2t-24t^{L(-\delta)}}
 {(1-6t)(1-16t^{L(-\delta)})}.
$$
In a no-hit direction they are $(1+6t)/(1-6t)$ and
$(1+2t)/(1-6t)$ respectively. All true degree sequences start at $d_0=1$.
In a resonant direction every pole survives, so the minimal eventual
characteristic polynomial is $(T-6)(T^L-16)$; otherwise its order is one.
The first dynamical degree is six in both directions for every parameter.

The canonical real parameters are $\delta_m=-a_m/2$, where
$a_m\downarrow4^4/5^5$ and $1-a_m/u^4$ first sends the orbit of $1$
to zero at time $m$, with all preceding iterates positive. They give orders
$(m+3,1)$ in the two directions, with the reversed pair at $-\delta_m$.

## 3. The actual proof mass and its organization

The intended manuscript would be English, anonymous, single-column
mathematics. The scientific body must satisfy the existing 22–30 page
requirement through substantive exposition, not forced page breaks,
inflated display spacing, enlarged margins, duplicated proofs or background
tutorials. No venue-specific template is selected here.

The following is an **author-side working allocation of 22.5 pages**, not
an observed page count or certification that 22.5 pages are needed. A
reviewer should reduce any allocation that overstates the natural content.
If the compact, complete treatment cannot credibly reach 22 substantive
pages, this candidate must fail the long-paper gate despite valid proofs.

| Section | Working pages | Substantive content and reason for inclusion |
| --- | ---: | --- |
| 1. Question, main result preview, and closest comparisons | 2.5 | State the map and the exact effect being computed immediately. Compare boundary-orbit methods, polynomial plane results and subdominant complexity by assumptions, with explicit novelty deductions. No general Hamiltonian tutorial. |
| 2. Precise degree conventions and theorem package | 1.5 | Distinguish ordinary versus weighted degree, all-indices versus eventual recurrence, and actual phase space versus the auxiliary ratio orbit. State the forward/backward and parameter results once; give the proof dependency order. |
| 3. The nonzero error layer and the three-step restart | 5.0 | Prove the initial layer $\delta x^{10}(6z-8y)$, the normal step with every competing term type bounded, and the three distinct critical steps. Establish the regenerated layer and closure $s\mapsto16s$. This is the central proof, not max-plus experimentation. |
| 4. Forward visibility, pulses, and the exact denominator | 2.0 | Prove that the visible map degree is always the $y$ degree; derive the pulse positions including $n=0,1$, sum them, prove noncancellation, and identify the growing residual. One complete $L=3$ example only. |
| 5. Complex critical parameters with multiplicities | 3.5 | Reduced iterate fractions, alternating numerator degrees, exact return indices, holomorphic local return and preservation of multiplicity, divisor inversion and strict existence inequality. Do not count roots as distinct or claim transversality. |
| 6. Actual inverse seed and backward degree series | 3.0 | Check the two signs and phase order; calculate the two seeded steps, unique degree184 layer and final-shear observable; derive inverse pulses and minimum order. Refer to Section3 rather than reprove its lemmas. |
| 7. The positive real branch and directional realization | 2.0 | Define the positive-orbit parameter intervals, prove monotonicity and first zero existence/uniqueness there, prove the parabolic-threshold limit, and deduce the sign-exchanged degree orders. Do not classify other real branches. |
| 8. Exact controls and the boundary of the conclusion | 2.5 | Give the elementary complex control and the real elliptic-clock variant in concise proofs, including the inverse degree; explain bounded periodic residual versus the candidate's growing residual. State the surface spectral comparison with its restrictive hypotheses. |
| 9. Conclusion and remaining mathematical questions | 0.5 | Record exactly what has been computed; separate unresolved conjugacy, simultaneous complex hit pairs, higher dynamical degrees and all-real-branch questions. These are not extra results or speculative sections. |
| Total body to conclusion end | 22.5 | References excluded; no appendix used to manufacture body pages. |

This allocation is deliberately close to the minimum and is vulnerable to
compression. The three proof files contain substantial displayed
calculations, but source-line or whitespace-word counts are not evidence of
body pages, especially because the forward proof is in Chinese. No LaTeX
draft or layout test is being represented as completed.

The sections belong to one chain: an actual error layer determines a return
law; this law determines both output degree sequences; scalar parameter
analysis determines which return laws occur. Complex counting and the
positive real branch answer different quantifiers. The inverse computation
cannot be skipped by appealing to polynomial conjugacy, but should not
repeat the shared induction. The controls prevent overclaiming rather than
serve as additional claimed discoveries.

## 4. Minimal illustration and citation plan

At most one compact original vector diagram is useful: a normal state,
critical state and three-step recovery, labeled with the exact $(a,s)$
updates, together with the differing forward/backward observation points.
It explains why the first visible drop is at $n=L$ in both directions even
though the observables differ. It is not a numerical orbit plot and adds
no scientific evidence. A small comparison table can replace multiple
repeated prose comparisons; neither item receives its own page allocation.

Use the verified primary citations in the
[base literature report](PAPER29_CANCELLATION_LITERATURE_20260905.md) and
the forthcoming directional supplement. The introduction needs Bedford–Kim,
Truong, Favre–Jonsson and Nguyen as direct boundaries, not a long history.
Blanc–van Santen and Xie distinguish leading-rate results from exact series;
Diller–Favre supports only its precise stable-surface spectral comparison.
Déserti and the directional Bedford–Kim example establish that asymmetry
itself is old. The independent elementary controls are derived here and
must not be falsely attributed to those papers. BibTeX metadata would be
verified from primary sources before any manuscript is written.

## 5. Mandatory novelty deductions and anti-claims

The candidate must **not** claim as an independent innovation:

- fixed dimension/support with unbounded eventual recurrence order;
- equal dominant growth rates with different forward/backward orders;
- existence of real examples of that asymmetry;
- critical-orbit equations as a new method of detecting degree losses;
- degree-series information beyond a first dynamical degree in general.

The elementary product/conjugacy controls already give the first three,
and the verified literature supplies the latter two. The remaining
comparison is the joint, exact all-parameter theorem for the specified
two-gradient family, with a genuine amplified nonzero error layer and
$L$ modes of modulus $16^{1/L}>1$. None of these sources or controls
establishes a universal conjugacy obstruction, and neither does this brief.

The results do not claim physical periodic orbits, integrability, entropy,
an arithmetic determinant, a spectral operator, higher dynamical degrees,
all-real-root classification, or a classification of simultaneous complex
forward/backward resonance pairs. A pure structure paper uses no fabricated
experiment package or Route A/B score.

## 6. Review question and process status

The unchanged conjunctive candidate gate is novelty at least7.5/10,
research value at least7.5/10, proof confidence at least9/10 and credible
22–30 substantive body pages. Judge the *combined exact theorem after all
deductions*, not the sum of scores for four weakened headlines. A correct
short theorem is not a passing long-paper candidate. No requested score,
presumption of PASS or permission to relax a threshold is supplied.

Two independent readers receive this same author brief and the literature
inputs without exchanging their assessments. Any existing check of
unchanged proofs remains usable; this brief asks for the unresolved
scientific-value/page assessment, not gratuitous rechecking. Candidate
acceptance would still not be publication or PDF acceptance.

The `paper-plan` claim/evidence and one-story guidance was used only for
this provisional content brief; the existing mathematical page requirement
overrides conference defaults. `research-review` uses available independent
agents because its prescribed GPT5.4 Codex-MCP endpoint is unavailable.
No cross-model review or manuscript build is claimed.
