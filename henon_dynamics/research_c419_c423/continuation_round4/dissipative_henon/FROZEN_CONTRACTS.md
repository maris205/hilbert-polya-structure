# Round 4: two bounded nonconservative arithmetic questions

Date: 2026-09-08 UTC. AI-generated candidate screen by the current internal
team. Write ownership is confined to this directory. This is not a paper
admission, formal evaluation, manuscript, or new C-number. No previous
mathematical program or accepted proof is reopened or rerun.

The inherited directory label `dissipative_henon` is not a determinant
claim: the forward maps below have Jacobian **2**, hence expand real area;
their inverses have Jacobian **1/2**. We retain the requested forward
native clock, not the inverse clock.

## Bounded comparison

| Candidate | Exact question | Primary risk before computation |
| --- | --- | --- |
| DH1: non-unit-Jacobian rational periods | For every integer $c$, classify every ordinary periodic point of $H_c(x,y)=(y,y^2+c-2x)$ on all $\mathbb Q^2$, with exact least periods and all exceptional parameters. | The object is not literally C412's determinant-one family, but nilpotent reduction modulo two may make the complete answer a short classical contraction application. |
| DH2: arithmetic size of a return ideal | For the fixed map $H_0$ and fixed nonperiodic integral point $P=(0,1)$, establish or refute the unconditional full-time limit $2^{-n}\log D_n\to0$ for the return gcd defined below. | A genuinely different arithmetic observable, but the general Hénon gcd-growth question is already stated in the literature; split-coordinate and conjecturally conditional theorems may not close even this non-split instance. |

These are the only two candidates selected. Replacing $2$ by another
Jacobian, moving to a degree table, or adding a third deep screen is not
authorized by this contract. No numerical census has been run or frozen.

## DH1 contract

**Map and parameters.**

$$
H_c(x,y)=(y,y^2+c-2x),\qquad c\in\mathbb Z.
$$

It is a polynomial automorphism over $\mathbb Q$, with inverse
$H_c^{-1}(x,y)=((x^2+c-y)/2,x)$. The inverse need not preserve
$\mathbb Z^2$; this does not change the domain of the requested orbit.

**Domain, clock, observable.** All $\mathbb Q^2$; one forward application
of $H_c$ is one time unit; determine the complete periodic locus and
the ordinary least period of every point. Cyclic rotation identifies
the same orbit; reversal is not silently quotiented.

**Classical inputs and nearest owners.** Monic-integral local escape,
finite-field reduction, and unique lifting at a strictly contracting
cycle are classical. The actually read C412 theorem has determinant
$+1$, not $2$. C109 supplies only low-period witnesses for one
determinant-$1/2$ map. Ingram's detailed quadratic period conjecture
has determinant $-1$. The accessed Hutz articles concern one-variable
quadratics or everywhere-defined projective morphisms. None is to be
misquoted as this all-$c$ classification.

**Success.** A proved necessary-and-sufficient parameter/orbit list,
with no height, parameter, or period cutoff, and a substantial
independent increment remaining after the classical inputs are deducted.
Mathematical closure alone does not satisfy the latter admission gate.

**First cheap falsifier / proof test.** Test by hand whether minimal
non-Archimedean valuation forces integrality and whether $H_c^2$
improves congruence precision on a shared parity class. If both hold,
periodic points inject into the periodic residue states and only short
period equations remain. This exact local mechanism, not a coefficient
census, decides whether the candidate is too short for a paper slot.

**Stop.** Stop as a candidate if an exact primary theorem already owns
the classification, if the remaining proof is only this classical
short application, or if no complete all-parameter mechanism exists.
Preserve a correct full short proof when useful; do not enlarge it into
a claimed new substantial theorem by adding counts or zeta notation.

## DH2 contract

**Object.** The same fixed forward polynomial automorphism
$H_0(x,y)=(y,y^2-2x)$, but the fixed initial point $P=(0,1)$ is
nonperiodic and the observable is a return ideal, not periodic states.
Write

$$
H_0^n(P)=(u_n,u_{n+1}),\qquad u_0=0,\quad u_1=1,\quad
u_{n+2}=u_{n+1}^2-2u_n,
$$

and for every $n\ge1$ set

$$
D_n=\gcd\bigl(|u_n|,|u_{n+1}-1|\bigr)>0.
$$

This is the positive return gcd over $\mathbb Z$; for this orbit it
also gives the odd return ideal away from the bad prime two. The
positivity, nonperiodicity, and treatment of that prime must be justified
in any delivered argument, not assumed from numerical escape.

**Domain and clock.** This exact integer orbit at all ordinary forward
times $n\ge1$. No averaging over parameters, prime fields, or selected
subsequences. No multiplication of the iteration clock.

**Full question.** Prove or disprove, unconditionally,

$$
\lim_{n\to\infty}2^{-n}\log D_n=0.
$$

**Classical deduction.** The return-ideal divisibility property, the
fact that each odd prime eventually divides a return term, and the
trivial estimate $\log D_n=O(2^n)$ are not the proposed increment.
Section 11, Question 47, of the 2024 Hénon problem list already asks
for circumstances in which the analogous subexponential gcd bound
holds. Existing bounds for multiplicatively independent powers or
split one-dimensional polynomial orbits cannot be applied to this
coupled Hénon orbit without verifying their hypotheses.

**Success.** A complete uniform-in-time proof or rigorous asymptotic
counterexample for this fixed non-split instance, with the increment
separated from the general question's authorship. Merely conditional
on Vojta's conjecture is not the frozen unconditional success.

**First cheap falsifier / proof test.** Read the original gcd-height
theorems and recent work: decide whether this exact map, diagonal
target, and orbit satisfy an available unconditional theorem. If not,
identify a concrete missing non-split gcd-height lemma. No finite
prefix can decide this limit and therefore no gcd prefix computation
is authorized as evidence for it.

**Stop.** Stop if already contained in an unconditional original theorem,
if the remaining statement is classical reconstruction, or if the
required non-split arithmetic estimate remains unproved with no bounded
closure mechanism. Do not replace the limit by a weak $O(2^n)$ bound,
a liminf, density-one statement, conditional result, or selected examples.

## Method and scope

The main scout has read this turn's applicable `research-lit`,
`idea-creator`, repository batch skill/workflow, and relevant repository
instructions/current state. ARS is used only for inline, bounded
source verification with its selected workflow and required references;
not a full, Socratic, or externally reviewed pipeline. `proof-writer`
governs any actual proof and blockage document.

Current-team work replaces historical paid-model/GPU examples. No GPU,
paid API, external model upload, Git operation, global state edit,
new evaluator, or manuscript is part of this lane. No currently frozen
mathematical execution is needed; any later genuinely informative exact
test would require its own explicit finite pre-execution freeze.

Source arithmetic and local contraction do not establish target Euler
factors, root numbers, automorphy, target zeros, or a Hilbert–Pólya
realization. `NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.
