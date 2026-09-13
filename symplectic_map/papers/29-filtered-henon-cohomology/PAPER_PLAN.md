# Paper plan: frozen natural-content structure

Title: Filtered polynomial cohomology and finite periodic tests for symplectic Hénon maps

One-sentence contribution: Ordinary-degree control turns polynomial Hénon
coboundaries into an exactly counted, degree-bounded problem detectable on one
effective periodic scheme, with a full fixed-field application to a symplectic lift.

Type: pure mathematics; local anonymous article, no designated conference.
Date: 2026-09-06. Exactly eight numbered sections, plus abstract and references.
The actual body must satisfy22–30 pages. There are no per-section page quotas:
the point of the authorized first draft is to measure natural content, not force
the earlier23- or22-page estimates. All proofs below were completed before drafting.

## Problem anchor

For the fixed characteristic-zero symplectic Hénon composition, characterize
polynomial additive coboundaries with their ordinary-degree filtration and prove
an effective exact test on a complete fixed-point scheme. Use the same equation
to classify rational invariants of the specified parameter-preserving symplectic lift.
Do not change the problem to pointwise/approximate Livšic, multiplier traces,
conjugacy invariants or optimal bit complexity.

## Claims-evidence matrix

Input abbreviations M, S, IM, IS refer to the two proof reports and their two
independent checks bound in notes/SOURCE_SCOPE_LOCK_20260906.md.

| Claim | Exact evidence | Manuscript |
| --- | --- | --- |
| C1: complete obstructions, rational reduction, degree-preserving primitives | M §§1–2,8.1–8.2; IM §8 | §§2–3 |
| C2: exact ordinary-filtered Hilbert series | M §§8.3–8.5; scalar simplification only from general formula | §4 |
| C3: finite scheme iff, exact support cost, effective/sharp stable thresholds | M §§3–7; IM §§3–5 | §§2,5–6 |
| C4: scalar R(x) rigidity and complete lift fixed field | S §§2,8–9; IS §7.2 leading coefficient ratio | §§7–8 |

## Abstract

About180–230 natural words. State the exact coefficient-uniform algebraic answer,
the no-degree-loss primitive, the Hilbert description, logarithmic scheme period
and the exact scope of sharpness. End with the fixed-field application. No citations,
review scores, research-process prose or unsupported priority assertion.

## 1. Introduction

File: paper/sections/1_introduction.tex. Set up the equation and the four questions
of solvability, primitive degree, obstacle count and finite periodic data.
Define the map/filtration and preview principal theorems in readable exact form.
Explain that a whole scheme, not one orbit or an average, is measured.
Position Bousch, finite approximate Livšic and additive-extension criteria in
compact methodological paragraphs, not a separate history chapter.
Use citations Bousch1992HenonAlgebras, PollicottSharp2004FiniteLivsic,
GouezelLefeuvre2021FiniteLivsic, Schneider2016DifferenceRings and
CerveauDeserti2018Contact where their actual content is discussed.
No repeated full theorem statements later purely for length: the introduction
can state concise main consequences and refer to exact body theorems.

## 2. Orbit algebras and the Hénon composition

File: paper/sections/2_orbit_algebras.tex. Define phase-periodic p_i,d_i,
orbit coordinates X_i and F*. Give one terminating, confluent pure-power
rewrite argument, including infinite finite-support input and the common-multiple
ambiguity. Identify the quotient with actual K[x,y] by two inverse maps.
Identify F* with shift-k. The same reduction gives the finite-cycle basis;
give the separate exact fixed-scheme identification and length delta^n.
Credit Bousch before the construction. Only N=kn>=3 is claimed for the cycle model.
Suggested labels: thm:orbit-basis, prop:macro-shift, prop:periodic-algebra.

## 3. The ordinary-degree filtration and bounded primitives

File: paper/sections/3_filtered_primitives.tex. Define the phase-product weights.
Prove highest monomials and mixed-radix bijection to(A,B), hence exact degree of
linear combinations. Compute the vector-space coinvariants by infinite basis
orbits and construct the finite cumulative primitive. Prove macro-step discrete
convexity including its two middle second differences; deduce no degree loss.
Scalar y^D attains the uniform bound. Prove once the absence of polynomial
semi-invariants/periodic affine curves and the rational-to-polynomial reduction,
using IM §8 rather than a second scalar reversal proof.
Labels: lem:degree-basis, thm:orbit-obstructions, thm:bounded-primitive,
cor:rational-reduction. Delta denotes the degree product, not the difference map.

## 4. Exact dimensions of the filtered obstruction space

File: paper/sections/4_hilbert_series.tex. Define H_D and W_D; use the previous
strictness to show dim H_D=binomial(D+2,2)-dim W_D+1. Define the exact digit
re-encoding rho with both explicit sums and explain its direction. Count
max(mu,mu') in A=Q,A>Q,Q>A; prove the general formula. Derive the scalar closed
form and leading cumulative coefficient. One(2,2)versus(4) comparison suffices.
Do not repeat the independent scalar triple-count proof. State that this is
coordinate-filtered vector-space information, not a conjugacy invariant.
Labels: thm:hilbert, cor:scalar-hilbert, ex:same-degree.

## 5. Detection on one complete periodic scheme

File: paper/sections/5_periodic_detection.tex. Define individual word diameter.
Prove the unique large cyclic gap, lifting modulo N and preservation of macro
phase. Prove full cycle orbit length n. Compare disjoint orbit-norm supports
and the constant term n c_0 to prove the scheme iff, including rational equivalence.
Explain precisely scheme equality versus geometric values. The period-one
dual-number example may occupy a brief remark and is not a long-period
counterexample. Do not repeat the finite-cycle normal-form proof.
Labels: lem:no-alias, thm:periodic-test, rem:scheme-values.

## 6. Effective periods and sharp boundary phenomena

File: paper/sections/6_effective_periods.tex. Define the exact L_ph(D) endpoint
cost; prove its upper bound and attainability. Derive the scalar balanced-distance
formula and general uniform estimates, then n_eff and delta^4 D^4. Present
degree-scale g_r and its exact highest terms; define the eventual-uniform
threshold quantifier explicitly before claiming leading-4 sharpness.
Treat scalar binary N=2L stable multiplicity and N=2L-1 counterexample with
L>=2,N>=3; give the k=2,N=6 macro-phase failure. Briefly compare the
O(D^2)unknowns direct linear method without declaring runtime optimality.
Omit the abandoned linear-span argument and duplicate coarse-bound derivations.
Labels: prop:exact-span, prop:scalar-span, thm:effective-period,
thm:sharp-threshold, prop:binary-boundary, ex:phase-alias.

## 7. Rigidity for a univariate right-hand side

File: paper/sections/7_univariate_rigidity.tex. Work with one H_p; invoke
cor:rational-reduction. Define the exchange involution iota and reflection r,
Q=y^2-p(x)y and the invariant ring K[x,Q]. Only the invariant highest-term cone
needed for f_y is proved, not the unused anti-invariant ring/no-curve detour.
Use the exchange anti-symmetry of f and of f_xy to force f_y constant.
Give the exact classification and concise degree/characteristic/Jacobian limits.
Label: thm:univariate. Do not claim this specific form for a multiphase composition.

## 8. Rational invariants of a parameter-preserving symplectic lift

File: paper/sections/8_symplectic_lift.tex. Verify the stated kick-drift map is
symplectic; pass to K=C(a),x=t,y=t-s. Give a short self-contained known
additive-extension criterion, retaining the ratio of leading coefficients.
Apply thm:univariate to V_a; obtain the entire fixed field, then compare the
highest two t coefficients to prove the exact polynomial translation exception.
Verify the global polynomial symplectic coordinate change. Explain why the
two extra generators are not a rational Liouville pair. One paragraph of
ordinary/translation/pure-parameter-potential examples suffices. Finish with
a short conclusion and the exact unproved geometric-point boundary.
Labels: lem:additive-extension, thm:lift-field, prop:translation-exception,
cor:no-liouville-pair.

## Citations, figures and validation

Only the five necessary verified entries listed in §1 are initially planned.
BHN is omitted because this article need not survey Hénon-like measurable regularity.
No numerical table or figure is required; formulas and one small algebraic
comparison carry the exact distinctions. No external figure dependency exists.
The first build must be based on the complete source after a faithful-transcription
check, not successive page-targeted drafts. Independent source/PDF review covers
the actual new exposition and remaining capacity risk, not unchanged old stages.

## Independent plan review

Pending a bounded independent check of this new dossier/structure and its fidelity
to the already proved scope. No new research review or page-estimate re-vote is
requested. After that check, freeze the accepted plan version and begin section writing.
